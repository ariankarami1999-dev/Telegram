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
<img src="https://cdn5.telesco.pe/file/HGpMlu_zNCOIiUKqQ5pU7BKAathb_V3C3T8ZwnUdpy-LEXzWQqt8HocwaHluBq2vsQDHY9oS-0Za289gkeePbJEkmaMwlYkh0ME-2Pvk-NhTarJaM9sbO4KUXb99MVLjzL7M0I7QWruie3qNXXAwks2ltlCMalDmzYLujJlk2HlHZKjpHiIi2PfkX48BEvV6CVPhcFswN6WktqCWmL8D04COjH5BExli_HPxMYJYZ1Qaeu1I1vQFjYPoUnQO9oGIAkxdnn_qNAZW4x--dluXRIYJB9eARVnoJU-1WQlqwDSasNHdr1B4Cs7kpg5UsbZuhfWe6GtGFOAREL9fLmY7wA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 469K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 13:02:44</div>
<hr>

<div class="tg-post" id="msg-103658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok43Hnz78bUsfiuVpOdr3FVsv-SVcAbznkdxkSKGvHJEAgMwGZNhl-Rihz4i8u2_CIBkPV1inQGVp_zZ24tZOrghirx3-Eu4GPbMxRv5F3G5RJfrkcEgKZRtDuLoewcF9zXdEFQd1pGUNYNFQE8pyV_Vs-RXBdB1bVZoKlWsx0Db9uUSd8K2G2fMsBpOvoTgVg4gOAkgH-aDQsOnRS28v5nAC6nOrUE3ly9Wu8DLoD--jYr4y0d910kvoDg4F7oweOA9ylh1UV_Y9qQTyF_qWHFbAO8CFZZLIRm5I7dk5tHBE3jHh9iocxdlCjRNmflcKX4pZZR5JD1yqcu6Dpjkgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری از فابریزیو رومانو:
🇪🇸
🇵🇹
بارسلونا مهاجم اسپورتینگ، لوئیس سوارز را در لیست گزینه‌های خود قرار داده؛ در صورتی که انتقال جولیان آلوارز شکست بخورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/Futball180TV/103658" target="_blank">📅 12:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103657">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8zrfhclwdkElou0iedY2EI7Cvc7V0TJ6kkcFywgm8vxgGgQKYY9qtlnULvkK9Q23GK5wrL9GbgFxVMmzkNUPrjXARxxfosz5A32exmCh_dW77CJg0kMvg7fi6oNPtys0w5on3-lrLVZFWm9mDXC-rKYydv-1sOKBMoLNbl9sCOHLiPlRg21f-eXn9tzJvzac5_KBA-fSlCLMzvMzD-5rwulJOQZqQzbXXthMgOuQ2AqBu7TF5q1MoVEEOODuvv-P54Q75Ic69orH17Z_9p6ZY4wJFhlIFlst1DEBZPzWTeQsiD-q_52bcK9IXxjrGuIpLFZNFKz652ZwNpc9COhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
از فابریزیو رومانو:
🇪🇸
🇵🇹
بارسلونا مهاجم اسپورتینگ، لوئیس سوارز را در لیست گزینه‌های خود قرار داده؛ در صورتی که انتقال جولیان آلوارز شکست بخورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/103657" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEFnyF7V7q8O__rnAmTv1tqh5FzA-ksT_kU_S0-b0BIMFeCydOLPv4y-qoZE9UwyrzzkOcKJdgjA2VYNAfDrV_-Ht9aIigErdjUQcPf3_o8TZ8akNgvCzjUHhB1UHXrEh7vhp51vt82_JYvYZihVUL4fo0SygoBho6JhRGnQj5f5-X-1W_sYTqvjNPdxKPSKz-fx2wXaNdUnOdoU06ysGDgs_ucVWB2mASv0RzFfRkYr7MQLL2SrUkcbw0IHlt_bje0xA-rZXl6nVQuISzFJE-zjCL2a48CrWT8NBOY_M1Dd0CyfRnsdLSh7vAZkfdUO5pPzOSVhxPgiYArvzqpbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
از رومانو:
🔻
پیشنهاد جدید بارسلونا برای رودری حدود ۷۰ میلیون یورو هست که آماده شده و انتظار میره بزودی(شاید امروز) و با این پيشنهاد قرارداد این بازیکن بسته بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/Futball180TV/103656" target="_blank">📅 12:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71c47edf1.mp4?token=pkpl-KuRzDulACVAZlmYuf1Ydi6tNRYv44ajJ_QUkaAFMFAvk2bkhpStBRmuQNKFE_wxa5GU_bHPAYLHV7TmTe7j4pvFkNI6noK6ni3omPH6pguOarC9tAnFxZwxGdLtKbkZG4EyZOlqwSD6vJDtnM_UJPT-5nowo0WCzoDktdLbzD6spjZMpG3OE2LKxj7RTeSSnmLf6zMoYIynX1ndFSptP0urjqoaQHx4HLZ1CNWk3xA_hzNgXG94z1C3sTRy2DPefbn5oovqoVXnv2-t_GA5ucI93UNJAFfIFEGSDn9BLbHKiGd7L7cIAteUkTzwfh8QydkLbs0RTbD-P0updqpzo9TZHahWEAwKsT9EYZyqD9ebBQibVQCAXTwVWcXhUL2q5rdlAypAYhpCcGUS0P3j1lo323_nxNppzWCPRbbAb8xUuC47d95s4q3doCjugt5HetClNsJ0oganj0m6DgNr3DB_v-4T-TRvpX5OSsrFDyJt_b2w0Zr6sQUhc7np729KEvZW2FkbDMO85hVG6RJGPYK2CrUtmFcHd2KdKcmiQs81WoJPt2YJ7vcJdOtsoRh6Oi_5Op-WOnO9DTi6V0vWF3mULrnniT6C1ELwLR1AJ4L3uxLoFMKUJPnL1dVAuv9oh4AQnCZEqhcdfy8nDAB8CCbWCr9Y-x0XMobFkB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71c47edf1.mp4?token=pkpl-KuRzDulACVAZlmYuf1Ydi6tNRYv44ajJ_QUkaAFMFAvk2bkhpStBRmuQNKFE_wxa5GU_bHPAYLHV7TmTe7j4pvFkNI6noK6ni3omPH6pguOarC9tAnFxZwxGdLtKbkZG4EyZOlqwSD6vJDtnM_UJPT-5nowo0WCzoDktdLbzD6spjZMpG3OE2LKxj7RTeSSnmLf6zMoYIynX1ndFSptP0urjqoaQHx4HLZ1CNWk3xA_hzNgXG94z1C3sTRy2DPefbn5oovqoVXnv2-t_GA5ucI93UNJAFfIFEGSDn9BLbHKiGd7L7cIAteUkTzwfh8QydkLbs0RTbD-P0updqpzo9TZHahWEAwKsT9EYZyqD9ebBQibVQCAXTwVWcXhUL2q5rdlAypAYhpCcGUS0P3j1lo323_nxNppzWCPRbbAb8xUuC47d95s4q3doCjugt5HetClNsJ0oganj0m6DgNr3DB_v-4T-TRvpX5OSsrFDyJt_b2w0Zr6sQUhc7np729KEvZW2FkbDMO85hVG6RJGPYK2CrUtmFcHd2KdKcmiQs81WoJPt2YJ7vcJdOtsoRh6Oi_5Op-WOnO9DTi6V0vWF3mULrnniT6C1ELwLR1AJ4L3uxLoFMKUJPnL1dVAuv9oh4AQnCZEqhcdfy8nDAB8CCbWCr9Y-x0XMobFkB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
آیا واقعاً مشکل بنزین، ارزون بودنشه؟
🔻
صحبت‌های شنیدنی و قابل تأمل جناب پیام الیاس کردی اقتصاددان در رابطه با قیمت بنزین و ماشین در ایران و کشورهای همسایه ایران...
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/Futball180TV/103655" target="_blank">📅 12:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103654">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
فتاحی رئیس سازمان فوتبال استقلال: خیال هواداران استقلال راحت یاسر آسانی مشکلی ندارد و می تواند بازی کند. کارتش هم صادر شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/103654" target="_blank">📅 11:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103653">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defca1f994.mp4?token=URckoJEnOhMVJPzv4P5rieBKaupcGF1A2rSJiTa-_TGabHrhaKsN91hcOcqqWiQ4v-Mrpk07F5Lh7MaFHB1rVmZ9aU_hUQBWWnSgxsF1z-EAuHSBL3r9JLlehNTfBxinE0ynX_tnLXC1niwH9SkDnX0HUBLxOJ4thAo9HVnw-VuCudflZGL5ACwESxEPZl17tynlnrbt5zExQIizpF8XYob0vrIJX5z3Q7yAXqfph-_kzMLltRTxKMAxv9lIGWcazAVAuBi0VkquvvqkrKL_g0xqE3IqwqLJXZ3uGQ5yzWm-k-JkXIPHnE27Ng4j1a2iuQtjGUu_4JehyOdsavXtCYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defca1f994.mp4?token=URckoJEnOhMVJPzv4P5rieBKaupcGF1A2rSJiTa-_TGabHrhaKsN91hcOcqqWiQ4v-Mrpk07F5Lh7MaFHB1rVmZ9aU_hUQBWWnSgxsF1z-EAuHSBL3r9JLlehNTfBxinE0ynX_tnLXC1niwH9SkDnX0HUBLxOJ4thAo9HVnw-VuCudflZGL5ACwESxEPZl17tynlnrbt5zExQIizpF8XYob0vrIJX5z3Q7yAXqfph-_kzMLltRTxKMAxv9lIGWcazAVAuBi0VkquvvqkrKL_g0xqE3IqwqLJXZ3uGQ5yzWm-k-JkXIPHnE27Ng4j1a2iuQtjGUu_4JehyOdsavXtCYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚨
‼️
سعید فتاحی زیر حرف قبلی خودش زد
: منتظریم فیفا جواب استعلام مارا بدهد که آیا میتونیم از ۴ شهریور سه تا بازیکن آزاد بگیریم یا نه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/103653" target="_blank">📅 11:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7ymH1gHckgSAsvvtWoF2_u5KWXrXwsrRb66-5TaHoHtfvN3drPF6kflm4NytituzGNWkS5XTPlh9bgUkse-KjYIlSt-ys1OUR-8TsdHKqriX5fPx9s9_OWwz-lC-B4N6iWb5rj3d7vDCNNwScXTkCmMPZ-k2mp470ichkbDtu3_2io8Nwid7NXquMmlL9-Oh3WQ2NnHAKpA3u4bhkUZUcic8CB9zn55MJ8yPQXqUgsNB8GWU9F9HvD0u0BP7kyG_j2R1xXyQrFrBU1wGpzn4dgi2EiUWp-LpY15CA8R1cI6x1GGQvCQ9oXV3Ae7Xrh5FoCk6oEzyeQeaoYTStYU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌سوم فصل‌آینده
منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/103652" target="_blank">📅 11:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af209c88e.mp4?token=iv23KAckDS1o_qlIcWn3Jedi1A_wfMdEFVAQCpgt9Jomdeobke1B-GSd-IunlWeikvDYlNmTXjiED3kufWge6IIidO_09kz2BKgpavmAAlRTn2XS1Oor3OdLDhtZba5hf_YXEdNg6YxpQ_kX4254TLtay2jxCXROkPqJePK7ZIFyF--o832yEFmzj-G_6aNWYHSqxxpoF7lS0L7b5hNJsZ3KW7E7DqV3PJZKstYnwS6Bw-u8xU3KTyRXt4xad2FgOrAKnwCRjPDXMQjcSoqf83_YDI0gO6tdlYWSVfPQP7Q6cJAZXyIgYk1xqIKIe8n9VWOlZXqSR6FrNKx8Q2ZG4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af209c88e.mp4?token=iv23KAckDS1o_qlIcWn3Jedi1A_wfMdEFVAQCpgt9Jomdeobke1B-GSd-IunlWeikvDYlNmTXjiED3kufWge6IIidO_09kz2BKgpavmAAlRTn2XS1Oor3OdLDhtZba5hf_YXEdNg6YxpQ_kX4254TLtay2jxCXROkPqJePK7ZIFyF--o832yEFmzj-G_6aNWYHSqxxpoF7lS0L7b5hNJsZ3KW7E7DqV3PJZKstYnwS6Bw-u8xU3KTyRXt4xad2FgOrAKnwCRjPDXMQjcSoqf83_YDI0gO6tdlYWSVfPQP7Q6cJAZXyIgYk1xqIKIe8n9VWOlZXqSR6FrNKx8Q2ZG4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
فتاحی رئیس سازمان فوتبال استقلال: پنجره استقلال روز 4 شهریور باز می شود و استقلال می تواند سه سهمیه فیفا خریداری کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/103651" target="_blank">📅 11:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148293e4ed.mp4?token=IGb7niZuSbr9juTDBOG0H8L8a404JFoibQFyAzlSkbbDMNgcXE2sqePSgMC9cnAk2htMyjA_Kizdih5W4S4TPukaFDcU1FpTbfhAM7es2QzqeTmCxjMbtgBpGtAylHw3hl2Tz-VIyc8pHoGXmsyAhVxSd_s61Rbm-3jmx7GemBeIDt1VV-G946I5SRUPq5KH0vFohgmDsE31Bmhx1RAfkDkn1QYab1-SWvAL9HZZ3UugbymxUrZQK50tIakqPZqB8YtGDyaOdyW6iNPfgzTth6Nq2SKCYjuNBaQo9isE22wQYk2yf-nHYtQ5gf3yZmOiUOY1Gi1pQ372Ov7ezDWuRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148293e4ed.mp4?token=IGb7niZuSbr9juTDBOG0H8L8a404JFoibQFyAzlSkbbDMNgcXE2sqePSgMC9cnAk2htMyjA_Kizdih5W4S4TPukaFDcU1FpTbfhAM7es2QzqeTmCxjMbtgBpGtAylHw3hl2Tz-VIyc8pHoGXmsyAhVxSd_s61Rbm-3jmx7GemBeIDt1VV-G946I5SRUPq5KH0vFohgmDsE31Bmhx1RAfkDkn1QYab1-SWvAL9HZZ3UugbymxUrZQK50tIakqPZqB8YtGDyaOdyW6iNPfgzTth6Nq2SKCYjuNBaQo9isE22wQYk2yf-nHYtQ5gf3yZmOiUOY1Gi1pQ372Ov7ezDWuRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
❌
فتاحی رئیس سازمان فوتبال باشگاه استقلال:  هیچ وقت نگفتم پنجره استقلال باز است زور زدیم پنجره را باز کنیم اما نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/Futball180TV/103650" target="_blank">📅 11:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUI4geg_ral6LLncMb_DmuMxdJRYJwqYj9qwD9m49MMxWwMNGONcq6mP9eTuON9kwQ0M2n9d-dFzo-uBiTlH6IoVRhlcAxsH-VW2hAGA99GxLf-WDJXTvhEQILh7PG4-zozoYtZVSHI4iyR9Of09IqsJv5J9rHKr5K47ecf9fDcJJeHWy3_xgxLEFb90YZbtu9R_ucF3Q0y_NZcB2HiPQRfWiW4-8aZrNy26JbENpcbZe09WTTWxNKK05VmlS_evGKEdEBRvF2RFHjgns4CnoFhSVXz5iKUm9Y24fvZnYZovj0vRT75M6LzMkPvmV8a1Qrv4fqY5c9kIb6PVV2cHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
🔻
رومانو
:
بارسا بعد اینکه دوبار پیشنهادش رد شد حالا پیشنهاد سومی آماده کرده که مبلغش بین پیشنهاد 60 میلیونی آخر و خواسته 80 میلیونی سیتی هست. بارسا همچنان به انتقال خیلی خوشبینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/Futball180TV/103649" target="_blank">📅 11:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d3d38ab8.mp4?token=dNQqlRUfnJ_KLoe0gzG0zH71HD_k3MfE3629k5POLkQBLKBN9atsXsCYLLJ1xlbANERj2WlcSIeVZHuu9BHuIKhgujdl9JE6bJ_qhBbuuAQPmmCsQiuyjoPLVgXKAnwEXc8p-b0h5nAv15r1d7XOuNX1V7c-jJ63IXBo4JAdm7Nym_u6uXUKdk9SXWFcllbvO6OImgm8kpA65IpBIM1rAGk9uo3FsnsOK-zQ9RYNktz2KdVbqC4pJIqqmdE3qVJbbxuiOe_Fqc7syaqO5EY-3hG1GrpHf9tSuG2RPlulQGEx--IL9qWP6a8sHLvPkH-bcMQTE8mCN2GRubzW9xLqvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d3d38ab8.mp4?token=dNQqlRUfnJ_KLoe0gzG0zH71HD_k3MfE3629k5POLkQBLKBN9atsXsCYLLJ1xlbANERj2WlcSIeVZHuu9BHuIKhgujdl9JE6bJ_qhBbuuAQPmmCsQiuyjoPLVgXKAnwEXc8p-b0h5nAv15r1d7XOuNX1V7c-jJ63IXBo4JAdm7Nym_u6uXUKdk9SXWFcllbvO6OImgm8kpA65IpBIM1rAGk9uo3FsnsOK-zQ9RYNktz2KdVbqC4pJIqqmdE3qVJbbxuiOe_Fqc7syaqO5EY-3hG1GrpHf9tSuG2RPlulQGEx--IL9qWP6a8sHLvPkH-bcMQTE8mCN2GRubzW9xLqvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
⚽️
استیون‌جرارد بهترین هافبک تاریخ لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/103648" target="_blank">📅 11:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a640041daf.mp4?token=eZoaJe0OJq8P6YRVQBMkZ6HAlf3NMbodjxThBE-EWPwSVzc2mA_m6G3e7nzEXXRT4S1G9RWDX2LFrfeBNi5_2_7CRIL74jxAlypziF7aR8SVlpdxHUyREU99H6_EjnWetlskoCwGMqTXlqMZ1Gino7a9OY0-tmU--TLarZUOsxZPczMJo3AWpzlHokN8LmNiQvr08C0Nthd9JjJc64ZpzMhxUCXmwutNTE5AN-yEFXSX5gbggOUZj3BwycfZ8du6q34_jg3lqzqz8RLqPCnRv9y7R4nZFP_I6ZcINT6GxrZDaZOlHKvCIlg_R0Hxe90quCDVUcEZPJrLRVOLkpmYLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a640041daf.mp4?token=eZoaJe0OJq8P6YRVQBMkZ6HAlf3NMbodjxThBE-EWPwSVzc2mA_m6G3e7nzEXXRT4S1G9RWDX2LFrfeBNi5_2_7CRIL74jxAlypziF7aR8SVlpdxHUyREU99H6_EjnWetlskoCwGMqTXlqMZ1Gino7a9OY0-tmU--TLarZUOsxZPczMJo3AWpzlHokN8LmNiQvr08C0Nthd9JjJc64ZpzMhxUCXmwutNTE5AN-yEFXSX5gbggOUZj3BwycfZ8du6q34_jg3lqzqz8RLqPCnRv9y7R4nZFP_I6ZcINT6GxrZDaZOlHKvCIlg_R0Hxe90quCDVUcEZPJrLRVOLkpmYLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استقبال شیک از پدرو پورو ستاره تاتنهام و قهرمان جام‌جهانی در بدو بازگشت به کمپ تیمش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/103647" target="_blank">📅 10:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmN648FV49vpN4wkRz4sd0U-OMW6EZSUmJ-zVAGBwg4oqZ-4l_DrI8nmOxFMSKvRonikiYvV3blE0iFO4Ma-TnMs0_OAF0gMgbEnMzsKpMlsqQ17lNNar7dUy0cptNfN99Zrvj3YTfKnoXfHAKvyiKtcfrUzcWP3du4MEegkBF-gfxXBZVjD2L_cSKd_NRWoPKAtxZX5_ZADl1s6ikJvNBIcXhjk8dJu-4vwCvM-lTjx3IluizzYOq1Gv8MWUQh4B-zoQv4NMnCFzZP7YkCPX6fiioDYPwQE1zlOS2-Wfj4L1bu3b6DYYU_Wa1_kV88c9r26HzP1gta9j2T2JDkttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
خط‌خوردن آلوارز از فهرست بازی اتلتیکومادرید مقابل مارسی در آخرین بازی پیش‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/103646" target="_blank">📅 10:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103645">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys_e4qF0-4vsJdvDMRG56sQbLrlfS5iFDi_otk5F6HsUHjfrArouYH6i__AnFXytdm7QxD8kA_R99IwM_wZnSAcpZBeuHS7wOcYrWqAMnUUM8m3oP_pzhf90Vn7Cb0jYLoVhR6zAIQaYy3swQgsAvclyQeRWXsUUSH3JzQer0lfYmHHP4m28jSRHpyswxvuRCDVrw_BzgpOhJL9VsOCktxtj4ydhT1qClMSd4e2NKSCIsFy4XB6SrjM8Gm6hP7ojZhgHYcB2o_5DRfYJ2OD8_HaWV59NTUd373ljwvQR5dmNEeqEOX8zVXIfrg-gF03vlvHgeosVQcPgxG0yH8F2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر استقلال برای بازی با مس‌شهر‌بابک
⏰
ساعت 19:30 شبکه‌سه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/103645" target="_blank">📅 10:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103644">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d0f47a29.mp4?token=bq6RmzIwJotZPTOwk2QFFFh0pUoPKyv_dZIbJAeMZtiwxHxj6fZLV372C2z1MkLHOqYjz5Rs2yW3xeoP8B1sr9pEBVQjNifh6JATuMPCH_sM4PssT4Mv_bQi_5gqojfmJH-NgPvkNuMJ1MPMTMPRNNh-C8FDmqryMOtcKvKAcpQFZD84XaUNwqbJStDPVx7vSk1Chd6G-Fv2XxVBoXVD_rRoS0ypw6x5OURjAjggA16tyU3JRfmmfBczahktWnK7yq7PYrOZYw7JSdGudfTzyIKHQez7BZg_TZcv8kZ3y-Eq1H81BpASBysyzTdFxH34_DYRA46R8N5CNNDd0UVNaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d0f47a29.mp4?token=bq6RmzIwJotZPTOwk2QFFFh0pUoPKyv_dZIbJAeMZtiwxHxj6fZLV372C2z1MkLHOqYjz5Rs2yW3xeoP8B1sr9pEBVQjNifh6JATuMPCH_sM4PssT4Mv_bQi_5gqojfmJH-NgPvkNuMJ1MPMTMPRNNh-C8FDmqryMOtcKvKAcpQFZD84XaUNwqbJStDPVx7vSk1Chd6G-Fv2XxVBoXVD_rRoS0ypw6x5OURjAjggA16tyU3JRfmmfBczahktWnK7yq7PYrOZYw7JSdGudfTzyIKHQez7BZg_TZcv8kZ3y-Eq1H81BpASBysyzTdFxH34_DYRA46R8N5CNNDd0UVNaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🎬
🥇
رکوردشکنی طاها‌نوجوان وزنه‌بردار ۱۶ ساله ایرانی در رقابت‌های جهانی که رکورد جهان رو با مهار وزنه‌های فوق‌العاده سنگین شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/103644" target="_blank">📅 10:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103643">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b4e45e64f.mp4?token=G25PrOOGtvAJaPF14VLMY4cH7Y0buBZs-M50QbOQIYaG3E_pOit5vmjwdYy3rwX_P8Opq91Ry3TnngyBfo-U1kmer2hD-elrMGpMnuRZXj8gmJ6LIUzSIbYMrZ7UglTgm2_iqwiGauouo4TnszoltsceXr4h6KRTcglXevqi9REhBPgH0jIzyn75Ok_XwVajZBndFkuM8tzScv5lCOo43gUuuPSw4j8wQYH5D0gHVo6vufOg2poVE6tcnvgor7WWRtpjU6mCHoDpgVKXMh7HrGZ3jQyR6b5H9L2pgM1JuoR7Z48bXyZJxFbhhYb7wGQCg_S0Zuvs-rM8_ti1Bfq2GYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b4e45e64f.mp4?token=G25PrOOGtvAJaPF14VLMY4cH7Y0buBZs-M50QbOQIYaG3E_pOit5vmjwdYy3rwX_P8Opq91Ry3TnngyBfo-U1kmer2hD-elrMGpMnuRZXj8gmJ6LIUzSIbYMrZ7UglTgm2_iqwiGauouo4TnszoltsceXr4h6KRTcglXevqi9REhBPgH0jIzyn75Ok_XwVajZBndFkuM8tzScv5lCOo43gUuuPSw4j8wQYH5D0gHVo6vufOg2poVE6tcnvgor7WWRtpjU6mCHoDpgVKXMh7HrGZ3jQyR6b5H9L2pgM1JuoR7Z48bXyZJxFbhhYb7wGQCg_S0Zuvs-rM8_ti1Bfq2GYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
محرم نویدکیا: سپاهان ارث پدری بنده نیست! رامین رضاییان را نمی‌خواهیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/103643" target="_blank">📅 10:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103642" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/Futball180TV/103642" target="_blank">📅 10:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103641">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMFh7Cos9AexoZKZP6VZiWF23Y6O1pl4IMQknGULzv0F1f6UpkdE13N6jXIxl9yI1aOlINl4yTzjCEe3ZNVJtESHs3GjoeY1ENgc0bALQvR9ZYW_DJ0dsBBpiA29gfCqhHFMX97WW31rO8J7I10jymrX3djBnGKTXg4SsA1BBpALG-N2gSbSvesUjFBpPUacCM7LT0zmKy7PLuKepwHAwEC0BT6heIV4O4UKkOfw4BvS5S57oBLoFjJVJYJLyiziMQT8Gl0_UR2rgI9hP3o4CwhlBFhIvWudNYKOpYbz7IBCZknbQ7-hu9Vasl_4jRKotjDGOrbKc5yGCs18epCFmQ.jpg" alt="photo" loading="lazy"/></div>
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
r23
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/Futball180TV/103641" target="_blank">📅 10:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKPy7tcWeAoyPlm1b1Hl9xz3RlySVbQ_MVcnzD2uaA_XHpNUGfEOsMU3s0eSeS7_1ILDTlO7AxChUuujV76wSLhdudC3WsL5CLYqPp0G-SRdf6AMA_GxfZ4e47Do47AXvom7hRTrPRO5hK_tMmKxknIA18vUucPdLsO-_xlwwQKnmRqdhbmkHK2bKbGMK22-j4hrb84gr2BjEgAFQqUBRDQTwbGmQDzesE2QY8ZfYIbDIw8VtgdVgoCng0s7DwrI7rGGFVgm5r1RjV9TjWJ5xaosIMiwuwiARW81cA2RAC6Ay9NT4Hi3RkSLYV4JMUH5yhDnYkc296-E4QIQLN4PHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
#فوووووری
از نیکو شیرا؛ لیورپول با پرداخت 125 میلیون یورو به جذب بارکولا نزدیک شده. قرارداد این بازیکن با لیورپول تا سال 2032 اعتبار خواهد داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/Futball180TV/103640" target="_blank">📅 10:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31e6ea024.mp4?token=CcsTyFNP2jthv2Gyuv3Fo-yAtDJofvN1L-UxXUisf9wa1nCrXsX0Aw18Rho_Vyo_UHOW1hWNGbF4IPlFPqUIjIo3cToL-jnV4i-YS0iW0UOS7VdtSx7tQZDCR-I_Zh9uCEmuxlHevbQF5OsDtyMTn7HawKYK9hXr0LRGcqF12si4BWKf92lkgDYiMP3IramHpqG5nObQoBEM_jjE7drHjMSAZWEQSNJOSOks_0r3hD7Imh5w1AYjO8dg-Fm5uHVNvcTRNJdrIjWe1VILHH4ng6_1A2z76-ZHcBlmBdJ4oV4yGBTnEAFz1gQFxEI2HURiGu0kBZeFgyFa9UhzeU45nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31e6ea024.mp4?token=CcsTyFNP2jthv2Gyuv3Fo-yAtDJofvN1L-UxXUisf9wa1nCrXsX0Aw18Rho_Vyo_UHOW1hWNGbF4IPlFPqUIjIo3cToL-jnV4i-YS0iW0UOS7VdtSx7tQZDCR-I_Zh9uCEmuxlHevbQF5OsDtyMTn7HawKYK9hXr0LRGcqF12si4BWKf92lkgDYiMP3IramHpqG5nObQoBEM_jjE7drHjMSAZWEQSNJOSOks_0r3hD7Imh5w1AYjO8dg-Fm5uHVNvcTRNJdrIjWe1VILHH4ng6_1A2z76-ZHcBlmBdJ4oV4yGBTnEAFz1gQFxEI2HURiGu0kBZeFgyFa9UhzeU45nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✅
ژوزه مورینیو: هر کاپیتانی رهبر نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/103639" target="_blank">📅 10:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceed0b675.mp4?token=fACzrMBHhRHzyEHvBBFYfFedqeuEmvlYRG3upu8sXcHIxhSaEKmFN6eQ09EIxxWqW7veMNBjGMSnzNW9Lz5PyNlusYBNhgQjRoz6HYf6P_r4peyXmmhcW5Z1KP909pieGkLAKXrZQqSOIhWTB79JUlGdOLf2ghEb3evlfTAaqI42k1SGDk349b7pBly1z617ryBnuy1hbVksFSp-6FNcV8G8KpbE-HZJS_DHXcqDukyEkEcwlqTK6Phdnjp-p7Q2cD02fVT920rE27Nbr_8X5yCoXdUQAnYU_tLFxRBCc9zFl0fmzpCWs-OpMIxR0RN-a40BoL31X3sd38_k6UYWQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceed0b675.mp4?token=fACzrMBHhRHzyEHvBBFYfFedqeuEmvlYRG3upu8sXcHIxhSaEKmFN6eQ09EIxxWqW7veMNBjGMSnzNW9Lz5PyNlusYBNhgQjRoz6HYf6P_r4peyXmmhcW5Z1KP909pieGkLAKXrZQqSOIhWTB79JUlGdOLf2ghEb3evlfTAaqI42k1SGDk349b7pBly1z617ryBnuy1hbVksFSp-6FNcV8G8KpbE-HZJS_DHXcqDukyEkEcwlqTK6Phdnjp-p7Q2cD02fVT920rE27Nbr_8X5yCoXdUQAnYU_tLFxRBCc9zFl0fmzpCWs-OpMIxR0RN-a40BoL31X3sd38_k6UYWQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🔥
🐐
لیونل‌مسی و یک در برابر یک‌هایش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/103638" target="_blank">📅 09:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
⚠️
پشماممممم اینجارو ببینید. درگیری دیشب هیئت چوب باز تبریزی با هیئت یزد درمشهد مقابل حرم
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/103637" target="_blank">📅 09:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L43FhTEPnzuBQuDb-ZfBfJixF_FLaNA2F8UdAilKBivSyHKxR0fR993ygFZB2ZcVn3FqieB5iTEnjpFQKxMJpNRyrb14p7iTHELJT2TQvpTWV2ceo0UH1lgR8LbMOV_cTvzlOKmwjvMUbQlfTG5YgVrxxMe5y_KJOiLzFlSn42sAmVdZzwYzXU6zMnGnjtltQ_AWiRcNfVXGzZfN575ntgNeHA2zlAg_3S7nzx7Wtcc2kufcUNTkwm_C0gdlvEqAa0MOJMVLpHjmBpbpcgkWDyiGdD2uB8QKSjshGN7eR8E3UO3Us5OrDPuFxgX6UOQAqJEcUdQTBv_Y9c5nviHE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽️
جدول مسابقات تاریخ پریمیرلیگ انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/103636" target="_blank">📅 09:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c1d2dd8b.mp4?token=PUliaqtYQ1aQz6s6yskVYsVu8p7HBYoKfdJf6WOtq3p1ZM1ZOHn__FBlAUKdep0U0hl34lNyY_zCBRagXTm9tKtdATXgw3-4BnczoVcPSIeoSz3aEZxwJSVjjYJc5JblmrUTIk1E-dImSZjOwsruKWXtcDU9jtwzLTquRPrnySIpVhfrhFpsOl3STPI6XvZzjPEXP0bpbBU_UKRzD5rDgOC0m44NmTBsBpBf5RIpNbN_J6n4VEdHZbSQF4wnLhRWiVBPHnI5jOZQOllZlUP5FMr-7u7ExgiYMy2NEce7wsM3RnL45BNqSgOUTNfGLgIicLjsAbB8aVDDfQkD1rQ2kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c1d2dd8b.mp4?token=PUliaqtYQ1aQz6s6yskVYsVu8p7HBYoKfdJf6WOtq3p1ZM1ZOHn__FBlAUKdep0U0hl34lNyY_zCBRagXTm9tKtdATXgw3-4BnczoVcPSIeoSz3aEZxwJSVjjYJc5JblmrUTIk1E-dImSZjOwsruKWXtcDU9jtwzLTquRPrnySIpVhfrhFpsOl3STPI6XvZzjPEXP0bpbBU_UKRzD5rDgOC0m44NmTBsBpBf5RIpNbN_J6n4VEdHZbSQF4wnLhRWiVBPHnI5jOZQOllZlUP5FMr-7u7ExgiYMy2NEce7wsM3RnL45BNqSgOUTNfGLgIicLjsAbB8aVDDfQkD1rQ2kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🪄
سوپرپاس‌گل دیشب نیمار در بازی سانتوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/103635" target="_blank">📅 08:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103634">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd29c5b4a.mp4?token=ShQ-qln8WfpMunHkfRLCLGpGqFh2tLjoBtZugTPM7G5PoeFyCIhZ5umZG1kvcIH8fRUNI4jRYv9u-q6Odte4OBlyRDfxDaDKEWmIAwVZaoEFpzrUn_8s_AtmOGvvoRexaH_ijXMmZugHXF91wlp1S12RdSQtrVk9QF18PE3sX0gtB-I-AVpTW3Xtx62gO51mzNDA36TI5UR_xn12-rXKFmD1s-vg_beWHab82KGW2_1ny7wWKjf2UQKpQaT-lSUlH_p8CD9_Ja0J4a6-32Cl7vhmEqE7DALLgbyAG1ixFUbltgCwbf40ejTnLgK4uVQ3-LY1XxsVLUPdmAHobC7ShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd29c5b4a.mp4?token=ShQ-qln8WfpMunHkfRLCLGpGqFh2tLjoBtZugTPM7G5PoeFyCIhZ5umZG1kvcIH8fRUNI4jRYv9u-q6Odte4OBlyRDfxDaDKEWmIAwVZaoEFpzrUn_8s_AtmOGvvoRexaH_ijXMmZugHXF91wlp1S12RdSQtrVk9QF18PE3sX0gtB-I-AVpTW3Xtx62gO51mzNDA36TI5UR_xn12-rXKFmD1s-vg_beWHab82KGW2_1ny7wWKjf2UQKpQaT-lSUlH_p8CD9_Ja0J4a6-32Cl7vhmEqE7DALLgbyAG1ixFUbltgCwbf40ejTnLgK4uVQ3-LY1XxsVLUPdmAHobC7ShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
پشت پرده تغییر رنگ موی رونالدو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/103634" target="_blank">📅 08:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103633">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFRmVeQGEeu4YxXz_mfSszq4zxbBpUUshEHz07f49TWoCO_MMtbybSdD50a1UrX0Otaitr-6nyOnLMTKZbnNSefHbBaG5hbGibmhPl81sw4D4lxyLoOQQLQtzbR0CBpepqDcJLoV4jUucqrug0TRyrKaBqfBJA1uViWqG4G-DmVqszX-PVSuafV19Ibf_46UEEdXY5Fs7lov6EuSElNMmRMaWdwylQnwEDeawc08yDvw4Fv_Oe1L1qpgubPdLi8a2IwH3fKqkbvp34X8e64fxlCoeissBcXSs6dv-oIYAK91cAdqKOBGyoMbU1IRJV74ueXqe6R_PY5X5ja_8wGgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
روزنامه کادناسر: خولیان آلوارز در جمع بازیکنان اتلتیکومادرید عذرخواهی کرده و اعلام داشته که ۱۰۰ درصد به قراردادش متعهده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103633" target="_blank">📅 02:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e844a831.mp4?token=rNcSA9dqbEksoguGQtq1yIzcVa9q70C9jcqPBmfxbhnCwwyrWui9ogjy0RGngNubV61-zVZbAcRiW2aQQkoUbvptDIPN8gRqMeBVU99Cucn9-pLN1GiwRtpBhAvkV0waOeB8fiFLL_cIACWWe8DnBH6-VIku0pDL0hjLox3H8qvru2b75FRi4W-_3H-c6jUmSMCIzH8_GwoAOV66rgxhLoW4867g0NPhO5atLB5JFNsGsA_1G1CIKAyxSHme9z_nO4Dwbt2VX0wZ1lJ1cQkzq2XCWXzeAvoP5w8gsuEWRmopjjxKumkSpoPFYz1fwRRLG2b-OFbnNRaWaW8zzdr8BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e844a831.mp4?token=rNcSA9dqbEksoguGQtq1yIzcVa9q70C9jcqPBmfxbhnCwwyrWui9ogjy0RGngNubV61-zVZbAcRiW2aQQkoUbvptDIPN8gRqMeBVU99Cucn9-pLN1GiwRtpBhAvkV0waOeB8fiFLL_cIACWWe8DnBH6-VIku0pDL0hjLox3H8qvru2b75FRi4W-_3H-c6jUmSMCIzH8_GwoAOV66rgxhLoW4867g0NPhO5atLB5JFNsGsA_1G1CIKAyxSHme9z_nO4Dwbt2VX0wZ1lJ1cQkzq2XCWXzeAvoP5w8gsuEWRmopjjxKumkSpoPFYz1fwRRLG2b-OFbnNRaWaW8zzdr8BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
جرارد رومرو ملقب به جرارد بنگی:
😳
😳
رودری تو هواپیما جفت جاسوس من نشسته بود
😐
بهش گفته که آره داداش این هفته توی سیتی قراره ویدیو خداحافظی بگیرم بعدشم بریم بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103632" target="_blank">📅 02:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103631">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری از جرارد رومرو:
🔻
رودری در هواپیما کنار یکی از دنبال‌کنندگان برنامه نشست و به او گفت که یک ویدیوی خداحافظی در منچستر ضبط خواهد کرد و سپس به بارسلونا پرواز می‌کند.  +بیشرف وسط هواپیما هم نفوذی داره لایو میگیره
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103631" target="_blank">📅 01:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103630">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-rpF1Njix9lqSCLLxpcz6t0xJ4hiEw6mDFGqLaW_N_uAZVJVYQ7Nq2AcW0b8zcONj4IxZ4j7yc8XdZCCzG3OHqE8MWon7XEhZGz3UVrDpGqsTxJfvmJoTLcYNSrf_NXKtpW0x62tE-RBoE9-g5HBybJ88MYyo0hjGODXQNDXeCVqCAkAavSceyG4LjxAm1GdjokYCAxgzS3CK5JFDUodEnoavAxtsTCXZrvIXfevTXqdYeX_Y_OpaL4eKz0kjTvSUo5kQkOqFf1Y54r_aHXXku6GZ18LI4nLmVJDe4aI-9GvoQad5pE6enspZmgqG9tmDbcGLWJl0avTlcbmjmkYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
رودری داره از مادرید برمیگرده منچستر  برای حضور در تمرینات تیمش از فردا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103630" target="_blank">📅 01:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103629">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2a0VT8TbBQhyLNGm6zvGORTNFPRyWHi-lGtNP-I4zKKykWeLyuVnokHWqr_ImJvpn7odA0Gq8a0mbkpGXBzIuUuXsIruxnFjawFSWZLEm2O3dbV7Qh2Xuc7Y_rfb_pDStnW595s3ihFAxgE9d35ZYk85_dn28UHE1hNC817MLK8dew4ATkKo8i1w0iUwDYtk5YsKdGB-MHR_I7hpWtPXm_trgfOH9PCadUjZdmILFz2qn0LIAk5zMi1CZ0AoP4bI64IGSYsy5qrwWMwHZzse1OwAk_Sqhl38TD2P-ZJWS7Z-b4p0g_IOg9f7W9_GdNyM5g4Gf5vJhYClmL1ke5Efg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🗞
#فوووووری
از اکیپ‌ فرانسه:
🔻
لیورپول در ده روز پایانی نقل‌وانتقالات با جدیت فراوان بدنبال تکمیل قرارداد بردلی‌بارکولا از پاریس خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103629" target="_blank">📅 01:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103628">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNf3rW8eErqt6z24Y14xOhAR5WBKFDpForDnpTZAUndWVXxNaGMJ9MowhkN1QHS-UxXJlBHcV19-ijfkvO2FGYIK9ksHqwhsmGbFg-3IczZm9lNQi3LqWp3dcZ5nmzTCEKtdAs56AP6zFp-WoG0kfqkUkARi4R4UDfuaUoPYmeZAkuYTdsswbd5R4tJJoIrqH5kcTFGPv8abmsNG2NUzoCEG5I8UofXiOUMw6x80qvVyd8_TjRE_ckvtAmDi6MVJOD7MbFQU3pD2zTJeZnk2XgnRleVU5512BCYUxyT6qPL9NafdenRF7LILIuCPSuatfgWGuPKruRIqkTar7Tua8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
رودری داره از مادرید برمیگرده منچستر  برای حضور در تمرینات تیمش از فردا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103628" target="_blank">📅 01:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103627">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEsRoVUfkmauCLgBHJ5P2-YePbjsg_NSntWcHSWUaaE2fO8szY-lS8ryLulH5YNUDWUWBagc64drFI3AGLKHRdJAYyElfCGkakLPi-hGvX6wbZZaw0oSF-pCueGpkfYba97EpGUV1Fgh3ni8MJ_Qa9m82217WW9fiqH3YTM_LtzuEn-1GMOJHDR0OwAIZxM6M27pyuM4kuuFyqoFlr74CqX9B2HJf5lmVIXo0EPOGsaXpbQ_jnJ3TvGKHs7yf8SkLbj4yZocWq5nyrRsmpw4c7Q47JINAYhkKo7rrKyVDpR340j0S5Y3kRtCZ1DhqvB78X-zKGwGLaQAPXTpskctdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
🇩🇪
شش سال پیش در چنین شبی...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103627" target="_blank">📅 00:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103626">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4393410638.mp4?token=SlPv-uYLW6tpXYvbIP2qI3mOEUm-gUmWBSBZtzswsIuZtT2Z6iM0SKpVkvv8YqZJN0bwtIlbH6gK3qKowHP6-zH0PLa49Tun00UYwpLI1S80Enh1N_KqQDivJbGTGTmi10rqA8igZTYjFnTjYcXZAbtpaTZhzB8cg4-WY8XINpFB6WhwqrfDRJrB2vdTPZZPP2OveuKj7MOLnDsPJIe4UZjEdsjFh1PbYe2TYy5ny8tc3yvRmiZsbeLikk6AptCRflBCl9UYp7XkQtJqEmZGfjdlwsyuRju0XqQtZB9mlkz5Zc9__iYfdBy7Ne3cHsEJhn7YpVBvofFbh6PPynjffg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4393410638.mp4?token=SlPv-uYLW6tpXYvbIP2qI3mOEUm-gUmWBSBZtzswsIuZtT2Z6iM0SKpVkvv8YqZJN0bwtIlbH6gK3qKowHP6-zH0PLa49Tun00UYwpLI1S80Enh1N_KqQDivJbGTGTmi10rqA8igZTYjFnTjYcXZAbtpaTZhzB8cg4-WY8XINpFB6WhwqrfDRJrB2vdTPZZPP2OveuKj7MOLnDsPJIe4UZjEdsjFh1PbYe2TYy5ny8tc3yvRmiZsbeLikk6AptCRflBCl9UYp7XkQtJqEmZGfjdlwsyuRju0XqQtZB9mlkz5Zc9__iYfdBy7Ne3cHsEJhn7YpVBvofFbh6PPynjffg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🤯
🤯
ویدیو خورشیدگرفتگی دیروز در اسپانیا که حداقل ۱۰ میلیون ویو خورده. واقعا پشم‌ریزونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103626" target="_blank">📅 00:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103625">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUJjRwfc3X7rMboykO2sR69KISQRxh0cmjV-O5ZFepjC0qYhuTIo2CkkOJ6oYNGFBMn3P0LxsFgGIgC8tegqAxFCpeVJEkmA6Xkx_rpHxPeVjROZaJTpDgYUGcHiYFTWsA7rS-Mz4CBA0yka25kNkXwQRiL8z6UZvgtEtY1e2OtATzjXd3Csk2zk48b2JvlZQgESSkWVMJ1KnqlF6iLzBu5UL8l7yWPOWyNAEamrws1U6Zv_hDCGjfh5RgkgmMDk3COB6JYcF0eAiuG2thE0Xi-sbF0A7L4pxI0PdSiXsBm3IKbMxkamd_eXcQTMYSOWqmACQES64xKUM86rrW4g9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎂
❤️
بهترین اپلیکیشن تاریخ، امروز ۱۳ ساله شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103625" target="_blank">📅 00:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103624">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvptbPh7rkUXHByFVA9IuYXFelX-BlOvnSD6bABPvjnswQdmUoCsAgRBF_0ClABCUfM8q73ng_Yw5dBgzGRuqv8j_S5FzdoCC0VpjZ6v-d_EONfKO6QeRESAXYCbAiWqPwaBjk8AmV4jEdvILujVyrkSA2_QMjhqVbvwBsucqpdAfh3mSsBYjK6azjkMD5RYu7_E1S00_q0Cl880wyUyFLZDJUuUyDQE3RCpbWNr-XNwnaPeP8MKe2tUFNc0PPhI17Q1FBorxFwg9fJa1XBa-BYdFMAa0TWh5syegeua1gcVGgmKiL83DQOkjf9PPYqkAjQDJXeGyCZmfJHb75k8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
🇮🇷
جدول پریمیرلیگ ایران در آخرین دوره‌ای که با حضور ۱۸ تیم برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103624" target="_blank">📅 00:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103623">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104964544.mp4?token=c3q9EGrzORIGi-c_LqoHVfyEJihVq__Mew_5lrYNOyLl39AQiKp2UJ1DeEAxxcsy1DVwfnOlhmnYPzsuyHA-NCEpZ7_gue9mg16lZ62d3z-bTrP4Jn_tLU4eMBDAVeRXEJ5fAR9HSqwC2zqs5NHYSDz-Cpvin-49UnXSBoS09_LT2Me4r3ka5n5QZhwQzGwvizdV3Q10WqBPuvcHQHG2KiEulP7PWqyePDFzBKF3SrPVrKOHyOHWz3Ft12OJEW3a9bNbiiie--5wo6052b_P8rFqv-isoAVgEE5Pu-4Zbt_QhqC4okk2ruYoWkVUJEVQbAHGhXoKt78cVZSl_L1nTozE3Y9Ph5S0bLlWWU5qByAYLLwEPXwsT8JdB_6llUUjiiJ150rCuUFNIqfUHhWFdBBR61wsrs4prN-ndmoVhIM556qjk7nphRf1y7O2qsLj9dujUuo0d4aRrHYRUbQGAG3R9NBBWE0SsXfDAkgQbLOK1W0rSOb4CtjOxno7fJz5lOJwIlfwUtarUj8Jqh_98lJRKDTK1FnP4GQkFWM_cUr8jb7VJsJWlgqHeGeaaVpmhW6vTK9T9lhFJ59Zo-QMOQboynnm9U8agnpxSYFTiNB-G1-SGMRfabplfXeL6JhLctjGYNkl2sd1UjmZWiEtsnvh_0FRUOKt3owqoqoG7ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104964544.mp4?token=c3q9EGrzORIGi-c_LqoHVfyEJihVq__Mew_5lrYNOyLl39AQiKp2UJ1DeEAxxcsy1DVwfnOlhmnYPzsuyHA-NCEpZ7_gue9mg16lZ62d3z-bTrP4Jn_tLU4eMBDAVeRXEJ5fAR9HSqwC2zqs5NHYSDz-Cpvin-49UnXSBoS09_LT2Me4r3ka5n5QZhwQzGwvizdV3Q10WqBPuvcHQHG2KiEulP7PWqyePDFzBKF3SrPVrKOHyOHWz3Ft12OJEW3a9bNbiiie--5wo6052b_P8rFqv-isoAVgEE5Pu-4Zbt_QhqC4okk2ruYoWkVUJEVQbAHGhXoKt78cVZSl_L1nTozE3Y9Ph5S0bLlWWU5qByAYLLwEPXwsT8JdB_6llUUjiiJ150rCuUFNIqfUHhWFdBBR61wsrs4prN-ndmoVhIM556qjk7nphRf1y7O2qsLj9dujUuo0d4aRrHYRUbQGAG3R9NBBWE0SsXfDAkgQbLOK1W0rSOb4CtjOxno7fJz5lOJwIlfwUtarUj8Jqh_98lJRKDTK1FnP4GQkFWM_cUr8jb7VJsJWlgqHeGeaaVpmhW6vTK9T9lhFJ59Zo-QMOQboynnm9U8agnpxSYFTiNB-G1-SGMRfabplfXeL6JhLctjGYNkl2sd1UjmZWiEtsnvh_0FRUOKt3owqoqoG7ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
‼️
⚠️
انتقادات تند رضا رشیدپور از شایعات افزایش قیمت بنزین در روزهای‌ آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103623" target="_blank">📅 00:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103622">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0689eacb78.mp4?token=gXikedu_OvzN6tBqHY8n6j2J08R7vPC5TttktOrNtggu6fQOJRaZ3tW398l3xRj5_NqhJemfimfconXrwxa8mnHfUu1PaVrebiiRpo0-fKSwoTREYoYw7uwx-pBetiQvsOViupDtgkMvN36b7clkZxtgqOtGq9zn13O85lKvzV8xgf_BhnguRqpsRt85MolW13dKfEy3s7QyspZRwoJPoDvH9lzj6ZYvUHfe6oo-hOUqjA0A07oUUaVwC4LIuEkADEBNQoyy7zw4NSC7YuejD_Hh_Qafixsy7NfGWn8X2594YTSZQPtj-FdmDa7NctM7Hrt9IxDy9LzuHkS42jZ8xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0689eacb78.mp4?token=gXikedu_OvzN6tBqHY8n6j2J08R7vPC5TttktOrNtggu6fQOJRaZ3tW398l3xRj5_NqhJemfimfconXrwxa8mnHfUu1PaVrebiiRpo0-fKSwoTREYoYw7uwx-pBetiQvsOViupDtgkMvN36b7clkZxtgqOtGq9zn13O85lKvzV8xgf_BhnguRqpsRt85MolW13dKfEy3s7QyspZRwoJPoDvH9lzj6ZYvUHfe6oo-hOUqjA0A07oUUaVwC4LIuEkADEBNQoyy7zw4NSC7YuejD_Hh_Qafixsy7NfGWn8X2594YTSZQPtj-FdmDa7NctM7Hrt9IxDy9LzuHkS42jZ8xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💍
🌟
تشویق اسطوره رونالدو در تمرین امشب النصر بمناسبت عقد و ازدواجش با خاله جورجینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103622" target="_blank">📅 00:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103621">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103621" target="_blank">📅 00:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103620">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=SS0cYK8UHYOAmhEyCB-PvsaXZnR3n7QFz0NeCB6tKJ3KZIibZL5muC_SkdHdv2IX5p2Au4VLJjbRQ_b6cwrIPktopno-ITcdlisvn_wQRMCFGDa1pNugouUEoJIQYZ54cYEMn3f8qFsC3XQFRjUOjePcLrXMgeiUzhT-4JQQG-p7bRHi6oJGEn5NPuCWXy3yT083EqW9Al3ePLIixfcXIkvYCngjW71Ipi-XY6Arv8-CDXlN_XfE5ThYanGOoXREO_WKv6a9P0eeliuyz3hn125kSKzNjYcd56JEz0qy1hBrYNeqdd6tpuIDJLcjabdQ8gr4k6OHjBUJVaoHnAWyRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=SS0cYK8UHYOAmhEyCB-PvsaXZnR3n7QFz0NeCB6tKJ3KZIibZL5muC_SkdHdv2IX5p2Au4VLJjbRQ_b6cwrIPktopno-ITcdlisvn_wQRMCFGDa1pNugouUEoJIQYZ54cYEMn3f8qFsC3XQFRjUOjePcLrXMgeiUzhT-4JQQG-p7bRHi6oJGEn5NPuCWXy3yT083EqW9Al3ePLIixfcXIkvYCngjW71Ipi-XY6Arv8-CDXlN_XfE5ThYanGOoXREO_WKv6a9P0eeliuyz3hn125kSKzNjYcd56JEz0qy1hBrYNeqdd6tpuIDJLcjabdQ8gr4k6OHjBUJVaoHnAWyRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a22
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103620" target="_blank">📅 00:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103619">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeyEOkQtmt9x7f1CnYGw7KGvSJnsve5uArDx5FlaSTkwUV_CzWitQnr8R6Ru5JRVzVyPrX0UmqHt6TW-JQxn7_Rr1AlaZj4J_Qg_m8b1yNvEb8fA0kCheW_qWqKSIEQOlOv6cgt2Xj5Zv71NPWXcscgx1T_S8WRupFFu0kZMHSUzv-TekNGGoJpMUWMen9NEXuM00sHIfEvkJ60GDtwkPXMquKfM4kOFxfS2o9I9xQIMMKuKSkHphk3pHdHOnYfIYZMlVSn_0CacCOYNIsIMnL3XJX_zvHM8xaTUR6e5Wt-ifCuBXtbdZx0a6dMuZrcS_-uX8DHevsXzwp8RjA3vyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
📊
فران تورِس در طول 5 سال حضور در بارسلونا در تمام مسابقات:
🏟️
201 مسابقه
؛
⚽️
64 گل
؛
👟
22 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103619" target="_blank">📅 23:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103618">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5dbVKEkf1njM_Rm1ihbJgI0wGSZhhT-NW3jAjW2EviAFRcv6yxystPlSIgtS5g5YDavexrCx9GYei_T8EV6N9FCQ_WbU34ldibrqfUqrGtldKUNzwkAXctCTnPqv4MqTHULi_YSSd_rp0K5LxrQ5pJr9apVM4x7aEy1-kLvxQIUnUNobUiJmQIymuOo3yEXI3sjti9TcPigNYc6YR21OwuSa5Y2-c5T5zqtTXKI5jUDWMeoQQsxlkc9SMqds8RVcjGalZZmp_gfpnroj7ZKEVQCfE47kvg1AuSKTeghMYO6I6kr9ckC_udE8yGPdYW-pY4yqIEuuVLZvE27MF-y0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری و #رسمیییییی
✅
🇮🇷
رونمایی از کیت‌ فصل‌آینده پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103618" target="_blank">📅 23:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103617">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
و
#رسمیییییی
✅
🇮🇷
رونمایی از کیت‌ فصل‌آینده پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103617" target="_blank">📅 23:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103616">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0NhnNmavj6wK0xyqkasuQTLwhmZVt8GFoZ5ULD5qZS9KWBbZUcR94h9Y-5FBKALCUBzihgiKttKjzVzeMPd98Gflcy6kiESHgImgOeYJiPq4kdVwEoeVGbo0vRFUiSTmyc-xqPX8kS4vvGbOLvE_ASJbxH2t74-R1QvSkuYd__GWnHLXEQjgT4eIwXE3uMlGGVsjb_ZALME3q3Iaye4TsFz0AGNtrS-eMtGvzmMr7aQJto54PtZOjpj76TlY_mLX08ePo_-MhTdC0A5DpLoro62CK96CZ_cutCWGlgMshjZVvZrvPhqClQSAdrwfCo4f-dbLEF7zrw_iYQPdgILLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
اسکای اسپورت؛ پیام رودری به منچسترسیتی:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
«دوست دارم برم، اما قبول دارم که اگه قیمت مناسب روی میز گذاشته نشه، در ۱۲ ماه آینده همهٔ توانم رو برای این باشگاه بذارم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103616" target="_blank">📅 23:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103615">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
😐
دولت جمهوری اسلامی درباره قیمت بنزین: سه تا راهکار وجود داره که یکیش اجرایی میشه
🔻
راهکار اول: قیمت افزایش نمیدیم ولی سهمیه مشخصی در روز میذاریم برای هر پمپ بنزین و اگر از حد مشخص عبور کرد، پمپ بنزین در ادامه همون روز تعطیل میشه
🔻
راهکار دوم: روزانه ۱۲۰ میلیون لیتر بنزین توزیع میکنیم با همون قیمت قبلی و مازاد مصرف رو به قیمت ۸۷۲۰۰ تومان می‌فروشیم دقیقا مشابه کاری که در کرمان قرار بود صورت بگیره!
🔻
راهکار سوم: چون ۴۷ درصد مردم ماشین ندارن، میتونیم سهمیه بنزین رو بجای خودروداران به همه مردم بدیم که بنظرمون عدالت رعایت میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103615" target="_blank">📅 23:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103614">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CK-buHU_q6_X9R9JGb_OJ2tFbDjvPuBfRLT7cbt3f-KIVqyhhpiddwIVeL_-_2m4I2voiums4S5Yc6i0_OEdmsBA_4Tu43r056hICkAbJGsYDVfOV9ko9JgAsecdT-SGlaNve8nkBS_Kyu9RMZD1dGV4S16DFuTFj3C_f1bE-OZUFP8FngrjcEyfuH4aZfcShc74z2d6hnCwbU1x8x1GXXwIsuGF0_IRSWNELJrSCgZ9r-4CpvarRvnhoiRCFuzoLPOfD7P_M3cBB0Lf-aFH7zAxfM2fug128GPkMblNvO-BrEkGc9bMWhRmwCEXBG2Ijjwxnb_FeqRiavXSxwXsww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
👀
9 سال پیش تو چنین روزی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103614" target="_blank">📅 23:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103613">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👀
لحظات فوتبالی که هرگز فراموش نمیشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103613" target="_blank">📅 22:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103612">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veCe8oCPnfBEyVUQFhZh8bzz6P3iLGiNchBShtmSFdD6M1KbJg8mPQEmxal1ZvpKkhqHaOPudG2LODb-0RPN3caHbNnKhRhFnrJrwInaSq6EQBk4IhqbTBlGFaQ0Q5ldTWGrUOstDZIzQAwJZLrtGY-Y_L9tMu39R0QHapK9iJTAvGaqp0VabG0436l2diN0gbb0DpjcOfhq94E5RrsZK83999h-8CQl6or67l8Gmb_Sh2UoXzrwWIawyZyQZsm8VJQTsAu2x9jN4MWtgadZxMrFp9pPX0HJs26L1_CX9Lsx6x8MJfRNE16FeOMJOiw7X-NuBZXZQsj6wqdfxEcrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
باشگاه‌هایی که از سال ۲۰۲۰ بیشترین درآمد رو از فروش بازیکن داشتن:
1️⃣
🇬🇧
چلسی: ۱.۰۸۴ میلیارد پوند
2️⃣
🇵🇹
بنفیکا: ۷۵۷ میلیون پوند
3️⃣
🇩🇪
لایپزیگ: ۷۰۶ میلیون پوند
4️⃣
🔵
آتالانتا: ۶۵۵ میلیون پوند
5️⃣
🇬🇧
استون ویلا: ۶۴۸ میلیون پوند
6️⃣
🔴
رن: ۶۲۵ میلیون پوند
7️⃣
🟠
ولوز: ۶۲۴ میلیون پوند
8️⃣
🇬🇧
منچسترسیتی: ۶۲۳ میلیون پوند
9️⃣
🇬🇧
برایتون: ۶۰۶ میلیون پوند
🔟
🇫🇷
پاری‌سن‌ژرمن: ۵۲۲ میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103612" target="_blank">📅 22:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103611">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_FgnRkBubrFXL83ZEUKLtW7PeCdb1swcQLu50zovqy1Hq6jQVXYao8sQ2zqbJdni3nbYWpKDd2NdSepesN2__Y8O32H-aKFaH_u_ohy-m3bV3LJDKDdid6HEnnsWEZrm1TCC279xO4gU8PV5T-M_hiwOAhfzCzyuakhScxNO-ra-DxYHkF3Gyx6edtAymPetjdLAVbSuJya4opmzE3zLbgifyCXZhv5gO2Pemv4ZvCHV8MZVK_D6TTRl1UULcgVfMHMEIu1Oq_LpfFvuBH7SdWTfxy_L-QTqNcceCvzZ42VoXJh4NEcKwHTN_BdlIQRt7jKzelbqx2W33eMivWA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ویکتور اوسیمن با وجود پیشنهاداتی که دریافت کرد، به طور قطعی در گالاتاسرای ادامه خواهد داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103611" target="_blank">📅 22:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103610">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIX8z-VOdM0Iba-faKwq0kODGaIsNp3-ZSLqcGlKlEaD4TWJIk5Zu_TvR2I2DQR68WNKPZK6gLAAmcMVkPqX45QmQjSdW4D1HDwxzfC3QPbQ_e5mjjxxchdtD_F4vO-9Ifkg2YNDsyGFuWtNdKD2rT5eZ1hi0DcJYhkyFlzjqKU_M1KpsWyfq-gwyZhvxcpBrbQR5IRyhrMGibILeIJrMMVwr3TCHiHJ3OFmKdTYPwWsAV1Ez8V38NfPdSRLAohz-3g0akrUz1iah0iHpSPHqhdGQuJCEijKls0EqCFOVGpfbGaF51CAEGIvoe-x7Au-p2DnCDGbVjgAktBn6EkMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
اسامی بزرگی که سرمربی‌ تیم‌های ملی شدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103610" target="_blank">📅 22:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103609">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEs7HPfd4ZHeK3AdleViGdLSDuI0OAHLzPX1pAQN4CNMspy14yHBB-ymTcrez3ZIlCxFHjy2jg5iidrjMa39aJyfZCDEOpjbFq-EvAr_vbi5jlmddiRL3rC57lHHFwd2FN7ano71Q1cSROU_StqDsaPR2KmMoq6ZjfYwyxTcQR4smaOzd8JGAYiRfiy_pOyYMIlNbfbyUkV4QyEBdXA6SOBfQtTkfY4dk1DUcMWzTNqINmnFnu28Qey8wsH1fAB0bDmbhMFcLV_m9LjYnr8SFef6rGfVz7TRUmcdC9acp7gM_UVvTqgrl3ANESWJdWZ5WaiKs3zMd0qUiyhHbmudfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاسمیرو:
از دیدن مسی تو رختکن سوپرایز شدیم، اون تعهد بالایی داره و برای همینه که اون اینقدر بازیکن بزرگیه، اون جزو بهترین هاس اگه نگیم بهترینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103609" target="_blank">📅 21:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103608">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
فوووری فابریزیو رومانو: فران تورس به پاری سن ژرمن هیر وی گووووو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103608" target="_blank">📅 21:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103607">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSH3sTW1Beae3P3kEkgxN4817pxFMBhjHtldFtjdv0bL32E2Huy3F_cJ2erRizvBHRHUdoGQfkwKKCpgSvhteDSraCKW1NeM2OcyDpt6yFPYIfB83fuDuwc0yHsKNm4lZh3bIh4NCt_mUDWy95LFZOzUP-_W4XVE2qTt-bE-RKNK8iNxEUYIDe--d5OE5UPRq9XDAfAZIt71Q-0du8K_mJNazRYKGMSGH4GTMwSNYsAJY-nH9pXp80W2SFmjxBnvWpVxkINuFoSJfT1-GuCvLt9hM0XKyk4wQH1s4HfvcxqUHsRZ2K6yH6R4KBZMMMvAWMtfsVNV1nUyy5ZJiCvnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووری فابریزیو رومانو:
فران تورس به پاری سن ژرمن هیر وی گووووو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103607" target="_blank">📅 21:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103606">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXBchBK8Dopk-Wu2oU__SN7IROp8LFlzoxF8I1fwhKuvxBSqaNahKsk-qfXRyN4Jryuac4QbD7_sRo8LNySjx3wZpnGrkfSCeGnAdhYpDiumtinXdl2wjsMlcs9frhxkrsP5_UQKx9hZzRnOpcvSS89Zzp_7WY3owBe7xHTWkUhvLrG5haxbjsxL8t2Ag_b7em9IcVhzKIY4OXdwqoOzUgdJAxwW1YB5JImLXAA6vrzUCTPLsKw2f2CqSuUdJoC40c-EgDMGblKxHE3tKfQuLukCcBj9bAPcx3vPV1ws7G1HsBGwJQUmcbSfbC-JDCP1KZiVe4Q7FhcEObocjKOjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مالکان تایلندی باشگاه لسترسیتی امیدوارند این باشگاه را با قیمتی بیش از 230 میلیون یورو بفروشند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103606" target="_blank">📅 21:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGKID7Fm-YOF5mKNkpEDG3ds479TFFYTdTl_YWg2PzBrYWFIGMKDQhw_9vV1179mMuY0o14wfvrUwKawgTZDnOw0qcH8IzqBMTjS1Tv9PUklr4a7598Fe2YaMACRuXh86cfDuBuEb8myDOR2piT-WRvmuAUIqxbEiMdzSFZfKTWd8DIgFDZHk4cRtPv1lhLSPFR7PiLCqC7T1Z0A9JmeVzzjBukO_Z02zVUTShV4ltbVC6YdyBoUMXnTqY_YnmkwO6VJR05ZBhDJ4gaMWiLbhWnLkcvw5jqLKnDazqM_HahoCyjFFtiLrx9Dk3nJ0rX3sfiehLvGBkX2GJGfgznjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد های هالند تو کتاب گینس
سریع‌ترین بازیکن تاریخ پرمیرلیگ با 100 گل در 111 بازی
رکورددار بیشترین گل در یک فصل لیگ برتر با 36 گل
بهترین گلزن تاریخ لیگ ملت‌ها با 19 گل و زننده 5 گل در یک بازی لیگ قهرمانان که رکورد این رقابت‌ها رو تکرار کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103605" target="_blank">📅 21:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103603">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awiGuGH5D6jgRPGOm-CULRu3JyfgreTDJo6mRtefA9micyLVUncVVoP9bljbLDfEy8VHaO35vfVAZwM_eVDZzfwhzGeDil6uZS_ywi7nNf_3f3H6KOI8S_xq97RY1TwyWqgVIvLLhiPmaStKVt6cVG-qzmQt89AIVz5-7E2okYIIpyeg1S1V8p4jhxGdV4_U_sYdZoP55JV09Aedu9-7oShvNpyv5KMht_S-Bx5eEzcKFGFRFgVJn_9EcP6iakCBCcLFVa1XI666z8EjFMoaP76NJXUXG_fyQ_iQ9xOj3KgVlUR3nTCvoyXMOoHLUHFZzzAd7W9wzwYxapw-5kX1ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5FE01qxwpmjzJfS9KjcInlr7NgCay7p-nwivi5wwauEEQCL81GpHARfGb5Fq4ZO76mm_uxym-ihnPUz7wMASvkh2LZeIAl_IP_1dU67DeGoFKN7XKYcxTf75_ghbO8LtGFZy0VJBJJZJ6IVTfd4BoR114BGZzuFZ676GFESmjptmk8x226jQDbplf3OwDv7NEQasXqOk4YY9_TnMLKad0xCvsWWyDYEyl45cqk7DHFQCVy4f2YtmA89_9BvWfdNTK124DKbETv837mbbsV4oxo0rZhXKzqaJY9yZVt0DtjXdMS8QEQze4eNFQPKWeEEjlrwp8OslPpYkmtPWmzA6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇨
مقامات اکوادور ۴۶۹ کیلوگرم کوکائین کشف و ضبط کردن که عکس ارلینگ هالند روی بسته‌ها چاپ شده بود!
گفته میشه ارزش این محموله در بازار اروپا بیش از ۱۷ میلیون یورو بوده! مقامات میگن قاچاقچی‌ها گاهی از عکس افراد معروف برای شناسایی محموله‌ها یا شبکه‌های مختلف استفاده می‌کنن. هالند هیچ ارتباطی با این ماجرا نداره و فقط از عکسش روی بسته‌بندی استفاده شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103603" target="_blank">📅 21:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103602">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
تاجرنیا و ماجرای ایجنت اندونگ
تاجرنیا در دوره مدیریت خود تا جایی که می‌توانست از ظرفیت محسن ابراهیمی، ایجنت اندونگ، برای حل پرونده‌های استقلال استفاده کرد؛ از کاهش مطالبات جنپو و نازون تا بستن پرونده زلیکیچ، آدان و منتظر محمد.
حالا اما به ابراهیمی اعلام شده که سهراب بختیاری‌زاده اعتقادی به اندونگ ندارد و استقلال او را نمی‌خواهد.
جالب اینکه تاجرنیا پیش‌تر مدعی بود با ایجنت‌ها کاری ندارد. گفته می‌شود اقدامات انجام‌شده در این مسیر حداقل ۵ میلیون دلار برای استقلال صرفه‌جویی داشته است.
کسی که استقلال را از بخشی از بحران بدهی و محرومیت‌ها خارج کرد، حالا کنار گذاشته شده؛ شاید زمان تلافی فرا رسیده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103602" target="_blank">📅 21:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103601">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys8NmE0DhzeUDgKL-xRgop4064PIsSIboe5-DvringKkxA2i2-G_uHeMJWlaC1LmeRVaj2jc_OJl5divw2Ja2CK6gSzjfplIw4lkJl6p5tZ2_4ZwMrWnlZPG3BWi0-j9Fy48AoIrx9Adox0ZX4VA-zjxKNiaHBkibaY-opQ3ua-DiYGTUUcTtl4NHEZ5vfmJQhMUqa7LteQRkc2MLySYbtQEdYIfEKc0tketNe3SD-YeVCiBa_ozbzBdMMbll0ETybk0vESdZMTaI5Pl863ki8BHD0UKmGzOg-7PZ_AUZrVXohfg-2Xj8AGtz8gPPhFd-XWuKFRyycD_ThRloSt5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از برخی منابع انگلیسی؛ دو تیم آرسنال و گالاتاسرای درحال مذاکره بر سر انتقال اوسیمن به لندن هستند. آرسنال حاضره بیشتر از ۱۲۰ میلیون یورو هزینه کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103601" target="_blank">📅 20:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103600">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ariA6oSJGmg8gwwA1eWu8jP6PfYRAU4qPFD_Xn43BZUlNKVCIB3-jsCcRfp8RoQlRrfeB-mSHWrLhJ8Go7J9GESORxBKynenuW5MeaNJwbk5cFFxwxGYkmUhPm1tgMEW72kd3sLIRjtgUHw71v9jGnSrvDsKLIrJKSf3Rb_0MYUA_veWT9oZxBzNHbzyJz1XmRnjd52If1dnq6tMg4GMzvl9-kke4PUXCWWVJ6m9GiGY98YNMnm96wmKAhPYi3lFd6n5tNtg2cld4xIrXxaMXNerzfY6V44lshDb3753eEuN-PjQA4GefvWBYQOWBVhXl_4inRUYyt7kJQ9vIY2BMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
🐐
رونالدو بعد مراسم عقدش با فیس و موهای جدید وارد کمپ تمرینی النصر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103600" target="_blank">📅 20:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dacd65c8d8.mp4?token=bOJ2zrDc8nCZBRux55lnKglk4VzePUiwom1SpuNz3syRvqU9rs3D97Gw8ClC05lrQjEtY0a1SAD7UYuZrw9mAGYXtEkMgLwu8yqXCczaiKUkg6HWWwPzhjTGBGBb6KjIFKyZd1YFIQCphPSYcHYBASQcSSD75jhkfiQtk7IH_lHXvLO493wSKtBCn1M0I6jvGTJ6elsexyt1Exwt8SDIXEwz2oKVn_Sfl32miqFgP45z2eJ-RS0uH5fQ-L978UBqgutCwlr8sY4mtxB2f0XUVe55CGlzNznYpIO6Swz44RPyi4UflXqV0u5wGUSot8373pEqARzYY6SXEtqzpPdbGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dacd65c8d8.mp4?token=bOJ2zrDc8nCZBRux55lnKglk4VzePUiwom1SpuNz3syRvqU9rs3D97Gw8ClC05lrQjEtY0a1SAD7UYuZrw9mAGYXtEkMgLwu8yqXCczaiKUkg6HWWwPzhjTGBGBb6KjIFKyZd1YFIQCphPSYcHYBASQcSSD75jhkfiQtk7IH_lHXvLO493wSKtBCn1M0I6jvGTJ6elsexyt1Exwt8SDIXEwz2oKVn_Sfl32miqFgP45z2eJ-RS0uH5fQ-L978UBqgutCwlr8sY4mtxB2f0XUVe55CGlzNznYpIO6Swz44RPyi4UflXqV0u5wGUSot8373pEqARzYY6SXEtqzpPdbGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
قدرت کریس‌رونالدو در فضای مجازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103599" target="_blank">📅 20:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103598">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00d2c02eec.mp4?token=PCqf8d84luvI_yWJBDX9zzHrLp6K-a2c6aNngyRrp9xGRIstqkk5aqAynAaAt5P5pIXfbmrlbJug49HwrmoJQSUUYEFJdPemUdPScQ3r2rvY41MSJ1DOIJqsSYoCcXhcFGCM6tDyOoI6F_LV1rHI4HN1x4sw9s4XnyNr4O8RfTCgPYaNNiM6smJ_HE9oVKefmhX88dleIhV2vO0YXRJjU37MZSThEwG2c_hppvklNNeqqUH1WMJVc7FSKkY9Q_5Gkc3Av763-tzhirj1a3QQzwui_2iyKXrn6M0X5QX8Xog9zoz3aYsliHH44fvK5vfyrUeIEUdzYBKUxxl1u_IfBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00d2c02eec.mp4?token=PCqf8d84luvI_yWJBDX9zzHrLp6K-a2c6aNngyRrp9xGRIstqkk5aqAynAaAt5P5pIXfbmrlbJug49HwrmoJQSUUYEFJdPemUdPScQ3r2rvY41MSJ1DOIJqsSYoCcXhcFGCM6tDyOoI6F_LV1rHI4HN1x4sw9s4XnyNr4O8RfTCgPYaNNiM6smJ_HE9oVKefmhX88dleIhV2vO0YXRJjU37MZSThEwG2c_hppvklNNeqqUH1WMJVc7FSKkY9Q_5Gkc3Av763-tzhirj1a3QQzwui_2iyKXrn6M0X5QX8Xog9zoz3aYsliHH44fvK5vfyrUeIEUdzYBKUxxl1u_IfBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به جا مونده از بازی پاریس- استون ویلا.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103598" target="_blank">📅 20:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103597">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxogK9sgjOMcLDMARHGcGyzpjzoBxOo-_13S0p0HzjCuUcPdzzU9kAHt5Vyy0teoLIAWs_uMYsDYecQGalMBzDmUpqua4wqPxfIxxjecbzrm6nV9S1vuyNtrSZTVAeqVtV26nBjR-5wPSTsgXJ93BcGRAjjfAck5-tl7IB25bj8_gEOIzI3xOWCKMBYEMDi8x47mavmhs8yv9L2v1JORJ399j2lF2La7QNux1uNoFy8FQQtxaFs4vipPCd9Kw19e4cUMqc9u7QZ4BciV5OZHrT0WuNx3i1F21nsd-KapNkA6dKhL4DRboO5q_qFkBT0YRnJhlW5WC24GqKpHSH3NBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدارهای مهم روز جمعه ۲۳ مرداد
🔥
آغاز فصل جدید لیگ برتر خلیج فارس
💥
بیشتر از ۴۰۰ آپشن پیش بینی برای هر بازی
✔️
شارژ حساب از طریق کارت بانکی،ووچر و ارزدیجیتال
✔️
۱۰۰٪ بونوس رایگان اولین واریز
✔️
امکان فروش شرط های خود
✔️
تسویه حساب بسیار سریع و بدون معطلی
⚡️
همین حالا ثبت‌ نام کنید و و از بونوس‌های ویژهٔ بتگرام بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103597" target="_blank">📅 20:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103596">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3xrv8YhSmCflq36qoaykMgqtVzE0_EJ3AlFPwRJWwp_LRN8KQVny4azWJayQo34pC8H8sGnxphoj27s1AcX95VoFdy7j4WX37nxiTeejQ2J4OB5e8djwZ2dE76oxUpNdDrDNDdYycLNkQpPGrDvGEsrL_fkv-N6C1wDd2W-I7rQIPzoOKvma6Oti5-UyBk9vKugXY005HvHyyuo-5wkPe2Xlw0yVMoT3E4KOHNZwxLaymbFRF4WGRgZrFjKAhYe0NxalwMnAfzuHxuJ8DgQ_rOrPIZJnm9AVsA731TqEgCmRhto3h38N-Xj1_EsZXF5rOwJH-K9HcXp-DsbGFUoqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لیگ قهرمانان اروپا (می)
🏆
جام جهانی (جولای)
🏆
سوپرجام اروپا (آگوست)
یه تابستون فراموش‌نشدنی برای فابیان روییز.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103596" target="_blank">📅 20:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103595">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyZ-9Cb-Nb547yRaLHQsfux_H9guNt0gxERNVqmKMoGVGr9pur7AqvoPGnfMN8lie9qxg7hfys1copvSG75Y3-vHLHiS4hrcXUqYTZEFspedAVaYdl_PEQw58oFbiPnqazRnKCN1dvrqn5ioRXfuSWjEGe_gV7tttKbvQ6wNZoWPq9vc1wY8kIYeb27UqCyv97UqK9cqJmi5C9wHPzkQcQu0-wQXe1yNbNaE3ZIXyv-bUWI9TL9IP24lk3aw6AS1FNVKt2Q8yAMqtDo1BqcfUxOBrdvaNJm3IxWlxViwFNWxNNsKiBGLX0wmzfzXl1_Qp0UhnH9C2cTLoBEMYBl9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
توماس مولر درباره کریستیانو رونالدو:
من آدم منظمی هستم، اما چیزی که کریستیانو داره یه چیز دیگه‌ست. همیشه خودم رو فردی منظم و باانضباط می‌دونستم، ولی وقتی به رونالدو فکر میکنم، می‌بینم چند سطح بالاتره. من تمرین میکنم، مراقب خودم هستم و کارهایی که لازمه رو انجام میدم، اما انضباط کریستیانو تقریبا غیرانسانیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103595" target="_blank">📅 20:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103594">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_XvbbQ9DJyetPNHuBjw4KhNOXTvcHN8_5f76goEHL0wco5gXFryICBaratv4DLVz8ey9hCZ8lZg_In2PBFhng4ATY6U_2-_8ypY1h6XtFtq-jBcnQrnGORE2RPscGK6junqUC8HwPatyrA_RPf8MknS7JROwysXrzWBv49gof4visUsyglM2TfE3Wuu31-spLDpA71yV6Ube5gUvl3sz29NG187zxeU4wyRcmVsCNM-UIdVSjsdOE2v7u46UyejaL0MRwA0OfkCDyjzZBXggk0mNNySuMyOS0w4mT9JdQR799sK1IrsuVrIpLjzBCDTHXcWTCTs_2cLsmxHS_oE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🗞
#فوووووری
از رومانو؛ تیجانی‌ریندرز از سیتی به القادسیه عربستان مبلغ 61 میلیون یورو
HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103594" target="_blank">📅 20:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103593">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇮🇷
رونمایی‌ از کیت‌اول باشگاه‌استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103593" target="_blank">📅 20:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103592">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn8nuzKhartRyy2JZ9QDIf6VYgrUNrf4TCbPSVl3W9p4OXSN1g5DEhi9zxgb36csnnqZJXVZITQpJELnpUS2JUFKOnqeXx1KjnFsdZwVVWlcFXblPvq6-CgPdXfZWzEE0ANkaPZtsvPKs0G5GWUXVgp4ZzABRrWxsbRQhZSyx1lC2ShWQ5hzYoM-zKxJ6nox84qfDiW2-P1HLjeFYC9UdqF_Eo_cGaxeOuBYuWLQt4ycLMkjDS3D8d-xGlTrptfFMZIyjasO1Zv8og_5Yrec5VLlHy4Hcr_hdZhEdWV2TKh_3Im9ceR2yp0R5_uage5X0qFb7g9ShFlNacqBUolhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
164 بازی.
🔺
168 گل.
🔺
49 پاس گل.
🔺
19 هتریک.
کریس رونالدو زیر نظر مورینیو.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103592" target="_blank">📅 20:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103591">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KidbM0J9Y2b9GXZ22gfl-ppNCwgOcJF0cnr4aTld3ubv3hpDQMB2vzl4WCI-853IoUnBkBpxKdCYpIhB2RdnUZ4oLlNReAlFsZy-zlN0KTMmqUGI3X2naloCfed3QeZN5L6Nd7Z6gG-_CH7Fjld8Dk3R6FpBjg29-TbnHUEyzMRJ_caSURjy2LI-urRfmgZ4S3kifYcPMIHAgJa4dtynYXTBULTLLHHzOddIVLYpenf9DfnAzE6h6XYkTrx09HZFIMK_HrOPKw1vYPZrSoA1it2oAFcRleMeeNX3g9x8lUqh5Uo5VnuapIe0N7PyjHzZOEd3qzQoRXq_OneQPNEvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👀
اتلتیکو مادرید تنها تیمیه که از سال ۲۰۱۰ به بعد، به‌عنوان قهرمان لیگ اروپا تونسته سوپرجام اروپا رو ببره. جالب‌تر اینکه این کار رو ۳ بار انجام داده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103591" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103590">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897693b97b.mp4?token=n8GDDxrf9FOiLzFljwNQ6wWHfUkXjbHBY3xsgr3JRKclHvDiRWaXWZMQZ6dKHa_GzUbshYWxaMugFbEGgaB8e_Y-422Q5VCmlQG9q27CLFnSrS9H2h6o9_Z9yl_PMEtA5aYc5ef2DlknNUaFmf22GAcy97ipIltYATB7b7Qlj7qXi2b1VrzZS0QK_o-lvF_6cDve2wmwBPm8ioGUmgyhA3DAkigra3MJmmjeUfN3EW1BdkwBVofgu4ZMcnAatGFsLOu4_NLZ73FpFbIB8QzHurmfvhYBDiatcoaUvbPqf-x9X8RMQ9u5IJPxLVZvK4dbwqgO3rb1dLobLiLVf_4VNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897693b97b.mp4?token=n8GDDxrf9FOiLzFljwNQ6wWHfUkXjbHBY3xsgr3JRKclHvDiRWaXWZMQZ6dKHa_GzUbshYWxaMugFbEGgaB8e_Y-422Q5VCmlQG9q27CLFnSrS9H2h6o9_Z9yl_PMEtA5aYc5ef2DlknNUaFmf22GAcy97ipIltYATB7b7Qlj7qXi2b1VrzZS0QK_o-lvF_6cDve2wmwBPm8ioGUmgyhA3DAkigra3MJmmjeUfN3EW1BdkwBVofgu4ZMcnAatGFsLOu4_NLZ73FpFbIB8QzHurmfvhYBDiatcoaUvbPqf-x9X8RMQ9u5IJPxLVZvK4dbwqgO3rb1dLobLiLVf_4VNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آنخل دی‌ماریا ورژن رئال‌مادرید؛ یکی از بهترین وینگر ها و چپ‌پا‌های تاریخ فوتبال جهان...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103590" target="_blank">📅 19:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103589">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1dd51b6b.mp4?token=c9JpoBTlG3zhuZYtR-IAGjFSvd84cN0bPbzAHm69d33uyunKYo8Tu2mYq47WrlAZTOIPMI_XNvd5HcDzsexGxmUJL9cbVfwmbNgNihGvnQDeqklSdB55t-X9qGCg-VuMgi_83eNpW2md-YVU3M1KGQdd5Fm08GYJieA5L0gVUlV7vfbz_h3cJnEaWOrvo5hKyioEZJk2pTSFroRMC0NWneFoZuHU58FQikcduD-b3G6RQfQZbEWuI_JKik1sOdFI5u9UwvO9n4tDFfxUgX7YEmRKORtAPqOvgo80KyoIuqwjaEhYA4vUUHdQnoMs2AuPanUSm4Zs98z0GO8O1Jh3Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1dd51b6b.mp4?token=c9JpoBTlG3zhuZYtR-IAGjFSvd84cN0bPbzAHm69d33uyunKYo8Tu2mYq47WrlAZTOIPMI_XNvd5HcDzsexGxmUJL9cbVfwmbNgNihGvnQDeqklSdB55t-X9qGCg-VuMgi_83eNpW2md-YVU3M1KGQdd5Fm08GYJieA5L0gVUlV7vfbz_h3cJnEaWOrvo5hKyioEZJk2pTSFroRMC0NWneFoZuHU58FQikcduD-b3G6RQfQZbEWuI_JKik1sOdFI5u9UwvO9n4tDFfxUgX7YEmRKORtAPqOvgo80KyoIuqwjaEhYA4vUUHdQnoMs2AuPanUSm4Zs98z0GO8O1Jh3Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مالک مروژ: ۸۰ درصد دوبنده‌های کشتی جهان را بچه‌ های اندیمشک تولید می‌کنند. ما از نایک عبور کردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103589" target="_blank">📅 19:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103588">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c064e81c06.mp4?token=Y3dS0fhIkYkIdKXtV0b0cDMdI6zmHTWwcWwOhZe2wK_7I0-PQb-QIfZ9NUlvM4s2s9YBT2MgpWH5pzy_S2RpNHyGgZiZIEfqQ1q242wql8ZIlIAsmPavCSnt0H_z-wi10Ray_qyqnv-Gyl0UeR1JF2evzEJKCXMkQ8ZZzHNjprgI0AlwbWy0t_K6_x1hQWy3_mtnaOVvJGNI1mOOOhNMiKb1fAPK5bJFmkfOJZrgN-9TSlPuahC9b2A9xvSymRmNdpdwblugVL-lqhApQ4e_i_uNp2yIEOkEHzd_g8_HJfJ11G4oxwJRxSPZubyPKVSZ6WG3mVjaYNM48oEHSA3wqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c064e81c06.mp4?token=Y3dS0fhIkYkIdKXtV0b0cDMdI6zmHTWwcWwOhZe2wK_7I0-PQb-QIfZ9NUlvM4s2s9YBT2MgpWH5pzy_S2RpNHyGgZiZIEfqQ1q242wql8ZIlIAsmPavCSnt0H_z-wi10Ray_qyqnv-Gyl0UeR1JF2evzEJKCXMkQ8ZZzHNjprgI0AlwbWy0t_K6_x1hQWy3_mtnaOVvJGNI1mOOOhNMiKb1fAPK5bJFmkfOJZrgN-9TSlPuahC9b2A9xvSymRmNdpdwblugVL-lqhApQ4e_i_uNp2yIEOkEHzd_g8_HJfJ11G4oxwJRxSPZubyPKVSZ6WG3mVjaYNM48oEHSA3wqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس یایسله در نخستین نشست خبری خود به عنوان سرمربی جدید نیوکاسل، پیش از پاسخ به سؤالات، با تمامی خبرنگاران و حاضران در جلسه به‌طور جداگانه احوال‌پرسی کرد و از حضورشان قدردانی نمود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103588" target="_blank">📅 18:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103587">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coWat84AJVVuto3mgd0dJZCkcPPHp2KtXgcBy8MHtqNlvWaDJ3mOgd2uolu1w9-JkGI6WVgfomDIHd5pqQe1QO1SjRHDlmAGnM-KpFQRLB9KDOZhf-_HWxgZCbHaYv0fhX0gE5sAvNhg9LNdl_i4e_bvIFQNeBeWMNdaOJmZbWuxxW9tZ8aVoo62JhJEhk4sDx8r19uAQSfTtvHuZi0bnb7PIWBg2D_FTjKPhNeKXb-vM9HkQurx3GOsWYImJPMbH9o4oaz8376h8Df9wcoMRguMQTlVNoK2lb4LTxTYSVZ-DuCJgsUThzVbotL3mqTzO1eX7CUVWmY0fd2DXIB7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر سیتی پیشنهادی به ارزش ۱۲۰ میلیون یورو برای جذب انزو فرناندز ارائه کرده است.
📣
سزار لوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103587" target="_blank">📅 17:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103586">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5264b04fbb.mp4?token=Teh0DVBi3jO9FC6rMo7FffEtNzYX55UOgTa7p6QcaiCtGPAxegACEe3x6pfarO55iVVw-BXVgZ2gyQdtomr-cykoaYmldJ-N6xY8VcwOY76Dthw8GTdaq31pH69A0tMZizA9mNQCRMxcrJq2akOOea57u7GhrAbqJv13wsN1oHLGzFenXZikdLYkpFZGcVEQEknBYF0clYu3YWCG-Fz3ndpRDePoVpeBqa9YeVgqK897UWwIvmYG9VWWIeyO3k0xjylUEJni9a56srCPx0hwDGG0eGZwnpC-a0zeJ5EQqeeAPecmF6oswWwxJP9qjlNugRiUJt2OLcxxJBZmQQQ8Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5264b04fbb.mp4?token=Teh0DVBi3jO9FC6rMo7FffEtNzYX55UOgTa7p6QcaiCtGPAxegACEe3x6pfarO55iVVw-BXVgZ2gyQdtomr-cykoaYmldJ-N6xY8VcwOY76Dthw8GTdaq31pH69A0tMZizA9mNQCRMxcrJq2akOOea57u7GhrAbqJv13wsN1oHLGzFenXZikdLYkpFZGcVEQEknBYF0clYu3YWCG-Fz3ndpRDePoVpeBqa9YeVgqK897UWwIvmYG9VWWIeyO3k0xjylUEJni9a56srCPx0hwDGG0eGZwnpC-a0zeJ5EQqeeAPecmF6oswWwxJP9qjlNugRiUJt2OLcxxJBZmQQQ8Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
عشق‌وحال هواداران فنرباغچه از دیدن لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103586" target="_blank">📅 17:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103585">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/103585" target="_blank">📅 17:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103584">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9gtW9RtHGCe_a4nWrieobIIuOoEPZIuaK6g8SfE7qkb7T_I-I9A8Q4_l4u8Dx0U6HER0BpTMTzi9QcK-MUeidN8QVVc4K78Wr6BdgsQ2OWRhgWgTQrEYv7qOlcUjIOaxpxqzF698giqJbVzSrs3kWE9vUOCv1tAW_vkDkfj_zWbp5xBuuOSHMAPq_-EQDebLjemyepyZtmUjBsBESb4-uGFaZ753PPeTP-i8FuFqh8zC5TCzS6gjXBQ94JgoC5vtDdamn79NzemhH723RKRPtA-gw7ZDjPwmMwaEsbnQFp4_za2vVIPxhLmzaJuCsa6R_Q0BHgJsCLNIjiMNqkeew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g22
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103584" target="_blank">📅 17:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103583">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر سیتی پیشنهادی به ارزش ۱۲۰ میلیون یورو برای جذب انزو فرناندز ارائه کرده است.
📣
سزار لوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103583" target="_blank">📅 17:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103582">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5eb10d932.mp4?token=oOK_GldBr3BMO5wlHc4V2777XQm0zEjEXqaNTwhNw7CKeQ5AazGsyLu6FiRDZnyN7q6YDWh4Qbytm9Qir8nkY2wAUK4B-9LW8ubptU-pNZWnEJ7QV5S59bV4dUIET6Zgj0BkSUVmdVsLkcUeyUHOFZmjFmXkGaw8WT2ChPU33J4VHPHiBt8VB5LoU83xfr-OPkcHlzZFdI2OTIERlmUx9wppo8ZjZWog_oasLWBVwhftR5NcLW0jLzYGaU-LgyctlgNytk_Z3y03kQAmscko8Bu3s55ju_q7_jzex2PR3GvJn00KR7HI7t-D_d1ZLhv3ZDWbaeMybhKq2Rhgm2t4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5eb10d932.mp4?token=oOK_GldBr3BMO5wlHc4V2777XQm0zEjEXqaNTwhNw7CKeQ5AazGsyLu6FiRDZnyN7q6YDWh4Qbytm9Qir8nkY2wAUK4B-9LW8ubptU-pNZWnEJ7QV5S59bV4dUIET6Zgj0BkSUVmdVsLkcUeyUHOFZmjFmXkGaw8WT2ChPU33J4VHPHiBt8VB5LoU83xfr-OPkcHlzZFdI2OTIERlmUx9wppo8ZjZWog_oasLWBVwhftR5NcLW0jLzYGaU-LgyctlgNytk_Z3y03kQAmscko8Bu3s55ju_q7_jzex2PR3GvJn00KR7HI7t-D_d1ZLhv3ZDWbaeMybhKq2Rhgm2t4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ویدیو کنایه‌آمیز رسانه رسمی باشگاه تراکتور به استقلال: اولین بازی آخرین قهرمان لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103582" target="_blank">📅 17:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103581">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6yUD-BJ_dLVxln3USO3-sfGxpczMUs1GdcyaBLuC4XFD54UyeaO9KeV3rMMEWOLsZypu6Foe5WmrEghwAYfiWRuLp-wLVXFkPpM6kHqQoOfDQdnJYeDxon_F6aiId_fyM5Jx_XDoNRC2zpPpdIwWuNi_v1EK5KhotKZs_ST0bLzTKLa59N7vG5-HardhNKbF1XuD_79RsSqxAfH6QcAuxQYGjxo7C6twmBvPfXDgoAXcZgX_0_dGPld5LOfQIB9QuebsqjuupJRLSd37XVVFSNfrfhD3Au4NDKk0UVVEEZr2aBN1LW95YH5DocuZQr9cMNLBTgKDOi5RIj52FeixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پاری سن ژرمن پس از جدایی امباپه، 10 جام از 12 جام ممکن رو کسب کرده در حالیکه 4 تاش جام اروپایی بوده. ولی شرایط برای رئال مادرید کاملا متفاوت بوده؛ اونا پس از پیوستن امباپه، فقط 2 جام از 11 جام ممکن رو کسب کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/103581" target="_blank">📅 17:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103580">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRAXBPdpOFAkEgka2hdKV33x_Zw2VcpPo1ATUhaiyHny9hsRhF72N9KQWVWRvYItzxZkGfOswnuwJJb0h0euZLfjdr5RRhfigLyPmQLcm0-ke8Eh5cl4KWB4irTdISz0TA44CU4VtNWrJ-tD9rlpusDT1Po6IlADIUJESWgHUZb8bvNvjImbIS6vcIxlJ-OdfrEcIjc_I2A6lUFg7yBsvxJBMsBX3X0s0T5G2AiRV6T7fTsmFs1s0_Y3ie5Q42NWGz28K-QynWdikyDNkDuxX3OvQsvcsMmNNXNFBet7ZxCL-Vgj4wt8jwrrOK5nVBZS2aZaubigvO_igphonhpang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✅
دریا بنگر، دختر محسن بنگر کاپیتان سابق پرسپولیس و سپاهان هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103580" target="_blank">📅 17:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103579">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
جرارد رومرو:
خولیان آلوارز همچنان با خشم و عصبانیت شدید به تمریناتش ادامه میده.
باید منتظر بمونیم و ببینیم بعد از بازگشت خیل مارین به مادرید چه اتفاقی می‌افته.
اما حس و حال کلی در مورد سانجام معامله خولیان اصلاً خوب نیست و کاملاً منفیه
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103579" target="_blank">📅 17:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103578">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6c2af722.mp4?token=WGyLWZzSbAr6jWM0zbmmgthJODs5w-8jeGshu973r8A8h6ntR58ddhwMqJGEqb32yO9mz9hKPbdtg4e8kE8dEzH8yud2LyI-l-8l6ftedxOzKQ4k1FPk3ZJKeqJW_x6DhNmEkvY8YJgEZWI6do5G4f1y4K3y7aPeIU3dilZ0-16etUHgKp_b5Ok5bCD0Rpmjf7FLG26QsC8If_idsy8lO08be0d4bkYgdWyjgDcbuuusHruQKQKhe_qZ8-gtuiu-fP7mKt3tdrecXXCpo-zPq1ZnDqQoOFLuI-yj0Urn3Ra7vUmYoyUBHaKOmv3EtIzvRKwE7Eb6a-DaVMefRt1UqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6c2af722.mp4?token=WGyLWZzSbAr6jWM0zbmmgthJODs5w-8jeGshu973r8A8h6ntR58ddhwMqJGEqb32yO9mz9hKPbdtg4e8kE8dEzH8yud2LyI-l-8l6ftedxOzKQ4k1FPk3ZJKeqJW_x6DhNmEkvY8YJgEZWI6do5G4f1y4K3y7aPeIU3dilZ0-16etUHgKp_b5Ok5bCD0Rpmjf7FLG26QsC8If_idsy8lO08be0d4bkYgdWyjgDcbuuusHruQKQKhe_qZ8-gtuiu-fP7mKt3tdrecXXCpo-zPq1ZnDqQoOFLuI-yj0Urn3Ra7vUmYoyUBHaKOmv3EtIzvRKwE7Eb6a-DaVMefRt1UqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عجایب سوپرلیگ کشور ونزوئلا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103578" target="_blank">📅 17:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103577">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
📊
🎙
🇮🇷
جواد
نکونام: یکی از تاکتیک‌هایم امسال هواداران تراکتور هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103577" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103576">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cdfdeee34.mp4?token=O6eTBMyCTcNn5fiTAOZ9Zrs5t9z4_SgswcfxVqNsTRAtSmFZApUG1pDf8OM0VfuSFqQD3v4Up4s1g5RZQcWw5OFSkUHCN2qwEq3ZpvwywdgzGvz8vzmuzbVqjkyZIcShsMyotpwlz_jibkX7FKCR_etupZPRBUAmyiLqErQ2eh-ZkUFIi9qLN-7J9qiPE9OEh6W5_ed3wCUfZj1oMeJfm62rZts5Byi4aIoxlQbSVeyFC2nlZmWEiq4--lmKqJqxgZjkdG6adDly5PArl21jlHGCQ1_GFgLMKSPy5YNT4CxTpUGmV15_ctrlIlhpy1LnxjcefRyXiKCkiGV3iu2h0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cdfdeee34.mp4?token=O6eTBMyCTcNn5fiTAOZ9Zrs5t9z4_SgswcfxVqNsTRAtSmFZApUG1pDf8OM0VfuSFqQD3v4Up4s1g5RZQcWw5OFSkUHCN2qwEq3ZpvwywdgzGvz8vzmuzbVqjkyZIcShsMyotpwlz_jibkX7FKCR_etupZPRBUAmyiLqErQ2eh-ZkUFIi9qLN-7J9qiPE9OEh6W5_ed3wCUfZj1oMeJfm62rZts5Byi4aIoxlQbSVeyFC2nlZmWEiq4--lmKqJqxgZjkdG6adDly5PArl21jlHGCQ1_GFgLMKSPy5YNT4CxTpUGmV15_ctrlIlhpy1LnxjcefRyXiKCkiGV3iu2h0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
زلنسکی رئیس جمهور اوکراین بالاخره دست به کار فیزیکی زد. ابتدا تمرین پرس سینه انجام داد و بعد تیراندازی با کمان را امتحان کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103576" target="_blank">📅 16:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103575">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_665OgA92-EOuDoZlB-uQsL1Vn0A_1ytbahjqZpFczFpfVIQQWr5B4yagdvvvSVELzqImRU6AN8xmb8njumz_hgb4G_f5pXfpU_8kataM45JbzXzBbc93BPlGFJMSFScOgr7-C0DU_4vAhA3NKSivC3V06cYxZsdTLgX6vUHlWHnd6n8MgL54udpGf-2mXHX46yq0F7bhM7fRm57OqU0HNCKiNpQVHWl0HXj1lzxzLw6jaEdZz0bCCvckgOY7ethkYjnZhp2kuhexI6mZRnb3TxN60GiVvUZdwoXtUKKanOmPEtlh3IKjrxkmXQthfuCXaDL9dvUr_TKCpXBQaSSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
پائو
کوبارسی ستاره بارسلونا برنده جایزه پسر طلایی فصل 2025/26 شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103575" target="_blank">📅 16:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103574">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef89e7942.mp4?token=usAxkEXiI1KQJjmEdInXNFbl3w3dTo8EuYqaSz91czt7iBmHBbNTqVb5YP9kPi2xHHBbO3ws-GwxlodOuKDoEobpXnq6_BogVisKgVi-bH0sOap1D9lV4QvvBTxoU-XQIUIg3ujw-gnm8pziJJ9-Xn4jQFqvwS0XlaaTnS7ZWR_4rKikqgvAN0cW-CGCY_RHdS6NHD5IQB-MVazoi9-B6UR-BxlqqvVZxaXy8utiM1QiPWP4S8b-LNRkkd-rEhPKuLs5ogiR6ASAPGvtKQKb8uOIq0aVTWQjH3Tt8LvDqNOU5jGEXdHvJh1Is7kgVuk0KL8d63mXKxBR3nK2a_wNaYdflYmTlz2hMk-QVLns9CScEJFHs1TksqY47qwssEc0-g5xbAVq-N-ZLCRrXyJu2HBOqW9MAj8n8lz9ombT9p7MeC9isYve1D6P5YB0x4t--aw1sAWwu1-aDYZ5HzS-UxUHSGvADr8VFgprWVzN02GtuVQiATPBrx904KF8FfRUYbkWqTXNVW7sGoatV_M5jaIPMLb9djtSIztdkwPfSce5ZSJ0jWokthSxaGj58LCfyzwv4-vJbPxs_vs3kgZZWlz1hxzk5jZFP0-htacn_P4s2z_DLR90YTeprhck-k2JXQJt7VwoOwZ9P4SrXv_cludQkBHArRsURpWkLCJnUfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef89e7942.mp4?token=usAxkEXiI1KQJjmEdInXNFbl3w3dTo8EuYqaSz91czt7iBmHBbNTqVb5YP9kPi2xHHBbO3ws-GwxlodOuKDoEobpXnq6_BogVisKgVi-bH0sOap1D9lV4QvvBTxoU-XQIUIg3ujw-gnm8pziJJ9-Xn4jQFqvwS0XlaaTnS7ZWR_4rKikqgvAN0cW-CGCY_RHdS6NHD5IQB-MVazoi9-B6UR-BxlqqvVZxaXy8utiM1QiPWP4S8b-LNRkkd-rEhPKuLs5ogiR6ASAPGvtKQKb8uOIq0aVTWQjH3Tt8LvDqNOU5jGEXdHvJh1Is7kgVuk0KL8d63mXKxBR3nK2a_wNaYdflYmTlz2hMk-QVLns9CScEJFHs1TksqY47qwssEc0-g5xbAVq-N-ZLCRrXyJu2HBOqW9MAj8n8lz9ombT9p7MeC9isYve1D6P5YB0x4t--aw1sAWwu1-aDYZ5HzS-UxUHSGvADr8VFgprWVzN02GtuVQiATPBrx904KF8FfRUYbkWqTXNVW7sGoatV_M5jaIPMLb9djtSIztdkwPfSce5ZSJ0jWokthSxaGj58LCfyzwv4-vJbPxs_vs3kgZZWlz1hxzk5jZFP0-htacn_P4s2z_DLR90YTeprhck-k2JXQJt7VwoOwZ9P4SrXv_cludQkBHArRsURpWkLCJnUfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
آخرین حضور اسطوره اوسین‌بولت در‌ المپیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103574" target="_blank">📅 16:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103573">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">📌
فقط ۲۴ ساعت عضویت رایگان باز شده از همین امشب چک کن ببین چجوری میشه پول دراورد
💵
💸
🛒
این فرصت محدود رو از دست ندید
https://t.me/+MT03hkV78q9kMTc0</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103573" target="_blank">📅 16:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103572">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0106cebdea.mp4?token=qeDyZ9t4OPAP0PUQ3HwAnvjnqix8vnj5SFNfDSYA2ul88EuTeNM86g40dGI64nQ1XlJUnP4Zjnw8NlVGxaO1ReA3GbK7ikCe_Q-G5kH8jRNw2J8sm7czBb-goV35pTaEMtgr7-h8qCQCSzkc472iFOzoR0FOYViqguRW-gznO182o4iBRQTEkaJHdF_VyM0_DxJJXLrBADCGQRdXmRcFbuhyw82KZJ1i7oDaBZbik2it26Gnqd6v_FRvaxGNyYlVTZLbfZWc_o6Bzpqp2cmC6gTrLDqMJUMlrclSZRH2AQx-XT1bTAg3ToQhLqqanZugA10KPQr-jKeMH7wtprUHZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0106cebdea.mp4?token=qeDyZ9t4OPAP0PUQ3HwAnvjnqix8vnj5SFNfDSYA2ul88EuTeNM86g40dGI64nQ1XlJUnP4Zjnw8NlVGxaO1ReA3GbK7ikCe_Q-G5kH8jRNw2J8sm7czBb-goV35pTaEMtgr7-h8qCQCSzkc472iFOzoR0FOYViqguRW-gznO182o4iBRQTEkaJHdF_VyM0_DxJJXLrBADCGQRdXmRcFbuhyw82KZJ1i7oDaBZbik2it26Gnqd6v_FRvaxGNyYlVTZLbfZWc_o6Bzpqp2cmC6gTrLDqMJUMlrclSZRH2AQx-XT1bTAg3ToQhLqqanZugA10KPQr-jKeMH7wtprUHZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💯
تنها کانالی که حتما باید توش عضو باشی
✅
چون راه پول
درآوردن رو بهت نشون میده
📝
حتما آمار کانالشو ببینید فعلا به مدت محدود عضویت رایگان باز شده فقط تا پایان فردا شب
🚫
⚠️
نمونه آموزش بازی Apple of Furtuneکه سودش تضمینیه رو براتون گذاشتیم پیش بینی های معتبر فوتبالی هم دارن
z22
:
📶
https://t.me/+MT03hkV78q9kMTc0
📶
https://t.me/+MT03hkV78q9kMTc0</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103572" target="_blank">📅 16:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103571">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e9ffe2f3.mp4?token=VYfb3S44wCM91fxJpnruutX1-cvpinUk88hZSs6f72h31HJhjUIG-PkWnpqrGnns_k4JJ1rkkJF8Pq3GF8WuSEAsPUPi7i7XYxxaOZOMWuZBXqesKwkQMi14VOVMvcXhCihapFjlQu3ttlfel2MMA4zgVIuaU00CAJqobLaqwo0_8PfSvA5F-TL3sqFkp7dLBf8zYwF5whByeD7QvmGoiukc6e_1LoqIl_qfZG_vtpi4_393Zh6oQunF4uj9nAQQPkcmF9QtTL_bZ5hgvZ59UvaRRJFvv9B19C7d1j6UzPY0wt5sGivGDJSYyjN3WEx7bXQtlj0wDGoSO6N47Rj5wTsRlxQlVXhb2th5QJvtjvZot0ipWYhL7cVqSDo-wOqG8Gfv53HDAT2K8paEjaXFB5H9LWikRejJVrzfV_86Sg9C2_eJtnOeD87BfaBO_JwBuHpnIStH37asb3Ne6hRKpIwY9HOdd3dIy6IDWcHJadMHgj8Xaf6o9jFtjnb2gWfUSXvu5j_qXCbhfO5qF8oi_GNCGYiqYP5ImqF_f_vOsrsib6H0Mffj4woWjPa-LodQ7qpoHZrUEoQDgGg_nPZ8Q0It0VxROF_bDr1mAIyrwPWqsuIZW4WS7CzX7_kR2QQBEx1e43jg30WlTHtnWyVc14vFYFCenKSIl0srDjmx4Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e9ffe2f3.mp4?token=VYfb3S44wCM91fxJpnruutX1-cvpinUk88hZSs6f72h31HJhjUIG-PkWnpqrGnns_k4JJ1rkkJF8Pq3GF8WuSEAsPUPi7i7XYxxaOZOMWuZBXqesKwkQMi14VOVMvcXhCihapFjlQu3ttlfel2MMA4zgVIuaU00CAJqobLaqwo0_8PfSvA5F-TL3sqFkp7dLBf8zYwF5whByeD7QvmGoiukc6e_1LoqIl_qfZG_vtpi4_393Zh6oQunF4uj9nAQQPkcmF9QtTL_bZ5hgvZ59UvaRRJFvv9B19C7d1j6UzPY0wt5sGivGDJSYyjN3WEx7bXQtlj0wDGoSO6N47Rj5wTsRlxQlVXhb2th5QJvtjvZot0ipWYhL7cVqSDo-wOqG8Gfv53HDAT2K8paEjaXFB5H9LWikRejJVrzfV_86Sg9C2_eJtnOeD87BfaBO_JwBuHpnIStH37asb3Ne6hRKpIwY9HOdd3dIy6IDWcHJadMHgj8Xaf6o9jFtjnb2gWfUSXvu5j_qXCbhfO5qF8oi_GNCGYiqYP5ImqF_f_vOsrsib6H0Mffj4woWjPa-LodQ7qpoHZrUEoQDgGg_nPZ8Q0It0VxROF_bDr1mAIyrwPWqsuIZW4WS7CzX7_kR2QQBEx1e43jg30WlTHtnWyVc14vFYFCenKSIl0srDjmx4Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
بیاید باهم چنتا رقص دوربین تاریخی ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103571" target="_blank">📅 16:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103570">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb4aa9e2a.mp4?token=jgkI20kUZQDynCfnWXlE_3cHicgwQeo0v5UF1EdN_T0VIlSWVXLYwIXbHTelspwI8wS6sL7l3LVYFWBSjaVx-kdXaGhX0K8sa8kdhX1MKUkuEp-V5Oz2Vj6VghhiAn6q72DqzsWRhkSK97Bobe_zG200RBiiR8g53pkblUas8y7A06RFWOo8bmZSz13gZQOj23AaFzrnuXYqGOse_aFJM9QboRv1TFu_COqTTCck0gtzByws3YLSuvqVs7BuKiKRt6RjMa-s37dEYyRgMbRLPo3NUGp9W-3HZnwzCe-w8eheS2K_UJN3WqhBZlr_Ad5_-v_goiGEvaYUvp1hqIvULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb4aa9e2a.mp4?token=jgkI20kUZQDynCfnWXlE_3cHicgwQeo0v5UF1EdN_T0VIlSWVXLYwIXbHTelspwI8wS6sL7l3LVYFWBSjaVx-kdXaGhX0K8sa8kdhX1MKUkuEp-V5Oz2Vj6VghhiAn6q72DqzsWRhkSK97Bobe_zG200RBiiR8g53pkblUas8y7A06RFWOo8bmZSz13gZQOj23AaFzrnuXYqGOse_aFJM9QboRv1TFu_COqTTCck0gtzByws3YLSuvqVs7BuKiKRt6RjMa-s37dEYyRgMbRLPo3NUGp9W-3HZnwzCe-w8eheS2K_UJN3WqhBZlr_Ad5_-v_goiGEvaYUvp1hqIvULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادار ترابوزان‌اسپور خوشحال از جذب صلاح
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103570" target="_blank">📅 15:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103568">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmxgbYJW5wyL_J9j4PdYORbhaejn85ZPm8caZ7erLRkdrrEBKFExy0zRXZE0dsScoHE5RBzsWOxBpERrD3P7LRzc_oUTTGrwGRStecC39W0AflWj-_g20yLpr14-A2FOJzjvIgtx5kmELHv2tvAWbNygp1UqkRkWSiP33IbYCMyLfz5QSPSxqFwvnpTflnCtCkFaH0Xmrt-4vAHD6zXAL0nec6IFv19mz2UHMWJDaAGCSolNQkanXu-xOQlirTk5fzqzzksEs9WIwuWbFuC45NbNKSGHhJriJdVLkFcX27UukPdykD8GI-j_tDH4f3Q_PfFuoTsSQA0NnffptKNJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dcaf140f.mp4?token=HPKL80StI7yCQ75IyBN4f2gZgaWrfZWc8r95gHGi2sjYVj9tTNKzhGrleq9EyZnVtD79ZlKRrhD9G8453hjtxr35wb7qpXjbImM8DxU2Fq9Z7kU2NcVsshXrE_fM5DJ4_DYIndy3lqltua3yenieYvGgHMal29XEMCf6L9O77sUCYJZXsYSrl1GtbV6ew2iJZWbm5oKInc25fVP6Go1dC9Z1N-fk0l3y90RIKki1k9fmZdDB_um3o6XbQGvxxjWQ6h_akkmdaBhdmQbZD5nVTjVYJguXvQBMrOtJx1Q4K9yJrrQXitLyAhboOORHYoWirVkzdUFV7FCcTK0euSWhew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dcaf140f.mp4?token=HPKL80StI7yCQ75IyBN4f2gZgaWrfZWc8r95gHGi2sjYVj9tTNKzhGrleq9EyZnVtD79ZlKRrhD9G8453hjtxr35wb7qpXjbImM8DxU2Fq9Z7kU2NcVsshXrE_fM5DJ4_DYIndy3lqltua3yenieYvGgHMal29XEMCf6L9O77sUCYJZXsYSrl1GtbV6ew2iJZWbm5oKInc25fVP6Go1dC9Z1N-fk0l3y90RIKki1k9fmZdDB_um3o6XbQGvxxjWQ6h_akkmdaBhdmQbZD5nVTjVYJguXvQBMrOtJx1Q4K9yJrrQXitLyAhboOORHYoWirVkzdUFV7FCcTK0euSWhew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زمانی رئال یه مهاجمی داشت به اسم ماریانو دیاز فقید که از لیون به رئال مادرید اومد. جالبه بدونید 12 گل برای رئال مادرید زده ولی 13 تا جام تو کریرش با رئال مادرید ثبت شده
‼️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103568" target="_blank">📅 15:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103567">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f385b11729.mp4?token=PIVKoJVxOiVdVf8td5Cwx3XhxxSxUzb3ptbp6vKdFRas9RKvp18-nG7JqJdI4y2j8Ij-JQS2GhqcmPr2vsmz4IW3tBeP9vgBeWGgZv4BvArffy829YgMGwRToAaFKr_PcuGEEXxVP-8ABls7_T_Y1gKArzjNU8plrd89n9AaZqCxrz3beHqlPJoj30soCSIdec4mNKs84l7Z7iM80O7ljsa9Qz6fgi9mbo7VzYWSzypuSSYLAcEbgbwD53vsAR47K9BUden3AVhsLM8Wy6RuHU33vhAVgqHtT2l0qLsr8oHP7zBwXmJhAU2LT4aWoE2m2n05fNSXhFn5XBHIfxg1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f385b11729.mp4?token=PIVKoJVxOiVdVf8td5Cwx3XhxxSxUzb3ptbp6vKdFRas9RKvp18-nG7JqJdI4y2j8Ij-JQS2GhqcmPr2vsmz4IW3tBeP9vgBeWGgZv4BvArffy829YgMGwRToAaFKr_PcuGEEXxVP-8ABls7_T_Y1gKArzjNU8plrd89n9AaZqCxrz3beHqlPJoj30soCSIdec4mNKs84l7Z7iM80O7ljsa9Qz6fgi9mbo7VzYWSzypuSSYLAcEbgbwD53vsAR47K9BUden3AVhsLM8Wy6RuHU33vhAVgqHtT2l0qLsr8oHP7zBwXmJhAU2LT4aWoE2m2n05fNSXhFn5XBHIfxg1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
کنایه‌های تند مجری تلویزیون به مشکلات کمبود دارو و اختصاص ارز ترجیحی برای ورود ماشین‌های خارجی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103567" target="_blank">📅 15:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103566">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe161733b.mp4?token=gPJd3V7rkNHgy7HBFBrPyvWbgjicTG4UPHsWqOT0xz2BA-EL3lfWfxE7_wGc1jtG6bxQuzd5JATLab7ENZzI1-OGPdelRbo_ZYNYu-3tIrs-2G4w3w9DpHlQV5mBjl73a2pO-rYjAlW7UIaonbW8qurFui3sdr7O2aw0pBdzmsQwVe_p2HzIjzAfNnfloDn9cgC88Gv1ceMsOHQiSuoTBF58KXwX0EjmLiUiljVH6wSl6eV38QMeIS3al4LVpcxJIrgMf4uHcajtwzjG8jjqUqUbzbFRSTB-WJVvdvGv_KzLZO1gBpogUTCTDiI0ihdLEgUbeUYbVXftkap5ZdfbiIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe161733b.mp4?token=gPJd3V7rkNHgy7HBFBrPyvWbgjicTG4UPHsWqOT0xz2BA-EL3lfWfxE7_wGc1jtG6bxQuzd5JATLab7ENZzI1-OGPdelRbo_ZYNYu-3tIrs-2G4w3w9DpHlQV5mBjl73a2pO-rYjAlW7UIaonbW8qurFui3sdr7O2aw0pBdzmsQwVe_p2HzIjzAfNnfloDn9cgC88Gv1ceMsOHQiSuoTBF58KXwX0EjmLiUiljVH6wSl6eV38QMeIS3al4LVpcxJIrgMf4uHcajtwzjG8jjqUqUbzbFRSTB-WJVvdvGv_KzLZO1gBpogUTCTDiI0ihdLEgUbeUYbVXftkap5ZdfbiIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدویی که بارسایی‌ها میتونن هزار بار پلی کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103566" target="_blank">📅 14:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103565">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5263acb67c.mp4?token=TTzo_n7O67WTW4HSct3iB_Ktk8OE9mkG2Sdb6o57U62npMJ0BGM7UeOlNZVOz4mnz9GVulOUIKJSiVPuOp8f9_lO-j0ts7c7T0D81onw4VENc9cgnrfLjlYNZoZxCZxZj6CBBvvQoHgMSTLmmLA11iF763YABcrNxHlgZCzDLw90Ap1KxATKYGxCn0eGt_24usnYKTHvpTqt3IY41pKM1eAjDXqKopPkI1P0ELLuTBlY2F3Be23KjHOPjlDyE8stOsYRRC4Mo39SXWZq8yc8CR3Hq2CggwNhzn5EHN36TCqD7D_W1tp0JWkPNrKM1Om_L4raWUWivH-kpocZDcrOdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5263acb67c.mp4?token=TTzo_n7O67WTW4HSct3iB_Ktk8OE9mkG2Sdb6o57U62npMJ0BGM7UeOlNZVOz4mnz9GVulOUIKJSiVPuOp8f9_lO-j0ts7c7T0D81onw4VENc9cgnrfLjlYNZoZxCZxZj6CBBvvQoHgMSTLmmLA11iF763YABcrNxHlgZCzDLw90Ap1KxATKYGxCn0eGt_24usnYKTHvpTqt3IY41pKM1eAjDXqKopPkI1P0ELLuTBlY2F3Be23KjHOPjlDyE8stOsYRRC4Mo39SXWZq8yc8CR3Hq2CggwNhzn5EHN36TCqD7D_W1tp0JWkPNrKM1Om_L4raWUWivH-kpocZDcrOdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
لحظاتی با مهارت‌های تماشایی کیلور ناواس ستاره سابق پاری‌سن‌ژرمن و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103565" target="_blank">📅 14:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103564">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw4Jbwy2vX6yIMMUKNT-tmRzoz7eVOCwc_9Ljd_QTxvIqyQC07PYKWNmGRkETKGeyEqpeacBCUPoJlKSmzNdqZkF5tNdSVz5ZdQVCGdxTsgb_WbkUopT4yo2dTUs4AQzEfn73wnx_7hQHrwTUUNStVvVqsKR_YB6DY0mYLLTIUMxtinH_a71WWOR2t0yF29IXJBLJKVGOQqA_WHW8OGVtgqhed2ZcUN9XFm-TeFVwWZ1xM_5cfYn6SP7nrLj1LH2xeSZMPZ000HLFI5eZdZyb9R-k8RKoywhgpTAiCOZX8g2D8wt8G4hK7zTRvALWl6TeYc6I0kc-dseBgbwr9AS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇮🇹
🗞
رومانو: دو باشگاه اینتر و لاتزیو درحال مذاکره نهایی برای جابه‌جایی داوید فراتسی هستند. رقم پیشنهادی لاتزیو ۱۵ میلیون یورو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103564" target="_blank">📅 14:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103563">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM23HPoLeFeLWXlFIfzhP1VF5Pl8r5pWBTh3X7cWbLEsZFMWFxue7OR1Mj56fT3BZ6GrbKamY0u-MEskoHyUpLy9dmP31vYDr569S_ofFFfqimyRoxlSL2UoyMmEBz1brrT04R6QQhkSD67UCBsoRV7mOf2Q20Z5xJvnz03PMLmniRnPlM4rtc66yxbXoS6AWwRskzwYWCHk2gr_3DU_BhR_8IDTncooqdi6KZ5yWraiM0eth_cHmE32nHQZeWF1Unw04NiHzuonipkytYHSgonUbbzfG_4J8Nj66UPHrJuqd9IhKEz_BpCz1r6IqBX59HcBkzHrnniffcPKK6hvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سوپرجام اسپانیا در استانبول برگزار میشود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103563" target="_blank">📅 14:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103562">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/734a158141.mp4?token=jD7RJDqZ8dbfDt6gDnh-gETzr5EC0BmcXN84kARkq5r6WWI0WfLI7RXooW5PNAiR6LTR0eNpbUX7bp0_W2FegYBkWEfKrH0K8C9RaQytxymB35UP7dqL2pVh1I5tomtF8WadXPg8enPHR9LZwCWB17g4yIbhWqE7oeV57ScwDzGJvw20unU3zNt-Be1a1YAEg6MSjE6bRa7XunU7O7NiYbpbTmkze_uxC_Xe-Ih_uZxBQ_ubq-o7ayDHAobA_nAG_X4i-cKPVM1SbGV0Ikh9jSGUdocGZrykUbEsc99s42BoOZVI8FP3rgk6bFeswaUcE6p55awnofYmxGYraYOITQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/734a158141.mp4?token=jD7RJDqZ8dbfDt6gDnh-gETzr5EC0BmcXN84kARkq5r6WWI0WfLI7RXooW5PNAiR6LTR0eNpbUX7bp0_W2FegYBkWEfKrH0K8C9RaQytxymB35UP7dqL2pVh1I5tomtF8WadXPg8enPHR9LZwCWB17g4yIbhWqE7oeV57ScwDzGJvw20unU3zNt-Be1a1YAEg6MSjE6bRa7XunU7O7NiYbpbTmkze_uxC_Xe-Ih_uZxBQ_ubq-o7ayDHAobA_nAG_X4i-cKPVM1SbGV0Ikh9jSGUdocGZrykUbEsc99s42BoOZVI8FP3rgk6bFeswaUcE6p55awnofYmxGYraYOITQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان رامبد وسط برنامه ۹۰ رفته دستشویی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103562" target="_blank">📅 14:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103561">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtK87S_b7_0Vg1nfQz5ZBxbHhwh771rFaDsst9mUebr3nxQUJ9PDK7yjay3UHnUiBnA67Izm3maWAwQXnSVUhkZcTKz2eFTnMuilTbATPVMNpwFLWvtlTcr1bCZXrrBz4oJKU7Y5mYw2eyrmMv8RmW5zuwXpXoKUHZPhkFOCerBTpbj8bdfe88uYhTa6WekY67XamVa-3Rfz4Zg4nR1PAqgD-j-R5MRXCqiFOFE7TwGXtaNqIavf8EeO7XHjuFjoAFouSxnru3JJrdtBlomK29WbqIOIZm0CJ3Wd5yk6K-e4dEjRZEtJAxNRkv_BBiXxcSRp4RXNLVjZm6F6V-EBIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ جرمی دوکو تا 2031 با منچسترسیتی تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103561" target="_blank">📅 13:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103560">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372ecd711b.mp4?token=dx7pJ6-zb380e0QDx-yDXGnq7mYnOZHvdgbtXbKuZtUwTcZTYHUKmVyp6I_vwzOMQ91bfPqoNlBXStb1low7SUBuDP8C6uIHLl6FC3mYOGLLhfz5fqUpxDyH5SwRj6fMaH9HG49rsaBxifQnkLV4L0HElBt1-PVK1Q7yhzkgPDwB-YvjjjtKSpTlx2PrqK_yeo-Vx8x5K3m7nReYjwUWkcdEFetRlJjTSyWD4biDMG0flZLQrRHanGw5aEt3dVsfaWP1n_c0aAUUL5ciZ7KiuqptErVst8_yJeDdTtW8wf5ajQvniRdiQbvp1ZtGamPsYCeiOjfrJjJdL3sbMd1ztQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372ecd711b.mp4?token=dx7pJ6-zb380e0QDx-yDXGnq7mYnOZHvdgbtXbKuZtUwTcZTYHUKmVyp6I_vwzOMQ91bfPqoNlBXStb1low7SUBuDP8C6uIHLl6FC3mYOGLLhfz5fqUpxDyH5SwRj6fMaH9HG49rsaBxifQnkLV4L0HElBt1-PVK1Q7yhzkgPDwB-YvjjjtKSpTlx2PrqK_yeo-Vx8x5K3m7nReYjwUWkcdEFetRlJjTSyWD4biDMG0flZLQrRHanGw5aEt3dVsfaWP1n_c0aAUUL5ciZ7KiuqptErVst8_yJeDdTtW8wf5ajQvniRdiQbvp1ZtGamPsYCeiOjfrJjJdL3sbMd1ztQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو: یک آغوش بزرگ برای تو و خانواده‌ات در این لحظات بسیار سخت، لئو. قوی بمون.
❤️‍🩹
🫂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103560" target="_blank">📅 13:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103558">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hzEaY5IU827KnCrUO3kH2NHVOxNisXkY0BDMl2EK064HJSLC6TfBaz7K5UyIfMknIOXVLPa03HI9owhMCzvK4rqi-jyYTnJQG3gEmPhQbgZaUyA12yqWEDwh3EwSpEf5_ekONKULXE_KfWTDQaVy5k43wVuB2l5jjlGWoz1F70caPULrEHY_T6zk4g1mUgwmsS2FE5mUclZjM20ZxgtNfuZtHMysHcpNG7HJUZRQQOBJesWqkNLgaOKu-VvcIoeDNFhh1ipUv4xxLFj3eKSXb2fm7T3kJMF9X9L1voiVWFwfWU5sZVnaivqPq7e64PCKXhCpmG-yRbbSOqOFC2DMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ku0C_2qW2awoLsavkDlmFZaqYN2jpIZHsBNLdW8-hcFEiaNfJvZAD-Kq6SZuqNbL57nrKlsjlqqnUtGb86CIl9m4hlMWEcG5BOjpfsH_2LhGrbrDTTc3mXMg1u1f-lAPpd5vhKjDjnAtZ3hgkXp7nCAfuqYN6EplRnmOAdUV5M4ZQNauguixtJv6jlggpdfE-URJ0j3vDRDv37jwGXx13eWvDGOyK-AV4Qlyht1mm1xprFPo-Cno1F-J85zjyTdWMu3ppG3RuMyu670vaMUfQARQGXxnHMFJLIj45HsioNyC4rGJCNblXL1a5taPbcJiW8a71_Ll2cgskipHet1gyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کامنت‌های سمی ایرانی‌ها برای پست رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103558" target="_blank">📅 13:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103557">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f44077de54.mp4?token=MQy2fduy9O_pMfp74YBf4w_mU8r51IelSwK3MLRNxSI9TVBMKGf2o6GHudEhH_OG0LYg9kZ8s1R-tNVs99fKR28ulrJdNujCamb8INvL1MWy8Af6F4bQpt_0KGD9uhVBKBBB8XxiQhdwWc7EsyLJBii7ZHFlrzZmSwr7lbSHEQMnNOORfppWdDswvSjOwwD6Aqy2_yazN27Gq4ne74-cFFOsyCwmW52CtvLqTxixGcz8y3HKOxK9A137mRRqBDCiH_rf67gPiTiy86d_aazi7BX-4vGXlwvBrlbHCHVs-KXjmSh3OP-1dsML4ZU5UHBNYFLi551cUEnITZ_61-TIvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f44077de54.mp4?token=MQy2fduy9O_pMfp74YBf4w_mU8r51IelSwK3MLRNxSI9TVBMKGf2o6GHudEhH_OG0LYg9kZ8s1R-tNVs99fKR28ulrJdNujCamb8INvL1MWy8Af6F4bQpt_0KGD9uhVBKBBB8XxiQhdwWc7EsyLJBii7ZHFlrzZmSwr7lbSHEQMnNOORfppWdDswvSjOwwD6Aqy2_yazN27Gq4ne74-cFFOsyCwmW52CtvLqTxixGcz8y3HKOxK9A137mRRqBDCiH_rf67gPiTiy86d_aazi7BX-4vGXlwvBrlbHCHVs-KXjmSh3OP-1dsML4ZU5UHBNYFLi551cUEnITZ_61-TIvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
ماندگاری، مدیر رسانه‌ای استقلال: درخواست سپاهان و تراکتور برای برگزاری تورنمنت 3جانبه غیر استاندارد و عیر قابل بررسی است. جام قهرمانی حق ماست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103557" target="_blank">📅 13:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103556">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d7de5b02.mp4?token=P3RT1BCKgPETR42iQB0tQxoxF0igLlf-YaNzi3OC271tTF7Y7kmvdtOT3rPfQmntRawipBbCu2HwbD3bMjfwqLsLsIPhhoHdQyKQj2PuWNKa3-znDkU-dhTaf_gboNWhYCqyQ3nUHNgxNk5vlFilP0ADjnMj5snKNvK4ucszKdAURGpfbCPF8L9uzRCyXu86XtLKV4ROL6g8-XzG8wTN39sCjFEThpMJGuRImzFEZkOl6B9ng8pKvfIsdYvnH6gLZd30_SIlEIi2b7kpVaoVuVYZTC_hvjGPrRMKkyPZ0WV0s5cXpcvt8bHiA7n3zT7xRXxNj6mH-3IPcVwk8epOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d7de5b02.mp4?token=P3RT1BCKgPETR42iQB0tQxoxF0igLlf-YaNzi3OC271tTF7Y7kmvdtOT3rPfQmntRawipBbCu2HwbD3bMjfwqLsLsIPhhoHdQyKQj2PuWNKa3-znDkU-dhTaf_gboNWhYCqyQ3nUHNgxNk5vlFilP0ADjnMj5snKNvK4ucszKdAURGpfbCPF8L9uzRCyXu86XtLKV4ROL6g8-XzG8wTN39sCjFEThpMJGuRImzFEZkOl6B9ng8pKvfIsdYvnH6gLZd30_SIlEIi2b7kpVaoVuVYZTC_hvjGPrRMKkyPZ0WV0s5cXpcvt8bHiA7n3zT7xRXxNj6mH-3IPcVwk8epOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
روایت ژوزه‌مورینیو از ترس‌همیشگی‌اش مقابل اسطوره تاریخ فوتبال لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103556" target="_blank">📅 13:10 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
