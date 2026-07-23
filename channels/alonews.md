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
<img src="https://cdn4.telesco.pe/file/Hy-43fF5_pucDh4i9ICWmaPkamxKDXaXLw93TRIUgNvvnJGOa12lfVMVRB9YnbNgvvtgVkKJJnc0ps-5s5590XN2PH1ZKKwAPG0MjUgncrs4MQpI28n8kkienMK66CGqKCJgiLPZXRXwBPSJDCwoVA_eOc4kO7Uw4foU8Pc7e-GVWEpSSOTv_SOhM_31KoxC7jpNuL90JENOCYlaaGZVTbcGZGrMurl44m1coZj-sFPJb5D62WaWBc54fp7GxUWhjsUvOwt71Rkv1VW8g1nbSv9pMdX5pgj-TY8HYMXCV4uHBc854Dxv1_-zAqyX75m317e1FSEgF4hE_tjk-cXhqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 932K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 22:30:52</div>
<hr>

<div class="tg-post" id="msg-137060">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ترامپ: ما به لطف ونزوئلا پول زیادی درآوردیم. ما به این پول حق داریم.
🔴
ترامپ درباره تلفات آمریکا:
این ۱۸ نفر در دو جنگ است.
🔴
وزیر انرژی کریس وایت ونزوئلا را اداره می‌کند.
🔴
او بیشتر از هر کس دیگری که تا به حال اداره کرده است، اداره می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/137060" target="_blank">📅 22:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137059">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c26191c2b9.mp4?token=hWYQOD3EWxlOxdaGU6ZnW87EYgK02dZS0G8LlvdE4bzgUlISqfS72_eS-H-SOD8fn5Jzpy4NsKSY30ewRlgnvdTz9FfFXirqtYlHIlsbAH3aQGu9xLqZC3EZt9OrrLPby6NJCE94pVOD5F4ChE_8oWpWtv54K8RO9Aw5W3xzZNbO85pWB-prUXamxyq6ibkSob-q1ZznlAwMjE3LUDLfVswi5vJHv5iMizDmFOIO0rxVMCftOWyRHhL-pBdb7UqyFjvIeOtbuXhJbGpcWQDnE4P7vhPC0i8M6JvMwwJq2uS2h-UhPoYXpulBiGD3pTgcu4_WJvlIK0r_-u0E6y19Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c26191c2b9.mp4?token=hWYQOD3EWxlOxdaGU6ZnW87EYgK02dZS0G8LlvdE4bzgUlISqfS72_eS-H-SOD8fn5Jzpy4NsKSY30ewRlgnvdTz9FfFXirqtYlHIlsbAH3aQGu9xLqZC3EZt9OrrLPby6NJCE94pVOD5F4ChE_8oWpWtv54K8RO9Aw5W3xzZNbO85pWB-prUXamxyq6ibkSob-q1ZznlAwMjE3LUDLfVswi5vJHv5iMizDmFOIO0rxVMCftOWyRHhL-pBdb7UqyFjvIeOtbuXhJbGpcWQDnE4P7vhPC0i8M6JvMwwJq2uS2h-UhPoYXpulBiGD3pTgcu4_WJvlIK0r_-u0E6y19Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در مقابل جمهوری اسلامی ایران عملکرد بسیار خوبی داریم. عملکرد ما فوق‌العاده است.
🔴
آنها دوست دارند کاری انجام دهند، اما من می‌گویم که آنها هنوز آماده نیستند.
🔴
آنها به همان چیزهایی که الان دارند، نیاز دارند. آنها هنوز آماده نیستند. آنها اهداف شومی دارند.
🔴
ما نمی‌توانیم اجازه دهیم که آنها سلاح هسته‌ای داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/137059" target="_blank">📅 22:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137058">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/058bc5f933.mp4?token=KAqTh1jaS-4egYPT6vWFGOfPaYvudDDnINx_7RB9fc5fXv4ytkCLRx4zO91KqF6J9hywe_yfXcEn4EUMBpAHVXqay-wqLdAEFmeJwWSo4RfN6jE8UaJ2J3NqdGsWof74DPYOd44XxbsxmHrhbgMehkJ984y-3Xvfci5o2kA4Dlk-DUIZJoEJi62HK3o1QIWDOEFAoWzCqQEIzwa6YiUzCxTn5liQU9Hc2FMozJR8SUFKsWm8-puSR6WtjeZ-6-mb92tyy08EKjAZy1F7F9fA_dN8OF1EErVyVPizXIoNGQeeXaw-AdPCdtRMROUOMmjOjYWelqSLY6QEiHHA5om9FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/058bc5f933.mp4?token=KAqTh1jaS-4egYPT6vWFGOfPaYvudDDnINx_7RB9fc5fXv4ytkCLRx4zO91KqF6J9hywe_yfXcEn4EUMBpAHVXqay-wqLdAEFmeJwWSo4RfN6jE8UaJ2J3NqdGsWof74DPYOd44XxbsxmHrhbgMehkJ984y-3Xvfci5o2kA4Dlk-DUIZJoEJi62HK3o1QIWDOEFAoWzCqQEIzwa6YiUzCxTn5liQU9Hc2FMozJR8SUFKsWm8-puSR6WtjeZ-6-mb92tyy08EKjAZy1F7F9fA_dN8OF1EErVyVPizXIoNGQeeXaw-AdPCdtRMROUOMmjOjYWelqSLY6QEiHHA5om9FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر از یک کشور دیگر خوشتان نمی‌آید، بگذارید آن‌ها به ساختن توربین‌های بادی ادامه دهند. این صنعت در حال فروپاشی است.
🔴
ما از چیزهایی استفاده خواهیم کرد که کارآمد هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/137058" target="_blank">📅 22:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137057">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba15abfb56.mp4?token=CpCyRXZCobUrzYsGWNv6QRCh8BGnUQTc63g6hNdsJJJpCy5INOVGQTqG9dvZQcedhgNvwtqXYMZr3-4Ul6pTIejxv55nCsjM8XJFGYguGOpe8FR2TxmgYNvpxLlTiRkuJ08J7KqXSm_qxpcL8BazrT0XvNUeTjRQhkdyag2YkjgZctQSdnpNJIULZsFYWLC02dGt21_5UQKuQD7y-PNNjsTgffIM-3yu0Kq62_7zxSlQVyss6NrmwbfRZjSb0YseaozVTESXZt1GnLlL2IORCXLyXLP9OJDhLYD_M8pR4Yp5hsh0WeY6m2ueDc0zoo-1Kx4YQbeZwgDj_95zrCAHnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba15abfb56.mp4?token=CpCyRXZCobUrzYsGWNv6QRCh8BGnUQTc63g6hNdsJJJpCy5INOVGQTqG9dvZQcedhgNvwtqXYMZr3-4Ul6pTIejxv55nCsjM8XJFGYguGOpe8FR2TxmgYNvpxLlTiRkuJ08J7KqXSm_qxpcL8BazrT0XvNUeTjRQhkdyag2YkjgZctQSdnpNJIULZsFYWLC02dGt21_5UQKuQD7y-PNNjsTgffIM-3yu0Kq62_7zxSlQVyss6NrmwbfRZjSb0YseaozVTESXZt1GnLlL2IORCXLyXLP9OJDhLYD_M8pR4Yp5hsh0WeY6m2ueDc0zoo-1Kx4YQbeZwgDj_95zrCAHnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «هیچ‌کس نمی‌توانست مناظره بین دونالد ترامپ و جو بایدنِ خواب‌آلود را تماشا کند، چون باد نمی‌وزید.» (کنایه و شوخی ترامپ با ظاهر و لقب تمسخرآمیز بایدن.)
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/137057" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137056">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-WSlteIm9P0hCyANpliIAV7SoNJZE-ULMMrkx2n66hZJHTsN1UlLvSgl1gxVxRJoAwbRqe3fjHomSZR6WKOt4DZ34LHSWCSQbQVSsEV3sab-EkPdEzomzSBGI5KNtQDYf5Qq1RcDWsn_wWSj2wmSkJDCmJCaeJZwizSRYPenfYPoDCAEN5ot8kp5PgReWTeCqPalWtwezWIFdk_1npXODRBhRk2GbaA8sADxpo8OdVYt6gunEvPDP9rjuevH1e-boykPOATxCRWQ43onh1un848GadbTn6zIhHPL1BxOn1oom6ndHXQznm4xABJSwSxAit9GxjLiWJBouKoYjTzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت به ۱۰۲ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/137056" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137055">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گزارش فعالیت جنگنده های نیرو هوایی ارتش بر فراز اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/137055" target="_blank">📅 22:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137054">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b623ee9c.mp4?token=ZnQnJNsPFpvf9rs6d8F5RBA1sImBnlQbI9Zgu3Gmwa1aA9pHy7dMedvOQ_7bTR7oSu3aLLeI_zIv3iCf5Lpci32TgnfMksa7W9YgtVtAVddSnb04-u0hnpKT9hEJFPfqRF2UggL7PQQGoJM-kDaVfxQSIfmqw1tAdgqu8K3ziMxtNXvzqFYEEqr-7JlnTyW0L76Y8ePKLUgVkLdnxZXo0xjOqCL1l8P1p3ubKScnGaDDWJC8UO0pNe5__Csy9VS5HuE1zf_FOEdvxPfZOx3bpNrdkUXSKxQrCuk-9rIZ93UbLa1bx3km7A6RPuZUJ3_C2Qglwf5h-pxfsSYOsTEDcmK5zRHEIIlrLhZGoNbUAzHP23NiVzSfI_efWaOzr15ZZx4r2dmP_bGhCQSleWvs1o_IBtXVG0J64ZSABwtgc_JfnN69CeuSYMGo2PTcoiEa_-cdu1mcs8chUn9W1FYAwaB8iOTzgddtiL6bm8m6bab8_KPcIvxlSE808jjk4KzRZ1sT5qdFzBIEuo54v4-Qb-H68emFU97lfDEJfWHQ1WWiK3xcnvcaR5uwK6trSd17LHWW-QP7Sglf6SPDORrM9ujie9UlCAUKcnml3Mp5TCPuyq4plCbC5tvvRIFNOsehuqiBQ7lIThGkti5IeNQ3l741NArA-eF2uO3VFxa9Kj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b623ee9c.mp4?token=ZnQnJNsPFpvf9rs6d8F5RBA1sImBnlQbI9Zgu3Gmwa1aA9pHy7dMedvOQ_7bTR7oSu3aLLeI_zIv3iCf5Lpci32TgnfMksa7W9YgtVtAVddSnb04-u0hnpKT9hEJFPfqRF2UggL7PQQGoJM-kDaVfxQSIfmqw1tAdgqu8K3ziMxtNXvzqFYEEqr-7JlnTyW0L76Y8ePKLUgVkLdnxZXo0xjOqCL1l8P1p3ubKScnGaDDWJC8UO0pNe5__Csy9VS5HuE1zf_FOEdvxPfZOx3bpNrdkUXSKxQrCuk-9rIZ93UbLa1bx3km7A6RPuZUJ3_C2Qglwf5h-pxfsSYOsTEDcmK5zRHEIIlrLhZGoNbUAzHP23NiVzSfI_efWaOzr15ZZx4r2dmP_bGhCQSleWvs1o_IBtXVG0J64ZSABwtgc_JfnN69CeuSYMGo2PTcoiEa_-cdu1mcs8chUn9W1FYAwaB8iOTzgddtiL6bm8m6bab8_KPcIvxlSE808jjk4KzRZ1sT5qdFzBIEuo54v4-Qb-H68emFU97lfDEJfWHQ1WWiK3xcnvcaR5uwK6trSd17LHWW-QP7Sglf6SPDORrM9ujie9UlCAUKcnml3Mp5TCPuyq4plCbC5tvvRIFNOsehuqiBQ7lIThGkti5IeNQ3l741NArA-eF2uO3VFxa9Kj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من می‌خواهم رئیس‌جمهور بعدی باشم.
🔴
من می‌خواهم کاری کنم که کسی بسیار خوب به نظر برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/137054" target="_blank">📅 22:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137053">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfdd7c5329.mp4?token=atB3eOc1DU3Ee4XnrqKzikeYqDwjScyH3T5tVcyJqGgYc6W4YlQNEqFbBqRK-3E7IbzxiSWbsBkX3BFe53XNgRblWYZS985jJI0QyBDM6OkVNCOIqkxb6cELb-pDoIIwtpkNSvrXGFOps5__aHArddMC4y5AOzpcqW8PN1IsLVwilguo_aLkVMNW2hdRXawmO_JKEHP6SqkKCqkSiOrV_Punom5NBzUxXs5BBBW-onD2rFcePsUF13L5jg_GBZYyAx4EHOWfPb2XfKZBxswAKKE9HFB68fow36xbme4RSIvslFxHaiojF4l0_WPuaXgPJfDO0R9yi1V5Kd2O9sk0QlD2XnWgom3AfBiZaUvUiTW57VIVUlyuJJQYrPrCF_SqnS9qM6RUh-49xRbtEkRlesop62dEPl2NbRqu42N8y0RggrRd0dHo7ht3bWEylFkUA3hsKq61q0GeZmNNBxdLgQ_7rfM6q7t6NZ9AULWLW8ISFvkTmgdF4tke2RWt96u_9lYKGmIABHdwKyIbrkSV-DuOH126YDD-pzcYJC5YPUUjjokrQim8Lxj09WV7q1xGUjK7R9bp7XMS8-eVHjaYy8accEAv62fGCOMjVXoUkJlN-AemouVN5tQkCoE7rt7a9keoKR19E-89aQMtRCfauJxdjAR4p32k5uuR8CSbTm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfdd7c5329.mp4?token=atB3eOc1DU3Ee4XnrqKzikeYqDwjScyH3T5tVcyJqGgYc6W4YlQNEqFbBqRK-3E7IbzxiSWbsBkX3BFe53XNgRblWYZS985jJI0QyBDM6OkVNCOIqkxb6cELb-pDoIIwtpkNSvrXGFOps5__aHArddMC4y5AOzpcqW8PN1IsLVwilguo_aLkVMNW2hdRXawmO_JKEHP6SqkKCqkSiOrV_Punom5NBzUxXs5BBBW-onD2rFcePsUF13L5jg_GBZYyAx4EHOWfPb2XfKZBxswAKKE9HFB68fow36xbme4RSIvslFxHaiojF4l0_WPuaXgPJfDO0R9yi1V5Kd2O9sk0QlD2XnWgom3AfBiZaUvUiTW57VIVUlyuJJQYrPrCF_SqnS9qM6RUh-49xRbtEkRlesop62dEPl2NbRqu42N8y0RggrRd0dHo7ht3bWEylFkUA3hsKq61q0GeZmNNBxdLgQ_7rfM6q7t6NZ9AULWLW8ISFvkTmgdF4tke2RWt96u_9lYKGmIABHdwKyIbrkSV-DuOH126YDD-pzcYJC5YPUUjjokrQim8Lxj09WV7q1xGUjK7R9bp7XMS8-eVHjaYy8accEAv62fGCOMjVXoUkJlN-AemouVN5tQkCoE7rt7a9keoKR19E-89aQMtRCfauJxdjAR4p32k5uuR8CSbTm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی رئیس جمهور اوکراین:
افرادی در اطراف پوتین هستند که می خواهند جنگ را پایان دهند، شاهد فروپاشی اقتصادی، فروپاشی لجستیکی و غیره هستند، اما به قول خودشان افراد نظامی هستند که خواهان گسترش جنگ، افزایش بسیج هستند.
🔴
آنها می خواهند ما را شکست دهند و آنها خواهان ادامه این جنگ هستند.
🔴
به همین دلیل باید برای گذراندن برنامه زمستان آماده شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/137053" target="_blank">📅 22:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137052">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cfd01a28.mp4?token=UPL8srRe0HiBbgFvx_NEg04QQVyuubZ0W7pum8zhfAJJgPvB3sPsEjH8SyRqvle-iyxjKc7ZOQ9mrwSPqpaug9U7GhC1WCiwJ0LdIaCETLqCkenRo0Qy6rMVdHZQrkNpJHg4kVFIwfmoRBs78W1guyqFA0JktejTSuL36cpCGtNUZMNHNaP_dfPuYQAxvDJl7sUnOQIGWxYXUXlxAIAk5XIeDmIYlb-lGGMyjCjNNVHmGWfTPvFoV0-PEwl2v95srVIbvTRYvMTAcjUZaWrh-3MfCS188AHF1vmh6UaQ4TEwEUYr7EWNECc_pOPR3JFf5voT3GSvt2jhqo8R0VUNWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cfd01a28.mp4?token=UPL8srRe0HiBbgFvx_NEg04QQVyuubZ0W7pum8zhfAJJgPvB3sPsEjH8SyRqvle-iyxjKc7ZOQ9mrwSPqpaug9U7GhC1WCiwJ0LdIaCETLqCkenRo0Qy6rMVdHZQrkNpJHg4kVFIwfmoRBs78W1guyqFA0JktejTSuL36cpCGtNUZMNHNaP_dfPuYQAxvDJl7sUnOQIGWxYXUXlxAIAk5XIeDmIYlb-lGGMyjCjNNVHmGWfTPvFoV0-PEwl2v95srVIbvTRYvMTAcjUZaWrh-3MfCS188AHF1vmh6UaQ4TEwEUYr7EWNECc_pOPR3JFf5voT3GSvt2jhqo8R0VUNWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما ۱۰ درصد از اینتل را خریدیم. آن را با قیمت مناسب به دست آوردیم.
ما در آن معامله حدود ۷۲ میلیارد دلار کسب کردیم.
🔴
آیا برای آن معامله اعتباری دریافت می‌کنم؟ خیر، من هیچ اعتباری دریافت نمی‌کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/137052" target="_blank">📅 22:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137051">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
عراقچی وارد قرقیزستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/137051" target="_blank">📅 22:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137050">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bdeb069b8.mp4?token=VIDx7s0J9euAV1eAbCnhdnlvBZ1AYQOZr9TVg3mMDMBVnpvwlgXIXIpvI1F9MGJkyGhYT3niRYD-JirV33_R3R0fQyR2bPCZIy9RnZOlcK7NS10evpNHnlIzaJt6Y7gItKka4BbpecOuU7lL9wqHECsFdWdvutoLrNX3n6SHNOZPxvJY_NRod92MuOXMwkHxyM7bvYHLWN813FPy4T8vSvQWscGBrxrJrN5NRqk5qm1DBRcmSzDZR1rJHUZm9C92ulRWJnv7J-ECLXVOvy1PS_dKTlfjMae04i7zToPSf3P4H0gMVbcs-CPcACi5DxRsMtVZK-7jWo-vaR5eiqlqEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bdeb069b8.mp4?token=VIDx7s0J9euAV1eAbCnhdnlvBZ1AYQOZr9TVg3mMDMBVnpvwlgXIXIpvI1F9MGJkyGhYT3niRYD-JirV33_R3R0fQyR2bPCZIy9RnZOlcK7NS10evpNHnlIzaJt6Y7gItKka4BbpecOuU7lL9wqHECsFdWdvutoLrNX3n6SHNOZPxvJY_NRod92MuOXMwkHxyM7bvYHLWN813FPy4T8vSvQWscGBrxrJrN5NRqk5qm1DBRcmSzDZR1rJHUZm9C92ulRWJnv7J-ECLXVOvy1PS_dKTlfjMae04i7zToPSf3P4H0gMVbcs-CPcACi5DxRsMtVZK-7jWo-vaR5eiqlqEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هوش مصنوعی بزرگتر از اینترنت است.
🔴
هوش مصنوعی بزرگتر از هر چیزی است که تاکنون کسی دیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/137050" target="_blank">📅 22:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137049">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: از زمان ازسرگیری محاصره دریایی ایران در هفته گذشته، مسیر ۱۲ کشتی تجاری را تغییر دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/137049" target="_blank">📅 22:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137048">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
العربیه: قیمت نفت همچنان در حال افزایش است و قیمت هر بشکه نفت برنت ۸ درصد افزایش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/137048" target="_blank">📅 22:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137047">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر امور خارجه کوبا به الجزیره:
سناریوی تصرف کوبا ممکن است در ذهن واشنگتن باشد، اما این کار نه آسان است و نه قابل قبول
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/137047" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137045">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpUocJTB7vbsJHXXwlEcz9LW-KGZ2b4PHXVHffIbmnY0o7OXlHRo5x4sv-nj0Axv8L8V27YbKNifZHqP_bIqwPOx2PdWoTRTnvq6PLSw5vC0IdVK5fxwpeTqwQouNkG1LXgeLlKktfIB2QsPvSQbiQWpsrbfmRj19I5IgW-hQ4DDUbKTW_EcNgzcUeYEfI4SAOfUxgRL0iozDMUCtmaCSZfbBj1wKJ6DFmtSnNW_dFwPlES2kwLAvfc_myjq7TIZuy1tySdrq6X-MDSEDRpsFmxvq04HF1iIlfjnDk3UJ7CDTyPouHWyTQ_mu0KuHjnQ2IWVERuY2OxLO6XnQUHdvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/toeIRropaMVj-NA9QUVlHxOaxLHnL-d27qrc9YaSxJtx-cdy9dkn0kaqSj7-QNSulyt6vbQ8gy_t0-_cGXBpXkFImdI-nCZKnAeLJns85xXTNAqxlp8OMSbcW9vjlhTL2Eslotj3biH21xpUWd2t9e6uz5Aoz6-tW6cbiJBpwqP9OE82dyPpnk5Oy6NcD6VFEuRwY4veizf-5hPGTJ3WGhvAqGmSlpdmJHz1viIbCLkoZnWBtpSlIXn3XAJpNjc82lpuxq3UoO68TjVRFS90ezrJ_6tpGSL4ZzwYG4O8Ofi-pjxoHWgQyatmTpEW4txissaoIM5pL4v4EslcoY96MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار نخست وزیر عراق با قالیباف
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/137045" target="_blank">📅 22:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137044">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گزارشات از شنیده شدن صدای انفجار در شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/137044" target="_blank">📅 21:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqjvXNPw38WQ9tdEY2uvkNB1eORNqqHIczwAGChUCkhI_WH5H7G-cTzAPIe82ltG37c2queNa_0f-NKquvdsFksafseGXkplFG6kAJhn93iYBMnycnsaRkoNz-jVTulD77R2T6SRIMxNhtfb1OdowCdAEpWIQd8C_UygTKInxJj1RQE4zYHo1xCGLsNu_pFCByEoF8XjkmYFa_wCBly6VJtCKZs9Fei5v285z26s7FQWDWr5u2KHADqA0ecBQ60hi0Eg9PcUq1gphj8bS8pmXwdY6BtoB3tVFu4i3QPOBG_Cem_Zhf7wlsNpU2BpnhI1-_Jxl7eR3V2dX_jMD5lJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐲
فیلترشکن تانل شده مولتی لوکیشن
▪️
5 گیگ 35 هزار تومان
▪️
10 گیگ 70 هزار تومان
▪️
15 گیگ 100 هزار تومان
▪️
20 گیگ 140 هزار تومان
▪️
50 گیگ 320 هزار تومان
▪️
100 گیگ 600 هزار تومن
👥
- بدون محدودیت کاربر (999 نفر)
🎮
- پینگ پایین مناسب گیم
🛰
- تمامی سرور ها تانل شده ایمن و پرسرعت
🖥
- مناسب برای تمامی سرویس های تحریم شده (
📱
📱
📱
📱
📱
📱
📱
📱
)
🇹🇷
🇫🇮
🇩🇪
🇸🇪
🇳🇱
✨
خرید و تست با دریافت بونس اولین خرید
🛍</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/137042" target="_blank">📅 21:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137041">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddd8bf81be.mp4?token=ZTzEaLl_xt2fSylFICcNO1RIJkMa3xmovuz6BeYZSPhi0WACnLO9N6LfWxEH-SaFEr0DNPmExVV3WWJAc1H_VR8eCISgnt0HqkZ9h5XVKRgty12BS4VjEmieiHI1cs9Wbh_VSZ9bYzQ-Nv3gISM2wLCCXXl3OpZHfPg1s-EwNTfGyjuEM4FgxyGplrTzk_nRemBMlT-Gz6dCevCUhs7viL9sk8qtiCRGwMlMQQa7lPLaJknGkCJ8bsbiud0WoR0qpbCh_tpiKcrBmMpuJkQACU9jiiPm2lcIGk_HVcd-k_D-wMxFGIJRA04cPcFTO-2qTbBidMpm3-jaYSJZhn2vfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddd8bf81be.mp4?token=ZTzEaLl_xt2fSylFICcNO1RIJkMa3xmovuz6BeYZSPhi0WACnLO9N6LfWxEH-SaFEr0DNPmExVV3WWJAc1H_VR8eCISgnt0HqkZ9h5XVKRgty12BS4VjEmieiHI1cs9Wbh_VSZ9bYzQ-Nv3gISM2wLCCXXl3OpZHfPg1s-EwNTfGyjuEM4FgxyGplrTzk_nRemBMlT-Gz6dCevCUhs7viL9sk8qtiCRGwMlMQQa7lPLaJknGkCJ8bsbiud0WoR0qpbCh_tpiKcrBmMpuJkQACU9jiiPm2lcIGk_HVcd-k_D-wMxFGIJRA04cPcFTO-2qTbBidMpm3-jaYSJZhn2vfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور اوکراین زلنسکی:
پوتین در حال آماده‌سازی حملات جدید علیه اوکراین است، از دیدگاه ما، در حال آماده‌سازی بسیج اضافی در روسیه است، و در حال آماده‌سازی گسترش جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/137041" target="_blank">📅 21:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137040">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde7f010c8.mp4?token=EmbXgkHZ0Q4y73ar-gx-MdL05XqfEdzU6fVQ9ZGZgrWD_CCEKNng61JbSk4TLd6sqFvAxaswHR1T249XoQqWnp2T6loCVn4zZpZ69mMeDL39ceu_HhPpIX-DbmkoD66YPdEV9_uInJm8Jk4IvlqWSwF6TBdNm1AjAgoJRdljGghmTI9x_GaZGAbjVPBoBQpsLij9XKy8zN0FmgkU-8cyYmralUG8UTmzBgiNoV1VKvLl2eM4fOHDtMcTMY7h4qh6v4y9SqdmSbS7MtfhLii6sMTHXH72SEjMiymFyycs4C7Hi5VJxTicgRDquQSszbSr8PyqGsXis52Y9ll8KpjTdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde7f010c8.mp4?token=EmbXgkHZ0Q4y73ar-gx-MdL05XqfEdzU6fVQ9ZGZgrWD_CCEKNng61JbSk4TLd6sqFvAxaswHR1T249XoQqWnp2T6loCVn4zZpZ69mMeDL39ceu_HhPpIX-DbmkoD66YPdEV9_uInJm8Jk4IvlqWSwF6TBdNm1AjAgoJRdljGghmTI9x_GaZGAbjVPBoBQpsLij9XKy8zN0FmgkU-8cyYmralUG8UTmzBgiNoV1VKvLl2eM4fOHDtMcTMY7h4qh6v4y9SqdmSbS7MtfhLii6sMTHXH72SEjMiymFyycs4C7Hi5VJxTicgRDquQSszbSr8PyqGsXis52Y9ll8KpjTdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقرار یک زیردریایی و یک سامانه موشکی «ذوالفقار» متعلق به بسیج در میدان آزادی برای نمایش به مردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/137040" target="_blank">📅 21:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137039">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GckRoa96tNq7DBCacY9n55GHLWYeWcdcbEzd0l5rT_1TjfMeeA-32k8t8BDEs750G_6xsWx9VLhTncM5HdqerW7aztgUKcShyiE_uCHnP7EGThIxiOIlJqq71idd8MYoN91uGirrVpFnwnnzIL8BI5u2ZIlJ_Vp7q6EKrqGTMwjZUQUd8rV91lG6ZUdwuDOn1-CtpB24rr28c_zeO1gqfufslsPdfUhkHXUNOX_-XpeDR-FrJRODt3qd6bDX-1EhQRV5z0k__eUFqU3r9OBSRkMJ_QsThqZCVi1rRouYwxutLdeMdnZrxgf7n-aMfIsmBIF2soVWXNM_FRFCAqVEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت ۱۰۱ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/137039" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137038">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ایلان ماسک: هوش مصنوعی تا پنج سال دیگر از مجموع هوش انسان فراتر می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/137038" target="_blank">📅 21:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137037">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
فرانسه تخلیه سفارت خود در تهران را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137037" target="_blank">📅 21:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137036">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67665193ec.mp4?token=Z3HCPuOb0lVBqL68HVVrWZob_EurezgizVmJkpB4WciUbRMD8BEghSTy4_Kc94BybFB9MoRlF9JvLY_ogqWHpjzFZswfD1io8Ny6QxfFUZtZerSdk7fzkrDJ_zrWfAjokdGBa1lFK-PmdOzujX98G89J1uij8IKQ65ZXX_e065axJ5IiMAtvr2j7iKKLdAhRXBPbbxNYxa7DOBZaHNoe6C2DvGpkDDqvARSYyh-_tUi2slHcWcsCRO9PIi94bHAdFgZqgl-0UsfYPRJU0DJPI2z_bHxMTLzTxYrrMI9Tkgv--ctRNSEkteAkhAzP5mQ-jpZwJsqdB7vGT4bne0MBooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67665193ec.mp4?token=Z3HCPuOb0lVBqL68HVVrWZob_EurezgizVmJkpB4WciUbRMD8BEghSTy4_Kc94BybFB9MoRlF9JvLY_ogqWHpjzFZswfD1io8Ny6QxfFUZtZerSdk7fzkrDJ_zrWfAjokdGBa1lFK-PmdOzujX98G89J1uij8IKQ65ZXX_e065axJ5IiMAtvr2j7iKKLdAhRXBPbbxNYxa7DOBZaHNoe6C2DvGpkDDqvARSYyh-_tUi2slHcWcsCRO9PIi94bHAdFgZqgl-0UsfYPRJU0DJPI2z_bHxMTLzTxYrrMI9Tkgv--ctRNSEkteAkhAzP5mQ-jpZwJsqdB7vGT4bne0MBooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: چرا عربستان سعودی به توافق هسته‌ای غیرنظامی دست پیدا می‌کند، اما ایران این توافق را به دست نمی‌آورد؟
🔴
سخنگوی کاخ سفید: توافق ما با عربستان سعودی، منافع آمریکا را در اولویت قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137036" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137035">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a0l6cQ3WzUJfY4Hzv2Uk1j1SuYWmxYY-kJOp7w0xgvJQc3ivi8W0AwdgYp2MIvC1PctitwxkxYnsoeEs63E3BZOzh6G-_m5Gpl75y2KVgyVXwcHoNHN58y3qsfa0_u0bTWQpaJw_4xOm9sED1b58CutPDzIQiQlOAxag-EjzEiJ1K43Ru2RAsVh8cjND4dAd7hLsvlDqLffAvAw3tITKWmZ6GCFMtwsJvq0VwgrYf_tMxPK3xg9RCvKiPfnWrFzSaD4Ca4QAID8491d4L__APeFujVg9EN9MFJX2QWOG4IsraH09HHFKjd5wQk2skyPBiis6tmjAM_0XgFwuHXdaKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای نظارتی E-3G Sentry متعلق به نیروی هوایی ایالات متحده در آسمان، که نشانه‌ای از دور دیگری از حملات علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137035" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137034">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
شرکت پالایش و پخش فرآورده‌های نفتی: عرضه سی‌ان‌جی با مشارکت داوطلبانه بیش از هزار جایگاه، از اول مرداد رایگان شد
🔴
این طرح با هدف کاهش مصرف بنزین عملیاتی شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137034" target="_blank">📅 21:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137033">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی:  تل‌آویو در صورت مشارکت ایران در جنگ، قصد دارد اهدافی را در ایران مورد حمله قرار دهد که تاکنون هدف قرار نگرفته‌اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137033" target="_blank">📅 21:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137032">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سی‌ان‌ان: مامور سرویس مخفی که از جی دی ونس محافظت می‌کرد، به افشای اطلاعات مربوط به سفرها و خانواده معاون رئیس جمهور متهم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137032" target="_blank">📅 21:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137031">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
به گفته برخی منابع  کاردار سفارت آلمان ایران را ترک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137031" target="_blank">📅 21:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137027">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729b02b020.mp4?token=YvWyk9Uxiv2tTyfEcDVmd7jxKyqtFXqkNSc83Ff4Z2-a4qPiU1m2VWlf9FllHjNPNBvHnyuD6cJRE6j9B6es08qZdMgxIEGeOoiF1CT1AiyBGOz9QiQFISbF38Z5dNv0T3-6ljD6xl_-kHsB_itw5PsldDUuBOLsFARVgiWojEGnjjowdk_Vw88c1R4uN56UoBpBACK30fzfJHCvAfp6qSkRz-aP2bR5gMw_46VZtj0FEu7qxaPdhRW9g4nV_9inJJHuYm5OeRDBUYsB8L-Fa_CBe1thfh-1olG5hFji1I_Qpm8GoE3_EAhyA-_IiUwBgAd9w4UzjPS0EKKbg8Du5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729b02b020.mp4?token=YvWyk9Uxiv2tTyfEcDVmd7jxKyqtFXqkNSc83Ff4Z2-a4qPiU1m2VWlf9FllHjNPNBvHnyuD6cJRE6j9B6es08qZdMgxIEGeOoiF1CT1AiyBGOz9QiQFISbF38Z5dNv0T3-6ljD6xl_-kHsB_itw5PsldDUuBOLsFARVgiWojEGnjjowdk_Vw88c1R4uN56UoBpBACK30fzfJHCvAfp6qSkRz-aP2bR5gMw_46VZtj0FEu7qxaPdhRW9g4nV_9inJJHuYm5OeRDBUYsB8L-Fa_CBe1thfh-1olG5hFji1I_Qpm8GoE3_EAhyA-_IiUwBgAd9w4UzjPS0EKKbg8Du5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قبایل عرب سوریه در شمال این کشور، بسیج خود را علیه ائتلاف نیروهای دموکراتیک سوریه (SDF) که تحت رهبری کردها فعالیت می‌کند، اعلام کرده‌اند و در حال استقرار نیروهای خود در نزدیکی شهر حسکه هستند که تحت کنترل SDF قرار دارد.
🔴
این قبایل عرب ادعا می‌کنند که هدفشان رهایی شمال سوریه از سازمان "تروریستی" است و خواستار آن هستند که دولت سوریه کنترل کامل این منطقه را به دست بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137027" target="_blank">📅 20:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137026">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU2lG87s-IhsC3HtCy7fg-BRa764MjQzwLF3X5dIqJEdfPM9fwldO3nZO4SK053ihU30Wre0SAohdTxSgAQcOQLjVY_TRdB0ruPRJWJ8HqV1neAfe-ekFfSnc3s1m8fHgTx2BsubIHAXk7BeW_GNdi66AVHzHO8oe-JbHA4PX1uPegrSMFrLZU20vzhLerq58MCugFL6lo4fFbG9S6_VrMDwV2EQBkFCnlf3ig4kmU4SD31QUG3SOJ2fOeb0_uEvldZclVCcttybxAWAp4OefGCsc399GR0hIolA31NvbesFrbMKU5ZA3xryNUpDcPrNLGlFrYFKhDypRZLaeAmqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک‌ نفتکش منتسب به ناوگان ایران دقایقی پیش از محاصره آمریکا از آب‌های آزاد وارد دریای عمان شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137026" target="_blank">📅 20:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137025">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e488927e.mp4?token=nrHs0JFSwtaNBxrbPKMP0waJ__-K3qs_OyzMZOSDELpEntFSeMETviUmujehO5lCTzPhArH5C2psI-FV9yIeHUa4BFD79k1dD5Z7voeau2DuLQ2mMeqNz8mTIzF2f7to_9TIEQ1d8KzC_UK6CBxC2WQ7cUy5qicWA7PSihUaP-wzeZQywsx-UDvB5z-2AfD4Dlh67r_67b3bJW2thOr5RgS_F2rdLSsW6_Wmfh8UlVuw-QYevf_IQ4ewQtqJjAZKEyOo3SyIDvw7M2gEglXZPu4xjU9NQKfahUjVHd-Cw2GWSo0-NmPfD6Hluy8KookZTqyEXIAdhT7uQ1XDGmuwuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e488927e.mp4?token=nrHs0JFSwtaNBxrbPKMP0waJ__-K3qs_OyzMZOSDELpEntFSeMETviUmujehO5lCTzPhArH5C2psI-FV9yIeHUa4BFD79k1dD5Z7voeau2DuLQ2mMeqNz8mTIzF2f7to_9TIEQ1d8KzC_UK6CBxC2WQ7cUy5qicWA7PSihUaP-wzeZQywsx-UDvB5z-2AfD4Dlh67r_67b3bJW2thOr5RgS_F2rdLSsW6_Wmfh8UlVuw-QYevf_IQ4ewQtqJjAZKEyOo3SyIDvw7M2gEglXZPu4xjU9NQKfahUjVHd-Cw2GWSo0-NmPfD6Hluy8KookZTqyEXIAdhT7uQ1XDGmuwuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرار گسترده زندانیان از زندانی در کلمبیا
🔴
در پی وقوع شورش در زندان «لاورا والنسیا» واقع در شهر «پوپایان» کلمبیا، بیش از ۳۰ زندانی موفق به فرار شدند.
🔴
عملیات گسترده نیروهای امنیتی برای شناسایی و بازداشت زندانیان فراری در شهر پوپایان آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137025" target="_blank">📅 20:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137024">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
به گفته برخی منابع عبری ، اسرائیل هشداری از جانب سرویس های امنیتی غربی مبنی بر حمله قریب الوقوع ایران دریافت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137024" target="_blank">📅 20:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137023">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
به گفته برخی منابع عبری ، اسرائیل هشداری از جانب سرویس های امنیتی غربی مبنی بر حمله قریب الوقوع ایران دریافت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137023" target="_blank">📅 20:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137022">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / بریتانیا: نیروهای ما آماده‌اند تا هرگونه حمله‌ای را در پی تهدیدات ایران دفع کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137022" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137021">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU52gar09Ovxf2dXm7cKw_kgZkmY5aFNAkPYbfXCC0Y4vUbpg0iShepnh_E47w1bRBa06BIuapH9B5OfebqL5TvnpLETUj2wHE3iMHZuYyeN1hNunbaXW5eAeJxFVm4PefFYMlTgcDg3NXnNizm468zWdi-PdoOk3X9tRizg_lsNAl-BGZ_u0mTolPAEuMGOLOY0qub4BgLVrpXEZwCeMTFuKEYsIH3lAcV5GSMvvO8nO2c9IvDYQv4kkjZsNUaLhV29aUF-Vh00tWOrRVBwCFHFx8K732vUWtdWDykuG8hEKfaKky0RuIdb_3cVrh_dHBw8eHqGynG40nAF5eafXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتسب به اصابت در بزرگترین نیروگاه برق کویت در حملات ساعتی پیش ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137021" target="_blank">📅 20:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137020">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
به گفته برخی منابع  کاردار سفارت آلمان ایران را ترک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137020" target="_blank">📅 20:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137019">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری/ سنای آمریکا پیش‌نویس قطعنامه محدود کردن اختیارات ترامپ در مورد جنگ با ایران را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137019" target="_blank">📅 20:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137018">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
زلنسکی: آمریکایی‌ها روی ایران متمرکز شده‌اند؛ این موضوع برای ما مشکل محسوب می‌شود
🔴
اوضاع در تهران به آن خوبی که واشنگتن می‌خواهد، نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137018" target="_blank">📅 20:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137017">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
خبرگزاری فارس: صدای انفجاری از دریا در جزیره لارک در جنوب کشور شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137017" target="_blank">📅 20:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137016">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزارت دفاع کویت اعلام کرد که گذرگاه مرزی العبدالی، واقع در مرز شرقی کویت و عراق، امروز مورد حملات مکرر پهپادهای ایرانی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137016" target="_blank">📅 20:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137015">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxFj2i1hj9bN1DKgcd-72BnXNfuAIyCb9uGrjU2d0qtUsJ3ifBS1lfXJu68LC6jGJVAP1fBjGEok8d9TqA-MPOkHSo8ME3qPd-31xQd2Fle3gfb6gw_lOnc3ueLpKnomRKhAymtDwFqxILXqh7eNhpEk4EV8cKP8A_jTfzT8U0-lkLpGSCWkcZw4553-nH_rAr4m42svcmoJ2VxFUZHSXIWLZv2CdzrAHFajEj1oBpBOSdCW2UYp9l2D8jM9aIn9KYfl_IfuJu0dtpgqy8iYgAhozaWVsNngT2iwPhymaqN-BUZYhjhpsd_Cf4HJDs2-kts_4hOH-ZQndhk0x8O_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی : رئیس جمهور آمریکا، با اشتباهات مرگبار خود، از "بازی دیوانگی" به "بازی ناامیدی" روی آورده است.
🔴
حمله‌ای به زائران در شلمچه و تهدید به حمله به زیرساخت‌ها، چیزی جز ناامیدی و ناتوانی نیست.
🔴
پاسخ ایران به حملات زیرساختی، تشدید شده و قاطع خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137015" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137014">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
دبیرکل سازمان ملل پس از سه رقمی شدن قیمت نفت: درگیری‌ها باید متوقف شود، دیپلماسی تنها راه پیش‌رو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137014" target="_blank">📅 20:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137013">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffeaff223.mp4?token=QGegCbC93EtRO8PRCgIfkUQlex5ZhbhyG4rS1jdsTOlUStuoN5XbMzG0QDGs3GkYqJMrKbuP4MGyBNdmOb9Gzp567YhuU9b4WQFkkpgvEsofFzJPIAPi8gcSzgZ4ru0MFOxz293_eFutuAW8gzIjGtaZxvR8bbpFS_TfB2pbrOEGx2QtahgB3GKZCqjlmjFptVp1ukzgbNORiVKz9ebifTxvQfvZvfBk1XTnSUdoJAqpcINm_cFIIdRYR5oIrT1aY_vfLaXFXH9Iw76XP_Z9udFp1eBx0KpwyQZ3w5kyheQTN9LOCYczUEIixqrHkHD65RAlNm7upln-SJfc9ksNIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffeaff223.mp4?token=QGegCbC93EtRO8PRCgIfkUQlex5ZhbhyG4rS1jdsTOlUStuoN5XbMzG0QDGs3GkYqJMrKbuP4MGyBNdmOb9Gzp567YhuU9b4WQFkkpgvEsofFzJPIAPi8gcSzgZ4ru0MFOxz293_eFutuAW8gzIjGtaZxvR8bbpFS_TfB2pbrOEGx2QtahgB3GKZCqjlmjFptVp1ukzgbNORiVKz9ebifTxvQfvZvfBk1XTnSUdoJAqpcINm_cFIIdRYR5oIrT1aY_vfLaXFXH9Iw76XP_Z9udFp1eBx0KpwyQZ3w5kyheQTN9LOCYczUEIixqrHkHD65RAlNm7upln-SJfc9ksNIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهبر دموکرات‌های مجلس نمایندگان درباره ترامپ: او بعد از فینال جام جهانی خودش را رسوا کرد.
🔴
او شبیه پیرمردی در باشگاهی بود که هیچ‌کس نمی‌خواست با او باشند و او تنها کسی بود که نمی‌توانست این را بفهمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137013" target="_blank">📅 20:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137012">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hpAdBqetVE2Kda9iCMStW-HwCcfKYkGypyvYhi6KaZDNgDmVM8yZH31uap4ZqUP6qKvrPWfEN8U3PpmfMxxJG7ST1osIbRXa6ea1YMW1Ir3CpwkeOyZtCOfBfD-fGzcByxVX52K9Do5ibYtEFPxAtwoWvLn__AIrJbIB_0zS_-Vwbt266tPZICQarwbVJx3AITQH4crRT_aD1a21lB1kT4D2OjNsCt1WeMNQJaDkcsiRKr01uv5ecUl-XS71FfmXck2ng_WilsrdDThvpOmKkgZpUahfrFELYBJPbyQXZLAEuB9HjojveUufWt611YB-6Fgi4SmJk0RYTAeo2PGvQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در میدان فلسطین تهران، بیلبوردی جدید با تصویر خلیل الحیه، رهبر جدید حماس، نصب شده است. بر روی این بیلبورد به زبان عربی نوشته شده است: «خلیل الحیه؛ کابوس اشغالگران!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137012" target="_blank">📅 20:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137011">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
صدای چند انفجار در جزیره قشم و لارک شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137011" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137010">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSzfHqHQIrtxfHhq3dDzyMNfMX7V8sHdFjtsXdJ2Qwmf4U5nTJFd7vtfBgkCtPGnzk3p1eebByjP6CW7djSSMQT8ZVmxq-C3mxOBzq-gjpSSrZ7eDmGhx3y_WxOvvJBmlQqdH3R1zERBRfEJt_OACXvvB32pb6aGgfFPCGoJOnWCsdUuOuD2dOOA6bZu3fDzRtHsC7I0uDTa3XojTmr3_owHERPr0F8tibyOoZXtECEeipv2DAf7fZ0BIcN07YK_9WnHa3t9xqzUYw0VlsACWz68HUUf1y2330WhnrZ0uM3WY5miVRyvxw2FKu3sp4NTRHRdJxlaXrag7wHk-CygoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137010" target="_blank">📅 20:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137009">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ارتش کویت: بار دیگر هدف حمله در منطقه العبدلی قرار گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/137009" target="_blank">📅 20:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137008">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBeGMOR58oBuf928zRoxNrtVTGCDEyYxg3MrxJjlBflTVFPiQZZWsXCLcJj7pcGuMwu6MkfWL6mzQaykWmrymMQ9yyl19pLtzJwFaVeCWgjxzz6mznzvLAv6c3rlq8es4R7s_-EeCp783uNDrKLFIW5Dzbzu4wu4dgREnEjHbJS99ztSXQgs755491tfdnOURV4_RKifAl0zGyyOeCecKgtX1vNTgsZVCwSNuvzC25acxoQ_FM65QeOC4Vf4Uvhbq2IAVJ5BnokR1J7gpRoOC2RrhPSy6kQCP0WV4EOVkmR0ArFidPQA-e3yyPJ0UG0chgLRIkSX16lcZo9FLTWJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اخبار اولیه حاکی از آن است که هدف مورد نظر در کویت، یک نیروگاه برق اصلی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137008" target="_blank">📅 20:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137007">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
انفجارهای شدید جزیره بوبیان کویت را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137007" target="_blank">📅 19:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137006">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزارت دفاع آلمان در جدیدترین تصمیم نظامی خود، از برنامه این کشور برای خارج کردن دو فروند از کشتی‌های جنگی‌اش از منطقه دریای سرخ خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137006" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137005">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
انفجارهای شدید جزیره بوبیان کویت را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137005" target="_blank">📅 19:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137004">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a655f0746d.mp4?token=fnd6bR6LICqkyqqsvCf6gigBELOI2arA8jZYFO1BpvixxF95iuo1spqtBNenlMYGHhyW3uUjOBXxdswRN1WJ63Sp70Pe-Kk9SC9wNEh-xqku0aVaCXGI_wCYqzpgrribrCtYAL3YnYo7Kg_omHCZNVKvDqnGItHYTmr9SwhlqMsUrCQ6wYB0Sn2kwo53Zkko6iQ69GF51ebM0rGUngBs-ypga9oi-d_CW75Vuph3A5rFyQROZq1zOCMRR2cxDFjugcAheezkRQittzGGszpCypNBBismvtARyFn4JZO_PNUIa1snJrHqKXJxsPTiZ4I8oYDhg5Cndb3bew_dJRTTIZFiSWzXZ5iBu_NEqiKkNxHFiH9oRXvFmGTxyullp8eciE4yKQA9BFTsJ1ZZMwCnr8Z3QTO05Q6iQKiOjvK2ZLUqSl8Ezwf8vUN-tt1eQzVN_QeyQiGOqoaxyDeAOYHXokxLOMjfb_atajWSivZFWRi0NxGsRWSDvAk5oSnc5Bz3KzkN5N9rGpLQLA48VcO-vGns42fOkX8wSQ-QiO_J4Inaqi8M8V122LdSaN9JGlAYHPwknNCi39dTZBDbY_N8E_hqGSkiymZ5J4TwINiOcCR8UPTuet-f1_oPW9eHD5FZNHsvV4SzUluSACv5Kl7VHFzsO-Ly1ofpZjdo3rAg99w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a655f0746d.mp4?token=fnd6bR6LICqkyqqsvCf6gigBELOI2arA8jZYFO1BpvixxF95iuo1spqtBNenlMYGHhyW3uUjOBXxdswRN1WJ63Sp70Pe-Kk9SC9wNEh-xqku0aVaCXGI_wCYqzpgrribrCtYAL3YnYo7Kg_omHCZNVKvDqnGItHYTmr9SwhlqMsUrCQ6wYB0Sn2kwo53Zkko6iQ69GF51ebM0rGUngBs-ypga9oi-d_CW75Vuph3A5rFyQROZq1zOCMRR2cxDFjugcAheezkRQittzGGszpCypNBBismvtARyFn4JZO_PNUIa1snJrHqKXJxsPTiZ4I8oYDhg5Cndb3bew_dJRTTIZFiSWzXZ5iBu_NEqiKkNxHFiH9oRXvFmGTxyullp8eciE4yKQA9BFTsJ1ZZMwCnr8Z3QTO05Q6iQKiOjvK2ZLUqSl8Ezwf8vUN-tt1eQzVN_QeyQiGOqoaxyDeAOYHXokxLOMjfb_atajWSivZFWRi0NxGsRWSDvAk5oSnc5Bz3KzkN5N9rGpLQLA48VcO-vGns42fOkX8wSQ-QiO_J4Inaqi8M8V122LdSaN9JGlAYHPwknNCi39dTZBDbY_N8E_hqGSkiymZ5J4TwINiOcCR8UPTuet-f1_oPW9eHD5FZNHsvV4SzUluSACv5Kl7VHFzsO-Ly1ofpZjdo3rAg99w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: چرا عربستان سعودی یک توافق هسته‌ای غیرنظامی دریافت می‌کند اما ایران یک توافق هسته‌ای غیرنظامی دریافت نمی‌کند؟
🔴
کارولین لیویت: توافق با عربستان سعودی آمریکا را در اولویت قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137004" target="_blank">📅 19:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137003">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S30xOxHxef1wRIF_YH1IfpxzyMIxXStgUmfUUaDS5pLw1tfFXlmsne8cHDBLi9F0JiSFmMFu4i3uZLSx8WyeujLA2BY3elbhKi-WHFXoccNgt63biBqne8i_3OzGxA624RRL9g2ZmHHwrNUKUP-fOLUv7mGBV2ycnylxx3X1C_gmldXiMtKAbtZCS2i71DgrbeCCKHYqmNuGPyJrRCFzhKWYAQMLu96uDwZe5IhQTgGcEcey3ripkK-ZWKvUXuszaroFIOBJJTbzqndlPKH1QeMNGA2WgkccMYjmrkIjzfL6HgbvR-sbBAcuSvlM7xybX_7CmSnuW2kkPJNoSuJeUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازار سهام آمریکا در بحبوحه احتمال تشدید درگیری میان ایران و آمریکا، بیش از 1.3 تریلیون دلار از ارزش خود را از دست داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/137003" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137002">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
العربیه: وزارت خارجه آمریکا از شهروندان خود خواسته است تا برای احتمال لغو پروازها و بسته شدن مسیرهای هوایی آماده شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137002" target="_blank">📅 19:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137001">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نتانیاهو فردا جلسه فوری امنیتی تشکیل می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137001" target="_blank">📅 19:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137000">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b0dd1cee.mp4?token=oxqPBdXjY9hUqD7xWU804I8bsQTD36YOSoiHbMWo4TKixQNnYXCaI-ZKw0234XuFFmBvYF74HW1wbLQDUpn_IT3x96MgE6Wh_M1TBmAHcU5sQAyuhnZE9scdD6TPlCSY9pfDFDeMGmqYxGnfV45ICQVXw1tOv04dI99OlNxZoMuLu8sD_1rXi4sDBAiJHBOhdyEhsGhuP1LB6MxfaEQyjNHYgHUNeU9Drv_d85S1g51Hovzpc2DSefi15Z5MhkPVXOrc49KJEeZ8WW_0pD4W2PSSJV9UF6OHDfG-xw0ejOEumv375YH7rDIHe9qeZU6vvlMT3v1nw38yVEZRxrVHJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b0dd1cee.mp4?token=oxqPBdXjY9hUqD7xWU804I8bsQTD36YOSoiHbMWo4TKixQNnYXCaI-ZKw0234XuFFmBvYF74HW1wbLQDUpn_IT3x96MgE6Wh_M1TBmAHcU5sQAyuhnZE9scdD6TPlCSY9pfDFDeMGmqYxGnfV45ICQVXw1tOv04dI99OlNxZoMuLu8sD_1rXi4sDBAiJHBOhdyEhsGhuP1LB6MxfaEQyjNHYgHUNeU9Drv_d85S1g51Hovzpc2DSefi15Z5MhkPVXOrc49KJEeZ8WW_0pD4W2PSSJV9UF6OHDfG-xw0ejOEumv375YH7rDIHe9qeZU6vvlMT3v1nw38yVEZRxrVHJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی کاخ سفید کارولین لیویت: کوبا به دلیل سیاست‌های کمونیستی چند دهه گذشته در آستانه تبدیل شدن به یک دولت شکست‌خورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137000" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136999">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ به آکسیوس: روابط با بی‌بی بسیار خوب است. اگر او اینجا باشد، با او دیدار خواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136999" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136998">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی:
ایران آخرین پیشنهاد آمریکا برای صلح را رد کرده است.
🔴
ما در حال تلاش هستیم، اما ایرانی‌ها تمایلی به همکاری نشان نمی‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136998" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136997">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی کاخ سفید، لیویت :  توافق هسته‌ای با عربستان مشروط به پیوستن عربستان به توافق ابراهیمه
🔴
امیدواریم عربستان خیلی زود به توافق ابراهیم بپیونده
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136997" target="_blank">📅 19:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136996">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از مسئولین مطلع:
هر دو سازمان سیا (آژانس اطلاعات مرکزی) و اطلاعات دفاعی اخیراً ارزیابی کرده‌اند که نوع بمبارانی که ایالات متحده در حال حاضر انجام می‌دهد، بعید است که موضع مذاکره‌ای ایران را تغییر دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136996" target="_blank">📅 19:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136995">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ به  Axios درباره ایران : آنها هنوز به اندازه کافی درد و رنج را تجربه نکرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136995" target="_blank">📅 19:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136994">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
الحدث: انفجارهای جدیدی در نزدیکی مرزهای عراق و کویت رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136994" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136993">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136993" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136992">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ به آکسیوس: ایرانی‌ها خواهان مذاکره هستند اما در حال حاضر برای دستیابی به یک توافق آمادگی ندارند و هنوز به اندازه کافی رنج نکشیده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136992" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136991">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ به نشریه اکسیوس: اسرائیل در عرض دو دقیقه به حملات علیه ایران خواهد پیوست، اگر از آن بخواهیم، اما ما نیازی به این کار نداریم و به تنهایی کار را تمام میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/136991" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136990">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
خبرنگار: آیا آقای مجتبی خامنه‌ای در قید حیات هستند؟
🔴
نتانیاهو: فکر می‌کنم که بله، زنده هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136990" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136988">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بیانیه‌ی کشورهای خلیج فارس و اردن: از شورای امنیت می‌خواهیم قطعنامه‌ای فوری صادر کند که خواستار توقف بی‌درنگ تجاوزات ایران باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/136988" target="_blank">📅 19:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136987">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری / تهران و بغداد خواهرخوانده شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136987" target="_blank">📅 18:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136986">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
دقایقی پیش صدای انفجار در قشم شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136986" target="_blank">📅 18:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136985">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883d56e3de.mp4?token=OTrBjwVnzIMzO97vahN0-86R33pEXSJc4HputwJTFNQLt711eygrew7lIShskpo8jnAkiGjRAoVtvR2VGLRu4fi5ZJMba7okoA9bVBnZ3cYUV54vMqNEwvzS3ZpTM1VFOJwnJK0aMpU6hNP9hj4tpzEhruqdgiT1gr-DVP9dhHCYAlYvflv8angpvjpJE9S0Y1O_PbWRt-IOFTPGs8wS7To9O3_1wCXKOhmUxZgyMj9l2173cbNyarLAu4CcBxmDkXU81_8ZULuxRJCkosWGKniEtyV0KoEobkXupJYUYICreCln7KTBB0cMOfzdGVMgjWGXKnKFcg5Uo_0tMGwfoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883d56e3de.mp4?token=OTrBjwVnzIMzO97vahN0-86R33pEXSJc4HputwJTFNQLt711eygrew7lIShskpo8jnAkiGjRAoVtvR2VGLRu4fi5ZJMba7okoA9bVBnZ3cYUV54vMqNEwvzS3ZpTM1VFOJwnJK0aMpU6hNP9hj4tpzEhruqdgiT1gr-DVP9dhHCYAlYvflv8angpvjpJE9S0Y1O_PbWRt-IOFTPGs8wS7To9O3_1wCXKOhmUxZgyMj9l2173cbNyarLAu4CcBxmDkXU81_8ZULuxRJCkosWGKniEtyV0KoEobkXupJYUYICreCln7KTBB0cMOfzdGVMgjWGXKnKFcg5Uo_0tMGwfoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوال: لیندزی گراهام — آیا او حذف شد، یا مرگ طبیعی؟
🔴
نتانیاهو: نمی‌دانم. ادعای آمریکایی این است که آن را بررسی کردند و مرگ طبیعی بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/136985" target="_blank">📅 18:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136984">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aeca53222.mp4?token=QtdMLUnc16aFJJqOBWOo8Rb5AXgM9ZBs2-yCVLVy1VpyNBsxPFawcdU9s5b8CN75GPSIoClmudWviY1wIIlRDJaUlMulquex15kScF03jWsd3ppYV0vzu3jDFmDNXubHuhbj51jLF53JHb7epEbVfF7cFqwubVDs3IyZmQ0Zt8WMAN6yZ1BENYANbgPAp5bl95DAH8ySaBdXPFgH5mrMBTHt9bSswydNTLsxbtqt1FBfGZjKtU0OJL4pQrZkBZHHJJK_ZXZs-80AqX9Jnl3sxhQZulnM82H8s_H5L7oUlw6CWc-ReGYlujrC21OUniUdJaVgpkovSnIdu8bdvMTtvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aeca53222.mp4?token=QtdMLUnc16aFJJqOBWOo8Rb5AXgM9ZBs2-yCVLVy1VpyNBsxPFawcdU9s5b8CN75GPSIoClmudWviY1wIIlRDJaUlMulquex15kScF03jWsd3ppYV0vzu3jDFmDNXubHuhbj51jLF53JHb7epEbVfF7cFqwubVDs3IyZmQ0Zt8WMAN6yZ1BENYANbgPAp5bl95DAH8ySaBdXPFgH5mrMBTHt9bSswydNTLsxbtqt1FBfGZjKtU0OJL4pQrZkBZHHJJK_ZXZs-80AqX9Jnl3sxhQZulnM82H8s_H5L7oUlw6CWc-ReGYlujrC21OUniUdJaVgpkovSnIdu8bdvMTtvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانياهو: در مورد حذف نصرالله، بحثی وجود داشت.
🔴
گفتند باید از قبل به آمریکا اطلاع دهیم.
🔴
من گفتم مطلقاً نه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/136984" target="_blank">📅 18:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136983">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
قیمت نفت: ۱۰۰.۶۵ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136983" target="_blank">📅 18:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136982">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: کنکور به موقع برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136982" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136981">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
بنیامین نتانیاهو: من بلافاصله پس از انتخابات برای دیدن ترامپ رفتم و با هفت اسلاید بزرگ به آنجا رسیدم.
🔴
اسلاید اول، اسلاید دوم، اسلاید سوم، اسلاید چهارم — این‌ها کارهایی هستند که قرار است انجام دهیم.
🔴
نه اینکه بپرسیم «آیا به ما اجازه می‌دهید یا نه» — این‌ها کارهایی هستند که قرار است انجام دهیم. به او گفتم. و وقتی به آخرین اسلاید رسیدیم، گفتم: این پیشنهاد من به شماست.
🔴
شما بمب‌افکن‌های B-2 دارید — این بمب‌افکن‌های عظیم. سایتی به نام فردو وجود دارد. اگر نیاز باشد، خودمان هم علیه آن عمل خواهیم کرد. اما بسیار موثرتر است که شما بیایید و بمب‌های سنگین خود را آنجا رها کنید.
🔴
او گوش داد و در نهایت به ما پیوست. و من بسیار خوشحال بودم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136981" target="_blank">📅 18:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136980">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d81db4c.mp4?token=epMNS_mP6AIjggklz54EEtFsnIusZtut2hb1OEx34NY2h42eW9eepVE4NMgRHfhY5CtrsqYuDDnE-TSrqBjsdot7LmAsi4nVrrShL4f2YJ-qT5KKMtNDt12V7kx7phXSoYrFKpoCC3B8RC8vK7c80PbfGCDNbXRqClNbTzyxIxspR4bNz6FFDXNqD7Oh7sk2r-LCHQcEM2frV4Dg446ylYh-WHSMr4DBmX_ludvxxr4toZ5S6t5VpkEMLborTI3A4OGgoeDpC-3utPdZyW9tN__hg6t1qdz1NBp3TerUjAWs7GXzmwR_bHShzG5rcvmRXs4v40hSA2CEZCvvihFqhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d81db4c.mp4?token=epMNS_mP6AIjggklz54EEtFsnIusZtut2hb1OEx34NY2h42eW9eepVE4NMgRHfhY5CtrsqYuDDnE-TSrqBjsdot7LmAsi4nVrrShL4f2YJ-qT5KKMtNDt12V7kx7phXSoYrFKpoCC3B8RC8vK7c80PbfGCDNbXRqClNbTzyxIxspR4bNz6FFDXNqD7Oh7sk2r-LCHQcEM2frV4Dg446ylYh-WHSMr4DBmX_ludvxxr4toZ5S6t5VpkEMLborTI3A4OGgoeDpC-3utPdZyW9tN__hg6t1qdz1NBp3TerUjAWs7GXzmwR_bHShzG5rcvmRXs4v40hSA2CEZCvvihFqhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی پیش یک پهپاد نیروی هوایی اسرائیل به مواضع حزب الله در شهر نباتیه الفوقا در جنوب لبنان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136980" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136979">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
مشاور رئیس شورای عالی سیاسی یمن: در صورت هرگونه تعرض آمریکا، ما به کشتی‌ها و تمامی منافع این کشور تا آنجایی که برد موشک‌هایمان می رسد، پاسخ قاطع خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136979" target="_blank">📅 18:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136978">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e404c630e0.mp4?token=FfCK6wHHC_wq_pkh6O5zSWmz8EFoutlQB9brttvbVLAuCjqjh5dibS8mAXQK4r0u93zK09KU-Z24t56oNSfOh5adMBQ_zE_4_jKIV6XM84-tXMjMh50X4QryGVA-KJwriDqBCAyX92pB-oLZtRTf5ArD1o-eve2wID-YtVynXJlFnDdDUk1diTK2ubCVzguNbZT6DPbsvtjj0LYOKnwNjhCCC_Np0LE6o6NJNBVxPjESA75menCdID2Hh6UvTK_dJgVlZ94my_tY90FH_DHZW64U5CutlCrqwcJF1q8P32E57tFMQS1SqtWp_GplenXlB0W-ZbiRU-nRHsqpxegbcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e404c630e0.mp4?token=FfCK6wHHC_wq_pkh6O5zSWmz8EFoutlQB9brttvbVLAuCjqjh5dibS8mAXQK4r0u93zK09KU-Z24t56oNSfOh5adMBQ_zE_4_jKIV6XM84-tXMjMh50X4QryGVA-KJwriDqBCAyX92pB-oLZtRTf5ArD1o-eve2wID-YtVynXJlFnDdDUk1diTK2ubCVzguNbZT6DPbsvtjj0LYOKnwNjhCCC_Np0LE6o6NJNBVxPjESA75menCdID2Hh6UvTK_dJgVlZ94my_tY90FH_DHZW64U5CutlCrqwcJF1q8P32E57tFMQS1SqtWp_GplenXlB0W-ZbiRU-nRHsqpxegbcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا روسیه به ایران کمک می‌کند تا به نیروهای آمریکایی هدف قرار دهد؟
🔴
وزیر امور خارجه روسیه، لاوروف: چه مدل موی خوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136978" target="_blank">📅 18:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136977">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBtnx7jEqL027YqX8ZQtvIV0Wa8QFs4Ov27OByQpWXkV9dMQWL9wRzO3E2wDUaJTkCKBXcXY-QN7DjDvH747lNDqgSGnEbhteQn8DOX2fwp2qcaSfqD4hf7V5qCjWtMTyf7I-rMhccBFaiVSaFl_05mRmlM5dnHckcfXuLZUU8xRHmjjI0cUiPM7CKKdPSM85WA7AAxIHWM1c4AbVNlCKWlTXUxATgCI264jnlHT5rqnfpwMvn0v--qjujnvzvHrkxfHCvFey-kl0mLHbpDfKH5V1zNLg0mo87Ky0qxEdrMmboRcOS14wLZ0KkstoAnl493pjQiMCP71D4A202PGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت قالیباف بعد از 100 دلاری شدن نفت برنت: اونا می‌خواستن ایران رو تنبیه کنن.
🔴
ولی خودشون رو با نفت سه رقمی تنبیه کردن.
🔴
استراتژی 10 از 10
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136977" target="_blank">📅 18:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136976">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEkFzb2QgSAwvhx5kK4VsIHu7Yx4OF7tX7wj4XaAgQWckq2qGkfItBSd19kHgvMVfQ_wImdPSOwDD946PjJZSaSh6fEmFqfiehlUEN8LG_zg_-a1zMN6AXRrERoDajvaE24gt-0b8YvNGJ1ZGP6Rnh2vULzbQb65WvxHTri6gppBFC9eQoIaDESrTuvCWKYWC3C5PUUuoWWmMHlM8jw519Dkge1zx3-DTXigUs_Q8zC_UerLyBOpcKX0eI-CBQQSTQAo0CWt6VJsZaKNcIXX6TB_sZLc4BbjkKe1uVxj_jkuw0B-abZN1WDS930U2QbkRHKzPZ59bpZyQfITmdTgEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه فاکس نیوز، فهرست اهداف زیرساختی ایران رو منتشر کرد:
🔴
نیروگاه‌های
🔴
دماوند پاکدشت
🔴
شهید رجایی قزوین
🔴
شهید سلیمی
🔴
نیروگاه اتمی بوشهر
🔴
کوه کلنگ هسته ای اصفهان
🔴
سد کارون 3 و سد شهید عباسپور در خوزستان
🔴
مجتمع گازی پارس جنوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136976" target="_blank">📅 18:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136975">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
مجلس نمایندگان ایالات متحده، طرحی را با عنوان "تفویض اختیارات جنگ با ایران" تصویب کرد. این طرح با هدف محدود کردن اختیارات رئیس جمهور ترامپ برای انجام عملیات نظامی علیه ایران بدون تایید کنگره، با رای 214 به 208 به تصویب رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/136975" target="_blank">📅 18:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136974">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اونایی که کنجکاون چه ویدیوهایی بوده، براتون چندتا رو گذاشتیم موقت
😂
◀️
مشاهده فوری</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136974" target="_blank">📅 18:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136973">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رویترز به نقل از منابع: ایران این ماه برای حوثی‌ها تعدادی از فرماندهان سپاه و تجهیزات مرتبط با موشک را فرستاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136973" target="_blank">📅 18:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136972">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5233e33b.mp4?token=SYUVndX8_S9gpVA2p8fKi4sXM5j2QcIQeubb9LO-3gzr8gRG5Vaq8jt7Y3zPpFETLy0RlUc7NaDGFU7w8HsP5RquCaVJDZL1AEvkvVeL5dvqvKsRiiWKhi49nf8aRJstCqWnIWT67H17VMZcJWTFL2zcMkI2vbXoeSWHMGdZuqy831EpP18RgDvkf-FMNkc5yX4CppZlZg591PeXnERbSsqri2s3v3okV_26x6w6RWOTsu8649-AgRYFLF0TseZQk-eRdK_LmpbarOwWYvSX66-h1TIgTWZZQiwtAMIhzq1YJGqloPthjtyO-q1pIHiNX3IaIjA-TPTIrJUjUKJ8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5233e33b.mp4?token=SYUVndX8_S9gpVA2p8fKi4sXM5j2QcIQeubb9LO-3gzr8gRG5Vaq8jt7Y3zPpFETLy0RlUc7NaDGFU7w8HsP5RquCaVJDZL1AEvkvVeL5dvqvKsRiiWKhi49nf8aRJstCqWnIWT67H17VMZcJWTFL2zcMkI2vbXoeSWHMGdZuqy831EpP18RgDvkf-FMNkc5yX4CppZlZg591PeXnERbSsqri2s3v3okV_26x6w6RWOTsu8649-AgRYFLF0TseZQk-eRdK_LmpbarOwWYvSX66-h1TIgTWZZQiwtAMIhzq1YJGqloPthjtyO-q1pIHiNX3IaIjA-TPTIrJUjUKJ8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی چند لحظه پیش عملیات تخریب گسترده‌ای را در منطقه کفار تبنیت، در جنوب لبنان، انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136972" target="_blank">📅 18:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136970">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EYpGwv0eESWdKqePcp6XUdoGKFUptuH7k3HV0ceiHJ_fxr41pahajORZ8_--Zj8L6jJt0kEkIUVya6dYFz0v1lhTKuuAKcpqAXrTQ9Pe5aGzuHhoG88R2bz2zhwaCBbUFwUUPN76tXKOdlg59yE-Teb9tnZ5IblQ0fdxnqOLDxuHNG-abqxZ4vStVU11orMK8Fee76HN8SsN5H6h9OFmN_8yjfeyF4GRQ83mGqZ8qjI5u1aZ4jC6d6vIkOY3Wmc_OeEzPbSIZRJcFI_Kvs9zgWW4EX7uBMYG3mLt8eu2tIneh9B7cC8BzoPNHq-PZU53cvJHe9E2byEEvNQfRm2GeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ta_bxUiCuGLleL3ZZGOGfKQcPORpgpyyB3A5FqisPxy1qSYtmy7ia6T_arAhMq2hgsE773pV-rOV_qrP28ZevT-L4bEJBxNBUhxr_sdPdzd8h94k-3yJExaPTnfXzOGH4XljeDQm2fXJORAkiKtiewLhn3Xnaci1cW5d19UcPW2vLR_R4tvdjw10E9LCOuf7FjYpoVS-7p3Mhu3fnaF13kA3xsGoUOfoDtcf5nV_PNACjqsdvsSQMkpEIbgl_w8qIw2_8V2Tk2ppp21frjV3T3bybjcwG-_ZPx1-NFz_wbSat7ovNPOHy1Lio80mSKfzRrBMVNufnGpvdgX9p2i7Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پلیس فتای استان خراسان رضوی، از دستگیری زوجی که فیلم سکسی ارباب و برده ضبط می‌کردند و سپس آنها را در تلگرام با قیمت های نجومی می‌فروختند، خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136970" target="_blank">📅 18:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136969">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
تایمز اسرائیل: بانک اهداف کاملا بروز شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/136969" target="_blank">📅 17:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136968">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
عراقچی هم به قرقیزستان رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136968" target="_blank">📅 17:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136967">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQhy6O6n5wg3s2PtWw9IsQBnR3U40-CgR22lH6UA42KYZnEZyKg2KZsWIS6Jjcf9Qt2Z4AIyw7NxDIeF63-QJedsRRyg6UAlnpumQWVbx4UP3dcA9FdMLA_me_9NL0fxpYgccilOQI4L41wP1nc5PqcVjhvIMp6XE-gfRNmtv3PcwspI4PlTGEgvg6Ad-hD9PHk_K_M5zKi-pfAUwPffO9SiWaFeEZ3HbI99ERFnJIjt3quD3Hqb2FcSfQeqipt1_WZZwSO0LeDWoTesm-jISZ8G_NiMscWKbEqzPAqnNoQH8bQnElhLFraIsQA6vkXJE-ol4teTs7MUeCFb45PTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکندر وارد دهلی نو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136967" target="_blank">📅 17:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136966">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سپاه پاسداران: پایگاه فیرفورد در انگلیس هدف مشروع ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/136966" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136965">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHXQaUyurWJZbzGHliyIqAY0csDpxIHCubwXxd4K5hYY_Eir4TsDrxFBz1JHFUi4bvValYT9Ew4O9vI2_qRQLNIyD0O3TuA_v04HBhF8y1yOz5ish0Lbz-dm974c0fFuBXiaubonxKDULKZ8Z2k2Gnxq9GcfhBrY6KuII8XRSKpY7sAU9e_F9fHp_ilIwDto4lmdIX7qgAIX0i6c5yYtr92CtmpDFh0pKKi80J7_9WJZnpRNd0ymm16upZKel1lIR-7CPXCju2qqcWDPaT9Oo_l01cBEx8lcznDr__GXyoGBsXAbCaywJ9iOrKBFQyk6PQ5AZbpPwA6BNCoY3k36sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت برای اولین بار از ماه مه به بالای ۱۰۰ دلار در هر بشکه رسید که عمدتاً به دلیل حملات یمنی‌های حوثی (انصارالله) دیروز به دو نفتکش سعودی و تنش‌ها در تنگه هرمز بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/136965" target="_blank">📅 17:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136964">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPx7SlV9sCX07mgL5r7nmlv4_htSpIXpvlJW8uxhuO7rKTjTdVxlqANu3FBHbNJb74_wOG_EgXEJ69Osr7NdrBvnupPd9qqZzMWhdy4SVGedFAVXJGCWSUnYOHRinjOVEaEQkS22U3A98UBZRySSewf5iPE_lTYAt_YaKmFPmZkL4mjlPJ82gEL3T_GmOwmfgpTe3T5iKoqj8oAWJpN-CBCYcR4w7wxN3Q-pM3plZEzqj_AdjPx2n8DxuFnmaohBokn-0sr7whHDH5mZYVTLrpReR3ujlnJSRrDAjUEzEBaAcTyl4DTy71u-rRnr7WptUnhB3LRgO305GgkVCCPLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال تایمز
: مقامات آمریکا معتقدند مذاکره با دولت ایران به جایی نمی رسد و برنامه تغییر رژیم را دوباره در دستور کار قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/136964" target="_blank">📅 17:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136963">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03794fcb99.mp4?token=C6YkqPB4p0-KKTdVHxcwJi7be5ZYW00jlpNUxs40FJSraItKtyHGmA_dVpQLy9lKGXRnYwvbmWsyxpNJC2d840MD3dFfxupbmMxWfdIo4DCcge9ziRGvJVLcx7vgrUhuXEobTJRD9uYyD-EdqivKMJqBG-Cqz6Q8CXQTcULaC1-FC-U0Kq5Iy2z_O2MWHCTs2NbFHdHZiVM3Y5hu65lspVHsbyMeGURFbAufcIFNcCom1pKeMDcgzxp7229L4fAnmuR2qIoneHQUiCFxnEd_MNxRZ3mfeSSZ5JNGOrOiNA5tN32dGwOIqMPDolw4vcJOyc3tReK1w3UrgYzuXQv0Cp8ShT9kPgNZLAVKIVh9GZsMXmZQDwkPOwxJI8X3vRjwprNRG_Shv6_e6VZsqW-3yR16pNKPhehsDISH5S9eXi8YihFeTBzYGSJJms2dtebvccCUji4ghcYS2MkBq7dImn189izPwZzVo-fsSuzLmKEW1DD7AvTC-cAECMq0cYFW0Mj86pdph_2lDzU5F2yohDsKN4n_XVE2AHcckUBzgE5SZWLBkyScqLfXMm0zVL39Lr89h8JIOt5WhI0sJL3ge6k9xLR6xRXdoSrcA3CiY7CMZ4qr9JgwLpHR0c634HzIbMrpuZRUgOB_HBUfybDL11YC2B73sBJYHH6XW2rR5Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03794fcb99.mp4?token=C6YkqPB4p0-KKTdVHxcwJi7be5ZYW00jlpNUxs40FJSraItKtyHGmA_dVpQLy9lKGXRnYwvbmWsyxpNJC2d840MD3dFfxupbmMxWfdIo4DCcge9ziRGvJVLcx7vgrUhuXEobTJRD9uYyD-EdqivKMJqBG-Cqz6Q8CXQTcULaC1-FC-U0Kq5Iy2z_O2MWHCTs2NbFHdHZiVM3Y5hu65lspVHsbyMeGURFbAufcIFNcCom1pKeMDcgzxp7229L4fAnmuR2qIoneHQUiCFxnEd_MNxRZ3mfeSSZ5JNGOrOiNA5tN32dGwOIqMPDolw4vcJOyc3tReK1w3UrgYzuXQv0Cp8ShT9kPgNZLAVKIVh9GZsMXmZQDwkPOwxJI8X3vRjwprNRG_Shv6_e6VZsqW-3yR16pNKPhehsDISH5S9eXi8YihFeTBzYGSJJms2dtebvccCUji4ghcYS2MkBq7dImn189izPwZzVo-fsSuzLmKEW1DD7AvTC-cAECMq0cYFW0Mj86pdph_2lDzU5F2yohDsKN4n_XVE2AHcckUBzgE5SZWLBkyScqLfXMm0zVL39Lr89h8JIOt5WhI0sJL3ge6k9xLR6xRXdoSrcA3CiY7CMZ4qr9JgwLpHR0c634HzIbMrpuZRUgOB_HBUfybDL11YC2B73sBJYHH6XW2rR5Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا و سیما: وقتشه عرب‌های خلیج فارس به دوره شترسواری برگردن
🔴
پ.ن: یکی نیست به این مجری احمق و معتاد بگه اونوقت چه بلایی سر ایران میاد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/136963" target="_blank">📅 16:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136962">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=U6CM3AyEvJCmKyAbD3_bHTtMbtiMUhltMBGwm7MRYWRxO7ySMFBxv_SGUi75ZbYxF6XqKDCcz23GeQZnha7J6N14T0q7lwVyb7ZolmXvEjhETklzpdywVeqO9NqdsO280mQqbC7j6BdIUIu2GRUdcnFrMzW8Oyq_-ZenYqFUWEaWtcU-JsmTs2w7S2QC4Lq6kU9fp-EL31BayN0bNTc8gKPJqGCqM39M8WnUA_MVcL6PzoWe8HPvn0nuhyvSJsEmFyQ6xUWdF-_S1A-JLMKYi-UCy7AHMuE_QLr_xePhYISY78nXjXExuQ39qfMFvilf-9VSM4tKNeJB5TkLb3WENQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=U6CM3AyEvJCmKyAbD3_bHTtMbtiMUhltMBGwm7MRYWRxO7ySMFBxv_SGUi75ZbYxF6XqKDCcz23GeQZnha7J6N14T0q7lwVyb7ZolmXvEjhETklzpdywVeqO9NqdsO280mQqbC7j6BdIUIu2GRUdcnFrMzW8Oyq_-ZenYqFUWEaWtcU-JsmTs2w7S2QC4Lq6kU9fp-EL31BayN0bNTc8gKPJqGCqM39M8WnUA_MVcL6PzoWe8HPvn0nuhyvSJsEmFyQ6xUWdF-_S1A-JLMKYi-UCy7AHMuE_QLr_xePhYISY78nXjXExuQ39qfMFvilf-9VSM4tKNeJB5TkLb3WENQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
باز نشر
🔴
شهریاری نماینده بجنورد به ثابتی: تنگه هرمز مال ننت بوده؟ مال عمه‌ات بوده؟ ارث باباته؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/136962" target="_blank">📅 16:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136961">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOAwT58po8BBfQID8kz6rWKew9X2efRDycZqTpjbwf5XwlN_Qiu8DXqK_9HpMue1nnDFXMmKkSL7i4xxilKu0KY0bidgvfCnppoHMZRQTOSOQ_SnWFMJMZh93rxTQGgGqhAYSodQGZPA7AOP9JdAMnSe0WYj4EmXECGcqD_hWuxtauEmA4RqDn1eLB8hPvIfpYjYoqP_wO6EoSEV7mrgsnxqIHCrsSIpMVhtYWGoNJh-D2f25SPZUccGWjE9iVWLapUsjQ5XVrv-fEN8ddmjONzDQbMn79SDNkqNFHelyzZW-p_cvoCmvtsqQI9scURx9dfIJI7VhjiYTjIMGi4YhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موج خروج اسرائیلی‌ها از کشور
🔴
هم اکنون فرودگاه بن گوریون
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/136961" target="_blank">📅 16:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136960">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gQA--exuyRcDZunrS5Z5hHEyF2j7327qttHQ_lX9_Wt3l8rxIqVWJWhtp7e_iTK4XScZr0VXh3TPbF51b-vQ6UgTrjw2bwPwKY8vyiHmYuBs2ftIEL3xxnPmGrmcIYe3TOdmO7ZHz6iA5RhmQnAIEGjLU2ZjURgBCEbNyUeH3fd7I4HqwBMB3Nx_qSeUScHA6ytBpZlsTeWtY731ys3OLRxDASVZll-H8IfdKH05Uh3CQAnlJh0d6z7JWvf566q_s5_GmjmWaKttUcsmCDdvhEJzZgf-dTwLxOardBe-oGBp72rrEUbf3G-dj2VAI87lQNjCkZIB7-4Sp3U1irZ5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آخرین پژوهش ها، مردم یونان با 164 بار سکس در سال، بیشترین تعداد سکس رو دارن.
مردم ایران هم به طور متوسط، 50 بار در سال
[ هفته ای یکبار] سکس دارن.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136960" target="_blank">📅 16:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136959">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نفت: ۹۹.۲۴ دلار!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/136959" target="_blank">📅 16:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136958">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L44Fp92yQMa0q4hD7iYBRUwLuBGw2EGtQeAPIALxCLqY9V6GPOB6rQW-0bSnK2R9BDosigqXdQ_hgdCZV0bGrZaQHGXgRsdGwAlTqlDssi5bJZLbZN8Vqsy7V9qmUyQbiASPc_K-zVfSP6SC0evOqwqt2Lr7Ynvs6EN1q1Y-Aoc3eeIgk9578tAyIYTamRWx12thvH4xME7bnFrllVpTdby2idltpxyMDag1Tq_j-Z5P-R4ayo0QqX15OkFbxs2lHfFBEwtmN28zb6r_kazjwnleWH9YU9MgqfmBslV2KjRGaaodinmzw200b4e2otxXCVYkfeNh0NVoUx3UPWHbQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه صدور مجوز استفادۀ آمریکا از پایگاه‌های انگلیس علیه ایران را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/136958" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136957">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnAyu-Fsd9VYAn0Od_lDIaCTpJR8ran6IDdqQnDVlTs-agjGcJNEgILYdjF5ZhHZahYTes71xF5GiS8OrjjEFUxr6rhrlqZnERM2s55gurP1yigQZHBM1lZazBtPp8viHz81MMixKlsah3jRBsiX5v_Hnw9cloL4abIngAynn0R8cr82pfftxKAy-1pCOtaKZ-dKBmyFyp63QLEgjip87r1cfKOGL3CQFjs1qqogWGTXNfNHhhErmpqemnkstQgD1XOBmAC4q4W0F_wyT_8l1U4Wnmp-NLqzMs3rzJtQmjO-Zc-NDY0p3If7qTG5JzuqWmLMyLvCtkOZKgfJvLumjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social: یک سال پیش، ایالات متحده آمریکا به طور جدی به حوثی‌ها به دلیل دخالت آن‌ها در تجارت و بازرگانی، با شلیک به کشتی‌ها، حمله کرد.
🔴
از آن زمان و در طول درگیری ما با ایران، آن‌ها به طور مسئولانه عمل کرده‌اند. متاسفانه، اکنون آن‌ها دوباره این کار را شروع کرده‌اند و شب گذشته به دو کشتی سعودی شلیک کردند.
🔴
لطفاً این مطلب را به عنوان این درک تلقی کنید که اگر آن‌ها دوباره این کار را انجام دهند، ایالات متحده ایران را مسئول خواهد دانست، زیرا حوثی‌ها یک ابزار و/یا نماینده ایران هستند، و مجازات‌های نظامی جدی بر ایران و البته خود حوثی‌ها تحمیل خواهد شد. من از عملکرد آن‌ها بسیار ناامید هستم، زیرا آن‌ها تا به حال به طور حرفه‌ای و هوشمندانه عمل کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/136957" target="_blank">📅 15:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136956">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9K7IJUxj1z7PLC6INmkgGmm04RjFvrxpRr5wcC_ABgXQWt49kDq3g4wH5klaSZ_XQrQ7zaUWZACxeQBeInGRs05jJvUQBDxflEq7cXD0a8aYJPJk6eW9ZG0GljKDaFRF75k-7Ao_ZC14XfrueqYdWU9Eba01hS0lKUQw2SQzdov2ukZ-wBrU7RBTzyovwWudQ5BjhgFILEvoBVAxAyM0akHUdGNKdf2Iwf7e2GUtiGcQ3tAvsOi8zgTaY160SGJiBpq0kmcalJnZr-wpU1SQJQLXR9ecb9V4OtcG-mKU0mIDeCvsVQ2It9rAh8ihV5r-pEKolOiqqAtCDknX2uGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش نشریه فایننشال تایمز، لورا لوومر، فعال رسانه‌ای حامی ترامپ، با رئیس جمهور زلنسکی در کی‌یف دیدار و گفتگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/136956" target="_blank">📅 15:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136955">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e803bd871.mp4?token=da_eD8pCOzvp2IPjQuRt8TEjHFZlg9FyzP9_c8pmYWITsXGhTZoRk5a707AXHV0jdmBqO3Ic0YvYVfRDJIr7BFYls8STH12--c6GL2aFHAaPwAvhWKtXk6_iFDzMYJwJrWR2DHOSzTgHEHWcAVgZ8mmFefO6XYtDPXDP9QXHC1vgItAb0jdLAE6s70pG94BWC-RxRkOW4WvM0Pn3rtZKk60emKED0dk-USwby3lvNbchZkbLpKlyRRCrkdp6Z51SfNPGs21DDOR98lbvn8XJlwSY3RkuUetLjPZ98Qmze4_e6-mfRi0AwCPplPIFojb-41PpAPL_f0VmjtL2e3dEtly_Ua3PZoCf_FAYADsf6Yq7IP_VOXn-hWkAYwyS8Lru40rlxrGlWAkZp7ur4rgHQfXhhCiMI1u2V542XEaCbaqiYS_tgcVOV9vfs6KqJBTmfWMkmcgb-psDZa4wvItYrJ1xFfVIZtrU6yKgRsJroqfrIN6-7lUC2ZWmpJnI5LbZwl5L-FCpRGH3pKJIO4Jb1ihwo2WnTdoARxeiDtJhhOpS7vkNuMfGZAyGCNydRaQChLfI8HNSVePqCn-9r_rnoaFpEkN-lQiBkoWVaQi16BbcFwkjLyxQN_pQc8bNGS0VjB5Sth1dI5MW_-0VPMSsCj6YnAgeLiXigfYIiVkJz2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e803bd871.mp4?token=da_eD8pCOzvp2IPjQuRt8TEjHFZlg9FyzP9_c8pmYWITsXGhTZoRk5a707AXHV0jdmBqO3Ic0YvYVfRDJIr7BFYls8STH12--c6GL2aFHAaPwAvhWKtXk6_iFDzMYJwJrWR2DHOSzTgHEHWcAVgZ8mmFefO6XYtDPXDP9QXHC1vgItAb0jdLAE6s70pG94BWC-RxRkOW4WvM0Pn3rtZKk60emKED0dk-USwby3lvNbchZkbLpKlyRRCrkdp6Z51SfNPGs21DDOR98lbvn8XJlwSY3RkuUetLjPZ98Qmze4_e6-mfRi0AwCPplPIFojb-41PpAPL_f0VmjtL2e3dEtly_Ua3PZoCf_FAYADsf6Yq7IP_VOXn-hWkAYwyS8Lru40rlxrGlWAkZp7ur4rgHQfXhhCiMI1u2V542XEaCbaqiYS_tgcVOV9vfs6KqJBTmfWMkmcgb-psDZa4wvItYrJ1xFfVIZtrU6yKgRsJroqfrIN6-7lUC2ZWmpJnI5LbZwl5L-FCpRGH3pKJIO4Jb1ihwo2WnTdoARxeiDtJhhOpS7vkNuMfGZAyGCNydRaQChLfI8HNSVePqCn-9r_rnoaFpEkN-lQiBkoWVaQi16BbcFwkjLyxQN_pQc8bNGS0VjB5Sth1dI5MW_-0VPMSsCj6YnAgeLiXigfYIiVkJz2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهریاری خطاب به ثابتی: در مذاکرات اینبار  هم شما با همین اراجیف تون نذاشتید پولای بلوکه شده آزاد بشه!!آمریکا میخواست پول های ما رو آزاد کنه و تحریم ها رو لغو کنه ولی حرفای منتقدین مانع اینکار شد!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/136955" target="_blank">📅 15:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136954">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / فرانسه کارکنان سفارت خود در تهران را تخلیه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/136954" target="_blank">📅 15:39 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
