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
<img src="https://cdn4.telesco.pe/file/Kqrw2d3HeKeAT43vrt5UezAERteLlF-rCB0pYoIw-c7Q1qXHWyzfMhGCeSgQaMKstOqVwp-SmZlcqYUh1NDYKX5ceuwe9I5XP4jHhURtNo2iyocUQWzD8CFP8DUEEJOKNtHpp1PxFmKcdzmJB_f9Y8tJgv2-aZUbX_oEjPwhZ-k2ckyZR7STAkGRDGv7utTudeDGSCua0FvMBgzEwdWfAj2Q2L8j6S_dlD2sBevTbTKV3kWluSb8o4c4BoNcC_z8veBKFiqghPt4lNs4lFwkwfjgSsZoDDHIouUZZ0GsFlnrw7tjfr72cXMY0wkCmxQwVz0YQgpokU9LT-ONX6rACQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
<hr>

<div class="tg-post" id="msg-141217">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرایز اصلی روی نیمکت تیم هست
✔️
✔️
پویا اسمی ۱۶ ساله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 213 · <a href="https://t.me/SorkhTimes/141217" target="_blank">📅 18:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141216">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f5a2397a1.mp4?token=Eem9lbcCXKfVHT8lUf8WxZA2D0-AgR1yq9D8YLZ2LVvCtWoOidDbzWEsETmfs94rAIuhUnzTtWsFsCe-7LYRQ_PZNF3R94nsQjIs7NyhZbI6sQKeQL6xKCHkZ0NRafYP4suceznjgzaBOJa13dVZVfN8L9PMETo3XDqrPr1_AomWAmqWm9A5GpZqNDp1NNksmLy1zZv2J9jRM7uXkNQBfXRmtMttNEEMW-vdTVu_agbnvN3m4G-VBgcfB_6oecgq0qtLsLeb7VAiR0V1avJ_kg8W839Tj8Uh3iqQK0iLd1XCZJ1BL84hx8sEfs688rkcm4ecEBHh2JvkQajE0dyHqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f5a2397a1.mp4?token=Eem9lbcCXKfVHT8lUf8WxZA2D0-AgR1yq9D8YLZ2LVvCtWoOidDbzWEsETmfs94rAIuhUnzTtWsFsCe-7LYRQ_PZNF3R94nsQjIs7NyhZbI6sQKeQL6xKCHkZ0NRafYP4suceznjgzaBOJa13dVZVfN8L9PMETo3XDqrPr1_AomWAmqWm9A5GpZqNDp1NNksmLy1zZv2J9jRM7uXkNQBfXRmtMttNEEMW-vdTVu_agbnvN3m4G-VBgcfB_6oecgq0qtLsLeb7VAiR0V1avJ_kg8W839Tj8Uh3iqQK0iLd1XCZJ1BL84hx8sEfs688rkcm4ecEBHh2JvkQajE0dyHqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل سوم پرسپولیس به صنعت نفت توسط اوستون ارونوف 85
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 274 · <a href="https://t.me/SorkhTimes/141216" target="_blank">📅 18:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141215">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
همون بازیکن همیشگی و تاثیر گذار ..بیفوما پنالتی گرفت و علیپور زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 334 · <a href="https://t.me/SorkhTimes/141215" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141214">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
گلللللل دوم توسط علیپور  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/SorkhTimes/141214" target="_blank">📅 18:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141213">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a110cac30b.mp4?token=Dm9Kz08zJ8ECfFpI3tw5BJg-NQ6tgu-X_UnELcKeBu75YVNNi3Qbi6wZjNylv6efRWBQygi8MdtCNul6Pz3Qs0HNioeXRekPY30isbrPcWyzieVHeruVuiHBg_UO0-yvTv6z4Ehy56YcgYJcLqyNFhO6t4RKP9V8IMvC-YDiLFjw5qePQ6PIo6xAo-Es-GS6FaLoo_q2tvd25_FGDngyHK9ax8onyihWcN-mvHqCDJA6GyK_fQ30cwppXjYqm0KYB2eWraOtuKg31psUIK9Ll-JGyTGPAlI2zTC3wD2Ued3VTV5gVblPCkvZTxylIKZFUfZTZNAU_EemJeThVseD-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a110cac30b.mp4?token=Dm9Kz08zJ8ECfFpI3tw5BJg-NQ6tgu-X_UnELcKeBu75YVNNi3Qbi6wZjNylv6efRWBQygi8MdtCNul6Pz3Qs0HNioeXRekPY30isbrPcWyzieVHeruVuiHBg_UO0-yvTv6z4Ehy56YcgYJcLqyNFhO6t4RKP9V8IMvC-YDiLFjw5qePQ6PIo6xAo-Es-GS6FaLoo_q2tvd25_FGDngyHK9ax8onyihWcN-mvHqCDJA6GyK_fQ30cwppXjYqm0KYB2eWraOtuKg31psUIK9Ll-JGyTGPAlI2zTC3wD2Ued3VTV5gVblPCkvZTxylIKZFUfZTZNAU_EemJeThVseD-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گلللللل دوم توسط علیپور
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/SorkhTimes/141213" target="_blank">📅 18:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141212">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
با تعویض اورونوف جای عمری و پورعلی جای لطیفی فر میشه اختلاف و نیمه دوم بیشتر کرد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SorkhTimes/141212" target="_blank">📅 18:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141211">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
چشم نوازترین پرسپولیس چند سال اخیر و میبینیم ..نیمه اول و با یک گل بردیم ...تو نیمه ای که سه چهار گل و نزدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/141211" target="_blank">📅 18:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141210">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
چشم نوازترین پرسپولیس چند سال اخیر و میبینیم ..نیمه اول و با یک گل بردیم ...تو نیمه ای که سه چهار گل و نزدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SorkhTimes/141210" target="_blank">📅 18:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141209">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36338a35c2.mp4?token=Mp9nXFyzZmTdurXe9TxPuM1kgv9UcGcro4z4U5myrDYJi5oKnXOaKyQ5drg74S6-ZHHMKVV3i5pnnOJsoVnb5B2jQMlsbTfasHovJfufKMG3k_iW1oMcQBVC4HF-LCg24baf0JhACiwHjGIfeVILE5yzfy8DNqLCpdtmhjnfFmMs6KeehNF6mLMRbsxbnASyibu3qvtPKXY7FPY6Xc0lTFDmtgkynjomPMg8AsCI7WXbbBl4_Z8-KYpBFd0NdX57TOm3v6BooFXT21Fx_37PWOGnWZ9yoTSiKM0XnF3E75LhLzkmdUhGS2kC8siZvGkNFYE2hy0r6I-7PT42GU-0qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36338a35c2.mp4?token=Mp9nXFyzZmTdurXe9TxPuM1kgv9UcGcro4z4U5myrDYJi5oKnXOaKyQ5drg74S6-ZHHMKVV3i5pnnOJsoVnb5B2jQMlsbTfasHovJfufKMG3k_iW1oMcQBVC4HF-LCg24baf0JhACiwHjGIfeVILE5yzfy8DNqLCpdtmhjnfFmMs6KeehNF6mLMRbsxbnASyibu3qvtPKXY7FPY6Xc0lTFDmtgkynjomPMg8AsCI7WXbbBl4_Z8-KYpBFd0NdX57TOm3v6BooFXT21Fx_37PWOGnWZ9yoTSiKM0XnF3E75LhLzkmdUhGS2kC8siZvGkNFYE2hy0r6I-7PT42GU-0qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چقدر خوبی شما آقای نیازمند
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SorkhTimes/141209" target="_blank">📅 18:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141208">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
یک گل زدیم و سه گل نزدیم ..و همچنان پرسپولیس مثل همه بازی ها سوار بازیه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/141208" target="_blank">📅 17:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141207">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
گل اول و زدیم خیلی زوددد....سرگیف داد بیفوما زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/141207" target="_blank">📅 17:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141206">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس که سه امتیازش به اندازه شش امتیاز ارزش داره ..دلمون برای پرسپولیس تنگ شده بود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/141206" target="_blank">📅 17:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141205">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس که سه امتیازش به اندازه شش امتیاز ارزش داره ..دلمون برای پرسپولیس تنگ شده بود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/141205" target="_blank">📅 17:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141204">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس که سه امتیازش به اندازه شش امتیاز ارزش داره ..دلمون برای پرسپولیس تنگ شده بود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/141204" target="_blank">📅 16:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141203">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرایز اصلی روی نیمکت تیم هست
✔️
✔️
پویا اسمی ۱۶ ساله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/141203" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141202">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرایز اصلی روی نیمکت تیم هست
✔️
✔️
پویا اسمی ۱۶ ساله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/141202" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141201">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
نیمکت ذخیره پرسپولیس مقابل صنعت‌نفت:
❌
❌
امیررضا رفیعی، ابوالفضل جلالی، علی علیپور، پوریا شهرآبادی، امیرحسین محمودی، محمدحسین صادقی، امیرحسین طاهری، پویا اسمی، پویا پورعلی، استون اورونوف، یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/141201" target="_blank">📅 16:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141200">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
ترکیب اومد ..جای جلالی تیکدری بازی می‌کنه..جای پورعلی لطیفی فر بازی می‌کنه و جای شهرابادی محمد عمری بازی میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/141200" target="_blank">📅 16:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141199">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c7ca0c681.mp4?token=HXQZVEnPAuNQg0DMe-xsUP07siPmkKFN42eTDjnDAAfKa0Conkoux6n1Og1yEG4gvMu0QgtxjSzJ9xIqJ0BThhNYRD4r-FyuSXLh7gq-JBIhOPmYOkXCNtuXvhiAhGIjybfPCBTo2m8nDBXCXgQNaPFMoAYwl-ZkCpLNy4EUVWWHFKBmAFjCYALnpC2WON91nI8bOeY0y9e7TWFmrtWrTmDbqP1lh4QtM0qMNavpuhW9lYiSSB3P75hAUQVWAhLbW4-rv3pILCpVoGTHFluogcHESbgiyT0-L-hsJzANS4Iu-a4FyhqHmUdwYU2w8LhGacR80rSGDELn9gDAaGj6Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c7ca0c681.mp4?token=HXQZVEnPAuNQg0DMe-xsUP07siPmkKFN42eTDjnDAAfKa0Conkoux6n1Og1yEG4gvMu0QgtxjSzJ9xIqJ0BThhNYRD4r-FyuSXLh7gq-JBIhOPmYOkXCNtuXvhiAhGIjybfPCBTo2m8nDBXCXgQNaPFMoAYwl-ZkCpLNy4EUVWWHFKBmAFjCYALnpC2WON91nI8bOeY0y9e7TWFmrtWrTmDbqP1lh4QtM0qMNavpuhW9lYiSSB3P75hAUQVWAhLbW4-rv3pILCpVoGTHFluogcHESbgiyT0-L-hsJzANS4Iu-a4FyhqHmUdwYU2w8LhGacR80rSGDELn9gDAaGj6Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
باران در شهرقدس و حضور بانوان هوادار پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/141199" target="_blank">📅 16:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
ترکیب احتمالی پرسپولیس برای بازی با صنعت نفت
✅
حضرات/نظرات:
📺
پیام نیازمند
📺
زارع
📺
ابرقویی
📺
جلالی
📺
عیدی
📺
خدابنده لو
📺
پورعلی
📺
محبی
📺
بیفوما
📺
شهرآبادی
📺
سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/141198" target="_blank">📅 16:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141197">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🟥
ورود اعضای پرسپولیس به ورزشگاه شهدای شهرقدس
❤️
..
🚨
هوا هم مشخصه باد و بارون شدیده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/141197" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gb0R2yt6fgT11gvqXeQwOGdhY8np6M-x4IqLqjGzJ8gukLtHzjR3Xhbn1v7h2rSFpUnEmk-MD_muvwMFLHxeiFGx1H0eZyGev3gGRlBTBJEkOKbMvzebgI5as4HB8CtGLVlSBOGKlTXk2MRx1FmAbOfK7qhCKj2kKYu0IHm3dN-OXjnUxXRlAgAcytYS8ghHjbdJevhCGpfSf_sQ0a6jSXd_BKTRLvDLI6oMSvByPHeOAk4NMe88QOoOQfjOUD1U3ZkJuR4ZlGWKre4BmMeSMULWoOQ2BUkAUHTpU1WVrE3Ius81FtCYfg2enm3cnraoF_qwi8edE7WtUszxqAog0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نمای آنلاین استادیوم شهرقدس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/141196" target="_blank">📅 15:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141195">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭕️
⭕️
با اعلام باشگاه تراکتور، علیرضا بیرانوند به دلیل مصاحبه بعد از بازی با استقلال از این تیم کنار گذاشته شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/141195" target="_blank">📅 15:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141194">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSWukLkUGNSm8DRavuakdzzukfv61lFygeMpTgLz2xBic_tREhg1SHlqto4PQzVYbCcztkfJRBFyahoCrCfdpMY4bndumGtHduH2DIsGsBjxMOjsHatbOeVfHeZ6-eEglstMIOn0kxlsAuTeiE3enBaO-mM6BY-NKGHHaBfbvw-KxJ63zTzLz4F0jlopJ8Qb35Xa1JOlirT8TLvpB-fQf6zXBvUXAiXeCw1p5D-po1Gef9LtoTv6pWQ9osJiHVrTFDrm3q2qzbcbHiU8QoCOaqYm4HQG00HMhKD5n2WL9spXjAiyvdkR-hIMFSm5ci3zKH_Lq6boRP-PBr890YaA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خروج اعضای تیم از هتل به سمت ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/141194" target="_blank">📅 15:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141193">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
فردا ببر و محبوب تر شو .حاج مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/141193" target="_blank">📅 15:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141192">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGlGdaJESonNsFGKyfenz5LDmKxiUrZZTvWOQnHGrCA6pRJqGcAMia7Sj32EiHLRwSMp6QvW_WWs3seDr-pvyGio2dU9OKAOH1LetAQCCS7yPDZDIDxFWPsq-y8Vz-r232ptWRr48RhLA_XsFM23CP6MsUAxOdQxYs26TH5S5HBYQSZk5vs4Kh6Q5LOPKaCYJ210RKXNxZfNhrbmxTbEYGXYb8W6noFJpDaakaHjIVBmeUzxixKZfPngByEKGXzsgI_CqIl-kgd9Xbj2swWMXi68dcpdxMF-vLlW0-XCdccpq5inf_JPzT5D2_m1AVp8VmqkiT6lFUc8lasTMBLmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
علی علیپور: از پیام‌های هواداران عزیز که نگران حالم بودند متشکرم. خوشبختانه مصدومیت جزئی‌ام برطرف شده و با آماده‌سازی کامل در خدمت تیم و کادرفنی هستم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/141192" target="_blank">📅 15:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141191">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
باشگاه تراکتور درنظر دارد تا با توجه به مصاحبه علیرضا بیرانوند، به او اجازه فسخ قرارداد و حضور در تیمی دیگر را ندهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/141191" target="_blank">📅 14:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141190">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
🇮🇷
🇮🇷
به مانند بانوان ، تمام بلیط های جایگاه به فروش رسید ، دم تک تک عزیزانی که توی این شرایط اقتصادی میرن هزینه می‌کنن و مستقیم  از تیم حمایت میکنن گرم
❤️
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/141190" target="_blank">📅 14:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141189">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🙏
🙏
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/141189" target="_blank">📅 14:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141188">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🙏
🙏
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/141188" target="_blank">📅 14:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141187">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU53jsbrRQSXQpawav2rszME08bKyB3FQpnBe3pJ52qUo3Dc4prO8LTOo22c4d-eKw8PlJiwvUwTELNQJUvi1VT1fBi1rLdnxpMAOQNQJtbECifPGM-jNyFmJi52F-hSp4NnlC6W60YOutVWhuWVA4B_nbYBSz7G5N6UuRUAR2aRuQZPEPSksPjDoKS-yVaGEWAzl82KdgDG3z4_lAZojyufXcW84F6GU24kwnk-cj2eAlurqka7yGHJLgwGwvQsFKqNS2aEwZM2ZCymNoJIVnTI6TVeE5IRp3mfKQwjJYiqrbHCAAgfuc44B7qeKF1LoEXufJaA1cb7U24GXyV0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت
‼️
علی علیپور در این فصل تمام گل و پاس گل های خودشو در این فصل در دیدار های خانگی و در ورزشگاه شهدای شهر قدس ثبت کرده
👀
✔️
پرسپولیس امروز در ورزشگاه شهدای شهرقدس به مصاف صنعت نفت آبادان می‌ره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/141187" target="_blank">📅 14:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141186">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
علیپور هنوز زانو درد داره و بازی کردنش ریسکه البته خودش میخواد که بازی کنه تا از کورس عقب نیفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/141186" target="_blank">📅 13:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141185">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
❌
❌
اگه امروز علیپور بازی نکنه و در غیاب کنعانی نیازمند کاپیتانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/141185" target="_blank">📅 13:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141184">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ck5tddBk9gKiGUAlWr_T_di3l6jJa2F6D4ZJeT5_hVXQGwUn05ngB7lQ7FkZGn9t4OEM24aznlWp2JWKkgs5G2IP7N6oUpDzsWWOsbVTgbqUDBD1y1zLD_imEOYEJMzfRWV4dKLu8Ycks1ajyCxpYsdnTFK3ih7hVyqNWiERYY44V8kI7CaI1FS22o3yZFXtIEEVljoAuv5-AZ7fGF3aL4S2_S-BjNT35N-l6oAaYq7K5v5l26UK1AH-QP7YBGkUaWDhAd-3EoDSnQ0x5f7bEpOTGnU5oYhXiIVsmxnJ77jf8dlXkycPKiN7dGBCrMencVSdjejcdDxVrClWB0V8FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سرخ‌ها در تعقیب صدر؛ صنعت نفت، مانع بعدی پرسپولیس در مسیر سه امتیاز!
🔥
⚡️
[
پرسپولیس
🔴
🆚
🟡
صنعت‌نفت
]
⚽️
پرسپولیس با ۱۳ امتیاز از ۶ بازی و میانگین ۲ گل زده در هر مسابقه، از نظر هجومی آمار بهتری نسبت به حریف دارد. صنعت نفت در ۷ بازی فقط ۲ گل زده و با ۸ گل خورده، ضعف محسوسی در فاز هجومی داشته است. در ۵ تقابل اخیر دو تیم، پرسپولیس ۳ برد کسب کرده؛ برتری آماری با سرخ‌پوشان است، هرچند غیبت برخی مهره‌ها می‌تواند روی عملکردشان اثر بگذارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/141184" target="_blank">📅 12:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141183">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf12ee8e5.mp4?token=v5b5Gm0bdEBmV9M0-irp-J06RjCJ6yk5FpXkj1YWvbiPCsIoHRQjAZqZEyE6cFDG-0jWsTGFjiBBF7wOKncN6X8KTWflHm_vk1w06mdvE6bSbrkYoPGkzEqAK-NaUhbZfe9-cuxk26GimeMdJ6wCVo2RCa26qnJIbiEeBLdq_Z1bhdL6esdRI-dSwNdwxYA7JNVnayQVIxoM0tRa16rv1gyKyBmKdb85BqROmbIRD1meMEcF4mYCkxKSCwAf0KqAdZmVTuGcLvMgVGZPTSV-ujdiBOn4QbmcafGAQGt_9_rF_xI3uP1By7YsNROKrDoMLy3UUmXq8-WMpAjhCIy7LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf12ee8e5.mp4?token=v5b5Gm0bdEBmV9M0-irp-J06RjCJ6yk5FpXkj1YWvbiPCsIoHRQjAZqZEyE6cFDG-0jWsTGFjiBBF7wOKncN6X8KTWflHm_vk1w06mdvE6bSbrkYoPGkzEqAK-NaUhbZfe9-cuxk26GimeMdJ6wCVo2RCa26qnJIbiEeBLdq_Z1bhdL6esdRI-dSwNdwxYA7JNVnayQVIxoM0tRa16rv1gyKyBmKdb85BqROmbIRD1meMEcF4mYCkxKSCwAf0KqAdZmVTuGcLvMgVGZPTSV-ujdiBOn4QbmcafGAQGt_9_rF_xI3uP1By7YsNROKrDoMLy3UUmXq8-WMpAjhCIy7LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پرسپولیس _ نفت آبادان
❌
اولین گل یورگن لوکادیا با پیراهن پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/141183" target="_blank">📅 12:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141182">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⭕️
⭕️
⭕️
زنوزی هم بالاخره طعم تلخ داشتن بیرانوند را چشید!
❌
❌
سرانجام نوبت به زنوزی و مدیران تراکتور رسید تا طعم گس داشتن علیرضا بیرانوند را تجربه کنند؛ همان مصاحبه‌ها، همان گلایه‌های مالی و همان کنایه‌هایی که پیش‌تر مدیران پرسپولیس بارها با آن مواجه شده بودند.…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/141182" target="_blank">📅 12:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141181">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2a79b142e.mp4?token=Qj4BKLLkEoZG3NPQ_gxB4TkorCfmmYUos6uzUV8oJ-DZL6r8EFaBxUqP7DcDukObdwutzPYY5kYALmwGjEz2OVMQcCrX854q4Vrdtlq9CVsLPqbF2K7_GRPLgnD0Be07IfqrE-BLdRCOwPcuVq5dP5JLUNE4HNNZVXeB1YS_YCwli5itiCUO1c7KKenQpF9IVPwYKZKsDRxWOUsPmd1SfbYTKamsD8_GELaVSY4f4y1YJUEhVd0V2Fj6QTPyjL39X4o8sajWnbIOTFDdDiFbTTDbVWHzg7X951f3Qs6JAyh17Lu6rqbHCcDYzMehxFpjrmOb5cMKNesyqviUebyeNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2a79b142e.mp4?token=Qj4BKLLkEoZG3NPQ_gxB4TkorCfmmYUos6uzUV8oJ-DZL6r8EFaBxUqP7DcDukObdwutzPYY5kYALmwGjEz2OVMQcCrX854q4Vrdtlq9CVsLPqbF2K7_GRPLgnD0Be07IfqrE-BLdRCOwPcuVq5dP5JLUNE4HNNZVXeB1YS_YCwli5itiCUO1c7KKenQpF9IVPwYKZKsDRxWOUsPmd1SfbYTKamsD8_GELaVSY4f4y1YJUEhVd0V2Fj6QTPyjL39X4o8sajWnbIOTFDdDiFbTTDbVWHzg7X951f3Qs6JAyh17Lu6rqbHCcDYzMehxFpjrmOb5cMKNesyqviUebyeNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
معذرت خواهی هوادار تراکتورسازی از هواداران پرسپولیس
😁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/141181" target="_blank">📅 12:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141180">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⭕️
⭕️
⭕️
زنوزی هم بالاخره طعم تلخ داشتن بیرانوند را چشید!
❌
❌
سرانجام نوبت به زنوزی و مدیران تراکتور رسید تا طعم گس داشتن علیرضا بیرانوند را تجربه کنند؛ همان مصاحبه‌ها، همان گلایه‌های مالی و همان کنایه‌هایی که پیش‌تر مدیران پرسپولیس بارها با آن مواجه شده بودند.…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/141180" target="_blank">📅 12:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141179">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b4db41c1.mp4?token=DFLrn6WoTB7YPy9n0vwkUfMmql6NdtATMwWzZHWrsX1rs2S2kfW11YFbgoQQm2wbkOVQ3P3lUp1nyhKYdTpKNIv1UHmAfpFtHH2zHY7MNmQGw2E0UD2-rAwpQD-ImRrPfv_49_c37X0UGMR3l4t9cu6PTUH7-26ZsEi5R-voTSy1lfpauC7bAO21d1QABlFbAD216pavFreoHQKTMXb3f__TGw1oBolyCE5l9tLxzFackUWnewuCL_0VF396hum-rOqwiK_n2wftJLuLjWb1G5BTYkk8MyjmhjRnWvlrdkDAYdGNMJ1JAXXxEPQBBMFSW6zuPvYfrzYK-Xl5UoRD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b4db41c1.mp4?token=DFLrn6WoTB7YPy9n0vwkUfMmql6NdtATMwWzZHWrsX1rs2S2kfW11YFbgoQQm2wbkOVQ3P3lUp1nyhKYdTpKNIv1UHmAfpFtHH2zHY7MNmQGw2E0UD2-rAwpQD-ImRrPfv_49_c37X0UGMR3l4t9cu6PTUH7-26ZsEi5R-voTSy1lfpauC7bAO21d1QABlFbAD216pavFreoHQKTMXb3f__TGw1oBolyCE5l9tLxzFackUWnewuCL_0VF396hum-rOqwiK_n2wftJLuLjWb1G5BTYkk8MyjmhjRnWvlrdkDAYdGNMJ1JAXXxEPQBBMFSW6zuPvYfrzYK-Xl5UoRD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دانیال اسماعیلی فر هم از ناحیه ای که رامین مصدوم شد مصدوم شده و احتمالأ یک ماهی نباشه
😁
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/141179" target="_blank">📅 12:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141178">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ff4bc2f6.mp4?token=eVNVKlOBCLySFsCWzhbd8r06XL7Gr_CQxXiR1dGz5_ChFQHofaimj8CS3KNAjPv9sLcz3DAyeIfilbuTl2wRhDx9iOZ9XsDV-cjA0RaGy3A2YQqjolp9ycPskoG9GAawNy7FkenRCit47kEXBXrsBvLgGwJNb0IRnNpZJeif7R4ivJ53pFslvR_TerS2HOcdkBuVrOSZWBmC92500IvYO62n62H3zLbdbdqqMp4FFf9zJCDmR1NTgIo7DJnSUGUE0JmDM0UFLJzUFlPc2GRwLoG74EXbDvvZbecMi5xUmfYqrVon_SZv9wbATQfQLRzIiQ04m0XmXn3GarGgFLqrsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ff4bc2f6.mp4?token=eVNVKlOBCLySFsCWzhbd8r06XL7Gr_CQxXiR1dGz5_ChFQHofaimj8CS3KNAjPv9sLcz3DAyeIfilbuTl2wRhDx9iOZ9XsDV-cjA0RaGy3A2YQqjolp9ycPskoG9GAawNy7FkenRCit47kEXBXrsBvLgGwJNb0IRnNpZJeif7R4ivJ53pFslvR_TerS2HOcdkBuVrOSZWBmC92500IvYO62n62H3zLbdbdqqMp4FFf9zJCDmR1NTgIo7DJnSUGUE0JmDM0UFLJzUFlPc2GRwLoG74EXbDvvZbecMi5xUmfYqrVon_SZv9wbATQfQLRzIiQ04m0XmXn3GarGgFLqrsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🤩
ببینید دختر هادی نوروزی چقدر بزرگ شده؛ همسر هادی بعد ۱۲ سال هنوز لباس مشکی رو در نیاورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/141178" target="_blank">📅 12:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141177">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r09tuiF6kdnGPQ4XxR5ipOppYrNH8mssk7Q1Ilhe4Ukz-WpVkU7pHpvAxgjvKt0kVa9Ri-To7RB5qX4JhOzM_eNhQaCiEA8tJSMKREK1xx5WcUwU9Hb936aO7Z5K6zQyh-L26GndulYIFAgc7MYZ9SsOF4z4-ng3Ho3LljB8LuROUln4FOYiGhTktR3a-v6gxZIWpOLd2G95D6FpyIcTOGhiSKxD4HqqCYpjkzVHn4sb6gYzorsjjI8V_c9fGGmGSiJ5T56IY9StN2hsGFq8TuTwM-mJdb1t9fw05wNAIU_H-9PEZOMWQAt2rQwZnwV9-TQGmwlsHF-QpEqslGTvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرسپولیس- نفت؛ ۹۰۵ روز پس از آن برد‌ خاطره انگیز
🚨
پرسپولیس و نفت آبادان پس از ۹۰۵ روز، امروز در ورزشگاه شهر قدس مقابل هم قرار می‌گیرند. در آخرین تقابل (۳۰ فروردین ۱۴۰۳)، پرسپولیس با گل‌های اسماعیلی‌فر، آل‌کثیر و کنعانی‌زادگان به برتری رسید و در نهایت قهرمان شد، در حالی که نفت با هدایت کمالوند به لیگ یک سقوط کرد.
🚨
اکنون هر دو تیم بدون مربیان قبلی (اوسمار و کمالوند) بازی می‌کنند و از سه گلزن آن دیدار، فقط کنعانی‌زادگان در پرسپولیس مانده که او هم مصدوم است و احتمالاً به بازی نمی‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/141177" target="_blank">📅 12:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141176">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
⛔️
👀
پرسپولیس ب که قرار بود به سیدجلال سپرده شود، احتمالا با محسن بنگر وارد رقابت‌های دسته دوم لیگ آزادگان می شود...
‼️
🟥
به گزارش هفت ورزشی، پرسپولیس که دنبال خرید امتیاز برای راه‌اندازی تیم دوم بود، سرانجام امتیاز پادیاب خلخال را خرید‌. گفته می‌شد هدایت پرسپولیس…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/141176" target="_blank">📅 10:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141175">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJSAnitzsc0Ch7xzDr_LP3xjgXvXMylzJzwnRLwXqhQ9WEcms6zz_z7YsOFr1F31EIkY0WTwvtD8yBhwjzfhIyuxc_Ai31sRYCtY1FB_vFqyFvwkDyF3Kuw-Ba0lFFViUEgSbBkqx9BMj6-tHF8tr-wp1ycrviTrqOujWx5WScxrsESJGzL_I0JhoIcDACJRRH1e06ZUTY8Mha6AuFlw09Y8zRZZHDez4zdcNhxst5YL-tM5KlM0wXp_89_ciq6Ko2jQhnxxUlU3wg7lF04pv-ye9fvemVqtg-jOmd9yHmlHVUUwMFolHF4GcM2rB_c9mqHo3_iOHYBGIwQPSabxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دعوا در تراکتور بالا گرفت
❌
شکایت بیرانوند از کریمی مدیرعامل باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/141175" target="_blank">📅 10:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141174">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
با نظر کریم باقری و موافقت مهدی تارتار ؛ پیام نیازمند کاپیتان سوم پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/141174" target="_blank">📅 10:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141173">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvEpxAbYYpExSis6uuyPdMamkvB48FQfE7xqzaxls7zv6Zl4pzCnS2-DXX7FYU_Ww6BYZMH91XmKTn9SC0MWF4KXJ4PjEXjUREKKSGooVu8DAwswvjVBTvUk65INv956aHdGH84vkLodLcwz-_qVp3I4KVy94XGdGwnC6YSW_q3m1ibxoMWGY4Y0KBQYphvjFCH4ioZ63lAp7qmruQ9rcdt223BwejN_Zht_k_z0QOdfu4bI90G1KweF17Ti_EH0ZIDUWqUxXd1o__hVqzRlDD9vbEGeuMetsrTsRuTmU6B4f9jf6suzPZmk-H6RaiSgstXGYdNNqHB4l7AFFdjx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با نظر کریم باقری و موافقت مهدی تارتار ؛ پیام نیازمند کاپیتان سوم پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/141173" target="_blank">📅 10:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141172">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
کریستیانو رونالدو امروز برای سومین روز متوالی در تمرین تیم ملی پرتغال حاضر نشد و طبق گزارش رسانه‌های پرتغالی و اسپانیایی، اردوی تیم را ترک کرده است. این اتفاق پس از اظهارات ژسوس درباره غیبت رونالدو مقابل دانمارک رخ داده و برخی رسانه‌ها احتمال بازگشت او…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/141172" target="_blank">📅 10:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141171">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilDe2j_MG3MH0VXqJyFan9bjSE5HQLIDMHaG1avE5KZtOGrbmD7ABfEq_u7KGdGqO2xAPGXNiFlf7Psilocs40WqDo1DKhkalWVs5hrkpCCkfvNiuxlP9ALuG3mUl6QpGQ1axgMm7j33h9rmcrPfvalf6VQNSNRlXSKpPJC0TKMwY0-6YiBTA7lizDjtE1PnWisoIC59L_NthH6UVWLyARQoi2O8dYV_uLYJJLZDey7mDvvIRyqRW96BTo---ZAuqGjoUTFeFWTS1zccBlRQzJKOxJCOb6MSXQeYItQRNpFSrqpMDBXkQ0-V52kKHIgO7qWgSvS2DTMZ686sz-GEHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ورزش سه: پوریا لطیفی فر امروز قراره جای پویا پورعلی بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/141171" target="_blank">📅 10:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141170">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
دعوا در تراکتور بالا گرفت
❌
شکایت بیرانوند از کریمی مدیرعامل باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/141170" target="_blank">📅 09:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141169">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
علیرضا بیرانوند پس از استوری کنایه‌آمیز شجاع خلیل‌زاده، کاپیتان تراکتور را آنفالو کرد. شجاع هم اقدام متقابل کرد و بیرانوند را آنفالو کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/141169" target="_blank">📅 09:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141168">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
شجاع بیرو رو آنفالو کرده و ازهمه‌اعضای تراکتور خواسته که این بازیکن رو در اینستاگرام آنفالو کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/141168" target="_blank">📅 09:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141167">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
علیرضا بیرانوند: من به رختکن استقلال نرفتم. شبهات درباره صحنه گل هم درست نیست. می‌خوان به اعتبار و شخصیت من لطمه وارد کنن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/141167" target="_blank">📅 09:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141166">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭕️
حجت موتوری: همه بازیکن ها 8 درصد گرفتند ولی بیرانوند 35 درصد گرفته
😂
✔️
بیرانوند گوه خورده میخواد بره استقلال بعد خدمت سربازی هم با ما قرارداد داره
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/141166" target="_blank">📅 09:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141164">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2x72EWT1ydlW0wkw3Hyq5SIOIPijSXdGD9zVB5Y8dlnkvQFIf5fuke46QBoKpvFj9e12EvtEWPjXbv5jkLTaYrYFnclwNZ_uwfflM7So6aX8Rqq6u16J2vzXFffrhS_SLHvhreni57aCcZt5yfnVuKDbxLcXNJDpqfoghj38xA0wiRtxYuksRszROdjKaxsgwS1nH0k0dbBM4BcawBueqVeu6fvXEdP0Buxj50OM18iM6C2xip3qOssDf7fEY3cJCaKVvzWime1-Cx3XdvlwvCWxpRnk6p3K6UPMK5ff2cP4AHXkV4iwef7x-8zcYxNpd6SefVyKhkA9l2j4TTG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/141164" target="_blank">📅 09:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141163">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FG_Yo0PhsrQ4PyzraQqALvNIn5CvNFUFxEGEVqVap61pSXJyqC_ksnCStpN8z42doikyjV6BOA-_eW1wbzsoQ3uNOYx-j9y0lvJXXXW199ZRSbUlV4CjzDUbuo9W7Ht4h5ZWfYjdzBokqFB9OmCjYkHUR06c3GXwKDclBftvbG3jU2LkhCXbTbT97YYT00C7Vo8GNyLf9I_MfpP18TVZiR15vX61UvsV7gcW4zlmuhWIfG0EDb2WQ8qBKe0DrqwhiiipNDdtCEcvcBZsFZaqDWovmyQdYF5Nft96Ajr4Ql-Fgxr0okFkhqe9YCOCfjjrFjAof_plNXEEs02JY-Stng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141163" target="_blank">📅 01:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141162">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
استوری کنایه‌آمیز شجاع خلیل‌زاده به بیرانوند: تمام حقوق خود را گرفته‌ایم و از زنوزی متشکریم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/141162" target="_blank">📅 00:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141161">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Novi_17YKIgV2593U7C8GosHZTSdzEO8nwPr1JU94MR97Eaw4NtbQtrVMymmYAjMlvm2_oW9DcXXYyam1XGseWr3XxrSaMXcrqAhC7pRNu-vUgdUF3Y4WJ34oPN_j6mmI9U0gVgSr1idX5L8tkOQac_9H4T97YwReyWi-BPomtb3XhK7Gv7jgY9p6fQWUJs0jTAutTQ00YHEY2P0b_PnCwNOOTyvFsv7IbeZfZtqCEmH9rdFbdR4USf5PsVvBf3Js2USYiopaKvHwPUFC-NlJvq5ZZFORv6uQn3h9RJLtsUBD3r7SpdqI7vflPA64BmTEP0qx59v0t434QpCF5w1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
بیرانوند تا الان عضو 5 باشگاه بوده که در هر 5 باشگاه به مشکل خورده و از اونجا به شکل غیر حرفه ای جدا شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/141161" target="_blank">📅 00:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141160">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
👤
کنایه خداداد عزیزی به بیرانوند: اجازه هیچ حاشیه‌سازی را نخواهیم داد و از زنوزی بابت انضباط مالی قدردانی میکنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/141160" target="_blank">📅 00:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141159">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdOtkN1YLnng1v6JpJXbHpnoHSSoT3u3e75hz7S2WKX-mGP0xWjjdColkaXF_LTAVdOumu1jYrRRaylYKi952d-AKhTt0si6s8CdNchY1xbAh8AEGUUcyzKOVPIOfSoXGg_ZpR6rISmuYOnTIxtGlEwRwchsi-ACfwtj5cNHifrD8q7RoHGZK_hyoaQYCs5IT7R3paNI1DUaLXUp5qLmFeRjx3bx1o-NcFbaueioQ7zkPKTrFU1QgKyQVln4CdLYT0n9zSBPGFKkAmjYYYOPXp1n6hQ2N0KtGdSCkRB3-NPUKN9Ds7odzFGfQl1DEoz0aASrqSt8_k_3zrWR3c7B8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کنایه خداداد عزیزی به بیرانوند: اجازه هیچ حاشیه‌سازی را نخواهیم داد و از زنوزی بابت انضباط مالی قدردانی میکنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/141159" target="_blank">📅 00:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141158">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
استوری کنایه‌آمیز شجاع خلیل‌زاده به بیرانوند: تمام حقوق خود را گرفته‌ایم و از زنوزی متشکریم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/141158" target="_blank">📅 00:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141157">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwxrGLGKdq-NYRFubEW7daRTBVqwi417h-AwaQf4z0phTDYSmGVlsZGFPP9lFMHrbyfDcHP3pfrCgv7qvZUDN-D2u9YWDfEZiK1D0wb8fH6J45SHGeiVAZgtX22nV3PNKFUDD8ouYju9q0X8pFD3taGAXcI3S-nZx1uzA2rlb07kUbRHtwqL_epOt5oIWTL9tCn3_PuiT5vsHXlY_b_cAn5i2BZTLPywj0f2vYBlkEL9C8wy0nbc45MMO3HBynB2J2ylBLfe8Lh93bfr9kE8guo1Hyy3Bm5Xiz2qtbhCrYTPP55ewagUEiR_x45Ci3Oe9g51e-zJFCF4jk1EF3VQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از آنا
🔹
باکیچ به دلایل فنی از لیست پرسپولیس کنار گذاشته شده و مصدومیتش کذب محضه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/141157" target="_blank">📅 00:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141155">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YErh4DI9GO5g1KCuJDBbrOnAnWTWYZE6sUTTnjfUoPJ-wCVX6Km9W_AayD8oOBUoOcuSyQcTyii5iUUfoef1fnUXrljJfW33hi7Q7r2epeZVVfympt2OAkI3Mtazz7yqgFw7-vWzr8AUTPf7-GWgqLcg6n_zNhISJKo-VMNZiHehMiprSRtfVvfJQTeyJD10Oj-vCeKCen1W5K621lyGm9AAMdXPovuROWxoWzSI1HD05JlnVfafaSgFOmKAn--IBdBzH_tgbvW4p7mQZwL0S7pseOKXtEGz5V5MztzfLHopX3FkIfvxEijY-QtQw2pXTJy7cY3-Qd3hdWyWztFxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از آنا
🔹
باکیچ به دلایل فنی از لیست پرسپولیس کنار گذاشته شده و مصدومیتش کذب محضه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/141155" target="_blank">📅 23:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141154">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
22 پرسپولیسی برای بازی مقابل صنعت نفت وارد اردو شدند / یک نفر فردا خط خواهد خورد!
🔴
1_پیام نیازمند
🔴
2_امیررضا رفیعی
🔴
3_امیرحسین طاهری
🔴
4_ابوالفضل جلالی
🔴
5_محمد مهدی زارع
🔴
6_حسین ابرقویی نژاد
🔴
7_مجید عیدی
🔴
8_مهدی تیکدری
🔴
9_پوریا لطیفی فر
❗
10_محمد‌…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/141154" target="_blank">📅 23:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141153">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
22 پرسپولیسی برای بازی مقابل صنعت نفت وارد اردو شدند / یک نفر فردا خط خواهد خورد!
🔴
1_پیام نیازمند
🔴
2_امیررضا رفیعی
🔴
3_امیرحسین طاهری
🔴
4_ابوالفضل جلالی
🔴
5_محمد مهدی زارع
🔴
6_حسین ابرقویی نژاد
🔴
7_مجید عیدی
🔴
8_مهدی تیکدری
🔴
9_پوریا لطیفی فر
❗
10_محمد‌…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/141153" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141152">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⭕️
⭕️
مارکو باکیچ و دنیل گرا از لیست بازی فردا خط خورند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/141152" target="_blank">📅 22:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141151">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
باکیچ و لطیفی‌فر شانس برابری برای حضور در ترکیب فیکس پرسپولیس مقابل صنعت نفت دارن و تارتار هنوز تصمیم نهایی خودشو نگرفته/ایران‌ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141151" target="_blank">📅 22:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141150">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leMNnhwloK-oq8AnhtHFnag7yU78ZD8gJotVGCpEwZTjhpHqTOSpefNq1hMLvmuHtCMjVw9KMVFOE6jjwa0p1UmUiN2ET3Vkq2QcdO4usy8Q93u6WAkO_CM819F6P1YBrZFbqFVGqanqHwkYKEtIqfhuSJQPp6Eunk-gE93NXN9zJ_hZsuD_jDLXfuiw4S0o3sAtvzB5PYV5lXwKBQiI_9tWuRXAybg5Kiv79PbtXL0yFPZiVgB-zQSzmqLJOxJ-vIi-87TGWrg4HHP2rIJ2z7GW-rJjxjFXSlGCiRuWF8oyrGrN1A--QyHj2R5ZnFeJP1r5vycE5ilyH_socnwOxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
کنایه حجت‌کریمی به کم‌‌‌فروشی سرباز
✅
مدیر تراکتور گفته گلی که بیرانوند خورد باید از کارشناسان راجع‌بهش پرسید‌. منظورش این اشتباهه‌ فاحشه که توپ از زیر دستش رفت‌‌. به‌نظر میاد به کم‌فروشی بیرانوند و گمانه‌زنی رفتنش به استقلال اشاره کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141150" target="_blank">📅 22:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141149">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⭕️
حجت موتوری: همه بازیکن ها 8 درصد گرفتند ولی بیرانوند 35 درصد گرفته
😂
✔️
بیرانوند گوه خورده میخواد بره استقلال بعد خدمت سربازی هم با ما قرارداد داره
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141149" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141148">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
جواد نکونام به دلیل مصاحبه دروغ، بیرانوند رو اخراج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141148" target="_blank">📅 22:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141147">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
⛔️
👀
پرسپولیس ب که قرار بود به سیدجلال سپرده شود، احتمالا با محسن بنگر وارد رقابت‌های دسته دوم لیگ آزادگان می شود...
‼️
🟥
به گزارش هفت ورزشی، پرسپولیس که دنبال خرید امتیاز برای راه‌اندازی تیم دوم بود، سرانجام امتیاز پادیاب خلخال را خرید‌.
گفته می‌شد هدایت پرسپولیس ب به سیدجلال حسینی سپرده می‌شود اما گویا باشگاه شرایطی دارد که مورد پسند سیدجلال نیست.
‼️
برابر با شنیده‌های ما سرمربی فقط حق دارد ۵ بازیکن برای تیم جذب کند که این پنج بازیکن هم از کانال مورد نظر باشگاه وارد تیم می‌شوند. بقیه بازیکنان را هم خود باشگاه به خدمت می‌گیرد.
انگار محسن بنگر این شرایط را پذیرفته و ظرف ۴۸ ساعت آینده به عنوان سرمربی تیم دوم پرسپولیس برای حضور در رقابت‌های دسته دوم لیگ آزادگان معرفی می‌شود.
‼️
راست یا دروغش گردن راوی که می‌گوید پرسپولیس امتیاز تیم پادیاب خلخال را گرانتر از قیمت عرف بازار خریداری کرده است. در خرید این امتیاز یکی از اعضای هیات مدیره که اهل استان‌های آذری زبان است نقش داشت.
همچنین رد پای یک عضو هیات رییسه فدراسیون فوتبال در این ماجرا دیده می شود، همان شخصی که یک دور مشاور مدیرعامل باشگاه بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/141147" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141146">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
بیرانوند هم ظاهراً از همین حالا خودش را در استقلال می‌بیند! برای همین بدون نگرانی علیه زنوزی و مدیران تراکتور مصاحبه می‌کند. خودش هم از سربازی و بازیکن آزاد شدن حرف زده؛ انگار تصمیمش را برای آینده گرفته و دیگر نگرانی چندانی بابت واکنش مدیران باشگاه ندارد.…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/141146" target="_blank">📅 21:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141145">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
❌
❌
❌
❌
❌
از سوی دیگر، گزارش‌های تأییدنشده از کاهش شدید پروازهای هواپیمایی آتا حکایت دارند؛ شرکتی که گفته می‌شود در سال‌های گذشته روزانه ۵۰ تا ۷۰ پرواز داشت و حالا تعداد پروازهایش به چند مورد رسیده است. اگر این آمار درست باشد، می‌تواند زنگ خطری درباره وضعیت اقتصادی…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141145" target="_blank">📅 21:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141144">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭕️
⭕️
⭕️
زنوزی هم بالاخره طعم تلخ داشتن بیرانوند را چشید!
❌
❌
سرانجام نوبت به زنوزی و مدیران تراکتور رسید تا طعم گس داشتن علیرضا بیرانوند را تجربه کنند؛ همان مصاحبه‌ها، همان گلایه‌های مالی و همان کنایه‌هایی که پیش‌تر مدیران پرسپولیس بارها با آن مواجه شده بودند.…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/141144" target="_blank">📅 21:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141143">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭕️
⭕️
⭕️
زنوزی هم بالاخره طعم تلخ داشتن بیرانوند را چشید!
❌
❌
سرانجام نوبت به زنوزی و مدیران تراکتور رسید تا طعم گس داشتن علیرضا بیرانوند را تجربه کنند؛ همان مصاحبه‌ها، همان گلایه‌های مالی و همان کنایه‌هایی که پیش‌تر مدیران پرسپولیس بارها با آن مواجه شده بودند.
❗
❗
اما این بار ماجرا خیلی زود به برخورد انضباطی رسید و جواد نکونام پس از مصاحبه جنجالی بیرانوند، او را از تیم کنار گذاشت و باشگاه نیز رسماً اعلام کرد که این بازیکن در اختیار کمیته انضباطی قرار گرفته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141143" target="_blank">📅 21:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141142">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⭕️
⭕️
با اعلام باشگاه تراکتور، علیرضا بیرانوند به دلیل مصاحبه بعد از بازی با استقلال از این تیم کنار گذاشته شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141142" target="_blank">📅 21:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141141">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
خلیل‌زاده اومده استوری گذاشته از مدیرعامل تشکر کرده و پشت بیرانوند رو خالی کرده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141141" target="_blank">📅 21:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141140">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
✅
مصاحبه بیرانوند:
✖️
اکثر بازیکنان می دانند که این جام ملتها آخرین جام ملتهای آنها است و باید یک کاری انجام دهند/ از آقای زنوزی خواهش می کنم به داد بازیکنان تراکتور برسد/ چندتا بازی دیگر نیم فصل تمام می شود اما بازیکنان تیم ما فقط 7 درصد پول گرفته اند/ تراکتور…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141140" target="_blank">📅 21:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141139">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭕️
⭕️
با اعلام باشگاه تراکتور، علیرضا بیرانوند به دلیل مصاحبه بعد از بازی با استقلال از این تیم کنار گذاشته شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/141139" target="_blank">📅 21:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141138">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/141138" target="_blank">📅 21:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141137">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141137" target="_blank">📅 21:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141136">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8lO041t6jFiEjwJRN8Fpe6MG5-6pgzGZm8RTOIvGA5c5wlTM2eP3O61wSwtWBIKBlQ_U6I3DnRP8YDfp3LIKfTZD33S0qjGKin5GCBIjhPhHYrP8L8m6jfeyIeKMekzWyL3RItDmWHYHDxe31E7tJAhHIW9jkSPtl2mYX3HcUgGrltynM0p9Gn2iQcQOybQthsSd3Wlx5E7vmhxwyKskW0KYanV9fTtjMlGbI-pzSde3kMnZsSGDOutCl8ick0uybsm7-A_kddgQ_2btcYLA1noonbQwrxTml9sFLydVcKCqUKPvll_ARIjWnuTJDNTj1U4rjxY1zee0g5an4Psww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
Sepahan -
🟡
Fajr Sepasi
⏰
Today 18:45
🏟
Naghshe Jahan
🔵
سپاهان از نظر کیفیت فنی، مالکیت توپ و قدرت هجومی دست بالاتر را دارد و در خانه می‌تواند فشار بیشتری روی فجر ایجاد کند. فجرسپاسی احتمالاً با دفاع فشرده و انتقال‌های سریع بازی می‌کند و تلاشش بیشتر روی بستن فضاها خواهد بود. باتوجه به تفاوت کیفیت دو تیم، سپاهان شانس بیشتری برای کنترل جریان بازی و ساخت موقعیت‌های خطرناک دارد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/141136" target="_blank">📅 21:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141135">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚽️
جدول لیگ برتر فوتبال ایران پس از پایان بازی‌های روز اول هفته هشتم
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/141135" target="_blank">📅 21:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141133">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjT-da62viiiMYHyGIsL4jAonw74xKVXp49RFHfD4_zIBf4o_y6ZKV63Yo3RIU72vdABqkxqjpcB_YGvv4giwhQ2y1k-PYquxOtlrLxMe-DYCHqunMRf3zKGgRqhFUA6D9GnX3kKVYmaSASWMsxHMyTwq1glspcyZWRrOhd0_5Hjq2d1DXhnJnRs5qbwywP0U5bsjYaGBpNat7nZg5dV0v_84guYNARTVj34wPrPUgarLduWW_Auetn6_E7PC195j1Ath28F8diCZkU8ExNqKyDLt7K2ZyWzaRV86j-MIsO2JZ8GV9NSShGokWddI4YYCtsjMKJA5AFGtZApHHQK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول لیگ برتر فوتبال ایران پس از پایان بازی‌های روز اول هفته هشتم
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/141133" target="_blank">📅 21:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141132">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❤️
🎙
علیرضا بیرانوند: امروز ام آر آی کتفم را برای نظام وظیفه فرستادم/ به هیچ عنوان درخواست معافیت پزشکی نکرده ام
🔴
نظام وظیفه اعلام کرد عکس کتف مصدومیت را بفرس که من هم فرستادم
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/141132" target="_blank">📅 21:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141131">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
وارد فیفادی شدیم، شخصا از فیفادی نفرت دارم چون پرسپولیس لذت دیگه‌ای داره برام
❌
میشد که قبل از فیفادی یک برد دیگه و یک بازی دلچسب دیگه از تیم محبوبمون ببینیم اما کارشکنی‌ها جلوی برد دلچسبمون رو گرفت..
❌
دم تک تک بازیکنامون و کادر فنیمون گرم که کاری…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141131" target="_blank">📅 21:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141129">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
تارتار: تعطیلی ۵۰ روزه لیگ منطقی نیست؛ حداقل تو این مدت جام حذفی رو برگزار کنید، حتی بدون ملی‌پوش‌ها. بازیکن‌ها هم باید برای تمدید قرارداد با پرسپولیس جلو بیان، چون پرسپولیس تیم بزرگیه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141129" target="_blank">📅 20:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141128">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: خیالتون راحت باشه. قبل انتخابات کنگره(۱۲ آبان) به ایران حمله نمی‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141128" target="_blank">📅 20:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141127">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aee740782.mp4?token=Ox0Ezb1oGigWq59V9K_HjPTfPDN_o3g2rJzQOjl-P7ULrxcVW90I26Pf2f3wlmq6BBQqdwN2PuFaNL2xBBaZaOyoJEDAzv5_5iZoi5xoomSM79CnWrlCq8vroRzxyJI6FF8FKjfDK1zrVTTCQIeI98d5e_wS7DccM6v-lN7ui0zT-kejtiU18-_4W3DsWJO8vHRcIgifDmMzA_M3tEfsm4G20Fi1HTIpZD9y-RqEYc9DU1w3_eCs6jKxQ7aZBKq7GkDAMOANLJg2hL1hS68pZnzcDLgLY-0iFFVfy-mw4b76TPNf7YW4MfMHj5dUxmgapukFw2iQKe67YECsUhxHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aee740782.mp4?token=Ox0Ezb1oGigWq59V9K_HjPTfPDN_o3g2rJzQOjl-P7ULrxcVW90I26Pf2f3wlmq6BBQqdwN2PuFaNL2xBBaZaOyoJEDAzv5_5iZoi5xoomSM79CnWrlCq8vroRzxyJI6FF8FKjfDK1zrVTTCQIeI98d5e_wS7DccM6v-lN7ui0zT-kejtiU18-_4W3DsWJO8vHRcIgifDmMzA_M3tEfsm4G20Fi1HTIpZD9y-RqEYc9DU1w3_eCs6jKxQ7aZBKq7GkDAMOANLJg2hL1hS68pZnzcDLgLY-0iFFVfy-mw4b76TPNf7YW4MfMHj5dUxmgapukFw2iQKe67YECsUhxHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🟡
ی سوپر گل دیگه هم ببینیم
✔️
گل شیشم‌ سپاهان‌ به فجر سپاسی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141127" target="_blank">📅 20:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141126">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45eaeb8981.mp4?token=WPRL6A4ApHiL_a5B3l7idttSxdCOAPD8AcOuYYbmspmzm6jvO7zYri90y0lE8YF4J-q3UTyBHowv6Gr_sx6vHkY4GixGWN1OxqPupolEf1GBjnMDXA1c5M-57ZsKYVFkM3MD2OvBUw32m-dVOtSU975sAScAMRcD-SUPkD8sEb--uf6hnNCcqrLwzjHD6bKgnqDeFxhf8xpOig_MjqY_Cpqs-Tv8E88bq5h_sUjh4hRcoTfgn2Tp0g2nxTNKKJNNOV3DeBJaZ1UtIwKpomHr_ClFxfORrTQ5eTy5Y-t1H8FaSsbt7ME3qQo8x26ukz_BsW3o21mM0CEH_N4bBq-IeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45eaeb8981.mp4?token=WPRL6A4ApHiL_a5B3l7idttSxdCOAPD8AcOuYYbmspmzm6jvO7zYri90y0lE8YF4J-q3UTyBHowv6Gr_sx6vHkY4GixGWN1OxqPupolEf1GBjnMDXA1c5M-57ZsKYVFkM3MD2OvBUw32m-dVOtSU975sAScAMRcD-SUPkD8sEb--uf6hnNCcqrLwzjHD6bKgnqDeFxhf8xpOig_MjqY_Cpqs-Tv8E88bq5h_sUjh4hRcoTfgn2Tp0g2nxTNKKJNNOV3DeBJaZ1UtIwKpomHr_ClFxfORrTQ5eTy5Y-t1H8FaSsbt7ME3qQo8x26ukz_BsW3o21mM0CEH_N4bBq-IeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سوپرگل عجیب غریب بازیکن فولاد به مس شهربابک
😐
🔥
🍃
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/141126" target="_blank">📅 20:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141125">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a34de23e.mp4?token=j7fhCpwGyR8AmDBeoX6dR_E9QcsCLBAX3ATpgbXUFKTwT1X8zYW5e-E5ATrdpY7z--0uWe70a8C396kNi0_5o-d9QsOb9P6X2QLvP-tvlXijHTuSBd3hV3yB9M4DCjVu6PFkvVljwWFs4zS3kIaAMiDYO_6232anIiUuNA3Fz5s-Zlgo8zkMRrzdRTbIcr37NM3asKUujhDTkFgqFuWM0JQxAAM7xT0GMQYYJDFJoFe94tOpSHPr7zI1Proi7r88z01I0r99NkL1c-Nn8aQSu0ITGkdvftsCwBPkJyi3PgcPjUGBlysp4Ry13m5SFxhuOEu6ZCJThCjVmgxPEY6dWT2tzn1twb18M9iZXUZHTtfgplvtvB1IHCLyGrz3q1QHq8vtfvIqzyfwkKvubV1z-B2ckttbwUI7HshI1Zh5batcH0kXigEzk0fxA84gYCugsHP7z_rig6KOOmC8apju2d9KdDPWcb3gQhEYvMOWjO7lr1F7bqheH_BBgUGcGSmz2eQE_mrsAz_oDSStmo_6KFA6diaquNvNwSzcttnBN03de_d-362TfbpoxvbXFpjBg-XrEYTEwe7tXP-pveNGwPYUPmvU_fa2Td7O8GIJWk0F7342FfuKlhH53H8EjBJ5YUZzl61dDFU_TEGD9hcRYkvDirZAwxUR8B0QXriK_a8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a34de23e.mp4?token=j7fhCpwGyR8AmDBeoX6dR_E9QcsCLBAX3ATpgbXUFKTwT1X8zYW5e-E5ATrdpY7z--0uWe70a8C396kNi0_5o-d9QsOb9P6X2QLvP-tvlXijHTuSBd3hV3yB9M4DCjVu6PFkvVljwWFs4zS3kIaAMiDYO_6232anIiUuNA3Fz5s-Zlgo8zkMRrzdRTbIcr37NM3asKUujhDTkFgqFuWM0JQxAAM7xT0GMQYYJDFJoFe94tOpSHPr7zI1Proi7r88z01I0r99NkL1c-Nn8aQSu0ITGkdvftsCwBPkJyi3PgcPjUGBlysp4Ry13m5SFxhuOEu6ZCJThCjVmgxPEY6dWT2tzn1twb18M9iZXUZHTtfgplvtvB1IHCLyGrz3q1QHq8vtfvIqzyfwkKvubV1z-B2ckttbwUI7HshI1Zh5batcH0kXigEzk0fxA84gYCugsHP7z_rig6KOOmC8apju2d9KdDPWcb3gQhEYvMOWjO7lr1F7bqheH_BBgUGcGSmz2eQE_mrsAz_oDSStmo_6KFA6diaquNvNwSzcttnBN03de_d-362TfbpoxvbXFpjBg-XrEYTEwe7tXP-pveNGwPYUPmvU_fa2Td7O8GIJWk0F7342FfuKlhH53H8EjBJ5YUZzl61dDFU_TEGD9hcRYkvDirZAwxUR8B0QXriK_a8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
🎙
علیرضا بیرانوند: امروز ام آر آی کتفم را برای نظام وظیفه فرستادم/ به هیچ عنوان درخواست معافیت پزشکی نکرده ام
🔴
نظام وظیفه اعلام کرد عکس کتف مصدومیت را بفرس که من هم فرستادم
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/141125" target="_blank">📅 20:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141124">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: خیالتون راحت باشه. قبل انتخابات کنگره(۱۲ آبان) به ایران حمله نمی‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/141124" target="_blank">📅 20:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141123">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
🚨
دونالدترامپ رسما اعلام کردکه تاقبل انتخابات که ۲۵ روز دیگر شروع میشه به ایران حمله نخواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/141123" target="_blank">📅 20:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141122">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rt-M_lSeMe5lX9uhCvppSvstVtShkuJUYkAhfO7j_DEgnKu5mK65WjJLJoApDDf4kmIYzcEw582FzpNXg0xacTUY3TDYj6ea97X0Y9Ck_Tapfpoobz4Z_4edSvJoeam8NS-AeaV3iD_UZl7BCSR1_HcFnwrP_XPxk2h5vGrHyA4Hs-pN0BYecTdM3_aYLi-xBZrTB_mChF1Be8XPd2JriJ1MUOKNOVK63N8CESdrMuTl9w56Dxpkq92sbmy0sVObVB1_6NWoLaxKyJukUlEQAyiQC7HyrjCF4v6Bq3U6s3DxES5hMh09ETIEf6IBBvbZMflXglAt3wo1Q1UoW-k9lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
🚨
دونالدترامپ رسما اعلام کردکه تاقبل انتخابات که ۲۵ روز دیگر شروع میشه به ایران حمله نخواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/141122" target="_blank">📅 20:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141121">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
حجت کریمی مدیرعامل تراکتور : آسانی مقابل ما بازی کنه قطعا شکایت میکنیم و پرونده رو به دادگاه عالی ورزش میبریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/141121" target="_blank">📅 20:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141120">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
فووووووووری گفته میشه که مصدومیت یاسر آسانی جدیه و ۷ هفته نیست
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/141120" target="_blank">📅 19:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141119">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
یاسر آسانی مصدوم شد و با گریه از زمین بازی خارج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/141119" target="_blank">📅 19:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141118">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b64ca5d3.mp4?token=EfVE-ldOV1tOn5T0x6jFsdTUv_EetXDMqlhwASFrxYmSe-sYjxvQ5xRyl3av4T0lRnZK1dcq2WCCcIAiIro6QjiASVPp2CTiGEuaErYtr3RKLdU2miAXoXtos9j02OdoE6OnB4Or79uVZ1w8rHtOFGkeDeSboRq2l0XMrGf0R5Epug9wPC17h-Gbx6oHd4s8PQnpu2Av8O07_egPg4kjwtfAiUjdwtADfz6fhRm7PLrn5DsNXGawp9eSF7OE_noqC8ijhhIu53P_NLMMZvk3L6Ex_prXrxolF9uH_ozCSv8pA7opI_YcnfyO4me4jCsPQpHYXzVhNkra8blBmpmiKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b64ca5d3.mp4?token=EfVE-ldOV1tOn5T0x6jFsdTUv_EetXDMqlhwASFrxYmSe-sYjxvQ5xRyl3av4T0lRnZK1dcq2WCCcIAiIro6QjiASVPp2CTiGEuaErYtr3RKLdU2miAXoXtos9j02OdoE6OnB4Or79uVZ1w8rHtOFGkeDeSboRq2l0XMrGf0R5Epug9wPC17h-Gbx6oHd4s8PQnpu2Av8O07_egPg4kjwtfAiUjdwtADfz6fhRm7PLrn5DsNXGawp9eSF7OE_noqC8ijhhIu53P_NLMMZvk3L6Ex_prXrxolF9uH_ozCSv8pA7opI_YcnfyO4me4jCsPQpHYXzVhNkra8blBmpmiKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اعتراض مغانلو به نکونام بابت تعویضش پرت میکنه کاپشنش رو نیمکت
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141118" target="_blank">📅 19:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141117">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS0rLvtyIhzDzTKtFoM8VFWO31RjCiBduPFuGWKJblNPZoZiWeq77rp0xkylidBzwlWqL6lw5DcdO6IEjAm_b6ZoIfc6csp4ac_mpYmxB-I5dKpFGH4ONtwbph73BstW2pKKRwpSigX1f2QQLk9JY7oMNutwn67r5GQDXYAGE0O85vEXC-XVfp5HNndGte7-elvm7ttRX5YYX1a9_ZlZlxpXJCK6L3gr7CHF0k3VFHfUgMb5nScU4nAPb6lUyKdHqRjbrMgEA005c3kDjO8c6nSEbdGsWgljwkV0krCNKC1qOh8q6Jadqdv6rYstlVL1CgEJPP98EnKc0XfWQ8WcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصاویری از آخرین تمرین پرسپولیس پیش از دیدار فردا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141117" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141116">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
یاسر آسانی مصدوم شد و با گریه از زمین بازی خارج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/141116" target="_blank">📅 18:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141115">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
کیسه نیمه اول و یک بر صفر برد و خداییش تراکتور هیچی نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141115" target="_blank">📅 18:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141114">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
ساعت 17 بازی ترتر و کیسه شروع میشه ..بهترین نتیجه برای ما از نظر شما چیه ...مساوی یا باخت هر کدوم تیما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141114" target="_blank">📅 17:47 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
