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
<img src="https://cdn4.telesco.pe/file/twB2f5s8u8cxNRFStLaAIydVA4yvXu-8XXfU6EqeAFU8fRKfYnWIJan_V5xbIO2JS1jwU8p-RtnQc_DWSwH1eTm0pq13vqFpTnmcIwIhdIYxxqMfvGcLfSuFE3k_olntFJYSUMnsw7xl_w0lu5Aj1NlsBMkHc1ZqlqtwCue0gy6A4OKYS8mY43U1Bh1IG3Zgo5zdAAleaWYU7aksCx09uOb0dmw-GFg7Qbuu6XPGQTon3eN1StGNWkCpaJ9dCMhwrrPF1X2HKVzAb5Dc82UN4NKjBSm9JalgFBmTBHubu60UM9YuHpEg_dBVl7IkEWFzQeN1VKsjL44hria09xlhTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 02:47:57</div>
<hr>

<div class="tg-post" id="msg-72609">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/news_hut/72609" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72608">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nd5jrcx0xapkMyvM7echGpNQvEtqnKQLsEyS8pp_yaKgZyvUJ4yZdRGjusNHA6BrqW-eWf0WB8Pj7XWW478qZaU3qWINDng3dJFYlK95A8fhdEmdq_r8V6gywVewry_7oH2yIWQ5DHdl73jBdjEecWE4Fjj3nsY603yAAjWD8VibNYa9U9Svfqdm4wbry6BFJYq3cuh2fyELwQrpe-E_VPLmV_eSALwwGml8dKSgSbTzfL47W_KpqnMbscRZzt6KhGaoEG9C1Wlv8SRhf0JE4rgo8EjBimWE26RF-e0a_6GlOtzEtD3hsi-1YCgR7zIcF64cO7F974iojEKBqZ4eFw.jpg" alt="photo" loading="lazy"/></div>
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
قوانین رو در سایت مطالعه کنید
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/news_hut/72608" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72607">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5821a90294.mp4?token=IOt4K9mfj4BOvo3ZAQK45E8U_rw3REsCfLF9kz6n7sjLmE26OAoDm09VvqjRHSgu_-DlOLQlYLdlDuijyXK3z8uEjdYrZF1WA_VvXAluEAprSUM6WNSPHaCkpwsgVVl6wwWjDu0OLq4UyCUddmRR1SNFdDoHdKsZRq9z00CRUgLhsEZsKdtTfJpNeCFgosA9qp5BlWAXSdsq1n2y5JJHS5bZWPpacA-SptoAcSkRGdmsTlDb53V5DNNm9H3rOVLe5diOBwmh1QavHzWFGvACU6Wkvs8iD8X5yub5UY1s4WQ0DBiLJq00VUbmb39siBuKf73gQm7b6oncLt80EsfW8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5821a90294.mp4?token=IOt4K9mfj4BOvo3ZAQK45E8U_rw3REsCfLF9kz6n7sjLmE26OAoDm09VvqjRHSgu_-DlOLQlYLdlDuijyXK3z8uEjdYrZF1WA_VvXAluEAprSUM6WNSPHaCkpwsgVVl6wwWjDu0OLq4UyCUddmRR1SNFdDoHdKsZRq9z00CRUgLhsEZsKdtTfJpNeCFgosA9qp5BlWAXSdsq1n2y5JJHS5bZWPpacA-SptoAcSkRGdmsTlDb53V5DNNm9H3rOVLe5diOBwmh1QavHzWFGvACU6Wkvs8iD8X5yub5UY1s4WQ0DBiLJq00VUbmb39siBuKf73gQm7b6oncLt80EsfW8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
یا کار بسیار درست و هوشمندانه‌ای انجام می‌دهند، یا عمرشان چندان طولانی نخواهد بود.
وقتی با آن‌ها توافق می‌کنید، بسیار محتمل است که به آن پایبند نمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/news_hut/72607" target="_blank">📅 01:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72606">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd837a9d25.mp4?token=fWjF0Q90NveQgpLTd0gqNd88EEUdTGkEQY2rmkZnumYBB3jqPx-apFIwhqfPkX6ExY7YoW8qILkNRaz-N4B03nUTRU4mOI7CRENkUK2-DVAN3HfDXEKfu0rsylr8kPEzNmrImKCcpr2EyDSLNZmfg84SjSFYloKskfPZBvozdqBZ7bjyUkQ8VOrx3K0brQC8_ltSXzRvchSMRSdXodqp1ZFK50YuVtRbUxB3Pf1uiWtXuIGuKYaFIdZwCrg6IvLx72UiQR5yeoZwsGMDDIfA-CTkuplxERJ9E2ptssz6e_dn7iOSBiOM79tDpxKztoXepEN0qzykA4QOUs3lMgs9TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd837a9d25.mp4?token=fWjF0Q90NveQgpLTd0gqNd88EEUdTGkEQY2rmkZnumYBB3jqPx-apFIwhqfPkX6ExY7YoW8qILkNRaz-N4B03nUTRU4mOI7CRENkUK2-DVAN3HfDXEKfu0rsylr8kPEzNmrImKCcpr2EyDSLNZmfg84SjSFYloKskfPZBvozdqBZ7bjyUkQ8VOrx3K0brQC8_ltSXzRvchSMRSdXodqp1ZFK50YuVtRbUxB3Pf1uiWtXuIGuKYaFIdZwCrg6IvLx72UiQR5yeoZwsGMDDIfA-CTkuplxERJ9E2ptssz6e_dn7iOSBiOM79tDpxKztoXepEN0qzykA4QOUs3lMgs9TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایران در فوریه ۲۰۲۶، تنها سه تا چهار هفته با دستیابی به سلاح هسته‌ای فاصله داشت؛ شاید هم زودتر.
@News_Hut</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/news_hut/72606" target="_blank">📅 01:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72605">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69424629e7.mp4?token=JxDqJ0ztbPKmvk2kOM9j1TV7e8HAvg-jbUOdw0JJo_yDi-ykaqbw6kHF5Kb-X-5Vem1ALEY4Xjz9ApVXCTOaxNCrxDuiEljjVQhO0C-SjDhIE0xo1hc9AbT9PAbJS0ZTbGXFNIbvfoeETbrQjqZdv6wN8NxDjZMvMEj1HgdTN6dA5GxKYnhDBoRMPa_1-bOeA1IKTWYiYWXaCoqaESHztK-FGccPtesKQirAPI_vT3qMjeJfb4rBJIJj_Q_B1VWmVtU6pVMOYt8fBI9VRiUdDPpdorwHSffrxy32MT8Fevqh8ABnhyU461TsaBNr9uoYv4kfgK0VPN_RsA_dtK_0wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69424629e7.mp4?token=JxDqJ0ztbPKmvk2kOM9j1TV7e8HAvg-jbUOdw0JJo_yDi-ykaqbw6kHF5Kb-X-5Vem1ALEY4Xjz9ApVXCTOaxNCrxDuiEljjVQhO0C-SjDhIE0xo1hc9AbT9PAbJS0ZTbGXFNIbvfoeETbrQjqZdv6wN8NxDjZMvMEj1HgdTN6dA5GxKYnhDBoRMPa_1-bOeA1IKTWYiYWXaCoqaESHztK-FGccPtesKQirAPI_vT3qMjeJfb4rBJIJj_Q_B1VWmVtU6pVMOYt8fBI9VRiUdDPpdorwHSffrxy32MT8Fevqh8ABnhyU461TsaBNr9uoYv4kfgK0VPN_RsA_dtK_0wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ونزوئلا:
ونزوئلا تماماً تجهیزات روسی و چینی داشت. ما همه آن مزخرفات را از کار انداختیم؛ آن‌ها کار نمی‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/news_hut/72605" target="_blank">📅 01:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72604">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2bdd7600.mp4?token=Pdp5yccJh6Pmg_O8xxIGO-eigWEQnNiFCSGTHV45q2OAYBK7nMFI19wp7bI-KXcMeGHPkMsW17hCL0t4n6IdnMTgXB1Uchg6nZY5nzTh8VDiC8-5OJJslIzUd1xCt8owY_IC-67WLj07_uEZgI_HIwoe3WyU6BtmW0CVz2HGLSRIpWh3Qd51vNjp4UeZ7Y1mJfZYRLADWj80If0NWXqVhov_WhzsVctrly8eE4WHdTuz1HKH-GxCyR-H6nnGHm4v1F_a7Uot7qonzkafosRnpOl6ZtvXISRKhC6tZt_GJ_dXV0t6ZR2TDFd9dcQ6hUPNwSuf5XUChOGlqUXFW_ky3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2bdd7600.mp4?token=Pdp5yccJh6Pmg_O8xxIGO-eigWEQnNiFCSGTHV45q2OAYBK7nMFI19wp7bI-KXcMeGHPkMsW17hCL0t4n6IdnMTgXB1Uchg6nZY5nzTh8VDiC8-5OJJslIzUd1xCt8owY_IC-67WLj07_uEZgI_HIwoe3WyU6BtmW0CVz2HGLSRIpWh3Qd51vNjp4UeZ7Y1mJfZYRLADWj80If0NWXqVhov_WhzsVctrly8eE4WHdTuz1HKH-GxCyR-H6nnGHm4v1F_a7Uot7qonzkafosRnpOl6ZtvXISRKhC6tZt_GJ_dXV0t6ZR2TDFd9dcQ6hUPNwSuf5XUChOGlqUXFW_ky3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
رؤسای جمهور [پیشین] ایران دیگر با ما نیستند، اما سعی داریم با فرد فعلی خوش‌رفتار باشیم.
بالاخره باید با کسی کنار بیاییم، مگر نه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/news_hut/72604" target="_blank">📅 01:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72603">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ درباره ایران: ایران آماده تسلیم شدن است. ما همین حالا خیلی راحت پیروز خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/news_hut/72603" target="_blank">📅 01:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72601">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9371c09764.mp4?token=RL_kpZ-v8ORmTgCIl9BUfbXqND-P4LEOhIypH1k4HeH3-GbpO6MHOAGVKmi5brA3PHWKhD-7IH17ZkQ-EpgVwfuiQBa01wSsONXp5zwz4oOACr27I9wvGJbijFkiPmAXkuQjVzQjMIBegVo5ApbiBdy3LsOK06aQAbV2272S_tYzXwb4mZuZGqnUsQ0636O1y1BcQQtq1B4dY-WfoBuawGsYq6nW-YbbdfZuQe3HzlOCVPne5oFE24vp4Kw9pdtlvSiDqTLk0bUVhqXPvxYxd_OjANYnw7KZXZq0xYb92wEK9zYstDZ78zt7ZD2k97I-aGg2EOVIzqER5LegyVL7iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9371c09764.mp4?token=RL_kpZ-v8ORmTgCIl9BUfbXqND-P4LEOhIypH1k4HeH3-GbpO6MHOAGVKmi5brA3PHWKhD-7IH17ZkQ-EpgVwfuiQBa01wSsONXp5zwz4oOACr27I9wvGJbijFkiPmAXkuQjVzQjMIBegVo5ApbiBdy3LsOK06aQAbV2272S_tYzXwb4mZuZGqnUsQ0636O1y1BcQQtq1B4dY-WfoBuawGsYq6nW-YbbdfZuQe3HzlOCVPne5oFE24vp4Kw9pdtlvSiDqTLk0bUVhqXPvxYxd_OjANYnw7KZXZq0xYb92wEK9zYstDZ78zt7ZD2k97I-aGg2EOVIzqER5LegyVL7iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛مامور های عربستان یه شخصی رو که قصد انجام عملیات انتحاری داشت در مسجدالحرام (خانه خدا)دستگیر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/news_hut/72601" target="_blank">📅 00:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72600">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=i6tRyVpIV6EVNoiUih0t_CAxqpDl-ZuKKOkBC4U2RXGaoInTEh9lf-qqqEwRKT0MBr3fIR2fRaxd-TgBY097jQCgmqE9Z_OsNOS0kzlrLteICY4q9udMSBWFQKL_RH8MKo26xpcyfU_sT8QzDemv2NdanBz8kNeaSkxXwUIzwnEweQJYsmPfWyTXgKp9ewnDGPt_QdYUo6bhEQ3b_dhOFdBWHZW5UR1wFc4CKibugHJpBR_Mh0sCR5eiPR2V5oMrfySkZrYSdalmGl8zTsRK67dPe5ZLakT-E-g4lovqZ-_GtsVgvHVLTrVmuiMSUWucHJ2SaemRWiDRPbK_6IABlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=i6tRyVpIV6EVNoiUih0t_CAxqpDl-ZuKKOkBC4U2RXGaoInTEh9lf-qqqEwRKT0MBr3fIR2fRaxd-TgBY097jQCgmqE9Z_OsNOS0kzlrLteICY4q9udMSBWFQKL_RH8MKo26xpcyfU_sT8QzDemv2NdanBz8kNeaSkxXwUIzwnEweQJYsmPfWyTXgKp9ewnDGPt_QdYUo6bhEQ3b_dhOFdBWHZW5UR1wFc4CKibugHJpBR_Mh0sCR5eiPR2V5oMrfySkZrYSdalmGl8zTsRK67dPe5ZLakT-E-g4lovqZ-_GtsVgvHVLTrVmuiMSUWucHJ2SaemRWiDRPbK_6IABlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا ایران در حادثه «آر.ای.اف فیرفورد» (RAF Fairford) نقش داشت؟
ترامپ: بله، ظاهراً همین‌طور است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/72600" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72599">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfBzZzppE9DLCd6QjcprysynumsK0kss-0bzW5RnM2nI7HI2uycT4wn2cWNuqdjhZ68S3NWlPfpBn2X_l8_mQX-Z_Cy4FV08lfywFa8wwAcwKchfgXmxX0UR_0OJO9FaBEdZ3dMFGo-RPsHszo55lzyie5eSifLyXEAD93wF2nkWi-3VnIjnQ5jPCN4c3ALDMsqZgRQz2RFJqNXT2sB3PlxFSs-Z4UBPQPQOCsPTWdq8lBgsaM9mw5Zn_LBszx-avAfiLUrbV4yKt8h_-5PSQBfQbrjjnWaC-pd8knV3bGEYQY_nw7ALfK3PYABTGCm7UAbfuei5IxLK2ERPJy1w9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال استریت ژورنال، ده‌ها نفتکش ایرانی و مرتبط با ایران در آب‌های آسیا سرگردان مانده‌اند، زیرا ایالات متحده فشار بر کشورها و شرکت‌هایی را که به کشتی‌های درگیر در تجارت نفت تحریم‌شده ایران خدمات می‌دهند، تشدید کرده است.
حدود ۲۰ نفتکش خالی ایرانی تنها در سریلانکا سرگردان هستند و برخی از خدمه با کمبود غذا، سوخت و آب شیرین مواجه هستند.
از زمان اعمال مجدد محاصره تنگه هرمز توسط ایالات متحده در ماه ژوئیه، کشتی‌های دیگری در نزدیکی مالزی، هند و چین سرگردان شده‌اند و از بازگشت بسیاری از کشتی‌ها به ایران جلوگیری کرده‌اند.
واشنگتن همچنین به سریلانکا فشار آورده است تا از تأمین کشتی‌های تحریم‌شده توسط شرکت‌های محلی جلوگیری کند و به آنها در مورد تحریم‌های ثانویه هشدار داده است. فشارهای مشابه و افزایش اقدامات تنبیهی در سایر نقاط آسیا، بنادر و شرکت‌های دریایی را به طور فزاینده‌ای نسبت به خدمات‌رسانی به کشتی‌های ایرانی بی‌میل کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/72599" target="_blank">📅 23:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72598">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bce71f4cf.mp4?token=mimec_zNz4PbflAth667MO0MoJVtyrMlx7MdEx-z8hf3Uxcx_aFS9UlwxBYHL8VDsF32DN3FStLPPguI4OGW-EP4l5-Uhxi84fpda9jEcnR7SPgPQldwkexOyaWE74S6-WwMIW8-1cAVAP7ngJoDxd-tnSMtTowDzSyQsdrVMz8FhgPUz74szoc-myAD0u3ZJiodm3uPstzSNopt7cDLC3Wqlz9bOF3Jgfbg9t5-2EiF5e96rrUm4tdk3fBLnuUqClzS_IujlPdFch9T_HcAKMJlysITJ9BGYxtNf_0__Jr4lMooyEXfRKe7Y0vz0FubraB06NmM5Af68w_FH6ZIZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bce71f4cf.mp4?token=mimec_zNz4PbflAth667MO0MoJVtyrMlx7MdEx-z8hf3Uxcx_aFS9UlwxBYHL8VDsF32DN3FStLPPguI4OGW-EP4l5-Uhxi84fpda9jEcnR7SPgPQldwkexOyaWE74S6-WwMIW8-1cAVAP7ngJoDxd-tnSMtTowDzSyQsdrVMz8FhgPUz74szoc-myAD0u3ZJiodm3uPstzSNopt7cDLC3Wqlz9bOF3Jgfbg9t5-2EiF5e96rrUm4tdk3fBLnuUqClzS_IujlPdFch9T_HcAKMJlysITJ9BGYxtNf_0__Jr4lMooyEXfRKe7Y0vz0FubraB06NmM5Af68w_FH6ZIZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با پیشرفت هوش‌مصنوعی، حضور و غیاب تو مدارس هم شکلش عوض شده و به این صورت با تشخیص چهره انجام میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/72598" target="_blank">📅 23:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72597">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaetEoFG7S1IG6D7pyg1rHtRpmypHQPUj67-eOTqq3xX6s6miEP0Xs27xPUcKS15jvFyKa6OBA1fd1ggnDPvMebrb5CipOGWGVAuhPGlJwemfUvjwwHXLPtjFfkhvYOL85tVW46vOoyQ5s0gBPRsMVEWPs14zolD5RzLQRZQvswjyWz7hfU4lLhNdCwzaVU-zAI4fNVx8CtLylyghtg6U1o3nMAKkF3qmYXsrjdHJ0_GYkQTq7P_N-BuJhdbgQsN9sr6WLs6jq512NIru4-zCzidlR8GD0aMX1mC189ZENJEb967pYvoYBWP_Md7x6dGfCriB891HHe516cvDfHgyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛پلیس بریتانیا اعلام کرد که یک تبعه ۲۷ ساله با تابعیت دوگانه بریتانیایی-ایرانی را در مرکز لندن به ظن «تدارک اقدامات تروریستی» بازداشت کرده است؛ اقدامی که با حادثه روز یکشنبه در نزدیکی یک پایگاه هوایی در انگلستان (که مورد استفاده ارتش ایالات متحده است) مرتبط دانسته می‌شود.
دو ملک در این منطقه مورد بازرسی قرار گرفتند.
مأموران مبارزه با تروریسم همچنین از مرد دیگری که تبعه ۲۶ ساله بریتانیاست، بازجویی کردند.
ویکی ایوانز، هماهنگ‌کننده ارشد ملی در بخش پلیس مبارزه با تروریسم، تحقیقات مربوط به پرونده «گلاسترشر» را «بسیار پیچیده» توصیف کرد و اظهار داشت که تیم‌های تخصصی در حال پیگیری «چندین خط تحقیقاتی» هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72597" target="_blank">📅 22:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72595">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_zpWOm7vuusdaFYHdFTiRvdNp9RH8PD0_AK8SG2jOdHF5G70RI1vEMC72UAxI-MQ2hL8bzM1P1poD8Xn-paNP0uglydIcPldfKn9PkfDIeC90myppW3h_ALviAH2lyuege3r5Ge7pph1MoVRYjk1vuUoAUBuBj9xeV4BeBZfB1KLAXhbPw6QDIGxqlKhjGyd9z6EYtWScLCSuI-mC09IlIH58nmJwIjSpejIUII3_V5EcX0j5KlRQqh6nYpzgKv3W_uqePVUmniEo6y7BOuG0k9-8dGUZLP7JjRFcJV1XZSekC8swjpy682ZCbqvhmQ2ziHE4p12vXIV0UQWgtVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=CpQMTT7wzFovSHAW5JOLJvXgkddUQUK-GXK7eLvrtliP1ttWehyRjgk5L2G9luZB-a9t0RRDH_Hjy1I7xUaIFKRcE-ppBgcmJzvuQQ7ZThAqPVqdM-pxZ_hxe420pxYtCtv--iloEInNwkhlcIFdVabLFdx3ItDuIgB-be5c-w6_WvN8YMbEa0vK0zEXrUESIzikXFEtkZUtOs22-iYhsAV1O6JoR4GSzpBVEQ4M6CS5du6A8fO-qz2qhe9juHWlyXg10EYPK6OyXAFVULXKJvlI-APN8rfUcIED7AUrjy8lHxsoS0RZGl_StLoNmdUihwS5aGc8s9AprDdNY5Cydw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=CpQMTT7wzFovSHAW5JOLJvXgkddUQUK-GXK7eLvrtliP1ttWehyRjgk5L2G9luZB-a9t0RRDH_Hjy1I7xUaIFKRcE-ppBgcmJzvuQQ7ZThAqPVqdM-pxZ_hxe420pxYtCtv--iloEInNwkhlcIFdVabLFdx3ItDuIgB-be5c-w6_WvN8YMbEa0vK0zEXrUESIzikXFEtkZUtOs22-iYhsAV1O6JoR4GSzpBVEQ4M6CS5du6A8fO-qz2qhe9juHWlyXg10EYPK6OyXAFVULXKJvlI-APN8rfUcIED7AUrjy8lHxsoS0RZGl_StLoNmdUihwS5aGc8s9AprDdNY5Cydw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ در‌تروث پستی از اعتراضات دی‌ماه ایران منتشر کرد که مردم در آن شعار میدهند «امسال سال خونه سید علی سرنگونه»
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72595" target="_blank">📅 21:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72594">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQiyHdajGvBONX6QbRG216ua2qWU5cfLFrZJiyRmUlubgUW2DCe8Ay6VIztPUo4whSJix2wCdPHKdH1ChtXBUQh6mNGINfWQEGSEh9V56WC3HyqzMSs1YbSTPhgw1AkPhXgsWrM18uWJnd7Rwa3QfeHLK4EvPO8beN2hys-Hqhgt5-vIaKC_chZufGUm_WEyAKUTu2-UvAY7f8TfdqFttBQykZmdJTdxUJwrrr7WYZYEoT2e-Ftu6WwMpHA6w5f2x7ZulIzoAa20peeXa7e8dPahXcegfrluvhMor2Vmob61ftJAJULAlYkxL3F9t2KrluaswtqQb0z6xYAHRU-7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ:
«گفتم برای از بین بردن تهدید هسته‌ای ایران ۴ تا ۶ هفته زمان لازم است، اما این کار را در یک شب انجام دادم. زمان باقی‌مانده برای اطمینان از این بود که این تهدید دوباره بازنگردد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72594" target="_blank">📅 21:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72593">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210cf276f7.mp4?token=sNlhwJcga0gwlMxpbid0rfVu1umgF6oL70G9D-7AsyyShWl2iwScG85JBjv6Ppnmyn-6kLy-z-qQyaFLVJ4t7TpL9E2VX9SWoH3cK3Q-2so92_uQJ1v7sEz43N3qvmiIyWUmD7NG8o-xtIjiGx6GHtXQUGyHgiBFlQXhpsQqrNooan6MH0Ru3kH42LCMAaxf77YkPTnTMdm5UPBlZDJDGZyl2Rp-F-vcSnHBYLyIzqfHHrO9Jln_cCZPkar_iL_Nzt-3-30rXg_6KLl-vc9dd_YJW_eEBpDFYPG-qE0wE-0QUgXBu5w_y6zRv7Wc5pwt6CIAyYfNcrX2buHtmN0Gxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210cf276f7.mp4?token=sNlhwJcga0gwlMxpbid0rfVu1umgF6oL70G9D-7AsyyShWl2iwScG85JBjv6Ppnmyn-6kLy-z-qQyaFLVJ4t7TpL9E2VX9SWoH3cK3Q-2so92_uQJ1v7sEz43N3qvmiIyWUmD7NG8o-xtIjiGx6GHtXQUGyHgiBFlQXhpsQqrNooan6MH0Ru3kH42LCMAaxf77YkPTnTMdm5UPBlZDJDGZyl2Rp-F-vcSnHBYLyIzqfHHrO9Jln_cCZPkar_iL_Nzt-3-30rXg_6KLl-vc9dd_YJW_eEBpDFYPG-qE0wE-0QUgXBu5w_y6zRv7Wc5pwt6CIAyYfNcrX2buHtmN0Gxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوسی (از شبکه فاکس): آیا ممکن است این خلبان [در پرواز فلای‌دبی] توسط سپاه پاسداران در آنجا منصوب شده باشد، یا به طریقی دیگر افراطی شده و سپس تلاش کرده باشد هواپیما را سرنگون کند؟
ترامپ: بله، ممکن است همین‌طور بوده باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72593" target="_blank">📅 20:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72592">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31205a46fc.mp4?token=G7Ev7M-g3RPcmcV_NyB_wZ30jvrsSF1F0-m_sXp_uVeSarTedgHzDgj1z7V0mllfsC8ntZRO0CFwJh-YHDFKH1I3vJ7Q43HrSkq85gv7NBQrV2BPtYE7WdAw65bzuu9TYd-_YgTlZU9r-dHVfXqrga5PqlLwzcqeK6gYr88pyH8tS6BJHVac8SCAGpipYeu1BqyS9qoYlhp6Pc6dwgYJ7dFtgd7LjjMhVOYqjFtHl8FDOkxVaghRiTkqhTB2x-BmB6-0QXKEU08-ewjN2iE2xpEpfqHbbH82MZ55UOIK5rjiDj3Ii4kdWF2jAPj_XVaXy6FF3834aFrzxIlU4w-HGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31205a46fc.mp4?token=G7Ev7M-g3RPcmcV_NyB_wZ30jvrsSF1F0-m_sXp_uVeSarTedgHzDgj1z7V0mllfsC8ntZRO0CFwJh-YHDFKH1I3vJ7Q43HrSkq85gv7NBQrV2BPtYE7WdAw65bzuu9TYd-_YgTlZU9r-dHVfXqrga5PqlLwzcqeK6gYr88pyH8tS6BJHVac8SCAGpipYeu1BqyS9qoYlhp6Pc6dwgYJ7dFtgd7LjjMhVOYqjFtHl8FDOkxVaghRiTkqhTB2x-BmB6-0QXKEU08-ewjN2iE2xpEpfqHbbH82MZ55UOIK5rjiDj3Ii4kdWF2jAPj_XVaXy6FF3834aFrzxIlU4w-HGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات ترامپ درباره احتمال دخالت ایران در حادثه هواپیمای فلای‌دبی:
بر اساس آنچه می‌شنوم، پاسخ را «بله» می‌دانم، اما در حال حاضر مشغول بررسی آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72592" target="_blank">📅 20:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72591">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=OO4bcJG-a_3pb_72dbivvzEt8ZRa379vvEbEDI9k9UYAemi7fyybpj0kg3FonsV4Xnw1BfUKQ3f5dKOgr4jp792xffmbPeUN0pAR0Vj2jtz1MfigI9MsbB5lDjljscVu6toJPaLWARYVdumtCkvbnh4P8EcSkipkTb0jkICS3zmuekWvdQA4vSIXjC6TnCCcsrrPd4rY9GF8Ie8oOJtdRQ9SEZ_SqCtJCyTTZFU8Uv7gOB6XjKuEDoYia1ymdmZcPbHBMbqJYxkrJCZLCa6SumxREHxUYQqWwNsvMRfLGoz0mXIqkcuGkunwTvAvIBiRFaUH_xDEuj9bnHcL0dtbJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=OO4bcJG-a_3pb_72dbivvzEt8ZRa379vvEbEDI9k9UYAemi7fyybpj0kg3FonsV4Xnw1BfUKQ3f5dKOgr4jp792xffmbPeUN0pAR0Vj2jtz1MfigI9MsbB5lDjljscVu6toJPaLWARYVdumtCkvbnh4P8EcSkipkTb0jkICS3zmuekWvdQA4vSIXjC6TnCCcsrrPd4rY9GF8Ie8oOJtdRQ9SEZ_SqCtJCyTTZFU8Uv7gOB6XjKuEDoYia1ymdmZcPbHBMbqJYxkrJCZLCa6SumxREHxUYQqWwNsvMRfLGoz0mXIqkcuGkunwTvAvIBiRFaUH_xDEuj9bnHcL0dtbJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
:سؤال: در مورد نیروهای نیابتی ایران، مثل حزب‌الله، چطور؟
ترامپ: سرنوشت آن‌ها به سرنوشت ایران گره خورده است؛ هر مسیری که ایران طی کند، آن‌ها نیز همان مسیر را طی می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72591" target="_blank">📅 20:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72590">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ درباره ایران:
به جرئت می‌گویم که صددرصد مردم — از جمله در سراسر جهان — با دستیابی ایران به سلاح هسته‌ای مخالف‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72590" target="_blank">📅 20:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72589">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سؤال: اگر ایران پشت آن حمله به هواپیما باشد، آیا دست به تلافی خواهید زد؟ آیا آمریکا تلافی خواهد کرد؟
ترامپ: ضربه بسیار سختی به آن‌ها وارد خواهد شد؛ نگران نباشید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72589" target="_blank">📅 20:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72588">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8061e95725.mp4?token=BUeZGZfNUTVS3aGVLFps8C-BLUXoxsF_VHDqAjIzBQTzq39xZ8SQ3vRrGzOaahqLsI9bF_qjTCQcLPo1r1NVha4SWFSlabXevLdyRNfXBvVh9EybnobS14B0rLnzl8Yl3CfK_fFbvLkWPHZAZdKBIoUxF4wgVBL34lQpCI2NiUb6DyH6YEf2KG6bxp9LGyF3_GSWV5VExU8C_1cNM8TOFQOU7ho3MPcH-wAsM0yf_V5BOk2oDm5Q8H6gYEB-Co4Pm3miF_XMgHnU-CnkZSATncdXxncH8MDPiWAg-MIO2ybBllM87hBN98nhOMKSK7GvbKBp_LxNms0LCmOFM_iXEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8061e95725.mp4?token=BUeZGZfNUTVS3aGVLFps8C-BLUXoxsF_VHDqAjIzBQTzq39xZ8SQ3vRrGzOaahqLsI9bF_qjTCQcLPo1r1NVha4SWFSlabXevLdyRNfXBvVh9EybnobS14B0rLnzl8Yl3CfK_fFbvLkWPHZAZdKBIoUxF4wgVBL34lQpCI2NiUb6DyH6YEf2KG6bxp9LGyF3_GSWV5VExU8C_1cNM8TOFQOU7ho3MPcH-wAsM0yf_V5BOk2oDm5Q8H6gYEB-Co4Pm3miF_XMgHnU-CnkZSATncdXxncH8MDPiWAg-MIO2ybBllM87hBN98nhOMKSK7GvbKBp_LxNms0LCmOFM_iXEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛رئیس‌جمهور ترامپ درباره ایران:
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72588" target="_blank">📅 20:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72587">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ درباره ایران: «آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند — و نخواهند داشت.»
انها توافق کرده اند که سلاح هسته‌ای نداشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72587" target="_blank">📅 20:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72586">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرنگار: لارا ترامپ گفته است که جنگ با ایران ممکن است انتخابات میان‌دوره‌ای را برای شما به خطر بیندازد. آیا موافقید؟
ترامپ: ممکن است. [اما] باید کمک‌کننده باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72586" target="_blank">📅 20:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72585">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ce76f49c.mp4?token=G6gSADseMl-cRfn1HXl5dmsci0meI_NvSDctJ95pV98BNJ0RwRg6MwIZQo4QgKe1syOiZnanmDwW4fkH0qKjrDXLURlH-9wxmFtU0GZw82kx5WUFqPKR1eD2XrVOWDl-k7wogPcHFHs9zG74VuGbJfIO1XOo-3qYg2C1aqkbYNqdNa52LDZgCsdtM4G_0QA9hBjAkmXXewU4rtB6_GFOTkOnpxDcYE9Vqw1OH8SSwB4lse6vqNM8qd50N2xmUVwUAosnMVC66I_8k0S15g0V2F4ZnquvvC5sIFeA4plt_44Rjxt-bwYp8Y8GHmzJt3Xsuy_qenogFjfAZAP9tUPGxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ce76f49c.mp4?token=G6gSADseMl-cRfn1HXl5dmsci0meI_NvSDctJ95pV98BNJ0RwRg6MwIZQo4QgKe1syOiZnanmDwW4fkH0qKjrDXLURlH-9wxmFtU0GZw82kx5WUFqPKR1eD2XrVOWDl-k7wogPcHFHs9zG74VuGbJfIO1XOo-3qYg2C1aqkbYNqdNa52LDZgCsdtM4G_0QA9hBjAkmXXewU4rtB6_GFOTkOnpxDcYE9Vqw1OH8SSwB4lse6vqNM8qd50N2xmUVwUAosnMVC66I_8k0S15g0V2F4ZnquvvC5sIFeA4plt_44Rjxt-bwYp8Y8GHmzJt3Xsuy_qenogFjfAZAP9tUPGxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ایالات متحده در حال اعزام گروه ضربت ناو هواپیمابار «یو‌اس‌اس تئودور روزولت» به خاورمیانه است.
تا پایان ماه نوامبر، سه ناو هواپیمابر و دو کشتی تهاجمی دوزیست در اطراف ایران مستقر خواهند شد.
@News_Hut
| NBC</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72585" target="_blank">📅 20:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72584">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a42198336a.mp4?token=ACDuFQC9hEPZPfvuO9H-TgCBbT9horTJgFBeEvohASoWvWvp2dXiOcJ4py-0yFu8nuqdYbBBX1fdxNcIXwfqAuZiSKxGW4tkh8l6pqEmGqCwKrfRs_qS6v8xK8Zdm5v5A-bZh20DcAPgQPUBO0rHlt2XhdvgyRJ5Z95_Fl0VeWD3_wWl_1Varesn-YUGoacby_HjwJOhgw-1Z2BwTfco4v51Vcq3ixcTHLAfQGlS5LWjUaYIfqSGna6oQENvHAkgWEKmws2TKD6FRl21-gwc3JPyhFeawbM5kqlvrAfHn1Pogg2WUx8Tnuin1kZdGD46jxJaI3urahZplBkLOVDJgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a42198336a.mp4?token=ACDuFQC9hEPZPfvuO9H-TgCBbT9horTJgFBeEvohASoWvWvp2dXiOcJ4py-0yFu8nuqdYbBBX1fdxNcIXwfqAuZiSKxGW4tkh8l6pqEmGqCwKrfRs_qS6v8xK8Zdm5v5A-bZh20DcAPgQPUBO0rHlt2XhdvgyRJ5Z95_Fl0VeWD3_wWl_1Varesn-YUGoacby_HjwJOhgw-1Z2BwTfco4v51Vcq3ixcTHLAfQGlS5LWjUaYIfqSGna6oQENvHAkgWEKmws2TKD6FRl21-gwc3JPyhFeawbM5kqlvrAfHn1Pogg2WUx8Tnuin1kZdGD46jxJaI3urahZplBkLOVDJgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری ثبت نامی های خودروی لاماری با شرکت وارد کننده، که ادعا می‌کند به دلیل محاصره دریایی چیزی وارد نکرده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72584" target="_blank">📅 19:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72583">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5610e80a6.mp4?token=c0UZM5kWApg4bz3dCe-ndgi5GPnMGU49XZtjXmeBs9EpPAla7yp5GcaPC2cCXDwXvJEKtFY3a0E6MHsefdoISSQPd9-jX1XO61ZyBbjOA8v1buAB_n-iiZdjM4lLXgsTeriUr4dNT0fb_TG_mf_8JHOYq_3tXMQxVQUEZuUMSCeY6yInkl925oIDAUj0VGpepNrZc6byKHYNivHtJAkkliPRm1CVkqkxifaHbTFtEoFj3RM_BgdcXH3eQvGX3Sx7pkfk3qVCdPkBNMxMZA7Hw5tBYAq63c6WIAR-JL17PHCkXu3uAy9CDQkHzstI5ZtPrGPLyYSAjPY55JC--onKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5610e80a6.mp4?token=c0UZM5kWApg4bz3dCe-ndgi5GPnMGU49XZtjXmeBs9EpPAla7yp5GcaPC2cCXDwXvJEKtFY3a0E6MHsefdoISSQPd9-jX1XO61ZyBbjOA8v1buAB_n-iiZdjM4lLXgsTeriUr4dNT0fb_TG_mf_8JHOYq_3tXMQxVQUEZuUMSCeY6yInkl925oIDAUj0VGpepNrZc6byKHYNivHtJAkkliPRm1CVkqkxifaHbTFtEoFj3RM_BgdcXH3eQvGX3Sx7pkfk3qVCdPkBNMxMZA7Hw5tBYAq63c6WIAR-JL17PHCkXu3uAy9CDQkHzstI5ZtPrGPLyYSAjPY55JC--onKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه آریامهر:
«کلمه‌ی شاه در این‌کشور (ایران) معنای ویژه‌ای دارد و همه آن را می‌پذیرند. ممکن است اهالی روستایی دور‌افتاده در کشور درباره‌ی اتفاقات جهان چیزی ندانند، اما آنها معنی شاه را می‌دانند!»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72583" target="_blank">📅 19:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72582">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72582" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72582" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72581">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm-7tZv02EfmO_BIRXnHsgscTlFxlubRv6d9EAUJROVwGV3XJF5FWMDZlLznRbpN88d1ivjGqGbnSQ63ur_703MSL3i9VMS8A0LUye6bTprV9TEayXToPi-qznNZ5oTE_rmykR0-vndea2DXFEf-bnb_x7Mv8mSHZt-5k4Ris9QowzO1CCDq7cRfoWIVipeBnMfMCorvsIi310qWNpp7Nn8aiLEz1T6_9JIaQWsEOqOBv6Pg7Vktlkl4NO6FqHFoPc9GnyAv6PSDeLndx470K4--Hyk1ykiDUhZqa8qKjpRkWZcB4cEF0WVcNpDxOMftYYyO6Zpf2XPTN9JFRMyR-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز پرتغال
🆚
دانمارک را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۵ گل زده
دانمارک: ۲ برد، ۲ تساوی، ۱ شکست و ۱۰ گل زده
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72581" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72580">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">#مهم
؛
یک
مقام آمریکایی:
ناو هواپیمابر «روزولت» و گروه ضربت همراه آن، سن‌دیگو را به مقصد خاورمیانه ترک کردند.
گروه عملیات آبی-خاکی «ماکین آیلند» نیز دوشنبه گذشته سن‌دیگو را به مقصد خاورمیانه ترک کرد.
حدود  ۲۲۰۰ تفنگدار دریایی در قالب این گروه آبی-خاکی به خاورمیانه اعزام می‌شوند.
تا پایان ماه نوامبر، سه ناو هواپیمابر و دو گروه عملیات آبی-خاکی در نزدیکی ایران مستقر خواهند شد.
با این تمرکز نیرو در خاورمیانه، فرماندهان گزینه‌های متعددی برای مواجهه با ایران در اختیار خواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72580" target="_blank">📅 18:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72579">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MVM1MZqpvZyU9-wjOwfqMVoc-Cs9hKvVQHuQNsfvfwC4gXsMQGi-_umfQVEmyOwPIC_5Ydus8r1uu7jSQV9ALg0I3kVcKdO7xw6hXwV7pp2GxBVxQSE3Q8qdAoiSGaSriOEDrnMuCaNgFSimmNctWD7vGyY7lJEnWT-YJrlrU0S0vCBPllNLSzIweU52eMYULQqV-MZhvm0YqQUJ_obtQVSQsPuMUYuQInMBgIlG-BAHKthz01jL3RPn_oTsKibxUlo56xU7MxYXS6iYO4q5GI-tUzb4XZyaGCICP87guSS52_tBB6gUjynsVLHs3RqPkwWbeywwv60t5kp7883NrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیرمحمد، خواننده آهنگ سنی نردن گوردوم، از بدن فوق جذاب و عضلانیش رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72579" target="_blank">📅 17:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72578">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f32d27e64.mp4?token=cVxq3X089acroYzxdr6yQJuqF0PcG_zR4G3WH_fQG_J6kxuLnh9I1Ck-rqtHl3s6vHGtFvwBlm6QJXBsi-auBr4pIUOU9eIDebP4-vKI6lVHtBkaosQ4Rv73lCSDhfy5p63TcUqIvEMfA6e0yphwWM9dHn9nNM5QtAbRWEqXfKcLrI_9eX42dFozumb88qXvFB38uATD-J2u0LcBQfdWISh678kHbRS1so4w4JVy44LcHweD7jHvwUtrx3mBdp4YDxnfrZvslWRmZ8HtPr61eUiItC-Gd7gHVr9KitRFximLG1P_U80nfWDdiuWC3uJr3bUqVQz9lAdsht1PSRHxxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f32d27e64.mp4?token=cVxq3X089acroYzxdr6yQJuqF0PcG_zR4G3WH_fQG_J6kxuLnh9I1Ck-rqtHl3s6vHGtFvwBlm6QJXBsi-auBr4pIUOU9eIDebP4-vKI6lVHtBkaosQ4Rv73lCSDhfy5p63TcUqIvEMfA6e0yphwWM9dHn9nNM5QtAbRWEqXfKcLrI_9eX42dFozumb88qXvFB38uATD-J2u0LcBQfdWISh678kHbRS1so4w4JVy44LcHweD7jHvwUtrx3mBdp4YDxnfrZvslWRmZ8HtPr61eUiItC-Gd7gHVr9KitRFximLG1P_U80nfWDdiuWC3uJr3bUqVQz9lAdsht1PSRHxxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیات حملات آمریکا به ایران از 28 فوریه تا 8 سپتامبر ( ۹ اسفند تا ۱۷ شهریور ) :
@News_Hut
| thecuriospark</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72578" target="_blank">📅 17:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72577">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8db6d91d.mp4?token=v-wdZrwkvs8IuOORtl7PPwYOAhiLuBsAbjHb1Iw6v9fF6hPbA-Uyz1IuqSjMvUVSirAct_wdAo8A1wBKDDTSoRMlcRHPjNbBf8gd9rUhdW-qvDDNJxnOf7XjEy9h-Pap9Tak_jPVdebX46FlZmfyEHIT8HStDAFA6mIF-noSUoiATvauQd6CYmmVE6D-ViRcKOQASkLkHRsVSRpBEats7Bp8f9nPSkfgrMFuCnluvqw5rO1zaRuXi6-wBHMiHH3TNPWtblrK3a4Ws1fR2zMvD6ZLzoVCW8fOh_49zeVUGrVOW5RtkZUtXEfN3x6IueLMbINzwtdHxsWJbj8BUJ-NWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8db6d91d.mp4?token=v-wdZrwkvs8IuOORtl7PPwYOAhiLuBsAbjHb1Iw6v9fF6hPbA-Uyz1IuqSjMvUVSirAct_wdAo8A1wBKDDTSoRMlcRHPjNbBf8gd9rUhdW-qvDDNJxnOf7XjEy9h-Pap9Tak_jPVdebX46FlZmfyEHIT8HStDAFA6mIF-noSUoiATvauQd6CYmmVE6D-ViRcKOQASkLkHRsVSRpBEats7Bp8f9nPSkfgrMFuCnluvqw5rO1zaRuXi6-wBHMiHH3TNPWtblrK3a4Ws1fR2zMvD6ZLzoVCW8fOh_49zeVUGrVOW5RtkZUtXEfN3x6IueLMbINzwtdHxsWJbj8BUJ-NWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو رقص این خانم ایرانی تو وان ترکیه وایرال شده و واکنش‌های مثبت و منفی زیادی رو در پی داشته:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72577" target="_blank">📅 16:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72576">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a415ffdec.mp4?token=tn-aCw1HJ3D4qJEoA_Ul-Mgvn_Vf-HeOLXVS-JbYfS0R4-ANmx37eS94nb82duR7L5eHDh3bnIAha8Af3eVazy4Vt11-4vqsnKkfOZagfUc517TjnqHUz27PaiXbRHeIdy3KK18w58MPq-dXZzbURhrGYW4Fykj5BIYv0VFuE612Ozwxx64-4tB6zmeTp1vvCXA9YTyWEXhGWTQJY6A9BJr1jZJWi5_1R2dgPus7q-JhUczebyAaVoIr3WbGdc16dT2KHadiMLKlmr-slHxeYxTignXlWORVr87X2SCDre1BPH5PG-9WvErZB5I8ZezzqeKvkDQF0eRUDhjY4c73Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a415ffdec.mp4?token=tn-aCw1HJ3D4qJEoA_Ul-Mgvn_Vf-HeOLXVS-JbYfS0R4-ANmx37eS94nb82duR7L5eHDh3bnIAha8Af3eVazy4Vt11-4vqsnKkfOZagfUc517TjnqHUz27PaiXbRHeIdy3KK18w58MPq-dXZzbURhrGYW4Fykj5BIYv0VFuE612Ozwxx64-4tB6zmeTp1vvCXA9YTyWEXhGWTQJY6A9BJr1jZJWi5_1R2dgPus7q-JhUczebyAaVoIr3WbGdc16dT2KHadiMLKlmr-slHxeYxTignXlWORVr87X2SCDre1BPH5PG-9WvErZB5I8ZezzqeKvkDQF0eRUDhjY4c73Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حساب اسرائیل به فارسی در پلتفرم ایکس:
حالا که بحث هواپیما گرم است، یادی کنیم از هواپیمای کیش.ایر که 31 سال پیش در مسیر تهران به کیش با 174 سرنشین ربوده شد.
زمانی که سوخت هواپیما تمام شد و در شرف سقوط بود، اسرائیل تنها کشوری بود که به هواپیما اجازه فرود داد و جان صدها بی‌گناه را نجات داد.
جمهوری اسلامی هرگز نتوانست پیوند بین دو ملت ایران و اسرائیل را از بین ببرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72576" target="_blank">📅 15:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72575">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ اظهار داشت که ایران خواستار توافق است و درباره پیشنهاد آتش‌بس ایران که در آخر هفته رد شده بود، ترامپ گفت پیشنهاد ایران برای باز کردن تنگه هرمز کافی نبوده است.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72575" target="_blank">📅 15:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72574">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سؤال: نتایج نظرسنجی‌های شما هرگز تا این حد پایین نبوده است.
ترامپ: این ارقام ساختگی هستند. من هر کسی را که امروز نامزد باشد، با اختلاف ۲۰ درصد شکست می‌دهم. نظرسنج‌ها فاسد هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72574" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72573">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سؤال: اگر «گادی آیزنکوت» در انتخابات اسرائیل پیروز شود، آیا آمریکا می‌تواند بهتر از زمانِ «نتانیاهو» با او همکاری کند؟
ترامپ: خب، نمی‌دانم. حرف بدی درباره‌اش نشنیده‌ام... فکر می‌کنید او پیشتاز است؟
سؤال: او نامزد اصلی اپوزیسیون است.
ترامپ: خب، خیلی‌ها بارها «بی‌بی» را تمام‌شده دانسته‌اند، درست همان‌طور که بارها مرا تمام‌شده می‌دانستند. من بی‌بی را دست‌کم نمی‌گیرم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72573" target="_blank">📅 15:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72572">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سؤال: گزارش‌های متعددی وجود دارد مبنی بر اینکه پیش از ۷ اکتبر، به نتانیاهو درباره احتمال وقوع حمله هشدار داده شده بود.
ترامپ: امروز برای اولین بار این موضوع را شنیدم.
سؤال: گزارش‌ها حاکی از آن است که مصر و امارات به او هشدار داده بودند.
ترامپ: فکر نمی‌کنم؛ به نظرم اگر او خبر داشت، حتماً اقدامی در این باره انجام می‌داد.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72572" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72571">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ:
اگر من رئیس‌جمهور نبودم، عربستان سعودی الان وجود نداشت؛ اسرائیل هم همین‌طور. آن‌ها از روی کره زمین محو می‌شدند.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72571" target="_blank">📅 15:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72570">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سوال: شما در ابتدا گفتید که جنگ با ایران حدود شش تا هشت هفته طول می‌کشد. اکنون وارد ماه هفتم شده‌ایم. می‌توانید توضیح دهید چرا این‌قدر طولانی شده است؟   ترامپ: فقط به این دلیل که می‌خواستم فراتر بروم. آن‌ها را از میان برداشتم. می‌توانستم همان‌جا متوقف شوم،…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72570" target="_blank">📅 15:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72569">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سوال: شما در ابتدا گفتید که جنگ با ایران حدود شش تا هشت هفته طول می‌کشد. اکنون وارد ماه هفتم شده‌ایم. می‌توانید توضیح دهید چرا این‌قدر طولانی شده است؟
ترامپ: فقط به این دلیل که می‌خواستم فراتر بروم. آن‌ها را از میان برداشتم. می‌توانستم همان‌جا متوقف شوم، اما می‌خواستم پیش‌تر بروم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72569" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72568">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سؤال: هفته گذشته گفتید که ممکن است ایران را نابود کنید. این همان واژه‌ای بود که به کار بردید.  ترامپ: بله، این کار را می‌کردم. چنین چیزی ممکن است.  سؤال: چطور ممکن است «رئیس‌جمهورِ صلح» خواستار نابودی یک ملتِ کامل باشد؟  ترامپ: چون با نابودی ایران، صلح را…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72568" target="_blank">📅 15:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72567">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سؤال: در مورد ایران، آیا قصد دارید پس از انتخابات میان‌دوره‌ای، حملات هوایی را تشدید کنید؟ گزارش‌هایی در این باره وجود داشته است.
ترامپ: ممکن است. ما سلاح‌های زیادی در اختیار داریم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72567" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72566">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سؤال: هفته گذشته گفتید که ممکن است ایران را نابود کنید. این همان واژه‌ای بود که به کار بردید.
ترامپ: بله، این کار را می‌کردم. چنین چیزی ممکن است.
سؤال: چطور ممکن است «رئیس‌جمهورِ صلح» خواستار نابودی یک ملتِ کامل باشد؟
ترامپ: چون با نابودی ایران، صلح را در جهان برقرار می‌کنیم. به عقیده من، تا زمانی که ایران وجود دارد، هرگز نمی‌توان به صلح دست یافت.
@News_Hut
| time</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72566" target="_blank">📅 15:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72565">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نتانیاهو با مسافری که به توقف حمله به کابین خلبان فلای‌دوبی کمک کرده بود، ملاقات کرد و به او گفت: «بدون شما، می‌توانست یک یازده سپتامبر دیگر باشد.»
یانیو حیون، لوله‌کشی که هنوز پیراهن خونین به تن دارد، گفت که مهاجم را خفه کرده و کنترل‌ها را به عقب کشیده است.
او به نتانیاهو گفت که برنامه‌های تحقیقات سقوط هواپیما را از تلویزیون تماشا می‌کند و به این ترتیب می‌داند که چگونه باید کنترل‌ها را به عقب بکشد.
او هیچ سابقه هوانوردی یا نظامی ذکر شده در گزارش‌ها ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72565" target="_blank">📅 15:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72564">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0687bd0f.mp4?token=LTqLxdsTQL-sxK0xbwN7QVPR2jhRPL3keJrioXfA1LCn7MR6dlRuDhAKkC7rzqkLIPkCNqQnhQX4H4ZObr61WFkS1CijNUOZLZxDoW6OCnU3if-CDre6blpQVRCCKcBuWzpDZObwEq8dSU6Bxb8ridnlC8qlQL21oHw1gPvNH0YdJWc8G2Xw7OkWSBKyKdpu50PsIZya2c6S4IPkV7Gm7laH405qkpnnEE_BJ-b5p0MXGVobmFGwImfiaIlovvyPGfJdPVZ-6UyeMJ5EqvP9fAWIyJbDwXrShGysnNqTxQDdQ7Fg4JHKdbv27RyRSJhvHl0xywyhzW9PUrJNJZiFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0687bd0f.mp4?token=LTqLxdsTQL-sxK0xbwN7QVPR2jhRPL3keJrioXfA1LCn7MR6dlRuDhAKkC7rzqkLIPkCNqQnhQX4H4ZObr61WFkS1CijNUOZLZxDoW6OCnU3if-CDre6blpQVRCCKcBuWzpDZObwEq8dSU6Bxb8ridnlC8qlQL21oHw1gPvNH0YdJWc8G2Xw7OkWSBKyKdpu50PsIZya2c6S4IPkV7Gm7laH405qkpnnEE_BJ-b5p0MXGVobmFGwImfiaIlovvyPGfJdPVZ-6UyeMJ5EqvP9fAWIyJbDwXrShGysnNqTxQDdQ7Fg4JHKdbv27RyRSJhvHl0xywyhzW9PUrJNJZiFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی آقامحمدی، عضو مجمع تشخیص مصلحت نظام جمهوری اسلامی:‌
گروه‌های مسلح آموزش‌دیده در امارات و اسرائیل وارد کشور شدن، مردم در محلات مراقب باشن.
جریاناتی در محلات استقرار پیدا کردن تا عملیات‌های ترور انجام بدن.
اومدن نتانیاهو به امارات رو جدی بگیریم. طرح نتانیاهو اینه که به‌جای اسرائیل از امارات بجنگه.
+البته این چیزا رو میگن تا تو اعتراضات احتمالی بخاطر تور و گرونی بهونه قتل‌عام دوباره مردم رو داشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72564" target="_blank">📅 14:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72563">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnSTpFTZuDoyUi4FHemt0t7X39MLBpw56XyFMVbhapVHC88_-dRCOSaY82cuMvTomu2oqqafNv-ca4tsgXQ_cHjN4yTc9wLa1m-XLcYTbCdvL4CAVq7Z-kq0L3HZ061RxcB0-Uszs8QvYWAOTXLlVp5A--Y1Wbo00In4XpS9ivotv26v9qQ8bhOpro_HW805ih18mqbVdLoZlfecKDq9f3blyMMJbaiKzwgU0-6Skb7UVM6onsQLdO49a554hKl2_M92xPD5zy2kHHe3PWD65qRp_pe0c3-59gcPfX6IKFCo579L_0D0-E_1fQi85JpF1elUr8myWBPMiFF4S_gT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گزارش نیویورک‌پست درباره هشدار اسکات بسنت درباره اقتصاد ایران رو بازنشر کرد.
بسنت: ممکنه ظرف دو هفته «چیزی از اقتصاد ایران باقی نمونه».
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72563" target="_blank">📅 13:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72561">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEXnZLiEssnFw6-RYjyRxslp7rbD8IJ5AjDsPO11BwOHOi7eiuzNvWiemgTVHIPzzpYZ6gOiJtWbx8q0UElbIiRsAdbKasLgMAhQOKdTCbBtUHtq1nNM_EXkCcq7Hfz-b5BdPJ4WHedcHeVnlpQ72oWUad_pFVn1LYh8yf-SmGRn21YQjUMxrnBTkXtlf60MaJTBcnSHEMTRP23BWHixaLw1OrEOiD6f0viQXXNz1wVwZUXXNjqB6_jxqf1lX2zmckJuCAbBFN-yzTjDC7oGuHPfnOiyJiOXtcLs6_IXDXEgSLqPXwCgbL1Q1TMQVYXTXmFtt1Iaue9MsluuR86ZNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKpnn0qjjq1SIQI0nW4VCdkzSIz5PVg8L4PqXTqdvhgpk4A-w68JzjoGj17SdvMMqpL9-4SxMxL9Rp8BvuNu5XvxoMxoeAwr3asTFb40Zv2nXq4mpy6VA2xdz7npfdd7bggIZ9JnVpaPzG2V1PHD15TlOUPrnN_WLWU8IlbcvSMMW2jPsK0mcpufBjYBliV4rDTfJhhc-T7fOvK90eknYJX8XyH00FYWBT8AZoiLxBLcUriFKBre77iEk_ECBLXxY7nRxa2vu630lnjoZNCJPn3ph1atASdtOo3ERRfwzcPMxBGoH9JEcw4ktStjm7Qtllr8k1A1S0OWFf1LpRyIHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیژن مرتضوی که همین دو سه روز پیش گفته بود شایعات باور نکنید و نمیام ایران دیروز لایو گذاشته که اومده تهران
+پست چند ماه پیش بیژن!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72561" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72560">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565ee82707.mp4?token=FpD-Z_8uyMKXs2QIN_R34FAyo42oEcR1hXrrOo-uqb1a9aWX-TAaNESBB7TMW5YGu1Cb1gTx893JL2rnmhYmFZTaJ4SkZZur5SaWdwzo4SfRqYB1ePpwVL128-NDfJq-SwuhGF8VpNq4wEFLu8xkU5StkDB1BRBTaEj3y5_Ch0CgpF4t5v_bONvP43Ec_fhOdhzOXazN9Y7BgvOENXBqbhlrJwOPnHmvNNFsN9UFZT8Bkuw54tp7qpck-xxDbcGlg0TIz4qmvBu9MrTSBCqzZ85S_FCd4CqE1_lC2MnhnpHCo4mvw2KnEgiVJfbRdq2SdlTJKyGNI8AAwDdNyyP6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565ee82707.mp4?token=FpD-Z_8uyMKXs2QIN_R34FAyo42oEcR1hXrrOo-uqb1a9aWX-TAaNESBB7TMW5YGu1Cb1gTx893JL2rnmhYmFZTaJ4SkZZur5SaWdwzo4SfRqYB1ePpwVL128-NDfJq-SwuhGF8VpNq4wEFLu8xkU5StkDB1BRBTaEj3y5_Ch0CgpF4t5v_bONvP43Ec_fhOdhzOXazN9Y7BgvOENXBqbhlrJwOPnHmvNNFsN9UFZT8Bkuw54tp7qpck-xxDbcGlg0TIz4qmvBu9MrTSBCqzZ85S_FCd4CqE1_lC2MnhnpHCo4mvw2KnEgiVJfbRdq2SdlTJKyGNI8AAwDdNyyP6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد حافظ حکمی معاون وزیر ارتباطات و فناوری اطلاعات با اشاره به قابلیت‌های فعلی استارلینک و فعال شدن قریب‌الوقوع «Direct to Cell» تو سط ماهواره‌های استارلینک و امکان اتصال مستقیم تلفن‌های همراه به ماهواره گفت:
«اگر استارلینک فراگیر شود، وزارت ارتباطات و شورای عالی فضای مجازی را باید شهربازی کنیم!»
اگر قابلیت اتصال مستقیم گوشی‌های موبایل به ماهواره‌های استارلینک فعال شود، سازوکارهایی مانند رجیستری تلفن همراه عملاً کارایی خود را از دست می‌دهند و شناسایی گوشی و مالک آن غیر ممکن خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72560" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72559">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72559" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72559" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72558">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3yd9kbvV3alkDHAFw7xTErXxX-By1U9oSkAMrfMZ6grCAeAUdpuh4v3T5fzxi3S-xXfkdIvXJG1xQHGU9ujCPrr5I8cAw6z6kkj1jh6Q3QfnrZYlbPJsLAza5guwtsEtaLUPRThfiq5w6MAF6ouOp-b0I6_XFl2zMbWg_6YXefgTQ894gWSV2woaEYJY0xLHFPGQoB3ktm7SwSNd7qA833sS_r2cSy4cZmij-jlFiQQBETA2r8e8lMSMufw_niFtv-gBR1PLfTBLmGT24sMyg4iE0rbXrIz_6NUjSgHG0raivs8gARTjubdtnRxgQPuNKCyKBEC68hd5lH70ZE6QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
صربستان
🆚
آلمان
هلند
🆚
یونان
پرتغال
🆚
دانمارک
نروژ
🆚
ولز
بولیوی
🆚
آرژانتین
اکوادور
🆚
ژاپن
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
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72558" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72557">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbA9B6zmL6-EY8UhLv5UCrLE9QKxLNrJvS4oX8fYUsHqXBl1VjG7Z9DcZVvMKnL1vGkw1kvBo8jZLmOkbG5-2ANbDOd0nZan7FcmAoc-vmzctJ9eYHgekV43CYeljaZPfgqSOzDJ0OA5gnyvlcJ9SNPAEYiax2pzC1gsVPI6Zq3bKounJRbovSgEwB6VJ3akbFQUZyqXTbrcw5zcEoPGnQgaShIT3MJ0mtN1Zw8BxHL-9ccMI5JnI1VIAUswnfOIGnafDtNlcBw0x_n269mWbAs9KpQ46DtQRN3nHf0W8nmmQKu5Kgedv6YgXc1IAbRMGPqmGadFnP2my4WxtHW1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد که نیروهای آمریکایی در چارچوب محاصره بنادر ایران، مسیر ۱۲۵ کشتی تجاری را تغییر داده‌اند. این رقم نسبت به گزارش روز جمعه، حاکی از تغییر مسیر ۳ کشتی دیگر است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72557" target="_blank">📅 12:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72556">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be557ff64.mp4?token=XX49lb8ZKj7Yq2-NfLM3lU9-7anyKM4oincMlSgcRiYuVz3B3Kj8PsnmX2loLIfnaVe_fNhS3Y92mun_zx0qI3PO4qaQ9lXd8O5N0WdbR8nOcXig7hLQqYK4lzejm_UnfHc1xx6lfsP_woDK80jbn_Incvhb8XhVF-2zWFohOTNtzQakxDRGY3FNBn3wTqsID-xyiufWPI_BsaSpDlDXjP3cWY-62ICMCywKTgjlmO1HjlId0IE7R5TYweryaAeMPWCYokVmxfjoAYyS8SlwcDe6NJrhoIkLODxiziJtugZopTUmUfHEk4XKFILbcyhFbdk-TjcMifTlv0Hq58AteQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be557ff64.mp4?token=XX49lb8ZKj7Yq2-NfLM3lU9-7anyKM4oincMlSgcRiYuVz3B3Kj8PsnmX2loLIfnaVe_fNhS3Y92mun_zx0qI3PO4qaQ9lXd8O5N0WdbR8nOcXig7hLQqYK4lzejm_UnfHc1xx6lfsP_woDK80jbn_Incvhb8XhVF-2zWFohOTNtzQakxDRGY3FNBn3wTqsID-xyiufWPI_BsaSpDlDXjP3cWY-62ICMCywKTgjlmO1HjlId0IE7R5TYweryaAeMPWCYokVmxfjoAYyS8SlwcDe6NJrhoIkLODxiziJtugZopTUmUfHEk4XKFILbcyhFbdk-TjcMifTlv0Hq58AteQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفر از هموطنان رفته بودن شمال که توی مسیر پلنگ مازندران رو هم دیدن:)
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72556" target="_blank">📅 11:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72555">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mv_ml6-c0wetIOW_iUszQPaVDFwWcYPPWjEctsA6gxJibi90mwVH5a0iMQH_HnUu3zfMEqubHUawy_KXHWgbUvJKcZJKGJKFeR5cPz721j-s_ODnmbvmBOSDR47FdIhXssxkPWsg96Oc1nb36_96woL1YWvhdDt6KEdZCE0gh0rXBkPIp5wevG-OzMXMRmRfS5Ysuj-pBBuElZ4I081wPV8HGaDGy0dMtrMlAICjl1JYi1G_WauL_nuvQ3jKOF6Ulohzg7kWbqp9nyci4lBHX5iy5V787RYQ6rVPVmhSPMc84Qx8PyoR5KtWO2TJ2wxVTsbUVifDS7SVp0dvbH3zOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛اکسیوس:مارکو روبیو وزیر امور خارجه بعد از اینکه مذاکرات میان آمریکا و ایران در روز دوشنبه به بن‌بست خورد،به هیئت نمایندگی ایران ازجمله عباس عراقچی دستور داد که فوراً امریکا رو ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72555" target="_blank">📅 11:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72554">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=jVdGYLZbM5j-c678Ty5acfFtRxaXGgIoLKHLmBzNKivJAj47rpR7gQFLEjVEfY5Al341eFVHTRykmdhoixB2NB4ito8jM06VmAZnwplEHG1GPcmMMQoodiTHwdPF3KWVU0hXnEvGz5U7-_RhTHg8hrawPtl-TgmUG1-SLL8b_5YEy925v9BbG6a8pHtBgIwGB4WmD_D16iu5FwaK0l0lkAyEFgFFX2yDAHNvbpttU6g-Zbmn1OMAkxDjkNBA1039HZvsObV402-9jpATvHaP4d5UESkcXt86UxvgansurAliitVnF0DW5Jzy6ihWySwOEmkzyeQJrzero6nN806W1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=jVdGYLZbM5j-c678Ty5acfFtRxaXGgIoLKHLmBzNKivJAj47rpR7gQFLEjVEfY5Al341eFVHTRykmdhoixB2NB4ito8jM06VmAZnwplEHG1GPcmMMQoodiTHwdPF3KWVU0hXnEvGz5U7-_RhTHg8hrawPtl-TgmUG1-SLL8b_5YEy925v9BbG6a8pHtBgIwGB4WmD_D16iu5FwaK0l0lkAyEFgFFX2yDAHNvbpttU6g-Zbmn1OMAkxDjkNBA1039HZvsObV402-9jpATvHaP4d5UESkcXt86UxvgansurAliitVnF0DW5Jzy6ihWySwOEmkzyeQJrzero6nN806W1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی یکی از وبینارهای مملکت بین یه دختر به اسم "پرنیان" که پزشکی قبول شده بود و "اشکان" که کنکور مردود شده بود، یه مسابقه برگزار شد.
نتیجه جوری شد که همه آخرش ایستاده اشکان رو تشویق کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72554" target="_blank">📅 11:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72552">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HUQIp3RSzu9KUEtG0z1ISXgopql6zC7XQNoC2apnAwqQNGLRFZcLT8DvNfwOlpa2NoU7l_eRyFdH8kO5oqG1sge8kxoOJfBjAC2bX02cKg8iYXbEPcZCaoFogeXD1GB7vkCXXnvOigr94Q6pG6Ze7VFZqol5Hya2KcBdxDvzMJl7FRJlJH3RZOOUBw2FBd29mxzQF84gFd3S_HLsy-liKXwNXutsqjglFi1X6LleAzrOEPiph7U73sj_3O7wwGpriH9OnB_T1MN0sq5_XFMz9hhZRCFR0_FVtHRBVtYEiEMCa99zsWRYieVmwHQJyqaVpCm41PEreGSUdlUgNMr5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V5941gjcczOnToAafS_nIx27wh99kYPpj_Mpk-rRiCifsUCMwRLqNCBmsqq5sM8GHgVGrqWQiVqQKOhbXTuue_VISWMTuRZ2LazuhAMtdOz-Hyq2mStnaXw7wfLFEGuAiW4XPmRoCW-M_nPyb4cLWB-VkMQLgL4fm148XbyYfMgSc2tUmcPLR9Ts_SqDm0pGlMt_hBDtleN8JIaVCzu2SBpGQ9kP_7sfnjR5_D431DJ9_-w5rPigFTg6zlW2h5XyuGXiZuguvm4xkRagCZJv1gJJc-LSbS5Ft32tj0oc-QHIxdjZX-9HetrTbQHVVvj6HD-c9_iEPGn15QaRGs4jMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از حامیان حکومت: من 13 ساله که یه بیماری درمان نشدنی دارم، دکترا قطع امید کردن و گفتن و تا آخر عمر درگیرشی.
تا اینکه یه شب رهبر شهید اومد به خوابم، بهم گفت درسته من کشته شدم، ولی مملکت رو اداره میکنم.
یهو اسمم رو صدا زد، مصطفی! رفتم جلو و بهم انگشتر هدیه داد، صبح که از خواب پاشدم دیدم الله اکبر! هیچ اثری از اون بیماری نیست و کامل شفا گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72552" target="_blank">📅 10:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72551">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b14d6c45e3.mp4?token=KX_-eRI0b3S1fROlfwQIiITmePaeeB9U8Py54TSecV0RIOH091eOxMv2bpe2_U4jo7-_XbtLjWMOt0HUAE4qIXd7mBL4EIUJBaQB-n4_USvltaLU0UbiWMy0plokxyzO8oSM3P-9VsSXcIzKHu9etoAwa-RCqynIdeS-IOrWIrYmKXiNlcOno_8Xb5ZbJ9JIJF6qBwNRWYJF1zjw_55Tl3dJvSlX0rTZ1Wi9_8BFAke0CEWT6ySR9mCUUR13gMKw-dYfAfLZUn73LM1oBCeKTMduoShf7uhjon8u0N7kspTL1Hzoiho-LRybeJ6uHlkePZc3sn46qWU7KBCJM0YP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b14d6c45e3.mp4?token=KX_-eRI0b3S1fROlfwQIiITmePaeeB9U8Py54TSecV0RIOH091eOxMv2bpe2_U4jo7-_XbtLjWMOt0HUAE4qIXd7mBL4EIUJBaQB-n4_USvltaLU0UbiWMy0plokxyzO8oSM3P-9VsSXcIzKHu9etoAwa-RCqynIdeS-IOrWIrYmKXiNlcOno_8Xb5ZbJ9JIJF6qBwNRWYJF1zjw_55Tl3dJvSlX0rTZ1Wi9_8BFAke0CEWT6ySR9mCUUR13gMKw-dYfAfLZUn73LM1oBCeKTMduoShf7uhjon8u0N7kspTL1Hzoiho-LRybeJ6uHlkePZc3sn46qWU7KBCJM0YP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کلاسای دانشگاه مملکت، یدونه پسر، با ۵۰ تا دختر، همکلاسی شده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72551" target="_blank">📅 10:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72550">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969c5e0df6.mp4?token=Wowrw5230BK2WcjCG2KQIBr8_flHymaYhfRj85vWTOMxG2wJggAf8m7IsYsGAbkVLP4U2h9CMWTQwrNhmj7esb8C3nLoIDPCQP4XhyKmYhhL7fxgiiddBKtzPkLSe7CbZCCoyoXiDjhomF6mQN5oqWliZcJD64baMt_wrkhEK_RxI85_fT9ypSDeLqVhURO87f71E8d7n42EiSyjpgOtMmBc8G7-CexRCKHN3g8U8epMwYlLcMZjD1F-mRaVhLRA0Vo5yn4nmbcqDJ8LN1eEDIsF3u4FTyEo6x12wPMNwBLCoJwpDhSKefZ0wRyV2jW0f-7FYD3mpPmdUk8hgZoK33errWtGKIMRNcBwmxU-o5oYjP8TAbRWAqi-mDvB_qaSuX0ydgGNIeIW02OH7qunWWOV_GXHw3w7gr8YxSthzxjmoCDHBrMr947ILot0JmxBPjGVmJ0DVOFzR83P3mpOM5rFFnGOgIqV1GG2iRAWZZxWDFuMhJ4EeO9Hqg0NdEUUWKtFtaP7MNAMZnzIw1xYFjCJD7g_spRN3FZukERa2vwl1ch35U3wfWyoy6y57PJZmM3JVwLjlB7KwS4UZ_R20XgRE7JAZ4xWzFWAjazZ64Swuf4Pv-83JZd8Rhq2kWgTtoM2wJ07x0uQAdOGBwLoDrJO22oLLxQ827y7WyASx8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969c5e0df6.mp4?token=Wowrw5230BK2WcjCG2KQIBr8_flHymaYhfRj85vWTOMxG2wJggAf8m7IsYsGAbkVLP4U2h9CMWTQwrNhmj7esb8C3nLoIDPCQP4XhyKmYhhL7fxgiiddBKtzPkLSe7CbZCCoyoXiDjhomF6mQN5oqWliZcJD64baMt_wrkhEK_RxI85_fT9ypSDeLqVhURO87f71E8d7n42EiSyjpgOtMmBc8G7-CexRCKHN3g8U8epMwYlLcMZjD1F-mRaVhLRA0Vo5yn4nmbcqDJ8LN1eEDIsF3u4FTyEo6x12wPMNwBLCoJwpDhSKefZ0wRyV2jW0f-7FYD3mpPmdUk8hgZoK33errWtGKIMRNcBwmxU-o5oYjP8TAbRWAqi-mDvB_qaSuX0ydgGNIeIW02OH7qunWWOV_GXHw3w7gr8YxSthzxjmoCDHBrMr947ILot0JmxBPjGVmJ0DVOFzR83P3mpOM5rFFnGOgIqV1GG2iRAWZZxWDFuMhJ4EeO9Hqg0NdEUUWKtFtaP7MNAMZnzIw1xYFjCJD7g_spRN3FZukERa2vwl1ch35U3wfWyoy6y57PJZmM3JVwLjlB7KwS4UZ_R20XgRE7JAZ4xWzFWAjazZ64Swuf4Pv-83JZd8Rhq2kWgTtoM2wJ07x0uQAdOGBwLoDrJO22oLLxQ827y7WyASx8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اولین موشک اتمی جمهوری اسلامی در  ایتا و روبیکا آزمایش شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72550" target="_blank">📅 09:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72546">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rMjffzKrxmjaiAApNcv7ciyPldrTAru8nt_C43ZWtigBkXSGsEN4ORxd5uJKfzTts0WBC9gDFhn1y8GID6e-ERU5lHkLbTEIY3mwPgFEG74sciNoOcu0eC7aQUVZ8Z8ShDCmrlc3C013ifKaWb9hrVFZD-zKHk5iqR1wZ0How551qij0UloYoMIAGVGeIr0cDpXVyyHDPU8K8ZTIUsdXju_zC6h8me44gW5Et7ig7T1dM1eZdAWzbYFDqxgAksX2YKTFvyD-73fRet-XCBcGgwObinkdig3u8Fl5abbEEDRfeB6cVRYI-nzOWBHiZcgif-J5fwTX1b43BI1aFVqljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jvU5Sq58kRvA8qkP2D_RUE5v2hLLXz7tpCeAz4UHlAflYViJSSNZ4EMtKwzEhXIgatgr_06dh--qw1pPQhFhmdVy3lJc5tIvnkk1a5kGHWpAhoVm1dX6aDB2QttP74WxVXzd3PXaYmCyqSqwgwhshMVTncN7z42VfWeMmr2edzlap6Yugov4fRxw_CDR0b6kjLUtuffRp6ppqwazzQqAgwlA8dOF5mcQ8UZyrEqjC86LhJL5fNJt9DmMrn-zcYrN9p4_a87X-d6zU5UbrkdGz5I6pgPe-IQVqGISPOc49MP1vMW5R_Rdzr5L7RsTCrRuOvLkexMX1UUXEt4h9E9Q7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E5L9N5b0Lp1xdBiLX7d5sa89nmbPNYN8ujPjFK5deQ1bqc3ZoesI8-PNN_NGOypYSz7e3l0nl_JQEG0iLTrl63WUWuZjSF9zY-fFWXYPYPaRWrUlI40NJ3C3GYUCu2Rk_9-kPwPitZQYuA_HdbWqROJ5KMpk1VfoejOKYoc41D3Ql6Ayan2tA2VJgcVPGRcb0pLvgpq7qbedycZgWrucK2qzEY1Xq25KB5oaDNqOBn4mj-HK9ruOJwppJ-DpWQTinKbJ7t1CL7LsaA56UmH8IvH_8hmNO2KF1NaxoTb9I5O29iecBn_wxggKZYvxSF86lZ3m69ypGpcYwLAxuWmxbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb63ca7239.mp4?token=gaiFzJyG8XZWpy6mPbYKSUxixmpveJa89aLJxP1Aulvf3UkuiWsjzFPagrSmZbZXKqDcmDzBaT_o6xR1vuboFVMpAieBuJ64X1R8tsQykumWT3sz0f4OeW4LNJCU7SI9fDl438rnP9lcqRAqNI28sZgJd2fEjh31DzaRO1ZJeVjdI4G7bS1Zo28QMbgS7IqfpG03wOxCImHsrzp4q6NCoCECsutWh3qK35PmK_2BZa4irgRFcrKAMSx2x9xpl9NSOMr7612Xx-clUuNtvLD2T1TU8HCm951wzfVpLZzpDJ9AR0xBmhmDwPG82BTogD2eQLbOE8nIM0mPeO2aNSrD7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb63ca7239.mp4?token=gaiFzJyG8XZWpy6mPbYKSUxixmpveJa89aLJxP1Aulvf3UkuiWsjzFPagrSmZbZXKqDcmDzBaT_o6xR1vuboFVMpAieBuJ64X1R8tsQykumWT3sz0f4OeW4LNJCU7SI9fDl438rnP9lcqRAqNI28sZgJd2fEjh31DzaRO1ZJeVjdI4G7bS1Zo28QMbgS7IqfpG03wOxCImHsrzp4q6NCoCECsutWh3qK35PmK_2BZa4irgRFcrKAMSx2x9xpl9NSOMr7612Xx-clUuNtvLD2T1TU8HCm951wzfVpLZzpDJ9AR0xBmhmDwPG82BTogD2eQLbOE8nIM0mPeO2aNSrD7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دارن خودشون به جنایت جمهوری اسلامی اعتراف میکنن!
دو روز پیش توی بندر کنگان، مامورا می‌ریزن خونه یه نفر و جلو خواهرش به رگبار میبندنش!
انگار گزارش داده بودن اینا گازوئیل قاچاق میکنن و مأمورا ریختن در خونشون، تا پسره درو باز میکنه، به رگبار میبندنش.
پسره، باباش جانباز شیمیایی جنگ هشت ساله بوده و خونوادش ۲۰۰ شب و هر شب توی تجمعات شبانه شرکت میکردن!
حالا خواهرش پست گذاشته که مردم راست میگفتن، این حکومت قاتله، ما اشتباه کردیم، داداشم و رفیق بی گناهش رو به رگبار بستن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72546" target="_blank">📅 09:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72545">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72545" target="_blank">📅 01:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72544">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/news_hut/72544" target="_blank">📅 01:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72543">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXX7vS_ENFxB6GboElbY7bGLNAtFEpvqTXm8ZAnMzbrOBQD7DXYsSMmDQmy6hOoarTHzN9ODfLO1vIO08kCtFMVWFj1ZGBm3uy06CXtZwlKBwag7Jvfhlbp4EO3JcoaSTWBK9j5od4DmFY_-4vSaKykgKb7WerkF8plhKMDU-3hTrK9Szz6wNteN3uJXs3quWfah-VQ6GjUlfZIroceZyF8x8mDsHsWdUNNVJLMqsOg8g3XF5PejWQ5pEcWvKaI9359EKZlJiTtkKRTBdIXUpEHt5vrWpWpeSuNS5X0S8j8I694q1_xFKyq_rVnYVsxZxoz5iOq5ihbwz0jn72KVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز پنج فروند سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز؛
+دارن نفتکش رد میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72543" target="_blank">📅 01:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72542">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=EtmKVUmMt3y2gZaPi24NkKNY1h1HvDQ8Dl39hedaonlVwJV1we2X8LGYvncT4SP-z9EZkbPI6S9IfoY4h7nYdVZz40ldrUq6gSq_rLPj8zeS1OIEpMiQi6s3ez45RrBqriyyREj8vbx6mowiJR1DHV8RinvCC8KpDaIe3Ukjj2u8Wq3lGeawsIsRnTF0TZcQs61YyeCZcVg71wNVeumO3sTjACXhcxXlZJb7gCdcqu5K6rVt6MOp7PlULmfJQf_E08ygjs4ZvlXSkvDLs31d3WO_ugzwYpthvDzfuq9j4WGrfZxw43o4kUfOhFUHY4qNaRYwq9KlhKi3GI3A7OiVCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=EtmKVUmMt3y2gZaPi24NkKNY1h1HvDQ8Dl39hedaonlVwJV1we2X8LGYvncT4SP-z9EZkbPI6S9IfoY4h7nYdVZz40ldrUq6gSq_rLPj8zeS1OIEpMiQi6s3ez45RrBqriyyREj8vbx6mowiJR1DHV8RinvCC8KpDaIe3Ukjj2u8Wq3lGeawsIsRnTF0TZcQs61YyeCZcVg71wNVeumO3sTjACXhcxXlZJb7gCdcqu5K6rVt6MOp7PlULmfJQf_E08ygjs4ZvlXSkvDLs31d3WO_ugzwYpthvDzfuq9j4WGrfZxw43o4kUfOhFUHY4qNaRYwq9KlhKi3GI3A7OiVCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال:
شما ایرانی‌ها را دیوانه توصیف می‌کنید. چطور می‌توان با آدم‌های دیوانه به توافق رسید؟
ترامپ:
شاید هم آن‌ها را منفجر کنید. ما باید در این باره تصمیم بگیریم. یا آن‌ها را منفجر می‌کنیم یا توافق می‌کنیم. زمانش دارد فرا می‌رسد. ماجرا خیلی زود به پایان خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72542" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72541">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02359c50e8.mp4?token=GrGq6l9cFGmAthA-KslYzpdd2bhketCj_F4gOWyquqqdKcym__i1qamSyRJGUJL5eBMDHnAY3qiTWtGbyoqIxZWWybCgwGzKHT3MbFXXf9cy8SZeCXhZja71SHgI4W4IjgT-WnsZhA2-0c9xNQaUzj946MDQHnB6SAQPWPNgCK3Ju1rcDz5ErSLZJBP_R_4Se7oSbyVrHsQo-iU2VHacBKIWTptfIMaDtnKr2Y_sqzopW328BKQIXsuSxNCe49x80LRvZSBAes-JS5G9QOZkGnmr0eCTmkElzfwLFFhXOHYe5fw1RhdSfitwL0nYg-NNfox2oxjMVPHhC4-9QxvP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02359c50e8.mp4?token=GrGq6l9cFGmAthA-KslYzpdd2bhketCj_F4gOWyquqqdKcym__i1qamSyRJGUJL5eBMDHnAY3qiTWtGbyoqIxZWWybCgwGzKHT3MbFXXf9cy8SZeCXhZja71SHgI4W4IjgT-WnsZhA2-0c9xNQaUzj946MDQHnB6SAQPWPNgCK3Ju1rcDz5ErSLZJBP_R_4Se7oSbyVrHsQo-iU2VHacBKIWTptfIMaDtnKr2Y_sqzopW328BKQIXsuSxNCe49x80LRvZSBAes-JS5G9QOZkGnmr0eCTmkElzfwLFFhXOHYe5fw1RhdSfitwL0nYg-NNfox2oxjMVPHhC4-9QxvP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
رهبران ایران با تمام قوا برای به دست گرفتن کنترل می‌جنگند؛ اما کنترلِ چه چیزی؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72541" target="_blank">📅 00:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72540">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fe1c6438a6.mp4?token=XSXOYEbY6f8ax8njDyd6w4W4nivJprXN_y0g13uB9D6U1wv3ZShJr6Jf7vUfSwBoLnhxHol1GS6sG6UAki6R4K3TfCbhfEwOo_OiDWJLa3CL3mRlPhIrvcMUsOx8ag19vndsGruR666Haa45GgOFSA_l6CyVviBkaWkTs-uRklRJ8Vebky90kYyO5yAbZOcwWzBk6l_zYJPVLd-oYOHko_MjSDlF8-9zAwPOm_nFzRoC3HMbxKhIlqlSUU-AHclXmsYK08ypWPSr4znfU-FCKgH5aIHwyEWWqYsJFFA0RxG_e0ma3S6VFu6TezcFcPze392hIQJx2omUxYzamKNVhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fe1c6438a6.mp4?token=XSXOYEbY6f8ax8njDyd6w4W4nivJprXN_y0g13uB9D6U1wv3ZShJr6Jf7vUfSwBoLnhxHol1GS6sG6UAki6R4K3TfCbhfEwOo_OiDWJLa3CL3mRlPhIrvcMUsOx8ag19vndsGruR666Haa45GgOFSA_l6CyVviBkaWkTs-uRklRJ8Vebky90kYyO5yAbZOcwWzBk6l_zYJPVLd-oYOHko_MjSDlF8-9zAwPOm_nFzRoC3HMbxKhIlqlSUU-AHclXmsYK08ypWPSr4znfU-FCKgH5aIHwyEWWqYsJFFA0RxG_e0ma3S6VFu6TezcFcPze392hIQJx2omUxYzamKNVhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنجاقک‌ها زیباترین مدل رابطه جنسی رو دارن.
اونا بهم متصل میشن و شکل قلب تشکیل میدن و تو همین حالت پرواز میکنن و... تا کارشون تموم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72540" target="_blank">📅 23:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72539">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a16c7cb51.mp4?token=L-3fKE6MwqgC1FBcr94FNgVMbROn6gRW7uqquGVhZ_xd0QSXaekW-E5pc2ejkj97dNcTwSTMW31LzMBsnINz4YEycSJKHNkU2sM-_jYGQI0bMNEvMdn-Po3iZrlW11XJRe5VZcbGBdJGKzabNqdRr5iOkbYPp2hvgT2gXhogUJr3APvTbjgcvB7lGwuUa3t_zUyD6uzOio9torUjm7-T7NOsbi2OGDLkQlM8fFyVqBbHIxMI6y4Uzo7l3B-lFfymC0hPOnCZIgweJ1KiOkfuyMkeH6nSH9IpWIYwP9NnMaI2seCqHiavGoqQFM3OHGRih53qYjFpYDIAd1daN9lsOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a16c7cb51.mp4?token=L-3fKE6MwqgC1FBcr94FNgVMbROn6gRW7uqquGVhZ_xd0QSXaekW-E5pc2ejkj97dNcTwSTMW31LzMBsnINz4YEycSJKHNkU2sM-_jYGQI0bMNEvMdn-Po3iZrlW11XJRe5VZcbGBdJGKzabNqdRr5iOkbYPp2hvgT2gXhogUJr3APvTbjgcvB7lGwuUa3t_zUyD6uzOio9torUjm7-T7NOsbi2OGDLkQlM8fFyVqBbHIxMI6y4Uzo7l3B-lFfymC0hPOnCZIgweJ1KiOkfuyMkeH6nSH9IpWIYwP9NnMaI2seCqHiavGoqQFM3OHGRih53qYjFpYDIAd1daN9lsOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای زیبای این پسر در مورد وضعیتی که برامون ساختن، ارزش اینو داره که ده بار گوش کنی و براش دست بزنی!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72539" target="_blank">📅 23:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72538">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Au2FuoN_eNcZhhtfGjbi-uLFCaYFBn2ObVuiNbBgU-twu7fUoWANATbjw5n339XWrWJnV9aRh5DjDmnpP3dhO4dtNqpkAJjpA5M2AJCYmrqDsnov50ZxA6nbDl7bIy65fU3DIOZaVMLtaLSrxBgwm5HEmw8R1ZmZNuARh4OZ2oQ40rEm-4o7nxZEUU8xtKwOiwLSkowmuJh5bOe_A3JXaz6zMdPZKiIZ0WwO0GUvyoriH2Yaf63WuzCS8uemj_lQfwo9Iapm9yfZuy24xOOUfo3YA9-o6GTPAw-g7N6zRJ8zi9mpr43TkAUn47jki87rK5F4C-jWO6jM3HUuvdew6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت بوئینگ با پیشی گرفتن از نورثروپ گرومن، برنده رقابت نیروی دریایی ایالات متحده برای پروژه F/A-XX شد؛ قراردادی به ارزش بیش از ۲۰ میلیارد دلار که به توسعه جنگنده نسل‌بعدی نیروی دریایی برای عملیات از روی ناوهای هواپیمابر اختصاص دارد.
انتظار می‌رود این هواپیما در دهه ۲۰۳۰ وارد خدمت شود و جایگزین جنگنده‌های F/A-18E/F سوپر هورنت و EA-18G گرولر گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72538" target="_blank">📅 22:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72537">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
ما تقریباً کنترل کامل تنگه هرمز را در اختیار داریم؛ البته باید بگویم کنترل کامل، اما هر از گاهی آن‌ها مین‌گذاری می‌کنند و اندکی در وضعیت اختلال ایجاد می‌کنند.
با این حال، ما عملاً کنترل کامل تنگه هرمز را در دست داریم.
در سه روز گذشته، حجم نفت عبوری از تنگه هرمز بیش از هر زمان دیگری در تاریخ این تنگه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72537" target="_blank">📅 21:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72536">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ درباره عراق: داریم با کله از آنجا بیرون می‌آییم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72536" target="_blank">📅 21:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72535">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88278c6cad.mp4?token=brnUk7YL9oFnYSBpsUX-JQJ_3NSEnRDT_8FlSBqf4hXMIRhjgdd1kH6mXewzs_Wn-s1PGg4E6XEgL9Jx0ugoa_kmX9tT-97adLn40GV5ODyFplUqddszBUTpJpPWK-E97D9DpQu-EkbJk6CfXn-jSHnbd4iCRPQlvPbvaw5yxew9ko8ON1eT80KmrooiGrxGlSE5dlJ_9O3OiXlVUTQt8mllQ-tbFrLfI_XL-1dfLebVDQb6U0BF80jhJKw-fhAZEZfmohZgepRixIP6NPocmJeljoMlr_GN8TW09ugKA325NOtZK84QxjP4mcwTkGY8NrnhN8Gkr9fWlT-MGxpQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88278c6cad.mp4?token=brnUk7YL9oFnYSBpsUX-JQJ_3NSEnRDT_8FlSBqf4hXMIRhjgdd1kH6mXewzs_Wn-s1PGg4E6XEgL9Jx0ugoa_kmX9tT-97adLn40GV5ODyFplUqddszBUTpJpPWK-E97D9DpQu-EkbJk6CfXn-jSHnbd4iCRPQlvPbvaw5yxew9ko8ON1eT80KmrooiGrxGlSE5dlJ_9O3OiXlVUTQt8mllQ-tbFrLfI_XL-1dfLebVDQb6U0BF80jhJKw-fhAZEZfmohZgepRixIP6NPocmJeljoMlr_GN8TW09ugKA325NOtZK84QxjP4mcwTkGY8NrnhN8Gkr9fWlT-MGxpQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فووری
؛ترامپ درباره ایران:
خیلی زود شاهد وقوع اتفاقاتی خواهید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72535" target="_blank">📅 21:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72534">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مَردی پنج ساله به بایدن فش می‌ده که چرا از افغانستان کشیده بیرون، الان خودش تمام نیروی نظامی آمریکا رو بعد ۲۳ سال از عراق خارج کرد
#hjAly</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72534" target="_blank">📅 21:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72533">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af74dbf4d.mp4?token=lnm-hr3dex-OnSFXl1z4afI6p5J1TyXituDlO2JxbhNiMQHYJ7-BiTYuJ5k7L79j3QSyTfQ6FHtfJ7UdQudAJRJLlpb03dZUrqUkIybxKsoCPI8KP9-cPLRuaXMProetL8KmC3VJb-vkXlcJvadavQSpFD2Y1DPnwCZ76mc9w5HMhQDs0Hw12fEFFSZnT52JvTXPoZ4prXQ2Nmg2t0zINmjkRp6X6NgB2GOaBA5aSTngddt2mTk3-SYcw3yeGrZH4HZ122LYK5nKSRmkjtY4FNJ_fxLR3K8LD6E79cRQ27BIu_QZAKAqRvEUHL6mHIBW1bV8VaTvAbEeMkXCOpuY7AoZlg3G-AQLjkkCuajb8b44mDltQdYcd-vnmrhaBdRc5b_sSHk4sBea4oh2G3_WFlc2v-bxLQTC-NEIeIocGzmBh-hYeMOfXGRXXM-DxI4WoaKJDOZQ0G2DGkfxJEdQjmTC3LkoxqV-c66B3-F5O1N2LxJ1lXhyXmDWJMjI4xAWNF1lMdgiEGD0tQPsURK3pt6qqh67cos_4YAuDynW2iCMANmFeJADHJA3qooFTUGxBRy4O06Sf0clkXvPFzVn-Cler3CvOtdc41YyH9QyeyXMgigGAWJ5-1QgruPjxt-mz4aOukOKnmfurrsxhk3yux7_eoBov2YB2u0sUsg2Teo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af74dbf4d.mp4?token=lnm-hr3dex-OnSFXl1z4afI6p5J1TyXituDlO2JxbhNiMQHYJ7-BiTYuJ5k7L79j3QSyTfQ6FHtfJ7UdQudAJRJLlpb03dZUrqUkIybxKsoCPI8KP9-cPLRuaXMProetL8KmC3VJb-vkXlcJvadavQSpFD2Y1DPnwCZ76mc9w5HMhQDs0Hw12fEFFSZnT52JvTXPoZ4prXQ2Nmg2t0zINmjkRp6X6NgB2GOaBA5aSTngddt2mTk3-SYcw3yeGrZH4HZ122LYK5nKSRmkjtY4FNJ_fxLR3K8LD6E79cRQ27BIu_QZAKAqRvEUHL6mHIBW1bV8VaTvAbEeMkXCOpuY7AoZlg3G-AQLjkkCuajb8b44mDltQdYcd-vnmrhaBdRc5b_sSHk4sBea4oh2G3_WFlc2v-bxLQTC-NEIeIocGzmBh-hYeMOfXGRXXM-DxI4WoaKJDOZQ0G2DGkfxJEdQjmTC3LkoxqV-c66B3-F5O1N2LxJ1lXhyXmDWJMjI4xAWNF1lMdgiEGD0tQPsURK3pt6qqh67cos_4YAuDynW2iCMANmFeJADHJA3qooFTUGxBRy4O06Sf0clkXvPFzVn-Cler3CvOtdc41YyH9QyeyXMgigGAWJ5-1QgruPjxt-mz4aOukOKnmfurrsxhk3yux7_eoBov2YB2u0sUsg2Teo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛
اندی برنهام نخست وزیر بریتانیا:
شواهد محکمی وجود دارد که نشان می‌دهد ایران در وقایع آخر هفته در پایگاه نیروی هوایی سلطنتی «فِیرفورد» (RAF Fairford) نقش داشته است.
در زمان مناسب توضیحات بیشتری ارائه خواهیم داد، اما می‌توانیم این باور خود را تأیید کنیم که ایران در این ماجرا نقش داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72533" target="_blank">📅 20:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72532">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">#فوری
؛کانال ۱۴:
بنیامین نتانیاهو نخست‌وزیر اسرائیل طی ساعات آینده با ترامپ تلفنی صحبت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72532" target="_blank">📅 20:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72531">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30841564f.mp4?token=Is9bJKBzLC8-Zn2IgQ1vpwv99B8HWRd26-MCw77vDMwpLr-NO1ebZeGj7_blEr2f7Z3mAQHkxvda_WH_olJ1UwKu_m4KAqV8d8E1-QlcBDPKEL6dQl23qMp60-JXE5RMrEvGawHi0YuwtTVxWy_jiR38k8psWMWlCmVOVYaTspZcgsWUbnQcNC0rq5okES2kYtcuDaIIL4YvCLlMfWGoITF54VEEsCisWkQPDaZjle3zLg_FM5PBpa0uC0585QebwLd8SO_jVl5cc4KH5HeBJBFjQFoNIDhq8fKH3OC9rEaXu95Zf_u-wswr8yETCoJwykiQdwrDf5UT9MQwRePCnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30841564f.mp4?token=Is9bJKBzLC8-Zn2IgQ1vpwv99B8HWRd26-MCw77vDMwpLr-NO1ebZeGj7_blEr2f7Z3mAQHkxvda_WH_olJ1UwKu_m4KAqV8d8E1-QlcBDPKEL6dQl23qMp60-JXE5RMrEvGawHi0YuwtTVxWy_jiR38k8psWMWlCmVOVYaTspZcgsWUbnQcNC0rq5okES2kYtcuDaIIL4YvCLlMfWGoITF54VEEsCisWkQPDaZjle3zLg_FM5PBpa0uC0585QebwLd8SO_jVl5cc4KH5HeBJBFjQFoNIDhq8fKH3OC9rEaXu95Zf_u-wswr8yETCoJwykiQdwrDf5UT9MQwRePCnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آشیانه‌های مرکز پشتیبانی لجستیکی شهید اثری‌نژاد نیروی دریایی سپاه پاسداران در شیراز، پس از عملیات خشم حماسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72531" target="_blank">📅 19:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72529">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_j4Gu0Zf7LtskrZx55OrumIQaQKD37oj7d5rivHciZOmGbgbQtlm1lr4QHLNfQvBkYJtSounr01urCS1PtpZ93xYbn7P3DzrgGznEvZM34MJgic2BTer5yDPaK4I1KNX04sKFRBBgrL_iHMHU3ZiGsi5lS0zWvyCWYRtVma6QqTGmtwRoADFU3BpbCNF32GC8gdcPiDBPjPcdY9JfDsDIGom5n1oGpcp0dshlB-T8heoAXw3klQWdZfXkhtAy_QC3jGA2VumhV4dXGxoF9v6h60AukQHhp9NUhmTc2g4xN9_IDebWL7B2SG9WmilvhYsiQ0IC2tGNDSl6Ehofnflw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAEPyOV-svJpLWDg05BPZ1nNrsXy1sUs5ru_y-0AIoyM5hU1bHrPVfCaB9BJOdh0X64w1DT1RKQZHhQ1qt6D8LQCTG9qMqMY5vghwfllPF-BKwlTGhJ4tBr3HTKJkvdpYYanKm71R8aXohnXh9LKKwxrNJbcQIg915m5BhC_JlRNm8F-iE5rRD8QiBiPRQK-PNJ0-sN3MNnnXiW-V4s668JxTayJlbIxvblW8qO1540UZo2ymra8TpbXAALSTOlnMDGNWwl4bRME3cBVs-IGPSAepaYhkz-PWrOy_CBOfPrNag-RO9lLCvqMn_Ggb8Sjg1FvTwMn5tf8v-XyYrItFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرتاب موشک از استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72529" target="_blank">📅 18:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72528">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو درباره حادثه پرواز دبی:
«یکی از خلبانان، خلبان دیگر را با چاقو مجروح کرد و ظاهراً تلاش داشت هواپیما را به همراه سرنشینانش سرنگون کند.
هواپیما وارد حالت چرخش شد و شروع به سقوط کرد. یک مسافر اسرائیلی و یکی از اعضای خدمه وارد کابین خلبان شدند و خلبان مهاجم را خنثی کردند.
یکی دیگر از اعضای خدمه پرواز نیز موفق شد هواپیما را به حالت پایدار بازگرداند و از وقوع یک فاجعه بزرگ جلوگیری شد.
خلبان مهاجم هم‌اکنون توسط مقامات سعودی مورد بازجویی قرار دارد.
به دستگاه‌های امنیتی دستور داده‌ام برای مقابله با تهدیدهای احتمالی دیگر آماده باشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72528" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72527">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72527" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72527" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72526">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHm7XL9nnPsVmCWmmg-QsorQJx3Hz0uK5NiW9gXjIeS_1X2CnmSWX7qK0auv7EjIxotAmRluuGpGFsrIcdcyATmUIW0ffr9CZQg4oB8eNaB_lVzlmtYH_tOaonl2nVJYt7s4ZGZtCQpNUDGsqRJLXiOhaOgGL7kZws_DOZ0ncjKYNYyYvji_09bYYgDV4xGuw6NhvpHVCMTEIEL7A2dG-oA6RISLKJ9vCBQX3tbT-TpA5kUfygp7bflNCTgH8imr7Qyp48lDR98stwwVhVfZKG8Rd8cOXC7xgRxx9qknjr-ZicbBrpVko_YjPTvM_PvS4v4yW78GFADpioZVwQK_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72526" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72525">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fbae6ebe2.mp4?token=vjNVBbll3X3Yyc_kS2s9rldGIMGgm5D_w-axCohhsbAfaSKkT-mn80-j6uLHl1uSnJakuwNJHTjDIecVzx-zf_bdzji0WFAl811ehTYKy_9FcWAPqSm8eeC07LCM6Uf1GHcDwO4i4F5LcGSfjPI8yfWw5MG0lP-bp7Us5wCagABe40xe6M-k0V5KwZsyqQtAmjz44EA4bcZNXwSIg2HX7hYMHFGJZ6vlZO8UwyeL3th3oSCSpyuXZsZD1p-tgxcSeOXPcFZHBAelVIFaFoHfvMOtcGB2qF_kfQ1QicIy_9VT5Y0UTD-ypXxMmP132p1SSbjBaf4e_U8QWiK7iSvZWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fbae6ebe2.mp4?token=vjNVBbll3X3Yyc_kS2s9rldGIMGgm5D_w-axCohhsbAfaSKkT-mn80-j6uLHl1uSnJakuwNJHTjDIecVzx-zf_bdzji0WFAl811ehTYKy_9FcWAPqSm8eeC07LCM6Uf1GHcDwO4i4F5LcGSfjPI8yfWw5MG0lP-bp7Us5wCagABe40xe6M-k0V5KwZsyqQtAmjz44EA4bcZNXwSIg2HX7hYMHFGJZ6vlZO8UwyeL3th3oSCSpyuXZsZD1p-tgxcSeOXPcFZHBAelVIFaFoHfvMOtcGB2qF_kfQ1QicIy_9VT5Y0UTD-ypXxMmP132p1SSbjBaf4e_U8QWiK7iSvZWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏عاقبت لایی کشیدن در نهایت همینه؛
ممکنه چند بار تو رانندگی از روی دست فرمون خوبتون موانع رو رد کنین، ولی بالاخره یه روزی میرسه که ممکنه یه همچین صحنه‌ای برات رقم بخوره...
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72525" target="_blank">📅 18:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72524">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8caf88eae.mp4?token=JmJGNvvzdvqkZ0HCyxxDJmtCKopblhhCo8UW1qNRP9z4d1RPEk3ZKjarqSwfgfpcCQxRKXKQ5_ZWBg5_fiUeeui15ZHjAmD_h1ikaeCmofTnUpsJai2FOmAkMhsheGb-pzYAGfgWtCpPFTD7PY5mQ09bzO5C4asyxBUvQg52LgBQ6Y0y09gcsKuXsDMGZUbfyEU2zhLh1j6-iQ6iJ3ya_3uaFz2JWO7057GRtTycAHrWYjCP7LcLVM-119vSEtjXsJec9MnpIH6OQwE-tTOcx5JOblsynle-4phQmM1Ll3NrzJ6YyIMShkVjGIt0xpn4Tq_rKrFMjOuKHdTMexaCCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8caf88eae.mp4?token=JmJGNvvzdvqkZ0HCyxxDJmtCKopblhhCo8UW1qNRP9z4d1RPEk3ZKjarqSwfgfpcCQxRKXKQ5_ZWBg5_fiUeeui15ZHjAmD_h1ikaeCmofTnUpsJai2FOmAkMhsheGb-pzYAGfgWtCpPFTD7PY5mQ09bzO5C4asyxBUvQg52LgBQ6Y0y09gcsKuXsDMGZUbfyEU2zhLh1j6-iQ6iJ3ya_3uaFz2JWO7057GRtTycAHrWYjCP7LcLVM-119vSEtjXsJec9MnpIH6OQwE-tTOcx5JOblsynle-4phQmM1Ll3NrzJ6YyIMShkVjGIt0xpn4Tq_rKrFMjOuKHdTMexaCCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ بعد از دیدن این کلیپ تمام ناوگان های دریایی شو جمع کرد و دستور داد همه برگردن امریکا
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72524" target="_blank">📅 17:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72523">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f862c5d3f.mp4?token=sAjiR580KxdAByKp0IvRs42H5YfxjzyBaOa5EDwP0wctTcLMD52qFd1hzCZGWUlatHZ7cY7f8fmnkvSLXmVaZEGmHDjI7JWVLvsHtoMYvZ5d3UTCZ9vGfVq1Z5ybPy5Yzx2YCJt3bRjzZwK0_gqB7Wzj2V7JJeCjZloZ1pnEXLUp8Qt7Nw-Wye_qAVxH8sQtc1UxpM1HsAKjkKyNmLu2D1eqjKRz5JQy4Z2o-Rahhl5s7l7eIyF4H5m5oKVLtYaDycm3STa5tHDeeXs2pA8Up2T-MHQSHF3drOrrfeQ3RKfPtre-FFJ26QHdrNGfkzgRclqP4CjiVUgI2onqVBjPOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f862c5d3f.mp4?token=sAjiR580KxdAByKp0IvRs42H5YfxjzyBaOa5EDwP0wctTcLMD52qFd1hzCZGWUlatHZ7cY7f8fmnkvSLXmVaZEGmHDjI7JWVLvsHtoMYvZ5d3UTCZ9vGfVq1Z5ybPy5Yzx2YCJt3bRjzZwK0_gqB7Wzj2V7JJeCjZloZ1pnEXLUp8Qt7Nw-Wye_qAVxH8sQtc1UxpM1HsAKjkKyNmLu2D1eqjKRz5JQy4Z2o-Rahhl5s7l7eIyF4H5m5oKVLtYaDycm3STa5tHDeeXs2pA8Up2T-MHQSHF3drOrrfeQ3RKfPtre-FFJ26QHdrNGfkzgRclqP4CjiVUgI2onqVBjPOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر بچه دهه نودی با اجرای رپ خیابونی، این شکلی کلی مخ زد و از دخترا شماره گرفت و بوسش کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72523" target="_blank">📅 16:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72519">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU0I0PmohANqvIbsAQ5bSKIWJRqmwARU2r516hbF4uv343tAjGGSq70rSOCAEc7Bx44BF_AEiBdvxpO_E8b0gpOhfv9QQQarhWk1Y2d2cuB49oy7v-n7dWCv36VbCI5dtgHcrQ4Wjb6OnQTp0OkUbX1XIHQ4em5K7dr6ixSkQvYyfcIdQGWjb8P3Tloc72__KkR79U8mK5aHVnKlPsUh0nI9CY6wOML99Kl05KDa7AnfEcihyw1ykDfbZzpbrBbJ0CW6iohbetEKBNpyvodbA48Pf7vFc4DvULsVLsIzqvxthC5BouiqFGTldnUJvgYyD4ut01fWr40c-GZejIwQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/670f963d1a.mp4?token=hHWRTllMIvUBqievFxyF88FaErs-amH0lKtTvYklHfk3t0Y41ry7LT76gKEIiVqvfK7ovOHvPlhzg5RB5xk7crHsVtUyVFzBEk-PGjYE7x0qmjGZcW9qNPP243L5vb6J-t2VaCqjMw4u3RRUsLL2phod2KpXIbG5cWClB1an3lkq36Hn_w3kgBRVaUUu-3_b6T6lVSoW2RWXS16L90-Z0joJcwl5jGk8x_-E0OXvIFLis5Y4eodpexXkapnjAwTw1CLYoGHCtJiOeGMc84jhh8qthIo1aWejJooF_SMsYlLaIWGeGevmeNdwhcGRkCzvsI03jg3OOc5asMz2VsWM_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/670f963d1a.mp4?token=hHWRTllMIvUBqievFxyF88FaErs-amH0lKtTvYklHfk3t0Y41ry7LT76gKEIiVqvfK7ovOHvPlhzg5RB5xk7crHsVtUyVFzBEk-PGjYE7x0qmjGZcW9qNPP243L5vb6J-t2VaCqjMw4u3RRUsLL2phod2KpXIbG5cWClB1an3lkq36Hn_w3kgBRVaUUu-3_b6T6lVSoW2RWXS16L90-Z0joJcwl5jGk8x_-E0OXvIFLis5Y4eodpexXkapnjAwTw1CLYoGHCtJiOeGMc84jhh8qthIo1aWejJooF_SMsYlLaIWGeGevmeNdwhcGRkCzvsI03jg3OOc5asMz2VsWM_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بمب‌افکن استراتژیک روسی از نوع Tu-95MS در جریان یک پرواز آموزشی در منطقه «آمور» سقوط کرد.
این هواپیما حامل چهار خدمه و سه سرنشین دیگر بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72519" target="_blank">📅 15:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72516">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZpAOKyYtnoGAG5gM0WksyRkQ-Zbbc7j3DAAohFyr9MagvX7dc1wVdVmotbfIHQ7QobHZzP2KHd5ulAtSs8-b76hheok895pjn4xUYq8I7ZSQTaUex9MLcngoZaTu5vJZXFXgVtGEbyPzyghLZV2-VcaV5Qy3i1DTv9-OEKBRZKkjdrHXIn3bL9tNibslvxBA_PolOr_4uheOs3SN5iU3FFmABsNUbC-glzUrJuri5AIc14jlZo7DF7n9ghSPc9s4ioFnRGOi-us1WRkeGpXeFSxwjQ-VwP41aVYbGGiuxFaFN0UwgO3kPORm7rWWjKgAE96N2eWWkpPsM33bN5l2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Khg0K2Imm2hBIaV0QvsrhlVioylh2az_-m4iTVYGFCkUbmaFkqmyrE-P7T9_u6Oy_ECLQSeqKPV7MZ6kXZ8-zRsR-ublmIXc7K7BYNLXKh2uyc2PmN57rPZdEEO80w_gbsjNIRV-psWkehCLK3J69KA1iZH4fMQM258bz4tHcMJ-KRqRf_EyKavkl7jb5vgFaV2x6jY7SdJV8w1V8ETsIqEKlU4kOxqvYjSvjrLigRjdpoLW0BL6h8b_7E70jRncxFBWcoHpVgAccjEpGn8528dgsyMd0F0P8kKuJQcXKNkNryc5kP_-ZfhsNEYH2LgElO7RrNtkisY8ePFbFj9NRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VeeYMsf8VBHfXn_ov6eGXdUkc9kEySH88i9juXIMHZAQlpZF7K-uAwX_4RUdxlYeTNd88GEBxNwDNTJXM0Ij4Pya0KK7ar_YeSAve4rvomY6SuPqHiv2WiQBMYR49kZ5qfJV06bJkw1oJlLPV7fT0Juzm6EHED-uG1a8Jr6Wq7MYogKuP2N9XV9OPwn9P0bnZPXYxL7eGcbZm3T9JraFXCjjh2QUImv4OkzObbspl-9BjMHkVu4p0cH-yApKw320XbuCAaI6RFx3goA4_tt8j7E29SpjOr65BJziaR-UR9cRhyQ1K0Fedk__8Mpp9OeJqRPwlFukB95BoTwKvCcXlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنا بر گزارش UKMTO، سپاه پاسداران امروز به ۳ نفت‌کش و کشتی حمل گاز در تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72516" target="_blank">📅 15:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72515">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4993b45c70.mp4?token=k3PMURuQAd2PyT9Jc3UWFt3fLzPERgaW0cLjjpmAOh7IKywfIAf1nKDmlO4-YK4gjzWkwDabRJPpMioqJZAd03CQJi-pmcXSDXLQ15aLLsny03_W6WpOen7FB5sIk_n6zEHvASzGHTsPZHfU4Zpl8rf4cmkaMef5yZ2lNu7s_1PFkMesn-rAQN8GZ3B8tBcizTEOvn9CDl-Y7igROPvPpFcCadtyRdyvmXTXtBzobmHF4Fs31iyYz6WaTpSjQXY18Yv6dy_-O7-6RWiFXLIriokEVbuzpl8yEJkM4Lrr2s4UAn69UoG_L-gRdvDk8Rw3qoveJF8F3VcwFgF6WI-KjZn0t9sajGPr_2FEJwO_a9fDC2Df5yqBUtMFbFjeJo75jc0zeKKyhKSaAbQTcytnblbh632YGyOWaQvJfU7URqIe1sdSQpj0eXZYGwIiwOu3voTxIeXiIwD2kxvquDWi8Y-kpnX8g70AH9QoG7vDI8i_J9ObrfWkNzkoSN2EGsOJUF5tycR-VV2FKjZTThfpjM9OxxZQCacBBn_uS7JfP6UbN1sn2J0YZVMUZnePutZDUFosd9b9twYG2J6rOUBG5Uz_ayRgJNHEv3X2cnwKNwr1slI8iPNO82BfmT7Mer4Isjdp-wG1vglRI4V9u_f4KkRiT3uLo4BzU5aDDomHSD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4993b45c70.mp4?token=k3PMURuQAd2PyT9Jc3UWFt3fLzPERgaW0cLjjpmAOh7IKywfIAf1nKDmlO4-YK4gjzWkwDabRJPpMioqJZAd03CQJi-pmcXSDXLQ15aLLsny03_W6WpOen7FB5sIk_n6zEHvASzGHTsPZHfU4Zpl8rf4cmkaMef5yZ2lNu7s_1PFkMesn-rAQN8GZ3B8tBcizTEOvn9CDl-Y7igROPvPpFcCadtyRdyvmXTXtBzobmHF4Fs31iyYz6WaTpSjQXY18Yv6dy_-O7-6RWiFXLIriokEVbuzpl8yEJkM4Lrr2s4UAn69UoG_L-gRdvDk8Rw3qoveJF8F3VcwFgF6WI-KjZn0t9sajGPr_2FEJwO_a9fDC2Df5yqBUtMFbFjeJo75jc0zeKKyhKSaAbQTcytnblbh632YGyOWaQvJfU7URqIe1sdSQpj0eXZYGwIiwOu3voTxIeXiIwD2kxvquDWi8Y-kpnX8g70AH9QoG7vDI8i_J9ObrfWkNzkoSN2EGsOJUF5tycR-VV2FKjZTThfpjM9OxxZQCacBBn_uS7JfP6UbN1sn2J0YZVMUZnePutZDUFosd9b9twYG2J6rOUBG5Uz_ayRgJNHEv3X2cnwKNwr1slI8iPNO82BfmT7Mer4Isjdp-wG1vglRI4V9u_f4KkRiT3uLo4BzU5aDDomHSD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که هواپیمای فلای‌دبی دچار سقوط ناگهانی شد و به سرعت ارتفاعشو از دست داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72515" target="_blank">📅 15:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72514">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8d2f0129c5.mp4?token=GY5DaTYDmbStxDc3XDBZdf0hp4khtWFCzrPEWrTS5YvxJ4Uw1ucl7s8qE7dH4WjoU-UI5UM2t7J2c5V7gNH2-6erOkuVVwBbvMwOynfdZwDWrO9SqFD1mcqYZTDSMVsu8ErGuV1pe9uGh_f1f6OkS1HAzKjFh_NugAr5dWv18GML2yYR3-Nw-d74quZKKbWoUtGDeywDl2q9L4g6uCLL73EknohlHQ4XWwa3SeJ5s5eY0LUYaweYFVTA8Y9UTroC4daNFoFy57Yn46O1LgyaP5xKLBhiwkN4fXYa8sekdBAjJXsMi9PB9CfGRs2m-lOz1uvoeG6tBbrSIUPkOhgQQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8d2f0129c5.mp4?token=GY5DaTYDmbStxDc3XDBZdf0hp4khtWFCzrPEWrTS5YvxJ4Uw1ucl7s8qE7dH4WjoU-UI5UM2t7J2c5V7gNH2-6erOkuVVwBbvMwOynfdZwDWrO9SqFD1mcqYZTDSMVsu8ErGuV1pe9uGh_f1f6OkS1HAzKjFh_NugAr5dWv18GML2yYR3-Nw-d74quZKKbWoUtGDeywDl2q9L4g6uCLL73EknohlHQ4XWwa3SeJ5s5eY0LUYaweYFVTA8Y9UTroC4daNFoFy57Yn46O1LgyaP5xKLBhiwkN4fXYa8sekdBAjJXsMi9PB9CfGRs2m-lOz1uvoeG6tBbrSIUPkOhgQQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این موزیک به اسم «مفقود» در مورد مجتبی خامنه‌ای، فقط تو چند ساعت بازدیدش میلیونی شده
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72514" target="_blank">📅 14:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72513">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آی‌۲۴نیوز:ارزیابی‌های اولیه حاکی از آن است که خلبانِ عاملِ حمله با چاقو در پرواز FZ1073، تبعه عمان بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72513" target="_blank">📅 14:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72512">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqeQX_qGhC0s9Q6e-mrKULPcq5afOdsyrqmVO2dLUpaXCOwoiJaTI9HH7khvcJX_qygF3u2N-o-hU9o7iiICV5ZlOuU2xfhSJ_lwciDaW1WgYhqJvUvTB9zqgmCYJ83Ii_KYNkYq3a0d-Tj2Eagdde_kqyWC5XN-WWY03mZr11HTZYV_bpyy73OD7zPPcmdBjwo3gwGRkj42Lc9mHa4Wxhkc-oybunUkw5bf8_dhv8CppF40hdHdy6KjJIY9uvwM77XeatB75VX4E2hlGbAugc1TfVVPXcMNG39svj_MDkOg7Rmn8j9T5jG4Y3YisaA5ONrtMyBoSQwb_DGSdacGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو اول تصاویری دلهره‌آور از داخل پرواز «فلای‌دبی» از دبی به تل‌آویو که ناگهان تا ارتفاع ۱۵ هزار پایی سقوط کرد، وحشت و هراس مسافران را نشان می‌دهد</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72512" target="_blank">📅 14:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72511">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8284df28.mp4?token=UZfomc4ZRff-Q1iPFWGLRvImQsvTT9q_pZ9tFMAF38yuu9hU14_JahFOT19qwMSGsncwTj7kiQvjm877_qGKFqRyvs606FV-NrGsjv2WZYitYSbq3yVQQHVsYOZX0JT6QwX-zgZCAaLlzPXVclMQByYGsh6gz1wTRr-JtSCflbZMdK2Iq9nRmoArkQ9_lpcjBO9wpO3lML1RA50MBnO4Rlqjx6jXpnAQBnjjYizKNvXiWwtNd7FXIWD6p0PuVnmb7AyfMmkemmAdfh0vZS5amXvJyUwH0AUu2HT7aGhcCK3hl1RixV1hgtj9bkxKhe9gtUFUddMjyTLeS3kQ0QGb6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8284df28.mp4?token=UZfomc4ZRff-Q1iPFWGLRvImQsvTT9q_pZ9tFMAF38yuu9hU14_JahFOT19qwMSGsncwTj7kiQvjm877_qGKFqRyvs606FV-NrGsjv2WZYitYSbq3yVQQHVsYOZX0JT6QwX-zgZCAaLlzPXVclMQByYGsh6gz1wTRr-JtSCflbZMdK2Iq9nRmoArkQ9_lpcjBO9wpO3lML1RA50MBnO4Rlqjx6jXpnAQBnjjYizKNvXiWwtNd7FXIWD6p0PuVnmb7AyfMmkemmAdfh0vZS5amXvJyUwH0AUu2HT7aGhcCK3hl1RixV1hgtj9bkxKhe9gtUFUddMjyTLeS3kQ0QGb6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌های غیررسمی؛
علت حادثه پرواز «فلای‌دبی»، مشاجره‌ای میان خلبان و کمک‌خلبان بود که به درگیری فیزیکی و ضربات چاقو کشیده شد.
خلبان تبعه روسیه و کمک‌خلبان تبعه اوکراین بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72511" target="_blank">📅 13:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72509">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f8e2c2fd.mp4?token=DoWM0RPIG6VWLdLJAc_3ku3oG5lyvIbYLEfrR6BpDdi-Mu2ZGQBv_yg8hnZhK-Cfzd1xB_4GpEoAUT_R3kFqXrUUw5ZqGHp8C8D2glovPMRdtyChKNKCnGwmXSewyem9FP6osbn6JgMGBY5VEG72Zm93_rHrJK9sf0hYzQ5Y7nuwh8A573B6uOn0tPP0Ta-Kr3gjzAQxbxGlxlzqjDG0Zc59oEdaDC8EJnw4TLGNdSr3lVJ462JYtBzAKvUgdFhT_cKuwySlTZnZQZ76WKa1VlebA6_PDz2GmnMBQzLVUoMsBPFpSdBrvZtGM5cE1ypRL58e6Y25SSuPyOVNQaJY7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f8e2c2fd.mp4?token=DoWM0RPIG6VWLdLJAc_3ku3oG5lyvIbYLEfrR6BpDdi-Mu2ZGQBv_yg8hnZhK-Cfzd1xB_4GpEoAUT_R3kFqXrUUw5ZqGHp8C8D2glovPMRdtyChKNKCnGwmXSewyem9FP6osbn6JgMGBY5VEG72Zm93_rHrJK9sf0hYzQ5Y7nuwh8A573B6uOn0tPP0Ta-Kr3gjzAQxbxGlxlzqjDG0Zc59oEdaDC8EJnw4TLGNdSr3lVJ462JYtBzAKvUgdFhT_cKuwySlTZnZQZ76WKa1VlebA6_PDz2GmnMBQzLVUoMsBPFpSdBrvZtGM5cE1ypRL58e6Y25SSuPyOVNQaJY7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو اول تصاویری دلهره‌آور از داخل پرواز «فلای‌دبی» از دبی به تل‌آویو که ناگهان تا ارتفاع ۱۵ هزار پایی سقوط کرد، وحشت و هراس مسافران را نشان می‌دهد
ویدیو دوم مربوط به فرود اضطراری پرواز «فلای‌دبی» در تبوک، مسافران اسرائیلی را نشان می‌دهد که پس از فرود ایمن، سرود «اُد آوینو های» (به معنای «پدر ما همچنان زنده است»؛ سرودی یهودی درباره ایمان و بقا) را می‌خوانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72509" target="_blank">📅 13:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72507">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlHM44D_nAS-Zf1gr-Un00M6aLAIHMudrSi8gHd9jZM8a9a-x0DbcVR9-0mg5HdJoh8-iBJ4PBwxDZ-hVGzEPZrL84Ov5ShI05FTeuB7nUUKTFjJyTVD86Y2Ql0Ydy7p1DT6fbAnva4Ssp7ePVAa2EjLu8ttB4nDIgZbDlfOXHYENE54nkx-2Xbe8HOaSHLlgs0yA1cpHwsMa7R_BmL4AnbLdvLVBaXjDbN8djKJUtX5LbpU5tOvwgjoK6rZQlRrH7W1FhObTLrOz30UtsycyH1On2KyRXVvrBADz0cL23jilw6XR5S0UouEc8wP98hUp9uxzRHh2Ziluj89wUgW9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d0fY1FWSWKK4yE6WWl7q3GpegZ4xHXXyTUqNX_OGPLNKxdzMgEQpElAQpF2FLpGjvljiV84d9zqQXNx89AE4JvgjyMgkWeMWqExnxH44ApaOyPGg5XfqK0uWjKjbDHm_49OePLD08gjBEM_bgQDb9u7GUI83oLAkxNrHv02Bp9NvtH_X7RPmWRIUopemDu5gDtJdZ-IlfLwqHMhDaRvD73NI6QKtVA79LEAlgMpsSFz5poiG1CFa3K188stJMqOXg4RUg-APxEqrOOdtK99rwXzWSPkZnB7umwIjzOaiBxgEA_rQcRude2R2kS_9Kli7uBICFN6Ehqe6WDKnBjUsVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حادثه در پرواز فلای‌دبی؛ فرود اضطراری در عربستان
پرواز FZ1073 فلای‌دبی از دبی به مقصد تل‌آویو، امروز پس از وقوع حادثه‌ای در میانه پرواز، مسیر خود را تغییر داد و در فرودگاه تبوک عربستان سعودی به‌سلامت فرود آمد.
این هواپیما در جریان پرواز کدهای اضطراری ۷۷۰۰ و ۷۵۰۰ را ارسال کرد. کد ۷۵۰۰ نشان‌دهنده احتمال «مداخله غیرقانونی/هواپیما ربایی» است و باعث واکنش امنیتی شد.
بر اساس گزارش رویترز، یک مقام اسرائیلی گفت این هشدارها پس از درگیری فیزیکی میان دو خلبان ارسال شده است. با این حال، فلای‌دبی تاکنون تنها وقوع یک «حادثه» را تأیید کرده و جزئیات بیشتری درباره علت آن ارائه نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72507" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72506">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4587e16a26.mp4?token=E-3_HhLlrsr6z2KUcyLc4zKteDzEENqBuja7aPpIzN4WweGj91sp9QZlrK13qDqJP4u9ob1evTJqdASYk3j3e47Q0zuBxqvo6Zvr_w7M-krcgdS1RMf4u59VPey1UtLV6o3UNGopcVF2OtBjCTSM0CQN7pQz_VzHoUjVzioIxmm_BAk5cDdB_iCnrv2gYjKgqS8iHOiPdU7t0eKaFmgsh6-3qSmxmCQlOuGQbmFfNtp0Y2BAiDCbltB6Icz7DROWcCfCqAvg1vngRDc2U2qsGx04CEF9V8GkmdEQzSVa54qGsNqbiy5M9GICBUK6I8mMhW9aQon1Ok0mjIGjfG8T6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4587e16a26.mp4?token=E-3_HhLlrsr6z2KUcyLc4zKteDzEENqBuja7aPpIzN4WweGj91sp9QZlrK13qDqJP4u9ob1evTJqdASYk3j3e47Q0zuBxqvo6Zvr_w7M-krcgdS1RMf4u59VPey1UtLV6o3UNGopcVF2OtBjCTSM0CQN7pQz_VzHoUjVzioIxmm_BAk5cDdB_iCnrv2gYjKgqS8iHOiPdU7t0eKaFmgsh6-3qSmxmCQlOuGQbmFfNtp0Y2BAiDCbltB6Icz7DROWcCfCqAvg1vngRDc2U2qsGx04CEF9V8GkmdEQzSVa54qGsNqbiy5M9GICBUK6I8mMhW9aQon1Ok0mjIGjfG8T6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۱۸ ساله به جای اینکه امسال اول مهر بره مدرسه و درس بخونه، با یه پسر پولدار ازدواج کرد و رفت خونه بخت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72506" target="_blank">📅 12:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72505">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBOKBlaJtwo64Zrk4aFRD1Juc5vkIgAb0PbOrajkb9hPjR8bUtcRtGTaYqw4EG5Xjf3LmC1QOcYVOCAaiM0rGalTrxvb_R9eM8f7GT-GI9Z3jJqEionFdoI3PgL3ajHJM3QvJOL_cgBTBPh9E38Enf3ZjURgxL3ecn0XSHZYJo8LJEFkDWcPVnsjkdIiT01QnYpuFvZnj8mnzuCD_ThAuoGCCYbffIRhG9-I77KlFjx1_3JV72KCj8kNj4_HQBRpQCBp-RTI6HhfqIyc1dzIS28LYb8yMSn9MQKBug8LEk_4DOp6HAKt8jVYNPMn2NoDCl-BzpYr7-RxDQLWkFHuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده و شرکای ائتلاف پس از ۱۲ سال، با خروج نیروها و تجهیزات از پایگاه هوایی اربیل، رسماً به «عملیات عزم راسخ» (Operation Inherent Resolve) در عراق پایان دادند.
پنتاگون اعلام کرد که از این پس نیروهای عراقی مسئولیت اصلی تأمین امنیت و سرکوب بقایای داعش را بر عهده خواهند داشت، در حالی که ایالات متحده به ارائه آموزش‌های هدفمند و پشتیبانی اطلاعاتی ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72505" target="_blank">📅 11:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72504">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4XftmtaSgGl7LbT6QJJdzmWZWEgozdhGc9h2hbKIOq5ZX13s2Mg0AHD5_PfvWJijRJ97YuPP3ufA5VgWPRJ9CUOoTEyhbdBLdQA3HE9Ic3bhFuW_2jBzPm1HYGJ6f_53X66W1ATlOkcrDA8aNQO2v2tpJRrs0rhuIVr7r9pXbzKCN2gdMIXkzxICy5sUWP-4uCThWBPclfzUCYOy6gvogvvm_Hkd4B7WPyLQ1SkyyQTNfuGaDpOYgtnqs4UYO9LYpq2IisRzLVRQQHtqPeo9eRNhQZX_aTblpLB8PQtalnWM7DpefErJYw84ZPPl2tBC23UBgoI-WuL_h1h9hte2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اطلاعات اطلاعاتی جدیدی را به شیخ محمد بن زاید، رئیس امارات متحده عربی، ارائه کرد که نشان می‌دهد ایران در برنامه هسته‌ای خود پیشرفت‌های تازه‌ای داشته است.
این اطلاعات شامل جزئیاتی درباره ساخت‌وسازهای جدید در تأسیسات «کوه پیک‌اکس» (Pickaxe Mountain) بود.
یک مقام ارشد امنیتی سعودی نیز در این نشستِ گسترده حضور داشت. گفتگوها همچنین تحولات منطقه‌ای مرتبط با حوثی‌های یمن، باب‌المندب و تنگه هرمز را در بر می‌گرفت.
نتانیاهو همچنین به حاضران گفت که ارزیابی اسرائیل حاکی از احتمال انجام یک حمله منطقه‌ای از سوی ایران در هفته‌های پیش‌رو است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72504" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72503">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72503" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72502">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1Fzsj7YkdZsUtMK4lkYemhPxdaSuh-Bv79655MCcdYkQgFvkf3Uibdur0VycU8SoncMi8pJq_rt3YB7vY92jZZAU3ae6XYcqvhlfu61kEduIGPBOrb42ULrXCsHCXUoeZuOyd922deGfay5MP8T29EtyGDUsDuq7738yXVc5dCblanY6_NJjEsqgqKVRtlHOWHTk8xg58CbGuv7jwmfzIddXRLHXyIESNTZOef6zVxDaHf-41mY0HjSMcvG55Sz89vLBQo6ZpMuXW1Ag4VUsrEdL6LQGQLs4uVkh2F489D3WeeeBPSsjm7vFqWAbZbW0qfDvHEokExUiwFQDbnw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط ۴ روز تا انفجار در قفس
🦖
​ناتالیا سیلویا در مقابل وانگ کونگ
جنگ سرعت و تکنیک؛ چه کسی قهرمان جدید
UFC
می‌شود؟
🦖
​شانس‌ات را در
TrexBet
امتحان کن و روی قهرمانت شرط ببند!
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72502" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72501">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58cfa5fb8d.mp4?token=ZYlDWYuz1kbNjzmYJfVUSYlepZjYyWtaVdJcKU89_HomuX7F2kSlJOrdQ8Mb-TSoEFD1t5r8Iq8MViwa-8VXBlJXNaXK5i-6fpwfRHvOgIPsA_hiDqKPqLqf6QqmVm9PBsMRjcXf612Xe-uA9y2nDk-WBteOHMlmQqp-FEv6gOdU9cG47PWiCOyQ14NL1DPGbvYPwjgr_8B6ATS0GYbUew0fR_GUaRIonKZ3nwB6ZAXfUg-sfOJkRE50kh-krXIpVXbbdPSeP4PIrQ24StLRLcHBiqGxKrXBaobjKKIo2QW6zWYQg7InCm0_uH2lHqjMyA0J-X__nbwjYLEmaUoHRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58cfa5fb8d.mp4?token=ZYlDWYuz1kbNjzmYJfVUSYlepZjYyWtaVdJcKU89_HomuX7F2kSlJOrdQ8Mb-TSoEFD1t5r8Iq8MViwa-8VXBlJXNaXK5i-6fpwfRHvOgIPsA_hiDqKPqLqf6QqmVm9PBsMRjcXf612Xe-uA9y2nDk-WBteOHMlmQqp-FEv6gOdU9cG47PWiCOyQ14NL1DPGbvYPwjgr_8B6ATS0GYbUew0fR_GUaRIonKZ3nwB6ZAXfUg-sfOJkRE50kh-krXIpVXbbdPSeP4PIrQ24StLRLcHBiqGxKrXBaobjKKIo2QW6zWYQg7InCm0_uH2lHqjMyA0J-X__nbwjYLEmaUoHRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان:محبوبیتی بین مردم ندارم و هرشب کابوس میبینم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72501" target="_blank">📅 10:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72500">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2b6a15d8.mp4?token=IJK7vSA_7axUWcqSOdkW3AZz0YRyugw9D9ACxv6pmVJT7Yu7oKM8KvkpInrlhl0yIcGKuin0Q-koMSKO7YKe-DOkUCfZfSKT-RldvkKf6ZB1HDdMlmaL1u9vGIHXyjUCUtGD8EgtG86n4Yuh1kn0AfymceFOOyDo1e7EoDMW85vdz4Tn23vWDKpigrz16NDHb_ZCbSzEqjYstnJeW3Ds-VxL2m9oAT_1QezKbmmShkdKEJmaxxKFD9_85_bcvUcAZaYLoT9gGJfMRCNU2uDgrupk9oTdbKHHeh8wmEt1-ATWaHPMwmNoumhMD5D2IY5YJ_DI01Mytk48wZZ6kwosmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2b6a15d8.mp4?token=IJK7vSA_7axUWcqSOdkW3AZz0YRyugw9D9ACxv6pmVJT7Yu7oKM8KvkpInrlhl0yIcGKuin0Q-koMSKO7YKe-DOkUCfZfSKT-RldvkKf6ZB1HDdMlmaL1u9vGIHXyjUCUtGD8EgtG86n4Yuh1kn0AfymceFOOyDo1e7EoDMW85vdz4Tn23vWDKpigrz16NDHb_ZCbSzEqjYstnJeW3Ds-VxL2m9oAT_1QezKbmmShkdKEJmaxxKFD9_85_bcvUcAZaYLoT9gGJfMRCNU2uDgrupk9oTdbKHHeh8wmEt1-ATWaHPMwmNoumhMD5D2IY5YJ_DI01Mytk48wZZ6kwosmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی یکی از مراسم‌های عروسی در ایران، عروس یه دفعه تفنگ رو برداشت و این شکلی پشت هم شلیک می‌کرد!
از نگاه‌های داماد معلومه ریده به خودش ولی کمکی از دست کسی برنمیاد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72500" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72499">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc8901fca1.mp4?token=NgflDjRRFgU245lEBEwe7zEoRwy4nG6KW0QC8bSEePR9ocWISElh_CE8rkn2WdiSZ1BH0RsM5kw2cger4vQGdHlvbu9uvgtI4diS2m0UlYu_e0d-rLa-gSMjtCmHdsbNZWKhyseKHttDWhhQATaXMj8vVfaDGVnBlde8ET-1FmbEosOH5HN5LnR9GUpXZRIaz_qnKn-Ni3Vq1gpYX9fLXde2rQFptm0Q65UvnK2F2-3l0_1cUUkrLemk7jZCi7_xaWwJjAQLOu7ryys5-ActxZVOMCJvGOE67Uw7QLC33sVB_0W0eyvTeBOc_6E8EPRat1PBMn74LreB6emm4z0fTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc8901fca1.mp4?token=NgflDjRRFgU245lEBEwe7zEoRwy4nG6KW0QC8bSEePR9ocWISElh_CE8rkn2WdiSZ1BH0RsM5kw2cger4vQGdHlvbu9uvgtI4diS2m0UlYu_e0d-rLa-gSMjtCmHdsbNZWKhyseKHttDWhhQATaXMj8vVfaDGVnBlde8ET-1FmbEosOH5HN5LnR9GUpXZRIaz_qnKn-Ni3Vq1gpYX9fLXde2rQFptm0Q65UvnK2F2-3l0_1cUUkrLemk7jZCi7_xaWwJjAQLOu7ryys5-ActxZVOMCJvGOE67Uw7QLC33sVB_0W0eyvTeBOc_6E8EPRat1PBMn74LreB6emm4z0fTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این فیلمی از رینگ کشتی کج نیست! یه دعوای سنگین تو فوتبال پایه مملکته بخاطر یه تکل ساده‌اس!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72499" target="_blank">📅 09:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72498">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324e32bd1.mp4?token=V4VMvH0B8JOonHt0uIm3rUkVPNhDpg7ted5DM5fMyYobAni70R3vJSjL7gCjT1mOVmT1G85N0XxYQBW8A8sFn1iYj17cbU-_fQ7HcfFfvE2rYT_kliDt1SnA6a2h_TGujRTMrEowscy9XJAQhYWLrnmNqTKr5EAS6SKRPLRyyoaG_1RhFevGeLNbZSzWQENIVXHBitd7-xFWIAyYO4k4TGJhDEtIiTXT3QC13LQmOiuul_wKMI24zAlljWmXYQL_vmXtDzW778h4nkc50mzo2pLocGdRXYdmDvQn3SqF0a_3oYKW3V5GVLy9bDGl4NfVRhof3vjJo75K_SDMQf6wKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324e32bd1.mp4?token=V4VMvH0B8JOonHt0uIm3rUkVPNhDpg7ted5DM5fMyYobAni70R3vJSjL7gCjT1mOVmT1G85N0XxYQBW8A8sFn1iYj17cbU-_fQ7HcfFfvE2rYT_kliDt1SnA6a2h_TGujRTMrEowscy9XJAQhYWLrnmNqTKr5EAS6SKRPLRyyoaG_1RhFevGeLNbZSzWQENIVXHBitd7-xFWIAyYO4k4TGJhDEtIiTXT3QC13LQmOiuul_wKMI24zAlljWmXYQL_vmXtDzW778h4nkc50mzo2pLocGdRXYdmDvQn3SqF0a_3oYKW3V5GVLy9bDGl4NfVRhof3vjJo75K_SDMQf6wKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره روحانی از ملاقات رئیس‌جمهور سوئیس با علی خامنه‌ای:
رئیس‌جمهور سوئیس به آقا گفت ما ۱۵۰ سال قبل کشور فقیری بودیم، اما دو تصمیم گرفتیم؛ دانشگاه‌های خوب ایجاد کنیم و با کشورهای دنیا روابط خوبی داشته باشیم. سوئیسی که امروز می‌بینید حاصل آن دو تصمیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72498" target="_blank">📅 09:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72497">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3jwWKhyDMmQWI00ocyJeBE-hLWsubd5GwJDdglAUxpzoOjgiQEaF7kdLIz8poFOZRpDT4gfw_rt1yrSFBV3gEInGtYeiYhKaRmwX36CD-_mYjk4gT_KSOfnup7D2tlMFToGVy3Ub5M2MemSWbeM5Tr4fbBfdk48sdPQNdk2m16Wyo_cP6Q7jPAhIcJ5aQTdPnbIOSZH_QR3lDw4oqVgbI7yQK0X9T0th6SRRFIu1c1aLze2MFLHlKpgqEsa71AkJDgcJGBxxwqiOub6PNeXWEKHVIzAEOJBLlyGz8S-SV0zp_37HtNdKTQDNdrgWYPEzK1M1Bq4xo-xDUBlnIc5hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛مذاکرات به بن‌بست رسیده،ایران میگه اگه آمریکا به تفاهم‌نامه اسلام‌آباد برگرده حاضره امتیاز هسته‌ای بده و آمریکا هم میگه حالا که دست بالا رو دارم پس کیر تو تفاهم‌نامه اسلام‌آباد و کوتاه نمیام.احتمال شروع درگیری‌ها بالاست.
اکسیوس؛
تلاش‌های قطر برای میانجی‌گری جهت دستیابی به توافقی جدید میان آمریکا و ایران پیشرفت اندکی داشته است؛ چرا که مذاکرات بر سر دو موضوع — یعنی درخواست ایران برای رفع محاصره دریایی توسط آمریکا و مطالبه واشنگتن برای دریافت امتیازات هسته‌ای — دچار بن‌بست شده است.
ایران تأکید دارد که تنها پس از بازگشت آمریکا به تفاهم‌نامه ماه ژوئن، حاضر به بررسی اعطای امتیازات هسته‌ای خواهد بود؛ در حالی که واشنگتن دلیلی برای کوتاه آمدن و مصالحه نمی‌بیند.
قطر، پاکستان و مصر همچنان دارن خایه‌مالی میکنن و تلاش میکنن که توافقی صورت بگیره.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/72497" target="_blank">📅 06:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72496">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/72496" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72495">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72495" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
