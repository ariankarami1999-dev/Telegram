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
<img src="https://cdn4.telesco.pe/file/BC-mhdXhf2ejNninwu1tvFgBvD0nsx_gHeooRZ-GCUq-b51D7xteGBusRQoY7NZ-GAm1uVS_tvZlD19jremcmI5C_cmgv8BjGMaglf2e9jGWS3Uo8MR-x0sGxXmShgmBqrpj5feCFKiYYwnKWUwHLCt27MoEOJbnlkgPm_0rlEO9uQUsY6fu_XmRzXtSlurxkgjE1YpqprBtgXcjO3M_XiFh0gHuwV3QnIwZuwcB7QMP-AToBqPLAug2GetDhNEgelrT3r6PAAw9c6f3FfWhB0kx-x2IgeZgKRMeuTjAu75S25oFFXsxnRbLOwZ4XexJZrA5-QK6kuGEgumxy_ktuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 150K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 12:59:04</div>
<hr>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=phHuMXE_dxpNg2ViGJ1xbpbRGeqdbdgEKFBxI9tYbZqQAKG7Bt9RN37QHn-ZxEv2WikYVBEalUITjaf8h3--Br6hU8J1ezmfG5fNAB8PuPkuCKLWn7Ja_Wauk9e_Y8vNIXUqbCmMGB-_nqXp4XFnQ2iiVwIKD0Vk3NhqvhMdDqSkXRHqqkymVe6BbMp5dTq5hBR51sxRxPf5JhZlfQUUCcUVKnGPYKror8h4ho3IQvDDmDvnbBNgYn5t67IIBVVZYBEdd9sbLTUc5yhwnlwGrZf9W25QXhY0E9FS8zWF2n5bmb-Zg3FBs59LzDHXrq6029_4zSSYPADI9aOaLHSVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=phHuMXE_dxpNg2ViGJ1xbpbRGeqdbdgEKFBxI9tYbZqQAKG7Bt9RN37QHn-ZxEv2WikYVBEalUITjaf8h3--Br6hU8J1ezmfG5fNAB8PuPkuCKLWn7Ja_Wauk9e_Y8vNIXUqbCmMGB-_nqXp4XFnQ2iiVwIKD0Vk3NhqvhMdDqSkXRHqqkymVe6BbMp5dTq5hBR51sxRxPf5JhZlfQUUCcUVKnGPYKror8h4ho3IQvDDmDvnbBNgYn5t67IIBVVZYBEdd9sbLTUc5yhwnlwGrZf9W25QXhY0E9FS8zWF2n5bmb-Zg3FBs59LzDHXrq6029_4zSSYPADI9aOaLHSVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvGz0K7XpgvaQxFRyCyWXWQ3UDmF4h2gMS8A1As14glMxi16DFJt6PIRBq07ue1q3VjRslbu2mlMxi7ekco8ErKa36ZqnY_TN9OXJkfPs-3sYr6dttFrR4GgD-EJDpWnXvoSVQAP1RCEyoFH3Uml-QaipD0ZxUXvLaTBXKpG_jyWQlMuceOvFrdxYVzYdJaWKg4Lt5AHxCXLx1YqC4cf3Xr8BGrgll2QIWAckzpbGZ66V6MRJeAYCU3NshkCzFB0Hi0saPb_TtZ884Gd2il1a9vKkIMNB9QqBAp8-J4MYj-Mcz-3V0lM1ctisfPr3fcS4NDlwpY1pnId4X-CVltUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=bmC2q_r9iy6MgP0ZnQOUUwtZwrn-TMIV-TOiUovlLoSqu6w25SbqEl9VusRpqMLRCgyoqvsFTMMascGkKXyrz3aTWB0WAfZkpRZQA_1IS-JGZDkI2k6C0-MGNl2JNkZhEVAXoosnjBq9aH9pkfZWLP_R6M6fqBHBmJt0CzrMOZ4W5aWzG9kaz6SVSk3r2AShSO2VOzckQLtqRi0were9ZBeVgQBds9eRE_8dbyqu3XIhb2R_dTWL1HF9qlwnrrz8VGXaeTEuyGj-K7EE3PLTHaz4kLQ0FyD8WB6YhKo2Bi4gFsgkjJ1LYQXhiXR0KJYYukwQmq9Q53iT-MlYE_AA3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=bmC2q_r9iy6MgP0ZnQOUUwtZwrn-TMIV-TOiUovlLoSqu6w25SbqEl9VusRpqMLRCgyoqvsFTMMascGkKXyrz3aTWB0WAfZkpRZQA_1IS-JGZDkI2k6C0-MGNl2JNkZhEVAXoosnjBq9aH9pkfZWLP_R6M6fqBHBmJt0CzrMOZ4W5aWzG9kaz6SVSk3r2AShSO2VOzckQLtqRi0were9ZBeVgQBds9eRE_8dbyqu3XIhb2R_dTWL1HF9qlwnrrz8VGXaeTEuyGj-K7EE3PLTHaz4kLQ0FyD8WB6YhKo2Bi4gFsgkjJ1LYQXhiXR0KJYYukwQmq9Q53iT-MlYE_AA3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=dIQj7mIsfpe9rn5KFKFpYcc51iViqR-AlrO8eNyAuFNmCx-iT7AsaNY-jm-rSS4xdXKiLW5Zns3MctgIeOjdbmhlic9Z6hNHvJldvLRpQmYbUeJlXwg8_AnnhdwzY7HNrAQGbu-mKM5f3DJbuZCWnp6NPMBKsWsnPM4UZpPXBgDFW8ntYXQeRDE9dnnGwSF8TZr_NjeL2n5H2caMrd7UiJv6dyHIJGfuwH55TiOwxobr85Ehf35saKjQzjgvEvRdsCPf7S8F-E2lnV4IZd03PCruAscpQmPZz_7tg19V015v5BLrMhbr-5VSmt0BLlQti2XV96x2gT1iT3i8q39bKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=dIQj7mIsfpe9rn5KFKFpYcc51iViqR-AlrO8eNyAuFNmCx-iT7AsaNY-jm-rSS4xdXKiLW5Zns3MctgIeOjdbmhlic9Z6hNHvJldvLRpQmYbUeJlXwg8_AnnhdwzY7HNrAQGbu-mKM5f3DJbuZCWnp6NPMBKsWsnPM4UZpPXBgDFW8ntYXQeRDE9dnnGwSF8TZr_NjeL2n5H2caMrd7UiJv6dyHIJGfuwH55TiOwxobr85Ehf35saKjQzjgvEvRdsCPf7S8F-E2lnV4IZd03PCruAscpQmPZz_7tg19V015v5BLrMhbr-5VSmt0BLlQti2XV96x2gT1iT3i8q39bKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=TZmpOkGjsKh-mvm2cFH34z8tpTwNssfLVJ7T5U7CVeHTY_sJ2A0h92p_SAsVcXeaOoOwwbo-V33UiPiI3JPoVD0ixsLR5MpL2HlmR2-xN-TjuHwuzE_DIPFP_Swj4uns6uYL5jYwOXolwYtdGCM5R5zUqIPsHbYK_5Jt_pZifmEJu7wrmd3iV9lhmCjZX5PjC-N8hJTE2nTWFT50b2Ou2tJ0HGfYc-QM6Cmg2PhPKy-pwv400Tisl-iG4v6HR3jL6oGMB4ArEXkdc8GJr6jGN7Y3R2-T1lusvycIr0IuCL8HlviiF0VqvHg6z2evP71sK5qGJ1_5n1dwNKEveFilHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=TZmpOkGjsKh-mvm2cFH34z8tpTwNssfLVJ7T5U7CVeHTY_sJ2A0h92p_SAsVcXeaOoOwwbo-V33UiPiI3JPoVD0ixsLR5MpL2HlmR2-xN-TjuHwuzE_DIPFP_Swj4uns6uYL5jYwOXolwYtdGCM5R5zUqIPsHbYK_5Jt_pZifmEJu7wrmd3iV9lhmCjZX5PjC-N8hJTE2nTWFT50b2Ou2tJ0HGfYc-QM6Cmg2PhPKy-pwv400Tisl-iG4v6HR3jL6oGMB4ArEXkdc8GJr6jGN7Y3R2-T1lusvycIr0IuCL8HlviiF0VqvHg6z2evP71sK5qGJ1_5n1dwNKEveFilHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=GFr1gtf-1OD5Dv07qRAZrmyfDu5yyCOHFSwzKUZPww3rCqriy3ZZmsJGhuLTSUcyxTIwbvG7qbTJZIE7sCtWFeIHx2edEHdbL7I_pmd3fW8HXH4JXU-AZk7KvCJ9tBOn581XTY-FkRAb4ainiR2uLGbWwYvvleONZsNtOEGb5hAHjdSOtfDPuYot-MpIzEfOWdsnb0gS8i1X5icOoEQGpMI6gFS155XA8mSGN9Jhf9dtQGfR59jTkviQhAAp7FVu17r8txpoNFh4RwD0hNPyCcvbYuUEXssyMdR6CMvspL-by4tKcIIIHDn8uJM2aeuBwKdrxwqJuzVEL4i12bv_cKmHsmBPwelJEM2WyKJ84SupmZ2afN_RiBUrmJs6vt7WUjbccigXf3MCRuo_uVP6HfollzU3zqERAvCkkdyr3L-OrS0igFoAlBW49WfmlRLnkS887qpqCTXPbkUhFpYxucSsM3TH6Jhn4Uawfyqroeqz72JOE--v5H6QVXSBxfjkroCcqyaedF4cnn3ErxxJ3kMmYYuhCx9r3EETb9W_RLP-9k39dEmjs23JyeB54IGG-ag6F13v6t8t8G5nk8otRGz2QTNNz3tJudsbCVV1gWiW35Nbr5IltasS64xfV4BfzB65ZNnU9koCX7YxIYGu730vAXqOWHPQq7AH555GUos" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=GFr1gtf-1OD5Dv07qRAZrmyfDu5yyCOHFSwzKUZPww3rCqriy3ZZmsJGhuLTSUcyxTIwbvG7qbTJZIE7sCtWFeIHx2edEHdbL7I_pmd3fW8HXH4JXU-AZk7KvCJ9tBOn581XTY-FkRAb4ainiR2uLGbWwYvvleONZsNtOEGb5hAHjdSOtfDPuYot-MpIzEfOWdsnb0gS8i1X5icOoEQGpMI6gFS155XA8mSGN9Jhf9dtQGfR59jTkviQhAAp7FVu17r8txpoNFh4RwD0hNPyCcvbYuUEXssyMdR6CMvspL-by4tKcIIIHDn8uJM2aeuBwKdrxwqJuzVEL4i12bv_cKmHsmBPwelJEM2WyKJ84SupmZ2afN_RiBUrmJs6vt7WUjbccigXf3MCRuo_uVP6HfollzU3zqERAvCkkdyr3L-OrS0igFoAlBW49WfmlRLnkS887qpqCTXPbkUhFpYxucSsM3TH6Jhn4Uawfyqroeqz72JOE--v5H6QVXSBxfjkroCcqyaedF4cnn3ErxxJ3kMmYYuhCx9r3EETb9W_RLP-9k39dEmjs23JyeB54IGG-ag6F13v6t8t8G5nk8otRGz2QTNNz3tJudsbCVV1gWiW35Nbr5IltasS64xfV4BfzB65ZNnU9koCX7YxIYGu730vAXqOWHPQq7AH555GUos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9CZvSGD712qutDCEn-IWPe6A-_8f8LEDaqR-dMbb6NLy0hjLIcqjCwL-3Szo-4qBQRgMO7-dSqXtQNDq2fGI5nyYdpprxxIYMxKmxvzoSlKaJ656Vr1X3La4b76yktqXsrV7M5MhxpBA3NQheTWBFDADpRjsxNFtcVGDio09RAyUWRNEUes7hWeUFiRS0j_haXqFnLh8Xz4cMh7Tyz1F2pCh3fM4ZYB7WDMvgC9ZcuvvgqVRBAaggYce4QskGv5nJvMPEoHsMREYB-6xkas1v_UarhB2Y9VgZMHuJ8UKWV8AFfVEhe8Eyr5p8fDXfVhadrCQRtnW6_hOcdnt5qFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Y637e86oqfy4Zqj_JBkteg6XCvO3Lomls-nOgyrqu2TbGUCYcvhFGkLHEC37Fuxblwu6sq9t8zqWRqY4Vp6TjNdrqaTBKf4yCH_vPJe1c4XwJeu4kIYQjyt1HqeYPvpt7UPPnTbnxwasLZ5I4RnIPLToxWvRQNYTdFSLplStWT9AdGQ1JDyBKWvxBUJgfIKm8dumYw_FggCdviECV0JNRuSY70Lw07J9A-nyTijSw1_BWAKTpoAxIvzS18x9bvIcQfwajSF9_v5yooLpOQEDzYxmlcBO26okmmXVAWJSoudWlo9L1wgsPrL7lMyT05ECCIlE5s3ynH19JpD2jRc4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Y637e86oqfy4Zqj_JBkteg6XCvO3Lomls-nOgyrqu2TbGUCYcvhFGkLHEC37Fuxblwu6sq9t8zqWRqY4Vp6TjNdrqaTBKf4yCH_vPJe1c4XwJeu4kIYQjyt1HqeYPvpt7UPPnTbnxwasLZ5I4RnIPLToxWvRQNYTdFSLplStWT9AdGQ1JDyBKWvxBUJgfIKm8dumYw_FggCdviECV0JNRuSY70Lw07J9A-nyTijSw1_BWAKTpoAxIvzS18x9bvIcQfwajSF9_v5yooLpOQEDzYxmlcBO26okmmXVAWJSoudWlo9L1wgsPrL7lMyT05ECCIlE5s3ynH19JpD2jRc4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g57WqUUzg8LwHxQH3VGR2fBvYfyJv_R1xsqeLQG1ucOJp-mJPk0CdZhqTxy-4Ek5-A3l5UdLGB-LLedcnfWtCcf-nY-S0QtLypTtZhIG9ip7qMLoe3u6MhtJuG9zuiYGGjGdPQO1FiNmMu9v6S5D0ftMf-1NR18dB_0YtByfeQH3ulvHx-gD3QEzGMGI4wP7199i-aIREfdUGec0DggmSpE9Jhauvmeij8awIQ_1IbPvFU5_tZTK63BxOfLYJu7pMcbbxYWXinIGkwxPrWv9RXfKV9FnbRmSu0EUVFqQYHpfqR2g2ax7LOnFKuzaLBETqsgyuW9kYm7gm_l4Zw7Z4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGpCGD5xQCsEQ4kUQ_77MIELxttBZ7uijsFU5HJ1mBe9aXNJ-Ib-RJo5zXyOAmWCMmjXsjDeEDJCNaxT9LfYriJ3GPRWROTMJk2iRUOhTFpLb75fJrIN70q2cAkzZ0YYC24AGXVTCgpRPr9YOjxmXLxiOpqhXwR7vztxXQrEzod8XA02g1GcDa80mhTqLxIwv596C8Wz1I2sZXDkZ7583uSue8xahXWaGZDZoNgvgkuFzy9zpC0rT9XL91b6uzvYqkKewcMtKLNia2RXk5O5nh6oo0vTLLiU3jqY1-LoQzfHLuI3ELB8vmKjFdHOr2SjelobZSlytsREppL7VHoR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY2iY2032c8-Blgxzx_NC-nPqp6ZXmHRHKnRXryQ6MHMz5fBhEcKXkwx-M8WrtxsS-88dDh7_gzmmLVclC4vbf_J3cFlVH785bMsl7v4J_4l3CDFtBpN3ptvlYZPLmBjllZJYk-kjjYC_9wqk9JL8HFdO-XqbPmRcGp3huTa9H0wWb3Q7HrSCAf1bgDZ1WdZAVKmV2Gv4IE-meXpG0vtGF0V7Hc2pFTToNY_IJULnecsr2DYrv0xcuenYSu1XyVFGsS0B7ye7kUzGSrAMkcQByWOQBCcr6QuUX0DXQsWv3I_gEM1XGVUqoFmKa2xpg5yxUFy5NslM3cccsoC4Xvcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiTIvqjpeDRmUBybUp-t3ol7m0Xnx9_UTFjFt1H7_vU1LECwMRgN_cks5RgnfTWd2Rg4Fcp3-GHDe2OZn2yzfjqiUbK9wAty2iD8T1njvuchOEOpwPYsYkmrrPXcuqXscZZX2eXcv5TI3dm3J6a2l_hQPTZuinkFSzhVZcVKcoAPODrHmEwmCRKQxatVBG0RBlLB4REwYZCUjOUTwNHVGXZ4feDR2eXPXz2xUKiBniodM_dFVawFmvVqH40_J7yfOI0YKFaZrniVJHaurUaKd6PzWBLJ41y-TRKkpj9Jzu4318DDfCcAu9uN4pWKPjzlh41G3GxE-RbuBquFokD1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlVgYXdiY0BC8c6JDSHPT6dtXYLQQJ9xddJPddzDViIjbbNFWpfRGImDsLnDm2DQuA1USXQdBYX-4rcObjd9mqJ4pYWPxzNBi2TAOK7fvXSB4KQDkefavYF6KW_MZaoWezRwLjYEgfj6W2S8mmx2d6E_ubNJdZCiWmeZUeeLTg0khnS8V4CbTDeuD1K-rRtnRR0nT_2gfCUTPgh7tYh0bixWksP3EOWLQ1JVogjyT7PUk30AivvLMjl_h3fvxwDfe6yb7NB3vCwebDQtsSaXv8UGc6LooBbzUICP5XDTiDTDd_CEqBfAAkH961dWK0FXWhSCXM5hSZq0-AXej4X32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFrCKb0XLuf15IazFSe_y7D6vjuZSCFQ0L9yQL10xu-vkAExyH0EhVtLazHie_zhlTpkC3MMcd6NxcZMMd0ZC2dnrf01dMoQyqO9PVvAKFFvqdAKnDaD8jcr8loQIIWWU19XcAtNvTt-BqGyvrlt9EOCsIZzSByxrDLMC7OeKg2SGl2voMNcuunEQ93MXqSl4gx0h-VsiRCutfwqTQ8_m1jH4X2_IrUEQuNpaf7pul3eKNWmfxvA4lHPrcLw74PhlKf1GI1ot0j3qgalx2yRvkUmXdlsWmS1WtaIQTuxEaoj7V7iHZfCslScpp-myn4diKmbT7--OLm0tONDnZLvYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=fWHAgN6jaLCfH6C-91HtrfEsM1zEGOqk573WaKmoGYLyWy0pcWB_31pVNkLLqtbj1JLTwRJUDDfgZZA_TwN1giz0J0ryQNa6Y5Cy3DjQXS7Uxc-a9ekim-cJirCdGnUsVudHnODH2LBKH2CwovSpbTzDd9a1659o-lUDKU2iBtuL_suA9FPr5mb6omHm0q7L41Aik_NEZ_Elv1uWDeFP2brPco2cienQHLN8hVVFhQbg4UVIYA19F0cz4dARuUS6q-1a-J1BoarXIqd6OIflzGNWX3qesBGNQBgOM5NWnOSrnxcDSmWzJVPopVpj-NBt1UdFczE8d30-OIuHJhXYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=fWHAgN6jaLCfH6C-91HtrfEsM1zEGOqk573WaKmoGYLyWy0pcWB_31pVNkLLqtbj1JLTwRJUDDfgZZA_TwN1giz0J0ryQNa6Y5Cy3DjQXS7Uxc-a9ekim-cJirCdGnUsVudHnODH2LBKH2CwovSpbTzDd9a1659o-lUDKU2iBtuL_suA9FPr5mb6omHm0q7L41Aik_NEZ_Elv1uWDeFP2brPco2cienQHLN8hVVFhQbg4UVIYA19F0cz4dARuUS6q-1a-J1BoarXIqd6OIflzGNWX3qesBGNQBgOM5NWnOSrnxcDSmWzJVPopVpj-NBt1UdFczE8d30-OIuHJhXYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=TnHD4MSGCj8UgjcUImrOx4f-AT_aV0yGMflr-X4WGouYrg9G9HSm0FtCxnPbuNhIUUS4chTIGfwiZBDEl_FkqPszvnRhyEWPMnTdKx4t8jSU5J377JtpqNyB4ZYCj5CSc60M4SK55OSZitdPt2kFilKxept7w9Tc3_OIooB1RQtSukQ1LjDHPyhcad4jz1ayhXMi029cNIB62G6Xrhp1U9atzYlN5rin1LBQxSBoo8UPUmPDrLWyc89BVqwKmM6O0W1JiU57UsE8Qrx9-zHst79fAnOsKbzfqQ5FSY6vEOnvSUsl_kH1Df274nksfJ84F-S0nmtqmW2qNfdX6dZ6hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=TnHD4MSGCj8UgjcUImrOx4f-AT_aV0yGMflr-X4WGouYrg9G9HSm0FtCxnPbuNhIUUS4chTIGfwiZBDEl_FkqPszvnRhyEWPMnTdKx4t8jSU5J377JtpqNyB4ZYCj5CSc60M4SK55OSZitdPt2kFilKxept7w9Tc3_OIooB1RQtSukQ1LjDHPyhcad4jz1ayhXMi029cNIB62G6Xrhp1U9atzYlN5rin1LBQxSBoo8UPUmPDrLWyc89BVqwKmM6O0W1JiU57UsE8Qrx9-zHst79fAnOsKbzfqQ5FSY6vEOnvSUsl_kH1Df274nksfJ84F-S0nmtqmW2qNfdX6dZ6hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=P_7xWwNzaw6cz8Ck_92kGJBu1aQfbZ4jKSKy76bO5vQ8-yDXfs6yOM1dRX41nxR1YkTckm0nv-OjgBldH0r0ucaXBq9xZS_1hTG7spwb8SWZJ3aqPLaLMXLAfzaoMYI9hjFVRkGx_QhlnrG8U7GBr_OGiNtx6_OiV-ua_-npgxy1T3EUlpsnCI2n4lG3EUhJtNtJ5H4ACRt4XD-WO-eKEVDh1T-mwmDqlmFAEw37es_BKR5NxDvWTJlrsJhzflIXrIulfHDQ9rSbtaMu-F_Qu29Ufk6OwRlo0eYsxPd_D75sL9Y2ZQwcrQNOlUO0KqSaS01PqRpHyVnFon_MW5A-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=P_7xWwNzaw6cz8Ck_92kGJBu1aQfbZ4jKSKy76bO5vQ8-yDXfs6yOM1dRX41nxR1YkTckm0nv-OjgBldH0r0ucaXBq9xZS_1hTG7spwb8SWZJ3aqPLaLMXLAfzaoMYI9hjFVRkGx_QhlnrG8U7GBr_OGiNtx6_OiV-ua_-npgxy1T3EUlpsnCI2n4lG3EUhJtNtJ5H4ACRt4XD-WO-eKEVDh1T-mwmDqlmFAEw37es_BKR5NxDvWTJlrsJhzflIXrIulfHDQ9rSbtaMu-F_Qu29Ufk6OwRlo0eYsxPd_D75sL9Y2ZQwcrQNOlUO0KqSaS01PqRpHyVnFon_MW5A-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=Av3SqfIJ5shLz8CSesIzt9RBeHSosGTpdM23s6jtLaxB4jsiOsI-YuH7LvqBDKr7gI7AiXS_BhSK3siCmc0OZbDzLkDCLu2ppTMyvlbjRoxdarUfDe3_qG5i2qcO7rSp9H3cv4eygfOtndT97uAHl4bl7kMu22QmIcsRKesmKN8iJkkMWo6JipV_4Ho4XwjPf3gEzxNqrm4oXAhq8MT5ckHcMF7rQh-KSIR-pY1Dza7TuJ03e9QnGgV5ePYubEJMHpzN5a-Qg54hHYc4X5Nk3nsIjKIlZVQPSpYmEwlhKzhhDR7sYKTWb18KQRCiyLBXFpeAiK61YnSdET5AQzi28Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=Av3SqfIJ5shLz8CSesIzt9RBeHSosGTpdM23s6jtLaxB4jsiOsI-YuH7LvqBDKr7gI7AiXS_BhSK3siCmc0OZbDzLkDCLu2ppTMyvlbjRoxdarUfDe3_qG5i2qcO7rSp9H3cv4eygfOtndT97uAHl4bl7kMu22QmIcsRKesmKN8iJkkMWo6JipV_4Ho4XwjPf3gEzxNqrm4oXAhq8MT5ckHcMF7rQh-KSIR-pY1Dza7TuJ03e9QnGgV5ePYubEJMHpzN5a-Qg54hHYc4X5Nk3nsIjKIlZVQPSpYmEwlhKzhhDR7sYKTWb18KQRCiyLBXFpeAiK61YnSdET5AQzi28Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=FYstXUprZbm14aLy3jqJz4KzdkQcUwiTSXN967zAax9Dc1twgpuAQOOdLGNA6vaXg5jxsYn08qB1AugUOT3D9fiqmRbkNXYpa9b4NoQsAqd8pbQJUMWv7MdY8XMUbj_aGI8A2lb9xG1bVafl4vwyBRURvf_sGwDPCtYj6ryrE7zWun9HNuWIkLf36aB9BUJxyXe212zMcVJ6zW8zg8ztaVgjYNjcGI5nm3RkaWraxCycMYtQEt0Npc_sHgjN0_YEIwCDooXix6wxwfJOaRfaeAF5oadGS00UNkZioi-uKaMFcDXK5nWcAP-BLmrxH-JpIj8MtvFaeKTbSrLuUg_WNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=FYstXUprZbm14aLy3jqJz4KzdkQcUwiTSXN967zAax9Dc1twgpuAQOOdLGNA6vaXg5jxsYn08qB1AugUOT3D9fiqmRbkNXYpa9b4NoQsAqd8pbQJUMWv7MdY8XMUbj_aGI8A2lb9xG1bVafl4vwyBRURvf_sGwDPCtYj6ryrE7zWun9HNuWIkLf36aB9BUJxyXe212zMcVJ6zW8zg8ztaVgjYNjcGI5nm3RkaWraxCycMYtQEt0Npc_sHgjN0_YEIwCDooXix6wxwfJOaRfaeAF5oadGS00UNkZioi-uKaMFcDXK5nWcAP-BLmrxH-JpIj8MtvFaeKTbSrLuUg_WNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=V3bsL4ZQIWA9BbURBfq3fPe-iOClvykzarFbvDkRwaHE6fabOH-vVdKjvgjB96dEFw0uwrlXM5xCXlyWHgXsjat_hKqj5u-6bdAbUaNADhTdGDpZ2QF7fVitoEyrVvNds3LhkkTNcRafEiXbnZAQ-MPATjQwrfH-GLcmSA7rsGxgqM2Zh8aJZDsocU1bs-iQeUk0WgHKlHMfJXeJKo-jThgqWwkjPOqK6uoksNb6ejpUHSvluQ_uwYb3eNVI64vm0CUuPsA6-Q3s_QHIvKM3uqRlhR0kj0HmepCOYHLZgKzPvCsSRJY7AL35Vl-NF9-dqkYiXeIDXyU49jrHP2sGcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=V3bsL4ZQIWA9BbURBfq3fPe-iOClvykzarFbvDkRwaHE6fabOH-vVdKjvgjB96dEFw0uwrlXM5xCXlyWHgXsjat_hKqj5u-6bdAbUaNADhTdGDpZ2QF7fVitoEyrVvNds3LhkkTNcRafEiXbnZAQ-MPATjQwrfH-GLcmSA7rsGxgqM2Zh8aJZDsocU1bs-iQeUk0WgHKlHMfJXeJKo-jThgqWwkjPOqK6uoksNb6ejpUHSvluQ_uwYb3eNVI64vm0CUuPsA6-Q3s_QHIvKM3uqRlhR0kj0HmepCOYHLZgKzPvCsSRJY7AL35Vl-NF9-dqkYiXeIDXyU49jrHP2sGcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjCyqkmWTdvPwhMAoAonqddVFj6qc_HjlXYibgMKHcKuBs0Lz2uBQnYwBn7PdEsfEgFPDCj46aF1LlJCqOhKBBBIgxR9_wblAXDU0VjCj8NGyR35QtJYCtcsmEZIFznQDnL99ZM6e6Gm7VJSuKwxZujsNKtPfz9VhuTV1Aac4jwGMUvNs73raOE2igI8UUoBT4WYc8elgp2g92fuL0z06JZTp8H9Vgi_GIivC-02VOCy4Bfreq6dNW0VP_zUF1DCEy5zeAtRVu73hh60_JjU7ufyljy60eUXOO9L_8Ek6roLBR-lx76PF8h9QDa0PqZOIcI8bDVoGvmKD8cBPI5o9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do-3LAilAcQQwVBj7sjCffFcAKLxt-lHIW0Qy8BrfqksI0pnuPxszcscnfC5fZeqdO7YzCO4GYhNRzu-LH2pi3fo4Jk-8vNR3IxEK3rVqVxG7_al-RM4_L-EhH2dm6IeH62MbRgh_gnrUTi57pJMQZgL2BFZwaZA8prxNxLHK4c8DLQ4HecS4dgThWNXdSqjBgFvOgM3Ty17ZEgs99n5y3MF87XuTrmmoDHj0zJwwvWvEbHMKuPLSFpaBkSlUVHrSrJx_QoeRs0Dz-DwxjCHivpi92q1IX3KA0WmfJMMfnE-nTzJv-dO_Y_O0TR9NNBlC3oH52mvawtPmR7wEGQDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtrw9PLrfxBiEX3_VLZcDzzILQmJsWtWSQduYmiq6Ra5LKQOiddNhGVYB1lJCdOrR87dKKzglN_CYb3Dl9o9AG2M94rl_1knXMHfxHYzg93xJbpLVc984739c5lEQloXOo4O3lJ4iq48J4nIa2UKNb3nhEmmQdT0eCiSgxnI-80Tg4MF1K0GZri6EKqE_GDBRRqXFMnIoN0ogujf2h5etRXaJToDU8QDgC9_Z-cDZ20RVy5xy-A0N0JR4-nzG-3lp4hPNQbQdu86oHtMbourZbGSWA-9ycxql2ED-IXuLbRmGiW54vCNjbe3e4HhGeA3YerIWMIM5B2COXJ3LcR80w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=ePxobxOOBKHgeK-lJVh2ZU-lqdzu7YEH6G1PieMUi3kzwL3-m2a80DLAbMyf7lOPy7Tk43XmHkfraXhIBhdSv3cghz-fEwkSQ2ObmYSLj1FRQ9oqbN323WMK5al2HVVOy8Hksg4z1xVS9MsNlnRqyyVF1Oa69lVHfeZFErcrtNlnsYx4AV0VdUK0Ymamcw1YJSEv2dIzMlI8kNN1BG1Na_467Kxgx0p0xcG2iAW7scn72-t0eqbW2mHQkd4LyGVu5kifReH2LctoydIYWYBlKJj1WZsr0uC2_YcE1UvT3zguNdA3oJjC4oEeuKg-YREznLXev1avSVmT-tH3CZCrRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=ePxobxOOBKHgeK-lJVh2ZU-lqdzu7YEH6G1PieMUi3kzwL3-m2a80DLAbMyf7lOPy7Tk43XmHkfraXhIBhdSv3cghz-fEwkSQ2ObmYSLj1FRQ9oqbN323WMK5al2HVVOy8Hksg4z1xVS9MsNlnRqyyVF1Oa69lVHfeZFErcrtNlnsYx4AV0VdUK0Ymamcw1YJSEv2dIzMlI8kNN1BG1Na_467Kxgx0p0xcG2iAW7scn72-t0eqbW2mHQkd4LyGVu5kifReH2LctoydIYWYBlKJj1WZsr0uC2_YcE1UvT3zguNdA3oJjC4oEeuKg-YREznLXev1avSVmT-tH3CZCrRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTDbUsg890V28bwRFCVnAMrBGp5LTwP-Gd6YO1eL2unsK9NZF-IDOyobt6-q56i_vQ3tZ6qLd_ggo0V-MBQUzUmFIRRSEMbsgJeCYfqFeSJ105a6yY3S6TJ-foENRJy6sPE4GkMH7NYsZwyjAHTY3JAV_5z5Ky5IUta4B8iwwzCCD9grj1DqigX0pWsBpDDuaZGavwcR0xDfq0KgTh9yKK_2e_rDczI8VH68r1VrqoCS2SSu3YXo_djd_3Xy3fUlUlu902reOT6JoQA6aZNd7IrAzvzR3nbJu7h8_DDiN-50C01bGveIo7BDrxu9XO7L_6PuCaC__uY44Jer9R2cLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3wP-PRjfN0rChdPj1lAaKMyPjEi5ity6ast4eqc6jV_B2cJLwL1xOSJOASUfqg-Vn900FZdJQR9Cl_rI28hulnThqRIcbOqxMuukrhZu-i3_KWtvJKUvqoUESngxmbIxC3tOTGWV4wFEbcOuzp7M8DhU0BuWtX1qhWQeH9KZQtECt35aix2gYxcy7yHtKi_0UJ1sTDoRGOW3IAUdpvTmerSmf5laLA7zhfQbRTK2mQPaqS5D6AqT8eR0IXHaEKFZHzqiHiGtSCmCGed5D3vqGGI3lUHI1BhMnvL5AadOw-j4Qg5ww76Uu64x1BiaYN3uK2uMdCsM8D5IfVb2xbcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=WeBFvpv9S2vUo2ft1T7vPBbZl959sxqyVwdy4Sa_un8XfYPWR1z6v9zSyHFkvXqx_oyt4BAE6T5XNWHYPV0NuwuKwL3vUr8XRDWLJW_UG1It0EQCm8iv2Ke4f7CKVGssBv_yuLa2Ay4v0zjUTahp_uf-aAq6S2eBP5H7fBMSKe0sYOgnl-qf0rt6Atr6gUjXzmx78uhVIKzRtRq2Z5O1-WaNRU-kvuj8tX6h4urPxuDtb1rM5Z4a8Pd_mo7NDye23ARPCmnbBWANz4GJMC7GQAeOtT7gZ_eR23ETL7KmSIVMXhmmSbEQSkoS5hzqw1mZkUw09ayRMj5ULosLWqdYHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=WeBFvpv9S2vUo2ft1T7vPBbZl959sxqyVwdy4Sa_un8XfYPWR1z6v9zSyHFkvXqx_oyt4BAE6T5XNWHYPV0NuwuKwL3vUr8XRDWLJW_UG1It0EQCm8iv2Ke4f7CKVGssBv_yuLa2Ay4v0zjUTahp_uf-aAq6S2eBP5H7fBMSKe0sYOgnl-qf0rt6Atr6gUjXzmx78uhVIKzRtRq2Z5O1-WaNRU-kvuj8tX6h4urPxuDtb1rM5Z4a8Pd_mo7NDye23ARPCmnbBWANz4GJMC7GQAeOtT7gZ_eR23ETL7KmSIVMXhmmSbEQSkoS5hzqw1mZkUw09ayRMj5ULosLWqdYHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxrBHIah5nKL2o7mWfpDQmMplfRxiK_r8i7DkKI3M-eGNeOr_5EApk2bpZqRdOzMNo1XZ7g6ZyZXmDG9aQJEJAofN9D5hpxy4wqRtUOHaLGrcYnc4NqEC2IyaNb9gkXcsQlRrbIY-G3V3JmPXv14C5NdSBJ8SfKRyfdt5EdMZCyI-WW8JjkB745w3gv4mvkfgSGnq0KG1SFL6tQlD9bGEbYTDwBYvrQJo0XbOwC0BKRvU_t1OOmhNCPQaTwbmqv8cbHf8bAb-jp5UqPHo5le1YGEoUanRAZ-r4wnfGnk9siijZ_oovwY27Ra0SqQrnhhGtlIiIWrGheTsY6Q7sS40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCI2BDdgJzYVyjqVgUX_Gb3BiJpuC3yr4xXgqcgg5kx09u3ph6lpEdoo3-SpRicLHKDfdyaTCM3rOmULi82ibopKKWXoYfN2msHyGZtZHZUBRKHV37zdL47HyJu712_6a427jsp9JtbpAFvBklWZKq3LdooO-clzYbxCVeJQ5aElcLWjI8ytHJBSLWfWh-bH3LzNDz5lI_ATyjxx7huUADUIEU-zOkSsyNsA08QS8Cl26s6UcKph4gFXo4BueNUjXlm_2SirVHDwSiqP_k5QLr2Hc-_jEvstDsRR3Tjx8gJc1GiKi76OGVAGE7XszcuNRWaNyd7UJgyn320ow1sIJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-ugwel2jBWUI22vSdKuN9uAQO307VExRi0KMZtHvatKHBH2EZIDeUGXMpCYP7PtHIPVnjQAKyxOI5AUBwgt3oJGI7IqQnqVHKcbgn_j4jPNPoDHgTvYizr0VNhGl3dne2d9se2T8uclp7LDurMcGANAbDGnIK4eLIqZbTdOHuf1qP96vdAzg-X-bRdeDbix6YJ2Gs67MTvfo3zvtb9IO-sjYseDYagrclL36GrFxfVUJf3A4JMk-REWiJaTxtWF-BqhGcCmlBt3svAsKHG-nSqXKYuD1i0bHhXaECocDVuBfrgsUFB8jKdf8Zc_kWCMVqu3epA6h2mg7aMVH7fSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l2TcmHtH0t14kG3A2gHu06i03AcXFCULLzdjaPtMNQGmNw971iBWNcDylxEn2HDTlZz7iJdBSPplTM7bVLSfJZOLwg3Vx9PCmgxXJy_x5SkrjPKbvr95Oq09g0AN7FpdU3vno_AMIyDdGN06f13r19LYwJVUHjra6NmXYFAa5IrUcF8bu0WI7-3kU9ePianWVvEhoP8jP8t-HPYtyb1t5i7scqouVuZ_jE7nJh9o4HbWwKCga-9pfgb3wnqHaQpQ03Laq7mKNlw-87SOLOQoYwRV7cn8LX19Ix6zVpsXLu2J51lpm5Ro28M6KsolqZ969-h31eXCBBvyHcCXN8f6SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=hN_Be3E9Uqf-V5BTTyfNTrQe81GoKUasWuhQfINfdOK3hOYVR97g8H8exp6ev1z9I2hGFYX3qVfvKnbq8l6-aKvdLC07BiuRyPqDmjUYoRa7tZFWPN_lt_wHoBu7BDzkEwzvAW2k9BU4wMKZTsi-gK1yk4hhuodOdgtlMuSi_9llZ-XJ8H1GNzaNwiNcwuiW3n9saZKiHIe9zjxT8pJSfR4He32W-NbKz0s5qN8kjvl0quajBycn9Pz16UA17-fqxVcBHcLQwhMb_a0xRzxKpPnLETxGBHw_1S6vg32XPf-uXenWlucfYQgQ2-phjaqQEAEN1ufT8igeJeuGBqQYFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=hN_Be3E9Uqf-V5BTTyfNTrQe81GoKUasWuhQfINfdOK3hOYVR97g8H8exp6ev1z9I2hGFYX3qVfvKnbq8l6-aKvdLC07BiuRyPqDmjUYoRa7tZFWPN_lt_wHoBu7BDzkEwzvAW2k9BU4wMKZTsi-gK1yk4hhuodOdgtlMuSi_9llZ-XJ8H1GNzaNwiNcwuiW3n9saZKiHIe9zjxT8pJSfR4He32W-NbKz0s5qN8kjvl0quajBycn9Pz16UA17-fqxVcBHcLQwhMb_a0xRzxKpPnLETxGBHw_1S6vg32XPf-uXenWlucfYQgQ2-phjaqQEAEN1ufT8igeJeuGBqQYFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=Vnl4TS2pQodfoVkymFX7mqG_fzGX7VHJmMlznV13NI8yNI4Y7TOm3e4f9_fIuDx_VMOcqZGqx4SJqFv1e5k6mXhrE-65B9Cm8sNzEN0eVDyfTxeJSToaT6CgPQZHQPy9cltIPx5BCOnEhwmfmbInQt9zE_skQujoUfHE2bMkeX_F-06rvJTD8iwqid90OLSyALVy7kmmIXoEPIxpCPvss9nwjYZd0vNZFwGw1QFLzprBS4b8U3n5bjuzzdGP-l5cu1pqa0m8Le5DZEHa1R_1-DgvVaJcJ5fEpRlCkTXpsHrZXyKuJacj2HLOYkt5ib2hsaO3iwmS2lf9zPr0rNEc3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=Vnl4TS2pQodfoVkymFX7mqG_fzGX7VHJmMlznV13NI8yNI4Y7TOm3e4f9_fIuDx_VMOcqZGqx4SJqFv1e5k6mXhrE-65B9Cm8sNzEN0eVDyfTxeJSToaT6CgPQZHQPy9cltIPx5BCOnEhwmfmbInQt9zE_skQujoUfHE2bMkeX_F-06rvJTD8iwqid90OLSyALVy7kmmIXoEPIxpCPvss9nwjYZd0vNZFwGw1QFLzprBS4b8U3n5bjuzzdGP-l5cu1pqa0m8Le5DZEHa1R_1-DgvVaJcJ5fEpRlCkTXpsHrZXyKuJacj2HLOYkt5ib2hsaO3iwmS2lf9zPr0rNEc3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKShnUAGg8pKxfvSjphB-6CiLGJjkWJHY97yxjqeBIcEj49pqNdVUKNHohISnLQ7qHtDnNQU3z9NDyoqQ9K_wsaWITu24EKh3moRCXKSiJN0TqCizU9t1IEjlITOQQoyfBoVvscqUOIlN306jJezfLpXxQjCgdlc5hXBuN_JJLPkJRmpRQqLd1j4HvzI6cCnV6wTqi8ABlqtflNFPTxx2IaiVWaQyLHUPki3sEJL120AZ1JVnA4wyDE2cux48fofwleUohQXodHLhN65OXSZDXSVUrfxTotMLh81r6uUJVP78lu7siK1KEfTj7PbfyWKQc75dw4_qgS8rLSOq7Sfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=YMuBaPSuOmjlhWmDjjtzgjRx4XF6iIhkIef0UXk1kzaQDb2WVSeZALfv2cBPZjQt5mHnroRHK76BVnhVUUj0CKJirErAAVezOUFF1x5G63PDm8B2v6lygQV-6cZybY95g9myu4iK05NRwFxBtWZXRnXsOIY5z0xeBFmL373AkE2z-H4A6AsHS_otII0aHhSOWdrKRGZHrQQIWt5g8wUuLm3fwYKydZBtSnOPnmj2L4ZGy4ieq4TbrUuqv5aLn3jqEbQvqhGU9RPhTuxb0kr39Ixx_2zrlL8j_S7sdqjhRny2cuWHI108w2IO_vl2NBqp39R_Oh1aFYRGhmHjcvz6eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=YMuBaPSuOmjlhWmDjjtzgjRx4XF6iIhkIef0UXk1kzaQDb2WVSeZALfv2cBPZjQt5mHnroRHK76BVnhVUUj0CKJirErAAVezOUFF1x5G63PDm8B2v6lygQV-6cZybY95g9myu4iK05NRwFxBtWZXRnXsOIY5z0xeBFmL373AkE2z-H4A6AsHS_otII0aHhSOWdrKRGZHrQQIWt5g8wUuLm3fwYKydZBtSnOPnmj2L4ZGy4ieq4TbrUuqv5aLn3jqEbQvqhGU9RPhTuxb0kr39Ixx_2zrlL8j_S7sdqjhRny2cuWHI108w2IO_vl2NBqp39R_Oh1aFYRGhmHjcvz6eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=HgbauoE11PvC4CxJs0fr0nGNseqoG1OtsyBA9ZKaYqDdwaprtHL2pkeWIGa9JB95rCtWG0xmeejqef-SdhHKcDeAJDbAw1PGWhWkDvwP7_fU6HRwXseLYLPT7T_q_80PfScYjhoh0lmoYlhG5tA7QSUNTFASNKj1b1pHRFD6HJYVQA0IpJsyGSrWl7Ewb-XZAw3RgsGKUWrzqvsPLyAdEZLLnxRd_ACjQgdHiQhNpaKg_aVktqZc_lauh_k_bpGwSTp5JGN6pUw0MBm0QEOl_tf1BAUQIqADrLK5GQpXpHp5Zfk-GrPJOO1NdSOMRWoVC3chnO7cldw7QXWZB1O1SSCSxHypg_KX6xw4jgy-wQ4FrPVStMWJm_rexDUg6VTpICJitud0A2UKjPGvyFCt1UO0sJ8d3FIFlTg6DjphxPU0EoDyuHQYaRndpJ-7giQqrcSIsGgRGCHD0bQeVz8Qrm-GIGAN0h4h1hAmQ3_ZtnxXIVXI1IOmRW_a_0Oc6Yq3WopNzq_hnRc64gkmX3TDJsjdGXVQTMjIztxwUA_qSbGmVhaySAgygAg3UiZYzzVNQXgMobkEe7tmbNXzhBYuWZO8ltXVfpEsav_FlSaqg5t-3Bsi-KXjoFpoTpXJjZUhnnrueT7DPNz_TEhxuorsKqUesFC7_g-xpjH4j3IbNU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=HgbauoE11PvC4CxJs0fr0nGNseqoG1OtsyBA9ZKaYqDdwaprtHL2pkeWIGa9JB95rCtWG0xmeejqef-SdhHKcDeAJDbAw1PGWhWkDvwP7_fU6HRwXseLYLPT7T_q_80PfScYjhoh0lmoYlhG5tA7QSUNTFASNKj1b1pHRFD6HJYVQA0IpJsyGSrWl7Ewb-XZAw3RgsGKUWrzqvsPLyAdEZLLnxRd_ACjQgdHiQhNpaKg_aVktqZc_lauh_k_bpGwSTp5JGN6pUw0MBm0QEOl_tf1BAUQIqADrLK5GQpXpHp5Zfk-GrPJOO1NdSOMRWoVC3chnO7cldw7QXWZB1O1SSCSxHypg_KX6xw4jgy-wQ4FrPVStMWJm_rexDUg6VTpICJitud0A2UKjPGvyFCt1UO0sJ8d3FIFlTg6DjphxPU0EoDyuHQYaRndpJ-7giQqrcSIsGgRGCHD0bQeVz8Qrm-GIGAN0h4h1hAmQ3_ZtnxXIVXI1IOmRW_a_0Oc6Yq3WopNzq_hnRc64gkmX3TDJsjdGXVQTMjIztxwUA_qSbGmVhaySAgygAg3UiZYzzVNQXgMobkEe7tmbNXzhBYuWZO8ltXVfpEsav_FlSaqg5t-3Bsi-KXjoFpoTpXJjZUhnnrueT7DPNz_TEhxuorsKqUesFC7_g-xpjH4j3IbNU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIdRqujFUpd5LBourgL1qnunnTTsmaNaBPKQCzxLMTgVVFMUOh6hBTu22ETAmyFjFcc0w4OA93QrNXccpT9zGdSlB-gjIPz-6n9IUhLLAixo7Dln7EtOr3oXFUJpaFevI_imzlP-te4WIc8MqLUfuPVJxqDWu5lsNXS728je6WW5gaaAUATnbN0CL954Ku0nEf7LnSe5ss75MA4VEdhsYCyXbyvOsW5yt-QInJsHyRdZPMcZQM5V_XKJFiua5UTtPd_iC9R2odpvizCgkmSrdtKnGThA-HBUb0cbdCpDchvSmT_l6rCI27Erdrz6w71k2OJuNU8U0u9blRLvdA_bzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Awv7N9aUxcb5UVNEdZzFwWEHfz3wFGXYKFhXPpEowhKc5pa-MVC3mhPfGIHyh4oqM7obKi4PV5ayrNx_RvWwD8OqCHIac2s5PrYduacBsmm8H1_6vcF17EDAZJrBT0bGBQE6EfdBDZvW0jc0vVixXtTYcsdo3jU-te3J3oYxclcw8YyBJROd2wdW96RRfei9RUjXLGB5DEyK6Tp_PN1UAZB-y0tV9aiyzcf-kMpZerysLITRQldbtp1cBvr8EibwuL6FFkJdNiNVv-r-AAY_nuQZnpPIatOT7LVE7jFUhMT3BK0OhsL2thorRA7vCCbn9rqI6fMvd4iwK-quW0Nc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YoqjBmPxvRAIvwUhwtjoR9j6FexkE6rkdPveynH_xTsYmbkAIlieIqSDf3LyGlLtGQo1rdMoQkgwewdALj_KbpbVyGjSglYKBYRbUDwCg6al2LawFV3xaRs-g95eNs6VjZSJPSOLhhuZZcrsK7iZ9aM9uRTY5KqIi9I5rzmVF81qhDRL5FvW_5i4lKsmAN3P3khAc0sw81zU6EGg8wV9tPgTH3LWLAvKSID0lTJ2wcGeGyGGsNbDpojD6apzNVfCrtVL_eW664g9fcy_ySpkhe_MVTX_gMfrt74dz3Ti9id3owU7fiymWT_qvn1ExzQFo1j0pIlC9lh6q4ZhTHiOvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlWODWKVQCuepxNNzWGRbH-NnW2pD__k_4drMeOnzySK_Z4_EK6Msr0sNqGbVcMH6iXHdgnr29FIXILJrjAKenKaz4ALyXMXZRVociGpaY9pEYGUWFdauzml01tiEcipAymW-MhfaXw6RNoSzq64lyxSABmtkomyxRMphyHRtzKukYCnf32dtXESSqc3xrukjYli-xNYThEXibmaTMcpzLwEAKvpSuvdSwM3WzCBx7Az9HVBmrKltqqhbpd6y3KmwLQlU8oTTMi4WbM-JE2ZOyU6uEK4a-IkZLB-oK8jIvUQDtc2oZBNz0nVzCaESSOt0xVYi07XASz1iyHckIjusQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=jublodssnu2tr24eJPIN6dpPvLVHCf9-yki0tz1bm_F1DSCc9SNhvEMn4Ksg1qxDbepLZP2gA_pvaMUDbh0j8AFB-fIM09rS5GXJypDUdmlD-AgR1dPEukZkn5wCXT6aQHO3UDg2mbvv1L0fPs9-Pw2udMyvZcMkswOspDHHYNPXI1eMNPume0TBB2v_ad-Pupwgfv0vjjTxfy145riQAezwgdoeVtNBIKRHgfRJZfPqenpI_zyUGsuJJTPYfh8il58ggkvXQlHh1_5bXSnLQSKEs_7nwGnY3ms7XWoQVmmLZFFlgbtumwhbc-q14J6rnrhWPD3Y-gJ1gO0ZO7uXIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=jublodssnu2tr24eJPIN6dpPvLVHCf9-yki0tz1bm_F1DSCc9SNhvEMn4Ksg1qxDbepLZP2gA_pvaMUDbh0j8AFB-fIM09rS5GXJypDUdmlD-AgR1dPEukZkn5wCXT6aQHO3UDg2mbvv1L0fPs9-Pw2udMyvZcMkswOspDHHYNPXI1eMNPume0TBB2v_ad-Pupwgfv0vjjTxfy145riQAezwgdoeVtNBIKRHgfRJZfPqenpI_zyUGsuJJTPYfh8il58ggkvXQlHh1_5bXSnLQSKEs_7nwGnY3ms7XWoQVmmLZFFlgbtumwhbc-q14J6rnrhWPD3Y-gJ1gO0ZO7uXIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlnTnno-7g4yQBUJnf1TjgNQxvRVim8PkIKaDP7wIOzyjjeURnaE18uSXjTQMsv4JQ8JeZ_eZIqn0mB3s89LCDgkFKoGOMveUU9UyH6igR5T7Gi8R6oIhhYIaYmHaa2gTZy-qFFawwNQm3SyFDgQr95GEQErCyBpFM_0PkMPoieGz1HKtdxmcegjBC3-BLjUb-cn7dXf3YNq79k7vjb4cy932Zlgz1e0iJXeNcfp3ajxIQ6aaIqM6ACrCPf7KfR_tFMUfq30h9WTKBrXvavhG7C7xmFFOv27xi73T47hOruqd0wlpyZAcRCkK65SS9YLCOnIsWR9gJKSbCFiQOHIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMjZ-3pUOzFbhvaPXQPrAnTQfuVTfWFp3vr8B8vnxeT6dDnI2Ehf_4SR-e_AsDzz6UXShcvSEK9qZky596uwYXo2Uuwb6WRFaCeq1_fbusOLQSdEEbZT3onmWof7vXio8cJZ96-JlwaNJ8SoblXQDaZY9H4f2ENdE3oQBtQQ9z7Lx8Hm3m9HfTHrsvJ6-LB1R1OknpyswIlX8AxrXrzRudluhhX0jmY1dZvxgsyZCB_PGQd1Ngqyk9ZC2bX4c2XwQe9hAWPhtLFPKSRYLueLrB3emWY0jSq_sBDmi3ZG13ImtklGJE5sRdh0KUSd12p7O2SXj9frJ6U1Vr25Jo5pHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=fNx8q3w7kSu3d5w91Ida22pGxVHSXidWAcdlTPnZ5Dc7VltUxs_iouqq8Phg5Vunid5PIDxAh2mLBlI1gyg93zgJqeiduVyHl6u-fWdZPfKNLaTcZ6MRxHXBIkVTKdLRZC2ubJI_9Sn4IQ0Cpv3axp9-ajb94CCWjWewvw4wX67IzSGBJhKZ2EyOF8xyQ0Qg3yNkS7Qu1CersoIaIBi-d_ypSMyFXcD1diLGZcHbA6JjWujISflnnXSI_7GZhMT68ToOtOVOEFfEQ-iuYRuzx7Zdf5eAmvbx_GJ-SBfebYkFI-kzpy06kaLwU0pdLasWu4oFEP1bXxbvqMvhhkaviw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=fNx8q3w7kSu3d5w91Ida22pGxVHSXidWAcdlTPnZ5Dc7VltUxs_iouqq8Phg5Vunid5PIDxAh2mLBlI1gyg93zgJqeiduVyHl6u-fWdZPfKNLaTcZ6MRxHXBIkVTKdLRZC2ubJI_9Sn4IQ0Cpv3axp9-ajb94CCWjWewvw4wX67IzSGBJhKZ2EyOF8xyQ0Qg3yNkS7Qu1CersoIaIBi-d_ypSMyFXcD1diLGZcHbA6JjWujISflnnXSI_7GZhMT68ToOtOVOEFfEQ-iuYRuzx7Zdf5eAmvbx_GJ-SBfebYkFI-kzpy06kaLwU0pdLasWu4oFEP1bXxbvqMvhhkaviw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=h8OyNPlmQQ1OeiBsPMYSZKQYgMQdHlfTsw2omo71mAKYYZKYBqNCa2O_9t0YrpueI5J5BBLmIyrDN39cTRFUmPdJ-jmnXyAKtOeBTXcLOmw6-oWSQisP3ezoDMeFi-KtJzcVVyZJtgjuFxJ2Ag8hNCgT8GicyVMAQvHrjXLYGrq1r-TkSn2OS849u7Y1Y8GdhyqD-zJyNIdSADRPWMlNtde5qVX12MXHMZs-X2p88s-oT5T6iF1VXtQERSVLSZUqEXudhevAi0t6_oOWMi-5AdMhv6mrO4pHJgbdYx2ac8QJCdmJolsLFyyY3J2bZog_pvomuExJ4prqYGdoegy7LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=h8OyNPlmQQ1OeiBsPMYSZKQYgMQdHlfTsw2omo71mAKYYZKYBqNCa2O_9t0YrpueI5J5BBLmIyrDN39cTRFUmPdJ-jmnXyAKtOeBTXcLOmw6-oWSQisP3ezoDMeFi-KtJzcVVyZJtgjuFxJ2Ag8hNCgT8GicyVMAQvHrjXLYGrq1r-TkSn2OS849u7Y1Y8GdhyqD-zJyNIdSADRPWMlNtde5qVX12MXHMZs-X2p88s-oT5T6iF1VXtQERSVLSZUqEXudhevAi0t6_oOWMi-5AdMhv6mrO4pHJgbdYx2ac8QJCdmJolsLFyyY3J2bZog_pvomuExJ4prqYGdoegy7LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=OuZawyDo50OijGB7XzKgsg-lcuaoSMJNEGOJjXmQ3w2dV_Z1U--pD4msSk8iTMqdygXUK7z1JvTRBGHlk29dXoAfd378HkcvZroqJMmCdI4El2SZLnAIX1nWsKlswXwFYVgnqeJnL-TzojVyXwnVCziVhrNszQXnUoJw6xQ2GzjBe2Kocq3d7OD4B1C7ugqcOAndr-9arVunzVMrJLrpwjVY9ypPuan0MJcRIjQxNpm66CbkuosT0NvEh1VqC-8BUrkYqT4awF700iyoAFFdTF79KbGJf9K5pEe10uaYIMULmMSELXdbPYYR0g5il0V5pQ7VCb-P7WKggyo1Nto8eoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=OuZawyDo50OijGB7XzKgsg-lcuaoSMJNEGOJjXmQ3w2dV_Z1U--pD4msSk8iTMqdygXUK7z1JvTRBGHlk29dXoAfd378HkcvZroqJMmCdI4El2SZLnAIX1nWsKlswXwFYVgnqeJnL-TzojVyXwnVCziVhrNszQXnUoJw6xQ2GzjBe2Kocq3d7OD4B1C7ugqcOAndr-9arVunzVMrJLrpwjVY9ypPuan0MJcRIjQxNpm66CbkuosT0NvEh1VqC-8BUrkYqT4awF700iyoAFFdTF79KbGJf9K5pEe10uaYIMULmMSELXdbPYYR0g5il0V5pQ7VCb-P7WKggyo1Nto8eoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=hmmB5fT2hZsezKq2x9GHaC8Li3eKhsb0kOxpf72HJF3aZKOQF5gLj0vhPXEo7J8TaLidql7g-6Bflhuk9jUMk3veO6fjpo_lJ8QMw9AVeCSqX3KcnwiS1b8X8sGEk__J4szo1eBPOMDIUPC5N417hb0QWKqPDVxFS4Bh5QjZ-vhswGDNSCs-TtK_i8c1Fty-TCO8an9-cy8lYYUAyRAblfotoMfhKnLtjiKsdLKR6r3BojwTJKhspzWIwNjQOPhGpfz70QAX5AC-0VgEPZ6tCRVwgNaRdFb-BawruZ0mN0RqBDdannq3cp_d5m7s9-tmbDk3yTrBsO1Tmd7nEmS6aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=hmmB5fT2hZsezKq2x9GHaC8Li3eKhsb0kOxpf72HJF3aZKOQF5gLj0vhPXEo7J8TaLidql7g-6Bflhuk9jUMk3veO6fjpo_lJ8QMw9AVeCSqX3KcnwiS1b8X8sGEk__J4szo1eBPOMDIUPC5N417hb0QWKqPDVxFS4Bh5QjZ-vhswGDNSCs-TtK_i8c1Fty-TCO8an9-cy8lYYUAyRAblfotoMfhKnLtjiKsdLKR6r3BojwTJKhspzWIwNjQOPhGpfz70QAX5AC-0VgEPZ6tCRVwgNaRdFb-BawruZ0mN0RqBDdannq3cp_d5m7s9-tmbDk3yTrBsO1Tmd7nEmS6aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=tPnIdk370VMm94leH1rAOyBglDI5lULUpuCZ-XaYYQUK6WZDWg9V1vhog0HNFNx5kvA3KxsVUCPgl8WGcThBO8wZaeVXU2WTtRW1BHs2ex6zlM6aaAev0GkxhkoSWBjTEHtkQ2svDn86-t8aWp0Z1FPXZgoq6MEBklvvXIL2D59VakbmLyqeYLzfRhN-tEE9EDbfzmmttMT1tp5SbgjV4NkOnFBJyO3uCQZQxHrBeaxLKkJwQ4uZawAqtnU3iWmmoeI-cCSFnIeWOt5UoZtufl2Drv75dYLW65dlX39Qv9mnrAbqYxQvZ0BhcUY5-uCc584wdOKfio5hOcHaseCBBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=tPnIdk370VMm94leH1rAOyBglDI5lULUpuCZ-XaYYQUK6WZDWg9V1vhog0HNFNx5kvA3KxsVUCPgl8WGcThBO8wZaeVXU2WTtRW1BHs2ex6zlM6aaAev0GkxhkoSWBjTEHtkQ2svDn86-t8aWp0Z1FPXZgoq6MEBklvvXIL2D59VakbmLyqeYLzfRhN-tEE9EDbfzmmttMT1tp5SbgjV4NkOnFBJyO3uCQZQxHrBeaxLKkJwQ4uZawAqtnU3iWmmoeI-cCSFnIeWOt5UoZtufl2Drv75dYLW65dlX39Qv9mnrAbqYxQvZ0BhcUY5-uCc584wdOKfio5hOcHaseCBBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=ArSJ4W-NH4VCLjBqsXT3zWPWi9CdBDeTBeOx4G_d7IT18YvEI7Im7Gx4d9GfQb03MY5mYhOjQ4boy384GbJ3x7dKmiVAn5ucWlGyMSwcbRkD5VScdtz90r-0YHy1G2Xx7iLBp4DtTWWsWWeWLQnGQvvhqqlBPecoLlivLV8Q9IYfhXqNjWHEuM0xnjSI-R9W1q81RBIXAFuAuFg-tnCjo8lZGSP7c5rH5K41vlDf1RAnDim2rZ4mtdYb_AWACcIqu3dYBid40c4JVG9E3XMszEjkLdT_NBrm5kIg1vTrvQOat19-Qw6dWSZBkdB8-hl6mE0pSYmnhgMMySeNc-DkOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=ArSJ4W-NH4VCLjBqsXT3zWPWi9CdBDeTBeOx4G_d7IT18YvEI7Im7Gx4d9GfQb03MY5mYhOjQ4boy384GbJ3x7dKmiVAn5ucWlGyMSwcbRkD5VScdtz90r-0YHy1G2Xx7iLBp4DtTWWsWWeWLQnGQvvhqqlBPecoLlivLV8Q9IYfhXqNjWHEuM0xnjSI-R9W1q81RBIXAFuAuFg-tnCjo8lZGSP7c5rH5K41vlDf1RAnDim2rZ4mtdYb_AWACcIqu3dYBid40c4JVG9E3XMszEjkLdT_NBrm5kIg1vTrvQOat19-Qw6dWSZBkdB8-hl6mE0pSYmnhgMMySeNc-DkOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ax74ceO13Hn3TyjDzTvOuteAz27HkLNmfDE3ZC7KymMqdZV20LDOUP4vXLhm3Mo97WpVrH7cxLtnibvM8D1pja-GYdxg5NrlUFwARdpUwVA01MSO0ccUV8E3GJjQHFpIUIyDJHAVS0eIsRHSjoFhmpj8ZHqt3FYWQOhDtZols0IwEjhNlXV1VkKbf0kxCP367iETP_6cSJD_Fs9SygwMKJ4pMk8_PybXVhEBJHCPdpGcjgFPScSqUxjA0gyPJs95KS9j9yKQ-_LJrGkvnDzAZ7AClK111svVLA8j-MqEgVGTweAAIFhzmv-9-Y0mZd3Oh98NI7k0nkXYHPPflVbBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXrFJqrx5Wgw-Qrudh7S9whnc0-U2WlerAL6tIoTHj36Zo6pqxIQaffV71q00bsjXcVuLV7L1sBqq6T0ckiAVfSFE3Rw01Yt2g-09P15OrESjdSvPZy13kgjAxvpcZZpPgYkFFdkDWRsknr4ckRjBDhlB58XKwSVSwT5Zksqc8S1Cf-qrHhDR1W6v_DHH0pUtIxg02lBGkAn-7b-3pSLnHb2Dl9n9mQuWFYEZg5x8JbhYKn5XrURefmuBgKQiWy0fEH1cp-Au8cT-Hhj8kElTTiYQmgHBi_nKZjnRNmj5H8M3U_ZhVfcO6cuXTPQmh-aSmKWDJbjmDoLWiiLQmo4JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoUnSSJ4aMaZ2ekGP1t6ADRUGS3r8GHkLpNsi4rbCEyNPc0w4fHk3tFLM7aD3aWdYm-uVBhBkWIzF9JUcx3tNyJGawGOb1GhqK-Mw6fWBevjnI5JPO_aw6q0SSD6jP5luTpWNSi0AUv2_ZtlF1H_DrAY1QDwTjDdPLqws54cFx3_wWFREbFPGmtbLZdThEpOEjVEEc7hhaFq67UMI2GdPdSpewgDWlhOY510R1RU_y1gEky-BK8VVh6jx1a9BALrPpgNbSsb-FNBs13cpezm4pm9CFlV715pAdTxUyXNy6L8rBXhTRahXD1KpZ8cQynJ-ORq8jY8aWgzR3veLvHykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=Gnt0WtrqUXEPDK01XHc-o4iAIsSNnoK8LLR9v9I96_SsFhH2X0Q99kkgVQGvG24yNFdB5fBNbiKPBzO6muD2xtX8WffasXQlikLCtQHnsR0K826U1TMiLfyL8fge6JuMlne6fvDaYFfXtRVrPksAd89sZh0uNDpyFa2uTa8b0V9zaEM8Z3388DDikvwJ9EVQSOqgAL6q6caoONbjRdShdBaaHY-DkK0zItSXlo8OJfx7gfS_JzXmolhXTcFNgSWAqO8aJYuYm0X73I6N2gAOtR584D2lt4MF3dOkn1gR0NjsO1cUTA3a4mKqFTVGDiLVa72eOoT4q5SKVKazhpCdJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=Gnt0WtrqUXEPDK01XHc-o4iAIsSNnoK8LLR9v9I96_SsFhH2X0Q99kkgVQGvG24yNFdB5fBNbiKPBzO6muD2xtX8WffasXQlikLCtQHnsR0K826U1TMiLfyL8fge6JuMlne6fvDaYFfXtRVrPksAd89sZh0uNDpyFa2uTa8b0V9zaEM8Z3388DDikvwJ9EVQSOqgAL6q6caoONbjRdShdBaaHY-DkK0zItSXlo8OJfx7gfS_JzXmolhXTcFNgSWAqO8aJYuYm0X73I6N2gAOtR584D2lt4MF3dOkn1gR0NjsO1cUTA3a4mKqFTVGDiLVa72eOoT4q5SKVKazhpCdJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=b1dNWaEJq5l0gwl8T3pLeSVRh-wGMr_XNBY7tTuW2aWw1XFlbKxeKWbGWJWyxbmCaHmqGZaOYjIPDjk_NCThEJ6PJVIAaviPb6wX7O2JgrSG4rBfA3sAFJkCbPSxLDLR8d0UypgqZG8MN8L345TK9_yC82ved5v6N0vE8wRLEiC3O49byeSndvYD_101yiQhQxVOsgzxqDiOPpH_f1lq2_RobdYKV5BACVS7WlJ8iJ78t_1Ry0g0WeWEsvaubcbYn4iE3EMJJimBrNHAY_1RUdLnqOIbMP49QAnh5hKukpfk-GqMdjHDOaotMZ0k7D0huOGwhI_s0p7bBY7xrKcMbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=b1dNWaEJq5l0gwl8T3pLeSVRh-wGMr_XNBY7tTuW2aWw1XFlbKxeKWbGWJWyxbmCaHmqGZaOYjIPDjk_NCThEJ6PJVIAaviPb6wX7O2JgrSG4rBfA3sAFJkCbPSxLDLR8d0UypgqZG8MN8L345TK9_yC82ved5v6N0vE8wRLEiC3O49byeSndvYD_101yiQhQxVOsgzxqDiOPpH_f1lq2_RobdYKV5BACVS7WlJ8iJ78t_1Ry0g0WeWEsvaubcbYn4iE3EMJJimBrNHAY_1RUdLnqOIbMP49QAnh5hKukpfk-GqMdjHDOaotMZ0k7D0huOGwhI_s0p7bBY7xrKcMbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=NUCVpaOLzSTwjRsIkMRq3Qq3IxKiSpc_RyicOyPTKm71CNOt8orm4DUde-Wj7jAaOsQFW-xWmM0IMgyTWCk6CmHOIeZYeTe8ip8R1BQVGFc1sD6erwGvsrUImLahC0f4gY7ytUgRLa0B5PhVLgQ6X4gLPIMZXteyct6bdJDwDPSeY1PuNBoEOlxnTTOKdZDv2NDoMMU3SCsOVXngdJdlSzMjsiBcGrGsb6Oo28fcS4rv7PDm9b_mL90OozCtimm8brC16iuOWK7wiXZKx1ZPSL4nXDiXB6lqtkKZ6qAgn3BW8KZtzDzXhgpj1M2atqGDQKZJpU4LWAYjseKC7OllOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=NUCVpaOLzSTwjRsIkMRq3Qq3IxKiSpc_RyicOyPTKm71CNOt8orm4DUde-Wj7jAaOsQFW-xWmM0IMgyTWCk6CmHOIeZYeTe8ip8R1BQVGFc1sD6erwGvsrUImLahC0f4gY7ytUgRLa0B5PhVLgQ6X4gLPIMZXteyct6bdJDwDPSeY1PuNBoEOlxnTTOKdZDv2NDoMMU3SCsOVXngdJdlSzMjsiBcGrGsb6Oo28fcS4rv7PDm9b_mL90OozCtimm8brC16iuOWK7wiXZKx1ZPSL4nXDiXB6lqtkKZ6qAgn3BW8KZtzDzXhgpj1M2atqGDQKZJpU4LWAYjseKC7OllOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBOfoPiq20kNhDTilKGp08hc1rSJDUtV_E_5Jd8vUDcAsfxwFwHsNTcVPtG20mGS3vHbw8RaU3MZGorFXBpVkbgekhGaM1hNjOoZnAEW5lx5f3ibdVSkJzjNjjJyUX6Jsk8K4LNS4JbraH0-dH5Aeb1gGcu0-rs_JTC-oe63fgWR5cRXUXGGN-c0NBlT_u_j0QKnUpFoCETzXNglNP1Ua2ao8k_xL3551D6XvZ43sAnlaLFYP8XrgZJz_5402j5EZXa0ZYqGYXPB3NfpYYWe9Xl1t2j_lrMe-1vxyNyupeyCildWmDpqQ5miY96my2eioVekJK4KJiwksB8MmkyRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=gDeBYt_1HZScZ008Xus3wmp33yDhgX_BGaH9LaIRN8GNYPISFU1SQCO_OGks65FL0ZGTmArhzPeZtpDf8J-_5tYbpg_IUG2hRWiRVckVDiDTWR3wD36tjEBH0AvlfpUSs7U5pCQgDH_PTESWZ5DPMhAzVybN1mZ_s7X-Sdmeubxje9JpATFPELu9dUPZnh6D3wDgaNZcsy-O_0YQVcyv3-lDb3uoJt0YcitA6Ro4cME6721JotG4JJqLeXJJux63nk2xqoRoxgCVxZkKojDEiL-jsMNLqcY5TbQO8hqa8c_jcaWP-GGAjCRRzIfcCUb2Yb05x6dDhmOIsD6HJ2ri9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=gDeBYt_1HZScZ008Xus3wmp33yDhgX_BGaH9LaIRN8GNYPISFU1SQCO_OGks65FL0ZGTmArhzPeZtpDf8J-_5tYbpg_IUG2hRWiRVckVDiDTWR3wD36tjEBH0AvlfpUSs7U5pCQgDH_PTESWZ5DPMhAzVybN1mZ_s7X-Sdmeubxje9JpATFPELu9dUPZnh6D3wDgaNZcsy-O_0YQVcyv3-lDb3uoJt0YcitA6Ro4cME6721JotG4JJqLeXJJux63nk2xqoRoxgCVxZkKojDEiL-jsMNLqcY5TbQO8hqa8c_jcaWP-GGAjCRRzIfcCUb2Yb05x6dDhmOIsD6HJ2ri9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=IU1n92y05el1ady9t2zEH12qG-LJnvgK-3EHf6pDIz6sRp-4sfC9j6Oaiou4u6V64NYgP4cpKqpX0bXhpDjZpBAqVhaoaC5eMYr2juD1kSh6MA0s5pd9dlJ-NaWQqgG0pk8JIXyHqougNsjxaB4B8zyReQkVpUIlYdiPhioRmyop4TH-7oBIqHPsgk0zxfoLZUbPhwJpq6DPk6duSAUm1B7GXcIdVY6ZvZnMisXbPJc21dZ3rKrIvsnHznaz2zcPwWgnrcrBhz_2NcP_klSpohA5DDs2kCxr-KwuszAsWoiYuX9Q0IIKL1Rx4pneMQU0E8yjpFrHSBESJuedn5U9Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=IU1n92y05el1ady9t2zEH12qG-LJnvgK-3EHf6pDIz6sRp-4sfC9j6Oaiou4u6V64NYgP4cpKqpX0bXhpDjZpBAqVhaoaC5eMYr2juD1kSh6MA0s5pd9dlJ-NaWQqgG0pk8JIXyHqougNsjxaB4B8zyReQkVpUIlYdiPhioRmyop4TH-7oBIqHPsgk0zxfoLZUbPhwJpq6DPk6duSAUm1B7GXcIdVY6ZvZnMisXbPJc21dZ3rKrIvsnHznaz2zcPwWgnrcrBhz_2NcP_klSpohA5DDs2kCxr-KwuszAsWoiYuX9Q0IIKL1Rx4pneMQU0E8yjpFrHSBESJuedn5U9Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksu9htoyqm3ftSGfTkj_bDqGQikRhLvpafy6ur6FkrlxySewNvGWLHTqcvBbmK3P97ZEByryefmDjteNCOfCzYXzmSDgl-G2P5gxovL3ALxEwoAMIW35WwI8Hpx_336HrU1GtrLSPu8ZHWMQ_U3Bubq0BsjUt8qNkcR2ylD_neLlDb2fDf5yfaaMJVGwgwU3PG3MzhGShZQflSPCkWDoUSC3rh-cB--p3iY34qwlSNvy9eBK20wLtVEFWkJuaxvUx_PW0EbV-Ztr2vyY6b0QdJQPLNyARTH0p3CQSEzgxvMJH5K2L5qVOGGcaFT0d7U0Vl8Yz5GfAym_rWFavLWPlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=QlJG_DwaoRyV3Wd4X5GLbp9Rs4PKwaB9Xg6o-4i8y-1GvO5Bccq4_57Lb4ZIG4jzOiTHMypchd0LorKEAGq-0GvGDIWXSUTWij2cY9ymJ3Si2CoHgeR0htLkkRBr1nxTcmmeq4V0u9qpTHUva5trbGLpxNLl0HjkY-Az44AL3C9xOKmjugiGx_jzbEKjt3_AlfhN7-mLl9nObIYJA8ueeSjp4KvX6oDjutEIe2FifBgtry1-BpnE61AuyE3OydrTmH9Qnf5PoBVZr_n8ofPMD-ZBoJom33tbP6l-v5gCXI5EK1XBd-t-gyQzskLkV24-GnwB9t7j9eOsVtB1jADrYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=QlJG_DwaoRyV3Wd4X5GLbp9Rs4PKwaB9Xg6o-4i8y-1GvO5Bccq4_57Lb4ZIG4jzOiTHMypchd0LorKEAGq-0GvGDIWXSUTWij2cY9ymJ3Si2CoHgeR0htLkkRBr1nxTcmmeq4V0u9qpTHUva5trbGLpxNLl0HjkY-Az44AL3C9xOKmjugiGx_jzbEKjt3_AlfhN7-mLl9nObIYJA8ueeSjp4KvX6oDjutEIe2FifBgtry1-BpnE61AuyE3OydrTmH9Qnf5PoBVZr_n8ofPMD-ZBoJom33tbP6l-v5gCXI5EK1XBd-t-gyQzskLkV24-GnwB9t7j9eOsVtB1jADrYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=BoI7UB0WLGQIrW9ojuxV6otx2jW_gNhKJGCkQGTGcAEjLT6ovl4bplZPGBTFVLotuawvAzayIuqdbmZI0bPeP5Y2ks3Q3nd55uM38kIsU_m7lqB7o_IS8W1Di3mIuqehJug4ITbta3TGvK-5D3K1L1xT84nuX9PqRkcNldx8ornaTVVARqnj0fr2jNKLt5zozJf2_sK-pgFy3GvKKxKXLmal_jU386Kow5bci7PywGJQ2cdlVZ-F0qd2CWNEL_As3g7hml0K7GRZpYFbNlqyVGj6ronQ4PxO1XsQJq0NG7XIcHIKZM-rfKLQku-2-b9SWuz0nENqSHvJzbKOvanJIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=BoI7UB0WLGQIrW9ojuxV6otx2jW_gNhKJGCkQGTGcAEjLT6ovl4bplZPGBTFVLotuawvAzayIuqdbmZI0bPeP5Y2ks3Q3nd55uM38kIsU_m7lqB7o_IS8W1Di3mIuqehJug4ITbta3TGvK-5D3K1L1xT84nuX9PqRkcNldx8ornaTVVARqnj0fr2jNKLt5zozJf2_sK-pgFy3GvKKxKXLmal_jU386Kow5bci7PywGJQ2cdlVZ-F0qd2CWNEL_As3g7hml0K7GRZpYFbNlqyVGj6ronQ4PxO1XsQJq0NG7XIcHIKZM-rfKLQku-2-b9SWuz0nENqSHvJzbKOvanJIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=HIKS6Kyg1_PHxil1sM_KJdUPGdGHZNZ_uI9DYBPKpjiNaauhhZZH5v91CGcvX-jiPxp_JmoGJNKZw02snI3FvHrw-1OdHKo5jm3UkXao3cQ0Z4kbvWOtMe0RIs6zbxJCqqribm66K-hGqsKVrORqj8TYxv4WScpjhwC6uEI6Ov_7C0UXRWBA8tetI6ipDIc3m1_aX--bs75fcT2P9HnmB3hbEUHJcCH-rE3kZ2D32eAS6sNqqAxlYGAHzFQNMPPyNXOiryfbS2EQxH-ncG_HlsyQAaD2kgU_CwjhqDOKBBr0N5Te1YdVeh5UrtuHkBw772ocN7aMxQmTvs7nJ1Pg2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=HIKS6Kyg1_PHxil1sM_KJdUPGdGHZNZ_uI9DYBPKpjiNaauhhZZH5v91CGcvX-jiPxp_JmoGJNKZw02snI3FvHrw-1OdHKo5jm3UkXao3cQ0Z4kbvWOtMe0RIs6zbxJCqqribm66K-hGqsKVrORqj8TYxv4WScpjhwC6uEI6Ov_7C0UXRWBA8tetI6ipDIc3m1_aX--bs75fcT2P9HnmB3hbEUHJcCH-rE3kZ2D32eAS6sNqqAxlYGAHzFQNMPPyNXOiryfbS2EQxH-ncG_HlsyQAaD2kgU_CwjhqDOKBBr0N5Te1YdVeh5UrtuHkBw772ocN7aMxQmTvs7nJ1Pg2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUfCxhERi7IfUOWI0ovzZl-V8bQxdd4bHWVwQboUoPcBW_Qf1ouFWdqSGjugq7jDAP3kx_oVnlcfz7H-Ob0aQCeJC5l9NcU5syojZUzA_eXgN4KGz5ONi27Z9HMR78Lbb6I8f5Efw84rihE-QE4_EhBxccOuQ_YYQme24LXaiSdD1E30ICTaATfG_JK5slpRljyFxHLyVzG4aWNdpy10wmNCAzdzM91urDFvjSrVYLk6H3t6aTdHjC5nYAYd_qJyNSGw3Z-A_Oi8J2A8hq8ZF7JSCNt3sTdstffmX2IITkx6c7UFF62bQVF__OVHU5b-QuQq6TK_6Dal_KIEkHvNtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=B0r2j-gyuilSy3Wd-nUhaj5mMwnUihoPHnh78SDfczqEkfQwipPloLBLcRPUG5WCYTgTMwzlditlfYiFjpL1k6rMysVg7-zBlgdDrM8LF0xG4oVmZpi-sqOdphZ6-JONP3BeOUL80BgswDXzbF1Dr6tcdDfasjFsAeA9ZnLbH4OWDQ_ixzbEuxGiQPCRa-1xVz3Eo00F0SYW1vtOyaRHx_x1dAJ09EXPazGdXM2wMHpb8525Z3hDWyqkDk4dvDTAaKOw-y-CY0jeoj2ci4Qhn25wi6BnNxS8PZMyL9zPG86fA8Oig98UOnzZ8h3UDgCWrq3kPHrMwksCWGTwgp-FEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=B0r2j-gyuilSy3Wd-nUhaj5mMwnUihoPHnh78SDfczqEkfQwipPloLBLcRPUG5WCYTgTMwzlditlfYiFjpL1k6rMysVg7-zBlgdDrM8LF0xG4oVmZpi-sqOdphZ6-JONP3BeOUL80BgswDXzbF1Dr6tcdDfasjFsAeA9ZnLbH4OWDQ_ixzbEuxGiQPCRa-1xVz3Eo00F0SYW1vtOyaRHx_x1dAJ09EXPazGdXM2wMHpb8525Z3hDWyqkDk4dvDTAaKOw-y-CY0jeoj2ci4Qhn25wi6BnNxS8PZMyL9zPG86fA8Oig98UOnzZ8h3UDgCWrq3kPHrMwksCWGTwgp-FEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
مقدار قابل توجهی از هواپیماهای باری نیروی هوایی ایالات متحده (مدل‌های C-17 و سایر هواپیماهای سنگین‌بار) امروز از اروپا به سمت خاورمیانه در حال پرواز هستند.
برای توافق دارن میان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=S2lHQXCYhaMj3IoJHoD-kQxVgPIha2VWNexflLqIhO7AYpEYXmkUMMh5O20LACjXMH8Zafwtvipx0weZSR9mRuQ57UbIYTeJ3GyJ3WmrpCe0mlWXpXG0-MXip_LTou4vrfHyLsRGxhopAbXLWu9cW7INp5BOvbseyE9d8iUO5ZHNqlepbrRXg4r7_YeGW1tjJqkPiDJOsBEq_4pVl-gXe58_YtcS5-sQ02BSwe1YI4zbrif5-jt__Zocj59pZt4uLfevS4q03vRMFBbH2KYKMcfeeKC_063H-bdQUQMqMp1dE3y5e11Zo_qXuiqWArY5r7ReDwtxAqxefuwzHftSCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=S2lHQXCYhaMj3IoJHoD-kQxVgPIha2VWNexflLqIhO7AYpEYXmkUMMh5O20LACjXMH8Zafwtvipx0weZSR9mRuQ57UbIYTeJ3GyJ3WmrpCe0mlWXpXG0-MXip_LTou4vrfHyLsRGxhopAbXLWu9cW7INp5BOvbseyE9d8iUO5ZHNqlepbrRXg4r7_YeGW1tjJqkPiDJOsBEq_4pVl-gXe58_YtcS5-sQ02BSwe1YI4zbrif5-jt__Zocj59pZt4uLfevS4q03vRMFBbH2KYKMcfeeKC_063H-bdQUQMqMp1dE3y5e11Zo_qXuiqWArY5r7ReDwtxAqxefuwzHftSCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFtBE8S_QQIe5ALg8rx43mtVRUammOP8jwD7fSNACYdGnjlQfb3XRPpuRXfzI-JiKzx0gvxrR3qjo2ULDvL88yUAmgB0X0MShyiVrk6ArnbIg7N9rvJoB3YtcKWd7SSzy5QNdlgEEqpKejwDdmaDcKg6D2nYfvYZZfnayjR7qej9j6jyYwWp0mYiii09_UJOEUAFu066f4bCF4L3TS_KQtbumlZeDx1GGAdm1KyNl2YAHmHyc9wjVxtny5Fb35U72_W7DYar4uDRByXthpjtuiy_7CBgHvUOyg9IIGUOk54KI8xhWm4MNqeTaiSyPnHPaS5Qe1yGfh81GQbag5xD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gtFpyiVqTUaBqqW8ZPqAdIC13yMjHO1WBYkW-8OKaAdGvMr5QFZKcZ9IQN2pfr1PwztGB66mJ8r-D47SLneQChNuBQRalpNedmKxpEI4xNp6Rnsf3bXDi-kvoUfB5t9TfOfibF9NNG932y-wMAsaEY5MsX1mpuukvI33c_1pHIUsEUPZCCD010mPQYUJdbpN0XO4BUqlx4CdCmSy63NiN2-h6jlDY4nIGy7xMyPTKNmqpYVCsP2IdmaQlR1I1YHlEETj2kBf38OniRKipyI7D5q63yvqISMW-mDTt1lJVxkQsXWbm6xSVAsx0tjHUxoC6ZUJ842adIr77vXlHHE1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gr4JeFegkoxgasQcQWHWJsdjxwaqCeuQHfXAsnJJd3UjwTy5xj2rxaCBSSLD8Yio8rBfrBydulTrs9DPIrbv9s3RaoCe_o2sEn4jcLrkljVxfpvP2a7PS-PsVVR4nk4ErPdyawWNORksSJUjyzY0SgAtLox1VOr-7xgHqeTAAe-h2pkfLyhHIKfL0XK1S_AtfowPVvKxQgIFnkNBpIm9VOfznoYNKhtNwvYtLi9TSlA-7_ppGYe52m4yUbCBoqlFKciZSXPlaJ1cdLdjYoVT_6J2gvrG6u-qwqZqDCA6a3cCfbQVWDN00cIXnNYGqG__JYsFKxSQZdCUIWgvhbFQLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=Bnjl490LAV-SIEc7Q1yZf5kfCiXZ9RkdxnjeG_scFbmhExvJ-PZK-3dtNcqVKQErLKMiPdUyQGdZcwEd4xSp_lqPexD0bkXL7458Gzab2mDgbh5FTAHxCk6FdL2me9YcusIJq9WHD17RAkxHeeq3_Vi5g96la_SjWN3MWAtLHxxqyW2xopl_PT-V86gflgnDIVSOqF_VuoVcFLflJonqoASfTcQiGxh-zAvNWP2LKzErOyArGa621yYsc83jXVBlk_bIKqTMT5XhjO-ekojzqy15b5CvjW7S2FENbj9FA1yGl6i0RFDA8m0GfoCp1YCDfnpu5QlYhdSU85Sun0OTwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=Bnjl490LAV-SIEc7Q1yZf5kfCiXZ9RkdxnjeG_scFbmhExvJ-PZK-3dtNcqVKQErLKMiPdUyQGdZcwEd4xSp_lqPexD0bkXL7458Gzab2mDgbh5FTAHxCk6FdL2me9YcusIJq9WHD17RAkxHeeq3_Vi5g96la_SjWN3MWAtLHxxqyW2xopl_PT-V86gflgnDIVSOqF_VuoVcFLflJonqoASfTcQiGxh-zAvNWP2LKzErOyArGa621yYsc83jXVBlk_bIKqTMT5XhjO-ekojzqy15b5CvjW7S2FENbj9FA1yGl6i0RFDA8m0GfoCp1YCDfnpu5QlYhdSU85Sun0OTwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای تهاجمی اوکراین در یکی از بزرگترین حملات از لحاظ حجم آتش شرکت بزرگ تجارت الکترونیک روسیه، Wildberries، را هدف قرار دادند.
این تأسیسات که در شهر کراسنودار واقع شده، به‌طور کامل در آتش فرو رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=QXUzpnYsVgkWJN1iZCF2K55vAJRIxT6JZwSzUZt7_akA6n3FzR6oK_MKTPA36k8Y8lCeoLFoSwQNXZ5oS4V3qhl-GpTMKnukuIcn_4miorndGfdZOu878re1VB2PPd8YDkKYlTo-QTPK7HDb1lMOjsCl8iJj1nkq4T7YYaIkyl8Ps5ErYUVZ6pEeJb1IKsALNxJkU3EOJMEvHJRVORuxJBdlLC7nxEjcnM95-9p0z4v2fOINNMQGXOOlfnciCN8PBlVdXb0hKm1bxjNqB868qTFCzkiFQgVnSAy-K3NrcEhwzs92G4FqvGGCl0EgvkUhoZ7dTkdYLQPoMxjwAvtvNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=QXUzpnYsVgkWJN1iZCF2K55vAJRIxT6JZwSzUZt7_akA6n3FzR6oK_MKTPA36k8Y8lCeoLFoSwQNXZ5oS4V3qhl-GpTMKnukuIcn_4miorndGfdZOu878re1VB2PPd8YDkKYlTo-QTPK7HDb1lMOjsCl8iJj1nkq4T7YYaIkyl8Ps5ErYUVZ6pEeJb1IKsALNxJkU3EOJMEvHJRVORuxJBdlLC7nxEjcnM95-9p0z4v2fOINNMQGXOOlfnciCN8PBlVdXb0hKm1bxjNqB868qTFCzkiFQgVnSAy-K3NrcEhwzs92G4FqvGGCl0EgvkUhoZ7dTkdYLQPoMxjwAvtvNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYsUSdjzeXPkGChUff1sIr3SYJok5N0eU4pm7S0R4EFrun8eFp1XJMLKxFv9UY5caeAdd5403qvAVJygQ9_QZpyZnXNTtQ9_Y3ijGnmcEz0DX_n4NWe35K8VB96H96WsM13fV6uxb6NCZCnZQ9yVsEragbitdC8mMZcKkjHLa-qfLmCH38HSVeczt7D1cyS7S3bZH_OmGWbfO5DBvQEo7uDPRznw6XclCWTsG8NQcF1rjkgzgl8tMOjo8sScK9e6WijmzBa7icbA7x4S00OcPdgkoFj5DVdWvvnPkMrFefrVDknCUfNFUAo-RlER5VT4oCp2qI9Sy_draIR4wrE17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=tiNIYrQE4MF6EQLhlTpO0FNqnIgrfS2gNNMrnO4lut0WxkbQiU3SsM4pPqy1cXH2E76EM6V0_9hkOp2ghJKa75NZdp24aYpVwke7c81SwaQQQra_mjipK4k_ka7z-YktREJ7Ed3iRBZnKRupH-qi9Sx9J77hdZtdWvfcmoAtjZPqKtJq6xbWiDk1Efbp_Bu3lQ3Lph0TZei9kRtrXb5yIeZW1zDWPscT7-YRcpYUtZIpAgZ9Q8h0y-50Pjdeyd1b-eUi-GFsu3Sj7J1fmuusNdlPq1D_2LlBfBlA-D3o_kzjTkjoFRHjokA_uq6GFc0GiZf5WnAboOEJE350eVW6ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=tiNIYrQE4MF6EQLhlTpO0FNqnIgrfS2gNNMrnO4lut0WxkbQiU3SsM4pPqy1cXH2E76EM6V0_9hkOp2ghJKa75NZdp24aYpVwke7c81SwaQQQra_mjipK4k_ka7z-YktREJ7Ed3iRBZnKRupH-qi9Sx9J77hdZtdWvfcmoAtjZPqKtJq6xbWiDk1Efbp_Bu3lQ3Lph0TZei9kRtrXb5yIeZW1zDWPscT7-YRcpYUtZIpAgZ9Q8h0y-50Pjdeyd1b-eUi-GFsu3Sj7J1fmuusNdlPq1D_2LlBfBlA-D3o_kzjTkjoFRHjokA_uq6GFc0GiZf5WnAboOEJE350eVW6ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=D1n0X3CbIXKG_90aT6kk7vTZflVDxhvm3F_wb5HmO6_8ICGEgS0aslSsUDdQoJcSg_RFGYi5TpRPNBuINISsbjue-PJK0C4S-WDnmz-J02yptUr6G5RM_EvpTm2DtBX4NNNKGcKCjqYHOaZ5mOmI3eok8GUOztOUBVbE-vels5pa5LQlsUPbA00DYVx4_4i12diiLK8QveC_lVSqPe-Fh739N5AmQS18UiicxdaX12twaHqBtn1cqptnJdfnOGAR4DBWETOQN6JM47j4UfJ-liVC-G0PMEGF3UVAdm_qDakQ4CaU5QF7hu5J1XUrxs8P96QTdd0QGsUjByDQSJspMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=D1n0X3CbIXKG_90aT6kk7vTZflVDxhvm3F_wb5HmO6_8ICGEgS0aslSsUDdQoJcSg_RFGYi5TpRPNBuINISsbjue-PJK0C4S-WDnmz-J02yptUr6G5RM_EvpTm2DtBX4NNNKGcKCjqYHOaZ5mOmI3eok8GUOztOUBVbE-vels5pa5LQlsUPbA00DYVx4_4i12diiLK8QveC_lVSqPe-Fh739N5AmQS18UiicxdaX12twaHqBtn1cqptnJdfnOGAR4DBWETOQN6JM47j4UfJ-liVC-G0PMEGF3UVAdm_qDakQ4CaU5QF7hu5J1XUrxs8P96QTdd0QGsUjByDQSJspMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__C5vxpxmyrYr1jfJ34K5GRkRZ48nK3GElKA5sO9szwDmitt7dnnRM3R5t_vOVuJOOD3IScBgM0q5dZrX-mO-p2xITGzWjpkK-SUDOtQ9BMX6nG-kZloC8kZXZ_HbpAy96DWoDIvGBorYTsbtVcsoEHQxeWIrEBTZ7KJT5ZQSSRGbqt9GxRAI6zeQmi3e9eHhVIomjaL9x0mrFYzds1yZIg5WyJDu5SlWYoCF9ixxUnJGmOuN0y-oVXWvxdwiP1oEon9h4zc6w6MNHHC3feqmJl4T9MXubcAfL35XFiQ8J8QbdoTPLKLfi9IdVgxu3NaRnzODPgS-eDKxHJ3xAS9UkCE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__C5vxpxmyrYr1jfJ34K5GRkRZ48nK3GElKA5sO9szwDmitt7dnnRM3R5t_vOVuJOOD3IScBgM0q5dZrX-mO-p2xITGzWjpkK-SUDOtQ9BMX6nG-kZloC8kZXZ_HbpAy96DWoDIvGBorYTsbtVcsoEHQxeWIrEBTZ7KJT5ZQSSRGbqt9GxRAI6zeQmi3e9eHhVIomjaL9x0mrFYzds1yZIg5WyJDu5SlWYoCF9ixxUnJGmOuN0y-oVXWvxdwiP1oEon9h4zc6w6MNHHC3feqmJl4T9MXubcAfL35XFiQ8J8QbdoTPLKLfi9IdVgxu3NaRnzODPgS-eDKxHJ3xAS9UkCE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VErvo7cWDO0083d3k0riw_iIFDF_ocJqGa54VOyvqrFvpMh18Cus0mqEMX5MesWGBvJmxZiAUFrDISQhH0p9atjbP8pUlU2gRc59qVh-_QeXgvz47JlVg25HoF6IqqSWI2VhnMwf5N_4VaPMdu9jWG_lVoBG-ZGOSA1QhUXNCuGTeeCP7UcZXSQbb3RGYOPpf5qVZYODEWmoK-uY0RoThFBnr4Fhd3F-XjtfiprHbGBh2xJYuUFQnK6uJa6wQkEkc134TeIljgdDmCxvC93w_yV2iLqqdjCl06dR_ZQwJUUv1gwBk4chmjiWvifr0FmEsthl848Q1rNpRrwC1F3rfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExzOqSE8kSBUvG5zsWU5v0xzXgI57npnk9mKIVts_h8fSDUJ5S-AhJdRZ2tqgw-SJeygJx-5OiWvmFW6MZVreSvYIno99EEQLRpVcjvtewmBCX6ALriqROkS1Z790v7jJ2ESvCTVht7Lgn9J6UggsEYorvxVIW9TlCVyEMUEtzXM0htwMZYWStXAKyCY2hZw6sNfOJPFTR7bK6hI00WG8EarWKozEsQNJkNY8jwbmIwzs67vqnRITyJI6zIUQhHyoH5LbDv9QZKAB3eE_jg0G5brN3eZAicakrwHpt9pe1LRsiP2xXmSismkziZMjdz9eKrVIGKMXyRTlWFHPgN2GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=DJqdbDrpaXzvc4BzfL8lmBKf8aaHzRVqWV9qwtwDgHBFs3p5fMukbBzJv_Bf5YnWTrNoab5fO3sKxHxlt5UBcv37rvij3_3hreetbnY9Q5dvbFnxRnTTjCzaaEm8K56DopX6jKQTKuYDa6z4AumgC3-Z1rEd_79bGKLLb-DbWKVrSFOK9xYAb0_-SYUxQofNeiXeMSua2EKec3jrFPJKgFuc3iKZSAtd2r275whHua3NRfffdl0czlXlOt0IhUhbsTRf6wzYdmEzONT4nXeJjTudSbeyHiyAcJK_uqRjIH85mEQRPEKolf8RiLNScmnj8CBIOSx7pBinTtZFDs-vTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=DJqdbDrpaXzvc4BzfL8lmBKf8aaHzRVqWV9qwtwDgHBFs3p5fMukbBzJv_Bf5YnWTrNoab5fO3sKxHxlt5UBcv37rvij3_3hreetbnY9Q5dvbFnxRnTTjCzaaEm8K56DopX6jKQTKuYDa6z4AumgC3-Z1rEd_79bGKLLb-DbWKVrSFOK9xYAb0_-SYUxQofNeiXeMSua2EKec3jrFPJKgFuc3iKZSAtd2r275whHua3NRfffdl0czlXlOt0IhUhbsTRf6wzYdmEzONT4nXeJjTudSbeyHiyAcJK_uqRjIH85mEQRPEKolf8RiLNScmnj8CBIOSx7pBinTtZFDs-vTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFOZJT83wKJdvzRFoqE0DyzpAOnG9iK5auG883ULjuWBxLfokfVUKrzIHiGxNzUBzJSiTuwQzp7qrLTep9GxLE1dEvveuE1Hj2M4DVUCQl1fC_o1KooSI6toKlWkMfCxk2DEkQUeznTzgqY0nRGrqvDc8cbT6r9-4HTxCOQHfk-nztyMlaUCzDq2IO3m3BtXtn10PXxdUD5Zw3i5Tz6OJIkzqUhZxR7i1zf5uHa9cmxQ5evGIBb-kv16vcq_3dNfb5FG91ZjBVkBNQWhpOcgEetI4J5WCDC4Fj1li0ZtD2r0o0WjWt_AzEnqOmpu3t1KE9z5UXdcUZsxl71mP_RajQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
