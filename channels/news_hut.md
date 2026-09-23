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
<img src="https://cdn4.telesco.pe/file/KVJmVVMvGxE_cIvCwsou34InN-tKimzrVg4jeze_6Z3DB2NGfPLzHAPoSlndf3vfKL6zIXWCHfIPh3QFeeI_yyGC6N3jB0_gh1rVdnS3EmufVZ4K2cVCK4CSJR5mUtLGZe_Uw4rT4KqkX8WJrEr5Ol7s5drh4jAh_odA9jJnekMGlNae0q9N4euogr3yTkAlg2Q7R6ZCC5pnYjhLLHjD26WnDKwUs0jirs_l0PpWrRxCaD1imNcDsfnHcqeSbhJLjdz629xi1hgDgx7mFBzq9uxcadwrIEJnDp_m8C-3q22Td0X7lj74pwAtH-GndMkyhgcDkMwJu8UbGyJYRZpmKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 18:37:34</div>
<hr>

<div class="tg-post" id="msg-72135">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0aa24390.mp4?token=kYjqYW4iGaKT2gSWiX-_Z07vntpo8MEsjsiXD4VzyOJHjX9lcE9DlH6fTtkbPkTxXei-wAZ-hOCDsRYHZq-TtuFwysR2UM_wjwZQziGz4zr_Acqc99pxDthzNyvR15v6ceD81CpjHPhDKBHg-h_wzFTlJB7VY7oGCbfCf3XyzyLkLxZO-9EQwD89YK9XDJHI5nmYJKY7LTlJj1cfPQeGmB0JqggZMsGnxkr5eB_ZSS7_Q0h0oZLhedbosfbke5nUG4caEC6EXx1xwp9nk0xGJAKKIv25uzmNpOsHtryT9CeiiiYknxZUYlfB8PUnlda3BgmMvuOhtXtynGChz5Ns9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0aa24390.mp4?token=kYjqYW4iGaKT2gSWiX-_Z07vntpo8MEsjsiXD4VzyOJHjX9lcE9DlH6fTtkbPkTxXei-wAZ-hOCDsRYHZq-TtuFwysR2UM_wjwZQziGz4zr_Acqc99pxDthzNyvR15v6ceD81CpjHPhDKBHg-h_wzFTlJB7VY7oGCbfCf3XyzyLkLxZO-9EQwD89YK9XDJHI5nmYJKY7LTlJj1cfPQeGmB0JqggZMsGnxkr5eB_ZSS7_Q0h0oZLhedbosfbke5nUG4caEC6EXx1xwp9nk0xGJAKKIv25uzmNpOsHtryT9CeiiiYknxZUYlfB8PUnlda3BgmMvuOhtXtynGChz5Ns9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
آقای ترامپ و کسانی که به دنبال زورگویی به ما هستند، باید ایران را بشناسند:
اینکه ما آماده گفتگو، دیپلماسی و مذاکره هستیم، اما زبان زور را نمی‌پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/news_hut/72135" target="_blank">📅 18:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72134">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80dd97167.mp4?token=r4whk5DPI0lGQexs0KJI2CCD-peSfJs9XsHjjDNtVpl3tcjC8B4qnhMOfg4Kh8j212KC3F1SMbVTkloz2Il8gy8Uk8KRnxJl5BcKYxdlcVnj1rj9dBr0pXcVupYn24lEF5cfqeRjhf9HGnrz6nSKS1u9lrJfsLZ_mZzTraKM67m_jl403Tq4Gsex7p_XHSHHxEFZ9DXSSseI-q_jSEBuL-eZIln_pnTuEsho2_IpkYcELnAGJt_53CGwdHWNLkmVTz3kSPGDJ82XY2goEz7uS9wyValMj6DFzABVPlcmYW9wgFevxfYmDdPrw-VJeoCbnEuL2QhOv9Mxmuvr8QN7zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80dd97167.mp4?token=r4whk5DPI0lGQexs0KJI2CCD-peSfJs9XsHjjDNtVpl3tcjC8B4qnhMOfg4Kh8j212KC3F1SMbVTkloz2Il8gy8Uk8KRnxJl5BcKYxdlcVnj1rj9dBr0pXcVupYn24lEF5cfqeRjhf9HGnrz6nSKS1u9lrJfsLZ_mZzTraKM67m_jl403Tq4Gsex7p_XHSHHxEFZ9DXSSseI-q_jSEBuL-eZIln_pnTuEsho2_IpkYcELnAGJt_53CGwdHWNLkmVTz3kSPGDJ82XY2goEz7uS9wyValMj6DFzABVPlcmYW9wgFevxfYmDdPrw-VJeoCbnEuL2QhOv9Mxmuvr8QN7zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ترامپ باید بداند که مقاومت ملت ایران در برابر تحریم‌ها، افزایش فشارها و زورگویی‌ها، تنها بیشتر خواهد شد.
ما هرگز سر فرود نخواهیم آورد و زانو نخواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/news_hut/72134" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72133">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مسعود پزشکیان:
بمب‌های اتمی و هسته‌ای در اختیار رژیم اسرائیل است، اما از بازرسان خواسته می‌شود که به ایران بیایند.
اسرائیل بیش از ۷۰ هزار انسان بی‌گناه را در غزه به شکلی وحشیانه به قتل رسانده است، اما ایران در حالی که پای میز مذاکره بود، هدف بمباران قرار گرفت.
اسرائیل بمب و سلاح‌های کشتار جمعی در اختیار دارد، عضو «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) نیست و در طول حیات ننگین خود حتی اجازه یک مورد بازرسی را هم نداده است؛ با این حال، همه امکانات لازم در اختیارش قرار می‌گیرد تا بتواند هر پایتختی در منطقه را که بخواهد، بمباران کند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/news_hut/72133" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72132">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7f87b6f9.mp4?token=DlGruuGYxRtTgFdV4-1mGciYUNEPGpN15P_UOEzL3gL3DTstlwUCspyPlRF_X2_YYNdc4F-Ty_-N4sMYReWhrQOkEBAsKgfwKnrQKbRXPB0gksWe6976I12N27G41-rJDa_vSrgZ5gtywlNXkMeFkET9R479jOtGa09JOkotMRIWO6hEpJNBg5o-3oDSA5m2BVpyB51RqMZPxnYLzv8x9Pd0ntF71wS9yBpIBQ_taOy1ULxVg9Yu78YCUcLj9sliSH8927JJSG9616QyocHK8AeQRt6WLX6MbKoaTd34QwIgiIzK39AltMQaoJcC7pNA3oLfRODbJPmVQJfZv2inbYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7f87b6f9.mp4?token=DlGruuGYxRtTgFdV4-1mGciYUNEPGpN15P_UOEzL3gL3DTstlwUCspyPlRF_X2_YYNdc4F-Ty_-N4sMYReWhrQOkEBAsKgfwKnrQKbRXPB0gksWe6976I12N27G41-rJDa_vSrgZ5gtywlNXkMeFkET9R479jOtGa09JOkotMRIWO6hEpJNBg5o-3oDSA5m2BVpyB51RqMZPxnYLzv8x9Pd0ntF71wS9yBpIBQ_taOy1ULxVg9Yu78YCUcLj9sliSH8927JJSG9616QyocHK8AeQRt6WLX6MbKoaTd34QwIgiIzK39AltMQaoJcC7pNA3oLfRODbJPmVQJfZv2inbYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
مسائل منطقه‌ای ما باید در درون منطقه و به دست کشورهای منطقه حل‌وفصل شود، بدون آنکه به ابزاری در دست متجاوزان خارجی بدل گردد.
هیچ‌گونه رابطه‌ای با یک قدرت خارجی نباید به ابزاری برای تهدید کشورهای همسایه در منطقه تبدیل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/news_hut/72132" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72131">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be5f428e4.mp4?token=DOa2DSnRBVx4zawXnqgEe7nKA77RMcc-Tk-PusN30X-86G8nsq8ObowD-IreeretwjttzTnMyG5iTobYW2qlVRkdOpo7Uoq1uAaDo0nOOC5CZP4vrsTiVNd-GDXWo-zaNl1xc18gr9ZpagKoYW9IDztLJaAvOLxtv3Lph6D90VBdOL2wHbB9awUBOjzV8lHYSr-32VnioOlx4mA7nIP1ZtP2GoP2UyK7Rn88quQ8BR6S17kH_DEr1qA9xUPmQYc7tb1zl9Zpgy81bJcUN8KDwZ0VoBUp3bZ3H1xXIUi3pQS87VacuDRWhab2xYOtjaLBphQzSmAnzisidepqDMadAgmVYGoC9d8wC3JbR10-NNtdZ9MCagNM-FYoLajM_qq2sAqWtTkKCw5NmpurM86IvA2oMJBSyJyryRXeiInFUIZBH4xX43BHa1Zr8cwXyzzw0I8nUz95LGZHOXSHwh5HxOWzQJRVOYI9MBbT7y67eOO4zGiYlmesDtQ9cA10eg0AceptRoSKGHzJj8tq8y1IfWmxpmZXK5r6iIBIwjyeXW_7bYKeuPeWcvxbx1hv1-s-HMjqgkxgs8zGeRfnN0gtAoxBdklaxpGAts73FFkki1Wq-Ntdc9f3E1YkIE9WWsOpiT4pb1rYUXXhGAO1RJMrVL4m7Xi1Il2aS-WaV7qm3lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be5f428e4.mp4?token=DOa2DSnRBVx4zawXnqgEe7nKA77RMcc-Tk-PusN30X-86G8nsq8ObowD-IreeretwjttzTnMyG5iTobYW2qlVRkdOpo7Uoq1uAaDo0nOOC5CZP4vrsTiVNd-GDXWo-zaNl1xc18gr9ZpagKoYW9IDztLJaAvOLxtv3Lph6D90VBdOL2wHbB9awUBOjzV8lHYSr-32VnioOlx4mA7nIP1ZtP2GoP2UyK7Rn88quQ8BR6S17kH_DEr1qA9xUPmQYc7tb1zl9Zpgy81bJcUN8KDwZ0VoBUp3bZ3H1xXIUi3pQS87VacuDRWhab2xYOtjaLBphQzSmAnzisidepqDMadAgmVYGoC9d8wC3JbR10-NNtdZ9MCagNM-FYoLajM_qq2sAqWtTkKCw5NmpurM86IvA2oMJBSyJyryRXeiInFUIZBH4xX43BHa1Zr8cwXyzzw0I8nUz95LGZHOXSHwh5HxOWzQJRVOYI9MBbT7y67eOO4zGiYlmesDtQ9cA10eg0AceptRoSKGHzJj8tq8y1IfWmxpmZXK5r6iIBIwjyeXW_7bYKeuPeWcvxbx1hv1-s-HMjqgkxgs8zGeRfnN0gtAoxBdklaxpGAts73FFkki1Wq-Ntdc9f3E1YkIE9WWsOpiT4pb1rYUXXhGAO1RJMrVL4m7Xi1Il2aS-WaV7qm3lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما سر خم نخواهیم کرد و از حقی که ذاتاً متعلق به ماست، دست نخواهیم کشید.
صریح می‌گوییم: نه سلاح هسته‌ای و نه هیچ‌گونه محدودیتی برای فناوری صلح‌آمیز هسته‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/news_hut/72131" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72130">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2213909800.mp4?token=bD6yq27gDQ8OM3UDuud_314V2IsyzJOArxAAwXzs_3OX9dOUdUw98dRaSrCYWC62mPdiLC6-5kM6vJewGFszARJc2zUp-sD1UYWfNyq-4UwYNIIwb25SCySZ5MigiOP86nJhT5tzzrTJwBC968RNCL41HlpkDL41fP4s8E114cHFPOJCzjwIMWNeyh-DHWnXxvxgNr7FQxYYwrZaCjkWUGU_8dosb8r7_xBCqCyhMLy-BTCY0VnZDq-NG8AKXVyrXb9gJ_cSGBoqMA7Mf9KWgwPF0f4mWHto_GQ5lxgfhIeGT9fgyq293ihEWIW1tGZyuHclro3W9ZHMifjeBM8hYlh3woes6oNZdas-avMwy1TxZE2kAIbAujL6rQmDV4FMg3G7uvgFzFfr9GEWjxkSo_Gwbb_TyZAlffKYt8JsuMjOzefprZbCBVJ6_nEVkv8UZujKCHcOKHi59dG2lGhxjb8tySodIH6y663YH6Jol-m4q33BMlXMgqXqLsgdIglh4T0IHfnukEl7KBkUx4XklaJPL6UzW_tOGzTEo-ilJ0zusgOdql49J5H8SBWHCvtG_nIBrrR_j8UWSsG5kyd2rw-KrGPxrena4w5BUr-expHBHPpeuaH4tsbSifHTqGHAFtzmaVJZsTgPGu-MVZLEdVwt-uA_OnBy_Uy67QeLDQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2213909800.mp4?token=bD6yq27gDQ8OM3UDuud_314V2IsyzJOArxAAwXzs_3OX9dOUdUw98dRaSrCYWC62mPdiLC6-5kM6vJewGFszARJc2zUp-sD1UYWfNyq-4UwYNIIwb25SCySZ5MigiOP86nJhT5tzzrTJwBC968RNCL41HlpkDL41fP4s8E114cHFPOJCzjwIMWNeyh-DHWnXxvxgNr7FQxYYwrZaCjkWUGU_8dosb8r7_xBCqCyhMLy-BTCY0VnZDq-NG8AKXVyrXb9gJ_cSGBoqMA7Mf9KWgwPF0f4mWHto_GQ5lxgfhIeGT9fgyq293ihEWIW1tGZyuHclro3W9ZHMifjeBM8hYlh3woes6oNZdas-avMwy1TxZE2kAIbAujL6rQmDV4FMg3G7uvgFzFfr9GEWjxkSo_Gwbb_TyZAlffKYt8JsuMjOzefprZbCBVJ6_nEVkv8UZujKCHcOKHi59dG2lGhxjb8tySodIH6y663YH6Jol-m4q33BMlXMgqXqLsgdIglh4T0IHfnukEl7KBkUx4XklaJPL6UzW_tOGzTEo-ilJ0zusgOdql49J5H8SBWHCvtG_nIBrrR_j8UWSsG5kyd2rw-KrGPxrena4w5BUr-expHBHPpeuaH4tsbSifHTqGHAFtzmaVJZsTgPGu-MVZLEdVwt-uA_OnBy_Uy67QeLDQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ایران در دو قرن گذشته به هیچ کشور یا سرزمینی حمله نکرده، اما همواره با صلابت از خود دفاع کرده است.
با این حال، اکنون ما به ایجاد بی‌ثباتی در منطقه متهم می‌شویم و برچسب تروریست به ما می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/news_hut/72130" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72129">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مسعود پزشکیان:
کسانی که خود تروریست هستند و تروریست‌ها را آموزش داده و از آن‌ها حمایت می‌کنند، ما را تروریست می‌خوانند. ما تنها از خود دفاع کرده‌ایم؛ ما تروریست نیستیم.
مردم بی‌گناه ما هدف حملات بزدلانه‌ای قرار گرفتند که بر کشورمان تحمیل شد. ما با نهایت قدرت از خود دفاع کردیم.
آمریکا و اسرائیل با پیشرفته‌ترین فناوری‌ها به ما حمله کردند. آن‌ها به ما ضربه زدند، اما ما سر تسلیم فرود نیاوردیم
@News_Hut</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/news_hut/72129" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72128">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baa7d4e9f3.mp4?token=nC3A9F2bOaVKbDgvUO4JVVGot3E6oEaj_Z8pHVi0C2KNhLY50u2fb9lPGe9RvihMjWmQufiQKCCZjDA_nTQZ-pi5m42Vkxd1Anjy6WgKoN5ilTUvz5kG8GTDZeabwzFp68-0jG5mm25kptd5lJSU1xX8vyuCFMb64-k9EIHgB3Y5gxLlM0y9GpRqq6dg12TxX3mhI7Zp6JhRl_KNCgLDZcRUBqzVkMKeltGwKYWAgZEPw7QdpUmk-1Mey8d-4rJk_VPSnw-_DxkXmhjNxUCSv2Cb8l66xG2a8aN0MAGItFz_reYNc5D1YH5JpPjEoer177vETM7s6VCVFR3FDCk56zY4liE-3OovDMI9MevTGM-cjZaYbH7cGNZr6WMgTmUyyvhwdqHEjJAsRN1KFTB-aVUPvNATJhEo0mQqo2jcJxCkYVuCX1yDkzh5igF0pFlBcJfDWYVb3DzQogNAiqFE3Yr4masOUByJOqdLq7yoByspx8Cmosq9cmx51AEXMX8PjXjSG7GjXGkQOIvs7WtfzbzfNBvuStO8F7EMm_295rEdfjVqJ5tFjZru7gwuVOlfIV44TetLtGOWK75_JW6cWE5MJZLzhc2Aks5FQG4Vly1yRvL0n8sezAqsNpdcaFlreKHecL7zp0CCYLQs7j3mX74bD4lpIY6iWcqUGbldWhU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baa7d4e9f3.mp4?token=nC3A9F2bOaVKbDgvUO4JVVGot3E6oEaj_Z8pHVi0C2KNhLY50u2fb9lPGe9RvihMjWmQufiQKCCZjDA_nTQZ-pi5m42Vkxd1Anjy6WgKoN5ilTUvz5kG8GTDZeabwzFp68-0jG5mm25kptd5lJSU1xX8vyuCFMb64-k9EIHgB3Y5gxLlM0y9GpRqq6dg12TxX3mhI7Zp6JhRl_KNCgLDZcRUBqzVkMKeltGwKYWAgZEPw7QdpUmk-1Mey8d-4rJk_VPSnw-_DxkXmhjNxUCSv2Cb8l66xG2a8aN0MAGItFz_reYNc5D1YH5JpPjEoer177vETM7s6VCVFR3FDCk56zY4liE-3OovDMI9MevTGM-cjZaYbH7cGNZr6WMgTmUyyvhwdqHEjJAsRN1KFTB-aVUPvNATJhEo0mQqo2jcJxCkYVuCX1yDkzh5igF0pFlBcJfDWYVb3DzQogNAiqFE3Yr4masOUByJOqdLq7yoByspx8Cmosq9cmx51AEXMX8PjXjSG7GjXGkQOIvs7WtfzbzfNBvuStO8F7EMm_295rEdfjVqJ5tFjZru7gwuVOlfIV44TetLtGOWK75_JW6cWE5MJZLzhc2Aks5FQG4Vly1yRvL0n8sezAqsNpdcaFlreKHecL7zp0CCYLQs7j3mX74bD4lpIY6iWcqUGbldWhU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
مردم بی‌گناه ما هدف حملات بزدلانه‌ای قرار گرفتند که بر کشورمان تحمیل شد. ما با تمام توان از خود دفاع کردیم.
آمریکا و اسرائیل با پیشرفته‌ترین فناوری‌ها به ما حمله کردند. آن‌ها به ما ضربه زدند، اما ما سر تسلیم فرود نیاوردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/news_hut/72128" target="_blank">📅 17:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72127">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مسعود پزشکیان:
دیروز ترامپ ما را تروریست خواند؛ در حالی که ما خود قربانی تروریسم بوده‌ایم.
من از ایرانی می‌آیم که در آن، رهبر عالی‌قدر ما بدون هیچ‌گونه مبنای قانونی یا دلیلی ترور شد.
من از ایرانی می‌آیم که در آن، مدرسه‌ای بمباران شد. این کودکان را می‌بینید؟ این کودکان بر اثر بمباران با تسلیحاتی که توسط آمریکا و اسرائیل به کار گرفته شده بود، جان باختند.
آن‌ها بی‌گناه بودند و هیچ جرمی مرتکب نشده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/news_hut/72127" target="_blank">📅 17:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72126">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aca1a8c79.mp4?token=hk4CGH_2eJE12xp88s5D7bRQieGy1R-jrcWwjOxUZuaPEh0VDXSTuHPTawJLCi2gzthS3lDIRJ1RDVYzlFzrfyn50CB4MEkr4IsT6DuUQq6fkRQb8FgXlBMSB9dLznxGdWiMYDkUSshPHHAgjdb8fHIu_wmKJR7gm3K_OA-cK6uTk-I3JUdkvWdWbH37OIrpfCTceTBgNzkQzWpfWojcPal0XaYbQstm-iXnCaClsS6XQmRGt6furiPzzfBtL1HBufq_QhtoEo9vhtnXVLv2ZcBFSvzX4RYzeduG6wvDLFs72MRWnalPdgzYVuglxevj8NMiGrB3gCxpjgkgYA6P-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aca1a8c79.mp4?token=hk4CGH_2eJE12xp88s5D7bRQieGy1R-jrcWwjOxUZuaPEh0VDXSTuHPTawJLCi2gzthS3lDIRJ1RDVYzlFzrfyn50CB4MEkr4IsT6DuUQq6fkRQb8FgXlBMSB9dLznxGdWiMYDkUSshPHHAgjdb8fHIu_wmKJR7gm3K_OA-cK6uTk-I3JUdkvWdWbH37OIrpfCTceTBgNzkQzWpfWojcPal0XaYbQstm-iXnCaClsS6XQmRGt6furiPzzfBtL1HBufq_QhtoEo9vhtnXVLv2ZcBFSvzX4RYzeduG6wvDLFs72MRWnalPdgzYVuglxevj8NMiGrB3gCxpjgkgYA6P-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت نمایندگی ایالات متحده هم‌زمان با سخنرانی رئیس‌جمهور ایران، پزشکیان، صحن مجمع عمومی سازمان ملل را ترک می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/news_hut/72126" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72125">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72125" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/news_hut/72125" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72124">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK3df6nuFNFO3s__nNultZAWE19qSm6QUYsMoTyepVCpzlXi7WowPF2iVjycTzTNuOIUUoUbB0OTPDmvoRta4wD_7BoyyoZ_caTmSHWkOmbDjYwW-IFZbpnxzXoBTbTQJEy-tZB_O_PGBR9lF51WxnXPJtJ4Zw7gZaIx8pjV_GQFI5An8SDnwnIed4SRcm5QK5cSJbAX3PUcGG7G_ud1oULmf731A4PtnXx4s_wXEz6ssyCFI23YmKHr_xknwoD07dlnCsNvQAPKNnBBUYfdvOKR-yMO3h68mmB1BrvEbITg69SE2vMP0tGLaTTeoW0WQG_iQl9EyBjhltxABhG-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/news_hut/72124" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72123">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4142dc5d8.mp4?token=Y4tpMLV6VSaBC0XrRWEP4i9s-NfRRx21NVKOpJvusyyuCPp-6ZwpigYB8PqVcxbIN1W66BRppHdH8to6JgCR3vdqzs0oddREnyklVo-F7ZQBnGkT5_AX10RE8zEU9FeEFZZQkynoTEG2eIMZArmQPpNZ0_c0Iwpqck0X9WEfrJgQJSDeTJDOmYFWg0r8isQcv_DOMNeljCAPOGdgJs7jFlNsLxcUilgJAar5KUZaHY26fYs0keFHYjr27LZnWHGHLMes8BmR70TbxpFhYGZA_MiGKgxD0EI1Nr2Xj0Bl4g3hVtwMloXJgqoCL_1RnDb7b8vyfbPi3bB-upVIYZ0nVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4142dc5d8.mp4?token=Y4tpMLV6VSaBC0XrRWEP4i9s-NfRRx21NVKOpJvusyyuCPp-6ZwpigYB8PqVcxbIN1W66BRppHdH8to6JgCR3vdqzs0oddREnyklVo-F7ZQBnGkT5_AX10RE8zEU9FeEFZZQkynoTEG2eIMZArmQPpNZ0_c0Iwpqck0X9WEfrJgQJSDeTJDOmYFWg0r8isQcv_DOMNeljCAPOGdgJs7jFlNsLxcUilgJAar5KUZaHY26fYs0keFHYjr27LZnWHGHLMes8BmR70TbxpFhYGZA_MiGKgxD0EI1Nr2Xj0Bl4g3hVtwMloXJgqoCL_1RnDb7b8vyfbPi3bB-upVIYZ0nVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیمت کوکائین در تهران چند؟
پلیس مواد مخدر تهران بزرگ ، یک بار بزرگ کوکایین کلمبیایی را قبل از پخش در پایتخت ، کشف کرد .
این کوکایین ها بیش از ۵۵۰ میلیارد تومان ارزش گذاری شده است.
گویا داداشی ها سهم  مامورا رو ندادن اونا هم بار رو لو دادن
@News_Hut</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/news_hut/72123" target="_blank">📅 17:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72122">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dadfb7a92.mp4?token=EBhPmvo3eNO9waFhn_4lJRsRi-uWbh4jL6osvqs1851coVsHZNGUcLuMiyZuZNJJ8HupCuO8IyS77p_LB45C17GkaYO5r2-l0JzoSRPTv1Ail3Ms4Y5CZ5Uzf0FphPbWbhEiAtNOGZFba92RYeeMP3tKhVUUHNa5nQA_StKjxQAQ8fvaxZGs3HUTJATfDtWcg8C0JOZCkqVjFSElaEatfysYNorUYr05QA4SZiwp_9-EiSwIajINFBIYGiUs-cMNO9URNUfm5Ic5KAge1Z7a-xR2zE___cqq8xU0d5x2dn61LEbNtdQUkYDuE6ob6sXdzwn9-y12i0Kdk0ik8_9U7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dadfb7a92.mp4?token=EBhPmvo3eNO9waFhn_4lJRsRi-uWbh4jL6osvqs1851coVsHZNGUcLuMiyZuZNJJ8HupCuO8IyS77p_LB45C17GkaYO5r2-l0JzoSRPTv1Ail3Ms4Y5CZ5Uzf0FphPbWbhEiAtNOGZFba92RYeeMP3tKhVUUHNa5nQA_StKjxQAQ8fvaxZGs3HUTJATfDtWcg8C0JOZCkqVjFSElaEatfysYNorUYr05QA4SZiwp_9-EiSwIajINFBIYGiUs-cMNO9URNUfm5Ic5KAge1Z7a-xR2zE___cqq8xU0d5x2dn61LEbNtdQUkYDuE6ob6sXdzwn9-y12i0Kdk0ik8_9U7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مادر توی کمد لباسای دخترش، کاستوم مخصوص سکس پیدا کرده، بعد دختره هم به این شکل مامانشو قانع کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/news_hut/72122" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72121">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAkI8k3zoQXiLmEOfa4WSYk23fFVLWsTiKkcEXHjynqX13VTlYrfuGl-AMpTu_m-F-xveYsGEDYt-xhR8CQ7z6tbu00eihb6hcvlUM3eroxyn2AD5rC-XqR7EucnnnFAWZ_frbGaYmibVS8CZExGeJQTWG-QTk65ygaNYM96Y8DEQ0xKB5ZC9zGPGivYj7ojdlNOwdXQ-eJMkrZMZKuv8HeCqqrMUpYDJOiFOU1mb4x4DwVXYPeTZ-WJpPm6miiTzpZji_ttNkjdHpJnr8jcQ-EfBgUoWVFow5lUwrtNXofNjDCYtB6nwgs98AhYPWDU63LxobOLlCpo7sW9zAfZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک کشتی باری در تنگه هرمز هدف اصابت پرتابه‌ای ناشناس قرار گرفته است.
این کشتی دچار آتش‌سوزی شده و بر روی آب سرگردان است. خدمه کشتی تخلیه شده‌اند و گزارش‌هایی از دو مورد تلفات منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/news_hut/72121" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72119">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056cf75693.mp4?token=ailiX5nH3XKieGhKxIXAWNqB2Wof8K15SE7YByYmNAh4RO4aWO8Bn0apRnwR9rgMA4-ghFmY8eHh0mf8b3bzIDzavvVzUltNCjVP1Imz5eFILQLznM5lNONeAtP3uPwrgkE05LU4QZmJlhZNSCQlGfvL8dTF8J2D0jbmnHhhFVZskp6zGSNEiT5UkneWiCdQ3sFyLrIZa4SZweiDlMydzAwf3T22IPABJAa1qAQjoDG4degS_CdgcjDXoDf0lLU-I3gO7DiJiwezx87CQ1FuWjVjySDahv24dQuOqnzRMSp4QDUlVUQsxWbzge5fM8k8Y2yKVH3B5BEVZLHHJLi9dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056cf75693.mp4?token=ailiX5nH3XKieGhKxIXAWNqB2Wof8K15SE7YByYmNAh4RO4aWO8Bn0apRnwR9rgMA4-ghFmY8eHh0mf8b3bzIDzavvVzUltNCjVP1Imz5eFILQLznM5lNONeAtP3uPwrgkE05LU4QZmJlhZNSCQlGfvL8dTF8J2D0jbmnHhhFVZskp6zGSNEiT5UkneWiCdQ3sFyLrIZa4SZweiDlMydzAwf3T22IPABJAa1qAQjoDG4degS_CdgcjDXoDf0lLU-I3gO7DiJiwezx87CQ1FuWjVjySDahv24dQuOqnzRMSp4QDUlVUQsxWbzge5fM8k8Y2yKVH3B5BEVZLHHJLi9dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانیال عیوضی، مجروح کشتار کرج، پس از ماه‌ها تحمل درد و جراحات، در دی‌ماه ۱۴۰۴ ترکیه را به مقصد اروپا ترک کرد و امروز خود را به سازمان ملل رساند تا درباره مشاهداتش از کشتار و برخورد مأموران امنیتی جمهوری اسلامی شهادت دهد.
هیئت ایرانی تلاش کرد سخنان او را مغرضانه و تند جلوه دهد و مانع ادامه صحبت‌هایش شود؛ اما با دستور رئیس جلسه، عیوضی به سخنان خود ادامه داد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/72119" target="_blank">📅 15:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72118">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96e8038a0.mp4?token=Pec3uk-3vV2yYusdaSEcIvs2XS8M61uM9m_lqilfMsP-n4puyT8SBjkvbra_iTSAmgHgKV6q_8MCZ621iEKEhXhthWmblLZ4_W3RFyrd_1RF-p8IwA1HYwy_9-HpljxnI91R8hi59a543uOa7E5LIunxDhEgxDBzqu50XZRXrge8HJmmFjDLV1ngbK-Yc_3rrLUjwWP0qrZ2bPMD_jFRq1fc2I0I4XyRso-BLKraiwQxFQkbHx0xb0Aht8JqK1eG7QLB8wd8RHWOIzpS3lLmwr4gTbyqKJ5idc5I-B1GR7kMLKwZWxpJqomY0N-GCCvnEqQGTBpTZJAw52pnin00_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96e8038a0.mp4?token=Pec3uk-3vV2yYusdaSEcIvs2XS8M61uM9m_lqilfMsP-n4puyT8SBjkvbra_iTSAmgHgKV6q_8MCZ621iEKEhXhthWmblLZ4_W3RFyrd_1RF-p8IwA1HYwy_9-HpljxnI91R8hi59a543uOa7E5LIunxDhEgxDBzqu50XZRXrge8HJmmFjDLV1ngbK-Yc_3rrLUjwWP0qrZ2bPMD_jFRq1fc2I0I4XyRso-BLKraiwQxFQkbHx0xb0Aht8JqK1eG7QLB8wd8RHWOIzpS3lLmwr4gTbyqKJ5idc5I-B1GR7kMLKwZWxpJqomY0N-GCCvnEqQGTBpTZJAw52pnin00_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقرار پدافند هوایی روسیه وسط بزرگراه رو دریابید
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/72118" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72115">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mn4xbYJQsACO_VMOpNqRhVTFD58SSOa41WV_l_NARCUxT9AqXVeFgDOCZukWcTmfnuFfO-4WnDNs9kg0U1nHp7hBTzPaSSTk9IdCC-InZJmR9jmCDgNbIRmCPLWuinLg4FnmkD5_vqRJO3RsDBZJRchDovYnSkbmUKbB8KQ9ebCn1A5x5y31BHh604M623r6RS1S3twqVxxDAesXXdq1GoXSMkaKkc0jBxDx3diA8x29gnIVGdNU0bhMrunzcCTmwRigl0OlkTL_TUNdAMaW8dFf5DEZtR3ZRKFbTQN2rx1ZljThdqY6WJ44USgQkdBu5RVfj5gOcshSi6ou3HhzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmHXXNDNOLaqePx1Th-lTC8PmwHDhWcHg7a6L1e7Xb0kB268paPUUKhnLw5oEiwcHv35BqhgHVjodnB0vlYwtNSiwfPN1puMr0pbJQrAfzIgHSvzl4ndn_ESNcEZyjzN57tZ6sl7kIRmG5IfhCrwjPvsDy-2n4MvzEVuozCzGJjK1mgfDyJpRZIZhXGGCPSEjpl8ZJhlaN2eLLCHERdbaFTmLPgvGNhAmq13rCMgHxQq8clFe6cb2pOB4MN3lpXs3dXwhJXtDvkSgyM1jrUCgV_gcgXjZIBPLMDGu1PaXTNZkv_Nes6BXeWRaF94oY7RJrS0x3J5LbMnG8n1a0xMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1KBaUTrsuWrFZbnfT4Z47zjW954uMd3plI2agqXQEUFAP2lFMQDgjVojhDuUjug5uKn6MRuNywnLwqAv_lREVBEYLzUOHXfVi33A06DLZRAp8euWZ2UNwvsyXAuLNfSkdUtsQL31JYYEChiDm60YzebxGkNjb2fTyFouCxIrCnT96Wg1XoalTM8XZDZ8XW2xetobdtwDnA9049b8c0DYbUCOOacGpz1b6u3ZiQONbiZo9smy3nPjIX1dX-sVkGT1AWechC4_G4b_lfcUpbZBILbY7Gi00nhv9TBugIuui-AE0cMWl_iuSyoIHY1Hg3AF8AlRiltcHzKq9HS14JChg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این بیلی آیلیش هم روز به روز داره خوشگل تر و جذاب تر میشه هرشاتی از خودش منتشر می‌کنه کلی لایک میگیره :)
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72115" target="_blank">📅 15:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72114">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه بخش هوانوردی ایران، چندین کشور را بر آن داشته است تا پروازهای ایران را محدود کنند.
محدودیت‌های تأیید/گزارش‌شده:
🇬🇪
گرجستان — ممنوعیت کلیه پروازهای ایران از ۲۱ سپتامبر.
🇦🇿
آذربایجان — ممنوعیت فعالیت شرکت‌های هواپیمایی ایرانی از ۲۲ سپتامبر.
🇮🇶
عراق — تعلیق پروازهای ایران به بغداد؛ احتمال تغییر مسیر برخی پروازها به نجف.
🇴🇲
عمان — توقف پروازهای ایران به مسقط.
🇶🇦
قطر — گزارش‌هایی مبنی بر تعلیق پروازها از مبدأ ایران.
🇹🇷
ترکیه — اعمال محدودیت‌های عمده.
برخی مسیرها همچنان فعال هستند:
🇨🇳
چین
🇦🇲
ارمنستان
🇦🇪
دبی/امارات
🇮🇶
نجف
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72114" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72113">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHZ0uBGVXfc4yVBymTJ9OFg8rDFslmH1mbECxWek44iGWPfL86BdKcNt5A-HN6JYMUC9DX9V-YAacIZD94KYG90LXPBzG08LPZjKlElUa6h8Rm_wM4LcWtGzKUTL3jrqqHEeolZMr5AwrXrjDVv9D-VhSrVI8crRq1ECo1eg9Gm5dxzQivguquIg--C2A63MkOF0SL46fOwQZktLrRJrAlNlxaBbh2oz6k1Rmnw2H1gfHk9fHkGpP6u94FrACgMqvYBjqpgI46aoNC7er5us1Q912tTqvZzM7LpWwoI7HIonB07H3KX_XOFma_BvtXYOtJ7EDqjj6qYsHVwDwWFCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بازنشر کرد:«ائتلاف نتانیاهو در تازه‌ترین نظرسنجی انتخابات اسرائیل پیشتاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72113" target="_blank">📅 13:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72112">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/foADMWJC8ZipsZ_fhlX-ND1ald90TeqN9vObvN9QdwuRGUcQd0Tr0nV8DgToKeHp9tMNCdJVStDDXgiQMnAEYFur75N-Wf7vXkFPv_6rv5X3W9QDbGIUkrZHSayPTcdCu58WWzL0oc_rAdJx4AGz7izp20oYzpPJ27YhgfAgW2M0jSTuo4UVusUWwIMsAEF-jDasbm8TdtVAE5kXcQCge4Z7D2K3G6Gcquk2WNT9-zhZqYch198cH2Rp7kVzduIRVySXjIGm6gP1XzFtj1d82ESZ8DjsUycwsy2azOs5TfTO_W_ziFjpl4I3rPgDQy0xFDVwTjnrwt2y3jZTlbUl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌ و هوای یکی از دانش‌آموزان در جشن شروع سال تحصیلی جدید:
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72112" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72111">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3684649a.mp4?token=eU_OFdvlc7GbDbj5wYDECjPdfC5HydsjA-Bro4FreduCu3lWajbVzY8E3m8tLwRwe9TrWjkbH8qe_TM-4VpM95Ct8YY5oqWNbFVuAWCdiVX-yBQERTahZKkY-TRUb2RgZgvFhmA_t0uzX72W236-xopBzIhiIcVOiiIHv0OPHN5oPwzgeRzEGPFF9jBCVOtQZ5T5qU_rseNe_tTLh_FW0uV2kSSn1qieXLD0JudxvJ7NMMa_ediRmWKLNaVf1HEq2MTBHTImu6Sok3htbfDtyQFGrh3RsCUuX6Xdz9PH-264XHBqbX4vepzvNXYfGQB38rKDdNiZbrKxgj86rYGCnIDEBQeNY5yasbYSZqkakRWoZpurBELgUvgPowQs_xCTrdIYPFTIuKP1TVXgcb1smZiAVtjI_paRNCST9VrI0s74P37_UI08NM666kGnnZrzLgyZKZdYZR1k058Gc9Tf8muEVOlYLNmzadfwvmN13xTzlhO5_c_Jtau0AUZGplbh6Hug_HFM6hjmAMHiG9PXJGRvuf-P-WHXWpT3n94RtmWf9DyFvzgmsN6WN62-vykNlujb7e-Jg3ndTvnNXlW2W1_tRblVHYatAdd4O08YK9hFfeKgZ4qxO5pi8OH1JkFuISmPgVbvVzpJqk7DqbzDNzMfpZp9We84hPfQHeRZyw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3684649a.mp4?token=eU_OFdvlc7GbDbj5wYDECjPdfC5HydsjA-Bro4FreduCu3lWajbVzY8E3m8tLwRwe9TrWjkbH8qe_TM-4VpM95Ct8YY5oqWNbFVuAWCdiVX-yBQERTahZKkY-TRUb2RgZgvFhmA_t0uzX72W236-xopBzIhiIcVOiiIHv0OPHN5oPwzgeRzEGPFF9jBCVOtQZ5T5qU_rseNe_tTLh_FW0uV2kSSn1qieXLD0JudxvJ7NMMa_ediRmWKLNaVf1HEq2MTBHTImu6Sok3htbfDtyQFGrh3RsCUuX6Xdz9PH-264XHBqbX4vepzvNXYfGQB38rKDdNiZbrKxgj86rYGCnIDEBQeNY5yasbYSZqkakRWoZpurBELgUvgPowQs_xCTrdIYPFTIuKP1TVXgcb1smZiAVtjI_paRNCST9VrI0s74P37_UI08NM666kGnnZrzLgyZKZdYZR1k058Gc9Tf8muEVOlYLNmzadfwvmN13xTzlhO5_c_Jtau0AUZGplbh6Hug_HFM6hjmAMHiG9PXJGRvuf-P-WHXWpT3n94RtmWf9DyFvzgmsN6WN62-vykNlujb7e-Jg3ndTvnNXlW2W1_tRblVHYatAdd4O08YK9hFfeKgZ4qxO5pi8OH1JkFuISmPgVbvVzpJqk7DqbzDNzMfpZp9We84hPfQHeRZyw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل:
ما می‌دانیم رهبران ایران کجا پنهان شده‌اند. ما می‌دانیم آن‌ها چه کار می‌کنند و چه می‌گویند.
به گمانم جانشان برایشان اهمیت دارد. آن‌ها دریافته‌اند که اگر به اسرائیل حمله کنند، تنها چند روز طول می‌کشد تا سراغشان برویم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72111" target="_blank">📅 12:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72110">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402f33620e.mp4?token=iTClk7YvGGUlVsJasreJCAzsDxxuNhWnLGRcYUx688aAVMmT-AUu7BkU5VKzZAepPfJ6aNdD2_opgFA9s2mGcWqTIt9pzwtDJsh4DtkmjZE0ncYZzXgk1Lq5AXXjEM_CQPAbmauiJlBOoXLFTwNpQeY8mB4ex33JwiJzwPhJ_w_BbNi4_GkFQhvEDdJUazCkbb9zS3dujRtnUVrhNhbVt_TQNncNVvORrYClGmMCYk1gK59xNzR5iYdyyGsnnmyee_YqQZzzMSGXOmrtlie_O3Q01jjidBXnwjafjYoisH4Rks1OmoLJiW7Wm1ZhhIayU1RwrD1PP2dEZ9uzMUDlSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402f33620e.mp4?token=iTClk7YvGGUlVsJasreJCAzsDxxuNhWnLGRcYUx688aAVMmT-AUu7BkU5VKzZAepPfJ6aNdD2_opgFA9s2mGcWqTIt9pzwtDJsh4DtkmjZE0ncYZzXgk1Lq5AXXjEM_CQPAbmauiJlBOoXLFTwNpQeY8mB4ex33JwiJzwPhJ_w_BbNi4_GkFQhvEDdJUazCkbb9zS3dujRtnUVrhNhbVt_TQNncNVvORrYClGmMCYk1gK59xNzR5iYdyyGsnnmyee_YqQZzzMSGXOmrtlie_O3Q01jjidBXnwjafjYoisH4Rks1OmoLJiW7Wm1ZhhIayU1RwrD1PP2dEZ9uzMUDlSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز یکم مهر ماه، بچه‌های میناب دیگه نیستن که برن مدرسه...
اما جاشون پیش خواهر برادرای بزرگترشون امنه
🤍
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72110" target="_blank">📅 11:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72109">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92a5ff67f.mp4?token=AsNjR0O5RvVyUFCg85qUE__kPsNvfMYMUNTJRr23zSbs9YD_Ab_xCfk-UtQizPNUAu32-ci61j-F18ENYoNAvmeg1m230IJKU08ZQOrdudHOqqUXAeUPMT1mqLbTHqyBe4_zMkHl98B8E3V6k7wx7wewd-ruVqXrzqzbEykAGxth8U8gFZmopxg1LGxas_idetjA5Hm7RgI82wuCmMgdfC50bK0yqiVbKjmyjHzi3VgvZ9V2A5lDNq2CNeokFc0tn3LXciomSQXSnRyllBJ1Q5TnKf7bkLMG_2V7WcRp9XW7rDO21LELuzZJLApP_huyLHBkpNr-GDFT18ZVvjXbN1iAUeK-t2VGz55es_QDG0Gv9WlXMWrPGFrjk9acLGdlIr9l_qYcRjvJdK2jtWMSI2AAwuZzIjXC9HeHtP34D1JUlk2s9mDXiw5fG_qYhFnmC3Ooh5ki5OhnoIAafGtwjAe1t_zTLjuHOG6uVEsRA_fdA7qb138USWbq3FaN-irQhdTmFjWMGPiphC9S8r026JopYyPKqDD6zzxqsMm-PW1MJjJMOlpPqu3QZFyLM1hcHf2YJenN4FTn6SYPPvyu3QTD_VO78yolHV108EcEvtSakPJ25JgVLCXjU12wgDnrNElkp78Ve-uwRWhNb-WO8TV7RfLUrYzGkZJIo3LPUpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92a5ff67f.mp4?token=AsNjR0O5RvVyUFCg85qUE__kPsNvfMYMUNTJRr23zSbs9YD_Ab_xCfk-UtQizPNUAu32-ci61j-F18ENYoNAvmeg1m230IJKU08ZQOrdudHOqqUXAeUPMT1mqLbTHqyBe4_zMkHl98B8E3V6k7wx7wewd-ruVqXrzqzbEykAGxth8U8gFZmopxg1LGxas_idetjA5Hm7RgI82wuCmMgdfC50bK0yqiVbKjmyjHzi3VgvZ9V2A5lDNq2CNeokFc0tn3LXciomSQXSnRyllBJ1Q5TnKf7bkLMG_2V7WcRp9XW7rDO21LELuzZJLApP_huyLHBkpNr-GDFT18ZVvjXbN1iAUeK-t2VGz55es_QDG0Gv9WlXMWrPGFrjk9acLGdlIr9l_qYcRjvJdK2jtWMSI2AAwuZzIjXC9HeHtP34D1JUlk2s9mDXiw5fG_qYhFnmC3Ooh5ki5OhnoIAafGtwjAe1t_zTLjuHOG6uVEsRA_fdA7qb138USWbq3FaN-irQhdTmFjWMGPiphC9S8r026JopYyPKqDD6zzxqsMm-PW1MJjJMOlpPqu3QZFyLM1hcHf2YJenN4FTn6SYPPvyu3QTD_VO78yolHV108EcEvtSakPJ25JgVLCXjU12wgDnrNElkp78Ve-uwRWhNb-WO8TV7RfLUrYzGkZJIo3LPUpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات روته دبیر کل ناتو درباره ایران:
چرا برای از بین بردن توانمندی هسته‌ای ایران، حضور ایالات متحده ضروری بود؟ چرا اکنون در ماجرای حوثی‌ها در دریای سرخ، همه نگاه‌ها به ایالات متحده دوخته شده است؟
زیرا اروپایی‌ها به نوعی از توانمندی کافی برای انجام این کار به تنهایی برخوردار نبودند. آنجا حیاط خلوت اروپا محسوب می‌شود، نه حیاط خلوت ایالات متحده.
در آینده، دستاوردِ داشتنِ یک ناتوی قوی‌تر این خواهد بود که اروپایی‌ها می‌توانند خودشان به امور حیاط خلوتشان رسیدگی کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72109" target="_blank">📅 11:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72108">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اظهارات روته دبیر‌کل ناتو درباره ایران:
می‌توان گفت که اجرای عملیات «Epic Fury» بدون بهره‌گیری از اروپا به عنوان سکویی برای اعمال قدرت ایالات متحده، غیرممکن می‌بود.
از ۲۸ فوریه سال جاری تاکنون، ۵۰۰۰ فروند هواپیما در پشتیبانی از عملیات «Epic Fury» از پایگاه‌های اروپایی به پرواز درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72108" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72107">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72107" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72107" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72106">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMwKJtxdI5XbA3k0yXXB44o2l-8K-4y6tkIsAjaHKrI_9cZo61sOmi3H0WX8H-h9s0Wu1eAvkTQtWugNVIjrUsYt5RzzxHRAJu9J6dwFeC1tZ9MQ8NwfZOIwU00KbzQWdrtb-Gfes8hMW_z4gd32X_YZ-PYVynX1BXBt4pFuDGAEZkuwn4YRvpflrEPNYTd-mIzTcHjuHES1-nDR5vImy7OH_lBynDBzxrB7O_uFlFxOveMu7GVFiYfp4m1ji03TyTxaYnIPjqfShQMwYn8iG8dIBSooJcNWFfrr6un5N4Vhq43LTU9GG9MTW6ZJbKNJkT3RKdaA9TvREp_QBiQaHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
هیجان مسابقات DOTA 2 را زنده در
TrexBet
دنبال کنید و با پیش‌بینی دقیق نتایج برنده شوید!
🦖
پوشش کامل تمام بازی‌های محبوب Esports:
‏CS2, DOTA 2, Valorant و ده‌ها گیم جذاب دیگر...
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72106" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72105">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت شناورها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72105" target="_blank">📅 11:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72104">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4629cd7c2a.mp4?token=fm-NKwYEJYgJu-ukOa9LUg7FdvRwiyP28xAsTZKZRNOWURgNfRi-Nt--krg4UFxiHXFa_STzYQBFFsTxdrBJI9MooFyo-anZP-rcbrim5X2CvrMuoiF5ERMF6e67tlxvCO0b1R0tFgmtC7-huoy7pVXyVhvtuCCOUV-35FFUDycsOutRWr7zWCS_j7-rx-xS0WDF9UOL3nswz4rBYXzmKRCGPZINiYIPtPHg6Lk1-zSX45SQs617_8EAbo1AGcPpfXIv7j8Lugkb-fXDw6-Ol7xup3JopBddMbvt99ClujHS6205H4Lr06wqCMXGBLgEeuSiXJio4VUT4g1Lnml3MmmkVOlYw24iL6cri8H6hF_dmFnCWOFCwCSj7Kia7zDQI1ojZTawC6nmEhn7Tj5GJ55NhByILJFIqcmqrNqCL9cg_Bjb2LbIIiRIGjrphXuNn0dCS2X785SsZbxlvMCFVLJhtePU0XxZ3u91AkmysuNZmYsttvcorb_xVUUixQ8EqRmBhU4NvYpNCnTuH2LfXGPydOLle9TwKW2B84lDaaDC1OIPNQmJ71F7dPsfipGpc4EFLW195RZB8rEbBqhPn-EwqIuNQ7cP65PdN76bXwwrpYgr7Q2ExEI58YHK_LxKvdYhCZX-spTnzi696AppbcNZ-rU4Qg358k33Ca7XWNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4629cd7c2a.mp4?token=fm-NKwYEJYgJu-ukOa9LUg7FdvRwiyP28xAsTZKZRNOWURgNfRi-Nt--krg4UFxiHXFa_STzYQBFFsTxdrBJI9MooFyo-anZP-rcbrim5X2CvrMuoiF5ERMF6e67tlxvCO0b1R0tFgmtC7-huoy7pVXyVhvtuCCOUV-35FFUDycsOutRWr7zWCS_j7-rx-xS0WDF9UOL3nswz4rBYXzmKRCGPZINiYIPtPHg6Lk1-zSX45SQs617_8EAbo1AGcPpfXIv7j8Lugkb-fXDw6-Ol7xup3JopBddMbvt99ClujHS6205H4Lr06wqCMXGBLgEeuSiXJio4VUT4g1Lnml3MmmkVOlYw24iL6cri8H6hF_dmFnCWOFCwCSj7Kia7zDQI1ojZTawC6nmEhn7Tj5GJ55NhByILJFIqcmqrNqCL9cg_Bjb2LbIIiRIGjrphXuNn0dCS2X785SsZbxlvMCFVLJhtePU0XxZ3u91AkmysuNZmYsttvcorb_xVUUixQ8EqRmBhU4NvYpNCnTuH2LfXGPydOLle9TwKW2B84lDaaDC1OIPNQmJ71F7dPsfipGpc4EFLW195RZB8rEbBqhPn-EwqIuNQ7cP65PdN76bXwwrpYgr7Q2ExEI58YHK_LxKvdYhCZX-spTnzi696AppbcNZ-rU4Qg358k33Ca7XWNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:
تولید ناخالص داخلی ایران در سال ۱۹۷۸ دو برابر کره جنوبی بود. امروز، تولید ناخالص داخلی کره جنوبی پنج برابر ایران است.
وضعیت اقتصاد ایران قابل تداوم نیست؛ پایدار نیست و در آستانه انفجار قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72104" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72103">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/582ee3d494.mp4?token=pLcacgW7Eb7vi9eCX05qoTtGIzBa5Ys4PgTlAroZ1NUrpQnyWpk8hmzzYdBUI7ibeFasRvpnPTk_tynuCC7JAM7GR4tVog6hR_Gf9ASkWWDEddfaJgiaMWSdvtuwgSUZ3co7NhG45A4MdaRgr49WaDiTOP-DQ5SuyPVx9Al6WrOM33hJYYKJbuqdEaAjvF1n4hHe9otrr6v7kpgAQRONFAPYbU26YfePeDHoL2sb2XthKVZp_BNFAmvyVEbgbXsZl9BatFXX2lXon9_V49PSaW4BjoVcX57crDeTyWGfWvtgMsde8_TUdlAMlzo1iCw6njHHLxPM4hhkEuO6hUiJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/582ee3d494.mp4?token=pLcacgW7Eb7vi9eCX05qoTtGIzBa5Ys4PgTlAroZ1NUrpQnyWpk8hmzzYdBUI7ibeFasRvpnPTk_tynuCC7JAM7GR4tVog6hR_Gf9ASkWWDEddfaJgiaMWSdvtuwgSUZ3co7NhG45A4MdaRgr49WaDiTOP-DQ5SuyPVx9Al6WrOM33hJYYKJbuqdEaAjvF1n4hHe9otrr6v7kpgAQRONFAPYbU26YfePeDHoL2sb2XthKVZp_BNFAmvyVEbgbXsZl9BatFXX2lXon9_V49PSaW4BjoVcX57crDeTyWGfWvtgMsde8_TUdlAMlzo1iCw6njHHLxPM4hhkEuO6hUiJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگان هواپیماهای باری نظامی، از جمله هواپیماهای «آنتونوف ۱۲۴» در حال فعالیت از فرودگاه لایپزیگ/هاله در آلمان مشاهده شده‌اند.
فرودگاه لایپزیگ/هاله یکی از مراکز مهم لجستیکی ناتو است که برای انتقال تجهیزات نظامی و محموله‌های فوق‌سنگین مورد استفاده قرار می‌گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72103" target="_blank">📅 11:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72102">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2bb73b79.mp4?token=VtSyj_658B3fEXxX3fVKHrPt4xJn-kEdbAUvIA5Y9aUDgu-IafHN7d9bh1Djjfrmt9zZjtR3hIv_xlVuOqNT_aVccBS_7eZqYPt_WpNsxTrOKKgTPPOeiagTJ6HNNSbaTMi-Q5e_1NHfjvv982gIr-nntC-m0fIzSxR_q978CjseJoNaCHGloRCj968h7lxLmkqqdJkMEkLkS2uLcZMGUkS2vXtrO0c_djup1EKByk6xIiTNN543l_drINcC8idy0Wzmx__SxK4WoUI_k_DDJXKVkkGWAWzSsPY86rMqjxISafzV04q2tlY0qhp2DFy2tKmk6sA6xpJOdtvoYBnnvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2bb73b79.mp4?token=VtSyj_658B3fEXxX3fVKHrPt4xJn-kEdbAUvIA5Y9aUDgu-IafHN7d9bh1Djjfrmt9zZjtR3hIv_xlVuOqNT_aVccBS_7eZqYPt_WpNsxTrOKKgTPPOeiagTJ6HNNSbaTMi-Q5e_1NHfjvv982gIr-nntC-m0fIzSxR_q978CjseJoNaCHGloRCj968h7lxLmkqqdJkMEkLkS2uLcZMGUkS2vXtrO0c_djup1EKByk6xIiTNN543l_drINcC8idy0Wzmx__SxK4WoUI_k_DDJXKVkkGWAWzSsPY86rMqjxISafzV04q2tlY0qhp2DFy2tKmk6sA6xpJOdtvoYBnnvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌ کم ربات‌های جای انسان‌ها رو دارن میگیرن....
برای اولین بار تو تاریخ، یه مبارزه رسمی بین انسان و ربات برگزار شد؛ که در آخرش ربات با یه لگد سنگین حریفشو انداخت رو زمین و ناک اوتش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72102" target="_blank">📅 10:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72101">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2331092d7.mp4?token=mJJa8bIP63VZ6R3j9wdt1z6vnNwJxHDz6dLY2rUDU9kbJe2bs6p3vs_9dl_2Cf-J4BDO8GRxaFdUGWhnei4M36t581hLQXGf2TPXX22D1U9Q12kthhMXT71j0rYCGe4sIUblmmL8Y8dU4aYbzl8mRrD5jcN1TVl1YlS6LRbWDq6wQnVTJ8epYEEkGqX-I_lhHIQdLJmtqPw1YpSp6l0-YX8YD3qCwf7sO9UGcsoES1dz2DHGtqmyCYo2jH7C3LbR7Qps8O3H_7-mJhsIBvAHJReaEZYsHJqQBe9BWPcwRqTHBWKdW4RvN2lGu2BbcZOEYFwayaapo2HTwc4zGkF8AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2331092d7.mp4?token=mJJa8bIP63VZ6R3j9wdt1z6vnNwJxHDz6dLY2rUDU9kbJe2bs6p3vs_9dl_2Cf-J4BDO8GRxaFdUGWhnei4M36t581hLQXGf2TPXX22D1U9Q12kthhMXT71j0rYCGe4sIUblmmL8Y8dU4aYbzl8mRrD5jcN1TVl1YlS6LRbWDq6wQnVTJ8epYEEkGqX-I_lhHIQdLJmtqPw1YpSp6l0-YX8YD3qCwf7sO9UGcsoES1dz2DHGtqmyCYo2jH7C3LbR7Qps8O3H_7-mJhsIBvAHJReaEZYsHJqQBe9BWPcwRqTHBWKdW4RvN2lGu2BbcZOEYFwayaapo2HTwc4zGkF8AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لمس ممه‌های دوس دخترتون واقعا زندگی شمارو نجات میده! این یه شوخی جنسی نیست، از لحاظ علمی این موضوع کاملا ثابت شده و اینکار مثل معجزه عمل می‌کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72101" target="_blank">📅 09:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72100">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575ce7dd12.mp4?token=k-afO3qZjkqITv35LmZhXMCRvWGsCd7mS1vtr9nvac2RlAiEIqrTInhrBH-UxKZl-FBSSA7DA1DK8eQIdnPDK8nye0ToKjT4tnDWjYua8tkev7VXm3SO6jWKKUHNd2eM1FQPKjud7KiGiR9n9nLAVILeIZg6PdcxJqSiObLW7hA9O592sIaCPTnj8sqdfhHVrA97UL6Vdcyhyo0XjrKkis80iniSteD5yryRvPhPAa5ZUs181SMP6R17IUsquwveEfGlmCLsgsU4ya8KwlH2tKnuRT1jEvxfuUhV9KQhYpYNM0xm16tmyiaA1DVTi713Jy88kDWv354UjCzppRvWsg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575ce7dd12.mp4?token=k-afO3qZjkqITv35LmZhXMCRvWGsCd7mS1vtr9nvac2RlAiEIqrTInhrBH-UxKZl-FBSSA7DA1DK8eQIdnPDK8nye0ToKjT4tnDWjYua8tkev7VXm3SO6jWKKUHNd2eM1FQPKjud7KiGiR9n9nLAVILeIZg6PdcxJqSiObLW7hA9O592sIaCPTnj8sqdfhHVrA97UL6Vdcyhyo0XjrKkis80iniSteD5yryRvPhPAa5ZUs181SMP6R17IUsquwveEfGlmCLsgsU4ya8KwlH2tKnuRT1jEvxfuUhV9KQhYpYNM0xm16tmyiaA1DVTi713Jy88kDWv354UjCzppRvWsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مشهد یه خانم حامی حکومت تو اتوبوس، به یه دختر بخاطر حجاب حمله‌ور شد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72100" target="_blank">📅 09:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72099">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=WlCmUl4pjBnlJX2Tp4TotCghqP1FRb-dPvxCyS_7xle1v58OX4_Vc6nbdBckFeqFUTQFaoqzhVTu-41TU-8a283NPLYDGsfBztDIie4xYzk8Oc6V2v4a5m_6rlC35EWq1dZgWn8xAU68k2g0LU2jwWDNomkCQbEEIHyqFUZ3-2tlIz2gOwhqozbyryehqBCIm20vWeaOZeXStZTgVDkPx4hS_vJV22H7W02F47AZfb5hwYdkV0Ws2JlCAN8jwVQla0NbDJA7-mzMnvwxtrDcSzeiXX9YYX0-KE31NKfhugxhKz_mjddy_yHT96s6PDc7G5iO9G-EvqIu9fL97nHvYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=WlCmUl4pjBnlJX2Tp4TotCghqP1FRb-dPvxCyS_7xle1v58OX4_Vc6nbdBckFeqFUTQFaoqzhVTu-41TU-8a283NPLYDGsfBztDIie4xYzk8Oc6V2v4a5m_6rlC35EWq1dZgWn8xAU68k2g0LU2jwWDNomkCQbEEIHyqFUZ3-2tlIz2gOwhqozbyryehqBCIm20vWeaOZeXStZTgVDkPx4hS_vJV22H7W02F47AZfb5hwYdkV0Ws2JlCAN8jwVQla0NbDJA7-mzMnvwxtrDcSzeiXX9YYX0-KE31NKfhugxhKz_mjddy_yHT96s6PDc7G5iO9G-EvqIu9fL97nHvYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در استودیو فاکس‌نیوز با مارتا مک‌کالوم:
«وقتی من میلیون‌ها ایرانی را در ۳۱ استان کشور به آمدن به خیابان‌ها فراخواندم، آن‌ها به صورت میلیونی حاضر شدند و ضمن اعلام حمایت، شعار پایان دادن به این رژیم را سر دادند.
آن‌ها از تمامی اقشار جامعه ایران، اقوام، ادیان و گروه‌های اجتماعی گوناگون بودند؛
این جلوه‌ای عالی از اتحاد و تنوع است.
بنابراین، هر کس که ادعا می‌کند پس از ما ایران دچار جنگ داخلی خواهد شد [باید بداند که] عامل اصلی این تفرقه و اختلاف، همین رژیم است.
همه ایرانیان می‌دانند که این رژیم بذر دشمنی و خصومت را کاشته است.
اما ایرانیان دریافته‌اند که پس از دستیابی به آزادی، قادرند دوباره برخیزند؛ درست همان‌طور که قرن‌ها فارغ از تفاوت‌های قومی یا مذهبی، در صلح و آرامش در کنار یکدیگر زندگی کرده‌اند.
و انقلاب «شیر و خورشید» در راه است.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72099" target="_blank">📅 07:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72098">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=BofmLe1kvbMc_bvBoMrA8X7eZ_o_Umk53KoHj_U16QjNPX-dx52NI0Jq5YfO_oBwvR1Uqg3w9NwUQYzUYg7-7V4b4EyHzbz_sTz2UCZk3Nsl-bQLI99aqY5O2AUBpRAPzKYSqp5XVe6S6sdZC6NBUBUyjMOHLRIr-NSN04WFXTs_KyX4DeWgv95dLKbeNl9L8L-3dg-4CB_WQ_P6dfhnK_Da7r2wI2tC-5Ba5jdOWKTXMbJPYi72a9g9wOFqqAA4sWfgbleL5Navjtygc1lVKXdhuU11I9jKosZXeMCQBhhDPoGJpElZe7VwlqBAjvuAcIJQHPO1SPdpdUUq-t_Ukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=BofmLe1kvbMc_bvBoMrA8X7eZ_o_Umk53KoHj_U16QjNPX-dx52NI0Jq5YfO_oBwvR1Uqg3w9NwUQYzUYg7-7V4b4EyHzbz_sTz2UCZk3Nsl-bQLI99aqY5O2AUBpRAPzKYSqp5XVe6S6sdZC6NBUBUyjMOHLRIr-NSN04WFXTs_KyX4DeWgv95dLKbeNl9L8L-3dg-4CB_WQ_P6dfhnK_Da7r2wI2tC-5Ba5jdOWKTXMbJPYi72a9g9wOFqqAA4sWfgbleL5Navjtygc1lVKXdhuU11I9jKosZXeMCQBhhDPoGJpElZe7VwlqBAjvuAcIJQHPO1SPdpdUUq-t_Ukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در اجلاس سالانه «کنکوردیا» (Concordia)، پرسشی را مطرح کرد که دهه‌هاست در سیاست بین‌الملل نادیده گرفته شده است: چرا مردم ایران در کانون گفتگوها قرار ندارند؟
جمهوری اسلامی با مذاکرات بی‌پایان یا سیاست مماشات تغییر نخواهد کرد. ایرانیانی که به دست این رژیم قتل‌عام شدند، خواهان آزادی بودند، نه توافق هسته‌ای یا کنترل تنگه هرمز.
انتخاب روشن است: یا همچنان بر روی رژیمی سرمایه‌گذاری کنیم که عامل بی‌ثباتی و تروریسم است، و یا در کنار مردم ایران بایستیم؛ کسانی که شرکای طبیعی جهان آزاد برای ساختن آینده‌ای سرشار از صلح، امنیت و فرصت‌های اقتصادی بی‌سابقه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72098" target="_blank">📅 07:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72097">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrOY9lWAR46FQimYdFuFuN6sPH9hJSMuNdI8haVYDzgAfwHxhG3K9SukDpLf389mEZ8gJKO96_AxLXPKl4v-ehlNqbSu26qDxB0y4yq9dcNP_VdgTrX57juUL2RR5h002BuLYfCl4AUYXvWJmXgyLKcqV5Fwl0iMSN2bi_lAkB1v9C6AGvH5h-Y5_QqTRg7fiaKLsQ49RpAUZL-bUR-E6mIU6oE1BSmX9VUAz7UB-cpqk1GVPi83uL2QDZVOLUZPNCXDNFWoGn7YLOqB0kSz_xWfnT4H0sMYYJqeH5tZa-BBl1PkvmrL89uTH8TtYNTLKg8Dvnct40TNopw_GmUEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛یک منبع آمریکایی به العربیه:
آمریکا درخواست ایران برای رفع محاصره را نپذیرفت.
فرصت‌های دست‌یابی به توافق محدود است.
اختلافات و موانع بزرگی همچنان میان دو طرف وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72097" target="_blank">📅 07:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72096">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjYjFGnGC49Hw0a8CusGDqcAoPT8AJo1Ey3th4Ej7T0pBLGXygL0nN0u5dDjF7_FABud29XvCMbx-ya0TIzGaSemdImQ_dalvVqp-pzK63_XVWbbaad3WwaMfsLStYSpffcAxK7ovkP2pDjYmtggYt35ku0tnkel7jM8rhX0ThqhsyjUTmbVzG0g0_nEFvdRNMdL2VxBBt5PGYiONDdYSSDjcouqnh98qEid-5beqfs9gglQRQF4pIWg0L7_S71-_KEaRaBR5ycRqn-l4Ylgk-DGB2RpMiUx11rQrj3DPCHGHwmbX_6cK9-YmkaayAjyAgoymC7xBqwNANkmHnfalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیو ویتکاف:
امروز در حاشیه مجمع عمومی سازمان ملل، از طریق میانجی‌هایی که در طول روز میان دو طرف در رفت‌وآمد بودند، گفتگوهای مفصلی با هیئت ایرانی انجام دادیم.
آن‌ها یک دور از مذاکرات را با موفقیت به پایان رساندند؛ مذاکراتی که امیدواریم سازنده و نویدبخش باشد. میانجی‌ها به کار خود ادامه خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72096" target="_blank">📅 06:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72095">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=Tn8AsIflYbJyNin_DihPWP1CoGyxpynEVIKT46etUaQirs9yWc1fDarZjtCF_-4gU4sgJx9RbvQSFxJvr9Q4pOWQZiolg9rf4ReVPvaDLhJoMducmWKVJ0Ps0D05MeIDq_Yedrat-plAOWTs_XwOwAXlQc0zRMpNoWkEAelmd8WL9VyPWXzGjWVphxSqrQ4EYeaeYOQ9s65WnCFkjQJWDM-r36386M8bqd1SYvIkQkWWsX1BvrgwFWuDfUEg73WHkgChYMXwKxQRYf4tk2zYtiaMkLke4lSbIg9hRQ1DEg0xl64mTMvAeb9fgo5KQo3DV63o7Rwx5ZWUc9gy2g98SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=Tn8AsIflYbJyNin_DihPWP1CoGyxpynEVIKT46etUaQirs9yWc1fDarZjtCF_-4gU4sgJx9RbvQSFxJvr9Q4pOWQZiolg9rf4ReVPvaDLhJoMducmWKVJ0Ps0D05MeIDq_Yedrat-plAOWTs_XwOwAXlQc0zRMpNoWkEAelmd8WL9VyPWXzGjWVphxSqrQ4EYeaeYOQ9s65WnCFkjQJWDM-r36386M8bqd1SYvIkQkWWsX1BvrgwFWuDfUEg73WHkgChYMXwKxQRYf4tk2zYtiaMkLke4lSbIg9hRQ1DEg0xl64mTMvAeb9fgo5KQo3DV63o7Rwx5ZWUc9gy2g98SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود هم رسید نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72095" target="_blank">📅 06:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72094">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72094" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72093">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72092">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صدای دوانفجار جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72092" target="_blank">📅 01:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72091">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2-m1rfZwPXJfDZ5jBwP1N76mCWCdXfy2KLov8CNYLplyEydn7uzQ9RCbgMmDI4hyPGTjDI7eZeFR6gzOuZ2OJcvYhARFVn1Q-Oc4Nav_dTta3hndyjqNAmF9f_k-LfAwLxEeutA20QO8vrsb0F7e7DKrJBK_rBRDiMjciRoM9PcD2T8evpBHrX06oybCQJowfTtqv0fs6l848DFpNA7_VKaBAcP5cM4Kkft2wWfK1Aj8TDatC4FLBRpOq8ZeUoIY5QZvwiXqedpG8aMZSKz1wo5IgsVAUuF324_RRWG6MpGkIZ1Y0cNVn7sVwReHpkf5LD1hH-L-uwp_uVmnF6Hew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای‌نت:
انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.
هیئت نمایندگی اسرائیل همچنین خود را برای احتمال مزاحمت یا خروج هماهنگ‌شده در طول سخنرانی آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72091" target="_blank">📅 01:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72090">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ایرنا: صدای انفجار در حوالی جزیره قشم به گوش رسید
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72090" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72089">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=OM3wLehK32NL9cH7mxvTc3OfPMZsKUvdqy8vt_5GTVddor0cwzfcavEtKZIRzVrcIQGyKb_YPOZF64kcK_k6RUJsZUOPJK4GefFd24iUeIrkU9fKmONoVPscbyfHPUX6CTI8S4AtzkOw250CJYM5PJC_CdQChZx7tcWNKZbCmvEKphCo1ZoJTM3KD62MudV1hpU2UwUK29qc2vOcgy9ezqrgu6XsIdIgxQkDnDhBLUT5SgnfIX57hVyzqb8OYU9dYPkSkBDbaAc4G7QUQ_rNn87x408gV6aPlsBcuVOwu4jjR1j1alC09qDANuvvAhYWxgxGER3FfdnHEPhunw5Llw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=OM3wLehK32NL9cH7mxvTc3OfPMZsKUvdqy8vt_5GTVddor0cwzfcavEtKZIRzVrcIQGyKb_YPOZF64kcK_k6RUJsZUOPJK4GefFd24iUeIrkU9fKmONoVPscbyfHPUX6CTI8S4AtzkOw250CJYM5PJC_CdQChZx7tcWNKZbCmvEKphCo1ZoJTM3KD62MudV1hpU2UwUK29qc2vOcgy9ezqrgu6XsIdIgxQkDnDhBLUT5SgnfIX57hVyzqb8OYU9dYPkSkBDbaAc4G7QUQ_rNn87x408gV6aPlsBcuVOwu4jjR1j1alC09qDANuvvAhYWxgxGER3FfdnHEPhunw5Llw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت
ترامپ:
یا به توافق می‌رسیم، یا کار خیلی خیلی سریع تمام خواهد شد.
آن‌قدر سریع تمام می‌شود که سرتان گیج می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72089" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72088">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fAXLkpXxXHHtUOo-wyL88_Q2FEJ7DMHZTDsNgaibsXufjIsHrBtmND865ui3xaT0Xccg2DxoWXLv2SP-sdvGPr8d5p3QX_OnzaiBPQ9quep5J-VmAeU4G-2RN3IRca_lBB3zafZikXsThhbvtJzSifU9900AgPjJ0-zD6PfRhdw9OqFWvSWoJSzqSwdI08rl3PlAaKWmg38F2XMHX4dvZRgTrB1Lzb992AGcYfdNacP0AXGrZH3g8BDOIPj4FCC7VZlzrro7UiR444c08aESssJj-XLcywDKKl4h6XIlx2MI5LsSxbXNKYZH0INPnCeTfeRFDbwkIPhDkZZ_6vs3xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که تندروهای جمهوری اسلامی از پزشکیان تو نشست سازمان ملل دارن:
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72088" target="_blank">📅 01:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72087">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تابستون هم تموم شد و رسما وارد پاییز شدیم...
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72087" target="_blank">📅 00:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72086">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ساعت ۰۰:۴۷ بامداد چهارشنبه؛ یک انفجار در محدوده تنگه هرمز رُخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72086" target="_blank">📅 00:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72085">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qG1z0C4DLELw528v3rviRdvWpmPopzjMqKjeRZFdmjuwKtRUldrM4pUoHZKWvI1d-lhUpCCMckwI_4liw0BRCaWOyvZw0xKATvUWUAF1mkLM_mKXe22XvDAa4ZI79AV_8uSe-tTqSysIYtU-0RzrB3Gv2bK3J4VQg6iWxAkvQYCkcdmUtuHPsUvnKTiqvL2uPAFpE8BLhrzLsSCXTImoNba61gIvA_-HMzkX7EWJ3nGXoNR1w09jHJVPx4YqYe_QW5XnIq40UduySFom86V7O5vAjBRuUBf1YwsZZC5PD4puZN-mYg41cKOI2nIn9vechLTQ5S0j9ZzKOUf0iSu-cjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qG1z0C4DLELw528v3rviRdvWpmPopzjMqKjeRZFdmjuwKtRUldrM4pUoHZKWvI1d-lhUpCCMckwI_4liw0BRCaWOyvZw0xKATvUWUAF1mkLM_mKXe22XvDAa4ZI79AV_8uSe-tTqSysIYtU-0RzrB3Gv2bK3J4VQg6iWxAkvQYCkcdmUtuHPsUvnKTiqvL2uPAFpE8BLhrzLsSCXTImoNba61gIvA_-HMzkX7EWJ3nGXoNR1w09jHJVPx4YqYe_QW5XnIq40UduySFom86V7O5vAjBRuUBf1YwsZZC5PD4puZN-mYg41cKOI2nIn9vechLTQ5S0j9ZzKOUf0iSu-cjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
استیو و جرد امروز جلسه بسیار پرباری با میانجی‌های ایران داشتند. باید دید در ادامه چه پیش می‌آید.
به گمانم انگیزه و شتاب زیادی برای دستیابی آن‌ها به توافق وجود دارد؛ این همان چیزی است که از همه می‌شنویم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72085" target="_blank">📅 00:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72084">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=uBPkQABiYy8MOXqTUhYmaymdJDAa6tTXiDVR22pzcnmhcpgu2gDLvGmoy3_ne3IPomA9uFycSMqMftdkatb-Dkp8tyd0ZokivYaZ_1B7ShmLwKdoU_nXUD5C6yw-8LiWmbWstcfE4TEO0vJW-DMnOz9agFyeRer9k1MSLtVQn-mq2BFaAWTHM33hKpawzkFWQXqmDcOZiAJ73-W9uYWA4axXeUNKCCg5jD3F2jTmykQuK9HTD8_dBQNcOO8UPQFrhiQOX3EtU8SgJ3Zg46Nmzvf7zTzLC9tuz7uVD3QyXqFCiv1c5GhVEcwSdf7WUPE1RRuNeSOHKjTbD7jiujvfwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=uBPkQABiYy8MOXqTUhYmaymdJDAa6tTXiDVR22pzcnmhcpgu2gDLvGmoy3_ne3IPomA9uFycSMqMftdkatb-Dkp8tyd0ZokivYaZ_1B7ShmLwKdoU_nXUD5C6yw-8LiWmbWstcfE4TEO0vJW-DMnOz9agFyeRer9k1MSLtVQn-mq2BFaAWTHM33hKpawzkFWQXqmDcOZiAJ73-W9uYWA4axXeUNKCCg5jD3F2jTmykQuK9HTD8_dBQNcOO8UPQFrhiQOX3EtU8SgJ3Zg46Nmzvf7zTzLC9tuz7uVD3QyXqFCiv1c5GhVEcwSdf7WUPE1RRuNeSOHKjTbD7jiujvfwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امیدوارم پیش از آنکه خیلی دیر شود، هرچه سریع‌تر کار درست را انجام دهند.
می‌دانید، زمانی فرا خواهد رسید که دیگر خیلی دیر شده باشد و ما دیگر فرصتی برای اینکه اجازه دهیم آن‌ها به عنوان یک ملت باقی بمانند، نخواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72084" target="_blank">📅 00:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72083">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تسنیم:
دیدار استیو ویتکوف، نماینده آمریکا، با عباس عراقچی، وزیر امور خارجه ایران، در حاشیه مجمع عمومی سازمان ملل متحد، پس از درخواست‌های مکرر طرف آمریکایی برگزار شد.
ایران اعلام کرد که از این جلسه برای بیان شرایط خود برای بازگشایی تنگه هرمز، از جمله لغو فوری محاصره دریایی، آزادسازی دارایی‌های مسدود شده ایران و پایان جنگ در همه جبهه‌ها، استفاده کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72083" target="_blank">📅 00:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72082">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qv38W8J6N36sBSWLRO224qrgDJtykUzQnAm_KuGsR5VvQxLII41IRbHwxoVuqOfm1FlK1Cwvw2rPPEq6rNIE-hsPycR-Tk9IbagVs-qBchkCjJx1KGTmKq0VJ8OxoRcKStowc6wkfX18IRIrypHIU-6F8-HBmjIFqDY8PTunV6dOOLVTDbDmNt_f9ko4YFJJBAjA2T0fKiHYGDW_u929jSIly0t9sWHeZ4A5VMXo4IhKvOrIN6JgA0YvMTBYNZyJ11sQhYdSfyCpnCOFr4em9hlVanLQCeu_hip6l1uAkx6I23pNHibJU4CGk0shjyHua5STbSxmsDyMRN_9EpY2YTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qv38W8J6N36sBSWLRO224qrgDJtykUzQnAm_KuGsR5VvQxLII41IRbHwxoVuqOfm1FlK1Cwvw2rPPEq6rNIE-hsPycR-Tk9IbagVs-qBchkCjJx1KGTmKq0VJ8OxoRcKStowc6wkfX18IRIrypHIU-6F8-HBmjIFqDY8PTunV6dOOLVTDbDmNt_f9ko4YFJJBAjA2T0fKiHYGDW_u929jSIly0t9sWHeZ4A5VMXo4IhKvOrIN6JgA0YvMTBYNZyJ11sQhYdSfyCpnCOFr4em9hlVanLQCeu_hip6l1uAkx6I23pNHibJU4CGk0shjyHua5STbSxmsDyMRN_9EpY2YTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز یک نشست فوق‌العاده و مثبت بین کوشنر و ویتکاف با نمایندگان ایرانی داشتیم
واقعا در مسیر خوبی حرکت می‌کنیم اونا خیلی میخان توافق کنن اینو همه میگن
شتاب قابل توجهی برای مذاکره داشتیم
اقتصاد ایران رو منزوی کردیم اقتصاد اونارو نابود کردیم این خیلی خوبه
تنگه هرمز رو از مین ها پاکسازی کردیم و نفت جریان داره همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72082" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72081">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=Oj_P81WtOVAVy8BXdyhV4ZgQaSa-M1gt74O2suNebcfvo0JNTFUL23TXJ5vDstDiRHSHx-b0EhEmM3gXpk_J7RgHHg6wRk9mFVkmeddQLSmec-yKiLWUslAl-6EWil4U3AOAEhOvf31Qo9o0WWzdog4be5PwUcGus-Acq0fgCCiTYOgbHwrt-8mvrgk_AzSP-haVCjpTtu9TGvv0iZzGRUePY0FDzX7Aj0IALsoXW0DHlw2og92_6lntMvDSf5z49-4Zho0RVSIj7XmKuAy9isjue3reUedklL_CDn7gS67-FF1g_y4tMPnBr94XCGxcoGmxXJO-ZfrO2v7Sb4_QlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=Oj_P81WtOVAVy8BXdyhV4ZgQaSa-M1gt74O2suNebcfvo0JNTFUL23TXJ5vDstDiRHSHx-b0EhEmM3gXpk_J7RgHHg6wRk9mFVkmeddQLSmec-yKiLWUslAl-6EWil4U3AOAEhOvf31Qo9o0WWzdog4be5PwUcGus-Acq0fgCCiTYOgbHwrt-8mvrgk_AzSP-haVCjpTtu9TGvv0iZzGRUePY0FDzX7Aj0IALsoXW0DHlw2og92_6lntMvDSf5z49-4Zho0RVSIj7XmKuAy9isjue3reUedklL_CDn7gS67-FF1g_y4tMPnBr94XCGxcoGmxXJO-ZfrO2v7Sb4_QlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
آمریکا داره آب خلیج فارس رو می‌ریزه تو امارات تا تنگه هرمز خشک بشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72081" target="_blank">📅 23:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72080">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=JJGH6k5m6VvAOFZsy8y8PGpOAC9A0kEg7fI30h0wYfQOhI0aJwNwtBtkkGtF6LhjBB5L0JXqCbvA_neOaGDwI-qtc5nH2Ezc6AvxgVQKKTHKJq28Jci1natGgpegvDl_qj1t6eiraBmqCtmf3xsAxRcylX_v-PA1WEy6oe_kAeXX4ulWSzqlxgZiKkSwVh7qfwX99IkXHXeB2arhDL6gOTpystJD3SxDrSuI05teIwTvIDP4mmGPyTXOPyAhaRmYgSMC9FXFHxLkNrxbtm5ZnFrBXOomTZbZAGj54cqoiow8jP5A3Qzr9t9MV0fVjev5gadQdeh92SEVOqcXY70wAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=JJGH6k5m6VvAOFZsy8y8PGpOAC9A0kEg7fI30h0wYfQOhI0aJwNwtBtkkGtF6LhjBB5L0JXqCbvA_neOaGDwI-qtc5nH2Ezc6AvxgVQKKTHKJq28Jci1natGgpegvDl_qj1t6eiraBmqCtmf3xsAxRcylX_v-PA1WEy6oe_kAeXX4ulWSzqlxgZiKkSwVh7qfwX99IkXHXeB2arhDL6gOTpystJD3SxDrSuI05teIwTvIDP4mmGPyTXOPyAhaRmYgSMC9FXFHxLkNrxbtm5ZnFrBXOomTZbZAGj54cqoiow8jP5A3Qzr9t9MV0fVjev5gadQdeh92SEVOqcXY70wAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72080" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72079">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=qPCMs2A_-e6wCUF2FIestRGtNYsBTdBPEqNtGqWe49kGCa4l-DJxOQL_sNH0L3h3xOZXsd-E9uExvbPDrD962cRwN3xUjX-6X7xYpuR-IQgdXRPxlddEyxMK2NUuzdg0-GMXLdndMuXa09egFfiElRmEZQNl1KSVieNK2gWwJQgkwLYq3j5zk06fNRjWiaDLq08b6F15_dBkILfPkP5vg7ereNMmXjv3J6_eopmZBpYMAYpm70bhTQFe5JX94o7CtJpsWAkXn6LtedXSA_XlZdmC4zEBmEhWGLvYQG-6thClu2iW5BfjyCfuI7Aze-Qiq0kPCICqReTIgnqMH5R9SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=qPCMs2A_-e6wCUF2FIestRGtNYsBTdBPEqNtGqWe49kGCa4l-DJxOQL_sNH0L3h3xOZXsd-E9uExvbPDrD962cRwN3xUjX-6X7xYpuR-IQgdXRPxlddEyxMK2NUuzdg0-GMXLdndMuXa09egFfiElRmEZQNl1KSVieNK2gWwJQgkwLYq3j5zk06fNRjWiaDLq08b6F15_dBkILfPkP5vg7ereNMmXjv3J6_eopmZBpYMAYpm70bhTQFe5JX94o7CtJpsWAkXn6LtedXSA_XlZdmC4zEBmEhWGLvYQG-6thClu2iW5BfjyCfuI7Aze-Qiq0kPCICqReTIgnqMH5R9SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی فروتن، عمو فیتیله‌ای:
این روزا وقتی دختر، پسرا میخوان باهم دوست بشن، خیلی برای همدیگه لاف میزنن!
معیار انتخابم که شده پول، قیافه، خوش گذرونی و... به نظرتون گند نزدیم به عشق و عاشقی؟
یه زمانی آدما دنبال کسی بودن که نه تنها حرفشون، بلکه سکوتشون هم بفهمه. به خودت احترام بذار و با هرکسی وارد رابطه نشو.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72079" target="_blank">📅 22:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72078">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">امیر قطر در مورد غزه:  اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند: توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72078" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72077">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=R4s6vHV41CYNTBcUVl3LAD3-6ZSPzLhaEKar112SznCn0L1JpAL9FaGJfwsgS16IdEevJnxJCz9vEFxJ5NgfFVsho-JiScPrPHX79bOtGmtvL2uYOWE5eqQ2HxInknPaqrGasW5vzu585g1UsrClkuwlYImhbVFYAIbepWuxNZfLuE7VQNbo6z44ursKRdUMFkTNYDDWszesi92Ste4jTwCsSg-eSUNBJgFKpCb9_CK95LAPgTdbUSQTKaEYs9Y-U_5ubF5yvmVd8AZsbXbmxuo3ZH79iQaJNl89bQnNOZx3vyqyZLSCOGy3RSG-VkPn_MFcmCxO7hp-McuHMD4Pqoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=R4s6vHV41CYNTBcUVl3LAD3-6ZSPzLhaEKar112SznCn0L1JpAL9FaGJfwsgS16IdEevJnxJCz9vEFxJ5NgfFVsho-JiScPrPHX79bOtGmtvL2uYOWE5eqQ2HxInknPaqrGasW5vzu585g1UsrClkuwlYImhbVFYAIbepWuxNZfLuE7VQNbo6z44ursKRdUMFkTNYDDWszesi92Ste4jTwCsSg-eSUNBJgFKpCb9_CK95LAPgTdbUSQTKaEYs9Y-U_5ubF5yvmVd8AZsbXbmxuo3ZH79iQaJNl89bQnNOZx3vyqyZLSCOGy3RSG-VkPn_MFcmCxO7hp-McuHMD4Pqoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قطر در مورد غزه:
اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند:
توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72077" target="_blank">📅 21:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72076">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9803dc4ebc.mp4?token=AxthH_8FTfAPpADnm8e_7f2cYq163E7PTTabkkalkR6kNJEjcu7nv92ZHAGmZ2U5gyZBuQ4hT1AbCtN4i3LY5PvyFc8XMo5KdWdiVVwrsGUIdBAlVup7l4nr7wHg0Ftjk5__kaQP3bI1Der-KouxBJAhjKloIZABefnCpzG-8OaxsYf92hw6c-pw8V7upWseceUtE_1qtWkMQNnZxOPAY12cwl5rBM4NAQPMFy-t_CQ9Qb0xlnwXO5DGN26Av740yytq1GMoPLuEGs-vhK6J43FtEIB0zP_kbI4Z0MOXCl7UO8LUwJDFuC4qsroMq0mdMKTxv9kDuVRHuklSB8OX1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9803dc4ebc.mp4?token=AxthH_8FTfAPpADnm8e_7f2cYq163E7PTTabkkalkR6kNJEjcu7nv92ZHAGmZ2U5gyZBuQ4hT1AbCtN4i3LY5PvyFc8XMo5KdWdiVVwrsGUIdBAlVup7l4nr7wHg0Ftjk5__kaQP3bI1Der-KouxBJAhjKloIZABefnCpzG-8OaxsYf92hw6c-pw8V7upWseceUtE_1qtWkMQNnZxOPAY12cwl5rBM4NAQPMFy-t_CQ9Qb0xlnwXO5DGN26Av740yytq1GMoPLuEGs-vhK6J43FtEIB0zP_kbI4Z0MOXCl7UO8LUwJDFuC4qsroMq0mdMKTxv9kDuVRHuklSB8OX1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیداری بسیار خوب و سازنده داشتند. دیدار دیگری نیز برای آینده‌ای بسیار نزدیک برنامه‌ریزی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72076" target="_blank">📅 21:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72075">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c847d96020.mp4?token=Ho1fT0XZs-CUSMANeVrobK1qjJwKTDAI6CSYwML1reQM5s_dR65pEOEZ5vlPSTKW6TMH6gsjZ_MvcA9kFutU1p6iwzr72Wh2kR2E4atVHmDPx9UPYdBT4rtoC_jHyBhJ_-8Y9Q2XZsllbT1Axcf_choZ3NKBmOaW5pNshMLSddh7dcjrJsTyxnkIulft_Ok_9zEbHqDG42Pg1I8bhJcAwdyDhze8RL52ufB-Jry7b75Bni6I1kvAhTABkrrGIpLe3r8GIm_2xtBTQWBCObqCUpk3k1UprC2X4eqp81gA38PRl6QWn-6o0z1n7rKuOibdGwxz1xzuTS5SIYBdejzklg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c847d96020.mp4?token=Ho1fT0XZs-CUSMANeVrobK1qjJwKTDAI6CSYwML1reQM5s_dR65pEOEZ5vlPSTKW6TMH6gsjZ_MvcA9kFutU1p6iwzr72Wh2kR2E4atVHmDPx9UPYdBT4rtoC_jHyBhJ_-8Y9Q2XZsllbT1Axcf_choZ3NKBmOaW5pNshMLSddh7dcjrJsTyxnkIulft_Ok_9zEbHqDG42Pg1I8bhJcAwdyDhze8RL52ufB-Jry7b75Bni6I1kvAhTABkrrGIpLe3r8GIm_2xtBTQWBCObqCUpk3k1UprC2X4eqp81gA38PRl6QWn-6o0z1n7rKuOibdGwxz1xzuTS5SIYBdejzklg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز، حدود یک ساعت پیش، گفتگویی انجام شد. گفتگو بسیار خوب پیش رفت و یک ساعت پیش به پایان رسید.
این نشستی بود که سه ساعت به طول انجامید.
مسئله، عظمت — یا عظمتِ بالقوه — و یا نابودی است.
در یک حالت، صحبت از نابودی است؛ و گزینه دیگر، عظمتِ بالقوه است. [ایران] می‌تواند کشوری بزرگ باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72075" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72074">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e59383b3.mp4?token=Fnd0_m3G9_M_DvDUmQJoy33v5CeJ-O3-XTsEHGIsDgfNn7_H8dV8V8f7lZhhZtyNcnkW2CLJHU8IDf9J_1maP9jNF4VKkx9psMprErrrUXcBPKjVbV3jL4N35z_QkkhKDowsUa4f4NmWBHc_yUkJhHpAKO_xrI0uLtdonw0AzVMdGDN6eWefNDuNN36MxHLZISknk6y4NTwlG3fpfeYMV8A-g8rsUhNy8ZPGkTQgqemme8F8rderV_cy_IOXtCR8cK-s6_Hs2OueU2TAuLkykRB9_gezVySeIDRHzSRiT8CDLcrU70xK3WtnUIK6zSnrvA6Ns2_VGUeT36FzRpF8Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e59383b3.mp4?token=Fnd0_m3G9_M_DvDUmQJoy33v5CeJ-O3-XTsEHGIsDgfNn7_H8dV8V8f7lZhhZtyNcnkW2CLJHU8IDf9J_1maP9jNF4VKkx9psMprErrrUXcBPKjVbV3jL4N35z_QkkhKDowsUa4f4NmWBHc_yUkJhHpAKO_xrI0uLtdonw0AzVMdGDN6eWefNDuNN36MxHLZISknk6y4NTwlG3fpfeYMV8A-g8rsUhNy8ZPGkTQgqemme8F8rderV_cy_IOXtCR8cK-s6_Hs2OueU2TAuLkykRB9_gezVySeIDRHzSRiT8CDLcrU70xK3WtnUIK6zSnrvA6Ns2_VGUeT36FzRpF8Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گفته خانم دکتر؛
مردهایی که به‌طور مداوم رابطه جنسی دارن، طول عمرشون تا 50 درصد افزایش پیدا می‌کنه و همچنین خطر ابتلا به بیماری‌های قلبی هم تا 45 درصد کاهش پیدا می‌کنه.
-در زنان هم باعث میشه سرطان سینه و کیست تخمدان نگیرین.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72074" target="_blank">📅 21:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72073">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc4e3a7b84.mp4?token=oIvctWdt15wkh4BnKqcyPr7sLxgKR-4d_ZxPFshG58bvi8PdFA9OLsKVUbwcWgEL619o4Rx8DRyFcavIJYWY7GxKVpmwMFD3oxJYXsn-HTc4t1EpnrV7jrmyEMt4AgRZFVzeRwW2ekVUSSLWneR73E5Z1wKXMwPfVuaITMUoKg8wN5hZvDoyAggN6gS67L_gCRqmdMNF-TP5UJXAplKsscMVvvLWuT2RPVZAe_fdhkSE4lbIj5iXeoE99QXMPd6WXf8jcYZRk_oB51KVk6Yq0hIz7kxTimyPSUXG5kHEI1AFBSPgymyuznB3Kx1lDLZmWwPtS__GjdeeIPAo1qsk7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc4e3a7b84.mp4?token=oIvctWdt15wkh4BnKqcyPr7sLxgKR-4d_ZxPFshG58bvi8PdFA9OLsKVUbwcWgEL619o4Rx8DRyFcavIJYWY7GxKVpmwMFD3oxJYXsn-HTc4t1EpnrV7jrmyEMt4AgRZFVzeRwW2ekVUSSLWneR73E5Z1wKXMwPfVuaITMUoKg8wN5hZvDoyAggN6gS67L_gCRqmdMNF-TP5UJXAplKsscMVvvLWuT2RPVZAe_fdhkSE4lbIj5iXeoE99QXMPd6WXf8jcYZRk_oB51KVk6Yq0hIz7kxTimyPSUXG5kHEI1AFBSPgymyuznB3Kx1lDLZmWwPtS__GjdeeIPAo1qsk7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: بانوی اول ما کجاست؟ یک جایی همین اطراف است.
ملانیا:
👋
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72073" target="_blank">📅 20:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72072">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اکسیوس:
چند کشور عربی در تلاش‌اند زمینه برگزاری یک دیدار سطح‌بالا میان دونالد ترامپ و مقام‌های ایرانی را در حاشیه مجمع عمومی سازمان ملل در نیویورک فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72072" target="_blank">📅 20:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72067">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/77b06fbdcc.mp4?token=YVpnYIcZ5pzlxbnr5ySyllQA5PRIqEbAwo2JYAAak7dXtAUTBf0QD1HWSRAgUqVTMx9R6LMIp5WI1uELoT6bYXjQpbn3YIUvIMELXM4auqSjUA6qKyx1T7HRUeq9wg6abaqB8Ve2Ukis5kKdvDobXlh7x56mKasqFgP7uHlP3PaVFeno1WZ5POJ13RzGdQrXX_uel6IdQod9lOcHRqjKPN-bWpY540AKMaAis2fIpsqkZDyjf-F1lBwhvD1CxbIb4ImygIax807FIjEpn4Eb0u2Ge3VV0iTNdFjItJrCQtvgFUvPZMpnfh9fXhe-26QKeoFqBJNew9gaTypN7yLw_A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/77b06fbdcc.mp4?token=YVpnYIcZ5pzlxbnr5ySyllQA5PRIqEbAwo2JYAAak7dXtAUTBf0QD1HWSRAgUqVTMx9R6LMIp5WI1uELoT6bYXjQpbn3YIUvIMELXM4auqSjUA6qKyx1T7HRUeq9wg6abaqB8Ve2Ukis5kKdvDobXlh7x56mKasqFgP7uHlP3PaVFeno1WZ5POJ13RzGdQrXX_uel6IdQod9lOcHRqjKPN-bWpY540AKMaAis2fIpsqkZDyjf-F1lBwhvD1CxbIb4ImygIax807FIjEpn4Eb0u2Ge3VV0iTNdFjItJrCQtvgFUvPZMpnfh9fXhe-26QKeoFqBJNew9gaTypN7yLw_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی در پایانه لجستیکی شرکت «نووا پوشتا» (Nova Poshta) در حومه روستای اوساتوو (Usatovo) در منطقه اودسا اوکراین، پس از حمله موشکی.
علاوه بر این، ممکن است انبارهای متعلق به شرکت‌های دیگر در آن نزدیکی نیز دچار حریق شده باشند؛ چرا که مجموعه‌ای کامل از انبارها در آن منطقه قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72067" target="_blank">📅 20:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72066">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOoXe_qEd92S_tNBmX5geDT1C6ciYKFEh1355VD1yYomnZnuRgijmp76RWUpsqsizPL-lUqCRQtBo5GuWiFXJzLofH2De_bX0q-Gyf0OY13gIRk0TRl2CGEEc46wCz_h7N2Oaw_xgvhZakIONJLkBNTuh1GsPPDrXi0EtuImnvMHEgERt-NETuNCMYtTe6tagJmckbZp7id6r1iPk4YqgKQCZHjdyJnYunwRUWpFPMHz1XILEGWhGDWZNxPMI9_S0PZhhJEb2Kgrznn2yTctYK5bCqY-4iOAEJgwxIq7oo58LLUMDXZMvEA5jW7zWrmB743nHG7FcqnwTKa9cu5KiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهزاده رضا پهلوی وارد نیویورک شده است؛ ایشان قرار است در «اجلاس کونکوردیا» سخنرانی کرده و دیدارهای خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد داشته باشد.
با این حساب دونالد ترامپ، بنیامین نتانیاهو، مسعود پزشکیان و شاهزاده رضاپهلوی هم‌زمان توی نیویورک هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72066" target="_blank">📅 19:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72065">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فعالیت مدارس استان هرمزگان ۲ هفته مجازی شد؛
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از مجازی شدن فعالیت آموزشی تمامی مدارس استان در همه مقاطع تحصیلی از شنبه به مدت دو هفته، با هدف صیانت از سلامت دانش‌آموزان و حفظ کیفیت فرآیند آموزشی خبر داد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72065" target="_blank">📅 19:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72064">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">در ۲۳ سپتامبر، فعالیت تمام شرکت‌های هواپیمایی ایران در سراسر جهان متوقف خواهد شد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72064" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72063">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079b2c614f.mp4?token=p008o7at57JloqChOkhpvaXjeIvK2Z-Yc7Log0WCYx_sDYTz6ylMTohsruBXKx8qSgTWSMxb1EK3ZigiTz1kbksW0GOwzCB4wd-YK1vRGm_p4zWyyipGG62GNDzC6qbvKpUcDGrFWj6tUhuLoIYgMM47fOWxw_uvgAGJtJgAnx7Qb0H_bOjVLu7d1_IMM0sJn4WbDiiuQFCbcPMawJeSGbGJF97pWGWWLaf1mRfeMbCdrtwrSapXCHO478M2wfq0JgV-eEPAqldxW9n-lk875j76CtFm8jqy1VK-8LdqkuJYDPHTs2ZNF3I7R7jAOItAXU7gKDfg91GA3cljETPwo71HU1EQcfuIjU8qhnzTdN8IdT-4AwDs1Seh2c2JkoD-cM6n2rDTw7_1lA8dz9lJVK2Qf7YBJLHqrTpyiniqeDXO1XX2htn6qF5w4kjCnFSnw1KznTqlXwWkDHHaNNRSIBD_I3l1sNks0aiI6tGuWhzEP8EG3zTFgRY4U0BgGEQt6XLWnWTCIC7v-caSKc4YzbWiyNfkYR4C2kiB7v9gKQPVKUYd4FackbRK3ZBoNZU5r4viU4hdF2OXASIWgplYXnk-HLAIf0ZZlho8FWP2PwT3J8FuL4lUzjceZfBu8N9OGUO-YYvKkHcMh3etpZlz86wX4EX2IDJoVQ0kkqKM88A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079b2c614f.mp4?token=p008o7at57JloqChOkhpvaXjeIvK2Z-Yc7Log0WCYx_sDYTz6ylMTohsruBXKx8qSgTWSMxb1EK3ZigiTz1kbksW0GOwzCB4wd-YK1vRGm_p4zWyyipGG62GNDzC6qbvKpUcDGrFWj6tUhuLoIYgMM47fOWxw_uvgAGJtJgAnx7Qb0H_bOjVLu7d1_IMM0sJn4WbDiiuQFCbcPMawJeSGbGJF97pWGWWLaf1mRfeMbCdrtwrSapXCHO478M2wfq0JgV-eEPAqldxW9n-lk875j76CtFm8jqy1VK-8LdqkuJYDPHTs2ZNF3I7R7jAOItAXU7gKDfg91GA3cljETPwo71HU1EQcfuIjU8qhnzTdN8IdT-4AwDs1Seh2c2JkoD-cM6n2rDTw7_1lA8dz9lJVK2Qf7YBJLHqrTpyiniqeDXO1XX2htn6qF5w4kjCnFSnw1KznTqlXwWkDHHaNNRSIBD_I3l1sNks0aiI6tGuWhzEP8EG3zTFgRY4U0BgGEQt6XLWnWTCIC7v-caSKc4YzbWiyNfkYR4C2kiB7v9gKQPVKUYd4FackbRK3ZBoNZU5r4viU4hdF2OXASIWgplYXnk-HLAIf0ZZlho8FWP2PwT3J8FuL4lUzjceZfBu8N9OGUO-YYvKkHcMh3etpZlz86wX4EX2IDJoVQ0kkqKM88A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر ترامپ درباره هوش مصنوعی:
هر کس در حوزه هوش مصنوعی پیروز شود — باید این نکته را به خاطر داشته باشید — و حالا می‌گویم هر کس در حوزه «هوش برتر» (SI) پیروز شود، برنده نهایی است.
آن‌ها همان گروهی هستند که پیروز می‌شوند.
و ما در حال حاضر با اختلاف زیادی نسبت به چین و سایر کشورها پیشتاز هستیم. ما این وضعیت را حفظ خواهیم کرد؛ مسیری بسیار مستقیم و موضعی بسیار قدرتمند را در پیش خواهیم گرفت.
من نمی‌خواهم مانع رشد پدیده‌ای شوم که ابعاد آن از انقلاب صنعتی هم فراتر خواهد رفت.
بسیاری می‌گویند این تحول حتی از انقلاب صنعتی یا خودِ اینترنت هم بزرگ‌تر خواهد بود. و ما بسیار محتاط عمل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72063" target="_blank">📅 18:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72062">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36fc0e287a.mp4?token=AiFg5sjpZxS2b4lt0cCq5X7v38-q1sfgE490FKqq4YcDLKBoSk37pkgV5l2B5N2hiyfcQ89udYU5hWTEV6NaB4mP3pE4DuWHuzonRky5xmMCPl8aLYB9jnoD_0D_bmY2tUbAEdfgnLbjcXmrsuPuZYtLZbfonnC6V4BF0wcY6fvh0-FLr8Ae03oGIBX8fqhI8Yp7Sl18juh9nfmNeMc81uwgDLjSkuD5P1JnKYe5hnQL6TRo8A4LbmyxYQNk75FpTwNQGfPlVDwYOcf84rz4rMAHoVs4GNnJrUyE566SOKE2JlT-SaNU3v4e0Ga5cMefpgU_1tK5PPSihEhYM5H-IRwQf76hhe_CExrmQTm97JLB9oyWsQ60X37n2sRy8-3cEWs6loTRbDPIlzxduK8HtYmwogfzsRzNB65_oad83lQnb439OKrslNUv7cqA2cS1Ev7I6qWD-VSG5GC6USPi1bkI1si9HcInZdd90XBRVE7qBYrhgJNjb23UBNxRFwK5yJPaQe3Xv2Q8N5EstcWmoTZl5TB6pjGvHH6j_Yv4IMqYA_-eVw7eiDOtCSWDeTcLeV3vSYljchsdddKEBhKGRNbGdht64iibMrna-m7thVYoR0xPlpadWGfQe9S3nQqWUbHy03PofGjY94BNti6_ZjP2g75sQFJejpOVppt-Iyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36fc0e287a.mp4?token=AiFg5sjpZxS2b4lt0cCq5X7v38-q1sfgE490FKqq4YcDLKBoSk37pkgV5l2B5N2hiyfcQ89udYU5hWTEV6NaB4mP3pE4DuWHuzonRky5xmMCPl8aLYB9jnoD_0D_bmY2tUbAEdfgnLbjcXmrsuPuZYtLZbfonnC6V4BF0wcY6fvh0-FLr8Ae03oGIBX8fqhI8Yp7Sl18juh9nfmNeMc81uwgDLjSkuD5P1JnKYe5hnQL6TRo8A4LbmyxYQNk75FpTwNQGfPlVDwYOcf84rz4rMAHoVs4GNnJrUyE566SOKE2JlT-SaNU3v4e0Ga5cMefpgU_1tK5PPSihEhYM5H-IRwQf76hhe_CExrmQTm97JLB9oyWsQ60X37n2sRy8-3cEWs6loTRbDPIlzxduK8HtYmwogfzsRzNB65_oad83lQnb439OKrslNUv7cqA2cS1Ev7I6qWD-VSG5GC6USPi1bkI1si9HcInZdd90XBRVE7qBYrhgJNjb23UBNxRFwK5yJPaQe3Xv2Q8N5EstcWmoTZl5TB6pjGvHH6j_Yv4IMqYA_-eVw7eiDOtCSWDeTcLeV3vSYljchsdddKEBhKGRNbGdht64iibMrna-m7thVYoR0xPlpadWGfQe9S3nQqWUbHy03PofGjY94BNti6_ZjP2g75sQFJejpOVppt-Iyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر ترامپ درباره هوش مصنوعی:
از این پس، تمام اسناد ایالات متحده — و به امید خدا اسناد سراسر جهان — تغییر خواهند کرد تا به جای واژه «مصنوعی» (Artificial)، از اصطلاح بسیار دقیق‌ترِ «اَبَر» (Super) استفاده شود.
به عبارت دیگر، به دنیای جدید «اَبَر-هوش» (Superintelligence) یا همان SI خوش آمدید.
باید دید این ایده چه بازخوردی خواهد داشت؛ هرچه باشد، خیلی بهتر به نظر می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72062" target="_blank">📅 18:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72061">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6100a5cc1d.mp4?token=V9Y_vFXKQbO-8QRpZAWKZ_5EM0bDhIPinaCg-GahqByjEpBdU4eNoAhCuMte3uoNOT2msxSHa1c33eLTe5zvDsacfwdQxwA47bXN9joJWyXEjo-G7bJ6X-pg_aAqPuPMswV30tkEsCRMw4tsBlcMonx9Vr0c43N6XY1iQZdS_fs5AAzteIagIz_kdww2l9Nwpf87f7Mcqs1KSraYeNkYbUT25k0ee7GInXflSC0kgutKTGENIX9msHkmF0OtAhS575O2pA7NbGzVBXJ4oPt0UXPprFUV2KG8XEMeymNili0wupA-i3NeVyPHMWg4-zOUYmTPb3MGuMjx647g_jsbqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6100a5cc1d.mp4?token=V9Y_vFXKQbO-8QRpZAWKZ_5EM0bDhIPinaCg-GahqByjEpBdU4eNoAhCuMte3uoNOT2msxSHa1c33eLTe5zvDsacfwdQxwA47bXN9joJWyXEjo-G7bJ6X-pg_aAqPuPMswV30tkEsCRMw4tsBlcMonx9Vr0c43N6XY1iQZdS_fs5AAzteIagIz_kdww2l9Nwpf87f7Mcqs1KSraYeNkYbUT25k0ee7GInXflSC0kgutKTGENIX9msHkmF0OtAhS575O2pA7NbGzVBXJ4oPt0UXPprFUV2KG8XEMeymNili0wupA-i3NeVyPHMWg4-zOUYmTPb3MGuMjx647g_jsbqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ نام «هوش مصنوعی» (AI) را به «اَبَر‌هوش» (SI) تغییر می‌دهد.
او می‌گوید استفاده از واژه «مصنوعی» باعث می‌شود که هوش، «ساختگی» به نظر برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72061" target="_blank">📅 18:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72060">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156037c15c.mp4?token=Fn992FHJro8kN2pq66oLQsiRImNoc_KThTYCH7SrK19BZUFd_q0ZSuzxwje-vLEmrCFSrWU7J_LE35RlzWB3elwmxJkcylj_Jk84gdtM-9eFwTL9HhmLwEs7gHX1D1kFAyP06BDL6H2igONMLUKDL3q6Uz_xEV1pPGZ5dOEHb6KS0pjqkBQoA2MB4ViaQ732tDhruMJffzXnPNf7npxBiDZLjCuAToeLTbtYPmJe8FSRglhzfuqKLrpbJiIndCLQsVzmU9NaWO_KWVsdtSDuHlqmOG9YhDtDc1Ked6YaTLUlTmUWS89I3u0QU4UVq1d3idBh15cWQkjXo8IVHHjZ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156037c15c.mp4?token=Fn992FHJro8kN2pq66oLQsiRImNoc_KThTYCH7SrK19BZUFd_q0ZSuzxwje-vLEmrCFSrWU7J_LE35RlzWB3elwmxJkcylj_Jk84gdtM-9eFwTL9HhmLwEs7gHX1D1kFAyP06BDL6H2igONMLUKDL3q6Uz_xEV1pPGZ5dOEHb6KS0pjqkBQoA2MB4ViaQ732tDhruMJffzXnPNf7npxBiDZLjCuAToeLTbtYPmJe8FSRglhzfuqKLrpbJiIndCLQsVzmU9NaWO_KWVsdtSDuHlqmOG9YhDtDc1Ked6YaTLUlTmUWS89I3u0QU4UVq1d3idBh15cWQkjXo8IVHHjZ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
نیروی دریایی ایالات متحده اخیراً بیش از یک میلیارد بشکه نفت را از تنگه هرمز اسکورت و عبور داده است و حجم نفت در حال عبور، بیش از هر زمان دیگری از آغاز جنگ است.
ما هر روز و هر شب، به ترتیب ۲۲، ۲۵، ۳۰، ۳۲ و ۳۷ کشتی را [از این مسیر] عبور می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72060" target="_blank">📅 18:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72059">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=BrTDocTaUnaPb8plo6TZ8BlMN-ZbfaGxlEGjXet9NkwOsW8JAvQX-MLvK2I937SPQL0Qs84A1AIXNsAjIzxsY43QODP4LrgiCFD-8rhJfHH4vXTkBwKhjqfxdcOgiMnqlYZaS3xTDeBsYzSZw4IH0yXC1d-J1pq8J8vpNp70aYHPSmdJ_mh7-WjSqPpbYGyb7wc8HxbB6eee_HE-P4JirqWMPjtSPyl8GRKYvA5cJPvLHsy7fTDoqWTWh_h8s41HyGy6a4anXuehZmhWXzo11UtdwpMLIOQc5QsdvZEZbaHSthPkAsiwNoS8h-8nyES1Nsy1J-MXpixFY9_SCtdBpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=BrTDocTaUnaPb8plo6TZ8BlMN-ZbfaGxlEGjXet9NkwOsW8JAvQX-MLvK2I937SPQL0Qs84A1AIXNsAjIzxsY43QODP4LrgiCFD-8rhJfHH4vXTkBwKhjqfxdcOgiMnqlYZaS3xTDeBsYzSZw4IH0yXC1d-J1pq8J8vpNp70aYHPSmdJ_mh7-WjSqPpbYGyb7wc8HxbB6eee_HE-P4JirqWMPjtSPyl8GRKYvA5cJPvLHsy7fTDoqWTWh_h8s41HyGy6a4anXuehZmhWXzo11UtdwpMLIOQc5QsdvZEZbaHSthPkAsiwNoS8h-8nyES1Nsy1J-MXpixFY9_SCtdBpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایالات متحده و ایران قطعاً این کار را به سرانجام خواهند رساند. ما به هر طریقی که شده، این کار را انجام خواهیم داد. این کار انجام خواهد شد.
این کار به‌سرعت انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72059" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72058">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9a7cd318.mp4?token=GTWudSiXtr4CGj3hTmpuEhPob79CLtZ8GRvUmj80EugeJH2yI3FBSllwbqJAQe4S828_3hd50D_LXi7KL8oEqxiplEBTcN96_PyqLfS73WleEFjBu4n-ZWRjFTBbfbdgRghXk4jaknmeJBgNRLBjadOYteR6tRVvisBBcNFJMlB4cCbvpMRSeMpl4saAPzBVExhXp2UmMB3X3Bx8Wr6mNMOcZiV4k-lYS6l_3Atohw_o-lxMA6XqKNY-aZGVhJcOM5J9lnc4ngXsa2PyQlN9yRS4aw68VhL6ptEaLipcoLj6kKFEHdLc2uUAooXv0pxp7HLz6wjP_qZ4KED3lcY0yUUv5-gUcbFZhfMq220PL_Du2p4SRG2jzaYzjczUbRhKUVb3L2Bdvbd375RCP9xyVmr56YfWoXE9T_eiOPH2-NSRx2BO2T6bp_uQ1wppMmRU7_SweyislsB882x94GUYR4uiWtfu9LfLDMT6lBXYvWMA22kAFmvOy759-eyLirWg8g_fbY0T3BYklvfL9vq2kyIPsSqvpyspc4pHXv3kbzljc-3rKadyGIv_EvKFqr5xiHeTDkVcEZ7074-QJTUlxlwY5gbHHaHotiGWmHRuCeMmTq8Ilh2fHQkVhSt4cZa7qC_TXLBvYiw_7mV8bzbQBbH01BB0FEkVXv4cXJ04F74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9a7cd318.mp4?token=GTWudSiXtr4CGj3hTmpuEhPob79CLtZ8GRvUmj80EugeJH2yI3FBSllwbqJAQe4S828_3hd50D_LXi7KL8oEqxiplEBTcN96_PyqLfS73WleEFjBu4n-ZWRjFTBbfbdgRghXk4jaknmeJBgNRLBjadOYteR6tRVvisBBcNFJMlB4cCbvpMRSeMpl4saAPzBVExhXp2UmMB3X3Bx8Wr6mNMOcZiV4k-lYS6l_3Atohw_o-lxMA6XqKNY-aZGVhJcOM5J9lnc4ngXsa2PyQlN9yRS4aw68VhL6ptEaLipcoLj6kKFEHdLc2uUAooXv0pxp7HLz6wjP_qZ4KED3lcY0yUUv5-gUcbFZhfMq220PL_Du2p4SRG2jzaYzjczUbRhKUVb3L2Bdvbd375RCP9xyVmr56YfWoXE9T_eiOPH2-NSRx2BO2T6bp_uQ1wppMmRU7_SweyislsB882x94GUYR4uiWtfu9LfLDMT6lBXYvWMA22kAFmvOy759-eyLirWg8g_fbY0T3BYklvfL9vq2kyIPsSqvpyspc4pHXv3kbzljc-3rKadyGIv_EvKFqr5xiHeTDkVcEZ7074-QJTUlxlwY5gbHHaHotiGWmHRuCeMmTq8Ilh2fHQkVhSt4cZa7qC_TXLBvYiw_7mV8bzbQBbH01BB0FEkVXv4cXJ04F74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من از همه کشورها خواستم تا در اعمال
انزوای کامل اقتصادی ایران با ما همراه شوند؛ تا زمانی که آن‌ها حملات خود به کشتی‌های تجاری را متوقف کنند، از جاه‌طلبی‌های هسته‌ای خود دست بردارند و به حمایت از تروریسم پایان دهند.
این رژیم تروریستی نه به این دلیل که قدرتمند و با اعتمادبه‌نفس است، بلکه به این خاطر که ضعیف و درمانده است، چنین رفتار نامناسبی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72058" target="_blank">📅 18:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72057">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415b898f05.mp4?token=ArndEapgZe6dAaUhE8iGC4gwE6hNLcD9XmjjfdRb4FOPY-BHFdoujiq2GB9iKZMnpb_C64qFs4zzI0bzJaM3P7qqQ6VLzxnakiSax0J77Cs4KL4lU2JQ19zO5cNf78M91ald2uJM2oizrX2xTRSaw4feEyzqqmCwpF4sfKTzz31auGEtvOSCq9fHakB2MBFFERr_GI00xgYW1p7NSNOEtu3mpYEmNVEYtFsBVvDibqKs_oDxelbCS5edHXq4Qdf9VadqUKP_XP0_Mg2ZtWOWuTG_7oA0NNggdZWzSnfwCTx0yF3u2DNve8114K-Qzzqku91yyAbAMFWGKIfVVPt6zqtNuWD1dXkcyC8HBE7gmQUU_tUdx3W220cgTX9bu1aIMhTRrtBPJ3lrn9XPN5WiHBJVR1kRLSj8ll3HA8qWzPOSK9UDsFEdMXqqgQhdlHzKu9OGT07VNkGbbKS-0k2YvDcaz9qEGxT7IoCRoTLDshHfCTMZE-FCIhFq5QYvvgU2Qk_HNJdhLHHELXN3CxlMwHuiHqEdXm2ODXKSlDR76UJltVDd_dsIdZKhJQ_7vARZwAp6MPxidPtRJ7chm3jXANVpqFH1PHWNO9LczPcL_IH3ikaHJhoCAmQviWwqdgWHMvb5aBj0t80mBd2W3XDR5jbfjS4Pik87X2bYRqCb4x0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415b898f05.mp4?token=ArndEapgZe6dAaUhE8iGC4gwE6hNLcD9XmjjfdRb4FOPY-BHFdoujiq2GB9iKZMnpb_C64qFs4zzI0bzJaM3P7qqQ6VLzxnakiSax0J77Cs4KL4lU2JQ19zO5cNf78M91ald2uJM2oizrX2xTRSaw4feEyzqqmCwpF4sfKTzz31auGEtvOSCq9fHakB2MBFFERr_GI00xgYW1p7NSNOEtu3mpYEmNVEYtFsBVvDibqKs_oDxelbCS5edHXq4Qdf9VadqUKP_XP0_Mg2ZtWOWuTG_7oA0NNggdZWzSnfwCTx0yF3u2DNve8114K-Qzzqku91yyAbAMFWGKIfVVPt6zqtNuWD1dXkcyC8HBE7gmQUU_tUdx3W220cgTX9bu1aIMhTRrtBPJ3lrn9XPN5WiHBJVR1kRLSj8ll3HA8qWzPOSK9UDsFEdMXqqgQhdlHzKu9OGT07VNkGbbKS-0k2YvDcaz9qEGxT7IoCRoTLDshHfCTMZE-FCIhFq5QYvvgU2Qk_HNJdhLHHELXN3CxlMwHuiHqEdXm2ODXKSlDR76UJltVDd_dsIdZKhJQ_7vARZwAp6MPxidPtRJ7chm3jXANVpqFH1PHWNO9LczPcL_IH3ikaHJhoCAmQviWwqdgWHMvb5aBj0t80mBd2W3XDR5jbfjS4Pik87X2bYRqCb4x0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
بزدلان و خائنان بسیار دوست دارند بگویند که ذخایر مهمات ایالات متحده رو به اتمام است، اما این حرف صحت ندارد.
ما بیش از هر مقداری که حتی تصور استفاده از آن را داشته باشیم، مهمات در اختیار داریم و با سرعتی بی‌سابقه مشغول تولید آن‌ها هستیم. ما با سرعتی بیش از هر زمان دیگری در حال افزایش ذخایر خود هستیم؛ آن هم با تجهیزاتی که در بالاترین سطح کیفی قرار دارند.
علاوه بر این، در آینده‌ای بسیار نزدیک، کارخانه‌های عظیم تولید مهمات افتتاح خواهند شد. هم‌اکنون ۱۸ کارخانه از این دست توسط برترین شرکت‌های دفاعی جهان در حال ساخت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72057" target="_blank">📅 18:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72056">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=c5wgwuE2m5GlnJccD9Hsyp4EdrmzdHxCI-jVHz4GMFJcqHmpludIkqSH0T4rPHeTUyCu-vSx0NFnvTjqixXw5rlOQI8s9tAxbfekppcl2V7eMRGpz6f3hei9a3Jbp7q25DJhTiaJ46_fZMeS6iotqRyoVeold5wV3pxxLeA7A29GAG0YDcEG8j6Y2GKsEHRHX0r5z0Z-1iQAEYOE8lJoInpasemuHmniyfpqMRxdEfIdjhMddeEAXEO_E4daax3kOVdGdy3ZF_AWVKrqHbeqAKfyuqp91rMKFl15QQy86rY4yfopZgOvolq8kQWAu6XBwNpv9evFxk5vKNaLCzkNpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=c5wgwuE2m5GlnJccD9Hsyp4EdrmzdHxCI-jVHz4GMFJcqHmpludIkqSH0T4rPHeTUyCu-vSx0NFnvTjqixXw5rlOQI8s9tAxbfekppcl2V7eMRGpz6f3hei9a3Jbp7q25DJhTiaJ46_fZMeS6iotqRyoVeold5wV3pxxLeA7A29GAG0YDcEG8j6Y2GKsEHRHX0r5z0Z-1iQAEYOE8lJoInpasemuHmniyfpqMRxdEfIdjhMddeEAXEO_E4daax3kOVdGdy3ZF_AWVKrqHbeqAKfyuqp91rMKFl15QQy86rY4yfopZgOvolq8kQWAu6XBwNpv9evFxk5vKNaLCzkNpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من برای انتخابات در مورد ایران مطلقاً هیچ اعتباری قائل نبوده‌ام و نخواهم بود؛ این موضوع حتی به ذهنم هم خطور نمی‌کند.
تنها چیزی که اهمیت دارد این است که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72056" target="_blank">📅 18:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72055">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:باید تصمیم بزرگی بگیرم.
آیا توافقی با ایران صورت خواهد گرفت که به آن‌ها اجازه دهد کشورشان را بازسازی کنند و کشوری بسیار بزرگ‌تر از آنچه پیش‌تر بود بسازند؛ شاید حتی یکی از بزرگ‌ترین کشورهای خاورمیانه یا حتی جهان؟
یا اینکه جمهوری اسلامی را نابود کنم—آن هم به سرعت—و هرگز به آن‌ها فرصتی ندهم که دوباره دست به کشتار و ویرانی مردم و کشورها بزنند؟
آیا آن‌ها را به جهنم بفرستم، بدون هیچ شانس بقا و بدون هیچ امیدی به عظمت در نسل‌های آینده؟
اما معتقدم که بلافاصله پس از انتخابات به توافق خواهیم رسید، چرا که تن ندادن به آن برایشان منطقی نیست.
آن‌ها منتظرند ببینند عملکرد من در انتخابات میان‌دوره‌ای چگونه خواهد بود. چیزی که متوجه نیستند این است که من اصلاً نامزد آن انتخابات نیستم. من آن کار را قبلاً انجام داده و با اکثریتی قاطع پیروز شده‌ام.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72055" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72054">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5ddeee9dd.mp4?token=e5fBNASFFAGqC-jd8ESbJjraEIG1AH08ESgPI076UnxHYyI8bAjraY8K531TJcM_1oAHc55ZIYE_enQMigUp4GQY6nzwEIBAJeVVbqRYCutWDNDfsPKQqUaTiYc0nr41hDrEcpFyPAL0G_Q0uU9oXD1EhZw3EU_9e2u1tfbMmww736VShWN8SeRoUMkUkc8HVo2oJG6r6RKcHC423FIFXbBm0ev98r3296xE8_AkVGKPV1Fse8xRj7jeou6ioBmKpya3KICMQeUwxsjkCNrATibjwhjTcP9wG5doQMYWcu_SBOdvSZILIqDqqoe5rAgWGFGVtVucRiqgJcPxcVnjU7QyyhEwFHzLazNVigReE-hX_xyAIvKPIJRneDe5Z724zP4xwY5L80TLarvz2uN3KFc-WdQXnmJUdG3NRhALXrIvIebZYJpiyVE1QXhhSnKv8DtICrvtZXKdV0LkVF-Ksnt0JpAw7H0ifJZPfxKBIgpyZ5w1NJw7Y59jz12H8UkeUgo3asj541hQP9ryhFLUUSid6rwwVQSYaWUAAYq8kEfl7KZ_Xpb4NHcIWPp9ZbSv-exOGW1HEGZoP2NvxH5JSf09b2OiIwOENezNSoMeIbF_12WkMdyJOUjYLfGLcd76WkKDIas1gutWoLNO4YGCWx1-AkRELnJqXEaZCsXI0Cs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5ddeee9dd.mp4?token=e5fBNASFFAGqC-jd8ESbJjraEIG1AH08ESgPI076UnxHYyI8bAjraY8K531TJcM_1oAHc55ZIYE_enQMigUp4GQY6nzwEIBAJeVVbqRYCutWDNDfsPKQqUaTiYc0nr41hDrEcpFyPAL0G_Q0uU9oXD1EhZw3EU_9e2u1tfbMmww736VShWN8SeRoUMkUkc8HVo2oJG6r6RKcHC423FIFXbBm0ev98r3296xE8_AkVGKPV1Fse8xRj7jeou6ioBmKpya3KICMQeUwxsjkCNrATibjwhjTcP9wG5doQMYWcu_SBOdvSZILIqDqqoe5rAgWGFGVtVucRiqgJcPxcVnjU7QyyhEwFHzLazNVigReE-hX_xyAIvKPIJRneDe5Z724zP4xwY5L80TLarvz2uN3KFc-WdQXnmJUdG3NRhALXrIvIebZYJpiyVE1QXhhSnKv8DtICrvtZXKdV0LkVF-Ksnt0JpAw7H0ifJZPfxKBIgpyZ5w1NJw7Y59jz12H8UkeUgo3asj541hQP9ryhFLUUSid6rwwVQSYaWUAAYq8kEfl7KZ_Xpb4NHcIWPp9ZbSv-exOGW1HEGZoP2NvxH5JSf09b2OiIwOENezNSoMeIbF_12WkMdyJOUjYLfGLcd76WkKDIas1gutWoLNO4YGCWx1-AkRELnJqXEaZCsXI0Cs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
ما در آمریکا به‌تازگی بیست‌ و پنجمین سالگرد بدترین حمله تروریستی تاریخ، یعنی ۱۱ سپتامبر را پشت سر گذاشتیم؛ حمله‌ای که جان سه هزار نفر را گرفت. درست در همین نزدیکی‌ها.
دو هفته دیگر، سومین سالگرد حمله ۷ اکتبر در اسرائیل را گرامی خواهیم داشت؛ حمله‌ای که در آن تروریست‌های تحت حمایت مالی ایران، ۱۲۰۰ غیرنظامی کاملاً بی‌گناه — از جمله ده‌ها آمریکایی و بسیاری از نوزادان؛ نوزادانی کوچک، ظریف و زیبا — را شکنجه کردند، مثله کردند و به قتل رساندند.
رهبر عالی ایران آن کشتار را جشن گرفت و آن را «خدمتی به بشریت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72054" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72053">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9289304.mp4?token=oUnV8F6chiAxM3wFFdJovVZlYzj91spitkWCltAzIP4PUO8ijyfFlKaANwwdsDThfhWyd66u3oNXDBTC94ZlITnbWOOLx1RuWqUJUTynpdEFIBi55AlkpDECRVMclx_aoCUHUa-U4AVETHqHntjYoy1XWkOtlbegT2qCoL5JNXZ8iyodb0b5619hMr24Cw0jbTNeDAgrUrp_r11DRy6KZcSpAL2ny-zRwM-B857R_CiXQsOvueredw0L7uXxi0DV8-NhpD_DHD51O7nBAKxQZJQVDJC7IvIfkaD1qmnk6cxoe3lWzA6IumKdMIFit09JBKoEw-zYcwAbUVTGUNcLnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9289304.mp4?token=oUnV8F6chiAxM3wFFdJovVZlYzj91spitkWCltAzIP4PUO8ijyfFlKaANwwdsDThfhWyd66u3oNXDBTC94ZlITnbWOOLx1RuWqUJUTynpdEFIBi55AlkpDECRVMclx_aoCUHUa-U4AVETHqHntjYoy1XWkOtlbegT2qCoL5JNXZ8iyodb0b5619hMr24Cw0jbTNeDAgrUrp_r11DRy6KZcSpAL2ny-zRwM-B857R_CiXQsOvueredw0L7uXxi0DV8-NhpD_DHD51O7nBAKxQZJQVDJC7IvIfkaD1qmnk6cxoe3lWzA6IumKdMIFit09JBKoEw-zYcwAbUVTGUNcLnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
این رژیم امسال بیش از ۷۲ هزار تن از شهروندان خود را به خاک و خون کشید.
تصور کنید چنین رژیم پلیدی قدرت آن را داشته باشد که از پشتِ سپرِ هسته‌ای، دست به حملات تروریستی گسترده بزند.
این واقعیتی بود که باید با آن روبرو می‌شدیم؛ واقعیتی که بسیاری ترجیح دادند آن را نادیده بگیرند. همه آن‌ها آن را نادیده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72053" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72052">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=LmvL__c_yR1wWT4fkNFTU8CIzWPLOV772mb6YJZ35vJ2jiB6E3h8lVkZc-UjOagbRBU2k18gKFwd7MpVjO0ia45Nl1D3fme-Ja9NQua1cE4faj17zeDsFLoJn4vrOtk2WKQjkQN1ZHtdW1YG9tgT_pL_iBTvPYFpctkI0eDc2wurmmwNAN3fgaMGU3dqhUssQXkjRhCGqQnOVWWAIp8DpBfpnC0cscQdZeU-cfXLTKs-BOjnaz7GkR6mMOm_BOcxATM0Riup3nNgaOmgyaCz4-OHVTPVUJazF4uqKYn7B4Fv3yfcrV4o-gike3RZWD_7nXdRJ7Z4lV2-XX9oyr8zBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=LmvL__c_yR1wWT4fkNFTU8CIzWPLOV772mb6YJZ35vJ2jiB6E3h8lVkZc-UjOagbRBU2k18gKFwd7MpVjO0ia45Nl1D3fme-Ja9NQua1cE4faj17zeDsFLoJn4vrOtk2WKQjkQN1ZHtdW1YG9tgT_pL_iBTvPYFpctkI0eDc2wurmmwNAN3fgaMGU3dqhUssQXkjRhCGqQnOVWWAIp8DpBfpnC0cscQdZeU-cfXLTKs-BOjnaz7GkR6mMOm_BOcxATM0Riup3nNgaOmgyaCz4-OHVTPVUJazF4uqKYn7B4Fv3yfcrV4o-gike3RZWD_7nXdRJ7Z4lV2-XX9oyr8zBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها موشکی ساختند که قادر به هدف قرار دادن اروپا بود و به آن بسیار افتخار می‌کردند. امیدوارم اروپایی‌ها متوجه این موضوع باشند.
هدف ایران این بود که در پناهِ سپرِ موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند.
اگر آن‌ها موفق می‌شدند، آن رژیم شرور آزاد بود که تا ابد به گسترش وحشت و مرگ بپردازد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72052" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72051">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=IbbJ7xgztp4y8-xOG4F9RcP3aR2FxFddeEzPKthnFSTiOgtr8qA9dva7sIaOdSWaVhN-Jk6xVn1bRwS5kwvQDu4Bz_107uzXLuC_FwEZQiyUWzJdqJ130CNQEsOL43hwiYSTwyjUt8QpILIFTcARynY1847u1olhZbtEqsf0zTuyjVApHRpR_XM9yOV4fgRPw4VFYD2aY691Y3V2B95xfxtlaUChtNcs5udY3X9mrym6e8WlKGpoxGnxCNaIlNO8iDKQas-y1SChFbu9VZvQTN5B1LQN3KrpljDVuzrzVuQ54DijwVEMf1BoI_qXwk9e-2Oq7gp2OtBesN9yGnRDzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=IbbJ7xgztp4y8-xOG4F9RcP3aR2FxFddeEzPKthnFSTiOgtr8qA9dva7sIaOdSWaVhN-Jk6xVn1bRwS5kwvQDu4Bz_107uzXLuC_FwEZQiyUWzJdqJ130CNQEsOL43hwiYSTwyjUt8QpILIFTcARynY1847u1olhZbtEqsf0zTuyjVApHRpR_XM9yOV4fgRPw4VFYD2aY691Y3V2B95xfxtlaUChtNcs5udY3X9mrym6e8WlKGpoxGnxCNaIlNO8iDKQas-y1SChFbu9VZvQTN5B1LQN3KrpljDVuzrzVuQ54DijwVEMf1BoI_qXwk9e-2Oq7gp2OtBesN9yGnRDzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
سال گذشته، پس از آغاز به کار، مذاکراتی را با ایران آغاز کردم و به آن‌ها پیشنهاد دادم که در ازای پایان دادن به برنامه هسته‌ای و حمایتشان از تروریسم، از همکاری کامل اقتصادی برخوردار شوند.
اما آن‌ها نپذیرفتند. این اشتباه بزرگی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72051" target="_blank">📅 18:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72050">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=cxNd6ttsiipKuGlcsRIoFa8TEqVDEU5TmxAKAuVuYc3vK3doh8ZB8MvdUqx671U7QYE_2JiE7Ma8K2L6FxRCh2YvhDs5-yGY_5DTjeV4SeF_znQaQ2MERitvlyZ92Hd4kjiZhEmdcwghANh3hVncnfmwSelUMQckHQJJBL-m7L6SAW6OjS4akelURJj3v46sE0tBUVtL-Ffw5-CPZbcQlIT9DwHmKYwDkL1VcV-NAxahvkG9o9HWN2gC_5ekRdMI7pGbVNtzP4cd5LZAqINWzhUGs1QZfIMiqP-rqC_seRCQrAqYrsdLw7pkQ5d8qAjoiHRmYzvZZzqPV-gR9DE1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=cxNd6ttsiipKuGlcsRIoFa8TEqVDEU5TmxAKAuVuYc3vK3doh8ZB8MvdUqx671U7QYE_2JiE7Ma8K2L6FxRCh2YvhDs5-yGY_5DTjeV4SeF_znQaQ2MERitvlyZ92Hd4kjiZhEmdcwghANh3hVncnfmwSelUMQckHQJJBL-m7L6SAW6OjS4akelURJj3v46sE0tBUVtL-Ffw5-CPZbcQlIT9DwHmKYwDkL1VcV-NAxahvkG9o9HWN2gC_5ekRdMI7pGbVNtzP4cd5LZAqINWzhUGs1QZfIMiqP-rqC_seRCQrAqYrsdLw7pkQ5d8qAjoiHRmYzvZZzqPV-gR9DE1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند.
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام:
هرگز اجازه نخواهم داد  ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72050" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72049">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a4eccca8.mp4?token=n6dJE1Elrss1bESRY5RstWQFBny_WTDfUS2c2CR06d7KfhDOaTNOBEJi1jI68vvP_kZDG3n9WEuVZPLS9Ugg7i80ZfsKgD9peiK1LfsKBhxEcEbZ7DlOskHeQYllHnQyGzHu-SLgIfF4BA6JAPVZ6oiyRGav74l3QsvjwxrTkRaWmZlrNJbz5zMkBWdVb5XUz3vsrrlPz0QfSjtzsLMIcbBY2CSUoSArN1eU3l_ncqv_-E2zNiyaK0eAvvMzDAnQBjrNM0ASyx-myz6_PJymMuvADjt2lOADPesloxrnypaC8WmeweaSJ084BFVCFhifdFFnQyp2gNPJkrlXAOUTgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a4eccca8.mp4?token=n6dJE1Elrss1bESRY5RstWQFBny_WTDfUS2c2CR06d7KfhDOaTNOBEJi1jI68vvP_kZDG3n9WEuVZPLS9Ugg7i80ZfsKgD9peiK1LfsKBhxEcEbZ7DlOskHeQYllHnQyGzHu-SLgIfF4BA6JAPVZ6oiyRGav74l3QsvjwxrTkRaWmZlrNJbz5zMkBWdVb5XUz3vsrrlPz0QfSjtzsLMIcbBY2CSUoSArN1eU3l_ncqv_-E2zNiyaK0eAvvMzDAnQBjrNM0ASyx-myz6_PJymMuvADjt2lOADPesloxrnypaC8WmeweaSJ084BFVCFhifdFFnQyp2gNPJkrlXAOUTgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
من هیچ تمایلی ندارم که اجازه دهم خطرات، حتی یک روز دیگر هم رشد کنند. من به اینکه بگذاریم مشکلات وخیم‌تر شوند، اعتقادی ندارم؛ چرا که حل آن‌ها دشوارتر می‌شود.
بنابراین، در حالی که دیگران حرف می‌زدند، من عمل کردم.
در حالی که دیگران از صلح سخن می‌گفتند، من صلح را محقق ساختم.
در حالی که دیگران تهدیدها را نادیده می‌گرفتند، من با آن‌ها مقابله کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72049" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72048">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7fee3bd0.mp4?token=lpDJAUqckQ4U7oeH_hUF3Ki27KdENkgl0gkmwBd3NxZmTUbi9b7Kw9KSU66qfoOcsaV7yJZvJHz6jMM80ZBl9sH1FaYbC_mJxjhTAavCjahGSiIt5GIEtp8Sv1IJWQU8yGZLdpYfvQicuveCa2ph2OzqI1vqRxIl30p-JZu8qZyWwzJLM1M3QlWzLToBl9NzSLtzjjcv1wvnhHmtxxszTE9GQudjQanAk4-XYX2yRP42boEfDEOFUM28FgFsQjqtaHJ1sMiUvIt_61BO7Sf6ZYCRbeV-Gqoli3IhjmX9pUsE4sYAqN399_vqy54nrlqBEpILRlJzBt9Q7IxCSV7KlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7fee3bd0.mp4?token=lpDJAUqckQ4U7oeH_hUF3Ki27KdENkgl0gkmwBd3NxZmTUbi9b7Kw9KSU66qfoOcsaV7yJZvJHz6jMM80ZBl9sH1FaYbC_mJxjhTAavCjahGSiIt5GIEtp8Sv1IJWQU8yGZLdpYfvQicuveCa2ph2OzqI1vqRxIl30p-JZu8qZyWwzJLM1M3QlWzLToBl9NzSLtzjjcv1wvnhHmtxxszTE9GQudjQanAk4-XYX2yRP42boEfDEOFUM28FgFsQjqtaHJ1sMiUvIt_61BO7Sf6ZYCRbeV-Gqoli3IhjmX9pUsE4sYAqN399_vqy54nrlqBEpILRlJzBt9Q7IxCSV7KlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ:
با افتخار به شما اعلام می‌کنم که آمریکا بازگشته است و کشور ما امروز قوی‌تر از هر زمان دیگری است.
اقتصاد ما مایه غبطه جهانیان است. ارتش ما قدرتمندترین ارتش روی زمین است.
فناوری ما بی‌همتاست و ما تقریباً در همه زمینه‌ها پیشتاز هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72048" target="_blank">📅 18:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72047">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سخنرانی دونالد ترامپ درمجمع عمومی سازمان ملل متحد در نیویورک آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/72047" target="_blank">📅 18:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72046">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دیدم که مراد ویسی گفته احتمال اینکه پزشکیان و عراقچی رو تو آمریکا مثل مادورو دستگیر کنند غیرممکن نیست
آدم می‌مونه به این تحلیلگر چی بگه
😐
🧠
#hjAly‌</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72046" target="_blank">📅 17:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72045">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e4ea7a67.mp4?token=tAiaQABrn3XQ4SpK8Eplxrm_uVNi-wg-MlsSKzA2kyLi9CvGotaHjXgyXsgTtsNF0lYIDSHDfQ3svZV-3LGPiCsUvTfvEGk5OJ3fIQBE3xeViqFc7-8JlCXA-NNRIoD7Ts37ANRDceQ4r15q9fxZf5BrmDYJbRVfVA9zC5Wotkz6oMFVoQYcwnJcWB1IOW8ZhxZn4VjYMetBPL6JzcmVGP-ZiY8jzpYLbvFaMo_dhvpsJehsqJ1QrAws5gGc0QWIS89wBea-e6tEQkQWXXP7RjryTb7nOLtdyr2YsUh9U_E_lk2JFRjZsM63fbKbRisUrMmRR2IS7grnd2O4CwKJdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e4ea7a67.mp4?token=tAiaQABrn3XQ4SpK8Eplxrm_uVNi-wg-MlsSKzA2kyLi9CvGotaHjXgyXsgTtsNF0lYIDSHDfQ3svZV-3LGPiCsUvTfvEGk5OJ3fIQBE3xeViqFc7-8JlCXA-NNRIoD7Ts37ANRDceQ4r15q9fxZf5BrmDYJbRVfVA9zC5Wotkz6oMFVoQYcwnJcWB1IOW8ZhxZn4VjYMetBPL6JzcmVGP-ZiY8jzpYLbvFaMo_dhvpsJehsqJ1QrAws5gGc0QWIS89wBea-e6tEQkQWXXP7RjryTb7nOLtdyr2YsUh9U_E_lk2JFRjZsM63fbKbRisUrMmRR2IS7grnd2O4CwKJdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:پیامی که می‌خواهید به پوتین منتقل کنید، چیست؟
ترامپ: این جنگ را متوقف کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72045" target="_blank">📅 17:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72044">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=cu8Exw45fsHLf0lUy21ILeqyg-Les_jRc9u7i_vG5hKRYVjbRhxv0vHuZKtUdzVgqoexcCBvDA2iaWWF-IvEUacMtFzPCrtO_f-CUIDCESBwcIaPZYpgaaWhYzCEOFkNjFjGUtJzFXkRSMapVP1oAcnmRRwfqJTT07z32wGDVKeLJ4iMAvofklEPD8DMF0o14knpsmpk-DSUDb5aWkcye_XLyEJsRtBjteQBOmLE7Lm6zX8qcgYA7zy_VO73Se1438gc5Uca9L4NWDOo8AUAOPm9TCwGszTKiVsqhDXGZX4BBA8goWIphQsQurl_agpPoQsd1HTteh3O_jt7gXgJLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=cu8Exw45fsHLf0lUy21ILeqyg-Les_jRc9u7i_vG5hKRYVjbRhxv0vHuZKtUdzVgqoexcCBvDA2iaWWF-IvEUacMtFzPCrtO_f-CUIDCESBwcIaPZYpgaaWhYzCEOFkNjFjGUtJzFXkRSMapVP1oAcnmRRwfqJTT07z32wGDVKeLJ4iMAvofklEPD8DMF0o14knpsmpk-DSUDb5aWkcye_XLyEJsRtBjteQBOmLE7Lm6zX8qcgYA7zy_VO73Se1438gc5Uca9L4NWDOo8AUAOPm9TCwGszTKiVsqhDXGZX4BBA8goWIphQsQurl_agpPoQsd1HTteh3O_jt7gXgJLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ هنگام ورود به مجمع عمومی سازمان ملل خطاب به سی‌ان‌ان:
تعجب می‌کنم که سی‌ان‌ان اینجاست تا اخبار مربوط به مرا پوشش دهد. شما نباید اینجا باشید.
شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مرا پوشش دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72044" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72043">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72043" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72042">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5tNk2FouaivxXRCsEXELPvrqOIATNwEzI0wBkqjylSM9PNouUyFNbCA_mmLXNt73y2bxmpmQDTnLeed4bwAoD6Ah_RnIHCOf_3imLuVNKdxC4eRGn1aSlafWSq2f_5z9vjvc8k76dM7L7J2S6cnNrEhoYdLDsuyM4ipdMF0iiYGiq-7l3lsykk-J3kbBxdq83YJ5rLSdK29oYaul6m7FVszhcAU1yHHm_thV7IFBrG1tDOMBaCPqaWvO1cq-oXEh4ORVjuAwH8wKqbfYPeyhrn257HTRaJfLuuMd3puvoZGHKeJNXaQBsJnt43TI6cDSLdWfk-4tp23IHWCj5s_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72042" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72041">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05f244ea4.mp4?token=Hdq0k6o0EnhcdMTfMae0_KM9OdFLYHdv7fyo0SV3KeW98L04zJWlseqBDbSjuRTb72ojpB5lEsc1Mo6udjddXF4J1fSERRv7AHV2VO4yEcRwXDmcGs_UL6HFBjXsUU6lVkWX9LpLlAdgs_6mgZCnghmZc2LiZxxfwv-VoKX4RbZeiAMXqBtZ3brTzolNXPrjP-gaurc1CDW5cDTJo2I-2YehMJmsyS5wOWT6G5WOeN79BuW3Ge3DB39StghNG2EfPAiDyN3JgfTwLa5__6xcBqc_GGfhYSqk0VDquPOkV8ZAQDeVktMLRcSKLiP6-LdKUh0z9zcO_lz-pnxZ5nrwsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05f244ea4.mp4?token=Hdq0k6o0EnhcdMTfMae0_KM9OdFLYHdv7fyo0SV3KeW98L04zJWlseqBDbSjuRTb72ojpB5lEsc1Mo6udjddXF4J1fSERRv7AHV2VO4yEcRwXDmcGs_UL6HFBjXsUU6lVkWX9LpLlAdgs_6mgZCnghmZc2LiZxxfwv-VoKX4RbZeiAMXqBtZ3brTzolNXPrjP-gaurc1CDW5cDTJo2I-2YehMJmsyS5wOWT6G5WOeN79BuW3Ge3DB39StghNG2EfPAiDyN3JgfTwLa5__6xcBqc_GGfhYSqk0VDquPOkV8ZAQDeVktMLRcSKLiP6-LdKUh0z9zcO_lz-pnxZ5nrwsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره چندین دوس پسر داشته ده ها بار باهاشون رابطه ی جنسی داشته حالا اومده پیش متخصص زنان تا گواهی بگیره به نامزدش نشون بده پردش ارتجاعی بوده و سر اون پسر بیچاره کلاه بذاره.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72041" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72040">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/396f2961ce.mp4?token=YoRmsc-w5JY-x68o54RzBWonm3Nz7e76MPKwBkemYG88-i35kBhXl-ScosoDkAgtt4_cz0bzxGS45PZea39_ZPn6r-8mx1aY1Yxjig_56TqmCeQI1a5RIUG3GbMqdu0O9kCFMnP5oBPUboixwehHy-lN11jEAZgJaW-uSjc0s3mK3VseZPE5faHTt-kmn7znbWOTZfjWewI3NlQVoMPDay0fXpO0JZbFFV5ZQdeuIFnfmFjexFrVs4Z1C9KING_D95ZXJWJIgYT6JmZ8p5hz0x66K2pED-uiB8SA1kX9zWr0tiy0xWTeL76jv0yTmbWSUXH37ZmAXkayELo24z68XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/396f2961ce.mp4?token=YoRmsc-w5JY-x68o54RzBWonm3Nz7e76MPKwBkemYG88-i35kBhXl-ScosoDkAgtt4_cz0bzxGS45PZea39_ZPn6r-8mx1aY1Yxjig_56TqmCeQI1a5RIUG3GbMqdu0O9kCFMnP5oBPUboixwehHy-lN11jEAZgJaW-uSjc0s3mK3VseZPE5faHTt-kmn7znbWOTZfjWewI3NlQVoMPDay0fXpO0JZbFFV5ZQdeuIFnfmFjexFrVs4Z1C9KING_D95ZXJWJIgYT6JmZ8p5hz0x66K2pED-uiB8SA1kX9zWr0tiy0xWTeL76jv0yTmbWSUXH37ZmAXkayELo24z68XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان کیریاکو تحلیلگر و افسر سابق سیا؛
اسرائیل با پرداخت مبالغی در حدود ۱۰۰ دلار، هزاران شهروند افغان را در ایران برای فعالیت‌های جاسوسی به خدمت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72040" target="_blank">📅 17:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72039">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تو نمایشگاه خودروی تهران که تازگی تموم شد، تنها کاری که مردم نکردن بازدید از خودروها بوده ؛
جکِ ماشین رو برداشتن، با خودکار رو کاور ماشین کشیدن، با مشت زدن رو کاپوت G700، کارت استارت ولوو رو بردن، شید سقف ماشین رو خراب کردن، خار دستگیره در رو گاییدن، دوربین جلوی ماشین رو کندن، جکِ کاپوت رو کندن، با خودکار رو صندلی ماشین خط انداختن، دکمه صندلی رو شکوندن...
‌
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72039" target="_blank">📅 16:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72038">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1637ed0d1b.mp4?token=nZi8l6cR-EpAsCGikVuG4IrQCEkgUAZzb9SLUG3sYqiuxdbveH8EPqJYOZaVr6YByigy-ZCsXRlzWRtjQOQwtFHMf5aNrtOf0l6eyqCjWTR7Ms0G2nICHA3_N2g6FYAzZYK-TIs08lWziFJiwHL9NRF84OVQ2nTcrY-TcA4VTT66KPYHD1U5GTklG27w7WUNEEnFemYNibgewfr7rg89vc87EvQVnocU0EM6D0ZINdl8Bxfwj4n0hz_SJsxBlF9LOns79IQ1vkXgIPllYYgRko5DEitTeGgI4pdagzTYDprqF1CR6S2PKHekZiEGmLgXHF_PHzy7xlyTqqU-Hj-Dgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1637ed0d1b.mp4?token=nZi8l6cR-EpAsCGikVuG4IrQCEkgUAZzb9SLUG3sYqiuxdbveH8EPqJYOZaVr6YByigy-ZCsXRlzWRtjQOQwtFHMf5aNrtOf0l6eyqCjWTR7Ms0G2nICHA3_N2g6FYAzZYK-TIs08lWziFJiwHL9NRF84OVQ2nTcrY-TcA4VTT66KPYHD1U5GTklG27w7WUNEEnFemYNibgewfr7rg89vc87EvQVnocU0EM6D0ZINdl8Bxfwj4n0hz_SJsxBlF9LOns79IQ1vkXgIPllYYgRko5DEitTeGgI4pdagzTYDprqF1CR6S2PKHekZiEGmLgXHF_PHzy7xlyTqqU-Hj-Dgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
پیش از سخنرانی رئیس‌جمهور ایران در سازمان ملل، کانال‌های رسانه‌ای سپاه پاسداران ویدئویی مفهومی و ساخته‌شده با هوش مصنوعی منتشر کرده‌اند که تصویری از نخستین آزمایش واقعی (انفجاری) بمب هسته‌ای ایران را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72038" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72037">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d6eda575.mp4?token=vHlEnB5qaOx0S5wqfmOKtYKqR_xLjK2wg5-DxOzIEQIGOjtqhN17PnRyxHvwHoG0Ypd5czv7gvFVU1D2LjHX6-VAr4KfQg6RvU-0heqVnxwsn8B5yxNujfHiw4gtiF7-vq_3ffQMNsCeg5sWmkRcQY9OwiEDelaJN8a_M9RJmnU4eGWrrYnA97VFi9BNYPymzHBgHZHzMdHDSEKf9qa_s9pvezz9GmueHxkqhpEp0g1CnkW3DWGMDwgygGHPLU8xhUeSAYy1LkIXnsB746eSnDnwnGSTacY7UC6_ON2UUuUm6CD6gFxEt_xxkiaMfpcc0s7VpLCF27XzpeGZZrCIHUk1AHSlx9Z5N8skEt7EhZ__irP8-06AJNlfKLxT01KFGqMun0mfqvaY3rn1SuPkPgtk7mwjZrA5uEmENCoI8sH0Fgw5gXVD3Otm2TR78orcimlZaihfkdhLMrGMTB-f8kTP8JqtRe7QYRhB0dFIMOAaXlYX4zoUYg9MqcyvpooC55hU_X_V7ximDN0iQyBKPIYvhR7CxTP5veWFlClpe9owx9bgS682-OYENGFLNmgHc0KdJrZokS4tx1s5VOahiTxMMW0umVp22TDWh3Lr7dhFJ4TtPqHCNvTq9ZVdNvewMm50LmQQhbPbvrzmlh8ZTOXe_3I8vqPq-R5hWSj4_BY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d6eda575.mp4?token=vHlEnB5qaOx0S5wqfmOKtYKqR_xLjK2wg5-DxOzIEQIGOjtqhN17PnRyxHvwHoG0Ypd5czv7gvFVU1D2LjHX6-VAr4KfQg6RvU-0heqVnxwsn8B5yxNujfHiw4gtiF7-vq_3ffQMNsCeg5sWmkRcQY9OwiEDelaJN8a_M9RJmnU4eGWrrYnA97VFi9BNYPymzHBgHZHzMdHDSEKf9qa_s9pvezz9GmueHxkqhpEp0g1CnkW3DWGMDwgygGHPLU8xhUeSAYy1LkIXnsB746eSnDnwnGSTacY7UC6_ON2UUuUm6CD6gFxEt_xxkiaMfpcc0s7VpLCF27XzpeGZZrCIHUk1AHSlx9Z5N8skEt7EhZ__irP8-06AJNlfKLxT01KFGqMun0mfqvaY3rn1SuPkPgtk7mwjZrA5uEmENCoI8sH0Fgw5gXVD3Otm2TR78orcimlZaihfkdhLMrGMTB-f8kTP8JqtRe7QYRhB0dFIMOAaXlYX4zoUYg9MqcyvpooC55hU_X_V7ximDN0iQyBKPIYvhR7CxTP5veWFlClpe9owx9bgS682-OYENGFLNmgHc0KdJrZokS4tx1s5VOahiTxMMW0umVp22TDWh3Lr7dhFJ4TtPqHCNvTq9ZVdNvewMm50LmQQhbPbvrzmlh8ZTOXe_3I8vqPq-R5hWSj4_BY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، درباره ایران:
رئیس‌جمهور ترامپ برای دیدار با پزشکیان یا هر کس دیگری آمادگی دارد.
اما اینکه آیا نتیجه سازنده‌ای از آن حاصل خواهد شد یا خیر، دشوار می‌توان گفت؛ زیرا تصمیم‌گیرنده نهایی در ایران، «رهبر عالی» است و رهبر عالی، یک روحانی شیعه تندرو است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72037" target="_blank">📅 15:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72036">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ab0515ff.mp4?token=rtJZOyaxFxyAwYhdlFQVZZpEHhwVhWwUjbcSgnn2YtKyfTDiZmKIseFqhG741Ktj3nb78EEClA3kKABdvcx4bVWDBTIEVFh9BeqQnF05yW4D_leq_BqbRgbxRgyvRGQervVVVThZFBdd9uMlalz8dXTydWJ8vgVUMZSis-DWJcYDgEcQOlrAy1m-_8oE7GVE8Z9WDJtmaNWkPot_QEsawS9E6g2Kr3BARKJVduneHLktH-EGpRY2VULLT0NCK9mm8is6i_RI383my-Sp0HTh1bBLCCuTsVNiEcS2n4-KIs24pysYZT_T6vFxvdlLv1yKRCp-uAiNGD25NZ2xlo8qzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ab0515ff.mp4?token=rtJZOyaxFxyAwYhdlFQVZZpEHhwVhWwUjbcSgnn2YtKyfTDiZmKIseFqhG741Ktj3nb78EEClA3kKABdvcx4bVWDBTIEVFh9BeqQnF05yW4D_leq_BqbRgbxRgyvRGQervVVVThZFBdd9uMlalz8dXTydWJ8vgVUMZSis-DWJcYDgEcQOlrAy1m-_8oE7GVE8Z9WDJtmaNWkPot_QEsawS9E6g2Kr3BARKJVduneHLktH-EGpRY2VULLT0NCK9mm8is6i_RI383my-Sp0HTh1bBLCCuTsVNiEcS2n4-KIs24pysYZT_T6vFxvdlLv1yKRCp-uAiNGD25NZ2xlo8qzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
مسئله اصلی این است که ایران توسط روحانیونی دیوانه اداره می‌شود که دیدگاهی بسیار افراطی و آخرالزمانی نسبت به دین خود دارند.
این افراد هرگز نباید به سلاح هسته‌ای دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72036" target="_blank">📅 15:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72035">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeeb195e4e.mp4?token=bRNzC967tngGY-sOHZlzabFeIurkVRCK-JHjPA_9RTkzPwxxluChBIyM1JRG7pPO9NDeP6vs4GQzDGMfYNrZymx03O6-_51t-C_RTJ4lqIuZPVP5LR2lN6I83BrIarr-Bdh1JlYpIMF44OxSCnD_-jR2F3XE4q5w1p2M3Do3WPkJasD5toA1STCmv48Lba5fM_mKSOGGEPuNSLyjIwFsDnGqX3B63Fg0t60_sp0PVSuBA6lNbxZCeYKzLvF9aMlBR61DKtSCGXUfrINW9u0_BEcIhjkXKN4Ee2sGAXiw-Xv-FSAhJb31pFPSbT2_AqTY8VMsiGKS04jrzGT41h2K5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeeb195e4e.mp4?token=bRNzC967tngGY-sOHZlzabFeIurkVRCK-JHjPA_9RTkzPwxxluChBIyM1JRG7pPO9NDeP6vs4GQzDGMfYNrZymx03O6-_51t-C_RTJ4lqIuZPVP5LR2lN6I83BrIarr-Bdh1JlYpIMF44OxSCnD_-jR2F3XE4q5w1p2M3Do3WPkJasD5toA1STCmv48Lba5fM_mKSOGGEPuNSLyjIwFsDnGqX3B63Fg0t60_sp0PVSuBA6lNbxZCeYKzLvF9aMlBR61DKtSCGXUfrINW9u0_BEcIhjkXKN4Ee2sGAXiw-Xv-FSAhJb31pFPSbT2_AqTY8VMsiGKS04jrzGT41h2K5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
ترامپ برای دیدار با هر کسی در سازمان ملل آمادگی دارد.
ما نیز برای دیدار با پزشکیان آمادگی داریم.
گمان نمی‌کنم در حال حاضر برنامه‌ای برای آن تنظیم شده باشد، اما قطعاً از چنین دیداری استقبال می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72035" target="_blank">📅 14:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72034">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شرکت‌های هواپیمایی «ترکیش ایرلاینز»، «پگاسوس» و «اِی‌جت» (AJet) تمامی پروازهای خود به مقصد ایران را از تاریخ ۲۱ سپتامبر لغو کرده‌اند و امکان رزرو بلیت نیز حداقل تا مارس ۲۰۲۷ وجود ندارد.
تحریم‌های ایالات متحده موسوم به «عملیات طرد اقتصادی» (Operation Economic Outcast) دامنه‌ی گسترده‌ای دارند و حتی هواپیماهای ایرباسِ دارای قطعات ساخت آمریکا را نیز شامل می‌شوند؛ موضوعی که شرکت‌های هواپیمایی ترکیه را ناچار به توقف این مسیرهای پروازی کرده است.
شرکت هواپیمایی «ماهان» نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72034" target="_blank">📅 14:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72033">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH0peE2bHDf3j046saKK5c_TB2Amg4m6TG3etAUOPmgn8oCg8S8BYFiqZeTXKXescIQJegBynYz0UYrAiLchFtXOsYHh1WLDEv2pja62TYT60UByIpa1KDkdZ8JvDKBq9pKPJYOlwtqJR0vJOeUVAVNHPIChWfBLuLbPtWo3z3uUBmd4x0VtFK-AE81y2havj1SQd7Pz0drtPA-KwhP2NtPCCpGBdGou2xgxB8lfqD0I7cr3tMO1hmlg0xxPKamOeV4Fm7tcSfa8GLfKPL5g5apIv-hD7BqoStljybNDPRH_MOIKOtU4cQlTLn8LLZoaq8AmsJYnRtAEfVvrdrwQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری ژاپنی «کیودو» و به نقل از یک مقام ایرانی که نامش فاش نشده است، ایران پیشنهاد کرده است که در صورت برداشتن گام‌های اولیه از سوی ایالات متحده برای کاهش فشارهای نظامی، تنگه هرمز را ظرف هفت روز بازگشایی کند.
این پیشنهاد که گفته می‌شود از طریق واسطه‌ها به واشنگتن ارسال شده، خواستار ازسرگیری مذاکرات با هدف پایان دائمی خصومت‌هاست.
این مقام ایرانی اظهار داشت که دستیابی به توافق همچنان امکان‌پذیر است، اما احتمال دیدار میان ترامپ و پزشکیان در حاشیه مجمع عمومی سازمان ملل را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72033" target="_blank">📅 14:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72032">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7B4dMVlBcFd2zpAWQBtxUEWLz3IC2ZAQDloG6bdUr6fu2MmUqVqF1TOpt7jS3SdsqtMoE6KclM41WFNGlh-8rdUOi7_05_bAMiFzEtDasqhNOZ7n-Jg1AMStskk4O_hw4pbalPY7WwqQgSB6bY_ARQbTLkNyQ9-G1PJFtiZoIen0m0Wl0V_itr52vkDunVqATQsE1AEcqhgSfyYFt8TQWSFvlaYXot0n1kUzDgYjF9XWHz8aJBoPtsIxCCIECkez53_R-C__dNLxD4JK4UOip_t0of-TpmTP3uYxhw_JK5KvkcDd_RIR4Ghmke1JivPl0ClIPYaR9WePg4IPzc_pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان صبح امروز برای حضور در هشتادویکمین مجمع عمومی سازمان ملل متحد، تهران را به مقصد نیویورک ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72032" target="_blank">📅 12:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72031">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3534317cc.mp4?token=HJ83Fe78Rcp7sY44Ye_T4d3qOkhl689-72HVKRGNE3u9BD9cyasWeD1VrtrbY8TiqVy9LBwbUigFohuX7Z_UDHnyfBIfjAQd-P-VKCxz7rgSyduCVAQ-2rhd88DppGvSKhxqgzlustvf3Ki2sCDw0fTGGaS_2wn-7f4opH7JyuWW2v-QPVhIv5vysQsjv-nxw2j-pXcxPU7M78GSw55jhdCWLmQ2iIIRUuFUijedBMgU0wza4BvBs-RPddC6VIhruHYnyhgEr77Ih3MzBU3EgOYZQ8QQnU2ouNUlYnhu7ulgmm3vAG_uzw-9dE7vVFnqvePqgqDaWCLsvT2kL2HicQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3534317cc.mp4?token=HJ83Fe78Rcp7sY44Ye_T4d3qOkhl689-72HVKRGNE3u9BD9cyasWeD1VrtrbY8TiqVy9LBwbUigFohuX7Z_UDHnyfBIfjAQd-P-VKCxz7rgSyduCVAQ-2rhd88DppGvSKhxqgzlustvf3Ki2sCDw0fTGGaS_2wn-7f4opH7JyuWW2v-QPVhIv5vysQsjv-nxw2j-pXcxPU7M78GSw55jhdCWLmQ2iIIRUuFUijedBMgU0wza4BvBs-RPddC6VIhruHYnyhgEr77Ih3MzBU3EgOYZQ8QQnU2ouNUlYnhu7ulgmm3vAG_uzw-9dE7vVFnqvePqgqDaWCLsvT2kL2HicQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت عجیب سربازان روس که به بالای دکل ها رفتند تا با استفاده از سامانه های پدافندی دوش‌پرتاب(MANPADS)با پهباد های اوکراینی مقابله کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72031" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72030">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72030" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72030" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72029">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXremLhN-WPyjogp4BMw9F-TfTqJFouz2jQ8Q7Em9EE9aqvNs9R0q74LdXSe3mTDZhxwP-478caMiGDSBTi_I6QI3MsAgGDa0x7lFPegZXqgVyOiM0vLuEdZSExaxBemLQ7wg6Atn9eNecNkApZN3sOsI9YwtRZH_89iVM5MbwgZUU4qhoXaamf7yhrogV8HVqAFifLd0Ws3WO3skOWwU2jJPq7HiypIi0k-8yiJn_ojopC_TVG2cH63Fiv40en-w6HR3rgeXItwsvhqAc3swR9NYCYT3ZsJfH5B7tdk27kKJCyxHb4tpsIaAwd9sqgoD3ii6rosJxgvBsgHXEvOmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72029" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
