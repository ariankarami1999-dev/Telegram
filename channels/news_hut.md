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
<img src="https://cdn4.telesco.pe/file/kdhEPiMl4NvOxJUBGPd5m5SJL5bYjJKPf5-EaCrWrhfpfnEx_nyUg8tmFqO2Yw8YKst6VHk-tnpT4y5J9PJyeEBczoacPuJpDQobTw-4rSyabWQtWgC82pQwt4Sz3Xw-uMiEAZOqDpoeCNtjxpNlFcJ6n7wdRJ7Kx19vhP179J3zy5VG2l-IHzd2MaKsg8EULqGethtoiN75Pv4UeztCt-ArVtO5x98u2fjMQ1nGnr9QBUbxFNMq1GWyNoCHwl8WglJql8hK2ssqZPuxPWMS2By7btOkWsurwGevyWXBc6GVPYorx8r-KrIg7sjO3F04Juli1J8G9DQjPFA0xgoqlw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 132K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 00:59:21</div>
<hr>

<div class="tg-post" id="msg-69712">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66931f1c30.mp4?token=EsexIXqcAgjg0wI1wh-JIStYU2cxmBt0yukWhMsxHjSmp9zkAM6lUT8U9Z9wlRw6qfQTHsH-g_8ARYLLwgF-lvFP4AM-RUVjUdtFZlhuqreOmwR6hJbzrUdIN5ew_nKEwn3essA151lzSeyMr2D2gpBCgJZvweYpPrXXZfJtLoSX_-96QIzLrEbVV2Q0cZ8E4ZNR8aeQvOGO5gYJ7Hb5Mcq9GR08jmLNpBOk0RY-lhX273fNLP4NFOyvt9iWEN4RZ3JWSIooLY7aJtzQp0dPgRACMaS0I0CT86QpYfk9pS6uciSiUQA8kWVuoBNfXaUlSoum0RSAo7cOngssz5GBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66931f1c30.mp4?token=EsexIXqcAgjg0wI1wh-JIStYU2cxmBt0yukWhMsxHjSmp9zkAM6lUT8U9Z9wlRw6qfQTHsH-g_8ARYLLwgF-lvFP4AM-RUVjUdtFZlhuqreOmwR6hJbzrUdIN5ew_nKEwn3essA151lzSeyMr2D2gpBCgJZvweYpPrXXZfJtLoSX_-96QIzLrEbVV2Q0cZ8E4ZNR8aeQvOGO5gYJ7Hb5Mcq9GR08jmLNpBOk0RY-lhX273fNLP4NFOyvt9iWEN4RZ3JWSIooLY7aJtzQp0dPgRACMaS0I0CT86QpYfk9pS6uciSiUQA8kWVuoBNfXaUlSoum0RSAo7cOngssz5GBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
ما هیچ امتیازی به آمریکا ندادیم!
آمریکا به تعهداتش عمل نمی‌کنه؟ خب اون موقع ما هم نمی‌کنیم.
تو جلسه شورای امنیت، 12 نفر از 13 نفر از این توافق دفاع کردن و رای دادن، چرا؟ چون منطق و عقل اینو حکم می‌کنه.
کسی که نمی‌فهمه همینجوری میگه بزن! خب این تبعات داره...
من از شهادت نمی‌ترسم که هیچ، واسم افتخارم هست ولی اینکه نتونم مشکل مردم رو حل کنم، واسم قابل قبول نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/news_hut/69712" target="_blank">📅 00:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69711">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372d7e9f3e.mp4?token=E_kPmRbU8mhyNUMPdm3AvMAjOoJwmSsIyMyM_kl3AgsoIkeqiMvNt_ZPo9BCegncEBof0BkhzwlUMHGuu1prQN_grNq3w84ZsqsyQSveUDRhOaFt_Tatt4GcKzwO40VJZIwG0Ediy5SSY9t8C_NNpLubWO6mFbyP7ZngfRXWyIIeqWSOUVgHPLhNTozuKPkCF_aU2qMM36C6Xq1qp6K5MNG7SE3zyF79ewtigPfBhPxFTe2_erw8miG_qZNY5IReJ4hPcmTgaLILNxl6uVUkCswrMeI-KHnzoTwMwfmsgoO6Kx8FygtgT81i6rQTDNIjgvVlejyrcJi1KlkAcBp4SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372d7e9f3e.mp4?token=E_kPmRbU8mhyNUMPdm3AvMAjOoJwmSsIyMyM_kl3AgsoIkeqiMvNt_ZPo9BCegncEBof0BkhzwlUMHGuu1prQN_grNq3w84ZsqsyQSveUDRhOaFt_Tatt4GcKzwO40VJZIwG0Ediy5SSY9t8C_NNpLubWO6mFbyP7ZngfRXWyIIeqWSOUVgHPLhNTozuKPkCF_aU2qMM36C6Xq1qp6K5MNG7SE3zyF79ewtigPfBhPxFTe2_erw8miG_qZNY5IReJ4hPcmTgaLILNxl6uVUkCswrMeI-KHnzoTwMwfmsgoO6Kx8FygtgT81i6rQTDNIjgvVlejyrcJi1KlkAcBp4SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ارژنگ امیرفضلی
:
بالا برید پایین بیاید، برید چپ برید راست، مذاکره کنید جنگ کنید نکنید:
🔻
هیچ چیزی به قبل از ۱۸ و ۱۹ دی برنمیگرده
.
@News_Hut</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/news_hut/69711" target="_blank">📅 00:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69710">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
ترامپ در گفتگو با خبرنگاران:
ما افراد بسیار زیادی داریم، اگر بخواهم درباره همه صحبت کنم، تمام روز طول می‌کشد.
اگر بتوانید به سرعت سوالات خود را مطرح کنید، از شما سپاسگزار خواهم بود، زیرا ما یک جنگ را پیش می‌بریم، متوجه هستید؟
این عذری است که من برای ترک این جلسه کمی زودتر ارائه می‌دهم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/news_hut/69710" target="_blank">📅 00:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69708">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4300472.mp4?token=QE4QTXHqbFX0Zkw5dqgT58gCvKU9tsR0l0HhoosmJQIFmkzs8lve4_MD_-i3qkenvMa2GrTG6zErwoJpg1vzAcn8L96yGEmmANd6AO892rTiX1O58j9z3zfhjS5N0QEm04_d4vYlOSXgHDKeQGp-RO0mTTRERcKpzh0ffMcrXT3xYAh2rps6k_KaCYc3OSZwYqkos9Kz2ARCjs3WYxys3PhJh9KZfI9czZCU_HNUwZm_-QfpUXpSL8iMQlcqYIczcw-RLz6LkuPtglgisOM5zFYPqFUCjSh85BxCR_dMtQsjVr_eW3bAbAp68AkYUO2h74-Yy8Kmnz1bgrYQKsc60g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4300472.mp4?token=QE4QTXHqbFX0Zkw5dqgT58gCvKU9tsR0l0HhoosmJQIFmkzs8lve4_MD_-i3qkenvMa2GrTG6zErwoJpg1vzAcn8L96yGEmmANd6AO892rTiX1O58j9z3zfhjS5N0QEm04_d4vYlOSXgHDKeQGp-RO0mTTRERcKpzh0ffMcrXT3xYAh2rps6k_KaCYc3OSZwYqkos9Kz2ARCjs3WYxys3PhJh9KZfI9czZCU_HNUwZm_-QfpUXpSL8iMQlcqYIczcw-RLz6LkuPtglgisOM5zFYPqFUCjSh85BxCR_dMtQsjVr_eW3bAbAp68AkYUO2h74-Yy8Kmnz1bgrYQKsc60g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی(برادر زن مسعود خامنه‌ای):
فتوا میدم بی حجاب هارو بکشید اصلا رحمی نکنید
.
هرکی خواست مقابله بکنه اونارم بکشید
.
این دولت شیطانیه اینارو هم جلو اومدن بکشید
.
این دولت شیطانی شده زیر نظر آمریکا ما باید به حکومت اسلامی سابق برگردیم
.
اسلام همینه باید ضربه بزنیم و ضربه رو دریافت کنیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/news_hut/69708" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69707">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a717b4bbc3.mp4?token=uaqSaqfwvoB0ywwUUYF1ZkFAIHs9YhGahY4aCOw6q2z95IjKLRamzwS5ucwGY1aVaZ7Izs8eRRXSyof8YYu7kVsMoaBKOFYVDHyxRWw6WKjUJkTYlrj4bha30_G6XXwlgLarhOpn--lnFhprl2FbMvlK0aoPwRwbJ7qvZTeB4lY4esV_IxHckd03xgcpjCaXETWnW7JmOwKoJlVEVWpCOC2D12FearfqLljQ3_ONhu-tpgV_qyKSLOdKBurnkEqWd9mssIZya5AI93FdkpoBxemmBsbKXspOBskrn06oGTL-dre-DYN_6UnTnXA-00iVmtKahIMPle73--EUH9_UEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a717b4bbc3.mp4?token=uaqSaqfwvoB0ywwUUYF1ZkFAIHs9YhGahY4aCOw6q2z95IjKLRamzwS5ucwGY1aVaZ7Izs8eRRXSyof8YYu7kVsMoaBKOFYVDHyxRWw6WKjUJkTYlrj4bha30_G6XXwlgLarhOpn--lnFhprl2FbMvlK0aoPwRwbJ7qvZTeB4lY4esV_IxHckd03xgcpjCaXETWnW7JmOwKoJlVEVWpCOC2D12FearfqLljQ3_ONhu-tpgV_qyKSLOdKBurnkEqWd9mssIZya5AI93FdkpoBxemmBsbKXspOBskrn06oGTL-dre-DYN_6UnTnXA-00iVmtKahIMPle73--EUH9_UEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تحلیل جدید محمد باقر خرازی از حمله مسلمانان به هند و چین در آینده:
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/69707" target="_blank">📅 23:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69706">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ea65bf65c.mp4?token=dZbdWULbMCbiZM-4FQCjoxGOTUVUW4-fQFdhpUEgv4n6Bkng197O3pQ3GxWPerqYUhTd8khRVS55cN594CH4nz4DTjtX1GCJ7bNX-LGaSesB_zyU1V1PY30s_LIAgS1Z085DLa4aF1UKiUYV7E9wRXkM5IOQ1O3U_RsLh9McZdA_dTKdjXY6xZx7G-YWnkfN2AINWo8afdlKLEPy4pgz7O595X1EkPoCDMUbSnmgggkcA2ljQr10BbWbGjFifiQEPAu2PYLUtcGlzETRFcWH90moj5riww7VHJ26W2Er6dFmCSNPavDFmuTa_Nr7Pcr3O6lotwAAJtkRNfDT0l21QA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ea65bf65c.mp4?token=dZbdWULbMCbiZM-4FQCjoxGOTUVUW4-fQFdhpUEgv4n6Bkng197O3pQ3GxWPerqYUhTd8khRVS55cN594CH4nz4DTjtX1GCJ7bNX-LGaSesB_zyU1V1PY30s_LIAgS1Z085DLa4aF1UKiUYV7E9wRXkM5IOQ1O3U_RsLh9McZdA_dTKdjXY6xZx7G-YWnkfN2AINWo8afdlKLEPy4pgz7O595X1EkPoCDMUbSnmgggkcA2ljQr10BbWbGjFifiQEPAu2PYLUtcGlzETRFcWH90moj5riww7VHJ26W2Er6dFmCSNPavDFmuTa_Nr7Pcr3O6lotwAAJtkRNfDT0l21QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
یکی از قشنگ‌ترین ویدیوهایی که درباره توصیف وضعیت جامعه در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/69706" target="_blank">📅 22:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69705">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rjgx9s1bkMnwU20q-Rwqx0maOzR4P8PHAfIMCxQgrjCnvWj7X5XvkrCK6PqInVel-mY0O5scuZEliT4CB0wBuFdIUsEksebTxhwEbqTcpD11WP4UsxCccrR5uUFzrULe2AKehaB9zkls7fdy9yWhjtEfFstfywQ-cOcp-PF4ZRa4Yl7EF5bOftj_7PNWkb8qFuEStAxvswDiWTJ8a6lK8xAzUX53QQhBM84wbVRTq_9tuo4_T3Iu_daCNCAWwiG1_s9PgEcZZEh5l9GAKUn8RyZfU76gX4-Rkf8KIr3eWqhdor1g-QX8Ug4UZTW9H8oJYZUngz6wLXKdIHDDtwPUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
نیروهای مسلح قدرتمند ایران امادگی و اقتدار خودشونو درباره بهترین ارتش جهان نشون دادن
هنگامی ک مسلمون ها کنار هم متحد باشن میتونن درباره هرچالشی از بیگانه با قدرت و قاطعیت ایستادگی بکنن
زمانش فرا رسیده که تنها بخودمون متکی باشیم و برادری واقعی رو در پیش بگیریم
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69705" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69704">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم  آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16 https://t.me/+5fvta-uF4QA3ZDY0 https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/69704" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69703">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NK62Cm5m_Ocxc9PXwDCR_C82eomyO5QBCc7ebWXsFDQQwIiApm2IbdhXq-5Y-r8rub_Dosbi_8QW_UwLpUJeJwAKIeQCEjCFn0EgypQ8z8ChsxIE7GX2MJ4J39jf5Xgs-F6FRwU95TcXaQrK12sOyWsieslzDownuug7gcLmnXqqS9Isg5HT4mbJLRcQiZANUqV--8_NpDI9-v0Kd6rdHALRhJAcQVEpo_kUWbF8No04gX_689QpbTIbLCSmeK90af0FoxORh_ggNagemzfb_8nYlr66_KmKXBtXEytZyrd4N_xEC9qMhDuE3thVzHJNy0aDiTMsQX6TltAYYIhUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم
آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16
https://t.me/+5fvta-uF4QA3ZDY0
https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/69703" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69702">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfaWTedRqFC4MCIzyqjpstJL_Z492mn3iGPMCZ4tKYSD-iMwPCpHqp1rmbMtAlhbScERvrC13XU1DU8AF0CzIdJGzR25NvuY1bqfr6xp1UaDSnWcnuBx0Utxd7ovoHEiKU9lnxbX0GG_AMzDPXc4YUQ67SocqQ0iAq_PBk29jh1vF2GK-6ec_NFb5rkgKJYxSaEjTOqkO0geQ2PXTPC4XYP43wKWjFnGN0XaCuSUzIEP-qgutCpmBnKxVqV6Xs7fnhUg9Dj0Ge-LrmSxktT9pxzEHZnCalwj-A2fX9fj4tXlZSle30sE6Nn5PXEeQYY4KmC8ZqoMnrVbgg-cICD2aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
مذاکره‌کنندگان ایرانی منتظر تایید نهایی از سوی شورای عالی امنیت ملی ایران در مورد توافق آتی با عمان و ایالات متحده هستند. این دیپلمات ادعا می‌کند که انتظار می‌رود شورای عالی امنیت ملی این توافق را تصویب کند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/69702" target="_blank">📅 21:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69699">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWFgJP2z6UNW8K7fiekLcc7CdRiumMC5NkiHK_R2w54SLpMJyLsq6N9Cd2T8BCBIa8gFIitmyvF9PWit1vg2hvrPk1rqaZR2ljcjU9FGBtEeYqfpshQ5ryHeZ_pVOKwR6_ivUvmIhw_bSa7JYWxfALOzjjB-drISU4jQMNdx_ExpzVPQ7fwEp3An_zzZWZhKcm-ofchzEF9JhKWSeQbdAbfgNoZr4KekNytgPvyHqBGaC5R9QyVHMImHGq9nzjZgjGqXB0D_bZeCeSlODkgLvUTrikBhFFEFish_wdxRtYTBq2ZPf1VLpfGnBoQ2f7XOt-0qtVy5wbajScoyvOQ1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVBRQgJErq413TKuX6mlBK705S-mQPxatYEXtTgI70bRg6aBW-LtTy-hJ2DPyzD-SVnUZMI0wd64_FrWtTfq6nrq190MeJxv4dA-yBL--jQajcdP6eWGI2LGw3lUatTYrKD_RLC4LAKWwNj2kpw9l3UztFSfV16jgvN2II31szzIdVwv6LGudMoic9EO3LWLNsCpDLgCGXlxEIe1zpNYK3bIA2AXAWS_FFjhzav_8d3ykkL-kBTxctjAfOBYyFCLiZqw8VHCQgarMle6CZ8NYTktxPFprfIqg9NPncrCFcs2TFEgKxDkrBzeLlA8Vkjr0ur5gBv4kIVd2ZdxiMBXgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ab8e5c4f.mp4?token=kHS1kMgBVwP7PXjtZA3RlEBWVp-YHMQuv5pOY9mijYufajhwNNTk5GkxU4kI853ghUSvHb6iTGuBJMMmpivHzJYbHZIZc_O0DbqS1OOp4GTtyEAG_OAYJOOlsznxoh08-CwIwvgq-FKNs7etynMBvR13OrK2D_JwjdUd5tw43pBPgiun2qnpMcaNLwl5iJGJ6Y5sZisj2ImqxSksuB2c-Ykd_3WnJibrcnpmDAYxyNz2dT0xXe3841IFOAU_6H4xPlj75M50ryBvYeZKTJcUu2kejy6P3PcZgqL2b9A8F11HwmSaMAMkZDymE6-zrQzeIav1zURIHU-EM1F7iUlIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ab8e5c4f.mp4?token=kHS1kMgBVwP7PXjtZA3RlEBWVp-YHMQuv5pOY9mijYufajhwNNTk5GkxU4kI853ghUSvHb6iTGuBJMMmpivHzJYbHZIZc_O0DbqS1OOp4GTtyEAG_OAYJOOlsznxoh08-CwIwvgq-FKNs7etynMBvR13OrK2D_JwjdUd5tw43pBPgiun2qnpMcaNLwl5iJGJ6Y5sZisj2ImqxSksuB2c-Ykd_3WnJibrcnpmDAYxyNz2dT0xXe3841IFOAU_6H4xPlj75M50ryBvYeZKTJcUu2kejy6P3PcZgqL2b9A8F11HwmSaMAMkZDymE6-zrQzeIav1zURIHU-EM1F7iUlIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیویی از محل اصابت بمب‌های GBU-39 آمریکایی به سایت پدافندی رژیم در جزیره خارک:
ویدیوی منتشرشده محل اصابت بمب‌های هدایت‌شونده GBU-39 ساخت آمریکا به یکی از سایت‌های پدافندی رژیم جمهوری اسلامی در جزیره خارک و محل استقرار توپ ضد هوایی قدیمی ZU-23 در جریان جنگ را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69699" target="_blank">📅 21:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69696">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P6g-lFnlG4kZd81l2EyDOY-YTMkSHHGwUW_MwFXvU8vPl2LRMwlagJE-NdI2BBASkEwEcvkQr4L2qXbIN44mGPRcE2l5PNODbRQSdHoVJ-Joo3V2XSqHbtMK6R1iaeEGoGjcwUMYfB7Pwi9jepyU-Y0DkG7YiXuqfHql2FSUzE8LBnHqPF01TfNrtz3dTKf2d67SYRbfAcCFHYPfRPbNd14NlzuRcxiwHsMKldv7plwUuKDFBbhze0GHB5agbfN1cwfB-TxF7Rw-7uR_qQ8AjJEAomIYbtI_6bFI-qw0OVePdCudt2vub1n9jR7TO7kFsemWORqF3ThkL0Y7HQudZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ed553c5ba.mp4?token=BDTXMDq0G5_9bJAqohPXhLkzqX2GGj2nttljt_wagPyhm-PULbvwFW6n9zWdmV7x0YS1-E7BKKgn_0ILEgNutMxI4yF3bv7ppG96jnzwizXjUnP1gQrXmdxl1BK3hT5O8eSkgojjKtlMGVaU-w99dGpF5iZWPv4RYUuIWTHO7_1HliAFiDu49gAWBpW4G4N3rNiLp7fBbb25DXEC2vkbTqmridN9u069aoxNPRm8YX2wK2mfrOuss6Dg9WsK8y-LcN4N1JP2EEunR_o3ECe6FKoCI5oMQCsALleLH8GLEMmGhs82iKCioFMvooh3wXSFJLlKJy1wX9P4PkkHReAD9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ed553c5ba.mp4?token=BDTXMDq0G5_9bJAqohPXhLkzqX2GGj2nttljt_wagPyhm-PULbvwFW6n9zWdmV7x0YS1-E7BKKgn_0ILEgNutMxI4yF3bv7ppG96jnzwizXjUnP1gQrXmdxl1BK3hT5O8eSkgojjKtlMGVaU-w99dGpF5iZWPv4RYUuIWTHO7_1HliAFiDu49gAWBpW4G4N3rNiLp7fBbb25DXEC2vkbTqmridN9u069aoxNPRm8YX2wK2mfrOuss6Dg9WsK8y-LcN4N1JP2EEunR_o3ECe6FKoCI5oMQCsALleLH8GLEMmGhs82iKCioFMvooh3wXSFJLlKJy1wX9P4PkkHReAD9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز ۱۶ ام مرداد، سالروز درگذشت فریدون فرخزاد هست.
مجری، خواننده، بازیگر و سیاستمدار ایرانی، متفکر، میهن پرست و آینده نگر.
به قدری کلامش پرنفوذ بود، که جمهوری اسلامی احساس خطر کرد و در نهایت ترورش کردن.
اون همیشه دغدغه‌اش، آگاهی و آزادی مردم بود و همیشه مردم رو به مطالعه و مقابله با خرافات تشویق میکرد.
از جملات معروفش میشه اشاره کرد به:
«یک روزی ملت ما آزاد میشود و این روز زیاد دور نیست. فرهنگ همیشه بر زور، ستم و قلدری پیروز می‌شود.»
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69696" target="_blank">📅 20:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69695">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH_5mTneZtX7Ngcxk8ZxiYsvWZPD3hpAEcMWK29KTXrpumVpTB76JgQByajukCeVvtdZxiZJ6jTgTtJst-yEOpWCIcImEdwx70SzRvsml3G6wQLXnzGWNdCET3PxcHfIP4xh7B_1O41C4IJXZX0Xxf59AeY1Bi9dux6Z-wtjhGfDsSLoBv_iivoK1DmeIgq9hWhK9_yWRwU3cznw0EHW9I0H89I2LLAoY1QLxOZ_xPE06JQ_uu10dBSjbtIWszNM1-mcUsT94AfPfk90Ouj1BLUFy-iU5tAALc_j0azeYVqhAXgixNNAswWh9jFmx_77QRRZ_AZy5S5RQlcFdKma_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
تسنیم تصویری از لاشه جنگنده آمریکایی F-15E Strike Eagle (با شماره ثبت 00-3000) منتشر کردند که متعلق به «بال ۴۸ جنگنده» (48th Fighter Wing) بود.
این جنگنده F-15E در ماه آوریل سرنگون شد و منجر به آغاز یک عملیات نجات گسترده از سوی ایالات متحده گردید که طی آن هر دو خلبان با موفقیت نجات یافتند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69695" target="_blank">📅 19:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69694">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bedb477ce.mp4?token=p5x0A17EYLxjwVA5WsxBW0RivKBJbD92DoU5ODgtHWgeCRRy4m0uVEzlRso8BOoUTIfS4qkxP_1on3KuEV8zCxe0WveiWHhOMBaYyuv-Ir5YrNhDCywi8k5CYGuwDCixKKXh7pPBA6yONZduJpdRLxZ00nF8DLw4kYnh5BJKoUjqvV9FLyVWzD69BQOsFlu9dW_IWcwrWlNY1SndmvALt7dLl56Yz3oT3eznic6TrT_97aqiSZ_yo9SrwUw9cNtIJplv5tTkawKujqcyh5T8uZuLArckwikZ0jQattGhTr4wGRIif0QxQdo5NLe6H8IG3Cy2LzaSFnasm37JLW2Wcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bedb477ce.mp4?token=p5x0A17EYLxjwVA5WsxBW0RivKBJbD92DoU5ODgtHWgeCRRy4m0uVEzlRso8BOoUTIfS4qkxP_1on3KuEV8zCxe0WveiWHhOMBaYyuv-Ir5YrNhDCywi8k5CYGuwDCixKKXh7pPBA6yONZduJpdRLxZ00nF8DLw4kYnh5BJKoUjqvV9FLyVWzD69BQOsFlu9dW_IWcwrWlNY1SndmvALt7dLl56Yz3oT3eznic6TrT_97aqiSZ_yo9SrwUw9cNtIJplv5tTkawKujqcyh5T8uZuLArckwikZ0jQattGhTr4wGRIif0QxQdo5NLe6H8IG3Cy2LzaSFnasm37JLW2Wcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⌛
چند روز پیش یه خانوم معلم به برنامه شهبازی وصل شد و این حرفا رو نثار شهبازی کرد :
من معلم دانش آموزان ایرانی هستم و خیلی رندوم مجری حال بهم زنی مثل شما دیدم
اسمتو از گوگل سرچ کردم دیدم حالم از ادبیاتت بهم میخوره از لفظ و گفتارش و از عدم اگاهیش حالم بهم میخوره
همه میدونه این مسخره بازیو که ایران گذشته چطور بود و الان چطوره حالم از دروغ هاتون بهم میخوره
واقعا صداوسیما انقد بیچارس افرادی مثل تورو بزارن مجری و وقت مردم رو بگیرن؟؟
البته دیگه افرادی براشون نمونده باید دست به دامان چنین افراد مزخرفی بشن
🇮🇷
حالا واکنش شهبازی: اینایی ک از سلمونی و کوچه خیابون گذرا مارو می‌بینید بهتره یه چند قسمت ببینید بعد مارو قضاوت بکنید
👍
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69694" target="_blank">📅 19:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69693">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H06SYM8WMYG0bXsnHmpmrr6t6sATvFXvOaXeS6D78HXJdno_WkIaINjJ5uRZgQQrbF5qMKraVg5lh95YHInN3FS0mdEU_WUgS8izx1_Qcrgw7nM35QZSnfmMKsNGhfEwYEOLmFVYVZhdXm7Y5YA1oQjn14aGdqQS3QH5RS73QS21U85HZs77KhB_ZVF9ctqkbg2HQOVe2YlXPoy-OstN-pL-4Tj_NoZNGFv6QTBrt6TF6dywFxqq2dzhcjx8Z_dsnZT4jdsUEUnU0lZiw_nytpxDgMk3NkGAcc2QnimravhuXJGBKY3gy265T-1yqwOP6Rn1yrMEpEKE5V5GdXC8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
به نظر می‌رسد که محاصره دریایی ایالات متحده، صادرات نفت خام ایران را متوقف کرده است.
تقریباً یک هفته است که هیچ تانکری در جزیره خارک، اصلی‌ترین پایانه صادرات نفت ایران، بارگیری نشده است. این طولانی‌ترین دوره اختلال از زمان آغاز جنگ است.
اطلاعات ماهواره‌ای و کشتیرانی نشان می‌دهد که اسکله‌های بارگیری خالی هستند و ترافیک کشتی‌ها به طور کلی متوقف شده است.
ایران همچنان درآمدی از نفت‌هایی که قبل از محاصره ارسال شده‌اند، کسب می‌کند، اما این محموله‌ها رو به اتمام هستند.
به جای پر کردن مخازن ذخیره، به نظر می‌رسد که ایران تولید نفت را کاهش داده است تا از تجاوز به ظرفیت ذخیره‌سازی جلوگیری کند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69693" target="_blank">📅 19:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69692">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af32e5c900.mp4?token=WumimYGrP0r1fJSWKIxg9L1WJuT705LcQLRgaevbQdNn42_Z4E1utSEzgaVqYTK1FuJMPo8_1sxEMF8hFCwHHBj9g7UGK-KPYGT3hPANekEwq4rH_PNY0N-3vN_OWEm89ztVhEWQCnasMvw0tYi3zrqy561WWIWx7LaL8QE9B30AUadHPzTAwXX-uNEE5PjA3Y8Wx53JspB4w3KDV_mlq9oWzmIaPJZvYR7_moXD3JnFazNJr9fF5U84nm7EHwIGRMaT4LOWHOfuKMv0_8xEmvH5Oc5DGkzYyksKMZaOKIfjF86Y-k5OdLDfWWS7pjKqH78ZZg8czWJiIimsQZ18PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af32e5c900.mp4?token=WumimYGrP0r1fJSWKIxg9L1WJuT705LcQLRgaevbQdNn42_Z4E1utSEzgaVqYTK1FuJMPo8_1sxEMF8hFCwHHBj9g7UGK-KPYGT3hPANekEwq4rH_PNY0N-3vN_OWEm89ztVhEWQCnasMvw0tYi3zrqy561WWIWx7LaL8QE9B30AUadHPzTAwXX-uNEE5PjA3Y8Wx53JspB4w3KDV_mlq9oWzmIaPJZvYR7_moXD3JnFazNJr9fF5U84nm7EHwIGRMaT4LOWHOfuKMv0_8xEmvH5Oc5DGkzYyksKMZaOKIfjF86Y-k5OdLDfWWS7pjKqH78ZZg8czWJiIimsQZ18PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت، وزیر خزانه‌داری آمریکا:
«ما آن‌ها را کاملاً تحت فشار قرار داده‌ایم و آن‌ها با تورم ۱۵۰ تا ۱۸۰ درصدی مواد غذایی روبه‌رو هستند و حتی توان پرداخت حقوق نیروهای نظامی خود را ندارند.
فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد دستیابی به یک توافق و برقراری آتش‌بس ۳۰ تا ۶۰ روزه باشیم و تنگه هرمز نیز بازگشایی شود.
در این صورت، قیمت انرژی باید کاهش پیدا کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69692" target="_blank">📅 18:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69691">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac71f40e4.mp4?token=Ah0t1G9prJ1JA7HXgaoXujVNGySv2XFI7gz4lmkNsQwnSs4uMxUmgX2SUglAZw6vpggUadGrA6WmxywcKtjEEcpAAsbDtdPbvDQBJuAIhsFZidO2sJACnSPYgWl-t-gxhhqat-Hx8CLDwCGXb36PxN7WqrwodHII85VCcsbSBTx8Uxs-CHGtrCgNGewWNm1ET0f4T4XC_zz6mZNai31523ejBb0tSm3JnUDWzXXt8cFma6n7vaV5bKEJ7RyVZmuh55SYNIAXNzC8a0D4-6sx1PioVdtl7V-KPkWzctTxpRgW6-h20tyS5whX3N57HnF5e6zf_0zfdltVkgVRlO3aRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac71f40e4.mp4?token=Ah0t1G9prJ1JA7HXgaoXujVNGySv2XFI7gz4lmkNsQwnSs4uMxUmgX2SUglAZw6vpggUadGrA6WmxywcKtjEEcpAAsbDtdPbvDQBJuAIhsFZidO2sJACnSPYgWl-t-gxhhqat-Hx8CLDwCGXb36PxN7WqrwodHII85VCcsbSBTx8Uxs-CHGtrCgNGewWNm1ET0f4T4XC_zz6mZNai31523ejBb0tSm3JnUDWzXXt8cFma6n7vaV5bKEJ7RyVZmuh55SYNIAXNzC8a0D4-6sx1PioVdtl7V-KPkWzctTxpRgW6-h20tyS5whX3N57HnF5e6zf_0zfdltVkgVRlO3aRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبت های یک حامی حکومت:
دیدید واسه اربعین چجوری از پول شما مردم خرج کردیم و کباب آهو دادیم به زائرا؟
براندازا بسوزید، بسوزید که هرچقد پول دارید و ندارید باید خرج امام حسین کنید، تا ابد خرج امام حسین و دینمون میکنیم یا الله!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69691" target="_blank">📅 17:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69688">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266f0707c9.mp4?token=G9d6Qf8Geki8mKeVS-Eig3mhh7SBwCHWfZ4t_dSzsqZ8WcKdZstC2CL4NOQnuEgWqrxWD9i4xEZPRRWuDVh_pfDrYp7dKtCvijShDOUt2oVGe2X3HE35wBmb6TNh08re_S_igUmmS7hTmxprnzB4lYC23nKmjJ98hczPtlHQ8PhyXIzL45rlp3T4gHkKaAE5CyUBqDmUeiQy6k0R0pzRVc9SPniMAvpm_9yNrS6Fp-NDgomTa8DZEBqcg0ihpF6kNss3UOLdlPRHKCumRB3hbQ1tiOsN29slKV4a8jMAbtzs8PmkW2JmpZvzJIEKEkjPy3jxKzotHismd3czrFoyfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266f0707c9.mp4?token=G9d6Qf8Geki8mKeVS-Eig3mhh7SBwCHWfZ4t_dSzsqZ8WcKdZstC2CL4NOQnuEgWqrxWD9i4xEZPRRWuDVh_pfDrYp7dKtCvijShDOUt2oVGe2X3HE35wBmb6TNh08re_S_igUmmS7hTmxprnzB4lYC23nKmjJ98hczPtlHQ8PhyXIzL45rlp3T4gHkKaAE5CyUBqDmUeiQy6k0R0pzRVc9SPniMAvpm_9yNrS6Fp-NDgomTa8DZEBqcg0ihpF6kNss3UOLdlPRHKCumRB3hbQ1tiOsN29slKV4a8jMAbtzs8PmkW2JmpZvzJIEKEkjPy3jxKzotHismd3czrFoyfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‼️
🛸
وزارت جنگ ایالات متحده، پنجمین مجموعه از اسناد مربوط به پدیده‌های هوایی ناشناخته را منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69688" target="_blank">📅 17:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69686">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727c872e40.mp4?token=lfzufphZMtKlzZHYygSCCuZDnl-UxkKck_SXDTHeFS_NTmJeip8w1WVDxZDbv8IaUd74zsMqLojBvWUNrHYVVBt_x2UBant7xUH0UTFZ25v1HtvnOLwpJQzYYh-YPBFpICFxx8ungxJgsZQ6G_4KItOxo6lq5LELEG2HCBL45bHRhrLZrPaN5OnO4rluN_9Vnzlze1NWpdjT453HvjDUdyGlcSIehcjozDOB51sEfVTRINVNvSN4lJ-EGkjXroBBYPKMYNTmXUggJ3yeWgeHKKdQAdKYX6moHgiTOJPTkrXyGM6llJl7w9zhXNbeymu7tkcSr5ucQssEq-uSpVPJKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727c872e40.mp4?token=lfzufphZMtKlzZHYygSCCuZDnl-UxkKck_SXDTHeFS_NTmJeip8w1WVDxZDbv8IaUd74zsMqLojBvWUNrHYVVBt_x2UBant7xUH0UTFZ25v1HtvnOLwpJQzYYh-YPBFpICFxx8ungxJgsZQ6G_4KItOxo6lq5LELEG2HCBL45bHRhrLZrPaN5OnO4rluN_9Vnzlze1NWpdjT453HvjDUdyGlcSIehcjozDOB51sEfVTRINVNvSN4lJ-EGkjXroBBYPKMYNTmXUggJ3yeWgeHKKdQAdKYX6moHgiTOJPTkrXyGM6llJl7w9zhXNbeymu7tkcSr5ucQssEq-uSpVPJKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از یک مصاحبه قدیمی با روح الله زم :
من با بالایی ها ارتباط دارم و بهم امار میدن کاملا
اینا پشت بیسیم هرچی میگن من میفهمم
هیچکس نمیتونه بفهمه منابع من کیه
همه مکالمه های بی سیم، سیستم ایران شنود میکنم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69686" target="_blank">📅 16:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69685">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b41beaa653.mp4?token=e0jjAXL5ZOFgOwo8YFVuma6hb0t3EZxTFw5xkfiow9cJY6X4SHblm2cxYC6jOknzQ-H9qUtF-f8bnsxY8NCs40OV0T35QRuRncAZhj3T31iX4gtpv8ml6J36UPjZ-ROyJSf6GR13q8dpd8EH-i1s2LHK2lIImcTm5lqkX1fnyIMVhSn8rc-MNjsET87zlGo6yR-Jzcne_6z5QZwpeoseZUqZe2kGODCyS5cPYdh83NB_9HlmhZ3bE7b1OZOo-WodLIhA7xvL1FEj22xCykQscjShyZ52ZatnqCFOSWOlF7QVOP8Vm_X5koDQSPj6jQZGCFs0KGOvFrhCCXk4ZIPnbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b41beaa653.mp4?token=e0jjAXL5ZOFgOwo8YFVuma6hb0t3EZxTFw5xkfiow9cJY6X4SHblm2cxYC6jOknzQ-H9qUtF-f8bnsxY8NCs40OV0T35QRuRncAZhj3T31iX4gtpv8ml6J36UPjZ-ROyJSf6GR13q8dpd8EH-i1s2LHK2lIImcTm5lqkX1fnyIMVhSn8rc-MNjsET87zlGo6yR-Jzcne_6z5QZwpeoseZUqZe2kGODCyS5cPYdh83NB_9HlmhZ3bE7b1OZOo-WodLIhA7xvL1FEj22xCykQscjShyZ52ZatnqCFOSWOlF7QVOP8Vm_X5koDQSPj6jQZGCFs0KGOvFrhCCXk4ZIPnbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از مرکز ترک اعتیاد توی بالاشهر تهران؛
اینجا ترک کردن کمپ، سخت‌تر از ترک مواده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69685" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69682">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZChU1PUvyvTs8UUECaEfY0ohXteqeUtjqfaTbLhMKgBE6guI8CrVEpDmgqquJ9l94obTo8tmbMx_jDbfAQeaoQeWEoKrZnv2wFUes-VP-tVNX_-Cq7PNaNhzP1jTXGQdp276K-BJl37I7t6TWUSfHXn_7WzCikqLomlziysg0HcHVmRA8bf9wtCIKeLDlfi7ZCshdtNxHX67vPuDfihkWTZAfdSYhSwcTBuwPTZaWLRNDcS72EjlfOHiFdnSJF5GdOtync8rBFAIB3Ojq5e87RQk_XetcrWA8UmwYjD_R7y8KYGvcfpjFuSW5l_uiG7pynX6Om4IeuZKSiAESxlRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYN7hDqiliOvtI3pqtdSkuNFP0l10Ii5T-ZUbvRANyHzgH_ZCVdz3W5_NGY0ZkNe8nP9pbdDiRQWS-1htoOjkFAL4DaltVDuzHlT4wEEuRpYX4hr-uVJlDrNHeTb1A7BlTVqj1gx-zXUB2KDz3PaUxyPDgwk7gHELTGXc82Gflxn4Ecfdrq73FbM3_bAP0NBvRBJmcRzmqUVgGqSnpwLco_CwOqHscj5c89hq_14hLyaTzGUxdWe1WwDexwxSMI-b4rsWhd03M753zoMmVXUFByLonyYd6q0gzcj7LMxChPjylSyu3-ulmb8I8bUuXEawJvo3QM6slJjDKWv6p4XIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dunZyGFfYGKJg5CAMyMClBB3hgXD6QGx81znpsZQzI5TvToM7yyKLfP_0TFIGyZjB3lZ14xzVxH1ALK-pp03AGKjX_F2e4_6qCDl_3oHaMkCzCDXU37kVuKt0qhhEF9HNXbDgqIA_c_PU1_oM0Ep7de8g_0uN8GmC3wiqH6yT1BbSMB0qT_v1tQw0KAIbn9SMx_ARbfedJs3ll_DYe7BqfVrrAgPT5CD_Q50uY97hbp05SVkhbKmaiZvAxs3XXnd0PqgvbtOEA0yhvVD6NQPVaDeGx41g79CqcwSgOt3TuXJdSWy-oyP7eChbIkiixeorcPtLFQ50bbV47w8cPt1KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری تسنیم وابسته به سپاه پاسداران تصاویری از یک «انبار» هواگردها منتشر کرده و مدعی شده این تجهیزات متعلق به هواگردهای اسرائیلی و آمریکایی هستند که در جریان جنگ سرنگون شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69682" target="_blank">📅 15:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69681">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5020dac98e.mp4?token=LIU8FS3w7IyZJ7n2LfVD9NleqQDgJNfMvJtyl7lziB3z-eQXHGl346IrqcZG1cH95KLoV_wTRDDjuudBju44cWvgo1e6HXg3paKu1HY1W_6pto2h5FkgVdMrHjKesX4-GW0lrRssGTj14BfupSPIrdWjFpon06Eqj4LYT03BrB-GtQ1sSjJajM4pE4bVPyWbHT2KEQlHmv6TAZNGi-izTIR-fF0jU0qe6ybV5QC0BZFDgkKMROcsGF42_fl3t-jMjVGxeXz8Nr9QlXIKtCQwWlq5q0TwyozsbyVyzQnueSNVfOXEG4-ejlS-q8z0X4zJFuDDQE8UzqdFkD3u9rNbQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5020dac98e.mp4?token=LIU8FS3w7IyZJ7n2LfVD9NleqQDgJNfMvJtyl7lziB3z-eQXHGl346IrqcZG1cH95KLoV_wTRDDjuudBju44cWvgo1e6HXg3paKu1HY1W_6pto2h5FkgVdMrHjKesX4-GW0lrRssGTj14BfupSPIrdWjFpon06Eqj4LYT03BrB-GtQ1sSjJajM4pE4bVPyWbHT2KEQlHmv6TAZNGi-izTIR-fF0jU0qe6ybV5QC0BZFDgkKMROcsGF42_fl3t-jMjVGxeXz8Nr9QlXIKtCQwWlq5q0TwyozsbyVyzQnueSNVfOXEG4-ejlS-q8z0X4zJFuDDQE8UzqdFkD3u9rNbQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار کوثری، عضو کمیسیون امنیت ملی مجلس:
ما هنوز که هنوزه موندیم چرا شمخانی با اون همه سابقه نظامی، اصرار داشت اون روزِ حمله جلسه بذاره!
رادان گفت نمیام و رضائیان، رئیس سازمان اطلاعات فراجا رو فرستاد.
پاکپور، فرمانده سپاه گفت من نمیام دارم میرم اهواز، ولی به اصرار شمخانی اومد.
وزیر دفاع رو هم با معاون‌هاش دعوت کرده بود.
الانم چون کسی از اون جلسه زنده نمونده، نمی‌تونیم بفهمیم چرا شمخانی انقدر اصرار به برگزاری جلسه سران داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69681" target="_blank">📅 15:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69679">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aij0ldap06_vRnGE2IecD3r_SG4WHDA1IIH0xWSzCng0YKXp5xvHT6Tt_YuzTvf3eq87oXVTj6zDQI79eQenAjDcJglEsmUgb-XlA4TruDMRf-O3lbdJzGioBEeOBpEJjmocygxej2XduT2HMjeAJAhGKLuSUhn2shO6Y_WHaMOKMVo6PS08meGJbiSFYc7dt44pKLUuY2AFsVdBHfkXDkW_tUaQP93K7VV-nbJYN4GIVqDlsVYZX-TZLSZF0x5Z7_ii7DdFe4qtkv9g2IjHDsv8ne0VgJARgAFUxbNGpcak5ONvQ0xel-gyekAbYmumQ1DpYPyjCpHlue0OByQ5zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JlxHxDPL2KHLIBfaaplYkuq2KE3bXpkEAL2E6LCKGZJpBvOUb7Dd0bhE3WOiCDgrlMvIcmZLQCYxOHEV_g1xz7z3G5cAjLM_XmdJ37QLa8Jh0_lYPZ5Eol4kHS5rXw4ls8b1FWWHFF6RBV07zvUlim_f3iUama-Y5aGPC5IUj8-2szKjyVxWuDCyl1xgZ3efdB3DM6ORgrZQ9C40qcqNn8po6I7Ct3S7n1x1I1kQIcnp_LoyK2qu4uuWipz011dGT7QZZ3-S6P_nGWyq0EZ3oUDeqWAAwzK8c8iYJ60uc6_dEcJayUaHb83Kf1Og6s6Q7SqXRQgA66Y69oB85OPQxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇸🇦
🇹🇷
🇵🇰
ترکیه، عربستان سعودی و پاکستان پیمان دفاعی «توافق‌نامه مکه» را امضا کردند: «هرگونه حمله نظامی علیه هر یک از این سه کشور، به منزله حمله به هر سه آن‌ها تلقی خواهد شد.»
این توافق که مذاکرات آن از سال گذشته در جریان بود، چارچوب نظامی سه‌جانبه و مهمی را در بحبوحه بحران منطقه‌ایِ رو به تشدید — که پس از حملات اسرائیل و آمریکا به ایران پدید آمده است — ایجاد می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69679" target="_blank">📅 14:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69677">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b215003af2.mp4?token=aIy4tmBwmBKDwbpzsPpgGZPG0C4zeifUdzSeIkQAeDLI2rX74yv0L7n02ACR0neVs3M-J9N20NQFGK6gF4cQOxyj4R4PARFOzF9BBPJs9wGHYU48Ta0WKBGybzGUhVsR2G3h8kU06imw0B_kOqtAv20h6J2nWiHuiVK55v87kqqKWxPkb_oSjszql2B7ekGd8OYgi_QFhsTpXdF_QJUQnjeGxNdZDiMPwqJJyYWSl3hmV3Qnhr18tVujywYfG5OIds_eihmufM0cihVlhSkpi8qkI65XgL2pAY5YGahYpmW9tgToFiyGwj2e5NCbCXVfzp7CMVgoyqYn0la2Qu3i-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b215003af2.mp4?token=aIy4tmBwmBKDwbpzsPpgGZPG0C4zeifUdzSeIkQAeDLI2rX74yv0L7n02ACR0neVs3M-J9N20NQFGK6gF4cQOxyj4R4PARFOzF9BBPJs9wGHYU48Ta0WKBGybzGUhVsR2G3h8kU06imw0B_kOqtAv20h6J2nWiHuiVK55v87kqqKWxPkb_oSjszql2B7ekGd8OYgi_QFhsTpXdF_QJUQnjeGxNdZDiMPwqJJyYWSl3hmV3Qnhr18tVujywYfG5OIds_eihmufM0cihVlhSkpi8qkI65XgL2pAY5YGahYpmW9tgToFiyGwj2e5NCbCXVfzp7CMVgoyqYn0la2Qu3i-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇹🇷
🇵🇰
رجب طیب اردوغان، رئیس‌جمهور ترکیه، و شهباز شریف، نخست‌وزیر پاکستان، به همراه مارشال عاصم منیر، فرمانده ارتش پاکستان، امروز وارد مکه در عربستان سعودی شدند تا در مراسم امضای توافق‌نامه دفاعی سه‌جانبه شرکت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69677" target="_blank">📅 14:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69676">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637fe07403.mp4?token=eUy1TUYaWNaZ-demEq9QqbXMcXlbDS2gRciiAogFIbrEbKDLQtdu-Ezl3LdZ86YePeaOVDd0f96REknqHoH6_iAzTEjVZSHbh5y35il000r1qyZenRwnjZEfa-pmiR_2OEoa6ZET2Dxsa32PbpinVlWkMVM66WBJW6B7o-WH1u9pqaLUmSMzf8XZqLDup0_H_fXWiY2VE0kmgh142wDKWAdBFfpZKQpE-5Mfzirexz-li3Ku2wSa_WvVx4aZreapgm_B4dI_yBk6pid1fOuMqh06579d_JGe66O13dYgLwFKDx0jr5yasjaVXBB1lK3sfPmOt5dNZE7bKlgpu7gLqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637fe07403.mp4?token=eUy1TUYaWNaZ-demEq9QqbXMcXlbDS2gRciiAogFIbrEbKDLQtdu-Ezl3LdZ86YePeaOVDd0f96REknqHoH6_iAzTEjVZSHbh5y35il000r1qyZenRwnjZEfa-pmiR_2OEoa6ZET2Dxsa32PbpinVlWkMVM66WBJW6B7o-WH1u9pqaLUmSMzf8XZqLDup0_H_fXWiY2VE0kmgh142wDKWAdBFfpZKQpE-5Mfzirexz-li3Ku2wSa_WvVx4aZreapgm_B4dI_yBk6pid1fOuMqh06579d_JGe66O13dYgLwFKDx0jr5yasjaVXBB1lK3sfPmOt5dNZE7bKlgpu7gLqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از صحبت های ترامپ درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69676" target="_blank">📅 13:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69675">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a5084b0f.mp4?token=vi3v6xlGf1pCVJY3dpMTnQU9dMSXlSDDiwODnqtI8Cfa3icAgRw9GTj-RHbkvl-oPBoLNvHbw5GoP9Y8VBOAQbBBM4pbxxTO4B5AEWIB8k7e_NJXB_sP1J1S3BDiNT3mVmNTRXK498VN3DXzz_MTLGVAigm05XyEC3DzESB3art940j5Ym2NC_LsigqJifxnVy95hso3ZOgpdsbE_eUn9Tj27Jr3Wj8Sv2OtEdSLxSDB_dsPum43tHKL6YTIvj5_dnSnuRvf8PB3AurIPfc956LEoxPGMC57kPKk5qy3pQA8sOWYzwrxPpIxp0OUoa5ajK97KmZxxaLo99ptrUX67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a5084b0f.mp4?token=vi3v6xlGf1pCVJY3dpMTnQU9dMSXlSDDiwODnqtI8Cfa3icAgRw9GTj-RHbkvl-oPBoLNvHbw5GoP9Y8VBOAQbBBM4pbxxTO4B5AEWIB8k7e_NJXB_sP1J1S3BDiNT3mVmNTRXK498VN3DXzz_MTLGVAigm05XyEC3DzESB3art940j5Ym2NC_LsigqJifxnVy95hso3ZOgpdsbE_eUn9Tj27Jr3Wj8Sv2OtEdSLxSDB_dsPum43tHKL6YTIvj5_dnSnuRvf8PB3AurIPfc956LEoxPGMC57kPKk5qy3pQA8sOWYzwrxPpIxp0OUoa5ajK97KmZxxaLo99ptrUX67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت کوثری نماینده مجلس از عملیات اطلاعاتی موساد؛ «رد لاریجانی از طریق گوشی زده شد»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69675" target="_blank">📅 13:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69674">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r16
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/69674" target="_blank">📅 13:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69673">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkG5hthzF2YoFGFRJgs4odJMyRdhOM3WK4YepLg0xM6RDKt08v-yD6SlBrxijT8lxfEpBI2qNr3x-yslZNwikjZsFAx4M909oSlgZlMRAOT2lRnhSiHaDQRed2bN_J1wVZ_cOLjyMRm0ByxfUGOndziXhyDil2qescE5NyyooAlS7moFLdYtMBK9tUJWJoAQuU9KBGzt8dI1kj5DCWPN_pLCk_a3Oa23Pr4bw1J27cT2TU6oenZ8ZSiDma2daVhWj5H1pzxQtltGxUH_K_zVk6bWrWF1QN7xNodTqV4G2H-rJhLhuvRYUEdU_65qgNX63EES53SULS7IdviuehVBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r16
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69673" target="_blank">📅 13:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69671">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0c63da7c.mp4?token=UXu1hHRjxdwOvmzMS4km79tY7jOvELJ1d4gaMb4slNFX_LZ-SkIZxqp91ynScPI6x3JN7iD1m96rJGFL0kW_YQf3A20pkWlWYLovmU7UkVd9LME4igpLqv4QiaimPSXzTt2LdiJukmSMOUY-gtvKGjJUnWXsRwlEWIbjkymaa3u2piHqwFY9iKNVHcDIZBseocT_Eh6Hm3PNWOgTbgVDCRnI03HUmI0Tz5D7KAvVsLgdvwBGxcGUaCNWibMmq1kWKjYnxfanUnn2Ta6TscXxaCLzi-7Yrt6B3adyGieWTIt-kE_HdTbQMd8RK-WGopsuBog0E8NDwzsnin-Obxz5xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0c63da7c.mp4?token=UXu1hHRjxdwOvmzMS4km79tY7jOvELJ1d4gaMb4slNFX_LZ-SkIZxqp91ynScPI6x3JN7iD1m96rJGFL0kW_YQf3A20pkWlWYLovmU7UkVd9LME4igpLqv4QiaimPSXzTt2LdiJukmSMOUY-gtvKGjJUnWXsRwlEWIbjkymaa3u2piHqwFY9iKNVHcDIZBseocT_Eh6Hm3PNWOgTbgVDCRnI03HUmI0Tz5D7KAvVsLgdvwBGxcGUaCNWibMmq1kWKjYnxfanUnn2Ta6TscXxaCLzi-7Yrt6B3adyGieWTIt-kE_HdTbQMd8RK-WGopsuBog0E8NDwzsnin-Obxz5xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تا حالا نوک قله دماوند و کاسه قله دماوند رو دیده بودین؟
۸ مرداد ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69671" target="_blank">📅 12:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69668">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10354b943b.mp4?token=MFV18z25psGHfitmAOS4f-AyHPSXIz9yiBl7f3Qtf8ulc-WIz8YTFh90x4SDB_ZUgaFvTIz5UQgHpIt7pr0PbaWenElVWZgEeWJveOKjWJhAbyUZ3V_h4G5jwFKEFGBjB1j4JjpXNlDRGzIKXzs0bYHvj1dJiEtEhFnwdpoJwqGS9OHxdc6Gw_SUZkqc6vx4mjvTmmrZHY5zvRkpZf3IXHsWZi5HG9jaKg2YG3BXsd5xON3ZV2zMz8ThoJYH8ksJu_aUTlttAarpOQNtph5wvhkeHsvD-dOU0KLxlCXPb_21R176bVRoN0LxUSOl43WfjlMtCkfSdGMURqw363sTlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10354b943b.mp4?token=MFV18z25psGHfitmAOS4f-AyHPSXIz9yiBl7f3Qtf8ulc-WIz8YTFh90x4SDB_ZUgaFvTIz5UQgHpIt7pr0PbaWenElVWZgEeWJveOKjWJhAbyUZ3V_h4G5jwFKEFGBjB1j4JjpXNlDRGzIKXzs0bYHvj1dJiEtEhFnwdpoJwqGS9OHxdc6Gw_SUZkqc6vx4mjvTmmrZHY5zvRkpZf3IXHsWZi5HG9jaKg2YG3BXsd5xON3ZV2zMz8ThoJYH8ksJu_aUTlttAarpOQNtph5wvhkeHsvD-dOU0KLxlCXPb_21R176bVRoN0LxUSOl43WfjlMtCkfSdGMURqw363sTlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🚀
🇷🇺
پهپادهای دوربرد اوکراینی در حال حمله به انبار شرکت روسی "وایلدبریز" در شهر یکاترینبورگ، واقع در منطقه سوردلوفسک، هستند. این انبار حدود ۱۷۰۰ کیلومتر از مرز اوکراین فاصله دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69668" target="_blank">📅 12:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69667">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff4cea8c93.mp4?token=Hre9ROwgkw1iKkQFegFQyUR6i1MZ7chyoNC2ZBTfVjhH-OqZlOSyVeW_HDd3g6GXS9RdduUIANK7t773POLtetkco6lJr--2jT_tiQ0S1WhbXsMKaGFUR19xxLZmRcqhEZl24DpJgldJp25pmmpauzkzs3OqkWhP_2qkE00mQd4hOEZbSMD9RvdXnpgZulHHO6V28ykPrrU9h2PdTdeSHvpwmK7OW6p3hTyUIFMEHp0Jl-rBwa0RoEO_gGX7FACbri5Z1gwh6reyBVIFIUsfQ41C6FD9G5QMGTWTV9oj0esmjXucapwBU7V64Xso1BZGy5WzgDtkzOoNbueJ7ppSZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff4cea8c93.mp4?token=Hre9ROwgkw1iKkQFegFQyUR6i1MZ7chyoNC2ZBTfVjhH-OqZlOSyVeW_HDd3g6GXS9RdduUIANK7t773POLtetkco6lJr--2jT_tiQ0S1WhbXsMKaGFUR19xxLZmRcqhEZl24DpJgldJp25pmmpauzkzs3OqkWhP_2qkE00mQd4hOEZbSMD9RvdXnpgZulHHO6V28ykPrrU9h2PdTdeSHvpwmK7OW6p3hTyUIFMEHp0Jl-rBwa0RoEO_gGX7FACbri5Z1gwh6reyBVIFIUsfQ41C6FD9G5QMGTWTV9oj0esmjXucapwBU7V64Xso1BZGy5WzgDtkzOoNbueJ7ppSZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسره رفته خواستگاری، بهش گفتن 114 تا سکه باید مهریه بدی؛
🗣️
اینم قبول نکرده و گفته کمه و من اینارو میدم؛
369 تا سکه
1382 تا گل رز سفید
کل طلافروشی رو می‌زنم به نام دخترتون
یه سهام کوچیک هم تو یه کافه دارم که اونم میدم
امیدوارم راضی بوده باشین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69667" target="_blank">📅 12:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69666">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
🇺🇸
🇨🇭
آمریکا حتی به سوییس هم اجازه ساخت بمب اتم رو نداد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69666" target="_blank">📅 11:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69665">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ca70a3a5.mp4?token=Qwwt2UXY3sEnGN27VcZ4xZ5MYRmZghZdOcHnH2u-Uqc0R3U0HCp3VRCTo_DR746iy79AbEIIwEpBHX68SsbZUusztmzLcfPIBgHYtcfVuAvAoN-C6YV-zLBezqDe75IkPSt6sR9FYJUZhNtzLsWBUqE7tYhQtBNZDgymcEwSTpDNFl8F6pQVeMBD-bQ635PWmmrMPeb_GOhTBJHbgv4ccF2OOGwJpgWxgEno9cOUklUomy3FX9iAhT7I6IY02pSZO4Ui_ucHnWLSq5Ul7Iu5zoKswnykou5Wb7FQKDdIC3XfTuJFABmLckLjn5k5IJxg8rtZYZDcJTWqgFis0OC9rzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ca70a3a5.mp4?token=Qwwt2UXY3sEnGN27VcZ4xZ5MYRmZghZdOcHnH2u-Uqc0R3U0HCp3VRCTo_DR746iy79AbEIIwEpBHX68SsbZUusztmzLcfPIBgHYtcfVuAvAoN-C6YV-zLBezqDe75IkPSt6sR9FYJUZhNtzLsWBUqE7tYhQtBNZDgymcEwSTpDNFl8F6pQVeMBD-bQ635PWmmrMPeb_GOhTBJHbgv4ccF2OOGwJpgWxgEno9cOUklUomy3FX9iAhT7I6IY02pSZO4Ui_ucHnWLSq5Ul7Iu5zoKswnykou5Wb7FQKDdIC3XfTuJFABmLckLjn5k5IJxg8rtZYZDcJTWqgFis0OC9rzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از شعبه بازی این پیرمرد، قراره هر لحظه بیشتر سورپرایزت کنه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69665" target="_blank">📅 10:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69664">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntXl6689R5LdgdbzQEyB7FzosrDSZw4THKAthnLJ-ksgsorub6hsyNKMnFztrGOPY5g8Csld7gvJB7P6xIwIW-MG0MR0T9sWTOHmwRK4EFFUkWbtGup7wYyMpDmzakJZSt5vp5uyCKDQa9P7D5SEJQWsnsrEiwEx_W_YuvD9kobxwlJzoQ_AEFSnGRZlDd_-r6bVy2mm-3lSk3hc7VshsLhPfiet6-ILR6UbT4aKoaVHpUY4MPMDjwBNfR9AfgKRyDrqH4DtVq66DfefDQf9JPgiOma_qeOuKpw14jGp43Lfgq-W5v4hclduX9eh6dKf5AOZrxac396R83lBOaTobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
عنوان مقاله ای که ترامپ در تروث سوشال منتشر کرده؛ دونالد ترامپ در جنگ با ایران پیروز شد!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69664" target="_blank">📅 10:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69663">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c98f66ca27.mp4?token=t6nNDfAMNb4ltdPq3jVrSwE4tQ3_ejwYfY1L5WKAMU1SId5i_HSNFSiDOelYR55k3H69imq3-ZcEE8ehdZOAeAhHz0gvfMEX7GIbUHzp1BjtNUJIWnztVsirrzwK1vhOh0hWV-Nx52lHkq_fJRJdWcBtrkG5PH6XDVpbNhb-6EL7KaVrgt9dTT2uHNLTMghv6AKBdWi3Zj9eLTiHL92idO87qQ7S2CbLQ5jA2Ll_PFzoKmM7id2IpDlXRMeEh8Cg69wV9Z2-Pizd0DIDVfj8q1GJMnGY12WRvMII-i_MyoSleYwCtPoQJZ9pML-Q1OunXQ0Z7BqP8o5IzWuKnXCPFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c98f66ca27.mp4?token=t6nNDfAMNb4ltdPq3jVrSwE4tQ3_ejwYfY1L5WKAMU1SId5i_HSNFSiDOelYR55k3H69imq3-ZcEE8ehdZOAeAhHz0gvfMEX7GIbUHzp1BjtNUJIWnztVsirrzwK1vhOh0hWV-Nx52lHkq_fJRJdWcBtrkG5PH6XDVpbNhb-6EL7KaVrgt9dTT2uHNLTMghv6AKBdWi3Zj9eLTiHL92idO87qQ7S2CbLQ5jA2Ll_PFzoKmM7id2IpDlXRMeEh8Cg69wV9Z2-Pizd0DIDVfj8q1GJMnGY12WRvMII-i_MyoSleYwCtPoQJZ9pML-Q1OunXQ0Z7BqP8o5IzWuKnXCPFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
این شما و این مجهزترین اتوبوس های مسافرتی چینی!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69663" target="_blank">📅 10:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69662">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6484080b.mp4?token=p7sPwD9EDUbz1euCjBLoCtt9RBnguiJAg2JIoIDKKTiyATbaM3ODawdXsJ8cbHvt4v48yid3DzvCs-PfNnIbyT0AdCxq9QL_VIU9vgzWz5ZA_lP23PZ8PjiBomY1_R-DM36Texl0PiDoXQWnD275pgrKVIqb7ZfI9jbkI3-Jgsz3kspDO8HJdB6YDvD7pHerKERqluOuh55YfBvRe6Zxcfyr_XP7uFflnG8ohOSGqmPTgrPjj39eOyyXua_eRJE6um0OPuD2krTyqRz3oNqSfkSCT7-xlxm_43ytLZYmXwAl6wb7b7K0P-x098t-wZQFghTgnN06J-RPf3tNtnhJoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6484080b.mp4?token=p7sPwD9EDUbz1euCjBLoCtt9RBnguiJAg2JIoIDKKTiyATbaM3ODawdXsJ8cbHvt4v48yid3DzvCs-PfNnIbyT0AdCxq9QL_VIU9vgzWz5ZA_lP23PZ8PjiBomY1_R-DM36Texl0PiDoXQWnD275pgrKVIqb7ZfI9jbkI3-Jgsz3kspDO8HJdB6YDvD7pHerKERqluOuh55YfBvRe6Zxcfyr_XP7uFflnG8ohOSGqmPTgrPjj39eOyyXua_eRJE6um0OPuD2krTyqRz3oNqSfkSCT7-xlxm_43ytLZYmXwAl6wb7b7K0P-x098t-wZQFghTgnN06J-RPf3tNtnhJoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو دیده نشده از لحظه حمله به بیت رهبری و ترور خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69662" target="_blank">📅 09:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69661">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/news_hut/69661" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69661" target="_blank">📅 02:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69660">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwDbAn4Ipdewpcs6iMxU-NWcug6WIhinsG2sCt-PwAjpgptCAnMHsVdJYziFsuCRPxnegDzv0HJhR87y0tZEBb8P_PSyISvhOcOjBwiSMcUwV4BgBTZ-uJt3c2BjN53IDApS0mfteQ6uV-1BSOFyCgi0CV-l7am-tvLgVp4llyrhKbnumrjwuAbtsEL1RTfUV7M0sXFZtd2K9d2rrDvR75FokmQT_PdwzfbYPLWBnF2LlB7TUvfycA5PJaEhodH2V-Ie4r6AkUvg46DT-uBym49jRMGHCBttnKsatg-xkrUVznyGR-rAkHga06wGy-M9XcTC3jXJPkuRRRYtm5C69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a15
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69660" target="_blank">📅 02:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69659">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwSkpo8xbqXcSpd_tT5TGIX0MkcUhN2bMKrfX9NPuhq60FO6W3-Ib5sqIO7G4KoaGWMUOvJnWFuLLCxz9mMd_1y_iS8iHdXwc0Nsbey4YovH6aD2Uxa3TfL5Goxklq6lWdA-t2OHA0boYxNPwPVi5gLCJHKvXZSSg4vq5C-oETYW_rRtKHfAOScjIf_iy9lOlOKD1P7Y6AGf9lUwl22YkA4kL3u4jZbnB4GlWf2pRbWJmA1G8MI6b8EineZj4fqNbreE_DYPMWTArQfCAsDQWuhPN30cEp1qDcdS8GfHApbbmGIggBpysbHMuY3L0H1i_BvhYUxD1jRE9ZMu9bPqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇹🇷
🇵🇰
رویترز:
ترکیه، عربستان سعودی و پاکستان قرار است روز جمعه یک توافق‌نامه دفاعی مشترک امضا کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69659" target="_blank">📅 01:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69658">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iihkg8ps8XN7Pt7kwrdEI4aT883p-g2iKrGTc7B56yeZ1UKUqO9-1nJ5SdSKA35rv4mlE8D6vsQOabMDsTKnbZ_GfbBKyp3KNfNU7Dr8qTG6vdZfCJEwl0B27aBY2E-f8UhJ9Q90MnLtGvWUKMCbnuGB0-77xqk1_mHVqiFgJcNc_L3sDdnPKbHIvkp2NiLPHXBaoldTHIZx9j9mejWuIrlDD0bbXanJ2szeAIssZZK5BNSfnucMLypClKmwsdHtq8Cg5goBkhqOpM-v7q-YJNq-dJYDSM8LM83VaYKIIsFqvA-OtY5-hLLbA8m6MQ_tMw_Rh5DYyz75RVAn7MA4Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:
🔴
یک مقام ارشد سعودی؛
اطلاعات موجود نشان می‌دهد سپاه پاسداران ایران در حال هماهنگی با شبه‌نظامیان مورد حمایت ایران در عراق و حوثی‌ها (انصارالله) در یمن برای تدارک حملاتی علیه عربستان سعودی است.
این مقام اظهار داشت که این گزارش‌ها به‌ویژه نگران‌کننده هستند، زیرا در شرایطی منتشر می‌شوند که ریاض در پی کاهش تنش و انجام مذاکرات صلح‌آمیز است؛
روندی که به گفته او، پیشرفتی مثبت داشته است. وی افزود که پادشاهی سعودی «برای اتخاذ تمامی تدابیر لازم جهت مقابله با هرگونه تجاوزی، درنگ نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69658" target="_blank">📅 01:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69657">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pm5kYG_7IhQle_vD2sfR20gBOghF0eNRXb7kujxifkfvMnyRvBQYTit4BpvqIVAzWxqDJGEUqGJTUU_vD45r-9bFUuEoUGnXRsS7gEnZd-efJFVs23gUIZVg32gQVhqmGx6DxkLk21eEjf8vMuBg4bG9gZcqrSGLb1rRZ7qmNGQLoUBgJ8aG-ZiI1lp3rhAY4xXIIdYNz4O4novVJp1gryok55SeBd3Jp7uPaKC-mCdJGGYGZsTBdJ7KyXcmO6z6VANKz-22wDwiW3UkWRZqDfgHU9jin1JvJJJ8gHj2xxf_G_q2B4Z9vQPJazC3c3XjmZkt8uArQLomonw0bX1YDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
کانال 14 اسرائیل:
محسن رضایی میتواند خودکشی کند، ما برای او مهمات مصرف نخواهیم کرد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69657" target="_blank">📅 01:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69656">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac1c12b672.mp4?token=FdBHju8y2_N3lU8KYeJXUTRQmMK5euQZfMHfXo8IZlyawKht08yhtNMAmy5yLTtZkYJRPH7696opX5535Rpwo3IbZ0JLJRgWw7j7DdGOuT--U-xR1t0OZ_z2I2MyxtQrIreac2xqFeoIZa2F_XRzqn4It7BVD4LsomnmE7wGUS8BQs1fh1gl02BCO4kzE-x3H1Ke0ijqNd2LvGdHDaHJPRhCLbpAvxx-rR6T7u1mAl3inMaPNP8Na_riLoPlLt2KFGeC-1U0irJRjDOxFoVxVn2kC0ADJnkNJwYs_oAvA1oOGGwcQJY2aM_oFoTXobvIj6lMabS9PxwNwq7z-3m2mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac1c12b672.mp4?token=FdBHju8y2_N3lU8KYeJXUTRQmMK5euQZfMHfXo8IZlyawKht08yhtNMAmy5yLTtZkYJRPH7696opX5535Rpwo3IbZ0JLJRgWw7j7DdGOuT--U-xR1t0OZ_z2I2MyxtQrIreac2xqFeoIZa2F_XRzqn4It7BVD4LsomnmE7wGUS8BQs1fh1gl02BCO4kzE-x3H1Ke0ijqNd2LvGdHDaHJPRhCLbpAvxx-rR6T7u1mAl3inMaPNP8Na_riLoPlLt2KFGeC-1U0irJRjDOxFoVxVn2kC0ADJnkNJwYs_oAvA1oOGGwcQJY2aM_oFoTXobvIj6lMabS9PxwNwq7z-3m2mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
تفاوت اعلام مرگ دشمن از طرف ترامپ و اوباما:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69656" target="_blank">📅 01:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69655">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7820062e8b.mp4?token=lst-zwH0WHUpmvFrhRDFZp40VoYGgW-mIIaGuxa_NBtDiJi0nCtXQ4QWrrHvgEpcus4wfRWZziFT9CpCgw3k65mxRTK3MTtdLn3mHSB-_SumVQzyuoW6-gsWbZbhnvfzXFI2_yZTLLJH5NoTT2mfa2BhLtU4vuNqWynJl4GGun3UEyC98ms2OieGg0e4S06NhHy9I8RQT1R5Zdj13HnYiQW-IjQgjzzsbO7ZddcNg4kkPM_03NwC4JIsh5XRPgXUqrv8p2jmTloaT6hsLQvj1ruhPsuO3NGCliJkR4R-OM6LLrYmTQGvPjMciYX0tiVX70aacTrK15IDO23K6AGowQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7820062e8b.mp4?token=lst-zwH0WHUpmvFrhRDFZp40VoYGgW-mIIaGuxa_NBtDiJi0nCtXQ4QWrrHvgEpcus4wfRWZziFT9CpCgw3k65mxRTK3MTtdLn3mHSB-_SumVQzyuoW6-gsWbZbhnvfzXFI2_yZTLLJH5NoTT2mfa2BhLtU4vuNqWynJl4GGun3UEyC98ms2OieGg0e4S06NhHy9I8RQT1R5Zdj13HnYiQW-IjQgjzzsbO7ZddcNg4kkPM_03NwC4JIsh5XRPgXUqrv8p2jmTloaT6hsLQvj1ruhPsuO3NGCliJkR4R-OM6LLrYmTQGvPjMciYX0tiVX70aacTrK15IDO23K6AGowQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آیا توافقی برای بازگشایی تنگه هرمز حاصل شده است؟
🇺🇸
ترامپ:
نمی‌خواهم بگویم [توافقی] حاصل شده، اما در حال حاضر کم‌وبیش باز است.
ما کنترل تنگه را در دست داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69655" target="_blank">📅 01:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69652">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6e63add2.mp4?token=rsNoACFizcS44IIz7EzPLesI8DUFh60y2KjF-fFSlCE-AEz6EDgMSSeMkpU-FPcImeRZonM4veLqIGAE0jjReMtPeIajEhIjJUSMX16Rni_WRSkPv0eVXuoQKYrI_nRr4xLFpIE55UMv7OVBSl-CZWfZOaSdZKyXd-j1eaPum7hfcKYrn6Fwj08ko3wDqjddqSxgGhAqpntT83-IIbtnxQFHgnx5YedSTSrUJM4p-tYCAHWqF1AE0EjaMf23CD6HtSI-Q5_NyzLVMnDfUEG6C0ycc1ros6u9NtJoh0oXdHEKLa4JOJZuNlf-8MkBiJVVr3lq6ovOMcPDKhb79Mr2qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6e63add2.mp4?token=rsNoACFizcS44IIz7EzPLesI8DUFh60y2KjF-fFSlCE-AEz6EDgMSSeMkpU-FPcImeRZonM4veLqIGAE0jjReMtPeIajEhIjJUSMX16Rni_WRSkPv0eVXuoQKYrI_nRr4xLFpIE55UMv7OVBSl-CZWfZOaSdZKyXd-j1eaPum7hfcKYrn6Fwj08ko3wDqjddqSxgGhAqpntT83-IIbtnxQFHgnx5YedSTSrUJM4p-tYCAHWqF1AE0EjaMf23CD6HtSI-Q5_NyzLVMnDfUEG6C0ycc1ros6u9NtJoh0oXdHEKLa4JOJZuNlf-8MkBiJVVr3lq6ovOMcPDKhb79Mr2qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
به نظر من، جنگ به زودی به پایان خواهد رسید.
فکر نمی‌کنم آن‌ها بتوانند این وضعیت را برای مدت طولانی‌تری ادامه دهند.
من درگیر مذاکرات با ایران هستم. اوضاع خوب پیش می‌رود.
ممکن است به‌زودی توافقی حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69652" target="_blank">📅 00:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69651">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7984246.mp4?token=ZCIftbU3AQ30omoYnC-BzJLs6vxI2OYkN5r5zA2FPwXQwTqYjtLdLWdYUMlr9CMgvKJalRZzFZWO6_v1dNIJgxldL-d816AuS8cpW6LC64b68J-DttJG51MV19A7oFi2ya5sdujFfPRkTkziQFAIQ7GSRo8o0OTOSmgm5Pp0vvW919q7gSgiRBq2r38MwQpQ1oDh7r550WmYlZ4HQWhclAY5nhLkN8cM3tmO6SWohVEDvjSoy87Yvesx-A7keCdpyrTHLFZdNO1h3r839mEYkXouE0fn5ZUKbS-SNlXH-bM_5iU0z8NPTn_ANFVYPENJcptAxozeVMMv8KPCChFaYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7984246.mp4?token=ZCIftbU3AQ30omoYnC-BzJLs6vxI2OYkN5r5zA2FPwXQwTqYjtLdLWdYUMlr9CMgvKJalRZzFZWO6_v1dNIJgxldL-d816AuS8cpW6LC64b68J-DttJG51MV19A7oFi2ya5sdujFfPRkTkziQFAIQ7GSRo8o0OTOSmgm5Pp0vvW919q7gSgiRBq2r38MwQpQ1oDh7r550WmYlZ4HQWhclAY5nhLkN8cM3tmO6SWohVEDvjSoy87Yvesx-A7keCdpyrTHLFZdNO1h3r839mEYkXouE0fn5ZUKbS-SNlXH-bM_5iU0z8NPTn_ANFVYPENJcptAxozeVMMv8KPCChFaYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حامله شدن دختر 20 و 18 ساله توسط همسر 50 سالشون!
🎙
خانوم دکتر:
یه آقای 50 ساله به همراه دوتا همسرشون که یکیشون متولد 85 و یکیشون متولد 87 بود، بهم مراجعه کردن.
خیلی جالب بود که دوتاشون با هم حامله شدن و میخواستن تاریخ سزارین‌شون تو یک روز باشه و این برای من خیلی عجیب‌تر بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69651" target="_blank">📅 23:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69650">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5609274449.mp4?token=sPodSI4EMZ0v85VhJOwPW7YgScnn_Y3kAciOwS5KdhNOiYW2m8ry3NBbUkEzdFJtkiSaYKnGnkpiTBIzupQafjqfyk26lVwhatbiQoCZt-3F1lDWheRguI4ca8WljlKy4pTFok1SQ9R6K5zFN6EPKYBV1W8QN-nGxMumzNQB9qXVs32PNLZf4PHqqVOYRHhMUQ3IT8aeSe5FD-lADmyZwgGneJkLkp01VYwF14x7G-dkr0eaaSkB1B_fDgmiXrg1zH1br0M1dLZ39K9k32TzjYHs-qmrutSM7J4b9rKRHDAbyndkUO-43qSimAsw8pQGtBEiHCkJWd1ctqVIroiKsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5609274449.mp4?token=sPodSI4EMZ0v85VhJOwPW7YgScnn_Y3kAciOwS5KdhNOiYW2m8ry3NBbUkEzdFJtkiSaYKnGnkpiTBIzupQafjqfyk26lVwhatbiQoCZt-3F1lDWheRguI4ca8WljlKy4pTFok1SQ9R6K5zFN6EPKYBV1W8QN-nGxMumzNQB9qXVs32PNLZf4PHqqVOYRHhMUQ3IT8aeSe5FD-lADmyZwgGneJkLkp01VYwF14x7G-dkr0eaaSkB1B_fDgmiXrg1zH1br0M1dLZ39K9k32TzjYHs-qmrutSM7J4b9rKRHDAbyndkUO-43qSimAsw8pQGtBEiHCkJWd1ctqVIroiKsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
انتقاد رونالد ریگان چهلمین رئیس جمهور ایالات متحده از جیمی کارتر در قبال رفتارش نسبت به ایران و شاهنشاه آریامهر:
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69650" target="_blank">📅 23:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69649">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kJpqaDoHjXLi0h1mMChPvwuhzzJJARbVRjB7_9tG_iSN3dLfOof7_X9N62zW5vk64hVAW_VVZ4C8u6ObgTEo0YD1oxBoMmcsbfzaxaM3NO-Qjzqc3HRIixBGL_dhcqIaBRek6k6aoisH1PxfzT4cctdOfwAAvsyS6zY_QuYJ1W1WzHnh9_52y6A4p3EP5RdhzwGNP7opcHDkQ-8FCdD6RAXztN0u832TgE7Noi3QM05Rff42LT5rxwiGT-DQJ0GEN-62vlBGEk_lxMqdByhBFGPDyEoGRFVEGGeRIOrUy0Jlh5SEq5mnJPjqQx_if5S27OMCQiA9xkUZWNagwK1kcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
«حمله‌ای عظیم در راه است... صبر کنید، بی‌خیال؛ آنها می‌خواهند مذاکره کنند.»
این همان نمایش دیپلماسی است که مدام تکرار می‌شود.
استفاده از زورگویی، وعده‌های نقض‌شده و اخبار جعلی به‌عنوان اهرم فشار، راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتری نیاز نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69649" target="_blank">📅 22:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69648">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/164214744c.mp4?token=YSGrL1BWmmKuPGbEtujFwkqOWhCwkWwpU_lBxUeweAomNKbXTmt6_kqgc16EPRhWC9sjAp5Yd2BIaVl_NoGNYTLBR8xGUr2UyHlPLI3U5nsZYjnM5zldCyw-3qqHQ36dORiUV9O-OicNMMvBnb4TiaKmP6X9X2xvxaqTI8lOdk2tkFPOXe4ICKb3RVJrgD_kh16ZtDHkhDC6RkCJ3BhTmF9SKFPIR1WpG7NwzCjvomkc6ZBjg6alGSGqLZeFeifNg1JbJv9835rV7xawi9paAKDY7jrW5YpU4p5SpJveVptYC2fkIJKyqQrTKnxYjzqO46efzr7and00NS7lYLevRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/164214744c.mp4?token=YSGrL1BWmmKuPGbEtujFwkqOWhCwkWwpU_lBxUeweAomNKbXTmt6_kqgc16EPRhWC9sjAp5Yd2BIaVl_NoGNYTLBR8xGUr2UyHlPLI3U5nsZYjnM5zldCyw-3qqHQ36dORiUV9O-OicNMMvBnb4TiaKmP6X9X2xvxaqTI8lOdk2tkFPOXe4ICKb3RVJrgD_kh16ZtDHkhDC6RkCJ3BhTmF9SKFPIR1WpG7NwzCjvomkc6ZBjg6alGSGqLZeFeifNg1JbJv9835rV7xawi9paAKDY7jrW5YpU4p5SpJveVptYC2fkIJKyqQrTKnxYjzqO46efzr7and00NS7lYLevRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:
پزشکیان: ما بچه که بودیم پنکه نداشتیم
مجری: آخه آذربایجان خنکه
پزشکیان: من تو زابل خدمت میکردم
مجری: آخه شما میگی وقتی بچه بودم
پزشکیان: من تو زابل خدمت میکردم و پنکه‌ام نداشتم، حالا چی میگی؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69648" target="_blank">📅 22:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69646">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
گزارش غیررسمی از شنیده شدن ۲ صدای انفجار در قشم  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69646" target="_blank">📅 21:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69645">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
گزارش غیررسمی از شنیده شدن ۲ صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69645" target="_blank">📅 21:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69644">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c949993e0a.mp4?token=r-KYJiQp4FwyQsq23bsTS-ArnYu7VimEZXdlAN1uICGWkI8sARr-yX0qPaE43H2CVTtFHHOy1GBNuPP5GeJhuy_XOs7Tn58LpfiUOzKhq74-rl0LSnLXW5SVjls1i4IPBfmJiYAru0Mmvv4qqwcV-mWfPNSQzRBOIJ3lHUKJj7IR1OpKdZaC4voHWANyP1F0Z-r48besmJt8ptgrlV9pC3U1LzAv5EsD94boEyRiGJnMY4eYPwp_RFRzHH48kJMoZGs7Qr8hweaP63EciR-QXjFjZYIeHRQ9u3TE17p8A6eK9htiaqP4L4aeNJAtrAK3Ya83xhq05aPy0HW7LgmX-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c949993e0a.mp4?token=r-KYJiQp4FwyQsq23bsTS-ArnYu7VimEZXdlAN1uICGWkI8sARr-yX0qPaE43H2CVTtFHHOy1GBNuPP5GeJhuy_XOs7Tn58LpfiUOzKhq74-rl0LSnLXW5SVjls1i4IPBfmJiYAru0Mmvv4qqwcV-mWfPNSQzRBOIJ3lHUKJj7IR1OpKdZaC4voHWANyP1F0Z-r48besmJt8ptgrlV9pC3U1LzAv5EsD94boEyRiGJnMY4eYPwp_RFRzHH48kJMoZGs7Qr8hweaP63EciR-QXjFjZYIeHRQ9u3TE17p8A6eK9htiaqP4L4aeNJAtrAK3Ya83xhq05aPy0HW7LgmX-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
تصاویر اولیه از تاکسی پرنده‌ای در چین که قراره به زودی شروع به فعالیت کنه...
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69644" target="_blank">📅 21:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69643">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slIzB-M1TYVpr0xLTieDEvIFs9X516Vg1DihzzphWTHbGpJ1LKhINtHoUcliLqRJQg4ggA5Togo6bOlbKfFVZZL6CJLw5kMyRgCj2Rmxhsv9wsKbpRz3I6wZnk_OXU_i0igg7qQfeSGRPaAvuSwH-4GdqePq8FgbBCNk3yorscWKCya20k825m6jhcrg6-wLrAPYmpeqaOCWc2m4fgsGRpZHb0SuLJ1a9HSeIuqkEh5a0kQ2AhLMNGZOLpuL6dVQPHcokS26ugEPp4k3cm5q62mhsU8JkbUEYLbJK57J3tyBbeFNWcsOWxRWadodWCJ6NcYCfIRpCatgVGdLuQEocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
خبرنگار الجزیره :
تنگه هرمز: به نظر می‌رسد توپ از زمین ایران و عمان خارج شده و به زمین آمریکا افتاده است و اکنون چشم‌ها به رئیس‌جمهور ترامپ است تا در مورد جزئیات باقی‌مانده و تعهدات آمریکا تصمیم بگیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69643" target="_blank">📅 20:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69642">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH4EQT-L4xfG3ydR91AyuGyuxowqX2yVPJOmnISiQ1hZOnSJacIiDSzgZR7RUGFh--z-mDi8g7dAj-5K7Xoo4_vWfaabbzZoZtj-fOndydrKczLTOjbAz_09_-EjASEAB7MxBbOBBF-P_FpAqg16nuVIm-ND9Zwhou61elyNUQ9V7hSkAfTlnaPBB3iTHVR8oSLCl3tMwT8kEryxDlsN0-lNYKJSfu7nFK2hyfejG7m3hB-aArC7reIlPOIa3FmAR_fpwS-yXzkRTVmkF5PXzXff8sgranfIOZay0VA7K3x1Qp_I_wL4hNJMhpUzHvk_mt1s3iHckuzMj47drZxDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
رسانه‌های «اخبار جعلی» طبق معمول در حال پخش شایعاتی نادرست و کاملاً بی‌اساس هستند.
من از عملکرد «پیت هگسث» بسیار راضی هستم.
همه چیز فوق‌العاده پیش رفته است، از جمله عملیات ما علیه ونزوئلا که نتیجه آن در کمتر از یک روز حاصل شد و به ما امکان داد تا یکی از بدترین جنایتکاران جهان، یعنی نیکلاس مادورو، را به دست عدالت بسپاریم!
در مورد ایران نیز وضعیت بسیار خوب پیش می‌رود؛ کشوری که با هدفِ «جلوگیری از دستیابی‌اش به سلاح هسته‌ای» در هم کوبیده شد!
پیت در میان نیروهای نظامی از احترام بالایی برخوردار است و پیشرفت‌های چشمگیری ایجاد کرده است؛ از جمله حذف سیاست‌های DEI (تنوع، برابری و شمول) و افزایش آمار جذب نیرو به سطحی بی‌سابقه.
این شایعه توسط «واشنگتن کام‌پوست» (Washington ComPost) — که یکی از بدترین رسانه‌های این حوزه است — به راه افتاد؛ آن هم با وجود اینکه ما به آن‌ها گفته بودیم گزارششان کاملاً دروغ است.
در واقع، من عمیقاً معتقدم که «گزارش‌دهی» جعلی آن‌ها مصداق خیانت است!
رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69642" target="_blank">📅 20:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69641">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50525385c.mp4?token=QFCcM_6M9SWgLgvi8lk6WdGyR4HtKZbOH6KAjvoNnabxHxCqslp-0Awx8dH8pz7OjfFQM2mk5q-hlS8JzmPrVsnOa6sFGGZp0IcGFtXYP2X91u3Cv03p6d3Wr4IjDq3ErBFVh0ZUeViT0MPbuA0-5KjKnEaqUEQjWryqeFQqo9667TrGFRSyMLjUTa7zZFYFTU2acfRx0Hl-g6vmBIagGWhNDOoscmaXTSyH72Rf2OdEtC0RDp1sgy3u8IqSBSutPaYYvEqBqLMO1T4PIbH2D_XHAOxLeFr2Jv4DFKOihh-68UgdsfZHWKfU_jKfd0mnVUY4YmiAsy-iIN_wiHqRIYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50525385c.mp4?token=QFCcM_6M9SWgLgvi8lk6WdGyR4HtKZbOH6KAjvoNnabxHxCqslp-0Awx8dH8pz7OjfFQM2mk5q-hlS8JzmPrVsnOa6sFGGZp0IcGFtXYP2X91u3Cv03p6d3Wr4IjDq3ErBFVh0ZUeViT0MPbuA0-5KjKnEaqUEQjWryqeFQqo9667TrGFRSyMLjUTa7zZFYFTU2acfRx0Hl-g6vmBIagGWhNDOoscmaXTSyH72Rf2OdEtC0RDp1sgy3u8IqSBSutPaYYvEqBqLMO1T4PIbH2D_XHAOxLeFr2Jv4DFKOihh-68UgdsfZHWKfU_jKfd0mnVUY4YmiAsy-iIN_wiHqRIYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
دیشب روسیه هم یکی از سنگین‌ترین حملات خودش رو علیه اوکراین انجام داد و اينجوری کی‌‌یف رو ترکوند!
4 فروند موشک مافوق‌صوت زیرکن/اونیکس (3M22 Zircon/Oniks)
24 فروند موشک اسکندر-M و موشک‌های شلیک‌شده از سامانه S-400
115 پهپاد تهاجمی، از جمله پهپادهای شاهد (که بیشترشون از نوع جت‌دار بودن)، پهپادهای Gerbera و Italmas، و همچنین پهپادهای فریب‌دهنده Parodiya
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69641" target="_blank">📅 20:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69640">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am-E0sY4es1Dx_9ideTA5If-NB4JpYTOAwKHV6HReZuLQRmSUkVOyj4LioBffot19OhJkA--7v7T8eZn9tlulcKGjeICOxT6ueCfApFBgpE_T0TS_YFOea7MdlkDIHqyf-XYV8f_h-j9Zob-xiFlvDeDhYli_skvQ4vlJLA-6sj82nbMknTo7scYtOcc3UO_jEFq1PNHQglVVHItaXlBvkvpbo4shfsRT5e6zTgN4DgJ6sCcEw2ftA8LSQ8luStG6ugvuy6CsI-OhzQ7tFou95xrAVyJeITuTsHoh0ZmYIde8gz6VKzWWthowWFIsgDqFyV7MaD3pNJSFLfGqLRvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
پس از استعفای محمدباقر ذوالقدر، فیلد مارشال محسن رضایی به‌عنوان نماینده رهبری و دبیر شورای عالی امنیت ملی منصوب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69640" target="_blank">📅 20:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69639">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇴🇲
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.
🔴
براساس این طرح: عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی و سایر کشورهای متخاصم از تنگه هرمز ممنوع…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69639" target="_blank">📅 19:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69638">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇴🇲
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.
🔴
براساس این طرح:
عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی و سایر کشورهای متخاصم از تنگه هرمز ممنوع می‌شود.
محموله‌های مرتبط با رژیم صهیونیستی، اعم از نظامی و غیرنظامی، حق تردد از این منطقه را نخواهند داشت.
شناورها یا محموله‌هایی که در اقدامات علیه جبهه مقاومت نقش داشته باشند نیز مشمول ممنوعیت خواهند بود.
کشورها و اشخاصی که به ایران خسارت وارد کرده‌اند، تا زمان جبران خسارت، مجوز عبور از تنگه هرمز و خلیج فارس را دریافت نخواهند کرد.
برای قانون‌شکنان، جریمه‌های سنگین از جمله تا ۲۰ درصد ارزش محموله، پیش‌بینی شده است.
دولت موظف خواهد شد با همکاری نیروهای مسلح، مسئولیت‌هایی مانند هدایت ناوبری، نظارت بر تردد شناورها و حفاظت از امنیت و محیط زیست خلیج فارس را برعهده بگیرد.
این طرح همچنان در مرحله بررسی کارشناسی قرار دارد و مجلس از صاحب‌نظران خواسته پیشنهادهای خود را برای تکمیل آن ارائه کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69638" target="_blank">📅 19:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69636">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a34485680.mp4?token=aR0THOn1uZ28HAzgeNjTFvhQZVB0zfcjZQ9NQbcx9vqNMs5RWGD2XQzZZs21utGAoKEI4eQ8Ev3ToGAoLUWdzpIQDXnaQRER8l29L28anHSXNEyRfUwZZmLF1Ac3UbrFF9Eh8MpUZSbDKB_cYIi86hisWguim-qc8JtVjC9bAk7blabx2II4WS4Sqj_3_YdBZolNhy4SiLZgW6_AuGhe6GRdzOcX5UZ4QIsF5gBSSoMrjWQzMqiID37Q551X1-tAJJfnPQLih4vdehTebwDuQWzrb0dKWnCcGKVo8fZjBXiUnG3EO3E_eh_tXXANVIJb8YhF-UI0XQlIICRPP46zypWpYxZFqMJlBztISob11pkXioXXC_Es71LgpwFLtjqBP2ZO2vvvcv65JTvhfGoKAt7yPhsBsH43UfvoVcbLbFgSGQOWRTctn1RuMsBxHyCPDifAHfwmM-xTJSYkzrVgeYjeOI6hiMgwecI2uDkxb_9JwWGwKUwTnOfM0sWYEJ-r6eLJgndkbcAGOGis6EcAm1I7bOy3OCveNLHxLkasknnjx-PKtGLMmthIsWioLE2FZCgob_2YI3x0f0dVo0zOB_ur2i2n_jg3q4jPA6zTqVLDSYyp98yezZEHI0e5OAFuRxzn2bvapS-8D9rqdvHOx6acV91i8-3ggOfImmUP0u4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a34485680.mp4?token=aR0THOn1uZ28HAzgeNjTFvhQZVB0zfcjZQ9NQbcx9vqNMs5RWGD2XQzZZs21utGAoKEI4eQ8Ev3ToGAoLUWdzpIQDXnaQRER8l29L28anHSXNEyRfUwZZmLF1Ac3UbrFF9Eh8MpUZSbDKB_cYIi86hisWguim-qc8JtVjC9bAk7blabx2II4WS4Sqj_3_YdBZolNhy4SiLZgW6_AuGhe6GRdzOcX5UZ4QIsF5gBSSoMrjWQzMqiID37Q551X1-tAJJfnPQLih4vdehTebwDuQWzrb0dKWnCcGKVo8fZjBXiUnG3EO3E_eh_tXXANVIJb8YhF-UI0XQlIICRPP46zypWpYxZFqMJlBztISob11pkXioXXC_Es71LgpwFLtjqBP2ZO2vvvcv65JTvhfGoKAt7yPhsBsH43UfvoVcbLbFgSGQOWRTctn1RuMsBxHyCPDifAHfwmM-xTJSYkzrVgeYjeOI6hiMgwecI2uDkxb_9JwWGwKUwTnOfM0sWYEJ-r6eLJgndkbcAGOGis6EcAm1I7bOy3OCveNLHxLkasknnjx-PKtGLMmthIsWioLE2FZCgob_2YI3x0f0dVo0zOB_ur2i2n_jg3q4jPA6zTqVLDSYyp98yezZEHI0e5OAFuRxzn2bvapS-8D9rqdvHOx6acV91i8-3ggOfImmUP0u4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی تهران برای افراد بالای 30 سال هم مهد کودک زدن !
یعنی شما صبح که از خیابون داری رد میشی ممکنه یه مرد 40 ساله با کوله پشتی عروسکی ببینی
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69636" target="_blank">📅 19:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69633">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCQa_gZjO6NnXA87E4b2zluastmSVZIuwMGG9GhpPpY8cZLvslUWdol16315IvDlofPwvga6QTOe_fXju52I0sr1VuS9RxroITNnISrzfihyLyZ6AuBFN-HhmxnLZ1Op3FF2fJuFRlbuT2MTVjbpRcydgLVcKnIIYe9dxpIlQOqb5kyheHW9vEOMAC4EpAwhWloDoQMFlnuH7GqePHq13ihud5Nmz0VfJ6w4OQambBwfnQFC42NhpLP9Nr7kVZrkMo0wa5HhgiJEI1sifwR9Avf6xiyNPC4_sEBjIKBuwJq8Xr1zYtll1Y1M71pZUk2QXX3ivsAdnPiFzjZIuBXauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a607d311.mp4?token=koF_z2FM5HbqdfVpsztk2bsqlpZiDKp30hddNmy9FArmWT04nu_LGuFQEN9x4ymNL0Rh5T054FHtYoZ8ZwBxlwHRt1LZ5nsxf1N4DfQDOeDvcYtSFSuCTCSZVDCLoNPQl-KW_BQfk86XyFmKJsJLpOPmBdMhBvqR5ojggjeoASURjqkSMK1qWesYQlG5ADgZOMsNUIAQUbTHNhMThwEgjv8ONy8iwulRvwMgqf95pzPuUEvqXlcAiRPVIMxlSuYfoq7Mq6WuNXAAGPIWlzZfQClU42Nh08QmAhhb0AWsqdSU5olZ6LazU0Za2_k-UBJ-21_OK8EJDNXlpXMLVCejVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a607d311.mp4?token=koF_z2FM5HbqdfVpsztk2bsqlpZiDKp30hddNmy9FArmWT04nu_LGuFQEN9x4ymNL0Rh5T054FHtYoZ8ZwBxlwHRt1LZ5nsxf1N4DfQDOeDvcYtSFSuCTCSZVDCLoNPQl-KW_BQfk86XyFmKJsJLpOPmBdMhBvqR5ojggjeoASURjqkSMK1qWesYQlG5ADgZOMsNUIAQUbTHNhMThwEgjv8ONy8iwulRvwMgqf95pzPuUEvqXlcAiRPVIMxlSuYfoq7Mq6WuNXAAGPIWlzZfQClU42Nh08QmAhhb0AWsqdSU5olZ6LazU0Za2_k-UBJ-21_OK8EJDNXlpXMLVCejVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69633" target="_blank">📅 19:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69630">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47221b6a95.mp4?token=qO8gxhP222Zv_2FXO0s28MsfpZJdkxqDM4v3vWSmi1E_gJlFqdoGJkhkl1Rb0_15u8GOgaxLja75S6h2bX2tX0wDpx3MLRtqw81nLQcCVepzEW0NNKjfh687TX9t6Tylo90-M0J6B0rMpONUKtMhgHO1P_bw-RJMMFp0itdm97-zOXyb4y4A7YqEYdFvGzkvqSbsNCLaEb80Dx2-7qaebYXPy2GThhpbQuJ75SIidTS7FJnbAnQGm4KPM7sHzGST3l6RhM2VqVWdaEinlHWrqmdWgfKMqCnqd4BU0BoGa284TMlfACf56ciUYnduWxrfdimNJRQS_X8K0NNfut7L_Gho4Ivzcc-kxMqrXk1vew6fMdu5WDZcxZWsuf1J2KFQngJmmRbVtS6YoCfL-iJkdvjf5E1h3TpPznLLNl-_dGwYORAIG9WnGKoKTQBJzzBiIt_KwsG8iTHA1wGhzssiVToBNQfnnNAB6iLezDIGdryx92UDSSeRnFd2XFZZw9bDbBHt5yHS4XSzRn1FfAp6IAphM-nfUmDAfZKxcGVWsfiFQ0h8FrLA9XVpF8Ba2icmadAacLIMnfEOFFXDZmFP9GVNYaPb0QEwUXldAVyl3XvQx8WOm2EO06K2rFcWzgVPIni2_F-Ms9up5x5y9qf_IO-JaVC0DJs1l5oi1_rbqeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47221b6a95.mp4?token=qO8gxhP222Zv_2FXO0s28MsfpZJdkxqDM4v3vWSmi1E_gJlFqdoGJkhkl1Rb0_15u8GOgaxLja75S6h2bX2tX0wDpx3MLRtqw81nLQcCVepzEW0NNKjfh687TX9t6Tylo90-M0J6B0rMpONUKtMhgHO1P_bw-RJMMFp0itdm97-zOXyb4y4A7YqEYdFvGzkvqSbsNCLaEb80Dx2-7qaebYXPy2GThhpbQuJ75SIidTS7FJnbAnQGm4KPM7sHzGST3l6RhM2VqVWdaEinlHWrqmdWgfKMqCnqd4BU0BoGa284TMlfACf56ciUYnduWxrfdimNJRQS_X8K0NNfut7L_Gho4Ivzcc-kxMqrXk1vew6fMdu5WDZcxZWsuf1J2KFQngJmmRbVtS6YoCfL-iJkdvjf5E1h3TpPznLLNl-_dGwYORAIG9WnGKoKTQBJzzBiIt_KwsG8iTHA1wGhzssiVToBNQfnnNAB6iLezDIGdryx92UDSSeRnFd2XFZZw9bDbBHt5yHS4XSzRn1FfAp6IAphM-nfUmDAfZKxcGVWsfiFQ0h8FrLA9XVpF8Ba2icmadAacLIMnfEOFFXDZmFP9GVNYaPb0QEwUXldAVyl3XvQx8WOm2EO06K2rFcWzgVPIni2_F-Ms9up5x5y9qf_IO-JaVC0DJs1l5oi1_rbqeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇱🇧
ارتش اسرائیل (IDF) اعلام کرد که در ۲۴ ساعت گذشته، مجموعه‌ای از حملات را علیه "اهداف حزب‌الله" در مناطق جنوبی لبنان انجام داده است. این اقدام در پاسخ به انفجار بمب در منطقه مجدال زون انجام شد که در آن دو سرباز ذخیره اسرائیلی کشته و چهار نفر دیگر به شدت مجروح شدند.
ارتش اعلام کرد که این حملات، انبارهای سلاح، مراکز فرماندهی و سایر زیرساخت‌های حزب‌الله را هدف قرار داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69630" target="_blank">📅 18:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69627">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acnDkmIFxFXWbSu2sa6raMh2I6ptQSqBgpMoZ1UXWLOT9xAebZY5yOVoOn9ElHiZHbOswotoRnA3pvFQuXysTGwbKnXY6EkBL3Vb29l1WBuTfzWM4LL3ETzvm0li6YH7OWFv7AUYLvBER0v17IV9_irTq_MEaEJlyWA6BnBywC68WtAK0K9Q_CBfJf3obQWPzyWmdkSzAqd0yZ3R099Txcdkp9iNskPD5L1j1m2BlIZevcc6WJuThNN9enCOrZtYjf72gw8qI98kKWpH4bbQ_9zUt2EKu4bRMAasdN61XK7m3c-SYQjSLzl9pf2spfsdoBr0QxR5MMDs_l_ytr-g2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb7351e85c.mp4?token=i2Sceas6KsPCRkhfjuMHRQf0MgiMXEBFR1C5AMOPTbozRL_0t4ABf-V46GCfocUonh4Gg9lpqNmEoVgt8YRcNHea6W9BiSquQT2WX_9CdADyAZiiD5Cwzms0kfKphZ0Ir6h2FEpUK5i_1rXhPgAe7CpzHUoy2VxiUv6qVgLrqLSOaGApltdWZxjjoHec5eA5RHJqu5-3hV93IYHjuPDBtVKrwqfpUzL43m7CHDfD90NzuE2cq98ubImCXgPyERICejINj8gVOkJDgsQnFSaiERj3sjDB8TEnhYGPcQFEbN2jV-gQyAACc-C67zSrKIUgVZPhdW7jWnRouVEf8rXu4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb7351e85c.mp4?token=i2Sceas6KsPCRkhfjuMHRQf0MgiMXEBFR1C5AMOPTbozRL_0t4ABf-V46GCfocUonh4Gg9lpqNmEoVgt8YRcNHea6W9BiSquQT2WX_9CdADyAZiiD5Cwzms0kfKphZ0Ir6h2FEpUK5i_1rXhPgAe7CpzHUoy2VxiUv6qVgLrqLSOaGApltdWZxjjoHec5eA5RHJqu5-3hV93IYHjuPDBtVKrwqfpUzL43m7CHDfD90NzuE2cq98ubImCXgPyERICejINj8gVOkJDgsQnFSaiERj3sjDB8TEnhYGPcQFEbN2jV-gQyAACc-C67zSrKIUgVZPhdW7jWnRouVEf8rXu4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
زلنسکی:
امروز صبح دو پالایشگاه‌ مهم روسیه رو هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69627" target="_blank">📅 17:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69626">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d7912f58.mp4?token=dBpKGXKPX3Gt6hIB5gOlaluHs4wNZL6v0iZdf3vBjEcPOCjU0epcsj-jBx8-u6zZ3A11pdVK88yn3yfgSE9nJcDR4rZnM_J7C58JnO-vK7ZeyqDsgsx2LcKp6mQzxBgscwwxkSt35frON7l-6eBT3TOKjmju7HfhUjsUqtu6_QW9axPkhBqqWytR9AwcFETZomLKCc5I7ZcpONXXHuT-5diCY94MyTeH0aeBA7d1zqVhioLlVxH5DitAoUJtH9UhxpgYb-T9eorN9pLOGWv0KjG4mwGfPjW4I1RF4IbCjtyFEN1BeJwjzyCOZKcACpDdqCNAdc0vjv_Nm4_znvtQspy2QTVbjHu-1k-GQAPb3OPGOQaSDCF--q4BpM_7OMDcyh91b-BOJF_0oXedUzi8gWeBSWofmkWER-pzLIozRFwbkwXFS9GejO-t8ks5Uva4R4tsv0PFiBCPAMSnMJQPA5r833X4L44HBdWjqjXE_OOQM7zQ9PFBA4oKt9GVcKyNbImlbN9DdI0BqQXCsY26v0EtJ7DJU9A0qigQM6POcyQsOjBm3y-n9CAsu6BxSMRHO9q0SJdmRbxKv26sVqhvhltZUxzG5Fo4UzM-lOfrA24RLnO1A7oxJRBCcpQu2KZiluSAxXRB5teFH7cdysscWsk3w4dQvssronmme9NR-CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d7912f58.mp4?token=dBpKGXKPX3Gt6hIB5gOlaluHs4wNZL6v0iZdf3vBjEcPOCjU0epcsj-jBx8-u6zZ3A11pdVK88yn3yfgSE9nJcDR4rZnM_J7C58JnO-vK7ZeyqDsgsx2LcKp6mQzxBgscwwxkSt35frON7l-6eBT3TOKjmju7HfhUjsUqtu6_QW9axPkhBqqWytR9AwcFETZomLKCc5I7ZcpONXXHuT-5diCY94MyTeH0aeBA7d1zqVhioLlVxH5DitAoUJtH9UhxpgYb-T9eorN9pLOGWv0KjG4mwGfPjW4I1RF4IbCjtyFEN1BeJwjzyCOZKcACpDdqCNAdc0vjv_Nm4_znvtQspy2QTVbjHu-1k-GQAPb3OPGOQaSDCF--q4BpM_7OMDcyh91b-BOJF_0oXedUzi8gWeBSWofmkWER-pzLIozRFwbkwXFS9GejO-t8ks5Uva4R4tsv0PFiBCPAMSnMJQPA5r833X4L44HBdWjqjXE_OOQM7zQ9PFBA4oKt9GVcKyNbImlbN9DdI0BqQXCsY26v0EtJ7DJU9A0qigQM6POcyQsOjBm3y-n9CAsu6BxSMRHO9q0SJdmRbxKv26sVqhvhltZUxzG5Fo4UzM-lOfrA24RLnO1A7oxJRBCcpQu2KZiluSAxXRB5teFH7cdysscWsk3w4dQvssronmme9NR-CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇰🇵
🇺🇦
روسیه در حال آموزش نیروهای جدید از کره شمالی است احتمالاً به منظور آماده‌سازی برای عملیات آتی در اوکراین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69626" target="_blank">📅 17:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69625">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d7f55ab9.mp4?token=ey0xXSfRvS3n10g-nrZzf6qaOMStNJeIyLlLD-gt4Pf_4w_k6WOZYP2PAeGI-JRxbQcpXuiJ6P0v9Vp4ihhTVxDSnXM054EUyuYN3UxMmKCCogwnQbFExOwJih-CTR9Fpu-Nq0JNGTFnDXdYgMjVUT3sKw1Yf1b5FDRrMJEXYwA398NRP3DEIG4mK8_ttVJ-76LXNVQprYidqZQNMOwfpr7BCpSAwHSm7VlFPf0iRIxHhjU7DgUr_PPRaC39IDrRtkZgIPjAM0sr2FRohwt1NjUtPUsN6vTpk5g-lSTt-9klB2l6vEKpMzuXRj8d2Pa497ZDZmT14nnOTWkOL04Wbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d7f55ab9.mp4?token=ey0xXSfRvS3n10g-nrZzf6qaOMStNJeIyLlLD-gt4Pf_4w_k6WOZYP2PAeGI-JRxbQcpXuiJ6P0v9Vp4ihhTVxDSnXM054EUyuYN3UxMmKCCogwnQbFExOwJih-CTR9Fpu-Nq0JNGTFnDXdYgMjVUT3sKw1Yf1b5FDRrMJEXYwA398NRP3DEIG4mK8_ttVJ-76LXNVQprYidqZQNMOwfpr7BCpSAwHSm7VlFPf0iRIxHhjU7DgUr_PPRaC39IDrRtkZgIPjAM0sr2FRohwt1NjUtPUsN6vTpk5g-lSTt-9klB2l6vEKpMzuXRj8d2Pa497ZDZmT14nnOTWkOL04Wbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
خرازی(برادر زن مسعود خامنه‌ای):
«آیت الله مجتبی خامنه ای سه سال از دفتر رهبری طرد شده بود.
برادر وحید حقانیان(از اعضای بیت رهبر شهید) عضو سیا بود.
پزشکیان الدنگ و پرت است.
قالیباف هیچ چیز از دین اسلام نمیفهمد.
خدا لعنت کنه دکتر مرندی(پزشک علی خامنه‌ای) ملعون.
دفتر آقا فاسد است، حتی دکترش هم فاسد است».
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69625" target="_blank">📅 16:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69623">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761165b2c7.mp4?token=ibKIhJ5Nm8lm8qY1jyf0zBS_E0FSiblU9LJIXoNctgjtQ4li-nLz65JtKhY6NdOugXObQolajDLNbn5TeNSCG49oB4ZXn1bC5vwe--wBb-vKxdnJT70DGodNJ-DNjRF1Itpg1XPop9TmssnvHQaFVvDoBeDhhGCS3CckGKJO-KA_r9QVypeRHnGgkLGftywp80VZ7qf7kh27kmYwrOc1Lph-P5Dsu26AhJBI2mvnO97VJXMRyLKikQ-yTR-SEOtxcAZ3lTJoKTZQinJli5mrnItlui7BuCDjcpgdx6E7J-BpqpA0Ywff2fyREbNtoMuH43Aa5qA46EDLTHbL5M_hSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761165b2c7.mp4?token=ibKIhJ5Nm8lm8qY1jyf0zBS_E0FSiblU9LJIXoNctgjtQ4li-nLz65JtKhY6NdOugXObQolajDLNbn5TeNSCG49oB4ZXn1bC5vwe--wBb-vKxdnJT70DGodNJ-DNjRF1Itpg1XPop9TmssnvHQaFVvDoBeDhhGCS3CckGKJO-KA_r9QVypeRHnGgkLGftywp80VZ7qf7kh27kmYwrOc1Lph-P5Dsu26AhJBI2mvnO97VJXMRyLKikQ-yTR-SEOtxcAZ3lTJoKTZQinJli5mrnItlui7BuCDjcpgdx6E7J-BpqpA0Ywff2fyREbNtoMuH43Aa5qA46EDLTHbL5M_hSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
❌
🇸🇦
در حملات موشکی یمن به مواضع نظامی عربستان تاکنون بیش از 30 کشته شناسایی شده و انتظار میره تعداد تلفات بیشتر بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69623" target="_blank">📅 15:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69622">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
الحدث:
توافقی میان ایران و عمان در خصوص بازگشایی تنگه هرمز در ازای احتمال لغو محاصره آمریکا، قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69622" target="_blank">📅 15:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69621">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-SGkz0Smq6fTIlbKtHeoKfSrplykUx9wCueJtjbiU4mw9yuvBlT-KmLyCQ9bmj3q6B08iBCM1od9qK8uXmERNxlOTQGX3Ol80D6faOAw7xm30TtLYuJJV2KeN6U2ZOF974NTAUjPF_5RpvtpKa_hiduWE1thD-PUUbeSP7WXj3bZnG0Z6-51CzFDGlZmDT8y54UXRqZP0Z41yQgg4ihu4f_1K9GMFVP9Y6NNOiNilIeNLDKoEpv7s1akBYL2o07QBKmFazaHcxFTVu8lHYRNTSHl2r_ETs48wHfpGD16YveaVQQyXSa4gbNUjYqz_CcEaZFMRxMCXpzDhUra4FqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
واشنگتن پست:
🗣️
ترامپ به طور خصوصی به حامیان مالی جمهوری‌خواه خود گفته است که می‌خواهد جی‌دی ونس در سال ۲۰۲۸ پیروز شود
و از عباراتی مانند «ما باید جی‌دی را انتخاب کنیم» استفاده کرده است.
مشاوران تأکید می‌کنند که او هنوز به طور کامل در مورد جانشین خود به توافق نرسیده است و هنوز رقابت بین ونس و مارکو روبیو، وزیر امور خارجه، را حفظ کرده است.
🔴
یک منبع این موضوع را اینگونه خلاصه کرد:
«جی‌دی دارد به موفقیت می‌رسد و ترامپ آن را می‌بیند.» و خاطرنشان کرد که ترامپ دیگر به طور معمول نمی‌پرسد «جی‌دی یا مارکو؟»
البته او با مشاورانش همچنان برای این انتخاب در حال مشورت است
.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69621" target="_blank">📅 15:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69620">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj77G-sw6YH1ifzbtrMATXzEIptGpXdaDYQECMtL4guB_yZj6my5fEvitv2k7VtCbTCGShSKXcPetHKdpldJxO3Adf5qYfokU3IG6xrxbfLjbZ5itur6BynYEWdep5GEVP90-UgJytaXH_1ehOkRzKHgazmTpdKdg8fV_V_dIpYGHqGQUZgpuNHw8HwKLspy1IbDAz4FPgH8EhsPWDyJwoC1cV4vDQQG_QkscZcDKBp7zgD2NHUdV3SSpZyk1ECjdouJtUf8b1JMTdL6kOQ3g82d5sPQzcs7VValOViIO5_cnaFszGmoT2qzGBRX8YA6-2dyftB2UpWCdA0E29gHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
آمریکا از ناوشکن جدید کلاس Arleigh Burke Flight III؛ USS William Charette رونمایی کرد
نیروی دریایی ایالات متحده مراسم به آب‌اندازی و نام‌گذاری ناوشکن جدید
USS William Charette (DDG-130)
را برگزار کرد. این شناور از نوع
Arleigh Burke-class Flight III
بوده و بخشی از برنامه نوسازی ناوگان ناوشکن‌های موشک‌انداز آمریکا محسوب می‌شود.
◀️
نام‌گذاری به افتخار «ویلیام چارت» از نیروهای نیروی دریایی آمریکا که نشان افتخار Medal of Honor دریافت کرده بود.
🔼
ارتقای سامانه‌های رزمی
نسخه Flight III نسبت به نمونه‌های قبلی Arleigh Burke دارای بهبودهایی در بخش سامانه‌های دفاع هوایی و موشکی است.
مهم‌ترین بخش این ارتقا، استفاده از:
◀️
رادار AN/SPY-6(V)1
این رادار آرایه فازی فعال (AESA) بخش اصلی ارتقای ناوشکن‌های Arleigh Burke Flight III است. این سامانه برای کشف، رهگیری و مقابله با تهدیدات هوایی و موشکی طراحی شده و نسبت به رادارهای نسل قبلی توانایی بالاتری در شناسایی اهداف دارد.
◀️
سامانه رزمی Aegis
سامانه Aegis یک سامانه یکپارچه فرماندهی، کنترل و مدیریت تسلیحات است که داده‌های حسگرها را دریافت کرده و امکان کشف، رهگیری و درگیری با تهدیدات مختلف را فراهم می‌کند. این سامانه هسته اصلی توان رزمی ناوشکن‌های Arleigh Burke محسوب می‌شود و در نسخه Flight III با رادار AN/SPY-6(V)1 یکپارچه شده است.
❓
نقش عملیاتی
ناوشکن‌های Flight III برای مأموریت‌هایی مانند:
⬇️
دفاع هوایی ناوگان
⬇️
مقابله با تهدیدات موشکی
⬇️
اسکورت گروه‌های رزمی دریایی
⬇️
عملیات چندمنظوره سطحی به کار گرفته خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69620" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69619">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b6e5f9de.mp4?token=sORjR2Nw7fwPHbrTkLQg_5F1bhWw8Eh36sapS0LWXJg8e0s4SuhM8xo_IqoKccF10RIjwLHspupCb78od7XK293pGImd9t-ncBZWXjQiEXTa4K7ZnT6ID26_EtioaoIrZoAhTyGOjrGGoutNd5KS2FEb6MY993MOH3wloDI3ID30yob0clhe5619l1FsuB2oVTzuhNNA-dPJv0tGnsKcH0tL2azijl8d-2myk7yfGaxHQ8JZSWU_MjUgOffyLmDfvGVW_hJ4jQNXwbEHbTiYhWqVZEPwvKM1iAvVzT8GyujqjMtxGPOMSzTpQ2lZY6NZAgVuyzAHgYysPEJeNl2GBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b6e5f9de.mp4?token=sORjR2Nw7fwPHbrTkLQg_5F1bhWw8Eh36sapS0LWXJg8e0s4SuhM8xo_IqoKccF10RIjwLHspupCb78od7XK293pGImd9t-ncBZWXjQiEXTa4K7ZnT6ID26_EtioaoIrZoAhTyGOjrGGoutNd5KS2FEb6MY993MOH3wloDI3ID30yob0clhe5619l1FsuB2oVTzuhNNA-dPJv0tGnsKcH0tL2azijl8d-2myk7yfGaxHQ8JZSWU_MjUgOffyLmDfvGVW_hJ4jQNXwbEHbTiYhWqVZEPwvKM1iAvVzT8GyujqjMtxGPOMSzTpQ2lZY6NZAgVuyzAHgYysPEJeNl2GBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
مراد ویسی تحلیلگر ارشد اینترنشنال:
قاجاریه در عهدنامه‌های ننگین گلستان، ترکمانچای و آخال، سرزمین‌های ایرانی در شرق و غرب دریای خزر رو به روسیه واگذار کرد.
حالا جمهوری اسلامی، از سهم ایران در دریای خزر به دلیل نوچگی روسیه می‌گذره.
مردم ایران، این روزها رو برای تاریخ به خاطر بسپارید؛ جمهوری اسلامی در حال رقم زدن خیانتی بزرگ به ایرانه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69619" target="_blank">📅 14:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69618">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de4ded641.mp4?token=o14m7DBeo2UMUAoj3pLDrHLa4_7pLLm21eod7oT1mBYeqf-eiFSYEFo5t3SvMso0pQXMWs7PfRp-rg-4oLIAoBmUO55gQAE1ZcoL-KWCpqQYpD6sxFlg7iQ7EKRy4H_KIrGj906VTc_3yx73IYVtz6T9Pqe4j-3y-WSr69_FRHUQ4ZtO4oJoFTnm0k0n4VoMgOGARCd4RcebSwN8IfhdaqGTfJBvMtVhxqucBiVq-yeKDAVMFNVd4ZRupBNxBlAcTQmeMz9SvwWMB26alEpgPwyskCtI8J-NrYFnj04oKUzQb3qBJXPH8-6EhY3tXj7d74Rg9FrHwbQjywLfp6REKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de4ded641.mp4?token=o14m7DBeo2UMUAoj3pLDrHLa4_7pLLm21eod7oT1mBYeqf-eiFSYEFo5t3SvMso0pQXMWs7PfRp-rg-4oLIAoBmUO55gQAE1ZcoL-KWCpqQYpD6sxFlg7iQ7EKRy4H_KIrGj906VTc_3yx73IYVtz6T9Pqe4j-3y-WSr69_FRHUQ4ZtO4oJoFTnm0k0n4VoMgOGARCd4RcebSwN8IfhdaqGTfJBvMtVhxqucBiVq-yeKDAVMFNVd4ZRupBNxBlAcTQmeMz9SvwWMB26alEpgPwyskCtI8J-NrYFnj04oKUzQb3qBJXPH8-6EhY3tXj7d74Rg9FrHwbQjywLfp6REKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از صحبت های یک دختر درباره مادرش:
❓
کی گفته هر مادری قابل احترامه؟
از میزان اشغال بودن مامانم اینو بگم که تو سن 13 سالگی پریود شدم و وقتی بهش گفتم منو تو خونه 3 روز زندونی کرد و گوشیم گرفت و کلی کتکم زد
بهم گفت تو چه گوهی خوردی تو هنوز بچه ای چرا باید پریود بشی؟ و این خون یه چیز دیگس!
از 12 سالگی هم منو میفرستاد سرکار میگفت باید خرج مدرسه و خونه رو کمک کنی بدی!
همینطور که اینارو میگفت تا اول دبیرستان بیشتر نذاشت درس بخونم و 15 سالگی ترک تحصیل کردم
مامانم گفت لازم نیست درس بخونی باید بیشتر کار کنی چون خرج ها رفته بالا اجاره خونه بیشتر شده باید بری کار کنی
به محض اینکه هم 18 سالم شد از خونه زدم بیرون و الان 6 ساله نه میدونم کجاست نه شمارش چیه نه باهاش حرف زدم
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69618" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69617">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79de90eb9.mp4?token=eyTWZ6RjCmWFOpmjvDG8WF0H_nmh3HxModtEFufa_uHkSOkUWgwGpaca05dhJFBwVChKXXF9jFwDwjdbONmRXIuhzGwBVR1kLER3mV__8JlDtEzlr6ihUHxh0EiTvGE6ZJGs3SAb1NMioUD_NHJU2SsxO_voXlCLzrdhNXWvV_8gJ7MzAPyWQYvGafeSWq7L5VxyvRxS59FwtlE5fTh3dtnJzTgZVB-CnanM0KcJAyCIK0KLppYB0gE-b9GWBCrRk7FKkS8M3q8z_8sJC76-FnFJjLFI15yHIMZULM2RCuokOGaaMR7ZIHIb4Dy4cDHyMCs7Wtp-9van65ipuBWkOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79de90eb9.mp4?token=eyTWZ6RjCmWFOpmjvDG8WF0H_nmh3HxModtEFufa_uHkSOkUWgwGpaca05dhJFBwVChKXXF9jFwDwjdbONmRXIuhzGwBVR1kLER3mV__8JlDtEzlr6ihUHxh0EiTvGE6ZJGs3SAb1NMioUD_NHJU2SsxO_voXlCLzrdhNXWvV_8gJ7MzAPyWQYvGafeSWq7L5VxyvRxS59FwtlE5fTh3dtnJzTgZVB-CnanM0KcJAyCIK0KLppYB0gE-b9GWBCrRk7FKkS8M3q8z_8sJC76-FnFJjLFI15yHIMZULM2RCuokOGaaMR7ZIHIb4Dy4cDHyMCs7Wtp-9van65ipuBWkOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی که یه خانم حامله ایرانی از میزان تکون خوردن بچه‌اش توی شکمش منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69617" target="_blank">📅 12:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69616">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLY3cmm8QUcXiJJxKtBwZytlx8YJuCckTXYHT27oWVqNG8vVMMnxr3xJmLjQuTHxjiE1nut4mL-DyNNGRjzBcqJna_hqwWslpo-XA1yDEzTTqWeuWDaZIA04bVIkv7Hsy1Cm2W4S1ZFy0-kbHHJxBKkmhNVzG-O3pfESaHTq9cUxBpvp_rn7iBs7kSr3_IH93PwaihwYaHyg-6I03c6p6iS5BkxhjmQzGoyWBxYI4vPUC_JKTvt0cKLw5iaYJOx2aizcAg92gmuYswDEsBXdNF1ALTfwSo9u5GfDsNe7w-2NvR3VPPUSEV1erkZxWOQDNcHuY27lfLcTNkQ3qak09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش واشنگتن پست
:
دونالد ترامپ، رئیس جمهور آمریکا، هفته گذشته در کمپ دیوید با پیت هگست، وزیر جنگ، درباره کمبود شدید مهمات در ایالات متحده به شدت صحبت کرد و از او خواست توضیح دهد که چرا به نظر می‌رسد او در مورد این کمبودهای شدید که اکنون تهدیدی برای محدود کردن گزینه‌های نظامی است، فریب خورده است.
ترامپ در جریان جلسه کابینه در کمپ دیوید به هگست گفت که فکر می‌کرد مشکل کمبود مهمات "حل شده است". هگست از خود دفاع کرد و استیفن فاینبرگ، معاون وزیر جنگ، را مقصر دانست و گفت که او اطمینان حاصل نکرده بود که ترامپ به طور کامل از میزان کمبودها مطلع باشد.
در همین گزارش، روزنامه واشنگتن پست به نقل از یک مقام آمریکایی، اعلام کرده است که بیش از ۱۳۰۰ موشک بالستیک تاکتیکی MGM-140 ATACMS ارتش ایالات متحده در جنگ با ایران مورد استفاده قرار گرفته و تقریباً هیچ‌کدام از این موشک‌ها باقی نمانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69616" target="_blank">📅 12:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69615">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d9f385e0.mp4?token=Aa3qYTeUOZXuZmBaOJCUM-Dpqq9zP5Jg7uH0OIerP4v6uY3IXcm4nnFFZvZkcZrBiDMHvfr-w-wJSP4Al37IfGt7sJKw9gow9u_bXzK9mxEPY-qXcPlju3CWb-A5hJbxtxQfWHYd411apNMq-2jCqZUnnOhkX6rgr3rmV6gSv1V9Hdx97oNueVmCOEMnca_8C0hWjtzNanJj_zNEouozywGMFOY_LTxm42rqh8guFfz7MfHvVaEP9TVIb-kRT16Tyo34hUask9EwyQ2KamIjnaIuKZYp03Cbyb0XBTOyoXTDRknRLs-lmTF-s1YYwF4suQuOoZNL2wDUcLKKkJucWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d9f385e0.mp4?token=Aa3qYTeUOZXuZmBaOJCUM-Dpqq9zP5Jg7uH0OIerP4v6uY3IXcm4nnFFZvZkcZrBiDMHvfr-w-wJSP4Al37IfGt7sJKw9gow9u_bXzK9mxEPY-qXcPlju3CWb-A5hJbxtxQfWHYd411apNMq-2jCqZUnnOhkX6rgr3rmV6gSv1V9Hdx97oNueVmCOEMnca_8C0hWjtzNanJj_zNEouozywGMFOY_LTxm42rqh8guFfz7MfHvVaEP9TVIb-kRT16Tyo34hUask9EwyQ2KamIjnaIuKZYp03Cbyb0XBTOyoXTDRknRLs-lmTF-s1YYwF4suQuOoZNL2wDUcLKKkJucWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این نقاشی هنرمندانه با ایجاد خطای دید، باعث می‌شه دیوار صاف خونه طوری به‌نظر برسه که انگار داره به سمت بیرون خم می‌شه و برآمدگی پیدا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69615" target="_blank">📅 11:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69614">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKe5zed_UI880AjGzGLMcuGPITtoFgKN9LUjbLJ9hirCW3Rg7VZ7Dqq2I-Ube9vCdefHzPqnYMXih6hkqX7gpzCi3VmNDtEkbD8IqgGJXbXaNNl5G3u_98UnWewljnGmfJki3UPmiTcfIwvL16hVSksuGYaHUAR5j60Aq4wrpbK9Sce_lYhcDDtRIfDYvu14Otl24ojUk0tKeDzqeyuTaQe89-1e8nbn-kAIqEYEIzriGEWXDx2wUK44UeW4LIPjp5pgT9glN9UHU418iPRtrwNaoI3-46_pd26H8bXtKzibSYuJ77-5jKcM9OEgvnIlqIra2N-hH7mZE1zfMhdp9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرکز عملیات تجارت دریایی بریتانیا (UKMTO)؛
پس از دریافت گزارشی از ناخدای یک نفتکش در حال عبور از تنگه هرمز، هشدار صادر کرد؛
این ناخدا گزارش داده بود که صدای دو انفجار را در فاصله تقریبی ۹ مایل دریایی در جنوب شرقی «کومزار» عمان شنیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69614" target="_blank">📅 11:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69613">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b71c6863.mp4?token=QDPcbquwV99nqFgj17kL5NRPKDphsVBMp8pWB0q13KuYgT_ARyPIXDe1Rs3pb0bM0lxYgKPZkYD0XXENVh1JuGaU5mTh9FKtCCclLdoyg1RGfBSm0tsr5momCXJnmbXUbzxAw0_v5PaG8S3LCqCWCZn1qW24w4CjBLjtWzGDOX5pr3SVi-v2zAqDz2Wptbc63qIZ-kNxA8A3FwWEbV4DO66XZwpJdUZTEcvULsuZvmC5i78I1kF9Fe2dch-Qkj3oTe8KGTbOXq1sXgkuktq5yFcHnL9VvuJDF_u2ldl2LwXUuOY6eaT6-mrO350t5fmu7LcGIVCtg0fz8_Et26ZyJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b71c6863.mp4?token=QDPcbquwV99nqFgj17kL5NRPKDphsVBMp8pWB0q13KuYgT_ARyPIXDe1Rs3pb0bM0lxYgKPZkYD0XXENVh1JuGaU5mTh9FKtCCclLdoyg1RGfBSm0tsr5momCXJnmbXUbzxAw0_v5PaG8S3LCqCWCZn1qW24w4CjBLjtWzGDOX5pr3SVi-v2zAqDz2Wptbc63qIZ-kNxA8A3FwWEbV4DO66XZwpJdUZTEcvULsuZvmC5i78I1kF9Fe2dch-Qkj3oTe8KGTbOXq1sXgkuktq5yFcHnL9VvuJDF_u2ldl2LwXUuOY6eaT6-mrO350t5fmu7LcGIVCtg0fz8_Et26ZyJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
حسن روحانی: اقلیتی می‌گوید اگر این جنگ تشدید شود، امام زمان زودتر ظهور می‌کند! می‌خواستند برای سخنرانی امام زمان در تهران جایگاه درست کنند.کاسبان تحریم ممکن است خوشحال باشند که جنگ ادامه پیدا کند.
عده‌ای دنبال کاسبی از جنگ هستند و از ادامه آن خوشحال می‌شوند.
در جامعه ما گاهی یک اقلیتی هستند که حرف‌های عجیب و غریب می‌زنند.
یک اقلیتی هستند می‌گویند اگر این جنگ تشدید شود و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم.
خب یک عده افرادی هستند که نه با اسلام آشنا هستند و نه با مهدویت آشنا هستند.
یک عده هم هستند که دنبال کاسبی هستند، همان کاسبان تحریم در واقع. آن‌ها هم ممکن است خوشحال باشند که جنگ و آشفتگی ادامه پیدا کند.
افرادی هم هستند که ممکن است یک تفکراتی داشته باشد که ما باید برویم جهان را بگیریم و تصرف کنیم و همه را به اصطلاح هدایت کنیم.
من در سال ۸۳ رفتم خدمت رهبری برای یک موضوعی، بحثی پیش آمد در آنجا، ایشان به مناسبت فرمودند که فلان آقا، اسم بردند، آمده بود پیش من و از من سؤال کرد که می‌خواهد یک جایگاه بزرگی درست کند در یک میدان بزرگ در تهران. گفتم جایگاه بزرگ برای چه؟ گفت برای اینکه وقتی امام زمان آمد و خواست سخنرانی کند یک جایگاه مناسب و باعظمتی باشد در شأن ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69613" target="_blank">📅 11:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69612">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcd7LJkhdzgd5wnWMpX0Gbst4mlNr3ZKeNgtLY9X1NpkkTjmI6AG5w-snit-H0LBxs9nXie9llgLaI8l7pDVKNwADGt-DjD5oDXr4-r7hSSlnheoIcry8wv9OeHCQm4auQ-ykci9F3jzTpmx9irlpd0L_qqUh8bXBnnVZYTaEMP4TTkxDi3sLutUE5x2vtp8kM6-1-kO7w7W0Y5QsAI9RsEFY6j5eEyYVCOkRfJ-Gpo994pmu6Q2W9C0IUNfw2d5yiyCcF_2tX5xfz_ZoJveiWl4MPnED_S4gRhoZ1iMHHJ8ln2RIxxhWNG2kpq7BbCcoAjs0dL_tl_4s8aFCbt5qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
اکانت رسمی تلگرام زیر توییت یه کاربر:
یه نفر پرسیده بود: می‌خوام بدونم دورف(مالک تلگرام) کجا قایم می‌شه؟
تلگرام هم جواب داده:
درباره خودش چیزی نمی‌دونم، ولی معمولاً منو خونه مامانت می‌تونی پیدا کنی
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69612" target="_blank">📅 11:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69609">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1558a77094.mp4?token=gnXEMLe0bYjtpbb8VBprb9k5ynWAMMH7EgdxdDOeeA-SE_7yePCFFPyf7z53NNKJnUiQSVao0XbLemBn3AAU6Rp1NDhLzFao7nhFiH66VriI7gWGehBXfQUYlMHbc2pqZY43dY-y_06vcf1sPtWqsRTlsHduHsg5NSoQ-xg9gQJcqwY7Hu86WTeUlggEpP6x0UREA40Cm8W_lDrSartCTJ67Dzb3892smpQ8EA1OJMyb92kn1yR2PKX3BFOjLTUh3RIuuKSBjZv4MJTxHD_SQkk4QnKexvOOlslzxUlm6MzlwG2OE5ELRlEOnhudect_7-rhlwl5rOTpuixUtJ4p5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1558a77094.mp4?token=gnXEMLe0bYjtpbb8VBprb9k5ynWAMMH7EgdxdDOeeA-SE_7yePCFFPyf7z53NNKJnUiQSVao0XbLemBn3AAU6Rp1NDhLzFao7nhFiH66VriI7gWGehBXfQUYlMHbc2pqZY43dY-y_06vcf1sPtWqsRTlsHduHsg5NSoQ-xg9gQJcqwY7Hu86WTeUlggEpP6x0UREA40Cm8W_lDrSartCTJ67Dzb3892smpQ8EA1OJMyb92kn1yR2PKX3BFOjLTUh3RIuuKSBjZv4MJTxHD_SQkk4QnKexvOOlslzxUlm6MzlwG2OE5ELRlEOnhudect_7-rhlwl5rOTpuixUtJ4p5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی که حامیان حکومت برای موشک‌ها درست کردن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69609" target="_blank">📅 10:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69608">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=k3t_SQPBRXmDJWk-H9W_0KreiShEABX-Hx3KnC7pJpqVbxFrXcUY1W42DM5Bk_0xW2AQ02Vk8P_A2jA_AYGxN0A0tK5kha44LuOLfN9HOJmkd43bNVs4L8VhB8jt-JMT2rvBQKd_384UULz7qxtl1hElOUxRJHpVVZCQh0QHJ-kkVHGLdKK3C2FO8wc7uB-cTQu-XR_GntVM2cCr-5V1FSuPxW8XV3YHeOMlzTmZD0daHcACARNUe4JmMh12VLeE48tm8QwiXQS1bSEmUxWjWcabNIJ1fUM9N85DuMEyu5NyS54adqR5YQxgXpl6vJ2_82tr6rgYb4NXd8YsAFzJqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=k3t_SQPBRXmDJWk-H9W_0KreiShEABX-Hx3KnC7pJpqVbxFrXcUY1W42DM5Bk_0xW2AQ02Vk8P_A2jA_AYGxN0A0tK5kha44LuOLfN9HOJmkd43bNVs4L8VhB8jt-JMT2rvBQKd_384UULz7qxtl1hElOUxRJHpVVZCQh0QHJ-kkVHGLdKK3C2FO8wc7uB-cTQu-XR_GntVM2cCr-5V1FSuPxW8XV3YHeOMlzTmZD0daHcACARNUe4JmMh12VLeE48tm8QwiXQS1bSEmUxWjWcabNIJ1fUM9N85DuMEyu5NyS54adqR5YQxgXpl6vJ2_82tr6rgYb4NXd8YsAFzJqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
پزشکیان:
حوادث دی‌ماه پارسال قابل فراموشی نیست؛
یه عده بیگناه هم قاطی اون اون افراد تو خیابون ها شده بودن
وقتی روند به شورش رسید اتفاقات سختی رخ میده و ما دیدیم شرایط اینطوریه گفتیم کد ملی اعلام کنن و هرکس اضافه تر میگه هست خب بگه
کسانی که کشته‌شدگان رو ۳۰-۴۰ هزار نفر اعلام می‌کنن، نامرد و وطن‌فروش هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69608" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69606">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8bd143a1.mp4?token=gmBNIZGlBzHHgSIVomOhuy1QHhnsRxuMlVSEF7rjU71EwS4XaYZmlU-QtkNpEzDjmY6HXzpu2J2x1of2Z3zCBQJsy-4O9boFa9QjYf7aFbxYkuYYb5FOJukKQMc8snvzFXgzo6wSSjCbgN67_PwM0RFNULtHBGdwwtSPwhwWVnLcEHpmecCSbh09de7yerkSzxLezYT5sVWAe1oF08HW_9syh6g_t_XEWTCdErBnmmRcNHsixuw283QGKxrYmrdY1esrRiNV9BSLOLdzIdb1KQzNKTcsa5H_4Si3NwRUoIb4ZISs_rrL5YnnvVOTjrE4CXTGi5dSZg6OAWV3QLQiWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8bd143a1.mp4?token=gmBNIZGlBzHHgSIVomOhuy1QHhnsRxuMlVSEF7rjU71EwS4XaYZmlU-QtkNpEzDjmY6HXzpu2J2x1of2Z3zCBQJsy-4O9boFa9QjYf7aFbxYkuYYb5FOJukKQMc8snvzFXgzo6wSSjCbgN67_PwM0RFNULtHBGdwwtSPwhwWVnLcEHpmecCSbh09de7yerkSzxLezYT5sVWAe1oF08HW_9syh6g_t_XEWTCdErBnmmRcNHsixuw283QGKxrYmrdY1esrRiNV9BSLOLdzIdb1KQzNKTcsa5H_4Si3NwRUoIb4ZISs_rrL5YnnvVOTjrE4CXTGi5dSZg6OAWV3QLQiWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
باقر خرازی (برادرزن مسعود خامنه‌ای):
ما باید از جمهوری اسلامی گذر کنیم. علت اینکه این الدنگ (پزشکیان) رئیس‌جمهور کشور شده و بی‌حجابی کشور را گرفته این است که هنوز از جمهوری اسلامی به حکومت اسلامی گذر نکرده‌ایم.
خدا لعنت کند شورای نگهبان را که این "آشغال" را توی پاچه ملت کرد.
چهل سال است با آقامجتبی رفیقم؛ او بسیار تندتر از پدرش است؛ اما یار ندارد.
باید به نیت حضرت فاطمه از هر شهر ۵۳۰ نفر جمع کنیم و به تهران سرازیر شویم و کار دولت پزشکیان را تمام کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69606" target="_blank">📅 09:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e59bbff0.mp4?token=GjlLbh6F_7ZrN2GTXP4UIp-HwTITor7KC9GgvbuC1fOxOqi0HsqeCxq16wtxiXMlEY5JfE-gd7HZiGiJ0I5XA5CZDXobDfLwNeyiZE31vY-hoeXE6kdiKP_OHtWoXz2pDc3pI-DOn-QnJvGGwxtkeb6aW_SSNh2511_zIe4u1GjgKXIIK-eQOPGN1wIHZkLnjcZ6yMVkRZtIIStptXF3oeHuacpcSzm-BgVgr0vbtfcbRhqoD_Y3kqc7DafHQkLHkH-vcCgx8UnvaRxITCRGguHZ3hh0sUix6aSidro4bgkapm0duVC81oSWQmXYtywZZtV9Gbl_MKOW-jFpy-ZR_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e59bbff0.mp4?token=GjlLbh6F_7ZrN2GTXP4UIp-HwTITor7KC9GgvbuC1fOxOqi0HsqeCxq16wtxiXMlEY5JfE-gd7HZiGiJ0I5XA5CZDXobDfLwNeyiZE31vY-hoeXE6kdiKP_OHtWoXz2pDc3pI-DOn-QnJvGGwxtkeb6aW_SSNh2511_zIe4u1GjgKXIIK-eQOPGN1wIHZkLnjcZ6yMVkRZtIIStptXF3oeHuacpcSzm-BgVgr0vbtfcbRhqoD_Y3kqc7DafHQkLHkH-vcCgx8UnvaRxITCRGguHZ3hh0sUix6aSidro4bgkapm0duVC81oSWQmXYtywZZtV9Gbl_MKOW-jFpy-ZR_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ممکن است دوباره قیمت نفت را «بالا ببریم»:
«قیمت ۷۵ دلار است. ممکن است مجبور شویم دوباره آن را بالا ببریم. خودتان می‌دانید وقتی آن را بالا می‌بریم چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69605" target="_blank">📅 02:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69602">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ecaba828.mp4?token=S4D1UpcFiBh836VoG29W8sB8AAn3yyk_IJY72P_MLlKnq0_LkftkNhxN1guxOqa4q0lK-nw_7FBQf2Nwf-n8L0nvKWvKf2Jy2l1KbVRQ5MLtZxYtWn30pUKOJJnzFTTn13eC8yDX4Mso9ANkQPFgSu63pIw0H_uosIjq-19vLXM351XyPZDyKde042GyuVHFgyKszvFII1brMEcLcmCriED01-psMPtGPLD3xWj_3SDkvwFo0PpMUxSD2DZRd2gYzRmYmhCDH0twuCIlCQleK9WRzeE7iJrB5DcXppxOB33PJAphkunG91YBZujx9IsHr2OzJlOoygFaFBhU-HcdLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ecaba828.mp4?token=S4D1UpcFiBh836VoG29W8sB8AAn3yyk_IJY72P_MLlKnq0_LkftkNhxN1guxOqa4q0lK-nw_7FBQf2Nwf-n8L0nvKWvKf2Jy2l1KbVRQ5MLtZxYtWn30pUKOJJnzFTTn13eC8yDX4Mso9ANkQPFgSu63pIw0H_uosIjq-19vLXM351XyPZDyKde042GyuVHFgyKszvFII1brMEcLcmCriED01-psMPtGPLD3xWj_3SDkvwFo0PpMUxSD2DZRd2gYzRmYmhCDH0twuCIlCQleK9WRzeE7iJrB5DcXppxOB33PJAphkunG91YBZujx9IsHr2OzJlOoygFaFBhU-HcdLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ترجیح می‌دهم با ایران توافق کنم، چون نمی‌خواهم آدم بکشم.
ایران به ما احترام می‌گذارد. آن‌ها به ما احترام می‌گذارند.
ما در حال گفتگو هستیم. ببینیم چه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69602" target="_blank">📅 01:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69601">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4b2dd818.mp4?token=fSS-MEZnlJBh7olT5VouV-qK6bA0K2zyiIAsK0ZES-MPl9_d3ZVfMFeSG5OWk5-VXQptnzZzIKEbjmlR5Joa416Np2XjtPm1TCaTb8OPzvhcw8wkl3YiADTvGA6hKAiadHfO536r28Sc037_DsnOHzUQQDcQlVog-3XBGtOPG1E2w6trIIzl4sM9qiv17PFhAeooQfaYt39uMQvjCVHiiVYbSKlIB8I3_rHifM9XUTQ32dkSmAi26vRQ61YUP4W8s-2fd-J6cmnlP8Qf7jSEOQnrxesR6OdHuY0WRBS6ef4e-w1b-tt0_WOWHfJg43CY1Yh1C3FzHn7k0YwtrVRmug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4b2dd818.mp4?token=fSS-MEZnlJBh7olT5VouV-qK6bA0K2zyiIAsK0ZES-MPl9_d3ZVfMFeSG5OWk5-VXQptnzZzIKEbjmlR5Joa416Np2XjtPm1TCaTb8OPzvhcw8wkl3YiADTvGA6hKAiadHfO536r28Sc037_DsnOHzUQQDcQlVog-3XBGtOPG1E2w6trIIzl4sM9qiv17PFhAeooQfaYt39uMQvjCVHiiVYbSKlIB8I3_rHifM9XUTQ32dkSmAi26vRQ61YUP4W8s-2fd-J6cmnlP8Qf7jSEOQnrxesR6OdHuY0WRBS6ef4e-w1b-tt0_WOWHfJg43CY1Yh1C3FzHn7k0YwtrVRmug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
هیچ‌کس نمیدونه که کلمه «dumb» حرف «B» نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69601" target="_blank">📅 01:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69600">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇷🇺
🚀
ویدئو منتشرشده از شلیک گسترده موشک‌های اسکندر به کی‌یف و حومه آن در روز گذشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69600" target="_blank">📅 00:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69599">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTW_7_u2seAutjbvIsDzlflVD43gfUyv_U2HRojtpgmztzfgb_K5BAq4fJRv39GU_RzkNrUmMbTI3BvK3yMJsKZYtZkisxSuEB9FgcH3SmmDwG02yRSORNB5UANcTHOvYz3VK-Uh1wyst6sUO7biou40jxx9n46Wmjtp9AN0wxKZz9_mg216MfYBR_5ExnzMNN4inbHYkFF2uuLF_fTkwP83_USI_XJUdEe_NTuGYyCZ_w1V2PMcMdqHYOa9_vVoMgolgVK4eYJzV51n9uAcwT1SYy4z6WPeUTvAxLJwFO_z2fOFNyJq2BL0EdSGcx4zTs9WOUVPCYQO7TtgF4d2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مود:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69599" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69598">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82acfe6016.mp4?token=Ne2ouX8yLtUKNSfWzh2MqFpeBE6YXSFjca4OtPFnhaVvZu2bBa6qVjc--LBwO_AMHCTp16XJadzJukMDd7CI9uxrEuM3Pr2v1CHEEYT-sKRzQTzlu4u0XldKsIAHcIDwRdxxxwrS1czrvPcSjjiTf1RlSi8up5Zhbiz72p_M8tqhZs7Q0S0L9QiKkoSlfP2JYcQrLzqfPjg2zFK_A4SSEfOWJ577YWjPJQBV3bG8bLnA8WUbplomIYTnlQ7_RmzFkRvsGZ2y0FcOItezm_FkYkwpqq7ouxqU04q8o2mXLYtRlYdRVn_NvL0KdvJ_W4aWu5w5pgRO9fH3-R2jrXMqYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82acfe6016.mp4?token=Ne2ouX8yLtUKNSfWzh2MqFpeBE6YXSFjca4OtPFnhaVvZu2bBa6qVjc--LBwO_AMHCTp16XJadzJukMDd7CI9uxrEuM3Pr2v1CHEEYT-sKRzQTzlu4u0XldKsIAHcIDwRdxxxwrS1czrvPcSjjiTf1RlSi8up5Zhbiz72p_M8tqhZs7Q0S0L9QiKkoSlfP2JYcQrLzqfPjg2zFK_A4SSEfOWJ577YWjPJQBV3bG8bLnA8WUbplomIYTnlQ7_RmzFkRvsGZ2y0FcOItezm_FkYkwpqq7ouxqU04q8o2mXLYtRlYdRVn_NvL0KdvJ_W4aWu5w5pgRO9fH3-R2jrXMqYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فیلم وایرال شده از یه کارگاه آموزش فن بیان توی تهران.
چه خبرا؟ به لطف شما:))
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69598" target="_blank">📅 23:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69597">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c05821a8.mp4?token=FWnLeeEsrCh-whUMm0edgA67_ILkxIXqa2PtusDdWYzUr4TyrXX0fSgAIf8xBVh6N6wDwLJVb1XzOE4Z6-cZuDMpSFyx6fzghQ4kR3Cu3BtI6Q1douGzhHTchJIzjwce1Fv3ZeXdb_I2bjNJ9aUxOgtZXkjQ79HDd39VEHp7jzc_tTmWir08rJQ1bzlPRT2E1Yl-m1ZOTwwrX4aF0ZJnSO3nUFcK_X9OqfMX5mFmp-N73HJAhGndCHapsXDJwMhGRcMeraXkaw6W_jCv7wJfj_Ff2ZaRxK1JjvzNpETotT8IJHrxjuu_x-5Vk6rU8Tq_N2WFJqS-0UQ45kpAF40IRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c05821a8.mp4?token=FWnLeeEsrCh-whUMm0edgA67_ILkxIXqa2PtusDdWYzUr4TyrXX0fSgAIf8xBVh6N6wDwLJVb1XzOE4Z6-cZuDMpSFyx6fzghQ4kR3Cu3BtI6Q1douGzhHTchJIzjwce1Fv3ZeXdb_I2bjNJ9aUxOgtZXkjQ79HDd39VEHp7jzc_tTmWir08rJQ1bzlPRT2E1Yl-m1ZOTwwrX4aF0ZJnSO3nUFcK_X9OqfMX5mFmp-N73HJAhGndCHapsXDJwMhGRcMeraXkaw6W_jCv7wJfj_Ff2ZaRxK1JjvzNpETotT8IJHrxjuu_x-5Vk6rU8Tq_N2WFJqS-0UQ45kpAF40IRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
دیروز یه خبرنگار از بقایی، سخنگوی وزارت خارجه پرسید چرا جواب صحبتای ترامپ رو نمیدید؟
بقایی گفت چون باید رفتار ایرانی داشته باشیم و حرکات زشت دیگران رو الگوبرداری نکنیم. آخرشم یه تیکه از یکی از حکایت‌های عبید زاکانی رو گفت : "فعل و عمل ما را و دعوی ایشان را"
🔴
حکایت کامل عبید زاکانی:
شخصی اَمردی به خانه برد و درهمی به دستش نهاد و گفت: بخواب تا بر نهم. اَمرد گفت: من شنیده‌ام که تو اَمردان را می‌آوری تا بر تو نهند. گفت: آری، عمل با من است و دعوی با ایشان. تو نیز بخواب و برو آنچه می‌خواهی بگوی.
🔴
حالا معنی حکایت:
یه مرَده یه جوون بی‌ریش رو پیدا کرد، یه سکه بهش داد و گفت دراز بکش تا باهات همبستر بشم [ کونت بذارم ].
جوون گفت: من شنیده بودم تو جوون‌ها رو به خونه میاری تا اونا باهات همبستر بشن [ اونا کونت بذارن ] نه تو.
مرد جواب داد: «درسته؛ عمل کردن از طرف منه، اما حرف و ادعا با دیگران. تو هم فعلا دراز بکش، بعدش هرچی خواستی برو درباره من بگو
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69597" target="_blank">📅 23:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69596">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
ترامپ بهترین دوست ماست، اما می‌خواهم یک موضوع رو روشن کنم: "موجودیت اسرائیل قابل مذاکره نیست.با توافق و مذاکره یا بدون آن، هر کاری لازم باشد برای تضمین آینده‌مان انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69596" target="_blank">📅 23:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69595">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Esgard-VPN.apk</div>
  <div class="tg-doc-extra">42.4 MB</div>
</div>
<a href="https://t.me/news_hut/69595" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پیشنهاد_ویژه
فیلترشکن محبوب اسگارد ‌وی‌پی‌ان
تقریبا با همه‌ی اینترنت‌ها کیفیت اتصال و سرعت خوبی داره. حتما امتحانش کنید
لینک گوگل پلی:
https://play.google.com/store/apps/details?id=com.vpn.esgard&referrer=628035</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69595" target="_blank">📅 23:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69592">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ezILjjJjI7Z4JtoENyHlV93j__KN9atCm9ulJIYPtY1pZ6iR7jtJISPJEZLiGYm_8R8qW3r-o1xDX9E21TXZHkp1260QW-Eoe53VqgnCd3D4zh9sqKoOL93jjv4Sz76kzqQS9ttO8cZD6g5bQmfm1txk_h7sJtfQCsU0Bjh3ybhOXjLQSIPBEu1ziYj1E8N6XNSwfuJZEJ1JFS6QIj9CBBL9Ggoa99jwd-HoFV6l1dgvrZWs_wuND-DGpsPVBqC2xEB4J8WdGAYjXrS1sA-f1gFY3Tc_plA8iaNSdUP4TLJY-Uebt8e-NP1cBE5SfFnHoWPbLZqmKP2w19_6p4Sv0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Weya6hgJct7AaewSPe_1XdfXAvpxOB8Y8fCSs6jFvu17aZ-AuXlvtSKpPJMiZwDnZX0EpfEGWpewKP-z8tKureIM_2TpiBnBVjadtqn7b8ICdvo3dI2dMzH1GxQ8743kkpTWyhOXRbxH65x-b6eDeMtaHMyr5H-ClrzZ21HKJk1foo4fzudMb9YjDM66XlEKgyD9r6MNMJvGchccn7z0xKVyXO5-KTzCQnY6e-edCxkBlcXVbjzoHIBQDV-HvrZ06cQwEmueGQ6GTReQsBZybWmVJDHEiQKYjCbixgcgTKjyEzOctVMevTI36F91Z7maTDEEpykhYPhIQPdHZ3itbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6780226a9d.mp4?token=FlcTAY_cRWajPS_FfYZPLLHm02E3v2aXylobG1vOr4cit__75uc3p94cFcrcOGgKZfNNQO-Ra0HQbcwHl-2UOBI5fDemmkQg-4PzArl931N_obYTKEzb5jsN4VUv7IlVEOX-UXjUNDb1kE7mrI2jgcFnA52tODEeW2wCOvHPiI3s5JDiZBdHmt6IyxBy6x0YtHwf1LI8PztFN3DYupC9kKG_MViC5ONJIbtspYcm3fM1QKu9KAovQG0mQOamx7zLAWxFw69Es-cl249P8rtD8AXMDFmulPOmm9FJ1lnHnBvbc9y6s-Y7hnqtRHsrim4-njwK_VK4u0YAcg5kAQw_tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6780226a9d.mp4?token=FlcTAY_cRWajPS_FfYZPLLHm02E3v2aXylobG1vOr4cit__75uc3p94cFcrcOGgKZfNNQO-Ra0HQbcwHl-2UOBI5fDemmkQg-4PzArl931N_obYTKEzb5jsN4VUv7IlVEOX-UXjUNDb1kE7mrI2jgcFnA52tODEeW2wCOvHPiI3s5JDiZBdHmt6IyxBy6x0YtHwf1LI8PztFN3DYupC9kKG_MViC5ONJIbtspYcm3fM1QKu9KAovQG0mQOamx7zLAWxFw69Es-cl249P8rtD8AXMDFmulPOmm9FJ1lnHnBvbc9y6s-Y7hnqtRHsrim4-njwK_VK4u0YAcg5kAQw_tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو لیگ دسته سوم تایلند، بارون میباریده، ولی همینطور فوتبال بازی می‌کنن
یهو یه صاعقه میزنه و صاف میخوره به یه بازیکن و اون بازیکن فوت می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69592" target="_blank">📅 22:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69591">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiZ4FFAdjp1fMtApvkIFazQ1tP4yeZn90d4efwVskL3fhzyXXK2bum0OMYBs09hulSxTzlE9dvoJL1bIsuk-2FtvuTfG3h2TAxI468J4PrGDvNTURiJiLxJPrXLsm1Z-Fw_0py2lMb74KIQDrt4ijcvJSKHIOm_fgU_hWjVeOXhmvKe8466P-cOkSfNCne7cpVFzRh-PniM1u7vq_vcjZ2e43JgBjoOQa7wR9v8ijp7APoHWItxJtrnZN0r_zb51IDEMMFqxS5_o3A8qnJhhGewMsjeuGsYtRh1hOM07SevUutok2HAUCNDUVdif2zR4bGGMWmCyShIeP6jV2Xltkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
🇮🇶
وزارت خزانه‌داری ایالات متحده تحریم‌های اعمال شده بر شرکت هواپیمایی فلای بغداد و چندین فروند از هواپیماهای آن را که در سال ۲۰۲۴ به دلیل ارتباط ادعایی با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بودند، لغو کرد.
این لغو تحریم‌ها، شرکت هواپیمایی فلای بغداد (که با نام عراق اکسپرس نیز فهرست شده است) و دو هواپیمای بوئینگ ۷۳۷ (YI-BAF و YI-BAN) را از فهرست ویژه اتباع تعیین‌شده توسط OFAC حذف می‌کند و به تحریم‌های مرتبط با تروریسم آنها پایان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69591" target="_blank">📅 21:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69590">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaHZbLBR3aFYAAoWdixLDa4CidOrfGCFpkLriY2I1IXZEjRDCYuOq_qtdQqQf7EUhcJ1uUvllcXXgEazkXFHqVROPIx1UqjsMB2ZkMd_KZpw5pa6pgVM_s8d7UUa3adY-pYtkPKPgLoFP72Fbf-JmmM_lsJPsccgs4STxOvIgOZw3E5qapNRPGwdX1GMXUkHxT0CwmAkvuYYzxF7YljbZHPcZCXBcn-45IURLLk-8no89he-Ne2lPqqeMOQvGQE6DyjQW6v_CzgW1fCnW3AzUlfWtXfMCA7qlXZFKV7PqhpfODIhmqwtcDkGYA-d_F9ydnVxcu8N5Pyt5aI1ZjXgew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی:
ایالات متحده تقریباً ۴ یا ۵ روز پس از آغاز دور جدید درگیری‌ها، پیامی مبنی بر درخواست مذاکره و حل‌وفصل مسائل ارسال کرد.
هرگونه توافق در خصوص تنگه هرمز باید صرفاً میان ایران و عمان باشد.
ما هیچ‌گونه دخالت خارجی در تنگه هرمز را نخواهیم پذیرفت.
با اجرایی شدن توافق جدید، مسیرهای موقت فعلی در تنگه هرمز بسته خواهند شد.
بخش قابل‌توجهی از مسیرهای تردد کشتی‌های ورودی و خروجی به آب‌های سرزمینی ایران از این مسیر عبور خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69590" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69589">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=IEoaFhuoTL4glVWLHInCzwF4hBFwYA4p_cWXT8S9pdcD2TWXzKAXzuxGGmgIQcEz1kTp9OGzoV5vrJ0fOAtQBSsOGNShrDPzUcIHkbJhTGbimmsznKLSlBCXc7D1GK-LsU-_dEjYub3deLMnQV-KfWVytGQTxDbYtcqPZT7l8tcqsifAagsaos2fRdxI4gkeXCokc5CgQd3K7tHb5u6m09nxew6xY-3k1DjrWtg3FF0imi40bjWM0aXw2oNpMfMJiPPOybe2owHD0_qeSU-gSWb9_FGyxOIVVad6sKv7twnkZcP4Xy_NxDKO7P_Kg7GarZXGrC8o7vOd991mev9f0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=IEoaFhuoTL4glVWLHInCzwF4hBFwYA4p_cWXT8S9pdcD2TWXzKAXzuxGGmgIQcEz1kTp9OGzoV5vrJ0fOAtQBSsOGNShrDPzUcIHkbJhTGbimmsznKLSlBCXc7D1GK-LsU-_dEjYub3deLMnQV-KfWVytGQTxDbYtcqPZT7l8tcqsifAagsaos2fRdxI4gkeXCokc5CgQd3K7tHb5u6m09nxew6xY-3k1DjrWtg3FF0imi40bjWM0aXw2oNpMfMJiPPOybe2owHD0_qeSU-gSWb9_FGyxOIVVad6sKv7twnkZcP4Xy_NxDKO7P_Kg7GarZXGrC8o7vOd991mev9f0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
❌
🇮🇱
امروز در پی وقوع انفجار در ساختمانی تله‌گذاری‌شده در «مجدل زون» واقع در جنوب لبنان، دو سرباز اسرائیلی کشته و هفت تن دیگر زخمی شدند.
حالا قراراست بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و یسرائیل کاتس، وزیر دفاع، ساعت ۲۱:۰۰ به وقت محلی نشستی امنیتی برگزار کنند. محور این جلسه، حادثه مرگبار امروز در جنوب لبنان است که منجر به تلفات متعدد در میان نیروهای اسرائیلی شده است.
به گزارش شبکه ۱۴، انتظار می‌رود مقامات سیاسی در این نشست درباره انجام یک واکنش نظامی قابل‌توجه گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69589" target="_blank">📅 20:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69588">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTSEKvZw2bMfofZzMFnFTc55uFJFvKNjIUIgAUz5gnpXLABo2zhZSaFoOaBucrw6ClBKDz_LMX4gJe4DtLBl-tSH2_HlRPv8LHyhfXRCktqkH3-L1dG1DNy1vmNjmS1Qj3wMIvUKXzU1jDU3Hg5pbLR-wbbjAQyz8eqSviSdSFP1frSUW4L-g6rvPxH-qbRb1XnHisf9-SAT_HnFaZ4TZqlw_z53qQ3K0mc5F1a8_0xfOYml3CqqgkZ5pFuABQg0YGIqCGeYRHa7PzX56FSWhkb9E08EFkJnC3UrCjUfAwp8CLh4sSnVESojLSo0aaAUIVPLlT4JuqN1xbGHtwkotBuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTSEKvZw2bMfofZzMFnFTc55uFJFvKNjIUIgAUz5gnpXLABo2zhZSaFoOaBucrw6ClBKDz_LMX4gJe4DtLBl-tSH2_HlRPv8LHyhfXRCktqkH3-L1dG1DNy1vmNjmS1Qj3wMIvUKXzU1jDU3Hg5pbLR-wbbjAQyz8eqSviSdSFP1frSUW4L-g6rvPxH-qbRb1XnHisf9-SAT_HnFaZ4TZqlw_z53qQ3K0mc5F1a8_0xfOYml3CqqgkZ5pFuABQg0YGIqCGeYRHa7PzX56FSWhkb9E08EFkJnC3UrCjUfAwp8CLh4sSnVESojLSo0aaAUIVPLlT4JuqN1xbGHtwkotBuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله ایران تا آمریکا با موشک فقط چند دقیقه‌ست، اما پیاده باید نزدیک ۱۹٬۳۰۰ کیلومتر راه بری!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69588" target="_blank">📅 20:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69587">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=eVqGj8AHB3Bmzv_ieTbaSB_5-OXsIE0eXRk_zjii2hgqFKvpjwHUK-RCkkkhopxwQrZE1igOfpX4AHBH7WQSobBVIT-jv1sxmJhz_vdhVM6DLJgwz6wMN_ZsYzIaxp_JFCR-fCMTPfL1El9yXWIi1lM2E0Y5obz3LGZOhgbZydYfbVF1uYdukBPvW8EkS9jpl6vf1PCPDdlBagBqporfz-zKicqsDPDtoFMM-JYcLAlYMSBdBoymSoi_3qefr5Jh1M3VO04p3e3DrOJSlK1h0Q0TQ4EC7bSDYREpZLwxJRofbziWnj-ageby9VC4VIjfDE_AU87HgErBt-eN02el0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=eVqGj8AHB3Bmzv_ieTbaSB_5-OXsIE0eXRk_zjii2hgqFKvpjwHUK-RCkkkhopxwQrZE1igOfpX4AHBH7WQSobBVIT-jv1sxmJhz_vdhVM6DLJgwz6wMN_ZsYzIaxp_JFCR-fCMTPfL1El9yXWIi1lM2E0Y5obz3LGZOhgbZydYfbVF1uYdukBPvW8EkS9jpl6vf1PCPDdlBagBqporfz-zKicqsDPDtoFMM-JYcLAlYMSBdBoymSoi_3qefr5Jh1M3VO04p3e3DrOJSlK1h0Q0TQ4EC7bSDYREpZLwxJRofbziWnj-ageby9VC4VIjfDE_AU87HgErBt-eN02el0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
ترامپ بزرگ ترین دوست ما هستش اما به صراحت میگم وجود اسرائیل قابل مذاکره نیست.
با توافق یا بی توافق هرکاری که برا آینده مون نیاز باشه رو انجام میدیم.
نیاز های الزامی سیاسی مجبورم میکنه این مراسم رو ترک بکنم.
در حال حاضر توی یه رویداد بسیار مهم نظامی سیاسی هستیم.
این جنگ موجودیتی هستش.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69587" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69583">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=b84r6RRLlPi2x6WgfITwKmu5EjCX7YiCQwpcVcJRJnI97G-BFipdFKoDcvDO2U0fMMDC_t3tLdsNmNR1Pc79L1w5yzUnpt7bcKRdEQwPn48hpkU1VkVgtEuEEBgoyvlcKAVV1uCZmyqeCzmYB8uD_2XsGqVMsaBAEokBZhH6VnIJolxKhMsjlqBGcais0uYJxJDGfpFeXzm5FbZIWSK9HNyQt7QTNW29P9xGluZpcVIcEzYYV0i5Hxl6lunKe79qnwYWooHjxUntDj1Y79wawC5njAgGj1Gu31qE1RociLP8F9vHRZdHrcYdj2JYJMC0xFeegkR-bszjtqdeHzWJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=b84r6RRLlPi2x6WgfITwKmu5EjCX7YiCQwpcVcJRJnI97G-BFipdFKoDcvDO2U0fMMDC_t3tLdsNmNR1Pc79L1w5yzUnpt7bcKRdEQwPn48hpkU1VkVgtEuEEBgoyvlcKAVV1uCZmyqeCzmYB8uD_2XsGqVMsaBAEokBZhH6VnIJolxKhMsjlqBGcais0uYJxJDGfpFeXzm5FbZIWSK9HNyQt7QTNW29P9xGluZpcVIcEzYYV0i5Hxl6lunKe79qnwYWooHjxUntDj1Y79wawC5njAgGj1Gu31qE1RociLP8F9vHRZdHrcYdj2JYJMC0xFeegkR-bszjtqdeHzWJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پلیسِ رشت یه ون آورده وسط خیابون و شروع کرده داره به دخترها اخطار میده؛
بعد واسه مشروعیت دادن، یه مصاحبه از این خانم رشتی رو منتشر کرده که‌ با میگه:
گشت ارشاد رو دیدم احساس امنیت کردم.
امیدوارم این کار ادامه‌دار باشه چون اصلا از وضعیت سطح شهر راضی نیستیم.
چهره شهر اصلا عوض و زشت شده.
الان همه فکر میکنن رشت این شکلیه ولی خوب‌هاش رو نمی‌بینن.
گشت‌ارشاد دغدغه اکثر مادرهاست نه فقط چادری‌ها!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69583" target="_blank">📅 19:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69582">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
منابع عربی از حمله موشکی سپاه به بحرین خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69582" target="_blank">📅 19:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69581">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d659457195.mp4?token=dC18H58lol5YriyieyYlJefsJ4i7lolQuc6Se0dejGC_pzzeei2yUha_XzTvJxUh8jmhIpxZSIO_kRQrc2CtadwiTBaIvPuDsQm70x6WbfQi_xKQHp9yR7swMqpCVo2YzGhYbm4db6SLqn-My9tulWplJur-bkbutj31EQaVP23kLyLSK_kJm6oT7C0RON1ECI0jLrufnzmjPZlld6lqzZ1S_xSPT3h3ZgABUqYgTTUM-uulL7OrXK64WybP17fgZ1gbzD0pVe94IZQgtvcTSleGAC0_PRuQE_XoO2dhVRfiYjEjGgfPIBxbNQSgV78VUHTKuR5uyLfqeRDX2jEUFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d659457195.mp4?token=dC18H58lol5YriyieyYlJefsJ4i7lolQuc6Se0dejGC_pzzeei2yUha_XzTvJxUh8jmhIpxZSIO_kRQrc2CtadwiTBaIvPuDsQm70x6WbfQi_xKQHp9yR7swMqpCVo2YzGhYbm4db6SLqn-My9tulWplJur-bkbutj31EQaVP23kLyLSK_kJm6oT7C0RON1ECI0jLrufnzmjPZlld6lqzZ1S_xSPT3h3ZgABUqYgTTUM-uulL7OrXK64WybP17fgZ1gbzD0pVe94IZQgtvcTSleGAC0_PRuQE_XoO2dhVRfiYjEjGgfPIBxbNQSgV78VUHTKuR5uyLfqeRDX2jEUFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصاحبه تاریخی فیلدمارشال رضایی و خنده مجری:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69581" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69580">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtCJCfDovWZAMJKKYuzclUeY0PjogTfCaRx8D-r5lDwaN9LxzkfyAusCCzraQJBOM2NcbgC8S_D79DcA1Zoc621Nt_WfICIVJWi9UBCo4hBc292pOL1LuLCZkkqVfePS7fXsokfSgXoXlRth8vXI8MUHbGKO_3JRXnGVsKtrTZUsxx10LDBhkqmK9mPFQWeQWdzUvCyBnxiiZfn5YBM41ve13R37AdA8UgeBcHLzM8K2E4gehtTmrtFTy919VlftERZhnpTajbSy88UkwLKJNuRL68wX6ZxXps8CwWHD-7OurP9x_M2uSHFCyKeJCYJmQhrjCHSfU4167T88sT52MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پهپاد مافوق‌صوت Quarterhorse آمریکا به مرحله آزمایش نظامی نزدیک می‌شود
واحد نوآوری دفاعی آمریکا (DIU) برنامه توسعه پهپاد Quarterhorse شرکت Hermeus را برای ورود به کاربردهای نظامی دنبال می‌کند. این هواگرد بدون سرنشین با هدف آزمایش فناوری‌های پرواز مافوق‌صوت، سرعت بالا و قابلیت استفاده مجدد طراحی شده است.
مشخصات اولیه Quarterhorse:
⬇️
نوع: پهپاد آزمایشی مافوق‌صوت
⬇️
سازنده: Hermeus
⬇️
طول: حدود ۱۲ متر
⬇️
پیشرانه: موتور جت توربینی با فناوری توسعه‌یافته برای سرعت‌های بالا
⬇️
سرعت نهایی Quarterhorse: تا محدوده مافوق‌صوت بالا (هدف نهایی برنامه Hermeus رسیدن به سرعت‌های نزدیک ۵ماخ است)
⬇️
قابلیت‌ها: پرواز خودکار، استفاده مجدد، آزمایش فناوری‌های پرسرعت
⬇️
کاربردهای احتمالی: شناسایی دوربرد، آزمایش سامانه‌های آینده و مأموریت‌های نفوذ در محیط‌های دارای پدافند پیشرفته
پهپاد Quarterhorse هنوز یک پهپاد رزمی عملیاتی نیست، اما آمریکا آن را به‌عنوان یک سکوی آزمایشی برای توسعه نسل آینده هواگردهای بدون سرنشین سریع و کم‌هزینه دنبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69580" target="_blank">📅 18:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69579">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=cu22CuZiq2KQhthtKTK32bbDpdV8lNzPOxxpTUzgPQcElQFi8JgfeO2v07yeKb31UKEyKMt0-P9DperkTvYRxGcLsf9DerQqaMFQ44AtPBXuNyCvIPeRfHISjQyXWQuXfkxXMJFuNlROxbv-bASdPSfIi6QLBzFdVghz7U0uyrKtGTyEt5na5mo8q1tYVYfvSOqem8HJWXkRomgm0EG8GVYbpAhqB9zW7IGGK_M9VOJyePp2aJ7YUfIaI9qk0d5eONeKZrR5J4ClCP7nTWdOuOS5L0o1J7DyXeriXEXRkMvoxgSvw3ibopGG5Xbt2LyXSX1DdJQeGmXTiM9x83iWDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=cu22CuZiq2KQhthtKTK32bbDpdV8lNzPOxxpTUzgPQcElQFi8JgfeO2v07yeKb31UKEyKMt0-P9DperkTvYRxGcLsf9DerQqaMFQ44AtPBXuNyCvIPeRfHISjQyXWQuXfkxXMJFuNlROxbv-bASdPSfIi6QLBzFdVghz7U0uyrKtGTyEt5na5mo8q1tYVYfvSOqem8HJWXkRomgm0EG8GVYbpAhqB9zW7IGGK_M9VOJyePp2aJ7YUfIaI9qk0d5eONeKZrR5J4ClCP7nTWdOuOS5L0o1J7DyXeriXEXRkMvoxgSvw3ibopGG5Xbt2LyXSX1DdJQeGmXTiM9x83iWDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69579" target="_blank">📅 17:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69578">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=lng6jRu-QW-9rtUtH-EOP4vlkrbvDpJasVObBYl-bq62A3CN1_F4w8VClPaAluYDukj7v5QJDQNfxoJN4Qd-yQ4C-DFQHZNxM66vD0TjGKEHJpYXD7yODOoPDsUhIENZ1ZtQBFnRuv7M6Y7MLkmFMrGqMBYZEEfFHX8VoKuqfgauJCJDeYp0hT19JAXPN6TWLNV8VrQ3mVr7cIroWOWgsjJlLiZkI-UritytperG-AgyBTc6WD6cicdtWWAhcPdGUuaiLqVAEyf8buzj1vKr7pGGIndicLGr1X384pmCAhlxfNfSdPvm7LEXlDwDf9WKFhOiW2knfVk2QUgb7Uw20Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=lng6jRu-QW-9rtUtH-EOP4vlkrbvDpJasVObBYl-bq62A3CN1_F4w8VClPaAluYDukj7v5QJDQNfxoJN4Qd-yQ4C-DFQHZNxM66vD0TjGKEHJpYXD7yODOoPDsUhIENZ1ZtQBFnRuv7M6Y7MLkmFMrGqMBYZEEfFHX8VoKuqfgauJCJDeYp0hT19JAXPN6TWLNV8VrQ3mVr7cIroWOWgsjJlLiZkI-UritytperG-AgyBTc6WD6cicdtWWAhcPdGUuaiLqVAEyf8buzj1vKr7pGGIndicLGr1X384pmCAhlxfNfSdPvm7LEXlDwDf9WKFhOiW2knfVk2QUgb7Uw20Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
توی مراسمات اربعین امسال آهوی ایرانی کباب کردن و به زائرین دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69578" target="_blank">📅 16:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69577">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnbs6g6Z0N1EvK51Tvoyl4sHHRa3mGikPdnzeQADU7jSF9aFTLROAxzrvowh9OeEvgHUOhGj24GQ6rooExtvv-_fnIVGU_xlNXgkNjeRs_7UbNv7hLBirFBMgfky3RGHFCHerfkQ9Gez39NfvuU3rRhHeJkUUp89B13YE9jBamyY-NbFJ7MpKJ_P4hPoQJNhOLHh0V8aPdFNOmTpKUhduKsEKXQBsUbF64Vsif2hCm4a03qdZ0307U5fR8DZL2DfYkebLlj5lsmPgM3IkSV60GKLNRfzSiaP4GF4TJojaxSPo8zGtL4lBUSAfhSPyDutUS0sEoP9ZYYvp1spj4Ba0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛ ارتش اسرائیل برای شهرک المنصوری در جنوب لبنان هشدار تخلیه صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69577" target="_blank">📅 16:34 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
