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
<img src="https://cdn4.telesco.pe/file/v86Oc6utbMeeY0UQf6ZixNb1XZ5qEeJoSvUnyi_2q889zebKEI5GeWFesJ5Tn0PNL1Zu8wMPsqOsCbj4Q5zHcPRE9JN7igugiS6-GgPzE9-dqnIKbXU-7wUHoGol2WjLWabd0uys01_5AyyhV_4MVNjv4xoBYWLujSJooPlb3z2uvHrJlLeSIoR_IeidmoBTYgNFTeaedtQLnptNy5Qya12DCn6U06EJ8fivA5g9WZC3YArLl0IX7O6bbsIyu9x59X5OyciGB4CmgiVgcvvAbjZ0pVlqxMzBEP4HbU8FfJ3VppybWlrNjAUIQbQ4jYXxCLiqyefi1Ffcsh1Xe5KbRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 111K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 09:42:13</div>
<hr>

<div class="tg-post" id="msg-71398">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0uwcYj4hrN72x4kbYJxArznDEFpuJt5NvrDKAHpvIx7IWvwwg6kzm4Z28Zc3vdNDR9MQMXfFUbYRqQOBu_69hzYHkreinsjiJfDwSTw9ghnH_7QagbLs07X813NjROifIdr_AP4zPgPERT9chHrXbRMZNCa8Vz8t5-JuRwkzIUGw9g7p8xJbdeAuAogc9SKqIzt7uZnOOyzcs9mcuBl-c2_CXi1H0vyXpTSuFMWx5qyFeOgI1FrdZD4O3jeuL_EWkRH_9pKaQa9PG5uzSNuqvcDskbNaG6yeYFEOzBsOfa3bczCZsqh-WfzRcOhJCPZ0IH8ro_fulMW_PesaE66Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
🇸🇦
رویترز:پاکستان در پی حملات گسترده گروه حوثی‌های یمن به عربستان سعودی، پیام هشدارآمیز ریاض را به ایران منتقل و از این کشور خواست تا حملات حوثی‌ها علیه عربستان را مهار کند.
اسلام‌آباد پیامی به تهران ارسال کرد و از آن خواست تا با استفاده از نفوذ خود بر حوثی‌ها، از بروز یک بحران منطقه‌ای گسترده‌تر جلوگیری کند.
به گفته یک مقام ایرانی، ایران در پاسخ اعلام کرد که «کنترلی بر حوثی‌ها ندارد.»
با این حال، دو منبع ایرانی به خبرگزاری رویترز گفتند که تهران حوثی‌ها را به تشدید حملات تشویق کرده و وعده تأمین بودجه و تسلیحات بیشتر را به آن‌ها داده است.
پاکستان اعلام کرد که هرگونه نقش نظامی این کشور ماهیت تدافعی خواهد داشت و بر حفاظت از خاک عربستان متمرکز خواهد بود، نه انجام عملیات در یمن.
@News_Hut</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/news_hut/71398" target="_blank">📅 09:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71393">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAiNYdmyDj4p0EB1cCFd_B36Ge3IdZB0aG5zWbKvVIx1dTA_Tf6SfuuFYf1pxKA6_qO4ykShaaXQGRF8_r5TJf4AOlb4lVcycSkG1pomECea2wvmn7Eiz9qvqIDi81LNb1fDuA5jMEuQK8zciPBGVE9bIvweaRV7xTHqeFgcnWB2NBI7pQU0T40Fs9zs_BS9mm0S7G5knno8wnQ1IEivNSbPBrO7hucy9ODmhKsEMRcKa0bqTzFaImv_cnx-DOr3syh7chY6BBhGZOoDi4dkHNF6klHf0RarfG6f1bIewO63JP34fB14Bxbo0zFyKnuSKqz2ADM1monrdcmv33mnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtPMy6sHCDW88EpGGew5eyznokVXl-gWoHUV9c0uZbO26mMuIkmIRadpcmmJ2CV6pS1rWNBU9U1rS3KRpZDES3IjSBNyDZd6QLR-5yo-BpCLnCQD1qy7gbXREnOvOx0W11WvMOivgtYpUWy7ADnLGOOemqyWlVlnMDmX-hqC4-kDQ-OYEQX97nRKZnL_vwVvCklNY_EsyZJExE-Yq1f2rxLRyo6gdn2E0vqKr9JZV6W37GzojQ1tfDvTF33E42ab0njFlE-bLx858AfRz7MlDcdX4C1oyRceE_IQPuQUPreC52M0IhV8qYLd2ozFXDcWtuJphP7GD_A5U5R2LaL8bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5Lk6n7UH3IiY-l5ItRif8WOhz96T5Z9s9oALjRF0osuNo3z-3OkMN6dYjVPxC2lLXyMVNVSsZ7NkxCUlGeXIi3Ajbh4pVkGWxWozVTqjSQuilerpjyWMMsBxzsb0Xhu55Q1iJW56_8nfEYje2JZRs35_LuFMH8zHnYcXrks0A3sI9A8KNBzKTO1b5vR6AZkovUc-zBNN4iom34qlxCVxKIURkzgGR1CXWKZVSf8enO3syFHPaeBms3KHIHMR4SnGxn_q3b74jzFSLDvP-6jL76EiWeQ_kKPiKvbQDkDNVybaovPjq9R2xaAk2QhYaZ1KuDLaUFTFQSWfN3SWcyUQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0nNbnxcQV32jH-RRnfQTS7DHvmGWgty4hymNcd-GxLJLC3IJoAu2ybPLuUAwwjiBnpuLtMiAUiiV-_04qNYhEmUmRTYISwiirmWKMPD84hIXBwXCQI04_VWIPr7g70y8FmA91SsbAoTpsPIUBPY0--pFUfLHd5TNaeHYwYAogCNqzdKqJQCBE1IBONGnAJjSc8aLfVF4ebZXLTijZFUQSesE59cUoA5-QHVUcCvz7Edc_KM_56cXqmJ2bLn7LMSdRObXp4DQmZ9xTr-NwkPxCGgE1ROTDtKxrk_JB6vWhWcYrteCcjrPzKUx1tYsTqh3-Xr8S5XJKYQimHRtOUicw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=vkS4kpETtVVmLYAKhUdmPW0H-tBNPsBtMXfZZI0PMiBzpuRXUQV40c6EKo86iQuSaz9eBZAKo9dIPCF6_4sCNwBziUt1_VWjRB4Bs6NEk0_69qgRyIRlmVGhKWlyPgEaJbX2b8C8K6d7P4M9oZQSoxMq6aR1P63uwCLT4GU_2iS7xS_-fYeJHHovfMRT_VSUAt-tSh2lNAoi258jIDM94vBB63B5BE4t4lsdfNJN60cTtd4MA0bSP5qYtCVF1RMr9oeP5ULxTL-5nAxhxbO-SYjmoXmp1x_2C7lk6LJ4tNH0BgKjFtMw9cE09jkRssbENkVCWDZye8kS3t7traw7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=vkS4kpETtVVmLYAKhUdmPW0H-tBNPsBtMXfZZI0PMiBzpuRXUQV40c6EKo86iQuSaz9eBZAKo9dIPCF6_4sCNwBziUt1_VWjRB4Bs6NEk0_69qgRyIRlmVGhKWlyPgEaJbX2b8C8K6d7P4M9oZQSoxMq6aR1P63uwCLT4GU_2iS7xS_-fYeJHHovfMRT_VSUAt-tSh2lNAoi258jIDM94vBB63B5BE4t4lsdfNJN60cTtd4MA0bSP5qYtCVF1RMr9oeP5ULxTL-5nAxhxbO-SYjmoXmp1x_2C7lk6LJ4tNH0BgKjFtMw9cE09jkRssbENkVCWDZye8kS3t7traw7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
شرکت اپل با انتشار این ویدئو، رسما و شرعا از آیفون 18پرو رونمایی کرد؛
🎨
این گوشی تو چهار رنگ عرضه می‌شه:
• زرشکی / شرابی (Burgundy)
• مشکی تیره (Deep Black)
• آبی یخی (Glacier Blue)
• نقره‌ای (Silver)
@News_Hut</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/news_hut/71393" target="_blank">📅 09:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71392">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/71392" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71391">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YiP3scPygf7TtU9kkNSQkddHBf1yDJYvsBCv0hQGxNsEGNGUuuJF685kUBOzbWBISeBbQamnWaJHrtzN4IZUNFyeZNkb0LE5K2Xcs4b_tdq0ycQbPs2Mu6_B918eQoeaWu3n_l6uwYL1JrQdivGT90AzOir71qES1VMe3dNKmYHH4asiPxJm87KDRsPCG_89hZdgh8BHilOOeuf1JJYIgD3gAtdmd9piBXKa4CNgXBPzDAoiItMzkglo7fWAZnHzICQLxhj-yvz_yOJWGz9zBd3lhCZF39U1TImM3M17FTzLt9VtvRB2RGpX9koEISGd0t29RqjNYoa4tQxQ0Io4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71391" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71389">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3GLnIoprc-PEsnPW8108z5-34U6TYToSnRAhgEed-nHb68QgGdGaFELLcaaXirR7cS78WxmJgEiKooxSAD9r2mU_v0oi25FHBjW9C4x4YKv4z4QZiv-I45qZSS7KbHHQFDRYCzIPzzgrMQe5PAOqxocq9gtFLYMS_jJ0McAH-gV1qqp4IT9xdQE5Kt9NTFTtDfaGD_Nbcm8BcA8cC_jpOJmLIX5QV2jK80tmHYT-HA0btxR2mg1uyoRraqMM9PiaZQKt53mga5LHfMVC6SffVu4q69g5chp1qJyvcqAjpXkiYM9WEaJb8hKW9uLQ0-lFJkBfrWtYy5mW6kL5_WThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X61ZyTFZj0tHRTiFRoaiW7SDYNLofDncnxZmEanK5mrpZVQaIrIAq7_3xLEN9Q-9JVWHlq7fmHKW0BEfb3xmHJQBpgRFRCcWjCM7ODkXZXgaTL7lvmlsRjoWI44kceWdhQAZUc-ndtXaubfLR2m6FXaGyIvYZ-2OyUDMU6Zkj8vYK-fPTokE8aTolHIjnk-6mZE3EiARA5yvDyVQ-3f2sLnUAQ-7Q2vIIbEYENQGIBaaIPlQ5xOuvlR4n81loJTWpoFj9P_P-HKTN08FN9BRZ64UtD6dSEejw0xrzqRl73tDXgSoTwqJI23Zzgduh1TnXxF7arGLCKoSyJUWRAauKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
به گفته منابع عربی حوثی ها وارد منطقه حیس شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71389" target="_blank">📅 01:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71388">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
فارس:دقایقی پیش صدای چند انفجار در مناطق ساحلی سیریک و قشم و مناطق ساحلی شهرستان میناب گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71388" target="_blank">📅 00:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71387">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
گزارش ارسالی از قشم:
قشم هم در خونه ما لرزید
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71387" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71386">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
دقایقی قبل صدای یک انفجار مهیب همراه با لرزش زمین در کوهستک (هرمزگان) شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71386" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71385">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=mncAUwasxpijFZP2k1NL2iK-_RL5EiJuO6NWNrtlgqr3G9cFGX6uIFA2AT5FNnaTQzFu1hF-pMtj3jrXaYvK4jO6b2H5czBjzg5qKxT56QpWyhkUYicQGc5SqoOxe3689FAzXSBTrn3ggXgI00G0HIXHT0yJJ-sKa7ejdG1kWPpONjFEdbztRwtSWvN4CmhDYMkBNtRBvo3v9rwcv3kwtyIDmyW1uXqBJmWT8nEoOR0-TbFzDGGFlykEvmWMeA-p1nK9dAwWounPXGJNM_qG0hpyB-ZgNmNGj4Gpx49Xk9noxu0jmJNadqmE2d2JIzpxA-ecduXffD1LhQgwNItpIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=mncAUwasxpijFZP2k1NL2iK-_RL5EiJuO6NWNrtlgqr3G9cFGX6uIFA2AT5FNnaTQzFu1hF-pMtj3jrXaYvK4jO6b2H5czBjzg5qKxT56QpWyhkUYicQGc5SqoOxe3689FAzXSBTrn3ggXgI00G0HIXHT0yJJ-sKa7ejdG1kWPpONjFEdbztRwtSWvN4CmhDYMkBNtRBvo3v9rwcv3kwtyIDmyW1uXqBJmWT8nEoOR0-TbFzDGGFlykEvmWMeA-p1nK9dAwWounPXGJNM_qG0hpyB-ZgNmNGj4Gpx49Xk9noxu0jmJNadqmE2d2JIzpxA-ecduXffD1LhQgwNItpIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ:
این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای مسلح ایالات متحده را به چالش بکشد.
🎙
سخنگو:
او به جهانیان یادآوری کرد — همان‌طور که بارها و بارها گفته است — که آمریکایی بودن، نمادی از چیزی شکست‌ناپذیر است.
اگر آمریکایی‌ها را بکشید، یا هر جای این کره خاکی آن‌ها را تهدید کنید، ما بی‌هیچ عذرخواهی و درنگی به سراغتان می‌آییم و شما را از بین می‌بریم.
ما آغازگر این جنگ نبودیم، اما در دوران ریاست‌جمهوری ترامپ، آن را به پایان می‌رسانیم
جنگ آن‌ها علیه آمریکایی‌ها، به انتقام ما از آیت‌الله‌شان بدل شده است
🔴
ترامپ:
خطاب به مردم بزرگ و سرافراز ایران:
لحظه آزادی شما فرا رسیده است.
وقتی کار ما تمام شد، کنترل حکومت را به دست بگیرید؛ این حکومت از آنِ شما خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71385" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71384">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71384" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71383">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=NZCbj1jercCy7eNirCDNVjryrESWXS2ARQIz0C02V-xCzY50ljmC8rtjmrBp8z9ABUUZyVXoGVXCy01EsNuiYe7Sdn18CqwBID7lZwr4Jj9rYZHC_el8lwGK_v1MkHkbYfNbv-qJBjz61DQ-1gwjQh-broksJQGTOpFVMkH2aE9IRguD1hpfMJNM0dSsZQZkWF1LKpRQkPnXE7DwU-fvM-xLA1ze8sLvmc0goKaacxarNzxpTAQiINPArskGjeDcyQhU7HazB49QfmPo2el9rpPbSam_w9AsbqOQCpFV8BzR1zLrfLbF1wta25Pa5C7GR4Fx1wZNSqDCO8iHx0k7-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=NZCbj1jercCy7eNirCDNVjryrESWXS2ARQIz0C02V-xCzY50ljmC8rtjmrBp8z9ABUUZyVXoGVXCy01EsNuiYe7Sdn18CqwBID7lZwr4Jj9rYZHC_el8lwGK_v1MkHkbYfNbv-qJBjz61DQ-1gwjQh-broksJQGTOpFVMkH2aE9IRguD1hpfMJNM0dSsZQZkWF1LKpRQkPnXE7DwU-fvM-xLA1ze8sLvmc0goKaacxarNzxpTAQiINPArskGjeDcyQhU7HazB49QfmPo2el9rpPbSam_w9AsbqOQCpFV8BzR1zLrfLbF1wta25Pa5C7GR4Fx1wZNSqDCO8iHx0k7-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
پرزیدنت ترامپ:
انجام کاری بسیار فراتر از توافق هسته‌ای.
چیزهای بسیار بیشتری از هسته‌ای وجود دارد.
ما به توافق هسته‌ای خواهیم رسید، این ۹۹.۹ است، اما چیزهای بسیار دیگری روی میز خواهد بود که سه ماه پیش روی میز نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71383" target="_blank">📅 23:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71382">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=TdbaI533OtqtZ84qRBSYHNyIeVbKmZR1fM-MGeYofKr2UdShWdCWAb-mJvgXBydC-Bt9lWncUCp0eN0VrD3OXzesKeQ_V5DBdvYNZP_7l348CEMXWe20Tpi_cP7ve60EiadWdzZERe7mQ-SusXvaDd-nM4J7Ewg_3NeWAQxMdxh-WHiO-rEHhVrvAETeKex2SwC9b-ts4oKGWo0ZYjeaQ9vBVhYRmN5EZ8KbSt1EelH4uaSRQ73UvydPbg1QvDJo_nfADJjF_JWyA79BKJZFfXaID7sKxTe6uQaonf46_ObGQraBBBp2Y-D20962gsSvdQ_X4jm0wNKZiiy9LjwUJ6FHYFn7bhLUUj43QjrUvzxkCB6igxZFz6-VhMihqSLYs3tfF4FJwTa0UpLnO4hqdTg6TPVhrSbNFbSWO-qG2xrEVG-pyXt7DpKHcb1Fb4DkSBT2nPfy4T7jq1pd1RB2IXV_Y2V_VfPVSxqUv1ZKTrJ9QfXVfovrdupf3z-Ovrawxf8zf5tlaVfZpdLOBOKrG3WldBDUWmd3oRUSh9vqwoiWnbGq87LmPQFdntnGn3hzqsIeYlZCxJLaqH0ANUGIgQU01zwZqJgJu6G6ESqolwyHVf5z_TkIGT16kZRg9YNgkUFTUNCOxb0qDJ7b8T1r3_TlRjJm9KV64sMKGk36zeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=TdbaI533OtqtZ84qRBSYHNyIeVbKmZR1fM-MGeYofKr2UdShWdCWAb-mJvgXBydC-Bt9lWncUCp0eN0VrD3OXzesKeQ_V5DBdvYNZP_7l348CEMXWe20Tpi_cP7ve60EiadWdzZERe7mQ-SusXvaDd-nM4J7Ewg_3NeWAQxMdxh-WHiO-rEHhVrvAETeKex2SwC9b-ts4oKGWo0ZYjeaQ9vBVhYRmN5EZ8KbSt1EelH4uaSRQ73UvydPbg1QvDJo_nfADJjF_JWyA79BKJZFfXaID7sKxTe6uQaonf46_ObGQraBBBp2Y-D20962gsSvdQ_X4jm0wNKZiiy9LjwUJ6FHYFn7bhLUUj43QjrUvzxkCB6igxZFz6-VhMihqSLYs3tfF4FJwTa0UpLnO4hqdTg6TPVhrSbNFbSWO-qG2xrEVG-pyXt7DpKHcb1Fb4DkSBT2nPfy4T7jq1pd1RB2IXV_Y2V_VfPVSxqUv1ZKTrJ9QfXVfovrdupf3z-Ovrawxf8zf5tlaVfZpdLOBOKrG3WldBDUWmd3oRUSh9vqwoiWnbGq87LmPQFdntnGn3hzqsIeYlZCxJLaqH0ANUGIgQU01zwZqJgJu6G6ESqolwyHVf5z_TkIGT16kZRg9YNgkUFTUNCOxb0qDJ7b8T1r3_TlRjJm9KV64sMKGk36zeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
در مورد ایران؛ آیا انتظار دارید که [چنین روندی/مذاکره] زمانی آغاز شود؟
🇺🇸
ترامپ:
راستش را بخواهید، جف، ما به دنبال چنین چیزی نیستیم.
در ابتدا می‌خواستم به توافقی برسم، اما اکنون کار از آن مرحله خیلی گذشته است.
در حال حاضر چیز زیادی از کشورشان باقی نمانده، بنابراین ما به دنبال آن نیستیم.
بله، شاید مذاکره‌ای صورت بگیرد، اما این چیزی نیست که ما در پی آن باشیم.
🔴
این جنگ بلافاصله پس از انتخابات ما پایان خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71382" target="_blank">📅 23:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71381">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtkHESg6lEmmg5Zmdt7Bs71EEsBoYb_zUPlfGHafNze8pDvdZGR5VHlmpO0_G1IPJKkbjy3ilxoP0C0DPQpECLQ5GDYZCJ3RqM1skWnxvWa0mHrAjyYUzU6Qw6at2cAoHd3u7_Tcu6hqBSTtf0CCosv62RDWIe6KriYkSicdgW9DjITU3h7v-5ETqWweSCaRu1Di8jx8Bwy3fcms_fh5TnompUbEVZHhsxw1JZk7MlVZ78mDqWT0CkCsiRqUgA1LUS3adx2mOSUYWGBYcWvC1lqlIzGTRVO0GFK9ERRdDdjUfV9jwMFdrnrJoZAhon9pzaOMxyffOW7Wq26OLeD1POlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtkHESg6lEmmg5Zmdt7Bs71EEsBoYb_zUPlfGHafNze8pDvdZGR5VHlmpO0_G1IPJKkbjy3ilxoP0C0DPQpECLQ5GDYZCJ3RqM1skWnxvWa0mHrAjyYUzU6Qw6at2cAoHd3u7_Tcu6hqBSTtf0CCosv62RDWIe6KriYkSicdgW9DjITU3h7v-5ETqWweSCaRu1Di8jx8Bwy3fcms_fh5TnompUbEVZHhsxw1JZk7MlVZ78mDqWT0CkCsiRqUgA1LUS3adx2mOSUYWGBYcWvC1lqlIzGTRVO0GFK9ERRdDdjUfV9jwMFdrnrJoZAhon9pzaOMxyffOW7Wq26OLeD1POlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
لطفا شهربازی که میرین هر چی رو سوار نشین؛ بعضی موقع‌ها همچی مناسب نیست و شیطنتتون گل نکنه بخواهین یه تجربه کنین.
این فقط دیگه نریده بود تو خودش...
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71381" target="_blank">📅 23:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71380">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owkasB1Lyo07PASVBFJOlmFXWKe3z9haj__PtuwdaKZBtXomIHr4LlnJVA5ZaJFUa9VmEHVH_OnwHz6YzTu_TsirqpVpjjoEaf4FNxkjAOolpgBj-m-QIpKse0SeeaUNvzLlAo4P_0_O9TS68TuPAzXaszez5ecF1jN9fpVQlLRPcs36O6vUh38jAKSd0yhPXYFWTz3eXEZ0HXyDxgDQ53YTEBUHlVMNpGDEXOQzZAfX15EY079OH79x0wG2iDbZcd8XP8QoMnZsZGz70aWzWlEV5H4mdcv-KWGjdTPxsjXGQikyqqbLXHIclv6IbGoWXgA7XMMRm6LgpmU_reB44IdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owkasB1Lyo07PASVBFJOlmFXWKe3z9haj__PtuwdaKZBtXomIHr4LlnJVA5ZaJFUa9VmEHVH_OnwHz6YzTu_TsirqpVpjjoEaf4FNxkjAOolpgBj-m-QIpKse0SeeaUNvzLlAo4P_0_O9TS68TuPAzXaszez5ecF1jN9fpVQlLRPcs36O6vUh38jAKSd0yhPXYFWTz3eXEZ0HXyDxgDQ53YTEBUHlVMNpGDEXOQzZAfX15EY079OH79x0wG2iDbZcd8XP8QoMnZsZGz70aWzWlEV5H4mdcv-KWGjdTPxsjXGQikyqqbLXHIclv6IbGoWXgA7XMMRm6LgpmU_reB44IdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ:فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام می‌شود.
دلیلش چیست؟
چون دیگر نمی‌توانند دوام بیاورند.
آن‌ها به‌شدت تلاش می‌کنند بر انتخابات تأثیر بگذارند تا گروهی ضعیف و مطلوبِ خودشان سر کار بیاید؛ کسانی که کاری به کارشان نداشته باشند و بگذارند به سلاح هسته‌ای‌شان برسند
تمام خواسته‌ی آن‌ها سلاح هسته‌ای است، و اگر به آن دست یابند، کل دنیا دچار دردسری بزرگ خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71380" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71379">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=i5UAizQFPg6V6KN7djTZ9BQrpMUIxCyACEaAwp28EdmTrdLzhtMbNxlnZo_y1HvWM-10C8PJ-BLQITHjL315GmXxIdJpGKq3i3yQuKaQSOIwkXt71Hso4Ea5Ax0QfTsEMXiXkviQS5JsnZs4MjQdM8fVASwQyK2lXHmYxC2G8K1Vq-dTyVnH8W33dfeXROfE2KJIowu1CCirAhEWE5ovXAO89uLBXp5vaD6zzL3KkJ7H7tEhzm8KQXRfj6XD62uO3cMBJNjY2r5kNgGw-I2ftjGB7teFLkuNkoAIzm7uq8-MivRX1p4sQq7IsODb6Mq1AKfeFfyHMZ6cjj-uSOOElg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=i5UAizQFPg6V6KN7djTZ9BQrpMUIxCyACEaAwp28EdmTrdLzhtMbNxlnZo_y1HvWM-10C8PJ-BLQITHjL315GmXxIdJpGKq3i3yQuKaQSOIwkXt71Hso4Ea5Ax0QfTsEMXiXkviQS5JsnZs4MjQdM8fVASwQyK2lXHmYxC2G8K1Vq-dTyVnH8W33dfeXROfE2KJIowu1CCirAhEWE5ovXAO89uLBXp5vaD6zzL3KkJ7H7tEhzm8KQXRfj6XD62uO3cMBJNjY2r5kNgGw-I2ftjGB7teFLkuNkoAIzm7uq8-MivRX1p4sQq7IsODb6Mq1AKfeFfyHMZ6cjj-uSOOElg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شاهد حملاتی در تنگه هرمز بودیم.
🇺🇸
پرزیدنت ترامپ:
خب، این حملات... این حملات کار ماست. ما 9 تا از کشتی‌هایشان را از کار انداخته‌ایم. بله، می‌توانم بگویم که این حملات از جانب ما انجام شده است. اما... و خواهید دید، خیلی بیشتر از این‌ها خواهید دید... وقتی که به آن ضربه بزنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71379" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71378">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=BYj5ZDcfcslyuQXV_tY2NHd7ME7UMGefEPksdh_MjCJWgf5UYJb75I7zQp9nKHUXS74xIADWhSz0229SQBeNCpSxXgg_GRHsTfildTm9o7MQ7_AfnwU3d-VydE_Cz6zI5z5Df0vcioIG3oIuKyqcZjXbritf215UNwIqprszhggvdbXaBoy2Zg-TwIiFfY5n926DrWVNClhOVq8QPwkUC0NFT6Dm3ifX8u4BvOrWdkoYnBbiBH2TFZu1WparJD881Q9OkCs93W9hJGcjJ_HUjS0Y09KLcnkhU4c157SbQokapbykpEeAn6eX5IxxN_US9NuxEUlqZ9qWyzFiXQYL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=BYj5ZDcfcslyuQXV_tY2NHd7ME7UMGefEPksdh_MjCJWgf5UYJb75I7zQp9nKHUXS74xIADWhSz0229SQBeNCpSxXgg_GRHsTfildTm9o7MQ7_AfnwU3d-VydE_Cz6zI5z5Df0vcioIG3oIuKyqcZjXbritf215UNwIqprszhggvdbXaBoy2Zg-TwIiFfY5n926DrWVNClhOVq8QPwkUC0NFT6Dm3ifX8u4BvOrWdkoYnBbiBH2TFZu1WparJD881Q9OkCs93W9hJGcjJ_HUjS0Y09KLcnkhU4c157SbQokapbykpEeAn6eX5IxxN_US9NuxEUlqZ9qWyzFiXQYL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
کمی بعد، اما درست بعد از انتخابات، چون آنها دوست دارند اوضاع به این شکل باشد، اما درست بعد از انتخابات، قیمت نفت رو به کاهش خواهد گذاشت. قیمت‌ها پایین خواهد آمد و فکر می‌کنم قیمت بنزین را پایین خواهیم آورد، به زیر ۲ دلار در هر گالن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71378" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71377">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=NBNmLCCdQkqJVbn20bRJXswAXBF9xErgpIkcGNXDLHNYD8_uLvbVwYSn4FXg2J37rE-1kQ2odXYxPz-tlc8IN6Eg9tp4Yl_YVkDwDLGpNkRhWb5YXcN1e1bx0TJy1XAHdILB7KrWrDug2isC4dw91atl1ap53ptH_fPio9T35QFQmCKtCWGJxGr6YuKXNgAkugqD28w8O6518MSfhMVRsy7ycBTWPW9gbsV-1x2OCgpqOSzb5GQV6YdIUxr2ZJBnIKBBVmk2htBTFMEr_RjE4aVC7tNEhFKwFXcbXGIPXqMEaTnqA9oravMcWTl0KGFx713SwzKCfydKj1Xv9BPj9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=NBNmLCCdQkqJVbn20bRJXswAXBF9xErgpIkcGNXDLHNYD8_uLvbVwYSn4FXg2J37rE-1kQ2odXYxPz-tlc8IN6Eg9tp4Yl_YVkDwDLGpNkRhWb5YXcN1e1bx0TJy1XAHdILB7KrWrDug2isC4dw91atl1ap53ptH_fPio9T35QFQmCKtCWGJxGr6YuKXNgAkugqD28w8O6518MSfhMVRsy7ycBTWPW9gbsV-1x2OCgpqOSzb5GQV6YdIUxr2ZJBnIKBBVmk2htBTFMEr_RjE4aVC7tNEhFKwFXcbXGIPXqMEaTnqA9oravMcWTl0KGFx713SwzKCfydKj1Xv9BPj9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه هموطن بعد از گرونی بنزین زد به سیم آخر و از بالا تا پایین مسئولین رو یکی کرد.
حاوی الفاظ رکیک، هندزفری لازم
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71377" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71376">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGBjchYjTo1VsigFjIPPFjAZAndno88yVrHfL9EinoHefCoWAUEfAfGrzpZzZuefo-f7GiQcdsAkxqlFsPkiQRv6pL9qWflMkuIhuNOx7ENoVqxeB-rDfQAcAl28iCKtk7vMGbygr8ccbFFMNXfAIJVtvI5_dHhsNjHWQuwGJ3_5UnWhhoBHsw0WH1NjrsW5dgcQ6r0zxUUUVR78Ty0m-S6hC33MvQRej0_eXbdH8Ef7nDGJsuj4ATA35Wl8HqsoUbiLTROR_7Y3sho-Z1gw0D-Fo2UwtHyooqRTRvJuOmYP8TnqH_WFDTYuKXF5Ki38u-7m7VwikZfG_vianrHj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
به گزارش «نیوزنیشن»، دونالد ترامپ همچنان در «بال غربی» (West Wing) حضور دارد و طبق برنامه، هنوز عازم دالاسِ تگزاس نشده است.
ترامپ در حال دریافت گزارش اطلاعاتی به همراه جی‌دی ونس (معاون رئیس‌جمهور)، پیت هگسث (وزیر دفاع) و ژنرال دن کین بوده است.
احتمال می‌رود این جلسه پیرامون موضوع ایران باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71376" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71375">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f299161.mp4?token=c--xFjwwPjfI7-nKX6w09apkVJ3R-tf5EJpbNfJdk2IlpieoZxnIlez5hG5ulUkr9VpnuI9Cdt2VmEzFkGdASSdMskkrb7xkxOnB1_L125P9EabAx6Oe0aY4vlFUZd95i_lC3Gb1bP5CTduco4VAz0JqjU5lOKrinQZdprWZCk4_nfx4jXAhpJ9Q507Xx3EwCTGud4hLUeJDUERrurSpPucwdltL-ssigFVs8UnTPODsEKFsdwqVrHgU1g6wMU-t4BAcpCnJaI0g4NVnk0zO7UVd8--aQR8-Mtc1T-XpQZH7PgE06eb46TtBTWnOoynJGvqiYRihkxYkwghHZur9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f299161.mp4?token=c--xFjwwPjfI7-nKX6w09apkVJ3R-tf5EJpbNfJdk2IlpieoZxnIlez5hG5ulUkr9VpnuI9Cdt2VmEzFkGdASSdMskkrb7xkxOnB1_L125P9EabAx6Oe0aY4vlFUZd95i_lC3Gb1bP5CTduco4VAz0JqjU5lOKrinQZdprWZCk4_nfx4jXAhpJ9Q507Xx3EwCTGud4hLUeJDUERrurSpPucwdltL-ssigFVs8UnTPODsEKFsdwqVrHgU1g6wMU-t4BAcpCnJaI0g4NVnk0zO7UVd8--aQR8-Mtc1T-XpQZH7PgE06eb46TtBTWnOoynJGvqiYRihkxYkwghHZur9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🤡
اوستاد خوش‌چشم تحلیل‌گر ارشد صداوسیما:ما به سوی یک درگیری تمام‌عیار و کوتاه‌مدت در پاییز می‌رویم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71375" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71374">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNOiIN7V-TVXvn0P-7r_pAQ_g4R1viyxVnoX3Z7c-zA0_RLjhJ5DgLzyPpAflCN4BpQGcotdMoh5Bw7H40w6YCf3JsXu5e5C_IkGW47A7A1Z0w4iJGXnYzH_AOkwWQE8cNk78D01dLSPoyxz0BqVlZUrlzfXSvQcTwKUJibH6lBQE4P_NQHozAiwhPdRGzQrBvBFXz-yEfmrSXA_HmRWgkFV3bk2Z2KtOzXqOhKupwuvlICCp0C1F_JdfNFo0DLDo_lY1DBRrFKVJU60KoGc1OKYjtMyieRh9HHAisSw0NEssvmOlCK93HsXqwR5Y1imZ-wqiW49TMouvVy7_sp6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
تصویری زیبا از رعدوبرق دیشب تهران.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71374" target="_blank">📅 20:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=GvL6ypJg7W46w0Xe0gX_Y3CfRqJ2yb2gXRiZcxqboloUIdHRxwBL_W8OCZKkyPzhcPqu06aggrc0ol07_I9N178FpFSW06E6tDdN6GQKU6kDuzs75BmBpTjaF4bxtgGvfY8LaLYcfUux4gyjA8bnrKIQIOuccXV46paMn_ZyHugDEsddC2DVkpwjjL1eT6HxtXRj1QT_yaQhioQicvNle_Kxa96F_NPPi6asaC_pZ9KaK-eNEc-u-pEyAjHgiGWqDTfsepz2f2NQacbPj6H5epbbnA1le-nFfIgtMAl8Fh-7tOhtyeKfziFB1J8LBmJHeMDyKxOosbWoh3Mk07HofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=GvL6ypJg7W46w0Xe0gX_Y3CfRqJ2yb2gXRiZcxqboloUIdHRxwBL_W8OCZKkyPzhcPqu06aggrc0ol07_I9N178FpFSW06E6tDdN6GQKU6kDuzs75BmBpTjaF4bxtgGvfY8LaLYcfUux4gyjA8bnrKIQIOuccXV46paMn_ZyHugDEsddC2DVkpwjjL1eT6HxtXRj1QT_yaQhioQicvNle_Kxa96F_NPPi6asaC_pZ9KaK-eNEc-u-pEyAjHgiGWqDTfsepz2f2NQacbPj6H5epbbnA1le-nFfIgtMAl8Fh-7tOhtyeKfziFB1J8LBmJHeMDyKxOosbWoh3Mk07HofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
#فوری
؛شورای حکام آژانس بین‌المللی انرژی اتمی امروز، ۹ سپتامبر ۲۰۲۶، قطعنامه‌ای را تصویب کرد که بر اساس آن، موضوع هسته‌ای ایران به شورای امنیت سازمان ملل گزارش می‌شود. این نخستین ارجاع از این نوع در حدود ۲۰ سال گذشته است.
۲۳ کشور موافق قطعنامه بودند.
روسیه، چین و نیجر مخالف بودند.
۸ کشور ممتنع دادند و یک کشور رأی نداد.
🔴
قطعنامه با ابتکار آمریکا، بریتانیا، فرانسه و آلمان ارائه شد.
دلیل اصلی اقدام آژانس، عدم توانایی بازرسان در راستی‌آزمایی کامل مواد و فعالیت‌های هسته‌ای ایران و پاسخ نگرفتن درباره آثار اورانیوم کشف‌شده در برخی سایت‌های اعلام‌نشده عنوان شده است.
آژانس همچنین می‌گوید به دلیل محدودیت دسترسی، نمی‌تواند با اطمینان درباره میزان و محل ذخایر اورانیوم غنی‌شده ایران اظهار نظر کند.
⚠️
اقدام بعدی در شورای امنیت خواهد بود و هرگونه اقدام الزام‌آور جدید در آنجا با توجه به حق وتوی احتمالی روسیه و چین با موانع جدی روبه‌روست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71373" target="_blank">📅 20:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71372">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=A8aVUNQCSIB7c9l5MXtXcf2JTvPF2HYGbgBJrYQK6xYSWi-1tlHrxBzuUQmsfpXVXHgnIwhikAUguxFwkWvuNhxLXw9yAQnab6iZjJmEfeK85mDZQG-k-FSvLRISOxvTr8TMNJoBcSi49L6k4gvfzM_sjcMHeQrJPEZ9DyvCz_iGKOhU3B2cHcGDyKiWufMtbgQxYq_h1PPDpzxuAntanECiyiThtNx4zeOhED1snx6JezhhwyMRKEP6Hone4rrmEKcTi8t2DzKxpcFnZNNoIQJmZZ3WAa4LW6fGjhhPLa0Soe1gAmrRrhwfFwCPgN-f4dk3xqWHdaQhC-FTfikuBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=A8aVUNQCSIB7c9l5MXtXcf2JTvPF2HYGbgBJrYQK6xYSWi-1tlHrxBzuUQmsfpXVXHgnIwhikAUguxFwkWvuNhxLXw9yAQnab6iZjJmEfeK85mDZQG-k-FSvLRISOxvTr8TMNJoBcSi49L6k4gvfzM_sjcMHeQrJPEZ9DyvCz_iGKOhU3B2cHcGDyKiWufMtbgQxYq_h1PPDpzxuAntanECiyiThtNx4zeOhED1snx6JezhhwyMRKEP6Hone4rrmEKcTi8t2DzKxpcFnZNNoIQJmZZ3WAa4LW6fGjhhPLa0Soe1gAmrRrhwfFwCPgN-f4dk3xqWHdaQhC-FTfikuBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
ساعاتی پیش، چندین حمله هوایی عربستان سعودی در حمایت از عملیات «شورای رهبری ریاست‌جمهوری» (PLC)، مواضع حوثی‌ها (انصارالله) را در جبهه مأرب یمن هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71372" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71371">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71371" target="_blank">📅 19:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71370">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqAIDyxRaO5-3WQOrttPODZnbH64PPzm_bdeLxb0yzWVE7_Sa5XTVkyVuZrhaTxtuWdyYTvwijQzryxNsIZcLI9hVLtAt2CrYtnC8TZ_WTuoYEKhZAWpMb5tBZm7h5mtXntmt0iFaS7w_iRrEjkc75sir_ZY-wMrtp9V46OEsrzxzfhYRJYPzl3MvFKX2aPx4H8x4vQdFjS364_mZ5iv8jiZ25XA67PkWhne1mqtpNBkd7rtpdAaim8LWqUJNeTAGfxxCyB-MrKneMwMRzZuiwo8eMHgICPkKqCKeLzNgBUOW863Yam0VH7x78DRyy7XcPhuz9cBzcUTDU1Jqm78nIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqAIDyxRaO5-3WQOrttPODZnbH64PPzm_bdeLxb0yzWVE7_Sa5XTVkyVuZrhaTxtuWdyYTvwijQzryxNsIZcLI9hVLtAt2CrYtnC8TZ_WTuoYEKhZAWpMb5tBZm7h5mtXntmt0iFaS7w_iRrEjkc75sir_ZY-wMrtp9V46OEsrzxzfhYRJYPzl3MvFKX2aPx4H8x4vQdFjS364_mZ5iv8jiZ25XA67PkWhne1mqtpNBkd7rtpdAaim8LWqUJNeTAGfxxCyB-MrKneMwMRzZuiwo8eMHgICPkKqCKeLzNgBUOW863Yam0VH7x78DRyy7XcPhuz9cBzcUTDU1Jqm78nIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پسر‌بچه ارومیه‌ای که چند وقته به شدت ویدیو هاش وایرال میشه موزیک جدید داده بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71370" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71369">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=F4kW1sC9NbybkpJf3P7f4LSKXBzReg2t5TopkSswMZq7c_RzDljKPgj4dXfWczl_YX4t92m7vqcSLATtEBMFb4idt1NXZsSAlfyXwE5g6Dj8aQ5oR3X-6BEyxrwh2tCCuo6sg3IneZV7V8jkLhVy7xoNbayqSE-OcNoA-FoWxvockqZjFp0IrtaHihNmr-lQg5dtUYzZEtXy8iV0pTRDDA_Zckft1wWcdTykEnG2ahBohWGcyKJV4LuMYuR_8Ptzxj4oFH2KP_9N-05ZAjWD8hVk8r_qZUikU4gv9dSU0IFlav096DBCJhLfL1oL0IKQu7vs-RJPCHQsjAOUBkYdKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=F4kW1sC9NbybkpJf3P7f4LSKXBzReg2t5TopkSswMZq7c_RzDljKPgj4dXfWczl_YX4t92m7vqcSLATtEBMFb4idt1NXZsSAlfyXwE5g6Dj8aQ5oR3X-6BEyxrwh2tCCuo6sg3IneZV7V8jkLhVy7xoNbayqSE-OcNoA-FoWxvockqZjFp0IrtaHihNmr-lQg5dtUYzZEtXy8iV0pTRDDA_Zckft1wWcdTykEnG2ahBohWGcyKJV4LuMYuR_8Ptzxj4oFH2KP_9N-05ZAjWD8hVk8r_qZUikU4gv9dSU0IFlav096DBCJhLfL1oL0IKQu7vs-RJPCHQsjAOUBkYdKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو بجنورد، فردی که سال‌ها با معلولیت شدید تو یکی از خیابون‌های شهر دیده می‌شد و مردم هر روز بهش کمک می‌کردن؛
به محض دیدن پلیس کامل درمان شد و درلحظه به‌طور کامل کاملاً شفا گرفت.
طبق گزارشات این فرد روزانه چیزی بیش از 20 میلیون‌تومان درآمد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71369" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71368">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Djc2buSiJ0pCKkotMSHkZt3L0-kUTvmZ-c7GBLMj3R66acEyp0_GuCni1L1AUdsMG9rnQHlB2tIdYdVM--IN3FOhR8vpMo34rANzVOCE9pzfJtJpYlagqor2zutCOqBHMChSPPdrQQ4S6gcVlEay2a6PVg1CNvHay3O7Mv4XfX3PVH7S8YcX5dLQT7vabGTT3It52Rr_fCrzT9MtKAXP1X2Rg_0QmeUTulXnu8frH8Ynn-uk9DgU_76AdTYvzr-zcNKS_KT11xjjW-HwjlV488U0dAzzxvfn8T9bvQPFOTVuYllFbe4xXvOtr7_-uR8fLfYjWsphkacrPd1AnNxCJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Djc2buSiJ0pCKkotMSHkZt3L0-kUTvmZ-c7GBLMj3R66acEyp0_GuCni1L1AUdsMG9rnQHlB2tIdYdVM--IN3FOhR8vpMo34rANzVOCE9pzfJtJpYlagqor2zutCOqBHMChSPPdrQQ4S6gcVlEay2a6PVg1CNvHay3O7Mv4XfX3PVH7S8YcX5dLQT7vabGTT3It52Rr_fCrzT9MtKAXP1X2Rg_0QmeUTulXnu8frH8Ynn-uk9DgU_76AdTYvzr-zcNKS_KT11xjjW-HwjlV488U0dAzzxvfn8T9bvQPFOTVuYllFbe4xXvOtr7_-uR8fLfYjWsphkacrPd1AnNxCJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازی مناسب برای جوانان خاورمیانه ای:
یه سایته یه بازی ساخته، میری توش بمب اتم مورد علاقت رو انتخاب میکنی و میزنیش تو شهر مد نظرت و بعد بهت میگه چند نفر رو کشتی
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71368" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71367">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCrMBgiod3AAtxGHnbsryD4SYpptlUHSFRa-V4eusO2gWJ5zmVQkXtKk598FWyhcjiKI8xeuJYQXCN74ixaiUqzTG4vapo1m24_HDaLh3wY802KwzJppVwBZvhy3RYZSjRjDqJ4mIFLz2wtb828r5AsantxirbwjN_ZEua6FxsLRr0nXjSdfH_HUNAbvusccorzWJMM7kb4daWcd55XPvOa-GKIIxMEQVE8bXRx1Dg1y_Bf7s_rXWXEGHoI_m_dkxg51qyNqkxsDxT81JjOMX_2yW01Rxpksj4yxxY6jnLaNRsLVif4_VqZKHK1b2MpAUEyD_hGONBO5vBViXNFnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
📰
سی‌ان‌ان:ایران به سرعت در حال ساخت یک تأسیسات هسته‌ای مشکوک است که در اعماق کوه گرانیتی نزدیک نطنز - ملقب به "کوه کلنگ" - دفن شده است و تصاویر ماهواره‌ای افزایش ساخت و ساز در سال 2026 را نشان می‌دهد.
این سایت احتمالاً برای محافظت از سانتریفیوژها یا کارهای غنی‌سازی فراتر از دسترس بمب‌های سنگرشکن فعلی ایالات متحده طراحی شده است.
ترامپ تهدید کرده است که به آن حمله خواهد کرد ("ما ممکن است خیلی زود کلنگ را بزنیم")، اما بزرگترین بمب غیرهسته‌ای پنتاگون ممکن است به اندازه کافی عمیق نفوذ نکند.
نشانه‌ها نشان می‌دهد که ایالات متحده در حال حاضر روی این مشکل کار می‌کند: یک روز قبل از شروع جنگ، یک آژانس سلاح‌های کشتار جمعی پنتاگون قراردادی اضطراری برای تعمیر یک تأسیسات آزمایشی زیرزمینی که در گرانیت در وایت سندز حک شده بود - مرتبط با شبیه‌سازی حملات به عمیق‌ترین پناهگاه‌های ایران - امضا کرد.
یک بمب "نسل بعدی نفوذگر" در حال توسعه نمونه اولیه است.
تحلیلگران CSIS می‌گویند کلنگ هنوز عملیاتی نشده است، اما ساخت و ساز از حفاری به ساخت و ساز داخلی و سخت شدن تغییر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71367" target="_blank">📅 17:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71366">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=A0YdovehugeydJExYFcX_1NGfFkb9_kFDCrNGdWS5Ft-yYcQlh_y_w4QbtJbsLSH2D6wgQG-7FWrsgJ600R9JrWGU4ri9NuE7JQUoji8OCDdlsJhOjid-IrFGR2TtNyeBQZSicQd5mh4MlIpz6Klw4_yMfgWNlwu2OIPx-viH0Iz4LA1HiAOolbhPiFEhMgDCkvDl5q3x3Fx1xoYE9qAwBDmJbBP5XMYGStibT0jvZH3Uat9sIv7-PBlKzZm5rEvbAH6YWc3_ubkGhaEcXB0ZV_GWL3NmTY1wewejRivFwE54IbMWTucH68doXXH4huFMzR-CyP0p7UHY8ap5RQDBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=A0YdovehugeydJExYFcX_1NGfFkb9_kFDCrNGdWS5Ft-yYcQlh_y_w4QbtJbsLSH2D6wgQG-7FWrsgJ600R9JrWGU4ri9NuE7JQUoji8OCDdlsJhOjid-IrFGR2TtNyeBQZSicQd5mh4MlIpz6Klw4_yMfgWNlwu2OIPx-viH0Iz4LA1HiAOolbhPiFEhMgDCkvDl5q3x3Fx1xoYE9qAwBDmJbBP5XMYGStibT0jvZH3Uat9sIv7-PBlKzZm5rEvbAH6YWc3_ubkGhaEcXB0ZV_GWL3NmTY1wewejRivFwE54IbMWTucH68doXXH4huFMzR-CyP0p7UHY8ap5RQDBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر مسی رو پیدا کرده بهش میگه بگو علی تولدت مبارک
😔
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71366" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71365">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71365" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71364">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as6w2wIf2m3RlcQvoIHR7VI0mNPz1-liWmG17TY5haVDDzppgN6MbuOU9Hv5XgIRMJ0O1Lcjv7W5xMcK69mYKPqXjPFLosBFHr-CshWtBhbpI6phNuNfTc9y8ImmnSiP38LSi35z3-87uTdclg5Fae-_4ocuZ6fgWjooMSpmS65vCy7q1VXHcXMNczsuDb3Y0CgBusRiRJ-32t8_RVVGQKVoSRc0-AAkaU8vQ1YurkK0Or9rjsvqZkxZarCQwlq6cqw3Lj3P2savsbQPClY1BfE4iZip5b8l7NYp02Tl7FE2OmIzOxTcjtxcM5s85pE_ATTh-CETE7M1GjSiD-hohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرسنال
🆚
ناپولی
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
آرسنال: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
⚽️
ناپولی: ۵ بازی ۱ برد، ۱ تساوی، ۳ شکست و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71364" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71363">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=hHuoz8uQgK3qBOENQsSa8Cvi20snGdWRlpxRtS0JTeyW2EsYk00IJMXxKtCsrT5sN6Vvyh-po5Rzib-SBDF6FWrytK5sqNb1kwtDaoKh6cBa11zthOypYvelqaOY5ysy6Opswm96E3SAB1OHttTIY1zBeOrj_CEQ9904Vg11747TY3balMTHb_UAcmj9UHWUr5tujKjRY5UlpaRVsXeoE06bOuPMBLkcOtT-xMmcyhVtBfvD3bta1RjrZhYxI8trcmCb5v7ai3Htfd1GwCmOBv4UWsrMbLFh03H8Z1ONoQVkDChMvuwQHyttxfQDJ3ebgaWqvBiwmV6pRqPY4CId3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=hHuoz8uQgK3qBOENQsSa8Cvi20snGdWRlpxRtS0JTeyW2EsYk00IJMXxKtCsrT5sN6Vvyh-po5Rzib-SBDF6FWrytK5sqNb1kwtDaoKh6cBa11zthOypYvelqaOY5ysy6Opswm96E3SAB1OHttTIY1zBeOrj_CEQ9904Vg11747TY3balMTHb_UAcmj9UHWUr5tujKjRY5UlpaRVsXeoE06bOuPMBLkcOtT-xMmcyhVtBfvD3bta1RjrZhYxI8trcmCb5v7ai3Htfd1GwCmOBv4UWsrMbLFh03H8Z1ONoQVkDChMvuwQHyttxfQDJ3ebgaWqvBiwmV6pRqPY4CId3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
دیروز تو سمنان عرزشیا برای مجتبی خامنه‌ای جشن تولد گرفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71363" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71362">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ece16841.mp4?token=GokGvW-bZ7cqZyBcEKSGkGXYvy3BavgL29oqacy6VulXGoFwh5KiymuL12NDHLN2atatr2d8qdyYnjMoswkA-AZ33A2VwgaZaxgaZxH-c3u9LxaM01PGOx6gysKkiOwqiY0gY5ekLHcjQhaVrNmxrAg2EqJNRYVKlE3hbpxEg1hE3OowXC1KtttSuw96KtX4QzSG4RAgk6o7jXHfFLkL_Z9p8k7fS6dqWxayTqVhTCrGzOYlLHtU-m6a4ECZnnx1AHg6AWEyfRAp4zI7BZfZNGaA3lid1y8KnD8VqgRYYQZw6maUUG_vnL4m9iiYntORUbJNmoklvX-wAnvbgmOCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ece16841.mp4?token=GokGvW-bZ7cqZyBcEKSGkGXYvy3BavgL29oqacy6VulXGoFwh5KiymuL12NDHLN2atatr2d8qdyYnjMoswkA-AZ33A2VwgaZaxgaZxH-c3u9LxaM01PGOx6gysKkiOwqiY0gY5ekLHcjQhaVrNmxrAg2EqJNRYVKlE3hbpxEg1hE3OowXC1KtttSuw96KtX4QzSG4RAgk6o7jXHfFLkL_Z9p8k7fS6dqWxayTqVhTCrGzOYlLHtU-m6a4ECZnnx1AHg6AWEyfRAp4zI7BZfZNGaA3lid1y8KnD8VqgRYYQZw6maUUG_vnL4m9iiYntORUbJNmoklvX-wAnvbgmOCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مراد ویسی:
جمهوری‌اسلامی سربه‌سر اسرائیل نمی‌ذاره، چون می‌دونه اونا نمیان "نفت‌کش" بزنن.
اونا میان "نعش‌کش" راه می‌ندازن
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71362" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71360">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBtC34mpGmiSxrADZdiCRA7mlUCVprzJhM0v5MdCyhQJR077Y67jlCo2TiC1zj9UaFIHKSYm_XAKc6C5mXHytuw3sxtEQDgaAxPyJXsepDi52XveqQQilP6EI0sfC6KW-UC8hbBqftH0COTD5gNdPQNs9rvcABZ-CKW_eC8pouCrUh6EeKctjjPVkCXARaHr3AUSVm-GdcFD7RldCwQimjLvjO9kvclVmLKViZYglQ_aehhEIX7rXP8146mmZkVS5ihnBi97J5dOZWYgo-QRRJD_PngKwCaBpWIf7tHA7kmu_wLnbl9BpD9N5vWfbymnuFoW6MqeaUfVg69_Dfcn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=KcWKoQoWr4ew_7unSKXl7y1Sv-nXp5wVfXM6hvaSadjglhFT10oQjdUk3NoT7qFFpR8hXxB9eCj-rT3gWld8nA7jPeJ8A0C5RBPN6iEgs6AvNge4Z0_GBYCnILhS0z7gWesLUIg2en-Tw42tVYHXL6xuZbHrcDT0OmUMiZ5NbkQkc96lUnW81EJTfeZ2Nr9NKghuDntk2sNsAhvHLhlMg27Bm_fKtxKwqOs0im7F-P35LWV9XiK5lDD1uqpf4PqQXP9D0dmDYKIQdP_9M6LwwXFFxO3fe80HBdP836-QxJSP0DJWgHP0bXHkZ5pyO1soEaWkpgARwPzjozsmPDJAMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=KcWKoQoWr4ew_7unSKXl7y1Sv-nXp5wVfXM6hvaSadjglhFT10oQjdUk3NoT7qFFpR8hXxB9eCj-rT3gWld8nA7jPeJ8A0C5RBPN6iEgs6AvNge4Z0_GBYCnILhS0z7gWesLUIg2en-Tw42tVYHXL6xuZbHrcDT0OmUMiZ5NbkQkc96lUnW81EJTfeZ2Nr9NKghuDntk2sNsAhvHLhlMg27Bm_fKtxKwqOs0im7F-P35LWV9XiK5lDD1uqpf4PqQXP9D0dmDYKIQdP_9M6LwwXFFxO3fe80HBdP836-QxJSP0DJWgHP0bXHkZ5pyO1soEaWkpgARwPzjozsmPDJAMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⛈
⚡️
ویدیویی که یک هموطن ساکن مازندران از وضعیت چند شب پیش آسمون مازندران منتشر کرده و نوشته؛
تو تاریخ مازندران چنین رعدوبرقی که بی‌وقفه ۳ساعت بزنه نداشتیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71360" target="_blank">📅 15:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71359">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkMRUfCZ0NjpH3ZHmpJcesmPf4lzqkGaGmB_kUMuzYBXT8NvmmPccQJl91Rj2JzAca89OoCvWhTcRtfLL6TyIVDrhjGZUZtvBDOiS1HdXc3lKPWBDuBJFIX-fEg7uFGhe4x2s8-OJ9Tn94aXyxgI3txEpwtVJ6I0hTCAO0YMmTPWlkKE34CUEuDGyPr7aM2gK4e9lHx-5S9sOaYqkTrTWR434YwSULc2mMBHGfGnH9kX5qoMLHOKGVGbLJnlcLzrPPMt_P3RCAoktrId7amkiTFKBXBxb5L_xCqQG0Kjjk9tEMS5nAckcdYySoZzsAFunOZVf8UlEaOo5uHUmKjbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
🇺🇸
#فوری
؛سخنگوی سپاه پاسداران شروط جدیدی را برای پایان دادن به جنگ مطرح کرد؛
🔴
اگر دشمن خواهان پایان این وضعیت است؛
۱_ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد
۲_ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند
۳_محاصرهٔ یمن پایان یابد
۴_۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۵_از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71359" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71358">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=sj7q-8T-H8ImwmqpYqZAlD32Q2ALTSFdrKFHOM8WUJZjzHKEQdXFS8Ok53ySHWn8X4OaC7FSGqtjlhshvgB0lpd5oCRQrUFbqUbOuBVnzD4VD2X4uWahxw-Jj_UazU6mlTsdq-G4F-6sqaJrT-q_3V4M6fWsjH8l61Pj5yXvJo-YyvdLZNvR8EktzMG5sW-M5eFQHzQS2Tj7fR_jTbz7OguNm-omXByAbthpAUGGOwdrVfkNRSU5IMAVtEaV97h61a2vIYtFHC-ItMFKIMVcyPFUkZUA0xWt1TxrKoFQxrIuHIn3L4gfx5JL4-fQwuWdTW8KfdANlmeKh44PZJ2YNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=sj7q-8T-H8ImwmqpYqZAlD32Q2ALTSFdrKFHOM8WUJZjzHKEQdXFS8Ok53ySHWn8X4OaC7FSGqtjlhshvgB0lpd5oCRQrUFbqUbOuBVnzD4VD2X4uWahxw-Jj_UazU6mlTsdq-G4F-6sqaJrT-q_3V4M6fWsjH8l61Pj5yXvJo-YyvdLZNvR8EktzMG5sW-M5eFQHzQS2Tj7fR_jTbz7OguNm-omXByAbthpAUGGOwdrVfkNRSU5IMAVtEaV97h61a2vIYtFHC-ItMFKIMVcyPFUkZUA0xWt1TxrKoFQxrIuHIn3L4gfx5JL4-fQwuWdTW8KfdANlmeKh44PZJ2YNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
یک فایل صوتی که اختصاصی به ایران اینترنشنال رسیده است، نشان می‌دهد یک هواپیمای نظامی آمریکا در مکالمات رادیویی به نفتکش جمهوری اسلامی هشدار داده به‌دلیل «رعایت نکردن محاصره نظامی» در بنادر و سواحل ایران، موتورخانه آن را هدف می‌گیرد و خدمه باید در ۱۰ دقیقه موتورخانه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71358" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71357">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcr65FOwbCxhzQVRrAcmP_0IOd8HTk5KfWwe7ohcHFZDiBib5ehqzNlhSqZCgc25jgex4iFVuIvgZlLonv_nNSqrSElD38AwCESofdqZE0n_pwTmPZJrWS3so3Y0Gv9e01BpQrdHwrSpv_lhCSEsZCvwjHet9KDHWbMwtt828YyJcMlA7hb3G6KUkUEfVcYng9UmY-YPuP4T6G8IY_B2yQk4tS0IimHESO6iRknIFzmIWtZrBu2xO6bhxIvOsDCuUGmP8xv9oBhTLv2lqHgM5u26MLPhjUPBPHy-DP2EZSD4QcSfJg78wdZ0LIMqL4TVtHEvd9j9nExWsUUlAKyUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع حادثه‌ای در ۲۸ مایل دریایی جنوب شرقی «الفاو» در عراق دریافت کرد.
فرمانده یک نفتکش گزارش داد که این شناور مورد اصابت پرتابه‌ای با منشأ نامعلوم قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71357" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71356">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSdfg8Qu9dSXOwWqX3AVZfo3crxjIvhn8afjoW_l7uHJuBn4daj1c82xef_d7D8YVjew5v5qnAAfMliK4Rqez9LD--slCQKajxMtruSbffem_sIPIdQv8VsDdJNw-uywpR2vStjuoXPZHugmNLEYv60MtwKsUmzNQooi1PenjrPXiNoVZ6pcvonQ71b2cJDiKFDvJaB3EoPaTqxosshXUtbBp1CnQ1LOKeAs1ddB_HjZbDd8BpH4WgBSgxglmMatDkqZuTChs70BU9Bb_X8LLRFPKuBZTCLrYyTDwJwQ0FbhjXqLJMzhxlOSeOMTr2G8pZ7YSQCqtFCz2WDqjv3oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
🫵
دقایقی پیش دلار و تتر به شکل عجیبی تا 241,000 تومن بالا رفت و دوباره برگشت و الان 234,000 تومن هستش...
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71356" target="_blank">📅 13:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71355">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7Lh59d7Su-5iqq_Feit-_dCQvSkzY7IT02pGP10ww20yzjefM6qb68RP3yHh9B4cISbb7rGNpBJnWU7j2s2c4jkPD_bIMyOeIdbWCtit9xjVOgU8yoTNnMCcbNMYUrQI1fSHXIClPm8WD5MxFW-lT-0ilRfSuy6xW4l_M_DWVkltxeeOwGYiwe5vmmGZelJdGfi-VhDWzp6i9HjFwK1LxWwZCGqYyA1aVEYL_Gywl8Vj3BOi-S2RUcTHRg0uSaF34_xk4b4p2Ae1ylr62izOMtGE-z0AU28_3PYOV9V3gHQoJVMakclsub-S0Bn0nD7UYH4s4nwVE-eqB2xU4s6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که به دو ناوشکن نیروی دریایی ایالات متحده در خاورمیانه حمله کرده‌اند. این ادعا کاملاً نادرست است.
✔️
واقعیت: هیچ‌یک از شناورهای جنگی نیروی دریایی ایالات متحده مورد اصابت قرار نگرفته‌اند؛ تمام تلاش‌های سپاه برای انجام حمله با شکست مواجه شده است.
در همین حال، نیروهای آمریکایی تنها در هفته گذشته موفق به انهدام ۱۰ نفتکش ایرانی شده‌اند. این شناورها بخشی از یک شبکه پنهانِ چند میلیارد دلاری بودند که بودجه سپاه را تأمین می‌کند و ایران قادر به محافظت از آن‌ها نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71355" target="_blank">📅 13:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71354">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=X2SAkz7F-lUPBnmgNFqMc_vXLW-lfoBN-N2JUtmrG-We3zXX77ru80SSZkRK5zyDQt5DsByjxlos0vspRDilgjnvXRn8El_vrzlviQF_zNXm2o83KXElNbvDHsSv54-tMPpmwUsLolpLFBIYmT2ZiGvJ17cidY7b6SDgZURua6wztIbUxqRIdh5R8ZoMEo26FVRAektYcarnyyNaND2Hh4m4EhMkLxVFw1O1hlQw__H36rEBlkVv9VzoFe5N1BdLvRH8XdsLKHcg0mRZvR70CyigeA5zDps1gqijjxhcQO-AL-HnfL894Xl1NBjFxFXw_9D-ioZzLWUGmT4HWND4vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=X2SAkz7F-lUPBnmgNFqMc_vXLW-lfoBN-N2JUtmrG-We3zXX77ru80SSZkRK5zyDQt5DsByjxlos0vspRDilgjnvXRn8El_vrzlviQF_zNXm2o83KXElNbvDHsSv54-tMPpmwUsLolpLFBIYmT2ZiGvJ17cidY7b6SDgZURua6wztIbUxqRIdh5R8ZoMEo26FVRAektYcarnyyNaND2Hh4m4EhMkLxVFw1O1hlQw__H36rEBlkVv9VzoFe5N1BdLvRH8XdsLKHcg0mRZvR70CyigeA5zDps1gqijjxhcQO-AL-HnfL894Xl1NBjFxFXw_9D-ioZzLWUGmT4HWND4vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
پرسنل نظامی جمهوری اسلامی:
رفتم یه شونه تخم‌مرغ رو گرفتم با یک کیلو میوه شده یه میلیون تومن. حالا نمی‌دونم بیست‌وشش و خورده‌ای هم دریافتیمه.
مثلاً بیست هفت هشت تومن سر ماه به ماه میدن به ما. مردم چکار کنن؟ خب دیگه یارو میاد بیرون حق داره اعتراض کنه دیگه. به جز این که اصلاً راهی نیست. بعد هزاری انگ هم می‌چسبونن که آقا یارو تروریسته، فلانه، بسانه.
مرد حسابی مردم گرسنه‌اند. خودتو زدی به اون راه. من با این لباس دیگه قشنگ با این لباس نیروی انتظامی ناراضیم. وای به حال مردم. یعنی قشنگ میری بیرون خشم و نفرتو تو چهره مردم می‌بینی.
می‌خوان جرت بدن منتها نمیتونن. یعنی همین الان میری بیرون اصن یه جوری‌ان نگاه نفرت‌انگیزشون نسبت به این لباس قشنگ معلومه.
حالا یه عده خودشونو به خواب خیال زدن. بابا دیگه خجالت بکشین. بی‌شرفی یه حدی داره. مثلاً انقدر. شما دیگه رسیدین به اون سقف. یه کم خجالت بکشین. یعنی اصلاً من نیروی ناراضی‌ام. وای به حال مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71354" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71353">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jciHwHbu0mjZ1DU61jWT25o0fPAdkqbbXtUJyMcaAzNEGvss-fpWpCGOztBfWhDAoqQQ1e4KpDvEhl2Xrg6tkt8LWvYa8UW-lxjteDs25OZxyphMeD2NldqKHFcwqjtejSHchZ8NcBnOtoMpnQgdoHylvHXicEQa_VTZWY3wVDhlGPEQ8-vRtKeDEEmxk8TWLzLvM8FD8VlaUmZCTncq3FypIiUsXgSfqBAo-LicBxI17DHwMu_EttpKx4nv-X75xFvYVwbIW7mrlmwSNANfNcsk72kztiiNiDDoudnhC-_tWu99HlYfU6mM-pYWdGhP1u06o3PcPvqUxwoy9oIXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی از یک طرف ثالث درباره وقوع حادثه‌ای در فاصله ۲۴ مایل دریایی شمال غربی بندر راشد در امارات متحده عربی دریافت کرده است.
فرمانده یک نفتکش گزارش داده است که شناوری را در وضعیت مایل (کج‌شدگی) در حالت لنگر‌اندازی مشاهده کرده است؛ وضعیتی که احتمالاً نشان‌دهنده ورود آب به داخل شناور در پی اصابت پرتابه‌ای ناشناس است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71353" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71352">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71352" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71352" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71351">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdRiaQFtXkCJyTqbtUCwZRDWosCk5qlKBXC2puc6prqoIzj8BCW7EKLTfNecLvm9hz9s-e2i8GVZSV46_aLbxyzHp9dYztlMovzOw75_qztQkehUU0TJofWjNA4JK9K1uygDW9CAnCkK_aoG-KYG-OMYc8gBDGsWdf5AWNzpDPYbGZXxCQPD33JITJJqjeuh_QtWHohbq7YvOUoXRyaRNYgNxHDCxCVHP4g48I0TPVddgODAMnfswvv2jtRl0ORty8YtbTkdacBUqotMP3MOZ9ro5eY-J8ypArVtDXIEdz67zy_JBwCahC-vWKD3t188ZT522IVnxvohsxJd2P89MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
اتلتیکو مادرید
🆚
لیورپول
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
اتلتیکو مادرید: ۵ بازی، ۲ برد و ۳ شکست، ۸ گل زده
⚽️
لیورپول:  ۵ بازی، ۳ برد و ۲ شکست، ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71351" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71350">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5Ady4c7H3JQbgOZ_Kk_WptbtRepiRj2bOnixZSoyPtdcOJZXDpbzEVNAYA-Y9StHrTGfrGpL2z3ScWrB1Rdh0YRMZ1f7clKtfueSgJeSDgifvPNoAe4s39Muc8YyYkiIt6JDPqJGAdrpHJNOpuKkiAXAHkdRdP5tWb6zPmxEhkp6E5YcSrA5LI5zvhoR3mzcMA4uJxEFVIg96w3q8iPahlgbNqv3lt6r4gyHSP1IO2dC0w9kEi-z2HUUxOrvmA-_mhjgrtPo1izASTo_otX-647PVnDGiC74c52Sraz7YIiPeqpep6uFKhN1AJSzgROK8WavIWHl6BU6mL2F09HwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📈
قیمت نفت خام برنت برای نخستین بار از ماه ژوئیه، به بالای ۱۰۰ دلار در هر بشکه جهش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71350" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71348">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YS0uQ4nLvTctwzVbvMNbPmypfQYjYCo3SH3U1B9fsGnLTn7__zaza8274aFIKF0VlGa2U8i5BLO6lz3zUdhgAxgglk0pXlMZvEmOojxIaFXVSHWZPc33V0omLaUvj7lpflWnn4Rt9Gt2mfZulYAgaBqZGCF0Z8g4AuqUv5HcNt5gjyZ7q0bZcesmUUOYuepMvjoc1E32LUI8nHKJ9a6iX1eG1N9olaUgqErJcjuOdKrEEz4SnoPQdh7rbs9f2DnhrIfcXWrq6Ny8WtsBZxJ9VESfbBBQzHJdLg8I1l3U1Uoitj13NCOwNmq4ek8hplLEMWP6h9i6-oYXDOxmqQc01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=BqakshGfk6PwR24r41352a5UeMj_2Fe3udGo_Tc1UlNluer4G8BHWQqY9HgiYOh50WwDZHHPyDy1bK6sGNct5zdOgK5b6KDhh9aJM8Ln942jZaIYAS8JPv_rkpeA6m9XtULfRX59USMzO_ywXol8BxVEDzZx5dWkm_0ol99AS9gvsDZLf_VAIqKLVJn9rOu63rHXe5NtJv3fUyrrrG8YAxPQdcab1BEgMVVGHhiRpW06GdDXwdjLbiyu5loZ8h0vLtYPiszmA9J_vKBjWDsXLLOfYfITSQmE4YnPFSQ08NfWsanEEGGs2PZiChx_wyEwRP5djdb2iFzvhKYvBa2CrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=BqakshGfk6PwR24r41352a5UeMj_2Fe3udGo_Tc1UlNluer4G8BHWQqY9HgiYOh50WwDZHHPyDy1bK6sGNct5zdOgK5b6KDhh9aJM8Ln942jZaIYAS8JPv_rkpeA6m9XtULfRX59USMzO_ywXol8BxVEDzZx5dWkm_0ol99AS9gvsDZLf_VAIqKLVJn9rOu63rHXe5NtJv3fUyrrrG8YAxPQdcab1BEgMVVGHhiRpW06GdDXwdjLbiyu5loZ8h0vLtYPiszmA9J_vKBjWDsXLLOfYfITSQmE4YnPFSQ08NfWsanEEGGs2PZiChx_wyEwRP5djdb2iFzvhKYvBa2CrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دختر یکی از پشم ریزون ترین خودکشی هارو داشته:
دو روز پیش "پایال دِوی" داشت اولین فتوشاتشو برای یک مجله تو حرفه‌ی مدلینگش انجام میداد که یهو وسط عکس برداری تصمیم میگیره بی دلیل خودش رو تو رودخونه پرت کنه.
ویدیوش خیلی عجیبه و بعضیا میگن امکان نداره این خودکشی بوده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71348" target="_blank">📅 12:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71347">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/032667483d.mp4?token=UcV0ueaRpJYPr7SH5T4L7IpKY2b4qfNzGYdjj2elz4LRs9F4swy1Q_hkKknrSxPeqss1b_hArxRXzY3ueWTqQ-xR1GyXbl58i0oM70OrR1ab24IDaoliDDywNYZsuc4JXLZw6RlGm_eouZooKPFxdrQFcdG6r03BistRAVtngTee9__HRe8ExO8JMNr88X8Qh0p2fyE3J-FB7OaOSVP1YfINnS-e6GK6D5A5Aml4LYlbeFHvirDSy60AfZbLmOfuVdv_eJCcGQSonmnJLSD8tz6tTUmlzO8un7kscSx25Nsilgd74gGRdDymHTgKjMSxolY6VFuZ8YqdsxDb8X5ApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/032667483d.mp4?token=UcV0ueaRpJYPr7SH5T4L7IpKY2b4qfNzGYdjj2elz4LRs9F4swy1Q_hkKknrSxPeqss1b_hArxRXzY3ueWTqQ-xR1GyXbl58i0oM70OrR1ab24IDaoliDDywNYZsuc4JXLZw6RlGm_eouZooKPFxdrQFcdG6r03BistRAVtngTee9__HRe8ExO8JMNr88X8Qh0p2fyE3J-FB7OaOSVP1YfINnS-e6GK6D5A5Aml4LYlbeFHvirDSy60AfZbLmOfuVdv_eJCcGQSonmnJLSD8tz6tTUmlzO8un7kscSx25Nsilgd74gGRdDymHTgKjMSxolY6VFuZ8YqdsxDb8X5ApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا طبق فتوای جدید حضور نداشتن تو اجتماعات شبانه، غضب الهی رو در پی خواهد داشت و تو زندگیتون ذلت و خواری میاره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71347" target="_blank">📅 11:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71346">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJCcWwI3goSWwiqM2KNFshGCTFD7N-5leKuHf13paryH1AtLyADkHZ02QKd3XtxJlJrIDVI9iyClNva9oMvw1MBC6KKvYomNBbnC9J12aRwhXVLprlpd3_bCVp2WZnxKLm3N1hNSvogKsJjTOBCNvtSFS1thPOkEX5AHwVD-42n8dclD-RIAR0OtbC9w6kV6AHdaPNJqrqQLLbJs1bBoUzBzKVMe2bJm8L41-sB7x2vHNLw0IEUHLWARRMgWdb130lLW_isGis-Zj548NYndePkf7Wcg7fg61tMY9YOIS90HBv3i9ppmmTaTOJ0-akXw50pZMK-JCtckHtBa9GYbeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
دوازده کشور با صدور بیانیه‌ای مشترک، ممنوعیت‌های ملی تجارت کالا از شهرک‌های غیرقانونی اسرائیل را اعلام کردند؛
🇫🇷
فرانسه
🇬🇧
بریتانیا
🇨🇦
کانادا
🇩🇰
دانمارک
🇪🇸
اسپانیا
🇫🇮
فنلاند
🇮🇪
ایرلند
🇮🇸
ایسلند
🇳🇴
نروژ
🇵🇱
لهستان
🇵🇹
پرتغال
🇸🇪
سوئد
مکرون، نخست وزیر بریتانیا برنهام، و نخست وزیر کانادا، کارنی، توافق کردند که وضعیت با خشونت «بی‌سابقه» شهرک‌نشینان و گسترش شهرک‌سازی رو به وخامت است و به طور خاص پروژه E1 را «غیرقابل قبول» خواندند.
آنها از اقداماتی که قبلاً توسط ایرلند، اسپانیا، هلند، نروژ و بلژیک انجام شده است، تقدیر می‌کنند.
این بیانیه از اسرائیل می‌خواهد که فوراً گسترش شهرک‌سازی را متوقف کند، شهرک‌نشینان خشونت‌طلب را پاسخگو قرار دهد و اتهامات علیه نیروهای اسرائیلی را بررسی کند.
آنها «قاطعانه با هرگونه اقدامی که منجر به الحاق سرزمین‌های فلسطینی یا آوارگی اجباری شود، مخالفند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71346" target="_blank">📅 11:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71345">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcf294068.mp4?token=Q5ioMJBhHuLuxjcO9zYqRjhkE4Hc05Anajp7AvLdVvZgKrxu3ulHhFX5GB0A_MuaZrHGaVeIYYcOfEYtyAPsBBKt9rqDA66w2fjUXexOmLoB37NBb1qgSg-A4672Bmxfd36S8Laua83H1MvPTSfMt9pSdzje-wJIqbgiIzGLN1zzOU82OYyCIzJgtUErF3eOcCp54j93fHXkdMJvi1RLjmKrhQaaslo1O8xRw_vkmvThnAXDDAmKg2A9bJ-Jjdm73cIDQUfPry5pEsshgKTzXewwMWyJVCJyZrmaxjhedR8HkNROHddiab45wEiZqjJC7ks_cTS5_r2AlDHv7_Ti9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcf294068.mp4?token=Q5ioMJBhHuLuxjcO9zYqRjhkE4Hc05Anajp7AvLdVvZgKrxu3ulHhFX5GB0A_MuaZrHGaVeIYYcOfEYtyAPsBBKt9rqDA66w2fjUXexOmLoB37NBb1qgSg-A4672Bmxfd36S8Laua83H1MvPTSfMt9pSdzje-wJIqbgiIzGLN1zzOU82OYyCIzJgtUErF3eOcCp54j93fHXkdMJvi1RLjmKrhQaaslo1O8xRw_vkmvThnAXDDAmKg2A9bJ-Jjdm73cIDQUfPry5pEsshgKTzXewwMWyJVCJyZrmaxjhedR8HkNROHddiab45wEiZqjJC7ks_cTS5_r2AlDHv7_Ti9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
سنتکام:
کشتی «ریسکو» (M/T Riesco) در تاریخ ۸ سپتامبر در خلیج عمان غرق شد؛ این کشتی پس از تلاش سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی ایالات متحده، توسط نیروهای سنتکام (CENTCOM) منهدم شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71345" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71344">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=ZZrk2FA1FVCCWYtzso1vhJfR4Efe0BreOuMsXlhP8YczgecVSvrhx4BeR0p4uw2SgKpKIPxCWt9GlmNPc2x2RqCMwBB68zf8jo5puWzszsdwMVW6t196PT92szxPZ2lZwva8SFL6TlYtaQP_8Z4Lk6F18j647_omSacivbRVFkBPDViyPdc-7k3J4ltwEyhLZu1_bWSJlIkGcvJycNOVxyea3TRGbK4f9BBtJW8AoFNAkAO4jYGGOR6Dhsirx8GF3rlXvOgdjDrzyls3KUlMcRUZ2FoDdWektwY8xHRZmZDfUffL2MBiIwdncprTMoDN7NgzdiLTrlEXlsW6nJSB5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=ZZrk2FA1FVCCWYtzso1vhJfR4Efe0BreOuMsXlhP8YczgecVSvrhx4BeR0p4uw2SgKpKIPxCWt9GlmNPc2x2RqCMwBB68zf8jo5puWzszsdwMVW6t196PT92szxPZ2lZwva8SFL6TlYtaQP_8Z4Lk6F18j647_omSacivbRVFkBPDViyPdc-7k3J4ltwEyhLZu1_bWSJlIkGcvJycNOVxyea3TRGbK4f9BBtJW8AoFNAkAO4jYGGOR6Dhsirx8GF3rlXvOgdjDrzyls3KUlMcRUZ2FoDdWektwY8xHRZmZDfUffL2MBiIwdncprTMoDN7NgzdiLTrlEXlsW6nJSB5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
مهران رجبی:
اونی که نمیاد تجمعات باید بهش بگی فازت چیه که نمیای ؟
این وظیفه ملی و دینی ماست و باید بیایم کف خیابون
ضرر نداره بیایم و شما کاری میکنید که کفار ناراحت میشه پس بیاید
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71344" target="_blank">📅 10:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71343">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=lXm77grJlTBim34yqhjh8cvWV01E5k9T49BVmKHZ84h3nUoluNa9ofWuiQfWdn6UNPhwE9XZPpMtewAtWJQU0Nj4ku0SchxKk-ukARizIW7m5RWII5hzPEjqUJ0TG3LU_Exvq59CVv4coytMQtTt_LpHut0zSQ9QUICD9z1rYhcfYwebExEDIye6ezehzkXDj4634DGG47RbOBL3KBy5AlsgvO-tU4rlSVSwCwC4yn4B6X_lm5CVs7PMezX7wvrl0Hupq4blcOwi4SIqoHazJ6OW8dePpBBK2s3kVjQGy7tuVzWJhAMnY3sEjRqve1ooztkMWVEqEyTD1ybt1P665w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=lXm77grJlTBim34yqhjh8cvWV01E5k9T49BVmKHZ84h3nUoluNa9ofWuiQfWdn6UNPhwE9XZPpMtewAtWJQU0Nj4ku0SchxKk-ukARizIW7m5RWII5hzPEjqUJ0TG3LU_Exvq59CVv4coytMQtTt_LpHut0zSQ9QUICD9z1rYhcfYwebExEDIye6ezehzkXDj4634DGG47RbOBL3KBy5AlsgvO-tU4rlSVSwCwC4yn4B6X_lm5CVs7PMezX7wvrl0Hupq4blcOwi4SIqoHazJ6OW8dePpBBK2s3kVjQGy7tuVzWJhAMnY3sEjRqve1ooztkMWVEqEyTD1ybt1P665w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از طویله مجلس
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71343" target="_blank">📅 09:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71338">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qGVZA4oqMm8g23rBhNZ9NXaM9D-J6pLPpNTqS7S_5j2bG84vMDKOPj8xOG2Ze8McXLgcKwD3_SigiuIJRx9h8y2R_2U2cOn80l4X46xBghsZO5elnw03XeakmCDKlKswUqXysYXhU_FIT9BvVTbaqwmjEP4OflRDhOijOrQS61W5WMAR1U3F0VvmyGOIflIEQsywiNZ_7E4aCbkO8s6LYVmK0cGihzqVzi2UpyVFJ6511VUFT5Ds3wkkqhItwEaTGm3vyQoxN9F9ENc9y9V985ZkUPwt1ZRqAo_1fd8t_beuo2WIjJFfzxnNes2uHxUtLqjOJo_c0gunt3lVK5xnfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKTf5QWMu-PbG2i6Ja2Yf8wQfTq9SxKR7dt8kstYASx6c-SNTJkChqM7kvCIUppAlKUDBaktTwS9glybdLSuDtfjC-TC43-7-sAjBKfgi4cM2_eWcqy6RYTmy96f3LgCW9hv2Txn3X-bEQfYlEON3cFjb6mJfJrQy_RwJD4letQgKizEhma_yY8DMHkKaRoTRE971u79sfTHbhR-myY6M0J3-a9H6kz-Jhj7__4DLTznLvXEiZXAzxh8GmRV-NLNymKGw_JnurtbWhxNJrfboH__p9Bx7aNEd8E9Ek2TuEIhVyEOOeEDe97hpKa6vHldhXQhj77mmCHo2RKhS6F6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BoJvK-dMyxGQOVVL8pkzFHPaRqMkoqw2-5pOYDTifQBqv-lhHUTxM5DT8-qgoLGN0qYj4CrPTM4Wp1eIbLAHk_veSbfrh3wKD20TjitH0g_FGcvDMwZwj_I-1eYFUQGqOXDD8ydGjwyTV-pZm0iGG5K08AaClXSHxCf-Uo5V1oa226lnaW2KRQv9LK1VBkyMHYBfTe6n1lqSqvBLg3MgLT4WmwEhtK4elyrvCtfRAzyhEEslrd1SIVjQ6yBWO3WCrGqidsOeHfBUlwuX2Ceh2rAVse1fq2rGMv_VfzO9PNV0I0OjCzBaQjjRZmNyxVej2FvdfrOsgW6bIWeDazpoDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDZWP9RgZXtrTdaM42Ow3gq88boM330LbCFZO-THvTXe4japXQDeHZCQ1IragfziNFkbjS1Tdt4eV2MhJcKXVfctDqu1dWRGCin2eqXxgs0ltEIdHE8tN-okLlolfu_D0qJAVV2URrokV2uUGPBHoNr6WDVZUPVsN7Nn4h5D1W0pGks2cfmc7vWcDxO41f-hj1txzYdlYIF-DgcWLrSKYxnodBOskzbYxquiLf8hSxnvufPPzly_ElcWm0Vy6vZqA_bwrUN8WTGCFBs3VXMP8L2GKJx4jQGhemFrH_c0FI5SM2Uugh3WxxnTCCmOs7e8HHQwDVAGs3YjxGGZjw5y-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2B3WQQYcwPa8LGBH_aw94iKtvoSXhGM6NX8jxPc8vDjQnnArmgH49EydjMsogNEAwHn1rOTQMhmDsYkt3loGZApFB6U-k2j5IdKSffxad-LffdawkrmpmOevwQ5o9zuFhRSX2XUGjgOJSqDzMKTUncVBh6qga3WZFVyGKIntZL4gxxI7E2Xxdvx6wYI-qr9zZr1EMfEaREkO9_dC5X5pVXiXqIlUS57gTvDJdrfdpmWyQJoLcxf5aTWZ0zfwTcneoXFz_woPJlztWNQ7DzpJ_ywnQ-7wx68bmCsyIUta1Z5nQhch7W8KtURS7NYhYbKsf9m9DrsicEQN2LZVOZZzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇷
🇺🇸
سپاه پاسداران تصاویری از زیردریایی‌ بدون سرنشین آمریکایی که به عنوان غنیمت گرفته منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71338" target="_blank">📅 09:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71337">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71337" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71336">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua7cQtnFIePLf_qx4PUC8CixTk5yK3CDJgR_PGCVRw09NPKdetNUqapKkCwszSNd50d7_rCIUwUOa76_4SBeeyUSlRaxddjBdjyMrEXz9cgtC-sGF-oWBDuZMNHThrbEeNKqrles3nT4kiEel0IgH3gKEWI_Gin9Oy-dGa9bbrfL3nDpVRSrgLXKh8HcU7DtdeGXSdiaZzCAQ7Ni3D6RiXLE78wf2YvbDzwZubaPHBUl7U4XlVdNcn5YKPXnrv85A92wmaPnPvfLCAu43TcPnO7S62UE5BikrDDeq0WZzzXdU82OIcIB1g_ws6N-ZPFzWbi9BXEMeAq9cVqgDq-KgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71336" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71335">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
〰️
#فوری
؛سنتکام:
نیروهای سنتکام در تاریخ ۸ سپتامبر پنج شناور حمل نفت خام ایران را منهدم کردند؛ این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی طی دو روز گذشته، دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد.
کشتی جنگی آمریکا با موفقیت از حملات تلاش‌شدۀ ایران گریخت و به گشت‌زنی در آب‌های منطقه ادامه داد.
هیچ‌یک از پرسنل آمریکایی آسیب ندیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71335" target="_blank">📅 01:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71332">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
📰
خبرنگار العربیه:
چندین موشک ایرانی در جنوب سوریه رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71332" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71331">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=dIuajY6Nlb96G4EODBlWmKtragLQ6qusfALC2K15V4ScqgLQ_lTPub_bMdLIDJ3plGQx_a4trm1w2xGUwvt1pH6CpOubA-du30_6vt5C6-VFOoY9mqt5cV3f3VDw8OK9h90TVNcuDPHoHvkpgGK-q0Sxm2S1sRzEccUoGlpiN70ZVaYUPn87hUiYv2ltXWP7_1S-craPYjOJ3osBt_MuCMJX0dhlQVcNaHiFAseMnqFhu7snI4j9lM4clrGkdUhQNQEVejboRPTuWGuEQzMKSts49Nw8FbT9XV3bux-d_EJbnEXF9BdoH44znGlXtcNBpf2xvCBQa7A-M81f7xtMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=dIuajY6Nlb96G4EODBlWmKtragLQ6qusfALC2K15V4ScqgLQ_lTPub_bMdLIDJ3plGQx_a4trm1w2xGUwvt1pH6CpOubA-du30_6vt5C6-VFOoY9mqt5cV3f3VDw8OK9h90TVNcuDPHoHvkpgGK-q0Sxm2S1sRzEccUoGlpiN70ZVaYUPn87hUiYv2ltXWP7_1S-craPYjOJ3osBt_MuCMJX0dhlQVcNaHiFAseMnqFhu7snI4j9lM4clrGkdUhQNQEVejboRPTuWGuEQzMKSts49Nw8FbT9XV3bux-d_EJbnEXF9BdoH44znGlXtcNBpf2xvCBQa7A-M81f7xtMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمون اردن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71331" target="_blank">📅 01:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71330">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=LH7KQ1JO3ENJryebBNX7IeqdfPuWkkB5N4eRAAKUpNGK4bWESs52JKm-InEHMNLYUSiSYoc_FBM-s9k-DYjP_XcjWOQWh8-r2fb9ulscPNtqzqj_hs33OIWxrq0IoD3ylmMMSmAPc1oIq3WmWL6H8N1fLGLci7BSyF3I1XiLfCMMJFyDIcWZHUj853eDPLNLOURcY0SgWL976PA7R7IAiWBa9tx1niJAAOwjTQ6h_ZNcS5ACYjC6RHaocg9vYL-_fING3YFyJhp8tp7X21bekahy3iH9VdQBbupBTYcyt2HniPz_wnic1S3jhMftHvl3gFcHAHU4D9ypn46_1AmBXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=LH7KQ1JO3ENJryebBNX7IeqdfPuWkkB5N4eRAAKUpNGK4bWESs52JKm-InEHMNLYUSiSYoc_FBM-s9k-DYjP_XcjWOQWh8-r2fb9ulscPNtqzqj_hs33OIWxrq0IoD3ylmMMSmAPc1oIq3WmWL6H8N1fLGLci7BSyF3I1XiLfCMMJFyDIcWZHUj853eDPLNLOURcY0SgWL976PA7R7IAiWBa9tx1niJAAOwjTQ6h_ZNcS5ACYjC6RHaocg9vYL-_fING3YFyJhp8tp7X21bekahy3iH9VdQBbupBTYcyt2HniPz_wnic1S3jhMftHvl3gFcHAHU4D9ypn46_1AmBXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
مهمات خوشه ای سپاه در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71330" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71329">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇮🇷
نایا به نقل ازمنبع ایرانی:
سپاه پاسداران انقلاب اسلامی، دقایقی پیش، موشک‌های خیبرشکن را مورد استفاده قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71329" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71328">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=L0IoUoz7dCulVSMppUmZ7PARst4pFOYB1WBaw77FzClhO3tWBi5vcwKahfh_WHR9Kliw2bsFO2cR6CGY88M49Kf3v4TdWOHQDZCboXQ7UH3OvFxmDC5WuNDhsQQB4NHYCkEhjF6OnoLuEWYDLmXTGgoTk4J9gOf7EOjZTbHXhMSCDow60h0xPeFfCWVO5iBZPsonGahY7tZpTBw8flDVzuskKz9_z5cmemLPTdacrzY01w3vh8QqAJLkzMh4orwZeE9g7EsjUMPpJOtmqYIZOV58rOErMaCqSZNYPkOUszvRiPlJiYP8EpWsA7RsdFfkexmGTUiVB6CC0bexU6gSVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=L0IoUoz7dCulVSMppUmZ7PARst4pFOYB1WBaw77FzClhO3tWBi5vcwKahfh_WHR9Kliw2bsFO2cR6CGY88M49Kf3v4TdWOHQDZCboXQ7UH3OvFxmDC5WuNDhsQQB4NHYCkEhjF6OnoLuEWYDLmXTGgoTk4J9gOf7EOjZTbHXhMSCDow60h0xPeFfCWVO5iBZPsonGahY7tZpTBw8flDVzuskKz9_z5cmemLPTdacrzY01w3vh8QqAJLkzMh4orwZeE9g7EsjUMPpJOtmqYIZOV58rOErMaCqSZNYPkOUszvRiPlJiYP8EpWsA7RsdFfkexmGTUiVB6CC0bexU6gSVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گویا سپاه توی حملات امشبش از موشک خوشه ای استفاده کرده
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71328" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71327">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f211389571.mp4?token=q0oXcM9OPMORi5Lh5dfJhMODdhlf8JCUo-YNEkWWVuHBB16jjW77dduDezTT7A5BInsgFlOqmM6pEwJLQjJbzi99pxBvxo2KEjii2yPNxkRKfdPLcWZZKoAd_Xr4RtwM0Vg4jHqpBLH1jzQnG6Pbnc2gOcjuVZ3auooA4RXZlI9cK1UTz2TZhMuY5ZiyilTifRwljatICwiigru6ixsqo8tZGJ-3IqP8c-7rpwYvE8WokC78B9R2uaME1kj6UDwIg8vea8sOqNx4P3Og13iDnw_YJU4b--C16IH-tHzpCOrR3ID0LEvPDHHp2GT4bJky6nwpPEzaIT-LNs3mdshWlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f211389571.mp4?token=q0oXcM9OPMORi5Lh5dfJhMODdhlf8JCUo-YNEkWWVuHBB16jjW77dduDezTT7A5BInsgFlOqmM6pEwJLQjJbzi99pxBvxo2KEjii2yPNxkRKfdPLcWZZKoAd_Xr4RtwM0Vg4jHqpBLH1jzQnG6Pbnc2gOcjuVZ3auooA4RXZlI9cK1UTz2TZhMuY5ZiyilTifRwljatICwiigru6ixsqo8tZGJ-3IqP8c-7rpwYvE8WokC78B9R2uaME1kj6UDwIg8vea8sOqNx4P3Og13iDnw_YJU4b--C16IH-tHzpCOrR3ID0LEvPDHHp2GT4bJky6nwpPEzaIT-LNs3mdshWlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت شدید پدافند در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71327" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71326">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
از اکثر نقاط کشور به سمت پایگاه های آمریکا موشک شلیک کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71326" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71325">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=al335BQnQazok-ykuMcYTMZI8qQMiCPHgLQ2tHi_O_xQYbfZcgzKiVHst0bTSlG2QE7Oe00FmQ6p6AvWQ2LOYBQ9k6bmtLZpRFWJUx69jauX3XRhAx3VnWvaCxBIlTfPuj7f-K5Hk6trGCvwi_XHzs_CJnkSx89fECX6tIlAA1LOfZEAKHaABPevvtmDLwegt-7EnuShRTQpu5Hom9Rf23sL2qAspve9MP2aXDrEtMhvCeaXoNDeeDdsHJIp0ENwQxT6WSfzMBfQAL4gcrxWsEd8qa6tBQO3fTEYRZmpTA6gT8sA_9zxv3LNRLHuAjXw51M09jrZrDlZ4I6du0hYoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=al335BQnQazok-ykuMcYTMZI8qQMiCPHgLQ2tHi_O_xQYbfZcgzKiVHst0bTSlG2QE7Oe00FmQ6p6AvWQ2LOYBQ9k6bmtLZpRFWJUx69jauX3XRhAx3VnWvaCxBIlTfPuj7f-K5Hk6trGCvwi_XHzs_CJnkSx89fECX6tIlAA1LOfZEAKHaABPevvtmDLwegt-7EnuShRTQpu5Hom9Rf23sL2qAspve9MP2aXDrEtMhvCeaXoNDeeDdsHJIp0ENwQxT6WSfzMBfQAL4gcrxWsEd8qa6tBQO3fTEYRZmpTA6gT8sA_9zxv3LNRLHuAjXw51M09jrZrDlZ4I6du0hYoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موشک ها در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71325" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
ارسالی از اصفهان:
از نجف آباد دوتا موشک از اصفهان ۴ تا
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71324" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71323">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=u_Adm060uHnyJFGJ3h4Ve09VmP70V1jH6nK-N05nlvj40F251n3-X2AJwG66J0017hSYx_B6_5LRvIgOr3DHJ4ytNjmbKw5n8McpUG5VNqsEKwbhsYrRI7j6UkfFylTdPshbT-4VwMqdIR2EGPyQjBaSAUJMMupCRwCKk8UKqk7takF0hwyLICg0nZT2-e_cs9yoj164F_iEWQpG3_2Fl6A6u5z-hMD8JcrphEaLEaa7Dmzg8QOKaMdhRdwYEkVpt9B72Zw1XnMv-nzMvTSDeBop-L-dsS9BF51Tflje-qIpbcltC9PnsaKzR3NHx61S9ZDpmD2kMmoooC43B-8CcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=u_Adm060uHnyJFGJ3h4Ve09VmP70V1jH6nK-N05nlvj40F251n3-X2AJwG66J0017hSYx_B6_5LRvIgOr3DHJ4ytNjmbKw5n8McpUG5VNqsEKwbhsYrRI7j6UkfFylTdPshbT-4VwMqdIR2EGPyQjBaSAUJMMupCRwCKk8UKqk7takF0hwyLICg0nZT2-e_cs9yoj164F_iEWQpG3_2Fl6A6u5z-hMD8JcrphEaLEaa7Dmzg8QOKaMdhRdwYEkVpt9B72Zw1XnMv-nzMvTSDeBop-L-dsS9BF51Tflje-qIpbcltC9PnsaKzR3NHx61S9ZDpmD2kMmoooC43B-8CcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71323" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71322">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
گزارش ارسالی:
از زنجانم موشک زدن همین ۱۰ دقیقه پیش
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71322" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71321">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfTDkRmtX68G6GzBRWTMWlxrn2qH69DF7e5B-4lnEolpeM63kHBHtd3mZ7X-TGxkO3v4BhUgXaUUDAWkd3EWx51aLdJUyFTF8S8LboBGkoArfVcGak0507E0JcMHTGlwzkA3_YqkVvAFRWLuExtn5EI-KB50iKQUDpeqwE0ZvAZLY8scYquvOJLeAZG2R8b6bD244aClD0quDag9yjEwaHVWNqNQRZbjQMVASXvOyvREdeHAQGbgtxp69TSj4y8_UEcEPG5B5JsRZjhR7gFCr10OluzwITsl3Xki2gknsOCS0VTJmq9dgVt10uuiSTX7n4hcpa9eOXoF7e6OuGfapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارسالی از نجف‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71321" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71320">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc98612785.mp4?token=FyLQpNUjp07s8dRfMHmGw4zoaU1crox4fXPgFcIwAoKUQgbnw5PeMu2q9uTDBCuR4NyKphgMIs7P61na8Mme8iGfiYL9pJO4Wl_lxoK78gdOy1OyY4eItyoSnUsE26_JYbFtumbWGKacTFltDhlv66c5gWPsUv77nlVsrpoLaIfwQV4EUb5Atj6SF_LcQpZ3yfXxhJi5jxFCsvGLcZY4jKA9rpJw9jemRS-EGu7IftYXRSe1a0TyHTGlZ14YqDjkdyXYOxsDe2KMJ2PoO0nqdCX3qSJSYWU1DSAJ9UKz7zG4y_T9WgYFq3piwzeFm8yu0RAPM5xgXr3GFLTJhqOz4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc98612785.mp4?token=FyLQpNUjp07s8dRfMHmGw4zoaU1crox4fXPgFcIwAoKUQgbnw5PeMu2q9uTDBCuR4NyKphgMIs7P61na8Mme8iGfiYL9pJO4Wl_lxoK78gdOy1OyY4eItyoSnUsE26_JYbFtumbWGKacTFltDhlv66c5gWPsUv77nlVsrpoLaIfwQV4EUb5Atj6SF_LcQpZ3yfXxhJi5jxFCsvGLcZY4jKA9rpJw9jemRS-EGu7IftYXRSe1a0TyHTGlZ14YqDjkdyXYOxsDe2KMJ2PoO0nqdCX3qSJSYWU1DSAJ9UKz7zG4y_T9WgYFq3piwzeFm8yu0RAPM5xgXr3GFLTJhqOz4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارسالی از اصفهان:
حداقل چهار/پنج موشک دیده میشه توی آسمون
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71320" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71319">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c50434db49.mp4?token=YOsQ6oDSaZq0xPwn2Of4MVaOfFO1QHuZ0VoGP6ijTsdH28NbTPPggVEJKK06nyinjgbZd1k8ZEtNKVC0GmR47bfLnZADN8CaRo0c2hUizEWxhODSncoobrlOsVsq9qVRLlQpAVPKuGfmWL6V1iGyi8bM5WPCi6WVF9V2BJx9TFTVvM375dkLZ-FLw6tufMDSHI153JAXMfxb8bWNjTTabtHBbzEraNuqnXqn6LaHuGUB_NO8LG-elTbg-Jb73E9tC0sK8YA71cgtfpgSCDIMOcuWg2SfEIXaBVer5EupTi3BHAjWIxJqrYGciIHu-8HvRc4pa_KNnopyJL783fmiQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c50434db49.mp4?token=YOsQ6oDSaZq0xPwn2Of4MVaOfFO1QHuZ0VoGP6ijTsdH28NbTPPggVEJKK06nyinjgbZd1k8ZEtNKVC0GmR47bfLnZADN8CaRo0c2hUizEWxhODSncoobrlOsVsq9qVRLlQpAVPKuGfmWL6V1iGyi8bM5WPCi6WVF9V2BJx9TFTVvM375dkLZ-FLw6tufMDSHI153JAXMfxb8bWNjTTabtHBbzEraNuqnXqn6LaHuGUB_NO8LG-elTbg-Jb73E9tC0sK8YA71cgtfpgSCDIMOcuWg2SfEIXaBVer5EupTi3BHAjWIxJqrYGciIHu-8HvRc4pa_KNnopyJL783fmiQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ارسالی:
همین الان از دماوند موشک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71319" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71318">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
ارسالی از تبریز:
همین الان از تبریز موشک زدن
سایت موشکی امند
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71318" target="_blank">📅 00:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71317">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
چندین گزارش از خرم‌آباد اومد که صدای انفجار شنیدن./احتمالا پرتاب موشک
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71317" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71316">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ارسالی از بروجرد:
سلام بروجرد هم فرستاد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71316" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71315">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
گزارش ارسالی از اصفهان:
هفت تیر مبارکه اصفهان موشک بلند شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71315" target="_blank">📅 00:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71314">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfUsC-el_UvWpK65KSfZdpFJUVUKvV9gPYI_Qkpat32Ad1R3W_N63Yo7Vhzv0f4MJaTGTKu3PZdZ7yOBsCBouz1YAnYfTmWeQXqB4ZyVBRN1XL9YAZbxTVCqogVeIKF0Pcjpd-85_ECFK0yFIlGcVy2jFP6-5OPjUL7Cz8BrdYaYcnOVBZY_-i8dAx7JkArwHmJb4B-bJa__DBMoBHtdmvyxplTmAkLtbDrnPcGn73nj3zqgnN071JnWsKft1rNRXuBKFh_Zg4Y-h9qVoAcyVhucORUzoVkM6_YB6srymaDvDxlLiKv4uZA-aLWCmZUP5vVTU4AVyQkZ5zOWrdz6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71314" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71313">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
گزارش ارسالی از یزد:
از یزدم موشک زدن همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71313" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71312">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
گزارش از اصفهان:
اصفهان الان زدن موشک نمیدونم شهر رضا بود یا نجف اباد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71312" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71311">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
گزارش ممبرا:
۱۵ خرداد اصفهان شلیک ۲ تا موشک همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71311" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71310">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛صداوسیما:
دقایقی قبل نیروهای آمریکایی به یک فروند شناور تجاری در آب‌های ساحلی شهرستان جاسک حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71310" target="_blank">📅 00:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71309">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YArkdj0bVOp_KhmWxgh2V9mfZz39mX2ITfLSry30rAo_SsKLcbMzOCCU-aAO-dtWKSZdeWf2ST-rscbSP3T4K5YyD3QcrJaoGlyJgBmooqnGrsQTClXBu0Yh8jDH1jOlBmlzKQrXKmB2umrsAIr20u9PTcOzs3gQ8veqYtIKixX7wQfGIdtBUiuA5H4cV4ox55REzyXQt11zNhwJoh-3LJ8LxZveb72V9hVszwnBtS76VX25Mp_osYGXPZB4OL82DJIj_sZaZBrWX3GY3OuTVdURciLpbaKAHiAh3wnrZXikkuHbZPAuVBXLwfBBg5Lw28MOmIaKw9sUY_AKcLnfvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:ایران ظرف سه روز، دومین موج حملات موشکی را علیه کشتی‌های نیروی دریایی آمریکا انجام داد، اما هیچ‌یک از شناورهای آمریکایی هدف قرار نگرفتند.
این حملات موجب نگرانی واشنگتن شده است، زیرا به نظر می‌رسد ایران از موشک‌های پیشرفته‌تری استفاده می‌کند که قادر به هدف قرار دادن کشتی‌های در حال حرکت هستند.
مقامات آمریکایی همچنین در حال بررسی این موضوع هستند که آیا چین یا روسیه ممکن است در شناسایی موقعیت ناوهای جنگی آمریکا به ایران کمک کنند یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71309" target="_blank">📅 00:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71308">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYkHKVmAPvWGW7b03AZ0u6wG32QBKWrpvVGdbgl8KgvHgsoxDE3MSBMKWEbrwM20AgHpaNY9YLQB-Z6EW7uavS7Q_-r7Sp7e9c6Bavfosv_3ikDCgsgO3qGLPryHgyHt8nd5re0zQcuLaz6cxih_B2MKj8LLr5Rxdu-8_ZVB7KOfaHoeVlpyIFOXMY1YAs8oWpMBWtNrC_ZztRvtXe6fICrSCfyd0kziouYUSe85gP-wy9D_rb7xWKK58xWgW3nBr1c2bFhFVwGVxf_OFrLFOHaVKIPs2vPTBGAq_jdMqOfE0cFaJrhaO1noe45jUaEqtl3j_PxbanhHmhkGw9TRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
به تمامی خدمه نفت‌کش‌ها در بنادر و لنگرگاه‌های کویت و بحرین هشدار می‌دهیم که فوراً شناورهای خود را ترک کنند، زیرا این شناورها هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71308" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71307">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9XMI8q-vpbFZWFV5XPYhZd1fBrHT7Pz78rea934XLAt-IZRp3xRaTzovkLNLp2GyI-sV9Zd7vh2fEpj2jPrbH8GqPVHiZh8qoLiJ8LItYbVH-njhsmMpGtcoZN2KbZyjsHe3rRteyj9RSQff62yg_sjh1-hAzVDyzw0o7b3YUbckslHWLlEx6ABWhbz5fxXKrxC1HoqnP6Nef6MV71yIzQlQuclXDDCgsAjWbGaxwezpiXnbI48vh8LbOs-yqJt7tkxncvzE-9PxYi6XP_6LHSKAE5raTjpMZoM32aVrABX2fVyj_UtY8cAkDef0uz_5Anc-po6Mjx9LqVd5x-kCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
مصطفی نجف زاده:
آمریکا با هدف قرار دادن نفتکش‌ها در سواحل ایران و مشخصا خارک، علاوه بر اینکه می‌خواهد بازدارندگی معتبر در برابر رویکرد تهاجمی اخیر ایران در حمله به ناوگان دریایی آمریکا ایجاد کند، ممکن است گام تازه‌ای در راهبرد محاصره نیز باشد که براساس آن، قصد دارد حلقه فشار را از مسیرهای انتقال نفت به مبدأ حرکت نفتکش‌ها منتقل کند و صادرات انرژی ایران را از نقطه آغاز با اختلال جدی مواجه کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71307" target="_blank">📅 23:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71306">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
📰
فاکس نیوز:
امشب
برای سربازان امریکا دعا کنید
نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز
ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی حرف‌ها* می‌زند
امشب برای نیروهای آمریکایی در منطقه دعا کنید
و برای خانواده‌هایشان که بدون شک نگران پسران، دختران، شوهران و همسرانشان خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71306" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71305">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=BTABvJr70eYtCFILDdChx4j83nT21XFCQ_wa8LnZHRE6pZ4xUn2knaSfJ9U6ApY79vLUvK4XjEjEWrD0cQDI3mkpvEnpEJ7fGNDNzRaAKU3nAoFU8BYSMeKvGxMQqgmw8AzicFCWVYyE9DX104IAZb4p67GN-QpW8alRHCFaCILAykUrJ3_cQza0fLth2Pfj2qFRtUo61C4CyoxkwUFpveN_soFZOF7ZsUHjTS0d_8cLIhacf0qtqoKILBZ-dm1RHEVKPhgGA20L9j-UvJc2qzB-YRj53O9V59losv0flfKukoXHnDaOXpFY90I1tx7mkwgAKGtnDVMY_3PFW38elQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=BTABvJr70eYtCFILDdChx4j83nT21XFCQ_wa8LnZHRE6pZ4xUn2knaSfJ9U6ApY79vLUvK4XjEjEWrD0cQDI3mkpvEnpEJ7fGNDNzRaAKU3nAoFU8BYSMeKvGxMQqgmw8AzicFCWVYyE9DX104IAZb4p67GN-QpW8alRHCFaCILAykUrJ3_cQza0fLth2Pfj2qFRtUo61C4CyoxkwUFpveN_soFZOF7ZsUHjTS0d_8cLIhacf0qtqoKILBZ-dm1RHEVKPhgGA20L9j-UvJc2qzB-YRj53O9V59losv0flfKukoXHnDaOXpFY90I1tx7mkwgAKGtnDVMY_3PFW38elQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این فیلم‌ لحظه‌ای را نشان می‌دهند که هواپیمای باربری آمازون در روز یکشنبه در فرودگاه بین‌المللی میامی از باند فرود خارج شد و متاسفانه ۵ نفر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71305" target="_blank">📅 23:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71304">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=dZCFs3gGDtbp-BHaDyaTKx2Mv-uVLvlzlbhNKqffD7HNeq09vKkbAui4fKm4pk0-ToGediVe81ADom5gTgu_d16ZedZgKSFSkDzKxjTfq0oIXkGQos4GxxqmQLicgILltIpl4ojDUoXZ-gykh3t7g0Rd-UKvkIfLJa6IDhMz8mAA7DDtaYh5x3jdTjaimpylGeYdlvO0JjIUCt5Uv6EB3v1emV3ANwd0BTOelFGx-X6jInox_Jy7_TSnSh2qLSYtTcgaGHT_6p-iuDB3af7zV1gcpgUkOh48OKOzqWLejuMmkxvTdTf51KaH2kenrIBXLdfB0nu8yTe1GrrbZPLnug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=dZCFs3gGDtbp-BHaDyaTKx2Mv-uVLvlzlbhNKqffD7HNeq09vKkbAui4fKm4pk0-ToGediVe81ADom5gTgu_d16ZedZgKSFSkDzKxjTfq0oIXkGQos4GxxqmQLicgILltIpl4ojDUoXZ-gykh3t7g0Rd-UKvkIfLJa6IDhMz8mAA7DDtaYh5x3jdTjaimpylGeYdlvO0JjIUCt5Uv6EB3v1emV3ANwd0BTOelFGx-X6jInox_Jy7_TSnSh2qLSYtTcgaGHT_6p-iuDB3af7zV1gcpgUkOh48OKOzqWLejuMmkxvTdTf51KaH2kenrIBXLdfB0nu8yTe1GrrbZPLnug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آیت‌الله بی‌بی‌سی از لندن فرمودن بنزین(۱۰ هزار تومنی) در ایران تقریبا مجانیه. این دقیقا عین جمله‌ایه که آیت الله بی‌بی‌سی برای مردم ایران پخش کرد!
تا حالا شده بی‌بی‌سی فارسی حقوق کارگران در ایران رو هم به دلار حساب کنه و نتیجه بگیره مجانی کار می کنن؟!
یا تورم رو حساب کنه و مقایسش  کنه با حقوق کارگر؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71304" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71303">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=YaHZ3RrLuuXEYx4pu_kjASc8fnoMxWF2WMx-O-U41Tx6AlJ5YtLGh0C9uJMY8ujRh5db62OyhNUdhKrdiiV_FZ5AKUgV51vXdBgYRwZo1oIzqLoskfk_jWRlPlwvtEtiM5-6x6FGXuquExMzJtXEO4nSqg_ASnYwKkYRgLqIAZ6xalQoWTfAhcaytknF20h_mUUMu00Zg6-KfoHvWyH6YlBezYXBvCxMlR3IW4R2ez49GoWJR1mHXCU87wRWp9v2LQ_GoC4HE2OE7FZfRwUqP0AQjW9Lc9GYdvZ4IMsh6_Sd0lcmVpiFSpvmqFZbAhAG2zJD-xqgIN7krm2RCIzRfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=YaHZ3RrLuuXEYx4pu_kjASc8fnoMxWF2WMx-O-U41Tx6AlJ5YtLGh0C9uJMY8ujRh5db62OyhNUdhKrdiiV_FZ5AKUgV51vXdBgYRwZo1oIzqLoskfk_jWRlPlwvtEtiM5-6x6FGXuquExMzJtXEO4nSqg_ASnYwKkYRgLqIAZ6xalQoWTfAhcaytknF20h_mUUMu00Zg6-KfoHvWyH6YlBezYXBvCxMlR3IW4R2ez49GoWJR1mHXCU87wRWp9v2LQ_GoC4HE2OE7FZfRwUqP0AQjW9Lc9GYdvZ4IMsh6_Sd0lcmVpiFSpvmqFZbAhAG2zJD-xqgIN7krm2RCIzRfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این روزا تور مدیتیشن و استراحت مد شده و طرفدارای زیادی داره
:
اونایی که مشکل روحی روانی دارن میرن درخت بغل میکنن و گریه میکنن
یا با حشرات توی جنگل و حیواناش اینا حرف میزنن حرف میزنن حالشون خوب میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71303" target="_blank">📅 22:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71302">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=YCNz-Tipt5NzkmNcBlEh9nD5ANPv3-ZTcu7Dls6DXqqzpQT7GAxGvB-jnnFppDWWlfZ-S_E2XqBB-EK6bUEcnQaO1HQI_FmzMOodgtZBbXXrNKLSYVfUoP-CiQc5lcpOKnmQGWCuM2_ZEUZLA3NDvJB9dBpLyfSCBMj_TvvT1VgIvQs0CELa1vDgedkBc4rfQqr-1z8CT_2fIFsipY0H4kwg_NINVlDE4FT2TtaBzJqBYLjpjNqcGqRG4DAwlaVENHnfixJOQyiogi4McW1C-Zxpp8kO4bE_iyBfKXR5q3eWOxt-MJogbXe8JRTK2-NiiJyRwjtKMKQbk27525OH6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=YCNz-Tipt5NzkmNcBlEh9nD5ANPv3-ZTcu7Dls6DXqqzpQT7GAxGvB-jnnFppDWWlfZ-S_E2XqBB-EK6bUEcnQaO1HQI_FmzMOodgtZBbXXrNKLSYVfUoP-CiQc5lcpOKnmQGWCuM2_ZEUZLA3NDvJB9dBpLyfSCBMj_TvvT1VgIvQs0CELa1vDgedkBc4rfQqr-1z8CT_2fIFsipY0H4kwg_NINVlDE4FT2TtaBzJqBYLjpjNqcGqRG4DAwlaVENHnfixJOQyiogi4McW1C-Zxpp8kO4bE_iyBfKXR5q3eWOxt-MJogbXe8JRTK2-NiiJyRwjtKMKQbk27525OH6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
زمانی که بچه بودم و در کارولینای جنوبی زندگی می‌کردیم، خانه‌مان نزدیک یک مرداب بود.
گاهی مارهای سمی زیادی در حیاط پیدا می‌شد.
وقتی سر مار را قطع می‌کردید، مار می‌مرد، اما خودش نمی‌دانست که مرده است؛ بنابراین باید مراقب می‌بودید، چون سرِ جداشده هنوز می‌توانست شما را نیش بزند و دُم مار هم ممکن بود تا زمان غروب خورشید تکان بخورد.
اما وقتی خورشید غروب می‌کرد و هوا خنک می‌شد، تکان خوردن دُم هم متوقف می‌شد.
🔴
حالا مار ایرانی — یعنی همان رهبری — هم هنوز نمی‌داند که مرده است، اما در واقع مرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71302" target="_blank">📅 21:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71301">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=tDb12_e2HrGAL-duPzBLHR6DF_ncuDXi_whYj7mQl5XOmO-4Tcmg23_1sT-cT21xhJ7Z3Gj_SZ388UA2IJlGgS6UvLtpQ51AJ6GABOjQHrpg2tThk3hLgXZg7vJIQzUuXntXW30dZxAOurT5vt-J1UujQdDCFlWqdvtV0GVDdTpf_XYNJK7XoQOM1VdXK5EbRmcYfjfQtvHb4TLwzvojhixJ66enlrtjrAaj72Ev0rXRW0XAZWR58ZbZ3nPfLzaMeJ5wtGGjtS6IlvqVB_Db0DyLO0VUTH9Jl-F9C2AsWL7poYpcKvawa0ctktT9MLyuFCSy0w630lcOZgTGhegoUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=tDb12_e2HrGAL-duPzBLHR6DF_ncuDXi_whYj7mQl5XOmO-4Tcmg23_1sT-cT21xhJ7Z3Gj_SZ388UA2IJlGgS6UvLtpQ51AJ6GABOjQHrpg2tThk3hLgXZg7vJIQzUuXntXW30dZxAOurT5vt-J1UujQdDCFlWqdvtV0GVDdTpf_XYNJK7XoQOM1VdXK5EbRmcYfjfQtvHb4TLwzvojhixJ66enlrtjrAaj72Ev0rXRW0XAZWR58ZbZ3nPfLzaMeJ5wtGGjtS6IlvqVB_Db0DyLO0VUTH9Jl-F9C2AsWL7poYpcKvawa0ctktT9MLyuFCSy0w630lcOZgTGhegoUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقتدار به روایت تصویر؛
🇮🇷
مقام جمهوری اسلامی:پمپ های قدیمی جا برای بنزین ده هزار تومانی نداشتند؛
یک صفر دستی اضافه کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71301" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71300">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">از دیشب تا همین الاناست که مسلمونا افتادن به جون هم، شیعه های یمن، سنی های عربستان رو دارن با موشک و پهپاد می‌زنن، یعنی کشوری که خانه خدا اونجاست
عقل
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71300" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71299">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZW1eBeUhOXAOYRP0fVEXUUIF3O8J6b0e2_GkI-jzPprq-Lkmb6QYDvTHzgt1Naieec_yxLKfN5s4OHkURIXZY-r91_1-qTzRijK9mRI1xj5cKAk9qdVEXNif9zb1XT7F79bkBJmUxdCkgb0RsKPN9U_dPWYwKe2bnMq7wuy04c0YbE7xnY7WCBwltwtlHLZiLfDk4t3etjydpfvFhlUa4At-HJ99ekxYN-ZuC4psSP0mNrlO4DkGSNFjUxa6yFOx9vczPvNLhffHTEWmiolOZZXIzwqJ_F37K16aJysAufqy0sCWVz_o0rhHl77QF3Wx3AkUEjBqThTDQJFD0UZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
وزارت خزانه‌داری ایالات متحده تحریم‌های گسترده‌ای را علیه بخش هوانوردی تجاری باقی‌مانده ایران تحت عنوان «عملیات اقتصادی مطرود» اعمال کرده است که ۳۶ نهاد را به دلیل حمایت از خطوط هوایی ایران، دور زدن تحریم‌ها و شبکه‌های تهیه هواپیما هدف قرار می‌دهد.
دفتر کنترل دارایی‌های خارجی (OFAC) ۲۷ شرکت هواپیمایی فعال ایرانی، از جمله ایران ایر تور، هواپیمایی آسمان ایران، هواپیمایی کیش، هواپیمایی قشم ایر و هواپیمایی زاگرس را تحریم کرد.
وزارت خزانه‌داری همچنین چندین مجوز هوانوردی، از جمله مقرراتی که پروازهای خاصی را مجاز می‌دانست و به شرکت‌های هواپیمایی غیرآمریکایی اجازه پرواز هواپیماهای آمریکایی یا تحت کنترل آمریکا را به ایران می‌داد، به حالت تعلیق درآورد.
این تحریم‌ها همچنین شرکت‌ها و افرادی را در امارات متحده عربی، ترکیه، بریتانیا، مالزی و قزاقستان که متهم به حمایت از ماهان ایر هستند، هدف قرار می‌دهد. وزارت خزانه‌داری اعلام کرد که برخی از آنها انتقال حداقل سه هواپیمای بوئینگ ۷۷۷ به ماهان ایر را از طریق امارات متحده عربی و عمان در تابستان ۲۰۲۶ تسهیل کردند، در حالی که برخی دیگر محموله‌هایی از جمله قطعات پهپاد، تجهیزات صنعتی و قطعات هواپیماهای ساخت آمریکا را جابجا می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71299" target="_blank">📅 20:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71295">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJDbhIZMjJTdoUfjr3eJHL07C53fp4gL78TBZFZFMKdJN-ttD5vrJG1wZfEaQq2ZjLhHnLEPgLl1rt75zsCMZhHfHC0EnA-DgiJXpv70qi83xH_ZIIomxleb8NeCtjWVPtlG_vMHnh9nEEe6J-T8si_rjPPCvCml1zj7rQDUi2DySSwYpc6sa9VX2YxJvimQ8IPEWdQUir6Kf4SxKp_QQW9pIUorNNpjzWwVqDifWTIDy3SN92kynTN_4whoDy8myIb-ETOz64021zSUWn7oopvAdyhkk8R-FQJ1xYprCKC988aoyQkSiGllVg4_m4XlEwM4_ikXxCTSORFVvsjBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d307bda604.mp4?token=b6UIiKS0sSpdbngRy_DSAjf_08VgRd24HYPEK15Y_9gLpElNe452-3ayCBRR-XqjE1C_EBuP1Pmj5ke43rs34-X21KymxdkHk26RU69_U3taiZ6_66uAfygXElNCab7Mvv2R1tY6e6hpo4lP9bDo3ynwYS9c8wa6xBf1gAGxW0R7Wehy22mjD01PeMaFiqt0NgB44b45OuyfM_zPZC0GTlMPt2KCDKzyx-ZX4OrYF_9NqTiuUWoTrDYZkwXeQxjb8aNT3ZrXdV_V5uWWVSiQpz_Ae91tOYrJe0Muk81yvsVE-EqvM__pbohzMLYgdqGLLeohlU-gRmZEKy_E0eFe4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d307bda604.mp4?token=b6UIiKS0sSpdbngRy_DSAjf_08VgRd24HYPEK15Y_9gLpElNe452-3ayCBRR-XqjE1C_EBuP1Pmj5ke43rs34-X21KymxdkHk26RU69_U3taiZ6_66uAfygXElNCab7Mvv2R1tY6e6hpo4lP9bDo3ynwYS9c8wa6xBf1gAGxW0R7Wehy22mjD01PeMaFiqt0NgB44b45OuyfM_zPZC0GTlMPt2KCDKzyx-ZX4OrYF_9NqTiuUWoTrDYZkwXeQxjb8aNT3ZrXdV_V5uWWVSiQpz_Ae91tOYrJe0Muk81yvsVE-EqvM__pbohzMLYgdqGLLeohlU-gRmZEKy_E0eFe4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌂
امروز صبح رسما شمال کشور رو سیل برد!
به حدی بارون شدید بود، که حتی آب توی خونه‌ها نفوذ کرده و تبدیل به استخر شدن.
ماشینا وسط خیابون تبدیل به قایق شدن و برق اکثر مناطق قطع شده.
باد و طوفان شدید باعث شد کلی درخت و... شکسته بشن و بیفتن روی ماشین، خونه و مغازه مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71295" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71294">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLBc6Wdvk-EQTBw-u-wyMvfh2upCBouSAliqLJyBbafS3wcnYLsWmkuoMYz7FYqBqo-8H82HDMfwgpQ4FUsJrcZz90UwnQtaz-cOxloTI8JS1ZZnOGzxQGHr4MSM2icggRvVTk-0Y0y1HRyDCDh_qozvxOXzs9NH5p3vbXoSNPLAr4Lg9RPhkckpRyM0Kb0Ul5FdCSQoXAfy8hKBbL3uTAzCjcLVL236y8-vP4pQjdVEijOhcHTFIDMonw4ylXBJ6TFpzVZDEghO2vaUqSwtb_dIodPtD_no7tyqIddNTkQ_ubzuWpW7J_OJMjygBPbZxUEFw-wtboL8wr1cKvtH_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران انقلاب اسلامی:
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی‌های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز طی یک اقدام پیچیده اشراف اطلاعاتی و عملیاتی در سحرگاه امروز به دام انداختند.
این زیر سطحی هوشمند از جدیدترین تکنولوژی در حوزه زیر سطحی در دنیا برخور دار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش تروریست آمریکا تحویل شده است.
گفتنی است این زیر سطحی اکنون به غنیمت گرفته شده و طی ساعات دیگر تصاویری از آن منتشر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71294" target="_blank">📅 18:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71293">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⏺
🤩
تسنیم:
تا دقایقی دیگر خبری مهم از شکار رزمندگان نیروی دریایی سپاه در تنگه هرمز منتشر می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71293" target="_blank">📅 18:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71292">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=aUiBBbdfslvaEjnBUbJVBndgTsgx4Zh0_KR36MAwnNyT7QlRowFSb_-S8gcIiaER3vrNGom3w_xoYZlipWka_o27QXF5zjU5pEkBE1SxnXFEzpSuzcxRhoSkWIxUkohtyl5Dqj7CM93FbiKc1s0FYZm1aeVUCFX0fkNTtgouK6UmsIdMO2joqPGbYXdJRhckWnCRkfLAgZh55hUKHEBdzuooRHwr9wAQCaSyzfCBM9RubXkYDvHyTHVCKgtgzavFsR86j4_4YOBqbHLQeUHLlGYdxQlMZgjTj_mveF43QDl8eqlQCJlE6H_EHFBYI29sNPeTigrqrwDhHN8jPSwZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=aUiBBbdfslvaEjnBUbJVBndgTsgx4Zh0_KR36MAwnNyT7QlRowFSb_-S8gcIiaER3vrNGom3w_xoYZlipWka_o27QXF5zjU5pEkBE1SxnXFEzpSuzcxRhoSkWIxUkohtyl5Dqj7CM93FbiKc1s0FYZm1aeVUCFX0fkNTtgouK6UmsIdMO2joqPGbYXdJRhckWnCRkfLAgZh55hUKHEBdzuooRHwr9wAQCaSyzfCBM9RubXkYDvHyTHVCKgtgzavFsR86j4_4YOBqbHLQeUHLlGYdxQlMZgjTj_mveF43QDl8eqlQCJlE6H_EHFBYI29sNPeTigrqrwDhHN8jPSwZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
⚠️
🇺🇸
افسر نیروی هوایی ایالات متحده که در ماه آوریل پس از سرنگونی هواپیمایش بر فراز ایران، دو روز زنده ماند، برای نخستین بار در برنامه «۶۰ دقیقه» (60 Minutes) — که قرار است روز یکشنبه پخش شود — به بیان ماجرا می‌پردازد.
این افسرِ مسئولِ سامانه‌های تسلیحاتی که نام عملیاتی‌اش «دود ۴۴ براوو» (Dude 44 Bravo) بود، یکی از دو سرنشین جنگنده «اف-۱۵ ای» (F-15E) به شمار می‌رفت.
در حالی که خلبان ظرف چند ساعت نجات یافت، «براوو» به مدت دو روز در مناطق کوهستانی ایران، در حالی که مجروح و تنها بود، از دست نیروهای ایرانی پنهان ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71292" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71291">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71291" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71291" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71290">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQ_h8xRoY2SeAZwnlKmky87wuoeHEAb__usBh1bhjv1OJ_99aBwuDclZRVVbGoar9LTBwentfv3g91V9aLQYulSfem3iJO-bpavdabfjr77ehfdW2L78a0W02xS4Igr5ZwjN7nXyVM04tmsYbwzYqM0SZP0VQS2dYc8MPtcczO3Pxe3pmig1X5h_FZ3SPiu7oyHmfPnm7fl48SkOxHiuI3-0_BYtjcrUKR4GqvLLoH_wYeReBK8LILMnD8v1-PLPuKGmb0CbFX2kdFGlkLFw9qnRTONWRVWJO-cWAnPRwv7yAbxyGDHtwC-b4ySMPEeEdQKxEGF3K1kXrQlReDlpfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
منچسترسیتی
🆚
پورتو
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
منچسترسیتی: ۴ بازی، ۳ برد و ۱ تساوی، ۹ گل زده
⚽️
پورتو: ۴ بازی، ۳ شکست و ۱ تساوی، ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71290" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71289">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
دقایقی قبل صدای سه انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71289" target="_blank">📅 17:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71288">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=MmXe-nIZOMGYf39ngHP00TrzwdgMmEsX3--ZCo9CiTdntDgnHTrDwCML6bK-JbtEgcU-rmrctD0GGUgBriMqNwW4HDxTSeWn5aOisTOWyX8j_mlyBTjEPyMNWY4Mu_IuMk7cn6tlQ62tq_R4yLdBHrtSz5VPICaPiiKKZ7juVhVdlVgLaTDnVtp_p1T3lx1Nmm25paLrBEsp3npLBUcWthbAs4TLqy_pJseU6ff3iAWzmpfYiGYIMlyZSVfzRtY66B-ZYuFFro7cktdGEuakAKXmLrMUWH1iNjKHMFOzd1NtabQD0GqA-Yqxwanco02c59qrzhJ15bnxCRi8z8zQzULQ_XpKGx2Q43GVPBdaCYSfDcLkwv_HwlFRndNaYNBBkAOUYR_RowBHxQHgmuJxj4rhQfaLhbcX6coVzfUr9L9dSfLO9YYxnctEoiHzVm0zXMssQoZqXqOCQIV3A9ZqQpiPflgI5U7vLMS0hVi4Ms9SP0AhNUgsTWg7J25J_MDZaEjLwJz93zUnqbYXlBbjQliHdizgLojZeO-oc3P54B2gIcyetZAggRzxI2xPsYHxlluyTMxE0-AmGbum8cE46V-KVfgqinMVCtDtW9I6xQtmtny1xwV6sHnqqL_TPaYrXFGYGbJwnlQnLovBzjN4mVOYkMtbJWc0qE4etCkcC8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=MmXe-nIZOMGYf39ngHP00TrzwdgMmEsX3--ZCo9CiTdntDgnHTrDwCML6bK-JbtEgcU-rmrctD0GGUgBriMqNwW4HDxTSeWn5aOisTOWyX8j_mlyBTjEPyMNWY4Mu_IuMk7cn6tlQ62tq_R4yLdBHrtSz5VPICaPiiKKZ7juVhVdlVgLaTDnVtp_p1T3lx1Nmm25paLrBEsp3npLBUcWthbAs4TLqy_pJseU6ff3iAWzmpfYiGYIMlyZSVfzRtY66B-ZYuFFro7cktdGEuakAKXmLrMUWH1iNjKHMFOzd1NtabQD0GqA-Yqxwanco02c59qrzhJ15bnxCRi8z8zQzULQ_XpKGx2Q43GVPBdaCYSfDcLkwv_HwlFRndNaYNBBkAOUYR_RowBHxQHgmuJxj4rhQfaLhbcX6coVzfUr9L9dSfLO9YYxnctEoiHzVm0zXMssQoZqXqOCQIV3A9ZqQpiPflgI5U7vLMS0hVi4Ms9SP0AhNUgsTWg7J25J_MDZaEjLwJz93zUnqbYXlBbjQliHdizgLojZeO-oc3P54B2gIcyetZAggRzxI2xPsYHxlluyTMxE0-AmGbum8cE46V-KVfgqinMVCtDtW9I6xQtmtny1xwV6sHnqqL_TPaYrXFGYGbJwnlQnLovBzjN4mVOYkMtbJWc0qE4etCkcC8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇬🇧
⭕️
#فوری
؛اد میلیبند، وزیر امور خارجه بریتانیا:
ایران هرگز نباید به سلاح هسته‌ای دست یابد؛
از این رو، ما نیز در این هفته همگام با متحدانمان اقدام به ارجاع پرونده ایران به شورای امنیت سازمان ملل متحد به دلیل نقض تعهدات هسته‌ای‌اش می‌کنیم.
همچنین امروز می‌توانم اعلام کنم که ما در هماهنگی با اتحادیه اروپا و ایالات متحده، تحریم‌های اقتصادی عمده‌ای را علیه ایران مجدداً اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71288" target="_blank">📅 17:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71283">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645274372a.mp4?token=mr9wNzmIFAjIQb0m4lcb1-QDZm5DSDryF17NyeRDd77geL1kbLgmxYwhpj9ewoG05OoN8IeC1v-nt7LaJgM2nSXy1UatoxjLzB9yx_ww7ywLsWX1GnTfLmbWRlfkSN4sM7t_yiVPSq52pkyxRwkW7vvnTnsXG71sN9Fh5iltuS0AkWNGmL4YrxkSQuXh_MAfsFqEnn42_B9NpvpePWaxx6OyV77S3SEb9uDlpA-gLbLkdoiK6jKsJ1-R4dK2E36lTqVkmnz67jYvRWlLGQtQxNBOSrphiTatzxN9E87JZOw7VfSxbGWwq2Qdr9NjI0GWkjJINwbp9mREn80ZHOrcQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645274372a.mp4?token=mr9wNzmIFAjIQb0m4lcb1-QDZm5DSDryF17NyeRDd77geL1kbLgmxYwhpj9ewoG05OoN8IeC1v-nt7LaJgM2nSXy1UatoxjLzB9yx_ww7ywLsWX1GnTfLmbWRlfkSN4sM7t_yiVPSq52pkyxRwkW7vvnTnsXG71sN9Fh5iltuS0AkWNGmL4YrxkSQuXh_MAfsFqEnn42_B9NpvpePWaxx6OyV77S3SEb9uDlpA-gLbLkdoiK6jKsJ1-R4dK2E36lTqVkmnz67jYvRWlLGQtQxNBOSrphiTatzxN9E87JZOw7VfSxbGWwq2Qdr9NjI0GWkjJINwbp9mREn80ZHOrcQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
نیروهای «شورای رهبری ریاست‌جمهوری» (PLC) تحت حمایت عربستان سعودی به همراه جنگجویان قبایلی، شهر «الیتمه» در استان الجوف را از کنترل حوثی‌ها (انصارالله) بازپس گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71283" target="_blank">📅 16:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71282">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⏺
فارس:
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق ارتش جمهوری اسلامی ایران شناسایی شد و هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71282" target="_blank">📅 16:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de453ade.mp4?token=A5Cl6bI2R53alal5ofKDRTMX_5jpmNuHyfCaQtUv0XdzAHVZ84wh3ZLmgYbMjUdebeLGzKOHYZS6Meqfw62NXxtESli9H_aTvGPH-G2UwTMypp6exeGtzLnOkbWQvaU3Hl8449ZgnFWnKuDawk8mQi70QpD52NLGhXGyjkc96otL9GoSS8ClV7NRUu1LVgSKTIINjP5qk3hq9zSlvNIX-fUt1s68ukI-5aSn17P9Ab8b5UzxzcejDEVU47Fox-9T-ewR95AWXdg-Pu1lzL41LPaGbGdotcPH7KHYnGAt4D19cQvyhncUOhF4BuaTEeNMjl309P0gz36i_CDz6D_ZIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de453ade.mp4?token=A5Cl6bI2R53alal5ofKDRTMX_5jpmNuHyfCaQtUv0XdzAHVZ84wh3ZLmgYbMjUdebeLGzKOHYZS6Meqfw62NXxtESli9H_aTvGPH-G2UwTMypp6exeGtzLnOkbWQvaU3Hl8449ZgnFWnKuDawk8mQi70QpD52NLGhXGyjkc96otL9GoSS8ClV7NRUu1LVgSKTIINjP5qk3hq9zSlvNIX-fUt1s68ukI-5aSn17P9Ab8b5UzxzcejDEVU47Fox-9T-ewR95AWXdg-Pu1lzL41LPaGbGdotcPH7KHYnGAt4D19cQvyhncUOhF4BuaTEeNMjl309P0gz36i_CDz6D_ZIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جنازه و تابوت ترامپ و نتانیاهو زیر پای طرفداران حکومت برای بار هزارم له شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71281" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=HDuAvu68Lz3A8-9uMzZqgbu8vL391IqjsT1MEtIx87ePFpRvBsBmXqwWggf-q7KvJiMyLELG0BYIxE1gz-O74BYmf3wO4eyJLuTh8o5mwpslum4q1iSYQ6wXrptgyQviNlKKKjOmoWWxFWL6pVsmEIscwE2h61LPsqQHVdh8RNBS72dk3m8XvQcsqK0AUZhOGMS-LkkKFY7-gB_gKjgHSyOisGIMiIpDcjTN6yqnyAlU18veHTSHOiXdHLovvNNESBsfcR79q5bWrmnsSlees10jbX62Pdlc6fuGPDGcfEl5o4qdtYGVJupvk3er1oiCl9eP_9b_ugQnVZ7RKSTl4wi2SNp0RAMuPwb_Yp5cbnVNlW2dgrKr_cNsKr6G9WEGbjRUuhEPHCpqjGdcWazCFR02szhvkhzjXx9tvZU6PMkooOzKbQ2BncLhfUCnxHH48IRKpLSUAyLY1P4j5jiC-GcimAkIK39jxv6WmJL4kOcVTDx6hh8EGAlSMlxhI-NCR0ftWQt1wdG4wEjiII8LdRBuduGNpMK31lH6g8gonHNxnmXB6U2VVQp4zJV51MnZz_AH8KamyY8QD0z3kXk9rSuPi1IY5B386xLEtaL51vJR_F7qv6Lvqi_NFkZLm4u8m5EJW4IpY6hdesShQw3jRmBxLmCRctiK85Fjl9VZLRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=HDuAvu68Lz3A8-9uMzZqgbu8vL391IqjsT1MEtIx87ePFpRvBsBmXqwWggf-q7KvJiMyLELG0BYIxE1gz-O74BYmf3wO4eyJLuTh8o5mwpslum4q1iSYQ6wXrptgyQviNlKKKjOmoWWxFWL6pVsmEIscwE2h61LPsqQHVdh8RNBS72dk3m8XvQcsqK0AUZhOGMS-LkkKFY7-gB_gKjgHSyOisGIMiIpDcjTN6yqnyAlU18veHTSHOiXdHLovvNNESBsfcR79q5bWrmnsSlees10jbX62Pdlc6fuGPDGcfEl5o4qdtYGVJupvk3er1oiCl9eP_9b_ugQnVZ7RKSTl4wi2SNp0RAMuPwb_Yp5cbnVNlW2dgrKr_cNsKr6G9WEGbjRUuhEPHCpqjGdcWazCFR02szhvkhzjXx9tvZU6PMkooOzKbQ2BncLhfUCnxHH48IRKpLSUAyLY1P4j5jiC-GcimAkIK39jxv6WmJL4kOcVTDx6hh8EGAlSMlxhI-NCR0ftWQt1wdG4wEjiII8LdRBuduGNpMK31lH6g8gonHNxnmXB6U2VVQp4zJV51MnZz_AH8KamyY8QD0z3kXk9rSuPi1IY5B386xLEtaL51vJR_F7qv6Lvqi_NFkZLm4u8m5EJW4IpY6hdesShQw3jRmBxLmCRctiK85Fjl9VZLRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چنتا دختر با کیسه زباله خودشونو شبیه لاکپشت های نینجا میکنن میرن تو خیابون...
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71280" target="_blank">📅 16:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=gfhTvD2rPr-Z3tujBGtDnhiKCV17Rg7LsHRfLr5p9W3Ssth9vGFJUeSsAOekxUQdrAifzCcBuX9tr6nfj_3MkCbrnK8K65orqt7hBE4cZp28Q7hykTHQOP_-oSHgX-pksh3AV-E6iUXBXvxcp6-hlyFdVzULG8pXz0qN_ue3L5YRrVK7EfDWer1Y4TYut90FR2iti5VCMCVwrfw6BJ8kRO520hh1W2roUC5w1-MCaZcP3eZ7pMYBy4pgqqPzAXwW4ij5LCfK4Qca4iXHT9_IGwBiiZLhw3uNzFgEFr8Fv7lWByQ7N1ovbf_KC-RRpmr4T3aix9HpGvObwUwqOIYQ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=gfhTvD2rPr-Z3tujBGtDnhiKCV17Rg7LsHRfLr5p9W3Ssth9vGFJUeSsAOekxUQdrAifzCcBuX9tr6nfj_3MkCbrnK8K65orqt7hBE4cZp28Q7hykTHQOP_-oSHgX-pksh3AV-E6iUXBXvxcp6-hlyFdVzULG8pXz0qN_ue3L5YRrVK7EfDWer1Y4TYut90FR2iti5VCMCVwrfw6BJ8kRO520hh1W2roUC5w1-MCaZcP3eZ7pMYBy4pgqqPzAXwW4ij5LCfK4Qca4iXHT9_IGwBiiZLhw3uNzFgEFr8Fv7lWByQ7N1ovbf_KC-RRpmr4T3aix9HpGvObwUwqOIYQ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
آتش‌سوزی در تاسیسات آرامکو عربستان سعودی در پی حملات حوثی های یمن
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71279" target="_blank">📅 15:30 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
