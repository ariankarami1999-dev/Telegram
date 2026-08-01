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
<img src="https://cdn4.telesco.pe/file/groI5xTpwv63gfZoi6J4nCDzOlcRYiL7alhPvmfSys8QS9iuFLn3N4KNX-dCNvym4v7j0bdQxS-ogrXW9QKkfhpqlFGC3LOOBlCFSi8DRxzRuhYuE12uKp8IWm5Q8oYnn5Dd6VABPOEdQ4RbRomkd5R03bDxF0BH2YU7It7nbLOcUU9Cvz57HF-l9sqznIzP27GAnZa4Wd98L-up_IT86s7Q0swHckr9_HxE5knU8gqfbWkSkbl1uv0dmCtMAmd5XZjW_L0lexBSNtKYIUgxAC_TWi6gkWzI0GZNdqQS4Ab_2Urlor3LYszHLvS5KhYuyEDAEpu4KLX0Q9TxtVkY0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 139K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 11:35:11</div>
<hr>

<div class="tg-post" id="msg-69348">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=HvV3YPFF7C6rwQGKWV4ObuAD7ud5WcupWaPsDbqs3SjP2tBNAvDPDRfwhcPjynGQihsBv8KxBFryOwB4vYwZuGPQLNJu0K9pFpmU4wzLvptweJv4vmXLqdJ7-BE0__OPvrsDhdGukdLp0NIraXAcE7uCT-vKTJiC9LyXT0_TLbi1PQ4q26v77CdUfJp_920rJrtJRPRVMQzpCs_vcSFMLsbwPbCWukmDz8rrf95xopbZESbqFodDD74hnPMsN9qE4pVKu0PEbe18-VQeuFVtVV3CeZug74Xb2Yk4DiAbBMjYWO5v8XdbKLuc59tPCrK5Cd9INFiDzOJtNvxpS-q0Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=HvV3YPFF7C6rwQGKWV4ObuAD7ud5WcupWaPsDbqs3SjP2tBNAvDPDRfwhcPjynGQihsBv8KxBFryOwB4vYwZuGPQLNJu0K9pFpmU4wzLvptweJv4vmXLqdJ7-BE0__OPvrsDhdGukdLp0NIraXAcE7uCT-vKTJiC9LyXT0_TLbi1PQ4q26v77CdUfJp_920rJrtJRPRVMQzpCs_vcSFMLsbwPbCWukmDz8rrf95xopbZESbqFodDD74hnPMsN9qE4pVKu0PEbe18-VQeuFVtVV3CeZug74Xb2Yk4DiAbBMjYWO5v8XdbKLuc59tPCrK5Cd9INFiDzOJtNvxpS-q0Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
آمریکا و اسرائیل برای شدیدترین بمباران در روزهای شنبه و یکشنبه آماده شدن و ترامپ دستور حمله رو صادر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/news_hut/69348" target="_blank">📅 11:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69347">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqjS9yyQR9WE0qztcvrY3fG5xPdGFwIUVGAANHNz65sgGdvRNATLdVAJA5ShnfNgiMFZi5Wi-HT3N5h3fBQDrIFTz3m_TfZGySu3tHqqUN2DNh-_bYZEJG-5z20pj-Cd18YeVplF_um7JgmhBWEautwP4vlR5j5kXvhTGJJNLdn0F8ewMkD7ilpfWaspZPAU7JC9JsHXm4mponQ_q7l8q-SWGLKguymrlTmWSRfYyeZ2SSKkDeuIKZmQpa1BgCbIvQxWcLL7wvfmP_m9yhoFVDPuXNNUhzrd0f-E2VXOzoEhQ2LcAcansFzU7pnQlXjM_JdSvErfus1AvLc2vL8cYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دقایقی قبل یک کشتی در نزدیکی خصب عمان مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/news_hut/69347" target="_blank">📅 10:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69344">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=g0zP31UQ5gOpszwG4vWI175WMdQlfHxa08PCHGtRpn1sK9nA31W4h4BYZhrTXLaasBwAqjsx2ktdAEichwPDA3TJrdJKsQyzh5Njn_rqIwKRPh9rjHlEYPDSeSbYw-WZNHY1uhDoPQDq_fdCC3DlOgfZMuYVw3sFt2dRj7ozCa74PF-qLqVBCRRd9smcVA-mYDF5UMGkGxS7LTyTQyAfdvz5KvWmog5q6Z2NQQ66hlTAmrojBMARFtmcVQlWdyHXu5aeARz5zBpTX2Zpn3e6KvJJMhyiGTaN65D5QyTrDSpsv-DBwtTTC3j0fAVNNvyX6nIGxB0-NitkzhwGA9YrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=g0zP31UQ5gOpszwG4vWI175WMdQlfHxa08PCHGtRpn1sK9nA31W4h4BYZhrTXLaasBwAqjsx2ktdAEichwPDA3TJrdJKsQyzh5Njn_rqIwKRPh9rjHlEYPDSeSbYw-WZNHY1uhDoPQDq_fdCC3DlOgfZMuYVw3sFt2dRj7ozCa74PF-qLqVBCRRd9smcVA-mYDF5UMGkGxS7LTyTQyAfdvz5KvWmog5q6Z2NQQ66hlTAmrojBMARFtmcVQlWdyHXu5aeARz5zBpTX2Zpn3e6KvJJMhyiGTaN65D5QyTrDSpsv-DBwtTTC3j0fAVNNvyX6nIGxB0-NitkzhwGA9YrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
بروزرسانی از اسپانیا:
نزدیک ۵۰ هزار نفر از مراکش و الجزایر فرار کردن و غیرقانونی ریختن اسپانیا!
برای کنترل این مهاجرای غیرقانونی پلیس فرستادن که پلیس هم کتک زدن.
این مهاجرا ریختن توی فروشگاه‌ها دارن غارت میکنن، از مردم دزدی میکنن و...
مثلا از یه مراکشی رندوم میپرسن چرا اومدی؟ میگه توی مراکش رفیقمو به قتل رسوندم، مردم هم باهام بد رفتار میکردن، منم فرار کردم اومدم اسپانیا.
@News_Hut</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/news_hut/69344" target="_blank">📅 10:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69343">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=rIZM4F3uqhhyg0Y5hNunnUBHQNEKDvEoRvaBLpXo8RFy6k5RAEcRvVDaxvawEPcHUqhQQge2afxcJ0dDCM_87mmZ5bGNSaqFb18aPbMq13_TiyrHMtbSSPcDvoOJ8V_euAKhQL3ocNMel6QM8zHt6-pRH4ol6hhEqrghzL6AWtnUAALo8vzbQ7kejgFiH9jeC4tkzq9vNta91A2UVownMOZxVMSbkCzbx8WPrDnzvkF9tf8qWYslgm0gKgOID5Af10AKvVTLX19m3Jd5HWgwZRJJGZdgk4CHq1PfenVUCgapx458MHXRbfyDkLL7pOvq4dFN2OY1Yb4TIpIJuNLrBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=rIZM4F3uqhhyg0Y5hNunnUBHQNEKDvEoRvaBLpXo8RFy6k5RAEcRvVDaxvawEPcHUqhQQge2afxcJ0dDCM_87mmZ5bGNSaqFb18aPbMq13_TiyrHMtbSSPcDvoOJ8V_euAKhQL3ocNMel6QM8zHt6-pRH4ol6hhEqrghzL6AWtnUAALo8vzbQ7kejgFiH9jeC4tkzq9vNta91A2UVownMOZxVMSbkCzbx8WPrDnzvkF9tf8qWYslgm0gKgOID5Af10AKvVTLX19m3Jd5HWgwZRJJGZdgk4CHq1PfenVUCgapx458MHXRbfyDkLL7pOvq4dFN2OY1Yb4TIpIJuNLrBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
صحبت‌های عادل فردوسی‌پور درباره ماجرای دست‌بوسی عباس صالحی :
تو عُمرم دستِ مسئولی رو نبوسیدم!
عباس صالحی وارد مسجد شد و کاملاً اتفاقی روی صندلی کنار من نشست. به شوخی بهش گفتم اگه یه روزی فیلتر 360 برداشته بشه، همه این نشستن شما کنار من رو ربط میدن به رفع فیلتر!
همون موقع که داشتیم دست می‌دادیم و روی صندلی جا‌به‌جا می‌شدیم، شب دیدم یه ویدیو وایرال شده و با یه تیتر زشت نوشتن که من دست عباس صالحی رو بوسیدم.
اگه قرار بود دست‌بوس باشم که الان برنامه 90 رو داشتم و 360 رو هم فیلتر نمی‌کردن.
چطور ممکنه من برم تو اون مسجد، بین اون همه آدم، بیام دست عباس صالحی رو ببوسم و برای خودم حاشیه درست کنم؟
من همین چند روز پیش هم گفتم؛ بله‌قربان‌گو نبودم، نیستم و نخواهم بود!
همیشه روی اصول خودم ایستادم و سعی کردم کنار مردم باشم. واقعاً این حجم از هجمه‌ای که به من وارد میشه حیرت‌آوره.
من عاشق کارمم و اینو خودشون هم می‌دونن، ولی نه به هر قیمتی. اگه شرایطش فراهم باشه، تو فوتبال 360 به کارم ادامه میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/69343" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69342">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=HGvuXuXclK7XGX2a2Y6f3VzzXdurC3ap0yFIxmYeKUgphfJm9v50NPCGAEVbuSbwQGV1ghKymfXHXgvbnTbPLyEcKGf4w4EHcOioHew604Mthvc_m3SIScWWpiM4460dJKrQFGgcRthSuRo0ofZgz9-BixGPXd9T7wIIxLCsytGu3QGsDpapWKYgXBUXw6-DNuDP-eySANJMx4Fl8Hz5uMhN-avbRbqHrTdVRZsajShH2EOk2Oq0Pc3tVr-9Ql_pU5H_Vq5Rm7zBfa6o2op5VdcvLQlj5l45LtZrY0q08kP3idlDt0OlbN3C1fRBVW5Tl1Hmp5lmYy3D5so3u9lX9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=HGvuXuXclK7XGX2a2Y6f3VzzXdurC3ap0yFIxmYeKUgphfJm9v50NPCGAEVbuSbwQGV1ghKymfXHXgvbnTbPLyEcKGf4w4EHcOioHew604Mthvc_m3SIScWWpiM4460dJKrQFGgcRthSuRo0ofZgz9-BixGPXd9T7wIIxLCsytGu3QGsDpapWKYgXBUXw6-DNuDP-eySANJMx4Fl8Hz5uMhN-avbRbqHrTdVRZsajShH2EOk2Oq0Pc3tVr-9Ql_pU5H_Vq5Rm7zBfa6o2op5VdcvLQlj5l45LtZrY0q08kP3idlDt0OlbN3C1fRBVW5Tl1Hmp5lmYy3D5so3u9lX9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سیدمحمود نبویان، نماینده مردم تهران، درباره شاهنشاه آریامهر؛
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/69342" target="_blank">📅 09:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69341">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69341" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69340">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ubIFrIVmfrTWHnuCtbRzu9qoW7Z-60em047zEXd40AcIRseJ5178qUKDUbLuEsoQu4v4e1C1EGV0rV9aXC2UNR64NuWSAGkWJun1LEXmDPE5JDqSQrZD2yY0Qx7Zqfh5ktVWg2TV0pJJbZVUe5ujp6XAcfy-jQPw3XjSwvEHway5b0XoA12PgJLTnQNL1LlzKNkyffKgatA12xmYiAjsk8e-QHrYmeMJOZtJoNYcTz20rRvxdXr37MQidt3rO8TTw3tbW2sAodSCUnfOmGNPgBjrK8mY0iGB55CRTqYBp2rRparGohcKAI7pQEf2Tme6XaFOcN231ukuodXk5v_bKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ubIFrIVmfrTWHnuCtbRzu9qoW7Z-60em047zEXd40AcIRseJ5178qUKDUbLuEsoQu4v4e1C1EGV0rV9aXC2UNR64NuWSAGkWJun1LEXmDPE5JDqSQrZD2yY0Qx7Zqfh5ktVWg2TV0pJJbZVUe5ujp6XAcfy-jQPw3XjSwvEHway5b0XoA12PgJLTnQNL1LlzKNkyffKgatA12xmYiAjsk8e-QHrYmeMJOZtJoNYcTz20rRvxdXr37MQidt3rO8TTw3tbW2sAodSCUnfOmGNPgBjrK8mY0iGB55CRTqYBp2rRparGohcKAI7pQEf2Tme6XaFOcN231ukuodXk5v_bKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69340" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69339">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس لیست اهداف انرژی منطقه رو منتشر کرد:مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی؛
❌
میدان نفتی غوار در عربستان
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
❌
تأسیسات ابقیق و خریص عربستان
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
❌
پالایشگاه الرویس و میدان نفتی زاکوم در امارت
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
❌
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
❌
میدان نفتی برقان کویت
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
❌
پالایشگاه ستره و تأسیسات المعامیر بحرین
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
❌
میدان‌های گازی لویاتان و تامار اسرائیل
ویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69339" target="_blank">📅 02:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69338">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWQ29HRBg2z_Mw4KjL5ZfryP8yLHViGyhftSRAaouPLohKcXCmw2kYOIh-BsWkOSihQEL8TIVQ06kQkEV3KEcS0ZGcRIYV1YtwyZAMcCpkjTPf0OrogLpeJMu9jukaibvjkl44zKehvEyiFdQpg5wARB1hz721fL3ZLhVlbH06iVY4qpLzcAkjT3gL0uAVj0hm8Yj3NkwKKpvGYp_En9OaXVnJA7_8nB51t-PBiiSoPzuJoBuUkyCFny1z9RbHmh_7jFz4QY_YshHgjTMGVebIR9jCFd893jUWlEGpqOXCPuwJQhk_6tz9DIs7BG-ETCduP23fGzagKSPstPLobh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:یه مقام ارشد امنیتی به ما‌گفته؛اگه آمریکا یا اسرائیل بخوان به زیرساخت‌های ایران حمله کنن؛
ایران از قبل یه برنامه گسترده برای جواب دادن آماده کرده.
به گفته این مقام، توی این برنامه، زیرساخت‌های حیاتی اسرائیل و تأسیسات انرژی آمریکا تو منطقه هم جزو اهداف در نظر گرفته شدن.
نیروهای مسلح ایران توی جنگ 40 روزه و اتفاقات هفته‌های اخیر نشون دادن هم توان انجام چنین عملیاتی رو دارن و هم برای انجامش اراده لازم رو.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69338" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69337">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7lHQXPE7qKFL0HhEJRxcvfFziZckvIFNzPAgfmoiej3hdAatRjjD4TSqyz2U76QudfbRnIGTbVFNhYbktPVob4TutvcBed0TvocL6P_DxXv1bt3vFBB790PineDaVkuhwEtxp5kkf7tNjKPYOP91SavAr3StiEVAbS6Ik0YJT5VgItc93cIIT9lpaLLR9fXXxpd05VcQs6jJLuH7tC_8L44_kMFn12cyHDCI0jV3FEYUutlWdC-k9RcQigvglytQdQIZLdi23di2FY9hwClmVj3iFm8MPoDFo5jjNPDWPfD292LhYNyTBHEEoqOv6hQDYojZwtPJgyl5nf5eHsNsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛آکسیوس:ترامپ در حال بررسی حمله به تأسیسات انرژی ایران ظرف چند روز آینده است.
یک مقام آمریکایی روز جمعه به «اکسیوس» گفت که رئیس‌جمهور ترامپ به‌طور جدی در حال بررسی انجام حملاتی علیه تأسیسات انرژی ایران در چند روز آینده است، اما هنوز دستور نهایی برای اجرای آن را صادر نکرده است.
این حملات همچنین ممکن است برای نخستین بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدید تنشی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین بار درباره حملات احتمالی گزارش دادند.
ترامپ در آغاز جلسه روز جمعه کابینه، با اشاره به حمله احتمالی گفت: «خب، ما ضربات بسیار سختی به آن‌ها وارد خواهیم کرد و می‌دانید، بالاخره زمانی فرا می‌رسد که آن‌ها خواهند گفت دیگر تاب و تحملش را نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69337" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69336">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh6iPzDhPdwlduq07g7itP38E8Ac_7vc7XMh7-VLJrcqiZOdNzAD_li_JdygVvKTDTFkBzYvqI8ao4HLIcH9h3ZxF0aH5uU5SASFnXVoVjOknPI3uGBAqApCMv0O0-t7Fa3O66337dY-0_DtBLPyPuArKVrbtA4zJsbmZ_nwTAXrXJAwsfzBBUKKRyRG7g8YeX5Gp_6tjF8JwuGJ0mGaUlPiCbWa3RwFFsFOAiW_r1BZQHUGW68K_Ip9FbQJDCOnbNZERnIzPAZN7Bro2-pGC4dlF-P4ckw2JSnqAiDouPuOe0HNhtY4uV5yiSPjjeWd3YvkP_IrzUUNU1g2B15Row.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
سی‌بی‌اس نیوز:
ایالات متحده و اسرائیل در حال آماده‌سازی یک کمپین بمباران مشترک بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده است، اما حملات ممکن است این آخر هفته آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69336" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5040574e14.mp4?token=SH7JVFr2wPhWBiSL2IQfVV0QOVFlg9bVaMA3Rid1L9f8izYpnvj-u8wZc98tUVixCnVU6bHFyjNFqbRC8QZoUIROG9Rk_4wyowVgkAaTbViLEdbW8H7Bj7BwYHgNz-VMWtZB9BzhhunKMBtkUFxVbPeEb7tUFZxKVh27ST2IuRrOvrdRYO3bQfuDTNI0IoFgDe_fgsUgwsyV7dWUa8LfJguo11dMIbdYJBThyl1PL1BG6zb9qjVgKWtpI4L2fORSsv2mWuq8je8j9m3W76BAXnMsaCgcZcFcYjoIJ9Dlpn3RvsC_URbzdzzk7eAq2xmdYdUHVRDA_N-er84E0pbAIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5040574e14.mp4?token=SH7JVFr2wPhWBiSL2IQfVV0QOVFlg9bVaMA3Rid1L9f8izYpnvj-u8wZc98tUVixCnVU6bHFyjNFqbRC8QZoUIROG9Rk_4wyowVgkAaTbViLEdbW8H7Bj7BwYHgNz-VMWtZB9BzhhunKMBtkUFxVbPeEb7tUFZxKVh27ST2IuRrOvrdRYO3bQfuDTNI0IoFgDe_fgsUgwsyV7dWUa8LfJguo11dMIbdYJBThyl1PL1BG6zb9qjVgKWtpI4L2fORSsv2mWuq8je8j9m3W76BAXnMsaCgcZcFcYjoIJ9Dlpn3RvsC_URbzdzzk7eAq2xmdYdUHVRDA_N-er84E0pbAIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مهاجر مراکشی درحال رفتن به منطقه برون‌بومی اسپانیایی «سئوتا»
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69335" target="_blank">📅 01:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69334">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.   مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69334" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69333">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQMQFNbbmuyn5It6LttqdteVTwTKCG-w26gU5jT7pNz3xIYNdC7BIVMybMleVphQpoo3sB4PAAwd3PENK30M5SQCELb6ys0g88mPY-iefrPW8fcTSXUus0K64j2qEYyn5dh9cvuRG4GDTGM_KsNfv2jA8Li9CaY5-3bD9VYTOPcBZUAvBbbYH14yBrnxpRnAPH-yQ02EfL5OPW3L_Nd9d_7lxkdBV94hn5gTSYVhN--oxgNp0QQ6jLc6n4Ck55TOV0wY-qhL3cnd71OTL_fYaAVSd9xz9CrAxjbVlqVukAcyGLvShiulBhJ7DUk6b2VR_qsCpxeAZHOcbf43w_ukoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.
مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند روز به طول انجامد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69333" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69332">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چندین منبع به CBS News گفته‌اند که حملات ممکن است در طول آخر هفته انجام شود</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69332" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69331">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=Jv1ted1NckymnvPw9h5hsSRTepCH6f6Ofk0MfLoUvWWLJZTjDnf_zgJGIORhdkqYc3w4DxSE8Kv-bRVDB7quZgje__qBNHRSLRD-bjyXSJuEQC6rTb4w4qMRdEA_A1XwcUXstUUmB-7KwW490M9x0P9tsin2muEisrHnizy-9f5lyqe-KF47UBkvRBRfQ8ma9k8qMdkCuackarbiXx4D5bNmTXMuEW5zPn86L5FKYbSSzzirF82KpFGmNPZAjmciXTk-pTLW7TKnM2hz6lmovAGzq-BK-sWeYAjdPy9Jg_E4ng2PqCDhFnP01UFeBTOFKV9goO_Q9rxjdsDeUowGyS3Tqlz2-ECj3AUo1Wo-mNIgnh5QKi80xcttXec3Y5hZ3hUOQA0COtxheFMfjVRmwX-oFeTO8YL6E_27_22ac9UYHmLGNOKYeMEl8s8znXzaUnv0oBCgzxUN0bQtMN691I3Bfxb9qN_eeO9WVB1IZCtuLovxXLJLyOTN_hf_OePdTZUv8-BLhXMoQtLCnlu02wBSKXPtUjfBGP-X1fmGDWzX9y-TFP5G44QOa1_rSUZGBa-MN8QTPpeoPzt4IAeFEcmIEfDWeCZqGfQYZiuRfiJv2NxFUckCFwp-D22yIxgQugR563TKpQF-PhWoWapLR4HMcN6cOkZ93W_75RcDWX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=Jv1ted1NckymnvPw9h5hsSRTepCH6f6Ofk0MfLoUvWWLJZTjDnf_zgJGIORhdkqYc3w4DxSE8Kv-bRVDB7quZgje__qBNHRSLRD-bjyXSJuEQC6rTb4w4qMRdEA_A1XwcUXstUUmB-7KwW490M9x0P9tsin2muEisrHnizy-9f5lyqe-KF47UBkvRBRfQ8ma9k8qMdkCuackarbiXx4D5bNmTXMuEW5zPn86L5FKYbSSzzirF82KpFGmNPZAjmciXTk-pTLW7TKnM2hz6lmovAGzq-BK-sWeYAjdPy9Jg_E4ng2PqCDhFnP01UFeBTOFKV9goO_Q9rxjdsDeUowGyS3Tqlz2-ECj3AUo1Wo-mNIgnh5QKi80xcttXec3Y5hZ3hUOQA0COtxheFMfjVRmwX-oFeTO8YL6E_27_22ac9UYHmLGNOKYeMEl8s8znXzaUnv0oBCgzxUN0bQtMN691I3Bfxb9qN_eeO9WVB1IZCtuLovxXLJLyOTN_hf_OePdTZUv8-BLhXMoQtLCnlu02wBSKXPtUjfBGP-X1fmGDWzX9y-TFP5G44QOa1_rSUZGBa-MN8QTPpeoPzt4IAeFEcmIEfDWeCZqGfQYZiuRfiJv2NxFUckCFwp-D22yIxgQugR563TKpQF-PhWoWapLR4HMcN6cOkZ93W_75RcDWX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«قیمت‌ها حسابی اومده پایین، به‌جز نفت.
دو هفته پیش، وقتی همه فکر کردن توافق نزدیکه، قیمت‌ها مثل سنگ سقوط کرد.
ولی ما یه
توافق واقعی
می‌خوایم، نه یه توافق الکی.»
🎙
استیو گروبر:
درباره ایران، فکر می‌کنید چقدر طول بکشه تا این ماجرا تموم بشه؟ یه ماه؟ یه سال؟
🇺🇸
ترامپ:
«پیش‌بینی کردنش همیشه سخته.
ما ماجرای ونزوئلا رو توی کمتر از یه روز جمع کردیم.
اگه می‌خواید همه‌چیز خیلی سریع تموم بشه، کافیه به یه عده سلاح هسته‌ای بدید!
اون‌وقت همه‌چیز خیلی سریع تموم می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69331" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69330">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=W5KUXZGiyEahOEexxHfoWgFUpNhHJzvcSjfEZUuwafcc8uNBxOJT579EwuZk-hyy8cTL2z0Su-hAAKc5_dwQVYk3XmzP8nsyZuM2Lw5AJj3Q6cjKj4etmhznfjALtHEzCjtoAjO1t6kGCzPMQ1nBKbhStdSmQhzxpXLiMpvkDkMK_DboDnzHKeFLk2qMu22hPWyligrMCrkQjaLkh9YE6E58kJf798bYMRHHXYtvVV_VJpxvux0_pJ5ws6dGllBQPRh2FwQNpKVqQ2iXqkrCj63HezVdP7bTe-2oZV-cyypwCZM4Ni7X9wb2UD3ej4IKIlMQndOyNP96lCljI2bzCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=W5KUXZGiyEahOEexxHfoWgFUpNhHJzvcSjfEZUuwafcc8uNBxOJT579EwuZk-hyy8cTL2z0Su-hAAKc5_dwQVYk3XmzP8nsyZuM2Lw5AJj3Q6cjKj4etmhznfjALtHEzCjtoAjO1t6kGCzPMQ1nBKbhStdSmQhzxpXLiMpvkDkMK_DboDnzHKeFLk2qMu22hPWyligrMCrkQjaLkh9YE6E58kJf798bYMRHHXYtvVV_VJpxvux0_pJ5ws6dGllBQPRh2FwQNpKVqQ2iXqkrCj63HezVdP7bTe-2oZV-cyypwCZM4Ni7X9wb2UD3ej4IKIlMQndOyNP96lCljI2bzCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توی درگیری با ایران، بسته به اینکه چه آماری رو حساب کنید،
16 تا 18 نفر
از نیروهامون رو از دست دادیم؛ که همین هم خیلی زیاده، چون حتی از دست دادن
یه نفر هم زیاده.
جنگ ویتنام
21 سال
طول کشید. ما تازه وارد
ماه پنجم
شدیم، ولی همون‌ها که آمریکا رو 21 سال توی ویتنام نگه داشتن، حالا می‌گن "چرا ماجرای ایران این‌قدر طول کشیده؟"
من الان دارم کاری خیلی بزرگ‌تر از چیزی که اول گفته بودم انجام می‌دم. قرار بود فقط وارد بشیم، توان نظامی ایران رو نابود کنیم و برگردیم.
ولی بعد دیدم اگه فقط این کار رو بکنیم و بریم، دوباره خودشون رو بازسازی می‌کنن. برای همین باید یه جور
کنترل و نظارت
هم وجود داشته باشه، وگرنه دوباره همه‌چیز رو از نو می‌سازن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69330" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69329">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=vpeGMwv53HQhGesQIAO9U8eFWUUyYHkpS61dbBVHziRAPt7KZy2N4wVYVbDL7JBYEVR0D8jo9zNuxFvtEOtXqjQOlBZcuChxXet26AjOii6pAUJyTxDPFgzeUGICGUkB1JrHWQ2d2skSboNzf4OgT8O6rkbQmb8Yjx6FhuOZfWWUqHekgpotjh1dF-oynomIVraufQLmD8fUzd9JXsUreUbPMVoLrDKgxt-QdQJ13Q7AuET1U6YD_dYl9I4K_J3udJrit0MyBCeitxRfVj-U2d_QZ8hD1ceuMAWW2zY7HJeIB1e1xWMoTs-QCDua2ti6uDSbAguuysXmsqFHXlH5uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=vpeGMwv53HQhGesQIAO9U8eFWUUyYHkpS61dbBVHziRAPt7KZy2N4wVYVbDL7JBYEVR0D8jo9zNuxFvtEOtXqjQOlBZcuChxXet26AjOii6pAUJyTxDPFgzeUGICGUkB1JrHWQ2d2skSboNzf4OgT8O6rkbQmb8Yjx6FhuOZfWWUqHekgpotjh1dF-oynomIVraufQLmD8fUzd9JXsUreUbPMVoLrDKgxt-QdQJ13Q7AuET1U6YD_dYl9I4K_J3udJrit0MyBCeitxRfVj-U2d_QZ8hD1ceuMAWW2zY7HJeIB1e1xWMoTs-QCDua2ti6uDSbAguuysXmsqFHXlH5uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه هموطن که تو خونش کره خر نگهداری میکنه و بردتش رو تردمیل تا دلتنگی بیرونو نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69329" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69328">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXk1itqMaVm3o8CBdTqlkSC06THVgXuYb8ONC1DeiHRl4UY9NRJHGoygdf1jWk-wVXY3AmIsQS95OK2N168PUZVmOgAov2AeQwQYpnQK9RJSn4OG9hFWrtZRJl04rcs4_UgLMupowA7yFznAhLzob75dtdg-KtvdOu7bsc4JLDuzM96O3jt8XW0ZJytIExm64OKWymxl-8SOVtI8nbtUWzLJ3TQzAuPqUG6f2mlQRG40W5s45vfPXyVNQUh_fSfCgti5GNoVryOcQDZBuJ4ToaHuuvFPGKUlRZXTjHlXzDJoWdooUCWpnE3xw5XHO66IsnNsdaEfJVkyc6OSpnJKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام برای بار هزارم:
تنگه هرمز بازه و ادعای سپاه مبنی بر بسته بودن تنگه هرمز دروغه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69328" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69327">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=ppQqpHC5xYGw14vLcFyJSmrIx0NSGZE5U7I5aZf0ublpv0ZM0dtDki_kfRsRTuEyDfSjlSVtT12NrKvv1-9YT1buAcn6InmNIMV-XBGaXwr-Rt0Qh8kC2G7reDObkMOOLRhOpzRKgPb18PXVcxsvNT0i4ToclVuBYXbVViT4JyBiph7YCKKIWliIHQshiQdrxaWv_XRET8kO2h9eewb3PUedOtE7vx2iSJmP5wT9ZvcvTqKkKGz_AjUrQVYHStVWfLOjQSki-5XrsO5GMP_73s8YNE-LK3vpKoHEF6wEBymYbvWKRWN3UhKeDNTCVsBb9SB8wNoI4V9c2-Gd8XPJqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=ppQqpHC5xYGw14vLcFyJSmrIx0NSGZE5U7I5aZf0ublpv0ZM0dtDki_kfRsRTuEyDfSjlSVtT12NrKvv1-9YT1buAcn6InmNIMV-XBGaXwr-Rt0Qh8kC2G7reDObkMOOLRhOpzRKgPb18PXVcxsvNT0i4ToclVuBYXbVViT4JyBiph7YCKKIWliIHQshiQdrxaWv_XRET8kO2h9eewb3PUedOtE7vx2iSJmP5wT9ZvcvTqKkKGz_AjUrQVYHStVWfLOjQSki-5XrsO5GMP_73s8YNE-LK3vpKoHEF6wEBymYbvWKRWN3UhKeDNTCVsBb9SB8wNoI4V9c2-Gd8XPJqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
«این‌ها خیلی وقت‌ها زیر قولشون می‌زنن.
توافق می‌کنن، بعد می‌گن باید
7 ساعت
درباره برنامه هسته‌ای مذاکره کنیم.
من می‌گم: "آخه چرا 7 ساعت؟ مگه نمی‌شه تو
10 دقیقه
جمعش کرد؟"
شما
5 دقیقه
وقت دارید که تکلیفتون رو روشن کنید.
آخرش هم فقط کله منو کیری می‌کنن!»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69327" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69326">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=Yq3AWc6PFTID-DHziq0vl2SiPq2H8EjRnGtqydkXn9zrgNVAQ7HwbRc7RRYRJEGlLsRX_1DMy0hcMNWdhM_gMO9Yzxur0wmoodyEUVm7QM0BAx6Nsowp0vk5plsveU4DhJP9q_UfV0Ybuwr8Q5s3bDuWi-gQ2lPXmOMLY-pK1fl5HIiAQ_XvoLSprqgRSu1oPYwuiSvEulUCNR46KAVT1Asfmav9nzBjkzFifGzfkpY1F3vtsxJTyBHKaATVxBfpvjxHyygTa9qkwscnq5DTqVmFYgcxE27VvOD43RTyYEviV8Y4auN1AqNzXlaOpbNlRvTJOneObz4X2vagPuOn_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=Yq3AWc6PFTID-DHziq0vl2SiPq2H8EjRnGtqydkXn9zrgNVAQ7HwbRc7RRYRJEGlLsRX_1DMy0hcMNWdhM_gMO9Yzxur0wmoodyEUVm7QM0BAx6Nsowp0vk5plsveU4DhJP9q_UfV0Ybuwr8Q5s3bDuWi-gQ2lPXmOMLY-pK1fl5HIiAQ_XvoLSprqgRSu1oPYwuiSvEulUCNR46KAVT1Asfmav9nzBjkzFifGzfkpY1F3vtsxJTyBHKaATVxBfpvjxHyygTa9qkwscnq5DTqVmFYgcxE27VvOD43RTyYEviV8Y4auN1AqNzXlaOpbNlRvTJOneObz4X2vagPuOn_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
خبرنگار:
سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
🇺🇸
ترامپ:
«هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69326" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69325">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVUUM8DoG3kTtA4OwjsslaJQwohhQDFRost5INQdWt37lOeITznSl0tSQvT68iv0ce7keooSY5UFUhgJFx4wcY3lyNN1gzBHcsaa4Jn1DFTmp_B1PTtFLosLe0Azz0LlNORZ1mIEl57MYiiKxOzcajfKqcQPFTs7Fo0UV3LwDgKpFuawptBALsexqo-GJ5voLLzcuAqsKTVbUshhbCbQ5WqxPbipu7P7kCS7NUBVcKTc33K7Zz5VIhcem1fF5L1FD_ASmj4PNjMBREDaofX8T3iAytOaTUiWwu2BTXw4a2_-cRaPwOmSUNR-0rKm_R6dGITKeo7Np8VPWYjKcaEWEr0h4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVUUM8DoG3kTtA4OwjsslaJQwohhQDFRost5INQdWt37lOeITznSl0tSQvT68iv0ce7keooSY5UFUhgJFx4wcY3lyNN1gzBHcsaa4Jn1DFTmp_B1PTtFLosLe0Azz0LlNORZ1mIEl57MYiiKxOzcajfKqcQPFTs7Fo0UV3LwDgKpFuawptBALsexqo-GJ5voLLzcuAqsKTVbUshhbCbQ5WqxPbipu7P7kCS7NUBVcKTc33K7Zz5VIhcem1fF5L1FD_ASmj4PNjMBREDaofX8T3iAytOaTUiWwu2BTXw4a2_-cRaPwOmSUNR-0rKm_R6dGITKeo7Np8VPWYjKcaEWEr0h4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
حسین جنتی، شاعر : سقوطِ زندگیم جایی اتفاق افتاد که سال 89 جلوی علی خامنه‌ای شعر خوندم؛
من سال 89 دعوت شدم به شعرخوانی تو بیت رهبری و شب قبلش بهم گفتن 5 تا از شعراتو باید بدی ما نگاه کنیم، درنهایت یکیشو اجازه میدیم بخونی.
ولی من شعری که اجازه نداشتم رو اونجا خوندم:
گشته‌ام میدان به میدان شهر را، هرگوشه دردی هست
ارتفاع درد از پیچ شمیران میرود بالا
درد من هرچند درد خانه و پوشاک ارزان نیست
با بهای سکه در بازار تهران میرود بالا
گفتم که خواجه در رویای خود از پای‌بست خانه میگوید
ناگهان صدها ترک از نقش ایوان میرود بالا
گفتم جوجه‌های اعتقادم را کجا پنهان کنم
وقتی شک شبیه گربه از دیوار ایمان میرود بالا
فردا صبحش اومدن سراغم و گفتن تو غلط میکنی با ولی‌امر مسلمین شوخی کردی و سقوط آزاد زندگی من همونجا اتفاق افتاد و اصلا هم پشیمون نیستم از کاری که کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69325" target="_blank">📅 22:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=WCoK8amzfKwice_gIVbB-qnZxyYsNBaF-UzlQodkVpUqYECwXVJS-ibF0uxQjZ45oqpLsnHWg1XiQ3_flbuwJhFIgzcAHNb1eRZiY1SiY4FxPucxBxAHRJR9e-rfKXQP0FCuseCV9fPif9j_sgoWvT1s89F5gySAi8ftkHCr5ShRwhj6D1IE2iT3N5me2gwOtRhrHDxqzC_u8K-bfjX2I0FtNhb0tNybZTZPZrxXdsjpPN2au__0eccBEt-tvRpfwpaV4mqFGSPja4OqkaALasM2205l7NGON3npIjkihQ9a18rllqVNg_GPfapkmQR3qaLYvV-DACeD51pEP48lODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=WCoK8amzfKwice_gIVbB-qnZxyYsNBaF-UzlQodkVpUqYECwXVJS-ibF0uxQjZ45oqpLsnHWg1XiQ3_flbuwJhFIgzcAHNb1eRZiY1SiY4FxPucxBxAHRJR9e-rfKXQP0FCuseCV9fPif9j_sgoWvT1s89F5gySAi8ftkHCr5ShRwhj6D1IE2iT3N5me2gwOtRhrHDxqzC_u8K-bfjX2I0FtNhb0tNybZTZPZrxXdsjpPN2au__0eccBEt-tvRpfwpaV4mqFGSPja4OqkaALasM2205l7NGON3npIjkihQ9a18rllqVNg_GPfapkmQR3qaLYvV-DACeD51pEP48lODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=gd5YPJIALEp4JxnQwqH2sbzdqtZJU4-0poQKgex7PM2brc1hPHPqW94je0AdN6XTy8JYH8EZHZc866FnR16DfJ5g4I0hV5wcF91flNswsQI94fuoECGXgKs7bPHjKQ6lSwV9mh1yj-UMpAq1vkgm_RuJZwreQtyW66ZmVReAdFhqp_7aJ9y-mGzJ83I-lyywis9Hy0nCWFHG2MhG6bjTGER7G0BpLISjFHXu8VX0BhHVydiDv3Kv54YSkh2ab3l9ihMWiRh2dLLaNxkD3mBH_J_BiUokve9zvyVeE0zGL8IuVVal9a50AzFjZhQmOb4xYWKb6GSadJqzfJQiJ0o4LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=gd5YPJIALEp4JxnQwqH2sbzdqtZJU4-0poQKgex7PM2brc1hPHPqW94je0AdN6XTy8JYH8EZHZc866FnR16DfJ5g4I0hV5wcF91flNswsQI94fuoECGXgKs7bPHjKQ6lSwV9mh1yj-UMpAq1vkgm_RuJZwreQtyW66ZmVReAdFhqp_7aJ9y-mGzJ83I-lyywis9Hy0nCWFHG2MhG6bjTGER7G0BpLISjFHXu8VX0BhHVydiDv3Kv54YSkh2ab3l9ihMWiRh2dLLaNxkD3mBH_J_BiUokve9zvyVeE0zGL8IuVVal9a50AzFjZhQmOb4xYWKb6GSadJqzfJQiJ0o4LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=vpO_GKVc4DD-1c6TVu7uY3QFE5dMaZQdWC-icd3ztubocQjo92wl1vG5CQGu72xz4K3U26VEDrN2gU6dAHb_fhkzVHbaC4TYF-bZinc-r6vtHYwLyy4zlgCAOeTfHzQ6xbbvfQy1hO3DMpclBbeg6ZFAagsUZrWlZdqWy6aklf-BkXWKAz85guuTjiRSGS3CCLG-pjQ_83Xxii84SYvMtcDDE3-GBIfx8gTiyHX0L_3BUMRTf-UHz2cgKKIXRQfBgRGf8s6Yi8osgml92uGEGX8Fa0CvspQ1xdtzgNrcqjSQwYh_mMByZGBXRxUknVciKz5fVkjZlDDw8yQRi1a_1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=vpO_GKVc4DD-1c6TVu7uY3QFE5dMaZQdWC-icd3ztubocQjo92wl1vG5CQGu72xz4K3U26VEDrN2gU6dAHb_fhkzVHbaC4TYF-bZinc-r6vtHYwLyy4zlgCAOeTfHzQ6xbbvfQy1hO3DMpclBbeg6ZFAagsUZrWlZdqWy6aklf-BkXWKAz85guuTjiRSGS3CCLG-pjQ_83Xxii84SYvMtcDDE3-GBIfx8gTiyHX0L_3BUMRTf-UHz2cgKKIXRQfBgRGf8s6Yi8osgml92uGEGX8Fa0CvspQ1xdtzgNrcqjSQwYh_mMByZGBXRxUknVciKz5fVkjZlDDw8yQRi1a_1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69321">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=eqbtQgnjP65D8QTs2qQxSqY5oI5IObx9Fu-CTkZHeBb_vK1GYe_gkaK8ak6697vYxHJ_I6Z_G7Ckr5UXoMsVw2eL-pfskPgzx6xPz96l1SZYICBzIKO6MBdrVQKyPxe_PYqd-xr_dctnmzz1p5AENXRCXAC7CYmI4jBd7Dp-xtLIZjhZCqhlgk4pWtVi9LZs3SiDh7skWB4GxB0kU7aQcLbATZNK2C8hNSlT8Ptdxxq0G4YPK_Ty5Kmr4F_UT9EQtO-9W6OYTs1k290AGqj5tiFhzEeUlZdYPINByLUmP9VZdwPI7Jf0akyf989HW_HAD5r7-LXmWlRDSqAKrMmshg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=eqbtQgnjP65D8QTs2qQxSqY5oI5IObx9Fu-CTkZHeBb_vK1GYe_gkaK8ak6697vYxHJ_I6Z_G7Ckr5UXoMsVw2eL-pfskPgzx6xPz96l1SZYICBzIKO6MBdrVQKyPxe_PYqd-xr_dctnmzz1p5AENXRCXAC7CYmI4jBd7Dp-xtLIZjhZCqhlgk4pWtVi9LZs3SiDh7skWB4GxB0kU7aQcLbATZNK2C8hNSlT8Ptdxxq0G4YPK_Ty5Kmr4F_UT9EQtO-9W6OYTs1k290AGqj5tiFhzEeUlZdYPINByLUmP9VZdwPI7Jf0akyf989HW_HAD5r7-LXmWlRDSqAKrMmshg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار:
در مورد ایران، گزارشی وجود دارد که نشان می‌دهد شما پیشنهادی از سوی ارتش برای گسترش چشمگیر فعالیت‌ها دریافت کرده‌اید.
ترامپ:
ما از قبل گسترش داشته‌ایم. منظور از "گسترش چشمگیر فعالیت‌ها" چیست؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69319">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=POdfRHA1BIFDPm1ytlYx-OFPGtMdLL4s1xse4ZN-bCpopTUfgFU4oRuqlOLju1sljIjJMvqp8SAYgIwe_J6vrRoLi67uzMn-vf1qwY5vtgA-RNMkggcz3F7cilaj1208yMDiM66WmelWO-ViEoTzMLnbb9GeKk4cFoGOdslW9uufrqEYDpUsHw2cYB-O3bYFs9Yh1x_44RtSugUXqKGjkXLLeuDZ4eMEiZ3mtDhwRgk5zfztm_KIuKTxAcdpnrVPy9gIcT1BTL4Itekgu663bZjlZWKNQHHRMEkMd2Q2viEczTeby12KojjExbEOTfi-7UpGPA7E1kqqKiE7TfBi1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=POdfRHA1BIFDPm1ytlYx-OFPGtMdLL4s1xse4ZN-bCpopTUfgFU4oRuqlOLju1sljIjJMvqp8SAYgIwe_J6vrRoLi67uzMn-vf1qwY5vtgA-RNMkggcz3F7cilaj1208yMDiM66WmelWO-ViEoTzMLnbb9GeKk4cFoGOdslW9uufrqEYDpUsHw2cYB-O3bYFs9Yh1x_44RtSugUXqKGjkXLLeuDZ4eMEiZ3mtDhwRgk5zfztm_KIuKTxAcdpnrVPy9gIcT1BTL4Itekgu663bZjlZWKNQHHRMEkMd2Q2viEczTeby12KojjExbEOTfi-7UpGPA7E1kqqKiE7TfBi1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران وضعیت خیلی بدی داره؛ واقعاً خیلی بد. اوضاعشون خیلی خراب شده و تحت فشار شدیدی هستن.
تعامل باهاشون هم خیلی سخت بوده؛ هم صادق نبودن، هم قابل اعتماد رفتار نکردن.
ولی این چیزی رو عوض نمی‌کنه؛ چون در هر صورت، حال و روزشون خیلی بده.
ما فقط پنج ماهه اونجا هستیم. اگه به جنگ ویتنام نگاه کنید، می‌بینید آمریکا بیست سال اونجا بود. کاری که الان علیه ایران انجام می‌دیم، از نظر من یک عملیات نظامیه، نه جنگ.
ایران هنوز چند تا موشک داره، اما خیلی کمتر از چهار پنج ماه پیش.
توان تولید موشک‌شون تقریباً از بین رفته و ظرفیت پهپادیشون هم تقریباً نابود شده.
البته هنوز مقداری از این توانایی‌ها رو دارن.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69318">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=DehNEmOMthUW7ACXrbNKdLK3wpDXvLn2UOcjjZa-aCYMwmwUoNM6EsbLujkpjKG9RwqgbT2C3RyAIXqPe6f1-srJWzU_VCpfrhuID1Z4P1NBQOsOCqwtidj3SVC9Gejape0Xef0qq85Fss6u8ba-yf2QDmtn6JNnvvAKUSIl1dYFUNCEDHxGBgg016AHsfZWSQMF7xzcQ7Jmg_ia70ptoPuGNpH9O_r2ArTHEzI8aoOVcxSB-oxyqTS6dm9Vk_MkMoie2xaMM1fY_HCsYklb_dco7ls99KrQAGzIhk9C9s34vzJ-Ukw3O7e_9OpmLE02HNF-G5QBLhk5swDuTpuS9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=DehNEmOMthUW7ACXrbNKdLK3wpDXvLn2UOcjjZa-aCYMwmwUoNM6EsbLujkpjKG9RwqgbT2C3RyAIXqPe6f1-srJWzU_VCpfrhuID1Z4P1NBQOsOCqwtidj3SVC9Gejape0Xef0qq85Fss6u8ba-yf2QDmtn6JNnvvAKUSIl1dYFUNCEDHxGBgg016AHsfZWSQMF7xzcQ7Jmg_ia70ptoPuGNpH9O_r2ArTHEzI8aoOVcxSB-oxyqTS6dm9Vk_MkMoie2xaMM1fY_HCsYklb_dco7ls99KrQAGzIhk9C9s34vzJ-Ukw3O7e_9OpmLE02HNF-G5QBLhk5swDuTpuS9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
اگر برایتان سؤال است که چرا حوثی‌ها، با وجود اینکه یکی از نیروهای نیابتی ایران هستند، وارد این درگیری نشده‌اند، دلیلش این است که به مدت ۴۵ روز، قدرت نظامی آمریکا را از نزدیک تجربه کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69314">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=looYEeFp3PFZCNd0pmQmR4RjoYZFpx68nIIXiYjDQiygEgWiXrUNZvpZFW2u0kaIV-UophQfTaudNTQuJ91yAlxZlXiU6rYuBIu8zGB2ym5TevWK3EIFoSC6x5_fhVsf4zfmiiyVY6N_YFtXtXIa-K-HYvzj9yarjAJmfpFNcAUKmLtQ7GcJa2lNoMoOIgqsEnRMjNSPUxqfDxkN8VrgNpOOGAwrhbZH-HuohTKk40K0rxz-oT3CFH0VsxYTI_OfYedgwjG0Hk2SycPWmlUrzg7epWvNzKwzYtmNNu0ZnWO03x4F_66k8Zo-jBIQ9hFTD9yKwbvTmxSZukK_P6_zUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=looYEeFp3PFZCNd0pmQmR4RjoYZFpx68nIIXiYjDQiygEgWiXrUNZvpZFW2u0kaIV-UophQfTaudNTQuJ91yAlxZlXiU6rYuBIu8zGB2ym5TevWK3EIFoSC6x5_fhVsf4zfmiiyVY6N_YFtXtXIa-K-HYvzj9yarjAJmfpFNcAUKmLtQ7GcJa2lNoMoOIgqsEnRMjNSPUxqfDxkN8VrgNpOOGAwrhbZH-HuohTKk40K0rxz-oT3CFH0VsxYTI_OfYedgwjG0Hk2SycPWmlUrzg7epWvNzKwzYtmNNu0ZnWO03x4F_66k8Zo-jBIQ9hFTD9yKwbvTmxSZukK_P6_zUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
آخرین آپدیت از وضعیت اسپانیا:
- مهاجرین غیرقانونی همین‌جوری تو سطح شهر پخش شدن.
- چندین مورد دزدی از فروشگاه‌ها گزارش شده.
- کنترل اوضاع از دست پلیس اسپانیا خارج شده.
- مردمِ محلی گروه تشکیل دادن و دارن هرجا مهاجر می‌بینن، کتک‌شون میزنن!
- تو بارسلون هم مردم دارن خونه‌هاشون رو از ترس مهاجرین، سیم خاردار می‌کشن...
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69311">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=QaslnsuNe7ljCAO0jvdjxj-9nW1OKSZe18eeQfjeg9Ad3QCuCHVr6mLYuyhfhnxBs7Qwg6iFvA1qYFvf2WouXrFkAW1tJB25_1B6XJWefweoW63VEpgby8WnuQSMbsN3Uhle3AQDKVBokUbqJFrhRuqcPDRy4P4p9GzGAzp1_vmt8s7BGp0sYPnnMQib41mEmVH_sjs5MMG86mg2CGLLeVni8P8yqZ-m6JBMbTT76AOsdiQeC_jT1pZHKNDM7ZeFqxXZUED1Ms3aKaVKs9kl2qG0X6kIat0BoKFQq8dWIEWcyTsi8BwKeB2XQpWXp2C5VbreXArzX5rBOwZjgVvcrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=QaslnsuNe7ljCAO0jvdjxj-9nW1OKSZe18eeQfjeg9Ad3QCuCHVr6mLYuyhfhnxBs7Qwg6iFvA1qYFvf2WouXrFkAW1tJB25_1B6XJWefweoW63VEpgby8WnuQSMbsN3Uhle3AQDKVBokUbqJFrhRuqcPDRy4P4p9GzGAzp1_vmt8s7BGp0sYPnnMQib41mEmVH_sjs5MMG86mg2CGLLeVni8P8yqZ-m6JBMbTT76AOsdiQeC_jT1pZHKNDM7ZeFqxXZUED1Ms3aKaVKs9kl2qG0X6kIat0BoKFQq8dWIEWcyTsi8BwKeB2XQpWXp2C5VbreXArzX5rBOwZjgVvcrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
ترامپ با بالگرد «مارین وان» (Marine One) وارد «کمپ دیوید» شد تا سیزدهمین جلسه کابینه دولت دوم خود را در آنجا برگزار کند.
فاصله کمپ دیوید تا کاخ سفید با بالگرد تنها ۳۰ دقیقه است و رؤسای جمهور آمریکا از زمان فرانکلین روزولت (FDR) در سال ۱۹۴۲ از این مکان استفاده کرده‌اند.
نام این مکان برگرفته از نام نوه‌ی آیزنهاور، یعنی «دیوید» است که توسط خود او انتخاب شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIIsQbcyc5Goq9u3pK_PRriNME95TrcMiryb4FnKJgRq3dgVsRj1iEDBRcOCW-S5M-ESm-FwU_Lu9ikDiTbisV1SLxQZ2aHL8MOk4-7hJ_HLxjpyJJuxhUs_H5GMtOMiFMfwFeyUOXU62VPPmdVQyojvswBIVwubgoMVapE6v_WzCz7SEzWnura34hpjiudDUYdfazRZz60Ht2gQLAH2nb3hHugXhjsM2Dk-9lZAG0wUghbVi5eEDAenAAGn7mB0CkB57l57G07LuQwiezOlyyys6bg2MaSf-wBiTmyf21GNFHy3Zx2ANJxPn_WwqbgqV4lhqtaCFK0pspN2lBtMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=GMuFe_6BXch6Zsse463gJe83Z5nQApA2F_mg3C3skeuXdQ9kjfBfVCqFFR6GmJpabKPtNZ6wu0rLEbZFYNuY9BlGxz2wbCJ2bfhPGxodGv_co5IMYhyMvIf3hvAJ8e3MqpmZ4HNJqL_NjxUyMFXJACUS3GIB92Rmaqi0ebEqFl1p-4QA90bPhd_zYYkbuzNCSAD-Oh_jYEfXYkx5ETxbYcOKM6qKGAg_wcEqx5gR_ReBAcWA7RHDgh91v9BAMup8z5cKoqI_awS8TEIq2nCbQG3Lk5ePP94dKzRPJiOj1uv6H9_kq1XZFp9I61aYTiYT_2d6WwrJGQJEIndEBqXsfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=GMuFe_6BXch6Zsse463gJe83Z5nQApA2F_mg3C3skeuXdQ9kjfBfVCqFFR6GmJpabKPtNZ6wu0rLEbZFYNuY9BlGxz2wbCJ2bfhPGxodGv_co5IMYhyMvIf3hvAJ8e3MqpmZ4HNJqL_NjxUyMFXJACUS3GIB92Rmaqi0ebEqFl1p-4QA90bPhd_zYYkbuzNCSAD-Oh_jYEfXYkx5ETxbYcOKM6qKGAg_wcEqx5gR_ReBAcWA7RHDgh91v9BAMup8z5cKoqI_awS8TEIq2nCbQG3Lk5ePP94dKzRPJiOj1uv6H9_kq1XZFp9I61aYTiYT_2d6WwrJGQJEIndEBqXsfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVl6I66r69-nAOgCecVKzTRfJOP6K82G6G2Wjo_bM-xy6DYIjujzUrypsbMOXpKkNRt4ZneaAoNVS9a8mCg2BeSnxuo50r1SFHGphosxJz2hKze0nEK3DpPzz0vtdk56OZGbedd3I_PyF0qR1KO0y8WtOQhffk4NhoFHvd5EIe_yZXl5yXsYJs6JxNpG_CnccUCtMyJrA-4CV_Q0ghe1q6x6qK4lnZ93rkd2Agope2qEkmfqb4Y9KXQfM7mNgr-kuZ45mT0hslzB0pJIM-4mLfpUn6xu1h7QX2QrWLxjKOsQpfnvoDy7R3l5lSj1hbqngGEaQw0wg90Hsg04stTUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=UxVW2cRaL8tnKM_kivj4_e2rJ1eRfjUFrgB-N1zhxcYxi4LdPf5hT32FLNS5gUPRlCyLLpSxZhRmnoTcweOaUED9zkBp8z1NxzXWDS8APKGuA4wIn7-a5xbX-b3xtHu1UoB8o6RKDvuZxEJnquB8Xmz92WDmZSymwNzmPjTJjMvTLbPMdgX4a20It-_Jfr0R8W2Rxp_htYR5I2eeK9MYFdDinqiuQkJescq01Gi2PLoOC9KoT92_t9gt4wDUb9uMrjIpdDviT5-M7O9TJIW2PqKyl01R_WuTWucbgAjjAlWbfTW9nS1WMa3lRPTdrkPvtjhEv-hVleO2cxQF8yEKiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=UxVW2cRaL8tnKM_kivj4_e2rJ1eRfjUFrgB-N1zhxcYxi4LdPf5hT32FLNS5gUPRlCyLLpSxZhRmnoTcweOaUED9zkBp8z1NxzXWDS8APKGuA4wIn7-a5xbX-b3xtHu1UoB8o6RKDvuZxEJnquB8Xmz92WDmZSymwNzmPjTJjMvTLbPMdgX4a20It-_Jfr0R8W2Rxp_htYR5I2eeK9MYFdDinqiuQkJescq01Gi2PLoOC9KoT92_t9gt4wDUb9uMrjIpdDviT5-M7O9TJIW2PqKyl01R_WuTWucbgAjjAlWbfTW9nS1WMa3lRPTdrkPvtjhEv-hVleO2cxQF8yEKiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=QCbWf6Q2x8QW7nKEBZgxukva0Z64OxEPOnySxsPjoj3wqWMU3-2VDVP_dpbZs-aX1u8rSV1OhrL05cF52PwFNICW7mCTIR0pu8erhz_GHQQ3O4nwbEkLRMeBAmitKpmekWQFZfs5fulrCf1GrGBWvdtsN2rYchRf6ynSaP2DW1CzeQ9PcanLG-gJCMX9PilMprTqLX9-RxYykl9R01K8LbqllO8A8iau32yDJTG9hOJetXthveLScdu9uRU-oGaWFQ8s1n6hPOXRumJSeg2KvsJcjfWLpWOh-y0mFfCOwFvbNJLu1iTGqjCS4OLHYulZS1ZY_GyOmm0VdsBnzUazmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=QCbWf6Q2x8QW7nKEBZgxukva0Z64OxEPOnySxsPjoj3wqWMU3-2VDVP_dpbZs-aX1u8rSV1OhrL05cF52PwFNICW7mCTIR0pu8erhz_GHQQ3O4nwbEkLRMeBAmitKpmekWQFZfs5fulrCf1GrGBWvdtsN2rYchRf6ynSaP2DW1CzeQ9PcanLG-gJCMX9PilMprTqLX9-RxYykl9R01K8LbqllO8A8iau32yDJTG9hOJetXthveLScdu9uRU-oGaWFQ8s1n6hPOXRumJSeg2KvsJcjfWLpWOh-y0mFfCOwFvbNJLu1iTGqjCS4OLHYulZS1ZY_GyOmm0VdsBnzUazmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkgP4KlZvCNlFthKBzizCStGrYydYX5Dn-5zev_uCb0V3q5zJCNw9SKg2p5fHAP6d1yTbQsXBhZk12uQYTy7Ny4MxvQu8U2ja1II8kKVLtailJyR5nFlUimqt0viZPXSr7e6-nhfBGDhMzrgYmsskh_DMVgw8OIf2zIsMtxmOrRNzyPeZgEsT6mqhfk6Qq9ykloZpMJWag5ZeA3AgxoeFmAqns1Ps3cIwpDzJCCzbwZe5nk3SwGU6dE5EChhlTwI1TFl9m61cHRcVvaVMgn6j_sN83sDa8WyZA-xHSWREU8o32c2ni7xFgYpi3ogvQx0ucKqZxjy_i7lsbHmU1Wudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgPZfjKWR2nOR_wloBFl9adtRIirLA1yz0_QaaFUflorXsfNcb6XC7h_cVHddCvMnMqrMXwW0oJYUtvDLdrrKHwvb5lNy6Gt2tDKFs-Wf54mtqBK6oYf-sAUqX7XpYB42zBrnrlk9G3GNcY2Ycs22c3yLcCUuUgDfCGj8h-gR39_h45hDQB57yYJdUp5KrzeaSrfsDn7_W-5i7cL9rNhUo77U46FapSUFCIpf25yNrH5Jhzixn4zL3bAIotvQBb7dqemA7vydBNtvbo3ok7UElhyXtTm0oa7-4x8KLhoUapK7Tzvmm1AtR3wljXigRHiTyeEQ3s0bZQc_GCTmXcbhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAEk7dHYXY7QdiQ4xE6-U-YZwXiERJWqeUj6ZFcj61aiyqcI2JUvnVKfApT9KQqiP4b1afXdjZygRkEblrOvSoeKyHJEbAnSRAAGbPjBeiXxQBUlkzT74lgljXyS_I52S5oJc1kEStpsuckOej6X7xH69fn8-adNwK0-v0L4-RKvTzrj2lGIjp5nGaXhXWT8yfFZXBJ5KFTtjiJJ8Ox0wOfd1WxcDoNneP0mWdnrhP9WyXyKii2RdaLkPS_UfYKxX_P-m2hkQTApl9jfk1KFmRB1Cw5FZlAWwqZn3Cb-pjT28C0oFM8-w8vqlUy8ypSaT9c4d1Xxhip3BNiXqIAypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=aFfAgR_6d6JK0B-bhw0k2a6fzaW2C-NmMu6R24FsWy6MXxcvWa8Ynagnx3ubSW98iPgOyd1fTv_qXYyGjhq8EgLTxa1P1XahF41jM4Bm1PWee3c5rKdEu3LRwwOvqXlPAa2ktqFSwyFSyudvjZQNNojjO1PxgrfYrh7rODDd9ZlMp8-bXJIhBNXxjIvXZvIWvhwSI6BuszhYYJad4iOb4TR8jnggRdSiZqxg40OgWDesN5YtALzv4G8aJ4HB-JxZkSfx1VXtix-NOv66DblSlBpmzxPbfJ15nxmqH389qcy9xgUgaVutLQGpuyzmqvimvzeG8Ol9RyD1P4bV0OYRkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=aFfAgR_6d6JK0B-bhw0k2a6fzaW2C-NmMu6R24FsWy6MXxcvWa8Ynagnx3ubSW98iPgOyd1fTv_qXYyGjhq8EgLTxa1P1XahF41jM4Bm1PWee3c5rKdEu3LRwwOvqXlPAa2ktqFSwyFSyudvjZQNNojjO1PxgrfYrh7rODDd9ZlMp8-bXJIhBNXxjIvXZvIWvhwSI6BuszhYYJad4iOb4TR8jnggRdSiZqxg40OgWDesN5YtALzv4G8aJ4HB-JxZkSfx1VXtix-NOv66DblSlBpmzxPbfJ15nxmqH389qcy9xgUgaVutLQGpuyzmqvimvzeG8Ol9RyD1P4bV0OYRkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=ch85Ifp3tj2PqQuH5Jg_dyR9XGEx_TPyXhPgeJEKOcRT-gzz4xiNUU__aWj7nop5bp0CwG69TJPrYEXKm5YZnpRQ3WpMDg8ki-yOpfnJ3w6YDN3kmQ0UIl-SXZP_JmVWGPPWfhkxYyNHMg2lFrpXa2ex_yjWYAM46iGthyMX-tnrykmODp5xn7pWLclweSnfEYOELr4zSCO6BkfxNYyi0kgQHu9U5Q08I19xYvrfCdTNPy64WxJp6LYtYLvGD39gqvK9FA_89LC3R-FYx9YDiVQ5y70QfeGby5cRsqUXSMxk5zRoT8fbJnKsV8PUKZoaQ_rJNQQ5aJfgQkWwhBbl2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=ch85Ifp3tj2PqQuH5Jg_dyR9XGEx_TPyXhPgeJEKOcRT-gzz4xiNUU__aWj7nop5bp0CwG69TJPrYEXKm5YZnpRQ3WpMDg8ki-yOpfnJ3w6YDN3kmQ0UIl-SXZP_JmVWGPPWfhkxYyNHMg2lFrpXa2ex_yjWYAM46iGthyMX-tnrykmODp5xn7pWLclweSnfEYOELr4zSCO6BkfxNYyi0kgQHu9U5Q08I19xYvrfCdTNPy64WxJp6LYtYLvGD39gqvK9FA_89LC3R-FYx9YDiVQ5y70QfeGby5cRsqUXSMxk5zRoT8fbJnKsV8PUKZoaQ_rJNQQ5aJfgQkWwhBbl2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jAFOVpMt7JxvWwkQKdo6x37XH0Wfr_M7Hep4d_AWzF71o6qMhQ5W8l0ZXsrAAN1tww-4zjKDr2d4hyMn0ZrMouj5YjixFrqgLAoqlt0MUlNspQB_AKxm0_cbaC88r9TlQU4MExZ4D7q8UsGiXElq_U1wEMOIguHa_EgRQn_FU9fF0U85rLGEV6UrdvB6eLCgUrtEUfnhApdhe9CqB5hX5pXmN3H_hhBEN-e7L4baxzY_d8my5qO5ZBcF8bcnTmS9gdeUhzfwk3FYKMaUQB2YwOcNoWEr-Y6EcrKIrWR4qaunGxHVl-99oj7z0jJWEwpSkpQNxzl_WJ7tBRqw89whDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=UwevnduQJcI9P_gKaoidpSp3il4sQIbI3DEibRtuSUHmlZYBiJFGtuZZCc0VXYdE9Qi8_129bDjOWwMG_G5X-mCV81MkYCwQzVBPmn6-Izkqb-gf1ToejtaJ4c5d40nMohStIJsVu34vSWLyzTyEp3Ht36qLMdBIsFpYbnEliJg4iQOoMV_A5phZI7eK6yRnECbBMMolIeTpkyqMwVgEzx9EwZJ64AxnqhEXPg1AzSgwh8e1ZVu3s5RRZkyyIoGk-pq8Y_NGYO8A1ab2Q7-eJGi0R4_vRO5L3Yf0QG6GLRMB8cV-H54cZsTYXgGMWgs2V8FtCa6b7wyI3rL0ljGwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=UwevnduQJcI9P_gKaoidpSp3il4sQIbI3DEibRtuSUHmlZYBiJFGtuZZCc0VXYdE9Qi8_129bDjOWwMG_G5X-mCV81MkYCwQzVBPmn6-Izkqb-gf1ToejtaJ4c5d40nMohStIJsVu34vSWLyzTyEp3Ht36qLMdBIsFpYbnEliJg4iQOoMV_A5phZI7eK6yRnECbBMMolIeTpkyqMwVgEzx9EwZJ64AxnqhEXPg1AzSgwh8e1ZVu3s5RRZkyyIoGk-pq8Y_NGYO8A1ab2Q7-eJGi0R4_vRO5L3Yf0QG6GLRMB8cV-H54cZsTYXgGMWgs2V8FtCa6b7wyI3rL0ljGwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3HIsXCylj7QZ3mhFW4OjDUUo6RKTS5uh1K1ltmhxIpHGCYoM1M6Ev5Gt7QYgaDRf5tBQSUW4JueuM-0gz49N2qrYpBjwFpGPEV0qfRvA8px7h6H660oQvo3bbI58fcXF4HduUhIY7jQPVRrmD3UMRYUP5MKxbY8GwZZi_DWMOAcpTV--Ls4gjN7ByfCjPyAR8M5HUr_gHG_pybdTtvD2UYOPMYYWoxTrWg3NDSzAmZO4Jzou9ZFaQEFh-x7fGwB_Ubl6Uon7oVwdSM_LPHkfHn8yjoUFLgNFRZPUYg145N4gZU8Hdfj4dk4wUPY6RD3WUM_s2C7KnCaI3YB65_7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAGSMrFIB9RXsMGA7XDFP7uqir1gh_b1rztlKtbCmLniZrG3cfTIXB1UTvnVu_0k7kBO9LM3JdYmhnmkXd4GvjL5K4t5--Ougp53ZXv7rjVQxE0cQRTFABvZcwzy9DlLddmMyY5oZbdZUTMW-MWB7ElwucEuMWmz8r5MY8r19yRwrr-Syxrcb_TciSQDo5-Heed1B5iXa9bE4izM1UJjLOnxOJKP8AMKXOG1scNOooHRhnLNGN24ugNmWlcZsqSEyjPgUlCo5Lo5AofyNxc8kRMuCq5Muv5eU-hcgUSmb46wYdzDg-v-nw3bVL_JygExlmz10DYbK_Nnt4CJ82lQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=RuqhRfpnG9XmIptCrpJnEgd8lyYGUVm1GXHLjR0QC5jrTyBxv26gTbb6NPrtIHhd1JWV1HLVXv-mjeyLBtlirSqiiUpn2xso-ZUcmHVghcqNjWcqBzMIIHgQNNNMggZGL7Ff55kdQoAcx_wqeNomvioz1o4zqdqW6-pCq0zUDGgvXbt_Zg-RfMW_2TyR_DJkj4hHgHu6bBjvVNg0dR9PMiVDiQIvUtJJ8GayRdajBkJSkxUO6PsAMMXFZaq9YZoGzafgxeektLRrARGqTyT74OzW6dqXZcumh274T1kgQpbP4U6lthBpRSlFNqjejm8uVvnKQF9LfPsz1nPP11lRgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=RuqhRfpnG9XmIptCrpJnEgd8lyYGUVm1GXHLjR0QC5jrTyBxv26gTbb6NPrtIHhd1JWV1HLVXv-mjeyLBtlirSqiiUpn2xso-ZUcmHVghcqNjWcqBzMIIHgQNNNMggZGL7Ff55kdQoAcx_wqeNomvioz1o4zqdqW6-pCq0zUDGgvXbt_Zg-RfMW_2TyR_DJkj4hHgHu6bBjvVNg0dR9PMiVDiQIvUtJJ8GayRdajBkJSkxUO6PsAMMXFZaq9YZoGzafgxeektLRrARGqTyT74OzW6dqXZcumh274T1kgQpbP4U6lthBpRSlFNqjejm8uVvnKQF9LfPsz1nPP11lRgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak8TjCVjOIvoJ9-8JWWmgfyiY5XUGatHbNR9M-SztIFJjMa-l2wFSqqOcHmVzSEZUa-LVboRRqbcBwkhUz3zHvxWtq3vcJ8AVD-NZaGghQBFMelZ8f27McFnswWBXrKmyOYTkUgL5_qMG3_FoE9Qag-C6ozfEpSbpYav2K0iCQLELFyLeYruaSqZQKhUfb-H-eQu8yIaymX7gjNA4JLixnDFeLK6A4rcrUcQnL_Q-usB906O_3oK_TXuULkkEy1cEcMwqvHSkgRvYL6L_7gwma1zoNPKjPLifgEdmMLnqaSeEkI942QBQnx5wZxDSija7w5PphS1YyGHNADtK8TdMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=qA5l3kZcFYIHDvykwmBszROD49Rd6dP_zpcILoF3cmINu_wcrcNwr49MA__Kdva4svbgd2_7k_GGl4-bGC5QRCdTGEA1d9Jk4L0Cj17-IvouAw50tr9AKwyngWUuakVYQBUzr4MNo-9t6SmsSbnkm6joXi_BhWOad7xu-Vabq3hjdV9mhWhJxLn4M0n6fPc2RbNj5eLF3gW-8t9t9T4UHYy3HZwOpHcDepR2q35tvpc6FfjYAAm-vvzbSQcoQWEsbKE-f8jhagur56SnIJO3yWwhDbKnYEeC9xVVYBscvVh9C1PcwvQOuciwpS9mzq0AbpOZPbXBXb-PQHZ0VLNrkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=qA5l3kZcFYIHDvykwmBszROD49Rd6dP_zpcILoF3cmINu_wcrcNwr49MA__Kdva4svbgd2_7k_GGl4-bGC5QRCdTGEA1d9Jk4L0Cj17-IvouAw50tr9AKwyngWUuakVYQBUzr4MNo-9t6SmsSbnkm6joXi_BhWOad7xu-Vabq3hjdV9mhWhJxLn4M0n6fPc2RbNj5eLF3gW-8t9t9T4UHYy3HZwOpHcDepR2q35tvpc6FfjYAAm-vvzbSQcoQWEsbKE-f8jhagur56SnIJO3yWwhDbKnYEeC9xVVYBscvVh9C1PcwvQOuciwpS9mzq0AbpOZPbXBXb-PQHZ0VLNrkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=aSCYfsUJTP3vXkAVmOYuU2wrBAN-m4lDwap6YO40AdKZRyyhVm5VFt9WhPje02XCQqqkrZtk9ESC8kL64SvLNa3glhwXnm_ivOSLfSLsuzl5GDNizc-oI0LsGlQc8shQUr9BKHAwgtzGtKlHlq72ZTt-I6NRforhc9pPpl-jtYmlqV4C22DHMi2SvmkV_KI-1Lr9fUQ3AAKTOojU9_wJj3icVcA7wXDExLe7iv06Z70xN5_BQg2oki0r8A1C4v0CkrG4vDud-pRlwzyt73AKy2S8xr8_COIJjhxVaAnq0wyqb82lVJgvNZry7zUCZYtzz3-ss0LLg1I0t0wONjmQYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=aSCYfsUJTP3vXkAVmOYuU2wrBAN-m4lDwap6YO40AdKZRyyhVm5VFt9WhPje02XCQqqkrZtk9ESC8kL64SvLNa3glhwXnm_ivOSLfSLsuzl5GDNizc-oI0LsGlQc8shQUr9BKHAwgtzGtKlHlq72ZTt-I6NRforhc9pPpl-jtYmlqV4C22DHMi2SvmkV_KI-1Lr9fUQ3AAKTOojU9_wJj3icVcA7wXDExLe7iv06Z70xN5_BQg2oki0r8A1C4v0CkrG4vDud-pRlwzyt73AKy2S8xr8_COIJjhxVaAnq0wyqb82lVJgvNZry7zUCZYtzz3-ss0LLg1I0t0wONjmQYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiwR4Vs8ciTqqysP67TxgDVl-9Xe0XVvD5e6yaCYpqAdp-IIclu-39Fp7UGm09o_IlsiAqa19aKDXwsp48J1bWvScLxVj_LbTOnmDwbQoMD8XIY7AF5QNHt62Ezv1OUyHEwrzAKjI4vfNE0BmSx3CXHzox_JILwpA0yWpjhoND4afG0x_pG3cBJHcCpOvyjCjGRMmSpvUM0Me-yVFQUNiv3PmlNdUfKF1bJg4-WJQrARM2ivXu9WVuCHqpIWEdOLGerSClf6mhm5kph3JGSqs2kupRssFeE_cNSijGXplpCcl14-THidxfanuUvyZ2F7BXHI7Hl3jdSooxx7CLBK9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8acYOhbMBLKIGbBMAzd6bKABbnHjLWQw70Q3cKsKMmqjUGq4cUAL6OpcvAes5sDRfsVnb22DGvKHijKchwYQOhcLGAXon8mV69Al85qRtX6FUuqIuFOSByYe6D7iow-DwZm1Yw1gvvJaKmVWpp0ujHIrpqcKbi8RdAWzaIw-I9gwApxauKYtngjh3-4t1KEIm_L3PwclozFQP6_u08J-wTdlA3_315RoOB_ayNU_jAGlH6SCHw4seOlwT29lmJnCfjuJmSv6VfmWiQJq4KhSp0JtIi34bpyWUpQjU2DC0SoDbKTGLYjjN276u7fiR4RPsfgKCtDi2mNWuhVFulxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=V5zz59BhS7zBcbRu2psodS74JR6SL4To3M62H-1X-tBTGWANykg1f55opWZ6v2QJc709-OcGkjSr05Rcg7QYfmcyuNdffRm07xjlEPU8WnmIVT2evkG21cFmWjg_V0ksXWCSXuX3UPpyZI1DoK8RWpgDT81A9R2rfKOlF-kDSFgS1HtpSwJ0f2kaMyaDilrRzACEVPF3Cekwht3rKLmuy_FjypH2vpiANHNlwDx8FBS0hDJ5CvfYx8jrp6mc9RgC1PkpL_ngxg_6sWoBAxP74IcLrcCHEvw8iyKNyked2A58nucgJxpI48er8QK2qLNV9hiP3BsTIJ06To8V6bLWIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=V5zz59BhS7zBcbRu2psodS74JR6SL4To3M62H-1X-tBTGWANykg1f55opWZ6v2QJc709-OcGkjSr05Rcg7QYfmcyuNdffRm07xjlEPU8WnmIVT2evkG21cFmWjg_V0ksXWCSXuX3UPpyZI1DoK8RWpgDT81A9R2rfKOlF-kDSFgS1HtpSwJ0f2kaMyaDilrRzACEVPF3Cekwht3rKLmuy_FjypH2vpiANHNlwDx8FBS0hDJ5CvfYx8jrp6mc9RgC1PkpL_ngxg_6sWoBAxP74IcLrcCHEvw8iyKNyked2A58nucgJxpI48er8QK2qLNV9hiP3BsTIJ06To8V6bLWIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClhWrn-FGMMDq-kAP-TV3RHHfe4P51lNHNkKH4ZNKHUDnugHHw4gO8kmTZLNkXeaMeM-E9y4fRgYrPNpSmXawfI815jz4IMp-nH1izTGlKmBz8M32slAq4cURtwZ6f9qYSNiwPmY_qo-ImDkO4URfCSJU6K2U-F6NZONlYLfFEILtPB5GoNBXbDaQukyjgfLZsCjpqJiHeWKVEG6iLUg1KQq5ax7PA81Rd7KcqFD0J_Tao-nZstpBtppAnW8Xn5JUGL2He47mCN6fU3evibEPWFxnSmc7fAZ6TZjR35trJBXmXe5BlJrW1ieobTdDKE6VAGj1OKfpw1apwYbYC2_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=Edd6wj8-GEng4i0NpOmQtmHyatWGv_5WLcEYJFLm-xFMaS96Ra17ffAHqfUlWlOJiytmKsBJaYlqHB5aSDnbKlj3hKAKYvFN0Uh0r6CmVbvoOlml2QMFjwtbljnAdzkB-emvAnQLBD-CG2jwp5zQ4bsOtijCMUG8Q7uz1TBsnrRWVOZ9r4fFeZRizZ2aeLqip2EAz-r5ma3T04I3vj0ocMxh3MnAdOaurww0Glyyg15mkt7tUhI0yfHYSPckEqJwTs5q_Pf09IAFWeXk82N7woNnzspEmRS2g1mfaDE_7TjH97XJlG5s7LSvc1DeFLYep5WrGzNfLH0DUhfUXpX_Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=Edd6wj8-GEng4i0NpOmQtmHyatWGv_5WLcEYJFLm-xFMaS96Ra17ffAHqfUlWlOJiytmKsBJaYlqHB5aSDnbKlj3hKAKYvFN0Uh0r6CmVbvoOlml2QMFjwtbljnAdzkB-emvAnQLBD-CG2jwp5zQ4bsOtijCMUG8Q7uz1TBsnrRWVOZ9r4fFeZRizZ2aeLqip2EAz-r5ma3T04I3vj0ocMxh3MnAdOaurww0Glyyg15mkt7tUhI0yfHYSPckEqJwTs5q_Pf09IAFWeXk82N7woNnzspEmRS2g1mfaDE_7TjH97XJlG5s7LSvc1DeFLYep5WrGzNfLH0DUhfUXpX_Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExMQS65U1udUV7h7mkLBwoPUNRkGCbRaqz9pWmKgFB98zhU3aZ1ySugm-YLuIDI4SyWs-reTqxXHihRlLzyK4tWvvVQSk_i44Ecsiu1JBxEtyG6J3LeicEvE5COF0hGVfXEE8aryJ0sw55DLTc3ctPJf5gPSCdfVwKd9iIUBcMnWyQHTxNnj1Bu2bN8DZqMAaU0NU9qnfqj1ICSN-Ha3BlsWF-eV0q-Jyo48rWuRqwwpDk01DaC-W2d1mCIqiI5hDIIILyi5q7PO6G7fdkbA7ztuDDGQ3ZPK-WFd2PNSAlJMByFpVaNceghPn4k2Vj3M_d9gj9v2mkO_JLygkQrvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=lxF5iG56QAHRNXObqxf2bfLA26oiCUZoV7M1GGHyDrAjD1KpdCzaFS0QzRVhzFX_RklNLN6hllTCwkVucD7IhCjh6SnNr42aR9TTNVod5fqhwAAUVl_e5iCyy4yZptxTX4slZjr6Xby8Fj58EJsD6CBNPxXR-bLsNTska7hC2ogS-l2zkBhWB5WE2uRGC6q7MfDXs7J_NJRQdW30gvYwmJIVWHX-G5lr94SAWkiEpOnsBvZy2gRMdPZgm8L72P1SkTw7a9cT682PWXVb27aPoGO_jUmGU8vvdlL_jUfpNVgen-5I0tAvross9cz1IH9Kr4KXPXdwYNPWl9zJD1IKfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=lxF5iG56QAHRNXObqxf2bfLA26oiCUZoV7M1GGHyDrAjD1KpdCzaFS0QzRVhzFX_RklNLN6hllTCwkVucD7IhCjh6SnNr42aR9TTNVod5fqhwAAUVl_e5iCyy4yZptxTX4slZjr6Xby8Fj58EJsD6CBNPxXR-bLsNTska7hC2ogS-l2zkBhWB5WE2uRGC6q7MfDXs7J_NJRQdW30gvYwmJIVWHX-G5lr94SAWkiEpOnsBvZy2gRMdPZgm8L72P1SkTw7a9cT682PWXVb27aPoGO_jUmGU8vvdlL_jUfpNVgen-5I0tAvross9cz1IH9Kr4KXPXdwYNPWl9zJD1IKfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=HMt8ezLL0LqHhLwxBgxtRJL1ZZqbHe9rqpn9UW-8TAHmoppk6uX-rhzCbpVVcP_BA6_Nkw11LwGhhyjeNFzLt9a67_7Ia4IC90Bo_lH9dEf0JsfpmukL-W7e3yVdvFFUrzFKC11bbdeNbeAqPFKUG94Hu24094AVKI-0BPhsRss9gSjNw81v-l3FzgbfkMPER1IBOUAIpbSn2gBp1HU8mK6Ybq8f0t1UpOqL_wHx0OqUNKLPQh_HT_BxbTA6O3xjyQE2xpFhK83LsRle6efRg4eXSNP5N4iKyyDBrN6cDOO5mbw5I15XXcXM1ekyTxdK1YC8YQnR9r4Ei1CufcNTSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=HMt8ezLL0LqHhLwxBgxtRJL1ZZqbHe9rqpn9UW-8TAHmoppk6uX-rhzCbpVVcP_BA6_Nkw11LwGhhyjeNFzLt9a67_7Ia4IC90Bo_lH9dEf0JsfpmukL-W7e3yVdvFFUrzFKC11bbdeNbeAqPFKUG94Hu24094AVKI-0BPhsRss9gSjNw81v-l3FzgbfkMPER1IBOUAIpbSn2gBp1HU8mK6Ybq8f0t1UpOqL_wHx0OqUNKLPQh_HT_BxbTA6O3xjyQE2xpFhK83LsRle6efRg4eXSNP5N4iKyyDBrN6cDOO5mbw5I15XXcXM1ekyTxdK1YC8YQnR9r4Ei1CufcNTSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaaO9Bb5K92ZRIXNDyFCR_jmGmq53L0_FUUMlkV1eCc_CpC0jD50ohcZxoaccN3nUfvXqXtyUBEgK9XEsYOEod_4zoJNtIwQR7Ngi3kn9U_oC7Cobs9RJJwfX5eI1QHsVymw8lOKYZXDNHXN0iAV0KIcWNSntZgZWOlyO_PM7GxPMv4lkdoEsMEkrUWitg84iX9SFc7sq2hBqFq_KsGlXr1utleDMdzzJ8H-IfbHHWnLz2JZU7dLmE_275RDXe88UU6ssBnlgpfnaekmDtXUfucpMoIqYlEkbE3_IvmEVtrXfJlXVdBgC5LxxseeekhGUyEpIHcBEnntQdOr_siWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhlM93sT4AHL5XXCbEg4rfrolHyPfrFGG0k_pxpMQfk-DYB8VTFOvsDJKu84V0omIxMzZ3hoAEyzFDxdSKUJmLIKkXlppG_BiMVfr-1LGOKALNNI5IBDTP4yYe73Im9QrvfY7NbNj4PWYpktWHXwVbEYe_Gm1mUKbAGYNAzNBxthMyKnWR7ccBd1zlvaJ4hCM3aZP_x2YX-_vPkw8eflcCNxgLmvHcATNHf7-ooVX__AtA9YodhT0EgS4DycCpk2AVWQpr8QpvsvWRTJRRVzqNRauZYkqgfBFh2kJy2CxJu4PvV76yIDlgsN4rCBv1w2COhw1nO41fIPVA3MTk3qyKh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhlM93sT4AHL5XXCbEg4rfrolHyPfrFGG0k_pxpMQfk-DYB8VTFOvsDJKu84V0omIxMzZ3hoAEyzFDxdSKUJmLIKkXlppG_BiMVfr-1LGOKALNNI5IBDTP4yYe73Im9QrvfY7NbNj4PWYpktWHXwVbEYe_Gm1mUKbAGYNAzNBxthMyKnWR7ccBd1zlvaJ4hCM3aZP_x2YX-_vPkw8eflcCNxgLmvHcATNHf7-ooVX__AtA9YodhT0EgS4DycCpk2AVWQpr8QpvsvWRTJRRVzqNRauZYkqgfBFh2kJy2CxJu4PvV76yIDlgsN4rCBv1w2COhw1nO41fIPVA3MTk3qyKh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZNPviMcXmHYW5Wggupitk3KV3j1WjBMfbCLy_kJ0gogF_PpfhyVhCQBR67Ee8Q594Egrcw5TCnis1d89QJ0aexR5d4Wjmklj3bqSXKQ4qqpI_sVL4sj43TWxP_9eGKi14N5u0oGiZQudAO4-yew78NaE-OrGRXtiIpw3RxOvAyut6D9iWicWVq4eBWxa9Z4o8E2bu9ns9dzNa_hiqXt_BOn3hVuIFrb7jwnNAcQxN2yJK7BAeNyLtK9909kvdTdaY911jcLyMT80wJGUhIMv41Ei8xi8mUwmG-ojHD4r5SVLp7CqGu8MDzK0xtPADeLJUW3vo0N3Bf5NunraCU3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AYSQ3k7B5c_rImxvlfgY5kRnolworEGMWDSvbR5DNLcpG3R0dFGOVVlOJVrhHqaCA2omtBgmcaGNzDykAk8ylVIhk6Gz04sh8boqEMsEs8u38_RVf6AvDQIDsMT9YeVqTFTXB7Q_EyzR-SfQSfYXloxzeP5THB5zqZ1y2bAZt6QhHLsAu19jg4MtgdiC1u96aEgqIUw1f2ic7OVszaFgZBf6E2SxQcJ0GvGbmEk_1a5CP22YuLarUIZrksy5DEUIy-FdYiGHAuRUfbe2HLBfsBOxw-9L78xBLEqtgLftD-Qwqae7R_2vGnAMr9ZIRQUtJIwQSlWN7YTvcgSxz7gSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=RJMtj3UtkJsEOaQx0YZyqY-8-YpX8vWApNkBizEEaw1NzhNgYQtsRD6-IS9L2O7m_dKRDFV8yB9-ayxYuGqjaX0oJTm3YasfBOrDOzGMQ54DtTknfKE7mpc0FuGAtFatjNdiNMqhkwXxgVQRWgQNsm2JP5tNhB_rw1lGtE1Yui7YmSVAtWf8YfV-FTX3IvgJpXeErrFVCv00h3IMn_GEPpEyCapmp3JNR_bYl6ylBo65KlAjbeUsubS3SMUMLp6tbT2030p1wDBTD4_UAkrAo12k5nP5T8e3L4IsxpRBN1VGEnl7dRB8s_Z4hD6zGx4QyBwZtP_kITDSke7FdJGmrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=RJMtj3UtkJsEOaQx0YZyqY-8-YpX8vWApNkBizEEaw1NzhNgYQtsRD6-IS9L2O7m_dKRDFV8yB9-ayxYuGqjaX0oJTm3YasfBOrDOzGMQ54DtTknfKE7mpc0FuGAtFatjNdiNMqhkwXxgVQRWgQNsm2JP5tNhB_rw1lGtE1Yui7YmSVAtWf8YfV-FTX3IvgJpXeErrFVCv00h3IMn_GEPpEyCapmp3JNR_bYl6ylBo65KlAjbeUsubS3SMUMLp6tbT2030p1wDBTD4_UAkrAo12k5nP5T8e3L4IsxpRBN1VGEnl7dRB8s_Z4hD6zGx4QyBwZtP_kITDSke7FdJGmrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=Bk9c1d4bwuUmJqCZBTkbxdgVewNF_cr8m1qLv5EjIMv3KrfNKae_YF0VnmKCk33SyZ2AqgjvUbyogArnjCS9TBVZXuxbCLqTgOiAu1ssUL5l-sQ2YdhND5iTOqWMpfRheAO4-NHniQU4hDRMWPE0VJOEL4Vbww_Td_qWZriPxgcvlikjSWgHNL7e_mHQM0JHaXz4h1oqfyzwL78Qo0eRVWlCgchEF7z5258DBS3urdk2Qnh19yuEW_Brs4J5Fv1JURKydCyqVftI3z9QXmZWZXEz6L-cgTWLM45uNl91Ex5jn0GdNESHqPk14-UXT9WbiVg4xHmI5q1fQuqfEXZhQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=Bk9c1d4bwuUmJqCZBTkbxdgVewNF_cr8m1qLv5EjIMv3KrfNKae_YF0VnmKCk33SyZ2AqgjvUbyogArnjCS9TBVZXuxbCLqTgOiAu1ssUL5l-sQ2YdhND5iTOqWMpfRheAO4-NHniQU4hDRMWPE0VJOEL4Vbww_Td_qWZriPxgcvlikjSWgHNL7e_mHQM0JHaXz4h1oqfyzwL78Qo0eRVWlCgchEF7z5258DBS3urdk2Qnh19yuEW_Brs4J5Fv1JURKydCyqVftI3z9QXmZWZXEz6L-cgTWLM45uNl91Ex5jn0GdNESHqPk14-UXT9WbiVg4xHmI5q1fQuqfEXZhQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=IEQJDSEQAgm1_gzARBsAskm06pxLiI5NYczkTyaejEDhEwjdGLu33X6aKydi5ZCy8IRjjm0xdzZZv6dPOq2GSq4zrOsETuS8nuN2X2zXi8MWbXt3CzItSd8a15HXhqLxRWc_OQpAWIhpI2031RkeRCDF4lV_zuECq1Q0C_fLQyN9fpLfJMIHBUAZGWbv3HZQXw-XM_JtWbuLq-8wL8EiMBxR7elPXy0ZyUyxSo9TSyvd8FNjiK92AImfm-FVUpek-hsjBTeG3S5lNqlHEnNJjOdkjuXnqYejA29b5c5aaLBWSNYvqcU9hEHrbBM5txlavxabC1VGda-Ct8j36ILe_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=IEQJDSEQAgm1_gzARBsAskm06pxLiI5NYczkTyaejEDhEwjdGLu33X6aKydi5ZCy8IRjjm0xdzZZv6dPOq2GSq4zrOsETuS8nuN2X2zXi8MWbXt3CzItSd8a15HXhqLxRWc_OQpAWIhpI2031RkeRCDF4lV_zuECq1Q0C_fLQyN9fpLfJMIHBUAZGWbv3HZQXw-XM_JtWbuLq-8wL8EiMBxR7elPXy0ZyUyxSo9TSyvd8FNjiK92AImfm-FVUpek-hsjBTeG3S5lNqlHEnNJjOdkjuXnqYejA29b5c5aaLBWSNYvqcU9hEHrbBM5txlavxabC1VGda-Ct8j36ILe_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=nNmGca93CdEDC-6ZUpL4FK56vcLfCVRo6Z00Jhap3iFwFANvu3ydIHRuh-4DWlOsHJ7sbcsJgaWSkhaKZ5t3b_fBM19fYFXlzVqhGzb-LYK5a4VZ9Xi1zvY6OMSG_f25bFmZAkHvIgHK036OYNeil8iRVCuwPGOSxdy3WAAC6ZmBFBxhrWmwRIfvVKV_8lAjtbmCMLA28-jtpVRJhPZmSzSzfu9hJl6RX8ky-_GYVd-gHyP9WZqzH7GQ0LKNl0kGt8FujO70mlJUvQgdwrnFbLsGdpyXw151pNcDKtxtfnekns0PbCU1_xCB7Xl8ohFWBtzgLybp0mXvDvKvkxE3Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=nNmGca93CdEDC-6ZUpL4FK56vcLfCVRo6Z00Jhap3iFwFANvu3ydIHRuh-4DWlOsHJ7sbcsJgaWSkhaKZ5t3b_fBM19fYFXlzVqhGzb-LYK5a4VZ9Xi1zvY6OMSG_f25bFmZAkHvIgHK036OYNeil8iRVCuwPGOSxdy3WAAC6ZmBFBxhrWmwRIfvVKV_8lAjtbmCMLA28-jtpVRJhPZmSzSzfu9hJl6RX8ky-_GYVd-gHyP9WZqzH7GQ0LKNl0kGt8FujO70mlJUvQgdwrnFbLsGdpyXw151pNcDKtxtfnekns0PbCU1_xCB7Xl8ohFWBtzgLybp0mXvDvKvkxE3Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=THnUG5SvW839sbaqHON85-6qKiSWNkTFBCddQfQkR5M0qYnCGN4Vd-H0LkwihtNHbJWDhla9Db_nTu2lIrdV3FFiqIKfVlQP0TYW33_8e4GCCdinSXo-t2xKc3qaSJM69VEtMhhJ55sGZASQbnAZLTGUIQW4Hjb7z36lrzGTtoPhE52N8J77Jd67_64blRNrmj8fEJXx0HWStbTLuqbVtIqxO9s6OQ0HCgz10zxwuwJFxzRUpjqY73CsmIPyUy1JKb7jlrLNfXoZy4lun3OGOv5uB7mtbPCSc-M3YVTxUaeLFuse5Ovtye6ROvSL-PDq9cm5x7E_oHJ7CP6_TVJUE1svQcqol4wK4LsNlZIK915iNX8Npx0A-_gDiasNXh_-MoqhsyZzRwU1qZoOM7c_5ZaMZpdB5ZJzq2r7AMvfBvyvMsnprWpB8BVIGf82xsrNPctpTculVwU2o-5jvXqe-Beo_H_DabaGvNE049zBbFNKFcZyANPyHVyIYM0WFCAJ1jBBqgItS8AEJTgQc77huGWmxJHB6doj_VDJJZhP04uEKSzYBAokh7bNMREpmxmW2DFhoVPQhzIQQLDMcdMhTXLHkiQ1giMNfBLoLFL3SJpQqE2jFNvZrxwQe3mDUzvUsEt6dqZJrkczt4uFyaTo7-IzqDiImZ17pbLq1Gew6dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=THnUG5SvW839sbaqHON85-6qKiSWNkTFBCddQfQkR5M0qYnCGN4Vd-H0LkwihtNHbJWDhla9Db_nTu2lIrdV3FFiqIKfVlQP0TYW33_8e4GCCdinSXo-t2xKc3qaSJM69VEtMhhJ55sGZASQbnAZLTGUIQW4Hjb7z36lrzGTtoPhE52N8J77Jd67_64blRNrmj8fEJXx0HWStbTLuqbVtIqxO9s6OQ0HCgz10zxwuwJFxzRUpjqY73CsmIPyUy1JKb7jlrLNfXoZy4lun3OGOv5uB7mtbPCSc-M3YVTxUaeLFuse5Ovtye6ROvSL-PDq9cm5x7E_oHJ7CP6_TVJUE1svQcqol4wK4LsNlZIK915iNX8Npx0A-_gDiasNXh_-MoqhsyZzRwU1qZoOM7c_5ZaMZpdB5ZJzq2r7AMvfBvyvMsnprWpB8BVIGf82xsrNPctpTculVwU2o-5jvXqe-Beo_H_DabaGvNE049zBbFNKFcZyANPyHVyIYM0WFCAJ1jBBqgItS8AEJTgQc77huGWmxJHB6doj_VDJJZhP04uEKSzYBAokh7bNMREpmxmW2DFhoVPQhzIQQLDMcdMhTXLHkiQ1giMNfBLoLFL3SJpQqE2jFNvZrxwQe3mDUzvUsEt6dqZJrkczt4uFyaTo7-IzqDiImZ17pbLq1Gew6dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=sySTOETtKvR6hXFDKTCbDNVZTonxQIL1vROUOAmvFOSfgIUQuEEAatRgaEP4ISSDxKoL2S_6ImJSM2sYmjl024BFcOtu0NK63JIfanVl7gpz2fA9M6eyWE_CzyA5ctDhcb-u6yed1ZFyBM-qXBq5Vm6GL1PG2Mhfp9Z4mTjWQ1U__es8GZDFFg3lGj2C3wMgzA3txA44aJd4mPSxGYkNu1nGfgKS4zkotYPqhzIith0NN403pK8aOtZKWQn6TZSKU47SsHUSEHctdIdJkss6QMLiolDPpLYiBdRnJCDsEv0ufjNefqbU9TgHgiZGCPT8BY2ERMvcDaIjuCFRn6MexQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=sySTOETtKvR6hXFDKTCbDNVZTonxQIL1vROUOAmvFOSfgIUQuEEAatRgaEP4ISSDxKoL2S_6ImJSM2sYmjl024BFcOtu0NK63JIfanVl7gpz2fA9M6eyWE_CzyA5ctDhcb-u6yed1ZFyBM-qXBq5Vm6GL1PG2Mhfp9Z4mTjWQ1U__es8GZDFFg3lGj2C3wMgzA3txA44aJd4mPSxGYkNu1nGfgKS4zkotYPqhzIith0NN403pK8aOtZKWQn6TZSKU47SsHUSEHctdIdJkss6QMLiolDPpLYiBdRnJCDsEv0ufjNefqbU9TgHgiZGCPT8BY2ERMvcDaIjuCFRn6MexQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=AmJlnrJ2KF1uuln_bSXDOxSzCEuj5XAvgkxZFvY9BNTQPFDOHem3QJJNfrpIQijfyac3YQxCHPaj2RC7aixx-6J9AFu2l5dy7m4CSjWuIg8clfru2plfDteFLSzWDV5hqCHNQ2EA9DVCzqSMEYCFheD4n97UJaufO7aECsQi9Ld6Tzmq2pG6eYSROvROW5UCmjBBp5jCvF2wZmQQjvcSIRgfd_aALJGP3BFF0P0BbZJ_5_LkfLRgadr689BdE1OmcAjqpMLVB5ihaxP-3sOWlQ-2eVJMp_VI1-TukgtNpV6LP59bMUwlIfyYEqjqeK1jzA6H9RFN1b8ZvsdJ2W_P3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=AmJlnrJ2KF1uuln_bSXDOxSzCEuj5XAvgkxZFvY9BNTQPFDOHem3QJJNfrpIQijfyac3YQxCHPaj2RC7aixx-6J9AFu2l5dy7m4CSjWuIg8clfru2plfDteFLSzWDV5hqCHNQ2EA9DVCzqSMEYCFheD4n97UJaufO7aECsQi9Ld6Tzmq2pG6eYSROvROW5UCmjBBp5jCvF2wZmQQjvcSIRgfd_aALJGP3BFF0P0BbZJ_5_LkfLRgadr689BdE1OmcAjqpMLVB5ihaxP-3sOWlQ-2eVJMp_VI1-TukgtNpV6LP59bMUwlIfyYEqjqeK1jzA6H9RFN1b8ZvsdJ2W_P3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXyMfml7wSeX9LE0DKz13wuELt7DpNoqhZ9Bmpw6ijkwFnKZ946RfPG9qsi9D5Ox3mEnYOXQ-6sYNm3W_UTC1BjY7wa5MZr4gNm-ZpSpgovEIwx_NNN87SlMJfN4APtisgmiFcc-f5g4Jz0j193icqHIcCOU7TEmHmbjGB42JmY8wRSrdPcJ6JV4N3_29EbtNYpFiKmGMvOr7QLY3rN25KyRlZoCrFUROREveEEvbwRPG1KSzmpiHWaqqxzWTVB8gkOx4wZA4h1tnSX-bdkc1ZAFY9PaGqALnaokJ8sg-xFWMXivPZPDSjn68WXG_aNlym6tfzVpNL-Yh4kau5M7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuWTIcCXPamwXyGOeweQSOgVT7GORk5D7kJenSgCaoNoM2eJF6j2tyB2Pii3_8m56dp-72RjZUybplqhwxwngyLtv-bbP3qdZutki4idAaehZFVmqYhnnSiTlPsbNztN_GT2y5To7CDck9lFxxa78pzxP2IAMQ1dQKJlaU7NncVXvZ_GQA7v_GECMlfR5WkLU4LYJFcg_Bm_THf5OffZcWLQZb_zuDiE6AkcdBllZbpbyUGuFgohxUGA38ZLo_S6KZMu2hBMcbtWqSWu0-gpxZSsirh60rfNRBNi6j5UUeCuNDYlkS1uKkm_S6Uz8eJmD6h1ieplXHUDJs2fbt9_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=diArCf38yIBVJQNWy9GkpM2syqX6x09PDOgTWtMiTttVhTFmlg-fiOHbPjbeXPCyRqED9A88p5rMJ-Gfa6cy1bLPR-aEuNNoe-dkk8KcgtzoC07qG87vJBmieEk3IqmV4gTNsrctVgKnIK54zKW86pylykBVNdER2fv4AMvAwoe35UknsDSFx_lugv1a6NZ7LyUVZsFRywHS4KaovOO46FxRC7f-w_Pei3nJt9aF4EqhRCiD01BN2rR0odZ3_DY86kQJMPvxS073Hu5Xmd1YyP9a9MG_v4PrMicP0QNs6IAr14ppvlLJ9BznzFEEXDdamfEQxmL_EqOMIFNB4ELoDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=diArCf38yIBVJQNWy9GkpM2syqX6x09PDOgTWtMiTttVhTFmlg-fiOHbPjbeXPCyRqED9A88p5rMJ-Gfa6cy1bLPR-aEuNNoe-dkk8KcgtzoC07qG87vJBmieEk3IqmV4gTNsrctVgKnIK54zKW86pylykBVNdER2fv4AMvAwoe35UknsDSFx_lugv1a6NZ7LyUVZsFRywHS4KaovOO46FxRC7f-w_Pei3nJt9aF4EqhRCiD01BN2rR0odZ3_DY86kQJMPvxS073Hu5Xmd1YyP9a9MG_v4PrMicP0QNs6IAr14ppvlLJ9BznzFEEXDdamfEQxmL_EqOMIFNB4ELoDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=Csd8ewujGEwxsSis3ZO4JwwtLosp4wiNQA6_jp-sdryo9o-_UvAxAZ79vMwYbWi0TghFRRNXjszIfLMDSegWJKJB-H8irbVxBIqwq4LX1KuzcTP_u-9IRuQPto8XMO5HhzvHxNqTuK8xi_3zfzyAB_UVI8dTbiOkUe_97lFwfqEh5QWxqMmSchPAbnwgdQz2AsYC2C251qnXNs2KeuhAzoxdRljA-MGHXdKpTA9KQRrpvl2tHV7kE_GZPxf3TQB16pwcNs3wt4G9zWnxR8Mizjwk_psXZQigsk7nFp-gTPe2fpHNHi2wBtce5wpWoF6Q-uFg35AK6RRHIvUgsp8Rhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=Csd8ewujGEwxsSis3ZO4JwwtLosp4wiNQA6_jp-sdryo9o-_UvAxAZ79vMwYbWi0TghFRRNXjszIfLMDSegWJKJB-H8irbVxBIqwq4LX1KuzcTP_u-9IRuQPto8XMO5HhzvHxNqTuK8xi_3zfzyAB_UVI8dTbiOkUe_97lFwfqEh5QWxqMmSchPAbnwgdQz2AsYC2C251qnXNs2KeuhAzoxdRljA-MGHXdKpTA9KQRrpvl2tHV7kE_GZPxf3TQB16pwcNs3wt4G9zWnxR8Mizjwk_psXZQigsk7nFp-gTPe2fpHNHi2wBtce5wpWoF6Q-uFg35AK6RRHIvUgsp8Rhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=TDN_t27FAhoCZXsjzkZ_wpKOuZ05pGCjJygw11kR1zDjtx6bhmL8Tlux2ne04fuu8jEpktDOv7GrM8z_e2_avkFJ5Si3C08F47QAqW4fAOX3pA70xGn6OiDGFowQVR-ZrNLRAHxi4DkY_7zFntKRqhsZwOHHFumXaZ_tseNi8LJO5t5Xe1kt5VYWwP_-MjGR2e2__P49s4MdPq0qy3aoeTWlxnazNETufR_GnZfjWsR1Q5FDjnSJ4JcpxIjHCUQ3ZbrnFM6q-0kk163qILbMosU95snnE6dyAhXuQthqMdQxNyV3KzlIX0SX5EfkXlPJTnV5SgEOuLSbmLdooaygtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=TDN_t27FAhoCZXsjzkZ_wpKOuZ05pGCjJygw11kR1zDjtx6bhmL8Tlux2ne04fuu8jEpktDOv7GrM8z_e2_avkFJ5Si3C08F47QAqW4fAOX3pA70xGn6OiDGFowQVR-ZrNLRAHxi4DkY_7zFntKRqhsZwOHHFumXaZ_tseNi8LJO5t5Xe1kt5VYWwP_-MjGR2e2__P49s4MdPq0qy3aoeTWlxnazNETufR_GnZfjWsR1Q5FDjnSJ4JcpxIjHCUQ3ZbrnFM6q-0kk163qILbMosU95snnE6dyAhXuQthqMdQxNyV3KzlIX0SX5EfkXlPJTnV5SgEOuLSbmLdooaygtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=glOiFD_5xJzwqrrQ4kdWpUrVH0bQfEnzTGa-YhehVhYKU-BV1Xl84vmhg9jmGdfhEyIZgU3KtU-LOuzSEydzRVA08gJJc2Pa2UTg5a6lRViBuqgFAWOfZQ_AhjxWk3iLuUdzurXTthGs1FMglfEmfcNT05rVWg02GGybou-BX_DZ4T3Q5UChzivc9nUmZj7QVguj5cazwEEHgLIcsOI6UHFsoDj9ynw63pSQLn3qOt9gZZFV7SJXGahuFwg0OZpxRW16g0LYMCDWT0T60nOY_fKW-JgVP78ZIGoqUCLQFD2uABcYn6oHpstjOLN20QYD91P3s9MvwMlA30Ols97kuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=glOiFD_5xJzwqrrQ4kdWpUrVH0bQfEnzTGa-YhehVhYKU-BV1Xl84vmhg9jmGdfhEyIZgU3KtU-LOuzSEydzRVA08gJJc2Pa2UTg5a6lRViBuqgFAWOfZQ_AhjxWk3iLuUdzurXTthGs1FMglfEmfcNT05rVWg02GGybou-BX_DZ4T3Q5UChzivc9nUmZj7QVguj5cazwEEHgLIcsOI6UHFsoDj9ynw63pSQLn3qOt9gZZFV7SJXGahuFwg0OZpxRW16g0LYMCDWT0T60nOY_fKW-JgVP78ZIGoqUCLQFD2uABcYn6oHpstjOLN20QYD91P3s9MvwMlA30Ols97kuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=Z29P9gBfkbScABiodETTqhl6JERzXUO6i_UJhPVZuN2atBljwFHJ9q5munn3-56Tp16Lobnvih1oti6uQ1VT9ZOhhYiV8WRkVQ7c9snE8olW4TM4Th8aTwWS-fHu9G_mjZI6aR6hoL6q0uLm7JOrxHOU2PaHoP9pFbPyrcEpHwZK95D_lCq42iew39N0iUypWlkyu1HqLoLhWVV_exrGxRYAqYVobbtORtXoiCAcHVFTxzI5Jmla4eQR__bHHdb2CF9H18vQvNDwJs0JZHk2tnlU1RPrh-DlM9qOOPAXaFFO5pYwvCRLRBPsKwkB9yIhxoubGfMXEh-ZWHzryEVrGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=Z29P9gBfkbScABiodETTqhl6JERzXUO6i_UJhPVZuN2atBljwFHJ9q5munn3-56Tp16Lobnvih1oti6uQ1VT9ZOhhYiV8WRkVQ7c9snE8olW4TM4Th8aTwWS-fHu9G_mjZI6aR6hoL6q0uLm7JOrxHOU2PaHoP9pFbPyrcEpHwZK95D_lCq42iew39N0iUypWlkyu1HqLoLhWVV_exrGxRYAqYVobbtORtXoiCAcHVFTxzI5Jmla4eQR__bHHdb2CF9H18vQvNDwJs0JZHk2tnlU1RPrh-DlM9qOOPAXaFFO5pYwvCRLRBPsKwkB9yIhxoubGfMXEh-ZWHzryEVrGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QSo0KrCI6EIhqiokjTmYKaTCMx15rx-0DysKB3yMHxvAEqNQV2WRtsI7EkTRQH8TO3RKPBwnS2KPEV5urHMGGlmIuz7p9BEI4nDPZmr8PP0pSt_MUycbJ3swvA47sK5Rqrm6k6hAymsOndp7zB43HJpKXfTtYLf1YwxxUpu2oY7AP4la0HRbjdyiLFV62bB52VuiUu_UAUYllIER-jMgwkKlUWI59x_QUXlvhw41y8z3IEf6lgNrEjhldJQ9ilkHE0yNndHkSIvyd2HMwskmleWsPPoESLFBINPPpk2J8ykMGmpbTqNCvmDl7mwWvhnOyeDFiaVLawmt2KamElZ91A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=t2XWzO5e-XiyzCwtosrhSlVOcHVeTYM09dIKL9hYPSoUc4xpH-fn83RiEMowHFzfC7AbwarnA2nnB18NROWU9R9JkpLzJAzRczKaC7rgQZD_IIaClXgghBWviT3X0bWS4IT5ePmPvZVtXdRow330DxNzU4DgOuPR-h9Dl0JkQHWXlq_rOP74AMpD7Cu6-l1oD1oB-oyrjpJ1YcrPteoh3SCW_qpnZoJm-t8-ytn7hnbZlI5RYz14i0wJ9qt37BY3mRslWEWmBRFFycfAUS80IOix4zwW6qiTX4TLonL8I85fPLOJ887KrYqkAOwnnma-LNyK20Q8Y_jmdNa7SAV2Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=t2XWzO5e-XiyzCwtosrhSlVOcHVeTYM09dIKL9hYPSoUc4xpH-fn83RiEMowHFzfC7AbwarnA2nnB18NROWU9R9JkpLzJAzRczKaC7rgQZD_IIaClXgghBWviT3X0bWS4IT5ePmPvZVtXdRow330DxNzU4DgOuPR-h9Dl0JkQHWXlq_rOP74AMpD7Cu6-l1oD1oB-oyrjpJ1YcrPteoh3SCW_qpnZoJm-t8-ytn7hnbZlI5RYz14i0wJ9qt37BY3mRslWEWmBRFFycfAUS80IOix4zwW6qiTX4TLonL8I85fPLOJ887KrYqkAOwnnma-LNyK20Q8Y_jmdNa7SAV2Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=OGqUNxp40r5GMsonpFuXAfTbwKhNDYtJn7Sod5se7Jg7vxvt_YphRjpl_nGdGQoEVbpb92kEBpNOELI9r7yARo4Xbz8QVOZ8fEXX13Hej6-E-CDgt7AeXDjBZPn0agJzGjxXJqXSNDtxKcRt4mi7mVRii0Rcig7WnTASivQl_4Mc13CE4rp_BtxRD_uYYAuvz9JnYwo-Rz0Wu2U44jLSl7cmdZMZYQy2Nxic0BByhqRmwg7jdyunCmQ5IgDhIlKfXyRS-wBl2NcbKQ6SfHqImU6fBg2WLsk2M2gey2cY1NUPTLgcm1qyqsOWnmjUjnbc7xSc179NndquFATDWdyQXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=OGqUNxp40r5GMsonpFuXAfTbwKhNDYtJn7Sod5se7Jg7vxvt_YphRjpl_nGdGQoEVbpb92kEBpNOELI9r7yARo4Xbz8QVOZ8fEXX13Hej6-E-CDgt7AeXDjBZPn0agJzGjxXJqXSNDtxKcRt4mi7mVRii0Rcig7WnTASivQl_4Mc13CE4rp_BtxRD_uYYAuvz9JnYwo-Rz0Wu2U44jLSl7cmdZMZYQy2Nxic0BByhqRmwg7jdyunCmQ5IgDhIlKfXyRS-wBl2NcbKQ6SfHqImU6fBg2WLsk2M2gey2cY1NUPTLgcm1qyqsOWnmjUjnbc7xSc179NndquFATDWdyQXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz2SmCVm2lp1JAGhIwKO9HZxqqNygRp70Bd4sUQA_Omfk-o66FGRfBgV_kDQ8Nqi8gfUVmEDEphyGq3buNmbJprAIjZ_2Lt7UvFIcdImHkPgIMBg2zHNRMueKVsGljuYo287H21YARflL913zMFb1LuvoDa8ieRxDiXSZxGokfoXyjJbKLjqnUa-xaDtlxLMeWgCQzY7O44_6h8YPL_GhQRiU4WBl8bUeJ0jm9Rr-g674c0GNoJFsuiy38GdARV8NPDKuzpNJ5jEB6cIg3xgJXgnIOMQETBzgHbI32R_4LlY13DYv9MtRzEO7ZfVVo1KuFwzWJHHouJwKmxZAErI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=oFi2CKJ7BDCMA6psMQ86pnPcvqt8H61cW7QzHhBc8ZXcGu011LMrA4T_N7xPHrYgPSVrUJ_QH0Ia-bhJCDiDWCoRvCPXv-AqCWObdmL3z9J99DTVPKVUtFHUSdWfefox3hvkyuBLcSgRwuGmDpPYIFbsXHOKY7MBXygxmZHSFLtYF-1usbGtYvkNsD0DDMOq_1B7ANgqNFYiMGkPeppD4S10pLpFXpcR9hNfu3J0cw6-eTL72WoMS00ev7hzCu037s7D-sDaDVv720SY0Sllx_FDYscPmr-M7lHmcQtr_Yl2byuGMutWWLGtwdn-3L6mZmlMc6p50v5p4Dd72NqQs3tzM4cfRReOk_ARtDZhm7muwvrPd9ZLy51lrXwfPPMjdJ8dG3c6AqUYJpVXAX7Zzovckb2XCqgzUoRnMAFKGPpdIJf1O8E_lY7qjcuIWx494hK49SIqYGzgvCOS7Pbu0FsQyiqSHzi4lMtI1CH7a-Mt7i3YTyugJPqBrrVq_IjB_aFZVjdPJTNhessfhSowx6ouGSAhyZMPQfoKNGV7EVyRu1MFNGaVELJTIhp25Gh-QCFa9pv9ZUXWvzkNTUtReHKwLB-byxlI2SyZOhN7jsoCx-JewE1_prRDPG3iXWrMYy9LYkIVDJJ2_fttdxcyW2Dn_n1zS-aDSBLawFIIBMo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=oFi2CKJ7BDCMA6psMQ86pnPcvqt8H61cW7QzHhBc8ZXcGu011LMrA4T_N7xPHrYgPSVrUJ_QH0Ia-bhJCDiDWCoRvCPXv-AqCWObdmL3z9J99DTVPKVUtFHUSdWfefox3hvkyuBLcSgRwuGmDpPYIFbsXHOKY7MBXygxmZHSFLtYF-1usbGtYvkNsD0DDMOq_1B7ANgqNFYiMGkPeppD4S10pLpFXpcR9hNfu3J0cw6-eTL72WoMS00ev7hzCu037s7D-sDaDVv720SY0Sllx_FDYscPmr-M7lHmcQtr_Yl2byuGMutWWLGtwdn-3L6mZmlMc6p50v5p4Dd72NqQs3tzM4cfRReOk_ARtDZhm7muwvrPd9ZLy51lrXwfPPMjdJ8dG3c6AqUYJpVXAX7Zzovckb2XCqgzUoRnMAFKGPpdIJf1O8E_lY7qjcuIWx494hK49SIqYGzgvCOS7Pbu0FsQyiqSHzi4lMtI1CH7a-Mt7i3YTyugJPqBrrVq_IjB_aFZVjdPJTNhessfhSowx6ouGSAhyZMPQfoKNGV7EVyRu1MFNGaVELJTIhp25Gh-QCFa9pv9ZUXWvzkNTUtReHKwLB-byxlI2SyZOhN7jsoCx-JewE1_prRDPG3iXWrMYy9LYkIVDJJ2_fttdxcyW2Dn_n1zS-aDSBLawFIIBMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=qiFZV8UFAOF_FZ4aOtMZgT7pRu2fVJ7QZ9AxPLsD3M48O0xCYKdO3iUPpVDSAn0VycH1a8Y2pbn5gvTnPw_x-TlRfdTimcea9jmndtsMIC4cUxeWJ6fIGHIkd7IsWzxovRKp5YuEhjcyXfzR2QDuhNaksshHoyC2iMXI_m2ia-3sEgikEsAQTcFg9oQHXEPAXwcmy14403OFsXye7A912Q2a0yO4mi0RoMB-VFoYBbD9wuK58g_adk0zkJzXL3l0-TCy21vPowFZqCzU3DSmXKxuTwOTEtYVVYr4Nab4s6mA2aD4QXFsdVfo1vltvpAZwp3wDmYEfKx471ehTBv-4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=qiFZV8UFAOF_FZ4aOtMZgT7pRu2fVJ7QZ9AxPLsD3M48O0xCYKdO3iUPpVDSAn0VycH1a8Y2pbn5gvTnPw_x-TlRfdTimcea9jmndtsMIC4cUxeWJ6fIGHIkd7IsWzxovRKp5YuEhjcyXfzR2QDuhNaksshHoyC2iMXI_m2ia-3sEgikEsAQTcFg9oQHXEPAXwcmy14403OFsXye7A912Q2a0yO4mi0RoMB-VFoYBbD9wuK58g_adk0zkJzXL3l0-TCy21vPowFZqCzU3DSmXKxuTwOTEtYVVYr4Nab4s6mA2aD4QXFsdVfo1vltvpAZwp3wDmYEfKx471ehTBv-4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s99_QwgWuhC_tMXDR4p759L0aNe6rh6AjusQ1uCxmiH3DZIQ4YVOBvS9N-7f3ufpONBsyP1f-OCh2xFmbFSUY63yKZXpAaQnFSQqb6jdaLsBUHvfBtplTc-_rLLMZYbgHfIpbBpzP__Ti0x7B9vgGNiXog5c5yn6IkrZIeO32ITagDVb74tEOVut2h0i17borRgxfoT7NSPVwF4ROgXH7dGj0Sg7AlfDF1J407jg8tvre936OWv8d7zT7GfLMviB07UeJfW3T95S61qP0A2Jqhlh9UFrA6UEblFgXLImTgS1qCKMRm0426r0xbeXFplnh_fk4_W7AM9SsRipA9hQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCJwXdiF274eAwuTAWzXgx2id632WwHdSpDr_Iqp8IEhmpfMop4a1TQb--z1a5NLKazmQ21J1Nzdul6_alcDnqdB3vclUC6UF2pA_4M_xOv7F03jrYci8uSNqQyJ4ApHM4JQcT8WfL29QcNsfRH8hp0kot9mYfcjRt2C8Rmmmm0UP7fH5KiNo0wfiyOu0fT891v18Ulw0LXWLtB7ZWxbhm0YACuHWHiXtoDXnlt3SJGlUEG-e8wWvpRxlu3Rvn04SPDwYOSKInx0IhxRvbN0Aei-wkkSAS_4Uus8vME0Ng87sgI00dmbeMznrvyx9bpY_QTYAC4XgHzxRWsnTCi07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=jXgmdM3qhZFTvctHqEMaB-6bfnvyYhQzy7yQrZW3i62_JS5tb8C2P4Jpc9QNfnnEi1-KshgY-BUqpdBXdkVBVr76Zyv9fUrOWXeNbfPEtJskxAHToscLN7ciBJ0B6x9aAccxwwGcdYcYMrVdC0tUx1i9d3GYydzKTCuJvydOWEa9xuSu5aMt-D_-wBNKtyhFTHKLUHNi7oQ_igb39Fzgw9b28P_t2AvxEHchu60kq6s5Mw9WqgcyiMwzEN6p4X74NfLd66x6c0xFKNUDBnsgqQmoCCyCkUA-VUB-xbjV6e0l2ycrm44JVMoooRDKClDPpc19F-ESoxu3sFU5g5ipmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=jXgmdM3qhZFTvctHqEMaB-6bfnvyYhQzy7yQrZW3i62_JS5tb8C2P4Jpc9QNfnnEi1-KshgY-BUqpdBXdkVBVr76Zyv9fUrOWXeNbfPEtJskxAHToscLN7ciBJ0B6x9aAccxwwGcdYcYMrVdC0tUx1i9d3GYydzKTCuJvydOWEa9xuSu5aMt-D_-wBNKtyhFTHKLUHNi7oQ_igb39Fzgw9b28P_t2AvxEHchu60kq6s5Mw9WqgcyiMwzEN6p4X74NfLd66x6c0xFKNUDBnsgqQmoCCyCkUA-VUB-xbjV6e0l2ycrm44JVMoooRDKClDPpc19F-ESoxu3sFU5g5ipmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=IKfn8BiaXeORLHt1vPOAdjYEuu2oMKRczpYSG0VgTj30E2hZduC2X6HCF4mo8tB9Yr2tKxr2_1i4vetnJqymKXujuHr3VPPBR4lxKe_uw2q67CpcIVBlxvzpJWT44sXU2guqI7DXVBR7cNxSoqvFhQEpRp73M1zKIJNc6CT6s3Otorzgqq_y99qoQvKWjf-UrSwcev4wd7sPA6wssZ5kaw7raNI4zx22P_j4CeWm4kImHTp4mBGatQjDA-rmVFX6V-OThbFeuaN2G_ymIbwbKvHcL2i0V293VAvKpesvu3Iy34alJ4VhuXOyeRTFPMialm_AXamb9P2M4FlaCyj0gg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=IKfn8BiaXeORLHt1vPOAdjYEuu2oMKRczpYSG0VgTj30E2hZduC2X6HCF4mo8tB9Yr2tKxr2_1i4vetnJqymKXujuHr3VPPBR4lxKe_uw2q67CpcIVBlxvzpJWT44sXU2guqI7DXVBR7cNxSoqvFhQEpRp73M1zKIJNc6CT6s3Otorzgqq_y99qoQvKWjf-UrSwcev4wd7sPA6wssZ5kaw7raNI4zx22P_j4CeWm4kImHTp4mBGatQjDA-rmVFX6V-OThbFeuaN2G_ymIbwbKvHcL2i0V293VAvKpesvu3Iy34alJ4VhuXOyeRTFPMialm_AXamb9P2M4FlaCyj0gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=qwa2lv1xtj84t_N3U6yKqg_VLmMprJgd5Hdrk2JAwSD7ugx_tjsv7tRAP2NeepDlXl5X-L23mtITS8Gllv9UP-j07jtcSn0iUHrALkyTKEobCHKmTl5ju7ZdR6OWSovXTDtoSJ9V8d5AhQpnys0FtrIFasb_ix_UtxXfXqckG0bITSXO99Ll7swCBxO-WsH-kR30rVwpLKC4GBNsIShDx_UvoEQGWWw1-BpXYgh-6QMFerAS-nYlbqNudK6KIGf15rC0encjHIv1VyAowxS2Wx77pBDNevXoNxWSXwgO0agaD2M_qGZBGW6J8o095GCMYeXCguakofzCZBGyQHybWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=qwa2lv1xtj84t_N3U6yKqg_VLmMprJgd5Hdrk2JAwSD7ugx_tjsv7tRAP2NeepDlXl5X-L23mtITS8Gllv9UP-j07jtcSn0iUHrALkyTKEobCHKmTl5ju7ZdR6OWSovXTDtoSJ9V8d5AhQpnys0FtrIFasb_ix_UtxXfXqckG0bITSXO99Ll7swCBxO-WsH-kR30rVwpLKC4GBNsIShDx_UvoEQGWWw1-BpXYgh-6QMFerAS-nYlbqNudK6KIGf15rC0encjHIv1VyAowxS2Wx77pBDNevXoNxWSXwgO0agaD2M_qGZBGW6J8o095GCMYeXCguakofzCZBGyQHybWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6h1eMi49YKcU5BUlhEoDWNRPtwAhs07koKO1YbQ4LzOx39bZHwkT4YC1JK-Bo4fqj78Dh3nBtb2VgvQOHOqfooTQM-rDsnkUvpUKchj51zj5HH6-SuHAcWcK92W8RNkefF938cMtaoL6Kfha5zJV1E0wJyyLUtK0nzJo9LQ6n-VxHGdiLlpOnvx4VSgQLqUt615I5MnBFVkJ8SROqTA2X1v06hcZVaSMpt9mmvStj-wDRTndkKPhywa3VbkXK3FpdYJS3QAb2YIgQHTsq2bM52SuGqnfisaLyEhhCoKW1XbnfvkTmZaPht6XAhkxrROkxPRSBu758AphHLtc8Ti7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=aqDJV-Z4inRbofSx3CABkW2nBWPU6aUvN60a-6_szhnmyqvwAMonAhUf_38qE9fSDnlCxKoe67z9zCvR87X17ooEULgIDmO9bRcdP_PGPB2vcwRrtEjNKRFyjyM6niBN8rh1G25TtpYAP4CIoiDw3P55BRJJ6Qk5iaNzMwila-YN6TD1sBH_x-9KvA-Mog25NTWbK_GhR3x68RqMkOJcb3LwhD-i7vP_ow0PMeB71Q8URermsovnW6TzdMGniuV9cKB12vdHnR3wm8tY2Vion3jOA0BkDK3L3othevmmgD81LimItd2TupSH07V4eATNZVPPOQZsFnrYJHJF_gNw4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=aqDJV-Z4inRbofSx3CABkW2nBWPU6aUvN60a-6_szhnmyqvwAMonAhUf_38qE9fSDnlCxKoe67z9zCvR87X17ooEULgIDmO9bRcdP_PGPB2vcwRrtEjNKRFyjyM6niBN8rh1G25TtpYAP4CIoiDw3P55BRJJ6Qk5iaNzMwila-YN6TD1sBH_x-9KvA-Mog25NTWbK_GhR3x68RqMkOJcb3LwhD-i7vP_ow0PMeB71Q8URermsovnW6TzdMGniuV9cKB12vdHnR3wm8tY2Vion3jOA0BkDK3L3othevmmgD81LimItd2TupSH07V4eATNZVPPOQZsFnrYJHJF_gNw4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=QiGUuVsug1ys4FUjWyo3_O69DF0CpwhthlYDoDycWLIbwQNxpHluRlkaQ4JqaGM3QVw83-qjy44Cxz5uKiO-n25feHNRX_h9zHoP1UYVCZPCCiwBm1eu41u_8KyM8mXL0nfOOIcxk5mcKlcqdzNLLMyNXoErOpxKCBDArnEv5W5sT1fSswLvyDvHoeRfdWvPQ9ECWKnVizSmcLNV1ECv8xdyl3YErAiQZ2rcDeZX3dkZFU4-GzsR9o3h38XOz9N4fVtklwFZ8sDI4XtUTqhb_5A_961m8ZiV60ClZb-MA9m7foPgIU2k2N4jmpXGqsvJDlBnXfQBhjgUXkKVY5FUNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=QiGUuVsug1ys4FUjWyo3_O69DF0CpwhthlYDoDycWLIbwQNxpHluRlkaQ4JqaGM3QVw83-qjy44Cxz5uKiO-n25feHNRX_h9zHoP1UYVCZPCCiwBm1eu41u_8KyM8mXL0nfOOIcxk5mcKlcqdzNLLMyNXoErOpxKCBDArnEv5W5sT1fSswLvyDvHoeRfdWvPQ9ECWKnVizSmcLNV1ECv8xdyl3YErAiQZ2rcDeZX3dkZFU4-GzsR9o3h38XOz9N4fVtklwFZ8sDI4XtUTqhb_5A_961m8ZiV60ClZb-MA9m7foPgIU2k2N4jmpXGqsvJDlBnXfQBhjgUXkKVY5FUNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
