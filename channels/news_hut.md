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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 14:22:34</div>
<hr>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=MHnevhGAXkWupFc21c9wSAQtHC8R_eqLaK45ptVQ5PwV1nu0cICrIAWD0U_92ALZr8k8VBvgdLv23a27lal0C4h2WHsMsOPQwDM1OkvBwza63aJmgNnAb_RU9sYh4rtD9m48JlMVkRDswjufV6v8KL_ELow-dtJ4YXOxpILwzq_zTSCxJAmtZi0EafgU2YwGJlcGqwg3efdTRM9ZSVEnDon_4GFU60TC4VR4Ylu_jr1cc4xCCCk4suYbmmcdBs8k6sWhwaaQKZdDBOzLgibQJq_dKDAunKVXUTRpVsQZIVzxvQKYjI5O1_m-lRaq3Wzd-u2VC4JJx1feqaovx0stjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=MHnevhGAXkWupFc21c9wSAQtHC8R_eqLaK45ptVQ5PwV1nu0cICrIAWD0U_92ALZr8k8VBvgdLv23a27lal0C4h2WHsMsOPQwDM1OkvBwza63aJmgNnAb_RU9sYh4rtD9m48JlMVkRDswjufV6v8KL_ELow-dtJ4YXOxpILwzq_zTSCxJAmtZi0EafgU2YwGJlcGqwg3efdTRM9ZSVEnDon_4GFU60TC4VR4Ylu_jr1cc4xCCCk4suYbmmcdBs8k6sWhwaaQKZdDBOzLgibQJq_dKDAunKVXUTRpVsQZIVzxvQKYjI5O1_m-lRaq3Wzd-u2VC4JJx1feqaovx0stjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlaHPhx4-xCMeKVcpbu59G1NJ3OklrZv48iCBFj9Mf_i6BznpNgJX_hQyyUR-wq4rrx6qq1ebRPLm0IeXHeeXYvrAw6UMjF0zsfgls2MHhFtABSQZ-tyXHvKpj4AVU44rOnv8W-kzOaKBELt4LcbHciMWgJKEqGk6Ifb7us2ukizxFfDqDSWlnKnMGOqI9iuUALs1h-q7g8OpyiqC_G1XCzTtJMavgYnI0dbehOERq3veXJ5eTmTe8zIyhNh7sj5a9I2RCaEBC5ri3pLDo_ojF0zSL83ZmM_e456Udpc3kCWdeRGRM_7d-9c3Xh-vPeE9SCSuTzd8egwMv3gZjw5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvGz0K7XpgvaQxFRyCyWXWQ3UDmF4h2gMS8A1As14glMxi16DFJt6PIRBq07ue1q3VjRslbu2mlMxi7ekco8ErKa36ZqnY_TN9OXJkfPs-3sYr6dttFrR4GgD-EJDpWnXvoSVQAP1RCEyoFH3Uml-QaipD0ZxUXvLaTBXKpG_jyWQlMuceOvFrdxYVzYdJaWKg4Lt5AHxCXLx1YqC4cf3Xr8BGrgll2QIWAckzpbGZ66V6MRJeAYCU3NshkCzFB0Hi0saPb_TtZ884Gd2il1a9vKkIMNB9QqBAp8-J4MYj-Mcz-3V0lM1ctisfPr3fcS4NDlwpY1pnId4X-CVltUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9CZvSGD712qutDCEn-IWPe6A-_8f8LEDaqR-dMbb6NLy0hjLIcqjCwL-3Szo-4qBQRgMO7-dSqXtQNDq2fGI5nyYdpprxxIYMxKmxvzoSlKaJ656Vr1X3La4b76yktqXsrV7M5MhxpBA3NQheTWBFDADpRjsxNFtcVGDio09RAyUWRNEUes7hWeUFiRS0j_haXqFnLh8Xz4cMh7Tyz1F2pCh3fM4ZYB7WDMvgC9ZcuvvgqVRBAaggYce4QskGv5nJvMPEoHsMREYB-6xkas1v_UarhB2Y9VgZMHuJ8UKWV8AFfVEhe8Eyr5p8fDXfVhadrCQRtnW6_hOcdnt5qFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g57WqUUzg8LwHxQH3VGR2fBvYfyJv_R1xsqeLQG1ucOJp-mJPk0CdZhqTxy-4Ek5-A3l5UdLGB-LLedcnfWtCcf-nY-S0QtLypTtZhIG9ip7qMLoe3u6MhtJuG9zuiYGGjGdPQO1FiNmMu9v6S5D0ftMf-1NR18dB_0YtByfeQH3ulvHx-gD3QEzGMGI4wP7199i-aIREfdUGec0DggmSpE9Jhauvmeij8awIQ_1IbPvFU5_tZTK63BxOfLYJu7pMcbbxYWXinIGkwxPrWv9RXfKV9FnbRmSu0EUVFqQYHpfqR2g2ax7LOnFKuzaLBETqsgyuW9kYm7gm_l4Zw7Z4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGpCGD5xQCsEQ4kUQ_77MIELxttBZ7uijsFU5HJ1mBe9aXNJ-Ib-RJo5zXyOAmWCMmjXsjDeEDJCNaxT9LfYriJ3GPRWROTMJk2iRUOhTFpLb75fJrIN70q2cAkzZ0YYC24AGXVTCgpRPr9YOjxmXLxiOpqhXwR7vztxXQrEzod8XA02g1GcDa80mhTqLxIwv596C8Wz1I2sZXDkZ7583uSue8xahXWaGZDZoNgvgkuFzy9zpC0rT9XL91b6uzvYqkKewcMtKLNia2RXk5O5nh6oo0vTLLiU3jqY1-LoQzfHLuI3ELB8vmKjFdHOr2SjelobZSlytsREppL7VHoR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY2iY2032c8-Blgxzx_NC-nPqp6ZXmHRHKnRXryQ6MHMz5fBhEcKXkwx-M8WrtxsS-88dDh7_gzmmLVclC4vbf_J3cFlVH785bMsl7v4J_4l3CDFtBpN3ptvlYZPLmBjllZJYk-kjjYC_9wqk9JL8HFdO-XqbPmRcGp3huTa9H0wWb3Q7HrSCAf1bgDZ1WdZAVKmV2Gv4IE-meXpG0vtGF0V7Hc2pFTToNY_IJULnecsr2DYrv0xcuenYSu1XyVFGsS0B7ye7kUzGSrAMkcQByWOQBCcr6QuUX0DXQsWv3I_gEM1XGVUqoFmKa2xpg5yxUFy5NslM3cccsoC4Xvcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiTIvqjpeDRmUBybUp-t3ol7m0Xnx9_UTFjFt1H7_vU1LECwMRgN_cks5RgnfTWd2Rg4Fcp3-GHDe2OZn2yzfjqiUbK9wAty2iD8T1njvuchOEOpwPYsYkmrrPXcuqXscZZX2eXcv5TI3dm3J6a2l_hQPTZuinkFSzhVZcVKcoAPODrHmEwmCRKQxatVBG0RBlLB4REwYZCUjOUTwNHVGXZ4feDR2eXPXz2xUKiBniodM_dFVawFmvVqH40_J7yfOI0YKFaZrniVJHaurUaKd6PzWBLJ41y-TRKkpj9Jzu4318DDfCcAu9uN4pWKPjzlh41G3GxE-RbuBquFokD1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=ULUkeXo2wKYiWrY5H0pZaMgT6efYJBAkfaSTe9FdsJH4zFt1SwqNdbepJuR-W5XKHlg2fmTV7C6ZC4PiMdYrrd-b-pA_JtQh4RbjptjF3yVMVpVnLjlLjETVA0-ds_gD8eA0ZAV7CIsNb9KgZeAnuKSbWbZqI2F79wd9U925pv-a4xLD5c508qvhhWG6lUfivwkMj3wRxyKNQm04656LaIWhuNBaz5kBnz5GNEO8kg8NJv6Man9ZqJMRYVAxWTed41U_R90SM4gZv0yM0URAq6lDQY_8RPB4hbe1qawPXS3gtH5dBolwGTibgwljCyH2h4FkKxrImUVWvLe5eIQb9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=ULUkeXo2wKYiWrY5H0pZaMgT6efYJBAkfaSTe9FdsJH4zFt1SwqNdbepJuR-W5XKHlg2fmTV7C6ZC4PiMdYrrd-b-pA_JtQh4RbjptjF3yVMVpVnLjlLjETVA0-ds_gD8eA0ZAV7CIsNb9KgZeAnuKSbWbZqI2F79wd9U925pv-a4xLD5c508qvhhWG6lUfivwkMj3wRxyKNQm04656LaIWhuNBaz5kBnz5GNEO8kg8NJv6Man9ZqJMRYVAxWTed41U_R90SM4gZv0yM0URAq6lDQY_8RPB4hbe1qawPXS3gtH5dBolwGTibgwljCyH2h4FkKxrImUVWvLe5eIQb9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=aGkjPUmHMDgPhzrMbu7RrjdCrGMj6W8fE_xfMaER3NGgAFmVzsYEryoL2zZJX99j59fOq1SiM_Ou8MN99guGhvMvJAgVIXUWkB3WMUwNIGGQ8xRh4DiKt6W8aGlI8uPJQcT1Oofpls8FnrSk42qwfWPWD101YX5sFETkxlr1PxCRwLnUN676BHyyjxJ8-OcEJGVsJU1742GiVuxgVk5QDqsoP26HgzG7qJm-2hJQaFfwEg9xAsINv2xjQuyTRZRyfkaIX2Wb1iF1ADdPx5RP1E0PJrhmvQdtT-KAjdqQO-Wc1Y0m9Z71x-jpezy-ajfWK6gyio0dvyltPPqXcUOuSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=aGkjPUmHMDgPhzrMbu7RrjdCrGMj6W8fE_xfMaER3NGgAFmVzsYEryoL2zZJX99j59fOq1SiM_Ou8MN99guGhvMvJAgVIXUWkB3WMUwNIGGQ8xRh4DiKt6W8aGlI8uPJQcT1Oofpls8FnrSk42qwfWPWD101YX5sFETkxlr1PxCRwLnUN676BHyyjxJ8-OcEJGVsJU1742GiVuxgVk5QDqsoP26HgzG7qJm-2hJQaFfwEg9xAsINv2xjQuyTRZRyfkaIX2Wb1iF1ADdPx5RP1E0PJrhmvQdtT-KAjdqQO-Wc1Y0m9Z71x-jpezy-ajfWK6gyio0dvyltPPqXcUOuSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyFYK0nTKlJIyq9jqat86SfyjuEOj3_6d7IG0e4oRDGTsDIVFeO_F-Xjq0VTUxAjlEIXR1G4JXbX2vDaF13Wt3iZrjMLJEJFGMcP3KC1GPfs-NEsfryO7msywhupnMR_MRLVMDObr5JkTEpU0qae9JupWLmzkxzP7AKfIotmg1kiYmM7t_581hHnWM78dTUHjKtlo1Rg5ORbFVwQYjTnwqdSi_bmB2yBcu_DDzEruTXOKPG-GOiQrp8xjtSwQYRm1WAyHoxvTIOZh2zAkCZ79CW72z1joLAHz6hacBfFvfvX5Gsuhf7TgkCLGj85vf9wiXLdrw2N1UwONcZwEL53hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do-3LAilAcQQwVBj7sjCffFcAKLxt-lHIW0Qy8BrfqksI0pnuPxszcscnfC5fZeqdO7YzCO4GYhNRzu-LH2pi3fo4Jk-8vNR3IxEK3rVqVxG7_al-RM4_L-EhH2dm6IeH62MbRgh_gnrUTi57pJMQZgL2BFZwaZA8prxNxLHK4c8DLQ4HecS4dgThWNXdSqjBgFvOgM3Ty17ZEgs99n5y3MF87XuTrmmoDHj0zJwwvWvEbHMKuPLSFpaBkSlUVHrSrJx_QoeRs0Dz-DwxjCHivpi92q1IX3KA0WmfJMMfnE-nTzJv-dO_Y_O0TR9NNBlC3oH52mvawtPmR7wEGQDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iif_lo7RVklVypxLiYFzfW-sVuwg5hX5qpV5yEjXpfo8qUOtSJPzPlbmRHxtc-xVXg8dAKuk1GKamA88JkqxUncF0Lko70J5JkHQ1lvkaTF9wOwb7H1ApWSoThI7cJzSeDVXifpP2UZ2Wix2xzIcH5_at8wYdDN4UtdA8jDg3AiKhU_S1do9V2g9G6pMRadYr8ByvC3zhoTGZ2YzGPickqcBGuUZRnSDEhYI5ZOcKXYpYziYga7RQIlABjbUgGazpy7fuj5O1Wufc0-GBqpnWINyN-VaxoSvhmB7tFpjzJ_NSfQkFoyd2Qxtrs6YMyt8NA3CgR9u1a1f_YwBFtSH1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4YiGp_k0hWJTYW8Zl54a3ghhW8hDkTHM0sgpju66oWgRhSdcbGKLNH8M0UCg1cg_l9oW9nPox-segg9h2ZUprzIIPCX7YPJ5lSNpbbvG9k3uVztvJpXicwsTTY_HCV3ZQFrw4zwbsC1fa07MBrqDCE0a2T31vhOQLSQmk9LmnIzhv_QQRk8GTbcc8rdjRGG9qT-eQ7aEGW6BCEXJEj9S7wQ7SPRTVT4fhXlaiYomXFAuiboEGAzJeyX6dR3Mh6uVbtb43vngiJ2tuEzDMoMeXhvUitaiaMT4mD4BZG71NDmdzj1OQ3YP4WlyZJQ7ikyfKgmdU_cLifLiYwJ8XZAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3wP-PRjfN0rChdPj1lAaKMyPjEi5ity6ast4eqc6jV_B2cJLwL1xOSJOASUfqg-Vn900FZdJQR9Cl_rI28hulnThqRIcbOqxMuukrhZu-i3_KWtvJKUvqoUESngxmbIxC3tOTGWV4wFEbcOuzp7M8DhU0BuWtX1qhWQeH9KZQtECt35aix2gYxcy7yHtKi_0UJ1sTDoRGOW3IAUdpvTmerSmf5laLA7zhfQbRTK2mQPaqS5D6AqT8eR0IXHaEKFZHzqiHiGtSCmCGed5D3vqGGI3lUHI1BhMnvL5AadOw-j4Qg5ww76Uu64x1BiaYN3uK2uMdCsM8D5IfVb2xbcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=vcnaqZrx7wDpnqZQu6KCvzLjx84uMp_9ZNv8q0QH6rIohgCuPxRZwX9SqMUG9kTmsH6JtRdTJnbFdzdNt6j-Nf4dqSkLyRSYZ_Vn8xCXIIxETUmXkUOD364_zOxSJw2SDPiM9vd80U883wiBjvw4sXCde0sxx3auwPZJ13cCWOUwwhZdSq1frpsWYXooPDzU6flUiI2u4rKgbCwxo4_r6WkYYGhC6dkcLLnAdQaZ1K93S99Y1Xh2kNO1BUbJsKEIJ9SGs3n1gtX5_s4cL0v6X1e5ZKQQMG6-8D1TJuQUdumuT_yueyKs0syrizzfxphHq74n_4JiUHxq8FQKf-1SXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=vcnaqZrx7wDpnqZQu6KCvzLjx84uMp_9ZNv8q0QH6rIohgCuPxRZwX9SqMUG9kTmsH6JtRdTJnbFdzdNt6j-Nf4dqSkLyRSYZ_Vn8xCXIIxETUmXkUOD364_zOxSJw2SDPiM9vd80U883wiBjvw4sXCde0sxx3auwPZJ13cCWOUwwhZdSq1frpsWYXooPDzU6flUiI2u4rKgbCwxo4_r6WkYYGhC6dkcLLnAdQaZ1K93S99Y1Xh2kNO1BUbJsKEIJ9SGs3n1gtX5_s4cL0v6X1e5ZKQQMG6-8D1TJuQUdumuT_yueyKs0syrizzfxphHq74n_4JiUHxq8FQKf-1SXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7j1cuqm1yVm7eHKANsPjtLon_GD92Ph4FORrb0K8Z33zpqRdoCSCfETDk89xv7Sk_KXtOZWroVa-BAvs5vQZOZv0XCL8eHYVyr13rTuR6fkKraWD0mV5UtX0kximVOZAYgzvcopvlKBfrKfqQzynA_7tvdJm4xQnAv-BkxV2yGt0Wud26KQMXyVdfaORxa8nMf6RTYFGpFzoGtu9NkaqcI8I4E7xZr-jfc1so6y-Q56-HmHqOuOuUHzUfSu45awxbo4g4DqlftZM89P5XqubrCZBtFPqR4s1f4IruxLG8K6E6J6UMkpSdVdJ1fpGaIyrEjZc23p85eC8M3U8-KLqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftGNicAEqtNBR22ba__6ABNIFcoGHR3pL4sMDQCtb0x2JvW2hTy8l5AzZFk7kMa4esxs_ICDDt6b6gJtx9grElMePjmQAphuGO0Ah_4tOVkxS646DLS0fzH052eVyPCri3tHlGr-d3isQbtQCNroEO4OHfxrfCZeGCxvzcqsh5zQVxUcZwkAmKV5KJgDPJxdiYkkeDR5o3WNll1dtj02ssBVPGGauR7lAD8pkJU82Gzrr454w-3iWCfOtACO-eQTJh6ApvFg5G9udpWNGgQ-iDTjbEDh7i3I_6VeHI-WCzVTMJsNEP01ZlyiHtUQSqeJwGB6DXuKHfJXioqszygbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svkxCSd22Xjdjh0GNvj51ZaXpFUGqMrcjYBFxBELGcpIjnQbF5EJam8_HSsnnGPFeifU5OMoqFIqEz0re2dJC1DOE0wABwYOZQFwPxiMoo7ZzU-fdPBeHN4zs4YsubdQ_hfrlq6L22rOQQxjZBTUL0lWyjFjG1zYSzBMuQvtJ0g0v0lhYMeWoNYTzdbUlBipBDxSxDf1VV__hksGXuipQ6DiL2_dexdArb4r0Qn_JwScjhMlKHB4GH438KadG5mV_M25YDli5pYj9NR6nIPEN2S6bWYgKBRVA-JOi9DcwEGxeyDRN6K90xkX71DdJHkuij1QdQdy0b9dt-6_GMQloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAaiv7u-TJmtIcZhoXGuzl_3uBEcDAh5XMZfkSzWdXK2WmCBXKBmJOVEW2_P0-sV5gEmVtGzBinz_OHbvYF9Iua0o1xR4AWDWXJ3zkrZfx2ywArt4Un7BJ6sIbgXTbCUUAeim2Uur0zxP_-xugCcoCmAVDyUdStfTOdlLY43G-mNSQmaq191CHm6UnkSbqKEGiJFDrDqENXr0jX7G8xfUd2xD6MPmqD3Vov3eTq8Gj8u86XjiOpZw1f3xaD-CmT_NrJvfyRsBdwV-MsnepFUMEmuqHXQEkA81GLnrysTH_xsdhdIxKo2p1mHV4cQbw9_MmVobR0nfCK7Vp0l-3S7gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=V4yzYx2fACsCf6utQ69EX4gVZJNt8qKtuFrUdhktJVXYjU9LcRnK-FfzHDaDwjEoeNAQszw2i11saQMzqmD6R36u0iUb5f5f7016uMCMltT1SNCtsF8xxOX-8RZQ2PPp7QVGu0f_jfhSJqXxR3mDNDFgkKdsd11tXL_GQMSDkXoX6z4yjm45UkWW4HwsLPhhnXCIK8CYDooPBUrslonqtI13Nuc1k26ruMn19hJCc_2vKq90BZ9NOzxuJnihzmqKUDYITqxHuQbn5mHk7B5doDdHtE600oQTsb1YqbxpJd-nxIomAOf6M55m47YMRe9yqVAD0_JbsRwE7eqy2gnjQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=V4yzYx2fACsCf6utQ69EX4gVZJNt8qKtuFrUdhktJVXYjU9LcRnK-FfzHDaDwjEoeNAQszw2i11saQMzqmD6R36u0iUb5f5f7016uMCMltT1SNCtsF8xxOX-8RZQ2PPp7QVGu0f_jfhSJqXxR3mDNDFgkKdsd11tXL_GQMSDkXoX6z4yjm45UkWW4HwsLPhhnXCIK8CYDooPBUrslonqtI13Nuc1k26ruMn19hJCc_2vKq90BZ9NOzxuJnihzmqKUDYITqxHuQbn5mHk7B5doDdHtE600oQTsb1YqbxpJd-nxIomAOf6M55m47YMRe9yqVAD0_JbsRwE7eqy2gnjQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKShnUAGg8pKxfvSjphB-6CiLGJjkWJHY97yxjqeBIcEj49pqNdVUKNHohISnLQ7qHtDnNQU3z9NDyoqQ9K_wsaWITu24EKh3moRCXKSiJN0TqCizU9t1IEjlITOQQoyfBoVvscqUOIlN306jJezfLpXxQjCgdlc5hXBuN_JJLPkJRmpRQqLd1j4HvzI6cCnV6wTqi8ABlqtflNFPTxx2IaiVWaQyLHUPki3sEJL120AZ1JVnA4wyDE2cux48fofwleUohQXodHLhN65OXSZDXSVUrfxTotMLh81r6uUJVP78lu7siK1KEfTj7PbfyWKQc75dw4_qgS8rLSOq7Sfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=pbcKljkW4n6qhWMh4tyqmR47nTwKqTkd7Gk61RXpUmadi47qVGwfYRW2Z7fvMKVReXj60f-IJjSDLBDsFo1vDhUpaAvX0uP1F_KcBVAtisqKQIKopBc1Kn3wkQg2MSO4StlZqyA17f4oHLiXryEDESk5RR7uhKyI-pICbVdo6LwJ5cH5tWsmKPJJeXRfWsRMKeZTJptnHuKw7GoYQi7CMSlELBlTGQTRlSDERAyk06vugiDOLssKBP_JV_Ulh0WjMMYpPme-cxjKqlIvCq21LjP0Lp8hLUvQ4o5fImq2ox22rRW89Q4yyxixG-YGoYrrjJ49GhxvSjvNzQ6RAmPccw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=pbcKljkW4n6qhWMh4tyqmR47nTwKqTkd7Gk61RXpUmadi47qVGwfYRW2Z7fvMKVReXj60f-IJjSDLBDsFo1vDhUpaAvX0uP1F_KcBVAtisqKQIKopBc1Kn3wkQg2MSO4StlZqyA17f4oHLiXryEDESk5RR7uhKyI-pICbVdo6LwJ5cH5tWsmKPJJeXRfWsRMKeZTJptnHuKw7GoYQi7CMSlELBlTGQTRlSDERAyk06vugiDOLssKBP_JV_Ulh0WjMMYpPme-cxjKqlIvCq21LjP0Lp8hLUvQ4o5fImq2ox22rRW89Q4yyxixG-YGoYrrjJ49GhxvSjvNzQ6RAmPccw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=hJ1NmIT6tZEEGxbBtKbcB4fqD3YmyLJiNWgOW4ulakMcuMLJnvegyF-VDfQjd8oN8z-8m1-Z2HRjFiuqvBLt-JV9HUKxe2BhB4fyvPSp3grxjAg14Lv9VQYV1xswwbbubjagVWsC0Lv7WTw7rJ76fX0sD2gyiKUQYRIHtS83deXgA6a-UVzSuc7DQuR767Yb-uE6JKvWIR3tgn60MQL955GKZQC3O0ZEyah3NvbChRm4JzGBCP1J9_7r1WKme5LVJdL3I8ekbA3zUjVkNxD1Dky-X-46KTbXLdvcOZSkkOUgfr6NOfFGnPAWpiJiZZUJn0wZMzMPQV4AmZb7tzfm5YQ2mXlpCgKq5Rj5XDju2gQdekMrccB3w0Iu1BPLpQbe6p7j69Fa9p9fm0aCe7ThMIfnqizMLk0WBVFNiC2S01R8HTQVNryqRlzDy70jp0asZGvTYTGxELIobCG2GCgv5KhyS8SBr8HxwaaLCchviLAuG0STBVul5BFpWX70xNxzvuanr_z6zLtUYEPmlOdFdxkPUKfBqe7GmW6AEw0I2jpGmgANx5tdJGRH1R6wSNBeZl_8OsB5BIKG1rPds7XcrkdQ6QV31T8hehVkcbEOCmtZ1z-tD-RE-GpIyjVZlZIjGwBGpE3fGZzbAkoIHC-rfITaz-cwhMWm8Hgv4oxg0qs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=hJ1NmIT6tZEEGxbBtKbcB4fqD3YmyLJiNWgOW4ulakMcuMLJnvegyF-VDfQjd8oN8z-8m1-Z2HRjFiuqvBLt-JV9HUKxe2BhB4fyvPSp3grxjAg14Lv9VQYV1xswwbbubjagVWsC0Lv7WTw7rJ76fX0sD2gyiKUQYRIHtS83deXgA6a-UVzSuc7DQuR767Yb-uE6JKvWIR3tgn60MQL955GKZQC3O0ZEyah3NvbChRm4JzGBCP1J9_7r1WKme5LVJdL3I8ekbA3zUjVkNxD1Dky-X-46KTbXLdvcOZSkkOUgfr6NOfFGnPAWpiJiZZUJn0wZMzMPQV4AmZb7tzfm5YQ2mXlpCgKq5Rj5XDju2gQdekMrccB3w0Iu1BPLpQbe6p7j69Fa9p9fm0aCe7ThMIfnqizMLk0WBVFNiC2S01R8HTQVNryqRlzDy70jp0asZGvTYTGxELIobCG2GCgv5KhyS8SBr8HxwaaLCchviLAuG0STBVul5BFpWX70xNxzvuanr_z6zLtUYEPmlOdFdxkPUKfBqe7GmW6AEw0I2jpGmgANx5tdJGRH1R6wSNBeZl_8OsB5BIKG1rPds7XcrkdQ6QV31T8hehVkcbEOCmtZ1z-tD-RE-GpIyjVZlZIjGwBGpE3fGZzbAkoIHC-rfITaz-cwhMWm8Hgv4oxg0qs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIdRqujFUpd5LBourgL1qnunnTTsmaNaBPKQCzxLMTgVVFMUOh6hBTu22ETAmyFjFcc0w4OA93QrNXccpT9zGdSlB-gjIPz-6n9IUhLLAixo7Dln7EtOr3oXFUJpaFevI_imzlP-te4WIc8MqLUfuPVJxqDWu5lsNXS728je6WW5gaaAUATnbN0CL954Ku0nEf7LnSe5ss75MA4VEdhsYCyXbyvOsW5yt-QInJsHyRdZPMcZQM5V_XKJFiua5UTtPd_iC9R2odpvizCgkmSrdtKnGThA-HBUb0cbdCpDchvSmT_l6rCI27Erdrz6w71k2OJuNU8U0u9blRLvdA_bzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhiCDUFK4U7C4aCS6icEqWunng-NwvbMDiLScS9RYvY7HW9tSJN_HElOCPFVbZEpQAy8qYZLTdRbGjrwnoxETBdV9lZNnqm1lpBMZRYvjfZA7xvPEedPhJj17bMCG5QXq8SadivNYTX_j49JaYYg9D7CZSxat83yurhnuDF4uim-LeqhKyDC4vC9uJNT3Ej_fpeBEmQgX91mchZ3JUQsNrpDpsqAZ-JPNyz1t31_2N01i-IXjQTI-TYn3Ls0crmBec7NRysHCoKYrvMB8EpqWOPTBiXlt4cOb2XJVkMpfH0idfe7wdfpBCig47SXxkebzKGU2O0Tg7xa1UrAyrbr_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YoqjBmPxvRAIvwUhwtjoR9j6FexkE6rkdPveynH_xTsYmbkAIlieIqSDf3LyGlLtGQo1rdMoQkgwewdALj_KbpbVyGjSglYKBYRbUDwCg6al2LawFV3xaRs-g95eNs6VjZSJPSOLhhuZZcrsK7iZ9aM9uRTY5KqIi9I5rzmVF81qhDRL5FvW_5i4lKsmAN3P3khAc0sw81zU6EGg8wV9tPgTH3LWLAvKSID0lTJ2wcGeGyGGsNbDpojD6apzNVfCrtVL_eW664g9fcy_ySpkhe_MVTX_gMfrt74dz3Ti9id3owU7fiymWT_qvn1ExzQFo1j0pIlC9lh6q4ZhTHiOvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlWODWKVQCuepxNNzWGRbH-NnW2pD__k_4drMeOnzySK_Z4_EK6Msr0sNqGbVcMH6iXHdgnr29FIXILJrjAKenKaz4ALyXMXZRVociGpaY9pEYGUWFdauzml01tiEcipAymW-MhfaXw6RNoSzq64lyxSABmtkomyxRMphyHRtzKukYCnf32dtXESSqc3xrukjYli-xNYThEXibmaTMcpzLwEAKvpSuvdSwM3WzCBx7Az9HVBmrKltqqhbpd6y3KmwLQlU8oTTMi4WbM-JE2ZOyU6uEK4a-IkZLB-oK8jIvUQDtc2oZBNz0nVzCaESSOt0xVYi07XASz1iyHckIjusQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4njLac3TykZuMtRLaSn_8pGVQe0iyIHMQkDzAbVR9L7YRVh-gSmepAUiSNS0-BgEhGjlNGS3Px3kB494Z7xGNuNHlv0_V-OQGLXrTUiv8g_je2kBazLCY-EmKvTx2Ua9zgHNbkjxNMTUF-IBvY5cX1Du8qnms2rPsPVAmcLBP1PLg5dfpi99tRv4dMMNuzUXoaHG02BiM9bOEazps591VlSMsVSVnk-tKVr__AcvND6EjY9b8i9TeRjMKEkeSfxX6ZRjlWHtrHjPE8yFgqID6QdatPRRAxdz7nFq4OISeGkfKdEFHM69A8_YvvMQrZNIrxVgWYwly1J0qHeh6Pkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=hYbA2HaZEL-1fey26SYSg5qBLYN1RU-4Admz-HvgOXvQPUfvmc3BNA312jEUK-ClkcePpLQBhOEc2Bb9rqIEnqwcAOd-OI-BLrsHeOitLWAPPmqg1hkMOoZl0RdmnrnMVy4N7SO0MWjrY4xoxyBp_KOLVuJRIUhZh4OE1dY7Smr9kjxRqF4YHHtxhs5wA5cAzKDBdFy0OzXK0Cm23eefx-Y78UMw_xrnwGD8GF4N46pYlhV2Fzp7wlfxa6yTN8jaZmzP7mo4CdfKKuBVGlYAeC07LG8SwjtWUR7Llq0OKzI9BhWQjjCmu7o7PXozKQrWbkjx0tDGBG09XT9IeAs5dw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=hYbA2HaZEL-1fey26SYSg5qBLYN1RU-4Admz-HvgOXvQPUfvmc3BNA312jEUK-ClkcePpLQBhOEc2Bb9rqIEnqwcAOd-OI-BLrsHeOitLWAPPmqg1hkMOoZl0RdmnrnMVy4N7SO0MWjrY4xoxyBp_KOLVuJRIUhZh4OE1dY7Smr9kjxRqF4YHHtxhs5wA5cAzKDBdFy0OzXK0Cm23eefx-Y78UMw_xrnwGD8GF4N46pYlhV2Fzp7wlfxa6yTN8jaZmzP7mo4CdfKKuBVGlYAeC07LG8SwjtWUR7Llq0OKzI9BhWQjjCmu7o7PXozKQrWbkjx0tDGBG09XT9IeAs5dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyepaeIr3rh8jY71dB5Imf_QniBS5uKYgusvH2JWnTn3Csep-77WIoUCGInBSOjj-_39bUK3fbaVLLm-H65XerPNBIsIURpxHd7exZ_7y-zBpj7KFpjfOChWIuFcmLlWVP5NZLyg26cWjSS2iAIk0b6B2JsyDayufnxlIzDunIt0RjfW9QbLtuTpYc-LhdJhSioq2ddDFKnnWEBFFC-78Acwto3B_mglT7ZMsbC-SO_mmMAoxtc3ywGyFKhHpYPnUsMe7jL7PGLFvmdLcbEtxDUzTYdSpnmbQoExRu_eZADnwMWXKn72aohnOmI0-7Y54dSzF_g68oJ10JCJXuyTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGVd4xvDZjdz5tAySuaPwalt-C4ZrZ6q9YL55GSoQIMu6CmAacIkwYFBiBvJ5_rBIkengLueSpsdGWHn6TdD81p9XKX2mZ7XsnmA2Pij1KoY22C2yiZGMjYTcY9GIOgBvweyZbAf9Ja4RsuBW979vzXypql4ij9rFvwVJ4JusU6pa3WpnqBn16HUyGlSiCB9m-RGeXsu1EiPkTAzB8MPyvhCuhaFZArzkEgakeS8qmFbvMbPU3y4bL-4MhRIKn6qtM2yPzqIpSXHqvgiZ7-FY9yPE0XP95YMZvOic73EirDG8ARqlGlcAHE242mv1VxFu83sMbDWkZs5VatoSrobtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0QywFItsLdgyAFzAJqOncB1sNeYCxZco1yxmehPDkwcudYvHrLBuMB5Kms6jnfKU0ECPDib9RZJmg_TeQnw3L96Cv8u1sR1ro3QesfzDrHK7DmXq2STYnz7FT_D3AndP8mZ5AgG-7ocNL8s5YK16yeikqKNj1hV1N9Y5k-TjQCGFOPSCkPWDsWIKWP7ER-r_BReXiBsLkucaJcIymK-2w3vrWvG2b_xUp_1U5eXGk6FuZ3pPBhGQ70ntcfJhtufd3ak3C_7EXrd5110-Loc1xYnBW0lGx1h8ogy-fCsavAeRj7zPL3E-HN1iePkAM3S30vsPVw9Wm7zMv8_bqzXAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=qut5jmc6hjIpjBeAO23jVffV66RlUHU7wtLCNhYDk0Ns6WNEUiE9hA7F49YubQisuJ1sVoKCuXr0r9NIuUqS2aDNqF_By4LdyB7hSfP4Zb0YGndLWvLftHsM4Pg7kabljOqI_ks61l6p_QYj1kELtDltCYb6-1qxlgFrv9OpIA6gHIG7jdSnpAFZQojMgkfhMRG12wGbu7jX2tq7eqJLBPZn44tZMcpfy86nrQYBd7mqPGr816-0mS1ddhRPHCfCxI9Xvaqg1JI9g2uJ1yLgWGInQUQOxS9GWX6wpFJUOn9zc0YjfcBMyeea9yNBzX4uGJpvlhhi0IgPz575_qWW4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=qut5jmc6hjIpjBeAO23jVffV66RlUHU7wtLCNhYDk0Ns6WNEUiE9hA7F49YubQisuJ1sVoKCuXr0r9NIuUqS2aDNqF_By4LdyB7hSfP4Zb0YGndLWvLftHsM4Pg7kabljOqI_ks61l6p_QYj1kELtDltCYb6-1qxlgFrv9OpIA6gHIG7jdSnpAFZQojMgkfhMRG12wGbu7jX2tq7eqJLBPZn44tZMcpfy86nrQYBd7mqPGr816-0mS1ddhRPHCfCxI9Xvaqg1JI9g2uJ1yLgWGInQUQOxS9GWX6wpFJUOn9zc0YjfcBMyeea9yNBzX4uGJpvlhhi0IgPz575_qWW4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=HYhVqYCBAWycpWABcxLjD21osE5tknnGe3KwZIatv8mfBx6JmlC9cRAmqqCbrdyHt-GWQfNOQXiGoF82p5x1MmTX2QS2GzuJOTrpnnCkfzIhBttzJJVZYptRtPb4Kc7lxgM256aD98iUc52u0qbMMZVozy7QyYrC-bpokFcY63dzDq-FdFNrEjz-gfGuJoMpQQca2mU25smTZVLq1PrRlMeAUNxF6Mh_Z3AkXGSnLjZmKiHrwuICaesw4Ku_ZMS-NghFac2TV_U9JLtQycmRn0dKrBUU-sQ_2CTugcnpinTQT2MDNB8Ji1mE2fALfFpqpTPkSlDGRz8iZRztK80bcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=HYhVqYCBAWycpWABcxLjD21osE5tknnGe3KwZIatv8mfBx6JmlC9cRAmqqCbrdyHt-GWQfNOQXiGoF82p5x1MmTX2QS2GzuJOTrpnnCkfzIhBttzJJVZYptRtPb4Kc7lxgM256aD98iUc52u0qbMMZVozy7QyYrC-bpokFcY63dzDq-FdFNrEjz-gfGuJoMpQQca2mU25smTZVLq1PrRlMeAUNxF6Mh_Z3AkXGSnLjZmKiHrwuICaesw4Ku_ZMS-NghFac2TV_U9JLtQycmRn0dKrBUU-sQ_2CTugcnpinTQT2MDNB8Ji1mE2fALfFpqpTPkSlDGRz8iZRztK80bcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=uyUNYFCJpB4qYFtgDBwNKPIqmO07w0Z_0BQpyvofIm-EkGFaLvo_yBF-r9NKqojrxFRPGRGu2ZP0bBwo6uScyajT_QHG6HbHkG_A4ks5l2R-JD2E8_dWXsrbRQqJkMPbs1I8H7Ok7FHWexW_-TwFZ4BGKZfEf5yvSRs-XxmOH6PWd8ajQFkam6D3IkLE_A1MHeJwzfIse5Xby1Vobu7XrK0p_we3YjaTew0XjINECTvKYU7ja9E963v6k-mJdubDr2Ou_rWngulHNjICOfa-2WCZHx-fvatbcLU5xMB3fMRljSIlG-UhdIC9WUAxMRt0OPHfogbNmUgMCRtxcN3nWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=uyUNYFCJpB4qYFtgDBwNKPIqmO07w0Z_0BQpyvofIm-EkGFaLvo_yBF-r9NKqojrxFRPGRGu2ZP0bBwo6uScyajT_QHG6HbHkG_A4ks5l2R-JD2E8_dWXsrbRQqJkMPbs1I8H7Ok7FHWexW_-TwFZ4BGKZfEf5yvSRs-XxmOH6PWd8ajQFkam6D3IkLE_A1MHeJwzfIse5Xby1Vobu7XrK0p_we3YjaTew0XjINECTvKYU7ja9E963v6k-mJdubDr2Ou_rWngulHNjICOfa-2WCZHx-fvatbcLU5xMB3fMRljSIlG-UhdIC9WUAxMRt0OPHfogbNmUgMCRtxcN3nWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKZ1OixDQV51ynybvjmAKPp6zb_HuHCq4P7M7SgE2QlLRYV2cN__Ebv-GF1aOlh7iRZMBLayeBozifCBPhTpcV8ul-K_GzqDGu6QVDw5aptx4pNfmblooFoTCQMxCV_3ZyQ3-eSYAugrQVVkJ86o3bKV2RgZx8cHhQzokWuZmKIYxfrxQmH0Ki7uasEg32cDM-QUo6usp7_D7Fa4WIYmARP_evtnOj_EW5vwEn0BxRNDnHRaySX5jvpgildfA5fqKfpJDK5t8MsOmnj3Etg9qUihsAjK1BtbT0WiGeattXGNn5r5MMEtP959nwCu-SfsXxMluUP-3E_jN61Ig_MF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Or1INVCOgZ7QOlB0XZyzPv8neeuLcsb8GPUUM7OLS3LwxjZIS1eI7pVPw2mF-DIgW2wxbhlVChNbCRh-1HjPSFzNrbnt2ONSi8NanOwI1-pCyTummTSA0KDhKssHiKrPR91eB88rdiCEp8IduhAi-O7nAnZObvmAIPruqoPAA0qlJ9JXOnLVhYbMMEjv1L-pQT8B-tLB2Lck6aXC_rUQ5_T15YAlliZIkuHhH9h51bl6U71SJenROuOTEPtgOUcPYyScZpbHmplIk2zrs_T_fsujzp-IivWhGIyLZbDoTXPl09_s1VsG_Qyy-j7OTZpKYQHjykwJvqemptwNfv8zQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Or1INVCOgZ7QOlB0XZyzPv8neeuLcsb8GPUUM7OLS3LwxjZIS1eI7pVPw2mF-DIgW2wxbhlVChNbCRh-1HjPSFzNrbnt2ONSi8NanOwI1-pCyTummTSA0KDhKssHiKrPR91eB88rdiCEp8IduhAi-O7nAnZObvmAIPruqoPAA0qlJ9JXOnLVhYbMMEjv1L-pQT8B-tLB2Lck6aXC_rUQ5_T15YAlliZIkuHhH9h51bl6U71SJenROuOTEPtgOUcPYyScZpbHmplIk2zrs_T_fsujzp-IivWhGIyLZbDoTXPl09_s1VsG_Qyy-j7OTZpKYQHjykwJvqemptwNfv8zQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=koCEk_0WACrNQOeD53cCeijAI7KwnJ1PrunnXlgotHmoJQ2PS8rrBl7RJf2bCA4_Cf3jHkExns0sf7Y6jxAqRDO_NeDPZJNwkqF85Aj5v98PFguu74RXz14vKwmOYLtYojUeRHQx-hJLnZkbCCHr95rCXJNR-ZifQMGY8WcqqrqbT_OAZlKfYmRduSvG9kEQ2En6zdoRPiTKFB3Ugmgab5R7HqQqdDpNrwEk8tntRrQb9U64fB9LvjTreFtd0dSdAOdS4TeWmlWiI3mUQGsoDV1bno0nd8swSFCO4D-ADNgZ_GotQtNhOxuN_QC_eVQZU-1tb8bGPryttXelhnAwvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=koCEk_0WACrNQOeD53cCeijAI7KwnJ1PrunnXlgotHmoJQ2PS8rrBl7RJf2bCA4_Cf3jHkExns0sf7Y6jxAqRDO_NeDPZJNwkqF85Aj5v98PFguu74RXz14vKwmOYLtYojUeRHQx-hJLnZkbCCHr95rCXJNR-ZifQMGY8WcqqrqbT_OAZlKfYmRduSvG9kEQ2En6zdoRPiTKFB3Ugmgab5R7HqQqdDpNrwEk8tntRrQb9U64fB9LvjTreFtd0dSdAOdS4TeWmlWiI3mUQGsoDV1bno0nd8swSFCO4D-ADNgZ_GotQtNhOxuN_QC_eVQZU-1tb8bGPryttXelhnAwvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLu2NR9locaK21RuF8XKDgJkxrDS7dWKEGLCb9O-tGuHppRV1QAgLuYCqusk4LNV4VouuIomJpdBXE1bfi9eYkcQ7a3dyVWwmgFMyg_tfmQIDabq6yJ1KtSBzpBRpaytFxZZnfKcxKxMYpY3S0M83AicrBE_piiCHusAMntnmG1dbdwIOgWlh4-HBl4pu1c73AmZIvPq6x7nTjboVx5UliG7fqDC7iVSIvtpZa6U6Q4UxjwjHCC_lkbDfTx3IWl2oWG5ZknudH_8lt3dxdKsqi_rxCmzXDRBhxQWYV_K21SODBIcGZG_zdAMY_W_ee814Pyo2ZAKynrE0XGX5G6_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=HnuP7FIyNXGhs-zsnsZlrL9amZtjmoj1aTpXutx2Y9hRdRIcbN7oOfFUOT9zaYQDdPjxsV1PBSrmyTns66orxN6wzLNib-Rjngi6skuz3FxSglt35oSaIiOEEL5XhWpcm2fjbYSZXTUf6D62sOoR5vgpFXJVJKKTmuNExiLRMUWKxx1Ke9IRaS8Gv5ARTTXyCuNmyZFxAH3jSO0IwCzEO0JQcAfqvSCVo2dmxImRbH-cSmPiDIHK4w85bVekHD3cjU7KdV-D28QDf7AEU2IObydm2vVraK1pHr-qxbp54pf02tC5dQefsWf3e4EEa6xkDUJ7dpTUceu2YEeUxeNHKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=HnuP7FIyNXGhs-zsnsZlrL9amZtjmoj1aTpXutx2Y9hRdRIcbN7oOfFUOT9zaYQDdPjxsV1PBSrmyTns66orxN6wzLNib-Rjngi6skuz3FxSglt35oSaIiOEEL5XhWpcm2fjbYSZXTUf6D62sOoR5vgpFXJVJKKTmuNExiLRMUWKxx1Ke9IRaS8Gv5ARTTXyCuNmyZFxAH3jSO0IwCzEO0JQcAfqvSCVo2dmxImRbH-cSmPiDIHK4w85bVekHD3cjU7KdV-D28QDf7AEU2IObydm2vVraK1pHr-qxbp54pf02tC5dQefsWf3e4EEa6xkDUJ7dpTUceu2YEeUxeNHKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=sNwIZ-QOyoZ48hOtpUlSykm15INvITUPKxHO6J0ku2G0ym1lHC0WHFgB6nNiNrSUOuNBa3e1Dc7uppdAR3NSKCe045V4eE2f8bB9NXVXttt7AkdKhYYiBvg3p9ixjYMO6wbf9sKvLbbHPnKLWOqyZIMFASagTgh5P0JeN6i0hjeUFpnK4uK6hQJZovNsVrVO--U9WlCxxGLd1i2snYevUbUBNmna3n19xcYOFUaPe6liJXr1vF6hNxDaOKh3ZlLQ7q9ZXAagMAWFJsA6-jUPjtChzLFhxJquEW1JiKJ4AF-PYnT02cNoK4Q93VZ1QpeXxPbqeTXR1uExJNmSAKku0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=sNwIZ-QOyoZ48hOtpUlSykm15INvITUPKxHO6J0ku2G0ym1lHC0WHFgB6nNiNrSUOuNBa3e1Dc7uppdAR3NSKCe045V4eE2f8bB9NXVXttt7AkdKhYYiBvg3p9ixjYMO6wbf9sKvLbbHPnKLWOqyZIMFASagTgh5P0JeN6i0hjeUFpnK4uK6hQJZovNsVrVO--U9WlCxxGLd1i2snYevUbUBNmna3n19xcYOFUaPe6liJXr1vF6hNxDaOKh3ZlLQ7q9ZXAagMAWFJsA6-jUPjtChzLFhxJquEW1JiKJ4AF-PYnT02cNoK4Q93VZ1QpeXxPbqeTXR1uExJNmSAKku0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=bbDQjVYgbbbqO24gMTsLlMPA5eER6ZDmQQTaqDp00CsFSAzR3D-AS32fcdfNfc1KtY4FYN9OK6MkTrpUce0FQgODT9dnzlONmrew38eAx1Cc9duWigX5r39TL2Bhv0tUzT3hL5DO67uxhhGNtSPGythpYGHAddnZ9QvauhHQ_R52hbMDxx3gtBfV5hwf6LliggKnhyhGHWTA4nGIqCfGfAL8LT8LJ24BWFyo1JHRQMptmMfqHYdS4fE2b4BPlrPPdBRADDoS2Tc0GOGrE1UDX3CbXJWp5EUHk3dkDUUGJj4_cebImwYnOF1v_QRwbpkvNUdV9VT8UlFEUYk8Usui4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=bbDQjVYgbbbqO24gMTsLlMPA5eER6ZDmQQTaqDp00CsFSAzR3D-AS32fcdfNfc1KtY4FYN9OK6MkTrpUce0FQgODT9dnzlONmrew38eAx1Cc9duWigX5r39TL2Bhv0tUzT3hL5DO67uxhhGNtSPGythpYGHAddnZ9QvauhHQ_R52hbMDxx3gtBfV5hwf6LliggKnhyhGHWTA4nGIqCfGfAL8LT8LJ24BWFyo1JHRQMptmMfqHYdS4fE2b4BPlrPPdBRADDoS2Tc0GOGrE1UDX3CbXJWp5EUHk3dkDUUGJj4_cebImwYnOF1v_QRwbpkvNUdV9VT8UlFEUYk8Usui4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0BNCT1N187y5Zl4IDiN3jVNm3qUgA1nTok9FHoWBduFBL7ilL-pVoe-K3X2OcHaS_H8KpHWMZnG7OY0smZ86M2KBR1gPYkzzpSW6WBIJQFHblH3hekQDZZ6dT4ktdSY3cUbWol2c-XzmsK6PKpzfOPaLhJ253ovVr6e-6wzdplJxarWpFZjw6tHl-2UPA87W6KTkw6F3xQq5uUagf9ur_UrLY_7TQN31p3awj9OyvBqOk-1RM2iLCpP9lL50xMa3oVHzYeVaaYblov_A7YtTAZI8Tpw4H5L3Q8wNX435aONnBAIvTmqMiR2X0i10nHqb1jpcxVR0IMM4M1JyD3SLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=sShrxR9YjHwiOGMOZnXNS2D_7Fv7rTfSOZZqFQvcW9YKqsFcE0xx2OAsVpJWTrN2E6qy3yQcv6VYSKheZknqjrqNMgLJZU8gpF_LULQY2ArV6LY-hfEBweES8wiZHNAxwH40AvtVCzlfKzCwOkTYYOUp-MiEHOSjqVUu32gP-XcdKCd2t-dHssmziDlD7eQ_jE9PjK8GEjJwCQv9byOCvK5DiGzCRajxjqoGhODxAuQnhV8jKGQob5L62dkBo6vHp8tHb4TIkMCbd6go2m0prWS7wSReLDnjcvLMmQMU5LOLBJYqobxBgTz8FgTyV7O6ATULMv5gXDv9tiwLWnHSNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=sShrxR9YjHwiOGMOZnXNS2D_7Fv7rTfSOZZqFQvcW9YKqsFcE0xx2OAsVpJWTrN2E6qy3yQcv6VYSKheZknqjrqNMgLJZU8gpF_LULQY2ArV6LY-hfEBweES8wiZHNAxwH40AvtVCzlfKzCwOkTYYOUp-MiEHOSjqVUu32gP-XcdKCd2t-dHssmziDlD7eQ_jE9PjK8GEjJwCQv9byOCvK5DiGzCRajxjqoGhODxAuQnhV8jKGQob5L62dkBo6vHp8tHb4TIkMCbd6go2m0prWS7wSReLDnjcvLMmQMU5LOLBJYqobxBgTz8FgTyV7O6ATULMv5gXDv9tiwLWnHSNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=Uv9nZcHSiFuwgA1O2DWs-qfMy8TtTSYEito_MGCMNQImXDVMtTnxigJJ4Lut_MaEVwuPVr4MLFBgqiDBummXbhCfV4fBaJdjTtn6a1dS1loQ8KhEA3Z919KKmrArgKQUf6xFkM9sCeO9LAlss0RaYC9ZtY8SD-Syo9wQZjlve2olN73X7p0kM5DcLDJ1r2Plv1iABGPD6YsWIJ5H887fW97C7jjyb3LmgxdGP-nshLpgmgJGd0RQgaZsZsT3hUdsilbfQDUOBKf9bEOoS0SL1Ei79iBxmxTbKahVqqDraRz_V9BGGj-YFoJQSDJT_GXMLrzABNDQjNWQesYE06RM6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=Uv9nZcHSiFuwgA1O2DWs-qfMy8TtTSYEito_MGCMNQImXDVMtTnxigJJ4Lut_MaEVwuPVr4MLFBgqiDBummXbhCfV4fBaJdjTtn6a1dS1loQ8KhEA3Z919KKmrArgKQUf6xFkM9sCeO9LAlss0RaYC9ZtY8SD-Syo9wQZjlve2olN73X7p0kM5DcLDJ1r2Plv1iABGPD6YsWIJ5H887fW97C7jjyb3LmgxdGP-nshLpgmgJGd0RQgaZsZsT3hUdsilbfQDUOBKf9bEOoS0SL1Ei79iBxmxTbKahVqqDraRz_V9BGGj-YFoJQSDJT_GXMLrzABNDQjNWQesYE06RM6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR4_ZBxXi-9pCwK0rufQi52BvGE8ekP6OxW5uRlgwOXhfBG4ec1dDJTCrN7qyaMw97367rO0Fnj6HRaC26Mk4nY4LVcF15GQ2mZbuHfoVpm3nLnDfvz9vWflbxqZ3L2LYvrL-1ndwyU018V9Uc_fDAM-irOGejTe1pkOE35raronAQkhkY7vFS9WDOmKKURJ2tRAsYWWdpqZkpM2ukoiDMrZm3TsTWTj5FtAh5PQYFli5sLFkybxf-VMp7YbD7nCPXVK5mlYDDOrNuq8XX9AfcFZv3dznTSN4Z18CHvr3-d4L6LH6XxEsgMkPJpj5FbMuFr85nJjqILGUBdj7IgIdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JG15dAJ7vQ4Jk8rG4FdVNcUR-tGiOP20pkn4SomyGjefnPQa9eywim09lFXHmCyZvH-wjxm0XgwBpCvOD3DkbDLK7vy6q85CTrY_4a0h7vpj6SiwTwUGE3GfVXaldW4exRMD45a9qZU2ESJe85P5DNxHXSSoYxzIuPa79geKMocyBYWzXIxYhcHxJc-99pb_sPbIly2r8OmP-Fv7OHOims4fqKIOzjfmQSPh_oh3dCL1s4q-aqMbJlCnVLK0aNSaDE_M21iKHl7ALpWpRcj25Cg-7YaacvuSvaKQSlkbf3TBqd0Hzzh-WDspr6dj0ylc_tLTZmnJJZ2QLP6KJHkC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5Xf1QFmn_FrC-Qe7AWz771njtjqZfomB3MuJcZTwyGpaNcdOoBLJ94F0QesTTAvTi-f70PW2cfgkJqCt2H6YjFcHVP6ftnrArSVdi87FU7RzBX5UfGUhccfAt0Vj8iXxYV-Z9FHXt8YMMnUOqZu5cnvBBfolkEgmq7NFFfcyt1ENy_LjSkW_CFALDSlCSar79f7vWRc5z5wGYGFLnXBBO4VcmEyl4wOGtp5OcUAJHAsecwUbBcNfrXnXihcck5fN7YPYStR8WMLFUyPPGbF7EX0DF0YMYIgaW_xW3clbi-FWWKUkZNn_Ze7kJwR_7FOVCOP9YYHMu8M-WDCl7KdgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=h2qNufbYjtS_tLGRIBIgw9L7uO4NRui1EcA6diUBvDPSO6a60TN9XFN92Sm4ugGVekA65BaqnDuX3ugsiNOBfdZnok7OXPEBnJoAJogIK3EmQ0VbEVqyzlITS1qc20psj3zQjtrFOwj-YYoiiKnxq24OAHDfwDjizj62cYbNC5eAjUDQMqkyWWUjIcfyjrehik-gm-h0B-YVcGXhlfT9jEjEVGW1EplWvWxpe3I4fPZZ7b1d45oGlj4MlOH9wm7mgoHURzBScAQ1QwunlkPFNqCiyi2U0Bjy-AhQea6b_rG9yaZpiPELILTJzsBPQTHlpsxQepKi4bdL_GP0CQoAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=h2qNufbYjtS_tLGRIBIgw9L7uO4NRui1EcA6diUBvDPSO6a60TN9XFN92Sm4ugGVekA65BaqnDuX3ugsiNOBfdZnok7OXPEBnJoAJogIK3EmQ0VbEVqyzlITS1qc20psj3zQjtrFOwj-YYoiiKnxq24OAHDfwDjizj62cYbNC5eAjUDQMqkyWWUjIcfyjrehik-gm-h0B-YVcGXhlfT9jEjEVGW1EplWvWxpe3I4fPZZ7b1d45oGlj4MlOH9wm7mgoHURzBScAQ1QwunlkPFNqCiyi2U0Bjy-AhQea6b_rG9yaZpiPELILTJzsBPQTHlpsxQepKi4bdL_GP0CQoAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=DLV8GvWR7Txgm1fCXSwhq_haYVlhsbBjEs2rs85L2oHngERYNWACWR78svFA-IeQAw6pyBUYIztOgPEST5W9Ffzp8RdwVoyXTPxYwR3Tz1oTTuzJG5GhfHxNXZ5KOPN9dxVwJ9meMr3GAQ_p6_gPe_T-ahWeKKFx5d9fYAxMjp4nLhtoxvjVMuF1RlgIO3VefeBgXunYG2PJw20Gjfr2jhy985tlm9fhWS2YpGaa8tqc3Q4i9a96OVcPnF8vSVPZgTwAhrW94tV-VK_f4R1AF3yOfuqFolmz_VqfzD5JYAw7c1AlqS4E7Ka62myhlML3GKujvtho6OOD2xSpXZQZaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=DLV8GvWR7Txgm1fCXSwhq_haYVlhsbBjEs2rs85L2oHngERYNWACWR78svFA-IeQAw6pyBUYIztOgPEST5W9Ffzp8RdwVoyXTPxYwR3Tz1oTTuzJG5GhfHxNXZ5KOPN9dxVwJ9meMr3GAQ_p6_gPe_T-ahWeKKFx5d9fYAxMjp4nLhtoxvjVMuF1RlgIO3VefeBgXunYG2PJw20Gjfr2jhy985tlm9fhWS2YpGaa8tqc3Q4i9a96OVcPnF8vSVPZgTwAhrW94tV-VK_f4R1AF3yOfuqFolmz_VqfzD5JYAw7c1AlqS4E7Ka62myhlML3GKujvtho6OOD2xSpXZQZaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTAniZqMiE-3eGy_z6JOULh1FGqecHexk8BWzOya0q7dr8h2Wc6RzQbp5-4kD7YIMIXZfeFxqx26C3Z2-nu8yuv29ESFh152Cc6diOIuOdBoxMGHuqzAjSCXSveOXHnerMnzR9TOHDf6fm70AsvOMAlzukTodUeqoz-9Td8RmqOGbdttYagtB67zz1oGzJJdjZK0D-0ydyWtfiZ2E0YrGgbfY2OSpFhFgpPHYdoT5WmUu8kaRVLHLMx5lFRTuWi5R15SPNaBwsEknwpm1wBKrU2R-R9hrTqYLICJk_m9wkGRtNtn4H3IC3e08d9lZN3L_OhwdOVSysOmXw0dvcWQNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=DJBEUihWGX2pW23BAGIKETp4X99TSN8M5wMKQI8f-0zmCjuyemb3_5A5LWqrqzyLVTuOYDSeE7kieFmF9O0I_e4h7M9Sett1qZdNjSx4UCYU2v072maZheYeIH9k2RQSzMjt4-yUjoz_gwQdszS9tLJUy2i7DPac1jkPPj1wLD1cNgfl-84Tc3-jSU6gfCLssZut0SbFevZvALxMBnurK0A-yT2b3ix231DsVwjIKbOLA-5O76OvxAvOsovPuNLNvhRlQSFC5A6mOTxWDlTT4rgK1WU6V-C9xOWlc90OKa80-awK52YscTP4gAy9W9E8IL5YYfUuVIRpmu_Rpr-rRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=DJBEUihWGX2pW23BAGIKETp4X99TSN8M5wMKQI8f-0zmCjuyemb3_5A5LWqrqzyLVTuOYDSeE7kieFmF9O0I_e4h7M9Sett1qZdNjSx4UCYU2v072maZheYeIH9k2RQSzMjt4-yUjoz_gwQdszS9tLJUy2i7DPac1jkPPj1wLD1cNgfl-84Tc3-jSU6gfCLssZut0SbFevZvALxMBnurK0A-yT2b3ix231DsVwjIKbOLA-5O76OvxAvOsovPuNLNvhRlQSFC5A6mOTxWDlTT4rgK1WU6V-C9xOWlc90OKa80-awK52YscTP4gAy9W9E8IL5YYfUuVIRpmu_Rpr-rRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=omwvSL1xYPG9tDpKdcUUi3YB3RWySHutQ7pNTGJg12rnFm3N8LQI36M2Sx5EPSwB3Hy5DXHA3HF2z2XK8cHyiSYpcVpnT6WSX_VlvdRJ9OdAducGyzt7JFUwYPU4hcgkwPgQZBbGoEK2zCv5T1AFSJqAEL42XTXkasN20VGKbGf3yIAzI20rUBNAXdQ2_HRKPrLRt1R_IhU5BfVEOG1U58wJCfqe2o5TUkF7qtW8ESNOj6i9N9Vc1qOPShXBwpTuXn7k4FcmrToJrfriNZad4-qaC1lnfvJFYI0IAGqh1W02c95lJbyY0iZXfTgHbZ5Jihe_pZ1qgRUT8re7RUO9ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=omwvSL1xYPG9tDpKdcUUi3YB3RWySHutQ7pNTGJg12rnFm3N8LQI36M2Sx5EPSwB3Hy5DXHA3HF2z2XK8cHyiSYpcVpnT6WSX_VlvdRJ9OdAducGyzt7JFUwYPU4hcgkwPgQZBbGoEK2zCv5T1AFSJqAEL42XTXkasN20VGKbGf3yIAzI20rUBNAXdQ2_HRKPrLRt1R_IhU5BfVEOG1U58wJCfqe2o5TUkF7qtW8ESNOj6i9N9Vc1qOPShXBwpTuXn7k4FcmrToJrfriNZad4-qaC1lnfvJFYI0IAGqh1W02c95lJbyY0iZXfTgHbZ5Jihe_pZ1qgRUT8re7RUO9ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=mOdm4VXuzLcE1L9YKMbB9Gp8B7mJAiSXZjac6tlTs_qDMI0YFqWUsL-i42SrxdbwISspp-S0RK6MvgMqxM7Xs1ouLKSeukcQyJZS2UPJrinwincD5VscF9QJOiMxa2rxlWicHDnYmwxM-nz_qHkx7UVfPPEHHmQbECmjAZATAtZ1KDXUjJ4b_s-WBsG_M_fklGq5nUhkkhYeohzCEvlfBmAow6lxVpYvW2amjAK9QV6tqpHlLft15ZXqzKNcW9fXNc5h4eSijFFuNKkdUUBqyG9OJKDBBbcKFymTa39pAO0aof1tdspUZBOAOk2QSI5eyM_LYM27rxDMZVpfYvXpowD5ZuLLaxdR_c-1f3h_hqpgkLcvRC1uTa4EASx2Z_SFXdnHG4hOWG299L72xNYjVO5yLSutSNwhzgFdc0qrD7SGS8fQw9FXWwddRoJ7opl7_6yv0go-5ncxDv-xdJmYNruhhtqqIIPXd6iDaml3MrWV8eGVwNzfHrAg7IUBFu-GbxqGYyqB_PUfJCwlUM9ZGpJGRrc7zIoAd4cwlcHqbNYLJ2ingVlH_eE07FZYEItzV0lYkvwEJB3eqjumnUOWgJuePCHapIXfcPureJJAPvpo_5OnZosEnfRh107MTivPcavvUGkdfmjeLSNRW9Am1gSCy945XM52wobOXaZHh1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=mOdm4VXuzLcE1L9YKMbB9Gp8B7mJAiSXZjac6tlTs_qDMI0YFqWUsL-i42SrxdbwISspp-S0RK6MvgMqxM7Xs1ouLKSeukcQyJZS2UPJrinwincD5VscF9QJOiMxa2rxlWicHDnYmwxM-nz_qHkx7UVfPPEHHmQbECmjAZATAtZ1KDXUjJ4b_s-WBsG_M_fklGq5nUhkkhYeohzCEvlfBmAow6lxVpYvW2amjAK9QV6tqpHlLft15ZXqzKNcW9fXNc5h4eSijFFuNKkdUUBqyG9OJKDBBbcKFymTa39pAO0aof1tdspUZBOAOk2QSI5eyM_LYM27rxDMZVpfYvXpowD5ZuLLaxdR_c-1f3h_hqpgkLcvRC1uTa4EASx2Z_SFXdnHG4hOWG299L72xNYjVO5yLSutSNwhzgFdc0qrD7SGS8fQw9FXWwddRoJ7opl7_6yv0go-5ncxDv-xdJmYNruhhtqqIIPXd6iDaml3MrWV8eGVwNzfHrAg7IUBFu-GbxqGYyqB_PUfJCwlUM9ZGpJGRrc7zIoAd4cwlcHqbNYLJ2ingVlH_eE07FZYEItzV0lYkvwEJB3eqjumnUOWgJuePCHapIXfcPureJJAPvpo_5OnZosEnfRh107MTivPcavvUGkdfmjeLSNRW9Am1gSCy945XM52wobOXaZHh1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9gEVvQQzpUuNDdg--JHqxUCNFfkAB6Kjnq0EUZjwkN6RUgqPVAt4MqPTiOOf5ukn-fX269SfR6YvQkASSmQY-7ChrWiybUslKkUOv6f-KALoG75f3AvsyHxQQ9pEPcvDK0v1iREssCOqBpj8KAgCmassXDbNokHuEwYDKzX2BJYmwEaxk4cUvJnlDpt0_UQxAXfelrEbjCsMYI21YUYvSqeO6WurWH184JNR3yeWl0o7gU5MVv8xWkVHVPpJTA-E1H30Vlr-EtbQ79UG2_Uu6h4F1TwjqiDmyMQk88TRE1Aae5WoiiIpZT5nCBlDCG6Cx_9Bha8zE81ScQG2yXM5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyBTK1bntFSG2rwXK6cCdqFiy_f0T6ZMVeDKSgsri--TWtIToJ3CPnPZgAKMK_7qpINCV1V9M_4cLTjRU4Z_4K65Bj2nloxX0cjz8ZhF7Fd7uSebIH2iuXoYw4I_SZL7MAv-q7Eu-jwvxBqr2Eb9MOH0qZ7yp0xvLPCBUx1yhWeIEO9SFecGp0-iVAHXVOIgmLLUe4y6kF45AzPxNAzUDdSUhl9Lh3SB3QbIYKvwCBZ9p9yltp2EsBej4CIghM-AQjVl0ypzU-k0PYFDOS2Logji1wtG4ry5mRF5etcDCy7LoiqgoHdU640L55OSUpNpTZtmZBSYsGwlihaTpqrbXg.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
