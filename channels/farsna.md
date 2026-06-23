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
<img src="https://cdn4.telesco.pe/file/PHTd81e0rJiS0rXjwkceDNqMOFRh0KxCOibq-MqnJoFX-brIVRgCYyqXhn8Libw4eWjvUyqsmoYV3O2GYZEseY7zxTJmf9voCtFPSKkJ3u1HJBkLGViPY4Lxgzd6520_7wjOB_dA12rW05s63cmjUM73YuE8bxgZZPdm-AFkGKpoGazUDU3XFvvZkK--H7g7A8-z6I83kNG7CmVoIF4U-wmtulQ_kbZhrE0xHJfTECf5KRu41OfZBNQqKr8TBE6HnHUkmLheEi_QodHGETRuhhsU6MxiOAjfIejsPjWimtLPvIN0vdcWYD_p7gow-F_6I_PZUI9rIg2eUBNWUWqj8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 22:53:04</div>
<hr>

<div class="tg-post" id="msg-444358">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هک بانک‌ها در روزهای آرام، کابوسِ محقق‌نشدۀ جنگ
🔹
اختلالات گسترده در سامانه‌های چند بانک بزرگ کشور طی روزهای اخیر، نه تنها روند خدمات‌رسانی به مشتریان را با چالش جدی مواجه کرد، بلکه به دلیل وابستگی سامانه سوخت به برخی از این بانک‌ها، موجی از شلوغی را در پمپ‌بنزین‌ها نیز رقم زد.
🔹
این حمله سایبری که از سوی کارشناسان تأیید شده، این پرسش را دوباره زنده کرده که اگر چنین رویدادی در دوران جنگ تحمیلی رخ می‌داد، چه پیامدهایی برای کشوری که بخش قابل‌توجهی از مردم آن در شهرستان‌ها و دور از خانه‌های خود به سر می‌بردند، به همراه داشت؟
🔹
بی‌گمان فشار روانی و اختلال در دسترسی به خدمات بانکی و کارتی، مصیبت‌های جنگ را چند برابر می‌کرد.
🔹
براساس اسناد و گزارش‌های منتشرشده در خبرگزاری فارس، در آن مقطع حساس، مسئولان وقت با اتخاذ تدبیری هوشمندانه، دسترسی به اینترنت بین‌الملل را قطع کردند. هدف اصلی این اقدام، بستن یکی از مهم‌ترین گذرگاه‌های حملات سایبری و خرابکارانه دشمن بود تا خدمات حیاتی و زیرساختی کشور، از جمله نظام بانکی و سوخت‌رسانی، با اختلال مواجه نشود.
🔹
در آن روزها، شماری از رسانه‌ها و فعالان فضای مجازی، این تصمیم را به بهانه‌ی جلوگیری از اطلاع‌رسانی، رد کردند و آن را فاقد توجیه فنی دانستند. اما اکنون و با تکرار الگوی مشابهی از حمله سایبری، واقعیت آن تدبیر دفاعی بیش از پیش عیان شده است.
🔸
با این حال، تأکید بر این اقدام به معنای نادیده گرفتن ضرورت تقویت زیرساخت‌های دفاعی نیست. کارشناسان بارها هشدار داده‌اند که باید توان سایبری کشور به سطحی ارتقا یابد که در شرایط بحرانی، نیازی به محدودسازی شبکه نباشد. اما در شرایط جنگیِ تمام‌عیار، هر اقدامی که از فلج‌شدن خدمات عمومی و سوءاستفاده‌ی دشمن از خلأهای امنیتی جلوگیری کند، یک ضرورت غیرقابل‌انکار است.
🔹
اکنون و با فاصله گرفتن از آن روزها، می‌توان قضاوت دقیق‌تری داشت. تصمیم قطع اینترنت در جنگ، نه یک اقدام سیاسی که یک راهبرد دفاعی برای حفظ معیشت و امنیت مردم بود. درس امروز هک بانک‌ها، راستی‌آزمایی همان تدبیر دیروز است؛ تدبیری که اگر اجرا نشده بود، آن روز در اوج یک جنگ فراگیر، شاهد فروپاشی خدمات ضروری کشور بودیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/444358" target="_blank">📅 22:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444357">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7becbf5b47.mp4?token=VYowFw1YmidXlJ3rWLeA3inEYbiK5s5HK1qozoMMS6yLjebp3IWTQGJJI_JriYJLKmLzNqBTppgWPKjB6OJ6gWNXogarqhwYLPqjneBtOYDBW0Qu1RG_5XdsAB0DmKPHmsekZmaQqnVtlBEl04LhjrGAqTP9u7KiiOGCqL2vMl2MPqY8mlAKU6nRauL8Rrr6VGtMWMaXnchqrltRxy7-Fcsh034bpwUHEvpfTZLPQuS9mxT9hoJZHCwydebDR-k_VYJFbZtAJt7Zzv1foilsT1n8FDe4H-LKSHBtqb_c0agreY6WG2ns21k4prjYo4Nf26nm8SYM1eFMUa5MIh5ENA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7becbf5b47.mp4?token=VYowFw1YmidXlJ3rWLeA3inEYbiK5s5HK1qozoMMS6yLjebp3IWTQGJJI_JriYJLKmLzNqBTppgWPKjB6OJ6gWNXogarqhwYLPqjneBtOYDBW0Qu1RG_5XdsAB0DmKPHmsekZmaQqnVtlBEl04LhjrGAqTP9u7KiiOGCqL2vMl2MPqY8mlAKU6nRauL8Rrr6VGtMWMaXnchqrltRxy7-Fcsh034bpwUHEvpfTZLPQuS9mxT9hoJZHCwydebDR-k_VYJFbZtAJt7Zzv1foilsT1n8FDe4H-LKSHBtqb_c0agreY6WG2ns21k4prjYo4Nf26nm8SYM1eFMUa5MIh5ENA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما خودمان را بدهکار مردم ایران می‌بینیم!
🔹
صحبت‌های یک جانباز در حسینیه معلی شبکه سه.
@Farsna</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/444357" target="_blank">📅 22:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444356">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b7f3a95d.mp4?token=Zd6v5JEgunsjEA51JA-d3eQ96ZXjqQMQTeMpoBcXGk1lazbXMKl8pHyHARRDWdhXWbnqUkyW4VPMjwjQxpCLO2nyQY53Vm6dVBwEKePu_vH1M8I94sb8CpEocYdfIDMHoQmPZJNU0voD7zaIFvH1K5LojRhcGIToF0nZas1uB97U21Ilr5Y1T0Q7999Th-wVjQMJh-P3K_Blfhn3OFXTBJRyn-b32auLav3OuOpEWEDsRBBO1Pit8SsF3fO3fe5h5EzvyyenFmhu4ioedpkm6d3DEPrWBJRmwSpH81KvZnNBV4074uI7qKAeIVKazEZF2O-zqqEgq345NkWgO6pY-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b7f3a95d.mp4?token=Zd6v5JEgunsjEA51JA-d3eQ96ZXjqQMQTeMpoBcXGk1lazbXMKl8pHyHARRDWdhXWbnqUkyW4VPMjwjQxpCLO2nyQY53Vm6dVBwEKePu_vH1M8I94sb8CpEocYdfIDMHoQmPZJNU0voD7zaIFvH1K5LojRhcGIToF0nZas1uB97U21Ilr5Y1T0Q7999Th-wVjQMJh-P3K_Blfhn3OFXTBJRyn-b32auLav3OuOpEWEDsRBBO1Pit8SsF3fO3fe5h5EzvyyenFmhu4ioedpkm6d3DEPrWBJRmwSpH81KvZnNBV4074uI7qKAeIVKazEZF2O-zqqEgq345NkWgO6pY-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری جوانان دزفولی در سوگ اباعبدالله(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/444356" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444355">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mepnykBtGINTT91__xlXV-eV78rcqfOWYvbfPdLfLrJ7PghWMEo-iDER1C2jqKojJXoXfOWBWkT8ncEZNYn70QpxkRjKfJJaWwlgPxsjetV-bLu_PDqDx9aay6WZhNp86E_K2_ibCAtYH8PYKDNEp30FJNxsXKx2h6Z8oieTQxo_SNYehuEPebLPncdgd8efFClMpO9bMnNqOA4mlTtcMQMLBiX6GypWxqI0xnS2OnJVn_nc_nFCPHFCFGSJUkHXsO1y_hw6QBGCJRywYFpKfjin4IWfpjz7ITTbVD0LdHHeTQ2lgmkb5lw2Mx-ohA4X2bYdfigl0cPeGEv1ufFJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل زد و رکوردشکنی کرد
📊
🔥
کریستیانو رونالدو با گلزنی مقابل ازبکستان به اولین بازیکن تاریخ فوتبال تبدیل شد که در شش دوره مختلف جام‌جهانی گلزنی کرده است.  @Sportfars</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/farsna/444355" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444354">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
آقا! تو اما نبودی...  لحظاتی از دومین شب مراسم عزاداری حضرت اباعبدالله الحسین(ع) در جوار محل عروج ملکوتی قائد شهید @Farsna</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/farsna/444354" target="_blank">📅 22:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444353">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c94f64cb48.mp4?token=XZao0AaWmid2b7j3N3FaxZTXygauhrLzHwylV13B6fNBedF7x28KJUGgo9DOTAVQ96KTBFg72iSf0lmeFT62ESKgbIg_GmXaGcpG2xW3Fxc9CxRb_ovvm7z9g9HoAN8dZwBTrgKfZ8toZOVRp4ObwhJMUUyIVrtr-4EyPoAjUA9kZh2at_wRPxdMRI9GZhTDJs0V0U6Z1hZsiKfOOlW77S3YIVlNyfmst9a-8LOtY9NbNuk2mNbVGal4nnoYEwrTTcuiuUHIltKL6Q9b8kGReNyRq1BDEO7onPpm33lsK4SnEIqjlkH9L-io_wABjRwd8t3XfA76r_yAtu01jdvxgCXUA0LPjwL7nsLlK-D2qDv-DyVQSYBPrxOsPwYvW6FZzxDI_3iuNkfZUWTU_lUPED4iCjPODxpj59-GVvolCT5tmfJXBc_bJzUgdIkv09tgaFl4-pmWVlq1TxBMZTQD-fpWZ7Mu-t2yaC4eyHXZPfyWzRdkZXJ9KcPoxM5YLdM0KY0NhO73TspGN0z2Jdhtr4qwaIwdYlK_kklutTzfZ47YbtVN0S0kjsKYGcHNb5CeGalSJw9u4GhFZFpon3dsFYPI-Q6Ylrpg95xoP5EKnu3ElBbzceCJk5zdczNN9naeW-GqNHrmgXF__1Usy_x59oVCZh-2_WIir1gfRrf49Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c94f64cb48.mp4?token=XZao0AaWmid2b7j3N3FaxZTXygauhrLzHwylV13B6fNBedF7x28KJUGgo9DOTAVQ96KTBFg72iSf0lmeFT62ESKgbIg_GmXaGcpG2xW3Fxc9CxRb_ovvm7z9g9HoAN8dZwBTrgKfZ8toZOVRp4ObwhJMUUyIVrtr-4EyPoAjUA9kZh2at_wRPxdMRI9GZhTDJs0V0U6Z1hZsiKfOOlW77S3YIVlNyfmst9a-8LOtY9NbNuk2mNbVGal4nnoYEwrTTcuiuUHIltKL6Q9b8kGReNyRq1BDEO7onPpm33lsK4SnEIqjlkH9L-io_wABjRwd8t3XfA76r_yAtu01jdvxgCXUA0LPjwL7nsLlK-D2qDv-DyVQSYBPrxOsPwYvW6FZzxDI_3iuNkfZUWTU_lUPED4iCjPODxpj59-GVvolCT5tmfJXBc_bJzUgdIkv09tgaFl4-pmWVlq1TxBMZTQD-fpWZ7Mu-t2yaC4eyHXZPfyWzRdkZXJ9KcPoxM5YLdM0KY0NhO73TspGN0z2Jdhtr4qwaIwdYlK_kklutTzfZ47YbtVN0S0kjsKYGcHNb5CeGalSJw9u4GhFZFpon3dsFYPI-Q6Ylrpg95xoP5EKnu3ElBbzceCJk5zdczNN9naeW-GqNHrmgXF__1Usy_x59oVCZh-2_WIir1gfRrf49Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علم عباس(ع) بر دوش مردم سرخس؛ ۱۱۵ شب همراهی با انقلاب
@Fatsna
-
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/444353" target="_blank">📅 22:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444352">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVG_Orf3XV3hi0vA4cdGUsN3FwP-nra0638RK2Jg93QKeOiBy8gjg4Qzi9wOEcp5rp8SnCzDIdLPBY_PPHseHSpKLpWhoBJaUPHeQQRg2TznnpqCRARuLqC4N-dzJ5OCG8X9bS7cDe0gtGAtd1V-uc_c5dFUgGVuu9lcRThvcvqZ148jVyIiuHwEQesMA5S5vC4jXMtECVg3oObiLJMgsy4O0zlSleZcxB20242zroa8jjIzD9MYSM_gMEORIadnHoSxwB3KyFlT3IH5GJ3O7M3JzLJb3GmVWex_JUjrYDF__6qaEPnz19H0uH99NBO-5TfKL6xmv75zX7Tk--S4bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پربیننده‌ترین برنامه‌های تلویزیون بعد از آتش‌بس
🔹
طبق نتایج نظرسنجی مرکز تحلیل اجتماعی متا، ۴۵.۴٪ از مخاطبین وفادار تلویزیون در روزهای پس‌از آتش‌بس، برنامه‌ «من ایرانم» را تماشا کرده‌اند و ۴۵.۲٪ مخاطب برنامه «به وقت ایران» بوده‌اند.
🔹
همچنین طبق این نظرسنجی، برنامه «گزارش ورزشی» با ۱۱.۸٪ مخاطب، پربیننده‌ترین برنامه تلویزیونی در میان افرادی که مخاطب همیشگی تلویزیون نیستند، اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/444352" target="_blank">📅 22:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444346">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsrxH0ONkvBn0ZXCrVErKoN6EwTPsKFmPonN_Ww33-DwC1Mrm2smtDr_bL8XGwt96C-gQrFukUurszI3d6oWDuYfqIXd2pwwW2CjuSE0XmuK4AdUzm9bgzqqL-7H1tWaZc-MWNSF2nE9-YbPM7d5cbIAzk2ChfcymfaTnR-RrT9N3_tdxB4ADkKwY4SAqW8KnIbuSz1CR6iy2rLQJkY7Y--4MGHesII8g0aXxh7yztwsVH_DNVSIPgDC_ESl8ESBzzOT3tKngfxOBnk0eiNjrQnI5JbTM40VoZdaBh59BoZitOkqIrB6xpwDzhifdgGfG0xYSox11rb69RegBYSVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXtwwic8ZBWD-Qw8RXJ-hV_E9bdhg_xPRwMPnA9M1sB9xI59ack_GyBZji_fMgWKfijJu0RTrLO4Hr6cWkA6j-YAM9VYIqbVBRUKoYWL3UqBygzzwhLw0YP4uOerjrmERg88jtuM7c1maofzIhSSILv3qyCpHyqT2lkUlhx0R-FSfN_D9HYuC2XWYVAArH1c8vpjMo9wnAvSEKCIKcN8ceOyT5uJN60diWdK-7N9oeHho7nIqoxHe9ym4SiBaQbQCu28HX_Bg8_WgbXLm6c__8XkYz9dypdlhKl4Fw-gvS4G06eX7serWCQDSOxThPsNzcTeWhJmhd1NrraYDfMF8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKyTuaLpo6cnftSU3IIuZXAvqXxO9mD-eE9w23iw1OUhrW9uyGHYGqby6HVnLQndeToS0h2NxFc0ARniy2296rEprHR0-K9vlpx4p4GNKfD8zg5L7pPjzBcfGLXTeAfMOANMWHcfdwnKtMbcfCgHLtLl4WoCoJdXQxdBWEMxM-wMd29X-0H3eWtxjdwHbj5Xtt6N0ctD0-NnAbAnU3B0IGrUZRihNfBaJNQppaQQ5nT1Zl6A_rtxqAJh4ssXlUv3LXYsYX71-_Iluof6mtdT1S_MeS2s9Swmlw6x4dpZ89n-c52Bhlw6m89NdGNPcNHeV42AfAVNRCzS9VDArZubdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVLFEVGKTpnlKZtNguMl7MIIlOFu23x0CytyIspSAbJXFE1Tyt4LlLceUvKEPPalONfCQpHEclwUL_a6Dg6SWeBGhXgR0HKYpRtziNFl11NupjTbXAVCb4WFYcOZCDPk3cCDB7oLgAT2On1bh5H-Ir26nrVIoNgRP5dWByHihK-07Shz6S-wx0xsfpAaZRbg22SSDKaLQh_uFaHxNvGV-ifQXUNMUrGDBS9JClshpVudEk3pFGIPR0i2qEyo7CHATPpJmETCQtOQdDyAH3KgHrgHsmFssM3HkCb7XUBlBFmOpUv5ZP4txK68WT_QwXKyqqQJ3grE0zLJac6xpPFwDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bpVjNAZXJX6OWvzB-19BYSnJw7fT7KJt3vXTX3MQG0TpOs-Nes24N3K4hQv47auz2fSNH7WaSXFQ90zSRjy7I2mkQzrduJ1Qw5idKQ5aTggyCTDJjV60S0iRCZ-k6HSgwXeIX6KkLWYcj0H8kCygN73z0TeudvvlcP5yt2ewHwvzkFyWfTTIZKFJRHG1z6EmlVx4qm77UmlPwAwzDocnILgJ-LM9Dq2nrbaL9GC-VQlPFjxCjlGjOgCrEceT9ejd3xSQHqNpwjlUUKKmmoSABqLmsw5J1OK_Fknfx_Rmdud9wXnmHEsqXR0S03iiZ5sxnkAExov_gfdeK9UwkitBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePyI2iV5gFB7_84VM3n8vN0I27Qx_1CAkWgL0thHd2LlLg5Pl8YJxu0T0qVFPx43L_4YPxDu4lYciTHPdNA_CMdg_VMrQZtuML9wMkMjBn0TJfCkEjj96jqLD4SgzTiq6MMSrSZRfWUqt_60iAW4PWX71ZtOMWkH5E6LUSEuQILq8wYWit4NlUXvX1soy7FsuLou-oEq50clyRmLIZOIuC2dq5xSeoKX1BZh1IdYtaP1eA9bMbghqnzfmGcQhu-H6RJKMHSlg-dhTR2bhl0z_RloeElGZnleTDHw0nH-dRkgN8X4yl7bXgfpwbj53LtvfloTJsdRyi3AHfTmHTdgaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خانه‌هایی که پرچم‌دار عزا شدند
عکس:
عاطفه گنجی
@Farsna</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/farsna/444346" target="_blank">📅 22:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Zakhmie Aftab</div>
  <div class="tg-doc-extra">Mohsen Chavoshi</div>
</div>
<a href="https://t.me/farsna/444345" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
شده آسمون غرق خونت حسین!
🔹
قطعه جدید «محسن چاوشی» به مناسبت ایام عزای سیدالشهدا(ع).
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/444345" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444344">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wnc91gyVilErG1Gl79VdkU1RyDp6A4Zea-eenZT0V5fAMpmnrysmQ9fn6RQym7n96k83lffyvI7DkK2qsZfCvqvctbizR-d5XhjnsNBkbVOS-5SpOsqQ9H2AmVvDWzi_B8BtR4cXk8inip-mR6HoNXHbP4b77IHKXt8sLmoiV5NGPgfEUibqK8iNCTU-eKdmczDe3Zz2FAHv3qUvTpIz9zRq3SnYvp_bfkiNrBq74Ezol120hi2HyRj2u78IkrPcWwAsaZGHOlCtyAXXaSM8eIGjOPZkfzTC9HtYGkNM44pg1qhiEpAjt-5CncSkTjmnoavaUp0KcyMMKfJkgJBEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو رسانه‌ای تیم مذاکره‌کننده: هیچ بازرسی از تاسیسات هسته‌ای آسیب‌دیده انجام نمی‌شود
🔹
آجرلو:  هیچ‌گونه بازرسی از تأسیسات آسیب‌دیده در جنگ نداریم؛ اگر ماده ۱۳ یادداشت تفاهم اجرا شود، درباره تحریم‌ها و موضوع هسته‌ای تصمیم‌گیری خواهیم کرد.
🔹
دربارۀ تنگه هرمز، طرف عمانی دیدگاه مثبتی ابراز کرده اما این دیدگاه باید به یک پیش‌نویس مکتوب تبدیل شود تا درباره مدیریت تنگه هرمز بر سر آن توافق شود.
🔸
ترامپ در ادامه ادعاهای تکراری خود امروز باز هم گفته بود که ایران با بالاترین سطح بازرسی از تاسیسات هسته‌ای خود موافقت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/444344" target="_blank">📅 21:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444337">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJPt_cflJnYiB56o2Q4p1HhLK0hytvZHIOHZ4VoiAvZmidl4Fwk5xToTLhN4EMA-VYgbAN2-z5LSIvWPswXPBHgHkG3KyTnxM9ozWtgDaFesXlMs9fiKNUUiDN0J__4P3_WuDVZ4ioa_CH_oRz6qMJtSiI2sY3bo6uRYKmuZdtDt3dW5fkeTGJ44sL-Tem9GDqgPbd2_tM0nZO1kFZ2eQ8iDPQrmMsczQqlDaNSl_hcFFEx-VdJoQV5SsfCzfiARaV_ypafj-Ocx9ri6dyC1bA-q6CjC4S3sQ2RPv4wSZji_8aVQT-uP9mqlHqQFUaXXwRRBS46MRPM1ISQqEmIZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9RttxsjZJRjTiukx8SggRpkkcfdnizNB50yTJ2RkQ5wfy1gP6H4aJ9Dg1coCxW6G6Oan2tuCvSf0L5YojVjTS8Ld1-sseFbNO4GF8rgvER5JCQIWcynT9vLZFhjCMPYcS07B6LoVENOMyHyB3nLTi6gKRDPSUvuwsGXjkuF1-tK9eq2u4P7EFchYdZDmgiVE7W16cWZdBVMFPAzbS6kHML47v8oV7szgex__JsM37Ktey2wWMt7fW1VLoDfbYcIArzffDiDE39oOL0bY1Jq0zw-xG-aTFd98W3Wa6R0FKZvMWutCirnNHsZ41G1kqBYhrLSPQXQmhL6YMRBSMm9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6lwH7NMDThErDCFGN2QyBoJ2AH1Lk9V5VIH6zoj8GCrH445gUmQUzNBNiTv6f9011bcSrlv88gCHI-SkEJEMNUZL_JAWnUmejkt5ADkdAnezwe01_rr5rPD4v1XbH6uem425cDS1TYsvsfzqzt-7PVYYfQdxjDXaL78N1hiHRTY4a3OhCUlhLEqglWQ1Uo3VxyE08acstXc6g6uURR2-mAIeemLvNneICDLIrBQ7oQZIzT3e8FjYfeCBZN4vN61yMLU6os1SefczQ0tSVIVAPP7OzbDNgbZxKKJJmOIejnVz4hR1achyksaEBxk7Vf9CHrmFIXCVM6FW6aX-3kH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqrECK_5sa41t6tlKvrlYnHVK_PIMXlQpoBaIfVNEf4OEn5C3z3O4mEiCNKRBS2eJRLDr5ddf6JiiTjUJsJvSU40ZS_j_z5qfCJzLUki6SUHTzoBK3chIa6PTYQFCsgtyAZtAhHlEDTcLS9VPY7oodEYunWbYGxTqWz-IWQb49pjFYDIxGZVozD0_mToN9pIYNHRJfhID1VuzpC1PW3e2U2fQP2hn1QZcAEEuVALr3J9uFcd8IR2OlEx2aaIF64fOJzNsap6c2_7nc4Po-l31OyAcztyn0W1jxugVg01JDAI67idCTv66RHUHBfTbQRAo8iUwiqJDfDFmUQGcebWXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LG_UtYCLgDrs0Sa7F3ASWS5m6wJ9rAeHPxUb5h3Zgxpg_fT0NyI_zh8HgA9J2oTRQuxtyVVtQwmAPoha0SOMtpgwhRvjt0v3N45nKKjuBzYU4jQW2qLDJAXbmlhOR38i1A0dXmHDofDTibOb5HzzUf40xc68BI2_JnjgQymdipqokV8Xzz3SsePt11slZrnOqlBjOe-OJwiyKMrD-m3X7t48QrYEKzM_cu-0iBh6cpDeN5CoRRDNIu739DEik7oCpKyk8jSd0zjzKlCrT8FftDbSPBgqXpiT2H2G-cXNj470qTSMSst65huQlLjLa8vK-7kPWXLrGXaLONNBJVGo9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3wgqQxs4uLW21XtjuWKqOZ1M4sm1Rny7B3xF6PtJQlEdrRGsa32zwWVD45N2q9-pWcSSZwdP-jEWAYpCSthxIvzubUwUyqUG82O8wWMSt6aRZggLy9WjmoNAGbhG1j8J8X9jQxBX8oF4PP9atreNXo8DIqiOKibCCqSD4TxW826wWU7pamelQbmylheDDiNh80C9Yu_PClQyxHq-vu4yTtTuVaiknVH82fDqEQvejzRVAkGR34QGHBIn-Kfh98q5DWRRlX4OXOpzGODzcaxPbFebRtHtBfO0dKW8dfIZvGQjuM0n7kx_EO4NUhlTNb1EizkS8N2J9RwUopoRMdpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SXRkLXsN6zSzumUbpNwsggaxzGA_sU5QzEzx6_AhaxtoWQZhOAIsMI4uZN_9HILQXh5riW6VvMpcvBIOwMsk8HP1TiULHw508yX5wmIlMq8yYFe28iyJdkb02RVJ-vm6yWya18SnJ082pxKUJraXJ2JvNMmPcxSVc8-gFSHVQ4lVjqfdxMUchhgxxVQ8hBCYoQ9z_TDDQbxidHCM9I7caxNxVqcP9HC8LOCTtMjEZeTQqx0MKeUS9CNX4oMe-w7VD-hFWoWpfSaGZdAbUN7JXX7P5hKOehHfzqMb1MVhIbInjwyMWI9FuuTY71Xl2QoReYixRwYw7L1sZNQ0vT3GUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مشهد الرضا در سوگ اباعبدالله
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/444337" target="_blank">📅 21:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444330">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IvSA88vUR-vF1o1SnkhR2dzFcZlA7LpiwXxrWmF1EbZpc05iW6gFt8VYChTi-hN0AR1FbaTV1LgQ9aaECZV03nUE6300St_-4FBDDekBhhQ2J4ScxY-RMOQjH42IJY6GsbG73pasEYNjAI0UBZzxjz0NmanLTjKkYZEF35PqYKhvUsp_-LZWbFhAd0ki9lMz4sXNKqrNrG9iO7t6LUubeyPGDkawnhSlhKl5XAQLD7dGCfnA8YvIHKmRnismb6SlRQPomPzFppzVPqdbT8f-EqpnX-mA9hGM9jqO_TLLpiMOw3cItfABoHdsJjDbHPMl5GVSOKeKPqyDFFQdLAVG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fbnaS8cA2MiFxg6I185dKm0f-zjtcTNJ663uqCkyFPvzefi3dAr7TesREqpcZ8soYaOQcTbevZyHU3OB8MbQffHW0rGe17VGsxUxNGhNa2ZSTvjqgzZnwez_hGYjhhD5Ca5dqie1wFHfg8SRwf3LywuIyV6mN2URBMMeCQdgS87j_9RyNRHY0HYiq8peXD5c7k8PhU8UhU3GlqFewT-9CO4y_1bBth2TkmOO12Aka0FYwjenluAgCtx_SlsmtqidPq38Y4FMhByfDce9VeeKgeNDNJbdEEPp9mIoDFWmfjWnGzG0cBUuRIvPgFg3poqYXXa4SOb4OWNYgPm70XnY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtB9jGAQDSDqGeKzeFYedeWBDoX4VOMylU4FKk0tA8tsDgGSEkBiSrAtjpMaOqC1pPjCHJN0gNSirqbmWyxW1Z65Ik4IJBIsfoUYo7gv4tDv9GvLlYoLTyQYFXAuX8n3GSMVGpRxjK0VLGOUEz3nNdSJGnepS964qZqoE-m8rn_VVequ2vem_lw4ZHKVpRvgpUxzFw7wRwh_QSXpDldz41In-ufoM6wxBUkiE8XMJwscUIRN-qBFaaDb1c94TFuDb9r6WoylV748Sl6nidboSnBU331Gj5xlHacMof7AK2td8k47Qo3u1-8OZOeRCjvFZrGtvwG5kC-9Ub92poQEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aokc3XFgul3LSJnqiCjMqTynsa869cZx5DRCqL5p829i432E_hN70kBDToFSoDyBJxhArMZ34DfFkkN-7ETUStT3MzTbahkUxaaJs-5u1NXXXjgcp93AdROEXlYaa3oP7zTcInlkNX1w6kqbMPUXdhuU2FnqaB7RhXW4rT_v_DgaS9b6uSWVXu4Si5zUt_L162AXeUIrkhPNj4eDYms9sp34sMs4hPENiWfK0wjv7959gaXKb-4EWeleCoMKx6ZpaM49v5Gm02VPXe-9zlPQOujSlOd16qAM7EEvg8a7dC5Z1DUS1O-z42gZzij8ouEJ7C0XbRMJRDL45WDyZXjVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I62l22SuBrDE9CBuqYNnj998pE6dGHbNLRLgU_ngyOLOQ-rCdyfFJGVEhEVCv5_Hk9ap39F-r0FeawrV7voF0FQgd4XWhKpgj_zqU1ruLHNsqlS3gkyrzRCc0NmYlkawq4lHNAvDdv1JpF5ZjzZllNHmHnA5QSbEKDL3wRjd-duT29ZiGK-Jk6PETRpy0JGnCX4EWuo2oOBg2o8XNY7YMeDqry-y04B8phdVB7jZtgoVUupoWnAe1FppoCrK3luKCUgaM3YLR2udth3n2WCZf66WaWYvggT4o0eR0H8_QWYngW6ng-_tvZKH2egIu-ggrwXiZJwhAHhJrWnRuPio0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGQ96gjrdOS5DfyuLjQE7mVPIFvpiFzj0Lvdkx56qUXuglAt_skfsKhzxnfdEtcdeAQ_314P7c0Whco5MMp7XUeVh5GKY6BqM2wTEIksMXLLbKmsr3kLw2lzaR10qmP93q6MsXinwlP9yVJPXX0XmAApZ5jb6V55R4sE-2NGsaN0Zf7bCAXTTjcwiYgpCFExmT2nQsMZvAvL_bdepUMPcnQjwBXi7zNAEYh5UdGn3uwVVEXblsfDl8xclLf4JwMyml1bSkzUf8JtAvdvaSL7xkotoNIbDpUNtpzAHhMwiX3Y4RT4E76CHWsyV5PgUhaw-vj6ukFiQa0yPYSEWYT6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2R2McYiMXYhEzGBl7fw8yIvglgwTOBnbg5_CTg5uP6DDh-wgGzIQgWuSRhsFtullrxzo-sj8twaLb3IyicA3Z6kpx9NRIENEEhN1A_YMWBsqKYKoczaenSGwywP7urd17zn_GeC6yMk8fJBsOy2AN7XdADIP-PXLRobYdEVEzWdpfIeuS9YrPBOLjEZjsvCjdnm0LFR1cakx014LXW6FXEjg3asaka-KyGvf3mGEZn5mn9b0I8ZMVieY3Z1hKanEjtBR4awIq8Loi43IaS2lBIUV4X6uZOo_55k3t1VF4CimO2RHzQsBhivaW_SDgl6gv6oQZ0SXMcc0kV_CNneKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم عزاداری شب تاسوعا در جوار محل شهادت رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/444330" target="_blank">📅 21:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444329">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbMdbaz-OGgWhWFaBYA-6ZxAZVniMYhhrt8ZqwVGs02VMlfZ-Ur3e3HmaQBiklATPdXjRX4h4q62Hqha9EmEdbGO1QIPTIvT1EVVe_ht57lIZuUqYTq8wb2as4BQaZcG6qwdbuAvTUus9KuDCdTzeBQwT36yFxn-lkhgzMr3tUddbsDZW2q_FQBPj9ZCheb1H3FEQG_pbzIU2WyA12eShI7M6mPYXTYRWP92pjt8wgxk3JzGJ9TuLz9ChqAFaYMyMXVb7oq3FQV_AjWZn1Wx2wjV48H8Un-YbkO-t_PWhJx4_ouT8nzuERUpoTtlYPO5L0pgzKVM8GfUqfVtIdpE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار پهپادها در آسمان جام جهانی
🔹
سازمان‌های امنیتی آمریکا از آغاز جام جهانی ۲۰۲۶ تاکنون بیش از ۳۰۰ پهپاد را در نزدیکی ورزشگاه‌ها و محل‌های برگزاری مسابقات توقیف کرده‌اند.
🔹
دفتر اف‌بی‌آی در میامی نیز اعلام کرد که برای ۴۹ اپراتور پهپاد به دلیل پرواز غیرمجاز جریمه صادر شده و ۵۴ پهپاد در ایالت فلوریدا ضبط شده‌اند.
🔹
مقام‌های آمریکایی هشدار داده‌اند که متخلفان ممکن است با جریمه‌ای تا سقف ۱۰۰ هزار دلار، ضبط پهپاد و حتی پیگرد کیفری روبه‌رو شوند.
🔹
این اقدامات در حالی انجام می‌شود که آمریکا در سال‌های اخیر با نگرانی‌های امنیتی فزاینده دربارهٔ تهدید پهپادها روبه‌رو بوده و سامانه‌های جدید مقابله با پهپاد را در نقاط حساس از جمله مرز آمریکا و مکزیک مستقر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/444329" target="_blank">📅 21:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444328">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24559c1356.mp4?token=OLftS1lMe4o4QhkOlvXcSgRs-soDSFVBYmo7WXyP8nV1NpLCPtW3rSsKP8O6gXJhVWct8lvvEFHmL_yITkFLvfFebeXaozaBKjiemMBQE47B-IihYOG--pv_585GQior7lajLTZDEqY-r2jcrr4f68y-wmbyG-ZM23tMc1wTJcBt9ZHRL-_5iaJtMi6FDFjFOjzDJCcce7z0u7v6d2N5NtcYK0Qas980P0vLrYCJlcudOVgKb4WqtQHlWDDXNRRe3m8mNJylmlY1supmA9rUOMpLJYgvCq9HYwxiBlOegaUP11dJ4zmWuvHCGaOIgR5FSACNnh3pbrhDt-aCtzFEmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24559c1356.mp4?token=OLftS1lMe4o4QhkOlvXcSgRs-soDSFVBYmo7WXyP8nV1NpLCPtW3rSsKP8O6gXJhVWct8lvvEFHmL_yITkFLvfFebeXaozaBKjiemMBQE47B-IihYOG--pv_585GQior7lajLTZDEqY-r2jcrr4f68y-wmbyG-ZM23tMc1wTJcBt9ZHRL-_5iaJtMi6FDFjFOjzDJCcce7z0u7v6d2N5NtcYK0Qas980P0vLrYCJlcudOVgKb4WqtQHlWDDXNRRe3m8mNJylmlY1supmA9rUOMpLJYgvCq9HYwxiBlOegaUP11dJ4zmWuvHCGaOIgR5FSACNnh3pbrhDt-aCtzFEmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژاپنی‌ها با فرهنگ‌اند یا نژادپرست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/444328" target="_blank">📅 21:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444327">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e447e3e393.mp4?token=cr3IkVHl0UPuDFsuZnJSzAwubXNtBM8I6ImiHPaJIipyIiBU6RnyFmxh4gDcqDL5Y9jdUGyRVshUpOY6DqPRphwKwDklB0Pk2OKunWTIuRQrb7nt8HMXzmNK29fmNK7nObdJN8hoUYP63lvRStnnZ6yla7f8cQgpzQsBQZtkag5i64WAuNHXD_RxmtoRmVQlXf8hYNdUcYmgc3QMakQ7FzmQ78vC1TVtPhC9-UYOzbU8oSkNT3pnlDVW-9OFJTmWdGvEsLxu7iO8YV4a6dAF1LAp92xFUchGKfCrcYD7Q1xkGdXgk7ULz3x5KDTXSheX_pIRlzCU3rTmIfrCWNbT7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e447e3e393.mp4?token=cr3IkVHl0UPuDFsuZnJSzAwubXNtBM8I6ImiHPaJIipyIiBU6RnyFmxh4gDcqDL5Y9jdUGyRVshUpOY6DqPRphwKwDklB0Pk2OKunWTIuRQrb7nt8HMXzmNK29fmNK7nObdJN8hoUYP63lvRStnnZ6yla7f8cQgpzQsBQZtkag5i64WAuNHXD_RxmtoRmVQlXf8hYNdUcYmgc3QMakQ7FzmQ78vC1TVtPhC9-UYOzbU8oSkNT3pnlDVW-9OFJTmWdGvEsLxu7iO8YV4a6dAF1LAp92xFUchGKfCrcYD7Q1xkGdXgk7ULz3x5KDTXSheX_pIRlzCU3rTmIfrCWNbT7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا باید کولر را روی ۲۵ درجه تنظیم کنیم؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/444327" target="_blank">📅 21:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eca1f9f76.mp4?token=GUyaC4iFmaDSVA3QnV1v2qHyU9nYbQVcnwjE7e7BCFAmZg0Vl6Ch1SF8KqG9_oNgLcZl_ZilygYB8aq4AF2iMLXJDI676fJ5tTFbGJfnG66bVsXrDvjAnUZ9mvjFCegoSKUI0nh_BumQzgij22PjV7LH3pOvVtVPrIJAs6nxXZVMKqDlq0YsvO07zD5xJ9DqIHfpVHUmyvYNZtelsUDHVyfPTGP9AFU0QktYg-xoMpGaEm5v8as01b9v4FQwTeIomt3fb3u1wJbGK_BG6ZWHzcbhoS6wVR8ClsoPlb6Rna2yEdt34g4SCFdeI0fX-86Zbm5hjUtlaJsQiZp2yJMhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eca1f9f76.mp4?token=GUyaC4iFmaDSVA3QnV1v2qHyU9nYbQVcnwjE7e7BCFAmZg0Vl6Ch1SF8KqG9_oNgLcZl_ZilygYB8aq4AF2iMLXJDI676fJ5tTFbGJfnG66bVsXrDvjAnUZ9mvjFCegoSKUI0nh_BumQzgij22PjV7LH3pOvVtVPrIJAs6nxXZVMKqDlq0YsvO07zD5xJ9DqIHfpVHUmyvYNZtelsUDHVyfPTGP9AFU0QktYg-xoMpGaEm5v8as01b9v4FQwTeIomt3fb3u1wJbGK_BG6ZWHzcbhoS6wVR8ClsoPlb6Rna2yEdt34g4SCFdeI0fX-86Zbm5hjUtlaJsQiZp2yJMhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: نیروهای اسرائیلی امروز در جنوب لبنان آتش گشودند و ۲ نفر را کشتند. آیا اطمینان دارید که آتش‌بس همچنان برقرار است؟
🔹
ترامپ: خُب ببینید، آن‌ها سال‌های سال، یعنی چندین دهه است که با یکدیگر می‌جنگند باید ببینیم چه می‌شود اما درست خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/444326" target="_blank">📅 21:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b67f614c0.mp4?token=RjshU6cPYleNS57rAE9GEOwgDSJX5tUF4hT4KzSu6eoRwNuH5_uqYZ5AgxOvkE07lwQLoD2pNSTtuGsLXwvWEzaKGFiqqI3L1DohsSRhaBZKScVmVTnxOCakhKBZJcvp9Egv6wYbQp1LxLJkhfYlhOcVD7_xLpZk0z_xwjQEm1O4eqWiVfJyZXhBQh-VZQq5yv0LSG6YcXkBA2PygLA5g64n9CsZXCRB_qYN9yXI4iyzYEBEvnhVyzSdKjgCx6zWB4tjd7PvHUISfZLVXcl9aN3ilYN_zxRGyHpyMKzHaBo8HXFYLdHrhUdV7YHyG2_TEEq86yfTOq35KuUoOZY37A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b67f614c0.mp4?token=RjshU6cPYleNS57rAE9GEOwgDSJX5tUF4hT4KzSu6eoRwNuH5_uqYZ5AgxOvkE07lwQLoD2pNSTtuGsLXwvWEzaKGFiqqI3L1DohsSRhaBZKScVmVTnxOCakhKBZJcvp9Egv6wYbQp1LxLJkhfYlhOcVD7_xLpZk0z_xwjQEm1O4eqWiVfJyZXhBQh-VZQq5yv0LSG6YcXkBA2PygLA5g64n9CsZXCRB_qYN9yXI4iyzYEBEvnhVyzSdKjgCx6zWB4tjd7PvHUISfZLVXcl9aN3ilYN_zxRGyHpyMKzHaBo8HXFYLdHrhUdV7YHyG2_TEEq86yfTOq35KuUoOZY37A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: هرکس که از توافق با ایران انتقاد کرده، باید آگاه و توجیه شود، حتی اگر از دوستان من باشد.  @Farsna</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/444325" target="_blank">📅 21:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM8MIoq5h1Lznn6Sh6KS3P0FC2kNE-IOc8QuF8ZWPed3_cRObFsZekTyQnVDZieRrmmIdeBDR8EWw1Cz07-KDveuqH5Xyu1MVsU5QmyDNnMg17QlHgS3yyXuh812-0bWO2_mL5-6e54fJ6eZukr1vf_ixhRnVTAte5gWyNN_jhPDexZOF4AukylOBYm_qsrSmoJXqgGNdxNeLXrkiPZvz2elacNmP34oWgr3guM47KLuN9yJKvFkWNxHg3vnC5YmU3XcDNj51WMFw1EBVCUYchoPCBqK8NETaRqNyTnDMVTeVdbpqKCQMRrM-iDLo2LX9SiXiJugfzxpc7eHfr-4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پرداخت حدود 11,000 میلیارد ریال تسهیلات ازدواج در خرداد ماه سال جاری توسط بانک رفاه کارگران
🔹️
باهدف تحکیم بنیان خانواده و کمک به تشکیل آن و در راستای ایفای نقش مؤثر در حوزه مسئولیت اجتماعی، بانک رفاه کارگران در خرداد ماه 3.236 فقره تسهیلات ازدواج و تهیه جهیزیه به مبلغ حدود 11,000 میلیارد ریال پرداخت کرده است.
🔹️
بانک رفاه کارگران از ابتدای سال جاری تا پایان خرداد ماه بالغ بر 8,600 فقره تسهیلات قرض‌الحسنه ازدواج و تهیه جهیزیه به مبلغ حدود 29,000 میلیارد ریال پرداخت کرده است.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/444324" target="_blank">📅 21:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8pTXVhsTr1H1gG887eOuS0-qb5owf67SHJuGrFvIP2L7RvjGwfSKQNXv_9rY6AzzJg_vEWSJ3NfZp4FU5Y6ccNZ5TEbvrqx2qWxCH9jZiCyfAM4n-sit5WP0Xe0DAN198VSG8-SEbDG-8QAaE-l93GMYfabiU6iE2Ao66QQUztAv9tylJhUhR6Ai6EdCF6MyQtslORfdN623oGGger0E4ffNL_U-Ao9z2A0-LvhoKLuSKTgo1oKVNOknWup75l9pxrheZunzwxLbEBvUqb_dcU-qU3TYL-oddLWrq_AxDMWMk8eosG2rNJkroytVxctZbqVTG-avpIk7IJfVAISxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/444323" target="_blank">📅 21:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/444322" target="_blank">📅 21:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db07f3a020.mp4?token=LXhCtJQqmhZO9VlxXvwMmCL1GfJ4F9der8EiPoOtXCNFYj_MKLh7I82cSLLXlXy_ElhVaprFU-8Y9fhYjzv0znpCigIYcgPjqWSoK42gtktFfhQh7pKUd8YAQGs04Uy-jjSsZ4iZdy6LCtH7Iv-NPTLO1ebHounco0nOrnAjEZcpEZUFtBa-SHhVpPZa0PWVdcvbhbSrlrPly-Iljb3FHQxxZwg0Wx7FXps0St7WdnPRd_4Ep_DzK9TrAUnkIwMJa-ojcvmNj4GDUQAT8L5-tuus-S8pew4BJdHAgXei45-iUQY66xIYzQ2f1dpiYewZAoDPdPdnBKBck65P96qBQmb2XkHnjMsDXbbRy9LvpJoqWsHf1S6lvJMBQS1i5hkWu8fApxoouuCdxcAraYiOL26I6a4Cj9eQcOuVAEWal7_65APGEZa7RRVnFAtWEBxPgqgQBh6bbZQi0GSsE9APgrS_A825jWLnVRB2jVeAu9uuv9X59Ctx1EtBpZDl2onBzquVCeLBo3LQjTUaTUoy25HxmoTozZrAyum2-LrzA7guvoFLke3REjle4qotwidCTWmLn3KgpTQIrSE302pZBWWQtYe3MshC4XodG91wCAXVORnmEvhayPKetTcYs--mqRoj1gDPxc7zvckhElvlMxdvKtTDFDJYrXxp1ZcCDBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db07f3a020.mp4?token=LXhCtJQqmhZO9VlxXvwMmCL1GfJ4F9der8EiPoOtXCNFYj_MKLh7I82cSLLXlXy_ElhVaprFU-8Y9fhYjzv0znpCigIYcgPjqWSoK42gtktFfhQh7pKUd8YAQGs04Uy-jjSsZ4iZdy6LCtH7Iv-NPTLO1ebHounco0nOrnAjEZcpEZUFtBa-SHhVpPZa0PWVdcvbhbSrlrPly-Iljb3FHQxxZwg0Wx7FXps0St7WdnPRd_4Ep_DzK9TrAUnkIwMJa-ojcvmNj4GDUQAT8L5-tuus-S8pew4BJdHAgXei45-iUQY66xIYzQ2f1dpiYewZAoDPdPdnBKBck65P96qBQmb2XkHnjMsDXbbRy9LvpJoqWsHf1S6lvJMBQS1i5hkWu8fApxoouuCdxcAraYiOL26I6a4Cj9eQcOuVAEWal7_65APGEZa7RRVnFAtWEBxPgqgQBh6bbZQi0GSsE9APgrS_A825jWLnVRB2jVeAu9uuv9X59Ctx1EtBpZDl2onBzquVCeLBo3LQjTUaTUoy25HxmoTozZrAyum2-LrzA7guvoFLke3REjle4qotwidCTWmLn3KgpTQIrSE302pZBWWQtYe3MshC4XodG91wCAXVORnmEvhayPKetTcYs--mqRoj1gDPxc7zvckhElvlMxdvKtTDFDJYrXxp1ZcCDBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم پای‌کار تحقق شروط رهبر انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/444321" target="_blank">📅 21:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444320">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5b2888b6.mp4?token=UXH2Lahbw79gKJHNT_b1tEA61XjC_svdF6zRZ2ait2nOqZoizjPXeFj7mvEU1o7NnPgYUlpXDiX7thm0EL5-yFxR0OyjKDkykOp4he71UMpm_QzgZ38ZS22_OL-jxIUebFuG4GerO1mTiTWwRgavEyQDZTQTNxC2opOec2B_JiMEeA3sUvN8ZvrMCtrN_rMk8YqqJrSNNe2kelVvg2_HvnKDXo-fBbL-sbdHjTCvWBK0yl50uakKC1Ri0_FgBCTGK9e7qStmbCA6qxv4VYUXUG-vW9x-tiWGgj6nUlTV6ky68YSiCJq9e5I80lGoe4Bz4p8ShwFf2PB5u6iP4YoWdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5b2888b6.mp4?token=UXH2Lahbw79gKJHNT_b1tEA61XjC_svdF6zRZ2ait2nOqZoizjPXeFj7mvEU1o7NnPgYUlpXDiX7thm0EL5-yFxR0OyjKDkykOp4he71UMpm_QzgZ38ZS22_OL-jxIUebFuG4GerO1mTiTWwRgavEyQDZTQTNxC2opOec2B_JiMEeA3sUvN8ZvrMCtrN_rMk8YqqJrSNNe2kelVvg2_HvnKDXo-fBbL-sbdHjTCvWBK0yl50uakKC1Ri0_FgBCTGK9e7qStmbCA6qxv4VYUXUG-vW9x-tiWGgj6nUlTV6ky68YSiCJq9e5I80lGoe4Bz4p8ShwFf2PB5u6iP4YoWdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: هرکس که از توافق با ایران انتقاد کرده، باید آگاه و توجیه شود، حتی اگر از دوستان من باشد.
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/444320" target="_blank">📅 21:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444319">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صداهای انفجار با منشا نامشخص در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/444319" target="_blank">📅 21:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444318">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quDZSjrWem1chC-GEDE8-Qce7b4zrj-F_6w9qxztfEq9VaCofFduIKz8cYUojEG-JEKGr-G87sBePDK90H6KerbYkGxMjODd61gbZR6iAtVzfIKE__MKUcFn8Vs70aLf4QByfhmk9P8cUBYRRXUgsKywHVi82dy4BocCUmL2hSMAidrSqcbi9k85eoY9didwVSS1oUQQCW6B1ZmFWHWquvhDRmiUooOiLI22BWwwVcsv_JUJWGrejVs99opFTEEsOYc9lHj9wABGGipjTnDns5Hqwboq8Ld9fqC9qE44lX5pyr1V58QmftqkXibZiNxwpDFiNRqQfmCRquIDu92F8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل زد و رکوردشکنی کرد
📊
🔥
کریستیانو رونالدو با گلزنی مقابل ازبکستان به اولین بازیکن تاریخ فوتبال تبدیل شد که در شش دوره مختلف جام‌جهانی گلزنی کرده است.
@Sportfars</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/444318" target="_blank">📅 20:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444317">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9a71a909.mp4?token=ky7zdeB_mzBndmKwsWsdv5CsawFmz1lnFsIVmGPTx3g5zOVKMKlmi5ytjk3jnz_KbhBDzDsMyqXLd2cd7Ni4jGGPscUeqe1AOybmzyx6U6jskKNfnwdR1-IURhwqzF1Fuk95qZduDbR3kCvJ684eO35hm1R4d-vwthXq6RDHBzjpL1T1eLaM44ZjMns2_6dosR7y5F_9CEzsaFz6kce3IKoNbd9bHh-mzJtxgSxkQBmv5me4VQUEJvyJYrFKijWwWd2eeEGAfK2sSc8CT5In13Qj8A59cBVpE_kdjg8JX0NIDLrYmoySShH-0P-bobxNFyX_Vo5p9Fn9419uLTAzXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9a71a909.mp4?token=ky7zdeB_mzBndmKwsWsdv5CsawFmz1lnFsIVmGPTx3g5zOVKMKlmi5ytjk3jnz_KbhBDzDsMyqXLd2cd7Ni4jGGPscUeqe1AOybmzyx6U6jskKNfnwdR1-IURhwqzF1Fuk95qZduDbR3kCvJ684eO35hm1R4d-vwthXq6RDHBzjpL1T1eLaM44ZjMns2_6dosR7y5F_9CEzsaFz6kce3IKoNbd9bHh-mzJtxgSxkQBmv5me4VQUEJvyJYrFKijWwWd2eeEGAfK2sSc8CT5In13Qj8A59cBVpE_kdjg8JX0NIDLrYmoySShH-0P-bobxNFyX_Vo5p9Fn9419uLTAzXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل‌زنی رونالدو به ازبکستان
⚽️
نتیجۀ بازی تا این لحظه ۱-۰ به سود پرتغال است.
@Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/444317" target="_blank">📅 20:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444316">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWA1vWvKUGX4eIoYeHQRxjfYHvNKrtcfMqqWnsqfY6bZUcsIRlFOGsFQU9N0BJ-ll1tzr4BxKMqhNEuC5Ik2szvdC1Vh-HbmTpAijhs0whkHCrffuR1hzs9r0dO58ZarWlMzcpEw0rojxMy1W3ux1lfTXkLGK3oMseEt436d6Vvu3AFxvR_IdFk-lOMgfC0TU6Jgyu0TFtaHnM6CbQQUJoWkXMxaqj0MQ2zAT1zxs79mEstU-z03u-MGtYJUROWiyVAQtFRFYeJ3HdTuIhyNViouLgE8UCK9bwg0fcKUpiXsiTehN5GSBXwHKq8Z_t-C2ngxPd_KrCi5HZGd4ry8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرسنگی دادن؛ ابزار صهیونیست‌ها برای گرفتن اعتراف از اسرا
🔹
دفتر اطلاع‌رسانی اسرای فلسطینی اعلام کرد که رژیم صهیونیستی از گرسنگی دادن به عنوان سلاحی برای وادار کردن اسرا به اعترافات طی بازجویی‌های نظامی استفاده می‌کند.
🔹
این نهاد تصریح کرد که بیماری گال و حساسیت‌های پوستی در میان اسرای زندان نفحه شیوع پیدا کرده است؛ این وضعیت در پی بی‌توجهی پزشکی و وخامت شرایط بهداشتی داخل زندان رخ داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/444316" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444315">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQYM-YqtrAQvYGIgtMtMUsFCIjX7HObzhBD6m8EexsHlRztho0_nvnXMpJvIBnPyYm9RSG-YMU8i8jOASK0YEmTN2mzbRi4sJW1aAPucdE-2PiuSVPW_h1O8yA3_-nZRYzoBpMHV7T0x1P8KNat44b517ckBy-DNeQran6P6NJV8fk2dtWPbX9xNyrRAFZmXtQvztl8PXBWcbsiN14e9QQRby1g6GUDXgdbM1sJ6mshLX0SQbF4DtZhIiiOKNkiZY3qhCjd-jiiFzh4oYwDRVB9CglkuN4vwU9rAwfKumaZzqLELEB7MvZ7tMghrz5Mf7q_bUZrKYy50wwqBzxol5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف وزیر اسبق آمریکایی به تسلیم آمریکا در برابر ایران
🔹
فرانک کندال: جایگاه کنونیِ آمریکا در برابر ایران، ضعیف‌تر از قبل از جنگ است.من یادداشت تفاهم را خواندم، تقریباً‌ شبیه تسلیم شدن در برابر ایران است. اهدافی که ما داشتیم و هر هفته تغییر می‌کرد محقق نشدند.
🔹
حکومت ایران همچنان در قدرت است. ایران اکنون به طور قطع نشان داده که می‌تواند تنگهٔ هرمز را کنترل کند و تا آنجا که ما می‌دانیم، برنامهٔ هسته‌ای آن‌ها تحت تأثیر این اتفاقات قرار نگرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/444315" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444314">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e3aa64f2.mp4?token=NHwgMzcIe1MsNE9r1HtuA8OprShNrgbCXwDeIn1ZMImtQLPDVLoW54G9BPdbqv9dR5Cd7D5QIQFjpyXciWh1pVr1Gy_Nisj2OIfgsrmxZXHshRECCwdRRQHFG3GlnbVcDMZBuMU_ZpWf_hqVrDy6T5sJWfiYaUTJDCfixU8AQNXX_NPyBWSNjmq47KDqkhS6hQGtvZIoIeaT2CeJgSiZ5ZiP6miqRHgihFvLjCP90YiB9rue77fx2wIu6xR1KAR_1immGJSPOL_QHD5n-Ifv323vP-Vsp6orB7ZSOlpShHKGZN_IJNo_UhNN-LrPWJVHvAU_XqxrEf7FwcN6mYhz2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e3aa64f2.mp4?token=NHwgMzcIe1MsNE9r1HtuA8OprShNrgbCXwDeIn1ZMImtQLPDVLoW54G9BPdbqv9dR5Cd7D5QIQFjpyXciWh1pVr1Gy_Nisj2OIfgsrmxZXHshRECCwdRRQHFG3GlnbVcDMZBuMU_ZpWf_hqVrDy6T5sJWfiYaUTJDCfixU8AQNXX_NPyBWSNjmq47KDqkhS6hQGtvZIoIeaT2CeJgSiZ5ZiP6miqRHgihFvLjCP90YiB9rue77fx2wIu6xR1KAR_1immGJSPOL_QHD5n-Ifv323vP-Vsp6orB7ZSOlpShHKGZN_IJNo_UhNN-LrPWJVHvAU_XqxrEf7FwcN6mYhz2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نخست‌وزیر پاکستان: شفاف می‌گویم که هیچ بحث موشکی در مذاکرات ایران و آمریکا مطرح نشده است
🔹
کشورهای بسیار زیادی موشک بالستیک دارند، چرا من باید اعتراض کنم که چرا ایران موشک بالستیک دارد؟ با قاطعیت می‌گویم بحث موشک بالستیک جایی در مذاکرات نداشته است. @Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/444314" target="_blank">📅 20:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444312">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df08714da6.mp4?token=DlPBQTAUcfoENw0ndpvPMvnz6bjNAtTohqmIl8wh06nw9AmaaNyARCFz8kCJiCcXRvvuAA9sZ4MhhMWtCNNEL9dEAhtgPGXvKYWyBmy2rMjgs-_d_ZbnbNzmftW0C3aBpiUFXG6BfWKNCSHpBg-ur8UuYvBhYebsKfzyjyILLJYSAhfE_8858pjWuIb3nE2nlsuN4SBT7v1WgDJ6F7Gx9zWOINo-AYt3Ro9fUPeNsbH_JNeH5w6tVXbaFqJLJve_cANuaVoGJ08pk7cfEy6mx3bQ_YIcc_yBdOECNyUyupHAAKdLvHjQE4c2sAzpRlnA12J9cxlM5zddCvVODb5m9TQfnOqFq_9y5kHzxJsGLPqjHHwocYTaROq6PQcUCUkNU0S0tWxn5V8QDh-V2utoJ1TdWh0yHt3djn31FCF-VkQP7P9sm5oGopZhs6HPYv2paNUaD3TXhYNvS_9xEL--1MaqHxf_YYXZ1yuxf1v70TQ89jhIQaIoE1kOXjkFJrFRMPNgPAhAyBzWRF_BzfDub52zgY5bpRilw5azOQbsed4pUhCnHNuC5DyRujynlPD2HOAuuSI6xXvyQzGSrnp57vDvmyedC_gJTmBNICGESQifsDmONn4vmiQ7K4VWotkzOA8YXyUH5xN8Th19J982xrO2280G9N5EKst6NShirUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df08714da6.mp4?token=DlPBQTAUcfoENw0ndpvPMvnz6bjNAtTohqmIl8wh06nw9AmaaNyARCFz8kCJiCcXRvvuAA9sZ4MhhMWtCNNEL9dEAhtgPGXvKYWyBmy2rMjgs-_d_ZbnbNzmftW0C3aBpiUFXG6BfWKNCSHpBg-ur8UuYvBhYebsKfzyjyILLJYSAhfE_8858pjWuIb3nE2nlsuN4SBT7v1WgDJ6F7Gx9zWOINo-AYt3Ro9fUPeNsbH_JNeH5w6tVXbaFqJLJve_cANuaVoGJ08pk7cfEy6mx3bQ_YIcc_yBdOECNyUyupHAAKdLvHjQE4c2sAzpRlnA12J9cxlM5zddCvVODb5m9TQfnOqFq_9y5kHzxJsGLPqjHHwocYTaROq6PQcUCUkNU0S0tWxn5V8QDh-V2utoJ1TdWh0yHt3djn31FCF-VkQP7P9sm5oGopZhs6HPYv2paNUaD3TXhYNvS_9xEL--1MaqHxf_YYXZ1yuxf1v70TQ89jhIQaIoE1kOXjkFJrFRMPNgPAhAyBzWRF_BzfDub52zgY5bpRilw5azOQbsed4pUhCnHNuC5DyRujynlPD2HOAuuSI6xXvyQzGSrnp57vDvmyedC_gJTmBNICGESQifsDmONn4vmiQ7K4VWotkzOA8YXyUH5xN8Th19J982xrO2280G9N5EKst6NShirUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
نخست‌وزیر پاکستان: به کشورهایی که می‌خواهند در مسیر توافق سنگ‌اندازی کنند می‌گویم چطور ممکن است خودتان موشک بالستیک داشته باشید اما این حق را برای ایران قائل نباشید؟ @Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/444312" target="_blank">📅 20:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444311">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎥
نخست‌وزیر پاکستان سخنرانی‌اش را به فارسی تمام کرد: زنده‌باد دوستی ایران و پاکستان
🔹
شهباز شریف: هفتهٔ آینده به تهران می‌آیم تا در مراسم ادای احترام به رهبر شهید ایران شرکت کنم. @Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/444311" target="_blank">📅 19:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444310">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda5c8ae83.mp4?token=b11WrTcglP7G_VJ8Yxe42QZ3rzvB4w33P0qBT8oGdZXM3HpEmMfbQ1Z5AINZok2y6Xh3Vq5DR3NWG4-hhTFuN4OdP6_zKkx0mONkOC4iOXSGJoPwwxT64g0sAk_bJLbCtw__xhOFzEVX8MjFrh5KDpbSTb33tJGmIWH3_e91n951cGWBPQhbg7vgZs4m17U-ynzpHdRLGCclDPhTOY1XSdZhKB08QmVM7gdSWElEsYZVYPqpXzskZGGxqpxPL1fjij29Fij3Mn4jEo-3sk1OfHL8qXXtKbQmDZedOb6GyEp7DVknsq7URMMitsiNgUZuHnSlBM09PFv4ZH7Ko4FMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda5c8ae83.mp4?token=b11WrTcglP7G_VJ8Yxe42QZ3rzvB4w33P0qBT8oGdZXM3HpEmMfbQ1Z5AINZok2y6Xh3Vq5DR3NWG4-hhTFuN4OdP6_zKkx0mONkOC4iOXSGJoPwwxT64g0sAk_bJLbCtw__xhOFzEVX8MjFrh5KDpbSTb33tJGmIWH3_e91n951cGWBPQhbg7vgZs4m17U-ynzpHdRLGCclDPhTOY1XSdZhKB08QmVM7gdSWElEsYZVYPqpXzskZGGxqpxPL1fjij29Fij3Mn4jEo-3sk1OfHL8qXXtKbQmDZedOb6GyEp7DVknsq7URMMitsiNgUZuHnSlBM09PFv4ZH7Ko4FMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جملهٔ فارسی نخست‌وزیر پاکستان خطاب به پزشکیان: غم شما غم ماست
🔹
مردم پاکستان همراه با مردم ایران هستند؛ ما در شادی‌ها، غم‌ها، موفقیت‌ها و شکست‌ها با شما شریکیم. @Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/444310" target="_blank">📅 19:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444309">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37bbe0e8e2.mp4?token=oC0y1iNZo3i7kA6H5moQVpLpbKRgPTjVPVfUKGPCgem-aZFhoAqNRdYjmq82N5acB6SKRrs4H6JdjgnZVFgGBC2TgqS1YCf3ekEECE6dfuJLeZeUCkV7Gwy44yOrQeRH2ms4zMKI6muzCuSP8S8VSjD90Rne3JS21yPLed6HqWrxEITsmYEplZ0roHcGEgPLRe9ugSN0UQJ3dxpJ7IX1QgF6aYEaebCkW6vgqi2EbSoKQ54qAcYS2z9EHA_SfS5y2rOnYAMNvVRWAm3WcnUzehHvnEiTyuuyie4KYW8LX00bg41-OQwHM9EccqAdEuiwgXyChr6qQrbiu3yINTFm1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37bbe0e8e2.mp4?token=oC0y1iNZo3i7kA6H5moQVpLpbKRgPTjVPVfUKGPCgem-aZFhoAqNRdYjmq82N5acB6SKRrs4H6JdjgnZVFgGBC2TgqS1YCf3ekEECE6dfuJLeZeUCkV7Gwy44yOrQeRH2ms4zMKI6muzCuSP8S8VSjD90Rne3JS21yPLed6HqWrxEITsmYEplZ0roHcGEgPLRe9ugSN0UQJ3dxpJ7IX1QgF6aYEaebCkW6vgqi2EbSoKQ54qAcYS2z9EHA_SfS5y2rOnYAMNvVRWAm3WcnUzehHvnEiTyuuyie4KYW8LX00bg41-OQwHM9EccqAdEuiwgXyChr6qQrbiu3yINTFm1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر انقلاب ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
🔹
مقاومت مردم ایران را ما تحسین می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/444309" target="_blank">📅 19:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2efa8e227.mp4?token=RP-mLXSjvW-iijeDpe3a6347dcJLVMK_VSQEQveXg814bKIZ_y-VKPt5o3yjDIGiEfhnNsAxI_dX1ezO5ehA99LeYJdD3zJuqjZuxI-IVGeX7mKOoBoo2f9WpZ3H319CAUhtshrdKs470qHqa5eajh7c_9V4kqIutfnm5JKn--x8cTHZYDfZPZ3iWfHgwEYqw59rfE_rQJX0SwFL7rbc8lYeXWINWf21BoHD7DzO1DanZ9t5Jdw6TOe30Yk3gdUMNkTNGbTJgMhOO_AO7ZRj39Zwkw3pfOikiLWC_5Bz4UfPeLwgBL2MG7K0Hn0HOurC36O0EvadpaFtK96YFri_lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2efa8e227.mp4?token=RP-mLXSjvW-iijeDpe3a6347dcJLVMK_VSQEQveXg814bKIZ_y-VKPt5o3yjDIGiEfhnNsAxI_dX1ezO5ehA99LeYJdD3zJuqjZuxI-IVGeX7mKOoBoo2f9WpZ3H319CAUhtshrdKs470qHqa5eajh7c_9V4kqIutfnm5JKn--x8cTHZYDfZPZ3iWfHgwEYqw59rfE_rQJX0SwFL7rbc8lYeXWINWf21BoHD7DzO1DanZ9t5Jdw6TOe30Yk3gdUMNkTNGbTJgMhOO_AO7ZRj39Zwkw3pfOikiLWC_5Bz4UfPeLwgBL2MG7K0Hn0HOurC36O0EvadpaFtK96YFri_lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر پاکستان: شهادت رهبر عالی ایران، آیت‌الله سیدعلی خامنه‌ای، را تسلیت می‌گویم
🔹
ایشان برای ما و تمام مسلمانان جهان قابل احترام بودند. @Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/444308" target="_blank">📅 19:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bdb4f54c6.mp4?token=oI3VyK4gGQexSiZOwT689Uj_hNBJZdajEmu56toqRleaGpZ-5mL_4ZDeDNIABaUgavbYb2QryDF8YEWDc5kYM55_uKv6nS4up7tvuwTz3Yzy23DP0ABNIiOx5552aT3GFBB76gd3dZVmG26ss43JfA_PdNqrnZ9D95RnfRvkGwV0mySjKc7x2zoLGB5iCiRkvqtFpJ19Lw2D52mqyvQTOV2SRN4Ji1AbvRGa-GR8ySxXBEI-RCdh0DhyEBtVDKXs4MQo1_Ej1uZ2I8uLoABoyMyNVaYQ07OvLdIeY8xMO205BzKo2-7QLxf799Bsd4S3aazHE-G5ilPaHQeS1_AADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bdb4f54c6.mp4?token=oI3VyK4gGQexSiZOwT689Uj_hNBJZdajEmu56toqRleaGpZ-5mL_4ZDeDNIABaUgavbYb2QryDF8YEWDc5kYM55_uKv6nS4up7tvuwTz3Yzy23DP0ABNIiOx5552aT3GFBB76gd3dZVmG26ss43JfA_PdNqrnZ9D95RnfRvkGwV0mySjKc7x2zoLGB5iCiRkvqtFpJ19Lw2D52mqyvQTOV2SRN4Ji1AbvRGa-GR8ySxXBEI-RCdh0DhyEBtVDKXs4MQo1_Ej1uZ2I8uLoABoyMyNVaYQ07OvLdIeY8xMO205BzKo2-7QLxf799Bsd4S3aazHE-G5ilPaHQeS1_AADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواپیمای پزشکیان با اسکورت ۶ جنگندۀ ارتش پاکستان به اسلام‌آباد رفت  @Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/444307" target="_blank">📅 19:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما با تکیه بر ایران وارد نبرد اخیر با صهیونیست‌ها شدیم و با این کار، قدرتی را به قدرت موجود خودمان اضافه کردیم
🔹
ما می‌خواهیم لبنان را آزاد کنیم و حملات و اشغالگری صهیونیست‌ها متوقف شود‌. @Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/444306" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
دبیرکل حزب‌الله: بعد از آتش‌بس، مرحلۀ بعدی عقب‌نشینی کامل صهیونیست‌ها از خاک لبنان است
🔹
ما از ایران تشکر می‌کنیم و به ایرانی‌ها می‌گوییم شما شرافتمندترین انسان‌های جهان هستید. @Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/444305" target="_blank">📅 19:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444304">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb26baee6.mp4?token=j1tW6pP2bHhPn3CMIREwadTgIuLxwjOs613mbLOZ5OFjmo0-t3p6zJixPQWNl81PmRPqJAdQ7DtG_aVCs9VCW6kWEjOa3seDklTjE1emvsgjBt2tATjH6H__Ak_K2caxrd_mo6cQC87QNt9QeWFHxvM2LgG7HYhy8-efMLQ53xEMZM5zos3ISE9S8TY01kHAPkOO716aIm-aj4vRKtoYRB4-uxls7GpQhavD7yrGfZQU5ictWDR3IaXBM4Jd4Ry-CEW9fqMs1iJk6njVH6rscH6vhxLhz0iAvhgXShwruqqqARTpkhOrFyqA8enmQ-iyfpXj1-DisgIe6rR9sZ6sKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb26baee6.mp4?token=j1tW6pP2bHhPn3CMIREwadTgIuLxwjOs613mbLOZ5OFjmo0-t3p6zJixPQWNl81PmRPqJAdQ7DtG_aVCs9VCW6kWEjOa3seDklTjE1emvsgjBt2tATjH6H__Ak_K2caxrd_mo6cQC87QNt9QeWFHxvM2LgG7HYhy8-efMLQ53xEMZM5zos3ISE9S8TY01kHAPkOO716aIm-aj4vRKtoYRB4-uxls7GpQhavD7yrGfZQU5ictWDR3IaXBM4Jd4Ry-CEW9fqMs1iJk6njVH6rscH6vhxLhz0iAvhgXShwruqqqARTpkhOrFyqA8enmQ-iyfpXj1-DisgIe6rR9sZ6sKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: تنها تضمین برای آزادی خاک، استقلال و حاکمیت کشور، مقاومت در برابر اشغالگری است
🔹
اسرائیل در میدان نبرد دوام نخواهد آورد و حتی اگر زمان طولانی هم بگذرد، نمی‌تواند به اهدافش برسد.
🔹
برای ما هیچ تضمینی جز قدرت خودمان وجود ندارد و قدرت ما همان…</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/444304" target="_blank">📅 19:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: تنها تضمین برای آزادی خاک، استقلال و حاکمیت کشور، مقاومت در برابر اشغالگری است
🔹
اسرائیل در میدان نبرد دوام نخواهد آورد و حتی اگر زمان طولانی هم بگذرد، نمی‌تواند به اهدافش برسد.
🔹
برای ما هیچ تضمینی جز قدرت خودمان وجود ندارد و قدرت ما همان مقاومتی است که بر پایهٔ ایمان، اراده و توانمندی بنا شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/444303" target="_blank">📅 19:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e6ca44db.mp4?token=VgNBEVK5e8olxEPuU7SHzaCNKnbhSJh3uSiZrtcY7NnDLf17zw_l8242cKEuI6vqEjYeS0g-iPqGS66yrldoKcX8aPaUWi8BKbWU87S19i6dru5i6653jfN4IhObHYpZgyTnsfJZTCn1XWz8FPafkBE_70Br3m6XGuj_MDKxFhj_Y5UNhzT68Qmdh64Cw7Das-Ka7yCQUjzUjwQxoQKaJoFgnnxypGqfS-T7JIgZ7NPALbJ3apw1pWiYtyRtDVMMCrZWzYGP5kUT1j0rCDVDLhlUe5c8wyQW8m12rhQXfeAF779EFnEhip5RqyrBEcbkjhbZb0Gf4jyOr05Ko2OltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e6ca44db.mp4?token=VgNBEVK5e8olxEPuU7SHzaCNKnbhSJh3uSiZrtcY7NnDLf17zw_l8242cKEuI6vqEjYeS0g-iPqGS66yrldoKcX8aPaUWi8BKbWU87S19i6dru5i6653jfN4IhObHYpZgyTnsfJZTCn1XWz8FPafkBE_70Br3m6XGuj_MDKxFhj_Y5UNhzT68Qmdh64Cw7Das-Ka7yCQUjzUjwQxoQKaJoFgnnxypGqfS-T7JIgZ7NPALbJ3apw1pWiYtyRtDVMMCrZWzYGP5kUT1j0rCDVDLhlUe5c8wyQW8m12rhQXfeAF779EFnEhip5RqyrBEcbkjhbZb0Gf4jyOr05Ko2OltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
سندی دیگر از جنایت آمریکایی‌ها در لامرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/444302" target="_blank">📅 19:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بستۀ خط ۷۵.pdf</div>
  <div class="tg-doc-extra">2.5 MB</div>
</div>
<a href="https://t.me/farsna/444301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۷۴.pdf</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/444301" target="_blank">📅 19:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43390b6bb.mp4?token=I1Q_T_q8wOFwnu1qvFsboCFBtHc_VuQzAxxWL03TBxtnidJsqEJ_LxzXl1-daqwoqzx7LsCnJa--glCUz4aKmkeo7W2t4hNLddJ3lkFht2_Y8TS4ZxKYwHP_Wdmo0iukhxg0XJx1UGx-00WNTU0y6renuVFIIstVom-413aJ-Gpoiz8eJTulDPpITImjiAO7mC27nmxmfB8O7dW7jbK-q1oqL_a2hbbsjaTww3-cszlBAKBNzK874Yxr7z-QjIRRDss0ZV70X7kBJP-Y6xB-i6cbVOap2qdF5_CuwYZbJOrSR2Wo9p9gazQnwHDNqzxwEBd2_3cyxQ9ANrQ0-Q0d0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43390b6bb.mp4?token=I1Q_T_q8wOFwnu1qvFsboCFBtHc_VuQzAxxWL03TBxtnidJsqEJ_LxzXl1-daqwoqzx7LsCnJa--glCUz4aKmkeo7W2t4hNLddJ3lkFht2_Y8TS4ZxKYwHP_Wdmo0iukhxg0XJx1UGx-00WNTU0y6renuVFIIstVom-413aJ-Gpoiz8eJTulDPpITImjiAO7mC27nmxmfB8O7dW7jbK-q1oqL_a2hbbsjaTww3-cszlBAKBNzK874Yxr7z-QjIRRDss0ZV70X7kBJP-Y6xB-i6cbVOap2qdF5_CuwYZbJOrSR2Wo9p9gazQnwHDNqzxwEBd2_3cyxQ9ANrQ0-Q0d0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار یک‌صدای زنجانی‌ها در حسینیهٔ اعظم: آذربایجان شرف‌دی پهلوی بی‌شرف‌دی
🔸
پهلوی شهزاده‌سین خار ایلمک چوخ ساده‌دی
🔸
تک بو دنیاده علی‌اکبر بیزه شهزاده‌ای  (خار کردن شاهزادۀ پهلوی برای ما بسیار ساده است تنها شاهزادۀ این دنیا حضرت علی‌اکبر(ع) است) @Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/444300" target="_blank">📅 19:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444298">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b87e7d200.mp4?token=ti1M5P1eiaQe_naouS3FMz80Omhfq9O_GuXrYzBBKo83EAwwKMV5V9Qq4AOpl-7_YOhOqpNQ89KVnpzh42nkNsdetFVeVfEWBFDcB8xOpFOC28QIkhUDkkToc7glpzGfMg6ueAq_CTTSSmwQ1tumxUu9PUj4qYE62KZhsi64hUH7KRpw9xR0BTu0GhK1ZlgrbxCtorHbPMJryUooUrWA4GXJoZ5hRSsxprIcjuGUxh_sKYSum_nlr0D_Zwj-SkA_J3lqdA3kctuBdrr-zOjerkJOjzeEY9V9c6L4AeZr0CGbgNVhVtT46g7H6H2Px9LV2fAWyebmW630aSUew8TmlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b87e7d200.mp4?token=ti1M5P1eiaQe_naouS3FMz80Omhfq9O_GuXrYzBBKo83EAwwKMV5V9Qq4AOpl-7_YOhOqpNQ89KVnpzh42nkNsdetFVeVfEWBFDcB8xOpFOC28QIkhUDkkToc7glpzGfMg6ueAq_CTTSSmwQ1tumxUu9PUj4qYE62KZhsi64hUH7KRpw9xR0BTu0GhK1ZlgrbxCtorHbPMJryUooUrWA4GXJoZ5hRSsxprIcjuGUxh_sKYSum_nlr0D_Zwj-SkA_J3lqdA3kctuBdrr-zOjerkJOjzeEY9V9c6L4AeZr0CGbgNVhVtT46g7H6H2Px9LV2fAWyebmW630aSUew8TmlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای «مرگ بر آمریکا» و «مرگ بر اسرائیل» در حسینیۀ اعظم زنجان طنین‌انداز شد  @Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/444298" target="_blank">📅 18:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444297">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9442cd8cc2.mp4?token=EmI6GUxBWputIrHbys53pwpjtEFQ5KdFQgeVMK6xjRlu0-1Salld1vaa4tO-rVKdBu-9w6WEHVKV953AmaL_GAkdUjBS6x9y1N5vH_zGf94hvA0mjmqRjjYKCTus0ybvG_URdncoHesSk9Q5C6YvXDy3MQUcn069l5ydwW7W6bhI1vNEVzhZkhUfW9KuueHb04VUB8rMA0AL09H1slFABC89pPwEGCHTYhJA1dv8YHNIs0J4QlxFub97ep_g_IPMPwj5axjty4ZhEdHjiBkDYgxJY7quutNpbmbYtaaTUOsqiZApPYukE6lgnjBe1mCnyId3uNhsV9aEACI95xxDSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9442cd8cc2.mp4?token=EmI6GUxBWputIrHbys53pwpjtEFQ5KdFQgeVMK6xjRlu0-1Salld1vaa4tO-rVKdBu-9w6WEHVKV953AmaL_GAkdUjBS6x9y1N5vH_zGf94hvA0mjmqRjjYKCTus0ybvG_URdncoHesSk9Q5C6YvXDy3MQUcn069l5ydwW7W6bhI1vNEVzhZkhUfW9KuueHb04VUB8rMA0AL09H1slFABC89pPwEGCHTYhJA1dv8YHNIs0J4QlxFub97ep_g_IPMPwj5axjty4ZhEdHjiBkDYgxJY7quutNpbmbYtaaTUOsqiZApPYukE6lgnjBe1mCnyId3uNhsV9aEACI95xxDSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
بو مقدس پرچم، آخر کفنیم‌دی
🔸
کِچمرم ایران‌نان چون جان و تنیم‌دی  (پرچم ایران کفن من است از پرچم ایران نمی‌گذرم چون جان و تن من است)  مداحی زنجانی‌ها در یوم‌العباس @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/444297" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444296">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
جمعیت عزاداران حسینی در مراسم یوم‌العباس زنجان   @Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/444296" target="_blank">📅 18:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444295">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c23cec62f.mp4?token=MPup09aOhks0Mdh52Jt0kwfJgX2ztDJ6bD97NJXLWJHmqUCsNK86mM4ZVqamVNhOVSQQvXjEE04VzTSAnUgm5bODzWQwoVHJFnCMDyCBwQJDt89yGwwtj7VRvpVoVCC9VD9VceqPlOoOh38UuJOYB-_ND5qFB3zlwX0i39oiwkzBymPi-aBQKrzEmPu5P3jUSf6s0hSGRt5lBXg0tS7d3PJOg3TJ4S5_WI0t2ANXK2J05F7ee2nOVyTEHqxtrLdvGYJRPxh60p3IuubYJywwdtTA6wZXqzUrbbcEfrvGFcBf9KDGxS3k4-GrwnPoEUFxMokivT8aAsLxS0VD3nMGtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c23cec62f.mp4?token=MPup09aOhks0Mdh52Jt0kwfJgX2ztDJ6bD97NJXLWJHmqUCsNK86mM4ZVqamVNhOVSQQvXjEE04VzTSAnUgm5bODzWQwoVHJFnCMDyCBwQJDt89yGwwtj7VRvpVoVCC9VD9VceqPlOoOh38UuJOYB-_ND5qFB3zlwX0i39oiwkzBymPi-aBQKrzEmPu5P3jUSf6s0hSGRt5lBXg0tS7d3PJOg3TJ4S5_WI0t2ANXK2J05F7ee2nOVyTEHqxtrLdvGYJRPxh60p3IuubYJywwdtTA6wZXqzUrbbcEfrvGFcBf9KDGxS3k4-GrwnPoEUFxMokivT8aAsLxS0VD3nMGtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم باشکوه یوم‌العباس در زنجان
🔸
حسینیۀ اعظم زنجان در جریان جنگ اخیر هدف حملۀ آمریکا و رژیم صهیونیستی قرار گرفته بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/444295" target="_blank">📅 18:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444294">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d9848065b.mp4?token=CTNGnqs7IP5hgvzstq7sNkk7LqglI1ZiALZ4QUrYsON2gU9W0ejnnazNZ-QQuNUplzNY3sKQZvyghyLV3l5lI4kdiR6cGDi92AJQHsyKZgnMpEfu3aIe99znGIjJPlMhlAqL8xG-w9NJcVH8JlP67z3oWHBH3Tz1pFMvXAXx9H5Ygy_Tn3GyodLKT-ZhbemZmCom6LWGh_bzbsko-CBW1PJ1ESiREyTLVPnCNA8zxnTRV_bWREjhD9XwjtVljsGq767af5xwP05LZe9XlvKEd-RjOWUgOMALPCksOYfVPm8O042F4DjTYxMqqY8VIqq9IYR5HgLZTsNaw8fb2t-New" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d9848065b.mp4?token=CTNGnqs7IP5hgvzstq7sNkk7LqglI1ZiALZ4QUrYsON2gU9W0ejnnazNZ-QQuNUplzNY3sKQZvyghyLV3l5lI4kdiR6cGDi92AJQHsyKZgnMpEfu3aIe99znGIjJPlMhlAqL8xG-w9NJcVH8JlP67z3oWHBH3Tz1pFMvXAXx9H5Ygy_Tn3GyodLKT-ZhbemZmCom6LWGh_bzbsko-CBW1PJ1ESiREyTLVPnCNA8zxnTRV_bWREjhD9XwjtVljsGq767af5xwP05LZe9XlvKEd-RjOWUgOMALPCksOYfVPm8O042F4DjTYxMqqY8VIqq9IYR5HgLZTsNaw8fb2t-New" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر انرژی آمریکا: ۱۲۱ سال پیش، آلبرت انیشتین مقاله‌ای درباره پدیده فوتوالکتریک...
🔹
ترامپ: هیچ‌کس به آن اهمیت نمی‌دهد!
🔸
وزیر انرژی آمریکا: نکتهٔ خوبی بود، راست می‌گویید.
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/444294" target="_blank">📅 18:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444293">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فرماندهی مرکزی آمریکا: ۲ ناو آمریکایی در خاورمیانه فعال هستند
🔹
سنتکام با اعلام تردد ناو هواپیمابر یواس‌اس جورج بوش (CVN ۷۷) در دریای عرب خبر داد که نیروهای آمریکایی با ۲ ناو هواپیمابر در منطقه حضور فعال و هوشیار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/444293" target="_blank">📅 18:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444292">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_LM4cSrXQ2qWUJYJ3S4FryuFWTyhnqxloHqHAdYQoA3Cr_LTfF6DUJlbOdtSObOuhBROveBa1NywDZA0khrdcD0JGVr2D8YLmyu1tlvrWOeZZHGu-xRLGqrlzZI3deQ6gnZNXIBGbQJp0g0ZiS6034Dr9TxeNnfI__TTrhywb0bgLGZFuoUjIs75GdlnmSNAJ4UpqGAy9xUy9GPOAVZDMZfMZ-GEdenDlNwAUkS64pQ-hjWP2EvriItl5eyVsXuRfbld7lya5Iscu4-AlyaplV7j5OUpulZqH4SmePlaDe57a--7BLyUQ1tcv3V8dbBtX7GL38u-7I33a7__KqMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جریان سوخت‌گیری در پمپ‌بنزین‌های تهران عادی است
🔹
پس از اختلالات ایجادشده در شبکۀ بانکی و پرداخت موقت هزینۀ سوخت‌گیری به‌صورت نقدی، فرآیند عرضه بنزین در جایگاه‌های تهران به حالت عادی بازگشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/444292" target="_blank">📅 18:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444291">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11d0b10e2d.mp4?token=HjpQCgt5yYyoyZYWCjWzAmZ-9FixCtZeGmZoQC1-YERbP4ZZ9pjqFU2GMiWaTDkRDzUMI-VK5qo-fxlF8DrsUwT4Ezup-fWITMDoKsN9DcYulc7wTucTa4AKYef1k6YMcZRWyjxL4em4Wz9ihQF03QmxIqSh7tF0HaXh61D84M6VTLM-w_YShiOWxwnyXOHUma6OKJ2xc9RtvSMaDsmxCeJW246i-rS_8knC-ib6KUETm10XgUjgf9XEprYAgfGWNclSkOe026yCm2Q8I-KjHcbd4G9HXu21HwALlustnNqiTH702ngGjUaCvrRWoricKm9rd7UV0azykR-JYf_8vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11d0b10e2d.mp4?token=HjpQCgt5yYyoyZYWCjWzAmZ-9FixCtZeGmZoQC1-YERbP4ZZ9pjqFU2GMiWaTDkRDzUMI-VK5qo-fxlF8DrsUwT4Ezup-fWITMDoKsN9DcYulc7wTucTa4AKYef1k6YMcZRWyjxL4em4Wz9ihQF03QmxIqSh7tF0HaXh61D84M6VTLM-w_YShiOWxwnyXOHUma6OKJ2xc9RtvSMaDsmxCeJW246i-rS_8knC-ib6KUETm10XgUjgf9XEprYAgfGWNclSkOe026yCm2Q8I-KjHcbd4G9HXu21HwALlustnNqiTH702ngGjUaCvrRWoricKm9rd7UV0azykR-JYf_8vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدرسهٔ میناب امروز به میعادگاه آزادگان جهان تبدیل شده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/444291" target="_blank">📅 18:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444286">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzi6xcjapTh0jYwBEKNkcv1m4yVxWSAqNjwENwQAMbVwxvZrY49fZKK0FPz1uqMIr4xjHK5DBBXXuBE92FyxswsOLWTF42Riv_30GZ2HKE5m5OF1izc36auenLJJlksPEU1nTRCDq1PnwHDiq4u_ItQYKSqTj7VbVDfylkoZ6bW-litVwnbz6s2eA7hPoXdUDzUKgHLGb6t9dYtUrdH0pqwS9SwpOPiI4JuoXKh1aTV844vkF15R4PFj9Z7Do5CSTgswtc7uzwwQCJoaZsRZTGrb-LE__50TUOkLUQtyo1qB_3f4a9k3L-We_IGQUWhphZx5FHjqA5jqokPlp1hyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k4f1l5OOzQiGuXZTESCq6Tjpu5CBImPzpi2ytT3gSwh0V7eFgAK8_TCZD80xr490r-iY0j-NaFM3Xb6kkG4OvXOLGIvPw7j1sJFS9kYQt9diebvY_C_bHRdLmfD3cXLjLLSGwZcu6nSdIhUt3wWnnPeFIaH0DCZZymMt__BKi3DeO3UoLCHr0-ajQ7erfqgm99CPdhQO0nHxeqgTRMZKhqdz7I8f6tuyVOSkMp1ZMcrZmOcRcbnu4-84Zosl3-pVUwOihWTwarZNdenjhFs9c-pGbI8ubbdFbULeC20H4n0dFFol64G2pB8QopZCkXRER9S7Ju_c06rmi4uLsfpqEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivcri7QMOhlBKJInb0MZU5vg57KVHekE-p4S6uQh8uKzuNhq2ajyX3w8Q1BH3RXTbZr6WNp8MoLC5bCpIouObS40hbPO-KzWNSqhxVL2qKez4Og3cBNFLTMkWR5qeY21ikMWkj4vAGFabZ4kYaVnMahSfeW8TtwnbpiieSYcOIQIKVcuP4hJLgNWMazB2Rs0Qe0s3vo5ZNA1imNe4u4NyFhWC31s-joYKkdVeIGwCAPyRo1weWbeMt8JdCbocz-npTSw5Aw34As3DLl-zo0j7erpDJCnuSa9Xc1eK9WNqh4BdkPtf3ZNbadv3rObHSzUf0gaVIphvWInuhqHJzDJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QL2r7BLtNIs0uQSCWGsiGcfBaa8mooXdrDetjRFRbDh5IS_HQQCCAFbZtiNAAgXFMDs-hNQm6J3oyApL7i4ypP21PSHmMi6BMEKs7214RVMRaaZssoQS5cN5fJWRfkmoBq9kob_ziJSFMOMRfcTqiR9-C07yBE2QxIdfs8YvFi0n4qtuMuV8taZZxLpUX-JNeONqDOZZFxdcaloGSp5iyfnyU7t92NjADyDhp9LBZ0Pmkrb4XyOUZeXBZ8t4Ye4WxYzCgy8BgPX28h5YlY2fL8l2Hf6IJn7zamG0qmKXWax7FxzaSBEbnzDPm-Cu-AzucYGcifb5yhw010wvENOkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kFzDQ0Dnmg6xGthK3UFgF9YheaU8zvh29RsZ1sFkV1nCHswJN44C5bgCU1_5CknulHscMARHbigXfhIQWKoK4fBje4ZvYsHHfuqBAF5nL3eIFTWW8q5bcdnfgdtud2euTqdptTf__X46p9XTkh1pMBQJzrl64Hub8Ig0pEKSAC2JpJpAsj_v2Bzk4aLAJC3GR_B4FoVz6y3KhArX5DR__FoSMJc5HnAoJEuM8pkAd1NaVb32ntMlqZYw-Sh82_kSIMLmbO7ss4SoM_7c9UzWIG4R9jhk0T3qgqlkYR7Zbgx3J3-mtDlXKkttTYIqW33jj8NOiiy0pUXs9oi72UGsxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دشت آزادگان غرق در عطر عباس(ع) شد
🔹
مراسم یوم‌العباس(ع) با حضور پرشور مردم دشت آزادگان، جلوه‌ای از ارادت دیرین خوزستانی‌ها به علمدار کربلا را به نمایش گذاشت.
عکس: میثم گمراوی
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/444286" target="_blank">📅 17:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444285">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82297da050.mp4?token=tiQy5M5nk1weW0LSJkz-diH9or7ErY0wyQOrEHZYYlb6uMOW6wN2-z10kxR6Nt4JPs3wbczpVBh26SPk9wBArL1evUrOO32Ntza0gQvLefHksdlhFK5GZqz7MidWN4wOKol-2gNTIxO3p2WZDl2LQTjqDXzXH-fZQhEkFDdlsS5FUY8j2cm7x2WvLiQwoi5J7F-EGG-sWd5uh6mxIEXJFAhj9PAT7-JIT3NIre4Pcr3gHkI_a30wedGoBSeNHTguU6vFXdluE8WYnQJRZnrGNGH2_P4NoOCOxBwrtDcdP2WHJJgeE0qihYbCuIQPAk2CujeWEHoeL6wjsfeyr58Qcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82297da050.mp4?token=tiQy5M5nk1weW0LSJkz-diH9or7ErY0wyQOrEHZYYlb6uMOW6wN2-z10kxR6Nt4JPs3wbczpVBh26SPk9wBArL1evUrOO32Ntza0gQvLefHksdlhFK5GZqz7MidWN4wOKol-2gNTIxO3p2WZDl2LQTjqDXzXH-fZQhEkFDdlsS5FUY8j2cm7x2WvLiQwoi5J7F-EGG-sWd5uh6mxIEXJFAhj9PAT7-JIT3NIre4Pcr3gHkI_a30wedGoBSeNHTguU6vFXdluE8WYnQJRZnrGNGH2_P4NoOCOxBwrtDcdP2WHJJgeE0qihYbCuIQPAk2CujeWEHoeL6wjsfeyr58Qcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اختلالات گسترده به بانک‌ها برگشت
🔹
در ادامهٔ اختلالات ایجادشده در شبکهٔ پرداخت کشور، امروز هم گزارش‌هایی از بروز مشکل در خدمات کارتی و موبایلی چند بانک بزرگ از جمله ملی، تجارت، صادرات و ملت از سوی مشتریان این بانک‌ها اعلام شده است.
🔹
پیگیری خبرنگار فارس…</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/444285" target="_blank">📅 17:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbRNBzkf2qq3gdmIQQ7UaHcvgg9bWf_fENVKteZJhabf7zZTJumw3eD94BlyV4H7403o9ZvFNdc4SxyONID_odEEE61cplnbGQmz5Z1HvWae_eyC-SK034dIZf4VZALpA4Nxdt8w9oGmxcuiLvgy_XaKd5n59hC8hutyvkL74LaXPZo1PEZmpDiTXuQ1qnFGOgrAGGA0pfMETGDOo5Aewaw1cSt7gqCNKO9NAcYLRnEj0nQ5sPXPtjvhutJUfIyfQuXZsOvyAc0NPXURIRl4I1eSG4BDz29g7phLmFt_29J7Cce1RBdvsBv5ljk5jIhx8JMcT1qRDQyeEOpm4CDbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط پیش‌فروش خودروی آریای سایپا اعلام شد
🔸
مبلغ پیش‌پرداخت: ۱ میلیارد و ۷۴ میلیون و ۷۸۷ هزار تومان
🔸
زمان تحویل: از تیر تا پایان مهر ۱۴۰۶
🔸
سود مشارکت: ۲۰.۵ درصد
🔹
ثبت‌نام از ساعت ۱۰ صبح روز یکشنبه ۷ تیرماه در سامانۀ
saipa.iranecar.com
آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/444284" target="_blank">📅 17:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444283">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
حسینیه‌ای در تهران که ۲ قرن چراغ روضه‌اش روشن مانده
🔸
حسینیهٔ سادات اخوی با قدمت حدود ۲۰۰ سال یکی از اولین و قدیمی‌ترین تکایای تهران است که توسط حاج سید ابراهیم تقوی معروف به «اخوی» در زمان فتحعلی شاه قاجار  احداث شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/444283" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444282">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رژیم صهیونیستی بار دیگر آتش‌بس لبنان را نقض کرد
🔹
یدیعوت آحارانوت به نقل از ارتش اسرائیل خبر داد که رژیم صهیونیستی امروز برای دومین بار آتش‌بس را نقض کرده است.
🔹
طبق این گزارش، سخنگوی ارتش اسرائیل اعلام کرد که نظامیان صهیونیست اقدام به تیراندازی علیه یک بولدوزر و یک موتورسیکلت در ارتفاعات علی الطاهر کرده‌اند.
🔸
ساعتی پیش ارتش اشغالگر از نقض مجدد آتش‌بس و تیراندازی در جنوب لبنان خبر داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/444282" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-fnBf4I_MxtGimcIB3BCkptBZk8qsyZev5oycq12OrurLTkEteIvjt7fu4yPxGGu5Rs6vVrAit3Ab2kVmg1bSAb4aF5vcrn-bY5DDSfopJkqzOx8YElRSJpjZLELCMcziK10eK3beqExD2wWkhpDUl8f6J6AA1QBfw3QhaMlhFnCoQhFWOJqCX8FoZQTL4M1T16BujWJgYHxDk9U8QqGDw1e_kiE2mZ6cMqmxrT-aWeJZdl9RA4PLr1ocRuj4AOxfBo2PGASEBk7-wVJM4SyjoG21QHt00Qpw91Dos9cXUDnPePxnxbauZUAG0pGrtOfya9uvHJUUUa9nw-9xur0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ بازیکن تیم ملی در آستانهٔ محرومیت
🔹
احسان حاج صفی و سعید عزت‌اللهی به ترتیب مقابل نیوزیلند و بلژیک با کارت زرد داور مواجه شدند.
🔹
اگر این اتفاق برای آنها در بازی پیش‌رو تکرار شود و ایران به مرحلهٔ بعدی راه یابد، در بازی یک شانزدهم نهایی غایب خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/444281" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444280">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f3309b0c.mp4?token=NRcUUWBAUqz9v5Vw6XKPT69VU7X9rxyJTDlTqSUV5tagHANSWWJbshouaKHquwIqrYE1q_RkCIzVxopzFwb1hHGh7iIal4NAvfcwUGa7PqL6Q3W3Ysg9ihxJiNdCTx00y3yK9TtjuhkICjOpMkD5JasfBjb3-gokU7DQqlKLubcFTAGHrWEJojWOO-9_UNvZbxTAJKvnFASD12X6J7KJinRD37HYzKUjPT3vHPhwq02LSj1-vN-rWxYWKPm5z-9ks0psKfuubv-msyz5qBhvD_AAkertQ3sbbsVpnRALb7wVimmge1ybMNjx2M7Dh8m2fDqr3Qf4z1STKWFMqmFLdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f3309b0c.mp4?token=NRcUUWBAUqz9v5Vw6XKPT69VU7X9rxyJTDlTqSUV5tagHANSWWJbshouaKHquwIqrYE1q_RkCIzVxopzFwb1hHGh7iIal4NAvfcwUGa7PqL6Q3W3Ysg9ihxJiNdCTx00y3yK9TtjuhkICjOpMkD5JasfBjb3-gokU7DQqlKLubcFTAGHrWEJojWOO-9_UNvZbxTAJKvnFASD12X6J7KJinRD37HYzKUjPT3vHPhwq02LSj1-vN-rWxYWKPm5z-9ks0psKfuubv-msyz5qBhvD_AAkertQ3sbbsVpnRALb7wVimmge1ybMNjx2M7Dh8m2fDqr3Qf4z1STKWFMqmFLdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواپیمای پزشکیان با اسکورت ۶ جنگندۀ ارتش پاکستان به اسلام‌آباد رفت  @Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/444280" target="_blank">📅 17:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444279">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e10d465c1.mp4?token=CKkPkbkv6651Nctp8sFBOm6LOOUO0upgC6OwpfzQJFsb7X3sfffy8VnSM-MmT9DHyRhl63GXK8vyIUTrZ1-t7OvsP7Nw91lhw7zMEqmtb_k8M5CwiZHo0obm178zSmFeMWiqMvnha9H33eSCyYmGuL7LIOmRjlBcLJ8N-BGthJc3GXpQQrbX8IZXINkvhWfIhloKmBrIrxzqdo3WsTf90ZKe7XVMdQFBA2DTD7jMdmxpNOcBEbcyXaaBCA7ooBfDIs72fdsHjX1hBm7V_swW5IPEg-TQnGEbB6rAJgQ9chKu9A1rtzu1zt6zk60cjZs638fRRCpZHHcNP-FP6vq6Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e10d465c1.mp4?token=CKkPkbkv6651Nctp8sFBOm6LOOUO0upgC6OwpfzQJFsb7X3sfffy8VnSM-MmT9DHyRhl63GXK8vyIUTrZ1-t7OvsP7Nw91lhw7zMEqmtb_k8M5CwiZHo0obm178zSmFeMWiqMvnha9H33eSCyYmGuL7LIOmRjlBcLJ8N-BGthJc3GXpQQrbX8IZXINkvhWfIhloKmBrIrxzqdo3WsTf90ZKe7XVMdQFBA2DTD7jMdmxpNOcBEbcyXaaBCA7ooBfDIs72fdsHjX1hBm7V_swW5IPEg-TQnGEbB6rAJgQ9chKu9A1rtzu1zt6zk60cjZs638fRRCpZHHcNP-FP6vq6Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم باشکوه یوم‌العباس در زنجان
🔸
حسینیۀ اعظم زنجان در جریان جنگ اخیر هدف حملۀ آمریکا و رژیم صهیونیستی قرار گرفته بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/444279" target="_blank">📅 17:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444273">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHThmRnDHYdL8su-jPeEsqKKMAjO6YZPWGcBsFKhE-X9MA_mYYH8RQOcVbuYLKzcvUnY4EHUwTKmXgsC0vm-dD-eG1dbfJVlNNS_MTJuvpTzwRsZlUYxpv8Dv-SBOPURUFH7YwYa6dCyJn2bcXvsksXSxmi67FVf19t56f9_nz39V9SYROLHW1uH7m_8EYtDaXVli_gxf0_0h1B-rxH-sqMVsrbYKxmfaT1gwstY9YccTxsJ178orkOMIkEjnRYx0SLcURU74vD0bBcMdTIDAnkON76DQG6QjtPyHiQyPqpg7RNjSBZ8JrZhzJqh1TetPi5B7-Eg0Fjg16VWKIz3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jayetwU7BDA54v9HeSB8eL-8Yy7HfGy1Un7kXDzMbVNPGs2k6JK2YNIhhPS__ORWhC5KcdOiEQLDjZ6ndROOFUo4D5IQiY0OyuzrXhSJy_pNERFc3NvBCnhBMGatN988YKQpqD4RWUic-Gp6SqmkLnNm0sHtfSADIfxjtHLCW5JRLh8jSxQgxDMAAoLX4XsySUHOQpMAJyi8_gSoFEvs1VHtP2SbvfL9rhrD_oqxsdvDPmZ-k_VruY7NHoZ7o8MpZufBLehqhN889ImnqYT86qf51sRY9aRKcL1MOcL1ttBdPOyx8-yNVSevujpAccHP_7e0YdK7ej-fhYaCDHjS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhSUrM7NOJX8wljIYURBWQDtlX6uImdY56GnrbXXP94IE9jt93SQupYigidnLFSt_wTqa3MCsDymf7tHNq5O8U4wAaDdyvyZjqYPK8q6IUX2JYo1Gc3aplWPim7hAYa-b3wqeLMGqK-uu8haaBuVHTMXE23bDfqt8XGyINVIHfqlrjVgBDgy9Br_dE1I5yLprPA7K5C83AyaoStvvZkGHljSzqv8CtOTwW4b0GFtEWP-4oiQLQWFqZ8wpE3gOruFv06sgiVNqdkbkKtzNYQ4X0aNyTQnCDwY8cEdVnVmuKlLRRBw0MZpjbBk1ojiXmGdl2Jnq5SS1yOVTmnegR-OeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwA_Hzn-9dls05H8bEyrjNxmab9udlxBL6GPMb6k6KeujRtLH3nfxi3cXB4mMTXSlwTPoUech0kVB0XSu3dSNgbjaRrYgPy2BqPkc5at-8Z4BoVRFpSofafgrhbLr3V1AVLganNA3aqoq79lHkQMxy1BhE3N3m3JMibK9pFB2nRbwe6OVsKHpxsCBu9-LjPk_w_L6PHEM4EH4Nf0JSEFvgqw6Ymz7QloSjL2j0Yb6cqqKSQWJSO3uauOmy959aSYIaIVxsOKpcWu_DQ0Gd3r1q-1XBgnk5twUAuB4xnC6OHec_sZfix6O8xm6lrCQv1bAlR7aZ8N0pYXXs4TYa-Thg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuNHZOqZphE1m4ipp_lQJF2mkdQnjX5IyAPw4kn_A-LuSF-KVt3Z4JFkFa5L6ZY7d-BHXnHoskiCfUKarCdPnNgbiP4jaeHtSRsleJJNn_sd_e3kXFr-vdQQdDntLPmR5aXLirx8xrmmkTBnEALhSM4BgH-pmX61IUNPYiWLyqhdNIDnfIUQUWXayOZECAB_D1HC9yHI0c7Royfcx-GKELRtcjwdwNP67Ar3Bci8HqcMVM3-OChsEoZxMnv23kG4zUy5H6_2L-jHmyqPOJsYdxDh0Mtut12OuYSEWwaf8GbADjmK0XihgPyYSPCjhoifjRnz4pQKJz6VQ28L0VbLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NK1-gYWFA4qRlLZq0NnKvduQxAjBHj52xyGNZVUxZSsviu2VG9dayMKmoKcrLAqlo6TLf38ucjgCKaIDYRuNDGa4_bNURV16aeXletBldz-5kGcnKBshbKE32z3S98XjZMcStAhNcnZSePYAc34tsTLLcxsn8Le-bFyfBXYGZvKkKdvae1qq292cLb6-Hp70A5SBmT7362mgDBQeC88GgrL8amkAU9pSGYHKzAi-n7VNiyRTBNsHzGoUXcyt_NagcLiZ15dv25wCWtu6BpuqmApC-Q1GCTkgGFiHO0Am_Gkz1lRwg5zABLUBKVxa-_J86coq3BAlgkjs_4Dqd0G73g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری زیر سقف‌های قاجاری
🔸
حسینیۀ امینی‌ها با بیش از ۱۸۰ سال قدمت، این روزها صحنۀ برگزاری آیین‌های سنتی محرم است.
عکس:
میثم ملکی
@Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/444273" target="_blank">📅 16:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444272">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJl3EkHhq-Iqw5M2DviQWAveO61h345RuxjHwS_FlUDD5S5LTbc2uzL33Fhqwp-aTdnhCTc5Cc4EryRgOpkxZaUOxBifwjJ1jrFfM49rg0rUbdyv43d0k1oV0XVsyhQ3eWmI773c_6njtuejZaFOrP2gb_s1iXUTaC-UFNTAmsHqcmsy-C0yvgv_CUXfitj656aL2AW2tPa9pjFKCSfqy51sSuhv0mHXnj81RYW_3BUaZmSKoypSkeCIwaoyhTUSP0ABfPyTvfeoLpg5qdUKvRQDajgDvbrh0anaLA2Zu-3RQ28u6o5s3Nj8PY5W32JohOJX9EwJe8ExGjF-9O0XeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویری از مشتِ گره‌کرده شهید تنگسیری در لحظه شهادت
استوری فرزند شهید تنگسیری در شب تاسوعای حسینی
@Fars_plus
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/444272" target="_blank">📅 16:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444271">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrmYs1B-_YYcIFZ94r1nrH1x55WEnklqgYpM9E9nsl2Z-JpAcj5-LPcQLWYB772cM9nXAEpSWZqX9mwDTAXfN9MJh2mVUp4pfoJ5YWkc2xs87Q2VEO6zwTrSyRLx2i6mq9YWFOcZwl7Fo_ptjZ55BYfCNVmwLeLTpKf-Jq2wSqD_-7h8s0uaUJm9nQuxKI1m3NNmsHX3OOZRecMpsnlT-VsJgXi65LuX7C_pmJBKiVwjXLdPumUUV7jLsRRItuF8E-2EKxwK8VSI1Y7Y5L5Ug3BwpnoY0rWkYQ-ZYufhn2NfU9FFfS9xQWmJXrYi3VZ-UTdRZl_7uhhIRz9LC_HlRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران و مصر با سوت داور فینال جام جهانی
🔹
با اعلام فیفا، سیمون مارسینیاک لهستانی قضاوت دیدار ایران مقابل مصر در دور سوم مرحلهٔ گروهی جام جهانی ۲۰۲۶ را قضاوت خواهد کرد.
🔸
این داور فینال جام جهانی ۲۰۲۲ بین آرژانتین و فرانسه را سوت زده است‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/444271" target="_blank">📅 16:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444270">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc9eacfb2.mp4?token=JauDC5JVqOt-2JE54saEiAAvwhR9MSiAPyOrbR28mV-1E8qDLzIliGsnKIvMMQgPJuD7Cjxu-iUoi25KNCaTM71lvn39DozEM2JyDscR8kkdYgtu0dkematMP9DHIZ3OZNe9pHHDbzmPvDGA1Ohp9Wo6g0t4BS3HZLzVHDY-cMu71yEDJsWuy4I802-XDNtkPFMPAlw7q48upyUtyva1jiFvS-UW6l_XEHnvjSLe5AW3CGgKh5Cgdw83MZ64OXqw4__EsQhINkRyVL7U1CMs6uIyVGIcgoboIo8Tecq4pFDxNsX6mUVmptUcHae4BibpXIyXYD1_iXcPYMbWc9oCSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc9eacfb2.mp4?token=JauDC5JVqOt-2JE54saEiAAvwhR9MSiAPyOrbR28mV-1E8qDLzIliGsnKIvMMQgPJuD7Cjxu-iUoi25KNCaTM71lvn39DozEM2JyDscR8kkdYgtu0dkematMP9DHIZ3OZNe9pHHDbzmPvDGA1Ohp9Wo6g0t4BS3HZLzVHDY-cMu71yEDJsWuy4I802-XDNtkPFMPAlw7q48upyUtyva1jiFvS-UW6l_XEHnvjSLe5AW3CGgKh5Cgdw83MZ64OXqw4__EsQhINkRyVL7U1CMs6uIyVGIcgoboIo8Tecq4pFDxNsX6mUVmptUcHae4BibpXIyXYD1_iXcPYMbWc9oCSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در ارتفاعات «کوهمره سرخی» در شیراز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/444270" target="_blank">📅 16:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444269">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
انفجار در سلیمانیه عراق
🔹
منابع خبری گزارش دادند صدای چند انفجار در سلیمانیه عراق شنیده شده است.
🔹
هنوز علت انفجار ها مشخص نیست.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/444269" target="_blank">📅 16:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444268">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caecdbf25f.mp4?token=gsbn4Dg78ANEf3xbN0yL2ogL3HpDK5KE8gVqx9N3gWBbXj3EPVW3q4X-21bVORL2w3gs2oTeRKh-yOG8x9W_XDv2esdP68fU1YQ05g_-Rso9_KarYngs8SktwADvX5YCmL3MGMF1zjlFAYFaF4VRAtNhmrMUlo3GW7PxFOfkxzVrlyWd8VYDodF4nm1uBnvmUh14yMNcqkiBcnnL9Jj0uqT5I3pzKEnfodo6N9tajIqR37fzCQcwdR1zG41LQ1gP1BwEsCcMgLFKMUgTzJiA31V721X7vjh9U9_GBYuN1Lmx3TLQjPMEeniF8SGSY158Q3EvTV-SB9UzBbWuvLPPug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caecdbf25f.mp4?token=gsbn4Dg78ANEf3xbN0yL2ogL3HpDK5KE8gVqx9N3gWBbXj3EPVW3q4X-21bVORL2w3gs2oTeRKh-yOG8x9W_XDv2esdP68fU1YQ05g_-Rso9_KarYngs8SktwADvX5YCmL3MGMF1zjlFAYFaF4VRAtNhmrMUlo3GW7PxFOfkxzVrlyWd8VYDodF4nm1uBnvmUh14yMNcqkiBcnnL9Jj0uqT5I3pzKEnfodo6N9tajIqR37fzCQcwdR1zG41LQ1gP1BwEsCcMgLFKMUgTzJiA31V721X7vjh9U9_GBYuN1Lmx3TLQjPMEeniF8SGSY158Q3EvTV-SB9UzBbWuvLPPug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آزادراه شهید شوشتری چطور شرق تهران را از ترافیک نجات می‌دهد؟
🔹
رئیس کمیته عمران شورای شهر تهران: آزادراه شهید شوشتری که به بزرگراه شهید یاسینی منتهی می‌شود، می‌تواند حدود ۳۰ درصد از ترافیک بزرگراه بسیج و بخشی از بار ترافیکی شرق تهران را کاهش دهد.
🔹
پس‌از…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444268" target="_blank">📅 16:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444267">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5af1d6630.mp4?token=PQlOw3S6QWWiWh236m5P003WI_BK9gXv250LG2Ey2Uia3CjfaFs4_r48vltGI23afWmN9DrDIiG8hZF3ZlR4Kf6Smr1bWZagS9GTWLARrHDAsSTedAi88PFm2QRIEk6oJ_YN77AXehyP6-FfGewrIxU4v8SSbM1NxPtBB16V-lAg618zhj64akhWxxeOqRCYax1r1n_NT2xlvvtsUrWrc_RE3xjime2ruThTIxaMkgPOa_GcorceNe_YpycEWnFRDy18oMg4U3ki72GIcRAwNELdPKgGkSi8A5lqEz2eXwuFIVljDC5IZ5wveM-D5NZkEUJaaqkxsrprC-aEZdM7cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5af1d6630.mp4?token=PQlOw3S6QWWiWh236m5P003WI_BK9gXv250LG2Ey2Uia3CjfaFs4_r48vltGI23afWmN9DrDIiG8hZF3ZlR4Kf6Smr1bWZagS9GTWLARrHDAsSTedAi88PFm2QRIEk6oJ_YN77AXehyP6-FfGewrIxU4v8SSbM1NxPtBB16V-lAg618zhj64akhWxxeOqRCYax1r1n_NT2xlvvtsUrWrc_RE3xjime2ruThTIxaMkgPOa_GcorceNe_YpycEWnFRDy18oMg4U3ki72GIcRAwNELdPKgGkSi8A5lqEz2eXwuFIVljDC5IZ5wveM-D5NZkEUJaaqkxsrprC-aEZdM7cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مقایسۀ رفتار آمریکا با دنیا و ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/444267" target="_blank">📅 16:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfco_D_SfJnW-2AVNkpZun3YxPuXNRC9nfHWfoj5QLNmchUAPBZ5ryFeWtHHxcEoFIS9vCBO_sjX7DM0I1AqL5Gowxkyre5XJWNtQUPdBydqXm-z9s3HBe2GVsyKjPqmyYiN6eu5uylfgcy-UyI1JnmRsR22jp99T1IQsp4_zwQLpEpFrBEmpfZs_m3Pz-G43jlZUI61P_bq4ywApULh5HfhNWpvzmUTIngaXrh9Lltf4NX0YYT3YVzh6WvR8lHe8C2b7iOQux8pJA7On4TXhgBgZfcZ3bUecUemIhZLabnsHbTtQuDMnvWOMj56lkrvyzwkJDK96FL4v7WLJKy69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاهای جدید ترامپ در مورد مذاکرات
🔹
ترامپ ادعا کرد که علی‌رغم تکذیبیه‌ها و بیانیه‌های رسمی، ایران به‌طور کامل با بالاترین سطح از بازرسی‌های هسته‌ای برای آینده‌ای نامحدود موافقت کرده است.
🔹
او مدعی شد که این تعهد، ضامن «صداقت هسته‌ای» ایران خواهد بود و درصورت عدم پذیرش آن، مذاکرات ادامه نمی‌یافت.
🔹
ترامپ در ادامهٔ اظهارات خود مدعی شد که براساس این امتیازات و دیگر توافقات، موافقت کرده است تا تنگه هرمز باز بماند و محاصرهٔ دریایی بیشتری اعمال نشود.
🔹
ترامپ همچنین مدعی شد دارایی‌هایی که آمریکا آزاد می‌کند، به یک حساب امانی تحت کنترل مطلق آمریکا واریز خواهد شد تا منحصراً برای خرید اقلام کشاورزی مانند ذرت، گندم و سویا از کشاورزان آمریکایی و تجهیزات پزشکی مصرف شود. سخنگوی وزارت خارجه و رئیس بانک مرکزی پیش از این صراحتاً این ادعا را تکذیب کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444266" target="_blank">📅 16:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444265">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6739fc2cb5.mp4?token=Rdpsap4NJH-9rD7OoPqNHxMnITrAdJpXlbMQCDUnqao8Lg2AwtMF2c9T077tBGOKzX06InYTMsT1D4oEIfpT5V6lpZ7omf3TaWND0gor2NnhWYWHNFKBcFRsDIe7dGOnsf73jdHCxOTpoA8nu3WLLNN7nDmGPIiaXZd47gW852wC5oTypKurxBdv6YKctYQM4UftEBiC4Z0pxStd3YyvboBdD8OIz4NHSBMRTeo_l5U380xH-koDrwmpuca4q-0xdF2dqSQaTKEB_CwGCcjLHloKU0h3yDmSUP916dj5RKlbow7R2Lef3r_SR6T2T4en0dfePR9PhuLOYLYuaLrWVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6739fc2cb5.mp4?token=Rdpsap4NJH-9rD7OoPqNHxMnITrAdJpXlbMQCDUnqao8Lg2AwtMF2c9T077tBGOKzX06InYTMsT1D4oEIfpT5V6lpZ7omf3TaWND0gor2NnhWYWHNFKBcFRsDIe7dGOnsf73jdHCxOTpoA8nu3WLLNN7nDmGPIiaXZd47gW852wC5oTypKurxBdv6YKctYQM4UftEBiC4Z0pxStd3YyvboBdD8OIz4NHSBMRTeo_l5U380xH-koDrwmpuca4q-0xdF2dqSQaTKEB_CwGCcjLHloKU0h3yDmSUP916dj5RKlbow7R2Lef3r_SR6T2T4en0dfePR9PhuLOYLYuaLrWVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان وارد اسلام‌آباد شد
🔹
رئیس‌جمهور در بدو ورود با نخست‌وزیر پاکستان دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444265" target="_blank">📅 15:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444264">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1nwFdJyo-_mn8waQdoH8BIwFeKztB7kiR624EZh9TOhNggHnrPld8V06f-IdtS8kRgub5S20Vluc5P2MuloiBWlffxZB13GE5lj8iAX557gRKRgzPjI172ekmV5WVkL8StE8wwiHhyB1iDof5cdQPnPqWBqb8juti-8mpIzZK2x91egaEVXi8bRAKLf8fd-8gOg58DITKqdFZX-Hb0Vh0x7HMAKkaOYShLLglewLfdhvXi8-Jd2xVpVqT0IrfxhPb4fRh-nXhPOQNCbYDZpdrSk6tzCphTKoSkrUBKTPBCtQh1s5DgW71DnPINm1Qi3_Cw3ATKMsFKcb28kFkp6mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اعلام تعطیلی چند استان در روزهای برگزاری مراسم وداع و تشییع رهبر شهید انقلاب
🔹
براساس اعلام معاون اول رئیس‌جمهور، استان تهران در روزهای ۱۳ و ۱۴ تیر و کل کشور در روز ۱۵ تیر تعطیل خواهد بود.
🔹
همچنین استان قم در ۱۶ تیر و استان خراسان رضوی در ۱۸ تیر تعطیل اعلام…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/444264" target="_blank">📅 15:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444263">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌ حذف ادعای منتسب به پاکستان درباره برنامه موشکی ایران از خروجی آناتولی
🔹
خبرگزاری آناتولی ترکیه ادعاهای منتسب به شهباز شریف، نخست‌وزیر پاکستان درباره برنامه موشکی ایران را از خروجی خود حذف کرد.
🔹
این رسانه ساعاتی پیش‌تر در خبری مدعی شده بود که شریف گفته…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444263" target="_blank">📅 15:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444262">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
حذف ادعای منتسب به پاکستان درباره برنامه موشکی ایران از خروجی آناتولی
🔹
خبرگزاری آناتولی ترکیه ادعاهای منتسب به شهباز شریف، نخست‌وزیر پاکستان درباره برنامه موشکی ایران را از خروجی خود حذف کرد.
🔹
این رسانه ساعاتی پیش‌تر در خبری مدعی شده بود که شریف گفته مسئله موشک‌های بالیستیک در دور آینده مذاکرات تهران-واشنگتن به گفت‌وگو گذاشته خواهد شد. خبرنگار فارس ساعاتی قبل‌تر خبر آناتولی را تکذیب کرده بود.
بنابر این گزارش، مسئولان تیم مذاکره‌کننده ایرانی تأکید کرده‌اند که موضوع موشک‌ها اساساً در دستورکار مذاکرات قرار ندارد و متن منتشرشده یادداشت تفاهم‌ نیز به‌وضوح نشان می‌دهد که چنین محورهایی در دستورکار نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/444262" target="_blank">📅 15:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444261">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
وزیر ارتباطات:  تا زمان عادی‌شدن کامل شرایط بانک‌ها، خدمات مشترکان تلفن همراه و ثابت به‌دلیل پرداخت‌نشدن قبوض، قطع نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444261" target="_blank">📅 15:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444260">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
ایران و عمان توافق کردند گفت‌وگوهای خود را ادامه دهند تا دربارۀ نحوۀ ادارۀ آیندۀ کشتیرانی در تنگۀ هرمز، خدمات مرتبط و هزینه‌های آن، مطابق با استانداردهای بین‌المللی، به تفاهم برسند.
🔹
همچنین قرار شد در این زمینه با کشورهای ساحلی منطقه و سایر طرف‌های ذی‌ربط نیز رایزنی شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/444260" target="_blank">📅 15:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444259">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">منبع نظامی: فقط تعداد معینی از شناورها اجازۀ عبور از تنگه هرمز را دارند
🔹
یک منبع نظامی با اشاره به وضعیت تردد کشتی‌ها در تنگه هرمز، دربارۀ آخرین وضعیت ترددها به خبرنگار فارس گفت: براساس هماهنگی‌های انجام‌شده با نیروی دریایی سپاه، روزانه تنها تعداد معینی از شناورها مجاز به عبور از تنگه هرمز هستند.
🔹
این تعداد از شناورها به‌صورت روزانه و متناسب با شرایط، متغیر خواهد بود.
🔸
گفتنی است، در پی اقدامات خصمانۀ رژیم صهیونیستی و همچنین نقض تعهدات آمریکا در اجرای آتش‌بس، تنگه هرمز طی روزهای گذشته بسته شده بود و در این مدت هیچ‌گونه مجوزی برای عبور شناورها صادر نمی‌شد.
@Farsna
- L
ink</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/444259" target="_blank">📅 14:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444258">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4de625391c.mp4?token=dJPgVMFFV1qGnGJfEgyU7UtcpLRh3rCqp4gpi8erjSP8wu-j3t68WcwrnsE76DFs_V-D9ebKUl0Q1ibc8_l_ecePWChKLR2z1Kf0SyaHCD__3KGBGbnALftTTQRm1ZEFK6TerObFqTtBt_v7y2XinwQ8xrdv4kE8vhW23arkl3o9_RSWnFx7ByL3gGybbghVZMu90agkLxXdOF37ALoLyDtUz4_HnhYudLGtxyNzhfv-QBoaXzxPu57vgxslxQlVDoTtrZQ3Hn_H_Z5KdQlAX7RNAR4lft9fheXY3OokB1MUz8_feUklZlsf2HRkLR6xk_1oJmextET7wq--imVIkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4de625391c.mp4?token=dJPgVMFFV1qGnGJfEgyU7UtcpLRh3rCqp4gpi8erjSP8wu-j3t68WcwrnsE76DFs_V-D9ebKUl0Q1ibc8_l_ecePWChKLR2z1Kf0SyaHCD__3KGBGbnALftTTQRm1ZEFK6TerObFqTtBt_v7y2XinwQ8xrdv4kE8vhW23arkl3o9_RSWnFx7ByL3gGybbghVZMu90agkLxXdOF37ALoLyDtUz4_HnhYudLGtxyNzhfv-QBoaXzxPu57vgxslxQlVDoTtrZQ3Hn_H_Z5KdQlAX7RNAR4lft9fheXY3OokB1MUz8_feUklZlsf2HRkLR6xk_1oJmextET7wq--imVIkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار و رایزنی قالیباف با سلطان عمان در مسقط با دستور کار ترتیبات مدیریت جدید تنگۀ هرمز  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444258" target="_blank">📅 14:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444257">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpPsfp4IF45dthA0ujE1_6SjCqx7fiDr2ohE7KWhQNnM-UJkHVxDgYSNbUbUBPK6JJ3b062I4OxRYH6gTDT06zwO96aWKFGH5NN2AIZK5OlDf1iCIPO_bCTyj5F4pN7qS4SHwVAE1zf2szi1wSWADeIG8SqcsLfoi_Qvx_jVim9fAV5AoCpXiPhZfHdRwzpRO3xNDTAq5CQmRa9AVTrv4Z4B_ktszzvoSEaF9cG-YarWLr4dmaJ5bMiHzXNlC72B_Ugeq7fpoMXA6sFiUKIBDRWDOPeMcomPbXCyNjw-Qz3wRRAqk8QCRUILDKhW4KKRXQ5Uh5_84Z-zw3YsAQBWNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر پوردستان: آمادهٔ عملیات پیش‌دستانه هستیم
🔹
رئیس مرکز تحقیقات راهبردی ارتش: در دکترین تهاجمی، عملیات پیش‌دستانه نیز تعریف شده است و چنانچه مصلحت نظام ایجاب کند، ممکن است با انجام عملیات‌های پیش‌دستانه در عرصه‌های ناشناخته، دشمن را به‌شدت غافلگیر کنیم.
🔹
نیروهای مسلح هنوز بخش مهمی از توانمندی‌های خود را عملیاتی نکرده‌اند و دشمن می‌داند که در صورت ارتکاب هرگونه خطایی، با پاسخی فراتر از مرزها و تنگهٔ هرمز مواجه خواهد شد.
🔹
در یک ‌ماه اخیر، ما چند نوبت تا پای جنگ با رژیم صهیونیستی رفتیم؛ لانچرها آماده و دست‌ها روی ماشه بود تا در صورت عدم عقب‌نشینی اسرائیل، جنگ آغاز شود.
🔹
تهدیدات قاطع ایران سبب شد تا آمریکا برای جلوگیری از گسترش جنگ، به رژیم صهیونیستی برای توقف تجاوزات به جنوب لبنان فشار بیاورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/444257" target="_blank">📅 14:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444256">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc369d335.mp4?token=epkEnYiqkSPuT1kImdrmHlZOSMooLS-MyyzMbZjsltp65nEqFlQgxXdd03reMPxNgKEW4VUZQYM57jV5h0wDAtQHFraYq9ETLC4ToRaXmoFS7SuuUl03BYQ-wG2Z7O1Dvep889yo6vtT0mD8gd2KGgf_702RBXB8z_3p3qrA6e-2DlNLgQSkB8asqKjcApXbcX0Q8fnk7yLSVFx8ieWMHahIOcsgc_uskErk_LpGCC6D4Y-198rksY8FFCNg3eUcOL4LARQW-LlPeOVCISrdtk2GRQE5zB77GAiDKM5jl50HXUfG6-L7b8oEczIi4nfW9qqQuQCwnKDViqzjzcDwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc369d335.mp4?token=epkEnYiqkSPuT1kImdrmHlZOSMooLS-MyyzMbZjsltp65nEqFlQgxXdd03reMPxNgKEW4VUZQYM57jV5h0wDAtQHFraYq9ETLC4ToRaXmoFS7SuuUl03BYQ-wG2Z7O1Dvep889yo6vtT0mD8gd2KGgf_702RBXB8z_3p3qrA6e-2DlNLgQSkB8asqKjcApXbcX0Q8fnk7yLSVFx8ieWMHahIOcsgc_uskErk_LpGCC6D4Y-198rksY8FFCNg3eUcOL4LARQW-LlPeOVCISrdtk2GRQE5zB77GAiDKM5jl50HXUfG6-L7b8oEczIi4nfW9qqQuQCwnKDViqzjzcDwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجۀ روسیه: باید شرمنده باشیم که نتوانسته‌ایم مسئله فلسطین را حل کنیم
🔹
نتانیاهو درباره «اسرائیل بزرگ‌» صحبت کرده. اگر این طرح‌ها به نتیجه برسند، تشکیل یک کشور فلسطینی یکپارچه و پیوسته از نظر جغرافیایی عملاً ناممکن خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444256" target="_blank">📅 14:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444255">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f3421a74a.mp4?token=HfFaVQvDFr5_PVDVWF387yrCwJbOUiXg3TsbhtN1ejOgqL6jyzZMmpVD8s6k0EqEyTDhMiLQszY_toO1R4EnmBBk529u7b6MdX43pj31ssxFrU1P7hxvp2GtI5JvD90GmVGcxUvUSFEQqG0DkS4CEOFisVAJNqV0YiVWgWXZc53cOfBtNvt81hHsKGIt54-WcblJqzQmkllJ0S1T9a-J3vLduZa2yi-spjPXhHYsMDGjUhNiDB-MnUonSwjhkAR8T5_UGcCJWEYkPJXXyg6DvaRCLPd9n-x1CiPBdgmxxw1tYz_gN1PNPbF8MsXxqkmepP-qfuvqnPF4M1OeYF0PHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f3421a74a.mp4?token=HfFaVQvDFr5_PVDVWF387yrCwJbOUiXg3TsbhtN1ejOgqL6jyzZMmpVD8s6k0EqEyTDhMiLQszY_toO1R4EnmBBk529u7b6MdX43pj31ssxFrU1P7hxvp2GtI5JvD90GmVGcxUvUSFEQqG0DkS4CEOFisVAJNqV0YiVWgWXZc53cOfBtNvt81hHsKGIt54-WcblJqzQmkllJ0S1T9a-J3vLduZa2yi-spjPXhHYsMDGjUhNiDB-MnUonSwjhkAR8T5_UGcCJWEYkPJXXyg6DvaRCLPd9n-x1CiPBdgmxxw1tYz_gN1PNPbF8MsXxqkmepP-qfuvqnPF4M1OeYF0PHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ احتمال تعطیلی ۳ روزۀ تهران در روزهای تشییع رهبر شهید انقلاب
🔸
سردار حسن‌زاده: در خصوص تعطیلی ۳ روزۀ تهران در مراسم وداع و تشییع رهبر شهید انقلاب پیشنهادهایی ارائه دادیم و در صورت تصویب، موضوع رسما اعلام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/444255" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444254">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI0_t0kgCdDs2_IG076Jdv1t_9oUBvMLbn2PFYZ0YSH5pR69HNvg9f7jTl3ys8nBkOF2txsv96WKyxnC59oh5mzJodeU8NwJisxOElZJ0LOpifxSVua0uQ3KnWH0LVmV-_SaHL5vHAMkI8DNz0Qy5Tbhgmit0VdQ8zNlArT__SVud7VgaB7C2niLOIHYTYVXtztkhPXLIFfu_3442pOub0yhEFiafTFCj91PYHqrUtb5L21cpUAMZiGk7L3v1NpSUo0mdrRHnZuJKcuzmwLSG_ymPriMY3aXxNlPQ_M1Jv34OyhJLMf-YytakrJy96NdWeAXJc4mZQGiBsGfXVpxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی پیش‌از ورود پزشکیان وارد پاکستان شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/444254" target="_blank">📅 14:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444253">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiFn8V70wbmLLUAAcEdCrunzu4Zv4Lxw8xQpbv_u9XeqxAQbC4pQ71msRXbteU1_1pZxZ8HuzuqyvOGQPdCWfG5eiheF-4hwstKCD8ycDnhw1b5dmMynbUKNvKh33L_T2rak1HeBzWyX1chqsHUtlYZCQg63JYSH4LFSPR7MaLT62xox9y7wgpm65S3ydbsr9LAe1xyL1_RdcrCqf7x2AlBwOWl2a4RyhDzc63eN598DljIeFUq0Dnr0ECL_8IHTpOzqsqc3bCZfBzR14wTVEKgQ-oMpRNPYfegahOMj4EQl3wyRq3HfIDPfBi0ohTdmQvkP7Nc5BPt4q2wlH56kXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان راهی پاکستان شد
🔹
رئیس‌جمهور به‌منظور گرامیداشت یاد و خاطره شهدای جنگ تحمیلی اخیر، به‌ویژه ۱۶۸ دانش‌آموز شهید مدرسه میناب که در پی حملات آمریکا و رژیم صهیونیستی به شهادت رسیدند، با هواپیمای ویژه «میناب ۱۶۸» عازم پاکستان شد.
🔹
پزشکیان پیش از عزیمت به…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/444253" target="_blank">📅 14:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444252">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3TNJsudsiPO0f0oHwomEG5RW5Rnj2xiakhSJn9XVMwaqRjbV3rQnph6hOv840k7ORsytpgVTrya2UVa-mkVWq-ymBkeG7pWch051OxdJHYm8HykNsRy3Jv1N7hIPmGT7OjxvTgcHN3X1yqzglp3lFcSwIs1pWgxYUjj-ZJmBh6_CXEP9PwNaE1rlxaQtwlUwMQ2I_nbtuH2xMaLTwnjFgYfm5rzsM2pzgOadluC98tKYqA7bFANnLKQ_BhDDyIs-7PxWo9e82vItwSREozYbrEdR0-SjAzK2aCxn-99J22wMahxznrq1WoWclCqTyc70MPQ9NvkNXsGnh13laF9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین: عراقچی یکشنبه به عراق می‌رود
🔸
عراقچی هم‌اکنون همراه قالیباف در عمان حضور دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/444252" target="_blank">📅 13:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444251">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌ توضیح بانک مرکزی درخصوص اختلال در عملیات ۴ بانک
🔹
بانک مرکزی: اختلال در خدمات ۴ بانک ملی، صادرات، تجارت و توسعه صادرات درپی یک حمله سایبری به زیرساخت‌های ارتباطی این بانک‌ها ایجاد شده است.
🔹
خدمات پایه مبتنی بر کارت با استفاده از روش‌های جایگزین دوباره در…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/444251" target="_blank">📅 13:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
یک شهید و ۲ زخمی در تیراندازی نظامیان اسرائیلی به شهروندان لبنانی
🔹
سازمان امداد و نجات لبنان خبر داد که نظامیان اشغالگر اسرائیلی در محله «الدیر» در شهرک «النبطیه الفوقا» به‌سمت تعدادی از اهالی تیراندازی کرده‌اند که در این جنایت یکی از غیرنظامیان به شهادت رسیده و ۲ نفر دیگر مجروح شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/444250" target="_blank">📅 13:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444249">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoDZ6HR4nX_rZZBSlwbn_-kj_NIDmXZ9RhC5k3vgR8dV0zf9ogi3HX08enePELsg8TGOQErH_S13K1km5KKiQLvpBzoThvPgllv5Um0GaeeXy1xzE7fKOl_DUdZYx7gBHh_ukIXSQz8vMoH_zg6f-7CjjenlVWeJWVqUIf14cRLuBilVbxfvKZ-C-v9vZ3g-eYMAqT9TO4vDsHPp3Aui8WF3FXYQuBpfxteQalJsQCnuYNgu8ECdsxK8MLgvhBFVzwBmc_WS2dLZ_Xotojcnrp8hTPiCqU-czM--MmZ3d2_Z7cBY-3Z7R9cY3OWF8gzO4o2Gj_KKsn39N3Asf36vNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از مجاهدین خلق تا اپوزیسیون امروز؛ یک خط ثابت در حاشیه جام جهانی
🔹
«هنوز مشخص نیست چرا سازمان مجاهدین خلق هزاران نفر از هواداران خود را به این مسابقه فرستاده بود.» این بخشی از گزارش میدل ایست درباره دیدار ایران و آمریکا در جام جهانی ۱۹۹۸ است.
🔹
فیفا در طول مسابقات حمل هرگونه نماد و پلاکارد سیاسی به ورزشگاه‌ها را ممنوع کرده بود و تماشاگران برای ورود باید از چندین ایست بازرسی عبور می‌کردند. با این حال، هواداران مجاهدین خلق موفق شدند برخی بنرها را مخفیانه وارد ورزشگاه کنند و پس از استقرار در جایگاه خود، با درآوردن کت‌هایشان، تی‌شرت‌هایی را که تصاویر رهبران این سازمان روی آن‌ها چاپ شده بود، به نمایش بگذارند.
🔹
اکنون و در رقابت‌های جام جهانی ۲۰۲۶ نیز  همان رویکرد همچنان ادامه دارد؛ رویکردی که به جای حمایت از تیم ملی در یک رویداد جهانی، تلاش می‌کند عرصه ورزش را به میدان تسویه‌حساب‌های سیاسی تبدیل کند.
🔹
تلاش جریان‌های مخالف جمهوری اسلامی برای استفاده از فضای جام جهانی سابقه‌ای چند دهه‌ای دارد، اما این تلاش‌ها عمدتاً در قالب اقداماتی نمادین و محدود باقی مانده است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/444249" target="_blank">📅 12:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444248">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fd326b9a.mp4?token=Z0BolmmNuVwPxNSwIqTXmutfHAZYn9e2sTcmD9vSFYiigPlxkilN5Xa0zZ-JcNvOMxhMtOQOAumAWTbUos90mvNFYjW3cNj7FeBR9uP_UVMInu9R8pXCP0vwo5_OWPZ6niJCivnP7bvp_7CH8jqquYqykxn9DJaChojL0X23m38KB3AyXaznCnxvB5fgdBbUpEA1F1923zpwLTgWOjpd9bb4EiQaXT2CaFiIpr7ulx98ZeonsJZTRA8PUqBbwQJ3tsKz5x7w8blTdemGLnQRqyleRRC5UwpaqZcsje_Qyf55BAUaujGN0M1VtHOldpdThXLK0RoxZdW0R-Xy5sqh0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fd326b9a.mp4?token=Z0BolmmNuVwPxNSwIqTXmutfHAZYn9e2sTcmD9vSFYiigPlxkilN5Xa0zZ-JcNvOMxhMtOQOAumAWTbUos90mvNFYjW3cNj7FeBR9uP_UVMInu9R8pXCP0vwo5_OWPZ6niJCivnP7bvp_7CH8jqquYqykxn9DJaChojL0X23m38KB3AyXaznCnxvB5fgdBbUpEA1F1923zpwLTgWOjpd9bb4EiQaXT2CaFiIpr7ulx98ZeonsJZTRA8PUqBbwQJ3tsKz5x7w8blTdemGLnQRqyleRRC5UwpaqZcsje_Qyf55BAUaujGN0M1VtHOldpdThXLK0RoxZdW0R-Xy5sqh0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: قالیباف قرار است به چین سفر کند؛ زمان سفر هنوز مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444248" target="_blank">📅 12:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444247">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_OflVkXJBAAKuaKM3qFtbjb99_0gKziv7RjyC9Z-QcW0jjP5V3jENtaqgSs7qlRyGjQYf8hYNrRNRk98zPBeh80JCFpT73Wt38PFJLMDdaT6pALhHcTGYWKgMrymD-iSn5-Y63etk5FwvtAlUUKQ3Dvo-g9nK0binbTAYT5Kzil3msov8yJSyNactmRZFWwyILYwXUslaVXiOp5P4Q_zLN8_CEx1z75DgEvvZgvL9GzlP5LqKHTb792PHbdU1qJ0LQQhyZRtXclTY8AUYWSk2knCv_0Ro7VBA1Qxu_oZlqrAyZoxMvuqhWvG3vdj999Puz_z-89T-1bWJQT29C56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با جهش ۸۸ هزار واحدی به ۵ میلیون و ۱۶۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444247" target="_blank">📅 12:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444246">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0qHXEyNqldFfSbdKe8HzzO-VJGldgN8ElfCzXGM1HlDpUraJ_nHWoJ_6NuqK3jd31NLgEwZ4Zva3ZVC5Ukdvj-kLkxnYTpYhm07YFGB6y_wP7y-zXb2KKpcmFKU09Oo_NzdE2sR2xVsIWbcjU_ACpoaQcLS4gBvfXCnDiby6oYMW1-bGWlaQXsQHQkmjNxP-yslUj3USPYDR7hUEtO9nkoKLL06--5PC4Xuvftjk99UR5dkYJs1Pl_9oWMbo6IYARrz6gG967Ji5Lzb7uLiGRXUGBaj5OYoWvoNNNEaxXvUE7aZob7j8rgjUuUBSY6zC6uOvF8SCoviArKBU0JULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این علامت‌ها خبر از سرطان رودهٔ بزرگ می دهند
🔹
سرطان رودهٔ بزرگ یکی از شایع‌ترین سرطان‌هاست که معمولا در مراحل اولیه بدون علامت است، اما برخی نشانه‌ها می‌توانند زنگ خطر باشند.
علائم هشداردهندهٔ این بیماری چیست؟
🔸
تغییر مداوم در اجابت مزاج
🔸
خون‌ریزی مقعدی
🔸
درد و نفخ شکم
🔸
احساس تخلیهٔ ناقص روده
🔸
ضعف یا خستگی مداوم
🔸
کاهش وزن ناخواسته
چطور پیشگیری کنیم؟
🔹
انجام غربال‌گری منظم از ۴۵ سالگی
🔹
تغذیهٔ سالم
🔹
فعالیت بدنی
🔹
کنترل وزن
🔹
پرهیز از دخانیات و الکل
🔹
تشخیص زودهنگام سرطان رودهٔ بزرگ می‌تواند شانس درمان را به‌میزان قابل‌توجهی افزایش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444246" target="_blank">📅 12:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444245">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91a9021eb2.mp4?token=Nmnfco_7s5gJy4ZcyHA-m0mDvcvAQxJm-5CvL4jZciNtrOyPjP3ziWGQgQBuBmfOpQ1MZiAXWU_9EyegMTCfP2lMJdcN4PlNWq88wPP4XnVke9d5Pi2lEleUzDHhBfFMEcgZZEYzusZgehZLRGcpJV3LdB-lfRGczpnh3a0e5bdz0x2xneFwnA0atqlb3_mCVfPQri3M9biua5X2CUsOfNk4ZKkIlR8mC2WfnpNS48go06nIKSQwUK1G6r5w6ATiuSEjy281sTz-3RR2Hs2xKlGfadPqdLdNK-g8IKuJbWOYK-LalCm352JZLj1-zmkNVvD_Z7jMoYrrDuPxs7k2RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91a9021eb2.mp4?token=Nmnfco_7s5gJy4ZcyHA-m0mDvcvAQxJm-5CvL4jZciNtrOyPjP3ziWGQgQBuBmfOpQ1MZiAXWU_9EyegMTCfP2lMJdcN4PlNWq88wPP4XnVke9d5Pi2lEleUzDHhBfFMEcgZZEYzusZgehZLRGcpJV3LdB-lfRGczpnh3a0e5bdz0x2xneFwnA0atqlb3_mCVfPQri3M9biua5X2CUsOfNk4ZKkIlR8mC2WfnpNS48go06nIKSQwUK1G6r5w6ATiuSEjy281sTz-3RR2Hs2xKlGfadPqdLdNK-g8IKuJbWOYK-LalCm352JZLj1-zmkNVvD_Z7jMoYrrDuPxs7k2RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز جلسات ایران و عمان دربارۀ مدیریت جدید تنگۀ هرمز
🔹
هیئت مذاکره‌کنندۀ ایران پس از پایان مذاکرات سوئیس راهی عمان شد و گفت‌وگوها دربارۀ ترتیبات جدید تنگۀ هرمز را در مسقط آغاز کرد.
🔹
قالیباف، عراقچی و اعضای هیئت ایرانی همزمان با سلطان عمان دیدار کردند. تنگۀ…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444245" target="_blank">📅 12:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444238">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CH_ToTkFUjcdVDEhy3GbOHB_IdNKCcK_A_hyTrfZSSMa8qXXg6ZVzlpBrv488aI8bbeN5bCvHWNHiQZbwx_5fps3l2CdciReseIN_SuArFIfki0782Ds5aAdjv7kQ-JZrG8981Z5-SY_0UtG_n4AnOm4-9YS6nq6J8S24D75zDf4LPfCvHGKdZaqGBfu7GjN44ovhN1acH3A3AYzy2h0cDivOP8xhfAg-d3QbTI8L3WzirHX1Z6XzW4Yu45GseSh1jvJrqDKAwvbCMeTvQBh54BjBQGG-fVRoRfxiXg5jzfMs5Z5nZHBH1Jmo4qY-WEtHHvnr-wbDFEF6cl-2ApxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z01RwB4xek_2cK4FIKEIQPMbD0sMo8a5-IN3LTRWbSjCw5WcSZJ-UHBWqjCFCj0EKajaoFZkrMsYFqeLFlksNx5Fg0lb1hT_ApzE5A24BOqoaBRFN18KEV0A0ZGT8d88yEhhfq0WfJREQfWUWIfp6SpU7LtTGv0vI2QUQ4vBaBu7qj-KpmNekd9WwLr1qJPT59XMw78a8EIQozU_isUmUYy9Vgqi1PUVHiZkLpAiJ7tyaZVwBpOjqM-ZatGUUzx--1sCUNw3a8mocUZw2UYX3G7DBev94ntAbFIKQO8BFz_fOkYHpugMte34e6fqqwYk38fAaXQKKRLP-Bi4ygFNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQnpqN9bbCAq320QdGXwptmJa0W7rTnvC5aLe1HpPv2yLw_2fPlU2EkpdiLLAYD1DtAUXmNNY_NgAtzpv6Y2ZM1YE5xAqoC-66bN-i9fraCnpUL24o6-dMoeD7KewsH8C85KW99HGIg9aMqL2dPKEwQ0vujHXe7EI4l-DoT8lsw6anubWRaCg92tIF8HaayoGWo3nvVkZC45x8-4vclHqpi1KkZSFSWnfCU0xOTFrtBYzxo5m8C4ByO6s5_T_yIR_wxkni3YaiHcB6ZLqTmd00BT_EvQHtEcZzYBIMPyIPK4XbVLfKKjCfApqvwP_JqCo3LHmi7gozT8_xgrDxfNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hso1i2iZ107T_SRoSRrjuRwRGtP9GSnyYmy5Kgm-TSzbcX_M-0q-yNknEzMw_a83Y_6pigquCv_YvMWsGYKDEeTS5SbeBPoA11ZJS1UBpMdDK0Cj2iAKXiZ7_b7o8wNE2whED0jqlzDixzL3twjnQev2BMsZMW6cPoVhBSv2Z5fZMqWF2nhM2tuIav4i2dnEwZIqdtNm5-7KZKFw6hTQNIVao4F3aKPOuNSmsF68fsw_oQ6SRjElF1Ux-vT_0ZmVHsgPsrPnIPkwsh84I-GxsfDY90BGQRoYlFOcZQ5WPAJ8gY4PgQsC6_GBIuXyayBuvKn0CRulDseZaas_ZzZrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBulbmXLSTb8m7mxZrZ8zqDIdyj95UPhpSzpVhnQmId2aIUPe6KFXtbjqxRpUjCGdYIHEdhZmCo2xS4SATVoECp_926H7lP5XrBtAyZvoC56kMidqLsYgSwxu5xIBYGZW7TsUxm3V8yGLFxQAUJJKCpzATkdllIrojfh7dlvHZfwflo8rDTeDgpEZ3cCFZPYcQWQOAreZ0dNzqNtoZLeBzUtNuYR9zEOY_8SEX7IhQuBXJTmWlxubxceLKhhWafFrpPEx2Cd1lsjvWrA5pH9dH5HOVVUTphbwr82R-iMk7fVQICfP-DqKdUQuZXTO8UPaVmDt8nYG1_k4hIfW8XC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QePH2mTLG-gr_shZliwaZvoW-1hIhpLgkaCRZ1838Ek97wupdjDrYfGVP_kcl0SSEM-FbVtEGLHaYYW_l29Uw1x_LkrJazSxBwGvOdrkpq9bHdKr2mCVK0NyutDrGCoPDoR1H5slIDir4Xc458qkJQwdw-Wwn65tHxAZRcLC0OBjfoiSfDDCfwiBpo__GapmmWDOhWSPoDoGmQqNy0qLSBk_10n1vJigQLYGNp0PpYo49y7qWoyz5wks6COzmc70kxFE9ff2pW8x9YjHf8M0e0iIXz4YuuJnkUou5SwAlVPWczg5jYflQVdQti6IAgcZWj_PLEJi2BhyfFqwedXIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgReAsU1yy5UfSk3LA-JxSyxF_jFHSp0vbYs2_-6H0T1gJhkgtR38meDoNuNdtW0CyuwDd2hySYuYKvzzM9LIGuLv-cmLY25-n1ehZDhLdAFfT4Qn-J3O7c94FUmY5JLmet6LJHYUAsGAYcuDX5DgfkZge0tGomaxCiEF2JD-UF35IAStUEh9nn1kzNff5-Dn1TqKfTOE4s6CEgLW4qWMQcmGaR4nqPImZ_jWPPf-UIPNebeLTD_vqOr4I04fyy3Rmd61FUUgg6CVTWWWHI3sRoQWrWBSLed5DSnxJuh8TM-lZBwJZDyFCg1cONab_njU_L_jZLgo_szKzP0XJxt1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور شهردار تهران در خبرگزاری فارس
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444238" target="_blank">📅 11:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444237">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a13e62494.mp4?token=ql3qY5MfYvGZ668AzCBYUc5L8XnNQ0uOUzgfcNPXGS_h1GKlvqN4oPKK85fPxlnfC1JbaXSoDjeFbE05GDhfptoYI44_Wk0F8Ik1bOcmavWncAk89ytStVf03-WbpUiUO74V2FkpnrY-OOpk6HpfnJkrxURQfYZpPucFhupp7Ffy8a8aTYa4y1C69K7gTaPEGmHGOJb18xK5Su_TVvpFt3cF-ZhfuzuFirq5od4eAwYVd8kPQd_tuJT4fKGsbOuXgXypbmXHLKaNOV9rUNlwqj-346P1eOfQ6pzA-OyWLadu0mpJhsrxPatFfLjWHXXVLNTVji6wJRR0hcVF3OZnaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a13e62494.mp4?token=ql3qY5MfYvGZ668AzCBYUc5L8XnNQ0uOUzgfcNPXGS_h1GKlvqN4oPKK85fPxlnfC1JbaXSoDjeFbE05GDhfptoYI44_Wk0F8Ik1bOcmavWncAk89ytStVf03-WbpUiUO74V2FkpnrY-OOpk6HpfnJkrxURQfYZpPucFhupp7Ffy8a8aTYa4y1C69K7gTaPEGmHGOJb18xK5Su_TVvpFt3cF-ZhfuzuFirq5od4eAwYVd8kPQd_tuJT4fKGsbOuXgXypbmXHLKaNOV9rUNlwqj-346P1eOfQ6pzA-OyWLadu0mpJhsrxPatFfLjWHXXVLNTVji6wJRR0hcVF3OZnaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: برای ما مهم این است که به دارایی‌های مسدودشدهٔ ایرانیان دسترسی داشته باشیم؛ جزئیات آن به ما مربوط نیست و این جزو تعهدات آمریکاست.
🔹
خروج خبرنگاران از محل مذاکرات سوئیس به این دلیل بود که ما برای کار رسانه‌ای نرفته بودیم؛ ما برای مطالبهٔ حقوق‌مان رفته بودیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/444237" target="_blank">📅 11:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444236">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d4781cf4.mp4?token=FTQnYZQjSGDAiTp4PAv9-FEZwqRVBumFJVi4P-arJuQl6j2kc82KiTY0ewHhvXzavoitCf1KzEvn06-EO8Mix-u0RZVQI0MEhnITYFBoVqO8mOQpHwWw8Y5sEcplXZsMcmUAHgK10V9MTAY45Y_de4gpgQ1Ig2CNr3O1IxLUrFKipCzrlgtT0GIX_DX6vMxM1r254sylMgenf-5_4A9o0gizzQRG-JiopTK0xOPt15U6sa4M3t3c4oj4-gCMNNPGIT9tjETIiyUv8zj6BEoPZgiaHs4_jcUr3qtdFM8evzw3dJH84M66b7TybTJDlR2FFfVnw2JTMsXZxYKLBvTYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d4781cf4.mp4?token=FTQnYZQjSGDAiTp4PAv9-FEZwqRVBumFJVi4P-arJuQl6j2kc82KiTY0ewHhvXzavoitCf1KzEvn06-EO8Mix-u0RZVQI0MEhnITYFBoVqO8mOQpHwWw8Y5sEcplXZsMcmUAHgK10V9MTAY45Y_de4gpgQ1Ig2CNr3O1IxLUrFKipCzrlgtT0GIX_DX6vMxM1r254sylMgenf-5_4A9o0gizzQRG-JiopTK0xOPt15U6sa4M3t3c4oj4-gCMNNPGIT9tjETIiyUv8zj6BEoPZgiaHs4_jcUr3qtdFM8evzw3dJH84M66b7TybTJDlR2FFfVnw2JTMsXZxYKLBvTYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: توانمندی دفاعی ایران مطلقاً موضوع هیچ گفت‌وگویی نبوده و نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444236" target="_blank">📅 11:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444235">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502e49ac2f.mp4?token=qWr-KtCZ7NLFoEUWYlUkuHnBgm0z8fJNY4urssMjx_Lauxl1z1473CXPiiDBtWFGamzldilz9QtVfPGHSXSK6gANZdszZkxadfXCELrVXFDFLtl4mFhRmNKaOGmNLim0so4cWxOmyIrR4UfhvTcSmMpa_oKJHsuBDP1fMppptBER5biNYjOwdm9-u-TEIH-g3L4oERXisMq1UxV0WjeuaA4iGcICjAV1SUflpWNBTsZeFoFX43rTDEE8AQTAcYC5o9MXeFApFpiZBBgQmsvrPfnfZuZ2_NIma0CbSt6IfvYI3b2uVBcljaMg7g1__dWhF9tWBN7tk-hNURV18t88ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502e49ac2f.mp4?token=qWr-KtCZ7NLFoEUWYlUkuHnBgm0z8fJNY4urssMjx_Lauxl1z1473CXPiiDBtWFGamzldilz9QtVfPGHSXSK6gANZdszZkxadfXCELrVXFDFLtl4mFhRmNKaOGmNLim0so4cWxOmyIrR4UfhvTcSmMpa_oKJHsuBDP1fMppptBER5biNYjOwdm9-u-TEIH-g3L4oERXisMq1UxV0WjeuaA4iGcICjAV1SUflpWNBTsZeFoFX43rTDEE8AQTAcYC5o9MXeFApFpiZBBgQmsvrPfnfZuZ2_NIma0CbSt6IfvYI3b2uVBcljaMg7g1__dWhF9tWBN7tk-hNURV18t88ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
کمی تهدید وجود داشت، کمی هم گله و شکایت، اما در نهایت، مذاکرات ادامه پیدا کرد و ما به پیشرفت‌های بزرگی رسیدیم.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444235" target="_blank">📅 11:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444234">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9d4619ca.mp4?token=Wtx-_GhGa9TkTN37cH9TaN3V9CgqHid5ozLDZwipAPK0d32NXqvuLw9p7_LWg0zxwjxb_Zv2ZQHHkiTLMeymuiagF8WBisE2L9HK2WIIXbwPpXqdLiqeVfCMwSNz9mwRcTqhCS0ZENjlcYOOM7bZcjg32kPhGUZBJYpeNb_fZj7B0URBOD7vNQV3ZcRAQLRatshcIpHSX8CSL2l4w7LJVHIystkxEqtE2j012QjnAfIOaL_DzMl7BQmtR5A3YBqxQeEGhpUpwKeaIH-n6t8Uu5GprU4G1L344tUgO7IbGgl2d3FzWFUev874yBuKtHUFBdACbXrjXBGkqlfTsXOoqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9d4619ca.mp4?token=Wtx-_GhGa9TkTN37cH9TaN3V9CgqHid5ozLDZwipAPK0d32NXqvuLw9p7_LWg0zxwjxb_Zv2ZQHHkiTLMeymuiagF8WBisE2L9HK2WIIXbwPpXqdLiqeVfCMwSNz9mwRcTqhCS0ZENjlcYOOM7bZcjg32kPhGUZBJYpeNb_fZj7B0URBOD7vNQV3ZcRAQLRatshcIpHSX8CSL2l4w7LJVHIystkxEqtE2j012QjnAfIOaL_DzMl7BQmtR5A3YBqxQeEGhpUpwKeaIH-n6t8Uu5GprU4G1L344tUgO7IbGgl2d3FzWFUev874yBuKtHUFBdACbXrjXBGkqlfTsXOoqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند
🔹
سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.
🔹
آنچه به آن دست یافتیم، از نظر من یک توافق کلاسیکِ به سبک ترامپ…</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/444234" target="_blank">📅 11:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444233">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfbfbc0c5.mp4?token=JKFLyYtLscPj6w776uJw0ES0R3C9PMKfJimH2vnmyNwZT9i3BtutZLW1bNh6DATX_zOM8nUkfEjtkmduqxZ9psSeQG8c4uT0l9af03msCnHuxd9lE_8dQNL5P3-hGk--HJcdf_xrChqZWwkDeMYuc-FWGlxqCCB-UpWIrrq9gCq3-7WJ9A7wCtVclKF68tsbiVa0rGCq29ZdyzNU9iFgkKQM91StH-8gfuVn5IaaxVuqsO4oPW2YaZRZ5vCm8Uk00ww3_ZAzLg7dSL8NFek2X2UnRWClClsnc0S_1Rp2pctZD3RK2QWJVrS89JuwXM9ZDB9hqDLgW9-nxKYVAb3mkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfbfbc0c5.mp4?token=JKFLyYtLscPj6w776uJw0ES0R3C9PMKfJimH2vnmyNwZT9i3BtutZLW1bNh6DATX_zOM8nUkfEjtkmduqxZ9psSeQG8c4uT0l9af03msCnHuxd9lE_8dQNL5P3-hGk--HJcdf_xrChqZWwkDeMYuc-FWGlxqCCB-UpWIrrq9gCq3-7WJ9A7wCtVclKF68tsbiVa0rGCq29ZdyzNU9iFgkKQM91StH-8gfuVn5IaaxVuqsO4oPW2YaZRZ5vCm8Uk00ww3_ZAzLg7dSL8NFek2X2UnRWClClsnc0S_1Rp2pctZD3RK2QWJVrS89JuwXM9ZDB9hqDLgW9-nxKYVAb3mkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ونس مدعی شد که «ایران بازگشت بازرسان آژانس بین‌المللی انرژی اتمی به این کشور را پذیرفته است».  @Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/444233" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444232">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh58wGa82UZZ0VHzd-T9_AmyNFbSiqM1LqD6YHXdhq0gvOuLVQ1eQY-MB-t_M4QnU22bsNXtTdJIec6pGUOlGcZkpDK77ry4vAWgyzwkE94RW6qmQuFBpz0hSaiQp54vzJ6BqJ_tR5-VDVof2cukkHszxKvgLIBVT4EYohbiz4uFzwg4_fxgEIIwLHEJ3N3ndHVgB8WegWypOb8fVhDfRMz58UxJD-NmA2QsskmMWmcaR6zvBMElKXaMWQGdkvjpC_WqSlHU8ja0-9KjrAIRMUbmHbuPi3w-ZqZvnUQN572LjCGLOAaO1k_DL_3u0MOsaHD5mXa4pd2hyw31WWjL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک مرزبان در مریوان
🔹
دانیال نوریان از پرسنل مرزبانی مریوان، در حین پاسداری از مرزهای کشور در پاسگاه انجیران به درجهٔ رفیع شهادت نائل آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/444232" target="_blank">📅 11:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444231">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia48Ch0681atVxRFbK48zVDRTS-aCyiFtlOFyRDAgOLoU3Rfn9psLj45QWqVMZsR9EqORXl9SM7OibSlsW4pSgi8F8HqoB439L9LBUjsq62s27ZAnLbBJkdRXmZ18btFMxGb65WYDDkHYMQ81vOeuLXLM3000t2wj9zSV7RJ3yCW-UjpzyiFsxX6PIOsnOSeteksBf6vU44yYgyxJIphacqGrTzmQWs3ZUT6KGkCBr0iLGoptjaHAs3UnjTf_1tgiLizVVoeSnfzKUfwYA0O4t6nolVXiQe5_50rram7vGET0rF6PqYUxbPho8q2tdjZNFzgkYAI91u3E4nJK_I4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزادراه تهران-شمال یک‌طرفه شد
🔹
پلیس‌راه البرز: با توجه به شرایط ترافیک سنگین، تردد وسیلهٔ نقلیه از کرج و آزادراه تهران-شمال به‌سمت مازندران یک‌طرفه شده و تردد از مرزن‌آباد به‌سمت کرج و تهران ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/444231" target="_blank">📅 11:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444230">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urcyV48D0gKMADZv4aJLBVAfbWcGIb16x-ODuVPBm96ZArZ4RyFrk09r9tyzT2M5qYOnYs1dBsTAF2DriCin3uNUs9iTz2Em5pIzfxAeTn8KfGitZ_J0AbIlrE-WvrVuUlYT3Zti5foF7ppNh_KG4Ax60757Et7ObdUbTsdX2yXgPNwUPOLlC1ushpgNb6RebLX65uN9Vbxtyh8TR6KxubN4IjmTrO0NZGRZDtgmvrt4q_e_IllKQqqv9XzWznldhQWoNMAZyBLmfV2dPBXLglOWYas2GOC8Y3wVvoBwQ18Vjg-amkeOvkzBDMu8RTRjbfN54BnVLl0tD9BVseANcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز جلسات ایران و عمان دربارۀ مدیریت جدید تنگۀ هرمز
🔹
هیئت مذاکره‌کنندۀ ایران پس از پایان مذاکرات سوئیس راهی عمان شد و گفت‌وگوها دربارۀ ترتیبات جدید تنگۀ هرمز را در مسقط آغاز کرد.
🔹
قالیباف، عراقچی و اعضای هیئت ایرانی همزمان با سلطان عمان دیدار کردند. تنگۀ هرمز و شرایط جدید حاکم بر این آبراه بین‌المللی از محورهای اصلی این رایزنی‌ها بود.
🔹
آنچه از روند مذاکرات برمی‌آید، تأکید طرف ایرانی بر این موضوع است که مدیریت تنگۀ هرمز و شرایط عبورومرور در آن به وضعیت پیش از تجاوز آمریکا و رژیم صهیونیستی بازنخواهد گشت و ترتیبات جدید در این زمینه در حال بررسی است.
🔹
تنها جمهوری اسلامی ایران و عمان به‌عنوان دو کشور دارای سواحل تنگۀ هرمز، مسئول تعیین و اجرای ترتیبات مربوط به عبور‌ومرور در این آبراه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/444230" target="_blank">📅 11:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444229">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چادرملو در آستانۀ انصراف از بازی با پرسپولیس
🔹
باشگاه چادرملو هنوز تمرینات آماده‌سازی خود را آغاز نکرده و همین موضوع باعث شده تردیدهای جدی دربارۀ حضور این تیم در دیدار با پرسپولیس به‌وجود بیاید.
🔹
گمانه‌زنی‌ها از آن حکایت دارد که چادرملو تمایلی به حضور در…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/444229" target="_blank">📅 10:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444222">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTmQvSfatbnVLRlhG6NMVaa5JNXXuokbx4Udi_WNfk35vS0SrsRbLm3SuXcJyIg5x6Y4oOlMT0DUqrELo9Ee2-hmDt8nlEGV6JyEl4fCXRfWP2HCmlnio5iYg_jucFCDUDpaRQtQPYZTiWxTn2d2qkWvwmvNGabDBsOZt0mLXWJ0GiSs5bLMWPDZGOdIyFeUHWWXbOHMzJYn4_voAB3HOlqW49rWZsCWgLWOEamtDxzHER8FpK3h8Ayp8FE1EuDE8buU-5oVnCkP-nUSuPnDeo_tF6Wt6IlbcDr341s-Yrs2H3cEqR2XTmFuesvBrfh8Z_GQO_SV5bBirA_vyssNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAN7uYBc4ueYObuZtyF4SW5JK9265w1_-K8cygizfB4fQ07nKCN71hvt3rOwpPRsTQO_vbNjBS0XnZwB8erR8g6WK9mTHczAblihXC2KguGncYrhWNwtmN8qbb780Ynv-9Yg8gsnKCGm1rJoz6BZWMIP62uDggt97NHGeIk-kfX7yRK3nFOKMNDK3NMPLFDO1eCPu7vVMF7rAcjJUdkPjcgjywbtq92HsIY5TqwVPY1NU5ogGHsRVhhCTFaK20n-yq7ENKdygfOvUSpQdqJV6B49GEdGlHOTsq4-9s1F-3maZBPLcxBruYYIX2Ce64sS8z6fx5pTcb6HjbxLzWAfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMx1UDY8LT_F-8w7GYjbFTTGpXAc69YmtbxTgD5lokzU_Kb6pVr6odDWrGNsUwtiCP7_UR_KQnIh87l0TN01rCx4nX5DpP4xVgDfGhDRRVGI8ulGovqsJ4fH7CF9e8kaYhdjx_LtHuAfBXB8WdX3m24L8U2d72--RprvziHZ5ncLxIcRzCX0XQd9Et7JCSVtgjEAfpctX4k5RBeGCqQURKaEDrV6JBhJJg5EJkT2VnyMfakX2AatKtzJtLG5d9R3pb8iCYox3O2gSpZCcjnYfS05WfH-YA-DWQ1UD45M6rxcANeUnQ42ohvp3_WFYODFHKFH0ovP2QabtM4eUkbXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJLujWf5QMpoID3onU17fa5V-ChZEftT7f21dVtFqd2Url06VTql6a1Ft1yf3dfrZl_UxViuW4C04fOs2i-UsT3OPy56gIaH22k03f-TjFUtK_OY6QpMj0takzvXHl_WbIvC7JDuedgzVm_xr_Pwvg3eMEn1YSZPE5B0DUPMPQgEGJGjoqi2dueJZ5Fb8LDh2PVm7ZBfBgoPbAFx9W92lC2XBcQ_ZtVPCaHeIX1_d7o6rPF9T7ru6g1RB9LghfUlc7hyaCJDwS-c5zmY3Hi8TJMIR7RYXsPcWxoEKXpKxhbThc78H-VYtVUdWf5k7AlLqKWZNljFUD9J9N3xFFzlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lb_l_84ZBYhLWnbmPTv9a5vqkXzlh3WLuKEb89Zx4xRkcyUg0nfk3TlTtgj-LozgIKzoIejVT8CJwRZm8JA4skvj076aK6JO9Dp2XFG0GYslc-Mms4G77gjYez96v3JezgGgCs58z8TLsTaGL15GNeuVEcecZ-83gaanMQq5jl3nw9dlLtIT5vc7nyQ-2AQyGkKsMcOyPcbWSxY06Jh1ZwIwR_HDmqwfDOOF8jGXjgLwX2hn3XT-vKYGDG4Wm1fyvWrsowtMmBj16zKpGCDay9RFGgfOAwfK5VjYK0ngGgtKO7C3eRjp4Upt1MiPNvADL_2qFXn64rGSHuYpLQRCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRCJFmOlzQteNt-o6obbFPfFVSH7D0kJoGNOHHOrR5WxrE8FiyFQFLklpZnmRT4eVRBcT7ixKo6xoFSLLl5vSMZj3QA3JcdwhdN6OvZeeh_UKtmuggRALyW_yZE0oa0W_n10LK9vIM2XuxqAWlm-YO-2vspzAo1APeNWbdUKAipmHdfaEMNZN1wi-dkPag3Ts13PM-cPrRGtORKwMMf0QqktVuxahRfysG3e3VE9RbSi2P3AKReZFsJTyO5xESx3Ihi6_fcgBCYKTQf8UlIZZ6z3ESU9bKO-S0MQXOEOdOkMp3utVp-DcyVkQ_RGh7HD376538aBOJHpxsNpFF-tcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YeC49fujz5q-P7Q1kp6QBO76yxCkCZD3JOPPHY0Ljl6B2lk03knsLgbiCvtj9KeV4TwK8Cq93w-U35ouskKyhdyjanK2DtNbx7eAxMv-tu4UhxSx6bIforbPayyEmNGO5kX7X5NUkKm_mnC_KRMV9LTG6fY2Jdo1YQpGqIkck_C-IxGulG5QuOex0P5uVAiTnaiH7FW03c_G0lQUzx8LDoygmctvDPhsalPzWFZMJbKjkKAE6seKLfr90HbkoUZvKLMlaHUwzvvz3XzMUvSz5o60HrIONyjadTkcQCvvd2Tm6D2fDMXokArWHPP7eKbEozswukbwJ_acVhQENeH5NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین «شاه حسین‌گویان» در باغ رضوان ارومیه
عکس:
محمدمهدی فتحی
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/444222" target="_blank">📅 10:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444221">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUW9fpvwJT8boHFn3zoyN4RMCWaVu5YXdkGugMnNyA_M4g7arhwTDRJPxZ5MLQB9fg6nTajBOepkcLj7kp7Pi4IJxWaKCedUVUFR7FfkvJLUbeaazMEDDRWHJX8ris59NiedewuULWrgmqhXOTRDPosd3kTkfGyLW03G7kP_l8pzGurRosfOv9XH7_bAIbILNFPmnK7nCn4lZOO-T9IxcA8re8mBVrFji_DkpTRyQouUUjok2w3qlP6spaDEGsXaBUq2lvIzcE6sXDZorVCDMr3c4aFdA_T7S8Rnqbone4qu5KgTlDTMci9VDtVyQR2GnNLZpU5QA5pddniRY6SJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مدیرکل روابط عمومی دفتر ریاست‌جمهوری در گفت‌وگو با فارس: رئیس‌جمهور فردا به پاکستان سفر می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/444221" target="_blank">📅 10:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444220">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKYagInETz0oLE5l3_8e8qgLqdtgbOsZzYzxHCQhMoE2E9Cn31FKH-wleSwxqsO-PBgdCLgpNLMQ3f58NTABkeWS8zUvKyZumztsuaeFLgR0KRFdJsIRBCSHcTkDAzpFxX5TIpVocQz2zuTOXJoJdWbvKi29JAfFX_i5C3F8Sxj0HtDLGOJO5tReILAnWDIaHAnViAHA_bqwAPteb2SIj9KXf8VSAnQDjzhZFUu78ei7FYcu6_aA8Og1_SWf8Z-Mj57R0nTB_ep92NrolpcmXyO3an7Vn63q8ZdLrHza4RO-U36_wmpHutZWztWRKpcdw9l60sirIyp2OevITZKRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز نام‌نویسی در سی‌وسومین دورۀ آموزش‌های رسانه‌ای باشگاه توانا
🔹
زمان ثبت‌نام: یک تا ۲۰ تیر
🔹
هزینۀ دوره: با حمایت تشویقی و فرهنگی خبرگزاری فارس فقط ۵۰۰ هزار تومان
🔹
سامانۀ ثبت‌نام:
tavana.news
🔹
پشتیبانی و مشاوره کارشناس باشگاه توانا: ۰۲۱۴۲۰۸۲۹۴۳
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/444220" target="_blank">📅 10:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444218">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqaEkkOgPcAVlfDFyNJh_cOYfpN-5HlgK2Wa5iPO6lI6Lp2pyQqBC9Ndh83OYuvny4eUnJY2kdltnNCK1Y4YtH_5vUH3NHkr_hsGqySsI8Xw0NrlWE0xsx4SnzjRFyN3GJ5RcKgceMfOt2gHHqLOXg_EkyzU0oUI5MfYtRpYusUCZA8cEK4cLep77IqeI2HaL88IcMoJY7Ezc4VcZexZqhDHtUFqop-asr1Jd09YGi893bYZSl5E1mKEHR-V04KHtum7g4EnTuxot6Cnl8ovW6CYMiW9T_nKx6nu_RjMhwQ8S4VBzVIbKWUpaEthjOt_rvJC0Fq1eLyVI0qhQ2Wbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efNh5mgoQQ_E0v8HGXNVTl9x5whuF2ohVzWxUZbSRcegLEidDEWF-HYcUbXWT-TpfEqpIiB6oIJ90rJnUl9Z2BTNX-okBxF7KMmEHTA0Uh5hJmsH7ZST6rzFooojOLBoel9Gy-oQR5qdDSMzmD2eUFh-q0FbtW88DoqBrQU4F__C1o5RlAgSOaE9HtpNVHJfEW6mQ4WVdDiOVSYxNdQKBs2ev8uL5L-oBncaqIVT-BVALLh-gtjJQYiGa2GpoSqizhDv3kwuW_kA21VKcL9fQLQqiSLatwZQyHYviIZirmjtsPYqQqqjjvPDGNQRIChyOpt5hekHrDgdnVZWoFCGMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۷ هزار دانش‌آموز خواستار تعویق امتحانات نهایی به بعد از اربعین شدند
🔹
کاربران فارس‌من در پویشی خواستار تعویق امتحانات نهایی به پس از ایام اربعین شده‌اند و گفتند: با توجه به حضور گسترده خانواده‌ها و دانش‌آموزان در مراسمات و پیاده‌روی اربعین، همزمانی امتحانات…</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/444218" target="_blank">📅 10:33 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
