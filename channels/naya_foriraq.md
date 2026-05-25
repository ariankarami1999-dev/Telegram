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
<img src="https://cdn4.telesco.pe/file/nJFPETt4V-tlikbppDGwPyo3_wUZnKOsTg6Qwd5QFod1QcAuGI2EIAghdrDNxHwazAY7Cwv2tYFELhjJckSKBN-L-jf0Fto81wMkB7hj_mwhqPapZmclXaP5vGNIyR14AkL03qNFEAVMkV2pMppapd3KJBollLRakJSATCmo7xu-v1VAd8fKdoUXhiLGMYOPAvKElnKX1PPIBYTeqJi5q6sffcF8cRM4ASoasZZWd9ICcfF4ZPlzxNPR4d2vCBLu_eR55Myp5T7Ce8W6mYn5iJ1amIYSh-fRXgy3cp44H13e1I9Q61pL5CcbFpbHtGlXyccCarLS1WBKhZItgVIGCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 20:30:38</div>
<hr>

<div class="tg-post" id="msg-76065">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني:
خبر الإعلام السعودي حول تفاصيل تفاهم وإتفاق محتمل كاذب وغير صحيح. أن هذا الخبر في الإعلامي السعودي، مثل العديد من أخبارها حول تفاصيل المفاوضات، كاذب ويأتي في إطار العمليات النفسية الأمريكية.
في نص التفاهم الموجود حتى اليوم، لا توجد أي جملة تفيد الاستعداد لنقل المواد النووية، وبشكل أساسي لم تقدم إيران أي التزام بشأن الإجراءات النووية في هذا التفاهم.</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/naya_foriraq/76065" target="_blank">📅 20:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76064">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9c91c53a.mp4?token=Qy8LlDs_n4m1H-3UECucy_PTiS7yrTlxZ4RdRONEOH5y93BtEmqVLOa_J1EbZ8dJtxBgz1guuqwqtn8pWUPHeWozDKMd_cO7nknLbtnHPlGBThY-hmgVKZR82dtWRG2SVcplvP8vaOwGOUO9nYOl8HqX5m0R3QyZ0pdEM0cGht2o6kVlrtU6ctNl56TCILGJtqk3qr0z8JN4UUDBjrJr2WUKcom-4iYWDx7fgsDia9jLfvc_X0hQf2gQnYCWkJ3jhpqMBsN_cVXCC967ZdWX9mGMj1y6ZRZdIru4RLO-R820A4vodn5tk_E-vPc5YjRb9WpJA-PvAAZk90x_GGG5LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9c91c53a.mp4?token=Qy8LlDs_n4m1H-3UECucy_PTiS7yrTlxZ4RdRONEOH5y93BtEmqVLOa_J1EbZ8dJtxBgz1guuqwqtn8pWUPHeWozDKMd_cO7nknLbtnHPlGBThY-hmgVKZR82dtWRG2SVcplvP8vaOwGOUO9nYOl8HqX5m0R3QyZ0pdEM0cGht2o6kVlrtU6ctNl56TCILGJtqk3qr0z8JN4UUDBjrJr2WUKcom-4iYWDx7fgsDia9jLfvc_X0hQf2gQnYCWkJ3jhpqMBsN_cVXCC967ZdWX9mGMj1y6ZRZdIru4RLO-R820A4vodn5tk_E-vPc5YjRb9WpJA-PvAAZk90x_GGG5LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مسير يحلق في سماء قضاء سوران بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/naya_foriraq/76064" target="_blank">📅 19:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76063">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cff5fa941.mp4?token=JBTQUybF1GdMjSzAuV-bsDqPjL40ERzif3dF_-9RdasntRyKtOvsoPe3j7kOZqdRNopkasV9w7HCEh3D7TqZN3SHobl-BeaWimMWnEPl-3Qaw5nzgdAa9mz5sgrxn8ybGa9eFSkDDP9AlrKAMcX4aWAUjLcrOOcZ1nRQ5DU2Qp2pCy6Fpm4TEYhneP1SQL0WQatv75fHNu8zyHsN8EyirvZzDlobQO7GXdf69Xfh3Hi5GEIj-MK3QpeWgxNud2xy6FByJBW3p7ZQUHrX9F6LTa-xjo4PU_KQRzn4c2hczu1VM_H77TtYSlmXu0fe9mR2zJWj20nQg-W7vnbtUg2AY0PO0RxpnQLrWJzXHu0nzB8W-JhAP9LelqVDsj-0LW7RFeTVerwaa_zry7VqvxUfXA_Plc5UIrTaCTE7bR_gJHFRjRheZJgu0Tupws95eg-w_0hszNZK6PQXyDI1DDaHUKHcrnqzlAmvG-_9Q1wFmDOnWGPukdsEw6hmQFUXvITuS0FLe7dA3bA7SQDV0bC0E1bMWu9vcpaSlrYdMSraMw9f5b47JLUoqOTD_HXYD01iOkwh0oeThtpAgSglCo1JjDcQhDj1IbaIUL7er4JJPfEOuFrjqaB970KzcQVChE2L-QkzC8ad7QA-eGC37lYUUM-usznpgHYUPutizVBvM6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cff5fa941.mp4?token=JBTQUybF1GdMjSzAuV-bsDqPjL40ERzif3dF_-9RdasntRyKtOvsoPe3j7kOZqdRNopkasV9w7HCEh3D7TqZN3SHobl-BeaWimMWnEPl-3Qaw5nzgdAa9mz5sgrxn8ybGa9eFSkDDP9AlrKAMcX4aWAUjLcrOOcZ1nRQ5DU2Qp2pCy6Fpm4TEYhneP1SQL0WQatv75fHNu8zyHsN8EyirvZzDlobQO7GXdf69Xfh3Hi5GEIj-MK3QpeWgxNud2xy6FByJBW3p7ZQUHrX9F6LTa-xjo4PU_KQRzn4c2hczu1VM_H77TtYSlmXu0fe9mR2zJWj20nQg-W7vnbtUg2AY0PO0RxpnQLrWJzXHu0nzB8W-JhAP9LelqVDsj-0LW7RFeTVerwaa_zry7VqvxUfXA_Plc5UIrTaCTE7bR_gJHFRjRheZJgu0Tupws95eg-w_0hszNZK6PQXyDI1DDaHUKHcrnqzlAmvG-_9Q1wFmDOnWGPukdsEw6hmQFUXvITuS0FLe7dA3bA7SQDV0bC0E1bMWu9vcpaSlrYdMSraMw9f5b47JLUoqOTD_HXYD01iOkwh0oeThtpAgSglCo1JjDcQhDj1IbaIUL7er4JJPfEOuFrjqaB970KzcQVChE2L-QkzC8ad7QA-eGC37lYUUM-usznpgHYUPutizVBvM6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
19-05-2026
آلية عسكرية تابعة لجيش العدو الإسرائيلي في مستوطنة مسغاف عام شمال فلسطين المحتلة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/naya_foriraq/76063" target="_blank">📅 19:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76062">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19805be467.mp4?token=EsGfk4UGSxUpleMGpe45n2l05VjmqZ5bzp0aGv8o1zmzEcXFyNSkU4fP1MeHRPI4j7qtplXV5y8u7bCqv6XD0aFsLSwjcmDkq2venSNMMDM5xTwXFYbOJUhhMMDDOMjyn4DN5SHR8M1h_elt7GqajuVzfmnB22Y_Gaaj2l3ObAo3oPg0nxpvM7z9svrZ6kXOiNU3cQNXZ-sSFy4U9Zn-CorF-Fg1BMAg7mI42o_oXJeW5sm5TOOvayRD8IduSOHLqR7OmPszUoJTiWBZ8STBh8qzjZ_NJefh5qwEZ8F1GOKtUVAkavXDVn2EsqJL1qwFArB-3Zqle4yWSAxC3DjaGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19805be467.mp4?token=EsGfk4UGSxUpleMGpe45n2l05VjmqZ5bzp0aGv8o1zmzEcXFyNSkU4fP1MeHRPI4j7qtplXV5y8u7bCqv6XD0aFsLSwjcmDkq2venSNMMDM5xTwXFYbOJUhhMMDDOMjyn4DN5SHR8M1h_elt7GqajuVzfmnB22Y_Gaaj2l3ObAo3oPg0nxpvM7z9svrZ6kXOiNU3cQNXZ-sSFy4U9Zn-CorF-Fg1BMAg7mI42o_oXJeW5sm5TOOvayRD8IduSOHLqR7OmPszUoJTiWBZ8STBh8qzjZ_NJefh5qwEZ8F1GOKtUVAkavXDVn2EsqJL1qwFArB-3Zqle4yWSAxC3DjaGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إنفجارات عنيفة وتصاعد اعمدة الدخان في رأس الناقورة بالشمال الفلسطيني المحتل عقب هجوم مزدوج لحزب الله بالصواريخ والمسيرات الأنقضاضية.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/naya_foriraq/76062" target="_blank">📅 19:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76061">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfe153a8f.mp4?token=aknc4laC9rFdXbR1GaZCk9Ct81pfcbGAxkMFwoHu1rct5dryw8JtpzOCPkt0au07guxb5RfQN0DZ-EWt4bnSsPs2Hfzou5MKLHqBZBRivSkWin3jAa9TkQiX7apAVSJMUpPRZJaxCGGTUW07veRQBWM2KNVSgVwO9HaBhcyTT28yRu0uB6JihoHDiEYTISX25d_IY4lfgFhN9b8uURBcToecIlZQ_Z9SV0NtEwq-TrSwKhACMFaLGNxCSRgBpEv35p6o7aBuT50A9d7IN01gpxFWy8HdCRZlNYhnEpAHTjz6efySA0Y3Egh3PX_6UZ2qVlc234QGBlmnCQoca5sW_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfe153a8f.mp4?token=aknc4laC9rFdXbR1GaZCk9Ct81pfcbGAxkMFwoHu1rct5dryw8JtpzOCPkt0au07guxb5RfQN0DZ-EWt4bnSsPs2Hfzou5MKLHqBZBRivSkWin3jAa9TkQiX7apAVSJMUpPRZJaxCGGTUW07veRQBWM2KNVSgVwO9HaBhcyTT28yRu0uB6JihoHDiEYTISX25d_IY4lfgFhN9b8uURBcToecIlZQ_Z9SV0NtEwq-TrSwKhACMFaLGNxCSRgBpEv35p6o7aBuT50A9d7IN01gpxFWy8HdCRZlNYhnEpAHTjz6efySA0Y3Egh3PX_6UZ2qVlc234QGBlmnCQoca5sW_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
عقب فيضان نهر الفرات..
حكومة الجولاني تدعو لإخلاء فوري للمنازل والمحال القريبة من نهر الفرات في محافظتي دير الزور والرقة.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/naya_foriraq/76061" target="_blank">📅 19:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76060">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3c4d237e.mp4?token=pFCR53UBSLbr3dsJHhBtWHjGYQBDHAvLgLWly2qdlj_n9r5Nvyo8cEzs-OEdVsed-O5fy2Dw6NkPrJKXfrQyNIkN1mmfGBgBlEV7iAVoxgxr3JRdd_YQwzSy-1ZV7HYtNnVRS6mZD6dXUzWydhUc3HRON-64C8riyw3U7941W9rT31SCtnM6irCrDbENmwfcFps0EmDdTF1eqNVlgxI9tLDobvuUf2IfGBJDCUcN0QlKiBTVt2-7BZB2sOcWL8tFglmTlwpiXD5_FMmc7ybv4jc2Wix8DeF4bpklLHSlB6BRppHMgbaRl6zONZtr7lnHCXsLs8gZT6gEHXTaSxIw9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3c4d237e.mp4?token=pFCR53UBSLbr3dsJHhBtWHjGYQBDHAvLgLWly2qdlj_n9r5Nvyo8cEzs-OEdVsed-O5fy2Dw6NkPrJKXfrQyNIkN1mmfGBgBlEV7iAVoxgxr3JRdd_YQwzSy-1ZV7HYtNnVRS6mZD6dXUzWydhUc3HRON-64C8riyw3U7941W9rT31SCtnM6irCrDbENmwfcFps0EmDdTF1eqNVlgxI9tLDobvuUf2IfGBJDCUcN0QlKiBTVt2-7BZB2sOcWL8tFglmTlwpiXD5_FMmc7ybv4jc2Wix8DeF4bpklLHSlB6BRppHMgbaRl6zONZtr7lnHCXsLs8gZT6gEHXTaSxIw9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إنفجارات عنيفة وتصاعد اعمدة الدخان في رأس الناقورة بالشمال الفلسطيني المحتل عقب هجوم مزدوج لحزب الله بالصواريخ والمسيرات الأنقضاضية.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/naya_foriraq/76060" target="_blank">📅 19:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76059">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb0OZBg9JF6srU8dPo3MJx2bEnruj9Rp3vWUKo56T-mBNvbeKQjRbbJZB9-TzG4VgQYgAfD9gJO9lFdtfI9Ousj5R65YaUoE6lakn253wVW251X8-alaHxRSMj4dmqwd36AuDqOOppkWidNkbaBeYv9_-7Mv691YG5FelouXV4apmqxsO4vyCn9m9lyFhMwN45KOZeHFp07HQwr2vZ6zkDtLVrFeH94EfERAmv_bkeOq-E5Tj0_voeSOlPict8NbjZuYHymf565rTaQ7N2oEdIJ2e9eSU0xET_u8w6j-aBNvDhZqPeOcYF9yMcwxkd-juVGKSDATfPN30SkciJzFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
أمين المجلس الأعلى للأمن القومي الأيراني:
"لن يكون هناك استسلام أو تراجع"
لقد أظهر الميدان العسكري، والميدان الدبلوماسي، والشعب في الشوارع هذا الأمر بمقاومتهم الشديدة، وأجبروا العدو على التراجع. الآن أكثر من أي وقت مضى، يحتاج الوطن إلى الوحدة والتضامن، حتى يخيب أمل الأمريكيين والصهاينة في هذا الشأن. ميدان الوحدة والتضامن ميدانٌ آخر في النضال. إن تضافر الجهود لمنع أي أقوال أو أفعال تُزعزع الوحدة سيقود إيران العزيزة إلى النصر النهائي، بإذن الله.</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/naya_foriraq/76059" target="_blank">📅 19:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76058">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ السبت 23-05-2026 تجمّع لجنود جيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/naya_foriraq/76058" target="_blank">📅 18:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76057">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c703c1c6bd.mp4?token=q801P8fct-Q4O0okFakikBf9XeBCVf4RNNQs_rENCfUaGmxnWfR_7vhTboQ9TUcAoKVgO9X16iSWC9-H1cVORSsbm-bIvk6-CaXMZAM7Fy4VEBQPYeIBcoB4hS6CidqSDSFFN7jz6JWKsp1lIJrDaLBam-D08gUnA3dSgd8QTSrFvnWojC6hywnAzjHrbaIg4mpV5hmzxtCixvprakPRefAayTYVHD_bVt5XNjAbasrBr1aQijuqi4fLlFDZmp_Yg4Bsid1C_syudspbNd-gNMFrUO07ReZp4F3qZrvkblnqqdC4e8B7yImjKSW7nrxF3VBPjZok-J0xlgBIh2mFSQQCBOjkMfFejv3jHACwgl3xBxxVg-56cgGaubjof7Es0XmNIedcR6zev7GuTaAjX39coHXeOXS8uQJODgIxFfSHxTpo5XjVmDeFe4a7jf-XM2y2hO8g6Sl2pG2gzduhfpxHpaa0-_Ht4F0uUEgHpjUu2J7QfkshdticPOFqB5EATsVJ3v2oM33uAqdHMm4v_uNYVr7mZuMOQOlbxXA2iNwev4bjaH2yIdPrcttd9fsEqpz2TUN2XYRsBXK7bDTzyJqxxw3me_V76SJG8uSES8weMT2nnY6EuKJSO1dPZOqgENoemJYFAa6XcUQxpEYjijaDATJmIOuNAJi1XnoQaKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c703c1c6bd.mp4?token=q801P8fct-Q4O0okFakikBf9XeBCVf4RNNQs_rENCfUaGmxnWfR_7vhTboQ9TUcAoKVgO9X16iSWC9-H1cVORSsbm-bIvk6-CaXMZAM7Fy4VEBQPYeIBcoB4hS6CidqSDSFFN7jz6JWKsp1lIJrDaLBam-D08gUnA3dSgd8QTSrFvnWojC6hywnAzjHrbaIg4mpV5hmzxtCixvprakPRefAayTYVHD_bVt5XNjAbasrBr1aQijuqi4fLlFDZmp_Yg4Bsid1C_syudspbNd-gNMFrUO07ReZp4F3qZrvkblnqqdC4e8B7yImjKSW7nrxF3VBPjZok-J0xlgBIh2mFSQQCBOjkMfFejv3jHACwgl3xBxxVg-56cgGaubjof7Es0XmNIedcR6zev7GuTaAjX39coHXeOXS8uQJODgIxFfSHxTpo5XjVmDeFe4a7jf-XM2y2hO8g6Sl2pG2gzduhfpxHpaa0-_Ht4F0uUEgHpjUu2J7QfkshdticPOFqB5EATsVJ3v2oM33uAqdHMm4v_uNYVr7mZuMOQOlbxXA2iNwev4bjaH2yIdPrcttd9fsEqpz2TUN2XYRsBXK7bDTzyJqxxw3me_V76SJG8uSES8weMT2nnY6EuKJSO1dPZOqgENoemJYFAa6XcUQxpEYjijaDATJmIOuNAJi1XnoQaKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ السبت 23-05-2026 تجمّع لجنود جيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/naya_foriraq/76057" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76056">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
‏
🌟
أعلنت الرئيسة المكسيكية شينباوم موافقة حكومتها على بقاء المنتخب الإيراني في المكسيك خلال كأس العالم، بعد رفض أمريكي لاستضافته.</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/naya_foriraq/76056" target="_blank">📅 18:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76055">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7x-2jwY1yvmkHb2x22aBoytGRcGXRJJoUipCCN4IzS-I21DtIGR0Xfd2WAf7lpyo-LbZ8dbNK8JYMrBceoEPE8xEO9suBDEmcB5SfjD04WbSrvReJmu4XlC93_M4QbqsAkMgDlU_gdrgNgNEtgzUvDbc4jmk7ajhsT1BY0kNLeIZ3Wobs3m_aq1YTegLei5VOEbnQk7keLoNCKM2GqCwdpVQB9hGCGlxVSZGXSuTKWTkcdDcCqEE3wDo3j1_LHK94vtYYwBFzwC0skhBdPMJqcmPn-SNORqawDnKutto75pobX79mpbpT9xYl9sUP1BlIgvsqSNpVhJqPaSissz5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
حزب الله:
بعد قليل...
تركضلي تركضلي
😄</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/naya_foriraq/76055" target="_blank">📅 18:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76054">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🐦
سي ان ان:
تقول المملكة العربية السعودية إنها لن تطبع العلاقات مع إسرائيل إلا إذا كان هناك مسار لا رجعة فيه نحو إقامة دولة فلسطينية.</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/naya_foriraq/76054" target="_blank">📅 18:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76053">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🌟
حزب الله ينشر:
وَكُلّ عيد مُقَاومَة وَأَنتُم في نَصر.</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/naya_foriraq/76053" target="_blank">📅 17:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76052">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇹🇷
🌟
السفير التركي في العراق:
166 مواطناً تركياً من المنتسبين لتنظيم داعش كانوا محتجزين داخل العراق، سيتم نقلهم قريباً إلى تركيا، في إطار ترتيبات تتعلق بإعادة الرعايا الأتراك من السجون العراقية.</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/76052" target="_blank">📅 17:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76051">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🤙
🔥
الخارجية الروسية : على الجاليات الأجنبية مغادرة كييف فورا</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/naya_foriraq/76051" target="_blank">📅 17:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76050">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🤙
🔥
الخارجية الروسية :
على الجاليات الأجنبية مغادرة كييف فورا</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/naya_foriraq/76050" target="_blank">📅 17:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76049">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5TGvHDFv1b7pgKm_Ma6n_kLtldDYt3KM7Y1vreiYPOCKuNNePcczz_yWMSw3GlJ0LoD6jOaZxwwUNO0uvl8BtO_7rLSS5XfTyr9o494uU4vbhcDLuW76vVc_7BVQ2RQha8bdCAVSjdeNBl6VqLXeeC_PbF2cgq1wf3Xt_KJMq3-zvvYmCk5LUqvAELTqi7zjLD9cN_LixMlw7PKKHCn8HjYSlNW91NpU1U-9_IY7ZHz3kMi-Vc5tolAdxk8x0To0gy0APgXw9AnSU185WpFU0nFD6OkfNgExIUuMNmcN_7AoAqdgfq_q933Ekcf4iU4tHuCZTXE9E0t7BwfjXfksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الاعلام الاجنبي
:
بدأت إيران في إعادة بناء إنتاج صواريخها الباليستية خلال وقف إطلاق النار، بوتيرة أسرع مما توقعته المخابرات الإسرائيلية والأمريكية.
بينما شهد قائد القيادة المركزية للقوات الأمريكية، الأدميرال براد كوبر، أمام الكونغرس أن 90% من القاعدة الصناعية الدفاعية لإيران قد دُمّرت وستستغرق سنوات لإعادة بنائها، إلا أن المعلومات الاستخباراتية المحدثة تُظهر صورة أكثر تعقيدًا.
نجا حوالي ثلثي منصات إطلاق الصواريخ الإيرانية من الحرب سليمة، وتم نقلها خارج الأنفاق المغلقة.
تقوم إيران الآن بإنتاج صواريخ باليستية جديدة ومنصات إطلاق وأنظمة دفاع جوي في منشآت تحت أرضية مرتجلة باستخدام المكونات الباقية والمساعدة الروسية والأجزاء المهربة من الصين.
يقدر مسؤولو الدفاع الإسرائيليون أن إيران يمكنها إعادة بناء أسطول طائراتها بدون طيار في غضون أشهر وزيادة إنتاج الصواريخ في غضون عام، أو ربما أقل من ذلك.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/76049" target="_blank">📅 16:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76048">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIT29PUHB5D4hmNTGc40E6is0yGhMxyuVrKWY7dfI3qo2mBnck8a0KvRv5P-e81cKxyo8hrqBXxIopX4m_1EQPd9DXaHz7TcwiItwAxm8bGzxnN-U-SfP7xuubOcJaZ5K2iwOhMuyFnvQPNouOC4STQrBrwwlAHQfKzzoB68W-kOEG6LZLNnSIdHVyCNmDgcJ8uTDTNfd8baPgxseO8xW5sVKWMaSHgIt0EmbpQdeuKU6sxp7E65NpIyotBFOsU1g2qvbqxsP7J9Hy1kNNatCvq8MkpksUzNeVdY_0Bh7HRy8sI3m6BKu6znmIC6PQivge6rYmx95LJplQtTVCofXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
:
المفاوضات مع الجمهورية الإسلامية الإيرانية تسير على نحو جيد! لن يكون هناك اتفاق شامل للجميع، أو لا اتفاق على الإطلاق - عودة إلى جبهة القتال وإطلاق النار، ولكن هذه المرة أكبر وأقوى من أي وقت مضى - ولا أحد يريد ذلك! خلال محادثاتي يوم السبت مع الرئيس محمد بن سلمان آل سعود، رئيس المملكة العربية السعودية، ومحمد بن زايد آل نهيان، رئيس دولة الإمارات العربية المتحدة، والأمير تميم بن حمد بن خليفة آل ثاني، ورئيس الوزراء محمد بن عبد الرحمن بن جاسم بن جبر آل ثاني، والوزير علي الذوادي، من قطر، والمشير سيد عاصم منير أحمد شاه، من باكستان، والرئيس رجب طيب أردوغان، من تركيا، والرئيس عبد الفتاح السيسي، من مصر، والملك عبد الله الثاني، ملك الأردن، والملك حمد بن عيسى آل خليفة، ملك البحرين، صرحتُ بأنه بعد كل الجهود التي بذلتها الولايات المتحدة لمحاولة حل هذه المعضلة المعقدة، يجب أن يكون من الإلزامي أن توقع جميع هذه الدول، كحد أدنى، في وقت واحد، على اتفاقيات أبراهام.  الدول التي نوقشت هي السعودية، والإمارات العربية المتحدة (عضو حالي!)، وقطر، وباكستان، وتركيا، ومصر، والأردن، والبحرين (عضو حالي!). قد يكون لدى دولة أو اثنتين سببٌ لعدم الانضمام، وهذا مقبول، لكن ينبغي أن تكون معظم الدول مستعدة وراغبة وقادرة على جعل هذا الاتفاق مع إيران حدثًا تاريخيًا بارزًا. لقد أثبتت اتفاقيات أبراهام، بالنسبة للدول المعنية (الإمارات العربية المتحدة، والبحرين، والمغرب، والسودان، وكازاخستان)، أنها بمثابة طفرة مالية واقتصادية واجتماعية، حتى في ظل هذه الظروف من الصراع والحرب، حيث لم تُبدِ الدول الأعضاء الحالية أي نية للانسحاب، أو حتى التوقف مؤقتًا. والسبب في ذلك هو أن اتفاقيات أبراهام كانت عظيمة بالنسبة لها، وستكون أفضل للجميع، وستجلب القوة والسلام الحقيقيين إلى الشرق الأوسط لأول مرة منذ 5000 عام. ستكون وثيقة تحظى باحترام لا مثيل له في العالم.  سيكون مستوى أهميتها ومكانتها لا مثيل له! يجب أن يبدأ ذلك بالتوقيع الفوري من قبل المملكة العربية السعودية وقطر، وعلى جميع الدول الأخرى أن تحذو حذوهما. إن لم يفعلوا، فلا ينبغي لهم أن يكونوا جزءًا من هذه الاتفاقية، لأن ذلك يُظهر سوء نية. لقد تحدثتُ إلى العديد من القادة العظام المذكورين أعلاه، وأكدوا لي أنهم سيتشرفون، بمجرد توقيع وثيقتنا، بانضمام الجمهورية الإسلامية الإيرانية إلى اتفاقيات إبراهيم. يا له من أمر مميز! ستكون هذه أهم اتفاقية توقعها أي من هذه الدول العظيمة، التي لطالما كانت في صراعات. لن يتجاوزها شيء في الماضي أو في المستقبل. لذلك، أطلب بشكل إلزامي من جميع الدول التوقيع فورًا على اتفاقيات إبراهيم، وإذا وقّعت إيران اتفاقيتها معي، بصفتي رئيسًا للولايات المتحدة الأمريكية، فسيكون شرفًا لي أن تكون جزءًا من هذا التحالف العالمي الفريد. سيصبح الشرق الأوسط موحدًا وقويًا ومزدهرًا اقتصاديًا، ربما لا مثيل له في أي منطقة أخرى في العالم!  بموجب هذه الرسالة، أطلب من ممثليّ البدء في عملية توقيع هذه الدول على اتفاقيات أبراهام التاريخية، وإتمامها بنجاح. شكرًا لاهتمامكم بهذا الأمر!
دونالد ج. ترامب
رئيس الولايات المتحدة الأمريكية</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76048" target="_blank">📅 15:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76047">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🌟
‏ رويترز: عراقجي وقاليباف في قطر.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/76047" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76046">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
‏
رويترز
: عراقجي وقاليباف في قطر.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/76046" target="_blank">📅 15:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76045">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من مراحل استطلاع واستهداف المقاومة الإسلامية للمربض المُستَحدَث التابع لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة وباقي الأسلحة المختلفة.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76045" target="_blank">📅 15:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76044">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
🇮🇷
واشنطن بوست:
المرحلة الأولى تشمل إزالة الألغام ورفع الحصار الأمريكي والإفراج عن 12 مليار دولار، مذكرة التفاهم لا تتضمن اتفاقا نوويا بل مجرد تعهد بالتفاوض على الملف النووي لاحقا.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/76044" target="_blank">📅 14:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76043">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf43a827a.mp4?token=JcXG1boHfGdFgr20WpJRseJN6Psds4scVtwIbqfv3jb6XSKFH-7kzNutXXV-0eJHrvUdS9qOvQxUBGVGQV_fZbSq1QDxhVaZ_4qom_2XPiTEfC8hYAqtAFOMpln2iylrH_hrQZxDN293xEcJvDzBcdRu0Yu5EGBjx3f-8YiKp8YtRKG0wSgQF80X85AlBKaszcD_ChFeGv296qIj9u4UNXxItuYnu6R5YxtuVDh3-2qSmny1NMAFnWu6kCLGrQOcB5_qUxsOBdzIxh9AgURKFURjzdraJvsl72UQlNUQ2i2AYCPLho5n6fbPSlAdIcVhCSQmnik_o3HelMKwMaD8ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf43a827a.mp4?token=JcXG1boHfGdFgr20WpJRseJN6Psds4scVtwIbqfv3jb6XSKFH-7kzNutXXV-0eJHrvUdS9qOvQxUBGVGQV_fZbSq1QDxhVaZ_4qom_2XPiTEfC8hYAqtAFOMpln2iylrH_hrQZxDN293xEcJvDzBcdRu0Yu5EGBjx3f-8YiKp8YtRKG0wSgQF80X85AlBKaszcD_ChFeGv296qIj9u4UNXxItuYnu6R5YxtuVDh3-2qSmny1NMAFnWu6kCLGrQOcB5_qUxsOBdzIxh9AgURKFURjzdraJvsl72UQlNUQ2i2AYCPLho5n6fbPSlAdIcVhCSQmnik_o3HelMKwMaD8ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
تُظهر صور قبل وبعد لحيّ الشابورة وسط مدينة رفح، كيف مُحيت المنطقة بالكامل ، بفعل القصف العنيف والعمليات العسكرية التي شنّها العدو الصهيوني على المنطقة.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/76043" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76042">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mky8g2hjkn-OUpizMyZhCHbPc_QuqyPHupHxEpeCTweY5ARJ2vLSlHPdsOFWmHeKObyXJcYdtR2KGWB72zOttlD-CjeZnXXAmfToI-MhDB2Wa7DrczKf63UDuKtFwe1puAOjzMlygsUt5y7uJk41jys7JRVTa1NlTdCbOEYyi4Q5Y61pNSWx8B8f5w7tu2I0hpsih9QOEirLWD_TGSAJmuXtOkXHfiOzXE_otygah2o1NLGQpOolJePI7W4IEr_FYZrOHk0qsWIRZFvRGaELS8Y-uj5lE34TGMfh0cpTfv1Uci1uQBuNBbvZaYW7Y6-niNlwp71kaQRVUQSr1GzvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
أضحك على جميع الديمقراطيين، والجمهوريين المنشقين، والحمقى الذين لا يعرفون شيئًا عن الصفقة المحتملة التي أقوم بها مع إيران.
الصفقة مع إيران ستكون إما عظيمة ومفيدة، أو لن تكون هناك صفقة على الإطلاق.
ستكون عكس كارثة خطة العمل المشتركة التي تفاوضت عليها إدارة أوباما الفاشلة، والتي كانت طريقًا مباشرًا وصريحًا نحو حصول إيران على سلاح نووي.
لا، أنا لا أقوم بصفقات كهذه!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/76042" target="_blank">📅 13:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76041">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09156df5ce.mp4?token=BAKPX-0oQZ73zqoPy4MQ_quDQl7iP0scMxkhqIhp5OFhKOUgSq2HKJlKqV5Kax4nHChms5dJS940ATRgUDauSG9Nz1p0b9BgSW2FLSvwSdsewg5qRcpqh9y7oKaGeABN0YQCu49YgNncwM5kGq5kbNGtMPt6kI_lhWxTBt6F93wX2IpWjCbMCmYTXdlNALS_oUg9q4BXMIyPQVfG3_-n9ic3XQU07klZ16Se68SyyxdxO92GsR2eeou8N7mZg7IMPhwj0tkmydW4hgH0lkLy5mVSO6mHIanvFzEN6Wdy-f0oFePjJq29STrSa3qk7tDsLgPGmTNa2f8ofpJxEysUIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09156df5ce.mp4?token=BAKPX-0oQZ73zqoPy4MQ_quDQl7iP0scMxkhqIhp5OFhKOUgSq2HKJlKqV5Kax4nHChms5dJS940ATRgUDauSG9Nz1p0b9BgSW2FLSvwSdsewg5qRcpqh9y7oKaGeABN0YQCu49YgNncwM5kGq5kbNGtMPt6kI_lhWxTBt6F93wX2IpWjCbMCmYTXdlNALS_oUg9q4BXMIyPQVfG3_-n9ic3XQU07klZ16Se68SyyxdxO92GsR2eeou8N7mZg7IMPhwj0tkmydW4hgH0lkLy5mVSO6mHIanvFzEN6Wdy-f0oFePjJq29STrSa3qk7tDsLgPGmTNa2f8ofpJxEysUIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الكيان المحتل جراء إطلاق مسيرات وصواريخ حزب الله</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/76041" target="_blank">📅 13:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76040">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6BsZU_oMhP1dY9LbmyAFySbjlT1elh3NmFceE4UUju2Max_LFFvo-5__vyTgOX1Y080tboIkW7WwjyBQj3t9hg2ekUmLznW-893MH42pVAUP4jfLuDs5rsOLwXVlELsYXGf3PFnJ3U7CrS0BwXqvPHBqfDYUOBZ1kAlerdOGUGevcrx1VFvGReF9ASGOji2ZAa2Aluc0AUjm5YeTiC4TKXJToQNr12dD8B5I4wwAiT6RlPueGGM0OSJYwFp40srxSpXMBzI09gMiJxqmXKSR8priPu9A30DK4tU4oOAc8q3AZlt0SnOuXF5yqpmG8Ck0zsa1Ba7dOPEXoE1aD8nqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف طائرتي إنقاذ صهيونيتين جنوب لبنان بمسيرات حزب الله</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/76040" target="_blank">📅 13:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76039">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الصهيونية: رئيس الأركان الإسرائيلي طالب بمهاجمة بيروت ردا على مسيرات حزب الله</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/76039" target="_blank">📅 13:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76038">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🏴‍☠️
انفجارات كبيرة تهز إصبع الجليل شمال الكيان المحتل</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/76038" target="_blank">📅 13:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76037">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الصهيونية: رئيس الأركان الإسرائيلي طالب بمهاجمة بيروت ردا على مسيرات حزب الله</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76037" target="_blank">📅 12:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76036">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🏴‍☠️
مروحيات الإنقاذ تنقل جنود الاحتلال من جنوب لبنان جراء تعرضهم لاحداث أمنية إلى مستشفيات الكيان المحتل.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76036" target="_blank">📅 12:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76035">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad59608b1f.mp4?token=Sz5p45jU1pYwpoiqKCYGfVvvj8ftUu1wWVKxEtHaEvAsUuXRAoiImwC_qDFhWJ5YsWWWZRj24w2CLk23csGJlN4XosK6zb9IrzEP9dnNX8EQsDZ6BJydKKT8etuyzbILQklWI37-lXRVrwRp2ZFG482ShlsRIHfN55kui7VUuDnH7aHO0gX_eXbL7Tf3Fmb80uWz0hVekoiMjLcpbuBgnkip9ka49cNN274cDDIwkaQbXlPKg4-MaHhK5rL29r-wP4GPLY0rKGveQDjCSl8fljgyJwbpNsoT9GKq_UlJjr54_VwonpUGGodrYcDuPTjJArGg0UG6EHiJyW8XV6XmLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad59608b1f.mp4?token=Sz5p45jU1pYwpoiqKCYGfVvvj8ftUu1wWVKxEtHaEvAsUuXRAoiImwC_qDFhWJ5YsWWWZRj24w2CLk23csGJlN4XosK6zb9IrzEP9dnNX8EQsDZ6BJydKKT8etuyzbILQklWI37-lXRVrwRp2ZFG482ShlsRIHfN55kui7VUuDnH7aHO0gX_eXbL7Tf3Fmb80uWz0hVekoiMjLcpbuBgnkip9ka49cNN274cDDIwkaQbXlPKg4-MaHhK5rL29r-wP4GPLY0rKGveQDjCSl8fljgyJwbpNsoT9GKq_UlJjr54_VwonpUGGodrYcDuPTjJArGg0UG6EHiJyW8XV6XmLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
منفذ زرباطية الحدودي يستقبل الآلاف من الزائرين الإيرانيين لزيارة المراقد المقدسة في يوم عرفة وعيد الأضحى المبارك.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76035" target="_blank">📅 12:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76034">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴‍☠️
إعلام العدو
:تخيّل رئيس أقوى دولة في العالم، الرجل الذي تعهّد بإعادة أمريكا إلى عظمتها، يجلس يقضم أظافره منتظراً جواباً من يتيم علي خامنئي. لا يستطيع حتى تذكّر اسمه الأول: مجتبى؟ مجتبى؟ مجباتا؟ قل لي، هل هو حقيقي؟ هل أنت متأكد أننا لم نقتله؟ ومع ذلك، يجلس وينتظر أخبارًا من طهران. إنه كالرجل الذي وعد بالقفز من سطح السيرك، وعندما وصل إلى القمة لم يتحرك. صرخ من راهن عليه: "اقفز الآن!". فأجاب الرجل: "لا فائدة من القفز، ولكن كيف ننزل من هنا؟".</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76034" target="_blank">📅 12:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76033">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: مسيرة تابعة لنا هبطت اضطراريا في وسط إسرائيل إثر عطل فني</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76033" target="_blank">📅 11:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76032">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية: واشنطن تغير مواقفها بشكل مستمر وأحيانا في ساعات قليل
لا يمكن القول إن توقيع الاتفاق بات قريبا</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76032" target="_blank">📅 10:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76031">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
إعادة انتخاب محمد باقر قاليباف رئيسا للبرلمان الإيراني</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76031" target="_blank">📅 10:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76030">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cff109ec.mp4?token=NH9ozKbJMRV6L7B0P9VMlKUXbC4YqwkHQuEQUTPI7RH1V1-8EG5-VflQ9HNHTq0Atte3kGHMCg2jrg2qDI3DrKhfDdwc9ctI6ppErj1T_JKulYu0vW4Bc6Yj8WGWZcoWmrXnPXP3vnTRp3FcmZbUhC0-J8bJy2za-R_GAM_pBTPwsRQoMikRPTnIIxjvZs2EOym9HX68R32kxlJbitAlz98li0eNiQr9GpvisLo8a4z53RPqd_hjsnKiFvd4dxIm0_j3sfXT66-bc32K1IU38sWMMSZaiOnIO5vkK7FlYMyIR8qmFddbPCfOQrcPYd0f9ewPp5L4rVMpljzwgIC51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cff109ec.mp4?token=NH9ozKbJMRV6L7B0P9VMlKUXbC4YqwkHQuEQUTPI7RH1V1-8EG5-VflQ9HNHTq0Atte3kGHMCg2jrg2qDI3DrKhfDdwc9ctI6ppErj1T_JKulYu0vW4Bc6Yj8WGWZcoWmrXnPXP3vnTRp3FcmZbUhC0-J8bJy2za-R_GAM_pBTPwsRQoMikRPTnIIxjvZs2EOym9HX68R32kxlJbitAlz98li0eNiQr9GpvisLo8a4z53RPqd_hjsnKiFvd4dxIm0_j3sfXT66-bc32K1IU38sWMMSZaiOnIO5vkK7FlYMyIR8qmFddbPCfOQrcPYd0f9ewPp5L4rVMpljzwgIC51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
دبابة ميركافا صهيونية تشتعل بصواريخ حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76030" target="_blank">📅 10:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76029">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🏴‍☠️
دبابة ميركافا صهيونية تشتعل بصواريخ حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76029" target="_blank">📅 09:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76028">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEeTnEn9f7CWMZ0cnUiLG7e9E8kI7j2DoXgglNcya__QPRBdzZAezw0nZZJh9GdA8iaCZHF7YAHivERIl5hmsE4NRF8epFLxA5_bRm6PmBb6VUT-UMOLeHlJh4ZuiPxbtlz2q1-jSwmQodD9B2HDIxf92MPNeJV9tX2Mr6_fBLGVG7dVEqzsw4kPwgos3G3Fc_OgBMVu-gVfjLm2XmMHJ8r5w7pgx-6oiaycGR3rMe0YWKsUXRmxjlTEq7cHrTStTQmcB-c980l5iRxNpWjgoXb46Dk44oE9IFR8bzySaJN4pfF4qAsROclIFEpKANUGSFkQbzqC9h3yOaDHCsj6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أنباء اولية تتحدث عن شهيد وثلاث جرحى كحصيلة اولية من قوات الحشد الشعبي</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76028" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76027">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجار يهز محافظة صلاح الدين شمال غرب العراق</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/76027" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76026">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجار يهز محافظة صلاح الدين شمال غرب العراق</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/76026" target="_blank">📅 00:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76025">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجار يهز محافظة صلاح الدين شمال غرب العراق</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/76025" target="_blank">📅 00:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76024">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع:
لا تشعر إيران بأي ثقة تجاه الولايات المتحدة، ويراعي تبادل الرسائل عبر الوسيط الباكستاني باستمرار حالة التشاؤم تجاه الحكومة الأمريكية.  حتى الآن، لم يتم التوصل إلى تفاهم نهائي، ولا يزال التحدي قائماً في بعض البنود، ولكن حتى في حال التوصل إلى تفاهم مبدئي، فإن ذلك لا يعني أن إيران ستغير موقفها من أمريكا ولن تضمن وفاء هذه الحكومة بالتزاماتها. أن للأمريكيين سجلاً سيئاً للغاية في المفاوضات، مما يعزز حالة التشاؤم ويزيدها رسوخاً؛ ولذلك، حتى في حال التوصل إلى تفاهم، ستراقب إيران تحركات الولايات المتحدة خلال العملية بعد إعلان الاتفاق، وإذا أخلت الولايات المتحدة بتعهداتها في تلك المرحلة، فستحتفظ إيران بموقفها الرافض لها.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/76024" target="_blank">📅 00:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76023">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpBPJRznJmENhgdscasw-t3siKQkjKPpjQuoYwHOMKBvnymkgMYv5ngx6ZbIu3QN_QHK1LAk9gRB6hn_oM6SUtmuqIZol2h1BdaNND10PfLBDGbrbDfAWSlNEk1RPsdNh3dhxVOLsGA6JxflyxTovd97DCFfHYhWb3An6rC87GF6289jJBRlQ2u7j0uNHVtEDXxChilgixl17P39eltDk3pidHhzwg-3x5bBKWyjdW7GiIB2miInEBZTs0LQ6AvAQAzRS-Qm83sh5fVMpPWaVpQ3bvY76iJ5zy-oyJAbHGeMItd7X1GjD0WNyxtjVlKLEwXsdIV-ikcTJKT0p8UCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر على حسابه الشخصي.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/76023" target="_blank">📅 23:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76022">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7EWTGTIOla1FX10HVgS_gIeS7lnvBnoV0MGhBf8fVOa60EI_8lYlBFRWdMYXVEPeq-y3mF_SbdAtAt9_ckAJUVbczv6YgOxQSho99K_EpYokK8fqX2yEKs6-JSAxrSU3vjdKao4mHmwvZQ3Y8px55ej1H7B3lQFZ2UHjCWgCtMmH6Cp0gvYNskJZPZ_M4EedpvC5_27Mng8pwNCstrfdojA5Y2OZuYhfgKodh0ItBYchRib6eBitnYaEAiYDUqfY3fQDyXUOF73_0B_Toab0ZzDmYFtcEOZMMvziS5RvZqxFaEA930mIoFvcCcG00XuSX782x6P_C4t6opFncKOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني صعب جداً في جنوب لبنان.. مقتل جندي وإصابة أخرين من الجيش الإسرائيلي جراء استهدافهم بمحلقة انقضاضية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/76022" target="_blank">📅 23:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76021">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي: قضايا مثل مخزون إيران الصاروخي وتخصيب اليورانيوم ستناقش بمفاوضات لاحقة.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76021" target="_blank">📅 22:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76020">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من استهداف المقاومة الإسلامية عبر سلسلة عمليات لقوات جيش العدو الإسرائيلي في بلدة رشاف جنوبيّ لبنان بسربٍ من محلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76020" target="_blank">📅 22:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76019">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
🏴‍☠️
لبيك يانصرالله..
حزب الله يعلن عن إستهداف طائرة حربية إسرائيلية في سماء جنوب لبنان بصاروخ أرض جو.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76019" target="_blank">📅 22:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76018">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOnGkp40nxAWSqcTJh7-_giI7Aw0haeMbAjQ8_ldeGFKslRFkpodoIWE8DqNwiI2KkS8iYniUPNvMPfyl1Ddb6EhYGrUyazrKybjh1m8grLniAzFSBYGW5S-hCwR68HRCxwchAUWv1vvWv42Ie7ZQsqy3jEfT5Z_rfdacjij6cO2zOLVKGKvhnQaOJ7Xq87bZJesMgcce88Io65iWPAdDDFqi0VaQ2KGFc4HZWwC6I7ZTJDfZ3Z9-TlIv9uxRQupHhAjvB3IW2Ar5I4SlOjSv2vXtIYS2zx8TcFnZ9avyVGdMsSJAwTKgfnI3n0lRIFlt3s__kInlPF0VF1bh5Iefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
إذا أبرمت صفقة مع إيران، فستكون صفقة جيدة ومناسبة، وليست مثل تلك التي أبرمها أوباما، والتي أعطت إيران كميات ضخمة من النقد، ومسارًا واضحًا ومفتوحًا نحو السلاح النووي.
صفقتنا هي عكس ذلك تمامًا، لكن لم يرها أحد، أو يعرف ما هي. لم يتم التفاوض عليها بالكامل حتى الآن. لذا لا تستمع إلى الخاسرين، الذين ينتقدون شيئًا لا يعرفون شيئًا عنه.
على عكس من سبقني الذين كان يجب أن يحلوا هذه المشكلة منذ سنوات عديدة، أنا لا أبرم صفقات سيئة!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76018" target="_blank">📅 21:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76017">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a74538399.mp4?token=oZEGnLlLuPd8626eKyJuDAaZNP3g3jsupzWTXw-essjKDwkpGKP-cZZHcFloW6fK1WyplSodDZtaJLdqpD_QxdwHDz5EkQpDOUTwaA6XSEgo_oIZS1Gmg4fyG8ubbom20Oys76RxU7ER7-3HAxMOa0rLrNsoK8YZwLCO_uNaphdePcE9PvZJWpZtlBZIeebDaVChZ_v24PLPoUW05F1oz_RVswW9D3NtWPvv522RK7Gk97BSbYIRmIFaPCKXbhRwXONJjFrFcgcxOTZyigdrkg4FBrwT1QMg-3Jxb_gWCQj10xKF6-U0fT_CONKrQFxyLJ24TStT2Wqoi7jDLJJdBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a74538399.mp4?token=oZEGnLlLuPd8626eKyJuDAaZNP3g3jsupzWTXw-essjKDwkpGKP-cZZHcFloW6fK1WyplSodDZtaJLdqpD_QxdwHDz5EkQpDOUTwaA6XSEgo_oIZS1Gmg4fyG8ubbom20Oys76RxU7ER7-3HAxMOa0rLrNsoK8YZwLCO_uNaphdePcE9PvZJWpZtlBZIeebDaVChZ_v24PLPoUW05F1oz_RVswW9D3NtWPvv522RK7Gk97BSbYIRmIFaPCKXbhRwXONJjFrFcgcxOTZyigdrkg4FBrwT1QMg-3Jxb_gWCQj10xKF6-U0fT_CONKrQFxyLJ24TStT2Wqoi7jDLJJdBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
إندلاع اشتباكات عنيفة بين عصابات الجولاني وأهالي منطقة ترحين بمحافظة حلب السورية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76017" target="_blank">📅 21:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76016">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة الطيبة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76016" target="_blank">📅 21:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76015">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة الطيبة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/76015" target="_blank">📅 21:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76014">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭐️
لمعرفة تفاصيل أصوات الإنفجارات التي سمعت في جزيرة كيش الإيرانية
👈🏻
إضغط هنا</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76014" target="_blank">📅 20:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76013">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع:
إن الولايات المتحدة لا تزال تعرقل بعض بنود التفاهم، بما في ذلك مسألة الإفراج عن الأصول الإيرانية المجمدة، ولم يتم التوصل إلى حل لهذه المسائل حتى الآن. وبناءً على ذلك، لا يزال هناك احتمال لإلغاء التفاهم في الوقت الراهن، وقد أكدت إيران أنها لن تتراجع عن خطوطها الحمراء لتحقيق حقوق الشعب.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/76013" target="_blank">📅 19:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76012">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏴‍☠️
رئيس الأركان الصهيوني:
مستعدون للعودة للقتال المكثف فورا لإضعاف نظام الإرهاب الإيراني.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76012" target="_blank">📅 19:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76011">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌟
الشيخ نعيم قاسم:
سنبقى حملة راية الحق حتى تسليمها للإمام المهدي (عجل الله تعالى فرجه الشريف).
ستدافع المقاومة عن الأرض والشعب والشرف وكل من يواجهنا مع "اسرائيل" نواجهه والسلاح سيبقى.
خسائر إسرائيل كبيرة جدا وما يحدث في الجنوب اللبناني سيكون سببا في زوالها.
حصرية السلاح في هذه المرحلة استهداف للمقاومة وخدمة لإسرائيل.
المفاوضات المباشرة مرفوضة بالكامل.
سنعلن التحرير الثالث قريبا بإذن الله تعالى.
من حق الشعب أن ينزل إلى الشارع ويسقط الحكومة في مواجهة المشروع الأميركي الإسرائيلي الذي يستهدف مؤسساتنا.
لدينا أعظم مقاومة أذلت العدو الإسرائيلي فاستفيدوا منها.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76011" target="_blank">📅 19:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76010">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkiCaexSrTx_H0sFpIYUuBj9kDnRiyJm28VP9OpFd6c6YVXEXe4FIvn948h_VnJfkvijPWEzBnHw3BCovfVxeDoY3xMRollskx8k8LhF4FtEriG3BDprfbiNxPrW1V4xC8cpwrLLFT5gWt7CvqW_RpbBq2Zl2vRdwocZ1J2wc1x8S6US0aJKVrulVt8rLVszq-PnT19XtH3mSUPHzMabw_v8YkDKPVQD_dHLsdewh_o_OvWfA9XX0YaMRJlg9OXfq3t-HQCubzhDG4qE8Q09T1d33gYACnNL0eZZMy1-HdIU3CtAFTvrLcarnw18CQgtuaPRccYGGZq6RTbKXsUXFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني صعب جداً في جنوب لبنان.. مقتل جندي وإصابة أخرين من الجيش الإسرائيلي جراء استهدافهم بمحلقة انقضاضية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/76010" target="_blank">📅 19:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76009">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
مسؤول بالإدارة الأمريكية: سنقدم تنازلات بشأن تخفيف العقوبات إن تنازلت طهران بمسألة التخصيب.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76009" target="_blank">📅 19:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76008">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
مسؤول بالإدارة الأمريكية:
سنقدم تنازلات بشأن تخفيف العقوبات إن تنازلت طهران بمسألة التخصيب.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76008" target="_blank">📅 18:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76007">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني صعب جداً في جنوب لبنان..
مقتل جندي وإصابة أخرين من الجيش الإسرائيلي جراء استهدافهم بمحلقة انقضاضية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76007" target="_blank">📅 18:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76006">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0XYhROpELo365no2W62c7qqih6NSTsMRSx7HH8HdtQ-c-bnpdPKIR8hqlTQ-QW7LQrs-Fa0qPiCt2epkO_peLAgasV7q-jmdBJLGA_ft1GpLzN91kc_PEV9vyt1jhvqlELEBI_FMJXqN3L05JRXJmg56B3whQjZ037Pm6QndihmWP7q6wEDRWS12phaumWxvQp6nSrZ9Bl_QvI5Sr6qMOBSnCsxrNFccKtTnHPZ3D4YNPsd66RvqSc9fx9pDOGkMF46KtlYR9NhM-ePVNsWXWtJCgLQRwgF43IHousf0q7Xl-UX9-Ffx-ljGJjTGPtPU0PI8huChObUpVglIojb6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب: كانت إحدى أسوأ الصفقات التي أبرمتها بلادنا على الإطلاق هي الاتفاق النووي الإيراني، الذي طرحه ووقعه باراك حسين أوباما والهواة في إدارة أوباما. لقد كان طريقًا مباشرًا لتطوير إيران سلاحًا نوويًا. ليس الأمر كذلك مع الصفقة التي تتفاوض عليها إدارة ترامب…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76006" target="_blank">📅 18:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76005">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e83ce1a0.mp4?token=CuFYvl477tOmD4571wkcmw0Tk2Kym9D6sOGSVHBTu3EzydkEkpooqAt9ZcYbIpK0YmirHfllkzmWhWGaqt_0pFrXVtxgYqQPxY-ELPzbcaYWoSnImA9wsujPOlsUqUcWIYLZhb_g9KurApvdfgI4l6ah_HKZhX-exNU3cOmZjCbcX0A2AIS8_AlzhNf5iN0udTYBCBLXTP2wPqF_EXeYIkWjc8cEhStQakXSu8DfDTlLM5cLtLhRazcxVZP2QfFuRdvL4EqH9LnY_A45QDKYbfYR_OK8uGmjgBNfpF4Rt5NX8qMTlfdX273uq2WBmc6eSq7caxB3l4_Yi7hwI0HAHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e83ce1a0.mp4?token=CuFYvl477tOmD4571wkcmw0Tk2Kym9D6sOGSVHBTu3EzydkEkpooqAt9ZcYbIpK0YmirHfllkzmWhWGaqt_0pFrXVtxgYqQPxY-ELPzbcaYWoSnImA9wsujPOlsUqUcWIYLZhb_g9KurApvdfgI4l6ah_HKZhX-exNU3cOmZjCbcX0A2AIS8_AlzhNf5iN0udTYBCBLXTP2wPqF_EXeYIkWjc8cEhStQakXSu8DfDTlLM5cLtLhRazcxVZP2QfFuRdvL4EqH9LnY_A45QDKYbfYR_OK8uGmjgBNfpF4Rt5NX8qMTlfdX273uq2WBmc6eSq7caxB3l4_Yi7hwI0HAHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق وارتفاع اعمدة الدخان في منطقة جبلية حدودية مع إيران بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76005" target="_blank">📅 18:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76004">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63f2c0f5a.mp4?token=L-GbHujWn4iWBmcMUY-ESZC2slYAGDBt9kLswum2o0rpaiuFUh6kXdNJu8atPqLNviKCkHc-BTYA99ils9MvuT4D2nj06OnXo13i_zX1rElQQ8W6GvA5wW8N6zZoXcTRu4JLXiQgTF5vwJcmS71-zuQgCDQCq5XL6QF0w1lIB2EFqSzFFHIhR54lfoIIxUS_2ddAlxWwwQxHr5OJnp_M3JZsghG9Wqn8WuY3UJC2W56FQuuYebi7d_p89Xtmp1YaoIqdy8vA0BcwC8qduvKAOxNAITs-P1dbohpjUBNpeBzfOsOhOh5X_s89Agtkrabc0rnwQxgcSD3c9LIYmxcmqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63f2c0f5a.mp4?token=L-GbHujWn4iWBmcMUY-ESZC2slYAGDBt9kLswum2o0rpaiuFUh6kXdNJu8atPqLNviKCkHc-BTYA99ils9MvuT4D2nj06OnXo13i_zX1rElQQ8W6GvA5wW8N6zZoXcTRu4JLXiQgTF5vwJcmS71-zuQgCDQCq5XL6QF0w1lIB2EFqSzFFHIhR54lfoIIxUS_2ddAlxWwwQxHr5OJnp_M3JZsghG9Wqn8WuY3UJC2W56FQuuYebi7d_p89Xtmp1YaoIqdy8vA0BcwC8qduvKAOxNAITs-P1dbohpjUBNpeBzfOsOhOh5X_s89Agtkrabc0rnwQxgcSD3c9LIYmxcmqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 22-05-2026 أحد جنود جيش العدو الإسرائيلي في موقع المنارة عند الحدود اللبنانية الجنوبية بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76004" target="_blank">📅 17:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76003">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dnm-KJRIsH6SrKSBNZKUdNGV3DExKrlwgbYYYOr4XHfotvohcJnKPOU55Z9UdKTcXB6xdZLswJCRMZTqPP6vOfwE8pWnkcylWwP5jlitGvgsYbYX67ZAwAMMI62uBCnm49vO19M8RBnNPf9tw_Gyg1V2JZasPdHvKm8p-P2b5MbfTmzJkPAx8Dez8UHm9rm6XAwEzw9-v9ZPzHEMkRXnu8UEtOfxC6WD8enoVQGHfP8ugvOMbO4SggjP50bRqMNkp4bt3Ua5QC5XV6KMK8Ns3wvc1nFl8o2ZXap3QblT9w1jltLDxtpdx65JJ1-eZLG-ZgT__ji9lVtJU6HbcObdtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
كانت إحدى أسوأ الصفقات التي أبرمتها بلادنا على الإطلاق هي الاتفاق النووي الإيراني، الذي طرحه ووقعه باراك حسين أوباما والهواة في إدارة أوباما. لقد كان طريقًا مباشرًا لتطوير إيران سلاحًا نوويًا. ليس الأمر كذلك مع الصفقة التي تتفاوض عليها إدارة ترامب حاليًا مع إيران - بل العكس تمامًا! المفاوضات تسير بطريقة منظمة وبناءة، وقد أبلغت ممثليّ بعدم التسرع في إبرام صفقة لأن الوقت في صالحنا. سيظل الحصار ساريًا ونافذًا بالكامل حتى يتم التوصل إلى اتفاق واعتماده وتوقيعه. يجب على كلا الجانبين التريث والتأكد من صحة الاتفاق. لا مجال للأخطاء! علاقتنا مع إيران أصبحت أكثر احترافية وإنتاجية. ومع ذلك، يجب أن يفهموا أنهم لا يستطيعون تطوير أو الحصول على سلاح أو قنبلة نووية أود أن أتقدم بالشكر الجزيل لجميع دول الشرق الأوسط على دعمها وتعاونها، والذي سيتعزز ويتوطد بانضمامها إلى دول اتفاقيات إبراهيم التاريخية، وربما ترغب جمهورية إيران الإسلامية بالانضمام أيضًا! شكرًا لكم على اهتمامكم بهذا الأمر. الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76003" target="_blank">📅 17:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76002">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuVCNpB-mZZLqJ-ZyFsFeF-yROXi1p69Qy-L64XUaUUZvysOqVqTTpDsONLflJlmGqCV-67kkBxECnOvlQr0gNOtiYt3bQ_wIGcbjtXVF8SF9U2Sxrk03MCAMSdCEBWe7VBNQbuTqfCRS2MTr6oPHPMtwhk5yp2FXygD9jaC9xOV14V5b-_cH18Dm_oieLUmQZh6qVKh4B-qpllzukRZgAajIjeFWpO8wveuUt9jilxL-JF_AW6NVCpNtZWy4ceV5Pd3UxTOm8JS62YWZ_dIzXXazTOF2aqZbbNWVpzKp6_8-ExKTuOqcBz9Gi-LOheqV-prOK0w3np1wbVSQIN6AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فاينانشال تايمز:
يُزعم أن قوات الحرس الثوري الإيراني استخدمت شركة مقرها في الإمارات العربية المتحدة لشراء معدات اتصالات عبر الأقمار الاصطناعية الصينية مرتبطة ببرامج الطائرات بدون طيار والصواريخ الخاصة بها.
ويُقال إن المعدات انتقلت عبر دبي ورأس الخيمة قبل وصولها إلى إيران عبر سفينة إيرانية بدا أنها قامت بتزييف موقع GPS الخاص بها لإخفاء عملية التسليم.
وكانت الشحنة مرتبطة بشركات مرتبطة بقوة الفضاء التابعة للحرس الثوري الإيراني على الرغم من العقوبات الأمريكية القائمة على الكيانات ذات الصلة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76002" target="_blank">📅 17:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76001">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1MuMFxNf9OvdQqgT6dda7f7XiPoJyeRJb-8bfg4C7gk7j_xOk6MMCJHDLq3z0K5ZTX94DXnymifTmLdxZqlzKRSiedmGADTyyUIWRMEVynWnYOMOeGLVl7rAS9OtaUXFuIZLVX4UZBwKo0okC-ao7XXrkGJqjtMKWE_MQUYKPBsPFJgT3LP62eYAM02msoF46mCvBcyDLSimsAmsJKWVutZbnW0e_D1jb0DyxNCtNjvAnQZlJd3YwNPw0AMI1zfEBhQ6Zj2690Q_AS56BbmZTt0ZWUx7vKH6Y59XIQowBEQRcQ9CpA7cIt9_QU1XokVmoKO4d175yObXgQKQUAR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
حزب الله ينشر:
بعد قليل...
الضاهر تركضلي تركضلي..
😄</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76001" target="_blank">📅 17:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76000">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQGSdxCRJu9z-LpLPCqGNvmGfePqlWK6M9D5UZRHOhsUfNv95Mz-UExJKWRiwZsFnMoUNSgh-u7v-143ONDUBZ6zHCZ_DhXrGlYjVaB1y_OgO5K09qzH5YKuBm_lx9ws2eY486WmpjA4MuP8uiFVAXrvELMRKvpK-oALOe3Jke0c-N2nx8SDV7RW4CWWTqVOY1_b-Y8LP1XcuVdk7YcocaSEKc3pWn7r2Nc_DOrrGYRNfx7qG_az3NyEFzw31885x7vqSivP_GUoMooQ56cpEDT_Bs3w5fA2nxZacFGKdn0KH5WTVvMKbQzICNvpeJ68lMYII9BiCDE203kqib5-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
نتنياهو يغرد:
لن تمتلك ايران سلاح نووي.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76000" target="_blank">📅 17:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75999">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
‏الاتحاد الأوروبي
: توسيع نطاق العقوبات على إيران بسبب إغلاق مضيق هرمز</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75999" target="_blank">📅 17:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75998">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bbaeabc5.mp4?token=l-lAcVSEoqVxkWpkZJPsUdiY8U1UhY6vOfBU4zvX0WXlcQYlULhHuPGOvoI1KJP-KJ6h3091hQxApizCDCKvcosSp9VuweIBf2ye4BDn7Onj93kRItvxpJs9OCins8fyVpIDoblIvjOWj4YGVIqgK7w5Kw4RqYxXtqE0dnMrmhUa53fd-UMxYr4OvfErV8cBeZiHURmbXWhLmgJDOj8n9c8X2WR0wHK1DhA5adD9Y_8YDGwU2T_RjV0JIE86h4ZKV6ZAgBlsITX1Sx34pp9quN4y1AeI83CGdJunKUeMu0sstZbElarr0vMU2XBypLL5cT_NgqmFdIqKTewmRq0CukZhvWlwHjpGFgyrKSV3rd_D_x7UUnO1K_QMKrE-aejlOHsZ0w4xlMLiJrhLr1EVyrtW-Gh1ellAWCCWbq4P9Fg--GllWrPL-MzuUq-SbJI_KGhoWb1zlBwr7QBmlUSZoc2cSTiDknPY-j1lSCSSTCwH30dOGAz1BK-CGwnpGiZNqfDVz66lA3LOFRwmV46RhQfNg3KfEvosMGerVwQNjovX3tPT5g_28c38--LpQeHK6SRSP6mvVr2mOogvrTh80u9ERlnyYbdJ2ZX3OjVZNZ224prg9XqxadzYX2Q2ptdKS1gZ2ph1KbWIWthBn7AHrx3faj0vAKIhDlXS6llhKZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bbaeabc5.mp4?token=l-lAcVSEoqVxkWpkZJPsUdiY8U1UhY6vOfBU4zvX0WXlcQYlULhHuPGOvoI1KJP-KJ6h3091hQxApizCDCKvcosSp9VuweIBf2ye4BDn7Onj93kRItvxpJs9OCins8fyVpIDoblIvjOWj4YGVIqgK7w5Kw4RqYxXtqE0dnMrmhUa53fd-UMxYr4OvfErV8cBeZiHURmbXWhLmgJDOj8n9c8X2WR0wHK1DhA5adD9Y_8YDGwU2T_RjV0JIE86h4ZKV6ZAgBlsITX1Sx34pp9quN4y1AeI83CGdJunKUeMu0sstZbElarr0vMU2XBypLL5cT_NgqmFdIqKTewmRq0CukZhvWlwHjpGFgyrKSV3rd_D_x7UUnO1K_QMKrE-aejlOHsZ0w4xlMLiJrhLr1EVyrtW-Gh1ellAWCCWbq4P9Fg--GllWrPL-MzuUq-SbJI_KGhoWb1zlBwr7QBmlUSZoc2cSTiDknPY-j1lSCSSTCwH30dOGAz1BK-CGwnpGiZNqfDVz66lA3LOFRwmV46RhQfNg3KfEvosMGerVwQNjovX3tPT5g_28c38--LpQeHK6SRSP6mvVr2mOogvrTh80u9ERlnyYbdJ2ZX3OjVZNZ224prg9XqxadzYX2Q2ptdKS1gZ2ph1KbWIWthBn7AHrx3faj0vAKIhDlXS6llhKZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 18-05-2026 آلية هندسيّة تابعة لجيش العدو الإسرائيلي عند خلة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75998" target="_blank">📅 17:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75997">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🌟
‏
يديعوت أحرونوت:
إذا تم توقيع الاتفاق بصيغته الحالية فستكون هذه كارثة على إسرائيل.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75997" target="_blank">📅 16:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75996">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117e266d3d.mp4?token=LacGFHNp5B78sMeEEibNayhADK3hd9iNSzLhG8TG8lJ9DIxWKrNwuhhliRA-tMlfX86r0A2cYkasVeLW0CKYJZEKJSuGwToDZ1qJnCB1JR2qxewjG6Ihntj2iCwbJgWicJtEHfctfNovpFCmR5MGJsyKCP11DTivtFy8aUINZIht8mBM2bBOKz90CYH62NLJwVGn1hZhw3-J1EtUZJibDuDyLjwvcnmw0hYo8V7MxIEu5ksk5qks9jxMwNXBUMwA8VloCbgOpMLJRJjI-pkNqYZYi3k3FJqzj_W1G37ErQtW7S8yQQJKDQ_p8pjTmXMVmYMcY3QN9j4pXFtM1YHZYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117e266d3d.mp4?token=LacGFHNp5B78sMeEEibNayhADK3hd9iNSzLhG8TG8lJ9DIxWKrNwuhhliRA-tMlfX86r0A2cYkasVeLW0CKYJZEKJSuGwToDZ1qJnCB1JR2qxewjG6Ihntj2iCwbJgWicJtEHfctfNovpFCmR5MGJsyKCP11DTivtFy8aUINZIht8mBM2bBOKz90CYH62NLJwVGn1hZhw3-J1EtUZJibDuDyLjwvcnmw0hYo8V7MxIEu5ksk5qks9jxMwNXBUMwA8VloCbgOpMLJRJjI-pkNqYZYi3k3FJqzj_W1G37ErQtW7S8yQQJKDQ_p8pjTmXMVmYMcY3QN9j4pXFtM1YHZYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب مستعينا بالذكاء الصناعي   كون الحقيقة مؤلمة جدا</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75996" target="_blank">📅 16:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75995">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRMWlJnijciLowUW5zrcX8khbx9pXTE0AX7_Ziw-K5-X5KQbPfoe3nPD273GFPns1jGKV0r0z8oyeQIdDbqkunj61k08g0n_EDX5u9R2rQR0DolA7P0dEwuBtbfleeBdx4I1F2DTRZdpDYrisPnAtpcSvgszXU_5YEJIH5XUCPM0aPlf0RXkbqh6F96rNGPdHGAcBk6yPi2v1Jwuv9FHUpaBZeLWFzI85dNwBw2UVsxT5es4ihZk4_GHPA-LdvRbqMQ7rPNKXEdKIM4HMVeET_PehflK-olk6CiWoaGi16L67M5MNhmHwL0QNwT6bnolRXtLfZJCu32Cpreg7KSwfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب ينشر مجموعة من ساسة الحزب الديمقراطي يرتدون زي المساجين!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75995" target="_blank">📅 16:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75994">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea9114205.mp4?token=ZHqZyzMuRKvkPCindcU7YIoiRNRmG5mjIUU-jZ89-U6WNSfnpTeyour9JCdatUNEIyXSqEP9yH22h3WGjyUMrKcK7mUWJPCc99aLGTYbuR1aF_WGwvIlbc_h0QT8rN2AdPZJL3pAyJKRTVfyIQht0nZJr0OMgBsHDzmaF_6wYcHri6KH9a7D4ZjQXYH5is4qW1PHz-4PK69WxfycfJ7tuRzCKNlaMfWUyNmEj7lb7YZFUrQ-wVJLYriQzKvtd4fhf6zZDYfa87wteR4LFL4RotIhZfDL4ger0-wSUpIJHq0zjwsT0Y0OR6ku9u43F8EnqjcSkGvZUKd8C1rrOp8pEIKTGaRBDFGx03L8s9gM6_w1LvhSFWLcU1LQYI9lKwcBTca2yQJRmTeKF-YKp5WzbFVbTHQoil7cAsm9SQcxZlegyRZMHXswy8Kz6j_7FwjxuG6wN8bI0rVDtsvUpH2zXyLndgeEIlHBCIsLDFVFDkoFcxddWXeogk8oEx25cn6BS2axwevakffPqlP2AAU85mTTQGZV9ARRB1jb_kbXjk_WjMJVKvB9WaW5MhtqAX8nQCiWketomBx0mtKSC-7NwWVgnWZN8rX24MVZQKYBKKgRl0fB37XXG7mNv6cWZsZA_IqFWL5_jO1wRH-lklVTamC1Gmk-GX261fsKFEUUXaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea9114205.mp4?token=ZHqZyzMuRKvkPCindcU7YIoiRNRmG5mjIUU-jZ89-U6WNSfnpTeyour9JCdatUNEIyXSqEP9yH22h3WGjyUMrKcK7mUWJPCc99aLGTYbuR1aF_WGwvIlbc_h0QT8rN2AdPZJL3pAyJKRTVfyIQht0nZJr0OMgBsHDzmaF_6wYcHri6KH9a7D4ZjQXYH5is4qW1PHz-4PK69WxfycfJ7tuRzCKNlaMfWUyNmEj7lb7YZFUrQ-wVJLYriQzKvtd4fhf6zZDYfa87wteR4LFL4RotIhZfDL4ger0-wSUpIJHq0zjwsT0Y0OR6ku9u43F8EnqjcSkGvZUKd8C1rrOp8pEIKTGaRBDFGx03L8s9gM6_w1LvhSFWLcU1LQYI9lKwcBTca2yQJRmTeKF-YKp5WzbFVbTHQoil7cAsm9SQcxZlegyRZMHXswy8Kz6j_7FwjxuG6wN8bI0rVDtsvUpH2zXyLndgeEIlHBCIsLDFVFDkoFcxddWXeogk8oEx25cn6BS2axwevakffPqlP2AAU85mTTQGZV9ARRB1jb_kbXjk_WjMJVKvB9WaW5MhtqAX8nQCiWketomBx0mtKSC-7NwWVgnWZN8rX24MVZQKYBKKgRl0fB37XXG7mNv6cWZsZA_IqFWL5_jO1wRH-lklVTamC1Gmk-GX261fsKFEUUXaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 14-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75994" target="_blank">📅 16:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75993">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe46a8c5f9.mp4?token=OzKuzasVyqiAV070Vz2p5UGLSpHMCqUaAixMsjsSl9qZZcc4lzRCrzvUkwvbubgUIpvSUj1Cy_O7VhYOiqDgR1KODPzUbIv6nTUHJgr3XPLZns4BtVo4nb3UK84qDAr-AlMlFzuz5cuYj6TTrgBkxiYMs9uMzZ2sNVUqn2uJ8cXft8k36MuukTHVAeuIndBCSofbwkjcseXucY0ZXCeQHPEhRzuGM7CI1lf7OGA9d2THKkXtoGl5D9_yo2mHzV7kPrf1CijdowlC6_HrpU_-TJDBfdkoq2tKniaaJGnLrQi49ZEsqgNK5OQn0bSMfhHH5iOjn5i33EzTXRIGRhh8Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe46a8c5f9.mp4?token=OzKuzasVyqiAV070Vz2p5UGLSpHMCqUaAixMsjsSl9qZZcc4lzRCrzvUkwvbubgUIpvSUj1Cy_O7VhYOiqDgR1KODPzUbIv6nTUHJgr3XPLZns4BtVo4nb3UK84qDAr-AlMlFzuz5cuYj6TTrgBkxiYMs9uMzZ2sNVUqn2uJ8cXft8k36MuukTHVAeuIndBCSofbwkjcseXucY0ZXCeQHPEhRzuGM7CI1lf7OGA9d2THKkXtoGl5D9_yo2mHzV7kPrf1CijdowlC6_HrpU_-TJDBfdkoq2tKniaaJGnLrQi49ZEsqgNK5OQn0bSMfhHH5iOjn5i33EzTXRIGRhh8Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تنفيذاً لحكم قضائي يقضي بتنحية أوزغور أوزيل من رئاسة حزب الشعب الجمهوري، اندلعت اشتباكات بين قوات الشرطة وأنصار أوزيل أثناء دخول القوات إلى المقر الرئيسي للحزب في أنقرة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75993" target="_blank">📅 15:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75992">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYDhTddp-LehismvKVx5X7EjUiMQrkFCVKVX7Pdh9CtSSYfuTe8CxJahMRdbbSb4dwyz26GMorF4Shvzfk9gQur1xQ4PaEqVdtF4kOjn2_QBp7ZV1X2-XPSDGRv9zLdX3p2CXGiVyBp5tj5bsMwZziOMMzswBpS2k5TxEtSLljw93fVMfjbY6ocaiu8yulv81Ihau_xCclBIo4VtyMm-5QS5EAe2nNLyiro55ZiyEz3ZBOb6x_NibpbfrTyItDK1eyCR7egElz5qG3HNs4yKPQdpkoe1RxWiI3qz2aoF9tnbA_Bb9vCsqtT3PcE7KuIpfKtQAKTp66Cf2UR2JGImKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب مستعينا بالذكاء الصناعي
كون الحقيقة مؤلمة جدا</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75992" target="_blank">📅 15:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75991">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff86c83697.mp4?token=lp42LE4oC0cETuO7GAkCCSWbeiwJiZgWxOqHLrxPQjiGBxnSzmRYKuMr5W0EsPqia-o_RcglxbAs7gcP91JvvNJbe99kbJo02VQPZl6T6pSYpRq29csn7g0GsaVD5M03YO7eQiSFpSAURMvTEKAvBTOexZInoVHahw3lZhxbqQAI7goCxhPD8e1rULH5y_FmZDQQyvFdyC5reH32eZAmTEv8aghQN_3ZtjhiyG_Y5p-zLoGWdsjIjd3xDE2BdQpkxnLkUX6fk90ZBbPXe85VnhIr3wTZE9GCw_Jr5J-lZEglfH7VhMzlnqHzyR8SpDb7AaaoVmCfp5Qedk-uCA0A56pH-z8geX3pp_4lrBAdDgwBVTJWt75_m9IETOVw68jfE15fGazQ9sUP8bXCNtaT8rfxUgqFBzCMFzR59NDiiMwpKK91PO7h9IXXLQ2jCIcEBSYP67YUGfYiygSIfCjV4bbESXSWXcyimIoBFlwLVZ2kaxGzMytwzeXD2J13THbE0tiGZoxNTj_e5clV-11sBxscBhWIQYRXeJRmwY8AwU-y-pYAdDsGaSMBOH-_ou1Y0Pbj7xt-Xy-D1Q9so-aYZvvgRaLJCz8lbXRzhKJjW6xpW1p1Vj9g5opkLlXWxzwUWB2oHZj88W_VjBeqlIPvthoNF8-seED1ljq8MGeKJWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff86c83697.mp4?token=lp42LE4oC0cETuO7GAkCCSWbeiwJiZgWxOqHLrxPQjiGBxnSzmRYKuMr5W0EsPqia-o_RcglxbAs7gcP91JvvNJbe99kbJo02VQPZl6T6pSYpRq29csn7g0GsaVD5M03YO7eQiSFpSAURMvTEKAvBTOexZInoVHahw3lZhxbqQAI7goCxhPD8e1rULH5y_FmZDQQyvFdyC5reH32eZAmTEv8aghQN_3ZtjhiyG_Y5p-zLoGWdsjIjd3xDE2BdQpkxnLkUX6fk90ZBbPXe85VnhIr3wTZE9GCw_Jr5J-lZEglfH7VhMzlnqHzyR8SpDb7AaaoVmCfp5Qedk-uCA0A56pH-z8geX3pp_4lrBAdDgwBVTJWt75_m9IETOVw68jfE15fGazQ9sUP8bXCNtaT8rfxUgqFBzCMFzR59NDiiMwpKK91PO7h9IXXLQ2jCIcEBSYP67YUGfYiygSIfCjV4bbESXSWXcyimIoBFlwLVZ2kaxGzMytwzeXD2J13THbE0tiGZoxNTj_e5clV-11sBxscBhWIQYRXeJRmwY8AwU-y-pYAdDsGaSMBOH-_ou1Y0Pbj7xt-Xy-D1Q9so-aYZvvgRaLJCz8lbXRzhKJjW6xpW1p1Vj9g5opkLlXWxzwUWB2oHZj88W_VjBeqlIPvthoNF8-seED1ljq8MGeKJWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 آلية اتصالات تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75991" target="_blank">📅 14:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGBolSMxbvl13LeNRTitYWpZW2WHlhCjM7Xwxy952KutaEhcCMY-UKCWumCgheMSiog26VP_0tChGXvtc6jNGxljeRY-B80M5n2jZSiQNnSoRZike7fobfyud6msdu6dKpRxzq8fOE4mnAcPmdHwZ3-VAc9VOXVrTICYjy5QmPYQw_l7TKl3qmjbyYlAixHQCG8X5hYZ9pC99VQugKszUvUKAoKbvuKJi-4gBbuIL6YoysF3cQM3XMqvuUWJj-WK0BhrQIN5omc1JjUMejRCrGM0fTCgPMw23HHz7UGTE9vynJY4BzVVHIuFoSLgQs4AH59gLBM3jcyGe5LJgowf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5NSlcmQyeJD1UDPUEqIcraNYiX69Cu6OQpSy8cNhyXhCfmlrh981P6QHpWtExORnGzmO0PjHqZR3D2x8wJo_dBQJaIn1kS14dGSXmo9dbDoRESF7T8iedPjcIBpXX2osk4_4tk4thr_5YawNbiPEefeXi4jylqEm1v8Ml-HYuCr6kBIbMsTqOxxGBhrqfwJQDvcnIsE6FktxYYdgUU2XaKkJhEUHluLbIMOtZyt8ZWdOU8QESZgIsdWz8p6saIHUSeYIO95LwPwdlyUUCMW63mWHMungBq1nV2BbPBFL5wfNe3cFNnFr-sVFbzX0JqBobYE5ECXhQikNiUfx1vM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYso8YS6rvZI5UbXlxzr_uVn988XQdw2ic9jYjnp9WGf_JKrJqutWAqBlA-Ca0VKFJsXwBQ3iQBokQCukHXHkJYb4rzUmhrrn2523DoKYClL0JQubrHedESjGkoM18WHjKWmuNZIdeDLXWsAjfyBDJ9Dejiv85TckGX3i4ZZik6kDG3L62HqAHWIuQ81caxlxjIqXRTzlPsAqscc_kAjIcaNa7p-J68Fw5Buasp4iTBY3fBdjC1-NZboDyRkp8lht1mg75m21b_kQjqoH0XnUznCNrrzac4YNVYfBVmFTGs-GGS6jKnZWvi54NILTiWlRgS5PMRevYo5ITMYbcj3AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
ابطال الحشد الشعبي يسعفون اخوتهم في جهاز مكافحة الارهاب بعد ان انفجرت عبوة ناسفة عليهم.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75988" target="_blank">📅 14:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎤
فوكس نيوز:
الاتفاق المتوقع ينص على بقاء القوات الأمريكية بالقرب من إيران لمدة 30 يومًا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75987" target="_blank">📅 14:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75986">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
حكومة البحرين الجائرة تصدر الحكم المؤبد لتسع افراد مدعية تخابرهم مع الحرس الثوري الايراني.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75986" target="_blank">📅 14:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75985">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8621a769e.mp4?token=b4vMXsdEG6-xEmSIf99syu-U3ZK2GiN50sK6FPBADTmWOwHT71au-Rv0IuRSX6Fv8_xUfGHJFivu2VVJMO-snkZdDtX-LXFAMc4o8ODVmKLf2ZqpWt9oKDx70tgT6TeH9Bd4inO2ETdbjNdygwzUSYX68iLX3Rogk6Ej6arqYfXFOzjwYsFSN7rywMLwd429JmjPTUkkDOJnxi_DbSDBz2TwftiPRgwn3qERprC5kTVpiP4BILQgHNdGFJaQa3C55MF1Pca7I0XwOQoBWPDF-LmG9q8dlVl3nlTct_CmokBC19tYGEDzouaxNLBSOVK3sZvkEbsmpJqwAadAKt5Tpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8621a769e.mp4?token=b4vMXsdEG6-xEmSIf99syu-U3ZK2GiN50sK6FPBADTmWOwHT71au-Rv0IuRSX6Fv8_xUfGHJFivu2VVJMO-snkZdDtX-LXFAMc4o8ODVmKLf2ZqpWt9oKDx70tgT6TeH9Bd4inO2ETdbjNdygwzUSYX68iLX3Rogk6Ej6arqYfXFOzjwYsFSN7rywMLwd429JmjPTUkkDOJnxi_DbSDBz2TwftiPRgwn3qERprC5kTVpiP4BILQgHNdGFJaQa3C55MF1Pca7I0XwOQoBWPDF-LmG9q8dlVl3nlTct_CmokBC19tYGEDzouaxNLBSOVK3sZvkEbsmpJqwAadAKt5Tpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
أحذية شهداء الجيش اللبناني أمام مبنى مجلس النواب في العاصمة اللبنانية بيروت، احتجاجاً على مشروع قانون العفو العام.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75985" target="_blank">📅 14:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🌟
🇮🇶
جهاز مكافحة الارهاب:
يعلن استشهاد 3 مقاتلين وإصابة 4 آخرين بانفجار عبوة من مخلفات داعش في صحراء الحضر جنوب غرب نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75984" target="_blank">📅 13:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 18-05-2026 آلية نميرا تابعة لجيش العدو الإسرائيلي عند خلة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75983" target="_blank">📅 13:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75982">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94daa968c2.mp4?token=pjys7Do70LWb-WnaOBB0vKcuIBbkemvqA341RX11TLq0jvEwZj_yEgt-FsWk5p5UVn3tDTbtVRJtqUzklHFIrHyNh5esa6FAjt14FYNdEtM89Q2khtsg85RZpmPbilwgCvQ5L9XBR8Kll75Hs0z21smuvWi2gdUrzSR_I_Sj4bzThUvvhP9MIaL_3McWLEHmkIvfJjrsSchjjQjzs3q2LR7sFc-lpohAtigLdJrl0R0Mfmc2Olf3-DAoQpr4iL3It-1dt4xD2U4mmkwG5sR4ir75vIMA8k_pvDE1nyIU2bOTgf44Oh3ZuxEX5EH3mzOepGnXWJiuTQL1nuvACRtaaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94daa968c2.mp4?token=pjys7Do70LWb-WnaOBB0vKcuIBbkemvqA341RX11TLq0jvEwZj_yEgt-FsWk5p5UVn3tDTbtVRJtqUzklHFIrHyNh5esa6FAjt14FYNdEtM89Q2khtsg85RZpmPbilwgCvQ5L9XBR8Kll75Hs0z21smuvWi2gdUrzSR_I_Sj4bzThUvvhP9MIaL_3McWLEHmkIvfJjrsSchjjQjzs3q2LR7sFc-lpohAtigLdJrl0R0Mfmc2Olf3-DAoQpr4iL3It-1dt4xD2U4mmkwG5sR4ir75vIMA8k_pvDE1nyIU2bOTgf44Oh3ZuxEX5EH3mzOepGnXWJiuTQL1nuvACRtaaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 20-05-2026 آلية نميرا تابعة لجيش العدو الإسرائيلي في بلدة حداثا جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75982" target="_blank">📅 12:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75981">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
إعلام خليجي عن ‏مصادر رفيعة: الاتفاق المبدئي المحتمل بين إيران وأميركا سيحمل اسم إعلان إسلام آباد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75981" target="_blank">📅 11:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75980">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
انفجار لغم أرضي في منطقة الطيب بمحافظة ميسان جنوب العراق ؛ مقتل شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75980" target="_blank">📅 11:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75979">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📰
رويترز عن مصدر إيراني: طهران لم توافق على تسليم مخزونها من اليورانيوم عالي التخصيب</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75979" target="_blank">📅 11:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75978">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📰
إعلام إيراني: في حال الاتفاق على المذكرة سيتم إعلان انتهاء الحرب بين الولايات المتحدة وحلفائها ضد إيران وحلفائها على جميع الجبهات</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75978" target="_blank">📅 10:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75977">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
أنباء عن سماع دوي انفجار في محافظة السماوة جنوب العراق دون معرفة التفاصيل.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75977" target="_blank">📅 10:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75976">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔹
في هذه الأثناء تزور صواريخ كنجال الفرط صوتية الروسية مدينة كييف   الهجوم الروسي يندرج ضمن رد موسكو على الهجوم على بناية سكنية للطلاب في جمهورية لوغانسك التابعة لروسيا.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75976" target="_blank">📅 10:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75975">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc1dc9836.mp4?token=PzfQoxKRCV7tSFIq-oNdLo16-PYPKmLdDrBB9Lf-tPuKe9Qzpt5QMWbvM-YNL1x-4_TMGniPr_1QM9T4qBpi3PD6VWmkjKxihe0MPc0hiMszUPRcg3fV1YkkxuKl06qh7IpX5E5Rq8ZNNDtvhwM7p6vWQLUkebW0RW1SLV8uc2lIF1_qCU-jb7S6TL7o1FFO5hPnk_iJw6krMsq5ezE5jCDpDui0fuAkT481e4KnXyh7R0QcNUusKn-GKy4pFuYXR6s28ItABwCd_xQZ67sLF55ayJ4bM3hx8U6NP1EiproZjWIUbDsh_j0TDqpmFt2hnF2rOhY2R3oKaEtP7kKJKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc1dc9836.mp4?token=PzfQoxKRCV7tSFIq-oNdLo16-PYPKmLdDrBB9Lf-tPuKe9Qzpt5QMWbvM-YNL1x-4_TMGniPr_1QM9T4qBpi3PD6VWmkjKxihe0MPc0hiMszUPRcg3fV1YkkxuKl06qh7IpX5E5Rq8ZNNDtvhwM7p6vWQLUkebW0RW1SLV8uc2lIF1_qCU-jb7S6TL7o1FFO5hPnk_iJw6krMsq5ezE5jCDpDui0fuAkT481e4KnXyh7R0QcNUusKn-GKy4pFuYXR6s28ItABwCd_xQZ67sLF55ayJ4bM3hx8U6NP1EiproZjWIUbDsh_j0TDqpmFt2hnF2rOhY2R3oKaEtP7kKJKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
في هذه الأثناء تزور صواريخ كنجال الفرط صوتية الروسية مدينة كييف   الهجوم الروسي يندرج ضمن رد موسكو على الهجوم على بناية سكنية للطلاب في جمهورية لوغانسك التابعة لروسيا.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75975" target="_blank">📅 09:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75974">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🏴‍☠️
إعلام العدو عن مصدر إسرائيلي: الاتفاق المحتمل مع إيران سيء</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75974" target="_blank">📅 09:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75973">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdaad755f.mp4?token=AJVcKJi6fpq7Salp4IVC8ZAELEy0iygbkcA7RnGOn2AHOYFgGHKzcH6neoRmod0JXBLdVJ1rS2S0tXOw1H31boZFuyNlOPwtalUskssOZafC5ZGqRqigDlH-AQREdDntL9zhsY-6uNLXDEHbxUhKKbb84Cj2HBpGaJkkGWtGFTsWxj3Q3FkjhdCXcK5y9Q7fIdrth8EjqYgEsbRVhOZNkPxREW4LxibtfQT4X7_s5PX9xG9OXrTNp4Dv1RRBV3Cx9-zTEG8SlAppR-C1IfXAl9y0GQZ27AQnz0hEvOHoYOdKFVyHBaJtPHZCF1mGwwGtL7XBxcka2qB7V21GLOsiqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdaad755f.mp4?token=AJVcKJi6fpq7Salp4IVC8ZAELEy0iygbkcA7RnGOn2AHOYFgGHKzcH6neoRmod0JXBLdVJ1rS2S0tXOw1H31boZFuyNlOPwtalUskssOZafC5ZGqRqigDlH-AQREdDntL9zhsY-6uNLXDEHbxUhKKbb84Cj2HBpGaJkkGWtGFTsWxj3Q3FkjhdCXcK5y9Q7fIdrth8EjqYgEsbRVhOZNkPxREW4LxibtfQT4X7_s5PX9xG9OXrTNp4Dv1RRBV3Cx9-zTEG8SlAppR-C1IfXAl9y0GQZ27AQnz0hEvOHoYOdKFVyHBaJtPHZCF1mGwwGtL7XBxcka2qB7V21GLOsiqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
مقتل ما لا يقل عن 20 جنديًا باكستانيًا بعد أن استهدف قطارًا يحمل أفرادًا من الجيش الباكستاني وقوات حرس الحدود في كويتا، جمهورية بلوشستان الباكستانية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/75973" target="_blank">📅 08:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75972">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🏴‍☠️
إعلام العدو :
تتضمن مسودة مذكرة التفاهم بين الولايات المتحدة وإيران إنهاء القتال بين "إسرائيل" وحزب الله في لبنان. ووفقًا لمسؤول أمريكي رفيع، أعرب نتنياهو عن قلقه خلال محادثة مع ترامب، لكنه تقبّل موقف الإدارة الأمريكية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/75972" target="_blank">📅 08:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75971">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF0h3k11-vTAd6zVPINLvhGDC2BNkgmGHTl5eOFuByUTMBvXZF-hdm_eg8npf22LQoOnyqetXhKSJwvauEG_za3XQEK3q9wSIhAgfl30cRZOaAfki7cOte2EyafiwEh39j3UptCssPnP5SVplWpMelmz8Ro-B-lVDXFKkdqptbjJqA0NuI1CUGT9RzSL2auMAKTe8LiDHBg5nhTbLpuOji6pqEO717-taBScKEGVCKypJczK76c-M-I2sKtj4kB5f-5iyXf4H_ExzXV2XfhidqhT7UaEul14uBekH2qdEBwY4xeKQtvdRYNZHrKo9AwSdb1JS4kFUZ-96yBDhu8vJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يشكر الخدمة السرية بعد إطلاق نار واشتباكات قرب البيت الأبيض</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/75971" target="_blank">📅 08:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75970">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
🇷🇺
على غرار التحذير من العراق   السفارة الأمريكية في أوكرانيا تنشر معلوماتٍ بشأن هجوم جوي محتمل كبير وتوصي السفارة، كعادتها، المواطنين الأمريكيين بالاستعداد للاحتماء فورًا في حال صدور إنذار جوي.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/75970" target="_blank">📅 01:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75969">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUK49HmARHw5qNpRizfgCTYcxCk7XyALHcI5wRklwxTMMEilnvgSrufrfAYwJHvlSa88rArnaZLnK0CpGxh9HU1ck_GUpXcq4smU0Cz4dozMSlcp2PtLrbuOT0mGhNhEmIgpiCq0b5uMd_fOcLdmDE6UdQgoWoWLFUOnqPwlZliCLVbdAVxVIvlVpHSDNQv6qioAdlpz9y22oAVnXRcJ95DHMcj1lwd0RWj-0ZneHUr3Z30mkAA5XgKLMkNwDyHP7MI3DStwRPaRJEYYrx2utb4n16pgWYSJrQAHigE4qhNy6drhxZnwHnLJG6o3aoWqwgFOZMWwxZv8XoOFoNGwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو : ترامب يعلن الاستسلام أمام ايران .</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/75969" target="_blank">📅 00:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75968">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
🇷🇺
على غرار التحذير من العراق
السفارة الأمريكية في أوكرانيا تنشر معلوماتٍ بشأن هجوم جوي محتمل كبير وتوصي السفارة، كعادتها، المواطنين الأمريكيين بالاستعداد للاحتماء فورًا في حال صدور إنذار جوي.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/75968" target="_blank">📅 00:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75967">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b8d79693.mp4?token=nSZnIsgmWysIMEooGVHCX30JxhQGhY6NRoSs-NgXA5hOJMIcStMGQFhlGXCZ3Tixc0Gv8OtOIuI7kSoyXIv3D5uYCFo1-woX8RHOo8mi8l0ejpp4z3XLECC_LThClkZrKBgdh3crHhRhjfHRIouct8gQN6fiE9NF7Ca5tRzO8Q9pk2LaFqkTbO-XGSjWb0gc12fXunTJ6b_sHHQCAhIREGwTEmqztIlcoojVfDbNlUtuR4utYSMPX9MJzH6AXjQ18B6qDSA_3Rfks7Ww0EykoOzn5lMylrxTTdgkUE45vmkwgBhtn5zaQ_7tsEGidk_cQuACsVf-Sduo48NpKLcyJmMAkiPRLBm57WtgNpEQQ3EiJw_AenhF57r_h8XXCIuFu33UZ7x460pLrEpDvKMobWlfzf5u4SGafW-Sqer1_YcTapghoX6TK5DXGewUFBlwnv1GMcfDKXKTqC6EY-aHmLqbxW8Dln0f1vgQdvyZNRrwyusSVAT2wszLTP_AFvzsVMW4z1bZQPbjXkq9gYJjdlJrcY8ZAE9VWwwpvWmHkGes6KEfbRUY1zWsKHBttQzODpUOj4wKvZ-C_w2rESYwg4AEhHBuCTN_P8Jol5Lv7F_-8i-wXyZb__IJ5ky-Hz00tcAyoa2FkqBPL_HciSRlVVTbICHwflAq90aMp2bfiuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b8d79693.mp4?token=nSZnIsgmWysIMEooGVHCX30JxhQGhY6NRoSs-NgXA5hOJMIcStMGQFhlGXCZ3Tixc0Gv8OtOIuI7kSoyXIv3D5uYCFo1-woX8RHOo8mi8l0ejpp4z3XLECC_LThClkZrKBgdh3crHhRhjfHRIouct8gQN6fiE9NF7Ca5tRzO8Q9pk2LaFqkTbO-XGSjWb0gc12fXunTJ6b_sHHQCAhIREGwTEmqztIlcoojVfDbNlUtuR4utYSMPX9MJzH6AXjQ18B6qDSA_3Rfks7Ww0EykoOzn5lMylrxTTdgkUE45vmkwgBhtn5zaQ_7tsEGidk_cQuACsVf-Sduo48NpKLcyJmMAkiPRLBm57WtgNpEQQ3EiJw_AenhF57r_h8XXCIuFu33UZ7x460pLrEpDvKMobWlfzf5u4SGafW-Sqer1_YcTapghoX6TK5DXGewUFBlwnv1GMcfDKXKTqC6EY-aHmLqbxW8Dln0f1vgQdvyZNRrwyusSVAT2wszLTP_AFvzsVMW4z1bZQPbjXkq9gYJjdlJrcY8ZAE9VWwwpvWmHkGes6KEfbRUY1zWsKHBttQzODpUOj4wKvZ-C_w2rESYwg4AEhHBuCTN_P8Jol5Lv7F_-8i-wXyZb__IJ5ky-Hz00tcAyoa2FkqBPL_HciSRlVVTbICHwflAq90aMp2bfiuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على الرغم من تنفيذ حكومة البحرين حملة اعتقالات كبيرة للشيعة ومنعهم من مواكب العزاء.. شيعة البحرين يكسرون القرار الجائر في ليلة استشهاد الإمام محمد الباقر (عليه السّلام).</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/75967" target="_blank">📅 00:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75966">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامب:  «أنا في المكتب البيضاوي في البيت الأبيض حيث أجرينا للتو اتصالًا جيدًا جدًا مع الرئيس محمد بن سلمان آل سعود، رئيس المملكة العربية السعودية، ومحمد بن زايد آل نهيان، رئيس دولة الإمارات العربية المتحدة، والأمير تميم بن حمد بن خليفة آل ثاني، ورئيس الوزراء…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/75966" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75965">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n093GBkE3s6A4wb6b4V8FWxnL_bHrVj5VxyZSz0O0a8W2Uvfi_KRQ6yRz_GB26t85D6ZWXGFba3ULNixLPdhlazpWhetvz6U8wthCWN6P2yhnIIc6Gw3lEvYPK1Mb9p6TH9ozMotRqsQOF4eV0F0QfvUlqrjKzL7qxB16w5Fj_lQvpClYF--JlnPYyj1efx5W1DjfAyQx0-x4quFqp0qWpyWXpVLvOy4Vg-aAsyMPXkxW2KDjYvEPQbiiGjTWTMGwILh3x6zH_huJ-3JpGTNzC_Wx2sprBBJ_PCIv-_0kIunhjiqMsslUst6u_PzGyulLEYE92QOXqUhkNMxVjV1Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إسماعيل بقائي: ‏
في
الفكر الروماني، كانت روما مركز العالم بلا منازع. إلا أن الإيرانيين حطموا هذا الوهم؛ فعندما زحف ماركوس يوليوس فيليبوس (فيليب العربي) شرقًا ضد بلاد فارس، لم تسفر الحملة عن انتصار روماني، بل انتهت بسلام قائم على شروط ساسانية: كان على الإمبراطور أن يرضخ!
﻿</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/75965" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75964">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75964" target="_blank">📅 00:25 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
