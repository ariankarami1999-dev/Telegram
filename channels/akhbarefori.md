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
<img src="https://cdn4.telesco.pe/file/m7bCQLEfXHB3TCwQgHen6R8sfZ8XWSGlfBfgWbKqP7KQ7drigxpzcb86KKN5P1iOzueWl_7twW9QnzLsmMXa_JfvJTC0Q_tKFZVnc4TWOP4snIDY02DWBPgzoGmE3ks5WuPcdcqcq1wr5-b951ELjR57nL3iMdnKiTsmswV9CMCc7d4v2U1LEWBrLfMAqYiuNeCDF-qhkfhPlXMxs8TNtEjNg5CvxPfM1I0tH3XZA5ngtVS9aJz4bIyU1Ni_FDLWyfx3foVrfVOyuB1YcG9XCxbOv3sJApkHu1ZfNVO_su1CkxxZG1q2Z2REaQqE0-PX_IkC1hlHsSUIiEyLrsuEfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 07:59:57</div>
<hr>

<div class="tg-post" id="msg-667728">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
خروج چند واگن قطار باری از ریل در زاهدان
روابط عمومی راه آهن ایران:
🔹
بامداد امروز تعدادی از واگن های قطار باری در زاهدان، از خط خارج و موجب مسدودی موقت این خط شد.
🔹
کارشناسان فنی راه آهن، جهت بازگشایی مسیر در کوتاهترین زمان ممکن به محل اعزام شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/667728" target="_blank">📅 07:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667727">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp6N0_Rzeyg4-VomKVki5NkI0hrB6VfGsGT3v26kD_Pu8hsHFsRi7sEaUVt4hdtZXOAQLK74h-7lRULpgCqAi8C6zyTRDqPJltyiB6vjlQMRYaEfujikt8gkAvQpvxo4QjlhCh9PpRmmQ9GE4Z5XMwW6cdU0z8GfkBg1jlbifoyTpVPbpqsQPOhyMaDhInK1tNHTBYTnBAguaaZeR_XGtFilX9X7gi7_Wccax2phOQaHSGC7YX89c51Sjr-WO1J3XSlng6HEiFMbmdHmrVeHgJMPU2Aba1pCLRrNq8v7b3MHtg-VezUVRTONzaGl94c0Ro1OiA0YMfdujXSySpTiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/667727" target="_blank">📅 07:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667726">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc26bff3e.mp4?token=f2xNyeoaIpRAeenX7z-UfLil-AM5cEY8IAIcm3dV1oywqG6myoGRY2KjngX0Izy90qQEGSpEH9EV-lrUtfS4ioX89ZMkcf0iLP_CRDOtmWvG8ghXHPAJio0Ma0eio4X-1LGUf9k8IcjhHf4Xptfduly65ocve9hLs2uAhfwwwEdnXWXYS8DgGuL94CjcWbEVHm9sdFisBTE2fgluOfIg0PCWyMWK7G-7VRPi7AAWRaQbr4aJbeCz2OFMiJVuvpsQcWZ5KmeTxElHUYlUuwGT6GT035KT59nmMg4pq1d8y2JyQyRgHlWt8MjGUX75S3XEKpLfSvRLDBYkR4ADslqQHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc26bff3e.mp4?token=f2xNyeoaIpRAeenX7z-UfLil-AM5cEY8IAIcm3dV1oywqG6myoGRY2KjngX0Izy90qQEGSpEH9EV-lrUtfS4ioX89ZMkcf0iLP_CRDOtmWvG8ghXHPAJio0Ma0eio4X-1LGUf9k8IcjhHf4Xptfduly65ocve9hLs2uAhfwwwEdnXWXYS8DgGuL94CjcWbEVHm9sdFisBTE2fgluOfIg0PCWyMWK7G-7VRPi7AAWRaQbr4aJbeCz2OFMiJVuvpsQcWZ5KmeTxElHUYlUuwGT6GT035KT59nmMg4pq1d8y2JyQyRgHlWt8MjGUX75S3XEKpLfSvRLDBYkR4ADslqQHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم خونخواهی و یالثارات‌الخامنه‌ای در دست تشییع‌کنندگان مسجد جمکران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/667726" target="_blank">📅 07:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667725">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f642d5f0.mp4?token=Kebu_vAxwQ2jEr3PwcGPygbuZDU7nlTP21EmQe9gjlxJRuYdnfvCQkkgwMAJ0Cx9NDcJQmB9b54fNpeFY3mC23mN9fmrzMBbsSP4YzHJ6OAa-LFYfCg4eurclyvjCscwunb3bdpue4Q65pxP0nVjybX22OO3YMMKG5rIcErWOFfc2600EWcfBMoZbZPaXifG7soUxOiAzW8ptCCiEbRsuaQecDbznoxzMp8OD07gKQYZQrlQCv6mAAYO7HFGApaH2SkM0cjlcbeDr-zN9xRYG-RkudHygjb5MSLDBbVLB4DS8J-OgXqwgaLtoHcSwbg6ymhS9gepI5D4LbTAVIWitw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f642d5f0.mp4?token=Kebu_vAxwQ2jEr3PwcGPygbuZDU7nlTP21EmQe9gjlxJRuYdnfvCQkkgwMAJ0Cx9NDcJQmB9b54fNpeFY3mC23mN9fmrzMBbsSP4YzHJ6OAa-LFYfCg4eurclyvjCscwunb3bdpue4Q65pxP0nVjybX22OO3YMMKG5rIcErWOFfc2600EWcfBMoZbZPaXifG7soUxOiAzW8ptCCiEbRsuaQecDbznoxzMp8OD07gKQYZQrlQCv6mAAYO7HFGApaH2SkM0cjlcbeDr-zN9xRYG-RkudHygjb5MSLDBbVLB4DS8J-OgXqwgaLtoHcSwbg6ymhS9gepI5D4LbTAVIWitw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین شعار «لبیک سید مجتبی، فرمانده کل قوا» در مسجد جمکران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/667725" target="_blank">📅 07:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667723">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
حضور جمعیت بی‌پایان عاشقان رهبر شهید در خیابان‌های اطراف مسجد جمکران پس از اقامه نماز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/667723" target="_blank">📅 07:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667722">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inpxhuUydXVvZ2lJrU1upEgCKE5KFinc_FtADi76OwvHRsCaZRChOHHSHHhuwx7JILHc0Q60InIoqC5nJqvTQOGkT3t8nGlIgJJ92ECucNNArtxj8hH4KpIjErmqq63Iivm_MAtZSiwS0gVMHv_y1HWZ9y6smRR-AjKxzkKWNkMBp9OBPo3aoOYBbbvHIkow9rkK48oC0z2HARaHVS0zpgHhcyrvZTIHXes47L7bQ-9xWhoD7zGNyLVOVt3JESaEu4XehF5EfdgDdMI6Mw11bh_A4UqygtoFBeJnSm929u3nDy_TJhmv2KJJJnpo8fn4UV59MTMDabRd7dtaDJx8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار درختی دور یک چهارم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/667722" target="_blank">📅 07:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667721">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae3dbb160.mp4?token=IHcQgI4xntbYASVuATYR8mmZD6WluPy_pOaxbsNXz7KmkBsy_BKIgQNiDtCWZv_n1PkcEtdkp_6nPQbAbBh9gY3q7cI420AnkdNdcsB6t7GBuz1iByGSY7XA3snaIZr2PAU3yCTk7WoppDMAGammnE9dUGc4fGePYZ1KfGYI9D1qEuP7VgCmuPhI1JyCg8dHwLOj08qeA7IEbCAGJRxTlBgTsrFsUaaD88VWsKnM3Xcx7QH_uumJaKhkOvuBuXtD4Bg5NIqFS-xmjIXlBMxFeK39Vshs4-R4z5pXpCsB5-pVeYZjw15grWI6twavtnwGgUytAZg2ad23O1Oh141BGoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae3dbb160.mp4?token=IHcQgI4xntbYASVuATYR8mmZD6WluPy_pOaxbsNXz7KmkBsy_BKIgQNiDtCWZv_n1PkcEtdkp_6nPQbAbBh9gY3q7cI420AnkdNdcsB6t7GBuz1iByGSY7XA3snaIZr2PAU3yCTk7WoppDMAGammnE9dUGc4fGePYZ1KfGYI9D1qEuP7VgCmuPhI1JyCg8dHwLOj08qeA7IEbCAGJRxTlBgTsrFsUaaD88VWsKnM3Xcx7QH_uumJaKhkOvuBuXtD4Bg5NIqFS-xmjIXlBMxFeK39Vshs4-R4z5pXpCsB5-pVeYZjw15grWI6twavtnwGgUytAZg2ad23O1Oh141BGoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخواست سیدعمار الحکیم از ملت عراق برای حضور گسترده در مراسم تشییع پیکر رهبر شهید ایران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/667721" target="_blank">📅 07:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667720">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQTLmpOW5RVkyKndiTGhUOJDoGBYASP_0b7DhwOfKJNG5ntWpdPxMvwcg3vhcDc-byXY7bYKnNONSNndbVj6K8mufA5_FsY732Xe9I1ACB00d57mFythfW6xTZpsdWApk2-JRine7Cs2Qd9mqfE86scmK5UNxXLlx9wVIV6nvhttpXtdEbvfNdnnN_bQV6kWfd0GexEFHKUqZKNLLyIp0O08taf0yg2y-f-nBdbYOdcbLO5-Vwh1LyLdjSAXGLBJ1TINQWOBy5a426OvaLBo6kjnSbrj0MzRlkd3gPj-NhEvXs_3YSTfpphIN6d93iI4wG2BY1RRu3ke9QZloYARKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب تشییع پیکر رهبر شهید در شهر قم در سی ان ان
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/akhbarefori/667720" target="_blank">📅 07:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667719">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUuTAprMxg-q_jfBQ-0BdJfwtUQzQ7fd0nJ2BkK6agmve9jC3Vi1jE1ZM1oUEh7bRePPWlJs2VPAV-QgkDYfrMkV0gLaJmG9T8i-cexoNWu7ujdaSy-v0wP_kSLYjgx1vezn8QzgbXz4e3IziZpRZWFqkPgwFxXSizTnE_npQk0isWROo3uRcLqNAFzouYLDyYogFY4oSE27MASWWDj2aUGjKABdSQWM9Qw8-khRM3EGN4sbadrw5CfFk91sUu9dpyYm-wDl1y3WJLL8WxBSYvmTCzqsTAx8JZHPql3z1xvVWorP-ih58F_s7Ez7m8PdltYs9Q5IATKWzuOkL69oUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از حضور خیل عظیم مردم عزادار در مسجد مقدس جمکران برای اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/667719" target="_blank">📅 07:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667718">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhilzOJiOlPuYhYZc7suqc64DEH30Y_EnBmWKRFHVDI9G3jJcFpAqdxPqOv8JlxKjOJltH2VSgx4nc4Nk6_Gk_OtR1Zl4HfTINAh7h5kdu4ptNNhn4ZWmtWroewCtS7-2UMsprqG3BwgnLrN_TBfPMjUcfvqn2dL-FDYXMLZE5luXwtO4jzaQvFKX5edROnuzz8qrW_oVI4qdHIhf8-GjAWniOxgnEvQWiMhQrEO7d5WKg8r3T3fwj2dfYfAfu468ldzZM8u86nWOo0thjZ8-sevudkpv1gQMrZrJMLPV69aqTCprOCE3SqnFhtdfih2FiIdldsN7aGfiPBv1JAuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دخالت ترامپ هم مانع شکست آمریکا نشد
🔹
حالا جام‌جهانی بدون میزبانان پیش می‌رود؛ بلژیک با تحقیر آمریکا به دور بعد رفت
🔹
بلژیک ۴ - ۱ آمریکا  #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/667718" target="_blank">📅 07:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667717">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6340788de5.mp4?token=rGRFParpYWj8NWyy_quDthkGYWIqkM2OHInCtBEz3xupDJiXUyxP2xhQ_XGv0SDXtGx49LMHW8hTEuZLD8qCq-N9CkPii5o20RjVESQinp1RcsWKrM8vLKd_4er2kVLsz-nrK2NPMQHMPPDCJI5jjvLpM5Em5urBHRSt8FtjTDuESy8pIFoPs5p9rgZHGoVgxNXG7AFhuBAn4VLiZR1HeUm7GXkisKzTW6ywwgFRxenyjGJTbICbht1kRjm4qwQ4v73Ntm3SKREbi0IJHP-wALUCOVSwxtrpSqhSW8hypdImtHmkMhMBT_s-mqFr4MSI3P22R7zgSpMrRrGBUqzxew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6340788de5.mp4?token=rGRFParpYWj8NWyy_quDthkGYWIqkM2OHInCtBEz3xupDJiXUyxP2xhQ_XGv0SDXtGx49LMHW8hTEuZLD8qCq-N9CkPii5o20RjVESQinp1RcsWKrM8vLKd_4er2kVLsz-nrK2NPMQHMPPDCJI5jjvLpM5Em5urBHRSt8FtjTDuESy8pIFoPs5p9rgZHGoVgxNXG7AFhuBAn4VLiZR1HeUm7GXkisKzTW6ywwgFRxenyjGJTbICbht1kRjm4qwQ4v73Ntm3SKREbi0IJHP-wALUCOVSwxtrpSqhSW8hypdImtHmkMhMBT_s-mqFr4MSI3P22R7zgSpMrRrGBUqzxew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم تشییع رهبر شهید انقلاب از بلوار پیامبر اعظم(ص) قم به‌سمت حرم حضرت معصومه(س)
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/akhbarefori/667717" target="_blank">📅 07:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667716">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65aac1072.mp4?token=kzAvyg3yyEupk_oVwK0MVWcFVHdlTdYIEuBcAcJkJhTfX_V_yV1NWDzYFAj0i38NYqubeQAeu0Y7ZgqLs3EmBw7q7SLm01uoynEftc5qeiItrwqQImYnOcd_x7MB8vR-CbKq6feMGB3pmhoZ0ik8M4NhBieoYqaaJgdSvL7ottrNU8HVMRqucvwhAaSxdr6pexGVgNSH2s_b3u0PX1BlD8A5iR0y4DfnTkqrXo835FEeeYM9_RHzxBj7BijydQRKwfpOg_dFq41Wv_eXV9vb_DyjO1FJxVNJpaB4Jix-y9Hr7GGyI9sVOjBOZwK0KAMBxswIlWfopVFd3BmfTPSigQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65aac1072.mp4?token=kzAvyg3yyEupk_oVwK0MVWcFVHdlTdYIEuBcAcJkJhTfX_V_yV1NWDzYFAj0i38NYqubeQAeu0Y7ZgqLs3EmBw7q7SLm01uoynEftc5qeiItrwqQImYnOcd_x7MB8vR-CbKq6feMGB3pmhoZ0ik8M4NhBieoYqaaJgdSvL7ottrNU8HVMRqucvwhAaSxdr6pexGVgNSH2s_b3u0PX1BlD8A5iR0y4DfnTkqrXo835FEeeYM9_RHzxBj7BijydQRKwfpOg_dFq41Wv_eXV9vb_DyjO1FJxVNJpaB4Jix-y9Hr7GGyI9sVOjBOZwK0KAMBxswIlWfopVFd3BmfTPSigQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیگر از سیل جمعیت دلدادگان آقای شهید ایران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/667716" target="_blank">📅 06:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667715">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
تصاویر هوایی از شکوه و عظمت حضور مردم در تشییع پیکر رهبر شهید انقلاب در قم
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/667715" target="_blank">📅 06:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667714">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4da758a13.mp4?token=ny5529t_KWOeJfN8NI2nDBbqmCSBHcbSoZaGPU0yzppghz_gEfNZ1Coc7oIEon1VldLRHZwAvpcpVsEMN2_PqjjoGYL-kX_HZhU8vOAp4fCVROl7PkhTQKlBcli1BQejqlDcrDDVemR0rsp8_9nVdWDzkgXypfNqozZDicn6G81MCOD7BjqjFdtrTxU26lGNFU_8HRQqRm9gpi1HnwTbEZNA_ZuPqUkgCOmTMnTZliwslvoqMFRQrWqDvrFdoXtpW3MyL38IdNDGxeku7Ong6K2wZ3z15_5pvXjdlaeHKjAeco4Kt_O0W43S8_9tk497zMIghqpjw08Qj6fhzZr6Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4da758a13.mp4?token=ny5529t_KWOeJfN8NI2nDBbqmCSBHcbSoZaGPU0yzppghz_gEfNZ1Coc7oIEon1VldLRHZwAvpcpVsEMN2_PqjjoGYL-kX_HZhU8vOAp4fCVROl7PkhTQKlBcli1BQejqlDcrDDVemR0rsp8_9nVdWDzkgXypfNqozZDicn6G81MCOD7BjqjFdtrTxU26lGNFU_8HRQqRm9gpi1HnwTbEZNA_ZuPqUkgCOmTMnTZliwslvoqMFRQrWqDvrFdoXtpW3MyL38IdNDGxeku7Ong6K2wZ3z15_5pvXjdlaeHKjAeco4Kt_O0W43S8_9tk497zMIghqpjw08Qj6fhzZr6Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب اسلامی در جایگاه وداع با مردم در مسجد مقدس جمکران قرار گرفت
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/667714" target="_blank">📅 06:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667713">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d199e23a.mp4?token=bJT_uQLzF-KgjaEXiefCrExILm1v-FcVQhNsUyn3qRyjZCi39-Qx_ttnp29uIMhaeo5V9uik8sQHlwK9NCIEkhbTosaeH62q7pZaydJBje0_KwrzhYC13a2irKkp6q8N0BeNqJlnpxzdxNoFmrksMm_ojHIhWITxKGGmgRlDRt6BGnpyWVrawLppKn4SnE_Ktzj1d-WoOZ7PjpQtW0kioMz1iRdwM9afxJMhV6RbL0nWCPKB2pcJIfYfzG_bMR-I9tCjJJsjxSAQAxU3XA6zAcwvLyaxg0Lslu5hI0mFgaq43m1So7TAMCLbpZ6A6LclrAg3fQosnYFmNpv7bXfBTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d199e23a.mp4?token=bJT_uQLzF-KgjaEXiefCrExILm1v-FcVQhNsUyn3qRyjZCi39-Qx_ttnp29uIMhaeo5V9uik8sQHlwK9NCIEkhbTosaeH62q7pZaydJBje0_KwrzhYC13a2irKkp6q8N0BeNqJlnpxzdxNoFmrksMm_ojHIhWITxKGGmgRlDRt6BGnpyWVrawLppKn4SnE_Ktzj1d-WoOZ7PjpQtW0kioMz1iRdwM9afxJMhV6RbL0nWCPKB2pcJIfYfzG_bMR-I9tCjJJsjxSAQAxU3XA6zAcwvLyaxg0Lslu5hI0mFgaq43m1So7TAMCLbpZ6A6LclrAg3fQosnYFmNpv7bXfBTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوسه حجت‌الاسلام هادی خامنه‌ای، برادر رهبر شهید انقلاب بر تابوت ایشان
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/667713" target="_blank">📅 06:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667712">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/708f8482bf.mp4?token=rdxvrQq5elQr9kBkogX9P5c9epGD4thOtAMRgTZsSZ2LMp8kV692GFr-J_hO3FNERPaGf15TgJhyVO5BRtAWKmAmSPkjQlhyGet6d9kn4e9gcOtttJT25-ng8j5bUbrXSURd_yN1jnDpctoTssGpFrN9SiMQxoY4wNbtzpjlw9VX1stz15Z2pJCP4wg-GSxAXtemhwTVFF-jrnN21dsOFtSmUxsGoke_5eZ574fKbbULHfJ1jy6UqWFnuufIt0lvE3QoSqd_s2sl0wt6dD2qL1CTYxIb_sOf1qWJzd010-kfdUGzKmKzVrJ0m01aqyZeBJcLXbR_XqZfg33TW_b9Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/708f8482bf.mp4?token=rdxvrQq5elQr9kBkogX9P5c9epGD4thOtAMRgTZsSZ2LMp8kV692GFr-J_hO3FNERPaGf15TgJhyVO5BRtAWKmAmSPkjQlhyGet6d9kn4e9gcOtttJT25-ng8j5bUbrXSURd_yN1jnDpctoTssGpFrN9SiMQxoY4wNbtzpjlw9VX1stz15Z2pJCP4wg-GSxAXtemhwTVFF-jrnN21dsOFtSmUxsGoke_5eZ574fKbbULHfJ1jy6UqWFnuufIt0lvE3QoSqd_s2sl0wt6dD2qL1CTYxIb_sOf1qWJzd010-kfdUGzKmKzVrJ0m01aqyZeBJcLXbR_XqZfg33TW_b9Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری عشایر لر در مسیر حرکت به سوی مسجد جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/667712" target="_blank">📅 06:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667711">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f0b87e60.mp4?token=Pgalp4lt-PoqRzK8JqaAVgPKPG16JYwSmQCQIYmHmn7B-bexAl2306Tt3-ZgdJwkEV3VJ67lSAkP5KhA2KAwLf-bauq4vHPj_eUk8-6pnYR-w67YvS7vdQitdb-QMPu_5PD7bRQv_Fcworze6-4hyoGKFZbg-rJas70QG5ghl09iWD5a2awg0pw_rnVpXEmNVbJFqUyQoG7zurHbLShSzaNovAlxxRIRppt7rFBaRsptc12akahvtX5oSF9iYJkt_hyJ8jLsIAFC3NX8qOZsAZqCv4M2aefg5ASWFmuY16ZwfG1-cpuoaooWILCXu781xQvAjeNOkg13VYsT3t7MeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f0b87e60.mp4?token=Pgalp4lt-PoqRzK8JqaAVgPKPG16JYwSmQCQIYmHmn7B-bexAl2306Tt3-ZgdJwkEV3VJ67lSAkP5KhA2KAwLf-bauq4vHPj_eUk8-6pnYR-w67YvS7vdQitdb-QMPu_5PD7bRQv_Fcworze6-4hyoGKFZbg-rJas70QG5ghl09iWD5a2awg0pw_rnVpXEmNVbJFqUyQoG7zurHbLShSzaNovAlxxRIRppt7rFBaRsptc12akahvtX5oSF9iYJkt_hyJ8jLsIAFC3NX8qOZsAZqCv4M2aefg5ASWFmuY16ZwfG1-cpuoaooWILCXu781xQvAjeNOkg13VYsT3t7MeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بانگ الله‌اکبر زنان شهیدپرور در بدرقۀ آقای شهید ایران در جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/667711" target="_blank">📅 06:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667710">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641069ca79.mp4?token=SknC-lOBZ-OQJQkWY5c8ScWM4QNhdnovG5L5WPTKDfauFJ3x1lQz79jn-LrNutMWHY_w6UzB8U2Ha2qrV3jH91rSaX2OthEgjjWmM6COjtbczZTAPdq2eQpx2AG_7SuosomfpV6Lo007p_BPM-h6mGSvmLsayb9Bb2EFfi88jTsSxe9YvIl6JUb9PyjZLx0J_R7jqB3fn6UunpqJcdKcdglnwpLpmCCyWRGCwvd9qwJvQIY3y0eBFdfams6NORSD6JpKtLO1xChzGT8KZgAt-OLNfkMoi8Z9Js1Xclfun4eXGIK_XDXAkPVsPOJh5nsUq6VPFD0yfpLrQRPU0n_ELIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641069ca79.mp4?token=SknC-lOBZ-OQJQkWY5c8ScWM4QNhdnovG5L5WPTKDfauFJ3x1lQz79jn-LrNutMWHY_w6UzB8U2Ha2qrV3jH91rSaX2OthEgjjWmM6COjtbczZTAPdq2eQpx2AG_7SuosomfpV6Lo007p_BPM-h6mGSvmLsayb9Bb2EFfi88jTsSxe9YvIl6JUb9PyjZLx0J_R7jqB3fn6UunpqJcdKcdglnwpLpmCCyWRGCwvd9qwJvQIY3y0eBFdfams6NORSD6JpKtLO1xChzGT8KZgAt-OLNfkMoi8Z9Js1Xclfun4eXGIK_XDXAkPVsPOJh5nsUq6VPFD0yfpLrQRPU0n_ELIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وداع علمای قم با امام شهید امت
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/667710" target="_blank">📅 06:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667709">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bae6eed2.mp4?token=KDZSqFJCBnkZWI_s_RvuWPHiludLNgJ9pHRRW1e9PkFtMUv7UzsKvf77RTFn-hgEKcGz41M8uz9aqJYbR-yTI5nfOMNoxwUsGeCbxfmUoeWGA6CsY6dXo2nMAl52soaEuEf_FGSJzDi8X1EtybBaAZUKP1hM_F8Fa9IE6iUU1xwGeVpGEQ2gSex1mTxEiJTAsvdr5X_rmJC8PdlLhSfbTdaLh1oYizNFu06UcnCG6tBvIOQ3Z_AH8mkShN8BnqDbl5NX23wEpI0Xl3haQJG2dmGwnCWWkqQSm2Hk__b72EOKSLp4_kvuNM2mH3pWoElGH6tWhBNe48GwneDynEzBL5jZHn8Co-O3Rnzy3nqAV9WoPfZeA7-eAy6cly1mc0Azc88OTTRbGHoHpjcReDhPuw0nemKCdlc08LuHiZ1y4ebHPaO1uUHIFoqJJjwSsYtta0jvR0aQ6jelCeyqFlnINBx9g3KpaBx7KMf0PA99EE49R51iMnXUqIhmwxk3XDY7F2aaH2Y9EygqgYM9TeL1ARk3yYMBQyi1MBGNbaucwpbdDVMHSx8qdzuDTWsvVJzsvLVFe-EBXuTdvKwiPirAzuhjHWzrlgrXom5I0vFtN_pBoN7tZjks0SAqaMnmCVdPlXUBvG9cvgjmcvKPn1GMypMrVz6PPFUi8AfKo45xHjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bae6eed2.mp4?token=KDZSqFJCBnkZWI_s_RvuWPHiludLNgJ9pHRRW1e9PkFtMUv7UzsKvf77RTFn-hgEKcGz41M8uz9aqJYbR-yTI5nfOMNoxwUsGeCbxfmUoeWGA6CsY6dXo2nMAl52soaEuEf_FGSJzDi8X1EtybBaAZUKP1hM_F8Fa9IE6iUU1xwGeVpGEQ2gSex1mTxEiJTAsvdr5X_rmJC8PdlLhSfbTdaLh1oYizNFu06UcnCG6tBvIOQ3Z_AH8mkShN8BnqDbl5NX23wEpI0Xl3haQJG2dmGwnCWWkqQSm2Hk__b72EOKSLp4_kvuNM2mH3pWoElGH6tWhBNe48GwneDynEzBL5jZHn8Co-O3Rnzy3nqAV9WoPfZeA7-eAy6cly1mc0Azc88OTTRbGHoHpjcReDhPuw0nemKCdlc08LuHiZ1y4ebHPaO1uUHIFoqJJjwSsYtta0jvR0aQ6jelCeyqFlnINBx9g3KpaBx7KMf0PA99EE49R51iMnXUqIhmwxk3XDY7F2aaH2Y9EygqgYM9TeL1ARk3yYMBQyi1MBGNbaucwpbdDVMHSx8qdzuDTWsvVJzsvLVFe-EBXuTdvKwiPirAzuhjHWzrlgrXom5I0vFtN_pBoN7tZjks0SAqaMnmCVdPlXUBvG9cvgjmcvKPn1GMypMrVz6PPFUi8AfKo45xHjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«محراب جمکران»؛ لحظاتی خاطره انگیز از حضور رهبر شهید در مسجد جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/667709" target="_blank">📅 06:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667708">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7406fc2868.mp4?token=YgGnylfRSAdB-qP2v0-yD9KBwHshnRSKH5n4cUFFh206EyMD2d2-RHK3JIA2vxFkhGvvt2RPciGe0GGHjimRcI9-n4b_6hSYJvePMEYkhjef4j76qqphBn6R4lKAAQrQk0rtLOZH9J10I7iRdXAmPyifm1_Juea_bJ2puNSltUyrDlPCgsY8gulKVu-P26JHsbtOFiw9_x5_bJ3ihmrxOOo_i4tAGqexeSgmruuI4cwVWgToCG59-sE75RA9Z1k1tTYc8jxHFnf2u9VtCLrDTihZ2kZgFlektfSxpUri5sOyvPP83bWG0h-7ok7fti6GWLyJ5mmFHWeyCf9FBuCKWRLI-C3EfsG9Ih5rVm8_B35g9lt1tZFQUUmNbJ7EwFJgqTvww9wYgO6NG6tolWdXCx8N7BLlHXtl2uhr2HlhuYeQJRjYL1N58csNs8TyU1a3dA3mcMMrXDFNJLiI9b-3zizCt5ZN72GeSZ9TtHLlcySPrdkNzgQ6K6da1mI8bYZXJZ7ygvAzDr2RQWXtq9PMQ0Ei1Xb2VeoBT0pEqek8VRExXDph-4tM2IkAQxshhgfE-idB1lYcWwmI6qDp6c5dBt3JDe9dRWNkmbM8cxDdf1AIi34aqTkdxpOc6WYTidxKHKiMRVVxNA337SwWxKtUyIyewJdWruBjPKGe_xouUxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7406fc2868.mp4?token=YgGnylfRSAdB-qP2v0-yD9KBwHshnRSKH5n4cUFFh206EyMD2d2-RHK3JIA2vxFkhGvvt2RPciGe0GGHjimRcI9-n4b_6hSYJvePMEYkhjef4j76qqphBn6R4lKAAQrQk0rtLOZH9J10I7iRdXAmPyifm1_Juea_bJ2puNSltUyrDlPCgsY8gulKVu-P26JHsbtOFiw9_x5_bJ3ihmrxOOo_i4tAGqexeSgmruuI4cwVWgToCG59-sE75RA9Z1k1tTYc8jxHFnf2u9VtCLrDTihZ2kZgFlektfSxpUri5sOyvPP83bWG0h-7ok7fti6GWLyJ5mmFHWeyCf9FBuCKWRLI-C3EfsG9Ih5rVm8_B35g9lt1tZFQUUmNbJ7EwFJgqTvww9wYgO6NG6tolWdXCx8N7BLlHXtl2uhr2HlhuYeQJRjYL1N58csNs8TyU1a3dA3mcMMrXDFNJLiI9b-3zizCt5ZN72GeSZ9TtHLlcySPrdkNzgQ6K6da1mI8bYZXJZ7ygvAzDr2RQWXtq9PMQ0Ei1Xb2VeoBT0pEqek8VRExXDph-4tM2IkAQxshhgfE-idB1lYcWwmI6qDp6c5dBt3JDe9dRWNkmbM8cxDdf1AIi34aqTkdxpOc6WYTidxKHKiMRVVxNA337SwWxKtUyIyewJdWruBjPKGe_xouUxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای مسجد جمکران در مراسم تشییع پیکر پاک رهبر شهید انقلاب و خانواده ایشان
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/667708" target="_blank">📅 06:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667707">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5477347a.mp4?token=ukUsrvBp7kDg1F3ok-4wT8skJ8GWSfyKssIE8v7qsnzykTIFwNmooIszqKNHYqKOHumMozYc-d2Vg3Zfj5G4aZHEGBTk-mh34O3J5ps6SqajYR2kZ7INik8oNRBiVnpIP6DtFg-p3iY90l_lhSJJA6DsmL0q7TFxcQ_AwAa9zyktk5HWWOEVS2VhUfigtlKtqsTgywsOLBXv0zGZXLg3xTWfApOKMK5c0-RgkedcA2xelYHM7jQFuQJe7N0-9XtPlb13NQERoOiDiBAJ8idhhWR1YYuGx29YtM1A5v14gnj7uZ2gdAZlIcOp4OOGZzsKcBaW7OdcAae4ZCkhmb6HfKUOWUaQjkJ_SkVfjTppRKjGLE9v8GaSkp5k4QWeNfuoUdv39kafDwsjQXVw4OV4eNcndreuPCiZHGlEI0s0oyc8FZIVRAFmMT-dLBvxcu3mzdzM0bB4jCEPYLDlSGtjv3y2f27JxVcHm1VOgWvQU7G1kc-LnNzzQ59ul3G3Mxf6xXxRlXfB_LLWpMewV5sjDLM9VHOXYdUTQ1YJq9wNDx22wsjUuj5ZbBv7AH9QqEcDHh3H6xL-yRwk6HQeAAzeifWA1GF4uyU9in7Y1W2s8qlmVakTW4CRu43AWz_QuG05-kRPOnElDdExdnPCm1Yc7giq_dRmWTCR68ODtE01V-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5477347a.mp4?token=ukUsrvBp7kDg1F3ok-4wT8skJ8GWSfyKssIE8v7qsnzykTIFwNmooIszqKNHYqKOHumMozYc-d2Vg3Zfj5G4aZHEGBTk-mh34O3J5ps6SqajYR2kZ7INik8oNRBiVnpIP6DtFg-p3iY90l_lhSJJA6DsmL0q7TFxcQ_AwAa9zyktk5HWWOEVS2VhUfigtlKtqsTgywsOLBXv0zGZXLg3xTWfApOKMK5c0-RgkedcA2xelYHM7jQFuQJe7N0-9XtPlb13NQERoOiDiBAJ8idhhWR1YYuGx29YtM1A5v14gnj7uZ2gdAZlIcOp4OOGZzsKcBaW7OdcAae4ZCkhmb6HfKUOWUaQjkJ_SkVfjTppRKjGLE9v8GaSkp5k4QWeNfuoUdv39kafDwsjQXVw4OV4eNcndreuPCiZHGlEI0s0oyc8FZIVRAFmMT-dLBvxcu3mzdzM0bB4jCEPYLDlSGtjv3y2f27JxVcHm1VOgWvQU7G1kc-LnNzzQ59ul3G3Mxf6xXxRlXfB_LLWpMewV5sjDLM9VHOXYdUTQ1YJq9wNDx22wsjUuj5ZbBv7AH9QqEcDHh3H6xL-yRwk6HQeAAzeifWA1GF4uyU9in7Y1W2s8qlmVakTW4CRu43AWz_QuG05-kRPOnElDdExdnPCm1Yc7giq_dRmWTCR68ODtE01V-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیتی که انتها ندارد ...
🔹
مسیر حرم بانوی کرامت تا مسجد جمکران مملو از جمعیت است؛ موجی از حضور که لحظه‌به‌لحظه بر گستردگی آن افزوده می‌شود.
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/667707" target="_blank">📅 06:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667706">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8c37f805.mp4?token=gJocUcyG736kB0k5y4dBTv4GDlFCk8T0iPHjkm80NiVfAWRlBqhzWjQYaXoZeXuM8qxxatYq3WgVNbdKTd9auBFlUyzldQajXweaH2-3ettSCnXAwl3YcUglCTKk1hsEClCgJoDqfD3aTaoTKMVV16_1R8Jl1FNQULAkxK2kjMgDguX87h0NHJEG60v8ujmmZJJkBNX-YZD3DxKdLTNN2U86fq1bPORKgSa1Cs9CqREqFGv41o3YxNnGOdh0GMaDHnyowE4ZO4s6hEJWbySbhaKvz1L4mCA8OC5DWvz1rOKehxPC-eM73ZJy0JGYdL40uD6Hb1BoWmVugEbNu5MAnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8c37f805.mp4?token=gJocUcyG736kB0k5y4dBTv4GDlFCk8T0iPHjkm80NiVfAWRlBqhzWjQYaXoZeXuM8qxxatYq3WgVNbdKTd9auBFlUyzldQajXweaH2-3ettSCnXAwl3YcUglCTKk1hsEClCgJoDqfD3aTaoTKMVV16_1R8Jl1FNQULAkxK2kjMgDguX87h0NHJEG60v8ujmmZJJkBNX-YZD3DxKdLTNN2U86fq1bPORKgSa1Cs9CqREqFGv41o3YxNnGOdh0GMaDHnyowE4ZO4s6hEJWbySbhaKvz1L4mCA8OC5DWvz1rOKehxPC-eM73ZJy0JGYdL40uD6Hb1BoWmVugEbNu5MAnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین انداز شدن صدای آقای شهید ایران در مسجد جمکران و گریه‌های بی امان مردم عزادار
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/667706" target="_blank">📅 06:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667705">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae271e6a3e.mp4?token=a8S81seqZSVBzTkpuNHlRY3kyO3lnyXwGGOeg71MfE8JDHQMZ9ZbYzrLukt59Kd0f26ORgG5tTcnizlZnBHn17dPjZJS1qQRtph_shwsquL1y3q0uSAd8GZRZ7ocXyLH5cqmP582bR5nZas-_AvZXY8K4d9FOMxLd_fCois2sj_3HSn1kN3d5VZD-KOMfPNFoSew3CFuljiiyfpfJHE5SreJEdiq-M8L0clP9gX9o6PIwCLwgL0w0fKqCj-rVTYj6iC9bwaA-e69oB8akj4-w-szD1bPJCQe-4i7MJuDNMI6COzdHoZ1nAKEqzmVlQHdwIY8310R7KiCCA5C8SFf2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae271e6a3e.mp4?token=a8S81seqZSVBzTkpuNHlRY3kyO3lnyXwGGOeg71MfE8JDHQMZ9ZbYzrLukt59Kd0f26ORgG5tTcnizlZnBHn17dPjZJS1qQRtph_shwsquL1y3q0uSAd8GZRZ7ocXyLH5cqmP582bR5nZas-_AvZXY8K4d9FOMxLd_fCois2sj_3HSn1kN3d5VZD-KOMfPNFoSew3CFuljiiyfpfJHE5SreJEdiq-M8L0clP9gX9o6PIwCLwgL0w0fKqCj-rVTYj6iC9bwaA-e69oB8akj4-w-szD1bPJCQe-4i7MJuDNMI6COzdHoZ1nAKEqzmVlQHdwIY8310R7KiCCA5C8SFf2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرار گرفتن پیکرهای مطهر شهدا در جایگاه ویژه وداع در مسجد جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/667705" target="_blank">📅 06:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667704">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9290566f32.mp4?token=X-4_2OBbVAO6QHYunY4HMen85ATDDk37CETtCc3z6zSQ9oE2bDjPuPfh7ojQMfKffw-NFJt48QAzkEWMtYBT_Gq451vd_Bwm40-_0I-tWPeQwThsDwVTf6H8RdGWaNfNa7IuRhNL3r8deEnYsOHR7dwvamT-SrXcdCwX1fRcKQ-_ykgqdsAR_cr40eayF05sB53yXmJ5zxMWVjbdVSdriZG8yWHG6Q112gXu18U1E3qxmGxJjAp37k1NXYEXcEb093fviqYsAM-oE05GIfd6lAOsWjsdy8w-TN81N4OOIZehjgQBGzEy-kAtOua5PRICvoxHddtaK-2YHPtt8uKfRketXuZr6Ca4s2d4eofUTwNcdDK1jYUveJNxL4ns2kVPaMDcZlCmfrEhA6Rbq395f6nB4CnvLFV0_pYpem29Ott3K2pcyp_2Z6Z1KKno3yjL4Vqsuyag00ocOd4O8qFdDj3RvmouEwqbSdf2FVKPdKUSBmR2wd89Mf4PMI8TYs3du0I-5uNwfjywcQqcSa31E2I2_1P6qcqwtbZnCtv2GTFkIQJQu7pONtGjNmSZMlnrkbXW-0n61YgN2wf7P290pYMHYJIZAmrqmDvpl5laOiDTlKXN0-4UljNwAlo-rLD4IepL41d2gGbmwMYdp3gNrjOZI2Z8Fl589wnPpVT-fYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9290566f32.mp4?token=X-4_2OBbVAO6QHYunY4HMen85ATDDk37CETtCc3z6zSQ9oE2bDjPuPfh7ojQMfKffw-NFJt48QAzkEWMtYBT_Gq451vd_Bwm40-_0I-tWPeQwThsDwVTf6H8RdGWaNfNa7IuRhNL3r8deEnYsOHR7dwvamT-SrXcdCwX1fRcKQ-_ykgqdsAR_cr40eayF05sB53yXmJ5zxMWVjbdVSdriZG8yWHG6Q112gXu18U1E3qxmGxJjAp37k1NXYEXcEb093fviqYsAM-oE05GIfd6lAOsWjsdy8w-TN81N4OOIZehjgQBGzEy-kAtOua5PRICvoxHddtaK-2YHPtt8uKfRketXuZr6Ca4s2d4eofUTwNcdDK1jYUveJNxL4ns2kVPaMDcZlCmfrEhA6Rbq395f6nB4CnvLFV0_pYpem29Ott3K2pcyp_2Z6Z1KKno3yjL4Vqsuyag00ocOd4O8qFdDj3RvmouEwqbSdf2FVKPdKUSBmR2wd89Mf4PMI8TYs3du0I-5uNwfjywcQqcSa31E2I2_1P6qcqwtbZnCtv2GTFkIQJQu7pONtGjNmSZMlnrkbXW-0n61YgN2wf7P290pYMHYJIZAmrqmDvpl5laOiDTlKXN0-4UljNwAlo-rLD4IepL41d2gGbmwMYdp3gNrjOZI2Z8Fl589wnPpVT-fYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقامه نماز دوم بر پیکرهای مطهر خانواده امام شهید امت
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/667704" target="_blank">📅 06:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667703">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
فیلم کامل اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان توسط حضرت آیت‌الله جوادی آملی در مسجد مقدس جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/667703" target="_blank">📅 06:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667702">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2472917a.mp4?token=m0BoC7jAoGFMsk4hXo9nwkxvYn7dEd8N7XkHwJutGIjJ4kmIUWG4wPflwRS-yf__qcGmobp4QEZ2VN9iRgIWmo6DOxgZp19g8z-jEWE1j7UKe26UNxRv4xubEfQNWT5f8vSNA1U6kP0TLvdkod1n5N75OAoOWqQnVdxY0F49o7z6vSxWjIVZzQRf8Mbetx2P4EvPhm2zcNViuVqZ0hEPHrudwPjDLdeVd8A2Otu1h2PDnY1Imz8GnVimteAiBzKM0MwZjz28yqexrtSnYZGZ88Vazl-sD3B1G3LSZIBgzar8pvjaKfn9_gZXXgENx-9ZGDoGEkhhlj89CpGvsDsJfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2472917a.mp4?token=m0BoC7jAoGFMsk4hXo9nwkxvYn7dEd8N7XkHwJutGIjJ4kmIUWG4wPflwRS-yf__qcGmobp4QEZ2VN9iRgIWmo6DOxgZp19g8z-jEWE1j7UKe26UNxRv4xubEfQNWT5f8vSNA1U6kP0TLvdkod1n5N75OAoOWqQnVdxY0F49o7z6vSxWjIVZzQRf8Mbetx2P4EvPhm2zcNViuVqZ0hEPHrudwPjDLdeVd8A2Otu1h2PDnY1Imz8GnVimteAiBzKM0MwZjz28yqexrtSnYZGZ88Vazl-sD3B1G3LSZIBgzar8pvjaKfn9_gZXXgENx-9ZGDoGEkhhlj89CpGvsDsJfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از حضور پرشور مردم در نماز بر پیکرهای مطهر شهدا
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/667702" target="_blank">📅 06:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667701">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38904b92d0.mp4?token=J6bUez6inClc3WSchBJ7SIYdFnPhuSDwHDGBBXygGW7CJtre1qkQxJnQCjFxYzcmNfu5uqPY1nA1MJJ0aLBNZS-gcEbPJvZYH5T8_nry0q-RRkoFeomrYzDEolW6dja_zzyfycmFrYU-kfLjK_DyWQbECWz2ZhnCLhZFchgjkdw4lneg44y9ZXMdMTfdLTwHsV8BXOeZaedPUepGFikA4gPMY1yp0mpoKw8NLUpMe1dCAZGsFASI20PmvQhNsvEBPCtECu8EzGGZN4p3Qv8Uj5P6YktCj9ysoSJ36OZgVsSl2ss35pv7XY5ltNLzS19o2PZLRNPwbP6mjG_Guc0g9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38904b92d0.mp4?token=J6bUez6inClc3WSchBJ7SIYdFnPhuSDwHDGBBXygGW7CJtre1qkQxJnQCjFxYzcmNfu5uqPY1nA1MJJ0aLBNZS-gcEbPJvZYH5T8_nry0q-RRkoFeomrYzDEolW6dja_zzyfycmFrYU-kfLjK_DyWQbECWz2ZhnCLhZFchgjkdw4lneg44y9ZXMdMTfdLTwHsV8BXOeZaedPUepGFikA4gPMY1yp0mpoKw8NLUpMe1dCAZGsFASI20PmvQhNsvEBPCtECu8EzGGZN4p3Qv8Uj5P6YktCj9ysoSJ36OZgVsSl2ss35pv7XY5ltNLzS19o2PZLRNPwbP6mjG_Guc0g9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعاهای خاص و همراه با بغض آیت‌الله جوادی آملی هنگام نماز بر آقای شهید ایران
اللهم انه نزل مجاهدا موحدا
اللهم اللهم اللهم انه نزل عندک شهیدا
اللهم انه نزل عندک قتیلا للاسلام قتیلا لامه مسلما
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/667701" target="_blank">📅 06:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667700">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
آغاز اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان توسط حضرت آیت‌الله جوادی آملی در مسجد مقدس جمکران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667700" target="_blank">📅 06:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667699">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNx4oGnoHtfOORhmBHYI0bzwXYYq-UTq138ax99HXXQxjO54AO_O35LChQm3zHXxWFace-4kvsKE0TkZqPeqPWZSFDr1A3buW0QA4Z0XEdhiO1sgbI0KOYvEXRLiRsJUUF-Mwc-HQ8o4Ups_6yChIOZLcXRcPEtvcVhmmPiEi1C_pEee-HDVG4j9EeNNiXnPCCV99EJddbJMKEGwthlIeuOGaiEq8nbpLEpT2ik7iZ0hFdNmzc2vi53mEXpuMsix_FOYCrGrgoLbHsZm9s2Tn8Cg6KOooy_2tGfCyfBQep59CUdq0_JERUqMcAKcW1XNEZjTsYAzLooxwrRYUG0wcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دخالت ترامپ هم مانع شکست آمریکا نشد
🔹
حالا جام‌جهانی بدون میزبانان پیش می‌رود؛ بلژیک با تحقیر آمریکا به دور بعد رفت
🔹
بلژیک ۴ - ۱ آمریکا
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667699" target="_blank">📅 06:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667698">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cb281cce.mp4?token=E4uW4w8GbD0YJ-va-Aygx8VU4KXlyWMPB-w13bYrXAUnMateglg314vd_yTbIUjgYY-zfwcOUq6WQ-tnE1dYb6s47kcheMtarTDqwZJQpBtey1lB_Z42wgYuGI6Bnj5ThQ_xRcJrtzBLI5LfcWs8HzQ4yGfw3AeXJCGQNIlavolWda2tkspHPFifQ5mu4Gh8THZJ4ObaOi3W2SQuFLhyfPt44inCS9FrEqRXJxs5hgjAywJJaiQFlQm3pC821DUkbrJNJ1_abqFgyVAO-obW1ETCbah-WttD2Rtknu7cNbpnbqUI-LFW7HCdKpgi_DEXW_5RzLN48h44G5dRM4OwEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cb281cce.mp4?token=E4uW4w8GbD0YJ-va-Aygx8VU4KXlyWMPB-w13bYrXAUnMateglg314vd_yTbIUjgYY-zfwcOUq6WQ-tnE1dYb6s47kcheMtarTDqwZJQpBtey1lB_Z42wgYuGI6Bnj5ThQ_xRcJrtzBLI5LfcWs8HzQ4yGfw3AeXJCGQNIlavolWda2tkspHPFifQ5mu4Gh8THZJ4ObaOi3W2SQuFLhyfPt44inCS9FrEqRXJxs5hgjAywJJaiQFlQm3pC821DUkbrJNJ1_abqFgyVAO-obW1ETCbah-WttD2Rtknu7cNbpnbqUI-LFW7HCdKpgi_DEXW_5RzLN48h44G5dRM4OwEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ انتقال پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان به جایگاه اقامه نماز بر پیکر ایشان در مسجد مقدس جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/667698" target="_blank">📅 06:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667697">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01056f55dd.mp4?token=mPf_0xDPf_YqVi3cah484hCTWQHHPhgenR2NKZs0cU8tUz3sHkTihyNkYlOjXyF2sQHaBErZcaRwD9x2Be79WYl1o9f9ciiLgrNRjR6SF95S8M6xhnmgW-o-RleTHbcGcWoEqZ0f406v5tW--2xlMVa3o8WlskKaUNrLYAp8KbyNNi4bIF3GqOT8J5WBD3gTB1Hc9bMr0L5mGq0x4AeK6WzGMaaUcD9dgsFVb33p8K-GhLLRDdHjhs02V-CsO9cPcbn-YIKvkag-nJl3VDQOkWwChUyVi98sVbSc99J_7lcIPTH-kBgO5PaaFBYo6YkEe1XSdluHfJE4h-78yrxclQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01056f55dd.mp4?token=mPf_0xDPf_YqVi3cah484hCTWQHHPhgenR2NKZs0cU8tUz3sHkTihyNkYlOjXyF2sQHaBErZcaRwD9x2Be79WYl1o9f9ciiLgrNRjR6SF95S8M6xhnmgW-o-RleTHbcGcWoEqZ0f406v5tW--2xlMVa3o8WlskKaUNrLYAp8KbyNNi4bIF3GqOT8J5WBD3gTB1Hc9bMr0L5mGq0x4AeK6WzGMaaUcD9dgsFVb33p8K-GhLLRDdHjhs02V-CsO9cPcbn-YIKvkag-nJl3VDQOkWwChUyVi98sVbSc99J_7lcIPTH-kBgO5PaaFBYo6YkEe1XSdluHfJE4h-78yrxclQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ تصاویری از پیکر مطهر «آقای شهید ایران» در مسجد مقدس جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/667697" target="_blank">📅 06:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667696">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87d0189ed.mp4?token=J9VD6YZLJuk8741PftqvSHfvun1aQlCN7b0o5JnmsNDIabWYuB6YPwAqBpKvbD5VPOabffD2H1Le4vAGBI1Uxahb9c114szpn5QKlaVt2yJGxdLAwIvtFvmoT2DlbuRQVbVh0axgGy18kMIFhqRcz6sUXPcvWQHh_RK0FyR_rBA3RJhdE9aAm5ncQ4NuJ3sCjDNaGLkTICXGDSRWTi72P8_Qcy820vATPCG1NiNsCYVUBP8X_OaEjKuLuKTCBnPugFJT6T8hfA7gVlPPANWYTHsa7O-Idb6LHFkJvBPdAfdQIX8d_VhQbyGwpk-LlZHi-6NV4WvwMAj6uCvh9kK47w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87d0189ed.mp4?token=J9VD6YZLJuk8741PftqvSHfvun1aQlCN7b0o5JnmsNDIabWYuB6YPwAqBpKvbD5VPOabffD2H1Le4vAGBI1Uxahb9c114szpn5QKlaVt2yJGxdLAwIvtFvmoT2DlbuRQVbVh0axgGy18kMIFhqRcz6sUXPcvWQHh_RK0FyR_rBA3RJhdE9aAm5ncQ4NuJ3sCjDNaGLkTICXGDSRWTi72P8_Qcy820vATPCG1NiNsCYVUBP8X_OaEjKuLuKTCBnPugFJT6T8hfA7gVlPPANWYTHsa7O-Idb6LHFkJvBPdAfdQIX8d_VhQbyGwpk-LlZHi-6NV4WvwMAj6uCvh9kK47w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوسه پدر زهرای ۱۴ ماهه بر تابوت دختر شهیدش در مسجد جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667696" target="_blank">📅 06:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667695">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3103f71a0f.mp4?token=TBBIqnvjbt2s8XTyOYUzGIW6CJ9MBy_q9CoLuo0rFPN4Qp4MT8K2O6-Lwoweh6-Wv16cS_BlzY2WQxTX3w7rRT9jw50obhjoCjwy4jX2VB5T-ZzS_YwyBMLePfpzyqxFsCB9JCy9H3YmB5MlNY1cUye6pkzztqviT5MnI-JqzOYfY7Q65ZMg3Shza5VH4v16_ocZgOlK8DcFjfkWQ8UweoaWl8aEV-P1ymAHFiYmRNmXY6WyBSaRwL9S1VpeKXgoLpuo006jMUG8B7b-aMd7k2S9hWGH2nmJq3o1SjGcoIZwBWHzWpZbPzO8WWodAZKdT705ey_AotLiMO-ikxIO4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3103f71a0f.mp4?token=TBBIqnvjbt2s8XTyOYUzGIW6CJ9MBy_q9CoLuo0rFPN4Qp4MT8K2O6-Lwoweh6-Wv16cS_BlzY2WQxTX3w7rRT9jw50obhjoCjwy4jX2VB5T-ZzS_YwyBMLePfpzyqxFsCB9JCy9H3YmB5MlNY1cUye6pkzztqviT5MnI-JqzOYfY7Q65ZMg3Shza5VH4v16_ocZgOlK8DcFjfkWQ8UweoaWl8aEV-P1ymAHFiYmRNmXY6WyBSaRwL9S1VpeKXgoLpuo006jMUG8B7b-aMd7k2S9hWGH2nmJq3o1SjGcoIZwBWHzWpZbPzO8WWodAZKdT705ey_AotLiMO-ikxIO4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای هوایی از حضور خیل عظیم عزاداران در مسجد مقدس جمکران و خیابان‌های اطراف پیش از اقامه نماز بر پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/667695" target="_blank">📅 06:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtoxOnsHaOMvnZbh7GihJf0NMCCPgVEDvdAbn1G-eeRjdGS8w4uHnO5rZHUWTXkhqx4ymTFoe0eKk84eQIp5lLOZ-B--yc9EYkWm0dcjj2dNH51siUqBusEH0tXChEsfPISZ5SaEnqr8X_BSBBE6_wySSayciMBz13hyBVRD2QOCe5yGeEhkx3Sb3-5lOpmIdYygUpvGmHIQIrxAB_wxbfYgfwoYv7iFbAQE5_qYDoacko99m2pZZFle-A3OcxRQQ4WDJN6eS_N-4FH6ybZJcN7bzeAA42lT0v-uCA3Jnldp01190St8RBNqTPrqMTS2btXe7RIe8bMJWvp0IMP6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۱۶ تیر ماه
۲۲ محرم ‌۱۴۴۸
۷ جولای ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667694" target="_blank">📅 06:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667693">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AV5DoRVyfLQvZIB4d8Lt0nXz33vAeEpDZUk2fRTJKPzOAcuSyRGOFfHN6_U-HR3UVcLuLCWLi0IBxVhk_HykUINKEjbO2_UXC3UE9DYlvZ0ULxt-PhigWx7Gkza7zBh0uCUeZhGbO9UGIpAqdF3tjdiuJ1cnfLPgKXEcsjLIOazLNMgEcxSkFB082B0M2_-LAWHr7vOyOvH5-uutJTHxkuxPXrXDuTuIzRWIvawd68EVtoM-_25_zXfVcRqxc2dOcGthFWz7lFaqa4aZ6RLc-hAYBkBygamdk975PTbUR6hbAtmx5swnn-1zO3KHRX1r2vPSH0VMdbRO6UcwgK0d7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک عما
ن
سازمان عملیات دریایی انگلیس بامداد سه‌شنبه:
🔹
یک نفتکش در حدود ۱۵ کیلومتری شرق شهرک «لیمه» مورد اصابت یک پرتابه نامشخص قرار گرفته و دچار آتش‌سوزی شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/667693" target="_blank">📅 03:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/107cdb1cba.mp4?token=cYONGKA4Dpv0KDY0R1b6R76zBfg3sck7AeWhGcYKE_Jnhxy-Z_CfiYlyRYqKWbF_5zEtLsTgvSAHWm3naQeEAO2vlWueOqS2DAArCgRjCzZ5MDo3UJuBzTyoJBlFhyWEE1i3pOo-iU6tIFklQTSfOd14RBOYWBcv3jnQiTjTlET42laTpZ9IfyBwTU6XzdKr42Xv1GGR_DYtqxM1lGEAulnTsSAoIxbwnMiOc9EH-V39ywe0LGk5FSF4yOOLtMuzaBfPKjVqI_kMF0atZzcprW4DzxYNuo7rzzKTtyn5z4ODvYKQmRTEnROBli3C_DZHhqOSR4jZHVn2rs2jBZSKLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/107cdb1cba.mp4?token=cYONGKA4Dpv0KDY0R1b6R76zBfg3sck7AeWhGcYKE_Jnhxy-Z_CfiYlyRYqKWbF_5zEtLsTgvSAHWm3naQeEAO2vlWueOqS2DAArCgRjCzZ5MDo3UJuBzTyoJBlFhyWEE1i3pOo-iU6tIFklQTSfOd14RBOYWBcv3jnQiTjTlET42laTpZ9IfyBwTU6XzdKr42Xv1GGR_DYtqxM1lGEAulnTsSAoIxbwnMiOc9EH-V39ywe0LGk5FSF4yOOLtMuzaBfPKjVqI_kMF0atZzcprW4DzxYNuo7rzzKTtyn5z4ODvYKQmRTEnROBli3C_DZHhqOSR4jZHVn2rs2jBZSKLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت خبرنگار خبرفوری از تشییع رهبری در جمکران؛ ظرفیت جمکران درحال تکمیل شدن است/ پناهیان در جمکران: مسئولان در خونخواهی رهبر شهید صریح‌تر سخن بگویند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/667692" target="_blank">📅 01:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2N0GMkTcMHi6JDxKqHiGivVl5BPvsuNDK1QOtzSX4fU6CH-PnTVuAXLhI-UT_9CF8aaC3OSj4rBx3_shzRyakyPuGJcLkJFHKOvEeir26iTJ_68zOpMTCC5x3Uf3z8VOkUquvcsO2wnKp9vAQTTcT4TacP4iUmPdTsmdxMlpAeZrX3jDmPIUvKVhHrRDhYaT5XnHmCTsDYqtGW8PsLErlcSp9eLLt82Oaq47ycjaso8tg6lJhyLfmmkwnMJmc5u4pN0wKtklNsNzqbeFhYWEG0TvbCw-cLqDXPrmBWwW636eShncLQFdvfUlYWBwqKzEGV3aYRWOpnrBR8Drn_jgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استانداری کربلا با عنوان خیر مقدم به اولین زائر اربعین امسال به پیشواز تشییع رهبر شهید انقلاب اسلامی رفت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667691" target="_blank">📅 01:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9965753a95.mp4?token=QrYmnUKHGpInZX3IgD8vzc2zHdKm2t7w9pleNYy6vvkc7VdPIKwk31RGdegtIRzKw__-X_MK6YdzG3VjIoXT1dNAq8vqBJecZEAiQt8OeKxq45rFrDV0v0CrzFpZQBgzpKMXB-wRPFd3CO0n-Zwop5oVsJA4hD5L4iwUveEpKqvCatFQUZVs5L5emsS2kFHrsB60NvaB26AMLdZt4PMoayvBUAx4Y3ysc6v5mtaz6QzeelTJV6jyj9eTA7_QXQIYQvEO6LF7l4UrB3O01-8WHEOoD9wr6-wTuwwTU_4O7gCiaUahk6AqhWq3gbml7F6vcq7UmewVYEh8F2A59AIeGXDwGwUi-gJPm7Os3MejzZGS5VUSPSzHPwka4EEcvyAWBh4gd_NqvpYNTAJTEmSJkmoYVgq_t5-AYJ8SYisuOHisN5p2-1bJINGSvgWfuGlumXZmzM1dIWTY2rYF0JPoyN0CyU9JThku1C8SGSmuOBtiT7me9HpO_VxHEJ8Le94VKvZKdjupQxBdlYyu4n7gmFjoZQvOHeGSr4yJjUGgai60VjeYGJH5HlgmQqMZgj0mjRgTeW_KWplHl2yX5Tes9VymyhVYGvqdN033TJdO_HgHJTP9soAWrt2o4i5n21d3inQyzP0Xn0-XsemoCKVfx--g_mg6TjYTwn_C7B7-ueA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9965753a95.mp4?token=QrYmnUKHGpInZX3IgD8vzc2zHdKm2t7w9pleNYy6vvkc7VdPIKwk31RGdegtIRzKw__-X_MK6YdzG3VjIoXT1dNAq8vqBJecZEAiQt8OeKxq45rFrDV0v0CrzFpZQBgzpKMXB-wRPFd3CO0n-Zwop5oVsJA4hD5L4iwUveEpKqvCatFQUZVs5L5emsS2kFHrsB60NvaB26AMLdZt4PMoayvBUAx4Y3ysc6v5mtaz6QzeelTJV6jyj9eTA7_QXQIYQvEO6LF7l4UrB3O01-8WHEOoD9wr6-wTuwwTU_4O7gCiaUahk6AqhWq3gbml7F6vcq7UmewVYEh8F2A59AIeGXDwGwUi-gJPm7Os3MejzZGS5VUSPSzHPwka4EEcvyAWBh4gd_NqvpYNTAJTEmSJkmoYVgq_t5-AYJ8SYisuOHisN5p2-1bJINGSvgWfuGlumXZmzM1dIWTY2rYF0JPoyN0CyU9JThku1C8SGSmuOBtiT7me9HpO_VxHEJ8Le94VKvZKdjupQxBdlYyu4n7gmFjoZQvOHeGSr4yJjUGgai60VjeYGJH5HlgmQqMZgj0mjRgTeW_KWplHl2yX5Tes9VymyhVYGvqdN033TJdO_HgHJTP9soAWrt2o4i5n21d3inQyzP0Xn0-XsemoCKVfx--g_mg6TjYTwn_C7B7-ueA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیرکل کتائب سیدالشهدا: هر که آرزو داشته در مراسم تشییع امام حسین و علی ابن ابی‌طالب علیهماالسلام شرکت کند، امروز در مراسم تشییع امام خامنه‌ای شهید شرکت کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/667690" target="_blank">📅 01:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667684">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKE92tBV-LgRPsJrf1KIuXiTI5C6_VB1OhwQrAff7PacHSaYFOdUbr4YoupDxhaFiEnZqJ7SCV33ATJAPu-JVaw4yLubdhcU3c6yypUQqt8wnum4GjfrBOwbl5VI2CLe_u6sM4aj7ejJndsbuwGAsH-yoiU2SZZDvX-uDPs2nXzSGb59-Bxl3gJL8i_0uiI3cbgPyDqLfQUlpM_7Uj0IR4r1d0DN8LWYqtCaYhSztl9NeLWjF4OxIv7-EkMuD3aaPbqGsk12vei1IX0K9cJrx49ZeDSe3wFRf0sTTttm6VFSdnAJhIU8fTxy-L1hYAE-eAQUZ-x4oDbrF6eR2haXOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-w70DxBKI-lCzEeldT_HC5G4COBH9fgKyakqsMSIStlppPJGZMVgGa2vT9-wePhKH0KTZhjEVlRUCAfK3ixvFQ7KnvkfNxXg5jRr_nUsZat4HcpQD3BojbFfKfNPJ77iM4agE1Mj4sGAMvymPzCC3nGgQWR7C0z0OPFDePTsZlsqBQ5eqRgGn5qCwBhln-3ga2eamEBooder6c0Kuh93dl3IPuK4Pd7dpoP6JE-hXr3l5w-m_iI19MarOdF1NSx41DzzGGO6a57gA3zXHSdCXtGxbF3gXNqW8X4vHp3fUPcCBg82KEtQ4Qhs9ieuv1HSTrmliTbUy-vXv8vD3l49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NaH_x6lojIVaqXPVS3dhDorFxP-QNumsdnZFXnd4I-uTB7Z-v7gjv5l4V1g2npILJRw8YrMPEY4cRYbFDbadmyxt_XYSUk4627tXH8mOlj0P4G8PzIQBwAh8KaSYH9DgOqCC5pkVruQZ2P_NoS5iqjgg-VM4QhpVt529phJ57tu0blteIalkYsu46AKsVXmyyxr1y7175UVF_RCvOdloSkNR8TPzS0-9DsJRVkud5Bgq5_dcKnvtbc-yL9rdchAsxo6nfOQfPu6iYMCJ11p6jkxX6BHEAUkt6rmSuA65XezGRx9gONyLymodH5O8NsgXQM-hesGQgfdgnuBx5S1HYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhG7Z16AEkVDUB3AIsm8ofXQmqUEtVbcMtgvHOj2xCkZfcrGwTBuStM4Bfy0M_O9IVYXkUcABG05AcII58iLd7-lhfglGw9qQ3QOTfpi3PhpPYv7DHxR2-wicupuHyYGJswDooPZzbuxvAHqhIcjoRy2THEZ3Jqj_vCP0sI-_Ooscq10_1wAM37S0hPb5mlZmGf_YjuJRXfUzy667q2MRmjdw9XRsXSCVisjQt_UbCBKOamBlctDBEGwldfg-486177-LLIaxI_wlA3n1KRMAzajurBCNHiAa6nm79_DIvRSSgQpKvvA1psBQJEbpDMubhRbZzZg7rqpGJ63oXbSOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd788d10a.mp4?token=oslpbYMJZ83SKkME1gbEWVJm482kPtim0XNk_eAGlO2AfvLyeJzPyJjLNITtcW4gU0e1CTJyGqoMLpSGoH6qyfzt67Bat9aU4WASA34jKrgaFEN8f1EfCnck4ihNovauhvsCNkhqa0XnPhT_Wxqw25_V3ml9iOyH3_a4oFjbX9KfDQ6ZvJYqmbPP3kgCzLI7bT6U2i-vDqd3yEK449Vuad6SPzzpT1WORiQ1Q-hDWDL--H4SXDWe0nj9GWd_rytK1KHKlEyp5nS-NuRFP-4C1N2uTU4ha0_YC78vFYp5AQ12bgw68IZaK-b-gLcbxXgIkswsaOM6XEC6C1uX28NDag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd788d10a.mp4?token=oslpbYMJZ83SKkME1gbEWVJm482kPtim0XNk_eAGlO2AfvLyeJzPyJjLNITtcW4gU0e1CTJyGqoMLpSGoH6qyfzt67Bat9aU4WASA34jKrgaFEN8f1EfCnck4ihNovauhvsCNkhqa0XnPhT_Wxqw25_V3ml9iOyH3_a4oFjbX9KfDQ6ZvJYqmbPP3kgCzLI7bT6U2i-vDqd3yEK449Vuad6SPzzpT1WORiQ1Q-hDWDL--H4SXDWe0nj9GWd_rytK1KHKlEyp5nS-NuRFP-4C1N2uTU4ha0_YC78vFYp5AQ12bgw68IZaK-b-gLcbxXgIkswsaOM6XEC6C1uX28NDag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک گردباد قوی امروز شهر هوانگان، با جمعیت ۶ میلیون نفر، در مرکز چین را در بر گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/667684" target="_blank">📅 01:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667683">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjZxpE1o-UF-CO1Bsp3rux4zNEnh2z-EKDM7c2ixuQngE-wxB1gqLgCSKGm1n5Nr_Qn9pcVZ5_-FkZ_SeJN0qXYjuSsPLDcbPFsIJJvxXJdMgyqDamt9Me53w5cnL_2icTpi1-wSCvmqze7ENQiNSlp3UA5FMAOnSXR_WQycpDIGyjjgIdZ5hujiC9bh_otyiLNotqKk5wwWjdGmxyFemk1pJll6x2IWdaA2kc6foyU2XYLqrpHJQw-MLsX2mjK-Yo8k-SoFzcppz5wUqq9cy59GRXxS-iMhshQ8WwJ1oBCOq_EMBz8QGed-VQBqic2a9MgTa1GdJQGHekmrvk3lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر هوایی از گشت زنی امروز گروهی از قایق های تندروی نیروی دریایی سپاه در تنگه هرمز
🔹
این شناورها در دو گروه مجزا به حرکت درآمده‌اند؛ اقدامی که توجه و دقت برخی رسانه های خارجی را به خود جلب کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/667683" target="_blank">📅 01:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667682">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
حمله توپخانه‌ای رژیم صهیونیستی به محله الزیتون در شرق غزه
🔹
منابع فلسطینی از حمله توپخانه‌ای رژیم صهیونیستی به خیابان صلاح الدین در محله الزیتون در شرق شهر غزه خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/667682" target="_blank">📅 01:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667681">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
معاون صدر اعظم آلمان: جنگ ترامپ علیه ایران غیرمسئولانه بود
لارس کلینگ‌بیل:
🔹
جنگ غیرمسئولانه‌ی ترامپ علیه ایران، رشد اقتصادی مورد انتظار آلمان در سال جاری را به نصف کاهش داد.
🔹
این جنگ هزینه‌های مالی سنگینی را بر آلمان تحمیل کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/667681" target="_blank">📅 01:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667680">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1cc9f3e9.mp4?token=L0EfWrjnQtTjyzww85e-B2_BO8hlKyYbBVz1-ja4gJDqvvnBQQWhAugb8IeqR3XK6taxOOwZTwc2QHGcqKHECsBoLtuglmhMz-Xz81vpOY_u_CYWP9BepWWYxvcnm5a0x7cGw4jqEIISJUba2SG1WY5E_GCE98-d_-LPDutcwr-0hELn72F0ROS1Ht6Df3AAdZsJhY5rH7s1knUSzAeDgNLYyicG4IRM8_91Cm8lFzZoBG2QQxdwOUdWQD70giN8LQc8Uqd1O4eryOpAhrH7O4ENnVAdo-PN0wpNDNmjoJbTq8rBz09JmXkrWId_dHzm_y1OtQ_J5lKa4OjXtPc4Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1cc9f3e9.mp4?token=L0EfWrjnQtTjyzww85e-B2_BO8hlKyYbBVz1-ja4gJDqvvnBQQWhAugb8IeqR3XK6taxOOwZTwc2QHGcqKHECsBoLtuglmhMz-Xz81vpOY_u_CYWP9BepWWYxvcnm5a0x7cGw4jqEIISJUba2SG1WY5E_GCE98-d_-LPDutcwr-0hELn72F0ROS1Ht6Df3AAdZsJhY5rH7s1knUSzAeDgNLYyicG4IRM8_91Cm8lFzZoBG2QQxdwOUdWQD70giN8LQc8Uqd1O4eryOpAhrH7O4ENnVAdo-PN0wpNDNmjoJbTq8rBz09JmXkrWId_dHzm_y1OtQ_J5lKa4OjXtPc4Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ نمای هوایی از مسجد مقدس جمکران؛ ساعاتی پیش از مراسم اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان  #بدرقه_یار #اخبار_قم در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667680" target="_blank">📅 01:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667679">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏆
آخرین لحظات حضور کریستیانو رونالدو در جام‌جهانی با صدای عادل فردوسی‌پور
🔹
وقتی برنده، تیم دیگری است ولی دوربین روی افسانه، فوکوس می‌کشند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/667679" target="_blank">📅 01:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667678">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHZHmqgXQbywpsCwqOq2huwXWl31EtlGuyrVhMJhK8-ZjdkUy3EpcAUlBFxqq7XCaj9J9xwHfsZbeNnSzQisgzGKeTNZJVYgCJXW7tY7iLokJGuI_171fvCJcm_cOdxRBn4L_gxSaZtEzxEeRfNh49aSqTSzhJQW1yeK_244-tnxPJgPiKVwe4_JWvIhBxP2DB-pDLcxNPbmSB_npU6ZWk-5wQk_yrHoinoVqGURfZWEAgjqPYLbjJqgMEJmHQvpvYmfyccEzGFLFLtizLq-DuCUFzx4IV_crTwa-siFR0DqaewVplmYLoS8P-_6f5W-spGkXtm8-8GOwkgCAKZzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موضع طلبکارانه آلمان درباره مین‌زدایی در تنگه هرمز
🔹
وزیر امور خارجه آلمان امروز دوشنبه مدعی شده که ایران بایستی در نهایت هزینه عملیات‌های بین‌المللی برای پاکسازی مین‌ها در تنگه هرمز را تقبل کند.
🔹
رئیس دستگاه دیپلماسی آلمان، «یوهان وادِفو» در مصاحبه‌ای…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/667678" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667677">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efbe8b7cc.mp4?token=QVfEHUHIm1gL7OP33bDJaYJ96n3bYMbJ7W8b82T1nP2K0U6zHWsp9cG7Ck0RqDk2fABfUdsUMof6IbNQJ-_fz2ocp558XEnFRmA7sxJBcPAurE2y4CAyGHR3SP4kohiL_xUCifJxJmmN2baqq0oy63tI1kKLd01mTQAyKkssFe5D6PHXTblFzuizMbq8-bkj6pjCPkGKO2iyFc2D7hMRGZRM8XKWUPy-UOybhW1DjZSKwG_RWEd4K1I4RbDRPPCP4rQuUkwWIX-D9yaGmLeoTSn_qMdSfT9IaVGEHCOXslz_aUjwMN4xQstuYdxX1DLvvZgiaV99avNJinRNADiITQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efbe8b7cc.mp4?token=QVfEHUHIm1gL7OP33bDJaYJ96n3bYMbJ7W8b82T1nP2K0U6zHWsp9cG7Ck0RqDk2fABfUdsUMof6IbNQJ-_fz2ocp558XEnFRmA7sxJBcPAurE2y4CAyGHR3SP4kohiL_xUCifJxJmmN2baqq0oy63tI1kKLd01mTQAyKkssFe5D6PHXTblFzuizMbq8-bkj6pjCPkGKO2iyFc2D7hMRGZRM8XKWUPy-UOybhW1DjZSKwG_RWEd4K1I4RbDRPPCP4rQuUkwWIX-D9yaGmLeoTSn_qMdSfT9IaVGEHCOXslz_aUjwMN4xQstuYdxX1DLvvZgiaV99avNJinRNADiITQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم‌های سرخ انتقام یالثارات الحسین در مسجد مقدس جمکران  #خونخواهی  ‏‌ #تقاص_خواهید_داد ‏‌ #WillPayThePrice ⁩
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/667677" target="_blank">📅 00:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667676">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cxdkd4TkmL8MNwrPox1YKE1i_qGLxv5bN9RCsJxiXPVOd2xCw0QxukXrEvabZw5vG3es9HUn-ewKupnoWurAhpVpV4qdNfdgbDVCAl3-JmpRbhJGJnSTvGrcGbDKf_adbKjo4QXcSCqYsZElpU0dBXC-logj3Qq500W2edgWT6nKrho6sbg76sxvbd9KxE3TZvLyZNXEk_i_N8l7EzeheAiRZMgEzRxgMMlIq27OthK3YQjER0wt5MdEwGSL0wbp7ARWqklU2mTcsDCSOCOHm6vG8hsvZ6708CibF5gaqSUU4qJ3zdm0sQS-V5wKyz0_xlz4uFC8tjilbrjoXFQuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت بیت‌کوین به کانال ۶۴ هزار دلار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/667676" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667675">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1611978093.mp4?token=QM4wCerLySJasGAqsygNw5_foYKsT1FsL5D3Dv7Dj7vTH6zsM3Nsiv-6telrBFj7QnEjcxGsmvRcPcrMbZKqnTi27WeHQJU8LX-xP_q2yPyJ0cCBYG-sfgb-ab6bRxvZZ0GrHlW-RKwaxOhX6ahSit7AUCA9VH-Rzu4Rq213hssi9qbfZeUB0ANwvXmmVGXi9sl0h3WNhaZRPHBHimj_XJfRA0BgQDa-hWdrHBHVTPZW9lWwMBQi1-Abm8Iw9ogqZNgWjP0-t3BTujRna5a2LfrMJyZB-r7RJzYlkq3wxcVofFs4PmX_MOs4AwcXW8NMhh2u4Bori5-HTorrRpZHcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1611978093.mp4?token=QM4wCerLySJasGAqsygNw5_foYKsT1FsL5D3Dv7Dj7vTH6zsM3Nsiv-6telrBFj7QnEjcxGsmvRcPcrMbZKqnTi27WeHQJU8LX-xP_q2yPyJ0cCBYG-sfgb-ab6bRxvZZ0GrHlW-RKwaxOhX6ahSit7AUCA9VH-Rzu4Rq213hssi9qbfZeUB0ANwvXmmVGXi9sl0h3WNhaZRPHBHimj_XJfRA0BgQDa-hWdrHBHVTPZW9lWwMBQi1-Abm8Iw9ogqZNgWjP0-t3BTujRna5a2LfrMJyZB-r7RJzYlkq3wxcVofFs4PmX_MOs4AwcXW8NMhh2u4Bori5-HTorrRpZHcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسجد مقدس جمکران در آستانۀ تکمیل ظرفیت
🔹
خیل عاشقان رهبر شهید انقلاب خود را برای شرکت در مراسم تشییع به مسجد جمکران رساندند و علی‌رغم اینکه هنوز ساعت‌ها تا شروع مراسم تشییع باقی مانده است، صحن این مکان مقدس مملو از جمعیت است. #بدرقه_یار #اخبار_قم در فضای…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/667675" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667672">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYc_MNmLJjiv-cvYs18XOtzp58Ev0oZN0xH_f2FH3R5GpgOd9uSDksOhMMVHNJnut3nxkwIZxEpOasjCRgkSGxI0n3NeqeOz4aLhNL8PtgmjYcLgJ3haQ5iQ1a_H980K5fNq2hHkwAvSVJIdA-4EQvDCfP6vUhlIRwjc8jD3EoStiJzOv7QXY4yH7p3u_m80mVjLr_HbYRZKaFr--74-YRJV0zmtb1P9JCSk_ofuE9RpcJgWG3FNWuAf4gRUz6HHLrstAv_QTny8iSKXPNiJQnQ20YXhm3UKmmcdkO8JIiii0Y6kPPDe56nXxPu9XbieGIcKYsUWKmlF0FcpKs_AQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INo3qp485q_2P6Im5RV_M4SGu9GU9K1gKMrJcJC1-scjHxZZ0F1X5WmlZ2Xq_mx-3iuw940EuDEskqcycRs7B9BFRS75dIKGx_JNd8H8sWHsNkYrLvuzVDl2OKc1XbdIMSFzin_QnKRBlIhzKTxCeM_9jQNlIb2BZTu4-U0vN48AXlwpcFxLXcKxgEZQ1vwXt3w_9gLaZMtI0W4MfVamFiSNeffE1Lr2d8Qf92ydxlZTXER346vQD27MGMDjJC7ycS6d9X7t93tE7kAhFpqbySe7eGIxC0x8R6jbuZPYrmIqjJZhnQ4Nykn1BZKmf6Qzmy_sGxoz9tZyZPDRzJhVNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e8334a47.mp4?token=T3BP19pzGKOHBeWoFKzSP6jWEsaSrNkTIVWSgJnwmkRITHxgLNf9ckgiqSqc9EuqAHY0V_UKLTsbU8f26SZjC5RX4UqPL1POvOywnS9Qna4CxAcw5zx1mIx3R28Qi6o6yglWavQ_ziMi5HnYGJPPF7p-QXp0thWqSxtNOrryw0bIXHWStJd8wJLc9rlbrQY6vfsaBUO3CrRYsdNSl-jcy2AiLU_iDaBdmAKTgEc37-0eDXLjajSEJWrg-fhnt58lo7hjH40T0VygvRW8FTudkpXTrPFVs42trgvgzKGSCdkJG0OhBLJy194I0wIcVsX-bOcFJtfK38rI6-8g_lMjFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e8334a47.mp4?token=T3BP19pzGKOHBeWoFKzSP6jWEsaSrNkTIVWSgJnwmkRITHxgLNf9ckgiqSqc9EuqAHY0V_UKLTsbU8f26SZjC5RX4UqPL1POvOywnS9Qna4CxAcw5zx1mIx3R28Qi6o6yglWavQ_ziMi5HnYGJPPF7p-QXp0thWqSxtNOrryw0bIXHWStJd8wJLc9rlbrQY6vfsaBUO3CrRYsdNSl-jcy2AiLU_iDaBdmAKTgEc37-0eDXLjajSEJWrg-fhnt58lo7hjH40T0VygvRW8FTudkpXTrPFVs42trgvgzKGSCdkJG0OhBLJy194I0wIcVsX-bOcFJtfK38rI6-8g_lMjFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های رونالدو پس از حذف در جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/667672" target="_blank">📅 00:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667671">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4AXvbTF2gAQ358i-biL_vuY5eKuJD_bWZe6s_ZKqYnNTC44TY8nFna1UFIYCss68-ISRPRhXKHyLwkakpkdXQZ9J31DMRQpFKekdtzfRnutX0u5Wz86YSICXotGhBeGEkCth8pBop1Oj_JRs-QyyEB_hSA0JhngaF_PHwdMEHtKFbfU51FQghaciNRf9r3y0axUY00L0VOnC-uHW1N3eB9weSrCl1I3iqRLov2w9uWvlTYhxY272E_LRj-h6BjmkZUNmdf8aTTT1wfEvT_hVjAVen4IGuQggHmR8NiQ2wmY0ORhGOk0ZUYiZjOYyGjUD2_okRHtCHKunh3jBZSr9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عصبانیت رونالدو پس از گل مرینو  #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/667671" target="_blank">📅 00:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667670">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8180ac8e2.mp4?token=B8XNBPi5j8R1nHk9p9fkqxLbrGXe_8gHg0RErzKxd6WilY-7si80AYrOOmAufoNf60HkG1cNeVovpIpwkJ3NoG2T5QokXkR_44w5FpAsvptuoMWOFJHb9YI8AAz85xtheO0iGxC6kScwlGFEdJAxHvonBfEpX0BCmz9ds0pfmaa9MtE-1mxhOw2Fdh83akBAmtV0dUd0b027Wi80pIki1vK0wyYNGnHSwBr9FprRQ_6T2Nw8nlgMinG0QdT1fTAs-KVva85-4NPq0RIvpdyE4EOBV-1tacu0CXuZer-LMsVsn9Vkp60jh4Y8FtIA-CLwI4uuSSyCEHmSe2dtVGuRXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8180ac8e2.mp4?token=B8XNBPi5j8R1nHk9p9fkqxLbrGXe_8gHg0RErzKxd6WilY-7si80AYrOOmAufoNf60HkG1cNeVovpIpwkJ3NoG2T5QokXkR_44w5FpAsvptuoMWOFJHb9YI8AAz85xtheO0iGxC6kScwlGFEdJAxHvonBfEpX0BCmz9ds0pfmaa9MtE-1mxhOw2Fdh83akBAmtV0dUd0b027Wi80pIki1vK0wyYNGnHSwBr9FprRQ_6T2Nw8nlgMinG0QdT1fTAs-KVva85-4NPq0RIvpdyE4EOBV-1tacu0CXuZer-LMsVsn9Vkp60jh4Y8FtIA-CLwI4uuSSyCEHmSe2dtVGuRXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسجد مقدس جمکران در آستانۀ تکمیل ظرفیت
🔹
خیل عاشقان رهبر شهید انقلاب خود را برای شرکت در مراسم تشییع به مسجد جمکران رساندند و علی‌رغم اینکه هنوز ساعت‌ها تا شروع مراسم تشییع باقی مانده است، صحن این مکان مقدس مملو از جمعیت است.
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/667670" target="_blank">📅 00:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667669">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWVYMhuJLPcsDyoHagVYACmWp2h6tmKLtMtDtLNRAfXUA5x-QyON6spNWW6BnKVV2lsg3aViOFog3T9u1piriZjOEOJjN1qrsdf0spsG9q_8gZELid_k6dfkcBvWf0NB9gfHM246YSX7-4kv2N9023KVZhKP5b-Ijux6xkZS3j1LRX-Xv4wS713I8FW5aaTyZsFyDhxaL9StD572jQP1CSgKVQb8-4nsK5i-D64lSH-Rag7po3wOxaLNmJETZRJQSb_T2WHnSoID7XDB7-G34loId-s9kxLK7viegFPiycGqSDfrWGZAaFYkiqjymBzQuKS3dkO1dlSj3E4M9NDg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل اول اسپانیا به پرتغال توسط مرینو ۱+۹۰
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا    #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/667669" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667668">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnFIcz2QGS-utAuu9qqAivQjNU40ranvtHN7pBhTbjewNTno1qlMDZ3ITUa9s6lyxg4hzCl6vuAPBYkB6NPFLCJ-mFsDbAJ4agbmsSSSJ5Svd8Cb_ezrmX-4nBlcW3xfL9w1hQ18MCkT4AQ_QLacsgd8xslxvDrUB6SrRTItNoWzS83G4AAT9FK4Vzr-RhRnJrU6Con8Cp3jMpMJHcnmj86v0gzu40WGTzIiJAbltjv4OZv0Vu06-wkzcHnf95VlBD3tB5g635QoDVsW8clWiKCeEqH91uD7ir50iswAFzu5FDhq2PiaXIX4WMB7YeS1m352aBuouRT7SK9R2IxUNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عصبانیت رونالدو پس از گل مرینو
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/667668" target="_blank">📅 00:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667667">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722eb4a2b7.mp4?token=NU7W5vCASRbPI3rg_vg97GronoQbcX_mvK33O24bSwdx9tTC0Syflbs7saLcSBaA7vTLPXjI740HDwgd6dn6rok_SZpGsh_ifS5BWe20CTQL0mhvSxICugKnbiDbdXktew-KGe0W5qTP4jD_YYOzJVXhJTYqVTRa8vWKqyMbFF4ngrusF8fL_RQN2CTWnQb-a_uKHSf6gIENwgRMfB2g3sdduQwwiZf6R2RbCfL3Lfa_tY_HFjQSbzrJqp-1GsGDmoPac2Q-OiOhBi2l90T7aCnRYD4zEpOHEMewo8XRV4gtr-JrZ5PvZ5NIge-bTbFzyBSGgbmiBMyTipFguz40Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722eb4a2b7.mp4?token=NU7W5vCASRbPI3rg_vg97GronoQbcX_mvK33O24bSwdx9tTC0Syflbs7saLcSBaA7vTLPXjI740HDwgd6dn6rok_SZpGsh_ifS5BWe20CTQL0mhvSxICugKnbiDbdXktew-KGe0W5qTP4jD_YYOzJVXhJTYqVTRa8vWKqyMbFF4ngrusF8fL_RQN2CTWnQb-a_uKHSf6gIENwgRMfB2g3sdduQwwiZf6R2RbCfL3Lfa_tY_HFjQSbzrJqp-1GsGDmoPac2Q-OiOhBi2l90T7aCnRYD4zEpOHEMewo8XRV4gtr-JrZ5PvZ5NIge-bTbFzyBSGgbmiBMyTipFguz40Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به پرتغال توسط مرینو ۱+۹۰
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/667667" target="_blank">📅 00:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667665">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmEGg_nJN3gFYdEYi5oIS_Yw829ZFjB2GZzcXDglGdLzAxTEZiRdFGLpf7Y-k7r-wfMy180RopzassVBe-OBSsdf-HjdXHtUESbhcO6QzUVbwEGyvJ59qfSdRsX0oMRdmSf_MS8G5vstYAQ6SjgiEv8BtJGcMq0fMpiEdJwsRrNFe1KHc3XwqO3f4_bK26aRMKomby1fD9nezBFJmnCtK_371KTjWPt_3ZZeeGXuALgsbB2E9GvR5pWF6gtiQZr5Mc-N_eZ31EyaMGEx3-as21P8BtEpBV6df1ufjxsSfV1B5s9JDcgmwhpfSCi5lC3k9XN0wc0cUnZ1XktPNcX76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قصاص جنایتکاران نزدیک است
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/667665" target="_blank">📅 00:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667664">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدرگاه فرهنگ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b651a243a.mp4?token=bTcS14z5rw5RsvIITwoYSav9JxzroysXz-LG8z-7_JNGyFdU3d2uWA7asd5RDsjxiEOvdAC_JoqVyVOj2j8oYAoVZ1gAW2WemfOvzZjivzo67yJMIvK9a3VR1prJ8CMiIGUQ5OzJ7rJmK9v16PcALHGqd3FWyP1hodaID3i8arTJ3eFjKD1FosEroZlATw2lROanqgw9FvVnJUfdMaMyzr93XDVZg2KKy_JA-GW8f05NvEL1FAjePfeoh_Em1QAh6HdbtWZ8fBLzg7WymRHCvPR1eJHcjdlxocosKzGYYISlGBypM83Ktty3NCt8nuhKosmkSlVy4p-JupMzE3DvziXDL0hsOgOlgeObhTtcIpcJvgrgYSuSEdIRZNsvUqC6jB8a1QnFHaIp-RHCmb86z3pW0NSSJyb-qYmYbN7TMlDa3M2OxOtFr88WemOSnp3qDoL9UWGjX7gFNORH4BbKTcB2lsIaKXbolHjQnnzgTpqMW0Ms0cKZR-ooZbQJ2IOOaQqJnbPFj_5OXWDTisrTn-wudpGW7SN8lJAtkSHYH7HpTds3w4Q-kfny6jPde_Ryr6OeY-JJUlK03sIBiVV9Kjm5LpFzK3JRlFPy1J8BS9gxeScpKIh-ZMC_e9_yEPrAFdIESMRkAsRcFuP-jVFcllnqPsAkou1WcebzViYz_2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b651a243a.mp4?token=bTcS14z5rw5RsvIITwoYSav9JxzroysXz-LG8z-7_JNGyFdU3d2uWA7asd5RDsjxiEOvdAC_JoqVyVOj2j8oYAoVZ1gAW2WemfOvzZjivzo67yJMIvK9a3VR1prJ8CMiIGUQ5OzJ7rJmK9v16PcALHGqd3FWyP1hodaID3i8arTJ3eFjKD1FosEroZlATw2lROanqgw9FvVnJUfdMaMyzr93XDVZg2KKy_JA-GW8f05NvEL1FAjePfeoh_Em1QAh6HdbtWZ8fBLzg7WymRHCvPR1eJHcjdlxocosKzGYYISlGBypM83Ktty3NCt8nuhKosmkSlVy4p-JupMzE3DvziXDL0hsOgOlgeObhTtcIpcJvgrgYSuSEdIRZNsvUqC6jB8a1QnFHaIp-RHCmb86z3pW0NSSJyb-qYmYbN7TMlDa3M2OxOtFr88WemOSnp3qDoL9UWGjX7gFNORH4BbKTcB2lsIaKXbolHjQnnzgTpqMW0Ms0cKZR-ooZbQJ2IOOaQqJnbPFj_5OXWDTisrTn-wudpGW7SN8lJAtkSHYH7HpTds3w4Q-kfny6jPde_Ryr6OeY-JJUlK03sIBiVV9Kjm5LpFzK3JRlFPy1J8BS9gxeScpKIh-ZMC_e9_yEPrAFdIESMRkAsRcFuP-jVFcllnqPsAkou1WcebzViYz_2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طنین اذان در لحظه ورود؛ گویی آسمان هم به استقبال رهبر شهید آمده بود
🏴
آخرین ورود به میدان آزادی
#باید_برخاست
#یالثارات_الحسین
@dargah_farhang</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/667664" target="_blank">📅 00:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
آکسیوس: یک تماس تلفنی، نتانیاهو از ترامپ خواست که رئیس‌جمهور اردوغان را «مهار» کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/667663" target="_blank">📅 00:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667662">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHr2tYnegb5jqb_FYnlZuGt5Mw_ZWXeG94NDe5yDEADl4cisvdfpAugWp4WJvfNuEIVNQSDiM-787VSoHZrp1Oc03uisgB2tsIwtIy5on77_5646Wa4xQH1l0bXf01yLyvnB3vz_AJWxy3xa1VrWn6vbSpWDv_3d38HW4qfsqfcaGNu6cziLpU6_5VJZzO6Kcgl9c8C2UgjoRQiEx43DC6b7L5RBD-RjLbZvxdb82leD7XfbFv9sLVEnFbhyFupKSLNICf0oIWGGMnO9rzPoVF5aKSLCWxeIsrJIuJMnvFlDQIc_24BEv80oc2gzMvpsZkFNTr5gbbpOEGC0ZjERbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت لئونیداس واتیکیودیس، اقتصاددان، روزنامه‌نگار و نویسنده برجسته یونانی درباره یک جانباز جنگ تحمیلی اول، شرکت‌کننده در تشییع رهبر شهید انقلاب
علی آقا که در جنگ ایران و عراق یک پای خود را از دست داده و از جانبازان آن جنگ است، می‌گفت:
🔹
برایش غیرقابل تصور بود که امروز برای بدرقه رهبر دینی و سیاسی ایران، آیت‌الله خامنه‌ای، به خیابان نیاید.
🔹
«ایران شکست‌ ناپذیر است. ما آمریکا و اسرائیل را شکست خواهیم داد.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/667662" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
فردا شب پیکر رهبر شهید به نجف وارد می‌شود  مقامات عراق:
🔹
پیکر مطهر رهبر شهید فردا شب وارد نجف می‌شود؛ برنامه‌ها شامل مراسم رسمی در فرودگاه و تشییع عظیم مردمی از نجف تا کربلا است؛ همچنین صدها موکب و زیرساخت‌های ترابری برای مدیریت جمعیت عظیم زائران آماده…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667661" target="_blank">📅 00:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667660">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19d4c2b1b8.mp4?token=icGIrl4XSeAYFrF02gvGIy_LR1NwwAjFlFTJc72FWYZ5UySx1hp0qynAuDBs8qv9MZ3bgulbi0cUyE94RNciCio_P8KnecWNPaBhf7wtDLjrSX-BKwqnMoPNaBzTWcgtVF-KJ4vZHBh_b248lp9IxcoQqRMLJ9s8wz_RteSd60UpVP1HqDG7rZXvoK8Mc145zAvQ03OG-duUfUEtX-pbsDydTEwyMwagUOLfkcVKkCe8UcEiMP8swc8KY2CFT_5vRFSzBhioT_N9dKkrSSuKyw7JkmsJnSETj8RF-4GvGy_NH7kBTbjEgV0L62sDhVhN91v08ZN6uIRQx6mhqJu65w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19d4c2b1b8.mp4?token=icGIrl4XSeAYFrF02gvGIy_LR1NwwAjFlFTJc72FWYZ5UySx1hp0qynAuDBs8qv9MZ3bgulbi0cUyE94RNciCio_P8KnecWNPaBhf7wtDLjrSX-BKwqnMoPNaBzTWcgtVF-KJ4vZHBh_b248lp9IxcoQqRMLJ9s8wz_RteSd60UpVP1HqDG7rZXvoK8Mc145zAvQ03OG-duUfUEtX-pbsDydTEwyMwagUOLfkcVKkCe8UcEiMP8swc8KY2CFT_5vRFSzBhioT_N9dKkrSSuKyw7JkmsJnSETj8RF-4GvGy_NH7kBTbjEgV0L62sDhVhN91v08ZN6uIRQx6mhqJu65w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور فرانسه پس از ۱۸ سال وارد سوریه شد
🔹
یک منبع ریاست‌جمهوری فرانسه اعلام کرد که سفر رئیس‌جمهور این کشور به دمشق با هدف از سرگیری همکاری‌های اقتصادی و تجاری با سوریه انجام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/667660" target="_blank">📅 00:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667659">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/667659" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/667659" target="_blank">📅 00:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667658">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/667658" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/667658" target="_blank">📅 00:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667657">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dzuqeer66W1bBl03cRdxf-jqr1mOX_AV1pa8JB5qRnSO9P1Jh6mYUh8t5f6pQxFijpPwD-I7rNgQ3SB7oQXgTU4gS_AKX6_y-Ex4EAbBcys8ld93v6Co9uzvvw65Aahin8PYDL86fe3St4UplhClZkS7KBhVlWn2ThZTvoYFAhFrdABbAqwsf0rMUJ-hwUuHJ9tNIzpgSwmrgsG6vQbBhz87vrgpyvrar0UW1hmOGqeWzoAPEjz9nqQq82pU0gqjehMJD1TujMZB6L49uFl2KtS0X_rYgeYTwBThLRFDMpaPl-9wQiy2tjE7gxga_XPsG3N_qOQWmPG3DLtS4s76-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_دوازدهم
▫️
امروز با خواندن زیارت عاشورا به نیت شهیده لیانا جان محمدی ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/667657" target="_blank">📅 00:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667656">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
راهبرد «اول بکش» اسرائیل اکنون ترکیه را هدف گرفته است | آیا منطقه واکنش نشان خواهد داد؟
🔹
دولت آمریکا در هفته‌های اخیر دو توافق کاملا متفاوت و حتی متناقض درباره پایان دادن به درگیری با ایران امضا کرده است؛ توافق‌هایی که از نگاه بسیاری از ناظران، دو رویکرد…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/667656" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667655">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6397ee46b7.mp4?token=FBo86rdJVulditMi4-FvzbvD088ErfvI2HLPBVpVdovQTPfepiaJ_5cy7i_YQWfwDfCY8QY-CB6kccx1yJkKfo-56joMezvAAEVzHEsFVK_Awl0qwLORDNH9D2f_jM3vJb1xcerJ4R60XEeibw_qzdyKBOzUcgZR5qBIua4tPHIj7zKf3HfUkgvDPo14wh0itj9SlVVjxkujULu7ZG5Ra6ComS85Tebs38WnWbxBg8ywTMLLpEDTUi6L2g7jlJf4QxKGH3lfEXGvAX-Pk8fbJHOmcmNZh-e9m3fgQSkJ-BtpkyRCpTIQI3zaP429PYjmZ2wZHRFt3xb6tTGW90GJkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6397ee46b7.mp4?token=FBo86rdJVulditMi4-FvzbvD088ErfvI2HLPBVpVdovQTPfepiaJ_5cy7i_YQWfwDfCY8QY-CB6kccx1yJkKfo-56joMezvAAEVzHEsFVK_Awl0qwLORDNH9D2f_jM3vJb1xcerJ4R60XEeibw_qzdyKBOzUcgZR5qBIua4tPHIj7zKf3HfUkgvDPo14wh0itj9SlVVjxkujULu7ZG5Ra6ComS85Tebs38WnWbxBg8ywTMLLpEDTUi6L2g7jlJf4QxKGH3lfEXGvAX-Pk8fbJHOmcmNZh-e9m3fgQSkJ-BtpkyRCpTIQI3zaP429PYjmZ2wZHRFt3xb6tTGW90GJkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حال و هوای مسجد جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/667655" target="_blank">📅 00:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667654">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPh0ZSfOtyqrpgWegV50WzKy5tdhpWQSjJoIWKtod36e-5pRMJ1XnXPpyWU0xo2jtx4i4C5rN36NtdsvXROvC7PfQcCMTlHk220D3yUnJ2flThoYjRL8VaNKpph4r-4yyb5gP0HnOvNMGTg6cwir8M8z0QhcGnSXsDpmmhMmljbGSr82A2WtEImDwspyVLngqxfcs0PlIswK63cnVDAxz7xMFkN3SjeDpGtMX6lfjEK1vp5oSvLszHob0AUQxqhxdn5gRpGXo6XcMlWvsu9pECMA4IAdboHKqu31GQORaQYcoZCeWUicxO8gfbueLfRQ5zgZCSjxmC0_0m8U6uiuLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/667654" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667653">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7PW00ZAV5RkIyUCTFNBdJxt6ohzi7P5UN8Z9Yshy2byx8xqqv0xfNwm5cLAO0KeMMcSa5zpASgjupmd3fd7HmKdnBS2m43ywtr-aWEk1vv6LdGmDUoDXIBbfhgYBMsgXcJgtozjGL_HMHIv1Kt92B3qFau2JxRpSeQEyEN-Bekj9fir-InGn2dNT4iTDP1e5QXTGNFUhUQvKmVhi6amv70tn7kEPYVDE28BgDPIb6LUOTcSttd7_yFUiO_hr_1mpQM76ghZs-UlmnXdoIW3mcTGgWRZdw9-zbdC9li2hGxjqLbClfYUmHjXXDugVfrkVdswbkcMLk2V3Bc2jco3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سِلْمٌ لِمَنْ سَالَمَكُمْ وَحَرْبٌ لِمَنْ حَارَبَكُمْ
پیام علی‌اکبر احمدیان، نماینده رهبر انقلاب در شورای دفاع جمهوری اسلامی ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/667653" target="_blank">📅 23:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667643">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sqc9rUHWDcqeaMC1bedg_BRO26pUfKu45j9NlVbMqRAMi9FJqDNVXGr_Tu7oMkl6XZFF22PlzByehvxg7F1zQsLk9E_UocrvNbuWeU-740oHLiWL_-EzkEJoASjm8Cg_N8YTzLXaVg3oyDvwhwVjplYJy9pO0iOF0KHRX-u1s8vgsQ8kASsK_vebQoje4ue14Pwb92pDXcvpt3GCLR2bLgRFp2fjXwEP9_PhPwDNtvnqYSv7xt8Y-A9V78tgU37ZZ701C4VYBDQMJf7hIoKKDC6m4bKJSES1DKUsNoVsX5iPfHRym6Wrc5Vay1L8CpPi1AdGOCSRAqLnugvjbJAJIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4-Zu1tkd2j8gv4qQSrdsKQReDrg9ayLlAF8g_2fuR60ubkAA7_FwQYEJmEeSp0Kj5ZIoFgWe9NcUP_h7uLFaU0t4iCIF0E7Lx6CrLiWS5Zc5eVoNbkOmaBV1RZJTSQF9Z-qG8x0sZAZtBZn16owcoDjfIUixS4aOb1SLOi-yghUaMq2oLICh3t6q9QEwyGY60qnTKaqKr5_5IreAC0MPt-Gdq36iXrptjKSo2Rmk2whgmlnGRsJPIBe9EK02QGBfKutGun7ZI-c4qf-X3CREflvOSuuJiWYHPoOcYsi0YSOsCKaZTLMnv1505UFThOvoDbZpN94WFVuqL9IrMICVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCU_0KCaUKdt4m3xMc4Jwit0X-vVLNg9q6LEybcSWJOqHpcoYg3r7LShx4pY94IIo8oP1eO8nE4rNf-Ilun6Jrabr36sIg-j8y-rbBMzvZV-nwCids_SAleb20OQaegOursJn7pVgcUSnZq6rGZh1WYGWewqLD6rtcsXZh1YAQbgfHu9HQ3Xi_p3k5BEzA467bvY6zjfKyR2-Qi45ioWsuHDTy5eElquLVjD2QXWYAdOPi8HR9AwcpfL48vtIJf122GXysHyXNoxiqvtLOljQaYi82lkrNldpK3Uy6wnvZF4eycpKKUvj4LOl6lRaCWtuDneXhqMDSWJTjD8m4ONRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMAaYJ0E1O9WRtJnco14E3BB1bo0qthbr5mP6Chark53XikHLFvafAUaNHRdjd62RWLZUVVSbgNepPlqGiZgGlVQdrMixErnbklGJKs4h4CEch_XUgJwO809KzblvD2AL-8VvgB-IGW2LMZD08lCDaKWbil9kVfH5N97b3qE_Gm-JZo9MycCqO6nu8qGKw4eoyhEgk-nD9TxxOo7Jwj6P7d6Ifme9RuVZIVZ5GduGM5FWmvZUNNIEM_OM4o3xP-sFlP834jMRILKxggzKsu2q2SSdYX3cHyvswGVtbcffb2UHuvJ32Dy22LdhjY6Vq152acpiyOgEfE1y08Dk5N9Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjH3qimFGe3waZOCjChp7n6_UQ5pE6G3LJZh1w8rjc7N6HzK1pXbAk8-L_JF7FeHjX-jUTYAPnPqVXYLARJ9uf9rfXJcO4_Hrr4-VwvlnJKvFQU5sms9jRkiexfJ2XlBmcliEZy3UooosvvxrJnLz7ZTJoDiHiYGR6R3xrDkaSLU8GxQhRUAclLSxA5pE_9oA2rc3iBRlx6FBHTAUFDtmyEdr6nKnn0YnNWfuRs77LbJq8WGB8zEcY78kJ8c3lsrXdHV19lmEwLdHer0atb3iB_U2xx_4iEgrms6XwHS7_PStduAv16eaF-3n_gdZCoDzcFbO24ExlQeT7KkGXn6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6dmz-o_T8EpXAY_kb0ojT_8BA9WqsXKcUW4jq4Xh3sESSP2jdW4nweoFFcW2f91l5PQJ5sfHeNSwUPwMbAU6WrTwKU3-qcAWcF1bHkdgM2PRfNVKjoJGtCPYNvSXskqUievUWkFDaIXoKFa0RRH5hHZFlyXhq98DfcK_Yh3836SQdNTKGlhjuAEo0QI7ZY7q2zJb4qH_Tf73RidvoDmYSX7IaC36aJqdw8JeoFS3cpMj1FFElNFAERJvVp6HIOuRwY-v7oi6iwUTA8WsMQ4ZEgn1K1YO1yn4bp2i_VcNfCVu4EKHkhgjRfQ0JkX8V-1CbO4q1nm4Ajklw8x77-IwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cB8xEhehZszaOVYVhrB4YgSz_wLGqTK5uDygIKrleN89VxGB5Lr6VhN5JhhBtlu3HlWMDLM9h9h4VUlGmf5ubtPPp738NzD3FQwG5xyJMJa5wTrVf2yWLq_nxYTEaZkKhkd-J6Wam7hhkgqDUN6O_awpBQeoDHxHXN8nPkeLTsrmIjYGdZcB9bSbPggn9AHHdCnbbFNmeutnzmgydm0dpCHkrgU0A5SGfeYqnpFo27AtzOcRP2eDshSnnZqrnPW-3V-AeqMJ8MSJVwopoWsG5iwGC7XT_77Nh2bQYmCJumbzsNyvcHmY75sy0Ae8Hp6DqdXsj8z82-TnmOJ6ss3SoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXAjc2ejfQuCA6T6haGaxZwJBmBEkcL3A9SXf-wMC_Rl2fpAc7K8aZ_oPsNWjX3MMfe1L8xvG-T_o9KjfF-ATnGLGfOrRi43spuaGhppes3RHpOJzaup5cWX_sP2oOGcLxio6SKeExquul0nQGICkk-EZVyj7xGSMaQqLsNpIh3L-tyJPt2pxTQdYXm4HroHHtv6pMElwJWKJQX2LEsS09Z9XYoBJCvZJE3tuwLGT_gcRLsD95Yq5mf-nnVulSOaRXYUHA3qjwUrtI3itgdUdjdCHhQNgDv_o00jcWMpc1jlMpJDbBYucc2hgJkNrSTtC0ljqLvl5qit9SZu4Q8lXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BsUtNUR1xDhWmCg1QHJiFxS-W-ucY4YqUlG0VFvxGcCV7TB5OPKtjcGiyP_GhUNHZxGweSfhGs-e2TqvbW88TXvvMBPYiTcXkVE_yTCYOXsmNupAnAICd-hoKSdYwIpL9Yh7Q5dIkANyMcSgH8-wcuX2PHbSslJe6GMLxdjLv9CA_dPMpHXWlgD9egoS5zauAc8vs5qe0Rb_DB0U3Xnnha2DCaHommhmO7JQZ2KABIy2ktuitnvXyWoj8x4DJRhftM9gANcp0p3CN8mdylw6WUDkV8OWM4HKebyOYTf6s_0Z3fShpma6rkpZOM005MyElWEjzuGYpJN9xm6_MM3otQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXnNp2hgfSOjCH9SVXNKCC_RoDwepJOXOQKUeWNWz3PNqs6getpVYB06tnKJspolN8FFRcThdarJByJH2R9zfuUbfeViG2wrDdXn0vGiomXsrKMAvmocMt7rYfx9Lg4dwUE0lj-He_m9JhnSUi3XVcFPxdCioLfRrjXWD5AebZHFxS-XZ1yJKj3FZbS54W8VIqwArevXe2j8AeWPCDwWHzSxkysX1QnZ7R4CBo_H0CPEYo-vP5WjUFooKWqqxUTRVZWjYTsUKS_uN7a9T9jOUYkEQoE7fryYzKY3IztmOw2BPk982LO5HoPY228x95k0hPS32eMAjEBxjSg2B7yWIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اطلاعات مورد نیاز برای حضور در شهر قم
جهت شرکت در مراسم تشییع پیکر رهبر شهید
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/667643" target="_blank">📅 23:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667642">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموکب خدمات رسانه‌ای همراه اول</strong></div>
<div class="tg-text">میزبانی ۳۱۷ خبرنگار و فعال رسانه‌ای در موکب خدمات رسانه‌ای همراه اول
🔹
@namabantv</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/667642" target="_blank">📅 23:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667641">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
قیمت واقعی تخم مرغ ۲۰۰ هزار تومان بیشتر است!
دبیر فدراسیون طیور:
🔹
قیمت کنونی هر شانه تخم مرغ بسته بندی ۳۳۰ هزار تومان است که حداقل ۲۰۰ هزار تومان کمتر از قیمت قابل پیش بینی و تمام شده عرضه می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/667641" target="_blank">📅 23:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667640">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e97b160da.mp4?token=Q35Lqy8dlip3vP0RyZ5p1qBfuHqH1kAYnAFZJcxVBGBrc_mEL1FYxSZgFmz3jjQk9BIuLrR-YvSqA-pe2871FI3iBrrT8lV0bpkCqRt9Drdk_Wy3pBqa_B45Lr75GrrT11GNC8q-q8nI_InLHq8FTVjtkNNkaIcpwJ733icGRWBIaCpKEF2e94ghanV9eR7wC1WpPQ9lEwfQeYmtAjqBo6yARFmo0GyS9fl0P3TASBwlX6CKIPBtZ4YrzbsPf4ieYIpcQDeQhtJX_jYHncV750FtQPDsRX3I_NFi0vSMLu2FCMfl34FU9WStdFiwBJWPvhG8rbYCE6NB6g2byBRpSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e97b160da.mp4?token=Q35Lqy8dlip3vP0RyZ5p1qBfuHqH1kAYnAFZJcxVBGBrc_mEL1FYxSZgFmz3jjQk9BIuLrR-YvSqA-pe2871FI3iBrrT8lV0bpkCqRt9Drdk_Wy3pBqa_B45Lr75GrrT11GNC8q-q8nI_InLHq8FTVjtkNNkaIcpwJ733icGRWBIaCpKEF2e94ghanV9eR7wC1WpPQ9lEwfQeYmtAjqBo6yARFmo0GyS9fl0P3TASBwlX6CKIPBtZ4YrzbsPf4ieYIpcQDeQhtJX_jYHncV750FtQPDsRX3I_NFi0vSMLu2FCMfl34FU9WStdFiwBJWPvhG8rbYCE6NB6g2byBRpSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صبح روز دهم؛ روز واقعه مردم ایرانه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/667640" target="_blank">📅 23:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=eiZFI_14uCf1w7Di50Lt3LliIyc7eJ8edUUivapD4j1bQDyaE927mG0x1MSQYE9Ai__RjHR8rhAsxc15vtEMVKnXX9a8ct0vAd6CYo7Ldo8Clqbk5OeZDB-CaBm5guwFEGDNUKDlJqe5xotxyQsgf7Ag6oIljYQXQwdzWfev4jFIewRomtFzkgkS5evRD0rT6EBFvOBvg2Qza-dPUTBv_E69Pl_G9uJJ9JZMk1eMtKtIO1hUbT2F-kIzwDxmxrtZ2yIh8PH8ZAoSl3jqnXae3huaZz0DuIYZW4mvdH7t4krkEGsNA7HTd5dtN10QqK-NADVzGMIL2a4urg11GxQSVY_ldke-gulUC8UQV44Aej5g2LhUfn0GdBlQyWzQSPVBZXL-3EKFR_tonJO5rrl7yNTmaOhTkuBd2TdQXjwa8USs-ZEONTpk_DA0w9SxgMVRahirlLNiJbay7DqFfrjwdKCSs5dtFepW6vcwu0Vgm8DFoyM2BD1ISb8Pdg0oHOnv4IsbD5Sc4IbNySH45m17hGXhgyh3MyG2Zq6HDV_R7OdEyqOw-IXkOoi-_GZCRw9H-zHj2FuURPjWtSidxZPgujEf7FwPtuLXWHjdl_PHx7e-qL_7eVzGb83HZ7TwwmudjCtIzymTOT0f2mpRbqt1FuqVw_fa1Wetvx6mYnw09gM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=eiZFI_14uCf1w7Di50Lt3LliIyc7eJ8edUUivapD4j1bQDyaE927mG0x1MSQYE9Ai__RjHR8rhAsxc15vtEMVKnXX9a8ct0vAd6CYo7Ldo8Clqbk5OeZDB-CaBm5guwFEGDNUKDlJqe5xotxyQsgf7Ag6oIljYQXQwdzWfev4jFIewRomtFzkgkS5evRD0rT6EBFvOBvg2Qza-dPUTBv_E69Pl_G9uJJ9JZMk1eMtKtIO1hUbT2F-kIzwDxmxrtZ2yIh8PH8ZAoSl3jqnXae3huaZz0DuIYZW4mvdH7t4krkEGsNA7HTd5dtN10QqK-NADVzGMIL2a4urg11GxQSVY_ldke-gulUC8UQV44Aej5g2LhUfn0GdBlQyWzQSPVBZXL-3EKFR_tonJO5rrl7yNTmaOhTkuBd2TdQXjwa8USs-ZEONTpk_DA0w9SxgMVRahirlLNiJbay7DqFfrjwdKCSs5dtFepW6vcwu0Vgm8DFoyM2BD1ISb8Pdg0oHOnv4IsbD5Sc4IbNySH45m17hGXhgyh3MyG2Zq6HDV_R7OdEyqOw-IXkOoi-_GZCRw9H-zHj2FuURPjWtSidxZPgujEf7FwPtuLXWHjdl_PHx7e-qL_7eVzGb83HZ7TwwmudjCtIzymTOT0f2mpRbqt1FuqVw_fa1Wetvx6mYnw09gM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوش‌چشم، کارشناس مسائل استراتژیک: باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم/ کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم/ این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/667639" target="_blank">📅 23:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
یک کارشناس سیاسی: دستگاه‌های دیپلماتیک و قضایی به طور جدی پیگیر پرونده خون‌خواهی رهبر شهید هستند
احمد تقوی، کارشناس مسائل سیاسی:
🔹
در خصوص خون‌خواهی رهبر شهید، اقدامات حقوقی و رسمی در مجامع بین‌المللی در دستور کار است و دستگاه‌های دیپلماتیک و قضایی به طور جدی پیگیر این پرونده هستند.
🔹
این اقدام تروریستی در دنیا بی‌‌سابقه بوده و باید نیروهای مسلح، دستگاه‌های اطلاعاتی و امنیتی و مقامات رسمی با عاملان و آمران آن برخورد قاطع کنند.
🔹
مطالبه‌گری عمومی و عدم کوتاه‌ آمدن تا حاصل شدن نتیجه، از الزامات این پرونده است و نباید اجازه دهیم این جنایت به فراموشی سپرده شود.
🔹
حضور نمادین عکس رهبر شهید در همه مجامع بین‌المللی و پیگیری مستمر این موضوع می‌تواند افکار عمومی جهان را حساس کند و همه مسئولان از نظامی و دیپلمات تا حقوقی وظیفه دارند حداکثر تلاش خود را برای مقابله با این جنایت به کار گیرند و این موضوع مختص یک نهاد خاص نیست.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/667638" target="_blank">📅 23:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
آقای شهید ایران برای همیشه تهران را ترک کردند/ لحظه به لحظه با متن و حاشیه آیین تشییع
👇
khabarfoori.com/fa/tiny/news-3228168
🔹
حماس منحل شد/ واگذاری اختیارات به کمیته تکنوکرات
👇
khabarfoori.com/fa/tiny/news-3228356
🔹
وقتی هالند بدون پیراهن شاهدخت را در آغوش گرفت
👇
khabarfoori.com/fa/tiny/news-3228327
🔹
حضور گانگستری عراقچی در مراسم تشییع!/ عکس
👇
khabarfoori.com/fa/tiny/news-3228302
🔹
آیه‌ای که سیدحسن خمینی شنید و مراسم وداع را ترک کرد، چه بود؟
👇
khabarfoori.com/fa/tiny/news-3228370
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/667637" target="_blank">📅 23:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667635">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d83be35470.mp4?token=HQUb30idm_D3CgJ60c2i5DCgxTQxdf2zEqP1GrHmGPjHobqCxEDHbbr2VX7MPmlY92k73NIoZ8iUSAByUOnzS8pdozsZZ3k67zVrmLQnwaFnaSzMXpK97huCL32wnyquhfeSKepSFbRQr2nAUXDxifhoxxh9cKpoyQaKgZUvfLIMBEuiQplmIb2QcZG5-SmVm9vd43APbUT93LtiYv0RT4PKhr52VW1XzvCWpriFN8dNC2pfU42WlHi_AQhHgJXEGSNTCNgd5i8Tf4KNBKDR1FrFl-BHWWpD87IJ45pbAm0g1q9oXwcRu8V0_TNToHrOBWIz8mp-7nojkzYppqZlog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d83be35470.mp4?token=HQUb30idm_D3CgJ60c2i5DCgxTQxdf2zEqP1GrHmGPjHobqCxEDHbbr2VX7MPmlY92k73NIoZ8iUSAByUOnzS8pdozsZZ3k67zVrmLQnwaFnaSzMXpK97huCL32wnyquhfeSKepSFbRQr2nAUXDxifhoxxh9cKpoyQaKgZUvfLIMBEuiQplmIb2QcZG5-SmVm9vd43APbUT93LtiYv0RT4PKhr52VW1XzvCWpriFN8dNC2pfU42WlHi_AQhHgJXEGSNTCNgd5i8Tf4KNBKDR1FrFl-BHWWpD87IJ45pbAm0g1q9oXwcRu8V0_TNToHrOBWIz8mp-7nojkzYppqZlog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از قم-جمکران: مردم از همین حالا در خیابان‌های منتهی به جمکران و حرم حضرت معصومه حضور دارند و بیتوته کردند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/667635" target="_blank">📅 23:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667634">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
بورگا، اسلام‌شناس فرانسوی: جنگ، محاسبات غرب درباره ایران را بر هم زد
فرانسوا بورگا، پژوهشگر و اسلام‌شناس فرانسوی در
#گفتگو
با خبرفوری:
🔹
رسانه‌های غربی در روایت جنگ ایران، آمریکا و اسرائیل تصویری یک‌سویه از ایران ارائه کرده‌اند، حضور گسترده مردم در مراسم تشییع و همچنین توان ایران در مقاومت، برخی از فرضیات رایج درباره نبود پایگاه اجتماعی حکومت را با چالش مواجه کرده است.
🔹
این تحولات می‌تواند بر اعتبار روایت‌های طرف‌های درگیر نیز تأثیر بگذارد و نشان دهد که واقعیت‌های میدانی، پیچیده‌تر از روایت‌های غالب رسانه‌ای هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/667634" target="_blank">📅 23:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667633">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdZ70uDJJqX9FIMD4AGQCbgdsDAHnDMXNLdrM_mLLX49KQXj6oNSucSR9pjHm9xzNuOnUZw27bzqWltfUj_95pEJyGJRy6Jbzig4-5-VgkTDgAbuMEfIs5T4gcmL3Djp_oKOfclWxN8MOsAALNLhkv-CbZBABIYb_q9ozB07hyBL52-C3siBp8R5W_RtROtcP2f2L--2DU70ZQHnp-eMQ9pkmyIpoPJvviicrxCf5ziY5N-Ztt6ycVB-wNo4ts3WOzxdq8oZU5DM4izhXBdB5lPTVivzdEBRiQ2VAZ4z7oEpAT5BUIJUiv1cY1N3E-LQ7G_29EKgXkFoDwgvzDTzsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وداع به رنگ سرخ
🔹
تهران امروز صحنه وداعی تاریخی با پیکر رهبر شهید انقلاب اسلامی بود، وداعی که در میان سیل جمعیت، رنگ سرخ بیش از هر رنگ دیگری به چشم می‌آمد. هزاران نفر با پرچم‌های سرخ، به نشانه خون‌خواهی، در مراسم تشییع حضور یافتند و با شعارهای خود بر مطالبه انتقام از عاملان این جنایت تأکید کردند. خیابان‌های پایتخت آکنده از اندوه، اشک و حماسه بود و مردم با حضوری پرشمار، آخرین بدرقه را به رهبر شهید انجام دادند؛ بدرقه‌ای که پیام آن، استمرار راه و مطالبه خون‌خواهی بود.
🔹
هفتصدونودوسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/667633" target="_blank">📅 23:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667632">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dd3d2a282.mp4?token=Xc1n879sNOTPg5zUJjsW99FqAPnRN9hnmR93YiPEjqb61im6Pr2D1iCl90FHCHP7Yvrc58Wwjc4JN7s_r-hZ0irDDRnIO5zyseatov_eDMbDnTFzcsoMb255_-GyeaSgpgkFFt4YfpkUxNcX6gApwyVDT43g-RKAgB7yiFRUs1qpHlbSjjvGhqYsTshySpzogJVSGzGorky9njuY_a7Yu3udEVMHkTX6adUrmSDnF9fKroXNfF_XxfhgyCZP-5EaYwDkfOoPWaVHO4ceNHBbQiUUF7CYT9q8OB8mn9Sk6jkJIwqVirPCkyUwjD1jPUUnLIQZuK92T8gAig8KqbhHFYktldEI4khRaADDnXhchAOZJ8rmgd_d7F59fZmGNFaVwXkOnnja9EM_1HeXvvP7puG43cp48SOGDsqyP2PQ_FrJQR0PCF-MUlyjWYBcdZhrAHYBbwUae2cLznShS16i0PvFAm8mW1F-WDiCP1wutmsVIQ-XUyqGeXuSo9F8mpFVt1aTMjbq4aepwYnZYVeFb_4HYMLivrVbNZ-RbgCKYweJ3LQq_aNLmNlPJKNy1Yc6p62BV75_THy6nUgLOdl8AARhk1Z6-yoHI7QrTBkPv2kvJeekWPpDtOVOinS7xJtdvMNjtl4k3ekyZwjzI6krrD8jOe_-WsU0VoY5nscVAlo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dd3d2a282.mp4?token=Xc1n879sNOTPg5zUJjsW99FqAPnRN9hnmR93YiPEjqb61im6Pr2D1iCl90FHCHP7Yvrc58Wwjc4JN7s_r-hZ0irDDRnIO5zyseatov_eDMbDnTFzcsoMb255_-GyeaSgpgkFFt4YfpkUxNcX6gApwyVDT43g-RKAgB7yiFRUs1qpHlbSjjvGhqYsTshySpzogJVSGzGorky9njuY_a7Yu3udEVMHkTX6adUrmSDnF9fKroXNfF_XxfhgyCZP-5EaYwDkfOoPWaVHO4ceNHBbQiUUF7CYT9q8OB8mn9Sk6jkJIwqVirPCkyUwjD1jPUUnLIQZuK92T8gAig8KqbhHFYktldEI4khRaADDnXhchAOZJ8rmgd_d7F59fZmGNFaVwXkOnnja9EM_1HeXvvP7puG43cp48SOGDsqyP2PQ_FrJQR0PCF-MUlyjWYBcdZhrAHYBbwUae2cLznShS16i0PvFAm8mW1F-WDiCP1wutmsVIQ-XUyqGeXuSo9F8mpFVt1aTMjbq4aepwYnZYVeFb_4HYMLivrVbNZ-RbgCKYweJ3LQq_aNLmNlPJKNy1Yc6p62BV75_THy6nUgLOdl8AARhk1Z6-yoHI7QrTBkPv2kvJeekWPpDtOVOinS7xJtdvMNjtl4k3ekyZwjzI6krrD8jOe_-WsU0VoY5nscVAlo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز این چه شورش است که در خلق عالم است
باز این چه نوحه و چه عزا و چه ماتم است
♦️
ما به شهیدانمان نمی‌گوییم خداحافظ؛ بلکه می‌گوییم به امید دیدار... به امید دیدار همراه با پیروزی خون بر شمشیر، به امید دیدار تا شهادت...
#سلام_آخر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/667632" target="_blank">📅 23:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667631">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e6b1dd5e1.mp4?token=X6aHfFPhsEuHcVS8b1EfVu-YKih3l9NdU40J_3YrMnssfZwntnaOx0AWmROxn3_CiBtiYXf_7n27eqToH9uDjdL2_4ItcrVDMEfUMndEc3Y8Z5l2CF3zg9yVTOur6NiLkqdVQah8iZdEGRaW4YaxwCqWH6KLQeW2BoekfD9qNnmq8A41sqfG30Nb9s0zNHdiMFqW7Rxei5MjhMerehCdQKGgyExSdIaJue8jRt5-Kh50m_vi5de_rIhuyPCLyNp0FmrTu1X8onLEcpWsxbdizJU5cOnFr0jXdr_tGwq7iHntvZMvGMwQuWvDUQa0yhLciy_huKF43lpeja3Xs_h6P4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e6b1dd5e1.mp4?token=X6aHfFPhsEuHcVS8b1EfVu-YKih3l9NdU40J_3YrMnssfZwntnaOx0AWmROxn3_CiBtiYXf_7n27eqToH9uDjdL2_4ItcrVDMEfUMndEc3Y8Z5l2CF3zg9yVTOur6NiLkqdVQah8iZdEGRaW4YaxwCqWH6KLQeW2BoekfD9qNnmq8A41sqfG30Nb9s0zNHdiMFqW7Rxei5MjhMerehCdQKGgyExSdIaJue8jRt5-Kh50m_vi5de_rIhuyPCLyNp0FmrTu1X8onLEcpWsxbdizJU5cOnFr0jXdr_tGwq7iHntvZMvGMwQuWvDUQa0yhLciy_huKF43lpeja3Xs_h6P4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هرچــه را که دوست بداری
یک روزی از تو جدا خواهد شد/ وعده دیدار اربعین، بین الحرمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/667631" target="_blank">📅 23:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667630">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
اسکای‌نیوز: تشییع امروز خارق‌العاده بود
🔹
سردبیر بین‌الملل اسکای نیوز که برای پوشش مراسم بدرقه پیکر رهبر شهید ایران، به تهران آمده بود این مراسم را با عبارت «خارق‌العاده» توصیف کرده.
🔹
مراسم تشییع امروز نشان می‌دهد جنگ ترامپ علیه ایران بی‌فایده بوده و ترور او نتیجه معکوس داشته و حمایت عمومی را تقویت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/667630" target="_blank">📅 23:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667629">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358fe1a189.mp4?token=mp3GyfCyBu4zUrlZuXurotSnHfpSlEp5Ok0RYWYnCjEueIbt2jgVAZpQ4cdcf_DaRLLmOcc8FzZY0PAyE6kYDI_wUoUgCQDBh6oEiXKPZmUq9DiJu85IW8qydGX30aihsojIj5w_BUocW2m4nC6b95bXScWWu1dEyEwh3ILC7u0UwLz_W8zIAp0Ip2WtbCLfKiVoIsHjIIVwYdc73L6x4i8n4bzH6ecigCxRDg-5lHmSWwEoBwHme1lh8SjcwhLO5lv_L-bG8yVu_F5wI62fgvIzxhxQkvLMk4sXCQswBZwV0Hmz3LEJZq7mqodlhvj7IVAW1972AmEDugqYvRq3UDDx2gz2xyv_BGe9h4Yy7RCYozO6ZwE8IbRk0681m72bGVHlxD2yNoe0AoVzqE78top9AFUviu4HWoIYX5LN266qa0WC0JqwCkwCZ6VCO7d6OWunUBFzuOBGtpXvFDUoRVQdXz3lMrRFakvd_81vW5Ea4z39ieydUzbg64yGxh_10y1cnFrjuiZVNWwA5IubhO2PR5N2kPBMXwB9vopVm-Ux6wYt9CSGKEeZopFwezGLqDMyGudgGbW-AfXsF8ofyZfo5rMLt9nXvvyaI-Qr1hAUKFgVUiyvgQx71xkAgDNMo1M5zJDpGEFGVrg87NNNLTt_rIymUsFg8L_vNk4V0EY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358fe1a189.mp4?token=mp3GyfCyBu4zUrlZuXurotSnHfpSlEp5Ok0RYWYnCjEueIbt2jgVAZpQ4cdcf_DaRLLmOcc8FzZY0PAyE6kYDI_wUoUgCQDBh6oEiXKPZmUq9DiJu85IW8qydGX30aihsojIj5w_BUocW2m4nC6b95bXScWWu1dEyEwh3ILC7u0UwLz_W8zIAp0Ip2WtbCLfKiVoIsHjIIVwYdc73L6x4i8n4bzH6ecigCxRDg-5lHmSWwEoBwHme1lh8SjcwhLO5lv_L-bG8yVu_F5wI62fgvIzxhxQkvLMk4sXCQswBZwV0Hmz3LEJZq7mqodlhvj7IVAW1972AmEDugqYvRq3UDDx2gz2xyv_BGe9h4Yy7RCYozO6ZwE8IbRk0681m72bGVHlxD2yNoe0AoVzqE78top9AFUviu4HWoIYX5LN266qa0WC0JqwCkwCZ6VCO7d6OWunUBFzuOBGtpXvFDUoRVQdXz3lMrRFakvd_81vW5Ea4z39ieydUzbg64yGxh_10y1cnFrjuiZVNWwA5IubhO2PR5N2kPBMXwB9vopVm-Ux6wYt9CSGKEeZopFwezGLqDMyGudgGbW-AfXsF8ofyZfo5rMLt9nXvvyaI-Qr1hAUKFgVUiyvgQx71xkAgDNMo1M5zJDpGEFGVrg87NNNLTt_rIymUsFg8L_vNk4V0EY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم وداع با پیکر مطهر امام شهید در مسجد جمکران
🔹
در حالی که هنوز حدود ۷ ساعت تا اقامه نماز بر پیکر مطهر شهید امام خامنه‌ای باقی مانده است، مسجد مقدس جمکران و صحن‌های آن مملو از جمعیت عاشقان و مردم ولایت‌مدار شده است.
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/667629" target="_blank">📅 23:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667628">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0073f2bda.mp4?token=sL0xiueuvI7BqWsIR11rFwQAXbmEW7LVt55dpxaHMt3RNJV2pT8U2TPuWGOVuGdokKHca773pqSSfLlyByEOD3WA18fLTh_uEueJ6Sk7cjpPuco42cvK1zd-xXsl-lX7ahv47Y4PVmWwvZ-XRC2ZUjASD9gA4AsMKdHLO_bXb_TAyOQGM5cR0cBpWt76HKvje_FCHsFk_w9V-rgURzoX5Ue11h50gkI52Ztk1ZXAY1RvD7e1lGwy4BzHr8H31lQPjPBAnbjTjmUFsSxRY20duB33E5W9KhJVjTniak5KHKJQlp_hRgfN5Qh5n7S2HuXmlDgN2JKVmUJUGWbSC_B55g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0073f2bda.mp4?token=sL0xiueuvI7BqWsIR11rFwQAXbmEW7LVt55dpxaHMt3RNJV2pT8U2TPuWGOVuGdokKHca773pqSSfLlyByEOD3WA18fLTh_uEueJ6Sk7cjpPuco42cvK1zd-xXsl-lX7ahv47Y4PVmWwvZ-XRC2ZUjASD9gA4AsMKdHLO_bXb_TAyOQGM5cR0cBpWt76HKvje_FCHsFk_w9V-rgURzoX5Ue11h50gkI52Ztk1ZXAY1RvD7e1lGwy4BzHr8H31lQPjPBAnbjTjmUFsSxRY20duB33E5W9KhJVjTniak5KHKJQlp_hRgfN5Qh5n7S2HuXmlDgN2JKVmUJUGWbSC_B55g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت عظیم دلدادگان آقای شهید ایران در مسجد جمکران منتظر آخرین دیدار
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/667628" target="_blank">📅 23:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667627">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90ed49aced.mp4?token=qg30B2dZ7QUB4Ot8vEu-apof7o9a6IkQ4Ph4D-FsfOun8WX2Q_icM0vg-VAMh73AB7bDZqytK00B4k9OXpgnA1cKWvj25vB56OIJ7mSSE5109UdA_HBFV9w_b3m7diB3NTbczNV5qminkQinfEk73B4M49bLIbBETcwCKi5TkCSoAa9-ngWKDzpueAcUMtlDnZw7wYIZJsa4Cgep3aJVqbzog3v_HiIkUysll3XnMChLT_fBySsa_bT6NtykP4DgjKr0bzFZTsMYb7aPpY3CyQTiEpJsiozttqi7dUb64rZAEEUwU4aFoO1yEq52jgvh7yZdN_a-WGtkA9j65urpuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90ed49aced.mp4?token=qg30B2dZ7QUB4Ot8vEu-apof7o9a6IkQ4Ph4D-FsfOun8WX2Q_icM0vg-VAMh73AB7bDZqytK00B4k9OXpgnA1cKWvj25vB56OIJ7mSSE5109UdA_HBFV9w_b3m7diB3NTbczNV5qminkQinfEk73B4M49bLIbBETcwCKi5TkCSoAa9-ngWKDzpueAcUMtlDnZw7wYIZJsa4Cgep3aJVqbzog3v_HiIkUysll3XnMChLT_fBySsa_bT6NtykP4DgjKr0bzFZTsMYb7aPpY3CyQTiEpJsiozttqi7dUb64rZAEEUwU4aFoO1yEq52jgvh7yZdN_a-WGtkA9j65urpuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و قسم‌ به‌ تابوتی که‌ برای‌ حمل‌ آن‌ یک‌ نفر‌ کافیست‌
😭</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/667627" target="_blank">📅 23:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667626">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPQHelnRZm6AndBkCWthUo0auDjC4Mmpn4KVjdC-pvFcidNLVrJ8IZkY6v24-QXecYgP9_9YYwKG27f7j6PQSg0-VK_YS7uO8t6mEaLoGqQlneCN3sGK_ipSL4RDSDCXkI13ueeZxIrgg-7_hyinZoKgWJLNf6G0tJWxNveekdHbLIgG6bqW1xjHXqVvXJB1Pdw1NlbU4lzU9IM7o1g8E-sIgm5v3x0StuxO2HQjNHpYUtMB9m_RVA3HIjH32vK1rPJ0G6-5bffXWD6OVcgrNKB4Infz282eEN_-H1OSnBnBjMvL94UM0Er15o44Y4gcdVFqGhgDFNWjnmj2BmRX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم اکنون|حضور مردم قم در مسجد جمکران برای بدرقه رهبر شهید
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/667626" target="_blank">📅 23:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667624">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dey9GRpTcZxdO96hGB9Q5bZk3mMyjdX6UaN2AK-3534esdeErM99IuVq3BeTC4ifUn7oJXHSWEjjL9uFsFsWa6JiWibpU7ygb-XKgQimbMthXd3gIpx4mfMMveDqAmMUoDuRjAG7UdM9_UG45YSyBuoLTxbbbGA09ytAunjx8Csyye7mp5bCLzYU9BSbLypxvO6VT0W8S2WeBGIivDcj9ad_7fUAJsl0yHyq0XUI6aM0l2i9EZ-t4xLEmfY_1UrHdSWbmaLjifjKzbUH2zWyvHtXVkAFd2e3LW5Y_0ISldmFOkpuSd7A_aYZw7Hd1kCq_R50xPyR-89ddVseJGYbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fd_Ub85VlFlpdaVN_HozS2FFtvN9puu_ld6hjqkFZXfpe6_HDDRczepOrLvzSAfg0xukwpXMOBQlFmYciwpwDXuDXI5BcyOQZgIuFQV4Py_PfBLn1FHNWK6ZkJhE_rK8SLfnhz5MfZvCF-k_-1ks4PGH5R2VGnGB0Br8MwKAYKhP_cF2ZzP7EjdtJxFzErklDr1XGRLSJjbw6xgKNFa0fLBtEPyvDIBhsHMrvphShBXcyfcobVtR2U8Bzje3Irng4Tzlhd_tE-T7CqXl-AbKbDxDkYW6tRtYSm_23hp3ZcXijFBXIHa1My2voDabSZkXYEN-3V3ZMA1xVVYx-XKNcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نمایش «دوران بزن در رو تمام شده» توسط مردم غیور ایران که یکپارچه با پرچم‌های خونخواهی، فضای تشییع را به رنگ قرمز درآوردند
#تقاص_خواهید_داد
#خونخواهی
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/667624" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667623">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q82tGmZ-NQAGwvJWZx8st7e2PlJnddB6oexlaQoLpNiKWlUV1HmE9sRCAJEkDmTmKILDDwLFDyZuXQyVnXisOBTARCosJ4_WWCwpcvysulvb5o541Qm9JnAm8jxpZN-lLAgJsC3KHTGR6NgFSBpvC1OeBjJeivfQhS27xxUTBn8B6X4sGCgVhYQ8fecrFGrs92VbFG6qUj1rE2UFqGuJOkZtsnoZ7DtfnSQ1JPY9VKAlxHBrDfWlN4TbZ56vZL2mNk0EXrxgLkU2eDG53xUDiHOLPzCaT6bLTeDuV1jBx2JGskhG08ougv6pvVV7JcZHS12mO7e0usDXN3ZMVk--hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار نگران‌کننده و مرموز نتانیاهو با ترامپ/ نقشه جدید اسرائیل برای ایران/ قرار است بی بی چه در گوش دونالد بخواند؟
🔹
سفر نتانیاهو به آمریکا می تواند تلاشی برای بهبود رابطه تل آویو و واشنگتن و همچنین، پایان امکان توافق و شروع جنگی جدید باشد. بی بی قدرت زیادی در مجاب کردن ترامپ دارد و این مساله را قبلا نیز نشان داده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3228326</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/667623" target="_blank">📅 22:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667622">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1RKyTE-Pny7nrLkYJfKVSI29aXKcaXBhgw8VD3qSQDPwJRbWuYyoSCrimVNHd4Y1VEHARkPuEvts-Kwg8nHId8lBOerctKXzl2tMFiHcIJ0aH-uEK2gqXMxo3ZzCQ3l9tD5RpWRsNrKQxSpohIJr1dEJaeisDRWCFxZk8gpi2yscktuIVbhXTkROTacFeOFdpiCvGh-ylpvpM4fqJzZnrHEGgiN2lrXQmlrH9gN2YvnvXL5WshbzaeKv8N_Sr0ZjSOcgTiWXZ-vSWUfp1n_zJD9hkKzcq3UXK-HNeRW_zEgOwQwBesZkIZ31HWeiSvgJ7NVFnc_jp8lx9uz30YVww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی در پاسخ به ترامپ: با مردم ایران با احترام صحبت کن، وگرنه با زبان دیگری پاسخ می‌دهیم
ذوالقدر:
🔹
به رئیس‌جمهور متوهم امریکا که امروز ۹۱ میلیون ایرانی را تهدید کرده است می‌گویم:
🔹
پیش از این تو بعنوان رییس یک کشور بی‌ریشه با تاریخ ۲۵۰ ساله با ادبیات مشابه از محو تمدن چند هزار ساله ایران سخن گفته بودی و نتیجه برایتان جز شکست و استیصال و درخواست مذاکره و آتش‌بس نبود! ایرانی با زبان تهدید بیگانه است.
🔹
پس با مردم ایران با احترام صحبت کن، وگرنه با زبان دیگری به شما پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/667622" target="_blank">📅 22:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667621">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLYnxCj80AoF4dNCQR_HTPdmYjVKWO6Lu5ajOxGbmtV7oakcCbFXQoSCo6Vpz7ue4eUsKP5ssb3QBAWS6WMxxGRaQip9Wvzt8bE0lQyV8boYHz0hse3L9ncKpqTVHtAX9MDrplG3uyNQDCfSHrZkp0ek5iNjEFcQjN_q1VAYA3_-QgVcm7cObn-Mz-Tsx4A_WsP5g8Te4HvWtD3kk2QhCtF51LSxf40xkzBKIcGNnm_EriKG1L4i19omNjlLm8xMBedcCSS3hxS9wdcMQ75JLjLK7OB4t4J27bb0ZV1JH0_9056LKF1feFH4LHAWaSlH54uZz43C4lc0E1AhPZVDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گلایه مهدی فضائلی از صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/667621" target="_blank">📅 22:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667620">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ترامپ تماس گرفت، کارت قرمز آمریکا بخشیده شد | جنجال رسوایی بزرگ فیفا
🔹
تصمیم فیفا برای لغو یا تعلیق محرومیت ناشی از کارت قرمز «فولارین بالوگون»، مهاجم تیم ملی آمریکا، موجی از انتقادهای شدید در فوتبال اروپا ایجاد کرده است.  در خبرفوری بیشتر بخوانید
👇
khab…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/667620" target="_blank">📅 22:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667619">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGYr-CmsrRFLKho7rh6FR_jHB1QuQ9apKvjcgbRvI566W-Q1C5EwaCP9gQGfHMGZZ2tay50Ybfa4h9caK90_YY4mAvvry8eaWcER239yExgnLL-fgYWlPcBBCw2vXY87yjk2CUBd5I_7G1QfDQndNZ5kCnueRjTA0k-cw23k3YZKOlNbulI_2cz7eA5e-1d6IAv_UTrKbxQh3MEcXgrD05cSGNyFUC7QOCvpRD-pHnAFlvSyixt9MLG2SPYVEAG1YRr8GUjE9XgKKYKSNB99ojuyq_firYNM8vZOYawzdU3jxcoG7twXMb_R0GNMlDUdj4SdoNItR6VPtaaw0R84qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
فراخوان خبرفوری برای مراسم تشییع رهبر شهید؛
«بدرقه یار»
▪️
مخاطبین عزیز خبرفوری، برای شرکت در فراخوان
«بدرقه یار»
کافیست از مراسم تشییع در شهرهای تهران، مشهد و قم عکس و فیلم تهیه کرده و برای ما ارسال کنید.
▪️
سوژه‌های پیشنهادی:
پرچم ایران
ثبت لحظات مراسم توسط مردم با تلفن همراه
حضور و شکوه جمعیت
فضای مراسم و جلوه‌های معنوی و حماسی تشییع
▪️
آثار خود را به آیدی زیر ارسال کنید
👇
#بدرقه_یار
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/667619" target="_blank">📅 22:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667617">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hITWT29qaiu4d80F-l344jfEhdLUt2txScNzcg0f2J8o6KSUZQu6uTjHmTvRCCOL6dUnTj8Z9mmlZD0TsJ85cAxJMfrYjHOpaVRGtis-NldWpAiXdq5kiUNcPhiBcFk58zMv8cSjj4KWYHbhViyQZ8rVOxTi5hMuJEC-vxKrF4_q--QKDJmM3gjjoX4GsCl27aCPEUSGM9ejxQmv0fhDPq_niKeS8d0pUtQJp62MLRA0BiT7hzAUU-SSzO0Y1Z6pTSTdtkoIQZ76YDaPMKXqiSaGYYOvvp6Ey9DZKxbzCWvAwBYQXHlTBqlR0Tao2hzqjDPoC1kO0GgAkxb23XvdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: ‏ملت بزرگ ایران، پس از ۵ دهه، امروز نیز با همان صلابت و ایمان روزهای آغازین انقلاب، شعارهای کوبنده‌ی خود را علیه آمریکای جنایتکار و اسرائیل غاصب سر می‌دهند
🔹
این شعارها که با خونخواهی رهبر شهید توأم شده، به خشمی مقدس و اتحادی پولادین علیه دشمنان این مرز و بوم تبدیل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/667617" target="_blank">📅 22:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667616">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ddde3e21e.mp4?token=F7LJKpbBc11BK8a5ELtE_g45oL67deoyPNS5OsZTGn42dEoLBzJxL0w9Dncdf2IqRJANpdAKri3J4ojuTefFVdxIqGqMhHc3XhrmPzBfcj9SEK-mLq9MGXiAGj0m7OKxtiKQfkTdlxOKvAq_gU26O9nMB2zRbhC6woTxNGt_TefJ8D1BWEr7i9VzsM7as53J6gQnjwW-pfh4sP2Q2Oe5omQh6vWur3aTn73J_JpNl6P7VHtdUKYak8Fp3LE2syRRrdrPbzAHtBx6DQHKfi0ojc-4_7dazVg6TETtxDrcNkExzRmHJ8bOlyvDIKze4I7um97l6_NFuaRe_OT3LB6Uj5ptqyjsHnGi-ZQijdoemRjQhCfRVa75Yu3NRT4z_9ln4Dj3PYtOEcIyGuUGz9e8wCp6K3Ry7WQV1Xxvlt-P_jK0Acm-fKV1Yw1olvKbG0jkXkf8Of1PQAyDvWVx5Jr8hxbVD-YqqvDwGXUaX4bOo7jHCXA8IpFB3VVKOEqD47pz6YNzLriGP8NuYuXppmgSLPNR62pX0EzgeXVp8-3ejH5eK9PIjkTH8Z329yDbhJhcUFRt78dxklZlWRCQm0jcRwMIrNyiPwtEQ8XRK80BpSmBkAcoKmJ5LOZdK6qek6AaCi0M-ImEDONOfm7IQdoiUuhxNZMqHpdVWW8A_WzSgpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ddde3e21e.mp4?token=F7LJKpbBc11BK8a5ELtE_g45oL67deoyPNS5OsZTGn42dEoLBzJxL0w9Dncdf2IqRJANpdAKri3J4ojuTefFVdxIqGqMhHc3XhrmPzBfcj9SEK-mLq9MGXiAGj0m7OKxtiKQfkTdlxOKvAq_gU26O9nMB2zRbhC6woTxNGt_TefJ8D1BWEr7i9VzsM7as53J6gQnjwW-pfh4sP2Q2Oe5omQh6vWur3aTn73J_JpNl6P7VHtdUKYak8Fp3LE2syRRrdrPbzAHtBx6DQHKfi0ojc-4_7dazVg6TETtxDrcNkExzRmHJ8bOlyvDIKze4I7um97l6_NFuaRe_OT3LB6Uj5ptqyjsHnGi-ZQijdoemRjQhCfRVa75Yu3NRT4z_9ln4Dj3PYtOEcIyGuUGz9e8wCp6K3Ry7WQV1Xxvlt-P_jK0Acm-fKV1Yw1olvKbG0jkXkf8Of1PQAyDvWVx5Jr8hxbVD-YqqvDwGXUaX4bOo7jHCXA8IpFB3VVKOEqD47pz6YNzLriGP8NuYuXppmgSLPNR62pX0EzgeXVp8-3ejH5eK9PIjkTH8Z329yDbhJhcUFRt78dxklZlWRCQm0jcRwMIrNyiPwtEQ8XRK80BpSmBkAcoKmJ5LOZdK6qek6AaCi0M-ImEDONOfm7IQdoiUuhxNZMqHpdVWW8A_WzSgpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داغ بعضی نام‌ها با گذر زمان سرد نمی‌شود؛ برخی زخم‌ها آن‌قدر عمیق‌اند که در حافظه یک ملت ماندگار می‌شوند
🔹
حضور پرشور مردم تنها یک وداع نبود، تجدید عهدی بود برای زنده نگه داشتن یاد شهیدان و تأکید بر اینکه مطالبه عدالت و پاسخگویی درباره این جنایت هرگز به فراموشی سپرده نخواهد شد. این مطالبه، تا روشن شدن حقیقت و اجرای عدالت، در حافظه مردم زنده خواهد ماند.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/667616" target="_blank">📅 22:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667614">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWMZbPG16-cYIwxqtYfWQZWt0Urrglj1kGhjbefuP57-n2HPhigIoCCpr49DxxTFN59qJdfcytt9CaAZWVefJjs1TVdMTKVcKXLGUmHwcLiPONVqOZJ8DRXO69ciCZxOyc21Pkkyo4hhgKhWmprYVPmZhP_FpdBDAwhbmb7pwnt_jb8csP8lze1RENIRJB_Y5VXRsi5L2ghJVCGqIg56pg09gYajXH7aWxRZI-bh57aj5MeurpTnmK4iXpLuFNaSUmcjyhIR4LQrpB1yiFs-IchNR7bK0ZcBpQ1edfd0Oa-84pcvmmL-xqxip-9LqqI9SkCoy60ormizXrVyB5VxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از حضور میلیونی مردم در تشییع پیکر رهبر شهید انقلاب #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/667614" target="_blank">📅 22:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667613">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDJ1WbyPO9k_w3LtPYgzd-d-LsBm3_YHVUO6AiCvKF5P7_EbRWlUUUZgHVswITOAQXrPI0RZTbpqo-SH27RxMt54Rr3KfUgzv12TzSfB-zt41guJlsItveqRLF19rFxdvm3gAd9tVO20UtOsAOWJSM1l5Ecb-FEy8UqrZ2GL855vYd91DnP-ur7-9vn-HxDd0Q5JkCLwqhsulHhjTUwI7-hVZdhtf_5T6kPWs1PtcKfHAM56o1b2YFJxxderhOiTdh6JXpmP4qbL6EnmrbaYWMn_ZuJU0YqW9eZ7MK7sM2SR7sX2ZGd-KX5m5plYEQdtr7ArCkIHgW_V4h3kTrBwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهران در سوگ و خشم | بازتاب پلاکاردهای جنجالی علیه ترامپ در مراسم تشییع | از جایزه ۵۰۰ کیلویی طلا تا ۱۰۰ قطعه زمین ۲۰۰۰ متری برای کشتن ترامپ
🔹
بر اساس تصاویر و گزارش‌های منتشر شده که مورد توجه رسانه‌های خارجی از جمله آسوشیتدپرس و دیلی میل هم قرار گرفت، تشییع پیکر رهبر شهید ایران در تهران با صحنه‌هایی از خشم جمعی علیه مقامات آمریکایی همراه بود.
نظر شما چیست؟ اینجا بخوانید و ببینید و کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3228373</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/667613" target="_blank">📅 22:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667612">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ماجرای حضور نداشتن سیدحسن خمینی در نماز رهبر شهید
انصاری، سرپرست آستان امام خمینی:
🔹
سیدحسن خمینی بدون تشریفات متعارف در مصلی برای وداع با رهبر شهید حاضر شده بود.
🔹
اما دربارۀ نماز بر پیکر رهبر شهید، ایشان به سمت مصلی حرکت کرده بودند اما به دلیل توقف خودروها در مسیر، امکان حضور در صف ویژه نماز فراهم نشد. او همچنین امروز به همراه خانواده در مراسم تشییع حضور داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/667612" target="_blank">📅 22:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667611">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15201da837.mp4?token=TmLIw7JsZII9B9EQZ_nBqBDXJoi1a9uy_IEdTXuub0gUwYTrux3TvR4v6asDzy8RtYoQ5oU_KWeSOCSNgQYChXHndgcmCn5coSg7Y9F4QHluMN5ZsB21y0S1nQplwyVkF713ZBRqm34vB4CBwbmHkE9r4EOzocj9Y5JxenPOaIIRf8kW-I6Xwjzi8VLjErvREbOAhbpl1gni40Gl1ZVzYU0XtpuTWTgKL73pyW_7HUwFvJ_UUQTz2A3KTe66JdvZkwD45ENZiVEPXSMneL6cqY-dfcMHsPosoQWv-I8dH0SBQtMKiX_du7g3GyeGBlxb8oFWwRKuYL8mwI2-A2aN6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15201da837.mp4?token=TmLIw7JsZII9B9EQZ_nBqBDXJoi1a9uy_IEdTXuub0gUwYTrux3TvR4v6asDzy8RtYoQ5oU_KWeSOCSNgQYChXHndgcmCn5coSg7Y9F4QHluMN5ZsB21y0S1nQplwyVkF713ZBRqm34vB4CBwbmHkE9r4EOzocj9Y5JxenPOaIIRf8kW-I6Xwjzi8VLjErvREbOAhbpl1gni40Gl1ZVzYU0XtpuTWTgKL73pyW_7HUwFvJ_UUQTz2A3KTe66JdvZkwD45ENZiVEPXSMneL6cqY-dfcMHsPosoQWv-I8dH0SBQtMKiX_du7g3GyeGBlxb8oFWwRKuYL8mwI2-A2aN6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع گردباد شدید و هولناک در هوانگ‌گانگ چین
🌪
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/667611" target="_blank">📅 22:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667610">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3tOVlM7puFiWdw3M953tAWzo5DJQr2cRm7rwM4H2SdWHLeFCwRdnzyhr2Wo7zqpC6Q2FOEVXcZ1RwgdEbl9RGZHIgOCGkCAsjQN1NCRkTggeJd-oXxNNSJtmTJvK5WQHHAzB8px6-Ci9tKnuatYtq8sjlzr0sO19zZXbim_zd55XcQQp6IlfkfKbN6UGZNvfUVAI6dvbEzmf4g87lVJ-v5Fw_7HJyLUUWppNv-5w0nAGzRC6WG15ZzFlf6n44oxbTnJE8t7RBBar02vkWgK_-ibaosT2B4YqdUilxOFGpQQ-DCRSUvr2iDn2TfRm2b-Asxbtw1jsVGti67a0lS-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها بیشترین اهدای عضو در زمان حیات را دارند؟
🔹
ترکیه با ۵۴ اهداکننده به ازای هر یک میلیون نفر در رتبه نخست جهان قرار دارد و عربستان با ۴۵.۵ نفر دوم است.
🔹
ایران با ۱۹.۲ اهداکننده به ازای هر یک میلیون نفر در جایگاه دهم جهان ایستاده است.
🔹
و از بسیاری از کشورهایی مانند کانادا، ژاپن و بریتانیا عملکرد بهتری در اهدای عضو دارد.
@amarfact</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/667610" target="_blank">📅 22:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667609">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
استاندار قم: فردا راس ساعت ۶ صبح مراسم نماز بر پیکر رهبر شهید انقلاب و خانواده ایشان برگزار می‌شود و پس از آن نیز مراسم تشییع انجام می‌شود
🔹
با توجه به برگزاری نماز در ساعت ۶ صبح، اما از چند ساعت قبل مردم حرکت خود را در مسیر ۷ کیلومتری بلوار پیامبر اعظم (ص) آغاز کرده‌اند و در حال حاضر نزدیک به دوسوم ظرفیت مسجد جمکران تکمیل شده است.
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/667609" target="_blank">📅 22:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667599">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZ1jeJi104K8IWzSvZ1d9m-ALBb0z0tGPXz2i4cX79czVmmjNrdK7MaqQJCeeeN9qmvJRvsHdiE_K0eg7VGU0DCZ7JcXrUvQNbrgDkg9wxHdVq85yxUCZL-uaF7NZSXU9c2vmMFHX9LIN9A3MwXWxSPJFN1MUal0yhAqyitoN04nk1DjMTpWa57CgnqkWO46JIOx3kNXxFQRiB1DUC_46zONPy-t1or1uRGooINw_SYN4XmCWuGm_ov0gMmcqm2I-fCQsX_4pu8zL_LG_haawThTzVHqgvRBRggPQVWPDwkuC7PXUhuxoVXndJ3U1z7jzFYmZSrsoDWaozbL8P4Udg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuu6FnL_9_M5gl4XHNhuPRKQEMs1CINCY0NzZmNxRcgVGxiakqatmueB0z5pTHxLEF8JJ3NesvfCWNksKrF1ezN6ZrdRe5vh6JJAgT3DCbdXjUtwliRj9eEvH6i491l2-VbQE3wQ_U4H50ov5KzD9YigPuoEWja8HtTrXXrIwO9heNYLKNINH-NJjC7BWrHPp7qT9Ufbb98AvPF5QP6P20eL8Xw_MOngw4ac0gOEncfqvvYfP7UkWa356XambgoFJHUPqEMXlOfWPRhJvfMkhhYTRz2UMspXPBcHtBDj-ym-vX5XXCCMhnZJn7PYJByRIsaq0Ndknv-vIy4vskP-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ECaposRBL6QpUPM52lR-l4nPPzHAb2c4Asg5rDHS_hwkJA7zzWS_zFDwqt995pMW_eQOB2isscd115BQbGUUeTjj_Z5771Zbwir3r5-tkslhQINkYMwFMIAJwhSZyuwjerUMQmJnq00j-73Omy1PmKY8DxnCFkbCXIwdZuSuGxOk0S8D8H0HSUglFIJszFqn2sb9qtgcunBuLH_KnjsAzBJuETMxHkUVEX2i9JarF0cRg_48Oec3LHytEhwqEx6SrySzc5qMLq-ElTsfsdSYIl6P1U1LMe3jYtOMU3dqh4qo1RtIc6_h0BmlXUeR_BA6ZGrdQyO7sdOscP1QmE6n0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9Abi67ADMrBaG8lH8BFJG3cAstWXeu4qpEwAjc-o3oh4L2I3W72QTrEZyv5fzPnRq5IjMkDV3RvnXGxt5ZqLNGHxphmV5-mzOk3wZ7GWy85cDBkGoI2TNTym-gwVvx0REkxthtqmRII3XaucoSwaYcnbL4-zma8Fy2lCt1nwxDCSxhC-jN2kmx7Y6gDnXPFvsHJs8FPXEDf6lc1A4iq7tNmom7VzvZGSpJE3IUyRJ6NXAUMs3CwExwj5PZbPoTcMJ7DHeHIami2z7s-RTz76PyNDt3gWaxWG7x7wkFVzRpPY7GP4vuvpzXaq6vfC2vekpLHdu0us8Vdru_3KEQAjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rr41JYQawCG-59-Yv2Aba0xNgpDm7tznNeXVukJU3VuG2w7l_xPgz7wsHtd0tSXILl6W2TgVuYlus_WfqJKIwTI_cDljznTPmWdFg32leveQhrdNq-wwQCb9fMKvzfZ3GDeBLqukRM4TR7KjH68eoascYdMHWuSWcy4LCFeFBR6zXPvPPsjl6DSOkJH_LuazCFlKEpseQeahDcsvYa2sI1r8hOzyGwxhnKxK-HoiM-3yPw5N2Pf0rm93Lgm7YJGG4jG3ZSsBONqY1rC48bTreNkyxrCGcF4dDEQLybGikM8bNZYqwIbXpmIswVlD0Ael67nBu39AWiuVyxoveEWMPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRJHyluWfCYmI5BYCbA9QmMZz3A8Y6xH_DDUZndknJ2H9IZbMGUXEfdi0f_133ZONKEjEYGKN-jSM963Ggb0Wy6-yaJt70RLoN73eXNz7Fq5u-r3ZsvWovijv1yfKDYrB_HtOxxp-49c8g-rxnsmaCky1EOOmh03V_aVOTVc9mjEreYL4EBvU0jHEiCx-6taCGlQnhajzwtvnUl1eQsctKhOyVPNG-P3MGGSha4f-HXdo01SuWgF5pN1cVVsJj8LZobXpFuX8EC0NKNpjHPTvo4KwuLgboiDZwYYfyCYhrP6NMN6KjN-cGLtUDnb_puk1KYHD5JjlnPZPkoYIeW8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIJmqgXOOIyIU6XGMU4gf7XyYvox-o5AAKGweqJnqC1kLFzA4lho9r1io6vYRWhEYFIGfSEuL0zTCpTn-ehYWQfhCUGEZJhWlTlXCop5dCy2Ycv3PUBwBG2Q914xJnk5cZMOo9bpnxCWs1gjuuxarPiNHOy8zcBpc5y9wuPDHdIa4omZTEX4K9Ljcku0fNfJmELD1IrzL_e7IIfH0AWfcrm6Ovyh1-Zeq7WDLwN6F9oGBzBESdMYcz8woNqutooOvnQ_K13J0GQpe2zeYwfOgwmyCRljJ9Y1iSd-xsbElLR-1b5baeE2zVVvtRWuqFOfWzVYeuJ5OW05LtvlepETAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TivRIkRSeyBSA5YDEby3F3PDVoc_X3ZoC3kapPrCUxfTGe20C9ij7uxsRKE19hfT4HSwb2SLkYR27evzuPdZorCVrthJ_6A_xdx_c1nsyNLN3vBcnv_n3oSk6R1jUiACzYjRcUEwbKZXZ4BnthJ89TMaBP7m0rT0kV4ysFpI40ZMFQcCLN-vWuS5rO15z4FLdWoJbyMMZ4A5o-OxVOC3_32QpSuTzVUx4_efJSPmPhKknCT399R3V2SvbA1Mrh0R7jVlUB6j4liQ2jIi-pkjkb-PReXwPPQ9PMp-7WyiGg4Icf7LT3-IWJ99lclq96UhFN_TfTa5pqUCQvl7oyWTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uw7VHGCIgEJOmh05qi4k7uFQzC0UKMWV6mBcOP6SjDu_0FtvPhGpkXMASVyj4zEoVpJoyhU_F4g8-T5KqI65rehqV2HE9KOZTPOpL_Iro05Ss669dpnE1XaugbDeo_lX_qA2D5IG9Hm0sMyMz30fLxUwjRjy87HqvFtr04GGb1bYStWkPgGv6qQVhIC4WIJctBhM-buHG8LXGkCrDb9SPPv4mUKpwgjR9OcrgNQ1N5KOBihicLwIZGJpJfMRzfxw6ahV35CekmZiSNIgS2PbuY6LBzxhaEiHhTOCNbU4drCp2FB4wCTrS1a21n6-ccm0PcAm-euQmKYZbqhA94YjCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s43HyEBejNDTMiZuJOco2u6XBmUIjBGynAkDtfkIvssphA9X1qZJX7Oa9kN1zxL2cUsblInNOIV7eNajsNEUEDzDX7Qddt-GzJP1PV3jPjZbjcVT2fBppuyU5KxEzQvqhq1JrMGIPKULrKH3ifQEsk6Fv7K0pfqt22tEx1p_-6fc0IhFbnmW3dY3odTLHX0oTHJV1_Vhw2DPqwvNBTwYs3Eh0qq4ky85fQtp5zq5c_VWacZahUlF1NI0F47OCTjzYeJEtlh458K00Pw6zLM1QqlWJVZHs7EUajJgmMlExA5NfntnxaH9spTAZKVehpNPtQz2g8nPkNce1MFp-LxZnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از ساعت‌های پایانی مراسم تشییع پیکر رهبر شهید در تهران
🔹
سمانه صالحی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/667599" target="_blank">📅 22:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667598">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
پست بلاگر هندی از سفر به ایران برای حضور در تشییع رهبر شیعیان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/667598" target="_blank">📅 21:59 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
