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
<img src="https://cdn4.telesco.pe/file/FKHlvjEDVU9q_fLGcjHvfUGNv90uwNr6RfMxM3Q46hT6ZoQq3ofAdA_kX23C_fGzPnIaxR57Ov-Kw-vaZnNQxtr5bd92n2QNUvx6E3kG6bkPhx1mMnlXLj1zUoXJiK9fPUjr_hdqVP4WYAGI7hUokHnDZzvQGzY2lai8gijiJlwIgsXIJBu7o0kMr3jaZh1XAj4TWrgBeOy8CBAGKnXpQKxRx0N850HO5YEcjktrpkwZ9yrZh4lWRDzj1L1nFE8xR3F2f9ZHQUjwplRMlS3PZV1hn-TfeHc2FzsKJBcDc4aVou2a26ct-y5iH0PE2fzyXlER9v5vnuEahbUdgPsvZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 22:01:32</div>
<hr>

<div class="tg-post" id="msg-83670">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2572e25a.mp4?token=tg6X75Uw6Mka9LoRJzejoWUuxpoQ6RoLbpfEz5p2tMmXJMDPiqR11JWz9S6lNtYL2cpfPiBuzh2jWdholJEyrVcgAG5-sVcxnUSxiImctPZexFiBZh5RLFVo8Plv6ze9q68gJQnOARRgbYhV58Sb25P1ROJe3nUFy_H9YWoEyW2FzH6Mp2aAvTJSIVWtqiEt5PfHmrdUwdNHsOTyjeB-RgZxwrLEkYRAjKS0H_PflGocbE_WcMltRMeQAcOXtW7a1yiPZ7qs3a5-AsiW88pbgH3afzGHMpZOldshDxOPpnuzx5BeA95G9DryPnqKN2jzezVIVQrVwzUi7QQdu7W-Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2572e25a.mp4?token=tg6X75Uw6Mka9LoRJzejoWUuxpoQ6RoLbpfEz5p2tMmXJMDPiqR11JWz9S6lNtYL2cpfPiBuzh2jWdholJEyrVcgAG5-sVcxnUSxiImctPZexFiBZh5RLFVo8Plv6ze9q68gJQnOARRgbYhV58Sb25P1ROJe3nUFy_H9YWoEyW2FzH6Mp2aAvTJSIVWtqiEt5PfHmrdUwdNHsOTyjeB-RgZxwrLEkYRAjKS0H_PflGocbE_WcMltRMeQAcOXtW7a1yiPZ7qs3a5-AsiW88pbgH3afzGHMpZOldshDxOPpnuzx5BeA95G9DryPnqKN2jzezVIVQrVwzUi7QQdu7W-Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد لتطاير الصواريخ من مقرات الاحزاب المعارضة في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/naya_foriraq/83670" target="_blank">📅 22:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83669">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNbpDMFF-FkqE_qd2aBvartNuZdIYf55pTkbqrc7Bv-qed9PnoWVTutghNsh3pdqki60qhs2ux9cDwuP6uSGNIKFV3eBZDmrzmLAGBv47flRqTN9rWd8EdNQW5wKdwasvQTaRqvDHJmkVU3fEhQgTIj2YviEb9ivPLicwUHa6ws1-heVLp1TofrexX5WnYJus7o08hZWJHGnXVql2NsY3fp3s9UiC9MdZ0W0SweFvyh4aeHFDSTHfYFXPgG85l_j9fAWgTts15H3CW7CS3BEyurdFQgdquO48omlJn3Zof_oYsR-TjEybh5bxVq2Qbe1qP7LF-YO8lRA5llsligD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خام برنت يرتفع بنسبة تتجاوز 4% ليصل إلى 88 دولارا للبرميل</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/naya_foriraq/83669" target="_blank">📅 21:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83668">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c567d28d5.mp4?token=qAcj5nus4bg2bD2sZ34SXb88vM_B_eAMCYKLBuzI1PRZPYiEnEogA2MlQAvQrauHfcy5OLA1f5ieLDrNPochs1vcANv27tlEMsqH5kgyxhIinZ5anoO_pt7i0h5gmLj58lmJzWZ4sCyng0E6ZUJzVzdwKZllPBcUSKlAKlD7X-ZFUY31J9GtQsCcJ2YhjjpJbhi2XqP4inqeK093EA4UOsgpC1L2D8it-OVoYna1BbNyGimg_XPetnqEk03c_6GSKun4w8yFp6aICwSgpBHYBthk8cKN2h6xyaUIhxz4-zdmIMoR0Ozr2aDOjfmjBcZlEwPh036h6kVHQaLrasO17w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c567d28d5.mp4?token=qAcj5nus4bg2bD2sZ34SXb88vM_B_eAMCYKLBuzI1PRZPYiEnEogA2MlQAvQrauHfcy5OLA1f5ieLDrNPochs1vcANv27tlEMsqH5kgyxhIinZ5anoO_pt7i0h5gmLj58lmJzWZ4sCyng0E6ZUJzVzdwKZllPBcUSKlAKlD7X-ZFUY31J9GtQsCcJ2YhjjpJbhi2XqP4inqeK093EA4UOsgpC1L2D8it-OVoYna1BbNyGimg_XPetnqEk03c_6GSKun4w8yFp6aICwSgpBHYBthk8cKN2h6xyaUIhxz4-zdmIMoR0Ozr2aDOjfmjBcZlEwPh036h6kVHQaLrasO17w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد انية من مكان الذي تم استهدافه الذي يضم مقرات ومخازن للاسلحة المعارضة في محافظة السليمانية</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/naya_foriraq/83668" target="_blank">📅 21:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83667">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الكويت تعترف بضرب موقعين من قبل الصواريخ الايرانية واشتعال النيران فيها</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/naya_foriraq/83667" target="_blank">📅 21:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83666">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28e4a12fe.mp4?token=f0hjqzQJOARolQQBWslbfH1NPdl9tvgRalf3zbZQaLHeZxdX-CuxC2XfsJn4x2m9WyDI6XvXOYO7Qd-5wUVNahqALDZKrjQroFTYnZE92BEIy5hYHip0slV3gua3deIPV-u0PPELxQErtE84gPKZl5QmBG3IMVT7Fo6sVKvMHGEIykoBKzYUupJS7chBtYwVFJuIjryfXW2k7sVJqosx47VuVqaljuQQ7DKWofzqCQW5IlI674ZYdT5lwmMQJzpz1Gjez2McEUYqCR7C7XMDuJ7JSUKflschpEjfUQ-XvuebW4xaaM0ZVk1-bR_wj8bFgAZmnTLIRmI4vtVyZ39Sxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28e4a12fe.mp4?token=f0hjqzQJOARolQQBWslbfH1NPdl9tvgRalf3zbZQaLHeZxdX-CuxC2XfsJn4x2m9WyDI6XvXOYO7Qd-5wUVNahqALDZKrjQroFTYnZE92BEIy5hYHip0slV3gua3deIPV-u0PPELxQErtE84gPKZl5QmBG3IMVT7Fo6sVKvMHGEIykoBKzYUupJS7chBtYwVFJuIjryfXW2k7sVJqosx47VuVqaljuQQ7DKWofzqCQW5IlI674ZYdT5lwmMQJzpz1Gjez2McEUYqCR7C7XMDuJ7JSUKflschpEjfUQ-XvuebW4xaaM0ZVk1-bR_wj8bFgAZmnTLIRmI4vtVyZ39Sxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات لا تتوقف ناتجة عن انفلاق الذخائر التي تم قصفها في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/naya_foriraq/83666" target="_blank">📅 21:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83665">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات من جديد في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/naya_foriraq/83665" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83664">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">السياح العرب يوثقون حجم النيران في مقرات المعارضة بمحافظة السيلمانية</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/naya_foriraq/83664" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83663">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ee2001e8.mp4?token=s7K4T1c-8xingbEE2p4qIc590PUIpfTwo_cKaOKpGixffdf_iGSBZfJSyRIHrS7wEBKBg5d61DV-Q4DmbhpGCj1Opw1fL7jMxA1j-UFsRl6bC2vx0WVJvkntlNoOFTr-ESqt9v_tyg0xYuFFOP1JiVw1zGP2PegWNZSO0OhsrXPXjvZJke9r1ZCA7d7NpvDaCa80JdYTtUsHMEfGfRZ14Dz-QcMwUTlFIrxSfhM7zRpyTJm8fEi5P3R6oG2sODCedJaHNlwqbJqAE4BoggIKdB_yz9n4vwVdNHNHurv-4sTWoLLhGV2z6mb5rYwWnrrPxearn1nCXbGZG9VVB7BEUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ee2001e8.mp4?token=s7K4T1c-8xingbEE2p4qIc590PUIpfTwo_cKaOKpGixffdf_iGSBZfJSyRIHrS7wEBKBg5d61DV-Q4DmbhpGCj1Opw1fL7jMxA1j-UFsRl6bC2vx0WVJvkntlNoOFTr-ESqt9v_tyg0xYuFFOP1JiVw1zGP2PegWNZSO0OhsrXPXjvZJke9r1ZCA7d7NpvDaCa80JdYTtUsHMEfGfRZ14Dz-QcMwUTlFIrxSfhM7zRpyTJm8fEi5P3R6oG2sODCedJaHNlwqbJqAE4BoggIKdB_yz9n4vwVdNHNHurv-4sTWoLLhGV2z6mb5rYwWnrrPxearn1nCXbGZG9VVB7BEUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مخازن اسلحة المعارضة الايرانية في محافظة السليمانية شمااي العراق لا تتوقف نيرانها</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/naya_foriraq/83663" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83662">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb8d54a56d.mp4?token=UwOTXxaqyzdaDvolAgfCG92hlyBQ_y01aUVuH7O5eo-_GuFE1zRye7UoBD_0Bcoupc_X3FkWpZHujWFkotHCQqW4yx60lq76LnYDlX544iES-_p4GI7yVxoz8VjddcPumTc03-xRnAeVxOAUc_-gNA-4LopMgc2KSkUa0u2oR6P_56TjW-9HuOXS701EWAaPJ9y7YfTb0yyV2odq3FrwMx0OiF3dbm1NFtoU0YWQ06LcbxMrBksr7AQUsmajmK-JaHiic2OQYRjBQNd2jdEoXEV7bEqA35JP69lwKbdeRdhGLBbxTkp_VJkzFfeH9R0igSBBN8fjY5K8Dx_LdhE4yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb8d54a56d.mp4?token=UwOTXxaqyzdaDvolAgfCG92hlyBQ_y01aUVuH7O5eo-_GuFE1zRye7UoBD_0Bcoupc_X3FkWpZHujWFkotHCQqW4yx60lq76LnYDlX544iES-_p4GI7yVxoz8VjddcPumTc03-xRnAeVxOAUc_-gNA-4LopMgc2KSkUa0u2oR6P_56TjW-9HuOXS701EWAaPJ9y7YfTb0yyV2odq3FrwMx0OiF3dbm1NFtoU0YWQ06LcbxMrBksr7AQUsmajmK-JaHiic2OQYRjBQNd2jdEoXEV7bEqA35JP69lwKbdeRdhGLBbxTkp_VJkzFfeH9R0igSBBN8fjY5K8Dx_LdhE4yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النيران لا تتوقف بالارتفاع من مقرات الاحزاب المعارضة في محافظة السليمانية</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/naya_foriraq/83662" target="_blank">📅 21:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83661">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e3aa20dcc.mp4?token=hSAPo6VLmswPfIfYhR5JSTErKXL_YcTzg9JC8OJPGTgUPV7w_IHkIfYiuO-0XgK-M54DY3_4nOUPow0bIDjkXOJTP_Vnaq8tVQZ3_FzlORJTFz5QAmWy7FrfSQXcB1wBzQDwyAUT-bj1S7G03fvNmxSUBsl-jqeVDNeOO450tzAMtp1Oa5AB_ncD_x3FusBBXxSHHJYaq8HVVjYK3g6g-x5jPmjk5Bc0cV1ArqSUF0vZ4RPZh8EZdce9C3Il705wDWnxx6U79kysvlYE6Ydp6Hz9bGtx1IMNd7tO-5iBX2qzvZw2OcX8WWovTwJ0bqL5D8UgcS5fq2zFEGqBphmZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e3aa20dcc.mp4?token=hSAPo6VLmswPfIfYhR5JSTErKXL_YcTzg9JC8OJPGTgUPV7w_IHkIfYiuO-0XgK-M54DY3_4nOUPow0bIDjkXOJTP_Vnaq8tVQZ3_FzlORJTFz5QAmWy7FrfSQXcB1wBzQDwyAUT-bj1S7G03fvNmxSUBsl-jqeVDNeOO450tzAMtp1Oa5AB_ncD_x3FusBBXxSHHJYaq8HVVjYK3g6g-x5jPmjk5Bc0cV1ArqSUF0vZ4RPZh8EZdce9C3Il705wDWnxx6U79kysvlYE6Ydp6Hz9bGtx1IMNd7tO-5iBX2qzvZw2OcX8WWovTwJ0bqL5D8UgcS5fq2zFEGqBphmZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد قريبة تضهر حجم النيران والدمار الذي لحق بمقرات الاحزاب المعارضة ومخازن اسلحتهم</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/naya_foriraq/83661" target="_blank">📅 21:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4be1967b.mp4?token=gJypykShARyy2zh75HQqNsNSK11VqT3YjYxtFKb3JfIf4Xp5KAfKlOCTbIGKX6f00088jKmqBGj5GqenUcmyD7MYpiL4wWuZ5kpGkop8DtU039LVoMXapSb2wseVon9_NRhRuzgGL_xYWeJZPbHibcavEcijhFO7TKXm7sja2hLGmJrwTnSA12-RUdt3wIq8bJOERQkJMFzteSZdysOMQrJwYVHtofiwiC7hVyo51vNSR7HB2wD0v7N_ZG9rV_uj-oDdUfW3e2JncJOYIgZWiaUiW5vkAuQOy-PHcdlN0R-xadnOZSJTEes116OAqvZkeyyOt1F3ZDjQrN3OdiWCISo8uiIUkJtzQLl1K__6kp6M382CUQkrZmwxt4lA8e9q8KEFp3Je6gupvpDFhy5kquAL7LxQxpOFFA9qew3VDZ6LiSn5WDkZQhclnGeZyLmh0ATBR9Ip4x1Pf1nZIo-ADGUkD-y_iIg1NS5HdkonWgcMXJRqtqx0rBQ2JYM71IBkD6kCi7jETHni-I8J-4Qc0UZjiKfOpPNikE2FAZHjeBXw7Crtrn-jiboPFaUxM5QCWq7Dn_BueG50t1GaP5E3a-ZyOGP7YeTvnW1K8ly6GbS2wxua1Gwte01zI0cB5WaYtG7uGsCDPnnohMEWW4J2lCy9cwieRTIdyvtZQczjTAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4be1967b.mp4?token=gJypykShARyy2zh75HQqNsNSK11VqT3YjYxtFKb3JfIf4Xp5KAfKlOCTbIGKX6f00088jKmqBGj5GqenUcmyD7MYpiL4wWuZ5kpGkop8DtU039LVoMXapSb2wseVon9_NRhRuzgGL_xYWeJZPbHibcavEcijhFO7TKXm7sja2hLGmJrwTnSA12-RUdt3wIq8bJOERQkJMFzteSZdysOMQrJwYVHtofiwiC7hVyo51vNSR7HB2wD0v7N_ZG9rV_uj-oDdUfW3e2JncJOYIgZWiaUiW5vkAuQOy-PHcdlN0R-xadnOZSJTEes116OAqvZkeyyOt1F3ZDjQrN3OdiWCISo8uiIUkJtzQLl1K__6kp6M382CUQkrZmwxt4lA8e9q8KEFp3Je6gupvpDFhy5kquAL7LxQxpOFFA9qew3VDZ6LiSn5WDkZQhclnGeZyLmh0ATBR9Ip4x1Pf1nZIo-ADGUkD-y_iIg1NS5HdkonWgcMXJRqtqx0rBQ2JYM71IBkD6kCi7jETHni-I8J-4Qc0UZjiKfOpPNikE2FAZHjeBXw7Crtrn-jiboPFaUxM5QCWq7Dn_BueG50t1GaP5E3a-ZyOGP7YeTvnW1K8ly6GbS2wxua1Gwte01zI0cB5WaYtG7uGsCDPnnohMEWW4J2lCy9cwieRTIdyvtZQczjTAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد قريبة تضهر حجم النيران والدمار الذي لحق بمقرات الاحزاب المعارضة ومخازن اسلحتهم</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/naya_foriraq/83660" target="_blank">📅 21:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83658">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f088c5b1f6.mp4?token=pyOWWfdaqJ3FoYgClGrNKfFLGro7AUFk2ZlPHntryKJqlv4jwvEvLLlbPoqnQZXl4pkHrXzLDf7md8u3JKITXstRKQ6y2Zfq04beckFi1eclNdRWJ2mw7KxIi3q3D469EDX51P6lESpUOlhTdxDSpdfP8nyK4hCEkSddHcM2sIlsjUBYkpgNey39GwcjcwuxLwz5-ozV0R3jkTdPx76wfjyaDAKyuvhwc6dYzY80k9t-RVbkqixya_AMG0SGoh_96S-CwxkmVu81OZmFuCZHo9jCJ-5eVmV6Crx-o07rcjvHPrpdbrEQw898BJGmJHEfkIOzttZnI7PJEnNN3tOMxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f088c5b1f6.mp4?token=pyOWWfdaqJ3FoYgClGrNKfFLGro7AUFk2ZlPHntryKJqlv4jwvEvLLlbPoqnQZXl4pkHrXzLDf7md8u3JKITXstRKQ6y2Zfq04beckFi1eclNdRWJ2mw7KxIi3q3D469EDX51P6lESpUOlhTdxDSpdfP8nyK4hCEkSddHcM2sIlsjUBYkpgNey39GwcjcwuxLwz5-ozV0R3jkTdPx76wfjyaDAKyuvhwc6dYzY80k9t-RVbkqixya_AMG0SGoh_96S-CwxkmVu81OZmFuCZHo9jCJ-5eVmV6Crx-o07rcjvHPrpdbrEQw898BJGmJHEfkIOzttZnI7PJEnNN3tOMxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اللسنة اللهب لا تتوقف من مقرات الاحزاب المعارضة في محافظة السليمانية</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/naya_foriraq/83658" target="_blank">📅 21:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83654">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fe5033579.mp4?token=wCBlcjJlOwfhSCeDeLGpl0KsSg1lYt5tFvXrvk3Jat2lTxcgWu_K1vzTNSYkOTNX4qeyU1rKVj5jyJAFnKjW01FomF31jxB_0TLZumt76GoiYETayrjPNanBn2c9bhyQvN4tU2OWIASuWBU68WxgKAdYTASogD_QaArBaQm31uBj_0sScnPFSVIUd3lyS5fVDfp79NI5glvL78O_nOE8T7jVkwmFoBoU6pf-Lpf2yrWo82e7Cb6VazY_GsUXOQd24NK5t-5s0mNt-y2zEhL8PlW2B1vZVqGdAR7_-iGxk2u40FOW0a3XCcn7TG3DCrRRKSaR_OlVcAzi_WzwYRH9ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fe5033579.mp4?token=wCBlcjJlOwfhSCeDeLGpl0KsSg1lYt5tFvXrvk3Jat2lTxcgWu_K1vzTNSYkOTNX4qeyU1rKVj5jyJAFnKjW01FomF31jxB_0TLZumt76GoiYETayrjPNanBn2c9bhyQvN4tU2OWIASuWBU68WxgKAdYTASogD_QaArBaQm31uBj_0sScnPFSVIUd3lyS5fVDfp79NI5glvL78O_nOE8T7jVkwmFoBoU6pf-Lpf2yrWo82e7Cb6VazY_GsUXOQd24NK5t-5s0mNt-y2zEhL8PlW2B1vZVqGdAR7_-iGxk2u40FOW0a3XCcn7TG3DCrRRKSaR_OlVcAzi_WzwYRH9ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة استهداف مقرات ومخازن اسلحة المعارضة الايرانية في محافظة السليمانية</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/naya_foriraq/83654" target="_blank">📅 21:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83653">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e1dab5ac.mp4?token=B9jLbzwiHAykhGhUzB2pRbXVuwZf-ZUiEqSFx7hOGZujPilahKvz6Q4AobzhAgDphq78QyQvECod3H-RwbOQpA6XjkEkFor3dkGMGTwXrPNicQZmbnR5Ig9paG7MVcZ8DqdeOpR_IrTBXIhHdH1fZgThb41B9GBekLSiGJqHpPiJgGrd5yoOCy6SWJYUDW4HbZcZeqaziye1mpSbjueI8tfYTh6zXPZj-FAQpssPuCtOPmvIm2BVEBL6l_eez3KQUAkl_WYYjbgHA69ny__BBl-L4VAHoe_-A8frXz8OdGQmXyP0sfKpzo7QsoDhHkHgIEYyViVURC8QfU0ZNJiV9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e1dab5ac.mp4?token=B9jLbzwiHAykhGhUzB2pRbXVuwZf-ZUiEqSFx7hOGZujPilahKvz6Q4AobzhAgDphq78QyQvECod3H-RwbOQpA6XjkEkFor3dkGMGTwXrPNicQZmbnR5Ig9paG7MVcZ8DqdeOpR_IrTBXIhHdH1fZgThb41B9GBekLSiGJqHpPiJgGrd5yoOCy6SWJYUDW4HbZcZeqaziye1mpSbjueI8tfYTh6zXPZj-FAQpssPuCtOPmvIm2BVEBL6l_eez3KQUAkl_WYYjbgHA69ny__BBl-L4VAHoe_-A8frXz8OdGQmXyP0sfKpzo7QsoDhHkHgIEYyViVURC8QfU0ZNJiV9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/naya_foriraq/83653" target="_blank">📅 21:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83652">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/naya_foriraq/83652" target="_blank">📅 21:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83651">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff35d068f8.mp4?token=KXdux8YDfSL1mvjtIwRYwQ5TJxm9-IzKiel7Zir0BGGMEE46BlsFGDvXczbiFC9f077LNt6U_2wXz1HqjdwKgy8UaMRwbM7EziH_cDnp_kScnNgTdJudwL4tz1qsohxGfNo0BoZaZN_3esN0lGenRVpGnUaa2Jy6x5fFuFJsWXoMv0R8J0WnoAIypX1-9tCnKmaM6aZ8DWru_yNZdLeb1CgVO0n4Dx6Gkb5JchU7QmkJDSuaDb7Dnf1j2VbzViEUetyC_t-6jxTlRVYAk62_3Hazhl0iOi3G5ZMqlpoePqTaGkMX7porwBvWDb8VA_fet0Hw25cLRbBqIYS6A8yCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff35d068f8.mp4?token=KXdux8YDfSL1mvjtIwRYwQ5TJxm9-IzKiel7Zir0BGGMEE46BlsFGDvXczbiFC9f077LNt6U_2wXz1HqjdwKgy8UaMRwbM7EziH_cDnp_kScnNgTdJudwL4tz1qsohxGfNo0BoZaZN_3esN0lGenRVpGnUaa2Jy6x5fFuFJsWXoMv0R8J0WnoAIypX1-9tCnKmaM6aZ8DWru_yNZdLeb1CgVO0n4Dx6Gkb5JchU7QmkJDSuaDb7Dnf1j2VbzViEUetyC_t-6jxTlRVYAk62_3Hazhl0iOi3G5ZMqlpoePqTaGkMX7porwBvWDb8VA_fet0Hw25cLRbBqIYS6A8yCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لتطافر الصواريخ والذخيرة بعد استهداف مخزن للاسلحة في محافظة السليمانية تابع للمعارضة الايرانية</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/naya_foriraq/83651" target="_blank">📅 21:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83648">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dbb3d9cae.mp4?token=RHyDAyvOrgzWfIhHTQfyl5s9uCRDe1sFcUrvznCeA1PcT_VIj6sMj56gqns0ngmYng69gV3KKd8LnVfXMas8QolCik027F5bLFqS-3tWKH2i_zOwBVhE4o_MAg79itQB0kzxlBH8DI6VNXK3daDbD6KgGbdzA-fEkvfktoI7v3DK-DzVdn__z5uYci8Kum4zIo5sGf9agZO01ZR_rjmv6pWpxTj7NTjxjZ_0jDoGm5RVFqFH5cMsE9QBfZTzGevRB8TmMnHKA83jC90Q7ZbAlkveVSY-BT-kka-pRzKeYiL_z35Zn3a1aIIrLYFxtbyTAf2V85IdTpru3PZ8RoOyxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dbb3d9cae.mp4?token=RHyDAyvOrgzWfIhHTQfyl5s9uCRDe1sFcUrvznCeA1PcT_VIj6sMj56gqns0ngmYng69gV3KKd8LnVfXMas8QolCik027F5bLFqS-3tWKH2i_zOwBVhE4o_MAg79itQB0kzxlBH8DI6VNXK3daDbD6KgGbdzA-fEkvfktoI7v3DK-DzVdn__z5uYci8Kum4zIo5sGf9agZO01ZR_rjmv6pWpxTj7NTjxjZ_0jDoGm5RVFqFH5cMsE9QBfZTzGevRB8TmMnHKA83jC90Q7ZbAlkveVSY-BT-kka-pRzKeYiL_z35Zn3a1aIIrLYFxtbyTAf2V85IdTpru3PZ8RoOyxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات لا تتوقف من داخل مقرات الاحزاب المعارضة في محافظة السليمانية</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/naya_foriraq/83648" target="_blank">📅 21:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83647">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f71242c684.mp4?token=VRH5_ImbcFxGhRPHPkR65AOXxJy5IjP1RAfrOiNItRw54Dy8NXNlAMTJaD8by0EX3UuiNo4-33RUzgiKG_jS9dx1-Th770YZgr9DdtPaLgpetBhgcMvobgDKRu1-sOt5i13t1RGWdp8bb-SVKrcKNzDfwp9Dk7nL61YVFrb5NJqWsLFe8hF2zWMvNWWDMOsxhfsDZEzxResvElBn4Jq66HrqySTwSEFaUGHHEzJQESw9156rRZ31kRKr_aZHtLypjcjlx_HRJ385KlxybzHrm19Kx3mRKDsSuMBIQX-vHSMUSjsL6ZBA6scdw-SVXGMyaER4ZTHl5k3u_7O1e6JAAQGGE7HkBc1GDhpUQ45NGTuTfm9dUjbqtELmVeHEXtu_SWx8ZphcGAMczCGWqV3AEsswI2CVItMikvY5AKa6cLf1xgP7H8JlOU-rhHtLVZJZZALC6MMSEKJ12hZOwQaO-4U9TEflAHK-1A598Oj2h6AliwnMupuK058IHH0M9TyAjco2oNd4QbnMNMoPqEL1KofWEyQPmeLlhobp8vWzkvws79kvcH1bHLiw0MGdwsVuXah4hRYagti2BOiAZr_-zT6QXU-0FtUHsA4jF7tUPNE0bkYznWG2jYJZHmODjd5qrHbbWMUuvSAzzNjOjZm9dFnv-sOC_r25mz-fyTZLr9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f71242c684.mp4?token=VRH5_ImbcFxGhRPHPkR65AOXxJy5IjP1RAfrOiNItRw54Dy8NXNlAMTJaD8by0EX3UuiNo4-33RUzgiKG_jS9dx1-Th770YZgr9DdtPaLgpetBhgcMvobgDKRu1-sOt5i13t1RGWdp8bb-SVKrcKNzDfwp9Dk7nL61YVFrb5NJqWsLFe8hF2zWMvNWWDMOsxhfsDZEzxResvElBn4Jq66HrqySTwSEFaUGHHEzJQESw9156rRZ31kRKr_aZHtLypjcjlx_HRJ385KlxybzHrm19Kx3mRKDsSuMBIQX-vHSMUSjsL6ZBA6scdw-SVXGMyaER4ZTHl5k3u_7O1e6JAAQGGE7HkBc1GDhpUQ45NGTuTfm9dUjbqtELmVeHEXtu_SWx8ZphcGAMczCGWqV3AEsswI2CVItMikvY5AKa6cLf1xgP7H8JlOU-rhHtLVZJZZALC6MMSEKJ12hZOwQaO-4U9TEflAHK-1A598Oj2h6AliwnMupuK058IHH0M9TyAjco2oNd4QbnMNMoPqEL1KofWEyQPmeLlhobp8vWzkvws79kvcH1bHLiw0MGdwsVuXah4hRYagti2BOiAZr_-zT6QXU-0FtUHsA4jF7tUPNE0bkYznWG2jYJZHmODjd5qrHbbWMUuvSAzzNjOjZm9dFnv-sOC_r25mz-fyTZLr9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النيران تلتهم مقرات الاحزاب المعارضة بعد استهدافها بمسيرات انقضاضية</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/83647" target="_blank">📅 21:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83646">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50736415a0.mp4?token=n6gOR2GIPRISpR18k4q-y8ESm7P4w6EcvgzEk4PK5wOsr3nVv8wvpm4CLOjF7yfOX5y3zEJaDw8sxjQOEvEZZfOed_70WUM_DDdzaMzGN8gAXv-0VAMmvrdTW4EZ424welWDbhz_jvp-bLBJ7rylqIq765d3EM-u1R1Dbw9lbgEoVc6L0cmFEZPuht4ipwCM6o7OEKXNa_5QkVWKC4lCsBcihujd59WAJBzKcwDWfIUuLatyncdV5lOKSnwq0d_NvcqLzEjkMavJGSj34JyoXhkrbNycHYVdI4t7bmoas3xN08x1unghFuFSvu0_lvY5YaMIV0X5jq7AU4I5FeZ9_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50736415a0.mp4?token=n6gOR2GIPRISpR18k4q-y8ESm7P4w6EcvgzEk4PK5wOsr3nVv8wvpm4CLOjF7yfOX5y3zEJaDw8sxjQOEvEZZfOed_70WUM_DDdzaMzGN8gAXv-0VAMmvrdTW4EZ424welWDbhz_jvp-bLBJ7rylqIq765d3EM-u1R1Dbw9lbgEoVc6L0cmFEZPuht4ipwCM6o7OEKXNa_5QkVWKC4lCsBcihujd59WAJBzKcwDWfIUuLatyncdV5lOKSnwq0d_NvcqLzEjkMavJGSj34JyoXhkrbNycHYVdI4t7bmoas3xN08x1unghFuFSvu0_lvY5YaMIV0X5jq7AU4I5FeZ9_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الانفجارات لا تتوقف من داخل مقرات الاحزاب المعارضة</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/83646" target="_blank">📅 21:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83645">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e581e4880.mp4?token=eGHY8B-MZcYbGPDkmtvcsV_fe721JtZX14gxPKlf2QvII63ve-69JzuaxKb8yO0n4URIYmuaMJJNiFgfV3Zs6LTjqiw5wKBF8W_sXQM6zVf3BE-1RuY1qplnkjquvWa9ucE8NRIlQMUAFwx8TAXu5lNyVgmUh2gOAF9AcqZBbppGrx6nQ3pqetMvGmFpLjmRalHvu9kOkJtDlbFvOS0BdZ8p5xjpDkd1nyhqtudTOGUksjaipPgYM8krFlvkl89kv2exY22BZ6mVnNlRwNIGHB_TD07TBHW3oYBmr8vQJ7fJbN3r97uS1yUO53nUoHUVqR9IbSHk6EoeiNBfImKE0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e581e4880.mp4?token=eGHY8B-MZcYbGPDkmtvcsV_fe721JtZX14gxPKlf2QvII63ve-69JzuaxKb8yO0n4URIYmuaMJJNiFgfV3Zs6LTjqiw5wKBF8W_sXQM6zVf3BE-1RuY1qplnkjquvWa9ucE8NRIlQMUAFwx8TAXu5lNyVgmUh2gOAF9AcqZBbppGrx6nQ3pqetMvGmFpLjmRalHvu9kOkJtDlbFvOS0BdZ8p5xjpDkd1nyhqtudTOGUksjaipPgYM8krFlvkl89kv2exY22BZ6mVnNlRwNIGHB_TD07TBHW3oYBmr8vQJ7fJbN3r97uS1yUO53nUoHUVqR9IbSHk6EoeiNBfImKE0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متواصلة في مستودعات الذخيرة للاحزاب المعارضة في محافظة السليمانية</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/naya_foriraq/83645" target="_blank">📅 21:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83644">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجارات متواصلة في مستودعات الذخيرة للاحزاب المعارضة في محافظة السليمانية</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/naya_foriraq/83644" target="_blank">📅 21:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83642">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce162465IVvBymmqeb0GHtIzatyCpZD93JFm6153_JEcGcDDZ0-tuEY4P7bOrpywZCy3bMof3kQU4KOGf1ex64Lpmc2Y_2hgIF5L6MeZ_CS6z59ndkcpGByGyjCXzP3BWhrz5EXhRPFKRPG4XFw8j7lMzmQtLRvh0iK8rU1HjDgciGFHP10oKXrtw7k98rXIno8MkkdV3IsEs75enaLRIF7YefrcuOT6ZFzoHxQd0z2W5S77TEj3ZWEdwjpfpA89_emtzbx6yGFj0a9Ds8AiJmgRwu2PgqQe5ku7iMJdg6qsv_CVokYnYxmJX9U7Gu1L5a62TbH4_Lv3dZDW8_-TcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e5d05971b.mp4?token=CwFkkohQb9mSncrWNFSgi7w7xc4WWUUcyZmFNKI47q3w9AldWK3xFNboBPaOpnCKyHuBpEwmPDCGb9OgMapUuHprX8xnN6m8BxR5HkF1CvRX6CUhiAOqA5kWuozCVIG8QjO5Epu_QAsOmVeGKfi6xk-16jVNxSyM0l-gp8QPlKoyGSzVdTcykqBHdZdCwAzh9V_IJSs3jSrGx1FJ_8f6c00tz_LI-OjOVQ-tQRXFePQyW6qxbBukA_a7rs2RVOMMRIIcK5--LMxQuaB4rj-p0gjd3eAEHPMgsTlQtoxGICY8SgQvWXfT6CutZBqlV71zc_sGicwxZjDgazsR6Ey5OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e5d05971b.mp4?token=CwFkkohQb9mSncrWNFSgi7w7xc4WWUUcyZmFNKI47q3w9AldWK3xFNboBPaOpnCKyHuBpEwmPDCGb9OgMapUuHprX8xnN6m8BxR5HkF1CvRX6CUhiAOqA5kWuozCVIG8QjO5Epu_QAsOmVeGKfi6xk-16jVNxSyM0l-gp8QPlKoyGSzVdTcykqBHdZdCwAzh9V_IJSs3jSrGx1FJ_8f6c00tz_LI-OjOVQ-tQRXFePQyW6qxbBukA_a7rs2RVOMMRIIcK5--LMxQuaB4rj-p0gjd3eAEHPMgsTlQtoxGICY8SgQvWXfT6CutZBqlV71zc_sGicwxZjDgazsR6Ey5OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق لا تتوقف وانفجارات في مستودع الذي يضم ذخيرة المعارضة الايرانية في محافظة السليمانية</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/naya_foriraq/83642" target="_blank">📅 21:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83641">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3c777ffb.mp4?token=W22UAgPGXU8gRGwV1WzzkdNL1F5R8_eEnTHP919zggHsMoJFLR4nRevNkDnb42QqoqRqgExzGq81D-Y8mqTfvcIxcdKUhDXdwd1LyVnDpHCABZ3RRs2UEzTmPSYWD5vFNEzxNV7PU_SOLRh_bRzXDb-KuMfB-SMJ6Ons4RrVNMBKZjiFFDY5_YsxVJBpm86C6cFzVEk4F-MInRoJkf7WBJeyTwUXAp9dlrALaql0YhR5i12pcuRRWQTRu_OeOmdhH_eiwPwq9JBEEUcWFejRt-mwpjKsXBKvkEz5NQXs1-uai5GA26Ueb5sbhk5pI3a60tMZ87-I66kxkpk1WvDduQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3c777ffb.mp4?token=W22UAgPGXU8gRGwV1WzzkdNL1F5R8_eEnTHP919zggHsMoJFLR4nRevNkDnb42QqoqRqgExzGq81D-Y8mqTfvcIxcdKUhDXdwd1LyVnDpHCABZ3RRs2UEzTmPSYWD5vFNEzxNV7PU_SOLRh_bRzXDb-KuMfB-SMJ6Ons4RrVNMBKZjiFFDY5_YsxVJBpm86C6cFzVEk4F-MInRoJkf7WBJeyTwUXAp9dlrALaql0YhR5i12pcuRRWQTRu_OeOmdhH_eiwPwq9JBEEUcWFejRt-mwpjKsXBKvkEz5NQXs1-uai5GA26Ueb5sbhk5pI3a60tMZ87-I66kxkpk1WvDduQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمس انفجارات في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/83641" target="_blank">📅 21:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83640">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/naya_foriraq/83640" target="_blank">📅 21:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83639">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجارات في محافظة السليمانية شمالي العراق وارتفاع اللسنة اللهب في مقرات الاحزاب المعارضة</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/naya_foriraq/83639" target="_blank">📅 21:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83638">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade0f0b606.mp4?token=b_a6xslhwyF-7B2IOkVCygqxs_UpPd3ARrHX8CO7PAd8wYHxd_CO-bYqM39uGepm1YEnYUBsbpwUBFHCqGb7IpdwJvyDlWoBcR30eI03Pgbz8ciGx0TfeBNt79vvj5L8qwWwPUca1618D0YkUltw40EK18gRBTMmqwx-2_g61gfYFgeupQq4N14-7FKlDrh37Q9PJXX11-6FF43EZ8ZEA1WEZQgjxHUp9KBXMrXfgUyXbXynzxxPY9If-gBp5AZIIn3_Hjz1ARV6Vtre2cMmIcDs-gfHSedNV7aZuDwXaptESoFGiNC_XirmW-0ODBhnFb9uQkFEm9Qi6MVBv1UnnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade0f0b606.mp4?token=b_a6xslhwyF-7B2IOkVCygqxs_UpPd3ARrHX8CO7PAd8wYHxd_CO-bYqM39uGepm1YEnYUBsbpwUBFHCqGb7IpdwJvyDlWoBcR30eI03Pgbz8ciGx0TfeBNt79vvj5L8qwWwPUca1618D0YkUltw40EK18gRBTMmqwx-2_g61gfYFgeupQq4N14-7FKlDrh37Q9PJXX11-6FF43EZ8ZEA1WEZQgjxHUp9KBXMrXfgUyXbXynzxxPY9If-gBp5AZIIn3_Hjz1ARV6Vtre2cMmIcDs-gfHSedNV7aZuDwXaptESoFGiNC_XirmW-0ODBhnFb9uQkFEm9Qi6MVBv1UnnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع اعمدة الدخان من مقرات الاحزاب المعارضة في محافظة اربيل</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/83638" target="_blank">📅 21:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83637">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d0dd0ff4.mp4?token=Rwc4rrHyXTw2q3EFBzn_YksXmzOV_ei2mfQijJcDVPxekvcg65KqYP7mL_VKJIj1RLO0Rwt5aCBYYruzFFLziIodc4nqOk7csaLQZPdGoaJlYljgNEXoXkAtXdN4OIW4hoDo766ePOPqOdCTizl3TLKEZYVgF9UA60p4zvzspEi0mQDrrlUScjdu5lvbAIdo-QCGe_l167_FfBiX-ZVyid81ot_iooR6zAIyp5VpUmKGDjuBylBhAXDuHVn7D1xP_04epwrVuqdiqqoBY8qZ6UWCNQaJKfGJpJ4rNrM7cPC4pSSpplbUNlsPvyVnkIBooSnyaADxAflZA_Jocyn_kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d0dd0ff4.mp4?token=Rwc4rrHyXTw2q3EFBzn_YksXmzOV_ei2mfQijJcDVPxekvcg65KqYP7mL_VKJIj1RLO0Rwt5aCBYYruzFFLziIodc4nqOk7csaLQZPdGoaJlYljgNEXoXkAtXdN4OIW4hoDo766ePOPqOdCTizl3TLKEZYVgF9UA60p4zvzspEi0mQDrrlUScjdu5lvbAIdo-QCGe_l167_FfBiX-ZVyid81ot_iooR6zAIyp5VpUmKGDjuBylBhAXDuHVn7D1xP_04epwrVuqdiqqoBY8qZ6UWCNQaJKfGJpJ4rNrM7cPC4pSSpplbUNlsPvyVnkIBooSnyaADxAflZA_Jocyn_kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
دوي انفجارات في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/83637" target="_blank">📅 21:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83636">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
دوي انفجارات في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/83636" target="_blank">📅 20:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83635">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
الولايات المتحدة تعيد طائرات مقاتلة من أوروبا إلى الشرق الأوسط.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/83635" target="_blank">📅 20:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83634">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d684ca866.mp4?token=rGhImTzMlgzXa-poGqlBZ68LTsMbZuNZ960vB0T8sErYhsPJqJpIIlqTfdXqy9np8s_Vd9-4WZPp7XM0TnHGdJWgqqAxKKI4s-W1efpOIzU9aFNbmUctC_JFPMnBs8cL03gzQae8t99YvWhteduW2KSTz1nxNaZ0vMFSQTxBQcxV5OYtoxSmL6CW6Dm06VbmXvZM406SZx9PuztRGVNEaz-psjWToO6xtX4ol0wU-xXT7v1_RY3iuanM6fkPfV1o1iOrZFRTa2G16TAQrX9G5exkVXK4tplJzvYO6heoozyS04WmIg1uw3DjZhF-kVu5B1k12u3qqXL3B00h2Fn-Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d684ca866.mp4?token=rGhImTzMlgzXa-poGqlBZ68LTsMbZuNZ960vB0T8sErYhsPJqJpIIlqTfdXqy9np8s_Vd9-4WZPp7XM0TnHGdJWgqqAxKKI4s-W1efpOIzU9aFNbmUctC_JFPMnBs8cL03gzQae8t99YvWhteduW2KSTz1nxNaZ0vMFSQTxBQcxV5OYtoxSmL6CW6Dm06VbmXvZM406SZx9PuztRGVNEaz-psjWToO6xtX4ol0wU-xXT7v1_RY3iuanM6fkPfV1o1iOrZFRTa2G16TAQrX9G5exkVXK4tplJzvYO6heoozyS04WmIg1uw3DjZhF-kVu5B1k12u3qqXL3B00h2Fn-Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
تدمير موقعين داخل قاعدة الشيخ عيسى الجوية في البحرين إثر ضربتين بصاروخين إيرانيين.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/83634" target="_blank">📅 20:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83633">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1x80uOt8s9tofmnW3O5kyPWXEEQGDWQFhpN6Kvxx9Q-JEDXQE4hZRIPtfU1PFigsNx5FITL_5ors4Evo3_GlbkFUfB5zWe1H728ITgs4ciyaFOxxI0jB5D8ysByWTTNNFn8YBlvFe3iS0TZQECHRJImJIqMPOqn8J2H8OzQ6azzBY-jR_LJaor4izmiznE-CPTBEzsvFFTK9f5ZqrT-ZkkG8lnmQXwpLYbpG7bR7-wC1rp0ee4MmiwZe_TVlkYHWmyFNJIajHaqJAU8M3Wq-1Il7XSMpjdpFcvuuantVZ1ONV1IDMsAKwXWkzQYyqXcaqXX93ZdGvnun33q-dDcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الأمريكية في بغداد تشيد بزيارة الزيدي ولقائه في هيوستن شركات الطاقة لتحقيق هيمنة امريكا في مجال الطاقة</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83633" target="_blank">📅 20:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83632">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6cbb7713.mp4?token=RSvesRsSK33rOIoi2OXt3sLh6dQ-bbwNKpuLWmyYuDDvshJ4JTOIPahN2LkDZBmmzCASK8imF8Vc5th8NcuRWnJ-s5aosCMdSw3Dy2ZTPznm9TZIpIOC0WxQzsX6-IaXy7Zv5OCz7C05rJLz8x3VV3N4HVomoUyy5_w9M4SrkICs34nTAXbr1BAbYf6_V-yIkJ3-iGVqKuzE4XpB8LLWS9_rnPWkgJW0QTKcQknrd9HjUdrl_XlTvq4Vwu3U2fSslL65zEgRv029JTBJmLhi9DhPy4vkg0wgSI_5Ql_b_atO0dhct3ECaaYdn3C8Vj0eiFkNxPG6VcQe84BNYO2MFmTMY5llTT8TPv_A7i0GeXz2y0wamefb2aiInPhbCK6fVEqifMSjljg3XJoc_FBdbUhr5MNCgRa9_6hQ1EDEzZr8gbt7CzkDSv0erm54adjHY_34fSWpeoNmi5tp4gDf2HRpOkaK6s-qPAc3JJMh-8QTkEgjdGBLAD5AMYVHCRQcowfEDJKmvKx65WrKaOSKKddL341GSeptn50maPxZRyup_JKykovLsopc-kAh7cai-DWdNlNQPWRcQGssbc2Mo7tssYDfRm7NlmOyvQOPkENqvjKcHCrFAP7o-UCruNbH15RlAlm9LyLYFUrG0XHYZ-0gGqyQGdc60Rw-rMGoAeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6cbb7713.mp4?token=RSvesRsSK33rOIoi2OXt3sLh6dQ-bbwNKpuLWmyYuDDvshJ4JTOIPahN2LkDZBmmzCASK8imF8Vc5th8NcuRWnJ-s5aosCMdSw3Dy2ZTPznm9TZIpIOC0WxQzsX6-IaXy7Zv5OCz7C05rJLz8x3VV3N4HVomoUyy5_w9M4SrkICs34nTAXbr1BAbYf6_V-yIkJ3-iGVqKuzE4XpB8LLWS9_rnPWkgJW0QTKcQknrd9HjUdrl_XlTvq4Vwu3U2fSslL65zEgRv029JTBJmLhi9DhPy4vkg0wgSI_5Ql_b_atO0dhct3ECaaYdn3C8Vj0eiFkNxPG6VcQe84BNYO2MFmTMY5llTT8TPv_A7i0GeXz2y0wamefb2aiInPhbCK6fVEqifMSjljg3XJoc_FBdbUhr5MNCgRa9_6hQ1EDEzZr8gbt7CzkDSv0erm54adjHY_34fSWpeoNmi5tp4gDf2HRpOkaK6s-qPAc3JJMh-8QTkEgjdGBLAD5AMYVHCRQcowfEDJKmvKx65WrKaOSKKddL341GSeptn50maPxZRyup_JKykovLsopc-kAh7cai-DWdNlNQPWRcQGssbc2Mo7tssYDfRm7NlmOyvQOPkENqvjKcHCrFAP7o-UCruNbH15RlAlm9LyLYFUrG0XHYZ-0gGqyQGdc60Rw-rMGoAeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
لجأت السلطات في محافظة البصرة جنوبي العراق إلى بذور هولندية هجينة لزراعة حزام أخضر على طول الحافة الشمالية الغربية للمدينة النفطية العراقية، سعياً منها لتلطيف حرارتها.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83632" target="_blank">📅 20:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83631">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163aae010f.mp4?token=c-s_anDeHIlkyCXRMH2f41gRixXYqwbki0Qrrm7j2-w--jujJz8fFiNUR5ccViyvG8NkWYN8efpWmad_0YhNBhtoA7Gjkc53wRUhE26LIFmChj68D7HUuPKS3u_ahRZo1tVb6pyXIpOC9k010Ifrxwj37dpasKig4ozPiDZIDkbEmYBzL-guQuW-8TZ_NXiGu3OA10miFAVqBco_JDp5NG8AAJyctsUYP5wN2L3Bo9qDU9umUBUkRKxRGXJkMlduhRRalkODR1VXhdBWRRFrdgXvmSDX0zkM0ChnRP3Vx-KEs0zzJmb8LIWchzmUcSIM5rf8W_L_jrt-6yvFJlUptw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163aae010f.mp4?token=c-s_anDeHIlkyCXRMH2f41gRixXYqwbki0Qrrm7j2-w--jujJz8fFiNUR5ccViyvG8NkWYN8efpWmad_0YhNBhtoA7Gjkc53wRUhE26LIFmChj68D7HUuPKS3u_ahRZo1tVb6pyXIpOC9k010Ifrxwj37dpasKig4ozPiDZIDkbEmYBzL-guQuW-8TZ_NXiGu3OA10miFAVqBco_JDp5NG8AAJyctsUYP5wN2L3Bo9qDU9umUBUkRKxRGXJkMlduhRRalkODR1VXhdBWRRFrdgXvmSDX0zkM0ChnRP3Vx-KEs0zzJmb8LIWchzmUcSIM5rf8W_L_jrt-6yvFJlUptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
انخفضت حركة الملاحة في مضيق هرمز إلى 8 عمليات عبور في 16 يوليو، وهو أدنى مستوى خلال ثلاثة أسابيع، مع تركّز معظم العبور عبر المسار الإيراني واستمرار تراجع النشاط الملاحي.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83631" target="_blank">📅 20:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83630">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
الولايات المتحدة تُبلغ إسرائيل بأنها سترسل عشرات الطائرات الإضافية للتزود بالوقود إلى البلاد، وذلك في إطار استعدادات محتملة لتوسيع العمليات العسكرية ضد إيران.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83630" target="_blank">📅 19:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83629">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c172eb3bd0.mp4?token=YPnmcDOF91vSz7k5_pox7Y10ubwpsCcQ4C2oGRhZcbRzPefyZiVDYUCjOxu3E6lywtQTK1icfmGgzeGFP2vnrAfJVOgQQzxEurxC_DBHzKzw98-Yb0ABJg3B2bW8Wf23bSga2J2C8UKSNPH3hMdHvHtPZXBZetPPW-DQrCFmO-5BYZr9I2MevEohQRDC2FDdxi7bNHl6TbH5o0Bv93ZQ4mV5xoKlNILtlUAaKS31JfPuB7565Fd-WtsihPpMkeg7sv-qirast6B10GTWrJv_7-YUjdrjrA0Cnt_-ivonblomBfbE87m31dNJN4ljMy42chCkUvs_iTa8Wcht7XC49g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c172eb3bd0.mp4?token=YPnmcDOF91vSz7k5_pox7Y10ubwpsCcQ4C2oGRhZcbRzPefyZiVDYUCjOxu3E6lywtQTK1icfmGgzeGFP2vnrAfJVOgQQzxEurxC_DBHzKzw98-Yb0ABJg3B2bW8Wf23bSga2J2C8UKSNPH3hMdHvHtPZXBZetPPW-DQrCFmO-5BYZr9I2MevEohQRDC2FDdxi7bNHl6TbH5o0Bv93ZQ4mV5xoKlNILtlUAaKS31JfPuB7565Fd-WtsihPpMkeg7sv-qirast6B10GTWrJv_7-YUjdrjrA0Cnt_-ivonblomBfbE87m31dNJN4ljMy42chCkUvs_iTa8Wcht7XC49g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تُظهر صور الأقمار الصناعية مزيدًا من الدمار الذي لحق بمستودع في ميناء عبد الله بالكويت، في أعقاب غارات سابقة شنتها طائرات إيرانية بدون طيار. واكدت إيران أن المنشأة المستهدفة تابعة لشركة كي جي إل للخدمات اللوجستية.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83629" target="_blank">📅 19:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83628">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
مصدر بالحرس الثوري لنايا
نفّذ عناصر اللواء 65 للقوات الخاصة المحمولة جوًا في جيش الجمهورية الإسلامية الإيرانية، خلال الحرب التي استمرت أربعين يومًا، 11 عمليةً خارج الحدود في إقليم كردستان، أسفرت عن تحييد 8 من القادة العملياتيين للجماعات الكردية الانفصالية، إضافةً إلى تدمير ثلاثة معسكرات ومقرات عملياتية تابعة لها.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/83628" target="_blank">📅 19:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83627">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5552eed251.mp4?token=f2lDDzEja_HblsuErc2W8xA-7YSjRQiifVvf5LwwOeeL7wRRAlaFKrZLNdfPp0Izli6SjHt556rfEX85Hdb9bcnkqcHa6kC5eUCxNTJVuxsJCEV3PMqQMI4GdfjpNObFFm7_rF3W-4PQ0yqVIlNhtznYDn86Jzm-VSPtLC3MCPitSN7RF4Dq_jpAdnc_z_gaDw7QKwg_F2_TgFqVdYKnJG6uSCpOhqy3dkq-eaWroQtHCmMhZFT0bii7c42_VJL7pR7U0szoH36OGE9D8rmy_x096yZFm-FqPXXuLQMsm3D36Hs69V_jCrlSJC5rL9xJ0LGyp_JeBoTUSju2NtBGcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5552eed251.mp4?token=f2lDDzEja_HblsuErc2W8xA-7YSjRQiifVvf5LwwOeeL7wRRAlaFKrZLNdfPp0Izli6SjHt556rfEX85Hdb9bcnkqcHa6kC5eUCxNTJVuxsJCEV3PMqQMI4GdfjpNObFFm7_rF3W-4PQ0yqVIlNhtznYDn86Jzm-VSPtLC3MCPitSN7RF4Dq_jpAdnc_z_gaDw7QKwg_F2_TgFqVdYKnJG6uSCpOhqy3dkq-eaWroQtHCmMhZFT0bii7c42_VJL7pR7U0szoH36OGE9D8rmy_x096yZFm-FqPXXuLQMsm3D36Hs69V_jCrlSJC5rL9xJ0LGyp_JeBoTUSju2NtBGcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
الخارجية القطرية:
دولة قطر تحتفظ بحقها الكامل في الرد على اعتداءات إيران وفقا لأحكام القانون الدولي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83627" target="_blank">📅 19:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83626">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3kPp1eRM2vPiA17m6x7W5SxB5EtX2ogqIRzNDWBPDHEwt670KU_42-BcHjnLY5CuJA89wTet_VBfvdVkfPOt5AtAIIOLQTaFhk63--7eARgiTyvaAqyuk6IIRikWNAFfelcrc42NOflOirzjK6Ry-5qDJfJdzJypHB6Qyx0RUKRb_9gud4rishQAkQrKucUXftc01xS3qiU_ziF-cgQPqBdp5CTB19g3BAoeJpcZbSLd0ZRbELqGsCZW7gU9-diny4Q6V24jCiTEKx_MXsLPEHzmGVIoDW2rxHOCP8kgDc4EZK4USeR-UIFoMwzwOpTfMw-NI3APwfWExabhhXifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الكويت تبدأ حملة ترشيد الكهرباء بسبب الضربات الصاروخية الإيرانية الأخيرة ..</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/83626" target="_blank">📅 19:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83625">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">زلزال بقوة 7.4 درجة يضرب منطقة 71 كيلومترًا غرب غرب بويرتو ماديرو بالمكسيك</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83625" target="_blank">📅 18:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83624">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
‏
القيادة المركزية الأمريكية تزعم:
تدمير برج المراقبة بميناء شهيد كلانتري في تشاه بهار، وهو جزء من شبكة مراقبة بحرية على طول ساحل خليج عُمان.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83624" target="_blank">📅 18:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83623">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">العراق يطالب سوريا بتسليمه السائق الذي اعتقلته عصابات الجولاني بتهمة التهريب</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/83623" target="_blank">📅 17:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83622">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شركة "كونوكو فيليبس" الأمريكية تستحوذ على 42% من حصة شركة "بي بي" البريطانية في اربعة حقول نفطية عراقية</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/83622" target="_blank">📅 17:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83621">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شركة سي بي سي:
ناقلة النفط المستأجرة نورديك زينيث تعرضت لهجوم أثناء اقترابها من محطة سي بي سي في البحر الأسود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/83621" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83620">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826f62ba3a.mp4?token=cX0jAg2kR1kP0IE72fLfMwKEtjRtc5CJmgOpdevrCEAyNuJjSoRDD3Ol-pot7jtKAfwUSX1rWmXbgWrwjo3EECUhW39is5RwE9e8zgQd0VYvsbCh0oQEBHU_Lx_J4WVqVHXweezyrB36bKQWNZzhTxwLwU0YrsT3UXFTsWVBUBI_iQFzhZIweaawVxa-BnhTtTMgjFhZ8Y42XqcHatPZlY1d5mTTV78OEkQDuwEYQdh4NLJ_pXb1U9i2W74tlOp5zK6WEbwjH8pK5q6k3W0PYg1W26SQ0gxM9UwMwp0rNvtfFChwWSc23dfcM3l-zLFTNksTqJQlF8XiwQclmi1__Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826f62ba3a.mp4?token=cX0jAg2kR1kP0IE72fLfMwKEtjRtc5CJmgOpdevrCEAyNuJjSoRDD3Ol-pot7jtKAfwUSX1rWmXbgWrwjo3EECUhW39is5RwE9e8zgQd0VYvsbCh0oQEBHU_Lx_J4WVqVHXweezyrB36bKQWNZzhTxwLwU0YrsT3UXFTsWVBUBI_iQFzhZIweaawVxa-BnhTtTMgjFhZ8Y42XqcHatPZlY1d5mTTV78OEkQDuwEYQdh4NLJ_pXb1U9i2W74tlOp5zK6WEbwjH8pK5q6k3W0PYg1W26SQ0gxM9UwMwp0rNvtfFChwWSc23dfcM3l-zLFTNksTqJQlF8XiwQclmi1__Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مشاهد من الاقمار الصناعية تظهر اخلاء قاعدة العديد الجوية في قطر من الطائرات الامريكية بسبب التهديد بضربات صاروخية إيرانية ومن المرجح أن تتفرق الطائرات إلى قواعد في إسرائيل والسعودية.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/83620" target="_blank">📅 16:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83619">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8c4cf5444.mp4?token=eumzvn5MEMrcNkqC6OZ5klOrfprhccchkSszNKFqnVKqwU1OQU6K0gdfRrI2HFjmz-VNNSfksyv0PicV-32_VYGrr6uBm14c2vLG3q4ap8oYM2csJO_mQ0D4T-aNYy95lxZjcHqbZZ_GsL8xS0e9oOBJthPsn9deMPp9eqei8VNwYnx-_sbdaQXc6c7d_0WWTMzKgE4zZGgG3P1mk3C1XOOIHZstO6uRM7SZFXgQ_ZLWFrVscITjTAQoAJ7gKGedgsE0dw9NrmkhlbeV38MolwNeaLLJRSrtx2_gsaPZaHN0aQOpELJRVqjSvfXpwRBjtX__B1jkcszb9eXBqFP4ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8c4cf5444.mp4?token=eumzvn5MEMrcNkqC6OZ5klOrfprhccchkSszNKFqnVKqwU1OQU6K0gdfRrI2HFjmz-VNNSfksyv0PicV-32_VYGrr6uBm14c2vLG3q4ap8oYM2csJO_mQ0D4T-aNYy95lxZjcHqbZZ_GsL8xS0e9oOBJthPsn9deMPp9eqei8VNwYnx-_sbdaQXc6c7d_0WWTMzKgE4zZGgG3P1mk3C1XOOIHZstO6uRM7SZFXgQ_ZLWFrVscITjTAQoAJ7gKGedgsE0dw9NrmkhlbeV38MolwNeaLLJRSrtx2_gsaPZaHN0aQOpELJRVqjSvfXpwRBjtX__B1jkcszb9eXBqFP4ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/83619" target="_blank">📅 16:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83618">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/83618" target="_blank">📅 16:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83617">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoML3In7n7mPIiqzvP_H50HU8-yxKHQhzkZnQNy6XDddfqzyM1R7OdSUpzZeC3JTrpqhlcFe8NLBvNWIzoZz9osoedNs0udDGT-17AOa3rS0iG5W_zLzUeRv6MJHduaJoUuIvdrr0Wtd3ez3ILT1LhcxJQz-2qqd_a3PSI2eiwWzQy2gVJ1AUWgyl8xohcBKPNOMC8u1wlP8CAI-XvbUmBJD0D8vx7LJPGKxnx0VVCuyqhkpySqSZOWkya9cJyEGrRUwho7jf5errkdKuiVUqFSXrHJ2FVeljdnuooPNpLIZzEUyj7VVWTMefAC6-eO3lpq_zRQMQPVrozYMeSkXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛐
سماحة المرجع السيد علي السيستاني يجيز للشيخ محمود الفياض نجل المرجع الراحل محمد إسحاق الفياض، إدارة الشؤون الحوزوية في أفغانستان، وتولي رعاية مؤسسات والده في افغانستان.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/83617" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83616">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">غلق مضيق باب المندب؟!   والمثل العراقي يقول " ام حسين ما رضينا بواحد صاروا اثنين" بعد غلق مضيق هرمز الإيراني الان باب المندب وميناء ينبع هو الاخر سيكون أيضا هدف نحن لا نتحدث عن شلل في مصادر الطاقة نحن نتحدث عن توقف تام  EU this, winter are to cold</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83616" target="_blank">📅 16:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83615">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي لافروف: الزملاء الأميركيون يدعون إلى استئناف حرية الملاحة لكن هذه الحرية كانت قائمة بالفعل قبل بدء العدوان على إيران</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83615" target="_blank">📅 16:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83614">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي لافروف:
الزملاء الأميركيون يدعون إلى استئناف حرية الملاحة لكن هذه الحرية كانت قائمة بالفعل قبل بدء العدوان على إيران</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83614" target="_blank">📅 16:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83613">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8aaed9139.mp4?token=Q_aVnbz7CvjKqUDBL30VVs11YGpf3jUYitGLScXsoMAs7NxgqQstbaGLg9MIpCgQShaVAJ4rEuMpXfB8y3qbR2rUHDLGB6oY5QDfwgzy6YlK6JGxUVr8Gngl6zfOt5CeYRuRVNz_dnvs_w7MFloiprMPcJkmIAT9j2MRFff8BzDP0-svDT8pJdsbyhAJwTH2wM64-L-nK938x8GduxVvTgtMBxgfDYU2VoABsxZk_yyWHuQ-5pOCktRz2jMNey4dgepXtf0SmTrkLKQv-z_TBURU0wTZG7mq7G_nYcWn8X45MnLcBYuaed7IA-QZB_ZcPYwk5SmoRcPm-6nawtGICg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8aaed9139.mp4?token=Q_aVnbz7CvjKqUDBL30VVs11YGpf3jUYitGLScXsoMAs7NxgqQstbaGLg9MIpCgQShaVAJ4rEuMpXfB8y3qbR2rUHDLGB6oY5QDfwgzy6YlK6JGxUVr8Gngl6zfOt5CeYRuRVNz_dnvs_w7MFloiprMPcJkmIAT9j2MRFff8BzDP0-svDT8pJdsbyhAJwTH2wM64-L-nK938x8GduxVvTgtMBxgfDYU2VoABsxZk_yyWHuQ-5pOCktRz2jMNey4dgepXtf0SmTrkLKQv-z_TBURU0wTZG7mq7G_nYcWn8X45MnLcBYuaed7IA-QZB_ZcPYwk5SmoRcPm-6nawtGICg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أنا احب قطر بس….</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83613" target="_blank">📅 16:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83612">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb30544783.mp4?token=iAEXWfcw-VQEmaH-xazLVDZtJxbCNjlswJu43IddP6EAcNlJuxWpsbHuR-RNr_Tt0rJq_XlpZs1PaqK2fy2llcHc-oQh6cmSnF2bhl2T_ncvdnMigVM4sFH53zKAYE-lNtdn841kLZc3vcUVqjYY12AQMMDfy6fo4Gl3kgOlo3s7mGXGFkkEnH5udtBBQwfZ2LUxB6KunOyWOX6I-NhX4JlS5FCPHuJ1xIFxamOwWt1OFvQPd3jkc2teIj7L612GnugvYDbjChhaAoan0emUdxJ4VuuRxYku4q20DjnAxyaBqP5IWftDgfxgEBQy5pdAuMP89Zr3e6tacrkdNT6kcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb30544783.mp4?token=iAEXWfcw-VQEmaH-xazLVDZtJxbCNjlswJu43IddP6EAcNlJuxWpsbHuR-RNr_Tt0rJq_XlpZs1PaqK2fy2llcHc-oQh6cmSnF2bhl2T_ncvdnMigVM4sFH53zKAYE-lNtdn841kLZc3vcUVqjYY12AQMMDfy6fo4Gl3kgOlo3s7mGXGFkkEnH5udtBBQwfZ2LUxB6KunOyWOX6I-NhX4JlS5FCPHuJ1xIFxamOwWt1OFvQPd3jkc2teIj7L612GnugvYDbjChhaAoan0emUdxJ4VuuRxYku4q20DjnAxyaBqP5IWftDgfxgEBQy5pdAuMP89Zr3e6tacrkdNT6kcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الاقمار الصناعية ترصد أضرار جديدة ناجمة عن الضربات الإيرانية الأخيرة في مقر قيادة الأسطول الخامس للبحرية الأمريكية في البحرين. ‏تُظهر الصور أن هوائيًا من المحتمل أنه كان يستخدم كمحطة اتصالات، قد تعرض للضرب خلال الهجمات الأخيرة</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/83612" target="_blank">📅 16:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83611">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVOfjUoQSIsq74W3IYftI9HKUwzVFyrk5ejRadnRzZwad_0gQEfcB4ilni1Qun_Y_XUmaHlfGGg2YUHlmAdos-S4Xmu0pVzdzjIY4AfPo_4G4B6dyOQUzXWpw1vjSOb8Z_DKseJtri8g5mbskeY--1_HskF6N2hW1Oq1oRdRg8btuk304FjJzqlDBS15YN73NVhp6PPZk8Z5FWJ14aBVNMmZjYG6BBo64t4vZtgODgGZKU7fCwiKXn8KogdwR3aiWJ3s-PUPr_lGzSGNR3hvOYm2qKazjY5iBt8deRWxSHTAa8J2rQwbEs6JkLnKqCVQhMZEDaZow-woDRNH7zyK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
صور الأقمار الصناعية تظهر أن مستودعًا لوجستيًا تابعًا لشركة هاليبرتون الأمريكية لخدمات حقول النفط في منطقة ميناء عبد الله الصناعية بالكويت قد دُمر بالكامل واشتعلت فيه النيران بعد أن تعرض لهجوم في وقت سابق من اليوم بواسطة طائرات مسيرة إيرانية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83611" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83610">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb38a92c43.mp4?token=vurnN4nlQY6VhLwQFkw3jccRGLZzaIuG_3UwcA0m5xYHfLwIB3ifpx4SDLmtA_D7pc5BavxbWyV14v3AOnoMExPtjYBYH92Kj-6biTG1C52NpvuC1au4Y2y1KakbvxTM0uWjexDLaaSViYBunrVIzlNuNaNU127N9Wa3h85EkBP9gMj8xXKHgsbcVrwDX-lz1yBEiXmQchpRDqKDB_dLfCTNXFEbAgYrT95OdZSM-3Qu4EPn3EfJj_uLKOgiInZNsq6IT73kYAv8PB5eGUQaYBHtTPLskwWcUw3jupJqdd8cooSNBVzk81m4Ddy7xPDOQlUQaPQiuLYDwYIj94Bohg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb38a92c43.mp4?token=vurnN4nlQY6VhLwQFkw3jccRGLZzaIuG_3UwcA0m5xYHfLwIB3ifpx4SDLmtA_D7pc5BavxbWyV14v3AOnoMExPtjYBYH92Kj-6biTG1C52NpvuC1au4Y2y1KakbvxTM0uWjexDLaaSViYBunrVIzlNuNaNU127N9Wa3h85EkBP9gMj8xXKHgsbcVrwDX-lz1yBEiXmQchpRDqKDB_dLfCTNXFEbAgYrT95OdZSM-3Qu4EPn3EfJj_uLKOgiInZNsq6IT73kYAv8PB5eGUQaYBHtTPLskwWcUw3jupJqdd8cooSNBVzk81m4Ddy7xPDOQlUQaPQiuLYDwYIj94Bohg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
صور الأقمار الصناعية تظهر أن مستودعًا لوجستيًا تابعًا لشركة هاليبرتون الأمريكية لخدمات حقول النفط في منطقة ميناء عبد الله الصناعية بالكويت قد دُمر بالكامل واشتعلت فيه النيران بعد أن تعرض لهجوم في وقت سابق من اليوم بواسطة طائرات مسيرة إيرانية</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83610" target="_blank">📅 15:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83609">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cq-bPeR3vimVpXK9QPVj5u2pCSul1jAQsS7VlEsklReFkW6Q_b06OJYdh7LsZtrRh1wG_BTK4f4UI9p5m9sQSmeQw1LJhWRmrXCmMVhwhI_S_eRs0K61k3hKyAH2jORjlwQi65AAqaJoNYGcGDZQYWASiIlFKX8OIyRNrX1sCkks4OZJU6eX3TqeprngA0prz1G_-lNYK3W6Z458qrz7GIg24HpWaynoHd1eSwss-1gdad2Px8PSiD6z54OrI-Uc933xnNJm-kTol7AgvQI7ZpY0vxSBp1hR-yppX97DFxb8bkgwU_KUZA9UaK9azIqvL9MAw6NZY5AdzQC6WqASLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
السيد مجيد موسوي
قائد القوات الجوفضائية التابعة لحرس الثورة الإسلامية:
في نظامنا الحسابي، الأرض هي الأرض، وطهران والجنوب جزء واحد لإيران. عملياتنا الفعالة والموجهة من جميع أنحاء إيران ستستمر في استهداف العدو حتى عودة الهدوء إلى الساحل الجنوبي ومضيق هرمز.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83609" target="_blank">📅 15:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83608">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجارات تهز سليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83608" target="_blank">📅 15:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83607">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات تهز سليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/83607" target="_blank">📅 15:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83606">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLRT5ywRYepD39uDtiLOkHVFem5lrhlI_2BaNDif9k9v_ue1bW_VvtExY1Z82xnsZ5_3DyiUwj4sgQm5Yff4eRH9F8_OgZE-uXIFLZOEgn9BpzzaFVh_8UrYjpCSfpeuLy1EEHHdC5vecgw0hbxlbtp2knjOx1UuiEzGGAT_VX7N9Z4OvANwogtSBTxGiXP81l2_COQOriAOKrmhUT_o0k2Px8p5Aj8hpotRbLHTygYOFd3IP-Yr5wn5RtP7QWbiwc5SajnTZGyzS_Qx0JZtrO_coqkdbl7X_K2woQY2azh42HaHg5v_qlNjabdF2E3QwYFbqIhvmSBOxY99M4d-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتعال النيران في منصة إطلاق صواريخ هيمارس امريكية عقب هجمات ايرانية يوم امس على الحدود الكويتية العراقية</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/83606" target="_blank">📅 15:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83605">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQm_UPaOYEO-PpByOEW_PKQVs3IcoujtU4j_zrsu5GpL3zaKQqjTNZip76utEm07OabvfWE032DUBPJJ2b2t52juGMJSKCFA-v7lwmeDnASgXWs-j3YNyOWk6AmI_cjkMlTEnz_wd3o-SmRrPNqiYWf6mHLXHE9yG1kX-dKsHKDn5gIfm8T6fMxbuQAS3T06qdU28f2eaONLPUY6XvJZUxZIJpOb5vDZ-RsaxDQZFb7LLB6-VmyOiXGff8UFZP3UFInil428O0votHfckiAvCovMNwNMOHl5VDHrf54mkiatH4XaWq1iEo82a1VoPWO_ExBpEBkuDquZcS8Wn6eiAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئاسة أركان ما يسمى الجيش الكويتي تزور عدد من الجنود الجرحى بسبب تعرضهم لإصابات اليوم نتيجة الهجمات الإيرانية</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/83605" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83604">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇬🇧
حزب العمال البريطاني:
فوز آندي بيرنام بزعامة الحزب بالتزكية خلفاً لكير ستارمر.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/83604" target="_blank">📅 14:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83603">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">طيران حربي مجهول يحلق على ارتفاع منخفض فوق قضاء سوران في محافظة اربيل</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/83603" target="_blank">📅 14:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83602">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مهاجمة سفينة في ميناء الدقم قبالة عمان</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/83602" target="_blank">📅 14:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83601">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/83601" target="_blank">📅 14:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83600">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اقليم كردستان:
بسبب توقف حقل كورمور انخفضت كمية الكهرباء المنتجة بمقدار 2500 ميغاواط.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/83600" target="_blank">📅 14:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83599">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">العلاقات العامة للحرس الثوري الإسلامي:
بسم الله قاصم الجبارين
﴿وقاتلوهم حتى لا تكون فتنة﴾
استكمالًا لعملية الرد بالمثل التي نفذها الليلة الماضية مقاتلو القوة الجوفضائية التابعة لحرس الثورة الإسلامية، وفي الموجة الخامسة عشرة من عملية «نصر 2»، وبالرمز المبارك «يا أبا صالح المهدي أدركني»، وإهداءً إلى شهداء الجرائم الأمريكية الأخيرة المظلومين، وبهدف تأديب المعتدي ومعاقبة الجيش الأمريكي قاتل الأطفال، نُفِّذ هجومٌ عنيف ومباغت على القاعدة الجوية الأمريكية في العديد بقطر، جرى خلاله تدمير منظومة رادار بعيدة المدى وعدة طائرات أمريكية استراتيجية للتزوّد بالوقود بشكل كامل، كما تعرضت عدة طائرات أخرى لأضرار جسيمة.
ليعلم العدو الأمريكي ومستضيفو قواعده في المنطقة أن تجاوز الخطوط الحمراء والاعتداء على المدنيين والبنى التحتية غير المدنية ستكون له كلفة باهظة ومُفجعة، وفي حال استمرار هذا النهج من قبل العدو، فإن ردودًا أشد تدميرًا في الطريق؛ ردودًا ستبقى خالدة في تاريخ المعارك.
(وما النصر إلا من عند الله العزيز الحكيم)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/83599" target="_blank">📅 13:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83598">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الأمريكية في العراق :
ويُنصح المواطنون الأمريكيون بما يلي ، لا تسافروا إلى العراق بسبب الإرهاب، والاختطاف، والنزاع المسلح، والاضطرابات المدنية، ومحدودية قدرة الحكومة الأمريكية على تقديم الخدمات الطارئة لمواطنيها داخل العراق. ولا يُنصح بالسفر إلى العراق لأي سبب كان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/83598" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83597">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الله اكبر   احتجاز السفينة من قبل أنصار الله</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/83597" target="_blank">📅 12:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83596">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">أنصار الله يهاجمون سفينة في باب المندب منطقة المكلا</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/naya_foriraq/83596" target="_blank">📅 12:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83595">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">أنصار الله يهاجمون سفينة في باب المندب منطقة المكلا</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/naya_foriraq/83595" target="_blank">📅 12:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83594">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/83594" target="_blank">📅 12:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83593">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خون ریختن خون بریزید خون در برابر خون پل در برابر پل برق دربرابر برق برج در برابر برج</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/naya_foriraq/83593" target="_blank">📅 12:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83592">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce814b2d1f.mp4?token=tlVe4KLa3ciCwVZAyTvCwW4uqLUkhXM8oTIfId10JQNoslf5_VtiDrDqN8HaHwYurIkCZ69GP9VjzoTyNZk6scwfRAqk7kimlRl-XliN2MZCE_SsaOXvbnHLdNrz0fc4DnND33_yvZU1gJ6j28jNZIkJy4ZB6bel9VqgYxMPRAzrtTpOsCkhiFvWhOzo74Ucp0DhfBnViRcaEg_34GS6CsG_Nhppdudp8v-qgnP2pWdzqjkPr3fIKuLPhd3TEfQCdC1juUlTkHW3ctNvIPOeORc6UQbDNxocJECRGcOVgGh4kRCSXv3RDRCsG0BLw8IDsCyGr-K8U9570dpi3NSjkLDcai2A49igrXSofe9HwF0iXdRAKexdccbxhGNfHVUIfUCHTlMDE5wUh3qk1W9KiUR2vBXVa5f-S_jjnpRf97i46OBA6lK5Uu7HDBdXUoT5hMh634mPM6oeW1thJwulfqaUxVGGVbRK3MYF3zLVBVqvk8-XeR6pAFJyqa-XnQknIfbBPPylCLU5qYRTf9_UJlZtZJKlRC-xH9zhhqo-mTamwTZo6WKjmkNf28iKAFVNWJXsW_r6IAt7DJ-nxSYc3UjxOg6BWtU3U8Hh1eUjGmrupxJS9zGufKzfRYsj7y6Uhp0u-Hg4tFz7E9RaM3gs6rN04W4KfmGCJCXjugR4rVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce814b2d1f.mp4?token=tlVe4KLa3ciCwVZAyTvCwW4uqLUkhXM8oTIfId10JQNoslf5_VtiDrDqN8HaHwYurIkCZ69GP9VjzoTyNZk6scwfRAqk7kimlRl-XliN2MZCE_SsaOXvbnHLdNrz0fc4DnND33_yvZU1gJ6j28jNZIkJy4ZB6bel9VqgYxMPRAzrtTpOsCkhiFvWhOzo74Ucp0DhfBnViRcaEg_34GS6CsG_Nhppdudp8v-qgnP2pWdzqjkPr3fIKuLPhd3TEfQCdC1juUlTkHW3ctNvIPOeORc6UQbDNxocJECRGcOVgGh4kRCSXv3RDRCsG0BLw8IDsCyGr-K8U9570dpi3NSjkLDcai2A49igrXSofe9HwF0iXdRAKexdccbxhGNfHVUIfUCHTlMDE5wUh3qk1W9KiUR2vBXVa5f-S_jjnpRf97i46OBA6lK5Uu7HDBdXUoT5hMh634mPM6oeW1thJwulfqaUxVGGVbRK3MYF3zLVBVqvk8-XeR6pAFJyqa-XnQknIfbBPPylCLU5qYRTf9_UJlZtZJKlRC-xH9zhhqo-mTamwTZo6WKjmkNf28iKAFVNWJXsW_r6IAt7DJ-nxSYc3UjxOg6BWtU3U8Hh1eUjGmrupxJS9zGufKzfRYsj7y6Uhp0u-Hg4tFz7E9RaM3gs6rN04W4KfmGCJCXjugR4rVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇦🇪
🇺🇸
🚀
صور الأقمار الصناعية تكذب وزارة الدفاع الاماراتية
صور جديدة تظهر احتراق ثلاثة مباني بقاعدة زايد العسكرية ، علما ان الدفاع الاماراتية قالت حريق خشب
😆</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/83592" target="_blank">📅 12:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83591">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEMn5baYAsrhiw8zPftexTB3jf7XGvBcdm3O9ayLVTCkWOt7vQat5t2htN0Qe7exDMtqreln7yw0BSwlK5mtgQwJvIAjun67OMXN8kaHJKtfuX5fGh1cM9QS14HGcrNWQsTQJW0QIZ6gASuHvyEVD__xXIiuiujLOTnWEZkfoH4oI4lt-YEAIWPIVQ7F0PTx14dpYyvKcuaVZXpAnFLSIONZdMC4-8N2kKLUMT1ssFKF1zyCCpqTUtCJDm1J56cswWgTuQ8vdz19VfR-x_yI7IJdYpORq8ALmv66Zw5nlDG_E6LmSMPRCx74Gmcur0ADq6rEpfoEx8NoCbakuXWS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
🔻
مسؤول في حزب الكومله الإيراني الارهابي : تم إطلاق ستة صواريخ على مقرنا، أصاب ثلاثة منها مكاناً قُتل فيه ثمانية من البيشمركة، وسقطت الصواريخ الثلاثة الأخرى بالقرب من نفس المكان.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/83591" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83590">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d374976c66.mp4?token=aR9ndIZ9uj9_YcTKKSD7iZbffoT0scVxPxBJWROrLiJYn4y6kHN7NQMLxBe48w177JY_01ycwJPSJm9gBlaBsnXS_GbMgcmEB97ZuT10qPv8tNW_QFjptx3N-dyZg9uNKL8g0M1x0cWh3IqjfSkWJmPquyW3F-yhK4526nc-QMyJ7Mi3hNPFRqpXUpLzCpwg3j7pherW1OGMFbw18u2K9eMm7n3Vzl1rEvYhUuBgDXXE0JqQoCoKJ5Fg9dSdK8dpsRcYWbv10jzC9lvp6-_36iJLbEKSM_jP9sfxr3uKns-BaJwmu8xhJrNR9dTDg4URdI9GZ-iTwbtR_B2TD7QPQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d374976c66.mp4?token=aR9ndIZ9uj9_YcTKKSD7iZbffoT0scVxPxBJWROrLiJYn4y6kHN7NQMLxBe48w177JY_01ycwJPSJm9gBlaBsnXS_GbMgcmEB97ZuT10qPv8tNW_QFjptx3N-dyZg9uNKL8g0M1x0cWh3IqjfSkWJmPquyW3F-yhK4526nc-QMyJ7Mi3hNPFRqpXUpLzCpwg3j7pherW1OGMFbw18u2K9eMm7n3Vzl1rEvYhUuBgDXXE0JqQoCoKJ5Fg9dSdK8dpsRcYWbv10jzC9lvp6-_36iJLbEKSM_jP9sfxr3uKns-BaJwmu8xhJrNR9dTDg4URdI9GZ-iTwbtR_B2TD7QPQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
US ready for airborne operations inside Iran</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/83590" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83589">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
في إطار استمرار عمليات "المعاملة بالمثل" وردًا على الجرائم الحربية التي ارتكبت الليلة الماضية، قام مقاتلو القوات البرية التابعة لحرس الثورة الإسلامية، في الموجة الخامسة عشرة من عملية "النصر 2"، تحت شعار "يا مهدي، أدركني"، بالإضافة إلى تدمير منصة صواريخ "هيمارس" في الكويت، بتدمير عدة مواقع لقوات أمريكية ومعارضة مرتزقة لأمريكا وإسرائيل، من خلال عملية جوية وصاروخية، وقاموا بقتل عدد كبير من المعارضين والقوات الخاصة الأمريكية. وتستمر عمليات "المعاملة بالمثل".</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/83589" target="_blank">📅 11:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83588">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات تهز السليمانية مقرات المعارضة الإيرانية الكردية المصنفة كمنظمة إرهابية في العراق</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/83588" target="_blank">📅 10:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83587">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/83587" target="_blank">📅 10:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83586">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkwsMZ_WqTaWQqPlZvFXnXoUHZH19Qs3hvGOwvbe375EYNvVXYUULba1F1UFAI4LFaEfm6itS1R5uwfzQcZzsJ2GNPZYykspCe9_s4MRVvWr0gad1DkaYJAM1sYdipS6DmMjTicA7R-LhtXuKztqW05UGFbx71dA1btLseTeHBZQ-J7xNh738uWC3PBuxqFlq7yBjiSNX_45dcJfDnntSVxzEQPklTsLiJLXXKn46TMgJKZ40kxjkfJy-K_JDNYsAm7830-5WgFt5kAoVV-RJ2ZmymsZaYnAn2iZ3MydZSVQNUvyFcjvMHxFEirX7flG-OqcJrcDxCikjbyw6A56Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشر وزير الدفاع الأميركي لقطة لاستهداف برج مراقبة في تشاهبار</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/83586" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83585">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d471f185cb.mp4?token=Y6DMl-eXMrz6a1tYPnihAPRgcd0ngAwKdC8Spatnc6ZyGHeuCLoQSnSlFKuoh8f5TXhkU7gbAjMu-ZIQ4t0G2ArJD8LBb4GQH5zn6jsh5nZddRKSwkh1vqErwvFlcXEMOF_mpN-YEJ_JRDcIzdKQfPfOZVRDs5lTbAXMWEJffqKmm4lifaBdwrHtYY_t10pEvaxWqofNVSUPNDRxauX-g_v-L-0W9rjcdRWN3mntLw1wPtEGsw2yUB_wlJnQ6FAywFxtUR2tF1P2c8Apstfy7Cy1CyoLMmGajcDQdO6Vm824ODYrVhq4yvXF1I2a0HcnKxyHtlNTf4JI_f6o3yr49GAHoHgJB7fAU1M6pLoFBVGrbYmdfEk5BRTMCvOu8XEfFZ1FxIicfzB5Mwkm2PkJGOnwrwcSaUXqXrcydZSr3EWITl4Ap-apetogWDNPhFNRLiuerCNff7qJlOAfvcjHurVPJIDb2Z-hEXMLrIUI9oQ-lWB_1yzypdRenLwW6HJmvg3DZlVfZBFlJdIKVCQH80kO7F_0ec_akrUmLOUk4OQS43h7oPytoo-53mvB8d6FUM9vJcrL2WwqMVtQJIo7GFQX8-acO6PxFZkSN2k6TIGGQuuYp8MhDyIKXpQY_V5y7EepGu-9dOBlXY50TkR6T8dwqUVV61iE-t7zBtCoAgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d471f185cb.mp4?token=Y6DMl-eXMrz6a1tYPnihAPRgcd0ngAwKdC8Spatnc6ZyGHeuCLoQSnSlFKuoh8f5TXhkU7gbAjMu-ZIQ4t0G2ArJD8LBb4GQH5zn6jsh5nZddRKSwkh1vqErwvFlcXEMOF_mpN-YEJ_JRDcIzdKQfPfOZVRDs5lTbAXMWEJffqKmm4lifaBdwrHtYY_t10pEvaxWqofNVSUPNDRxauX-g_v-L-0W9rjcdRWN3mntLw1wPtEGsw2yUB_wlJnQ6FAywFxtUR2tF1P2c8Apstfy7Cy1CyoLMmGajcDQdO6Vm824ODYrVhq4yvXF1I2a0HcnKxyHtlNTf4JI_f6o3yr49GAHoHgJB7fAU1M6pLoFBVGrbYmdfEk5BRTMCvOu8XEfFZ1FxIicfzB5Mwkm2PkJGOnwrwcSaUXqXrcydZSr3EWITl4Ap-apetogWDNPhFNRLiuerCNff7qJlOAfvcjHurVPJIDb2Z-hEXMLrIUI9oQ-lWB_1yzypdRenLwW6HJmvg3DZlVfZBFlJdIKVCQH80kO7F_0ec_akrUmLOUk4OQS43h7oPytoo-53mvB8d6FUM9vJcrL2WwqMVtQJIo7GFQX8-acO6PxFZkSN2k6TIGGQuuYp8MhDyIKXpQY_V5y7EepGu-9dOBlXY50TkR6T8dwqUVV61iE-t7zBtCoAgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دريغا كه ايران ويران شود
🇮🇷
🔻
🇺🇸
Trump , If you are man come in the ground</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/83585" target="_blank">📅 10:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83584">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">استهداف سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/83584" target="_blank">📅 10:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83583">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">استهداف سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/83583" target="_blank">📅 10:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83582">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات تهز السليمانية مقرات المعارضة الإيرانية الكردية المصنفة كمنظمة إرهابية في العراق</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/83582" target="_blank">📅 09:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83581">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بكين وباكستان تدعوان إلى وقف إطلاق النار واستئناف المحادثات بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/83581" target="_blank">📅 09:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83580">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">استهداف رادار أمريكي في سلطنة عمان</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/83580" target="_blank">📅 09:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83579">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/83579" target="_blank">📅 09:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83578">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URWjItrk5Ks5n7xyvrB7n-f5GooEkqlpQ0BzlLHGkGozY7Qk-0VBfJDz8mhXxJKnFl_ERW-KfVW_ahTKgqAm9pAt2yzXefnRB9tCwmtutxIOoSAyCmI4BnCgd9et0qtjgn4rJ7efd43xxcQD9hCG-TYjmR8ZJeRDNboXcu0opsb2RXZvPdfHjX1QVpnHn8op_s80f1qDnxE2b2d1pNKpF-WrCrAPkcSDaThqgO3PxwUDD6zWVsgOtI-x4A373Vm2n2vRX2t-l03ti5HN4ZAYGtdpD_PGrh5Piy32vRa35HZYFcjSz5o2hICirpEUF0tnHsFMjx0NNMS3WiBOIvOQSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
🇦🇪
بالتزامن مع تبادل الضربات
الإمارات ليست برئية ، حيث أظهرت بيانات تتبع الطيران تحليق طائرة تزويد بالوقود جواً من طراز Boeing KC-135R Stratotanker تابعة للقوات الجوية الأمريكية فوق منطقة الخليج الفارسي ، بالقرب من سواحل الإمارات .</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/83578" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83576">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a186bf2799.mp4?token=nE_9O7G8Hg-rQM21npF3DPbz10PXEU4hANRcV1pD9OXHWJrCzqCiWqiTqPDdUI7L9I7i68KLamvw4enHVJZ3PtH0NfotOL4iwZLP2lbpRD5Q3u8UVT42VKU4rHHFz7Awv0THJ6-bc4bkrTPtP7Fr-K-fm_f37YeowD_u6fDFoO4jjMAL_s9GaioI_3Y8JX0RLPI6g_cQSdzA1LcuoRegTkis8TK5Lo5vxeDWKBlQ52nATIQc5Z5HddrqIr9al4oQ7-_Lo9buZ1XdTBrAToT_fSqhLjYsGm91M-VdautkT3uX-DdlqVZdwbkLVkG9I5JFQJMYuQRz5XiyBKMsT7dsvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a186bf2799.mp4?token=nE_9O7G8Hg-rQM21npF3DPbz10PXEU4hANRcV1pD9OXHWJrCzqCiWqiTqPDdUI7L9I7i68KLamvw4enHVJZ3PtH0NfotOL4iwZLP2lbpRD5Q3u8UVT42VKU4rHHFz7Awv0THJ6-bc4bkrTPtP7Fr-K-fm_f37YeowD_u6fDFoO4jjMAL_s9GaioI_3Y8JX0RLPI6g_cQSdzA1LcuoRegTkis8TK5Lo5vxeDWKBlQ52nATIQc5Z5HddrqIr9al4oQ7-_Lo9buZ1XdTBrAToT_fSqhLjYsGm91M-VdautkT3uX-DdlqVZdwbkLVkG9I5JFQJMYuQRz5XiyBKMsT7dsvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز السليمانية مقرات المعارضة الإيرانية الكردية المصنفة كمنظمة إرهابية في العراق</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/83576" target="_blank">📅 08:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83575">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUN_7ALzk8ppSYc0004XmHXeM4SUru26FDBM8JlbI_AaiAnAsBFItu5gSFEvn80ZPdYRiTZb7BNG36sm9smvUm0_ckW0vPeu_gXdQA8xN4EnUoORk4Sxv7FBaH6iZt8-pzsO6ov08qxgkFDdMIBjOKiptkIbI4u22u7MZ26S6jdrZmvysksjWz_MuigESZ8mS_WTUyM5VXsuHRAiXCJdBIscutZnycHBUHKhhkiiXWBsZ-a6OG0n75J-SZtNQn8MPKK4e3_kHngFY1hkSnTrnNqz8scvHZbtMmzapP30wzlSUdvgDgvc3v4admgKKPW7jnybthabVRJFca1K3tNzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خون ریختن
خون بریزید
خون در برابر خون
پل در برابر پل
برق دربرابر برق
برج در برابر برج</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/83575" target="_blank">📅 07:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83574">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  ردًا على جرائم جيش الأطفال الأمريكي، قام مقاتلو القوة الجوية والفضائية التابعة لحرس الثورة الإسلامية، في الموجة الحادية عشرة من عملية "النصر 2"، تحت شعار مبارك "يا أبا عبد الحسين (ع)"، وإهداءً لشهداء مدينة بمبور في إيرانشهر، بهجوم مفاجئ على…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/83574" target="_blank">📅 07:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83573">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/83573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/83573" target="_blank">📅 07:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83572">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/83572" target="_blank">📅 07:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83571">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
ردًا على جرائم جيش الأطفال الأمريكي، قام مقاتلو القوة الجوية والفضائية التابعة لحرس الثورة الإسلامية، في الموجة الحادية عشرة من عملية "النصر 2"، تحت شعار مبارك "يا أبا عبد الحسين (ع)"، وإهداءً لشهداء مدينة بمبور في إيرانشهر، بهجوم مفاجئ على مركز قيادة العمليات الخاصة للعدو في منطقة التنف السورية. بالإضافة إلى تدمير نظام راداري، تم تدمير عدة طائرات هليكوبتر خاصة تستخدم في العمليات الخاصة، وفي انتقام لدم الشهداء الذين سقطوا الليلة الماضية في إيرانشهر، تم القضاء على عدد كبير من القوات الأمريكية المجرمة.
لا يزال السيطرة الكاملة على مضيق هرمز في قبضة مقاتلينا الشجعان، ولن يتم تصدير قطرة واحدة من النفط أو الغاز من هذه المنطقة طالما استمرت جرائم أمريكا.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/83571" target="_blank">📅 07:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83570">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veRXBs0YWIxcPhAYJUOa8p95ClvMlB4ht8gt_uXD0mvMLKSXzn3mzTe__Sn3la8S_sTSDKeNk9qH-M1sdTkVcKym1Y4U7uubI8YoOQiPpxwCUsKj-7pyuf0zNUvKg36F1V7XnApQB3AiVlXf3xPiSZV15SvLUAA9Ny3nIhBuJFFtQQuBvRpbyRQzFBK2PkE2VRokND3BDXxsmMWxxJ8fYmc9BrvmUqw1PvFOKiW05YtMDRfHa8mvMOgxkZZifwk4K3MJfAjLwa34Xeet5MhM435oVmyyKw9SYX3Mtz_yEgZSY_Nz7n1sByXeIg2rM4xpY8QSMnH9hb6rOK8TdpFHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشر وزير الدفاع الأميركي لقطة لاستهداف برج مراقبة في تشاهبار</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/83570" target="_blank">📅 07:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83569">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انفجارات عنيفة تهز السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/83569" target="_blank">📅 06:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83568">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انفجارات البحرين مجددا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/83568" target="_blank">📅 06:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83567">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هجوم جديد على قطر</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/83567" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83566">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/83566" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83565">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/83565" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83564">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سماع دوي انفجار مجهول في العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/83564" target="_blank">📅 06:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83563">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-LMUysa1TjaTm3vZ4OtBvP-HmZhtkvhnNRPdu6KrvtAuwZa1gwVWqqrCOvOtx-efE8GLbDZ9HXlF6mRDwRvCuU3g67bdvhY2MpYDno_2yyOrZg5_OZc6kIVOe4n2pnPVfm5-c4axBD3PK-5mNBDbVks4jHefbcBQK-Rb2QjdB6hG21Gp6PbRtKyAKFWChUEV84ElpNYf6BC3dB6cRENPCqAXZ7orwAhL2Oj4mf6FwMLOEITQ0ODLE65zWVgtKj2kYL5uhJzwp2O5qtRYuKZCruBCcUnFvu-L54c9qP2pcwOghj8j6Mc9NdCG4hOK8H-XsXUYim9o35huePsFQnqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مروحي أمريكي  من نوع اباتشي يجوب سماء البحرين في محاولة لإعتراض الطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/83563" target="_blank">📅 06:26 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
