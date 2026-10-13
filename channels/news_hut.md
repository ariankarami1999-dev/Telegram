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
<img src="https://cdn4.telesco.pe/file/IdrBVNgS2lgGwepqQYJQzi1rm7ssfTVDJ4zabDbc5MdCo5GysBWeosTjxEROEW4hXG63qHr5dwoggbqyuueZjOdcinI_x0WCOzd0XSBMGAs8rAyoEqtWZHCm4L2Gq017_K3I2xb_muxw5td5A_wUJuah5mifVxFipx000qjL77h6BXyX52-DzhqyXhKcXNShaeEmeA5nt4jFB5kyi_EjjV7sOXiRiY-qrp-oNy1Khas7CeJIs1euZgXevgWVP7TvVdstNNHNo-4RThr1zkeI-8Gtui0S7yAd85-jd7bNr7H4iC2e8atGFe9Rhm0x6pVu38kg_71ckJnUdSC-ZLPBXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
<hr>

<div class="tg-post" id="msg-73217">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی:
به‌زودی به غیرنظامیان هشدار خواهیم داد تا مکانی را در صنعا تخلیه کنند؛ این اقدام به منظور انجام یک عملیات ویژه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/news_hut/73217" target="_blank">📅 15:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73214">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eC9sy_GxcsNsCmA2OfnQeocR4cb3NXQ03oS9BhgMgj2FsMPgDaI0Umm0nHfDVdwwFQWx0RPooHSI_URh0og7KjMeqHad4h6XG9bHZG8ckIwVYq9UCXUd6Uz94SN9Y6esrOk1GCcwuuFvGxD86Ny94tJU6GUyYEZ2Gwf64KXOMikHf4ocqB_edrCoT0xDM6lUK0p74MhWfs-kHmUWtzYCScjjuKbPd9Ld7EMDOq8nicZu46NjcUcpKSqCCSkYDd5r8x0StWPYt5UgPVQTAVNpV_jUKkjKwbsvf1cUaH6mDjUqCrCFqMpP2Lz9zkDZ2Zj5vAdxok4xNMXhxXcKcg-JrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVlm2UwcB1IDFS0S0VK5vlNkqjab9nRnlXlGUgNpOfxxTUVZ1S3NDTSTGtUQZzu9LLpnQzNNNdCPmUDaM3-Y1TjIZ-ASvtn5qaSmXSQ_3f0ac7GpWEZRv9ACtlykF4X00cPq9Dp62cGcCtmVQCwza95ka0rm-ZJAdFf-DHb0NiytMkteBWYVecoqfYtAKVnWd_N2HKtTbSl0x_eQRj7cdQmJn5kQ5SWMcz2m3INvnvfXllO2qwlDpKjNzXEGQc-hGAElwdjMp9t0DE9hAuoUoAbKruhb1m9QN-BfgdVIoMBx7CGUoRZj0o37EK_-jwwNTVNkkqwGh9M30O1Q7o5x6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDTYBeTtlOS7m5CzLX1Kq53QEk1cE-dkSv6V6wqUkd1-4rn1EifFPjEvspV-Ele4fl0BrgesvtMqEjoeW24CO0KL3ltC0XqqysQ86ZXSUOA9nBSKE7fH2U6pSBDcu4Bc_gUHlPOH61mY7rcCGjno_-qBxcK6DQnShgx9FB6s04kkJ-pYD3y1ceo7E9CEg-eK6pUNO2rcVxajJWxTaNKlTY2vdZkf-kw3Ee1FHCVB6sJoJHYmGjnjMm5w0faluBn67nQFxlsov2PIHgDRebbfIAXIUAwib46MepHIMVFXXuVjlQQ9Z4fVKDBPUjeh8IcEDGks9ZpIg2Lwse557AggeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حدیث ستاری، مدل ۲۵ ساله ایرانی و دانشجوی دندان‌پزشکی در امارات، در مسابقات بین‌المللی زیبایی «میس گلوبال ۲۰۲۶» موفق شد دو عنوان «ملکه زیبایی خاورمیانه» و «برگزیده مردم» رو به دست بیاره.
+لباس ملی حدیث در این مسابقات با الهام از سیمرغ، پرنده افسانه‌ای ادبیات فارسی، و نمادهایی از حکومت‌های ایران باستان طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/news_hut/73214" target="_blank">📅 15:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73213">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90850a02ad.mp4?token=CFyT8aQoyBj_J04C7Kh5bdT_yjMbo4K8Y349uQYyFiN3SNRIuMmKSJsY-b7dHo8A1b_0XL30i87brfjNWwxRk8to1u5C9tbIwf9azEk2sr0TF-Pn0JgHfGDk0I9c8mlsYn41CMs2-cUnaaPW-HHcMw4OoMciD2nZGmJes2-7rkIjDQfTVG2b-KCU9RSyGUT7S4ZHR0EVsMp_1VAklToL8OVpNW_BJ1TVqdM5pFSRS-JwI1lsq6kKqPp6xW4ICyPiQYa-C7r2SmJQNQlihLydEDyi4L59KVfQWrx2n0mG7mFs39fV0SUictRZ5Dt74kXbK0jqD3ZLlxkYW5PrAOzwzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90850a02ad.mp4?token=CFyT8aQoyBj_J04C7Kh5bdT_yjMbo4K8Y349uQYyFiN3SNRIuMmKSJsY-b7dHo8A1b_0XL30i87brfjNWwxRk8to1u5C9tbIwf9azEk2sr0TF-Pn0JgHfGDk0I9c8mlsYn41CMs2-cUnaaPW-HHcMw4OoMciD2nZGmJes2-7rkIjDQfTVG2b-KCU9RSyGUT7S4ZHR0EVsMp_1VAklToL8OVpNW_BJ1TVqdM5pFSRS-JwI1lsq6kKqPp6xW4ICyPiQYa-C7r2SmJQNQlihLydEDyi4L59KVfQWrx2n0mG7mFs39fV0SUictRZ5Dt74kXbK0jqD3ZLlxkYW5PrAOzwzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرازشه شب گذشته،  در میدان انقلاب تهران علیه مسی شعار دادند  !!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/news_hut/73213" target="_blank">📅 14:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73212">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7vaKSHnTT66crwXjfT7lYv8Z--XSkVpBtlRZHcR9M5sCAdfwfoG5kyN8AS6ZMB-TlFOFvOfnuo394kAjnwgqngJiRUfVQRWH8qokpVsgbQKyqIcYn8ag_BInbF1AgKdtsy7h-9N9Zeci3zt4pONdromv-6gCNMiJO1BjV0JPiY2z_OGMrPsAC4SPaqD8YG10nK0oCzTxO-zJ8LLc1eL7WMADn3xJ_6PdLMa3Q_QOJFnqJQkRo134nADw9EfuONEs3JEFstvXad146lr2meOFPWAQrPkd2t4Qr4_nt7B1Tcnwu0akNVAyC7BlTXX-6RNxSUtLOMLn-O6Tr60hRI5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش روزنامه «هاآرتص»، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از طریق میانجی‌گری ایالات متحده به دنبال جلب موافقت عربستان سعودی برای مشارکت اسرائیل در عملیات نظامی علیه حوثی‌های یمن (انصارالله) است.
نتانیاهو این پیشنهاد را فرصتی برای تقویت روابط با ریاض و پیشبرد توافق احتمالی عادی‌سازی روابط می‌داند.
با این حال، محمد بن سلمان، ولیعهد عربستان، به دلیل نگرانی از واکنش منفی افکار عمومی در داخل پادشاهی، با مشارکت اسرائیل مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/news_hut/73212" target="_blank">📅 14:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73211">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876aa9210f.mp4?token=Kar4qf6KB2xMctl9tGUMZIcmDPfRQaUw-Nnj_NaKoAqQFSxK81oCa44egQiqmMLVLOzJXYIxxaxoHzx6Ijq7PZphhpiiuNKo7XggRZm9QHeTbZ9_UETelBRZeJMWaaH2Heq30-o5S3sJYND_hSqgyjZzeG0XIrzDoYF-FomDXxNxOG5IRtMAof5RJl5sr4riJFVBIlEsY1ykG528hJneA6SnncvSlBEnA7C32eujJDS4NcRizkSh-d_pyFwD8RxEPDwphfW8qP8rFhODAxZ4nUg6u_E-wN7DL0q7jf0wAKrkP_KPJzOdrlOYVjih0lGlrugUGsMuVVv7Lk1JRBIBCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876aa9210f.mp4?token=Kar4qf6KB2xMctl9tGUMZIcmDPfRQaUw-Nnj_NaKoAqQFSxK81oCa44egQiqmMLVLOzJXYIxxaxoHzx6Ijq7PZphhpiiuNKo7XggRZm9QHeTbZ9_UETelBRZeJMWaaH2Heq30-o5S3sJYND_hSqgyjZzeG0XIrzDoYF-FomDXxNxOG5IRtMAof5RJl5sr4riJFVBIlEsY1ykG528hJneA6SnncvSlBEnA7C32eujJDS4NcRizkSh-d_pyFwD8RxEPDwphfW8qP8rFhODAxZ4nUg6u_E-wN7DL0q7jf0wAKrkP_KPJzOdrlOYVjih0lGlrugUGsMuVVv7Lk1JRBIBCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل شرکت آب و فاضلاب استان تهران: قیمت آبی که به مشترکین ارائه می‌شود ۱۱ هزار تومان است درصورتی که قیمت تمام شده آن ۸۸ هزار تومان است؛ فاصله وحشتناک است.
@News_Hut</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/news_hut/73211" target="_blank">📅 14:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73210">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54425bdea.mp4?token=GEGuviMMOzQsbDhm3AN56-_8NZgLaih4tHPhQKvIoMZlRVxaIEYnXO_DKHdAAc5XboKuBZ2MAIPXT7tewOGLRe3NDAjjN3_eHjMbeODJSN_u5yrJKuUs_BsBH6UcB3m-O9tjVtbNu789LV1f7HX4w3xlX2o53B11X5WcvqEuRNQRd9zmnFRolOv3g-_r6WilQJkS1xSc9H2zSfmBubShiOUSLOC_lsMddrMrun1FohZmw6BQbIgaRtGWQUKhRrFuurdOx4fEZ2KT9wOevRx5odGsIVlU0skIZwz20zVKAAQx6HISqpuMboR3zQWlM-AyNOG51BvLkT2Jw0AjwN2xUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54425bdea.mp4?token=GEGuviMMOzQsbDhm3AN56-_8NZgLaih4tHPhQKvIoMZlRVxaIEYnXO_DKHdAAc5XboKuBZ2MAIPXT7tewOGLRe3NDAjjN3_eHjMbeODJSN_u5yrJKuUs_BsBH6UcB3m-O9tjVtbNu789LV1f7HX4w3xlX2o53B11X5WcvqEuRNQRd9zmnFRolOv3g-_r6WilQJkS1xSc9H2zSfmBubShiOUSLOC_lsMddrMrun1FohZmw6BQbIgaRtGWQUKhRrFuurdOx4fEZ2KT9wOevRx5odGsIVlU0skIZwz20zVKAAQx6HISqpuMboR3zQWlM-AyNOG51BvLkT2Jw0AjwN2xUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر نتانیاهو :
کشورها، حتی آنهایی که به ما حمله می‌کنند، به آرامی و پنهانی می‌گویند که رژیم جمهوری اسلامی باید سرنگون شوند، آنها ما را خفه می‌کنند.
ما مطمئن خواهیم شد که آنها(رژیم جمهوری اسلامی) سرنگون شوند. آنها سرنگون خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/news_hut/73210" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73209">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6a75e3c2.mp4?token=kwXBE3GC_zevZhMKjRLEGUK1TaEgdpQTOnVBlIy5D0i4ldaseEOmSypLGGB8K1qje2M1OtV9zYKE95BePmiDzDYIycMZodTcPBy1BtV0RapBSn6xRnP9o9qRG0VV9jukt9cIE3_yu8r62uBtH6h8MZr1IIi8lpf-vfrjz1IEcgfZZUpTQ7yyJ0tD4AutP-XgdEfvgxZDG4LPoEEJEjUbwgw5igJC6NpAWyQmTP5G3GWCrwPdBjbZrCHFy--E9L-pL0jaYF6Sv-EwNrenSzJVO3oilSd0I_-4mYnHdfDsQ7Zkj02BZbBduGnnvs5X_IS5z23e8vQV0GZ9MkqTk2nA2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6a75e3c2.mp4?token=kwXBE3GC_zevZhMKjRLEGUK1TaEgdpQTOnVBlIy5D0i4ldaseEOmSypLGGB8K1qje2M1OtV9zYKE95BePmiDzDYIycMZodTcPBy1BtV0RapBSn6xRnP9o9qRG0VV9jukt9cIE3_yu8r62uBtH6h8MZr1IIi8lpf-vfrjz1IEcgfZZUpTQ7yyJ0tD4AutP-XgdEfvgxZDG4LPoEEJEjUbwgw5igJC6NpAWyQmTP5G3GWCrwPdBjbZrCHFy--E9L-pL0jaYF6Sv-EwNrenSzJVO3oilSd0I_-4mYnHdfDsQ7Zkj02BZbBduGnnvs5X_IS5z23e8vQV0GZ9MkqTk2nA2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جالبه بدونید این ویدیو که خیلی وایرال شده یه بداهه از خواننده و طرفدارشه و بیت شعرش از قبل مشخص نبوده:
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/73209" target="_blank">📅 13:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73208">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96bc792f3.mp4?token=OIwiVqNmnBsTHG43r_MdUMvETpmLdNv3jM8Z03pIA98bQgEmzn5FGC7jeSaWDh8ZIbexwjpB-DsBG8_2ydNMokjg-VBKNxT3LKNl3YMFLpiF6_yfKc1BWLTS8G2aWH_Bl4NOCCNyar0S8JiGru70jBLq6ul44VCShi8fs9ITMogo-MkW1bIqEzdRxvx0cQVHLINWxGSS4tbSbQCHj1JE9ritnuR2eqSeT6TmvG9vn3p9mYmYAwLfzicacwh9CC7kEdPHzI6AGedAUCw8kyIvoMjujDmnXOkwuQtX_mOW5q_-KAjuAxsQj2MwkgcYSKv9C-AORMTx2aEuCacxHLu3CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96bc792f3.mp4?token=OIwiVqNmnBsTHG43r_MdUMvETpmLdNv3jM8Z03pIA98bQgEmzn5FGC7jeSaWDh8ZIbexwjpB-DsBG8_2ydNMokjg-VBKNxT3LKNl3YMFLpiF6_yfKc1BWLTS8G2aWH_Bl4NOCCNyar0S8JiGru70jBLq6ul44VCShi8fs9ITMogo-MkW1bIqEzdRxvx0cQVHLINWxGSS4tbSbQCHj1JE9ritnuR2eqSeT6TmvG9vn3p9mYmYAwLfzicacwh9CC7kEdPHzI6AGedAUCw8kyIvoMjujDmnXOkwuQtX_mOW5q_-KAjuAxsQj2MwkgcYSKv9C-AORMTx2aEuCacxHLu3CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال‌وش:درگیری در منطقه تفتان-سیستان بلوچستان بین نیروهای نظامی جمهوری اسلامی و گروه های مسلح ناشناس:
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/73208" target="_blank">📅 12:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73207">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98721d1ae5.mp4?token=KpslO5CYWeGnspCMC5MIsZwfS0S_a16YBJuHoahfIy0TC_g7SLe8d1YkggqA__8XWvm68Z5rbrhLQ_PY6D64r2QT9n8Q2feqfP38znMgyQDAWil2AN2ioOfhg9BM3TlPYIO3t5sEwRPbjPn0EHuy77dn49Erq6JkBdUX42Mw9UAsmRvnd219gqyukwPubl0WyyTsk2MS2Z7ADTO7PIE1OgDH8Nqp54GQ7KGvXGkkxGrStyF1-WF3PJ4qszuKQhlu4SRIoEBlOJiGsgDQ0_DLqFZQlbzDvcSEHIbmFGmx6qS2ZjceuHrmLsqM6bo_v0asT96QQBKPUyirqHuDezRPcRo1qZT1fGaNCu5Cyl6IFiUYAPyxbXZLds9ipJqh_LiI2ZVbu4jb7lv_GfnFAn94RPLC27bryWFeAy1tveQB2rwm0kM3ZaiAlovlYtDKIrIGt_v3xEiP2aoQAvJhivq4c59U7fIv23KxtCP9t4kRWbhgb0iVvfv7ntZ3KwgiP72DNJX0XMjkgtmP5mRjmnKFQl7GUU5Bux4wmxbZqs-nTLBH5nkkaW6gyWXQC8feifHNNh3FuNFKZVhkqnoB-nIw03xY5rwLIqBKCfGnW2p0IHJ4m8wkvUONLKd9k_a6IKyclWsxHhIHe2HR1tsj7trqMm-2LAxJbD9z_BRP_iTaVM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98721d1ae5.mp4?token=KpslO5CYWeGnspCMC5MIsZwfS0S_a16YBJuHoahfIy0TC_g7SLe8d1YkggqA__8XWvm68Z5rbrhLQ_PY6D64r2QT9n8Q2feqfP38znMgyQDAWil2AN2ioOfhg9BM3TlPYIO3t5sEwRPbjPn0EHuy77dn49Erq6JkBdUX42Mw9UAsmRvnd219gqyukwPubl0WyyTsk2MS2Z7ADTO7PIE1OgDH8Nqp54GQ7KGvXGkkxGrStyF1-WF3PJ4qszuKQhlu4SRIoEBlOJiGsgDQ0_DLqFZQlbzDvcSEHIbmFGmx6qS2ZjceuHrmLsqM6bo_v0asT96QQBKPUyirqHuDezRPcRo1qZT1fGaNCu5Cyl6IFiUYAPyxbXZLds9ipJqh_LiI2ZVbu4jb7lv_GfnFAn94RPLC27bryWFeAy1tveQB2rwm0kM3ZaiAlovlYtDKIrIGt_v3xEiP2aoQAvJhivq4c59U7fIv23KxtCP9t4kRWbhgb0iVvfv7ntZ3KwgiP72DNJX0XMjkgtmP5mRjmnKFQl7GUU5Bux4wmxbZqs-nTLBH5nkkaW6gyWXQC8feifHNNh3FuNFKZVhkqnoB-nIw03xY5rwLIqBKCfGnW2p0IHJ4m8wkvUONLKd9k_a6IKyclWsxHhIHe2HR1tsj7trqMm-2LAxJbD9z_BRP_iTaVM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرازشه شب گذشته،  در میدان انقلاب تهران علیه مسی شعار دادند  !!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/73207" target="_blank">📅 12:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73206">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be338c559.mp4?token=lJ7Ow4x2OwI3Fm9D_em5JtEoiYtqgPRlK9GsRA1gh8Doervwq0Eg3V0BvIHOi4dLn9krrXJh6D-pcrz1sbk_YrB58SWfsilm83BscSUul5J6UCadJ_AF0idlKLh9YCkZpIbpPD0w0sdD91_aO19gvE49lZrBIRy_vbCjrK1WL9ooVkWrierW6xGQ2ieH7Mg3mQ2VPwhcqxk2Jo-Amjt7XGcrrH5b664ADtOgjpwyH1Shvxj83F4UMAT_XDlETIU1Kqm8l01Y090VoCcNVRb6rSX5YvZJbSVLn1gccQPQpOwLgxhCfql7mUDqsq4Yp7fPcP5lL4q-Br8AzkNpkmyRYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be338c559.mp4?token=lJ7Ow4x2OwI3Fm9D_em5JtEoiYtqgPRlK9GsRA1gh8Doervwq0Eg3V0BvIHOi4dLn9krrXJh6D-pcrz1sbk_YrB58SWfsilm83BscSUul5J6UCadJ_AF0idlKLh9YCkZpIbpPD0w0sdD91_aO19gvE49lZrBIRy_vbCjrK1WL9ooVkWrierW6xGQ2ieH7Mg3mQ2VPwhcqxk2Jo-Amjt7XGcrrH5b664ADtOgjpwyH1Shvxj83F4UMAT_XDlETIU1Kqm8l01Y090VoCcNVRb6rSX5YvZJbSVLn1gccQPQpOwLgxhCfql7mUDqsq4Yp7fPcP5lL4q-Br8AzkNpkmyRYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عده‌ای از اراذل و اوباش سرکوبگر سپاهی و بسیجی با لباس شخصی و پرچم فلسطین و به بهانه حمایت از دانش‌آموزان فرانسوی در برابر سفارت این کشور در تهران تجمع کرده‌اند و علیه دولت فرانسه شعار می‌دهند:
«مکرون حیا کن، دانش‌آموز رو رها کن!»
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/73206" target="_blank">📅 11:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73205">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73205" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/73205" target="_blank">📅 11:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73204">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw4cPzuCVKvhBciGG-3pAWOolrsyZuukHY2p8AAZ9gT4aLJ9ttAJ2GeZgIFypJB2lpWjJWrII4XeBP8t4neqi5MdrZOc5uqhr1MV9j6H10h_vdwDNsAPORbytrUmeYsCCJqBflVKOk5z2zlRmbBZbemSNaCKyIJ_diGOVnOFSgysQUMRa4_cfpFTm8KNiRrcgWBuz1GG_lejiSjSLW5q7l36Gp-rr0g_b2xnEwrOBfybc70Si-zgIGQ2K0ncLCp7BWw4UX5cdTT3yhlHQ0MpXhQbei_-_dVwR3VG_22w42tZEpLfo5xvA3pmzv839afNGgvXw0ZECiO3oe2m4x6c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بارسلونا
🆚
گالاتاسرای،
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
🦖
گزینه پیشنهادی:
بالای ۲۸.۵ شوت در مجموع بازی (Over 28.5 Total Shots)
با
ضریب 1.64
📉
با توجه به سبک هجومی دو تیم، تمایل به خلق موقعیت و آمار شوت‌های مسابقات اخیر، انتظار داریم دیدار گالاتاسرای و بارسلونا شاهد موقعیت‌های گل‌زنی متعددی باشد.
📉
بررسی ۵ بازی اخیر هر تیم نشان می‌دهد که مجموع شوت‌های مسابقات آن‌ها به‌طور میانگین نزدیک به ۳۰ شوت بوده است. به همین دلیل، خط ۲۸.۵ شوت می‌تواند گزینه‌ای قابل بررسی برای این دیدار باشد.
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/73204" target="_blank">📅 11:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73203">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پرونده کنکور ۱۴۰۵ بسته شد /نتایج نهایی اواخر آبان اعلام می‌شود
با اتمام مهلت انتخاب رشته داوطلبان، پرونده کنکور ۱۴۰۵ بسته شد و نتایج نهایی اواخر آبان اعلام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/73203" target="_blank">📅 11:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73202">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=P1UnLQmxfoOJsoW3nIPX6zykOcg7B64a5sGqysgkjE5ushDpu1XOCC0Pzm6r264_J6Mqvt6-0rh5tAkQ7XwlHULiQcZSjs1Mo7HYevVQzgSKsV4xxUpqd2TO48xn18oaUGPAUQu8Lp53It2Ihw5UolaWPxlT10uJVNTvSjmu4mfqXhT9V2UM6DZBojOPjsT7VlVnT-42LAneFRG4925ffGvwV_JsRTgQ5Xlia_hw08TUD3mwDKMzcEMP6UzIgOjnNYQpkxlbpWvwNgnfrdyhnmqCrke2qm45zvvy-qwyijAEi-W0TQh5VVDYZl2HjFCStdy3kjiJvG3F3Ba4DUlc_zMHZq5tWOEEilqLKum-hhUKPy7n3Mr_VVCz04Oop-D37Vc_gzAiHtUid0IYwR6fPhMEV_XeGjyNSFsNwW8D6cqVdwx68NapY19Uys54n4fWD5NJWxMKqEaH7wYoUKriKhWalJMuSyOA9ppZyo70LwiMY1vV3xAOyz0QnJ90ZGEHmea9kj8CfrnbGHgCd4YXRV3fCJkMxzKm6-jP-hsvikx0iKPV5Efnkrwv6wEW8rYHFLL0DxD87ziO6O26BA-q1rE5rXszJq322e0bhNXEtY9TL1lywhv5DmgIojmUT6eQy4_tbIZXUvFrggfQkMJAJwThabvca9rTmpHwP_0aPhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=P1UnLQmxfoOJsoW3nIPX6zykOcg7B64a5sGqysgkjE5ushDpu1XOCC0Pzm6r264_J6Mqvt6-0rh5tAkQ7XwlHULiQcZSjs1Mo7HYevVQzgSKsV4xxUpqd2TO48xn18oaUGPAUQu8Lp53It2Ihw5UolaWPxlT10uJVNTvSjmu4mfqXhT9V2UM6DZBojOPjsT7VlVnT-42LAneFRG4925ffGvwV_JsRTgQ5Xlia_hw08TUD3mwDKMzcEMP6UzIgOjnNYQpkxlbpWvwNgnfrdyhnmqCrke2qm45zvvy-qwyijAEi-W0TQh5VVDYZl2HjFCStdy3kjiJvG3F3Ba4DUlc_zMHZq5tWOEEilqLKum-hhUKPy7n3Mr_VVCz04Oop-D37Vc_gzAiHtUid0IYwR6fPhMEV_XeGjyNSFsNwW8D6cqVdwx68NapY19Uys54n4fWD5NJWxMKqEaH7wYoUKriKhWalJMuSyOA9ppZyo70LwiMY1vV3xAOyz0QnJ90ZGEHmea9kj8CfrnbGHgCd4YXRV3fCJkMxzKm6-jP-hsvikx0iKPV5Efnkrwv6wEW8rYHFLL0DxD87ziO6O26BA-q1rE5rXszJq322e0bhNXEtY9TL1lywhv5DmgIojmUT6eQy4_tbIZXUvFrggfQkMJAJwThabvca9rTmpHwP_0aPhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«شاید در برخورد با رهبران ایران زیاده‌روی کردیم، چون دیگه نمی‌دونیم دقیقاً با چه کسانی طرفیم!
راستش رو بخواید، به‌سختی می‌تونیم بفهمیم باید با چه کسی مذاکره کنیم. فکر می‌کنم زیادی جلو رفتیم.
می‌تونستیم همون سطح یک متوقف بشیم؛ رفتن به سطح دو و حتی دو و نیم، احتمالاً دیگه زیاده‌روی بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/73202" target="_blank">📅 10:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73201">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec03fa2f2.mp4?token=FN7yHnTPW4ohK_HlRwWYL4tS109LnL1a__JRXyaiqY-PmqQyi3yQ_hWGD8WEj9IRPyG314INunjdcueBJzGJPUY11cqGGBRoaxYIl2o0q4S3uQS15Q0B2H4Mr4TvnBPI9TWA22lQnGPRKR0lwv9-xpuUEXl7JPKQGSt5Fqo62pmsHwjgOYQZM1YmYo0UxsnP4Ur9_tOF6FW22GhTx-VIc8rvx1EG6IhGYI32zRwhhGJEy6k7n4dG2zqh_7yvcM_fUDZHFr-rQAmjwQUjCwU4q44XX0JAgyk2gJqwUKBsboyizWkbAv6hSP84Lgp0mGL1qBBl9zCzfEI6Uygozhb_yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec03fa2f2.mp4?token=FN7yHnTPW4ohK_HlRwWYL4tS109LnL1a__JRXyaiqY-PmqQyi3yQ_hWGD8WEj9IRPyG314INunjdcueBJzGJPUY11cqGGBRoaxYIl2o0q4S3uQS15Q0B2H4Mr4TvnBPI9TWA22lQnGPRKR0lwv9-xpuUEXl7JPKQGSt5Fqo62pmsHwjgOYQZM1YmYo0UxsnP4Ur9_tOF6FW22GhTx-VIc8rvx1EG6IhGYI32zRwhhGJEy6k7n4dG2zqh_7yvcM_fUDZHFr-rQAmjwQUjCwU4q44XX0JAgyk2gJqwUKBsboyizWkbAv6hSP84Lgp0mGL1qBBl9zCzfEI6Uygozhb_yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند شب پیش در تجمعات شبانه تبریز، یه دختر توی ۲۰ ثانیه کلاشینکف رو باز و دوباره سرهم کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/73201" target="_blank">📅 10:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73200">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دونالد ترامپ:
«شعاری که از همه بیشتر دوست دارم، «همجنس‌گراها برای فلسطین»ه!
می‌دونید اگه تو اونجا همجنس‌گرا باشید، باهاتون چی کار می‌کنن؟ از بالای یه ساختمون پرتتون می‌کنن پایین.
شما رو می‌برن بالای بلندترین ساختمونی که دارن؛ البته ساختمون‌هاشون خیلی هم بلند نیست، ولی لازم هم نیست بلند باشه. از بالاش پرتتون می‌کنن پایین. با این حال، من مدام می‌بینم که می‌گن «همجنس‌گراها برای فلسطین»!
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/73200" target="_blank">📅 10:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73197">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YnG-M5EKCv0AzteFsMCF3wj04Ie7EySiy3kkjEmqjTCfMvZUBTnJ3Ci9MV4oW_Kpf_usDC7g6XJ2CJpmPm9BJtAb7zSoh8hTGQsduE0tTUiwEc_t8jZceFA0GoThTYpL83sV_xuwzQ2GTMJaNtjk0zcxYSFf96eXOpskaLMA5rUYwIKxCyBWyt8zBgbhBjEDSImj6qpf9ReuJKwWJ09Bc8z6jhZFwq0qOeIWCSdG8b9QosFUtfzMRwxWHvYLDetSJsok4Kpm-wAXiiwG3x_R3DD1ATyPumnOJyBU0j0Fptv4cMsBnm-cgNKhjUlfRh1ys_qKgrxihttGlTBkWKy-jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ixp72XPKPAMkCTil5_urMqm51NuQQ61D0Eh8gjc6tGMPCTs9sG16WM5dpjQyQgZlppA0-RLa3Z1cTjQJI1bCUdk1M6j-3uJPWHwXd0Wj4jWa5pX-k15zXy76v1_SuK8DyFidJzxbPFPOJ5oIfjOeMsU3zzvUTqbMTZ-u8PfRwTevfPKLHLqPphxq6VnTNf4XJRK4Kyaav48OUP_e_TSsYYhoEaIGSNUkOH1StaZurMHo1kQxBtV7hgCU6ZU5pAak4-Hfh0Ica6h_FegE_irb1Ct4zJayffHKgQHdQKn9iBedBPA-A_mHWdVLqzeN3kPYGd45ZQeULjr7IbIx7Oby4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/352c619970.mp4?token=GVMpfEhSzzg4z9lam0MemZR4XJrLkFVmo4vTNp2gmwVKB5MIBPv0H_A87n5vOct74diultqkoohcPPOq1CnJEl8VNAQY703D-WuXquQl8GeAPXjs7X3zRZE2pvZb2q_wCc7H1VaeIe_8BsH4QNjhPtHqbXIf5HKSYNg8gwCY4fpXBi8gUnNITK_iu2y_TEmjRKU7wwxONbxfnWqYolyxIGACUbGiGyMDxBjOMQNRUoNCLD1IbdIMiTYAFv1fplf8T9m4gFnzmQYayH2uNANPCaxaKUpXcIMSNC3SsJyGaRI4wJg8j0x6hehS2WCtZ8Lp_4XC086Mjie6R1jpVXqx-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/352c619970.mp4?token=GVMpfEhSzzg4z9lam0MemZR4XJrLkFVmo4vTNp2gmwVKB5MIBPv0H_A87n5vOct74diultqkoohcPPOq1CnJEl8VNAQY703D-WuXquQl8GeAPXjs7X3zRZE2pvZb2q_wCc7H1VaeIe_8BsH4QNjhPtHqbXIf5HKSYNg8gwCY4fpXBi8gUnNITK_iu2y_TEmjRKU7wwxONbxfnWqYolyxIGACUbGiGyMDxBjOMQNRUoNCLD1IbdIMiTYAFv1fplf8T9m4gFnzmQYayH2uNANPCaxaKUpXcIMSNC3SsJyGaRI4wJg8j0x6hehS2WCtZ8Lp_4XC086Mjie6R1jpVXqx-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر دانش آموز ۱۶ ساله از اندامش فیلم گذاشته و حالا کامنت دخترا زیر پستش:
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/73197" target="_blank">📅 09:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73196">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a7342c7.mp4?token=Z6oiLOQ71ZUU-ZdRDb0yQKmuFfSpQILCipRl9iPT_b6insusUF5jcJYkBgGSYoEpzwtOS6BaicuGnzStBUynUFljnxtcf4SQXD9l9kxd4o41QvNc8W0DyMRthStlfptjyYUSHEVWcHqgGJpDsGO0ak6JcU738QtKSj2xi5jkFOp9PwceGzBnUyvPbcR50QLLff3Ayx0OO1xh_b7TRhc6E80Bab3t0SBPWDdozehbFR8_fLAbKDABM0nmi5z0jDlVAwJmbiWypEEptgK8z3tXT69at7TujNDDlZoCznI2MOHr3v9R0rdLN3Wpm9a-0sfawGBefjCIDawnAh04UCwE9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a7342c7.mp4?token=Z6oiLOQ71ZUU-ZdRDb0yQKmuFfSpQILCipRl9iPT_b6insusUF5jcJYkBgGSYoEpzwtOS6BaicuGnzStBUynUFljnxtcf4SQXD9l9kxd4o41QvNc8W0DyMRthStlfptjyYUSHEVWcHqgGJpDsGO0ak6JcU738QtKSj2xi5jkFOp9PwceGzBnUyvPbcR50QLLff3Ayx0OO1xh_b7TRhc6E80Bab3t0SBPWDdozehbFR8_fLAbKDABM0nmi5z0jDlVAwJmbiWypEEptgK8z3tXT69at7TujNDDlZoCznI2MOHr3v9R0rdLN3Wpm9a-0sfawGBefjCIDawnAh04UCwE9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از ساختمان پلیس دیپلماتیک در میدان فردوسی پس از اصابت موشک در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/73196" target="_blank">📅 09:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73195">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/73195" target="_blank">📅 01:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73194">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/news_hut/73194" target="_blank">📅 01:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73193">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: انتخابات میان‌دوره‌ای آمریکا تأثیری بر سیاست من در قبال ایران نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73193" target="_blank">📅 01:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73192">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52adbd7bd6.mp4?token=YHKuJMQ71kT0zbY06i7EfbgOH5ntSuhLO51M3S6OEwUf0G2JKMdcq1LgKmp4kRHlW64YA63EvDhfTzBSiCapPn7bY0O8xWEZPQjPKVeiuoTvmjhTj-0BdS0_-BJ2ptFkB8krbbPuomUlzic3RhLZRHgDRPMveD66i2udevDe5xvs7ga_x7MzRAgkiGQlmQsMC224tIAgbyXpYnk5azpOCjXs77Zls5t2IkJUZLuxuirwTM86AQtqWAuzCpkx_OYseXnLSPqvb133lYtx5LLl3emgW-oYK_EGMKJJ37O6_2lNqCvqYEeNE97PT4KOJjW8JHsB5mdiucRmkCkUF8FQvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52adbd7bd6.mp4?token=YHKuJMQ71kT0zbY06i7EfbgOH5ntSuhLO51M3S6OEwUf0G2JKMdcq1LgKmp4kRHlW64YA63EvDhfTzBSiCapPn7bY0O8xWEZPQjPKVeiuoTvmjhTj-0BdS0_-BJ2ptFkB8krbbPuomUlzic3RhLZRHgDRPMveD66i2udevDe5xvs7ga_x7MzRAgkiGQlmQsMC224tIAgbyXpYnk5azpOCjXs77Zls5t2IkJUZLuxuirwTM86AQtqWAuzCpkx_OYseXnLSPqvb133lYtx5LLl3emgW-oYK_EGMKJJ37O6_2lNqCvqYEeNE97PT4KOJjW8JHsB5mdiucRmkCkUF8FQvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: بعد از اینکه متحدان ناتو ایران رو به طرح حمله تروریستی به پایگاه هوایی فرفورد بریتانیا مرتبط دونستن، آیا قراره اقدامی علیه ایران انجام بدید؟
ترامپ: «باید ببینیم چی می‌شه. اقدامات زیادی در جریانه. وقتی می‌گید اقدام علیه ایران، (باید در نظر داشت که)اونا دیگه نیروی دریایی و نیروی هوایی ندارن. تورمشون هم الان به ۳۰۱ درصد رسیده.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73192" target="_blank">📅 01:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73186">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FG2OwW8UxsQ9qZjpg6IQ1dB3TYBJR7Pfbuo5mOBa49H29s-biADwLLO5tQUKTofJASUB-NjAf9kyR-j8PTZKmbE0QFwRUjqeC9ZDoMfCkomrznly0Yp9CFe3vatmdEVulePkTJTMkng68fbXYkLzImvIhqZH4EFsU91w7lCE5ZrBU_Q0VyWF5ZBgfZ_dmczsH4wTZbH2XoP-UdkAXoBNwn-wf_wBEdYd0mISPL9KOQK8ZXneUk0jcbX6UeX12kaJd4yre7RFPYLbO93x18IjUbg784d11gzcvQj56982kPH_Yiigez-GnAkF5C0WKvZrtsrFu4ydFmRbCic-ChRjgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cg2s2zNDisnMJt9liN9XYsvqkIpU6tCGx31wXPpo5aXvqUsEkuSo0yDaaR3okHpq3RYsNkNG45Q2DY-O71XJgox_Jvd1U4rNzT5vJRiEkofAsOLRdq1q7pwwe2F7vJuvpFRla9WuwUEZrl-3w_8lYGK-f-ohcXN1akDuuacYn5WTcVemDa7TM_MQkh-zwc9us4f1OSlExYlflu3xtxX1MFVUTlZUuLE1lHTcEggHwYXuzqtSQP5SiJDjQ2eb13LSFjVKe-g92MmHhhBF3C5tAkPzZktrGGYT9v9bBxaHArAvPi30KGB950vtxV7fIG5x87heo4s2-3G9R5hU7A-PIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sTuJE09N2A3Xl9XKIJz7ZP-4-cZ3_UXE20pUhVGQgtSSHR79Ff1fEvZaoJlJOaX-a9WVRgT8Q2gwlCmtJBj8c4VaDnST8h6NZ_sPMmH90Hboo9tkSATSDTtcTanZNrxSmEqfZvYK5UyNd0VSWgga0Jo4MH58A5jHrbsj_KHoh7JLx_Pq4oMf3OhRyQM-cRw19vVYQTBNV2IoI5DjxLmMa_U-dIlalb5DN4XyG9cXtF614ST35YpcZ-kVfLdCRDCnLwp-Xfq_b7YcrvTcACGVsfEBHplfa3BC0Oe0X21Db6gfVf1Nen-XLSutYJX4_K7eC6a8nqtl2jHt8awtllJYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wk_fmcZsLmkRxhUPIaTEUFgzTWptGggGOknOBncsQtDK2eswNnVR5BLf970bUYCBDaKl0ID-E6US1R5yzl-apGyQ2_hqKs9VJh-KY3PYlNzZgWC71ScWhQ5kATnHUFjmXdcpvyYp_fROqIXwn0HdD3SzqFALPw3af91woHrBBUXc60BKNPE5x4RmdoGJNiMvczYGbsWu88O_PJEuOF9o9zE-Hx3G14rHmISas4Jh-N6F1-com3MYp4UOPAZi1Ar3IV-9lp9xrHN3OeFFYjnMPGYEB2Ru8LD0tpJk-9UFeiZlzhbV9Hmg5Ya9hbWMbKtdhAmFzuBs8qHdE2dC6CV_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PuR08bjhHRKfQ8Rkc5C495p2iYDG3iXMzTpQqbfk20RQYFGmeJ-KhI0FPLr_obkuDKqgYoHiyrl6fCCD7boJlgxe5Cg2znXLG0RTGn_dibIhbqpdS7jyA-6MaGFLXtMFFhLtZTlBgeG0ZmJXWZ-n99URn5KT0CHIMlmJHB5C5TZy6znTrjKBI323p5cWZ4hRFvoE6zUu9r9s44KT2wYnMZLNVhIV98aoNfL0Cni9mkM4L4a2wkd_SSdsU6uzoV1C1PVq67tH2-dMKpDO9IxBbuNLWzfuj0JjC8fcIR3rQ5uHuH_SPqA4wWD1Dedw2HmfDevgs3lDGtyMj4P0QDHqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rh7wXwrDqQat5-myr4QtRyqVXvdjdNBp2RvprLop00amVWGjeHM8xNtH4t33gDLkKHOvZd2Y1pTIXUlDhoCY5_b-5mGbNzWoK5stTaLZSV53130r524JjT7az8sPXSw6SGXN0FLL5jyahEIoe0OUX6df0nD9dwoYoaWKZvT7ZngIMUoDlUUUYzNhJS1Q9UPbQlPiqY6Q5y2-IpGUKKrDug1O-nTTsJREUeNnBj8Rwah-5jpjS2wtgNCnbpI-svQKia7s8S6-leYR1Taw3DbVDfT1d1yRDmn-fUWRWsEq9sMd_5iAEkU5Umz2fZgyQ7wEKqGExdLo5FcCDOhhK05OwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در ۲۴ساعت گذشته سپاه پاسداران به پنج کشتی در تنگه هرمز و یک کشتی در ساحل عمان حمله کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73186" target="_blank">📅 01:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73185">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f60941af.mp4?token=LLDl1HvkgIfoDrEGtOKBh0_RiEgNddcvQIjTYw3S6TU2ucTmI4iAGmW51SAIOpEQgB3eOi0wEyazqHwm-4YL7Jp9gy9RjEuo8xSuXyTLsxLFoZQIKRxzlEyzacK1AcPnDoAte8qv4aFEM7pP6Hc2utKBpqv8FsMS0K49oMBIzuBhJFKwRl17gabopXvMAuEfP9xnermjcOmk3iL8aJ8Zbj1Lir72UQICLLvwI9tlW7i5Y6IZL5fvzXSwigrrW8LQ92W61bV0rlwXt02isMD6LRnHZqs8FUjrbFMAWCMI8hEjF6EL0czHMVTumkC_wiEO2dCYkBggh0jgAPN4wz3Mxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f60941af.mp4?token=LLDl1HvkgIfoDrEGtOKBh0_RiEgNddcvQIjTYw3S6TU2ucTmI4iAGmW51SAIOpEQgB3eOi0wEyazqHwm-4YL7Jp9gy9RjEuo8xSuXyTLsxLFoZQIKRxzlEyzacK1AcPnDoAte8qv4aFEM7pP6Hc2utKBpqv8FsMS0K49oMBIzuBhJFKwRl17gabopXvMAuEfP9xnermjcOmk3iL8aJ8Zbj1Lir72UQICLLvwI9tlW7i5Y6IZL5fvzXSwigrrW8LQ92W61bV0rlwXt02isMD6LRnHZqs8FUjrbFMAWCMI8hEjF6EL0czHMVTumkC_wiEO2dCYkBggh0jgAPN4wz3Mxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: انتظار دارید جمهوری‌خواه‌ها مجلس نمایندگان رو ببرن؟
ترامپ: «ما عملکرد خوبی خواهیم داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73185" target="_blank">📅 00:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73184">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=cUoLrAjOd5xMarx1y03zfX0JcQuo77IsX_NtH9nyAILRSHNdDU1obzb1Aa9pyUBr8IexBieyuoqgd8G8gOCvhlTsG-6wSNCHwilmUYMGJrd9alipYblx9K4Kj7mr9Intgd_C80fXp9QZBBslQz3QSyPTd4Yom5BaNlWaBwNp3NwrW2CzaZxWi2o-ZlfxhIUmZoxCmCzUSnPZY_d_Mpc_Kiys4qRkX5xR-l1ajOcumTIoD3P8HHnDPAWhiL6pyMIQT3Or3h1PmQY68mEQzXw6xmNcoDAFRVp5FpGjnOTC7q5UsYMPhmG007fikecFBj4gFfo6TTvdUZMJJk6pmXv1gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=cUoLrAjOd5xMarx1y03zfX0JcQuo77IsX_NtH9nyAILRSHNdDU1obzb1Aa9pyUBr8IexBieyuoqgd8G8gOCvhlTsG-6wSNCHwilmUYMGJrd9alipYblx9K4Kj7mr9Intgd_C80fXp9QZBBslQz3QSyPTd4Yom5BaNlWaBwNp3NwrW2CzaZxWi2o-ZlfxhIUmZoxCmCzUSnPZY_d_Mpc_Kiys4qRkX5xR-l1ajOcumTIoD3P8HHnDPAWhiL6pyMIQT3Or3h1PmQY68mEQzXw6xmNcoDAFRVp5FpGjnOTC7q5UsYMPhmG007fikecFBj4gFfo6TTvdUZMJJk6pmXv1gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفتید روسیه و اوکراین با آتش‌بس موافقت کردن، اما هر دو طرف می‌گن چنین توافقی نکردن.
ترامپ: «موافقت کردن. می‌دونید چرا؟ چون من گفتم: شما موافقت می‌کنید! دلیلش هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73184" target="_blank">📅 00:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73183">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b813e1384c.mp4?token=mRbtmEZ1-2r26cJTh0XfNRSjqM4Mk2uab0AwDCGHg6FJzuYT4N-S-zUmmSAabLj2dmJ88rHtxiK3pHbHOEjlwOhnftaXa6i8mbcCdBshzUUC-8cutNAosK1r28q76nk_DQaW68tM_iceMR8wCWpip_iWp-pF42urs9g2apT-F1BvzXs_Te6BHf2vnd9Kmg78M_GqZP7qDPEAzUKg9ygwYTkoR6IHgYc_6t_jnvqMNEK5xWwfSw1_gHB-8rO2nyCKVcch9Sf9lbFnlYcdMgaWs24jdI3nALZ4XhRq689UNQdvtpDM4AD9sMuQen5TKBfMF2hwmS_caMBt2zH1Dv0ejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b813e1384c.mp4?token=mRbtmEZ1-2r26cJTh0XfNRSjqM4Mk2uab0AwDCGHg6FJzuYT4N-S-zUmmSAabLj2dmJ88rHtxiK3pHbHOEjlwOhnftaXa6i8mbcCdBshzUUC-8cutNAosK1r28q76nk_DQaW68tM_iceMR8wCWpip_iWp-pF42urs9g2apT-F1BvzXs_Te6BHf2vnd9Kmg78M_GqZP7qDPEAzUKg9ygwYTkoR6IHgYc_6t_jnvqMNEK5xWwfSw1_gHB-8rO2nyCKVcch9Sf9lbFnlYcdMgaWs24jdI3nALZ4XhRq689UNQdvtpDM4AD9sMuQen5TKBfMF2hwmS_caMBt2zH1Dv0ejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: روسیه همین حالا آتش‌بس رو نقض کرده و دیشب به اوکراین حمله کرده.
ترامپ: «در این مورد مطمئن نیستم. بررسی می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73183" target="_blank">📅 00:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73182">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQygZSelmDjDpjPvKgW1u1qUptio48hC4tgeW1pFtjrT9NKFjLFZ1NhwrtsmnE9xXZ3QAtUWJlLDRduKDYbmh5eEfCu02NmvWCCMDspxw29LkocVJtUCOUvXdb5Z4-EOtqevm3JqfN9xPV6VO19Fo6ql_DlW4wnXJO9FkJuzeFeo07jtopoXdScQGGZguQNE6yQX1n_Oycb438dMbuj1wO_muHXqThC1AcEg8rUOwwWveI17qphrZ4GrVkLJMJIWSzA_a69lMgWC-mWt4Jn96uRX9iDMY9kaEJqhUtzBIWWIEZ0DVsm4vw5gZOC0SQkpNUJATjU8CYx29GGV8irqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آر. جی. میته، بازیگر آمریکایی که به خاطر ایفای نقش «والتر وایت جونیور» در سریال محبوب «بریکینگ بد» شناخته می‌شد، متأسفانه در سن ۳۴ سالگی بر اثر خودکشی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73182" target="_blank">📅 00:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73181">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a66098169.mp4?token=OVG3jFqNtCKexA4zu4A9CMUF37dM0A_qxR5rI7S4aCBWeCPZPF2BkxS2gPRS0l5CL0L0hKaUnqq-2ER9d19MoGsbuThB-lDC6MN-k4a08_uCyG3qoxzb5K_VkHe48YZpls6Fd9YzxgDpd-nth9GYDFF0RdCasnnUlYN2SE8Q-JZyvYRHneyVoVLfzgj6fVfmNF8lX7HYQ-DxyclOHcKlg6nOn4jFl2qjxyRyEPkO8V8Iy5gpa7qw3GNkcZq4-hYjFQRsNWYp1-U0Ydm5BFjcD8JSG5pnEu7EZEC3ZhbPg-x-oIuCsBoPzE5fGiu25wtx7myg6bgw1kCr25tT6rST8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a66098169.mp4?token=OVG3jFqNtCKexA4zu4A9CMUF37dM0A_qxR5rI7S4aCBWeCPZPF2BkxS2gPRS0l5CL0L0hKaUnqq-2ER9d19MoGsbuThB-lDC6MN-k4a08_uCyG3qoxzb5K_VkHe48YZpls6Fd9YzxgDpd-nth9GYDFF0RdCasnnUlYN2SE8Q-JZyvYRHneyVoVLfzgj6fVfmNF8lX7HYQ-DxyclOHcKlg6nOn4jFl2qjxyRyEPkO8V8Iy5gpa7qw3GNkcZq4-hYjFQRsNWYp1-U0Ydm5BFjcD8JSG5pnEu7EZEC3ZhbPg-x-oIuCsBoPzE5fGiu25wtx7myg6bgw1kCr25tT6rST8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالملکی؛ وزیر کار دولت رئیسی و عضو هیئت علمی اقتصاد دانشگاه امام صادق:اگه گرانی رو در نظر نگیریم، هیچ مشکل اقتصادی توی کشور نداریم.
+اگه ۴۷ تیم دیگه رو درنظر نگیریم تیم جمهوری اسلامی تو جام جهانی قهرمان شده
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/73181" target="_blank">📅 00:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73180">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بریتانیا دو تبعه ایرانی به نام‌های «روح‌الله بازقندی» و «شهرام علی‌رضا تمرزاده جاکی» را به اتهام دست داشتن در فعالیت‌های اطلاعاتی ایران و توطئه‌هایی با هدف قرار دادن افراد یا دارایی‌ها در بریتانیا و سایر کشورها، تحریم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73180" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73179">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EYGqc0o5cYxMBTtI1Wmj5ciO5hhl38c4I2RuTTCJ7RJCMuchamHXfGHf6byTs89EzlDLA9Ra7IM9fW_8a9ARYmccwcraUe9s1NbClxs9IKdzaD561VHFjndhj_ktQscIHDIlMoAfJ3yWXc8fFv-hthFXoXb7jV8HV4Mt5IhS8ErgqIzDNC1VX9n0BE8H6rLAsUPN6eIBtjJ1ZbvQ6eJtxMy-44p3wcpnv_xkBhpBqKBSTuH5uvkK9Vuz9n6FgLR4niKFRoOKRKtXwStrNkOcPrfee-vua1hAdvXZuklroLn6D3fNVvt0qJ84tH2Z6Z8Q2DJ2DPPfaJioLHcUUp6Llw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو امروز لایو گذاشته بود و خیلی جدی داشت در مورد انتخابات اسرائیل حرف میزد که یه ایرانی این کامنت شاهکار رو گذاشت:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73179" target="_blank">📅 22:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73178">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=N6uU6_sWNoEPs2ZCO1tTFIstpT4rO43gfGwGer8pfDJdiF397LbqDOLWbzrfNKOO5__dZ2zAbwZjrhMW1HCr_74DIz8vSrZ10221XT7MCLB7tziMeDfS3U_1e1o6qGG-cutCk079hk-44CWaFjfjSEXiv_He1xZy2_O4vDqXT_Qy6KUl7WY7ZmDRJAVN6ksQaqF9W8Wl2LtJ08r2EAbC2QUK9tthVIm6-NtneOJNBCj9umIbN194G4F5z6ZXpKBJOBRx-7xJg27q_f1xH4T7AltJ18d_WYVWCPtj3U7AIxgRSn4PKte6x6EYrLrTJb-N-QOnEKb2EWDD03AC-Pa-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=N6uU6_sWNoEPs2ZCO1tTFIstpT4rO43gfGwGer8pfDJdiF397LbqDOLWbzrfNKOO5__dZ2zAbwZjrhMW1HCr_74DIz8vSrZ10221XT7MCLB7tziMeDfS3U_1e1o6qGG-cutCk079hk-44CWaFjfjSEXiv_He1xZy2_O4vDqXT_Qy6KUl7WY7ZmDRJAVN6ksQaqF9W8Wl2LtJ08r2EAbC2QUK9tthVIm6-NtneOJNBCj9umIbN194G4F5z6ZXpKBJOBRx-7xJg27q_f1xH4T7AltJ18d_WYVWCPtj3U7AIxgRSn4PKte6x6EYrLrTJb-N-QOnEKb2EWDD03AC-Pa-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض به تاخیر افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73178" target="_blank">📅 22:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73176">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzmwdPSfxS2R59pTnB5OB3NIerKOdOc8N1bXZSS4SSdWmZgYQnZRES1i5g17S0AIPRvIwjvF9hyXH2AIDfLnawSBf2hQDmD29PCWyxsaoV5sEcOTVJUn9JzuLfK5qDEf4zdtMvWoi5l5b_IlEILCPeqnpzP7Ubv65fV0LauwxoSs95X8fIaVfQDK2mat7dW22tsCxEWyI2UuKmc4vKFTojkfXY-UBpnlwK9WH3ofnIhfsJeyXcw8HGpnBLkg9MX_ZEcWpCqQEFQAGpJeg_gOSdzh9O2Y_hG7I1rVseMX4jGRMO3MzfyRluq3XOXUHo2HWZRaJO-Ht2P1Y934o4CQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که یک نفت‌کشِ حمل فرآورده‌های نفتی، هنگام عبور به سمت خارج از تنگه هرمز، مورد اصابت یک پرتابه ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73176" target="_blank">📅 22:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73175">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2fd3a4fd.mp4?token=R9MH3trdVbl3_EW7hQF68_Q3lDPwlrXy5Ll_oS8328QYICwx6Lw9C2w0HLTOm_5M922TPtUGcRhSxWZw18qlhLyNKAUs7MwmUVHONA5KZfcuQEBJpawkZxmjuPIa7hUchDSgwwerWJZ4ZFfeutIUVwishenLJQPmoB6rSqt9GdzcETcaFbRW3WCPMwXd-IudkP41EAZZ3-D9fhMDYGEneuNedhlHVnzUV9Dv5DeaHwRzqmSEL3siDEtvh5vYxomnLMFEq9BnaEmaW6s5ZCpM7zV7gFznJsuyxobBeRDcS1TlI_fVDhMfBwT8nyCnwg0oaDveaFozaXm8wSzlZDY6Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2fd3a4fd.mp4?token=R9MH3trdVbl3_EW7hQF68_Q3lDPwlrXy5Ll_oS8328QYICwx6Lw9C2w0HLTOm_5M922TPtUGcRhSxWZw18qlhLyNKAUs7MwmUVHONA5KZfcuQEBJpawkZxmjuPIa7hUchDSgwwerWJZ4ZFfeutIUVwishenLJQPmoB6rSqt9GdzcETcaFbRW3WCPMwXd-IudkP41EAZZ3-D9fhMDYGEneuNedhlHVnzUV9Dv5DeaHwRzqmSEL3siDEtvh5vYxomnLMFEq9BnaEmaW6s5ZCpM7zV7gFznJsuyxobBeRDcS1TlI_fVDhMfBwT8nyCnwg0oaDveaFozaXm8wSzlZDY6Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از یه مدرسه پسرونه!
معلم اون جلو وایساده داره درس میده، دانش آموزا دور هم جمع شدن و کله‌پاچه میزنن...
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73175" target="_blank">📅 20:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73174">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtCELL68f85DlgQZErVtsop0pt3UeRsjovl9eqo-QN_OOWsMGWY83qWxa5LNklBQWGidGp4P446Cn55M9Ix_vTAh-AzTeQNMqxhORx5MxmtrkNUT_uxhRk_AQ4cz_jn25EuAgGUv_2TKsJvWIUq4P7OOqvQGnD1v8HJTjWz0h9qGLyQZB7kmle5m9AGR6rj4XuQ8D8yw5cd2r7c_nx4UaLxN0WB1TAYqgG9OG13B-ZI3hmb_02DtQ1-18uqaV-DRidaHjVipRJSpjhCFdPE_Cx-hpdsJd4P1JzGPjx63WtlHI9OdofaacXug_kHypcQp4l0g7wR4SmFz2QB-iyf6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار تصویری، اعلام کرد ۱۵۹ کشتی ایرانی در دوران ریاست‌جمهوری او نابود شده‌اند؛ همچنین مقایسه کرد که در دوران رؤسای جمهور قبلی این کشتی ها روی آب بودن ولی الان کف دریان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73174" target="_blank">📅 20:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73173">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7da0f71e2.mp4?token=fyu6ydgb6NxSqvz3g3ddgbTI6VtR6ghBBo3hDcxATFzyn3V9HXaOhe3-2gTdBxRpT3UlbKI5LTFqYB-ZFAAL-lgmxv3L3IbnNZoIv3iD1Q6YpAE2Zr9PKoqhCeIQlvFv4Q4PG7-mtY94T4zTmUQkZSbQozwlzdsQ12wig-FOLHZ-1EmUJC1KarsHYqV4ad0giFuY6k5Zw6y9yw9ewCCOJyFEKMQWyTp7iibAvgxv_BZCRKg2TmLZ-NBOz6h5ugRFzcPTmV5JbO78bcNo3rU-w7IS1NUlmbSOdG7BIKbrGxX0PUh5-S7Nv2JcpSk_9hL-72mhBZw4-eFmWPDkY1M4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7da0f71e2.mp4?token=fyu6ydgb6NxSqvz3g3ddgbTI6VtR6ghBBo3hDcxATFzyn3V9HXaOhe3-2gTdBxRpT3UlbKI5LTFqYB-ZFAAL-lgmxv3L3IbnNZoIv3iD1Q6YpAE2Zr9PKoqhCeIQlvFv4Q4PG7-mtY94T4zTmUQkZSbQozwlzdsQ12wig-FOLHZ-1EmUJC1KarsHYqV4ad0giFuY6k5Zw6y9yw9ewCCOJyFEKMQWyTp7iibAvgxv_BZCRKg2TmLZ-NBOz6h5ugRFzcPTmV5JbO78bcNo3rU-w7IS1NUlmbSOdG7BIKbrGxX0PUh5-S7Nv2JcpSk_9hL-72mhBZw4-eFmWPDkY1M4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سرباز روس تو خط مقدم، سربازای اوکراینی رو که از پله‌ها بالا می‌اومدن، با نیروهای خودی اشتباه گرفت!
وقتی اوکراینی‌ها به سمتش تیراندازی کردن، تازه متوجه اشتباهش شد و درگیری از فاصله نزدیک بینشون شروع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73173" target="_blank">📅 19:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73172">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8047543035.mp4?token=v987uI4gViEQwo4oC5hQ7Gw9pPn6wT_w34qyzZGFPFBfhENhf8OaZhonF611MgeCi83ZIcrla0RoxhXdibMXusbfQUKryq-l1oXpr36FMUhLQ2FcvFJ54UUDWtY1m_yr2o1MVA2PmlDQIWPtcmgYhRPqYLIdS4TKdXce61uUh7ocFflV9CuexrR3i69PJGiJqF1FVuwt_9VqNdykeh67CQVmhXLfE4D2qTM4EL4fB-iWlZbQRoMRdVz2_TEQrydQgOnqfRyZccVR_h_myFJzzfy5Lu4clKBeNK-MqX0Au3G4vh8rOZdBi30lSPQ7xBZQpUe3_wpn3azVRIJltEvstQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8047543035.mp4?token=v987uI4gViEQwo4oC5hQ7Gw9pPn6wT_w34qyzZGFPFBfhENhf8OaZhonF611MgeCi83ZIcrla0RoxhXdibMXusbfQUKryq-l1oXpr36FMUhLQ2FcvFJ54UUDWtY1m_yr2o1MVA2PmlDQIWPtcmgYhRPqYLIdS4TKdXce61uUh7ocFflV9CuexrR3i69PJGiJqF1FVuwt_9VqNdykeh67CQVmhXLfE4D2qTM4EL4fB-iWlZbQRoMRdVz2_TEQrydQgOnqfRyZccVR_h_myFJzzfy5Lu4clKBeNK-MqX0Au3G4vh8rOZdBi30lSPQ7xBZQpUe3_wpn3azVRIJltEvstQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش علیرضا خمسه به کلیپ معروفش توی فضای مجازی(خلوت کنید آقای خمسس...) :
منم مثل همه شما یه آدم معمولیم. صبحا میرم پارک پیاده‌روی، بعدش میرم نون میگیریم و ...
بخدا من بادیگارد ندارم چرا به من فحش میدین؟
چرا به اون جلوییم که اون جمله رو داشت میگفت فحش نمیدین؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73172" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73171">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73171" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73171" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73170">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9ABFIfj74x8n4d3WMIerwIRXIQ6zrgZB3gGBCzE04sG90rYhsgOO7SwKSl0nn8XelQWwLKjCJVXCt6lkGnI3qgmSuah-JVswj9zdnj88cM5BDqQm26p4S1rbskNVypTHCf6yQQ0MSZScTAqth7Z9JHWh6s5djOC3tBYJ2NcJPs54l58MS_0dzuqbcN6og_Pg5dKWpi55AqdljA8CT7to9ayQaz5QWB5-C71mN_qQ-TYJ1Ai4WXe_S5pXnzHfEoqibRsiGYkVrYrUa33A03qNtXg-koFEVT2Av8Y7Sgnk4l_7pdkOjE3GrraYSCfgvnD5pEZceNSsg5FJmlSFr47ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز استقلال
🆚
الغرافه رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
استقلال: ۲ برد، ۳ تساوی و ۶ گل زده
الغرافه: ۱ برد، ۱ تساوی، ۳ شکست و ۶ گل زده
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73170" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73169">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">#مهم
؛
اندی برنهام، نخست‌وزیر بریتانیا، می‌گوید می‌تواند تأیید کند که حادثه پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) «تقریباً به‌طور قطع» توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است.
من می‌توانم ارزیابی خود را مبنی بر اینکه این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریباً به‌طور قطع توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است، تأیید کنم.
ما این تهدیدات را در خاک خود تحمل نخواهیم کرد. ما با استفاده از تمام اختیارات قانونی خود برای هدف قرار دادن شبکه‌های جنایتکار مورد استفاده ایران و همچنین منابع مالی آن‌ها، با این اقدامات به‌شدت مقابله خواهیم کرد.
ما تحریم‌های بیشتری را برای محدود کردن توانایی ایران و سپاه پاسداران در آسیب رساندن به خودمان اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73169" target="_blank">📅 18:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73168">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50742ac121.mp4?token=RGRYzidJxvV5LMpyQKaJJc6B3Zfe8m8z3s-K6a2gjEGABmAZtKVYEU8WIqNnKfCDwHmAxsVByGeO7Yqm_KHvR-AhsgUENK4vmUy7MPY6PMXO-a22dvuKg1MbsY6I-CvAUzeDLoOu3M_8791cmAYvWGT0C-6ICwsb9qgHPLJHa-X7_kYaKPjuQYnNEefJcPBaDdJrmqBCUbW6jExf4scoUVPiswV-h4mNJFZ4qY3ukrqzEIlNQexmHpHMO3zrXIZCYwM5TImxFnULzB72RNaMJTjrFWZNtywCFX4t8Qz9TfSUFmC5kW1SB_MboP0nQP6Uui9_sJrqa3KgEqIa25AYMr-18YFIpK_swYoGTmiYUE4Qh9k-Egb1RaMCmdnuk9MJ5XwlY85-hiMFIfp2A__8Expu6LUxQt5NAehmjBFx2yMQbFZKKREPJYnLZNJi_ns0fxfUgape8lv4GShF3tirubaiq9uTn5iVJAAV7xKF3Yn3virudJ2apZvFrpmktRtqk2aMjo3IxKsiXrVKAkhQtdMLtvmRbfKCe0hjiwMwvO1JmnD9nXSgHyxIIFLtjh9labvQ1WYGmCx82rDkr_oyexFbDx-W2NRz6EOs-z0dS7MEB_IEGDN3I3tPpewx_PIDA2cMTLQ_hcv9DYKW114YmNcND8u1D86dcE9lHroHyAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50742ac121.mp4?token=RGRYzidJxvV5LMpyQKaJJc6B3Zfe8m8z3s-K6a2gjEGABmAZtKVYEU8WIqNnKfCDwHmAxsVByGeO7Yqm_KHvR-AhsgUENK4vmUy7MPY6PMXO-a22dvuKg1MbsY6I-CvAUzeDLoOu3M_8791cmAYvWGT0C-6ICwsb9qgHPLJHa-X7_kYaKPjuQYnNEefJcPBaDdJrmqBCUbW6jExf4scoUVPiswV-h4mNJFZ4qY3ukrqzEIlNQexmHpHMO3zrXIZCYwM5TImxFnULzB72RNaMJTjrFWZNtywCFX4t8Qz9TfSUFmC5kW1SB_MboP0nQP6Uui9_sJrqa3KgEqIa25AYMr-18YFIpK_swYoGTmiYUE4Qh9k-Egb1RaMCmdnuk9MJ5XwlY85-hiMFIfp2A__8Expu6LUxQt5NAehmjBFx2yMQbFZKKREPJYnLZNJi_ns0fxfUgape8lv4GShF3tirubaiq9uTn5iVJAAV7xKF3Yn3virudJ2apZvFrpmktRtqk2aMjo3IxKsiXrVKAkhQtdMLtvmRbfKCe0hjiwMwvO1JmnD9nXSgHyxIIFLtjh9labvQ1WYGmCx82rDkr_oyexFbDx-W2NRz6EOs-z0dS7MEB_IEGDN3I3tPpewx_PIDA2cMTLQ_hcv9DYKW114YmNcND8u1D86dcE9lHroHyAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ اندی برنهام نخست‌وزیر بریتانیا می‌گوید می‌تواند تأیید کند که حادثه تروریستی در پایگاه نیروی هوایی سلطنتی «فیرفورد» «تقریباً به‌طور قطع» توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73168" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73167">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294900b4d0.mp4?token=CFNuD3IfpailPPtVx-uXKUHyenjZo7659jzC5Z4jODHB5PyB6Y8BBbw47ygQjNXCKZnhxRRGMZCuofOVS1UN0KJbQdwHrk7GuzIA7QcGSwyAwSRnp2ocrxxDM99qnzeppImnxL1uurX7jF00Krtf2O3K5W9H8GF5VqRHh1jcx61VJlEFvTA2WTZRTDpRq6fD32nWOqXf-bYaeorom9UQr88SvcTmnyu8jUsIpnmGFzlaF4jDuGUmYVml0sv4c0yigADxwZGPyw2W13wDacV0Pk_uY7cHyU0PrMYphzVPh_bUCtmf2G2iBQF7QTmsSHX3pL2Fr6z6jKW-iPP8bv69mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294900b4d0.mp4?token=CFNuD3IfpailPPtVx-uXKUHyenjZo7659jzC5Z4jODHB5PyB6Y8BBbw47ygQjNXCKZnhxRRGMZCuofOVS1UN0KJbQdwHrk7GuzIA7QcGSwyAwSRnp2ocrxxDM99qnzeppImnxL1uurX7jF00Krtf2O3K5W9H8GF5VqRHh1jcx61VJlEFvTA2WTZRTDpRq6fD32nWOqXf-bYaeorom9UQr88SvcTmnyu8jUsIpnmGFzlaF4jDuGUmYVml0sv4c0yigADxwZGPyw2W13wDacV0Pk_uY7cHyU0PrMYphzVPh_bUCtmf2G2iBQF7QTmsSHX3pL2Fr6z6jKW-iPP8bv69mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد که طی دو روز گذشته به سومین سوپر نفتکش در تنگه هرمز حمله کرده و موجب آتش‌سوزی آن شده است.
سپاه پاسداران اعلام کرد که این نفتکش هنگام تلاش برای خروج غیرمجاز از تنگه، سامانه ناوبری خود را غیرفعال کرده و به هشدارهای مکرر بی‌توجهی کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73167" target="_blank">📅 18:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73164">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1oBPqj6SaIqbUsqLBUi-xK4Q3Q7F7h8_Ove1LUg9alkioOhCuAGQblHWTCS88bWrj5Z-qfJHZxO54j8W-I7ra2rYvpCp63ZY4VfhD_6OO17yZrlbN-lleEX-dL6xuJ1J8wUaX1jUUBf7k6f_4CwlA4-yaxFK-hSd_kUVaBcSNu-8BeBivh_TyzDoVJTCAD6fCSq75wW0NGp4hQPb0jtElUuE9425RRdhOVqdMiyxoNJpe5WnOFZjhcotnaT-CrlYSk6dY3xe2pYUjbCGJCgc3KCb0bZcezKQY1DVx70nkg9VrArREDKj50hOWRp8DRLZlEQ1zCn1kU81eti9slF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LncsvKZMmfDgStvo650nOBe2JvX9OMn4b8IFa914aJO6YWc4T27Ryc3g-wPFa-BEAIuIP77CVNav21-c5-pl37_Uiiy5xv0UPsEEEull4gISwVbmqkBx3l9rQBHmEj2XSLFnULh1qS_HdEF2usxtT00gVFoh1iu_VWVOFVSTBNb7UHjEgL0L7RP3t8R2VRLOj_PAYe7D-xprvzbfeUMlyH6UBtkCZ4qBQNGBJMEtOAkflsMSJXbICliZ03hQ1CmKvqj8-9lwvLPIPZ1KWTCSEXRw0bB4n52tCFIoJPWXUlqr3l6O6PPdIJaRMFplUs6dFwjQ7F9nk1eY6KLC6IPBTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4sNoK29wej7nln_KQZoKqsHfoRsErNqJdxvfJe05_EI6HF3rL_HDbRKv101bknLS6-DuImi7RPT2zmoQck1gs1bey0DtqHvekFjFT7lrXxrUT8Qe2xYyW6N8nqhFCUEGrqTSLPS5lc7ItuvSBLC-yAamo4YIAPJV1fEPRXDqMx1yHaGqOY7K1ETrCEXA1Uygny5yD6Rg42XukBc3SsGqvOUfwMm6_Wej7BL1ljHkrftKf2hRo32acVoK646qWmPnMplTeHGa4SxCUlYquqKX0tDppNoQK1doUS51QbYhAORtRF4plwoeeu6kCiTOFhHnPV60WhIdayydlCeIsh7uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آزمایش موشکی سپاه در یزد:
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73164" target="_blank">📅 17:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73163">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1f4cc034.mp4?token=k-igTRzNuMrHAwZE4-Vh2dUWCFHuhEPFG-Nce_KAtXBRBy8oL2KEKXweYMuMn5iUm94Epbf-YrAjyY2V6ygJ98HiIUHsEO_P5w33d5ffSa_9rD6XG3byj8W2QrwM3sXY50ohm8FrriTQn0NA5HoDQH-fqEW7oHvvQE_bU0ITi5lB3xZouO6q8ZH4vCpvnYNeZ9yo4CnikKKcplqbeWXoKa4NqkoXLWcDphO5EjiDbfIzWR6lY-Yueo14nCK3K7zo6knH2mYJamdB0GErtTZGYWgOkAAquIbjk0_9S2cx_TBNpNWqYYe2t7fJkmnTpfRzWe4brFwqlXTFVWBmC8PPEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1f4cc034.mp4?token=k-igTRzNuMrHAwZE4-Vh2dUWCFHuhEPFG-Nce_KAtXBRBy8oL2KEKXweYMuMn5iUm94Epbf-YrAjyY2V6ygJ98HiIUHsEO_P5w33d5ffSa_9rD6XG3byj8W2QrwM3sXY50ohm8FrriTQn0NA5HoDQH-fqEW7oHvvQE_bU0ITi5lB3xZouO6q8ZH4vCpvnYNeZ9yo4CnikKKcplqbeWXoKa4NqkoXLWcDphO5EjiDbfIzWR6lY-Yueo14nCK3K7zo6knH2mYJamdB0GErtTZGYWgOkAAquIbjk0_9S2cx_TBNpNWqYYe2t7fJkmnTpfRzWe4brFwqlXTFVWBmC8PPEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از اولین اصابت و انفجار ها روز ۹ اسفند در پایگاه سوم نیروی دریایی ارتش، کنارک
؛
در این ویدیو ، یکی از پرسنل که به ناچار و طی غافلگیری به اطراف پایگاه همراه با هم رزمان خود پناه برده بود، می‌گوید ،"جایی نداریم ،فعلا همین جا بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73163" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73162">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/73162" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73161">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GiKCPSbNbf2Oxz7_bdJ6hT-0TmqhUrcD61hzt-RsWwXhuJRWINE3mmd_4oXZqiZSkxIBfXF_V7TH3Rl7BVgsnVuDnmt5nKO1Lhj6G8EkMJxMPW2FhPJIbHN6ZBD1XQA1OS43jqvV4qySepk0Vnil3ab4xfCQMzv6eKdoRnf-BO0wS_uWB7q8y1_MImI7JHmqVHdTQFzhH7Z-Esc_800SX4-RFAHTrcZDCUm9oALWgE9xkgC6G3KytYwPgMQVc5wRiSmbCx8pKUTCLD47VriP3ViYp2LPJeqTm2qjbMayAQ_4LZS9rGQw-_cjAyYXA6viQ3qCxmemEAES9D7uuuoR9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73161" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73160">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ارتش اسرائیل در پی وقوع حادثه‌ای در شمال این کشور که منجر به مجروح شدن گروهی از کوه‌پیمایان (که گفته می‌شود معلم و دانش‌آموز هستند) شده، وضعیت «حادثه با شمار بالای تلفات» اعلام کرد.
این حادثه احتمالاً ناشی از برخورد با مهمات عمل‌نکرده بوده است.
گزارش‌ها حاکی از حدود ۲۰ مجروح است که وضعیت برخی از آن‌ها وخیم بوده و یک نفر نیز نیازمند عملیات احیاست.
ارتش در حال انتقال مجروحان با بالگرد است.
نتانیاهو حضور خود در برنامه تلویزیونی «The Patriots» را لغو کرده و در حال عزیمت به محل حادثه است.
فردی که در وضعیت وخیمی به سر می‌برد، اکنون جان باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/73160" target="_blank">📅 16:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73159">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bba8b18ff.mp4?token=bxCNfoWccA7ZlnbYnI9vyLSCtyxUkYPtDCvg1FPo126-xIJ3RpfbtpRvXfW5eAUhZVlU-0A6TVCuULBhj4sJMNXjTxDmMoyrpKgN3UCMkYQxiUCf7gEd5HSeyG8np2ZBAQy3XbMpM7MaxY16cC8AK0lB0nGnWXsrXhHs8K42t_VOLagDUCwr3PviGyymeUMShxB3kNAH3oSSOCb9Ha5TZ3HUkf9QO2-4BmpispcgW8KZuqAEnwMHEC3NzIzJWRfU7YHG-HoSqEzr5L15wBOrZxAwErzgfD0kiWcENk45hLtZwIrMLVsPSSf9QM2s6235ExbOsQKsSW36Occ-FrknZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bba8b18ff.mp4?token=bxCNfoWccA7ZlnbYnI9vyLSCtyxUkYPtDCvg1FPo126-xIJ3RpfbtpRvXfW5eAUhZVlU-0A6TVCuULBhj4sJMNXjTxDmMoyrpKgN3UCMkYQxiUCf7gEd5HSeyG8np2ZBAQy3XbMpM7MaxY16cC8AK0lB0nGnWXsrXhHs8K42t_VOLagDUCwr3PviGyymeUMShxB3kNAH3oSSOCb9Ha5TZ3HUkf9QO2-4BmpispcgW8KZuqAEnwMHEC3NzIzJWRfU7YHG-HoSqEzr5L15wBOrZxAwErzgfD0kiWcENk45hLtZwIrMLVsPSSf9QM2s6235ExbOsQKsSW36Occ-FrknZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها دو ماه پس از سیل ویرانگر پیشین، نپال بار دیگر گرفتار سیلاب‌های شدید شده است. این حادثه خسارات سنگینی به مناطق سیل‌زده وارد کرده و بار دیگر زندگی ساکنان این کشور را تحت تأثیر قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/73159" target="_blank">📅 16:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73158">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d202e2650b.mp4?token=jMqBLA5KDysE_b-iVIBRQg32K2QfWfdTPBjVogSRHapoclEVki6LbF04k6lE2591ai8uAqm49_pYitUnedxHa6qLAzenZf-pG4A1a2JQbqIEHmmUs4Zs7kkMtKu46NTkJz9BYLLTyzlxD6x6ZVsW-IOh-xhRnx4ZAb1gWiSEvI0rOEmZCvbzV0yWYB4iBFjqNIU_GBo5ais2U6DYFUXQ00QZV9NbZXaYQtoaPJepkiO5DGVXG8PEYkoqPUqKy4Zv7JbaOe4GLbz_KjwFUr5Ji7hflVUIN95f0qSD51InXtcCofkduoByR1iSipoAINvEOIftNVw0cidCHHjpUli0EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d202e2650b.mp4?token=jMqBLA5KDysE_b-iVIBRQg32K2QfWfdTPBjVogSRHapoclEVki6LbF04k6lE2591ai8uAqm49_pYitUnedxHa6qLAzenZf-pG4A1a2JQbqIEHmmUs4Zs7kkMtKu46NTkJz9BYLLTyzlxD6x6ZVsW-IOh-xhRnx4ZAb1gWiSEvI0rOEmZCvbzV0yWYB4iBFjqNIU_GBo5ais2U6DYFUXQ00QZV9NbZXaYQtoaPJepkiO5DGVXG8PEYkoqPUqKy4Zv7JbaOe4GLbz_KjwFUr5Ji7hflVUIN95f0qSD51InXtcCofkduoByR1iSipoAINvEOIftNVw0cidCHHjpUli0EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی عجیب که از اعتراضات فرانسه وایرال شده؛
مردم تو یه میدونِ بزرگ با جمعیتی زیاد جمع شدن و درحال شعار دادن هستن که تاچشم کار میکنه پرچم فلسطین دست گرفتن و حتی یه پرچم فرانسه هم دیده نمیشه :
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73158" target="_blank">📅 16:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73155">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=DSqcyaisbmeeHiwNxhyCE9sdlHXe2mFx3y7Rqt29CCKXKD-WafYquysjJLO64_O8_iiPRxFnj-nZHwf7WUWq27nhWP1JtwV_ABpAHcJ3Zqg_9IQs6XASfj9E7Lo-GTTaD7wcywaMTYfn0Vf9RFGI29XXbqLIpcZm_081jiR68_EIj2EUFrJbR0wX5cBtBBRvO2Gozsa0hJy9GoSfHlm_MDcb43UD4Mdpcym1L5VELblNKNKXaMVZuQFTT-Yd1e0HcN8EAZfGTAc0PwTyf1EXTP4SqpxcHTrMCuJrTZHexqpF2Izq3QUrDIGBFmjpFL1GJW4_FXjc0f7vdMWMRbpO3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=DSqcyaisbmeeHiwNxhyCE9sdlHXe2mFx3y7Rqt29CCKXKD-WafYquysjJLO64_O8_iiPRxFnj-nZHwf7WUWq27nhWP1JtwV_ABpAHcJ3Zqg_9IQs6XASfj9E7Lo-GTTaD7wcywaMTYfn0Vf9RFGI29XXbqLIpcZm_081jiR68_EIj2EUFrJbR0wX5cBtBBRvO2Gozsa0hJy9GoSfHlm_MDcb43UD4Mdpcym1L5VELblNKNKXaMVZuQFTT-Yd1e0HcN8EAZfGTAc0PwTyf1EXTP4SqpxcHTrMCuJrTZHexqpF2Izq3QUrDIGBFmjpFL1GJW4_FXjc0f7vdMWMRbpO3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو بریتانیا، یه مرد جوون وارد محوطه ببرها تو پارک حیات وحش یورک‌شایر میشه و اونجا یکی از ببرها به نام آلتای بهش حمله می‌کنه و نهایتا میکُشتش!
مسئولین حیات وحش اعلام کردن که خوشبختانه ببر سالمه و داریم بررسی می‌کنیم بفهمیم اون کسخل چرا رفته داخل...
یه ویدئو از قبل ورود این مرحوم اومده که داره به یه زوج بریتانیایی میگه "
من میرم بین ببرها، ازم عکس بگیرید!
"
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73155" target="_blank">📅 15:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73154">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e5000591.mp4?token=LBoTdgp4vAN8sGvQ2-hEotYkL8IyCx2AimEJWMGHhHEDU_IVX-RLUjK4es-_tXUeS7-8zOE7bGpbS4i0yMcwX9Bp5BgdoXa1STs31dDuZ1g9iDKtbeIYh5lA_FA7ApyyB8UlTV2VQLZ1eXY7OhvC2DkTxdUkWJZR-lRfPJUPdAkLvyQqWwNjiis5NB59EWh-i67SOuYL6QQeuDm2DzS7UI2cSPg4kCAxLjm5Q73H9z6niRHX50JAThchAbXg2dg3mQN7Pmr5vWAUu38bsVdmovRs2iumfP7EiT1dPlWvEJbh1xrciHFd_gqigC3_a66ikKOASas6tXIZLuSjVM6TKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e5000591.mp4?token=LBoTdgp4vAN8sGvQ2-hEotYkL8IyCx2AimEJWMGHhHEDU_IVX-RLUjK4es-_tXUeS7-8zOE7bGpbS4i0yMcwX9Bp5BgdoXa1STs31dDuZ1g9iDKtbeIYh5lA_FA7ApyyB8UlTV2VQLZ1eXY7OhvC2DkTxdUkWJZR-lRfPJUPdAkLvyQqWwNjiis5NB59EWh-i67SOuYL6QQeuDm2DzS7UI2cSPg4kCAxLjm5Q73H9z6niRHX50JAThchAbXg2dg3mQN7Pmr5vWAUu38bsVdmovRs2iumfP7EiT1dPlWvEJbh1xrciHFd_gqigC3_a66ikKOASas6tXIZLuSjVM6TKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با نیسان از اصفهان راه افتاده و رسیده به پلیس‌راه سیستان‌ و بلوچستان؛ اونجا مأمورا بهش می‌گن می‌خوای کجا بری؟ می‌گه ایرانشهر.
مأمورا بهش می‌گن مسیر خطرناکه و توی جاده احتمال کمین گروهک ها وجود داره؛ بهتره صبر کنی چند نفر دیگه بیان تا باهم حرکت کنید، یا بین دو تا کامیون راه بیفتی تا همراهی‌ات کنن و به ایرانشهر برسی!
+
گنده‌گوز منطقه حتی نمی‌تونه امنیت جاده‌های داخل کشور رو تأمین کنه
!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73154" target="_blank">📅 14:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73153">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZMDWH_7HUVOzi2opgFP4hYcg8sCiG_xs0ShcJrJ0qYX61fR8WlS1SUQayspKttm6TulglUXYPrxSYzINJXPkZl1er7FvDwnybDnKk8-iOORX9S1eg9otzPWs6L4yVXog76PpkMTqe-0fB-uINv1fDeN3k43Ave_NODWDjKrYAa2XPPqCobM5WpY6I1edmsV1rV8mI0saxMpoczHHIl4u7nOSUuKs45jFHWYkeLjzKgL46jiMkWGRGbu4FVsEVsuxvFj-bdddS4LF3LVH62S6uXyC_XDc1AWqbfcoS9fTr9kgW4x6yFlI69J49UQdUo09apq8Njd_3BIV7zxh2vmTQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر به هوش مصنوعی گفته هر چی میگم، در جوابش بگو جمهوری اسلامی.
بعد ازش پرسیده بهترین حکومت تاریخ ایران چیه؟ اونم همچین جواب شاهکاری داده:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73153" target="_blank">📅 14:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73152">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff8e97c86a.mp4?token=HHlMeU1o5XpvTt-Q5vYiB4v0WGmlb5IMf75kh2bu6FL31AcTEgQd1zT8YryJYjM95qRZd80wSWHSGpIu-yzpXojqKdxvSLBGt0G0IoqmplaRtSM8q7fqizhWSEfBl5223x0JJCcphCCh56e93ipqWRByzAvGJ_j9db5AaBy3Y-tx9z699mke9jYf9NZ1sTLPd5AAtKMxL3sIAZNeqBF3pPbr6LriPzIkgLe5J42RFPfDMfhUICunknXe2kjU8NRdg1gJByCX7CoWmRX_ATV-muWhB1h8-ChzQacLJSrz38FpOeY76tofsMBdk_H0Y9g7EkoehfLXzWkgfLw-Vyfy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff8e97c86a.mp4?token=HHlMeU1o5XpvTt-Q5vYiB4v0WGmlb5IMf75kh2bu6FL31AcTEgQd1zT8YryJYjM95qRZd80wSWHSGpIu-yzpXojqKdxvSLBGt0G0IoqmplaRtSM8q7fqizhWSEfBl5223x0JJCcphCCh56e93ipqWRByzAvGJ_j9db5AaBy3Y-tx9z699mke9jYf9NZ1sTLPd5AAtKMxL3sIAZNeqBF3pPbr6LriPzIkgLe5J42RFPfDMfhUICunknXe2kjU8NRdg1gJByCX7CoWmRX_ATV-muWhB1h8-ChzQacLJSrz38FpOeY76tofsMBdk_H0Y9g7EkoehfLXzWkgfLw-Vyfy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دوربین مدار بسته از لحظه وقوع سیل‌ ویران‌گر در شهرستان گرمی اردبیل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73152" target="_blank">📅 14:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73151">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350f6d8da8.mp4?token=dF1VK_-NZSOuwQ56i18QdwCEpQce0HS1lL6yyvyJTjSSNTpypTuFQ_ehw6XFcbQjubgaXqBHVSD-jbVcNfoLNEmf4__ORU6K7HtSYXRyjLSCYYd7bknLIMSOc5J1lV9n3K9S1BmkgHRTMzkBYDH9N5eTcbR8BmFb2EVVZWH9cyq1yOvvLW6QSUK3X9fyDozPR7lW2tX1Mx7I0gO_OLwEKE4WMex1ut607vPZ11U6C5Eb6ltnd_ghRrGlw2dtQlc1IZK2yd7MTrohseMckvxar8JY2ohGsAlCY9taRrCU7Q80xkw1CH5fnbzkNGWMBOnjbYOZowc2o9V-XFB24SHSqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350f6d8da8.mp4?token=dF1VK_-NZSOuwQ56i18QdwCEpQce0HS1lL6yyvyJTjSSNTpypTuFQ_ehw6XFcbQjubgaXqBHVSD-jbVcNfoLNEmf4__ORU6K7HtSYXRyjLSCYYd7bknLIMSOc5J1lV9n3K9S1BmkgHRTMzkBYDH9N5eTcbR8BmFb2EVVZWH9cyq1yOvvLW6QSUK3X9fyDozPR7lW2tX1Mx7I0gO_OLwEKE4WMex1ut607vPZ11U6C5Eb6ltnd_ghRrGlw2dtQlc1IZK2yd7MTrohseMckvxar8JY2ohGsAlCY9taRrCU7Q80xkw1CH5fnbzkNGWMBOnjbYOZowc2o9V-XFB24SHSqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاش یک روس، برای سرنگون کردن پهپاد انتحاری اوکراینی با استفاده از یک نصف آجر:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73151" target="_blank">📅 13:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73150">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f347ef349.mp4?token=iYSeIrTK4z9IcSG2zx8wfZNUA2mtwwSUe-bTGF8tW0nfvoIkWmOQ3kCXZNhaayi9js8D5M954CA5myU0w0X6ykHbScR0xlwsiIPSLwTBGW3ygM0JPDB0bqn2pYhwdU098BIIZNXNHRzlS0FPZYhBLr-1z-ctjXXvJcqPuAIR6UrUs_zzfkTbqU1G3_9VbF59cw9QobgXekpM_ys5VdoC-Kw_g58ecyrEjtP2Q-NsiI9L6_BabugC_wUwyGfZS1J8F3_dVJ7GQ_y2dF8j17rxG8KkMAt2Rc5aakSMlqgJjPFJd_lOyNjy9ibdjidB4jDkkR5tMdFxGzHDV0dGy9GO7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f347ef349.mp4?token=iYSeIrTK4z9IcSG2zx8wfZNUA2mtwwSUe-bTGF8tW0nfvoIkWmOQ3kCXZNhaayi9js8D5M954CA5myU0w0X6ykHbScR0xlwsiIPSLwTBGW3ygM0JPDB0bqn2pYhwdU098BIIZNXNHRzlS0FPZYhBLr-1z-ctjXXvJcqPuAIR6UrUs_zzfkTbqU1G3_9VbF59cw9QobgXekpM_ys5VdoC-Kw_g58ecyrEjtP2Q-NsiI9L6_BabugC_wUwyGfZS1J8F3_dVJ7GQ_y2dF8j17rxG8KkMAt2Rc5aakSMlqgJjPFJd_lOyNjy9ibdjidB4jDkkR5tMdFxGzHDV0dGy9GO7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی:
«بلافاصله بعد از پست ترامپ در تروث سوشال، روسیه حمله‌ای هدفمند به یک نیروگاه در خارکیف انجام داد.
معلومه که پوتین تروث سوشال نمی‌خونه!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73150" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73149">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7cc0c459.mp4?token=BkLOYDj-mDZYYZYF4EqU4MqEIEW_GijCLs_yAqIoHnjP-Axp8qOPZr8RzftAwbJ7T-38A1XY7Yd5XX07ho3i4kCL3Grbb1SMZEpLm8RwxL6T15DBQTJtIlYL5k68I8airwx9HwmhRbGoDHj1aSmcH1mHam5nslgugAqQk3pnP3FoI3zA9jwdE9Gx2s-BOnzYTBJzhf4c3taJ4aQt3F5mlc_lcO0jlC8TZti4c-3pXDU-Nj2m6RpTBN0PfdLle5ELmBZGh-V4hHITrHr53-0WJQj4PW7s3CN7eCd3FvQ6zfCKhUyugWJlYrDS1i76wbcmC4Eger-cWXHJ-Jxrl2Tzag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7cc0c459.mp4?token=BkLOYDj-mDZYYZYF4EqU4MqEIEW_GijCLs_yAqIoHnjP-Axp8qOPZr8RzftAwbJ7T-38A1XY7Yd5XX07ho3i4kCL3Grbb1SMZEpLm8RwxL6T15DBQTJtIlYL5k68I8airwx9HwmhRbGoDHj1aSmcH1mHam5nslgugAqQk3pnP3FoI3zA9jwdE9Gx2s-BOnzYTBJzhf4c3taJ4aQt3F5mlc_lcO0jlC8TZti4c-3pXDU-Nj2m6RpTBN0PfdLle5ELmBZGh-V4hHITrHr53-0WJQj4PW7s3CN7eCd3FvQ6zfCKhUyugWJlYrDS1i76wbcmC4Eger-cWXHJ-Jxrl2Tzag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بیکارِ کنجکاو رفته بازی Resident Evil 4 رو روی نوکیا N95 دکمه‌ای پیاده کرده و همه رو به تعجب وا‌داشته :
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73149" target="_blank">📅 12:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73148">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da351ee96c.mp4?token=tBzArv_jBO4Ma74DfHQlux_WKXAkl3EkH5FOzFSDFIUp6V5H7CzyiAyhgxM55UeB20wh9Fq_iVs967p9wbznz8Ntn67rKUBZ7zzh64YAlmGdtW6keqjetBDBc6ogThrN6y711EFoM9Qr7SOoNkMDnAncXfR2mCvw7CKCzj8e9qtmcRT7Gw1lKbhxprIW-R7oqvz0LyqMnxTzbIlOgIy5CIFTkwl46X1HHYU_3lp795v54X8i_WtzVURJmUA7I1apeoyJ1RcvgDuUhsnrsNWnHScfOWzdMkyqc8ny5Hgfkbz0J6u0qSpbCNQcBdYIx-sxTa3fZEeBq4vhbyYOU2wfvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da351ee96c.mp4?token=tBzArv_jBO4Ma74DfHQlux_WKXAkl3EkH5FOzFSDFIUp6V5H7CzyiAyhgxM55UeB20wh9Fq_iVs967p9wbznz8Ntn67rKUBZ7zzh64YAlmGdtW6keqjetBDBc6ogThrN6y711EFoM9Qr7SOoNkMDnAncXfR2mCvw7CKCzj8e9qtmcRT7Gw1lKbhxprIW-R7oqvz0LyqMnxTzbIlOgIy5CIFTkwl46X1HHYU_3lp795v54X8i_WtzVURJmUA7I1apeoyJ1RcvgDuUhsnrsNWnHScfOWzdMkyqc8ny5Hgfkbz0J6u0qSpbCNQcBdYIx-sxTa3fZEeBq4vhbyYOU2wfvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیسکو مذهبی هم آنلاک شد و توی تجمعات شبانه یه رپر آوردن و حامیان حکومت دورهم میخونن و میرقصن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73148" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73147">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73147" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73147" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73146">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfgHOAhe7I113QA7-fCOEV3aIuCReLIY5wEEMOuSm2c_a6Vz39Nl90KOsNVUv98LJ_R6S4giHGxwn1tUasfYYezW9p2n_kueBSdycYzRH7vfbVaD7Xn_IM4iqoBGjQyU6mpuRe1_PTfA_Tub7GO0sdGNTV-BaYb3MTehZjHHtpFuTcqqBwT3CyChHPpM6UwFhRnC184gsNMJurtRU44NRfWYUG90BMOxEIc1pvsvBq-OcMMcM9E7j28Dq8wDSTVUdIGcQzKIoqFvfviNxeOV6hDqQ5yJ-3fosAfg9lG-sjJ0swjmFcHej1ux_W7lsJXgbPAUUWjiysUF2HVF-mr_Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
کاونتری
سویا
🆚
لوانته
ونزیا
🆚
آتالانتا
اودینزه
🆚
تورینو
نفتچی فرغانه
🆚
النصر
استقلال
🆚
الغرافه
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73146" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73145">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291083b4aa.mp4?token=UO3RJV9t-2l7cufKHQYxb485r7SPyLp_WD-ygPN0udIYgjKamM_2au2DmOweI8benN2lhWC1nRcfd9Bqh1hZWqWyI0fENHQ79tAMM01f2yU4ujfycDHvFx0Mdb3f8yhJHgVe-EurYf58ptVIg2h2CHLCcINQEGjb1pstE7fiX6mGmw96EkB6NmBe1U8By9bUS_4IUqqrHOQsQ2RRkRqfkpxFwMjiX9fzkom3DBEOxDXrfyDnm2io61xRrKL3ZdDUPz2c55Ax2Q_uH8kcMAPZ4e9-UBPS-0clXyXVd6b1YEP2hLmj9sX4E2sHOx-DmI7bqBua--l4ugHsnkM1NPXEVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291083b4aa.mp4?token=UO3RJV9t-2l7cufKHQYxb485r7SPyLp_WD-ygPN0udIYgjKamM_2au2DmOweI8benN2lhWC1nRcfd9Bqh1hZWqWyI0fENHQ79tAMM01f2yU4ujfycDHvFx0Mdb3f8yhJHgVe-EurYf58ptVIg2h2CHLCcINQEGjb1pstE7fiX6mGmw96EkB6NmBe1U8By9bUS_4IUqqrHOQsQ2RRkRqfkpxFwMjiX9fzkom3DBEOxDXrfyDnm2io61xRrKL3ZdDUPz2c55Ax2Q_uH8kcMAPZ4e9-UBPS-0clXyXVd6b1YEP2hLmj9sX4E2sHOx-DmI7bqBua--l4ugHsnkM1NPXEVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف رائفی پور به باز بودن تنگه هرمز برای همه بجز جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73145" target="_blank">📅 11:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73143">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29e4b6ff2.mp4?token=JQc4_cBl7Bst-J_53-7nMcNWd25Qcf9oFumu9zOmGTovOEFSxxZJFviOQdU0Neb4z_tXe7wSyb8ApvwgFJcJU2CNNnzTNimba-WBA86Vukfgoarc3UWnk5ot58XR3g5KsSdXx4Axiqf7kq2Uxk6Yw88BvZ33ifInw9tsVLuYno0IQMB2yjY9--wEF6e9HH40s-lRwn799oZ_s9UvJ7uqsPuV-b7L-lvivaCXh4Biy4vW89CeGr3WxlwBcXa2ULb6hwf1FPyN52XZF-RvjEDdq5PMDyKJeFZfSf4k2QXDV7JoqQqrqyiwtPgDrt8DcdgpNXTIUt7d2jXtraY--q2DlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29e4b6ff2.mp4?token=JQc4_cBl7Bst-J_53-7nMcNWd25Qcf9oFumu9zOmGTovOEFSxxZJFviOQdU0Neb4z_tXe7wSyb8ApvwgFJcJU2CNNnzTNimba-WBA86Vukfgoarc3UWnk5ot58XR3g5KsSdXx4Axiqf7kq2Uxk6Yw88BvZ33ifInw9tsVLuYno0IQMB2yjY9--wEF6e9HH40s-lRwn799oZ_s9UvJ7uqsPuV-b7L-lvivaCXh4Biy4vW89CeGr3WxlwBcXa2ULb6hwf1FPyN52XZF-RvjEDdq5PMDyKJeFZfSf4k2QXDV7JoqQqrqyiwtPgDrt8DcdgpNXTIUt7d2jXtraY--q2DlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زینب ابوطالبی، مجری صداوسیما که سال ۹۸ گفته بود «مملکت مال حزب‌اللهی‌هاست، هرکی نمی‌خواد بذاره بره»، طبق گفته محمدرضا باهنر از ایران مهاجرت کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73143" target="_blank">📅 10:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73142">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b195be8e00.mp4?token=OOTCcF_H8Ye3EL6Lt5SHVhwmen43rDQUNJZTC4NWug5IlKNdmbgXhuJ_dvOBDn0tX3CoXWOpm9JbmO4-Y1ayOCK4-I8B7ojD69udiQDv1T15mf4qQK25RiJTR6or96x8rWzgWiRBeSauNwno4ezM1lY1RB0sZK3C0T2KvXiSZtcsEmg52uaIbKKGbCqnWMpU1GkYzDjBoAQk4vbbG4W-l9lQUjqbWhrp6e5b7sPDZTv_TMAxUbTPrPlZgKjqiO24lCW8iBNbv0eeEzUiHVgu8UVZ1gnS1M4odGbCG07lf8CCiZMG4pTgod4t8CqrYYCshTHIHa0cpEcLTlkQXPvNAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b195be8e00.mp4?token=OOTCcF_H8Ye3EL6Lt5SHVhwmen43rDQUNJZTC4NWug5IlKNdmbgXhuJ_dvOBDn0tX3CoXWOpm9JbmO4-Y1ayOCK4-I8B7ojD69udiQDv1T15mf4qQK25RiJTR6or96x8rWzgWiRBeSauNwno4ezM1lY1RB0sZK3C0T2KvXiSZtcsEmg52uaIbKKGbCqnWMpU1GkYzDjBoAQk4vbbG4W-l9lQUjqbWhrp6e5b7sPDZTv_TMAxUbTPrPlZgKjqiO24lCW8iBNbv0eeEzUiHVgu8UVZ1gnS1M4odGbCG07lf8CCiZMG4pTgod4t8CqrYYCshTHIHa0cpEcLTlkQXPvNAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای این خانم در مورد کادوی روز دختر و گل‌های چند صد میلیونی که این روزا بلاگرا به پارتنرشون کادو میدن، حسابی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73142" target="_blank">📅 10:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73141">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479627e865.mp4?token=Xkfs_ByiNkMFl1YLVAwHigkEyVph8moIPmInPKMifw3QzZcVcvzUsrc2pW51ssLY1eDVPPKEOlbR83VCbgQmU-V53UPjUEEBaP58WBTOhTmhuK8kOjdx5J0hkh6NvBH5q5jDx8hB-JdeY1T8wL_WvtHmhkTm3jBg1vv-wrAlqvOKwn-029lENA8n0YpRPRnGDXSo0Y-NIQ85lsudzYkZbKm09syUm2DbhTWoieu7WFgAaoNR5zKE5id6UVBmj3PWclvDbmDsdv_w1acYD2T88z2j4fvl5PxDwi_oA9VebH7zZNVstaJ6dHf0wNLZw-2fpzR8YF3pdk2b8va76l1Nfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479627e865.mp4?token=Xkfs_ByiNkMFl1YLVAwHigkEyVph8moIPmInPKMifw3QzZcVcvzUsrc2pW51ssLY1eDVPPKEOlbR83VCbgQmU-V53UPjUEEBaP58WBTOhTmhuK8kOjdx5J0hkh6NvBH5q5jDx8hB-JdeY1T8wL_WvtHmhkTm3jBg1vv-wrAlqvOKwn-029lENA8n0YpRPRnGDXSo0Y-NIQ85lsudzYkZbKm09syUm2DbhTWoieu7WFgAaoNR5zKE5id6UVBmj3PWclvDbmDsdv_w1acYD2T88z2j4fvl5PxDwi_oA9VebH7zZNVstaJ6dHf0wNLZw-2fpzR8YF3pdk2b8va76l1Nfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شبکه یک صداوسیما:دانش آموزان معترض فرانسوی، می‌تونن بیان تو مدارس ایران که همگی فول امکانات هستن، تحصیل کنن.
شما هیچ معلمی ندارید، پلیس هم داره دستگیرتون می‌کنه.
ما اینجا کلی معلم اضافه و کلاس خالی داریم.
اینجا ما آرامش داریم و همه چیز عالیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73141" target="_blank">📅 09:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73140">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22084c4b3c.mp4?token=vajeHSL9eMHCq1BT2scYadMnWvwzahWgT4TeXMO0jOnOokZR1DxNygazKUMUZw_NZhyl89xm-B3VI0RuQAYSq-BBUzofjylroxkdqbaJ0MoPIt8rkmQ8mki1TugGtcm0qaGGCpXOB-ehUjOwQztn6OZ3Me0cyReWyb6l6_u2QauR8wREr3Atj9WiIsRdyZcPRm0gDY7qd155xe49lp2SQzLAT1ORdYHhDrtDJxTANbVA8zaX7LYuiMTJHK7bdB3YdWMhVR2lpWXSJcxypJTVwpy9OoPPyHcBD_vo-XvZMlNzJghZ8VW6d9Ok6IhpQVSwY7KxSLXORuQ2s1IhlYnteg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22084c4b3c.mp4?token=vajeHSL9eMHCq1BT2scYadMnWvwzahWgT4TeXMO0jOnOokZR1DxNygazKUMUZw_NZhyl89xm-B3VI0RuQAYSq-BBUzofjylroxkdqbaJ0MoPIt8rkmQ8mki1TugGtcm0qaGGCpXOB-ehUjOwQztn6OZ3Me0cyReWyb6l6_u2QauR8wREr3Atj9WiIsRdyZcPRm0gDY7qd155xe49lp2SQzLAT1ORdYHhDrtDJxTANbVA8zaX7LYuiMTJHK7bdB3YdWMhVR2lpWXSJcxypJTVwpy9OoPPyHcBD_vo-XvZMlNzJghZ8VW6d9Ok6IhpQVSwY7KxSLXORuQ2s1IhlYnteg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که روبیو درباره خشایارشا صحبت کرده و باعث شده عده زیادی از طرفدارای حکومت عصبی بشن، یادی کنیم از مصاحبه قدیمی خامنه‌ای درباره خشایار‌شا که دوباره وایرال شده؛ جایی که می‌گه خشایارشا با بیش از یک میلیون سرباز به یونان حمله کرد، شکست خورد و هیچ منفعت ملی‌ای برای ایران نداشت!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73140" target="_blank">📅 09:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73139">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73139" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73139" target="_blank">📅 01:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73138">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IE3PIEUyGD0WOtX6sXu5L9PZf60hARoQSopq3sJ1zyY1Bk5IrlbaClat-0pmu8jiu56VqrdaNt-gQObFu-PYIgdwb0uK72lwU3vASgzzXfuJfVOaPfqMU8Z2GYVMvbjcJmr4GBEyNzj2GCEDdsIxQaSp0VazMJ29sbEnPk2jV3uLKAtGqdVRv47xaJHVWH6dv2I-l9TfNn18cuPd7T4wkjvXlpNrjXpS6cgK_iHeAvP0OdEyOT2H2x6nZQnNZYvLty5sPEpjLjCCYT6HuylmInnrmPbcjbpz0eHp7y-E11kvY4xWvMFjXctHQ0YErZbH3s4gg4CUALt-fxuwFNYH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
[
قوانین رو در سایت مطالعه کنید
]
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/73138" target="_blank">📅 01:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73137">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtCpuISs1gRBqWhQUcj1KdK9Qy6PjbaRHUK2_SmT4h53wrOTruEsFqjaa1fNRoxbG9UJSvAqZJkvlk7xC3pwLbtQ65OAKOFVsxp3gV-JprkSy0_WJzPpvd5GiCSkFwAdlMCOEc0pNrgxdtpM54YRjxdJVxeRzaaoj7S0Hf-P3agAIppOZGUXpCP3rEbg3jQFNSPvkUu_UMCnYESlJrVwVZgDXBFNZF90XWD67VnnjE65uBhVSF_NqoopN2y6fi-GTVCUaqbCNgpWCjb9gXXPl0GIII82sNN4FM4RamITzp8HxSFZFW7DpGE8dEtKcGbMP64fomeAaIlzLb-ATEZCiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
«آمریکا با بعضی از شروط هفت‌گانه ایران موافقت کرده، اما از نظر ما پاسخ آمریکا کافی نیست.
دیپلماسی ایران تغییر کرده و دیگه اوضاع به شرایط قبل برنمی‌گرده.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/73137" target="_blank">📅 01:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73136">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ویدئوی لحظه اصابت موشک حوثی‌ها به فرودگاه ریاض
تصاویر دوربین‌های مداربسته، لحظه اصابت موشک بالستیک حوثی‌ها (انصارالله) به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض، در روز گذشته رو نشون می‌ده.
بر اساس این گزارش، دست‌کم ۱۳ نفر کشته و بیش از ۳۰۰ نفر زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/73136" target="_blank">📅 00:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73135">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13d27cb81.mp4?token=FbPEiDSuMEhL1T0Bm3XFe0oqps-S4MEGSuhv0IpkTI10mbMukS3wK2KN_xgMEte-0HUJGsxRyLSz0ys9bt0zI6lbdy_oZxNBIV42T9aV7lLjm-Kz4kW15JLGZurEZWVPFuexvdsFQYTfVhM1uyFDaGOFJQxxT4eT4QDwMmk1y_A9wy0HRdIFBkQ56PDdb7gdkrM8ZtL2wJD-S5kxaSnW4en2UmZld-ideebItHiCttCLi8PEkHFPVWpMttTGmlgdRAV5LrEC0NqqPDIP_iqosULiajiZZyWv3BSiYxiAxhudZgyaAt9e_Gtgf2OiaKpK7b3-CgmOwopF2S3O003o6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13d27cb81.mp4?token=FbPEiDSuMEhL1T0Bm3XFe0oqps-S4MEGSuhv0IpkTI10mbMukS3wK2KN_xgMEte-0HUJGsxRyLSz0ys9bt0zI6lbdy_oZxNBIV42T9aV7lLjm-Kz4kW15JLGZurEZWVPFuexvdsFQYTfVhM1uyFDaGOFJQxxT4eT4QDwMmk1y_A9wy0HRdIFBkQ56PDdb7gdkrM8ZtL2wJD-S5kxaSnW4en2UmZld-ideebItHiCttCLi8PEkHFPVWpMttTGmlgdRAV5LrEC0NqqPDIP_iqosULiajiZZyWv3BSiYxiAxhudZgyaAt9e_Gtgf2OiaKpK7b3-CgmOwopF2S3O003o6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مدارس پسرونه، اسپایدرمن تبدیل به اسپایدرعن شد :
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/73135" target="_blank">📅 23:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73134">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58aeb38.mp4?token=hME4PljF3p0uvr5KdAgIAryP_k-9eK6u_Lv_bELHzjHkBgYgLB8r3ibWTdofXLn3OM3P0zOyqOgPj0pCjtdPDzCkRa6hWafvf0U32arI9k2yW6a9rKrvXCDbfDFlXsAYKgGy12wVCbnfeiK3s_PaeW-RpGd6B04sFawf-IaUtpYMnmPLjM_XykfGIz_gS3NiKqnTQgeYfMCbQusf4Bgrboud38U2J9BRP4IeUdDSKMimXcfFRDBd43drackwmLxkzvvnnGkV59NxesBZlJd4OW0A96PQXD8KK6Hv1x4D0LvVnXOWcLcezxMRPhxnLIzBHM_Meuta_8M_VDVdP7niMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58aeb38.mp4?token=hME4PljF3p0uvr5KdAgIAryP_k-9eK6u_Lv_bELHzjHkBgYgLB8r3ibWTdofXLn3OM3P0zOyqOgPj0pCjtdPDzCkRa6hWafvf0U32arI9k2yW6a9rKrvXCDbfDFlXsAYKgGy12wVCbnfeiK3s_PaeW-RpGd6B04sFawf-IaUtpYMnmPLjM_XykfGIz_gS3NiKqnTQgeYfMCbQusf4Bgrboud38U2J9BRP4IeUdDSKMimXcfFRDBd43drackwmLxkzvvnnGkV59NxesBZlJd4OW0A96PQXD8KK6Hv1x4D0LvVnXOWcLcezxMRPhxnLIzBHM_Meuta_8M_VDVdP7niMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: اگر لازم باشد برق اتاق‌های دولت را خاموش می‌کنیم اما نمی‌گذاریم چرخ کارخانه و تولید متوقف شود. مردم همکاری کنند فشار دشمنان شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/73134" target="_blank">📅 23:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73133">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b9ee6a71.mp4?token=O-gm4X2M-YoSbWsMRa8LPVf9YIYIso7xOa6-DkL0S6NcMDN_TMWtXqatXtq2VGBp5mV2CL-UQwTDQoSgxLgPOmQq3g_ZZJlcjjsFl1n8i9W7f6rivlzcJBrOtBQkTm2G9IEwxoTcw5FHod_1ZEErFySXynKvrjIqyXmAgVQTQllAA_hHtf9f6Q4eh78zDF4IDf3PXrR5Mnr-XSsIstsHcKab8KTcp-JTk0Dk96lEiFdoE7J7LGsjOSVfGN18tE_RAsIsSYdz3u1rk_2pgmO7G9AAk-q2MsDh5PdxOwnGm3RviUzNEpREAKgHqHMrqdZ7HP2de6LBWR_20Mil59756Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b9ee6a71.mp4?token=O-gm4X2M-YoSbWsMRa8LPVf9YIYIso7xOa6-DkL0S6NcMDN_TMWtXqatXtq2VGBp5mV2CL-UQwTDQoSgxLgPOmQq3g_ZZJlcjjsFl1n8i9W7f6rivlzcJBrOtBQkTm2G9IEwxoTcw5FHod_1ZEErFySXynKvrjIqyXmAgVQTQllAA_hHtf9f6Q4eh78zDF4IDf3PXrR5Mnr-XSsIstsHcKab8KTcp-JTk0Dk96lEiFdoE7J7LGsjOSVfGN18tE_RAsIsSYdz3u1rk_2pgmO7G9AAk-q2MsDh5PdxOwnGm3RviUzNEpREAKgHqHMrqdZ7HP2de6LBWR_20Mil59756Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ مربوط به پشت‌صحنه یه تئاتره؛ جایی که همه با هم دست می‌دن و همدیگه رو بغل می‌کنن.
+ عرزشی‌ها هم از این صحنه به خشم اومدن و می‌گن باید این بساط جمع بشه؛ حالا هم افتادن به جون عوامل تئاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/73133" target="_blank">📅 22:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73132">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=gQvumnCqY7ZQGj4gw-KmzYvH-h3XZZH_4fLcvLiC7u55s63SpQprVT0EF8FbhBSISmcDcDDkmbY5BQvDQdVNLUoWJbfJdCaFWuQq_upbyLkBA5P88BRsNK7OLu_UpWVaWmNiBklJXVxaDozmncw4yJ-Pujt0I6ShHWVGVHFC-tun3V4zRxo3wfkWaJOjX1vi_qYQEZRyCPs4HY6LAm-N3t5Mlgoox_7qHAdEbcD06RRTdPGz0jNQ40s1GTwMdC5hQFdsS3IU6DR9DC4iZKeuheMoaaHxHXtLfilKIgHC_ymHVW1OUlgyVuK3s_I7Q0aZpKC2AIlgEV7oitC1PzUr9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=gQvumnCqY7ZQGj4gw-KmzYvH-h3XZZH_4fLcvLiC7u55s63SpQprVT0EF8FbhBSISmcDcDDkmbY5BQvDQdVNLUoWJbfJdCaFWuQq_upbyLkBA5P88BRsNK7OLu_UpWVaWmNiBklJXVxaDozmncw4yJ-Pujt0I6ShHWVGVHFC-tun3V4zRxo3wfkWaJOjX1vi_qYQEZRyCPs4HY6LAm-N3t5Mlgoox_7qHAdEbcD06RRTdPGz0jNQ40s1GTwMdC5hQFdsS3IU6DR9DC4iZKeuheMoaaHxHXtLfilKIgHC_ymHVW1OUlgyVuK3s_I7Q0aZpKC2AIlgEV7oitC1PzUr9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه مدعی شد سومین نفتکش از دیروز تاکنون در جنوب تنگه هرمز با مین دریایی برخورد کرده و دچار انفجار و آتش‌سوزی شده است.
سپاه هشدار داد با کشتی‌هایی که سامانه‌های ناوبری و شناسایی خود را خاموش کنند، به‌شدت برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/73132" target="_blank">📅 21:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73131">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=No3dn5eVAa2qkLZ99D5lEFQTKwE66_nHKDhzwuGDPVGNrPPNEwWj_GwScyFpGx5i_dh7m6_d5RffUqWgQZ-g69vXu0UN7owK2MYjLaF9bt1wPp9N7c3iMfIOcbnwqUPQG-QTB908CZUc9VAavBFYa3PEIvIy9Kut064VQUcYQpb1FdPodfdZkQh74LqjzGT3lXzcAPJ3UTzDlNhAka9-hMVr_QbMoDHcuhjXJ_0KebINt0ulOnApdRk29d7usY16c926Zb_yuzmiCfEBJPRCAIj7yhRceU3x_byYXljnrN5Iv4OJhqMFFT2FAEqopb3CFR0_pt6IeF0gxZjZyFelYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=No3dn5eVAa2qkLZ99D5lEFQTKwE66_nHKDhzwuGDPVGNrPPNEwWj_GwScyFpGx5i_dh7m6_d5RffUqWgQZ-g69vXu0UN7owK2MYjLaF9bt1wPp9N7c3iMfIOcbnwqUPQG-QTB908CZUc9VAavBFYa3PEIvIy9Kut064VQUcYQpb1FdPodfdZkQh74LqjzGT3lXzcAPJ3UTzDlNhAka9-hMVr_QbMoDHcuhjXJ_0KebINt0ulOnApdRk29d7usY16c926Zb_yuzmiCfEBJPRCAIj7yhRceU3x_byYXljnrN5Iv4OJhqMFFT2FAEqopb3CFR0_pt6IeF0gxZjZyFelYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم وایرال شده از جشنی که یه خونواده، برای اولین پریود دخترشون گرفتن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/73131" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73130">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=h7EoTpoEWHB2v0A25Z23_imMAaV9TPqpTQSkO1XcQRmwj6DfhmsCVQPhZmW-MQd9Y3Ov_95IGfjZxdSSniDd0fdfKJwxKB3IIob_Pabcn4cjHYI356ZLDS1agjEGeyjzSPGe7XGcjuvBQ2xPINdaMpOE7r6miR7iG7BiMV3OEKlfUmSNoLVp-9Vhsrax-IvZr6a7h-lAidcJRd1JLudcdD6MVqYv1BQGE1m3DlKByQ7K9fL0z6QGHBplnbffZ1FVqueLVYIww6Dbc9SHnljR6u_QFKnUdsg58OL7G5LyP_mDXeMse1oI9eZWItfyhdFVSor4v9w3kz2Xl5EkRctMMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=h7EoTpoEWHB2v0A25Z23_imMAaV9TPqpTQSkO1XcQRmwj6DfhmsCVQPhZmW-MQd9Y3Ov_95IGfjZxdSSniDd0fdfKJwxKB3IIob_Pabcn4cjHYI356ZLDS1agjEGeyjzSPGe7XGcjuvBQ2xPINdaMpOE7r6miR7iG7BiMV3OEKlfUmSNoLVp-9Vhsrax-IvZr6a7h-lAidcJRd1JLudcdD6MVqYv1BQGE1m3DlKByQ7K9fL0z6QGHBplnbffZ1FVqueLVYIww6Dbc9SHnljR6u_QFKnUdsg58OL7G5LyP_mDXeMse1oI9eZWItfyhdFVSor4v9w3kz2Xl5EkRctMMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سازمان انرژی اتمی: منافعمان را یا با دیپلماسی می‌گیریم یا با نبرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73130" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73126">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=RobqFStyAmnG106GKZ07yyM-RApGT5zIcm5l3fTl9DMK9hzLuxVa1A_Vpca_UsEoPm9_vfs4LS-YOzBplPOi5vhQVhwjhq0fjr1EpKDG9HVbHsmTHcpNnrqWYetCdMM0DxO2-W3cCM_bmR-mHWRcfkM7xB1cxBrA3kIlLU4QCYPxypDpiap2A-ZyEeej2SxXlf_BowRLwE4UEvNoJzuY6gMgDGSUmrSmdEhg5hcD3MnGIXyj51K0w7slcOIfi0POTLhWbmmZKqPI5zNar729SY4Nqe4fM8C9S1-pror5nqFyS1t0WR7A8TVSPMUv-7ZszI4SvPp0H_8dRpKxl5FZ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=RobqFStyAmnG106GKZ07yyM-RApGT5zIcm5l3fTl9DMK9hzLuxVa1A_Vpca_UsEoPm9_vfs4LS-YOzBplPOi5vhQVhwjhq0fjr1EpKDG9HVbHsmTHcpNnrqWYetCdMM0DxO2-W3cCM_bmR-mHWRcfkM7xB1cxBrA3kIlLU4QCYPxypDpiap2A-ZyEeej2SxXlf_BowRLwE4UEvNoJzuY6gMgDGSUmrSmdEhg5hcD3MnGIXyj51K0w7slcOIfi0POTLhWbmmZKqPI5zNar729SY4Nqe4fM8C9S1-pror5nqFyS1t0WR7A8TVSPMUv-7ZszI4SvPp0H_8dRpKxl5FZ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی امروز گسترده‌ترین رزمایش نظامی خود از ۲۸ فوریه تاکنون را با مشارکت سپاه و نیروی هوایی ارتش برگزار کرد. تصاویر منتشرشده، پرتاب پهپادهای انتحاری شاهد-۱۳۶ و موشک‌های بالستیک و پرواز جنگنده‌ها بر فراز تهران و شهرهای دیگر را نشان می‌دهد؛ تحرکاتی که می‌تواند نشانه آمادگی ایران برای دور تازه‌ای از درگیری باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73126" target="_blank">📅 20:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73125">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">محسن رضایی:
«اگه جنگ دوباره شروع بشه، خیلی از کابل‌ها، دیتاسنترها، مراکز هوش مصنوعی و زیرساخت‌های دیگه تو منطقه نابود می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73125" target="_blank">📅 19:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73124">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpCNVWhEsIZWOeR-PelaJpbaHkRdco9Yrrp2RUiVRq7bpVuEChp_aY67g_HXdkL3lVBKLdmh0jgIDJ02qQ9zYAIuI9ja43wwPQVT4EUP3yX5DPeXColkDaaD6qembIXZQz5O5uqcrL2zsHk-bPAxZGqJEkL_X-RdcSG-4JAMxwPN6w7WXBZQx6ImSR0hjh-JDb0M-_UHcgaxH6gD4Jd2Pk0yXYnXNwlFYOvzUSmwAk3D3SY6Xj1QeyxQ9SiFf6ya6SirM3Rgrf2Y-z4PMrIZfZ-1YMMauaicMUHMzPexlPzKOU-XlvYwCHzPbQpqTqEQGHYpIoOCjdt-4O6a6yFWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
«ترامپ به قاچاق روی آورده و با استخدام تعدادی مجرم که در آب‌های ساحلی عمان فعالیت می‌کنن، این کار رو پیش می‌بره.
اون هر روز ادعا می‌کنه تنگه هرمز بازه؛ اما من در پاسخ می‌گم شما مشغول قاچاق هستید، در حالی که تنگه هرمز تحت کنترل ایرانه و ما مدیریت اون رو در دست داریم.
طی چند ماه گذشته، هر شب پنج شناور مورد استفاده قاچاقچی‌ها رو در تنگه هرمز هدف قرار داده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/73124" target="_blank">📅 18:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73123">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee20290170.mp4?token=kc5SBT4TLeiR0lK6R0XOytHj4fMKMPGyyK4E7tw1rgUUCD0wKHJf47QYHmIAW1diONpLgnHbclCxVQpIdwj_vgALLLQpd_R_-j-zPtQrfnKgjshLruUSOKf33ViG9kOyuXTFbRZXEmdq6hiTkVA3wUd8OyoPCOJJy38sPa5NjXzpxX5j1xOZNRsa2XUm4GPuYQI6BjYfTCMOfhKtJIay2wom75qNcvVfO4qINGR0qJXqKKHs2B1tzgq7dfIlKBxaokU4mZbN6bz47zPffDtfcAKGwRtFslLEKd_Tu_DQzrSMTb9uslszLQsOni3MOTHlJ11vog3sBLvpJ2xUlJM0tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee20290170.mp4?token=kc5SBT4TLeiR0lK6R0XOytHj4fMKMPGyyK4E7tw1rgUUCD0wKHJf47QYHmIAW1diONpLgnHbclCxVQpIdwj_vgALLLQpd_R_-j-zPtQrfnKgjshLruUSOKf33ViG9kOyuXTFbRZXEmdq6hiTkVA3wUd8OyoPCOJJy38sPa5NjXzpxX5j1xOZNRsa2XUm4GPuYQI6BjYfTCMOfhKtJIay2wom75qNcvVfO4qINGR0qJXqKKHs2B1tzgq7dfIlKBxaokU4mZbN6bz47zPffDtfcAKGwRtFslLEKd_Tu_DQzrSMTb9uslszLQsOni3MOTHlJ11vog3sBLvpJ2xUlJM0tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارشات رسانه‌های عربی حوثی ها مجددا به فرودگاه ریاض حمله کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/73123" target="_blank">📅 18:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73122">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">زلنسکی در گفت‌وگو با باراک راوید:
«اعلام آتش‌بس برای من هم خبر جدیدی بود. اما اگر روس‌ها با آتش‌بس در حوزه انرژی موافقت کنن، اوکراین هم موافقت خواهد کرد.
اگر رئیس‌جمهور ترامپ این توافق رو با پوتین مذاکره کرده، لطفاً به ما بگید آتش‌بس از چه زمانی شروع می‌شه. ما آماده‌ایم و این توافق رو می‌پذیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73122" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73121">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1MrSbSErQrr501KVGDHDeTP2MkLLy27qAEV04AMhMFFOtSGM6TJcQRtHdgdThLnI7OoP683VrSbkLIW-BitH4xtnZAorObOGHj8cv6vglW8NWNilmKSmmooDJJvIuHikW5tPnocwV5M6qcZLU7wYk-tqTu9L32vodaRQO2as3hIg9WwlYuM0_OeV4nq-6tIKeDq0j8bpqjH9Kt7PkyT5_QBNvlMhljcLfl1DEnGbS1Rh00W1ZNfsb7R7_4sQFg0TjjtqMjZHKXpQ5x8tghBRxZfftSFZGEwLQy-CxBA4JUJ9beDSQU1TuSHXYwC_sAGWzbtyd5-SNhtvKqkdkd5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ از آتش‌بس انرژی بین روسیه و اوکراین خبر داد
«از همین لحظه، آتش‌بس در حوزه انرژی در جنگ روسیه و اوکراین برقرار می‌شه.
هر دو طرف با این توافق موافقت کردن. این آتش‌بس رو نقض نکنید!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73121" target="_blank">📅 18:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73120">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73120" target="_blank">📅 18:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73119">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uaum86tq2ivSalTWpf6cU1j28g6xFeFSL54ELVVCLBMML9-Vuab4auPrSh_wbcsiPfcPywOULjTs8mOvTPrMvwpz_fezM2_8TrOhdHDDUsijuRIHWrEV7QsE5qCAK7T2jxiG5Xm1GhnpUcxVB8qKMkeWWV0ujjkXL5H10-IMufRVEdiop0HVEjov-eE4n_P-JGuO1quWvmYAi_P3SGR_Ghp13DFoxmCFXnHMMink8kckxu7Mr0pjwNOW7KP8ELLKnfELvvnNYBVeYvhiB7vr4-xz7NGMae2Hi0UdQi8JgErleFSR5lSD-Tb_gvDXXPqETHqn6xZx-q-U3JhkdNvMmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز منچستر سیتی
🆚
لیورپول
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
منچستر سیتی: ۵ برد و ۱۴ گل زده
لیورپول: ۴ برد، ۱ تساوی و ۸ گل زده
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73119" target="_blank">📅 18:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73118">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6d17c940.mp4?token=jTCHfaCQLF3sZeQzNrU_KjUNGhHXo60i_icZj0x_d45gPV6NnoAXmKf0vVdZjwIEU0AntQlgUbiu03m1j0zmHWRJ3edX80W5ljxwr0niqAQgRk8pP_hSdP9aE-AIldwdDfy1T4UWmtOTTR6lw9wtl6Kbl4lbYRgP8hFzFN2LfxTChdvpGjsnQvRtUE112fPCw-nKe9qw-LJfX1vxi0J6WeK9barTRdD1TzgefccQU9AI-tEh9hRExyNkiapG4dYOHl6tHuuIEJp9ODgK1iZR9DOV8dHsXjvaDYgi58VNO4aq3RA4igaVwXyH1JZbO8frLjSHAr-HBY7Hw2hXSYBaZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6d17c940.mp4?token=jTCHfaCQLF3sZeQzNrU_KjUNGhHXo60i_icZj0x_d45gPV6NnoAXmKf0vVdZjwIEU0AntQlgUbiu03m1j0zmHWRJ3edX80W5ljxwr0niqAQgRk8pP_hSdP9aE-AIldwdDfy1T4UWmtOTTR6lw9wtl6Kbl4lbYRgP8hFzFN2LfxTChdvpGjsnQvRtUE112fPCw-nKe9qw-LJfX1vxi0J6WeK9barTRdD1TzgefccQU9AI-tEh9hRExyNkiapG4dYOHl6tHuuIEJp9ODgK1iZR9DOV8dHsXjvaDYgi58VNO4aq3RA4igaVwXyH1JZbO8frLjSHAr-HBY7Hw2hXSYBaZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
«نمی‌دونم این ماجرا چطور تموم می‌شه؛ هیچ‌وقت نمی‌شه از قبل دونست پایانش چطوریه. دیوار برلین هم بالاخره یه روز، یهو فرو ریخت.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73118" target="_blank">📅 17:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73117">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=SiHPqy6L5hs-uH8lZPesU6VQRx_Nh6xpwnZ7zwM26K3TYtJIDF-sQ13hcX4YA1nZMnu7ujuCkZsS2Aj8EldX_fEmR-hKPLLDZnILmN1hmqVOnjfIz8jdzhT7GWzpDPCEtH06umoizloBWN2pljgfbM7dN2wMVJ4J6jZ0So3FxFdWsEKtaBs2--4RPv5g7OFPg-yrkYmBSPeGucLWPwWClKl1zXW7KD1SlObbDdufIn1Qn5-HA_3fawmIuvvjXaNEYZizpVZ4tnRdHsH3RFLRP8Y6JETZh5aBlvIM530-kW049QiKomTgmmVvZiccmsXEZ1sBGooezfzaANOsjU5DJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=SiHPqy6L5hs-uH8lZPesU6VQRx_Nh6xpwnZ7zwM26K3TYtJIDF-sQ13hcX4YA1nZMnu7ujuCkZsS2Aj8EldX_fEmR-hKPLLDZnILmN1hmqVOnjfIz8jdzhT7GWzpDPCEtH06umoizloBWN2pljgfbM7dN2wMVJ4J6jZ0So3FxFdWsEKtaBs2--4RPv5g7OFPg-yrkYmBSPeGucLWPwWClKl1zXW7KD1SlObbDdufIn1Qn5-HA_3fawmIuvvjXaNEYZizpVZ4tnRdHsH3RFLRP8Y6JETZh5aBlvIM530-kW049QiKomTgmmVvZiccmsXEZ1sBGooezfzaANOsjU5DJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
«اگه این ایرانی‌ها کشورشون رو دوست دارن، خب تبریک می‌گم؛ می‌تونن همون‌جا بمونن!
این فشار مستقیماً به نخبگان و مقام‌های حکومتی ضربه می‌زنه؛ دیگه نمی‌تونن برن لندن و اقوامشون رو ببینن، تو پاریس به دیدن دوست‌دخترهاشون برن یا به پول‌هاشون در سوئیس دسترسی داشته باشن.
اونا از دنیا جدا شدن و ما به ادامه این فشارها ادامه می‌دیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73117" target="_blank">📅 17:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73116">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=duWKo9FrU4SVHvK-jeWmxpRpz9Fod-M0NRPi-5HZYapmFehN2aoda1S5leVHO5El3EtJE2dGLRRpKpT7PUyGAJC03VoMJ2tjOTsh2OHHBf8bMPGvsY_c4r482glnlNP6BllbbwyFDYe8_Y9NOAGECD1k36tJBnJ30fjzaNIPj3tIJycykrSykL-cLgt5nN1X6hlgUaVllytwWJQbRZNBF6MZNsQ3Y1XPBreYZXWRX6rQF0vs2n-KoHPGRrpyQ2Lkore_RB_fj8LTtYnYYtmb1T5q4oq7iRX-BQUkALUCdU9XaJ1fGnrtaSFoItHz82-kTSi9Idtlx_25V75zwhj0EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=duWKo9FrU4SVHvK-jeWmxpRpz9Fod-M0NRPi-5HZYapmFehN2aoda1S5leVHO5El3EtJE2dGLRRpKpT7PUyGAJC03VoMJ2tjOTsh2OHHBf8bMPGvsY_c4r482glnlNP6BllbbwyFDYe8_Y9NOAGECD1k36tJBnJ30fjzaNIPj3tIJycykrSykL-cLgt5nN1X6hlgUaVllytwWJQbRZNBF6MZNsQ3Y1XPBreYZXWRX6rQF0vs2n-KoHPGRrpyQ2Lkore_RB_fj8LTtYnYYtmb1T5q4oq7iRX-BQUkALUCdU9XaJ1fGnrtaSFoItHz82-kTSi9Idtlx_25V75zwhj0EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«بزرگ‌ترین بازنده در این ماجرا، حکومت ایرانه.
اونا سعی کردن با بستن تنگه هرمز، مسیر عبور و مرور رو تحت فشار قرار بدن؛ اما این کارشون جواب نداد.
بعد تلاش کردن با بالا بردن قیمت گازوئیل، فشار ایجاد کنن؛ اما این یکی هم دیگه جواب نمی‌ده.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73116" target="_blank">📅 17:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73115">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d595a9a29.mp4?token=jZt0fx4lMsg7ZBq3XEypNYsIMhhjO4GCXJoTH25i7UWDby12aJfEoV0PZaPJwEBOGP7cFUbUtIWTq33uzO_xpM22XRhn-7YWgzAFttW84LsdhEV9vWvCZiKn1oTJw3_sYN0CdRGOHFlhYo5s0ZmCxIKD9t8KF9znpAlKmbhwSGAtEOmCMWgQOXnsqr9x9XRxyRJsCSSRSQ0MN7cjnc-keQ1TmxtUBvwDkEyszGPVWWfIWpo66XeWgIdVNGe8DUIxcx5oN5v7Ncb4ERr2tiAt9kGw-ll3OA9MpDNTxdNklvQzjuRCUydp7RLbam5RqV-RZgTStTo_ueBBoVxDVDkBUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d595a9a29.mp4?token=jZt0fx4lMsg7ZBq3XEypNYsIMhhjO4GCXJoTH25i7UWDby12aJfEoV0PZaPJwEBOGP7cFUbUtIWTq33uzO_xpM22XRhn-7YWgzAFttW84LsdhEV9vWvCZiKn1oTJw3_sYN0CdRGOHFlhYo5s0ZmCxIKD9t8KF9znpAlKmbhwSGAtEOmCMWgQOXnsqr9x9XRxyRJsCSSRSQ0MN7cjnc-keQ1TmxtUBvwDkEyszGPVWWfIWpo66XeWgIdVNGe8DUIxcx5oN5v7Ncb4ERr2tiAt9kGw-ll3OA9MpDNTxdNklvQzjuRCUydp7RLbam5RqV-RZgTStTo_ueBBoVxDVDkBUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«کارگرها دیگه سر کار حاضر نمی‌شن.
ایران به بازار دلار دسترسی نداره، برای همین کاری که می‌کنه، چاپ کردن پول بیشتره.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73115" target="_blank">📅 17:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73114">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbe1e496c.mp4?token=ofZQ-lcs_LO6L1n-y5VpzH4yxgJgrVwr9exaBQXPXvdkN2cHLLZzE8g6gb6iAucmvfiZLk4NlK-d2H3sF48PENg7jzCKfMLPT2nXF3F57oibQWTXEl3l2wpAaZdPEjhy-Uy31_zzV85sQaMo0S7YeJRJronTZQXl9zYp9WlMw9Z0IqYL7_Er6iZ6MM1RZ0hDk4-qn-X5jMzKyCwcBIgJlCjFsU2RSdSezGfPSFXu9z6ZA145T0T2-9Fz7kAUjEmAOiH6LmH-nFbuYa-0A_6YvPTsCZY5lRry4kYyLWe7nZy4w33GIdZo-0vOc5H4A2Jre0UheTXWYnT-EwQwC3l3yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbe1e496c.mp4?token=ofZQ-lcs_LO6L1n-y5VpzH4yxgJgrVwr9exaBQXPXvdkN2cHLLZzE8g6gb6iAucmvfiZLk4NlK-d2H3sF48PENg7jzCKfMLPT2nXF3F57oibQWTXEl3l2wpAaZdPEjhy-Uy31_zzV85sQaMo0S7YeJRJronTZQXl9zYp9WlMw9Z0IqYL7_Er6iZ6MM1RZ0hDk4-qn-X5jMzKyCwcBIgJlCjFsU2RSdSezGfPSFXu9z6ZA145T0T2-9Fz7kAUjEmAOiH6LmH-nFbuYa-0A_6YvPTsCZY5lRry4kYyLWe7nZy4w33GIdZo-0vOc5H4A2Jre0UheTXWYnT-EwQwC3l3yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«ایران دیگه هیچ محموله نفتی‌ای در مسیر انتقال نداره. جریان نقدی‌شون منفی شده و ما راهشون رو بستیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73114" target="_blank">📅 17:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73113">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aafe668bc.mp4?token=Cx5qZD3TQKk_GaIodRWA4iLX8920zZ4KX1UDlb2gbaqK1X-tLphHeKqKXx_C6VBls8n-vTfTg9X_Sfv-fcnmSzoeI6Negi2dmMH8BtYXrtLNmykSQwxcvl7A62EHm29dB9WlVgCfDqDGmr1ZhCjMBf1ifQ0rLdG-NTO0TvSrel4EDWtmuiyWXmPeKxnBvZfVZawycWmoMbhj82_bVKmUCJSUCDcJbn10KVhBYydLbXdCh-P_RxZ4xxiO3-VEZljL5c-6ox34I4cY0qgNsBC33vpknh7ioErUvA-DUbJHpF8HLPYiqBFfxMahDiuMplsjOK8K8N4Hbd9ePfu7-3H7hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aafe668bc.mp4?token=Cx5qZD3TQKk_GaIodRWA4iLX8920zZ4KX1UDlb2gbaqK1X-tLphHeKqKXx_C6VBls8n-vTfTg9X_Sfv-fcnmSzoeI6Negi2dmMH8BtYXrtLNmykSQwxcvl7A62EHm29dB9WlVgCfDqDGmr1ZhCjMBf1ifQ0rLdG-NTO0TvSrel4EDWtmuiyWXmPeKxnBvZfVZawycWmoMbhj82_bVKmUCJSUCDcJbn10KVhBYydLbXdCh-P_RxZ4xxiO3-VEZljL5c-6ox34I4cY0qgNsBC33vpknh7ioErUvA-DUbJHpF8HLPYiqBFfxMahDiuMplsjOK8K8N4Hbd9ePfu7-3H7hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«همون‌طور که رئیس‌جمهور گفته، انتظار نداره درگیری نظامی تا قبل از انتخابات میان‌دوره‌ای اتفاق بیفته؛ دست‌کم نه تا بعد از اون.
نمی‌دونم معادل عبارت «تسلیم شدن و درخواست توقف» به فارسی چیه، اما ایرانی‌ها بالاخره به جایی می‌رسن که از آمریکا درخواست کنن دست از فشار برداره و تسلیم می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73113" target="_blank">📅 17:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73112">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=EQ0OHdQkO1qE3gNMr3C8XtP3zEU7ThdieGJ8wwcYmT4eEex5MzgmPoAs7hz-x7FLOCmXhGol-YrI1kgX0yaL89svvgIYZ6vjx7Y27D-peNEFqhgwsVjOihy1wlkXWSQPJxtyR_QNf6m-Agq13MGk_5Na_pCT5IuMVbiwj4DgQQ95L7dHOcJh3clBvMXd3QL5cFhqDWOKwFbeTu2c46of5yRUzLjj6Sqip2VWe7CTn5KbNL9hWvs9th79TJYGJIQDPFvkhapBgAeoUAftn1xmyKSZSuhVGk3ea5ZX_jjtd0NhTB953-NLxiQh9iK3m67uvVTl1MOFgxH7kjPDGkJMDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=EQ0OHdQkO1qE3gNMr3C8XtP3zEU7ThdieGJ8wwcYmT4eEex5MzgmPoAs7hz-x7FLOCmXhGol-YrI1kgX0yaL89svvgIYZ6vjx7Y27D-peNEFqhgwsVjOihy1wlkXWSQPJxtyR_QNf6m-Agq13MGk_5Na_pCT5IuMVbiwj4DgQQ95L7dHOcJh3clBvMXd3QL5cFhqDWOKwFbeTu2c46of5yRUzLjj6Sqip2VWe7CTn5KbNL9hWvs9th79TJYGJIQDPFvkhapBgAeoUAftn1xmyKSZSuhVGk3ea5ZX_jjtd0NhTB953-NLxiQh9iK3m67uvVTl1MOFgxH7kjPDGkJMDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی یک کشتی در مسیر جنوبی تنگهٔ هرمز بر اثر اصابت یک پرتابه:
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73112" target="_blank">📅 16:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73111">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صدای دو انفجار از طرف تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73111" target="_blank">📅 16:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73110">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=DyAuzq1ZiS6BzFIShfq93W_NGThGOHWjpIMOXTdSHu4A8iv7NVASgSSokV-pwetwj_VQYiVQlxvSFYg1BNo8_lIAm51G1gYbvRvjK4qi2qmYq_wsc9-LMF1oK0MzPJkUc4jjhBQG_kgjQzCB6kUVCgDKJZYTJjYNy5N1g5cFUlQClcMBe46Dy3XKE8M_1TBBNGJetNfbCMJRFSIqyFK2IZvjbbbGr73BtGGIhEyyZKboIImg8_eMAmwfuQBWots4NuqoTG-IK_lhAyVj5Tt9fPKdnWfFyd37QtpTJHFOd_-IYrC8iHTSYyulRTokpfljFdcgROS9isna0kxefeuzhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=DyAuzq1ZiS6BzFIShfq93W_NGThGOHWjpIMOXTdSHu4A8iv7NVASgSSokV-pwetwj_VQYiVQlxvSFYg1BNo8_lIAm51G1gYbvRvjK4qi2qmYq_wsc9-LMF1oK0MzPJkUc4jjhBQG_kgjQzCB6kUVCgDKJZYTJjYNy5N1g5cFUlQClcMBe46Dy3XKE8M_1TBBNGJetNfbCMJRFSIqyFK2IZvjbbbGr73BtGGIhEyyZKboIImg8_eMAmwfuQBWots4NuqoTG-IK_lhAyVj5Tt9fPKdnWfFyd37QtpTJHFOd_-IYrC8iHTSYyulRTokpfljFdcgROS9isna0kxefeuzhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس سازمان مدیریت بحران کشور: احتمالاً در ۴ ماه پایانی سال کسری انرژی خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73110" target="_blank">📅 16:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73109">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=muzkdXAEIrvFyoQzlOe8VExccmHLJ2nYiZx1_RTxgGl-fZTr9EdBCotBcZYAVDuHAJMK4l50igEVq_YozbhkvSNAzCBpkDH6-wqMvK15aMiF384laHAlRmPAUGbfZP0euKGThAddoaa_TTNl3KemvMzzqvD1k1yXWATHkF2-zFEVhIz5eBeMOrg1qPlDBViYbX5IPVwztFEkXAnJMMjlLlzmhYBiDUPxCczcwfT7EpwW80lnomV59c6jOjxVwOwP81HAX2_K_BsB76Inv20Cwh1HtdOy0j9i5PuNLMwpDLK8begxh6oRit4EM9g69yp203kl9887RzZosHymVvL5Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=muzkdXAEIrvFyoQzlOe8VExccmHLJ2nYiZx1_RTxgGl-fZTr9EdBCotBcZYAVDuHAJMK4l50igEVq_YozbhkvSNAzCBpkDH6-wqMvK15aMiF384laHAlRmPAUGbfZP0euKGThAddoaa_TTNl3KemvMzzqvD1k1yXWATHkF2-zFEVhIz5eBeMOrg1qPlDBViYbX5IPVwztFEkXAnJMMjlLlzmhYBiDUPxCczcwfT7EpwW80lnomV59c6jOjxVwOwP81HAX2_K_BsB76Inv20Cwh1HtdOy0j9i5PuNLMwpDLK8begxh6oRit4EM9g69yp203kl9887RzZosHymVvL5Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا بچه مچه با خودتون نبرید طلافروشی، یا اگه میبرید با طناب ببندینش به خودتون که همچین منظره‌ای خلق نکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73109" target="_blank">📅 15:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73106">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=iCGY4w_zjE33oSZzjifQAdrx0bdV4dq9ovHrDAozZexMIKpSLJ_VZxyaz_d0wIOIw6dW999RwpVtelRbQBux1cqXN0yBXRB9qlC7dFtC89EBMd-7Ubo2VSi6_tDTxuQ4KhgqmGDPUCnDTYqZQCpV2ZenKULrpfhbkFl-SSgK06oz0ogLq-9-Y5u0WEQGUsirqvHOqnrLLCzko1wNLMbtJ8NprZEL4OJldFrs5wMxplbVHTzZs27LRc_KC2rmnvwlffRWzA_ak6m9xpu0xdJnZgHIOcb9LE2P_YtrGWTzocM55Epc7E9lhsdEKGy06jJHNfbqpp32XP5Ae9R73cUZoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=iCGY4w_zjE33oSZzjifQAdrx0bdV4dq9ovHrDAozZexMIKpSLJ_VZxyaz_d0wIOIw6dW999RwpVtelRbQBux1cqXN0yBXRB9qlC7dFtC89EBMd-7Ubo2VSi6_tDTxuQ4KhgqmGDPUCnDTYqZQCpV2ZenKULrpfhbkFl-SSgK06oz0ogLq-9-Y5u0WEQGUsirqvHOqnrLLCzko1wNLMbtJ8NprZEL4OJldFrs5wMxplbVHTzZs27LRc_KC2rmnvwlffRWzA_ak6m9xpu0xdJnZgHIOcb9LE2P_YtrGWTzocM55Epc7E9lhsdEKGy06jJHNfbqpp32XP5Ae9R73cUZoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت گرگان بعد از سیلاب ساعاتی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73106" target="_blank">📅 15:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73105">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=J-C9RGxVzgQtmVwsLsOuKxliyAoighojVZTDoI-YbRZtRIBvOz501V7FpzFaON7ijekY23bmuoktdVlh3UDrfNq6rZm4LDD7Dy6tQtbPvFzGRs1eQMDqK0MojLc9AyxwyaGaNxANhUuMxSmiXNC1Yrtp3ywlzgwHmlnoQfJ0XGSO-yL0pkLy9o8W_x7hYE4GP2WQjE4ffPD2S8O1AmMPOGfTYQxNdeiDnHXg4SsiBEOLLet6-nZsapnaOIw2Z-FB56x73JYGrTFavHNAZT9i_jnzcnbdQXfhTkL3g4xhPwenqj960tpATKnI5CsYny2YLRha2IodcQz3_jOZVo7piQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=J-C9RGxVzgQtmVwsLsOuKxliyAoighojVZTDoI-YbRZtRIBvOz501V7FpzFaON7ijekY23bmuoktdVlh3UDrfNq6rZm4LDD7Dy6tQtbPvFzGRs1eQMDqK0MojLc9AyxwyaGaNxANhUuMxSmiXNC1Yrtp3ywlzgwHmlnoQfJ0XGSO-yL0pkLy9o8W_x7hYE4GP2WQjE4ffPD2S8O1AmMPOGfTYQxNdeiDnHXg4SsiBEOLLet6-nZsapnaOIw2Z-FB56x73JYGrTFavHNAZT9i_jnzcnbdQXfhTkL3g4xhPwenqj960tpATKnI5CsYny2YLRha2IodcQz3_jOZVo7piQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف:
من به مسئولین گفتم، با برجامی که کونتون رو پاک میکنین، فردا باید دماغ‌تون پاک کنین!
ما کشورهای منطقه رو تهدید می‌بینیم، برای همین سفرای ما در منطقه جا بازرگان و دیپلمات، نماینده سپاه قدس هستن.
ما همه چیزو تهدید می بینیم، زن رو تهدید دیدیم، اینترنت رو تهدید دیدیم، کشورای منطقه رو تهدید دیدیم، ما حتی حجاب هم خاکریز می‌بینیم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73105" target="_blank">📅 14:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73104">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=fLTTLDBNzN6usMb4cQhyPFp9Y3e3UELCbMIwa7v7HAHpEDWg6ievdwtoaFviZJYpqXeiNQ8Ag7TtPFeoihCP1_9xSEnvp_bIH7_sAAt0FJ5XxG1dC3eiikhWqvIqDG1FAiFTUQmJ2YddDEClnlDYtwojQ4LdDXEX-3rVuSSoWt-R9s9k2gUHhxcGkFCso-ACEUz7IFCotfscNEusZQmgmHOgIFH8rxAH1M4Yq5OOPBDJD87D2RESRP2QufoPfHgH-M7RUzL8Ileu9X-CJSV8JUCbbnijjA-oYk8mhBqK0XmRrl_nCnaT4Nb9pTO9-k8ssX3sDnW12_mYWKc5ZRSrXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=fLTTLDBNzN6usMb4cQhyPFp9Y3e3UELCbMIwa7v7HAHpEDWg6ievdwtoaFviZJYpqXeiNQ8Ag7TtPFeoihCP1_9xSEnvp_bIH7_sAAt0FJ5XxG1dC3eiikhWqvIqDG1FAiFTUQmJ2YddDEClnlDYtwojQ4LdDXEX-3rVuSSoWt-R9s9k2gUHhxcGkFCso-ACEUz7IFCotfscNEusZQmgmHOgIFH8rxAH1M4Yq5OOPBDJD87D2RESRP2QufoPfHgH-M7RUzL8Ileu9X-CJSV8JUCbbnijjA-oYk8mhBqK0XmRrl_nCnaT4Nb9pTO9-k8ssX3sDnW12_mYWKc5ZRSrXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری منتشر شده است که لحظه حمله حوثی‌ها به فرودگاه بین‌المللی ملک خالد در ریاض را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73104" target="_blank">📅 13:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73103">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s42bU_9xIuO6sMXe8_ZsSvd6bFlXko9F3RozSJvFu3dA0-EMIAMGzEENTMMVPnMNwooPb8wlmraNIQfSOAedPRhrZYI7i3O9V7eykMloVa47JV2XHn4jYl1n3gQASxoDiUEyt9hyPgwEVNO0B1JRIwlvcDQNqUsuODpuYCcCLynILa7y82Px7IzClIkKEqYcMSMkpr1oAP3_UmpNQHHGQiM8ZMyzJcxgUy5v1iK5HOn6O11UxbkH9li6ZxoKU4RCYhL4E1WAXwGX08g4Du9W4IA44HSoQNb4zuWHMuXq-MEgQU20FCv1RQc3Fx1Z9lNi8aSIffLPK8wK9SJNas72hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی دختر، بر دختران سربلند و آزاده‌ی ایران‌زمین فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73103" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73102">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzHECMmwD1Qpfmn8Pmwu3vehA6BsQlEapEU6yRj2-BZIzbUrQPkGfqmAnCsjQnCnjRjiLqgIdy1sCbtQe8v1jGlrXkL8kYcf0niYrc1EHArqSV_W7-ehhVXIxOX2Zvxl_C3dEOvQQENBB1eJ8QyDL7jZth-01lhnROeLK9RfHcBVZalk9yMrWXaPZ1nWI1G1lbR2yCgY9MRESVeI8amc1KhR1dDGelFu5dhEacx8cJDGpT7lG0MkoL0hCp7opZIzq9wj27vU8KNXAYpSJA-i3BmM702HfBMBEOFxpONTgvBHCHPT-MDyGTz6WWSFZKWh9uHLaHcYCgX-t7cj6PznOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست موشکی از جنوب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73102" target="_blank">📅 12:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73101">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=nlcC0tqs1uJ9kvbNkVu2-c0wyOA9s2KZhzT865kK0JY3nJcYQ6uD3ZuqN4hjeJJ2h_oPGY_Hk5ff9UjprGNRbSgKd36ftCQp1nmuhnPX-27wttqRPvUDeol5s6Cg0qJEWKhtcFVLNWHX2oWl0FY9_UexNfA8j6utV6WpQ9e04FntJpA64jsRgRW7AKF7QGhHmpj36cFJqJx-kpGv7Kzvk_bVqa7DyJj1-yKOh3Y1yfNyqPIbd5d1NnRCut43XM9gHcBPijrJuC2MVGRLziCTDj4R_wDgpnUUUJ153z1JFTW_hhaMpoo0xrF_IPnEdXpDLLEn-BN5VGDCtUDUqeqFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=nlcC0tqs1uJ9kvbNkVu2-c0wyOA9s2KZhzT865kK0JY3nJcYQ6uD3ZuqN4hjeJJ2h_oPGY_Hk5ff9UjprGNRbSgKd36ftCQp1nmuhnPX-27wttqRPvUDeol5s6Cg0qJEWKhtcFVLNWHX2oWl0FY9_UexNfA8j6utV6WpQ9e04FntJpA64jsRgRW7AKF7QGhHmpj36cFJqJx-kpGv7Kzvk_bVqa7DyJj1-yKOh3Y1yfNyqPIbd5d1NnRCut43XM9gHcBPijrJuC2MVGRLziCTDj4R_wDgpnUUUJ153z1JFTW_hhaMpoo0xrF_IPnEdXpDLLEn-BN5VGDCtUDUqeqFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: یک کشتی باری در دریای عمان هدف حمله آمریکا قرار گرفت
فرماندهی مرکزی آمریکا (سنتکام) اعلام کرد در ۱۰ اکتبر، یک کشتی باری با پرچم پاناما به نام Ocean Molica که پیش‌تر از یکی از بنادر ایران حرکت کرده بود، پس از بی‌توجهی به هشدارهای مکرر و تلاش برای عبور از محاصره دریایی، هدف مهمات دقیق یک جنگنده آمریکایی قرار گرفت.
به گفته سنتکام، این حمله پیشرانه کشتی را از کار انداخت و خدمه آسیبی ندیدند. همچنین، طی سه ماه اجرای محاصره دریایی، ۴ کشتی از کار انداخته و ۱۳۵ کشتی دیگر وادار به تغییر مسیر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73101" target="_blank">📅 12:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73099">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=tNotZQL2lUIpr5KaaF8cIdfTCTqi1dod5qapoHA_7nWc_cXolsKhwrPMiv96PqiP45ZnVVBHQOShAh9BxpUatfrbV1463RZzjsTb6Pa_zJT67_ZeNQPjdI2TZ-wC91NV7gfl4Z3FpAmsAucXaeQCxHoMgR1eVKvYtMHjn6XWFtUwzivsodTu67WFpqYe8GJcbWk2sbuRy2zVA6RqutFN6jX0rMFwOPIdRUeSO3CvoeWhrs-z0FHJNm2bVccSQKd6CZVvG_MyEY1xiFkwj84zvlwAkHSaJSeZ_Rrm2qOn30uLUydQ0A0K83J00PZ6jbR6OswfklNx_gsqJ6UcnJB_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=tNotZQL2lUIpr5KaaF8cIdfTCTqi1dod5qapoHA_7nWc_cXolsKhwrPMiv96PqiP45ZnVVBHQOShAh9BxpUatfrbV1463RZzjsTb6Pa_zJT67_ZeNQPjdI2TZ-wC91NV7gfl4Z3FpAmsAucXaeQCxHoMgR1eVKvYtMHjn6XWFtUwzivsodTu67WFpqYe8GJcbWk2sbuRy2zVA6RqutFN6jX0rMFwOPIdRUeSO3CvoeWhrs-z0FHJNm2bVccSQKd6CZVvG_MyEY1xiFkwj84zvlwAkHSaJSeZ_Rrm2qOn30uLUydQ0A0K83J00PZ6jbR6OswfklNx_gsqJ6UcnJB_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی رفتن ویدیوی رپ هوش‌مصنوعیِ بی‌بی رو نشون خودش دادن، اونم به شوخی میگه از کجا میدونید شاید واقعی باشه:)
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73099" target="_blank">📅 11:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73098">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مقام‌های سعودی اعلام کردند در حمله روز شنبه به فرودگاه ملک خالد ریاض، ۱۲ نفر کشته و ۳۰۹ نفر زخمی شدند.
ملیت کشته‌شدگان:
عربستان سعودی: ۴ نفر
بنگلادش: ۲ نفر
آمریکا: ۱ نفر
مصر: ۱ نفر
اردن: ۱ نفر
سوریه: ۱ نفر
فلسطین: ۱ نفر
سودان: ۱ نفر
برخی مجروحان در وضعیت وخیم قرار دارند و حمله خساراتی به تأسیسات فرودگاه وارد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73098" target="_blank">📅 11:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73097">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=tNfY5uw6gXwviPz5thx-OSxIz8lEnc9ErOH3bc8GsQdNu-kP3PifSjjcIsrBQRxMwhoCBVNtYxyObvZBh1AsKXCcleIQE6-KFaThpuW3Av12AWhPfwTUwlU2dXMrJll0JMmwENp5BDuqrhfx0VvwUP_DGjdXk7hEWNX9FiPZTGzQC5rvgpmcRs_w1N7UuRVZ9Z1gLW8Q6576sce3v53Gwtbvu-WPMQnsK43nb0O0VC-mrp6T2FrzCTlhfdyOXfFuvzk1JyqeUHWP7IzKd9vWbIzuC7Q3QLiCCtJQQdFdUp4deMbEcLyQnluG8rAaRIrSGdSUfv7OeBQeNniXzcGiVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=tNfY5uw6gXwviPz5thx-OSxIz8lEnc9ErOH3bc8GsQdNu-kP3PifSjjcIsrBQRxMwhoCBVNtYxyObvZBh1AsKXCcleIQE6-KFaThpuW3Av12AWhPfwTUwlU2dXMrJll0JMmwENp5BDuqrhfx0VvwUP_DGjdXk7hEWNX9FiPZTGzQC5rvgpmcRs_w1N7UuRVZ9Z1gLW8Q6576sce3v53Gwtbvu-WPMQnsK43nb0O0VC-mrp6T2FrzCTlhfdyOXfFuvzk1JyqeUHWP7IzKd9vWbIzuC7Q3QLiCCtJQQdFdUp4deMbEcLyQnluG8rAaRIrSGdSUfv7OeBQeNniXzcGiVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: نظرتون درباره حمله حوثی‌ها به فرودگاه ریاض چیه؟
ترامپ: «به نظرم اتفاق وحشتناکیه.»
خبرنگار: آیا آمریکا هم وارد ماجرا می‌شه؟
ترامپ: «خب، خودتون متوجه خواهید شد. اما به نظرم اتفاق وحشتناکیه.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73097" target="_blank">📅 10:54 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
