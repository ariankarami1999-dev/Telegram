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
<img src="https://cdn4.telesco.pe/file/IrqY-hBrIozaRRJ_awMicG7B3J-DiSl20Kq-jgaV_nQGen9fYzsdQsiLiA3uMF2cruf_RjZWeY82fgpYbSfmc5_oNiVWmlPLXjc3dLU35ZTPy1MD78LygHDPf-eMcPK17Ap8ZYq3xyJ414dkTE16DQd-S7oQofuh9idjssbdCwkFLGcsQu1JF0eD9EyVinwW6urUcckXnZnIYqsxnlM82UmaIrFnV0pX-0N67zBw6D5DXFGGP8NVfBVTBJ0n4UZhf6dfOGO7uSgH9Drrj3k5Mqi4ZnKsb1TCl4gjsfYgzEckYS9CJgVoQunBCKjAwreFOJoCzeAgIgrRWIuE0zxG1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 118K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 13:55:23</div>
<hr>

<div class="tg-post" id="msg-70609">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJgQKNZp42lPrkkj4hNK-3eauC4r6EFmwf0z0h6v3pk_eQ1VuTjouAHSdHdTM7e7ExA1andi5IeFCqneg5bgFveoUm5gAq9Br8pFdlLwfSWyUWZ35Qxxgry8rXn17eO3M1tj2jsPyfTA8gZ3L2ilw3K69_OOhS4LHzVYwM0bdEdsWBdPaCYhohL5cyNPGIkMcWHZK-dLRlBku_LyV2wPMqldr-1ZS0fSC_aslvDtoW0gZ5WDNY-D8M9JfzB58pBM7kJR1jn1qcNUvZP4ZCwvzssh0HiUiy8MtLbxEEvWtUmfpxTPaQireJC_ayfQjIMAcaQgeDMOxLu_Y3slxNMDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زمان شاه هر اسکناس هزار تومنی، معادل ۱۴۲ دلار بود!
@News_Hut</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/news_hut/70609" target="_blank">📅 13:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70608">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=DQv9IOswWGSCcbPG-xB6n7D3WOB1mfdgtiR9LtOTfZYaiOub6H7NWTX-s7GNjQOfOxGturTwB5iWLLl_kA8EcptcKvm1vLGl9q1EHMAcu78ZEETNDvqmBPpcV97NWRbgh--ud6LSfgMJUdF8vdHfKzXLjUnQzBW6kXAWbiJ75ObE7rJ9BUfgxEysYk26LUyuqATxHIYAlwhRTA2xEqusCioi_teNeoYPuPLFCPV12UFhu-VHtxBcBKDenSRBk6zyIIqLCQiwGdLyCoxe3CKd6AKfyipYDdwzMQPejxH4708WtPMmQqyECTfHExPxUK0mV73HYuNRf4tYLHlc1yc4kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=DQv9IOswWGSCcbPG-xB6n7D3WOB1mfdgtiR9LtOTfZYaiOub6H7NWTX-s7GNjQOfOxGturTwB5iWLLl_kA8EcptcKvm1vLGl9q1EHMAcu78ZEETNDvqmBPpcV97NWRbgh--ud6LSfgMJUdF8vdHfKzXLjUnQzBW6kXAWbiJ75ObE7rJ9BUfgxEysYk26LUyuqATxHIYAlwhRTA2xEqusCioi_teNeoYPuPLFCPV12UFhu-VHtxBcBKDenSRBk6zyIIqLCQiwGdLyCoxe3CKd6AKfyipYDdwzMQPejxH4708WtPMmQqyECTfHExPxUK0mV73HYuNRf4tYLHlc1yc4kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تا آخر شهریور هیچگونه تغییری در بنزین 1500 و 3000 تومانی نخواهیم داشت
‏مهاجرانی: تولید داخل و ذخائر استراتژیک بنزین مناسبی داریم و جای نگرانی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/news_hut/70608" target="_blank">📅 13:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70607">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8a784e93.mp4?token=QaPZasNMp2aH90awUqrSXwzObk2m1vARq8ms-UI6o5GGMaWttZmEr6GNbG2gE6BXP6lYnS-MSAyaiRC4XdJUHgYifbn2fNxaw7ii_3KNBiv1EaTSIwPaE7MEWk8MG1Vw5rpftn4OYvuv3upXq1ScxoOF3dpp5QoaNGvZ9wQW7XlmViLKCh6AZsGzK6Fll3By8C7iCuqbOjh0YbbrmspJbRkJYLQuRzsEO0eYqeZumhi1YGyzTwz2eBmJnrTKRozFQMAtORwKBpBWLBBRF02DFNv2UrujTzScGwtpDx2X0InL5P2vzXlSIkOGW3jk7UJPZPJdWClNDyOGHenDkzxckg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8a784e93.mp4?token=QaPZasNMp2aH90awUqrSXwzObk2m1vARq8ms-UI6o5GGMaWttZmEr6GNbG2gE6BXP6lYnS-MSAyaiRC4XdJUHgYifbn2fNxaw7ii_3KNBiv1EaTSIwPaE7MEWk8MG1Vw5rpftn4OYvuv3upXq1ScxoOF3dpp5QoaNGvZ9wQW7XlmViLKCh6AZsGzK6Fll3By8C7iCuqbOjh0YbbrmspJbRkJYLQuRzsEO0eYqeZumhi1YGyzTwz2eBmJnrTKRozFQMAtORwKBpBWLBBRF02DFNv2UrujTzScGwtpDx2X0InL5P2vzXlSIkOGW3jk7UJPZPJdWClNDyOGHenDkzxckg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ایران:
می‌خواهم به شما بگویم: ما همچنان با چالش‌هایی روبرو هستیم.
چالش ایران پایان نیافته است.
ما همچنین باید کار را در غزه، لبنان و سایر عرصه‌ها به سرانجام برسانیم و برای انجام آن مصمم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/news_hut/70607" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70606">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feb89091e.mp4?token=e2e7ML4kAvgTmBRIT47lldtpcBY5ATdfMAwdGb29I-4ehumgY0kjM0_PFmxRzyEjsqL_9A4F7ZuiQXFjRK3WDfWQ6i5Odn0islh3jLeehU_dAx9XDAIBOMW1Ar1DK9hwcCiYG5Xxp_2bH-JEvg42-G0FQkq1nAqrWGjjC0ICpOhBdgpHn221VgX5neEGwhNiy_iek2JxUcI9z0G1Xpo75lf6Lt1FSe1iSc5grcmmp6YXGEjdDSmOwRiTMfRRxyf2gFnlQogJUqj4-JuaUsmSG_y5cd5peWpGf88ANzornwGcQn58p7wffSYA93zZL3w9xamc9-mduZ_Wo_2KU08YfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feb89091e.mp4?token=e2e7ML4kAvgTmBRIT47lldtpcBY5ATdfMAwdGb29I-4ehumgY0kjM0_PFmxRzyEjsqL_9A4F7ZuiQXFjRK3WDfWQ6i5Odn0islh3jLeehU_dAx9XDAIBOMW1Ar1DK9hwcCiYG5Xxp_2bH-JEvg42-G0FQkq1nAqrWGjjC0ICpOhBdgpHn221VgX5neEGwhNiy_iek2JxUcI9z0G1Xpo75lf6Lt1FSe1iSc5grcmmp6YXGEjdDSmOwRiTMfRRxyf2gFnlQogJUqj4-JuaUsmSG_y5cd5peWpGf88ANzornwGcQn58p7wffSYA93zZL3w9xamc9-mduZ_Wo_2KU08YfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ایران:
⏺
و من به ترامپ گفتم که احتمال سومی هم وجود دارد: تشدید محاصره.
او دیروز آن تصمیم را به شیوه‌ای بسیار بسیار قاطع تأیید کرد.
اقدام دیروز رئیس‌جمهور ترامپ، تشدید محاصره ایران بود؛ نه از طریق تنگ‌تر کردن حلقه محاصره خودِ ایران، بلکه با تشدید فشار و محاصره بر کسانی که به این رژیم — این دیکتاتوری هولناک — کمک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/news_hut/70606" target="_blank">📅 12:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70605">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c258982c.mp4?token=LgpU1NWs-SPE3c0ffUCITxpb2_ayaxE033B307bM2BdWMUok0lIQ1k22dPn0s4hYKZmMbeKtLYMAYwP51LGQ2ikDR-NizVAiPvNMhaMxVU3IqYwmiXcS_sNts9UJ98R4nvk1WEj9uotCk-FyHngTod8sOYG9fJqki6znB8lv5dH7eflT7fBrfGm1nfz7OArfQYrDDWRlRKxBpZG4YuHl2Rlho61-kHM7n2PubrWLfVlRGLTxnFFi4F_Plb_3KFBrta8XivtbMI5nsol7T6StkUJpbzcaugC-og98B3vZ0oRnlIutrmQh_OUz9z5RkeVtK5CzG5JfMn5HwyK6qXG-Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c258982c.mp4?token=LgpU1NWs-SPE3c0ffUCITxpb2_ayaxE033B307bM2BdWMUok0lIQ1k22dPn0s4hYKZmMbeKtLYMAYwP51LGQ2ikDR-NizVAiPvNMhaMxVU3IqYwmiXcS_sNts9UJ98R4nvk1WEj9uotCk-FyHngTod8sOYG9fJqki6znB8lv5dH7eflT7fBrfGm1nfz7OArfQYrDDWRlRKxBpZG4YuHl2Rlho61-kHM7n2PubrWLfVlRGLTxnFFi4F_Plb_3KFBrta8XivtbMI5nsol7T6StkUJpbzcaugC-og98B3vZ0oRnlIutrmQh_OUz9z5RkeVtK5CzG5JfMn5HwyK6qXG-Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
⏺
به ترامپ گفتم:
البته یک احتمال این است که شما با ایران به توافق برسید؛ یک توافق خوب. ما هیچ مخالفتی با آن نداریم.
اما تردید دارم که بتوانید با آن گروهی که آنجا هستند — با آن وحشی‌ها — به توافق برسید.
🔴
به شما می‌گویم: نمی‌توانید با آن‌ها توافق کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/news_hut/70605" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70604">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=uQifEj-KVP9oNyLwxUBXvIU584p3Cu4Kdfg8hvbvZMCrskMQ7RBgU5UbKuUXq1rqQWyruClghHHOb3AdSuwNj2oW8oFE_MHmMPCR6RrjbOVQ6N1Ynep1TWpOAbWOis9v3MvdtlQc_nnPEzYDvo8z52UhphdO-VrQchsMRRV6oB_b1OgMDIaYSkLLn4cAuBA1nNsXKRI7OVfERcJ6EcaKM-0hAE1TZRhHCevwyzAyX3zJZsiCnbsZq2k3wl4mkOA6zJg7W4Jg3dxYXzA90rkywDS-cBFIlFr5fRptMGwqFAi3IK9IDFafryl22S7sDjADqAO3D_bz76LPe4-UiDdogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=uQifEj-KVP9oNyLwxUBXvIU584p3Cu4Kdfg8hvbvZMCrskMQ7RBgU5UbKuUXq1rqQWyruClghHHOb3AdSuwNj2oW8oFE_MHmMPCR6RrjbOVQ6N1Ynep1TWpOAbWOis9v3MvdtlQc_nnPEzYDvo8z52UhphdO-VrQchsMRRV6oB_b1OgMDIaYSkLLn4cAuBA1nNsXKRI7OVfERcJ6EcaKM-0hAE1TZRhHCevwyzAyX3zJZsiCnbsZq2k3wl4mkOA6zJg7W4Jg3dxYXzA90rkywDS-cBFIlFr5fRptMGwqFAi3IK9IDFafryl22S7sDjADqAO3D_bz76LPe4-UiDdogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رفسنجانی سال ۱۳۶۰:
پهلوی همه همت و دغدغه ش این بود که مردم خونه و ماشین خوب داشته باشن؛ زندگی خوبی داشته باشن و ارتباط ایران با کشورهای جهان خوب باشه ولی الان دیگه اینا ارزش نیست و برای کسی مهم نیست .
الان دیگه مردم دنبال معنویاتن.
@News_Hut</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/news_hut/70604" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70602">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90ae8ead9.mp4?token=a_eYgzkJHrOkh1I6LT27XBioEMB-YnqYBlIqXwySGEiRzSZNxIOsIVNrsZivNu_AMbloodnAauMOgY5uNezjC_fK7H9jvbhgX4pD7pipjKxqTDc5cIdJSuYCEMob6W39mI0g1-3tXuf3SlFUKLiFJI-cDlMVLFDvfKmshOE8mR4rgUGdtN5V0iamYfcHaCL82OburL4Wfxube3Zs6SDxwYXpy09XDrkL12eQmaR9xDPkITlLnyTaJRvnuhck0n8MFeIuO4QgK7f6K7ibP0KAsdV4NjT6vbdNjuaQTkr6060h46PQiVnlbW5glSPFzWc89dI_GHA3P5gITwcd-1BOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90ae8ead9.mp4?token=a_eYgzkJHrOkh1I6LT27XBioEMB-YnqYBlIqXwySGEiRzSZNxIOsIVNrsZivNu_AMbloodnAauMOgY5uNezjC_fK7H9jvbhgX4pD7pipjKxqTDc5cIdJSuYCEMob6W39mI0g1-3tXuf3SlFUKLiFJI-cDlMVLFDvfKmshOE8mR4rgUGdtN5V0iamYfcHaCL82OburL4Wfxube3Zs6SDxwYXpy09XDrkL12eQmaR9xDPkITlLnyTaJRvnuhck0n8MFeIuO4QgK7f6K7ibP0KAsdV4NjT6vbdNjuaQTkr6060h46PQiVnlbW5glSPFzWc89dI_GHA3P5gITwcd-1BOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مدیر شرکت «فردا موتور» داشت واسه ثبت نام کنندگان خودرو توضیح میداد که ماشین نداریم. دو سال و نیم صبر کردید؛ باید چند ماه دیگه‌ هم صبر کنید که مردم گفتن «سیشتیر بابا همتون همینو میگید» و ریختن سرش.
@News_Hut</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/news_hut/70602" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70601">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70601" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/news_hut/70601" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70600">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_YINNULRupLL0mIi_IbjL33VtZprRnNXHiLmoaxQY3gisjo0Ob6eTS0fay-V1skEPFQPMmtZlsIzL2fhdFRAW1CE9hyGUlGB0A8gQXfFYhEXbFHJNGGs05GqGW0YuI_ruvPUFKL4pEkhETTAaZKc3F-IQlCycRavKvOAh_YS6Z9Kp4dCEnKZy-xqpAxOqgMow08UxnD7tnnBeVt_Ca0exEDd6boWiJQvjQh8y4JbH74FqGzBPTkWAy71ixG5OxoYE5_WmOZXOsFRL_fVYrbxHOLeZzW_ZTTYQHL0FWp6Zsei-_VF_Y0A0tpk0MZiGcldfcyYPh1JfDFifx4QIMEGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r4
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/news_hut/70600" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70599">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=pFPipaB6P9uhSNKgT1K_w5NEfz1maSjuHiPhq8ytYDQq_JmhLOs__78_nB3QCOKULkrQia-Ky6VPDtXiaX98W4RVQS1xenk555PUZkCzsjK3wih7vJZslGrEGXbdgyTGA0NcljwuOLrg0MCNJwpZoGy_JinmjSFe28pdffNnmpxWC2Y0e-BDe0T8JCD-JR9ElThTJqzr8P3m7OZof1M-S0AwrJIh4Fq0qCaNrkme9jPWllrLRqluwlo4NF95-gjOQBKqdudlTi__noxer_vOiqQjBpyIsizr1mPKmO47uPffyDCuwzZoLLihZMTCo0NvGvr3_mwuymajl6XJAVHz5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=pFPipaB6P9uhSNKgT1K_w5NEfz1maSjuHiPhq8ytYDQq_JmhLOs__78_nB3QCOKULkrQia-Ky6VPDtXiaX98W4RVQS1xenk555PUZkCzsjK3wih7vJZslGrEGXbdgyTGA0NcljwuOLrg0MCNJwpZoGy_JinmjSFe28pdffNnmpxWC2Y0e-BDe0T8JCD-JR9ElThTJqzr8P3m7OZof1M-S0AwrJIh4Fq0qCaNrkme9jPWllrLRqluwlo4NF95-gjOQBKqdudlTi__noxer_vOiqQjBpyIsizr1mPKmO47uPffyDCuwzZoLLihZMTCo0NvGvr3_mwuymajl6XJAVHz5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای یه آخوند طرفدار حکومت راجب حجاب
:
اگه شما آزادی پوشش داری، ما هم آزادی تجاوز به شما رو داریم
چرا اون کسی که میخواد به زن ها تجاوز کنه آزادی بهش نمیدید؟ آزادی باید بهش بدیم دیگه خودش انتخاب کرده که مزاحم همه بشه
اگه مردم آزاد باشن که هرجور دلشون خواست بیان بیرون پس باید متجاوز ها هم آزاد باشن
چطور میگی قانون باید جلوی متجاوز رو بگیره اما قانونی که باعث بشه لخت و پتی نیای بیرون نباید جلوتو بگیره؟
چطور تو آزاد باشی اون آزاد نباشه
هرکی لخت بیاد بیرون حقش اینه که سرش بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/news_hut/70599" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70598">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5b717c94.mp4?token=I7Nm5bSRmj0ZsGFaAXRGGKqK7rqb-YstUpFisWKX05zJToqLh9UkmXJOjiTfXEmMBsJ1upBJEZrFxe0PepJFFb_qHBTDsK0BiPAUPQe5rXXwlIu2NtzjZr1EbW2_oZkTi-HZS0ZGW7xUfGHcT273OrppX8V9wFDgCp1Ca2EO301gAQ--WTLxJbuNdV-tSA_IWLf2wBA6nD3MN-Ox-f31yEqScNtDPmnj17ZL5ZGCV39kcvVU1MwbCByYp7gVCWCYJadVtlsZE3QiGh2h1VqzoSXfwJOY0ShX1Yn0WnS-pN9Y_qZYn6jFnoAl8ZcS7-_Y5DifUO9VnWurB_Wc-poYrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5b717c94.mp4?token=I7Nm5bSRmj0ZsGFaAXRGGKqK7rqb-YstUpFisWKX05zJToqLh9UkmXJOjiTfXEmMBsJ1upBJEZrFxe0PepJFFb_qHBTDsK0BiPAUPQe5rXXwlIu2NtzjZr1EbW2_oZkTi-HZS0ZGW7xUfGHcT273OrppX8V9wFDgCp1Ca2EO301gAQ--WTLxJbuNdV-tSA_IWLf2wBA6nD3MN-Ox-f31yEqScNtDPmnj17ZL5ZGCV39kcvVU1MwbCByYp7gVCWCYJadVtlsZE3QiGh2h1VqzoSXfwJOY0ShX1Yn0WnS-pN9Y_qZYn6jFnoAl8ZcS7-_Y5DifUO9VnWurB_Wc-poYrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این خانمه داره مشاوره میده یک فرد چطوری با رابطه تریسام کنار بیاد
😐
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/70598" target="_blank">📅 10:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70597">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdd3ca324.mp4?token=rabd8qor8MVV9E01oPhetU8kxrwRCMBmCBO0ZC4i3cvrXXCHY8Tdpvudynwjig4dpZPeTN1IRfb8O0WfqfptoX6Jn-_rJoy0hlDHpBqaxXQJuPsw74Rz_zQo1M27FcIuHlKaid4KrzcocVwfC-CbosEWiIb-a-raeOhOrPBREsrcm7q4hKz9jPggvl9J2ulE-YFRNn82LaVX7PAY8fjy40evtt5D8NmX1L32TXwmd4iPFlDHTPuNf9rRaPws0fep-xnEOLvmkW4raftqqtGqh9YDG9xHwmHchk2O1id2upGyFGJXlNF-rZrS1Mnp0ljmTnVydEFOsFfl8jLmBhmnOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdd3ca324.mp4?token=rabd8qor8MVV9E01oPhetU8kxrwRCMBmCBO0ZC4i3cvrXXCHY8Tdpvudynwjig4dpZPeTN1IRfb8O0WfqfptoX6Jn-_rJoy0hlDHpBqaxXQJuPsw74Rz_zQo1M27FcIuHlKaid4KrzcocVwfC-CbosEWiIb-a-raeOhOrPBREsrcm7q4hKz9jPggvl9J2ulE-YFRNn82LaVX7PAY8fjy40evtt5D8NmX1L32TXwmd4iPFlDHTPuNf9rRaPws0fep-xnEOLvmkW4raftqqtGqh9YDG9xHwmHchk2O1id2upGyFGJXlNF-rZrS1Mnp0ljmTnVydEFOsFfl8jLmBhmnOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
همتی رئیس بانک مرکزی :
علت بالا رفتن قیمت دلار طبیعیه و نوسان های خاص خودشه
ما نمیتونیم بخاطر یک نوسان بیایم مسیرمون عوض کنیم
مسیر ما درسته و خوب جلو میره
اگه این مسیر ما طوری باشه که میان مدت دیدیم درست نشد اصلاحش میکنیم
ولی من معتقدم که این شوک هایی که ایجاد شده جوسازی امریکا هست و شرایط مطمئنن درست میشه و رفع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/70597" target="_blank">📅 10:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70596">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
ویدیو وایرال شده از یه جوون ایرانی خطاب به مسئولین جمهوری اسلامی
تراپی خالص :
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/70596" target="_blank">📅 09:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70595">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0e780a212.mp4?token=aVD8z77z6EryafkbYfMkv8Q7Eq_eyC2DFNU6IoNEFkM_c2yWM_KafWi3tfx-xHJZboxFzW0ZFchGdEb2HYlnuTYJbSX_Xm1OiI6wjcOKFjoab8lGhoM3cRiBVske3QPTEfCjEdegu8aMCHq6pGvId2pjGBkkIdP23LXavpcnTFQcHvURYTOzuuhvU9m29My0OYWv-tQ5z0hRlIRl946R5M0zigylmEAVV-B1asWAzF4frDIOQ4e6R0RwR4X1lQKvO3GzRPbsEDh-l24gzO67cfxTo2adMrx9S_RUOPWkn1wCGrg0ywYSglWtvuJ7ufeIhC40cGkw6VhfvoPdAcuoFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0e780a212.mp4?token=aVD8z77z6EryafkbYfMkv8Q7Eq_eyC2DFNU6IoNEFkM_c2yWM_KafWi3tfx-xHJZboxFzW0ZFchGdEb2HYlnuTYJbSX_Xm1OiI6wjcOKFjoab8lGhoM3cRiBVske3QPTEfCjEdegu8aMCHq6pGvId2pjGBkkIdP23LXavpcnTFQcHvURYTOzuuhvU9m29My0OYWv-tQ5z0hRlIRl946R5M0zigylmEAVV-B1asWAzF4frDIOQ4e6R0RwR4X1lQKvO3GzRPbsEDh-l24gzO67cfxTo2adMrx9S_RUOPWkn1wCGrg0ywYSglWtvuJ7ufeIhC40cGkw6VhfvoPdAcuoFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
غریب‌آبادی، معاون وزیر خارجه جمهوری اسلامی:
چرا باید همیشه منتظر حمله آمریکا باشیم؟ ما میتونیم پیش‌دستانه اقدام کنیم
بازگشایی تنگه هرمز فقط در صورتی انجام میشه که جنگ در همه جبهه‌ها تموم بشه، محاصره برداشته بشه و وضعیت یمن حل‌وفصل بشه
به فرمانده ارتش پاکستان گفتیم ما توافق رو نقض نکردیم
اگه آمریکا میخواد تنگه هرمز دوباره باز بشه، باید همه شرط‌هایی که ایران توی توافق گذاشته رو قبول و اجرا کنه
ما هنوز در وضعیت جنگی هستیم و تا وقتی این شرایط ادامه داشته باشه، تنگه هرمز هم بسته می‌مونه.
اگه آمریکا به اقداماتش ادامه بده، ممکنه قابلیت‌های نظامی جدیدمون رو هم رو کنیم.
تنگه هرمز تنها ابزاری نیست که ما در برابر آمریکا داریم. آمریکا نباید فکر کنه فقط خودش می‌تونه به اقتصاد طرف مقابل ضربه بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/70595" target="_blank">📅 09:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70594">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70594" target="_blank">📅 02:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70593">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=RfdGncfEvqMSR8bG7VUB9xdJD4eWfP8aGvQx6Cb82Ny1-OjM7OwR3iDzVsZ30tApfiWQO0Sdnq0E02wl4Yb76b3SboSh0YnDJ22RaEAOsAkycl8S3wfU6Ub6evbYhzCgJftDeXvwuHkjI8PwTeHjFY6uZicnix4uJYBJr79xoFU5drzEzEW3iUPtE936aPofm3FYrOyl1NxPvEt8oq9UUeoRvUSHerBmhM4hMxLaNlQqX5t6oqP6ENzm3CzTVUvexkXcX8AlSALEKyOdVR32yla2skOcRKv0cQk5hhLehtIEG8wHYkSMsfxzw0gKAs11zgtLvDo5aAm0rNmcxvm63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=RfdGncfEvqMSR8bG7VUB9xdJD4eWfP8aGvQx6Cb82Ny1-OjM7OwR3iDzVsZ30tApfiWQO0Sdnq0E02wl4Yb76b3SboSh0YnDJ22RaEAOsAkycl8S3wfU6Ub6evbYhzCgJftDeXvwuHkjI8PwTeHjFY6uZicnix4uJYBJr79xoFU5drzEzEW3iUPtE936aPofm3FYrOyl1NxPvEt8oq9UUeoRvUSHerBmhM4hMxLaNlQqX5t6oqP6ENzm3CzTVUvexkXcX8AlSALEKyOdVR32yla2skOcRKv0cQk5hhLehtIEG8wHYkSMsfxzw0gKAs11zgtLvDo5aAm0rNmcxvm63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a3
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70593" target="_blank">📅 02:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70592">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKnsJwWi_X94QsM6tSpHIPjlvwewU5x6FLwMaYVr8c4pSK993uPZwxybOfAHs-gMXdRn6ckPj89M5aFKt_zSz70XvXQnEA8UILGRF5VUolPwomTlo9TvO41bUCnfZ9RcVId0RzANhdTJE74_2iIC7ywSyON904Pq4Btqxf32Vv-1eS03xObrQgZkkJJ_wslfLJPi90mBtqHeu7-Hhlj2R4fRNVvUqLYw_aHTqGSp3BDEpVKKXIgxMIH6JLKU7mAc03ukEb2psvZtRqqjTGhB7tslUBozqW-LJogOVx7tnZ7oMPvFeNQHnKoA09LTci-QIDtR3na0pEYuzM7nJH5OqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وام ازدواج برای یک زوج ۶۰۰میلیون
⏺
یخچال ساید ۵۰۰میلیون
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70592" target="_blank">📅 01:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70591">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZPOYan_Hz9rLMr1X_u0gJR6RkGUnifmnBxi_3cFf9l4d7aZDjcI_wwU-Nsq0-mzmSqFVgxg-0xj0jgCbqOfQ128UDWJktJC6uhfRUFQi6zkKg2A35PmSuEpMJAaCPkB5WR9jV3FHNB3mYEBd2rsAlfk2j9xW7Y62iakawHhIRWUg3W96Wo5bNUnEZrXT5asLiHeGok3ORz6WJgxatFL_8-wmieTrcMQ4H789fPJxQjtfiCvEcVqCqFgbDSVv1YKyu3bDPNG_zBnTzAKjvsubgO758pdxy76llkhegvVJ77lswG8pJUmRIbP65ZHKEmDj-jwIOnWCIrD6QTWSesbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
🇮🇷
اکسیوس:مارکو روبیو، وزیر امور خارجه، به چندین تن از همتایان خارجی خود گفته است که ایالات متحده «در حال حاضر» برنامه‌ای برای انجام حملات جدید علیه ایران ندارد.
در عوض، دولت ترامپ بر اشکال دیگر فشار، از جمله محاصره دریایی و کارزار تحریم‌های تازه اعلام‌شده، تمرکز کرده است.
روبیو اظهار داشت که اگرچه واشنگتن برای بازگشت به عملیات‌های رزمی گسترده آماده نمی‌شود، اما در صورت حمله نخستِ ایران، همچنان امکان انجام حملات متقابل وجود دارد.
انتظار می‌رود این سیاست دست‌کم تا پس از انتخابات میان‌دوره‌ای حفظ شود؛ زمانی که ممکن است انجام یک عملیات نظامی دیگر مورد بررسی قرار گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70591" target="_blank">📅 01:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70590">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpjKFYp3wJXhLOXRBgWWnD3acZFh5gU9GoS_IvLRtMC_N-sl1ZnZm_NNfJ4cVXns6fXFJQtrMaSVBXbFvPr8fxTSwQqr6qGm-HBQjeuld01jhLbr0OzDnTCrEi3cjbzDvJJW67xeziUY4Xjl19BHH2x5oFamXe0l_xJ0IQmC4AUa7UlEIo5PzfCfzVUKOPyF7irc_GX17B2y1XA4prWkmtF3Xf6mUWdui5SPS4LvWTMuhbyJOWoCySiYFR2GcI9BOfKzlB6fP75Wdkmkjz4hkHdP808ebJFmrrYUfYXhqzvwZ02EhPVMQg5B1oX1rb0pnCgcfM91nkW5ZuNUmYH7Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خروج یک هواپیما از باند فرودگاه مشهد
روابط عمومی فرودگاه مشهد: پرواز تهران به مشهد هواپیمایی سپهران هنگام فرود از باند خارج شد اما مسافران و خدمه در سلامت کامل هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70590" target="_blank">📅 00:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70589">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⏺
🎙
وزیر نیرو :
تا دو هفته دیگه شرایط آب هوایی به حالت عادی برمیگرده و خاموشی ها تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70589" target="_blank">📅 23:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70588">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJZzmBDCvVFkm3VIM3GpUIp_ydJy4yilsex2ab9lxLimoMFpavR8TCGwYclt-TyNPUikKQZiclxr04bFS8NQCj1eQ3JXK9gLeOaJDfz7skNyxWPMBc63v9el-D3OS1du-xkClxSikDEnCo-0WPqneuYQoBUuhjK40hc4YUPjc583Hky7TwhetJlL190jHg_lkW41YeP_Jl-ucLxPnDiLnWnT-c_VazkyrOWy_L8OAYbblOGI6LmeTfuA1wBqoYy2uTwHrGJrwNyAvffddoNORXCIT0bz20bIouHrXasUOsWH08R1ixrHSkmPG_nVImSc37faFDF_T-JQAS5YPfB1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇴🇲
بیانیه مشترک ایران و عمان: دربارۀ چهارچوب ادارۀ تنگه هرمز گفت‌وگو کردیم
رایزنی وزرای امورخارجۀ ۲ کشور بر ازسرگیری دریانوردی ایمن در تنگۀ هرمز با حفظ حاکمیت خود متمرکز بود.
🗣️
چهارچوب پیشنهادی شامل این موارد بود:
ایجاد یک کریدور مشترک از طریق تنگۀ هرمز
اجرای پروژۀ مشترک برای مین‌زدایی از تنگه
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70588" target="_blank">📅 23:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70585">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=EHrELH1e-9bb4h7MNfWdlsEitbw2G6GtKjt1n6JkkkGY_frQrTySEiebfh3LtPUcGgpKtcPZqM1UOkNSvpZD3YCaiM1fJMWbOJYR8ou-9EZLD6pKmgEohDGTFOu8cleZWzjaxdcddc-5aysxWZfm-g2HaevKKJPbGQ25LAm6hM68U5yTa98-fKIGD9IpJY1efn0WmWzgJjLncgSfFcme9TOMHILnERA5YEahWWX3tOf2WDQ8pEl_AB3xJySqJkcEtpoodjyagNA9369Pi7UGDGpik9mEIjZSqRuLjnMPqN9U7S8AWgFeoKiywB0MDRp48u49hcf7uAUlnLXhsheSlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=EHrELH1e-9bb4h7MNfWdlsEitbw2G6GtKjt1n6JkkkGY_frQrTySEiebfh3LtPUcGgpKtcPZqM1UOkNSvpZD3YCaiM1fJMWbOJYR8ou-9EZLD6pKmgEohDGTFOu8cleZWzjaxdcddc-5aysxWZfm-g2HaevKKJPbGQ25LAm6hM68U5yTa98-fKIGD9IpJY1efn0WmWzgJjLncgSfFcme9TOMHILnERA5YEahWWX3tOf2WDQ8pEl_AB3xJySqJkcEtpoodjyagNA9369Pi7UGDGpik9mEIjZSqRuLjnMPqN9U7S8AWgFeoKiywB0MDRp48u49hcf7uAUlnLXhsheSlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به پالایشگاه نفت آفپسکی در منطقه کراسنودار روسیه حمله کردند.
در پی این حمله، آتش‌سوزی در پالایشگاه مشاهده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70585" target="_blank">📅 22:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70584">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49911fbc7e.mp4?token=gnlMYgw3RRcRWs9SzIULv0Fpc8FVjrlvUpVi62sN4ZYmrxvxXUTvSPLicIEXyv9nZoetrJjmCRpJNAciCTkIExQ6EEV7T9aFuPX-zu6vRDF-b3ZDYzY3d0jkT70_VaFezu5uJlsJVzHOCZ4q12yO9ppUjhaPybni2rV7DMnYW1hOgETllqlQhXIZQYYiGnF-tVlpVT9ZpA7swws9zhVnNAT7qXz-TPq5x0FczmGHMx0NFUWFY_VwLLxLO9wyOFLxMqybktXN6EwK670xLzxeoGDVRonG_rtgJzS0-MU9SBIlL1_StApvFRGMUUbkqdXacZcuo2g3urtEMrEbH-v1IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49911fbc7e.mp4?token=gnlMYgw3RRcRWs9SzIULv0Fpc8FVjrlvUpVi62sN4ZYmrxvxXUTvSPLicIEXyv9nZoetrJjmCRpJNAciCTkIExQ6EEV7T9aFuPX-zu6vRDF-b3ZDYzY3d0jkT70_VaFezu5uJlsJVzHOCZ4q12yO9ppUjhaPybni2rV7DMnYW1hOgETllqlQhXIZQYYiGnF-tVlpVT9ZpA7swws9zhVnNAT7qXz-TPq5x0FczmGHMx0NFUWFY_VwLLxLO9wyOFLxMqybktXN6EwK670xLzxeoGDVRonG_rtgJzS0-MU9SBIlL1_StApvFRGMUUbkqdXacZcuo2g3urtEMrEbH-v1IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مستر‌بیست(یوتیوبر معروف) یه چالش خفن اجرا کرده که باید خودش و دوستاش از دست 100 تا نیروی پلیس به مدت 12 ساعت فرار میکردن؛
برای اجرای این چالش ماه‌ها زمان صرف آماده‌سازی تله‌ها، دوربینا و مسیرهای مخفی شد و حتی یک شهر رو به‌صورت کامل اجاره کردن.
خود جیمی (مستر بیست) و دوستاش به مدت چندماه تو یه شهرک نظامی، آموزش‌های نظامی و امدادی دیدن و جالبی این موضوع اینه که مستر بیست برای خودش 50 تا بدل درست کرده بود تا پلیس‌هارو کصخل کنه.
این ویدیو یکی از پرهزینه‌ترین و پرچالش‌ترین ویدئوهای یوتیوب مستر بیست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70584" target="_blank">📅 21:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70583">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b72e753c.mp4?token=bZrwU0vT6zP2cIj-yJdFZ3tyxC-NuX4-sfXWKMjnWeiBwhWbdBc9gqLQT0ezOsk_dutkpmoM3tPv3bHXHo68EatuFmHxhMe92JoKwliqq-crXB1wJjx6VXRDoQPIf_y0R7-FNz2ijOnkgpbONv3EPGQCr5owfthPqHCwWOw_SAKPNEetxh8Dj-S1N4kJ-g1YNFUVVDT4U6YLmzkn1cRL3P8mZN1i9FcDK_Zl4gT4Ya-dCDqYsgI1rUUXrzIjTjckQnYpmxemETq9GD5vXepXGfuCZCj3wCgclrE-f34XqP8zHq1IQG36yTIfVx0wNM0Bq3OoL1P7RxqJudyVm5KHfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b72e753c.mp4?token=bZrwU0vT6zP2cIj-yJdFZ3tyxC-NuX4-sfXWKMjnWeiBwhWbdBc9gqLQT0ezOsk_dutkpmoM3tPv3bHXHo68EatuFmHxhMe92JoKwliqq-crXB1wJjx6VXRDoQPIf_y0R7-FNz2ijOnkgpbONv3EPGQCr5owfthPqHCwWOw_SAKPNEetxh8Dj-S1N4kJ-g1YNFUVVDT4U6YLmzkn1cRL3P8mZN1i9FcDK_Zl4gT4Ya-dCDqYsgI1rUUXrzIjTjckQnYpmxemETq9GD5vXepXGfuCZCj3wCgclrE-f34XqP8zHq1IQG36yTIfVx0wNM0Bq3OoL1P7RxqJudyVm5KHfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
سوال خبرنگار از شاهنشاه آریامهر:
فکر می‌کنید در کشور شما کدام‌یک تاثیر بیشتری روی زندگی مردم داره؟مذهب یا پادشاهی؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70583" target="_blank">📅 21:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70580">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMVe-Cxo_ELVkxVdXGJnPrruYKHZzh7EehwXE9vdKSI33K3oBGtOmj1m2cd8wQGw8uDcF9HVx7mDTUIWMESEeBuTC-O8t4pKQdSlML6aa5tZ50Nty5ppz_EyJiYVo8Blyv4zoaymwuIMWLJzV8jcKHph38Vp0f2D4otXn-unH-i4Y0X0gh6xIlpjGruQ_bAokqVPjOT2MVLfZ7sfvMiD8kHBMa6AY45Imu4RfFGr6tCygADNxwu15VnT9NyVEZyCkMo78d0oMtQEEh_SaoS411rjD7Z5gqm9ZUEl_IM59rArTwHii5vx0ef6synLHq39n554SdmzfJcnsyuLiZR3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VndmRhUbRQPf7KdVm-Z3J9ar3X_qGD1jooVmgvLiU-RY2SMzMbMAmV1noV59kyKECUJ0_Z5OF0RAwhz_7embX2But3ypb2cEMrKXrPWX0bAsr83i8bV5TlQSzo98qciDkStiwTfeV1hUMxzGeLJTfT4zvlOXFSMmklSYRYV8TACtnYC9zRSU_2YRLsB27JqTzgO2GhXT0YFGt-v1CR2J8PGt1sIm77uYKzivN2ltoZ0KYhHWxBjMJwzf54kWLNL3GNmmki--ICB8memgGWTCfAVqZf-EwGupQGQB1sTybA16h0oCYuRjHJ0xrrPZqC4XXsMqGC8yyqRyF5itz-UwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dAbPSAyE6wCIivBPbRIWplB_xdWuKg5M5aEluYX_kIKFla7gdGAV9L_qr_nbTvEiLETVEa4qMCjrIylZsqFNM4t_ezLTqPnM1GuOklr_UmYVe85bmOLkJE-got6UJEhcNQtbWwn-VsfT8-kl-0qsGcXBRernIFVn37wnR9cTxR8AeunpuH5AuV-PFk_enD-t5U_eknPFVhVHEMV2gB435WM4E5-CXWIWrxxkO0gSR99oZ99v-ww70oj2vZnBik9WTUC2BbQeOD9gIbkymasIrRRGOtlTcrlVUJK7YyywQB5pcKhed-VNf_APcW0NVdmjpha-8aQhNzwrRrf1CtY9rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
〰️
🇺🇸
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
🔴
رهبری ایران به واقعیتی اذعان می‌کند که اکنون برای جهانیان آشکار است:
فشارها کارساز واقع شده‌اند.
🇮🇷
مسعود پزشکیان، رئیس‌جمهور ایران، ضمن اذعان به کمبودهای اقتصادی کشور، اظهار داشت: «جنگ باید بالاخره روزی به پایان برسد.»
🇮🇷
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر سخن گفت: «هر چقدر هم که قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و خبری از گردش مالی، رشد اقتصادی و تولید داخلی نباشد، دوام نخواهیم آورد.»
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری همچنان به قطع تمامی شریان‌های حیاتی اقتصادی که این رژیم را سرپا نگه داشته‌اند، ادامه خواهد داد تا زمانی که تهران کاملاً منزوی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70580" target="_blank">📅 20:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70579">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfomaLXFewvRnBn-L2yNFknKbAmQeRJ0bPWxlEBNkemoF5LUrXO4eHlpYh7rJNsjGRi1oI7dmmr74pc5Nf5Xf9vnS4sTjkcDlR_v5AZF4f52H_7a1gaiQHMdmkHo3s2bortazUNoUefQ45qTzPcGsz0e_IqabPdq-aBEFNvSwq2HPlMHnfn8HRbLW5Ptgk_agzLjGMmAIkdRZf7y3GmkM1-_r0yHbyuTn5pWU8SUz6Vdj9uClvIkHtWrqL5xKNr4_7zN18mNJVEJrOD10yNpfg3nB9ANoWSlPpR90h--K14ypOXeyd-rOoPMmxxwexSUsy5lY6UeFUprOhcyysbZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
اکانت رسمی تلگرام در پلتفرم ایکس :
امروز به کراشت پیام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70579" target="_blank">📅 20:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70577">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370e63e8ae.mp4?token=gcoFnAETh1yg3v88XPtQQpLTC5r-fp0PARKw3pvCbYG-KSg40JS1KiDDOTwM1fHJzeG8OSRosEPUq6YYf_SwVvg0tM8BaYwqm_96Cmj4UmxSBPRLnaiaBxyPcBp-Pi3b3mySqNQM27LtIJZt-JHQijQ8XCCgn1XbpWm5HrmTopkg_QEuvOlTWRERH5cGezKN5sVcoS03QnXhB2gRbTJbn9niSsKmmLWmCQxCrde_hsfQTd5bNeZs3uZ5BlDgzpZ_nhZAXvtbpkQ4hLTVcOL-nfMC6Uv6cDQRCXRnxFiRcOcDzyVRxH72YkqGMqnX1A6i--oktLg_g_sMw1EmGHWxFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370e63e8ae.mp4?token=gcoFnAETh1yg3v88XPtQQpLTC5r-fp0PARKw3pvCbYG-KSg40JS1KiDDOTwM1fHJzeG8OSRosEPUq6YYf_SwVvg0tM8BaYwqm_96Cmj4UmxSBPRLnaiaBxyPcBp-Pi3b3mySqNQM27LtIJZt-JHQijQ8XCCgn1XbpWm5HrmTopkg_QEuvOlTWRERH5cGezKN5sVcoS03QnXhB2gRbTJbn9niSsKmmLWmCQxCrde_hsfQTd5bNeZs3uZ5BlDgzpZ_nhZAXvtbpkQ4hLTVcOL-nfMC6Uv6cDQRCXRnxFiRcOcDzyVRxH72YkqGMqnX1A6i--oktLg_g_sMw1EmGHWxFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر ۱۶ ساله رونالدو و دوست دختر خوشگلش:
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70577" target="_blank">📅 19:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70576">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070dff64b7.mp4?token=pGVoA35UV8ilqQWzP4pP5b8NkEY8lXtuVByMq3H5YjIR6y4Ip6T7qRaJVazVJ7_IRt3ORyxFTJDToW9n-T29z9Dny1VSz5X4lm_B5jewzaPY5aq2ohaa4VEy-PbOD3YExZMWDkMMewoKkjrS7c1X2qLmm7zvD8zs8MwQFheohAI1DB5P-BonDO0eMaX977dDMGbV-1IOalLGhNA_f73MNiAsFvWwKgrz_ak6qiDrXsIa94Bp03pnIGQmIPkU8qzL5BAwQn2DplOlyZa-gbneMZcDBIsx0jMQxYv4mY6gLfEmvJ3XE6DziNWph0SqcAKpfypokFco6yQzI_dkWduwZhDX0_qhiBgymxijUlGnoy_9OD9A0mglN7cOYTXVtCxSlnmIr3iLAK83xxe-xyECFqi5CSlw1KGwHIZek89G67O4IXwfYVejqW6AgVeSwv14a8cUpvikxRG6rKsaMlbUf4JFloDnsg9kL3m-NPMe4oPWXSaab395HnHe608jzjjEpj1bZeLbZ3b74_Wy4xR-Q3-oKEfTBzTBO_IUFiim-tKcnLMvI8z893p7uoPgEDSajudEmMfoO3qEZr9lNFrVmL42iX5PR0LPBSW7digdpUtwLxzKQ8UEHAy0AP39eUklUDWlCKtVC8m8MSnj-Xv64XSVLgwaWaSvE1p5lnDPk4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070dff64b7.mp4?token=pGVoA35UV8ilqQWzP4pP5b8NkEY8lXtuVByMq3H5YjIR6y4Ip6T7qRaJVazVJ7_IRt3ORyxFTJDToW9n-T29z9Dny1VSz5X4lm_B5jewzaPY5aq2ohaa4VEy-PbOD3YExZMWDkMMewoKkjrS7c1X2qLmm7zvD8zs8MwQFheohAI1DB5P-BonDO0eMaX977dDMGbV-1IOalLGhNA_f73MNiAsFvWwKgrz_ak6qiDrXsIa94Bp03pnIGQmIPkU8qzL5BAwQn2DplOlyZa-gbneMZcDBIsx0jMQxYv4mY6gLfEmvJ3XE6DziNWph0SqcAKpfypokFco6yQzI_dkWduwZhDX0_qhiBgymxijUlGnoy_9OD9A0mglN7cOYTXVtCxSlnmIr3iLAK83xxe-xyECFqi5CSlw1KGwHIZek89G67O4IXwfYVejqW6AgVeSwv14a8cUpvikxRG6rKsaMlbUf4JFloDnsg9kL3m-NPMe4oPWXSaab395HnHe608jzjjEpj1bZeLbZ3b74_Wy4xR-Q3-oKEfTBzTBO_IUFiim-tKcnLMvI8z893p7uoPgEDSajudEmMfoO3qEZr9lNFrVmL42iX5PR0LPBSW7digdpUtwLxzKQ8UEHAy0AP39eUklUDWlCKtVC8m8MSnj-Xv64XSVLgwaWaSvE1p5lnDPk4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صادق خرازی:
به آمریکا در افغانستان کمک کردم و حتی فرودگاه در اختیارشان گذاشتیم اما جرج بوش ایران را محور شرارت نامید!
بیشترین خدمات را به آمریکایی ها دادیم و حتی خون دادیم
این نشان میدهد یک جایی در پشت پرده محاسبات دو کشور نمیخواهد رابطه ایران و آمریکا به جایی برسد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70576" target="_blank">📅 18:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70575">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b7fd64d7.mp4?token=nhCYvLX6M7CVZTucSSYCEQSUK_bBlSDGbt5M02mEeHNx36iXeVisDQBI1MKFRSZWxStbq6_O6kTbaK8D87tQqLYykQkHPbN4Q2qXYBbZJHuBE2Eh-CZNft5NUQAHmkic7CfDVV4WL3koD8FuYsVIQ5YTSaLuYzTwtf45xxvGcY8T-wXsIaSVSh0FZRVYAT-SxEjCmeC35Agf7Xp_uy2OxZ93hqNeLPpGMmQzd0FUOhmft8-9nLMh4g0YjNC6a9ruLlB_Y9BwF7uQNek1eMZuBQdemHdgv9Oq6g3EPl1QlxaG5sBHgZ22cjBwpQ82KyQFHgG5tMCcbivXkJnBecWAqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b7fd64d7.mp4?token=nhCYvLX6M7CVZTucSSYCEQSUK_bBlSDGbt5M02mEeHNx36iXeVisDQBI1MKFRSZWxStbq6_O6kTbaK8D87tQqLYykQkHPbN4Q2qXYBbZJHuBE2Eh-CZNft5NUQAHmkic7CfDVV4WL3koD8FuYsVIQ5YTSaLuYzTwtf45xxvGcY8T-wXsIaSVSh0FZRVYAT-SxEjCmeC35Agf7Xp_uy2OxZ93hqNeLPpGMmQzd0FUOhmft8-9nLMh4g0YjNC6a9ruLlB_Y9BwF7uQNek1eMZuBQdemHdgv9Oq6g3EPl1QlxaG5sBHgZ22cjBwpQ82KyQFHgG5tMCcbivXkJnBecWAqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
نگاه هویدا به یکی از بی‌شعورترین و بی‌سوادترین مخلوقات زمین
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70575" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70574">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70574" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70573">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOApMNfEI9-OVwvyNXA0bNZz_gbB9BU5jLZBkXyyJh-RAuo34n0avsqbf1TU_hlSs8unh_WNsPg5Alkf-ah1PD0mTjdUCawrYrlop15VCibV2mKPxh8FFyhP7K8GTIyoBgMoSlAeT5tVSJXHgwceWPN5kMZ2KvOEIihUkebfj_zOEKlPLNeEZzBwd91Un4O9XoBB11OB-YXQRSFQjiXcO7Sklxp7Q56EAjwyX9ruvgRQ1KNW86PqtPCBXXYRVof13oL-_1Zddkc6p7ocYb7_jb0TUCOq_H_spMKNgRgmjMsXLmm3OSoQo5lD0ZDMGm-ewKtvdyGKSya0dVYHoq86p36bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOApMNfEI9-OVwvyNXA0bNZz_gbB9BU5jLZBkXyyJh-RAuo34n0avsqbf1TU_hlSs8unh_WNsPg5Alkf-ah1PD0mTjdUCawrYrlop15VCibV2mKPxh8FFyhP7K8GTIyoBgMoSlAeT5tVSJXHgwceWPN5kMZ2KvOEIihUkebfj_zOEKlPLNeEZzBwd91Un4O9XoBB11OB-YXQRSFQjiXcO7Sklxp7Q56EAjwyX9ruvgRQ1KNW86PqtPCBXXYRVof13oL-_1Zddkc6p7ocYb7_jb0TUCOq_H_spMKNgRgmjMsXLmm3OSoQo5lD0ZDMGm-ewKtvdyGKSya0dVYHoq86p36bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g3
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70573" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70572">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8T40UbdSe71WEuw_8tPwVCcApZUnS1I_FVcplmcqlhpjGVYZebMEYI_z_WFxKdTMHuWrgMW6G6J_DqyN1VfBl-tT32QG-3Cj9YhPort7q3fO17-38W-mQCi6EMAaCWdX2bSql_VEqzHJqbugeNyRWwesVKxOYj2hSeKebXlNyRkEWXb6yNURNUo9beqGaPARONVqGWcnQ_cKfePW9X7DCDas-dVo_geG2eNdVBUwYgyaK55m8XYnbHt5D3Hp84DxmT87o3ij9kUva1Eni8xCgAMG3M-G8l8XroueLpfcmlBlSqDnZL4CdyAjxryubpETK_ADP2MzetofHWUhpaFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
نیروی دریایی ایالات متحده به من اطلاع داده است که تمام مین‌ها از داخل آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند.
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدیدی را در آن کار بگذارد، فوراً و به طور سیستماتیک منهدم خواهد شد.
ما از طریق نیروی فضایی، هر اینچ مربع از تنگه را زیر نظر داریم، همانطور که در مورد کوه پیکاکس و سه سایت هسته‌ای دیگر که قبلاً نابود شده‌اند نیز همین کار را می‌کنیم.
سیاست عدم تحمل در مورد مین‌گذاری با تمام قوا و به طور مؤثر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70572" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70571">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8133b3536e.mp4?token=WlKMzwwKqIPTB2YivH4GdeUpHl7k4SbjujewE1nej_SiGNXqyP6VhYsgmtS63-cVLpD1KQalr2y0TaZztPi-GJspqnjiI-zGC4Dj3XOfg0rMvyulPjzJErcNWXNr4jmQsXkf9ERtgsH0AdWBFB7YLvpxF6hVoQVBgALdd9muZ-nBG6JyeRZkuVqEsQpRWuTES8l_X8206aBBS5QciTs_upuWwwJL210c4MRqKrD6jVqcP2cxA5dhgkirzTTm1yvpFSHvG97Pzet7TWzN3_y6-AYMDgVu8ng4t9kDVx3amxQRdfygInVo5kOfc4VlKBTLICbNQ_N-61IHkRl6_O6ZiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8133b3536e.mp4?token=WlKMzwwKqIPTB2YivH4GdeUpHl7k4SbjujewE1nej_SiGNXqyP6VhYsgmtS63-cVLpD1KQalr2y0TaZztPi-GJspqnjiI-zGC4Dj3XOfg0rMvyulPjzJErcNWXNr4jmQsXkf9ERtgsH0AdWBFB7YLvpxF6hVoQVBgALdd9muZ-nBG6JyeRZkuVqEsQpRWuTES8l_X8206aBBS5QciTs_upuWwwJL210c4MRqKrD6jVqcP2cxA5dhgkirzTTm1yvpFSHvG97Pzet7TWzN3_y6-AYMDgVu8ng4t9kDVx3amxQRdfygInVo5kOfc4VlKBTLICbNQ_N-61IHkRl6_O6ZiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید باورتون نشه ولی ایشون بخاطر اینکه آلت تناسلی بزرگی که داره، گریه میکنه! میگه تا میخوام با دخترا رابطه برقرار کنم، جیغ میزنن وای هیولا، چه مار بزرگی و فرار میکنن
😢
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70571" target="_blank">📅 17:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70570">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb0dbc493.mp4?token=mVm1TVYJB57ZEfBbhBjeRJSK_Mk2c3TvIVHEsVBdHYDdQJVyJErlxguvGY20txMunVLtYJVzOo53t_jNpuJo9kp75HHAeL1r4wpLulkScbSpOWgrrmHkFUIz9KySA4mLKjfjWEEesNumnG0WrxeLUX9Q_Q2mHAdMr8lBiFKJlGaXbCaH-YsgWT2OVJVQHaMlDrtXkaQgsFQxEZfjiAu5iGNN9YuzWKtWGltqVJgyyqUyi9d7K_1wowHzuVrbIys0sGdvicEao0wuuHMbf9s7_MpAhU_b-3J7hjNW_aX6k9I5LzHEYLzkv5H9SXCCSYwlIbZp2r3OJaKPMk7yL-bwUofulMZVBKm1UOLhRXN_eFKzQklt6ESBk5cl8HqXpqPYm8nJDm_JigzxO81LW2FA2CHm4lf-f-Q0jpEj-WFJj8VP-ARCQ724E5T6DWQAnhItTt2-_XRjUhRpYl6YXYL_JD-139J3Tt_J2Uhfy6RjIiK8F2OfMpnqa4YD2u1eRTvHGFTnSdoJjCNvBWuV_OpKkEPu9OFAf8zuhELhnoEKtvfwLpTWgn036hXz6kTFW9okzWtdGtoDlGLzFuuJuUnqzD1MR6tGhcVCR39ZV1tK0GkXIfviEcGAfGqKt4O6FWlgPlXYOCN7jQ8okYtzISo7xnDvpxPnp3H-n5ZYyT_CH_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb0dbc493.mp4?token=mVm1TVYJB57ZEfBbhBjeRJSK_Mk2c3TvIVHEsVBdHYDdQJVyJErlxguvGY20txMunVLtYJVzOo53t_jNpuJo9kp75HHAeL1r4wpLulkScbSpOWgrrmHkFUIz9KySA4mLKjfjWEEesNumnG0WrxeLUX9Q_Q2mHAdMr8lBiFKJlGaXbCaH-YsgWT2OVJVQHaMlDrtXkaQgsFQxEZfjiAu5iGNN9YuzWKtWGltqVJgyyqUyi9d7K_1wowHzuVrbIys0sGdvicEao0wuuHMbf9s7_MpAhU_b-3J7hjNW_aX6k9I5LzHEYLzkv5H9SXCCSYwlIbZp2r3OJaKPMk7yL-bwUofulMZVBKm1UOLhRXN_eFKzQklt6ESBk5cl8HqXpqPYm8nJDm_JigzxO81LW2FA2CHm4lf-f-Q0jpEj-WFJj8VP-ARCQ724E5T6DWQAnhItTt2-_XRjUhRpYl6YXYL_JD-139J3Tt_J2Uhfy6RjIiK8F2OfMpnqa4YD2u1eRTvHGFTnSdoJjCNvBWuV_OpKkEPu9OFAf8zuhELhnoEKtvfwLpTWgn036hXz6kTFW9okzWtdGtoDlGLzFuuJuUnqzD1MR6tGhcVCR39ZV1tK0GkXIfviEcGAfGqKt4O6FWlgPlXYOCN7jQ8okYtzISo7xnDvpxPnp3H-n5ZYyT_CH_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ارزش پول مملکت رقابت شدیدی با گوه داره؛
یه مادربزرگی گوشی نوه‌ش خراب میشه و میاد این پولارو میده به طرف که گوشی جدید واسه نوه خودش بخره.
به گفته‌ی خودش این پولا حاصل 6,7 سال پس‌اندازه. از دو هزاری بگیر تا ده هزاری جمع کرده که تا موقع نیاز ازشون استفاده کنه.
حالا طرف اومده پولا شمرده و مبلغی که به دست اومده خیلی جالبه‌:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70570" target="_blank">📅 17:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70569">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439a914edd.mp4?token=bD9HDiAf4eNS314ROwvjXRnjoDSxNEUC6HoHhNFI5Xi-z8FlPruPL6-ljPdeyrQnhV3s0S4TRyeXjt7AGW2BMwzaS63CZaHlOMYqbLjpvuN-1xvknZCH8gZlxBb00ziYi7TJR6zt0tKBHuIJMU0c6rww1blUNSZKGpLSDw6pY8kjEjqex7sU2B_RSLWA2ks97ZWH6kqbCnMu_LsCM7qON1_XGWv6N4V_utTIk0J5hLM4tbZX98AdCZsQv2NyCSHBjRwjXOJlpyNDZ_T4ufxP3PowojzW6ousd_fRVEiWz9p6HD1gnT7gDH8VlIhke2RuVwiP84b6GKzZlG5f30a6Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439a914edd.mp4?token=bD9HDiAf4eNS314ROwvjXRnjoDSxNEUC6HoHhNFI5Xi-z8FlPruPL6-ljPdeyrQnhV3s0S4TRyeXjt7AGW2BMwzaS63CZaHlOMYqbLjpvuN-1xvknZCH8gZlxBb00ziYi7TJR6zt0tKBHuIJMU0c6rww1blUNSZKGpLSDw6pY8kjEjqex7sU2B_RSLWA2ks97ZWH6kqbCnMu_LsCM7qON1_XGWv6N4V_utTIk0J5hLM4tbZX98AdCZsQv2NyCSHBjRwjXOJlpyNDZ_T4ufxP3PowojzW6ousd_fRVEiWz9p6HD1gnT7gDH8VlIhke2RuVwiP84b6GKzZlG5f30a6Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70569" target="_blank">📅 16:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70566">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BB9lvkHXoeLIiVjn7JMCrqmFuvrQ5up7wunEdHIGV9p_lyA_Ch0FnunLx27XJBDbXjLSZYI6VhajpsKodP--rDEM9UfHJNxHmsG5N0Vm2uHFdoQBP_5a39D5CS-kwaSICIdlgSwoz9jaY8ek3GM5JdVqT0Wfs_j9nLmeKOJyl-WyIFFrOLVp1bQ-EinzV4IjK0fRoEdiOlQ4x7QUnhiUYbEFGuRAgEGjXuFpSF4Fse0PeLlaXjHa0TBN_EKyoe2gWttR9_Lku6tsD4hvuXS8f4C1nu92h3lMgLT2STIMAg9Tegj1Gpo4hXMLq5gE7iakSBdcJTxw079yTVDlQt8KVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fVtorTMPzXXEwJ19tUR81VKTumDjCeSyh_Zo1wulYOVjIGe5rS-5vFOAtTgDtMmpT4dlM7H43RiRKxkIGAnYyPxX6_Ry9lD7BYsKFyNmGSWgmMzhSg2W3BdWe1wGm97AUAo7oxcmrH4G03aCQ8V8l9lwYnaQMccTBi9_4Rz20NTs1uwQwZEpX3I-BdTMaZ2zVa09hJqbA3KziAwrj-f_b7u8crkNo1nkNzHnS_k9WgeH19abc7lTocJfaE8xgeNXzbkvvteEGwmirbt2jwVBoV9S0n3WmE1p0-grz2t2uNaQW_RvaL3mFjYRGSlfm-WaHdqJ_E5tKGTTCgdQGfum6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XmVWhkov93jwlW8SsNOwqkrLRDq34OzXk1zADDpfJ_IcwMLxODVKfLXtMmKTFmpK3DcF7Q_GfxlKTj-_AaTcvCnKlLQWaWFT5Lkbp5MzHt3HY2WVFE42_DyIOcI9YY-8xNExR9SkkYy2FePToBhfNyZXoqaUKAlxMHIh4rR4r_LMn_bFVVy1x-CCj5dAQIzaAAuTKHri4fjWCDj7YLT1xPSxcs8c1sEIr02x20R-1c37c3XHJMjffpuTfeVFUEd2dRgU9STz5NrGyJz-qx-Xth9KigaNEEzhhUsMEuu7OrChqxIWQp9kSlYbByRdIzRHpEdsPnyKroaIVLwGTTVn8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇴🇲
🇮🇷
وزیر امور خارجه عمان، بدر البوسعیدی، با عباس عراقچی در تهران دیدار و گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70566" target="_blank">📅 15:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70565">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCh1ZR4-a05kZ-7PXxaPWmy8GMhk8F0karhsgGwlMfV1h2dLe4Q_JcP1tY6rgHH9_bHDibS3IJHp7HalHyVpPwhB1zgpTZ18hS84UkH3Dh644ZqsZIU9-_iH1dYvh1h01lThxj4Go71kUQLQtKwgFcFEMrY638RjpAHx4BVP0UFqivGLiQ6mZcqCtaH7f2X5ZkeAN5ZqW0fhbIbhhX6s87dnoUtqk5T4NC4nInYamKH9B5TiXl8yWC0YX0qkJKsfq3De1oc4IFJnBZOXYik-GnG523IfuhX4mXtNuvvPXBqmmnNq5b4HgRg8iyCcDcWMn7rp_TcyjI5ESsPesPS1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
بانک ملی ایران در سال ۲۰۱۸ به دلیل حمایت از تروریسم توسط وزارت خزانه‌داری آمریکا تحریم شد، با این حال همچنان در سراسر جهان شعبه دارد. اسکات بسنت (SecScottBessent) وزیر خزانه‌داری آمریکا به‌تازگی اعلام کرد که تمامی این شعب باید تعطیل شوند.
🚫
مکان شعب بانک ملی به شرح زیر است:
۱. امارات متحده عربی — ۷ شعبه (دبی [۲ شعبه]، شارجه، رأس‌الخیمه، فجیره، ابوظبی، العین)
۲. عراق — ۳ شعبه (بغداد، نجف، بصره)
۳. عمان — ۱ شعبه (مسقط)
۴. آذربایجان — ۱ شعبه (باکو)
۵. آلمان — ۱ شعبه (هامبورگ)
۶. فرانسه — ۱ شعبه (پاریس)
🚫
بانک‌های تابعه / سرمایه‌گذاری مشترک (در ۴ حوزه قضایی)
۷. بریتانیا — بانک ملی پی‌ال‌سی (لندن)
۸. هنگ‌کنگ — شعبه بانک ملی پی‌ال‌سی
۹. روسیه — بانک میر بیزینس (مسکو، کازان، آستراخان)
۱۰. افغانستان — بانک آرین (کابل؛ سرمایه‌گذاری مشترک با بانک صادرات؛ وضعیت تأییدنشده)
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70565" target="_blank">📅 15:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70564">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJ_l4ePDhOdbHQDCDyAsrlOkaTSLR9ZyOC7fHrfl_pYIm7gxwTSiasWQ99XfXKj8xjwfiy9wB7B2L5wP-yk80XfGhfk7hgQJGYX7YoE7D8inMUFw_Hg436ak3Dnjjq9MM8V07irq6Gx7W5wmpunzdgUsnsrlAtlc6b48xjEm1KeE2hLN7PQ7jJ4bwGqH2aqxbRkX0_xIjvjwlDevL-cLDbgACDoEfwIPfTqZtUPL-tuvcIlM-DW1VMw_rxyJfGhp9kvqLaIEeF__a36CwGR1PjHkiQeM7x7nnTK6Q-TDj073HVJE6kPm4Fro6w4IV6bzj5Envbd4Ugu2pgZz7_Mp-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی ایران که در حال فروپاشی است، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را — حتی زمانی که مشغول اعتراض نیستند — با شدتی بی‌سابقه به قتل می‌رساند. این یک بحران انسانی با ابعادی عظیم است و باید همین حالا متوقف شود. رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70564" target="_blank">📅 14:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70563">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=co3v8SmY-55xKlHrqRnBk8p6G7qIzAZ3bgwy6cTsxG5b17TZbZnRtDA2X4LYgvhBr1aBukQach200zmxOitdsPAN62OwCTcDQg3979RZRmFsBPykbgPzkE60OUYnzw7XEx9sDfnzYnWg4k8HOg5ZXWRhYKEbqXMhjWAB6rw-o985-z5B7uNfTZzqsG7XBpIaKheN51cpbAhAHS5KZr4jysmJQAvZeG2HkBLjy1kgEThmgNY7MEIIKvDrc3sEuUfN4auvVzmJrxdqxjuLaOVzMiXWYpERKhAtMJrvEy__G6ReLQHfCihNd4wp0yDHWJD_DRh_lfv19lbwFJLaCuzXoyCQyLnp43D5b2T6U8O34oXEYVn0fii9uruvKKMoR2oPZzRf9uFqVTBhdhKHz_tEmhqvKfmF2W0wCQqZmFF5Xnj4njhCYWwv405UurKdU-4CPMIj3RrFJlv_CF5tWRHP89AwVeOmdeTIdQ2xTD9t9MeR0wbLUdG-6HWws7bvqp_Rg-7R-54YgjoHYvsbFEtnmJ1fBhhkRq5iNtISswQtcD9qNb6c-6muRdDelh-NLUp41yaHkN7pPoD7D5OepQgFDn6Y4-7dqc8YzeUSz3QD7TgZCuStnuxWwhwO1I5uyJXzNhzeot0ME8Eo0mRLgDwpvX-_9Xcc6CdLakVpd0nBeDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=co3v8SmY-55xKlHrqRnBk8p6G7qIzAZ3bgwy6cTsxG5b17TZbZnRtDA2X4LYgvhBr1aBukQach200zmxOitdsPAN62OwCTcDQg3979RZRmFsBPykbgPzkE60OUYnzw7XEx9sDfnzYnWg4k8HOg5ZXWRhYKEbqXMhjWAB6rw-o985-z5B7uNfTZzqsG7XBpIaKheN51cpbAhAHS5KZr4jysmJQAvZeG2HkBLjy1kgEThmgNY7MEIIKvDrc3sEuUfN4auvVzmJrxdqxjuLaOVzMiXWYpERKhAtMJrvEy__G6ReLQHfCihNd4wp0yDHWJD_DRh_lfv19lbwFJLaCuzXoyCQyLnp43D5b2T6U8O34oXEYVn0fii9uruvKKMoR2oPZzRf9uFqVTBhdhKHz_tEmhqvKfmF2W0wCQqZmFF5Xnj4njhCYWwv405UurKdU-4CPMIj3RrFJlv_CF5tWRHP89AwVeOmdeTIdQ2xTD9t9MeR0wbLUdG-6HWws7bvqp_Rg-7R-54YgjoHYvsbFEtnmJ1fBhhkRq5iNtISswQtcD9qNb6c-6muRdDelh-NLUp41yaHkN7pPoD7D5OepQgFDn6Y4-7dqc8YzeUSz3QD7TgZCuStnuxWwhwO1I5uyJXzNhzeot0ME8Eo0mRLgDwpvX-_9Xcc6CdLakVpd0nBeDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر اقتصاد:
تفاهم‌نامۀ اسلام‌آباد روی کاغذ نکات مثبتی برای ما داشت اما اسرائیل و تندروهای آمریکا نتوانستند آن را تحمل کنند
امید داریم همان تفاهم‌نامه یا بهتر از آن احیا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70563" target="_blank">📅 14:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70562">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUARblfSQzlmRCnJvqRY6zbCPvreaAoOobXX8MqoWxl_hH7XB-nResnPswozTg6RcEup_tbuKJOF2hjNmf6bljminj0tyTuN3nEjwMkrL40YeEkJJIS08NGXbkvz9-fmN7-AuqQEexzvqB8mBbJJqgGpcZ3_H9clVg1ho2qgvj6MJk6l_0VJpCtpSllgEzt33UxpNM6b4s1W8wAQGzEq5RC0f4d3p_LKhgJOnlLjk839ymU1ApOOGMWSIMkXiDAjsHHiR1mZNMNsugMjJrbJ4BIP2O7ExDeaeWIli_JoGKZ_whUea5VyvBWc8ersqjyyBPRwQtxtyP262lG2gJslUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
حساب اسرائیل به فارسی:
درباره ماجرای دایناسور خراسان، احتمالا فردا امام جمعه مشهد می‌گوید: «این دایناسور از برکات نظام و نشانه پایداری ما از عصر تیرانوزاروس تا کنون است!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70562" target="_blank">📅 13:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70561">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
📰
اکسیوس:۵ نشونه فروپاشی اقتصاد ایران زیر فشارهای ترامپ:
⚪️
سقوط ریال؛ دلار به حدود ۲۰۲ هزار تومن رسیده
⚪️
تورم شدید؛ پیش‌بینی تورم ۲۰۲۶ به حدود ۶۹٪ رسیده.
⚪️
فشار معیشتی؛ گرونی و افت ارزش پول، خرید مایحتاج روزمره رو برای مردم سخت‌تر کرده.
⚪️
سقوط صادرات نفت؛ محاصره و فشار آمریکا درآمد نفتی ایران رو به‌شدت کاهش داده.
⚪️
رکود و بیکاری؛ فعالیت اقتصادی و اشتغال افت کرده و پیش‌بینی میشه اقتصاد ایران امسال حدود ۵.۴٪ کوچک‌تر بشه.
با این حال تهران قصد تسلیم شدن نداره و ممکنه دست به اقدام نظامی بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70561" target="_blank">📅 13:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70560">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a518ac30e.mp4?token=qneq-ByVOrVUDiJML1bYQarBRX37jsrg3aMfQcwWoLJhXHjtswJJqB_ps6KrgJupm8W9a_6l8vPi1kniUQw_uMh0yMl_IVyFZlQn0EUrWW5vN2-J7LXBx5jdg1_nwZUx6ELsKbvD4TzhfjGgmSQ9SHmdbSLEVbraZEXLWPGwtkc-LytoXTZ1mreStOmd7fktNE95sBARWBDZsP_UnU_goBnrydKvuOHj_die_5fZW5MFyplfT0egdrXw8QFgU5Y3SVIcXyM00hJe2ryxgoVXctxzAs_qfBRirlQu769IsP29LnuminyJwysW1-i8abFVdRXgkRYtV--1QSF9xZpfzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a518ac30e.mp4?token=qneq-ByVOrVUDiJML1bYQarBRX37jsrg3aMfQcwWoLJhXHjtswJJqB_ps6KrgJupm8W9a_6l8vPi1kniUQw_uMh0yMl_IVyFZlQn0EUrWW5vN2-J7LXBx5jdg1_nwZUx6ELsKbvD4TzhfjGgmSQ9SHmdbSLEVbraZEXLWPGwtkc-LytoXTZ1mreStOmd7fktNE95sBARWBDZsP_UnU_goBnrydKvuOHj_die_5fZW5MFyplfT0egdrXw8QFgU5Y3SVIcXyM00hJe2ryxgoVXctxzAs_qfBRirlQu769IsP29LnuminyJwysW1-i8abFVdRXgkRYtV--1QSF9xZpfzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما یه ویدیوی جدید با هوش مصنوعی درباره پسر ترامپ ساخته و اونو تهدید به ترور کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70560" target="_blank">📅 12:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70559">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/377055b126.mp4?token=hLny5bLzbkdoP8ojVBD_fsvudBOiyJUrbk9wpSgSTKGeh4xYg820GU-FqR0DmrVP7N-10ZXJT9CzUcBHPzthh1Iam7vpIDUtNAMGvK8GSNMPWMEN6hVh-tyAlSLfMAC5L-M4mvT7c4F1vRj7SaG5RAiqGidXegpR38fDy78SQcdrnqqyKBMA5X7hGthQesAmi2aQDlMDtJ_lJir-EK5xoLtDsNpFDBLz6Ll3PNWdxE4bZT6I7ZCeLyJug4j9W2NIBCLZDS5bkIl895LWDHg9I-tMJ8ckrl4faT6EMYahiMQuVuqgWj0hnXwZE02_yuidxelyO6ZmnEdsYRrEp7jpZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/377055b126.mp4?token=hLny5bLzbkdoP8ojVBD_fsvudBOiyJUrbk9wpSgSTKGeh4xYg820GU-FqR0DmrVP7N-10ZXJT9CzUcBHPzthh1Iam7vpIDUtNAMGvK8GSNMPWMEN6hVh-tyAlSLfMAC5L-M4mvT7c4F1vRj7SaG5RAiqGidXegpR38fDy78SQcdrnqqyKBMA5X7hGthQesAmi2aQDlMDtJ_lJir-EK5xoLtDsNpFDBLz6Ll3PNWdxE4bZT6I7ZCeLyJug4j9W2NIBCLZDS5bkIl895LWDHg9I-tMJ8ckrl4faT6EMYahiMQuVuqgWj0hnXwZE02_yuidxelyO6ZmnEdsYRrEp7jpZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این شما و این برج زنبق واقع در منطقه ۱ تهران:
۲۸۰۰ متر پارک و فضای سبز اختصاصی.
هلیپد برای هلیکوپترِ اختصاصی شما.
بیلیارد، سینما، سالن اسکواش، باشگاه، مجموعه آبی، کنسول PS5 و سالن ماساژ.
اتاق بازی کودکان، فضای اختصاصی برای جلسات کاری، غذاخوری و...
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70559" target="_blank">📅 12:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70558">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e23f896bb9.mp4?token=vuAV7Q3Oybt41rO88MlRlyTMW5_fJAk_P4iMMHwFU2KFPB0DI3qU67bH5aWPhsI4Bz6kG5qwUc7mv0dqam1C9PVMP2SrGkWXkWfdOGV9XJK_KiDyQCGmdI_W08NPoJKoc_SKDwDhKTU7P2jtgDRV2EJu3Z7_80ryYVGckSeBOdFocJLUSzYzp7w15x88g_LnVZRxV-CIXiA2ylQwGbZzqeRXaQFmCFajLyfxtqkhWSajde5EQ32Wx_twHxKfNUw3lEiZEONRSE2xH1-M_MPeckLzTpJlT6bHu7XWuE9kFRJJGhpoSkbHzRzGZsrep11vxjvnxIT0pTGXqXvGL3kuDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e23f896bb9.mp4?token=vuAV7Q3Oybt41rO88MlRlyTMW5_fJAk_P4iMMHwFU2KFPB0DI3qU67bH5aWPhsI4Bz6kG5qwUc7mv0dqam1C9PVMP2SrGkWXkWfdOGV9XJK_KiDyQCGmdI_W08NPoJKoc_SKDwDhKTU7P2jtgDRV2EJu3Z7_80ryYVGckSeBOdFocJLUSzYzp7w15x88g_LnVZRxV-CIXiA2ylQwGbZzqeRXaQFmCFajLyfxtqkhWSajde5EQ32Wx_twHxKfNUw3lEiZEONRSE2xH1-M_MPeckLzTpJlT6bHu7XWuE9kFRJJGhpoSkbHzRzGZsrep11vxjvnxIT0pTGXqXvGL3kuDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه دختر برای پارتنرش شرط گذاشته که هر بار دعوا کردیم، برای اینکه باهات آشتی کنم، باید برام طلا و سکه بخری و پول بدی.
بعد از یه مدت رابطه، این صحنه خلق شده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70558" target="_blank">📅 11:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70557">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHczLovlK-8Kq9pAt_CFIinY4QuBra3RT6NpZaOrSGnCES7lbuFxyHWDf3ZWPqNtqUUNZABxwVtzmj5Ckt4N0Sn2Qy85eq26O7Dv3G_YG6iD-e5AI1iZ2JRi2uCSxLyBG8hHIpuqxNk44LUz5jdQ1_ZswmAUWE5uXE4aFdD9M6ZwA3migHa2u0qeeo8BufOGrVQNNxX7n-ozqSnj4fOG72Uc5AENIp5G9o6oj06An8T9ZL0pkgVwhBGqDF4hlsBfHLs4WIUj-XD36wvtFLDXwaaie-tzcur30OPw3X_ZhD450QrWC7EsiJqVcLN5CdrnTN0kC6Nl6BINgm57gSH_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی از زمان دلار ۳٠ تومن تا امروز که هر دلار بیش از ۲٠٠ تومن رد کرده به آینده اقتصاد خوشیبینه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70557" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70554">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=kylBem14u6E9AyS7jjRwlRb_P3XBbdbXKQ53tpbwaOIgoEO2VIYZ1PM5pYqJ8NovBDD5rCvxMkyuDzk6gw4toVm3Q4hbH8DLtr_CfGpW8lWAFcMpkYqe27yq9MpzEu8onumb4sbCUhNA3FI5swLO9nxfWKUen9uqeCBlrjj8Roff-kDlNqC_SD2J7EnBxfdAEmrziNFYYGemmtntic6fxHTu17q1CN0gKOBpeRf4e7JsWEUlr-Px0MpLIDIb6dh4y7nBHtYkoiDhwEGbh5nYoRiMfV6vMay6j6jD8ts3uArkDA3sLIJZPQn3whnzfDfRLPFHa_6NutjuTK_g0nqFaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=kylBem14u6E9AyS7jjRwlRb_P3XBbdbXKQ53tpbwaOIgoEO2VIYZ1PM5pYqJ8NovBDD5rCvxMkyuDzk6gw4toVm3Q4hbH8DLtr_CfGpW8lWAFcMpkYqe27yq9MpzEu8onumb4sbCUhNA3FI5swLO9nxfWKUen9uqeCBlrjj8Roff-kDlNqC_SD2J7EnBxfdAEmrziNFYYGemmtntic6fxHTu17q1CN0gKOBpeRf4e7JsWEUlr-Px0MpLIDIb6dh4y7nBHtYkoiDhwEGbh5nYoRiMfV6vMay6j6jD8ts3uArkDA3sLIJZPQn3whnzfDfRLPFHa_6NutjuTK_g0nqFaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی در طول شب سه مرکز لجستیکی اوزون را در سراسر روسیه هدف قرار دادند و تأسیساتی در آدیجیا، استان استاوروپل و داغستان تحت تأثیر قرار گرفتند.
این حملات در میان مجموعه‌ای گسترده‌تر از حملات به مراکز توزیع بزرگ روسیه، از جمله سایت‌هایی که توسط اوزون و رقیب آن، ویلدربری‌ز، اداره می‌شوند، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70554" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70553">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70553" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70553" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70552">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCTgJRhnm8RtxozBrW-Iuu6fnTizKR3D3nwx-8K6trwgbe8ddNp7Pw7_HKKggS_1gFIA0iOI6bEooKzarWNeEtehP9W0fnNElPNN4kLU54pqE71S2fZniqMTvZevOcxyXRpla-_CvxvT3SyYMFdfjGLaK37wtAuojdBX_1Wpa1KvMC5aGFCvFw6CEsPfRokWewBHIRv-Hyq5kT6SPXgi2lhHRHKgvKwanq3TRpxa34JCdkvo55ErXAECOmsCgzBhjo9KiDv0oqhSXqGNVl9kwZ-3ZlFIv5FrowTKWxGUlygvs2nfrSa-NZUOBRZir9AiCWzqhrAcuPqXaDKO4R2NBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r3
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70552" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70551">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇵🇰
وزیر کشور پاکستان: پیشرفت قابل توجهی در گفتگوها با ایران حاصل شد
⏺
📰
خبرگزاری رویترز به نقل از وزیر کشور پاکستان:
پیشرفت قابل توجهی در گفتگوها با رهبری ایران حاصل شده است.
ما در حال گفتگو با ایران برای فعال‌سازی مجدد «تفاهم‌نامه اسلام‌آباد» جهت حل و فصل اختلافات هستیم.
محور گفتگوها با ایران، تمرکز بر تنش‌های منطقه خاورمیانه(غرب آسیا) و یافتن راه‌هایی برای گشودن مسیر صلح است.
دیدار با رئیس‌جمهور ایران با نتایج بسیار مثبت به پایان رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70551" target="_blank">📅 10:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70550">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b422bdb1ee.mp4?token=HtyDJTOt4d3sCOzBkb-y7h5sL1jCU76ScCpzWMFlyFWKpYpidzZjpfw-uuFYghuuX6b-RSCtkF4dSg5ullRJWtNtDBge8NdmRToMbnI-JI_ixCg-bMbfpVX8jU06zsuzVi0NX2bI3G_e0OM3DJNv3BbuwBmq5Y5V48wBTT4BHrekqkNTB6teX-o1Z8ieNSY819ZdrmGaHPmR3i7dQzuuO70SM3Fno2UYucGGPO56DllyMbxirWCbPhxG2vcIs16mxLtiCc-JswtNl8aUkjj167H3AuOR8H5o5YqPD7ZlZhqw0mtTvxaq2dWqZ9tTAf_j4ggBvis6YUQ_XECvyiQU6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b422bdb1ee.mp4?token=HtyDJTOt4d3sCOzBkb-y7h5sL1jCU76ScCpzWMFlyFWKpYpidzZjpfw-uuFYghuuX6b-RSCtkF4dSg5ullRJWtNtDBge8NdmRToMbnI-JI_ixCg-bMbfpVX8jU06zsuzVi0NX2bI3G_e0OM3DJNv3BbuwBmq5Y5V48wBTT4BHrekqkNTB6teX-o1Z8ieNSY819ZdrmGaHPmR3i7dQzuuO70SM3Fno2UYucGGPO56DllyMbxirWCbPhxG2vcIs16mxLtiCc-JswtNl8aUkjj167H3AuOR8H5o5YqPD7ZlZhqw0mtTvxaq2dWqZ9tTAf_j4ggBvis6YUQ_XECvyiQU6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو به تازگی وایرال شده از یک گروهی که رفتن کرمان و در مکانی بنام قلعه دختر مثلا جن احضار کردن
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70550" target="_blank">📅 10:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70549">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a52e52e69f.mp4?token=FMuh78GkfkEnPzLn9blCF9APVEfj9VCVyfWkVHjGIA3r5Z82uWMSFRQCT1wLLXI0hAUKb-h_cHdgQsYKzUGEnNqglawp2Eb98CORxhG4RCYaUqbYyd7LX7jvumGAypThVJctAnsCskqPeRxyEfWQEoopB0cQARNQvOKhWn1mRt6LDXPvEMYoWujN29MvN80Ezq29UG6POyPumB0shKQjdGnHnxq2WZUpe1MKxKQWMLIdtMt1h8se8Fb366DgP1EZAvQlLPhhjkbALyn2t0hPC0OQaYSRxs5zKWe_ZucqAuinHgemw7btkM7zXoUR4BCu31p3gaUtkLwm4tNISG7JzVX_UWR_kKFoOUNzIplCj2nbiKcbJC5fQatYkfxX859koberthYUKzpZV4u2pvgJ4BqF1iq3SGOJ0xjceenq61hSUcdLJ4z0gS9rcnpBvXGZXSfxWEN3yvfOOf2369D_YQsct8QM6melS_HUngUGTX9A_1ZCGoDJqJ-1XR925yFXXaltRFlhIrXzNyBnuRu43xcQ5cI4oO2Q-UjeDeHHWRWh-2z__G6zJiQUshMwOiRdk_SkRDFu-PrtUB4OaSRftJZhUogTjPB6meakMOM_WADqQXytJJnAGK9R7APw8nZsIpHtPl3Ak16KopjAu9mc3y6TN0amcwnSShffjDRHOCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a52e52e69f.mp4?token=FMuh78GkfkEnPzLn9blCF9APVEfj9VCVyfWkVHjGIA3r5Z82uWMSFRQCT1wLLXI0hAUKb-h_cHdgQsYKzUGEnNqglawp2Eb98CORxhG4RCYaUqbYyd7LX7jvumGAypThVJctAnsCskqPeRxyEfWQEoopB0cQARNQvOKhWn1mRt6LDXPvEMYoWujN29MvN80Ezq29UG6POyPumB0shKQjdGnHnxq2WZUpe1MKxKQWMLIdtMt1h8se8Fb366DgP1EZAvQlLPhhjkbALyn2t0hPC0OQaYSRxs5zKWe_ZucqAuinHgemw7btkM7zXoUR4BCu31p3gaUtkLwm4tNISG7JzVX_UWR_kKFoOUNzIplCj2nbiKcbJC5fQatYkfxX859koberthYUKzpZV4u2pvgJ4BqF1iq3SGOJ0xjceenq61hSUcdLJ4z0gS9rcnpBvXGZXSfxWEN3yvfOOf2369D_YQsct8QM6melS_HUngUGTX9A_1ZCGoDJqJ-1XR925yFXXaltRFlhIrXzNyBnuRu43xcQ5cI4oO2Q-UjeDeHHWRWh-2z__G6zJiQUshMwOiRdk_SkRDFu-PrtUB4OaSRftJZhUogTjPB6meakMOM_WADqQXytJJnAGK9R7APw8nZsIpHtPl3Ak16KopjAu9mc3y6TN0amcwnSShffjDRHOCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیوی جدید از حمله هوایی و پشم ریزون آمریکا و اسراییل به خرم آباد در جنگ ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70549" target="_blank">📅 09:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70548">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10dcd43f2.mp4?token=jqsBjo8ZkfxGTizWhqRORtAN-kY9PzF91DnA9916SsEpmZGaLWeWHK_lXPOYcw5GnmWvtAYatrbHet_gnTFcVumz_UfPHwxUsbqNDujR4-gngWLgMqKQ1vlH8dFW9MP5F_axwzFE53oacs3WdakXQmKGJCyD93QFwGIk9Rp29BPKKP5nYXGF0YkIO_Zt_NP-gwWMtuSqnuUE8wjAJJeSZXrSBxEJrfruXoL1Y_OR6un4O5IF5-GoH8gxaBBy1pt3P2ygOl0xjLFJDB2QlaQZhgHOgtmwgT1CSv6BtCqiNDIl8YnQCchdYWNb9chaLzmJ1UwVWT0UczHval7sYHi1vBi3IwZQiOTRFUbO_rjsWBuyl0T-nyqfCEwUP7DZa_LzPDVw4tB7y_mZzngALI-aTV2EcUFAZLwgiVyezEPUFZ0EH_4BK2E-BAyKN84Ta358HbPiWQEcW52TeWir_CfoJzJ9G7YhpuxzT191kQ1lqLidnhlG3YbvLxZyIK8de9Z8HEhnX8JYnUJxhfaEsqz5p44Orx1ItwyKzAyfVdigl5KwZsX48JLY9GS10plSV6j1hN_cVqUn8TTceL3TaHRxSMCIrvHge_jcbYkBbRgPnS1__OdfBkPnN3G9FfMhyaNhnZfCTZriSwApHDN915yRSx4wDh68GhsCojbwXnaNiis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10dcd43f2.mp4?token=jqsBjo8ZkfxGTizWhqRORtAN-kY9PzF91DnA9916SsEpmZGaLWeWHK_lXPOYcw5GnmWvtAYatrbHet_gnTFcVumz_UfPHwxUsbqNDujR4-gngWLgMqKQ1vlH8dFW9MP5F_axwzFE53oacs3WdakXQmKGJCyD93QFwGIk9Rp29BPKKP5nYXGF0YkIO_Zt_NP-gwWMtuSqnuUE8wjAJJeSZXrSBxEJrfruXoL1Y_OR6un4O5IF5-GoH8gxaBBy1pt3P2ygOl0xjLFJDB2QlaQZhgHOgtmwgT1CSv6BtCqiNDIl8YnQCchdYWNb9chaLzmJ1UwVWT0UczHval7sYHi1vBi3IwZQiOTRFUbO_rjsWBuyl0T-nyqfCEwUP7DZa_LzPDVw4tB7y_mZzngALI-aTV2EcUFAZLwgiVyezEPUFZ0EH_4BK2E-BAyKN84Ta358HbPiWQEcW52TeWir_CfoJzJ9G7YhpuxzT191kQ1lqLidnhlG3YbvLxZyIK8de9Z8HEhnX8JYnUJxhfaEsqz5p44Orx1ItwyKzAyfVdigl5KwZsX48JLY9GS10plSV6j1hN_cVqUn8TTceL3TaHRxSMCIrvHge_jcbYkBbRgPnS1__OdfBkPnN3G9FfMhyaNhnZfCTZriSwApHDN915yRSx4wDh68GhsCojbwXnaNiis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان تحلیل‌گر ارشد سیاسی در مورد فشار اقتصادی آمریکا؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70548" target="_blank">📅 09:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70547">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70547" target="_blank">📅 02:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70546">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAmxYoJeZMzw8gdGk71NAqD8bhkHxPA3c79NR1OaANHLugv60QMV81EBDR9X_vWlnuVUVuxoYOpJK_Ec6GvoO1c_JPIEGlDZKu9DzdaPlSYmcvwiGtqO9202QM2JJmmKoUzGBQS4WKc8GrcseX3b3zjVMfASBVdw4umtgPCPsjBVO_Nu-3wPTfPIbBfCNAY4bQQGof3ff3RrdJ7P8n9cyuBTLtFSGlHmanJB94oqJ4EzaV4OZoTQxkaDI9LL0ilBmxuR0JtfJs6eqpWAAH_puFEAdb9XzgO5bg-ufnjLUeqhlIuaeTpplcrsfjOw8Z-bZ2QRGDSYJUU9XOnn-dINd_QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAmxYoJeZMzw8gdGk71NAqD8bhkHxPA3c79NR1OaANHLugv60QMV81EBDR9X_vWlnuVUVuxoYOpJK_Ec6GvoO1c_JPIEGlDZKu9DzdaPlSYmcvwiGtqO9202QM2JJmmKoUzGBQS4WKc8GrcseX3b3zjVMfASBVdw4umtgPCPsjBVO_Nu-3wPTfPIbBfCNAY4bQQGof3ff3RrdJ7P8n9cyuBTLtFSGlHmanJB94oqJ4EzaV4OZoTQxkaDI9LL0ilBmxuR0JtfJs6eqpWAAH_puFEAdb9XzgO5bg-ufnjLUeqhlIuaeTpplcrsfjOw8Z-bZ2QRGDSYJUU9XOnn-dINd_QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
⭐
کانال اطلاع رسانی سایت:a2
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70546" target="_blank">📅 02:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70544">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bk_bwNWPnIAnnR4NDI2DaQWAV-Rx-0CBYegzTNgFfXvesnlLK54KRd2-aJcSN2LHGSAubQE4lZnfZ2lw084rZI-p8yqlxpurXNEc5G2AvgKZE7eLYJeeJr8F4o21yznTULa_lMikl7Yg6pfUyII1r2Ex8JlrM4utwQAFRLVR8B-VK3AEPh2FkmYGbZrmxzrzh3x1nr0UtAtvKlb-4cV_PqHzQt-Icd6uNQWqOYdsFMhn1krWQktRJ3KotZ__skXBG0A7HBkh4BZja8LzHE6BZV07DWbKNHklfNWPAwSvzPF1V6v-cbOz-WVKay4u-8n-_emZqYKzSGwkONCiJuGZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCLxhc1CX-rN_tmEo1UM4Aga7yuriLEiU9-rvmS2jH-XiSWrHrOZlC9O85RKniCT13vbGCGZfRyO4Qg9kGqSetcGK7NuQ6sdvb0z7fvjXCqmxiyL5aTqvcxVJkDDh7yK-MyQ8OZtkpX6LwtI9wX0W7H92McJkUYIayrqaJu6BxSWhG9LmHVmn0FVm_-_AH1njqCMxEq8BtqbUMJuEloot4I69GDrbG9UTRXffP5vrggDgwo46M09gUZRlKIW8yE5U5rXipfM9nO6g0sl-Zh6zlIHdWNx6p3C6iZi6Zwmh_9YEaZjJSa-Jni4ke_5WbS6giopQVJhppkPBNm_mrWLKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
#فوری
؛وزارت امور خارجه ایالات متحده:ده میلیون دلار برای کسی که اطلاعاتی درباره رهبران سپاه پاسداران انقلاب اسلامی ایران ارائه می دهد
احمد وحیدی/ فرمانده سپاه پاسداران
علی عبدالله/ فرمانده نیروهای مسلح (خاتم‌الانبیاء)
سعید آقاجانی/ فرمانده واحد پهپادها در ستاد هوافضای سپاه پاسداران
حامد لشگریان/ فرمانده واحد سایبری در سپاه پاسداران
مجید خادمی/ فرمانده اطلاعات سپاه پاسداران
⭕️
خبر واقعاً دوباره در ۲۴ اوت ۲۰۲۶ در حساب (Rewards for Justice)منتشر شده است اما تصویر قدیمی است و بروز نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70544" target="_blank">📅 02:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70541">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=diLYV4aYPW9oF50mqKmFFPWhYfOplQT633rF7jcvhVFmQQWH5yLO55ATli-fpfn0KYl9iqaXBggbZZnIFvcf1ACVSn_gwH_ErWJIb4yeVMf4vUjuuXaBTVNVERB_zyGg6QHrBmZ1xeFdls_cFAspHjGCX4b9pVxYxuTZPorKYwWaZrlxtYDbm_HwSEQ2RKbZKT4YWnVUfw2E80_5CqwUrqJ5Ai-zgwt4L5vh8lU9sGyVfGvDXJJdkjwwI9Yn4K_aCcTRvxPHZeXivX0bIZKrMezN44KRk5HPCbkcSy8A9TgmZWbUo7v287YnsWISWOK8aNXmib-imBe_tEfWPYJb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=diLYV4aYPW9oF50mqKmFFPWhYfOplQT633rF7jcvhVFmQQWH5yLO55ATli-fpfn0KYl9iqaXBggbZZnIFvcf1ACVSn_gwH_ErWJIb4yeVMf4vUjuuXaBTVNVERB_zyGg6QHrBmZ1xeFdls_cFAspHjGCX4b9pVxYxuTZPorKYwWaZrlxtYDbm_HwSEQ2RKbZKT4YWnVUfw2E80_5CqwUrqJ5Ai-zgwt4L5vh8lU9sGyVfGvDXJJdkjwwI9Yn4K_aCcTRvxPHZeXivX0bIZKrMezN44KRk5HPCbkcSy8A9TgmZWbUo7v287YnsWISWOK8aNXmib-imBe_tEfWPYJb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم تکون دادن ترامپ در رویداد «Freedom 250 Grand Prix» در واشنگتن دی‌سی، برای آغاز مسابقه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70541" target="_blank">📅 02:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70540">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xsr1ZB05nZ1JLJcXk8RLURm12EZIPLhDk-MXGcPv7ugPtyw-M0CuaBijR3swyJpxte7sGd2nlxUX_xe_nW70lPgkfvi_NUMf9f2U8t5GaYbQDmJrbkB5JNEu5YF_vVKXXhvUgdHI-baA206dFI-BU4ul3I_BCfq4_IK42FvEHPqcCs1LjW2hI2_RMcNzh4KGtDMexi8om8dVlwFDVylfWDtaaR1gwP5DUDfE4rPb68gm2bt9tn4lHi7VeItEdTKmhRWlETRY1fGbXgoeO5Ro4BCjLgmQV7zcRQ37e_i0qaT3efgF4oqnQfCSNKwmk9TaO1wfsFyZ4E3O9-mea5zmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا:
ما گزارشی درباره وقوع یک حادثه در فاصله ۹ مایل دریایی شمال‌شرق منطقه الشیشه در عمان دریافت کرده‌ایم.
یک نفتکش مورد اصابت پرتابه ای ناشناس قرار گرفته، بخش موتور آسیب دیده و کشتی از کار افتاده.
خدمه سالم هستند و تاکنون میزان تاثیرات زیست محیطی این اتفاق مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70540" target="_blank">📅 02:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70538">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6611759db.mp4?token=FuC2ry9r76OZr5JdABEkj8mWOsbYSiw1_b2CZaTr_slSJmvKdyv7DsVQU9uXDhGyY41f1ehwQLaL8tkYhr51xBlmw2r5Q99GDHJNiT_1p0tswEEJGDrhSQlIqCpWDVjiKN1txXMTTTB8kLjufvNLjmSLHkeBC0lKF3qTKf8oHSods73rN2GQDnXxq3gMjSgyjB3k6EBldGe6Bxc6lPOZSUUiZko1hrstOnDs4d0zNvo1Kuqf53tO44LYY-phdSTnsBFTeEy3MBXGmeYkKudabk3Mgc3vmNo9-CeTQBs9TU8yTEZiDI-Kf6MOftcMdkc8HN6NRNuEo3faDVy0URPPig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6611759db.mp4?token=FuC2ry9r76OZr5JdABEkj8mWOsbYSiw1_b2CZaTr_slSJmvKdyv7DsVQU9uXDhGyY41f1ehwQLaL8tkYhr51xBlmw2r5Q99GDHJNiT_1p0tswEEJGDrhSQlIqCpWDVjiKN1txXMTTTB8kLjufvNLjmSLHkeBC0lKF3qTKf8oHSods73rN2GQDnXxq3gMjSgyjB3k6EBldGe6Bxc6lPOZSUUiZko1hrstOnDs4d0zNvo1Kuqf53tO44LYY-phdSTnsBFTeEy3MBXGmeYkKudabk3Mgc3vmNo9-CeTQBs9TU8yTEZiDI-Kf6MOftcMdkc8HN6NRNuEo3faDVy0URPPig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
برخی از کاربران فضای مجازی مدعی شدن امروز برای اولین‌ بار جایگاه های بنزین تهران با کمبود بنزین مواجه شدن:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70538" target="_blank">📅 00:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70534">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsF9oOW4go6hE0jXbbvtOtsA16e7LIJ0tWsKMTKaTQZqJw_Jgk7jsH3eKzWA326-Rg37jg2xMRi7UKZ3vBxx3EHJm7cqoF2WosKcyBW8F37r_SvoCIq_2wKOCyLVyiuKz5g5KJ5LzgWbnhAzCUNWh0yeOoinVtykFWrhKZdHHtexrlOuSSiWcdgrOWihAJNaq7_2snAs7lxUkEXZH6H80x4JnuuCM7bNP11scIjbAgoaBNRbGnnsksHCTP1ZpOEJKru50-LQndGlD_xlc7-rZc1R2YYX81lDEe5YTsNN8_sZd8g1anycSksJLMT3KLOEYP6UkBNVKBXEGUsIN9R2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a3f2ccf.mp4?token=l502aQh3cy8yNkDExIVmqPLHjb-pxeNKLBk-NPvDZmFrMrXiF81TaPUFW1jtHZ_XdsvBayn1K2XvblQp4b25P1u63TKPMmRws-W8U2aNDuXfFDVdHYWqWdl0p_3MB5hXKCjFYuUkI7xWYztdiGhwNSK9PmZTIPwiQ1z8sqEd6xxTAO2owqFYrp_NNDdnhw7N4V6_vehUtB2cGayfzo791YZ5KhnBGJH56LcBg-kr-imkFeG920Hcif_IC4yM_yQtePy1iZ3igKyI_UWQWE5p0GEyvuN_Mw0ZkquHMhJWGDq7jPVbidsLi-jAvggKbn7MoRnLSn9xGJRiXBp9CBjegA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a3f2ccf.mp4?token=l502aQh3cy8yNkDExIVmqPLHjb-pxeNKLBk-NPvDZmFrMrXiF81TaPUFW1jtHZ_XdsvBayn1K2XvblQp4b25P1u63TKPMmRws-W8U2aNDuXfFDVdHYWqWdl0p_3MB5hXKCjFYuUkI7xWYztdiGhwNSK9PmZTIPwiQ1z8sqEd6xxTAO2owqFYrp_NNDdnhw7N4V6_vehUtB2cGayfzo791YZ5KhnBGJH56LcBg-kr-imkFeG920Hcif_IC4yM_yQtePy1iZ3igKyI_UWQWE5p0GEyvuN_Mw0ZkquHMhJWGDq7jPVbidsLi-jAvggKbn7MoRnLSn9xGJRiXBp9CBjegA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خرسی که وایرال شده بود مهمون سفره کوهنوردا میشه
متاسفانه رئیس محیط زیست مشکین‌شهر از شکار شدن این خرس خبر داد
💔
شکارچی هم همراه ۴ لاشه از حیوانات کوهی دیگه دستیگر شده
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70534" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70533">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTX9EJn1KqgiMd4r5FWKwycrxd-JBgN9-BxQiBKxiWZHm-i29QJj32fmGzC3bU7l6sNzWWkWdIw4VuL0nsMDxGb6cGSI50VfsQOwzgEI-H-Wz-J6GsdNUdyuldmu2eOjtpff2TJ1w5YmcpteVR2lViJmbeXQ7y4LW1fmXrba26kQE_vqHc5kQORLVf1T73N-LSH-XE54vwdAdp9C3Cj-2Ntk9ii5aXswo2YIKc7lNlR1smS08AcwhZni3d9LVyiYH-fN6zUpgcN7hQmlNMW6xsQ1eFXPemFo4zeH8CSFbhI2NVQ2YSlMaEj8reElP2UUp8wresJtxQ_Z-xuC1x6Yxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
به دونالد ترامپ، رئیس‌جمهور آمریکا، و اسکات بسنت، وزیر خزانه‌داری آمریکا، بابت تحریم‌های جدید علیه جمهوری اسلامی تبریک میگم.
شما کاملاً حق دارید از این دیکتاتوری سرکوبگر و کسانی که به ادامه اقدامات تهاجمی اون کمک می‌کنن، هزینه سنگینی بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70533" target="_blank">📅 23:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70532">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=SyzfBPnTuoFt7bcbrvbrduhUQy9e_5-Gtbbim4dLKUS2239YnZ4Kmg32NlLyUD9tx5zW6U1WEvBmJXSncieTlujjZogq7dIADtmihS_8PCwXfrlAaUk_7c7C62Q-rMMkKOwUcR_7vfgJuGbsmhhgJhXSIYNcyyk8cKCx5LtWxxhU04JX-NPfj8mrhvZdke-roUcKKSJCl-pD09Ajrkqjwg3W8c8nMCoIQLsCCMlEliKvvkgxX_y1kFUyP4CHQ2BBk862jekgkfbtqsNXvH5y7PEiuJ_qeIBzBRuLB2lGWNKqqs_wFFKrUQuUMnkP1Qr4RqhNvJH8TmDBHEeu7SNfdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=SyzfBPnTuoFt7bcbrvbrduhUQy9e_5-Gtbbim4dLKUS2239YnZ4Kmg32NlLyUD9tx5zW6U1WEvBmJXSncieTlujjZogq7dIADtmihS_8PCwXfrlAaUk_7c7C62Q-rMMkKOwUcR_7vfgJuGbsmhhgJhXSIYNcyyk8cKCx5LtWxxhU04JX-NPfj8mrhvZdke-roUcKKSJCl-pD09Ajrkqjwg3W8c8nMCoIQLsCCMlEliKvvkgxX_y1kFUyP4CHQ2BBk862jekgkfbtqsNXvH5y7PEiuJ_qeIBzBRuLB2lGWNKqqs_wFFKrUQuUMnkP1Qr4RqhNvJH8TmDBHEeu7SNfdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اوستاد خوش‌چشم :
جنگ بعدی تو آبان و آذر با بمب باران شدید آمریکا شروع می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70532" target="_blank">📅 22:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70531">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">با این کیر شق شده‌ای که من از اسکات بسنت و ترامپ می‌بینم، مطمئنم خیلی زود دلمون برا دلار 200 هزار تومنی هم تنگ می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70531" target="_blank">📅 22:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70530">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=eRDa04v43AXkfQkwo8F7uv7KWHq0xZL7yQsFlglELqeOg92V9OAIEGbrzZLIycZMT-y-EffTxYVC5wdTGReVghrjp7mmSFzDyr2xKYGcdpQNr86_GUapQdt2oKSBwttyEBdaa4qyiK15XotQOxIYLcrDK0e_Db3Mu3NIWOUCjMebj1vRyZYDUARw63Lkbbg3vhjidO326Ccj8zyiu01c8uHBI-HYe9HufMKOoy_Gvqnogdk7J9iGCkqMRx550oM8PhPM2S2D_8gwZTQOPIDxNhOyvuOLc-g37M6I26vGOmXXSvcjZ1-MCCUU1LkDBCQVob6_YWEvpp9DvW1JXzbLtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=eRDa04v43AXkfQkwo8F7uv7KWHq0xZL7yQsFlglELqeOg92V9OAIEGbrzZLIycZMT-y-EffTxYVC5wdTGReVghrjp7mmSFzDyr2xKYGcdpQNr86_GUapQdt2oKSBwttyEBdaa4qyiK15XotQOxIYLcrDK0e_Db3Mu3NIWOUCjMebj1vRyZYDUARw63Lkbbg3vhjidO326Ccj8zyiu01c8uHBI-HYe9HufMKOoy_Gvqnogdk7J9iGCkqMRx550oM8PhPM2S2D_8gwZTQOPIDxNhOyvuOLc-g37M6I26vGOmXXSvcjZ1-MCCUU1LkDBCQVob6_YWEvpp9DvW1JXzbLtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیوی وایرال شده از یه پیرمردِ حامی حکومت که به طرز سنگین و عجیبی داره پرچم تکون میده:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70530" target="_blank">📅 21:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70529">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9839729319.mp4?token=owRLGUwQC4wggMmuk35MtxzNzXdCLDJF8c9JHOSwQfEHlJKdmLk6Octft5_wM93Mitiwz_uOIoYuozWrdFt5heTL7X2O0luRO1-4L8WbS3ZkTdJm6AVLsGnVJutDjVibGpXueFYerGgR54kJG4MmuPh6-L2qWJC-ELcXHFwW9seR_ya67zYCScXZ693uKglVEvw-SgvumodT0mZaNR6OEEtv0uo8jsL50AQm5_W0kh2voHZeXt-Sn4Zu0hNlidCIrdKi5HyWpEK3fUU4pwAKfNrKtvHbHPn6oJ-raPSm6BOpczuDr-5LvEE_Az4V-9-JZBcXQdu5qNMaqone2ZAbJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9839729319.mp4?token=owRLGUwQC4wggMmuk35MtxzNzXdCLDJF8c9JHOSwQfEHlJKdmLk6Octft5_wM93Mitiwz_uOIoYuozWrdFt5heTL7X2O0luRO1-4L8WbS3ZkTdJm6AVLsGnVJutDjVibGpXueFYerGgR54kJG4MmuPh6-L2qWJC-ELcXHFwW9seR_ya67zYCScXZ693uKglVEvw-SgvumodT0mZaNR6OEEtv0uo8jsL50AQm5_W0kh2voHZeXt-Sn4Zu0hNlidCIrdKi5HyWpEK3fUU4pwAKfNrKtvHbHPn6oJ-raPSm6BOpczuDr-5LvEE_Az4V-9-JZBcXQdu5qNMaqone2ZAbJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
«بِسِنت» درباره ایران:
کشورهای حوزه خلیج فارس در طول سال‌ها از سیاست مماشات با ایران چه چیزی به دست آورده‌اند؟
زمانی که ما ایران را بمباران می‌کردیم، ایران کشورهای حوزه خلیج فارس را بمباران می‌کرد.
سیاست مماشات در قبال این رژیم کارساز نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70529" target="_blank">📅 21:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70528">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fd4a88095.mp4?token=GgkC9dej4eP5sN69jTMJIkgUt6kvKJjDEk_Lpv970v7ZZICCWayafqOYnHz5QnW8lrGFQmPbHJYF1a2v9Iqn5lEgOn6QsmO7tyLf0ebtYYAcPEsya_QFzIAUVKuGzeHSBJybWwEhr_32yfEuf1WUYXhE-dQI4YpQ-WS-ntLdR_zRLasZWdLWilcI0f6Cspv51FOjLo5uNYlxufZWChwMSqPVcZFKJWjxgunVZIZAAfINnNqmD_6VYt2Mdwefbjk3ljsYyclFEivZKPvbaJ_iFtzCSwkYVLiaJafcBzQSCrg6GvRnUoeqt0J6d7MVrPfhVc0MaGAvZpDYaSmHWxlOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fd4a88095.mp4?token=GgkC9dej4eP5sN69jTMJIkgUt6kvKJjDEk_Lpv970v7ZZICCWayafqOYnHz5QnW8lrGFQmPbHJYF1a2v9Iqn5lEgOn6QsmO7tyLf0ebtYYAcPEsya_QFzIAUVKuGzeHSBJybWwEhr_32yfEuf1WUYXhE-dQI4YpQ-WS-ntLdR_zRLasZWdLWilcI0f6Cspv51FOjLo5uNYlxufZWChwMSqPVcZFKJWjxgunVZIZAAfINnNqmD_6VYt2Mdwefbjk3ljsYyclFEivZKPvbaJ_iFtzCSwkYVLiaJafcBzQSCrg6GvRnUoeqt0J6d7MVrPfhVc0MaGAvZpDYaSmHWxlOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
بِسِنت درباره ایران:
کسانی که در کنار ایالات متحده می‌ایستند، از مزایای شراکت ما بهره‌مند خواهند شد.
تمام شعبه‌های بانک ملی(ایران) باید تعطیل شوند.
🎙
خبرنگار:
گفتید ترامپ با رهبران جهان تماس می‌گیرد. او با چه کسانی تماس می‌گیرد؟
🇺🇸
بِسِنت:
ما نامی از افراد نخواهیم برد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70528" target="_blank">📅 21:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70527">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d89159ae.mp4?token=vGYqnXMLm3XJuf1DuRajFOFPAeqkQKgkN6Pv8_5eWe1GiXW5BNoV_ZXuCt9T_1MTTcW3URK65cqa1Qz2nseAzrnjX8BJ9fgIckqSmK2N6jJnVHRlU1BebTdQbSoLcvtyUwGCqMDAHBrinssz0Iira_BJg322thIbtRNUnA-mCRPNCaXnCmmcU7FGhZrCIeBJHYzCwhWdbMQnOBy0hpvPnZlifFU6huAYx4Svex5QQUdbFR3WzH9AYJXhqxZ5WehC8voyJv-CCaGN8akA-8uzDX4v6ew1JZ3zJ_HlTjkU3U0mlDDX2FyTKeaGMI66-LOLI7YrQ8RPbdMqq44jbPm8RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d89159ae.mp4?token=vGYqnXMLm3XJuf1DuRajFOFPAeqkQKgkN6Pv8_5eWe1GiXW5BNoV_ZXuCt9T_1MTTcW3URK65cqa1Qz2nseAzrnjX8BJ9fgIckqSmK2N6jJnVHRlU1BebTdQbSoLcvtyUwGCqMDAHBrinssz0Iira_BJg322thIbtRNUnA-mCRPNCaXnCmmcU7FGhZrCIeBJHYzCwhWdbMQnOBy0hpvPnZlifFU6huAYx4Svex5QQUdbFR3WzH9AYJXhqxZ5WehC8voyJv-CCaGN8akA-8uzDX4v6ew1JZ3zJ_HlTjkU3U0mlDDX2FyTKeaGMI66-LOLI7YrQ8RPbdMqq44jbPm8RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اظهارات «بِسِنت» درباره چین و ایران:
امروز می‌خواهیم به صراحت اعلام کنیم که هیچ‌کس از دسترس تحریم‌های ایالات متحده مصون نیست.
اگر آن‌ها تراکنش‌هایی را تسهیل کنند و بخشی از آن چرخه‌ای باشند که نفت ایران را به پول و ابزار سرکوب تبدیل می‌کند، هدف تحریم‌ها قرار خواهند گرفت.
⭕️
اکنون زمان آن فرا رسیده است که رهبران جهان میان آمریکا و ایران تصمیم بگیرند.
انتظار دارم تا پایان همین هفته شاهد اعلام خبر مهمی مبنی بر اعمال تحریم علیه یک مؤسسه مالی باشید.
🎙
خبرنگار:
شما این وضعیت را یک «روز دی» (D-Day) اقتصادی توصیف می‌کنید، اما «روز دی» صرفاً تهدید به تهاجم نبود و ایالات متحده هم برای آلمان ضرب‌الاجل تعیین نکرد. چرا تحریم‌ها همین امروز اعمال نمی‌شوند؟
🇺🇸
بِسِنت:
چرا باید بخواهم نظام مالی جهانی را منفجر کنم؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70527" target="_blank">📅 21:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70526">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155ae6e1ec.mp4?token=OSlSMChp0AEHnrqammOVsoaWZI-fJs_uxPI-ZiHDK2PktBc9sPjEpHewqsjudA88j7tSJwG2U-Bze6IYwEt9QdWNSmXotcPEuEbs2YNcRJCZ5POtCMbstPdDxTVwWym_1NWAnDX2wn9GQIvgvPNdi06QqbSTjgSlGHiLJxXkky6SBuAFR4cmExaxsaS_XHAyJuzPo2RINdLpfo7yxAyKSsdiu095AOZGtu_6xzWW7sACvOlDdaN_B4YFD761TXwvI72kY1WgV6MDSYJvkJWW4A0QW6hu7qP4P8NQJEj1gjkrtj0DmYyUYCIj9Q6noayHTFVAh2J88-gixewr0KtnDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155ae6e1ec.mp4?token=OSlSMChp0AEHnrqammOVsoaWZI-fJs_uxPI-ZiHDK2PktBc9sPjEpHewqsjudA88j7tSJwG2U-Bze6IYwEt9QdWNSmXotcPEuEbs2YNcRJCZ5POtCMbstPdDxTVwWym_1NWAnDX2wn9GQIvgvPNdi06QqbSTjgSlGHiLJxXkky6SBuAFR4cmExaxsaS_XHAyJuzPo2RINdLpfo7yxAyKSsdiu095AOZGtu_6xzWW7sACvOlDdaN_B4YFD761TXwvI72kY1WgV6MDSYJvkJWW4A0QW6hu7qP4P8NQJEj1gjkrtj0DmYyUYCIj9Q6noayHTFVAh2J88-gixewr0KtnDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
«بِسِنت» درباره ایران:
⭕️
خطاب به سربازان عادی حامی این رژیم:
در شرایطی که پرداخت حقوق‌هایتان بیش از پیش متوقف شده یا به بهانه تأخیر به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشور را به سوی پیروزی می‌برند یا نابودی؛ و به یاد داشته باشید که دیوار برلین زمانی فرو ریخت که سربازان عادی تصمیم گرفتند به سوی مردم خود شلیک نکنند.
⭕️
و خطاب به کسانی که راه را برای تهران هموار کردند:
بهای آزمودن عزم و اراده واشنگتن را دست‌کم نگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70526" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70525">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91fbf3e30.mp4?token=Zobqe673AHLdBkI691QYRPNw1RlblKm1KDKpFlYuRvB9QGNc_WOoJDNyA6gxhf96AOjR2OKkv-xNcgrx4uNkTOpI3vtBFeTgMun7XV2fnZLMwa7YTLb_bY_BvMaGqOmlykyETrwOrK4SKvLs7EMqxHmo_q5bpob-dTjA90g5He_-WCHsKxiH-8DD4RE2LDUIyBMeoR-u-nwp6wWqbl0QAFomrcsAYGEgw0c66KQOpFhuCovvLea0rT6-YxOs--tAMIip_X6tP0y-c2vVc33YN50lt8nr027ZKtYRSYiUiP8dkRXJl45ioaEjSvig84uhemMmPEQ6RSb1qdWnOs5hQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91fbf3e30.mp4?token=Zobqe673AHLdBkI691QYRPNw1RlblKm1KDKpFlYuRvB9QGNc_WOoJDNyA6gxhf96AOjR2OKkv-xNcgrx4uNkTOpI3vtBFeTgMun7XV2fnZLMwa7YTLb_bY_BvMaGqOmlykyETrwOrK4SKvLs7EMqxHmo_q5bpob-dTjA90g5He_-WCHsKxiH-8DD4RE2LDUIyBMeoR-u-nwp6wWqbl0QAFomrcsAYGEgw0c66KQOpFhuCovvLea0rT6-YxOs--tAMIip_X6tP0y-c2vVc33YN50lt8nr027ZKtYRSYiUiP8dkRXJl45ioaEjSvig84uhemMmPEQ6RSb1qdWnOs5hQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اظهارات بسنت درباره ایران:
از امروز، حلقه محاصره را تنگ‌تر خواهیم کرد و تمامی منابع درآمدی احتمالی را که بودجه سپاه پاسداران و رژیم ایران را تأمین می‌کنند، مسدود خواهیم ساخت.
ما رویکردی را با هدف جلوگیری از هرگونه نشت (دور زدن تحریم‌ها) به اجرا می‌گذاریم.
ترامپ با رهبران جهان تماس می‌گیرد و مشخصاً از آن‌ها می‌خواهد که تعاملات خود را با رژیم ایران متوقف کنند.
هر نهادی که به نمایندگی از ایران پولشویی را تسهیل کند، از سیستم دلار آمریکا حذف خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70525" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70524">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75070defdc.mp4?token=Kci_MmMmxUbKNGPie34aw-Y1tmwrGJhu4PxrT4lLDK4RoEz-zX95iF0HNyfV0cxahfk2jKA-BJVx610VkWdqTIikTnpJo0i8HOG7mWgTyHpIGJAW3HpVOM4kzVCcShY4zTXjkgAF88WyKx4yTfA7c3pqGSdfMCRmTaUpfiesmeu3qmlf9EPLPIHInCtXJaoVOV4OccireDzbTr9QfGmQlQNgMP4jtYkOMfUOJChSzUdiISJEx9M9aqn16BCd0HZ-w-xTrjZWDzA8A84qAFPcbOaXjVEirNeC_WGRn8_iayQ6hk9818F6y0DUVSLFV23AIJ4jXy6VtA_dVXaQKvt5aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75070defdc.mp4?token=Kci_MmMmxUbKNGPie34aw-Y1tmwrGJhu4PxrT4lLDK4RoEz-zX95iF0HNyfV0cxahfk2jKA-BJVx610VkWdqTIikTnpJo0i8HOG7mWgTyHpIGJAW3HpVOM4kzVCcShY4zTXjkgAF88WyKx4yTfA7c3pqGSdfMCRmTaUpfiesmeu3qmlf9EPLPIHInCtXJaoVOV4OccireDzbTr9QfGmQlQNgMP4jtYkOMfUOJChSzUdiISJEx9M9aqn16BCd0HZ-w-xTrjZWDzA8A84qAFPcbOaXjVEirNeC_WGRn8_iayQ6hk9818F6y0DUVSLFV23AIJ4jXy6VtA_dVXaQKvt5aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
اسکات بِسِنت:
ما در حال آغاز یورش اقتصادی علیه پیوندهای مالی ایران در سراسر جهان هستیم.
هدف ما قطع تمامی شریان‌های حیاتی اقتصادی است که این رژیم ستمگر را سرپا نگه داشته‌اند؛ تا زمانی که تهران کاملاً تنها بماند.
🔴
در دوران ترامپ، آمریکا دیگر صرفاً تهدید ایران را مدیریت نمی‌کند.
ما در حال پایان دادن به آن هستیم.
ایران دو مسیر پیش رو دارد: انزوای کامل جهانی یا مسیری به سوی بازگشت به وضعیت عادی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70524" target="_blank">📅 20:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70523">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b43c7e4e6.mp4?token=WnVq8hD2cs8SR5eKhd-XMF3xtXeURlea8FerYyDkMh8iaV4uCRXF1UhMC6PMsqcxFX8kf4X3DfiD6Om3NQ6lSX8-gy3jTP7WfwXrbP1YV7zaPnQ0CVmjyEAHDYRI0ziyUVakp6OF1M7gXtEzn2jyLuQtMUUzLrN8uxYs8Y_3t31MuPp59WSE3kGCyO1Wew7eAYbpp-Pijj87gHaWHyY_9E7mSEDcDGkhzWMJQeNSiflDkuW408v6UTjFn3am6OA2x7mDrcU8cFmX8U8QOPOzQsI_jAx7R1bVnscfK5U9Kr11zx6UvvlBS3w9OWh6dJgUBY49_wSmqQcK0lQETNwW_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b43c7e4e6.mp4?token=WnVq8hD2cs8SR5eKhd-XMF3xtXeURlea8FerYyDkMh8iaV4uCRXF1UhMC6PMsqcxFX8kf4X3DfiD6Om3NQ6lSX8-gy3jTP7WfwXrbP1YV7zaPnQ0CVmjyEAHDYRI0ziyUVakp6OF1M7gXtEzn2jyLuQtMUUzLrN8uxYs8Y_3t31MuPp59WSE3kGCyO1Wew7eAYbpp-Pijj87gHaWHyY_9E7mSEDcDGkhzWMJQeNSiflDkuW408v6UTjFn3am6OA2x7mDrcU8cFmX8U8QOPOzQsI_jAx7R1bVnscfK5U9Kr11zx6UvvlBS3w9OWh6dJgUBY49_wSmqQcK0lQETNwW_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
اسکات بِسِنت وزیر خزانه‌داری آمریکا:
امروز، وزارت خزانه‌داری ایالات متحده «عملیات طرد اقتصادی» را آغاز کرد؛ کارزاری بی‌سابقه علیه جمهوری اسلامی ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70523" target="_blank">📅 20:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70522">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhgBs3Oh7QLI4D_yTmrA-kljnc0JJjQ8fgPaEkrpdzho2WV6aAR53Tv-aQSmuoHiJrUULbAQ_y_UF6jfuD2t7V6hSKP_VtbIa9g7hEcJ6K7GUSeaxuSarm5DGGqILqqj4Le19xZuLSrd4KUFKfylA_PjFGTXvQ3qmjFjddBMxH_3NZ_AnDyrjlFfLlhmmcfiE_qqrBWY9FbbKLs6zm_OpSqO_7keegINA9Zi1p2C16QOh--ueIMk3riqe1ZFLN0BcJe4F1GwRMzIfgzID75G9iyJNm1BVLgL3L8xysyO4D9ILYCePfUvga8CN8034DnLuiKFGOoIi7wuGrSm7oHvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو:
ایران تلاش کرد یکی از پسرانم را ترور کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70522" target="_blank">📅 20:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70521">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Smkz8Ob1lEcp0Frz_bKnLb2Ga5XwRZRGRXzAG_sGzEvdrp4l4YMYJ4kGkO7EAqvouP52R7wbnH0-pcNFd7LJVaRBXPK_C3wG49fIuwnbEs4IERB_koCLrPyZjZz-tvXibadeNw5SzaA1DkoGLH_fs0aQA-f6LUMgve5xOO0nEI4Jy-JtotHeCnGX7ouUYZSSsLYv_9QQogdzOjnE69Cgqq7tJpHusxR8RQmjnrWQHzU_x4RsxDQhVKZH5ey7A5Ce1dKXembcDiCcnUMZvXLsHfWoDc307umCpQmH07fr0CK01teDKo5uGnpSBBykYw9Ep47FFuRUpH_ZnNV9L9V-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دموکرات‌های چپ‌گرای افراطی با انتشار نظرسنجی‌های ساختگی، دیوانه‌وار عمل می‌کنند. آن‌ها این نظرسنجی‌ها را در سطحی بی‌سابقه منتشر می‌سازند. این اقدامات «عملیات تضعیف روحیه» نامیده می‌شوند؛ تلاشی برای دلسرد کردن جمهوری‌خواهان تا پای صندوق‌های رأی نروند.
اما واقعیت نظرسنجی‌ها عالی است و روحیه مردم کشورمان در بالاترین سطح خود قرار دارد.
⏺
ما در حال پیروزی بر همگان هستیم، از جمله ایران؛ کشوری که در گرداب مرگبار اقتصادی و نظامی گرفتار شده است.
از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70521" target="_blank">📅 19:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70520">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDB7zOKOF67tVDjQ27lSyedg19st9ZVK4WCySIoYeNHG9X2ARlUKCSgC6MPuI-y4mgZ8Lx-F0oCoQk45iXFda3tiVnWYNn6dQ5zYOqYwJf-wBhqVLwwtXTaouxJYuNogpkALciohE1z32HjEjwtOSC7ZqoQCQXC2BuRFf_SsA7mDMeANx4o3_EtSCzeu64pxkAs-bgsg2QZiCWJoWkPc2OjqbUBxVsnibX_AbDfO4C35_d5dbgroAfVTZiyNY4uksZMoiXSUCHve15jEIBUpniWS0MOncNVMk-pGyj4W_MZpHF3pcV9hieZHAPb_aIcoELFludBvEGtWG1gEesMyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
قالیباف در دیدار با عاصم منیر:
تعهدات طرفین در یادداشت تفاهم روشن است و این آمریکا بود که با بدعهدی مانع برقراری ثبات در منطقه شد و دلیل دیگری برای بی اعتمادی به این کشور ایجاد کرد
رئیس هیات مذاکره کننده ایرانی، ضمن رد تاثیر پذیری جمهوری اسلامی از فشارها، تاکید کرد: ما پیگیر اجرای شروط یادداشت تفاهم هستیم و این امریکاست که باید به تعهدات اش بر اساس تفاهم نامه پایبند باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70520" target="_blank">📅 19:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70519">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235f69fa4b.mp4?token=bd8q4SWnI_OJLo_yS2Dpv95Cvf6YHif-3fV_OU8zxLD6A6MARNfEmCgxUaH9Vte3p2BeN8JERJITggAijOxtf97Okbq_NLpGdX7E-4Bt-BKqK6kX9p77J5Q0pmphWny8Ku0p7OlDYND0BOvEG5HVwSY6Dj2V46DHC5cK_xOfn78yNzYxO9vvCspNS7UYZbXS5KY4HV-tG1V6Phwlk_EcGp4y_d58GPy0_medRh53HeEqTRAcSxC6wmDK2TdtiMKtbqK2yvBYOUWSTPCjy99NKQJS1fTELM6XlI1HzUecDcXr-djW1zzVRXJO7xo68Vgzg2Xk6wFq2g5gbnxRvCN8mjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235f69fa4b.mp4?token=bd8q4SWnI_OJLo_yS2Dpv95Cvf6YHif-3fV_OU8zxLD6A6MARNfEmCgxUaH9Vte3p2BeN8JERJITggAijOxtf97Okbq_NLpGdX7E-4Bt-BKqK6kX9p77J5Q0pmphWny8Ku0p7OlDYND0BOvEG5HVwSY6Dj2V46DHC5cK_xOfn78yNzYxO9vvCspNS7UYZbXS5KY4HV-tG1V6Phwlk_EcGp4y_d58GPy0_medRh53HeEqTRAcSxC6wmDK2TdtiMKtbqK2yvBYOUWSTPCjy99NKQJS1fTELM6XlI1HzUecDcXr-djW1zzVRXJO7xo68Vgzg2Xk6wFq2g5gbnxRvCN8mjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🟥
فاکس‌نیوز:
در حالی که ارزش پول ملی ایران به پایین‌ترین حد تاریخی خود رسیده و تورم همچنان رو به افزایش است، کاخ سفید آماده می‌شود تا آنچه اسکات بسنت، وزیر خزانه‌داری، «سخت‌ترین تحریم‌های تاریخ علیه ایران» می‌نامد را رونمایی کند.
ایران تهدید کرده است که علیه کشورهای حامی تحریم‌های آمریکا دست به اقدام تلافی‌جویانه خواهد زد؛ این در حالی است که فرمانده ارتش پاکستان برای تلاش در جهت احیای گفتگوها و میانجی‌گری برای دستیابی به توافق صلح، عازم تهران است.
همچنین انتظار می‌رود وزیر امور خارجه عمان برای انجام گفتگوهایی با هدف کاهش تنش‌ها پیرامون تنگه هرمز، به ایران سفر کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70519" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70518">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بزرگترین کانال پیشبینی فوتبال در ایران
🔥
g2
فرم های ما رو از دست ندید...
⚽
@Tabanii_Mafia
@Tabanii_Mafia
⚽
@Tabanii_Mafia
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70518" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70517">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4mPGXTG32kP82k132HA0QmeRACtDAzwueNSkGGzQqYzgSySTjf8eTF-KiNBr6OiX5lbveeyz9xC6R7_748UCNb6SuWeVEm026Mo0apywMNts5XShVQcSZ6uprWh-qlJNSwlAkTgbocztjmZWbA9Vye9Hyw2SarU5bhBR5Eb3pog81QtlA4Yl_aqEj6f_W67YyMnz7oArVBMivsyZCd4YS8Q5XZb8m1HFIWGYLPOkDVKiHGC3TH1qo1I3y3R44r_1DTmGQqcJXXjilL-aeMzUPzAMTYYNxJh6EjMq5VlWPddrzBJynccCzBKULMfdoofME01gGaIwEL6vTb9sF54Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
❤️
✅
✈️
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70517" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70516">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384afb6ff9.mp4?token=NO5toEvZblxHmQ977itH6Zwk1xrBTPd-jS_I0Aljzw8mGRfMFFNAXJLQWKO3J6sjNhkdGe3kXhnNk3n5fJNpdMYvo-GeKSDNfhh5C9_efSqxUCUrqs38CERQD0Dqlxjs4VQMlKlLiEYgKziRJmAoUA5h2txiUWo8Bq9IYMgVE6UU1oNxnFiPULJBp1Jnb2E4mAw70ly4jR74XPkXzqS5DvqjIPPkbm_sdtFXCBqL7wJfMSjS-_CgUOHxKpfO7iGMPBLu4fLX1KtwgnzutyYokKeOl5xLN11_9vMvtHjwtL4NVfp5w5nUMLnbzS4GCkWiW8ikAcj48a3XyTK0WHbgrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384afb6ff9.mp4?token=NO5toEvZblxHmQ977itH6Zwk1xrBTPd-jS_I0Aljzw8mGRfMFFNAXJLQWKO3J6sjNhkdGe3kXhnNk3n5fJNpdMYvo-GeKSDNfhh5C9_efSqxUCUrqs38CERQD0Dqlxjs4VQMlKlLiEYgKziRJmAoUA5h2txiUWo8Bq9IYMgVE6UU1oNxnFiPULJBp1Jnb2E4mAw70ly4jR74XPkXzqS5DvqjIPPkbm_sdtFXCBqL7wJfMSjS-_CgUOHxKpfO7iGMPBLu4fLX1KtwgnzutyYokKeOl5xLN11_9vMvtHjwtL4NVfp5w5nUMLnbzS4GCkWiW8ikAcj48a3XyTK0WHbgrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن حاجی‌میرزایی، رییس دفتر مسعود پزشکیان رییس دولت جمهوری اسلامی، از قطعی بودن کاهش سهمیه‌های بنزین خبر داد و گفت: «افرادی که بیش از سهمیه تعیین‌شده بنزین بخواهند، باید آن را با قیمت بالاتری خریداری کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70516" target="_blank">📅 18:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70515">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a8609222.mp4?token=OXlV0xC_0iBWixc_hhNjkkl49susOQ_7A7ys-s6f7WoiYVJTW2IrfHbQQPEzqMs-yzANS1wGLJh__xOCcsC1zzXCS6JqNaCD2lHiWEtzefo1QE3A0-aMEF0k0jvt1aa2XMC6oInX5yi1SFCU-uIJDK5mABvccNKX8q-hgplYx58y8o0ekNmHgHKlxwF4fG4FrjHPJLz7hUOqFeDvpkIz1GQXdd23EpSaOXbb8yBWHIVzfW9c2svNye14uyN56twLZSepb3bnWwr-BaWu2bdhqW-a77xnZWPLgjF2jw9cVp8NWy7nyWlEu54I4rOQcPIAzy0hvvJ-p5SgU1SxFF-Ztg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a8609222.mp4?token=OXlV0xC_0iBWixc_hhNjkkl49susOQ_7A7ys-s6f7WoiYVJTW2IrfHbQQPEzqMs-yzANS1wGLJh__xOCcsC1zzXCS6JqNaCD2lHiWEtzefo1QE3A0-aMEF0k0jvt1aa2XMC6oInX5yi1SFCU-uIJDK5mABvccNKX8q-hgplYx58y8o0ekNmHgHKlxwF4fG4FrjHPJLz7hUOqFeDvpkIz1GQXdd23EpSaOXbb8yBWHIVzfW9c2svNye14uyN56twLZSepb3bnWwr-BaWu2bdhqW-a77xnZWPLgjF2jw9cVp8NWy7nyWlEu54I4rOQcPIAzy0hvvJ-p5SgU1SxFF-Ztg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو ماهیگیر جنوبی موتور قایق‌شون خراب شده بود و چندین روز بود که وسط دریا گیر کرده بودن و دیگه جونای آخرشون بود
که ماهیگیرای عمانی دیروز دیدنشون و جونشون رو نجات دادن
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70515" target="_blank">📅 18:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70514">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16a65d9f01.mp4?token=nbKwZii_H7bi9xg_gD1vyLiOHfhZYXXGtmUeQ8OfKwdfRnNkQawiBqLReU5T9srWSgieCLL4t425ARClzPYgZxyXUzxDqvoSOJ4ZeKPdoFqv3JWvMddmqmCtDDPMPooOgMz7inHUnKQWjmd6VCR8483at3sSV0ckQryX94-eS42rr_Lka45Ug7RDlJeUlO0zJFm8DQ0IaB5QYQq0IJLtQi_Aa4hh_FQdN-2vZZ8FIOVMiCLiLuTfIQvpvbzmin6xfAYoT6s0_xmAVOGBT45NhG7gUuKru8ONOyI4BMgvZjsyVm2ix0AlhJixGm53pC9Lg9s1pKGmFmy8HXNhlH_lUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16a65d9f01.mp4?token=nbKwZii_H7bi9xg_gD1vyLiOHfhZYXXGtmUeQ8OfKwdfRnNkQawiBqLReU5T9srWSgieCLL4t425ARClzPYgZxyXUzxDqvoSOJ4ZeKPdoFqv3JWvMddmqmCtDDPMPooOgMz7inHUnKQWjmd6VCR8483at3sSV0ckQryX94-eS42rr_Lka45Ug7RDlJeUlO0zJFm8DQ0IaB5QYQq0IJLtQi_Aa4hh_FQdN-2vZZ8FIOVMiCLiLuTfIQvpvbzmin6xfAYoT6s0_xmAVOGBT45NhG7gUuKru8ONOyI4BMgvZjsyVm2ix0AlhJixGm53pC9Lg9s1pKGmFmy8HXNhlH_lUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به تازگی توی بالاشهر تهران، یه رستوران ساختن مخصوص شوگر مامیا.
خانمای میانسال جا افتاده و پولدار اینجا جمع میشن و پسرای جوون و خوشتیپ هم میرن اینجا، تا برا خودشون شوگرمامی پیدا کنن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70514" target="_blank">📅 17:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70513">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CXlcm839mE_7oXPWD_ZAFXhhenAQmJm8aY30PseWB-Rx4Ec_tcVqwwL6b8mCfzpRm2ddPBmXlgHLb8bM8iQQHqvwfkeDeNdjsFCynDu46BtcCl2xjWLBZqV6jdAyEqJafhYRur-MYOCgdczn3X5BDfOGZ3kRVifSi3EWCW7K0lhJYTgUIJ9J4Tq5VCQHRDyKaK8BWDO2X8oKunygkp1TX3O88zx8bFLeIH13EiDNEDag5tTSSN334gGqiaAasusUtwj8M2HZBCVHMwF4WmZ9ofgDmIXnOAttf2NoUoTAEr2qLV_DCsn0IGM4gMEG70M66PNWRiOoX20677DzsLZp7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قطع برق کمیسیون انرژی مجلس،هنگام بررسی علل خاموشی‌های اخیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70513" target="_blank">📅 17:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70512">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX_0qksqb4AzSTs2wUQpWwRu6MSukXVe-eNmPMEW4oadOJh-UxkEpi8sjozQgynv5Wq_H1kVR2eUG2-Raxh2UC1yxsQ5DZPbdDj90Xk-UvHpTCG1JY6KHom30sNk_bVQang7iMlZEvKmcOvZLjpwi28npTJwe8mdn_KA2SufqqRJKGCvk0LkSkIOZViSbttc6P8xD7TgHkrrze-6jOCYw_BTzfqoYd_wKWUzIZ8sLd0qLQz1UNRPzIicdck3OYPTIyD9YFC6aHbJGiCUGN5toanX44IRRsZSfXgnz3hou-evnH3r6YaKBqmzJ1Y5DDDnWVQfXeSKd4SsvE_2WuhDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ
:
ایران به طور کامل در حال فروپاشی است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70512" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70511">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98f13e516e.mp4?token=ax4NTl50WKrayxH1WGmWaDruLSYzBAYoqtPqFOvHrScvEffzevabf1ddAUcGm_i82fK3qjdIdmI4vSIxpf4lXVLVTekVYKUM52oleCQi1PwDu52p8F85-Bf8FcjtlUJ1BnCAPDixgPg1l8VNVJrBvciX8UdnsJZyfNpvndnBbc4it-niR7K8KPPQdsesp8oRVfd6WzhB-EO1hTNxIs-0zhNs9mrNcGsjUkrzpXX19zZ7IjKEunsANnaeni7yotL_U558BBd90LA8HHRQkprBIqi8QmlPeF9-g3CaeMVVd8pXJsKzHfuxI8DTsDXbcrZobatZ2_Afr82D_ptiIRH6LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98f13e516e.mp4?token=ax4NTl50WKrayxH1WGmWaDruLSYzBAYoqtPqFOvHrScvEffzevabf1ddAUcGm_i82fK3qjdIdmI4vSIxpf4lXVLVTekVYKUM52oleCQi1PwDu52p8F85-Bf8FcjtlUJ1BnCAPDixgPg1l8VNVJrBvciX8UdnsJZyfNpvndnBbc4it-niR7K8KPPQdsesp8oRVfd6WzhB-EO1hTNxIs-0zhNs9mrNcGsjUkrzpXX19zZ7IjKEunsANnaeni7yotL_U558BBd90LA8HHRQkprBIqi8QmlPeF9-g3CaeMVVd8pXJsKzHfuxI8DTsDXbcrZobatZ2_Afr82D_ptiIRH6LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه واحد 131 متری تو ولنجکِ تهران :
131 میلیارد تومن
🇫🇷
یه خونه ویلایی استخردار 1080 متری تو فرانسه :
130 میلیارد تومن
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70511" target="_blank">📅 16:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70510">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/685fbb8085.mp4?token=nCkQTKI7N-ZGURZDnw3QbrtsWlpCl0SKz27xNU-CbDme9ibOcNQ4Wb6bXKgTs4eFb2apM6exichy19C2fVZ5FmE3PyBFIczhRLEdgjvOG0LsLTb2N6qh2Z_J432tWBC9DhTyT5YxHY-exfQES9q1i1ysatcjYgkyk5d1E-KD0-iOufCYHR_eWBQcpod3BY1ZbyaxLWEVxLv-PH1XnDts4DU8wtSphTNnFu4dbzhFpkhP1t1rZY3VwPgqQfumBxrCWUePZJIDaggrakApXX4lih2Q3SHWP4eLYLzfNLvkXMCNCqnZ4UKySSUISUQNNZ25Pf7vMYkrcdxuM6mTRimg2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/685fbb8085.mp4?token=nCkQTKI7N-ZGURZDnw3QbrtsWlpCl0SKz27xNU-CbDme9ibOcNQ4Wb6bXKgTs4eFb2apM6exichy19C2fVZ5FmE3PyBFIczhRLEdgjvOG0LsLTb2N6qh2Z_J432tWBC9DhTyT5YxHY-exfQES9q1i1ysatcjYgkyk5d1E-KD0-iOufCYHR_eWBQcpod3BY1ZbyaxLWEVxLv-PH1XnDts4DU8wtSphTNnFu4dbzhFpkhP1t1rZY3VwPgqQfumBxrCWUePZJIDaggrakApXX4lih2Q3SHWP4eLYLzfNLvkXMCNCqnZ4UKySSUISUQNNZ25Pf7vMYkrcdxuM6mTRimg2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
ما از قدیم شطرنج باز بوده‌ایم، در سال‌های اخیر پوکر باز هم شده‌ایم.
الان هم مدتی‌ است که ترکیبی بازی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70510" target="_blank">📅 15:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70509">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9pYzEMjfiDC1c0kVnQWESvI8WoGHRXrTZB_-KMeRVlcwKMRY1atyitIO--Yy99MG7XHAM0Tv0U91y9g3YYiZ2PNfQeIpqeznal1zQYBHPxrE0rnMMgmYjjSYX-tFYDbPkt0h8zA15HGF4q_9WphxuKqTI8KUfcMYE1kJavD5_V5gViZrFOo-F3ImwKioHWyO-aW66LdSo5WbVoJDsaCuYN5Qsa663jblHR9ODAVJAgD7gpz7bRDZtMmI_fj9QKZN8FYGTi_Q_VAUJ5d4UphOtwWzdZnfLpi7-7g9OcDtnjhqTBYUvIzR4v63TYJvgwPUfKJEiuWKh9x_Z9Oh68Fsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
🇮🇷
ترامپ در تروث؛از قول رئیس مجلس ایران: «گرسنه‌ایم، نمی‌توانیم دوام بیاوریم»  @News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70509" target="_blank">📅 14:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70507">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8XWnj-MeMsHRwmJbagCVl2FiU_6Z6Hnhh2_mmfJ2-83hY2KL0sLulf2SxWh5HLh0Q9ehWh-Ix3VK94ArSy33um8odxSoAUEYyr-2h2et4z_RGSRFr-d6_ElhEeXHAk0-ZaZZqVnx7aJctYNTfjXVD-XVsz6W3j3Nhl7N971hOmIRWMmcagzeLzAkE6gzG-y4GXoqObVk0EiqjBJ4L4GN9DpDfg6yL8m76ZEv8dapV-CXhnFetfBNjMpO27gmynIeultSwEbrhpDudkqT6H6Z1yr8CNJg-pMeug8afeGiN5DpHjm45YrRx6zZMdrCJ8xqg7BD1UUy6Q-uHCQxKPm9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7684c0f69a.mp4?token=lsT9wOHu2T_wEPX76gMKoblAgzgA_apZWl12natfVYslH2P2YXfnWwRkngTyIFyOXu3tFulvizH5C0Ok87-7EmJoKvbc0fnINCHgBNE9zd73fjOSphTU2L8FWmObf7_5JdfpYOMUkc0FNWdeipbso0gflKU9EgnvK4Br6pu3X3gY8II6cbHEDlHQAv8fMi3s4xvKkHCtpH5wyOFGHRn5WadxrQr2i3VjyhN7swlpFVgpj57663j6OeCYgq0Nrs91TZPjSnqv9eWOcBrPkb5U_BWglh8xE7AjXe_I80MPqeSAYV5bbYJ3RkrO6bSoJi8Us7pFxDxb-M90RPo6Sct8Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7684c0f69a.mp4?token=lsT9wOHu2T_wEPX76gMKoblAgzgA_apZWl12natfVYslH2P2YXfnWwRkngTyIFyOXu3tFulvizH5C0Ok87-7EmJoKvbc0fnINCHgBNE9zd73fjOSphTU2L8FWmObf7_5JdfpYOMUkc0FNWdeipbso0gflKU9EgnvK4Br6pu3X3gY8II6cbHEDlHQAv8fMi3s4xvKkHCtpH5wyOFGHRn5WadxrQr2i3VjyhN7swlpFVgpj57663j6OeCYgq0Nrs91TZPjSnqv9eWOcBrPkb5U_BWglh8xE7AjXe_I80MPqeSAYV5bbYJ3RkrO6bSoJi8Us7pFxDxb-M90RPo6Sct8Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💲
❤️
ثابت نگه داشتن قیمت دلار درطول ۲۶ سال حکمرانی شاهنشاه فقید ایران
💵
قیمت‌دلار
زمانیکه تحویل گرفتند: ۷۰ ریال
امروز بیش از ۲/۰۰۰/۰۰۰ ریال
یعنی ۲۸/۵۷۱ برابر!)
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70507" target="_blank">📅 14:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70506">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3317e927b3.mp4?token=Lqkf_Hym7BYuu3nEQ_-1g32veM4ie3zx98dc2Z-AK394vtYORyoUco-V3olmwMa4_KeQXF22UbR4SCY2LQZtefYZGgc_x7zp0UbQtElPcZCskBeeVhA11r8-bqtOEYU-CbKOJSTNqFoGuZGvKb4aaCnvtNA29MJ4CSCw_bR-wvxsHYUV35dOUoLNIK4Ibe4mPv6HYr0xjpGVQjugu9PctNdkLg168_Fid36WTtGN7cXnWiEbAMpDY7xuZh0EdcYoweOy2P8RgeKjYFpZIS-Cp_8uQfTGku6fBajLlW22_kmkAWwvaPlKBJABJky4mnYwlze0SN31UKWkSwMeBfYWCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3317e927b3.mp4?token=Lqkf_Hym7BYuu3nEQ_-1g32veM4ie3zx98dc2Z-AK394vtYORyoUco-V3olmwMa4_KeQXF22UbR4SCY2LQZtefYZGgc_x7zp0UbQtElPcZCskBeeVhA11r8-bqtOEYU-CbKOJSTNqFoGuZGvKb4aaCnvtNA29MJ4CSCw_bR-wvxsHYUV35dOUoLNIK4Ibe4mPv6HYr0xjpGVQjugu9PctNdkLg168_Fid36WTtGN7cXnWiEbAMpDY7xuZh0EdcYoweOy2P8RgeKjYFpZIS-Cp_8uQfTGku6fBajLlW22_kmkAWwvaPlKBJABJky4mnYwlze0SN31UKWkSwMeBfYWCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدحسین عادلی، رئیس اسبق بانک مرکزی و دیپلمات سابق:
بر فرض که در آمریکا، صف بنزین تشکیل شود، چی گیر شما می‌آید؟
اگر فکر می‌کنید در آمریکا صف بنزین تشکیل می‌شود، باید بگویم که نمی‌شود
چه خواسته‌ای داریم غیر از موارد موجود در یادداشت تفاهم؟ کاخ سفید را حسینیه کنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70506" target="_blank">📅 13:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70505">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4e1f5587.mp4?token=gOF0_N0H0gPtYbfVmeNoBdoPimsRkHgqwjHwK_rDJ2J6U2TQKlT4o03zKOFHWAUMC2zGBytEck3ZSpjvcNMKZ6Y9Q1rbHJ4j42ChA1qziBVTgUrAFiZl3KoYfkNwmaTMcBj6DbDGuSbAXX8tvj4_jql1SSBsFfwOLZ6tCRdxuuuicPwdcqXfJuY_RTnHAIm2P38W3b-owUNBkR7H5iCDJCVUIx1LZwvijrO1sx_Yr1SvDa0xtV7-S8nl0bYBP5mbhrSlYLZu1bBlf5JOvs5PCgs75TuT0sjjLODfNBSuVFrxDSFes-7pQT5MBu4KjqiXeqhea_gO8oqC8nvQBe-HNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4e1f5587.mp4?token=gOF0_N0H0gPtYbfVmeNoBdoPimsRkHgqwjHwK_rDJ2J6U2TQKlT4o03zKOFHWAUMC2zGBytEck3ZSpjvcNMKZ6Y9Q1rbHJ4j42ChA1qziBVTgUrAFiZl3KoYfkNwmaTMcBj6DbDGuSbAXX8tvj4_jql1SSBsFfwOLZ6tCRdxuuuicPwdcqXfJuY_RTnHAIm2P38W3b-owUNBkR7H5iCDJCVUIx1LZwvijrO1sx_Yr1SvDa0xtV7-S8nl0bYBP5mbhrSlYLZu1bBlf5JOvs5PCgs75TuT0sjjLODfNBSuVFrxDSFes-7pQT5MBu4KjqiXeqhea_gO8oqC8nvQBe-HNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدئو از کنترل خارق‌العاده با سر و گیتار زدن تو ارتفاع دو جوان ایرانی، حسابی تو فضای مجازیِ وطنی و خارجی وایرال‌ شده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70505" target="_blank">📅 13:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70504">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⏺
🇮🇷
🇵🇰
تسنیم:
عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشور وارد تهران شد.
عاصم منیر پیش از سفر به تهران با ترامپ رئیس جمهور آمریکا گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70504" target="_blank">📅 12:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70503">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d7db3b25.mp4?token=tou3NRko7yjDPPQz29GbTto9IFr0h8zIMpkCCQpw6rAPSK-vi4S04mBZSylAxs6yBZV8ln2S8km6SSS3rqWBI0IFy0YS9LaNzR8qddcA5hNJS1qj0kWeeTbyIPm1SiPqBAe7sILc6_NSBA2h28Qtpd8n67q5F89JZJCg7m7Rsvz58IC3EkR3lMBf3eLKCvQ32ig9WJV1mfBs64k1xUKsgg_QydAX6O-HzQJF5bDGPTY74q8QAw697XmAwZf_PwJmmmPS8JeqKVHHFs1IAvamnMlC9l03nECDztewr-en5JQLXMCRSqo96iPAZF9gjbZYFjNrhjiUZori3t-61YN6LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d7db3b25.mp4?token=tou3NRko7yjDPPQz29GbTto9IFr0h8zIMpkCCQpw6rAPSK-vi4S04mBZSylAxs6yBZV8ln2S8km6SSS3rqWBI0IFy0YS9LaNzR8qddcA5hNJS1qj0kWeeTbyIPm1SiPqBAe7sILc6_NSBA2h28Qtpd8n67q5F89JZJCg7m7Rsvz58IC3EkR3lMBf3eLKCvQ32ig9WJV1mfBs64k1xUKsgg_QydAX6O-HzQJF5bDGPTY74q8QAw697XmAwZf_PwJmmmPS8JeqKVHHFs1IAvamnMlC9l03nECDztewr-en5JQLXMCRSqo96iPAZF9gjbZYFjNrhjiUZori3t-61YN6LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی نزدیک از ظاهر موشک تاد و پاتریوت؛
موشک THAAD: طول ۶.۲ متر | قطر ۴۰ سانتی‌متر | وزن ۶۶۲ کیلوگرم | سرعت بیش از ۸.۲۴ ماخ | ارتفاع درگیری: ۱۵۰ کیلومتر| ارتفاع درگیری داخل و خارج جو | پیشران سوخت جامد | روش انهدام Hit-to-Kill | هدف: موشک‌های بالستیک.
موشک Patriot PAC-3 MSE: طول حدود ۵.۲ متر | قطر حدود ۲۵ سانتی‌متر | وزن حدود ۳۱۲ کیلوگرم | سرعت: ۵ ماخ | ارتفاع درگیری ۴۰ کیلومتر | پیشران سوخت جامد دوپالسه | روش انهدام Hit-to-Kill | هدف: موشک‌های بالستیک، کروز و هواگردها.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70503" target="_blank">📅 11:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70502">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7ee8a017.mp4?token=QQQhkQYGwoSCCX60HzwgxfuXuTvh3_UQnYE8GqJwqCWEkGSLZM_ZStL_9AChPd8vVQFszzXItRTuJaf2UUUMIkUvSBddNpi2nEgGHQSRhNoI2-g0oki_pMza656w1R59PLa-rXVY3CCdyAR70gW-zm8brg_l_yFHBtJamVaorIbjEt28H61dq6HEUzFbrjlTjJvzhocu5OkIXL_Xrrhe6Nr5LN46m0Jf2FxFhiZ74U4wwQgE_KoqqeWBIw2_55l7BSkhPRkXQnhO8fC8k-Q4OO3DUMmKLirGanDjvvlXfKKWIlJVD6FjLgo6stv3gq_GbNuw5Q0JExnpj7CyPuJWZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7ee8a017.mp4?token=QQQhkQYGwoSCCX60HzwgxfuXuTvh3_UQnYE8GqJwqCWEkGSLZM_ZStL_9AChPd8vVQFszzXItRTuJaf2UUUMIkUvSBddNpi2nEgGHQSRhNoI2-g0oki_pMza656w1R59PLa-rXVY3CCdyAR70gW-zm8brg_l_yFHBtJamVaorIbjEt28H61dq6HEUzFbrjlTjJvzhocu5OkIXL_Xrrhe6Nr5LN46m0Jf2FxFhiZ74U4wwQgE_KoqqeWBIw2_55l7BSkhPRkXQnhO8fC8k-Q4OO3DUMmKLirGanDjvvlXfKKWIlJVD6FjLgo6stv3gq_GbNuw5Q0JExnpj7CyPuJWZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محیایی، معاون هماهنگی امور عمرانی استانداری گلستان:
تو استان‌های خراسان شمالی، مازندران و گلستان توی فصل سرما، قطعا بین 60 تا 90 روز قطعی گاز داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70502" target="_blank">📅 11:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70501">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70501" class="tg-doc-link" target="_blank">دانلود</a>
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
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70501" target="_blank">📅 11:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70500">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQIMbOE6J04txcMxfCrHpdZ4Q48W9OpivyiR-Ecc2W3te_KAKTpcmDXHxu7um2TktSxerc0a1CvDbtvAgWrgCZ3m4daBzrFQ6PQCyjpK7Lky7GElOlwv5SpbcTngaQQ7-s03wsXTk5YEZsuF1dbKdvTI2Jo6gm-lDKWBRVeDWYmpUuZlCoZ5jvLDkHMrfAFo_ozleloMM0UrQfnK5i0Tlg6n6l0lADzRNaxQI4Oa7dGDLyakCGdUB9xdSOsbg21c3JtmjSp5R3qK_kTl_Gu6n8cqz1hGqyCrNLGDJk3KGsFjue78q62y3pIBFxKu0LZYAxZIB_ole72agv76Po-xxA.jpg" alt="photo" loading="lazy"/></div>
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
r2
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70500" target="_blank">📅 11:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70499">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKUyVrrFx9vCMwc0_3uSy7jc4DCEiJJi5nLrS0FtQDc_JZs0cuFDLNxwLeH1YVpPlF-3fZn1Wbc86C6W6qA14mZZLczbygy-0T8fVCVwzlgyzLFjoq5Nuyv5ukuhgGhfDuGRRFFWmg0Xu4FhSXWuJ0e2MT3rOmGMAYVVmv5B7WEv7T_vMQFGQcSSnoUaoi_8WafZwAIikoFMXR8uNvID2gCeTkh3hGbw3fX8lFuDYblzwvJReN1---Be8d-qsin_1OxE0_ydUeEWzZAixE8TV36z2lOCBiNRXxKqji9oxGpJ9bznL8MK7rKgsxY_OF8F-Bsu4nIckVxLJeMQz6OWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
🇮🇷
ترامپ در تروث؛از قول رئیس مجلس ایران: «گرسنه‌ایم، نمی‌توانیم دوام بیاوریم»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70499" target="_blank">📅 11:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70496">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcrjvxJyQNm6EJeacmq7fYSPPyihaTgUXVzdJv89262e5BWlyuU9bwWDz3U1RV2a2E0KO-q4xqk2DKgWMNSYiWJsjD2CueVshBXC-X2G3ZTb6qpIDOgvSbJq3zwMDJBcIVOLRqSA64bkz5pTDxKG0Tovn8FhN5W_w19Rux8QWPT5fBQObA66NsN5PuKhoZOCLV6bSG3HsXREtCvvzBzcItLt9j_UkGB3T3L1XpS0h61NK24c1_isD2fZn96VWFaNKoRZmySd5yiFFNB3qBU-TQyxCx8rZ-Uj6JwXB7vU-Wk6sghQo7QbKst8xuPk6egNGJkAX7dDSQoz2iAm5Nj8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tn8HUE-93QGGHC5UzFQmfDAsClBoCi2-jSgovgOuK_kA3kj4N2yxV7AI2jAZDOqy7sBYRtAOZMRSPQBVZnupIf_FOiLPzL3TDwBH1ZDbD-BpGntcZP1j0zZtqfefIFhYB-MGdUNHMJ_YtFRs68swwJ21jEAQ4AsVrY89P6hidtavCttpbXLnSf8cJz5qId1IaFnJROIcaxrLqpF5BPF-Ify4Pf1yCrWSlssgob5iXYucq8TyTUl18rlCMdQnd5G8A3vklZjnBUe-KSJYkOAFmu3P0R96RTMLsvf2VLJlbI5pcR3-ZCRKpV-R_1jHdFewwvRFPp7uKYqUcvrb5HiHCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73af71539f.mp4?token=FeruHEBI_r2uDL3Ad8H8Oa_2IxzXatsm7eteNLIrymcPb7vpcJN7VMrQOWrsz1or0yf7T5T3woCYn482Q1OMboggeMA99PL296es8wMLl5Bg0jD3-OqBxHjh9d_cZMAxBUkhJOW1V2cZsIHJ4hcvSBmkAf9fEcON-gAy-aAzDn-f7UNSx0iDRjwXCkOrCAE6R7wOM4cDRSsjvcsvFtyTptOh9h9beYo766PPMvA3Y6kn52fwm_KdB6BSGhEC8LmzKGJ5xYsjFXbj1XEWEt0pryr_m55VvBgunOwIvcamheFKn-Ta8F5jn29QXR8qhBtmsPU8_J3NsvufYrIP3EVk6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73af71539f.mp4?token=FeruHEBI_r2uDL3Ad8H8Oa_2IxzXatsm7eteNLIrymcPb7vpcJN7VMrQOWrsz1or0yf7T5T3woCYn482Q1OMboggeMA99PL296es8wMLl5Bg0jD3-OqBxHjh9d_cZMAxBUkhJOW1V2cZsIHJ4hcvSBmkAf9fEcON-gAy-aAzDn-f7UNSx0iDRjwXCkOrCAE6R7wOM4cDRSsjvcsvFtyTptOh9h9beYo766PPMvA3Y6kn52fwm_KdB6BSGhEC8LmzKGJ5xYsjFXbj1XEWEt0pryr_m55VvBgunOwIvcamheFKn-Ta8F5jn29QXR8qhBtmsPU8_J3NsvufYrIP3EVk6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوالات کنکور زبان امسال رو بردن گذاشتن جلوی یه آمریکاییِ باسواد؛
طرف پشماش ریخته که اگه اینا به زبون ماست، چرا من نشنیدمشون تاحالا؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70496" target="_blank">📅 11:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70495">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⏺
📰
ایران اینترنشنال:
قیمت دلار در حالی از ۲۰۰ هزار تومان گذشت که پزشکیان گفت کشور در وضعیت جنگی تمام‌عیار قرار گرفته. همزمان، محسن رضایی به نمایندگی از مجتبی خامنه‌ای کشورهای منطقه را تهدید کرد در صورت همراهی با آمریکا در جنگ اقتصادی علیه تهران، هدف حمله قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70495" target="_blank">📅 10:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70494">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c05438d58.mp4?token=in5XhUUP6JskeORzsr_q05X1jZuX3yQ_zwjN1wqj4XpAoW_4vIig-la0Zb2oz3feGpeCtdY2SU_opFmClK0UoajQwVj62WqSxxoysD77nXw2GqUyGSvsm5g0ad9e7BLr1xnRQ1VWZ7xm9ss9WyeJBdLubB2VG4kFvJyBUqo4tn0aCjoRD3vmHnp7ImkisZXAuEZfAJljHl14oozaaMjlqPfAieq6_nwMbxPol-i-Z2KAFLhN3y_RqQ_nhemWLW_TKw-06kH-Eucbrcde8NL6dEVhM_N1xLq2BrGoe7VUrX-fXs8oQU7fl0_EQGBn1A5QQ9ZKjAOgFyJfKqK11wygKwxFkkxSmrnlGZXXMJG3DzdNuV31bV--mqXoQeNt5ledYqtcV6_uYfZpjE5EBIXRw93_CYTYw_zwt_czyXY2h1b4nSKz8aSatjR844dlb3YkU97OSjFkR8ubCzuHk_NBSKAVT5Ev4Em2A6z1SR-xc3BmMw6z00zoRPpNEuYsQNHdrUTSMaAd7wx3mb0zoED-3ephGpcmLwsYnZowqPls9bs_rUoHBPiFifk9nsLEsJn_NcAlCj8SQ0Bqv-BZ011JhTBdVNuaVXWHF2wbfRodxPKJF4VTcsndcJ6Jj4n15u66q08BsbbTP3vMWRFXZb2A9BcD0mz4ejUxsk6ciHEor28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c05438d58.mp4?token=in5XhUUP6JskeORzsr_q05X1jZuX3yQ_zwjN1wqj4XpAoW_4vIig-la0Zb2oz3feGpeCtdY2SU_opFmClK0UoajQwVj62WqSxxoysD77nXw2GqUyGSvsm5g0ad9e7BLr1xnRQ1VWZ7xm9ss9WyeJBdLubB2VG4kFvJyBUqo4tn0aCjoRD3vmHnp7ImkisZXAuEZfAJljHl14oozaaMjlqPfAieq6_nwMbxPol-i-Z2KAFLhN3y_RqQ_nhemWLW_TKw-06kH-Eucbrcde8NL6dEVhM_N1xLq2BrGoe7VUrX-fXs8oQU7fl0_EQGBn1A5QQ9ZKjAOgFyJfKqK11wygKwxFkkxSmrnlGZXXMJG3DzdNuV31bV--mqXoQeNt5ledYqtcV6_uYfZpjE5EBIXRw93_CYTYw_zwt_czyXY2h1b4nSKz8aSatjR844dlb3YkU97OSjFkR8ubCzuHk_NBSKAVT5Ev4Em2A6z1SR-xc3BmMw6z00zoRPpNEuYsQNHdrUTSMaAd7wx3mb0zoED-3ephGpcmLwsYnZowqPls9bs_rUoHBPiFifk9nsLEsJn_NcAlCj8SQ0Bqv-BZ011JhTBdVNuaVXWHF2wbfRodxPKJF4VTcsndcJ6Jj4n15u66q08BsbbTP3vMWRFXZb2A9BcD0mz4ejUxsk6ciHEor28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدئوی وایرال شده از دعوایی که  تو گیلان رخ داده؛
یه مرده به بهونه‌ی دفاع از زنش، دو خانم دیگه رو کتک میزنه
!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70494" target="_blank">📅 10:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70492">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536dc396b0.mp4?token=bCho9rjfDeOqp8WrP_DhOzFBc4JXoduI4xoxtA5nxmZrRaWY6kJ7Du36If2RM0ol21pSok1Daw0T_DdB7vc-xJeTe2IEcck3yaz_G1eZemWsdPZCQYGipbeBr1jfMf_koNwtvan_FWtomp-jpZruywLhjKY34J1Pk4mjbNNmi4IjghqXDj5P0HNyesFC5pFxM4RSQbLh04fdYgNSt2ZkaR5mvzXDOODtmNoxGw1dG7OQ8DBI5pplVmK-uGTuzZfEhQrH8gNQ3vNl2rHyxWAp6VY_oaYc8ZsZZ0Cy2FyNu9Xob4RLclgUUJWstnAg3pZ9KBiz_TYp3Q7oCCfjI8R6YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536dc396b0.mp4?token=bCho9rjfDeOqp8WrP_DhOzFBc4JXoduI4xoxtA5nxmZrRaWY6kJ7Du36If2RM0ol21pSok1Daw0T_DdB7vc-xJeTe2IEcck3yaz_G1eZemWsdPZCQYGipbeBr1jfMf_koNwtvan_FWtomp-jpZruywLhjKY34J1Pk4mjbNNmi4IjghqXDj5P0HNyesFC5pFxM4RSQbLh04fdYgNSt2ZkaR5mvzXDOODtmNoxGw1dG7OQ8DBI5pplVmK-uGTuzZfEhQrH8gNQ3vNl2rHyxWAp6VY_oaYc8ZsZZ0Cy2FyNu9Xob4RLclgUUJWstnAg3pZ9KBiz_TYp3Q7oCCfjI8R6YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
هلیکوپترهای CH-47 شینوک، UH-60 بلک هاوک و AH-64 آپاچی ارتش آمریکا، در کنار AH-1Z وایپر تفنگداران دریایی آمریکا، در یک نمایش هوایی ویژه مسابقات Freedom 250 Grand Prix در واشنگتن دی‌سی به پرواز درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70492" target="_blank">📅 09:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70491">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6f5402ef.mp4?token=cGaiMNWLMwNwwKnctx9-sGBnltdD_R_MM-y-MfXWGtD7Il2vDCP0f6tElevKoPYQ_p6vGzrwCEE8342iPGTDbnrkxc4EFxaYPfmr8_NFbF4XrUBEiv-0Ky16GYXojwq5B_de4Uqk284ZKrJZ-t5PaPvxxlpAFudzIB5lofpfOY84IPLiLS9RdcUaj3cLOPe8eY2MV1_yNTme1B7vRtAu9yTvXiRrWhwqVJfetBJ1Yu8KQ9GEZGR6GHMm1hqHtqiNwEKqhyQVhqmIXpg2YabaObNgSiTBK7A94aVkgKRIflfxc6CBXFeJ2WzzveMitZF1qUr9t_XWohx5KRl--KHnOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6f5402ef.mp4?token=cGaiMNWLMwNwwKnctx9-sGBnltdD_R_MM-y-MfXWGtD7Il2vDCP0f6tElevKoPYQ_p6vGzrwCEE8342iPGTDbnrkxc4EFxaYPfmr8_NFbF4XrUBEiv-0Ky16GYXojwq5B_de4Uqk284ZKrJZ-t5PaPvxxlpAFudzIB5lofpfOY84IPLiLS9RdcUaj3cLOPe8eY2MV1_yNTme1B7vRtAu9yTvXiRrWhwqVJfetBJ1Yu8KQ9GEZGR6GHMm1hqHtqiNwEKqhyQVhqmIXpg2YabaObNgSiTBK7A94aVkgKRIflfxc6CBXFeJ2WzzveMitZF1qUr9t_XWohx5KRl--KHnOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
متکی، نماینده مجلس:
۹۰ روز آینده روز‌های بسیار مهمی هستن، ترامپ ایران رو مشغول تفاهم اسلام آباد کرد تا انتخابات میان دوره رو پیروز بشه و بعدش قراره تازه بیاد سراغ ما.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70491" target="_blank">📅 09:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70490">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70490" target="_blank">📅 02:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70489">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6iZ0Xi1_IV3D4utTvkgKhj69caZHmlVAc6kmjLtjUIspd-uGlZKTrjsdUPZqC8r5aGV98Jz0c2Eq06jRxPJjx36y4QQnMbHD1lWSRgAiHdvlQg4B4AnW6wn9yCLc5LNctts_e_PZOm6ioUkqdjnmFMplfZL11AWZYVK2VGggCpK0IetpWkQoSiuRwdTplSI_pepQM_-zzqdMRIt9xSBsrJaOBD0_9rzVEwR8xB2uEbEZ1uWUk8yn1AiDspaQyB8_lUNfCUbZ4m8acjqeRTGkZp_dBqfLIv5X8bja5Gkre-gYyZ30tSZlXt7QNX5tHyarqzxKMzys0Ih1oRL3rmF51Tk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6iZ0Xi1_IV3D4utTvkgKhj69caZHmlVAc6kmjLtjUIspd-uGlZKTrjsdUPZqC8r5aGV98Jz0c2Eq06jRxPJjx36y4QQnMbHD1lWSRgAiHdvlQg4B4AnW6wn9yCLc5LNctts_e_PZOm6ioUkqdjnmFMplfZL11AWZYVK2VGggCpK0IetpWkQoSiuRwdTplSI_pepQM_-zzqdMRIt9xSBsrJaOBD0_9rzVEwR8xB2uEbEZ1uWUk8yn1AiDspaQyB8_lUNfCUbZ4m8acjqeRTGkZp_dBqfLIv5X8bja5Gkre-gYyZ30tSZlXt7QNX5tHyarqzxKMzys0Ih1oRL3rmF51Tk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
a1
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70489" target="_blank">📅 02:25 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
