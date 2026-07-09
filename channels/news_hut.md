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
<img src="https://cdn4.telesco.pe/file/hPcx50AwDt5oNyv-C_yvlUfVjEgdqDRbv_QrwAAkl-mneZLe9IP0LG2O38v7EDn1w7TLvERJcewgzIAztRBXGIUEw0SkNN_zKHE9T6nLSD4UYEXRNJvk22yBrEIqzTdxaYKVt8GVghqnph7Na9fAyZ40luWZdggqdHtNXblQExWQdEe7k8zQlJQ-JCHCtByiDxwxcqOe65wWCMzs2-7rM5ce9AEtrkadXi7On-XvPzanoaoWX3mAZWZTxvY_FnWbSTTFtgOcoyzhuJhQ9XGWdiryG4HGnGPYX7MEqE_tcz1bFGwlag5Le3L01kxZ5urtmEnRTfg7NmTSdvQiF_EV0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 190K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 18:03:59</div>
<hr>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=FSC-fCBzdF5xLPb86Ic2hLt-Sr8P9kbpLecXY0zhNFcWG1oxV_0QeaFL7xmCiod2sirQhDIFvGHd7EyR4XrJWMgtdyeNExnVbOPbUBRgZllEV3yXTFDeKsqPavM1q68wOfLM3BwKSuR69IX9WoMOD6BNyoS1Vkrk6MD7lepDkr-ODcG2Y8cnma47SAmuas_5ctQoez0frwfo-uNdV_7YEDSAXw6HXFMyWKSoc_8DldKZsiTUNZ7SHPmNRrHe6MHCk88Qj9M71V6uBvVs3ehO-8YzLHAQ1ANbmPKH7U-wmOCT1HRMOfRZyaA4n-rV6n4zw-XrEqU4r5rkKppVRoZRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=FSC-fCBzdF5xLPb86Ic2hLt-Sr8P9kbpLecXY0zhNFcWG1oxV_0QeaFL7xmCiod2sirQhDIFvGHd7EyR4XrJWMgtdyeNExnVbOPbUBRgZllEV3yXTFDeKsqPavM1q68wOfLM3BwKSuR69IX9WoMOD6BNyoS1Vkrk6MD7lepDkr-ODcG2Y8cnma47SAmuas_5ctQoez0frwfo-uNdV_7YEDSAXw6HXFMyWKSoc_8DldKZsiTUNZ7SHPmNRrHe6MHCk88Qj9M71V6uBvVs3ehO-8YzLHAQ1ANbmPKH7U-wmOCT1HRMOfRZyaA4n-rV6n4zw-XrEqU4r5rkKppVRoZRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=SEAsSICsKnB9YEoOL8vK4kjcYBfbt5dXnh59je0Sp8T9i_Lbq9vFqXgUqP2cwqgA47WAVSYxUdqAADVDrVoUG42E0LwU5gAUqb1eGzyjkEx3WVAewSh3oiKQVB1qLE-lKr3bSsWrcAXT4XifviFVbOwPZShMBiPd5inJZuDyvl7TQtM3IAFaAQMLf8og4OjEeXnU4N5h2egtZBillqY9y1PYnk7y-mGGfHUwtLz034RNqFO35R2_VXoP8YQMz1nTAcr3OzfLELGsmIFUXv95UHgGp3KbkKP33rir89dCRmFQ3ZGJbvQTwc5YHYnf3WVthefgzmcC3sJDigK02FsRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=SEAsSICsKnB9YEoOL8vK4kjcYBfbt5dXnh59je0Sp8T9i_Lbq9vFqXgUqP2cwqgA47WAVSYxUdqAADVDrVoUG42E0LwU5gAUqb1eGzyjkEx3WVAewSh3oiKQVB1qLE-lKr3bSsWrcAXT4XifviFVbOwPZShMBiPd5inJZuDyvl7TQtM3IAFaAQMLf8og4OjEeXnU4N5h2egtZBillqY9y1PYnk7y-mGGfHUwtLz034RNqFO35R2_VXoP8YQMz1nTAcr3OzfLELGsmIFUXv95UHgGp3KbkKP33rir89dCRmFQ3ZGJbvQTwc5YHYnf3WVthefgzmcC3sJDigK02FsRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=IavZ4JrrdRjZF0XIgwClSuopoCXKVxhkxTi-_rp873lKd-V3vSJ7ERln7jXeAfNNJOT_a94BV5ooENRvmWkqB1NOHk7SLAvu51gn15E7yjIauzkINLYqzCBIh5i9mAGB-4xS0a_6YGbRM70k7fZiKjpBcfzPA72j_g4xOrmguDurTRBbOLJoIKcLSO0NPGMJrJCepYJAp9e42S32h0Hr0NwmUg1OJ4cKaNRhfvCfVqTC5DX0TvE0LwlqcCN9JxEQz72EwB_R9mMpIbc6GKlBUosC3eY-d9Nn99aKGTObxOaF2D63ZwiFcm1tHgpsJUUIth1WKMsKJ0Q1slat3MfykQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=IavZ4JrrdRjZF0XIgwClSuopoCXKVxhkxTi-_rp873lKd-V3vSJ7ERln7jXeAfNNJOT_a94BV5ooENRvmWkqB1NOHk7SLAvu51gn15E7yjIauzkINLYqzCBIh5i9mAGB-4xS0a_6YGbRM70k7fZiKjpBcfzPA72j_g4xOrmguDurTRBbOLJoIKcLSO0NPGMJrJCepYJAp9e42S32h0Hr0NwmUg1OJ4cKaNRhfvCfVqTC5DX0TvE0LwlqcCN9JxEQz72EwB_R9mMpIbc6GKlBUosC3eY-d9Nn99aKGTObxOaF2D63ZwiFcm1tHgpsJUUIth1WKMsKJ0Q1slat3MfykQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RupB3tBmfu-IFHaNW_mstZDYGIaXuy3J2xrXe-K7-Vsxkcn6ZS7lVqSYNayDU6rcJodHiXcQs4hjyH9EmYjxCqEXvYROOjVJZ6r-RNO91IuRlQxC3mf4lYaM27ImztrqJFmsalk_4Ez4ZQJjY0w30UAcBC78phGCpq_niFDCR0vGDj5MLpf-r7aBIBZmFHgF32G6-iuZEwSHqpI4qLlcSYQLwlLivVU6-5AF0r7R2OoE0LFqqEk2Zqov6-gF4fePNzm2Fn0LLZYyFin_Tyb5AluhbOQAv1jM5kWyBZbLD-gW8WBz0iA9B_D-yiqdcqwR_sFNUlswem3EUI0pda_S-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=C-MdvsEP3R8NRDGHNlrFvWaK7-IqPqHjBmYfaielEGdhTZKyiAfnwN3tHxP_CJmEbMWBG-dFVqiDUpfGZwGQmqK0BMwrxQNyu6hx7JUU1Sbb88bglQMCU__jFScdOdWNe_diRRnjJ19oeWaTNdm0drrGeNEf_W6g1QlK2amglLai-APtHyNmzy1z_vVxZtjW_rCxWGrwXgLBMB6ceM215gGElNuG3jH8109OxXWemC-R3OqaY6KOb4HkvAt4QCC1FSikR_2wGNR-ZLNzd2sgRUhZzXUq8vLYoAMf8lxZpXy_em1TSjdt_D5jiUDXk8iBgarjAN0H5XhRZu14cQKogDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=C-MdvsEP3R8NRDGHNlrFvWaK7-IqPqHjBmYfaielEGdhTZKyiAfnwN3tHxP_CJmEbMWBG-dFVqiDUpfGZwGQmqK0BMwrxQNyu6hx7JUU1Sbb88bglQMCU__jFScdOdWNe_diRRnjJ19oeWaTNdm0drrGeNEf_W6g1QlK2amglLai-APtHyNmzy1z_vVxZtjW_rCxWGrwXgLBMB6ceM215gGElNuG3jH8109OxXWemC-R3OqaY6KOb4HkvAt4QCC1FSikR_2wGNR-ZLNzd2sgRUhZzXUq8vLYoAMf8lxZpXy_em1TSjdt_D5jiUDXk8iBgarjAN0H5XhRZu14cQKogDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRz7vVKslJVLSYB6OfYBY2N-jzP0BN2gYFQD7PR4tMg3n3SsF7oh0B6Qkw9HJakytuIReoxPPr4Wzy-paMAaW8M7yP7F-ISqgcYw7avYF0STCF1HpzcGbZMr3x0o5SPK7NyCd1R6eXrwRsek2IqHmfBD2OnqODHy4_27qXwff517b6TJy7bB3kmMTWMXa7p2UwVR6s2jMOsTFr7-6w0tjMU8Fg0rT4N3AjAe0MkWfEl1zbbshivCSvbCHch9lP4q_4nn8RdyjfZlGnZGAyH32_pEPTJpVu_0okcobYwCqezziDg413Ga-MV_Jw9l_ycWwm7p75KUfKEd2OkTQEi8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8w9KJjUe30YVEfPHLbRoPb_h9B5ee3LJcVvuv6-GZBgoLUTMtPVcXRONF3T5NoGSisMpI4pg0md7qyr7clYceJgUWjgB0R2nPTIvHiJcnnhl-vOLrIiXkLGvmkig19c0k44OsLoaNnmeDHJGQr-HLaT5tW5ZwFEum_ZoPM4-gIPtqxOK3nVxww-KlBy3RnDcszpSGmHktGkZwo5lMHDSZefLNETEbTikM1h_wAUOv4JSY_wloZNYOq39QA2gkIr-HIn7D4joywmbpbqEwqwz42wuuFi9MBRGYaey9yiBYtL2tdNe8SAlcMdGhUwsTwU8fzPG_aRvKdqTW0galspPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptqKEGFqrf1dbbCbAMtpm_b6PKulP-CqlmHChPbI5MtDeMCAiZeXLqe8Njo1q9a4HaAOqFImAqhHfb3sfmInrfxpeRnal0CmL-8voONI7Ct27IKEZtWY-bDclXndywfLEM966zN2LNSRJC-LjcFSMGYiYVGCods7f_18ub6Fesx_U1iptEEw5p3sS23rmtktFjvVZOVDMBTmf0f4_8o6etCZvS-0FXctQjp49OedCFDdlx7QlWjIcW5fTOyNzJTTQc9RHBkN6UNCGetTBKMf7DCaEC8tHN_euG9s9lF0Ca-D2MrdA2wi5BPkg5RoNUyQBUbfBl1QFZ9pBXMGcsPOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqIrv6xg11mmymbkGNYklRBLXp_lcK8p4RlfTPqEibIYVzm-zyylU-Ya_HydSkJ0tWLJ7Ju_jEXH8lZK_A5_iQBxMbIEITSu0KSg5ZRRorqJbppYDDDxXPEDUcRvyXcKjp3ccQKw8HqXOJMWuLdWk3xtMwNv0u6LaoRLIePetJZWcX2tXqK-zcSanbnv2H1Zw1gcTxQMuUDOnJy3x-ED9IarNNpitf-I5uI40ZAdJNNs8UQ7T14wWiiizqq7sUzQxm_BJeSSPmkmmTSvVJwFP0bKMPLqCFzaTIxkuMxg9Z3whl9e2WeZ2LTt5f9OgqWy0uNq6FyrltjATR2ymsoEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=Zv1Zjfts_yHmAGeJydjPRGpzbCp5MC4IiDnrAFZ0Dm_ekpeez8UfmHE0taNnF89UWx0IyVpyTUbgv2GnEqzCxmwiGSjgzuRfM2g6A4Uu99gj8aWaXQFwDHyL27hXi665qGgHYIFkapUBE2NKfWXo2XioaKb2DGbXmOgMgPGJnbzpyylTbxp9cFxe5vthKs7W5XCSiWPDBXfTVG7SvdZrHqkAY60HVWwSEr8dRS0BDf3s0RVIyLdPoc6ZxTDpIHGShfQ7u-zvqHhb3P5fUFY2pcHa_3_3-ZsaeAOVwfv2ymxcnFbsGZ-aW-VC4R1DVBfW-yckJiqPW3Zcq3cP-tG1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=Zv1Zjfts_yHmAGeJydjPRGpzbCp5MC4IiDnrAFZ0Dm_ekpeez8UfmHE0taNnF89UWx0IyVpyTUbgv2GnEqzCxmwiGSjgzuRfM2g6A4Uu99gj8aWaXQFwDHyL27hXi665qGgHYIFkapUBE2NKfWXo2XioaKb2DGbXmOgMgPGJnbzpyylTbxp9cFxe5vthKs7W5XCSiWPDBXfTVG7SvdZrHqkAY60HVWwSEr8dRS0BDf3s0RVIyLdPoc6ZxTDpIHGShfQ7u-zvqHhb3P5fUFY2pcHa_3_3-ZsaeAOVwfv2ymxcnFbsGZ-aW-VC4R1DVBfW-yckJiqPW3Zcq3cP-tG1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=gxCorWM3LrpgqzJIIBBr7NkqcOgqjit3hsRvGhS1g31ls3e8dlC93IUPc1f0SbMPlCmSnlvBNCVy4hp7fSL95yd1OJw5jU2aZlRlFlulGqAwGiKnpg4LWfVpKlbSbW11-Fd7KDPUbTXykcpcsYFlgJOphQOkxAd8VbnYJCoOODajL76IkjPItoqCpVCub_YY9Qd58DcuozhxbF8YfbaJsL2hRJtLOgljRklLc8jqW09BgblKg9Q8kP9O2KW2lUh2t_lwJcrm6taLb45okKjTXbIyiiu4zFrrxauUqjU-lMm32QVB6baejeh4DPF76oW1uJEyH5EH8v5wK6xClZTpMFVTiLLEkEP7L52AZrLKQ3fdkIkAlzGJk_ahyaOwel1a38ojgBtTEAjaMxi6GCr1z0waKbO3kX1gxa0wTQYm9pDlusAs7hGORTu8MhIwqCYt_9DLSSK12-L95H_CaEqluOe3e3kPVwKyudSUugJxpDGBxUfswMhcp9QocleprMJBJgGcHTfyMuw8iwuElRi_5SvAnjUnmgvfZ02MejNke7j3C4rE-h-B7JqAiW_OgzrDyemn--_fW5J55b-Sd_ovoQy4eM0EEUTpv46rbX2dIAqIuGj7yq0tfx4ym93c1PEKF2G1zr3SV3yAYH22IyA-1HIiyLecJ3274BbYemOE5l4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=gxCorWM3LrpgqzJIIBBr7NkqcOgqjit3hsRvGhS1g31ls3e8dlC93IUPc1f0SbMPlCmSnlvBNCVy4hp7fSL95yd1OJw5jU2aZlRlFlulGqAwGiKnpg4LWfVpKlbSbW11-Fd7KDPUbTXykcpcsYFlgJOphQOkxAd8VbnYJCoOODajL76IkjPItoqCpVCub_YY9Qd58DcuozhxbF8YfbaJsL2hRJtLOgljRklLc8jqW09BgblKg9Q8kP9O2KW2lUh2t_lwJcrm6taLb45okKjTXbIyiiu4zFrrxauUqjU-lMm32QVB6baejeh4DPF76oW1uJEyH5EH8v5wK6xClZTpMFVTiLLEkEP7L52AZrLKQ3fdkIkAlzGJk_ahyaOwel1a38ojgBtTEAjaMxi6GCr1z0waKbO3kX1gxa0wTQYm9pDlusAs7hGORTu8MhIwqCYt_9DLSSK12-L95H_CaEqluOe3e3kPVwKyudSUugJxpDGBxUfswMhcp9QocleprMJBJgGcHTfyMuw8iwuElRi_5SvAnjUnmgvfZ02MejNke7j3C4rE-h-B7JqAiW_OgzrDyemn--_fW5J55b-Sd_ovoQy4eM0EEUTpv46rbX2dIAqIuGj7yq0tfx4ym93c1PEKF2G1zr3SV3yAYH22IyA-1HIiyLecJ3274BbYemOE5l4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=by_qLuAoLy444ditUoIzDFVt1LNl8JJShN5x6nn-7RJlpn5lIyMpfBYOLSFW2ZTZBg4regShUAo-g60nJprqMLAtl1UoD0piwgMy0brK4jxwI2hO1eu9oiVw53tk3yarSSfQzy5_RNqZWAmifdRJAXAgImTv_ZvwsKvai2dqfEnlp-rWSt8pxJZVMcraZARU1tE70Nyl0N9i24bSCTcRsvCXtProFFwJOk9Lp9K2hGN0WU5H-fgU4xGR2ge5SNXPs9Z8KNnHJM9dwSchDdqgoNrsME1mUOECvqgbOnQH7B8sJx8pAiGYzS-WSwmDHw62aEtwKDHU2jiz-z-ZJctAyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=by_qLuAoLy444ditUoIzDFVt1LNl8JJShN5x6nn-7RJlpn5lIyMpfBYOLSFW2ZTZBg4regShUAo-g60nJprqMLAtl1UoD0piwgMy0brK4jxwI2hO1eu9oiVw53tk3yarSSfQzy5_RNqZWAmifdRJAXAgImTv_ZvwsKvai2dqfEnlp-rWSt8pxJZVMcraZARU1tE70Nyl0N9i24bSCTcRsvCXtProFFwJOk9Lp9K2hGN0WU5H-fgU4xGR2ge5SNXPs9Z8KNnHJM9dwSchDdqgoNrsME1mUOECvqgbOnQH7B8sJx8pAiGYzS-WSwmDHw62aEtwKDHU2jiz-z-ZJctAyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=n0PGKZsEOpQ5PFRgQtZFJmqtwj2zbik2tPI2hnD8-TYT1uNMeOO3EwG4Pm1fMs-D_upwAIG9DXUvAOAqbJDQWF2wCag5r31rxLbSWw4fTW7W6bXijbCrCUU5xTT8rcHaM-B3znC3VldDWo_WACKcrXmB7JMeRETTrszoMftifb2HX_SOuxslzbKct6keKJjawPN38AkXQ45x0aQEf8efE47rDTLcgmN3IRAQfkGt5HidKeGzoY1jjw_SqIun9QfjOyJeSDCoxypeAfhflO6HAf6gvamMJEVbljdImBXx8-8GdCly_nbgQF95_joThBS04ZY05hmZ5RcSfyiJr-39pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=n0PGKZsEOpQ5PFRgQtZFJmqtwj2zbik2tPI2hnD8-TYT1uNMeOO3EwG4Pm1fMs-D_upwAIG9DXUvAOAqbJDQWF2wCag5r31rxLbSWw4fTW7W6bXijbCrCUU5xTT8rcHaM-B3znC3VldDWo_WACKcrXmB7JMeRETTrszoMftifb2HX_SOuxslzbKct6keKJjawPN38AkXQ45x0aQEf8efE47rDTLcgmN3IRAQfkGt5HidKeGzoY1jjw_SqIun9QfjOyJeSDCoxypeAfhflO6HAf6gvamMJEVbljdImBXx8-8GdCly_nbgQF95_joThBS04ZY05hmZ5RcSfyiJr-39pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0Z4drlLg_tIqekvEUSvys_cZqRhm37k4P_GvLyc2Z93ukifiYbG5mZywiRt6DFoCmlC8DA1zc5i8vciRw6dRqRbYcioMAJslyW_IhGCdoEdby4kKOrhjtNm8r5CcAM5eczQzjFcQDhmE1UF7Aqqm519W7X-KcDgFEW9isNcPd65yV7O4m6XosuYf05kXJ5UD98xl7YsC-7ibu7uwtf74FMhpBIc1c7O_m40TVhfRuCLSTtoh-IieGTVvutTb7baocThDdGyegIlPerySmp39khyWBwCzhroEZCwmlwC6Vk1OGETAqrb-2OtEsdpyhVQwzmMyCdLg4k3GoJ-Sv22dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzntyK3wU0DVaJUEPrBVJw_1HGB0oZ7lyEWC5NYyGMumEoedLxeZWErlbkU2WRn0yHcsrt-cnPwdy14dif1_Kib-4NPbxC3l8hPM9VntnR_nNqosv0xZdKHXHT_I21HlVe-Tbjvv3TZ_4mMaZqARXzNeet6dQLbZUp4NeWO52m9JnSBhaaNxD-64pvpPNHy1QOvp4TIC5QqF52AVL0_-AjfSjPGrV4_R3X0cAKSIwvBEE3Vdzt3iXvOG5jKi8ijt47nvCIV2oTtaeG71SO38ogFoxX5e03wOWm-qP0KeEdzCoVHIF-pGr1Vmnj7afPPz6udY1AKDhgcTwkWBBhjKKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpFJeIATxCyvEvldAWWX4JOUiMoiaC7O_GQ_oE5tvgPCegXPrv6cCTduahYHmY0F0Dbk5GZ4kcK-QCcSdVdnz5HJV4RQJQkVD2-bxni88icvzZfpbzE__POnxjIqqTXI-IOwARfMBt7YTOE_MKVyb7X1rhBBFnJqsFq_3xTLawrsf0-vPJu3iPFMkhur2U9za8EGcjktqKFpEUZY84Z4xv_QhcbWmK1pnq9lMScLO1rwnEHuyjEomRq4cLR0-BzoOuWymhqiJP3kBXPTvt70OUdPPiFJhV3BB3mRlXUx7UY09YvtEd2orlKaVHsJ46jmtf9LcUzVJd3Hrrc3gFBvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKXEK-2L9aplnzWinOdG3r1BP1Fz2zi1iqueSnGv4FKbQ8dyT5Slr78Xw2vELc3OSxst5yL3fUE5WHaWHZ9pLXlb7kJ0Y65lC3diPQCsO7Fxyw7UqJ0QKXxziKUAZKlfM9zlElao08rXY464XchS78MEBCajY75Cp8Rjuzmhw8FpCMVIZGpYk6DK-8OHOD_sp2TJb6TMSsxn3Bd8phd-i9hMKBFzxedA6HjgU40VsRiAJZcagqpOY_57Et-COTcXuizICBKTxBgWIH2o6DzDojPiDNuVucQ0tP8hvnqtaXBjfPVqe4A6ubMkjC6BVm1j9agsW7PpXsCS9k1EJtqKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdPw50F13GaRTzfYNL4KIHEHmAXqndT3wV70aNEUkXOXV5p0gJHVMfVBmEZjhH6rRxPwzGf6yBT2R__Zz0dnKOBavUznoVNB_gx84x_mlcTsnScJ82IORMTeH8yyIXJqKMejZF_xzrRRDUKTwEN8E4C23ygR85PEFrTVv1QurMuKgxSynAYsNxSKNlk7Gmiurxn5I-9LjVejXikNAq_cLDmSZKOvZNLSaAnS3LVlLYVRPVmVpbF52JLBK8mnxFrmf4nighIrzdw9SbrNyYBSP1zGP7X1J4VmNQEXonEbsUDlRTp3f-rDuylow9QimG6-GGu46yYcf-_wEGSoMFS9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i65SXitqmPGUo6iUFGu0DCNNAszxU_YZrrqLvYdHzpggTgTrn78uhd39prjwcXpnFD-Ml6EhUJLFl5SFOwSwevw-SwCZ9gBer6NTydFpcQqNMjfSQ_eecIySwz0nvbiv4fbHa2N8_f5NcbUnB1kBmNZO7yNdwDNLNIFJi_hP_J6ZfWxsztM_gD9m0rEUDnbzXuW27J9uxHI4BVZPHTjSKjjiYQHKrnZNr0ZzuiCeb4jllGNAHM1biz13uWa2oGtq2xiMUyyAc_5EQZ6CwVrzfjxj6XE8XqNFMD0p2efIRd-MjoNKtLP1nIEc0UjVqrbTs95Oyzcj1gTUwgZ8bAv57g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEIzpfrbOHefyYfMjnEF47G0bV_UJgNlWBcZKhY5A__fVP91mfIR6KLuhPPKAffVAUDYgzh2QAsbSQNvXfL2ELwlrjXpeF__8T5XoOJ0fgHuxzwPowq2W8rhBPuqOjLfEz5TAkR_oy3MKhD6Nr7WLVUMGEiCW0QVRY2ePyQqjgoOj7UStieMo0gR8iFWInk-4ZExv49s5mX0eENIXwhIEgsDw2pHOZirpDs9rwouhf91gZuO1zhElU559KGoX-V02DSUWtBcLfrkzvJ2PF_HJdINQuPWBPxTLusq2j5daSgW_LtpiIkDcQGeUOO3hm7-d-LerAI57FCN7Cc5EhMrLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7AGy89lmKvtUxhCxFLg2qq25BZosRfqCbATCxv39gT-72sjLYg9E_tuH8DOgr3Lc7CacWCOcGK62lXt7dG3uLEVaD-coQ3EnexHIp3ZlXYmUMlWk5HxpSOvzqysQzm0UMNFMNcpx1u2cYMNPoZT8B6uUGVwyy4n_QO9n0QnFLmS6QNCtoNDq4qYNWMungJY2mLp8NPnRXBqca-kKPynjosJh32cWRozaV_Os9d_S7Tl7dV_2Grs1lVZ4IhxoHSiACf6ArGEp6n8_eacSGzwuS45a3b5NUhoo4KARv9UC6TvqePb8XMbFopamIiEWRbYjOAR51xrPEs9fCo5hMkTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=jyGteO5QAsbRKbl8NiAIvvG3MB30ZbrsDpqXyiD9Uo8z94JF5fLPY9cpx0E4HiJsQt3hYAV9W-sYkKE6dSdXEo4noZzFDn4TtONIjBhmCjaCmQ3ZYnzTmat4ZQcVDZDJ0sHu7tEEHY3ujuQ0LaXLw94XlBXgzxDUihuskS4-Dpcib9UGbTmyHk23zboLvTI2CfbuwWu_A9hj5HvSiE1b8M4a0CBHPCkDZppiZ_BTaL2ErAJe-BYleOPZ4yHD93uTbMBW90-Of67PurwQkc7Fm6Ujg26nPgq-5ISPuq0S_MRJJujQHowc1Xt7MYvjuwoNisp2TVSwvVYDlwuwaPyTvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=jyGteO5QAsbRKbl8NiAIvvG3MB30ZbrsDpqXyiD9Uo8z94JF5fLPY9cpx0E4HiJsQt3hYAV9W-sYkKE6dSdXEo4noZzFDn4TtONIjBhmCjaCmQ3ZYnzTmat4ZQcVDZDJ0sHu7tEEHY3ujuQ0LaXLw94XlBXgzxDUihuskS4-Dpcib9UGbTmyHk23zboLvTI2CfbuwWu_A9hj5HvSiE1b8M4a0CBHPCkDZppiZ_BTaL2ErAJe-BYleOPZ4yHD93uTbMBW90-Of67PurwQkc7Fm6Ujg26nPgq-5ISPuq0S_MRJJujQHowc1Xt7MYvjuwoNisp2TVSwvVYDlwuwaPyTvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=gmH9NdUoLEYQTqEnjFuLVjw7LvLosG0HJh_zw2O7RU2fCZMbRTPHyfLQVqM0eLVUhYoDzXjSpSQVb4rxWGMlHxIr0roj0wK6WCDZ3UblDYrLu8Ssz027tjcqUDhBzPqEQCU7Qy7fLWORPhmt0jKMHrgz2SUoXD74_bK4C_ye069UDm8lUYdWvXqxLxPCF0qbSrMkIXuJqPhcIZr2_iRrCGl9NnNA1XcJvNohdOIDu_or_iX4BRLFo41LXcXn9SHMbEAdTWvt2ZytnohHmQqq-xl-fUSOcOz9labxEkFqx1xn1wMdhDu_ghIuUr33vSP_pXtif4esAXpZlHeIPMWl3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=gmH9NdUoLEYQTqEnjFuLVjw7LvLosG0HJh_zw2O7RU2fCZMbRTPHyfLQVqM0eLVUhYoDzXjSpSQVb4rxWGMlHxIr0roj0wK6WCDZ3UblDYrLu8Ssz027tjcqUDhBzPqEQCU7Qy7fLWORPhmt0jKMHrgz2SUoXD74_bK4C_ye069UDm8lUYdWvXqxLxPCF0qbSrMkIXuJqPhcIZr2_iRrCGl9NnNA1XcJvNohdOIDu_or_iX4BRLFo41LXcXn9SHMbEAdTWvt2ZytnohHmQqq-xl-fUSOcOz9labxEkFqx1xn1wMdhDu_ghIuUr33vSP_pXtif4esAXpZlHeIPMWl3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4T4cvUx2wAj44U5QjBTZnmEEYit1209fAECxEb0nPn00gKi4Sov_GQnGs3rMnPmewhsZ_Wwt-BuKqQ38vg76LTlsjPGW2r15wPVJjsq9Bn5h75b0lYFiEBVX0CtUYUabF4iuwLnNwqbESxZm7LDaeDS9hl9W-VEokHf4JyCzHyH1cJFlL1vjeNu8y7qL3DEXQYNKu6eSiqjGrimeVenaoGDbzLvAEAn4RSwiKOhNhKs2lfrOa6UT_ocpYjJpo2kZSRvASol_TNPnVDF7T0p-4rwtlMs9SwA5ZVJD0Qt_cZwen082aX4SmL99Ie4dmhcjcK4IGLPtuq0E2nTYIVYxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=Uj7Fz4Yj2lgZQjjlhidPQS0ocCTzsTf36OnLXSyc1OVyIFzETFD1JduCt3WnQzzcC2O6DLovCY-L96iIvH7kbkPBQ-GO-TuM6I8srWa3W8M123OeIlGT7pRtw4fr_mxd_mRud0ZxjTDYPOBHc2x66tK8IDb_vUKNqtB550bDWP-S4Lcw4eJwRO1zSabftAWBY7xbFAYvVKcJwkBE7__dK94IeNtK8Tcm5g-Yhefip7D9BHk4mNc_1nN6emU72pwJU3Qzv36EfAwe6x2RJNiMc3kDoIaXVcCBVRL4J-0ARlNR7ZzEylTHus9Z0kv5abODUnlIDvYMjLTzugpveMxdnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=Uj7Fz4Yj2lgZQjjlhidPQS0ocCTzsTf36OnLXSyc1OVyIFzETFD1JduCt3WnQzzcC2O6DLovCY-L96iIvH7kbkPBQ-GO-TuM6I8srWa3W8M123OeIlGT7pRtw4fr_mxd_mRud0ZxjTDYPOBHc2x66tK8IDb_vUKNqtB550bDWP-S4Lcw4eJwRO1zSabftAWBY7xbFAYvVKcJwkBE7__dK94IeNtK8Tcm5g-Yhefip7D9BHk4mNc_1nN6emU72pwJU3Qzv36EfAwe6x2RJNiMc3kDoIaXVcCBVRL4J-0ARlNR7ZzEylTHus9Z0kv5abODUnlIDvYMjLTzugpveMxdnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67636">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=LxTvvLTqwE-s8HqFf0OwkMRJ7XNXiqgfTIYR5DgpI1ijD8_by56iMeRuBMsDvj4qFbOr6GuKPWnJHym7L-vvarCFm0qb0dJTxheAoktbtmOOBCmTaiqgfSu1vXbjufVVTwciuo4yXmOFGmBwsKpqzQsXuB5yRXPZ6f9IElHLUvazz4RixcH_RZx6dPmvymQZdMo0quQZ3h4KOAEDpewjjtsW39sAqmpORI3Ac7GHueDudzFXObf7pFov7WdY4sQDRzbRDlYEQZt7A28k4FBo3p2h-Dbga7tiu-PFVy1o6aKg7e0P7WJyjPYV770xrKWoC1cRTvM8Lz9wp2fWMxQS2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=LxTvvLTqwE-s8HqFf0OwkMRJ7XNXiqgfTIYR5DgpI1ijD8_by56iMeRuBMsDvj4qFbOr6GuKPWnJHym7L-vvarCFm0qb0dJTxheAoktbtmOOBCmTaiqgfSu1vXbjufVVTwciuo4yXmOFGmBwsKpqzQsXuB5yRXPZ6f9IElHLUvazz4RixcH_RZx6dPmvymQZdMo0quQZ3h4KOAEDpewjjtsW39sAqmpORI3Ac7GHueDudzFXObf7pFov7WdY4sQDRzbRDlYEQZt7A28k4FBo3p2h-Dbga7tiu-PFVy1o6aKg7e0P7WJyjPYV770xrKWoC1cRTvM8Lz9wp2fWMxQS2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
🔴
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور دیگری از حملات را علیه ایران به انجام رساندند تا توانایی این کشور برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
🔴
نیروهای آمریکایی حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، انبارهای موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
🔴
این حملات جدید در پی اجرای موفقیت‌آمیز حملات تهاجمی در شب پیش از آن صورت گرفت.
🔴
نیروهای سنتکام در تاریخ ۷ ژوئیه حدود ۸۰ هدف نظامی ایران — از جمله بیش از ۶۰ فروند قایق تندرو متعلق به سپاه پاسداران انقلاب اسلامی — را هدف قرار دادند تا در واکنش به نقض آتش‌بس توسط ایران (از طریق حمله به سه کشتی تجاری در حال عبور از تنگه هرمز)، هزینه‌های سنگینی را بر این کشور تحمیل کنند.
🔴
نیروهای ایالات متحده همچنان هوشیار و آماده عملیات بوده و برای اجرای دستورات فرمانده کل قوا آمادگی کامل دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67636" target="_blank">📅 09:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67635">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cwXkVCTdU8uQJMmqmH_BCjU9x5iyzvfQhGqmZK7XRsHMpbnZspZH_nu0OD0Kz1GSYFS2AQ7b-eMnZ3f_JUWvg_HOOOWd3J8OHbUJYzQPjsOfM8M8kOefcCMKBy8GJzMFuLZJwvpppBj5wNIZF6cSLm4caeSShYXZ-eLZHEnaX0yY_PHo8blW6kjLNfzVbX3foKHQkyHNxBS7jPxv89XLAmH0BtOhSFRx6w5bEzxyWceBoWW-NF7eOYK4QpznG5RGjPtPmI7s7sItChJJ64teo-wFG3TYIvAjxxyEizbJomNHlz52n7LygLjXHqAIPdZVzBcAlKZrFQghVAvrWqmq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت برج ترافیک بندر چابهار پس از حمله ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67635" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67629">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hiMTyo0JLkH_OtsbrmsTn3-2EnfptY_3rzglUOjlUo2RjgV5DAU88iJ_WCjVV9P05wgUPbZ__Hjo4zbP91pXS8UhsweCoT32US6ab9tEpcWUkA-AYa1oEGwHC0Tws9-t6rY2isWG5k9DVvF9jx4m2ZDSM8s1Ussj__tRPNclUm99lf09SqJedKg44STTnmatc3g4JHPjUTPIGDdC-60VzMRZwX33iDMp87hwtglWOAIq9dVgXnsYe9hE7J1sBehZB2b4-p8hoi4L7HYm54TRyurXlSIAkePArIHIPW5-C_1N4nsFS1W-kj6TxADGxxVwp_jDsFp6Qt_RjV3bCLu8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6dRadEgRbdNq_cDOaX0EHRiEcDP3iwxUNpqpKJVnPtZtiW5AqlpreeSNG7T-hVsq4o1HiQ2D9WyQEuVGKIn096E9UFpDtpyvymFUmKAEslPoh-LTaG1kPqwtbO-aDz7dTlvHmZx7lVFUEV2DZqcSXStzohT9mxZr4wtxBpQZEo1M_87cpBS2dz0X1sI9W3yrItg12zqv3JqLKjbmyOzljTqPeXbIfLXyQDnrXsVGdVuR2HS7aEGmRMs0yIVIC21eoh0XoQ8HsOdreM-UgjwfJeAq9Z3r3ugIie9FngrupDBk9LdyZWMRgW1hrXKD829P9xFGT4tn8i1de1njeJgmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=Hda2q_i2EdlL04Z3kl_J7cd-KJNlHmmJYkozlQQQlGk2vkxZv-k75l7BpxwpvtE_2t01uePtmMbO8nJouD5LW1HgSo7CAFSs7yx3j1OrVXz_73vDQnToDFBplJVEF2rxhGPAd-GfHb-K74TMKHb8lpRpLbiAWDot0oQE-asZE_IRTpn_WVGSkMTOrsQiWMt7RVb8HyFI5uGEbj4lVuwU6hpLvFRlvN0gPrmBueV3bHXzJpKRWAorMKxm8RHm9NZY8TN1KkCrznDn_qiUdDhIasuoj-ovpctT6S3Uvt8r97jrvjUiPfD3mmFxjc6lLB-PPurTR7OXDPJk-O9b8dqHUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=Hda2q_i2EdlL04Z3kl_J7cd-KJNlHmmJYkozlQQQlGk2vkxZv-k75l7BpxwpvtE_2t01uePtmMbO8nJouD5LW1HgSo7CAFSs7yx3j1OrVXz_73vDQnToDFBplJVEF2rxhGPAd-GfHb-K74TMKHb8lpRpLbiAWDot0oQE-asZE_IRTpn_WVGSkMTOrsQiWMt7RVb8HyFI5uGEbj4lVuwU6hpLvFRlvN0gPrmBueV3bHXzJpKRWAorMKxm8RHm9NZY8TN1KkCrznDn_qiUdDhIasuoj-ovpctT6S3Uvt8r97jrvjUiPfD3mmFxjc6lLB-PPurTR7OXDPJk-O9b8dqHUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر مرتبط با لحظه حمله و پس از حمله به خط راه‌آهن گرگان در نزدیک روستای آق‌قلا، پل دگونچی
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67629" target="_blank">📅 09:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67628">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67628" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67627">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RdTvWLfrr-cYpD_XrThhT4-muQAmN5ZTl0-UUgRLj8T8awiIRVrmpjjmQvDwq_z-7BKBglrwwRGYaUXsGdQN3MNmBCfx8Lj5B4QPU5XTONSnVyZBGdNf4yejLqUlvWfWrA92OhFZd5XmBvvk9yYNqF-YgdC86Uc4qRsUdAq-ieiNpOebTPbISGGySNmU1tnk7UyJk3MeKBfsiKDz3atsBkKZHgirIG-QwkIJ2zUt1T2sZSRHyKZWd-e5CADauzMCTnoNIfrEEl8265_sZVs5a9WVQJVy-7OnMYFY_cmIOTNGaOFRcsSgu2nU5eMwRJ0K0enCDHctK-yhVqQmA6T2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67627" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVOYQLeu8MRy_olNPbXwr0PEgjBESnpRfZFgqVP9mz70TvVkhz7ZjjVWAqWkDQif6B_35keJwZ32xCZwpVYyZBU01enGmFWZ28nayzvbwQqMAt_aovQ5gZkOzGZtEVbLzzbDOeuFAN7hrLzrOeDZPsNuaJC0jpV3uoitJqNFKyrAZENWE-_FoNS3AU4YOMAOGGxyTBh1di6GpeGwH7v3BloL627NsnA0jnQ1XO96MBC2VEkBsdizv-d5jJAv6wMtvxgu_oxk3Gfo0AzMX5xo41s94PsgZtITGoWRrB_r5ZeYcyrjxv8vcY74hgwWTSbd5xwJztHRMOYdxe7IPvMLyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uq1KYyY5Enf41lAxXRCi2P6yCwpPGp_Cqk0y376gSreltXQsjFPNlQnigSA08t06IT7EuGTrA2fy9EMY2qHyhGt9sLNl7fjuaQMMP13VMtj4Vhxj0qEw4AVIjOgZd0dMi9CsYh7cKxOKiOuXATOGMQdzkxOxBvIX2bluoAr8ak-9S73T534juEnGsNH2q_KwK03BFVhS3ga5TTZ3cmqhtOaDV7icdGiRS4OlCvUnrXb-3dlHi2NFRM1QW74YHytgmmMmW1tDAExuPcjqy0a3vAUXEvIwpn_CRexxs7iXEXxHSfHFRkViC_RiJ_8v8X94fL8yjUbnTA6L83wOMcJ7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEbVw9makQMG8XU2GV4ex0C4shtvl8ffd_KSPtCSdDh7i3E_Tz8QHebNYwaD-MGCj52Jfmds0mOda8doujRGZISI0uEGTIDyxXNSqNTDSvllccZ-6jo5BYekHQS0zszuQBkrnVZCEnqypNYXsm0cXQBCJ9ibjilu7qr9KCT2OLCnrmFgbZSpj4PfgTwWjmorPfz0jh03hpJ0xVhVek3GrqzRTm55iAQFTEPkh3hgD6QFDVOCyZbEHgvsMCbDMEIxoiCzYYehaUdyzYzmi7wh1FUkRsnPceNS_erJmO0JALrLG8ixw6bRz_SWp41_uN54phRHtayOKLD_r3QLsAygsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
راه آهن نزدیک آق‌قلا در گلستان هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67623">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=H14-XX_pbsiclObweHMKU3wG_a3PcK4TfLjUtlV4Jjpx81_ArpKeP1egGN49cxivewaVSVkB0PrxddgmFX6n7dDC3LFpQ98Ebr8wS7KZHEREFuxoZNv6anHvom-b0zHjMWmjD50ttTWdtNyw07DOfTyECiInGzz4OINaHssrVPyUOjNhNgozMONz9u62geAMnLWY_gLeDaZHBg1iNgMI6AcCYm4OuYt79W92121_rn4IlXYJCOsIq_iwJ_YmRapAurP00YplUvnvywngADyBm0Vm1PGUlkyUXKuX-t7EOr0iHd4nYfUZaWWobrqosRbyPi6GkoLyE7sjHAW9JsSepg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=H14-XX_pbsiclObweHMKU3wG_a3PcK4TfLjUtlV4Jjpx81_ArpKeP1egGN49cxivewaVSVkB0PrxddgmFX6n7dDC3LFpQ98Ebr8wS7KZHEREFuxoZNv6anHvom-b0zHjMWmjD50ttTWdtNyw07DOfTyECiInGzz4OINaHssrVPyUOjNhNgozMONz9u62geAMnLWY_gLeDaZHBg1iNgMI6AcCYm4OuYt79W92121_rn4IlXYJCOsIq_iwJ_YmRapAurP00YplUvnvywngADyBm0Vm1PGUlkyUXKuX-t7EOr0iHd4nYfUZaWWobrqosRbyPi6GkoLyE7sjHAW9JsSepg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
ترامپ: چون... راستش را بخواهید، این موضوع کمی عجیب است. کمی عجیب است. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان یک توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67622">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=O5ayhDcOfukpCbSRj-q77HgchdzYONddES8_dmPE7GUuYOU9ILQnW_vKTJWvcoKSERDMp5GgZA2uu3D1blKyPdRpLbveEHzVD0Ki5XhEs4lob9dvJuhcJEiC1oo-tHYA6Smmv5tyNU4BoKJUE7sd7y0S6_LRymBA5nR6qq72Vw-20qjnRwSd_iLTcLNHaCFi_3rdOMu1ujNU1ebtY15r4TeIDLauy3Ity7MPiFFfDH7fz5qidedF3SG-knPhUGl9735wDCWcnCoHpGGqWv6QYO8MhEFDy1oGjduGhz0SJ-1bodnqMBou1837yizBA8GgXZYs-HeQtArR_jPJDGIXcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=O5ayhDcOfukpCbSRj-q77HgchdzYONddES8_dmPE7GUuYOU9ILQnW_vKTJWvcoKSERDMp5GgZA2uu3D1blKyPdRpLbveEHzVD0Ki5XhEs4lob9dvJuhcJEiC1oo-tHYA6Smmv5tyNU4BoKJUE7sd7y0S6_LRymBA5nR6qq72Vw-20qjnRwSd_iLTcLNHaCFi_3rdOMu1ujNU1ebtY15r4TeIDLauy3Ity7MPiFFfDH7fz5qidedF3SG-knPhUGl9735wDCWcnCoHpGGqWv6QYO8MhEFDy1oGjduGhz0SJ-1bodnqMBou1837yizBA8GgXZYs-HeQtArR_jPJDGIXcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما از نظر نظامی، پیروز شده‌ایم.
آنها مدتی پیش با من تماس گرفتند. آن‌ها واقعاً می‌خواهند یک توافق انجام دهند. اما من نمی‌دانم که آیا آن‌ها شایسته این توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67622" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67621">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=QINXKmvfJyPLsSntRy4MjGWPEgAwst3X2TCcxyEihY6qUDQK5DRSWiSqFhssyfncVl9j8Hn-qEuRNmI5cHX0krxyV_Zb2YoASfNRryEKH6MHwd3MufcZKi4jgA8DUOVNqlo9YpjYRqw6lu3v_H_Y1tfQG7Px8Ou5BkDQpyZyXShhfZsPM7CqQJQ-FoLbGacYajyyBBMLzfs8IRyOQB7fwPMfOfrv_NuQ1TBplyq5VZEeS3X3e6O6HVBFH7MyjYPwIgy_oqCKpgqvjevtc2OdbG8BIFRZCH6_TLKvoGKsWh6_0L2avm6e_BSZtmt6kE7DqcVMdvet4r-LmaJx9Xf5ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=QINXKmvfJyPLsSntRy4MjGWPEgAwst3X2TCcxyEihY6qUDQK5DRSWiSqFhssyfncVl9j8Hn-qEuRNmI5cHX0krxyV_Zb2YoASfNRryEKH6MHwd3MufcZKi4jgA8DUOVNqlo9YpjYRqw6lu3v_H_Y1tfQG7Px8Ou5BkDQpyZyXShhfZsPM7CqQJQ-FoLbGacYajyyBBMLzfs8IRyOQB7fwPMfOfrv_NuQ1TBplyq5VZEeS3X3e6O6HVBFH7MyjYPwIgy_oqCKpgqvjevtc2OdbG8BIFRZCH6_TLKvoGKsWh6_0L2avm6e_BSZtmt6kE7DqcVMdvet4r-LmaJx9Xf5ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما به آنها ضربه بسیار سنگینی وارد کردیم، و من می‌گویم که ما به آنها 20 برابر ضربه وارد کردیم.
هر بار که آنها به ما ضربه می‌زنند، ما 20 برابر به آنها پاسخ خواهیم داد.
وقتی آنها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67621" target="_blank">📅 02:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67620">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d252421.mp4?token=GWTTPSkG3f5Q7HJaQUUvZIXqKA5JIAti6tz2hf05YKxNU4oX8WFXLum_9F5wflsUYk9iMMlm-3Z6Ye4lwqikF6XGQ2Fs8YNr0e5FAdyt9KxJTVmcGbEQCkhnXbrNLrmrT2nxewoPupj_BXLevKrpQof9FBuPQXCv12ulEKd6I0kTwfw8Y1IuBIhpMBL7AKazBY9Zw9AsSt4k3sXpz9x5wJpgjH-5LRzeFsRoTR35CqM33L3vBpdhSbsiEB-jZ0-tuuZg2u--gBMgU1jWEfIklhd6OIr9hmTsaygi1gC8u4Jnq9UsurVKxtLrm-ZfJ0YfddFqelmQBSzjSaEc3Vae4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d252421.mp4?token=GWTTPSkG3f5Q7HJaQUUvZIXqKA5JIAti6tz2hf05YKxNU4oX8WFXLum_9F5wflsUYk9iMMlm-3Z6Ye4lwqikF6XGQ2Fs8YNr0e5FAdyt9KxJTVmcGbEQCkhnXbrNLrmrT2nxewoPupj_BXLevKrpQof9FBuPQXCv12ulEKd6I0kTwfw8Y1IuBIhpMBL7AKazBY9Zw9AsSt4k3sXpz9x5wJpgjH-5LRzeFsRoTR35CqM33L3vBpdhSbsiEB-jZ0-tuuZg2u--gBMgU1jWEfIklhd6OIr9hmTsaygi1gC8u4Jnq9UsurVKxtLrm-ZfJ0YfddFqelmQBSzjSaEc3Vae4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
من در صدر فهرست(ترور) اولویت‌های آن‌ها قرار دارم، قبل از شما.
اما اگر من [مشکلی] پیدا کنم، شما هم [مشکلی] پیدا خواهید کرد. بنابراین، شاید روزی بخواهید شغل خود را تغییر دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67620" target="_blank">📅 02:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67619">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
انفجار سمت آق قلا گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67619" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67618">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در گرگان
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67616">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=dcy0rTkDa1XjjNRV89KyLTwhBJn8JsZxIX2-UuySw_SdwNRFqZXrr1gyK3XJWb87Fbcn_kuOwv32TaDZTWvexTfH46kDUpUK36cIRUz66x1W7CFHrVa7Awrw-krv2pAAFIeKzD8bkn8J_bOdMrFyxX8bnTeSV22bttun5wPid60-jEyMw3_xosZaDS5AuTP-28qMV-IzK85BCvKtbVxV6ZXRoPGPb9nw1VNJ5UWVcy_Nr_ZQ7iTiUQWrz_RccBnAPlWPqRpQoz0sgTKOH-ODHam3owQTBl5XTzsBmCgCMARdUcpQUYmbZD7Iner3H0kl3jSc8-d3CVZwcKmvNuJwhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=dcy0rTkDa1XjjNRV89KyLTwhBJn8JsZxIX2-UuySw_SdwNRFqZXrr1gyK3XJWb87Fbcn_kuOwv32TaDZTWvexTfH46kDUpUK36cIRUz66x1W7CFHrVa7Awrw-krv2pAAFIeKzD8bkn8J_bOdMrFyxX8bnTeSV22bttun5wPid60-jEyMw3_xosZaDS5AuTP-28qMV-IzK85BCvKtbVxV6ZXRoPGPb9nw1VNJ5UWVcy_Nr_ZQ7iTiUQWrz_RccBnAPlWPqRpQoz0sgTKOH-ODHam3owQTBl5XTzsBmCgCMARdUcpQUYmbZD7Iner3H0kl3jSc8-d3CVZwcKmvNuJwhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت نوه خامنه‌ای رو با سرعت دارن کجا میبرن؟!
🧐
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZSbpXLbS8SJrK-Ma0QsnlUBkOKQ9qhgkHHBguWKcQwzSdc3vhzmkLPvi-5l48j47Z3qu3N-wKXSBEOO9Zv-MFYBxSNyJHqG4ZtfNYXD6sigm0wWIpbDuOaCdwJlBsrFBQjGQggxu3odSbWY_inSBE-2EpJM6s4GJPh0y9fVnQCEoXEDsdzzQg8W082CCiHUz3zkBY4R24m-91BaBrJbIK6ga1zudeEpRXYcOOtqvwnz6-EDGvIbjvM196Zrsk9q3V1w6UMNadKcs5dlDK-Gx6nNzFyucwjN2u5dR5UIkDRQXlFOPrris3K2SwfMvytPwkr-koHAOXCLpu4JskdFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقاطی که امشب توسط آمریکایی ها هدف گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67615" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67614">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر بسیار بالااست.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67614" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67612">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kL2Lu9-3BGpGhRT0yQJvE3RtTryxoDHFoHCfjWLe9n7p7fFuolcKtF7sWRWIcim_UhImeNLvJp_SoexQ6Knb4itni13hU6g2ab7pgqE8pxxmAIoLYkV3l5iyfJJ6bVj6s0N_YcCh8VggZySDFRESa5VVWk1XuWCSBn0ivGJCSWUHRtWj4b8gRbc-x-IIebGsXQ55UXvPMBUo3wBofZcKjAl54PaJw_EH2SKSRNsfdFYxRifPQ-YMwybHfZz-KjDzXlNwKMz6okOfS1ao1lkgSpCp-T5nUPD3p8UgS6_Z1NRoR0HLM0LTYdJPhnEuLmekE-j75xO7uikIpnS1nGipNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=MRCx44hkHKaPzINsJ-OMMMDanMX2n8FdPPdyyW8BlFpy_k5IAOYnWsyZuYdjG2SrDQfad9_gC94OPEd3M-eh6hOZsOHGdwDGWdFzwcQO9_YUDHOglpuw7YWk_JaNKJgX8PVXv-_ZdJHZ6NS6bfntsbMqtl4QbvH8VxvlDUvBO5UsBiKOfWnK1UTR7xFJOyWa6NEyzuEOtW9h0iO4iP5o6CdHAYsxmBdD52H7CJXL2QHLXmK_g3XFop1-lpRNKNUjfCiaAmvz1afM46kODGieybWr0sNyHu5t7UW6FzfKZI5DPbvKqkCPKmnWLDO2is4U4pNblcericSSHSetFsnX-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=MRCx44hkHKaPzINsJ-OMMMDanMX2n8FdPPdyyW8BlFpy_k5IAOYnWsyZuYdjG2SrDQfad9_gC94OPEd3M-eh6hOZsOHGdwDGWdFzwcQO9_YUDHOglpuw7YWk_JaNKJgX8PVXv-_ZdJHZ6NS6bfntsbMqtl4QbvH8VxvlDUvBO5UsBiKOfWnK1UTR7xFJOyWa6NEyzuEOtW9h0iO4iP5o6CdHAYsxmBdD52H7CJXL2QHLXmK_g3XFop1-lpRNKNUjfCiaAmvz1afM46kODGieybWr0sNyHu5t7UW6FzfKZI5DPbvKqkCPKmnWLDO2is4U4pNblcericSSHSetFsnX-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای منتسب
به
حملات آمریکا به ایرانشهر( سیستان بلوچستان)
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67612" target="_blank">📅 01:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67611">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3zgmJz_lIrysFuRqAq6dAcKYWneEWoq4xvQDjlE6DGr1xCg-Rf7kBwQIEGF_D-WjPyf9pOIq0M3c8o2i7k1YUugRHfiSlAxuM8w_Cqmg1rJJpel-XQGU2ubpUex2kKH1C4tvW4qrNoEgUWxkCHZKEpMbujsy3ZVjTQoVNDi4ZurzNWREf_mcITQMBoxClbnKqGmAhWIerTSOyA6ERcxjDUt_qIKHqiflLw1Ns64O1AkJ6h7_BAnvWqMBByk4tGBJdz9QfMN1bJNBUuey9lj38v9XCB9UYwT0hLueyV9lh18-KX1N2QEQBwYgyaVIIdEaPaon4qVLrm6sZnsEed2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67608">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjSvJ1GKaMIBYGmG_3D8wglEh8kyKG34cmnhJkEjI6EUJLFDFTj1UV1r9FCvJmMNIIcNjQtYOQKrUjNwsYRdKbUvP3-Few-8eiVlIahNGymPz_2NyMRORv-eXRp0hjWzm2KOUqdv8n5jhzY6zp-x4WRt0o8vxrCbftN9mM739DVXqdaBkrndO2Sr7Up-OhMqdGphcSjAYdiaG8nThRWBGEjscDItiA5Myj8oABHwuET_diUfyNY-uU93DF1LnsYX0zxs7x3bJEQlH_d03NcPavVToaCCES_fYPjNcI5vTrwY7nGv-DfjuIZ2SA-oZHR7TOC6Gr5om7bXlEujRJ_RPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgy7828fXhVPFRvJjXcpp9BeG-i5VPqYWk52s7IT8ezoPdGvFJw8BHg9lednj_TRaYv0dd3kvUnJiOA9I0g9_kv2OUvjS9n1jV2Lx-YzJwneARzPoq2V9TnL1vXMWailUTPp5Q_Hu4Wqaxid5ALdFtUfNWuSPFbxBeF0uAhddYuN_aQNWg-xlnRwSBbkYRn3JgGYzyKIss0MZCFf52qzW4t8J8KvR92gAWA4q4JhmKCgHJeVvJfDQNykavHxViZvIDiSC9xx865wJmCAkQoY2tXrzfB1TC5h9y2Xrd4fbBnsvctRvgzRRXaxAOC_grP1HzOG_t7IQvKs8BC93nxXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ah6MPQsTi_lVi40909OsF6Ww0eN0V5tXQNwpO-QkQ2lAyjIfX67y-_Dc9Hl1he4kK3X725n0EVESAi3MjGqRRThbQpmfc2vQv8ft9Ge2Lz3Pv44Yqjrlsrea_UF_tHHVFPPx4Q0BmfwdLGGo7OUhcSj5Lx1LDtCypdc1x9Hi8ZXYiznBwJb3ZLSdAsBV9g2_eJGGU_BZpBT1OpQSlSlNBHbeVgjmE46Y_D5dg7oFB4hDxLsZ4utuXezB2WYMA3xf5D_Au73q0pFWPRaeYF-TDcutJIyy4LWXw8bm_U4PIehYG_bCC8Smg4LIxbDmfolLEtpni1ZHFac02c5Pe2KbFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ تصاویر حمله به جنوب ایران رو در تروث سوشال منتشر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67608" target="_blank">📅 01:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67607">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دلیلِ این چص‌حمله هارو متوجه نمی‌شم واقعا، آخه کسی که زدین رهبرشونو که از نظر اونا جانشین امام زمان بود رو کشتین، اتفاقی افتاد مگه که الان بخواین با زدن توالتای پادگانای سپاه اتفاقی بیفته؟
صرفا این حملات شرایط اقتصادی رو سخت‌تر می‌کنه همونطور که امروز دلار ۱۸۰ تومنی رو دیدیم، خود ترامپ هم می‌دونه تنها راه حمله زمینیه و اولین نقطه هم خارک ولی جرئتش...؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67607" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67605">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=GtM2TQEPDCVZercTyfQAI_2sIEXTaWCzg_TTZf4trui7WjxwqWE3P24CR2mX_t1KPgqXrCLy1f4qh1i8XJ4lodqG2fBMptnqCGX7Uc4z8_AiodxBUvBMi1jlpxKI35eEsADgDZBVf9oed7qoImh2rPU4R0UwJ9gRV3gkXvAjwHuMOIODIMNAsbDeeR973OHiP2jSBUTFlwafJFxZLclPbgyiPSbphXfFPDWovyZcYOLc4pwhFF1mY41knShhpQrwnZI9JvXg9M3nKa6XndFISgya_EGfdd0uqpoyhaZHicC1GiBjkOuoyAsH5di0FRHob1h3HnD9BVfgabn1TyJesg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=GtM2TQEPDCVZercTyfQAI_2sIEXTaWCzg_TTZf4trui7WjxwqWE3P24CR2mX_t1KPgqXrCLy1f4qh1i8XJ4lodqG2fBMptnqCGX7Uc4z8_AiodxBUvBMi1jlpxKI35eEsADgDZBVf9oed7qoImh2rPU4R0UwJ9gRV3gkXvAjwHuMOIODIMNAsbDeeR973OHiP2jSBUTFlwafJFxZLclPbgyiPSbphXfFPDWovyZcYOLc4pwhFF1mY41knShhpQrwnZI9JvXg9M3nKa6XndFISgya_EGfdd0uqpoyhaZHicC1GiBjkOuoyAsH5di0FRHob1h3HnD9BVfgabn1TyJesg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدئوهایی از لحظه حمله آمریکا به برج کنترل دریایی اسکله شهید کلانتری چابهار :
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67605" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67604">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
انفجار های مجدد در جزیره بوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67604" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67603">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ماشالا ترامپِ شیردلِ مادرجنده‌ی املاکی
😊
#hjAly‌</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67603" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67602">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67602" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67601">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcxXEYQ9NgX2C7l_kn__70M2WfZbPXSLOaubGi7Vsx6fg2w-YWaoZhBSGWLaabssmQIDU8iACeUECS_lgK-wCoI5q8gKvQlB6F2AMXXPYQMumqXL-Ac7kNlyQ9zn6iUXSLjdEuup7c7WWnf7daK5CbfXz9poXu1lM6IWbI3fSkvH7nitgZB81E-Zc8gCagLp2Z9RCqm0Dni_zIN-Vx_uYhLZOoo1OY2LFXn7pnXcqZ8fofBuJItN2FtXqoyHq_a-uzmfpVc2qlNsWNRp44uVHCZCpzA7TOsNVAFMXw9XkE_d9fxEAKeYaFSQV-ZN0JRKDLyVf102amPT8MQoAr3ReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
یازده فروند سوخت رسان نیروی دریایی آمریکا بر فراز خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67601" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67600">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvEXFkMC-UPpCAo5Vm9ymsrfd0HsO0niFe4WwrJDnFEjhSuVr4sjbhgW-PiyB-_umVk-sKjaJOLNBjPB_Z03PgOLyMRFsnCtZYczhO01Ms_YbF4mrBBLwZDP4ztyibX4ciUGTJLEC5iCMrKm6uEOLviNkQEyMCBcVAJKDJpkkEYX6fjQvAE3ohfwuo1tbXKo_sHmIpzJWUxktY9KAz6UeYdR14k-ZbXUrM8Y1atvwQ1Nkd3sCvL8XmxFMMgAh8y_KkganW6DA1cWoG8acnqFQSOEAH_WZxMUmkOolouPVfnwhL7NHGGn5tAzn-Kn4AYAKD_LBxoUbPZgLX5mjklI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت شهباز شریف بعد از حملات آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67600" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67599">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
صداوسیما :
نیروی هوایی آمریکا در حملات به چابهار، اسکله‌های «شهید بهشتی» و «کلانتری» رو به همراه برج کنترل ترافیک دریایی این بندر هدف قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67599" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67597">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dch-CvsK5bMsL6jpaG3jbVyUKM5xR_gq8mFBdWjCGlNRhGI-dg-bcyWO6xWO-qQMfIlqeDKR_ZFS9sqAUjr3E_Af5PAKvf2ScXsx-iw5P8nNVkVw4jd-vFC5hPrWAs91cIxSTHrEvfzrj77YXFrkMJ0OSLtk2PeLWXdgvwIL5Cd47sb5CzflXjrV90lrXpwPR4s6U7VoghySLY6zyFahSnRxH29AiA5Dvrqqaugzrpr9I9xGyR0cg_8lQ5-DllVJOVxfhj7PmhcIaPSI4HH1eC_AeqxH4-q9ZtrD5W2KisBwUHprAnvq3kPlMXiVAtWSYOGONgVA33UzK25Gb2ig1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ad_pvbekbSIk0EuCRKGq65lHbEnpOPUL6X1tEp_ADA6wXW1eTgLUpCMzFDlImXJk_k2flLJlkkSivYol0DXBFKZ1wBriig51xT5cfsK1BRDiwNS74V0LUthR7032pKMIWWgvBdanhN8752hznyiTW0nmRd4NToRAjkBjG3-nzWxTLXPmEUl2SelXEuGEZGkBLgeDfGyRViXxh2GKMBHZW4m1TGhcAP1Wt6GZi0DvrH8WX2OvUE2lOHtueOfVN6TdnyHcf3rTA68Bb-aX5JzcswQw63pc62pwi-3ORIZRtq1hxPCkDy1c8X2w-HP1VZoo217xylDdHHO7eMYP7r_jpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
برج دریایی اسکله شهید بهشتی چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67597" target="_blank">📅 00:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67596">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇮🇷
محسن رضایی مشاور رهبر:
دشمن متجاوز و همدستانش به شدت تنبیه خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67596" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67595" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
چندین انفجاردر بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67594" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
فعلا تمرکز حملات مربوط به خط ساحلی جنوب کشور بوده
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67593" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67592">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60497304.mp4?token=RagYa3_oeLBs9yYBXjoBTbuB_4bxvkZTUwROZxo7gLN8r7cAE65rurPIHYHMq3-KMd2UM1V1KN6e4F35h7s5tEGYCb13xpJQr5uLaS_9q0320BF_8k4UyA_h8mUhl8yyj8EnviTfgk2-ztcyfJ6Vw8whdq74tH3rYNG5xxKMc7gpXh7RVFzIjuUa4Rl6rD5vd6-QC--EIAM-y1Ep9TbY4UkQ-76WgAz5ntPuFAkqAlqjV-2XmSorhX5Z0uE4R714QWl1K50ZfFYS5j3NVex0pDxYae2pZgcfMU0l5QQ4WFCuWHWsVpR5GO925bKg6F0garaoA4v2GmqBEseDEmahzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60497304.mp4?token=RagYa3_oeLBs9yYBXjoBTbuB_4bxvkZTUwROZxo7gLN8r7cAE65rurPIHYHMq3-KMd2UM1V1KN6e4F35h7s5tEGYCb13xpJQr5uLaS_9q0320BF_8k4UyA_h8mUhl8yyj8EnviTfgk2-ztcyfJ6Vw8whdq74tH3rYNG5xxKMc7gpXh7RVFzIjuUa4Rl6rD5vd6-QC--EIAM-y1Ep9TbY4UkQ-76WgAz5ntPuFAkqAlqjV-2XmSorhX5Z0uE4R714QWl1K50ZfFYS5j3NVex0pDxYae2pZgcfMU0l5QQ4WFCuWHWsVpR5GO925bKg6F0garaoA4v2GmqBEseDEmahzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67592" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67591">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67591" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67588">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drFBQes7UlJH_llbEiuJGrPgGlLdQ0Ruf-TBgrFCrNJ5PbEBR89gAfK6mxCOvjGwmQSLwcZig3Oe_h52eVjtkuq4XenGX13e6n1BHt_WsUndQs34mC0YL_VOYqluEJsIh1V6WE03dBlQKrsTu6VWo3z18Ksz-bdCNL630zxvSg4f3bgma9bK8UMHgLn2qe1ZVrKqOSQQTfQZ2hPt0peC6RY4LfG4p-u5CmUXm_crDqxpHF6yWylBzhGmXRtA0efOoCihhdLas2wj6DU6PquGKK8Ar1NNdkKsSm34T3KQSQgZ_q2GqU3roD4TWezPqj2m8mHOe8UuLR2i4plqLzTi8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=W5tvRiDZtlESwOzt97x5Tw5XxzP7ACLj8NXT_SwK7MI7APqbQ5WKQ6idacQnrrzVllKq3DZVajuzuAHBZOTN4srUyFSijUarnCfgd9rTR3VRbiTHQ_G8h0QFl5ZfqyvHwPJb0G-xmYYloypmjJ_YrUjnsA8wdGNHS2qGH4y6THSxuXlgxUmcU733aho6UWYv0KQ0So8ZGSqWmj8oEBPARak3jS2GnSJ6lC9ssakKDi8ntVaFSNItPwN99R7g_NgPkoRoLgYRfUfUDjBf1qkdvEz742rVLS_TJVYGfR11FscRFVPCnyP6kvSilcej5IWEN_9Tv7yHkQgvtgyiXzy-ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=W5tvRiDZtlESwOzt97x5Tw5XxzP7ACLj8NXT_SwK7MI7APqbQ5WKQ6idacQnrrzVllKq3DZVajuzuAHBZOTN4srUyFSijUarnCfgd9rTR3VRbiTHQ_G8h0QFl5ZfqyvHwPJb0G-xmYYloypmjJ_YrUjnsA8wdGNHS2qGH4y6THSxuXlgxUmcU733aho6UWYv0KQ0So8ZGSqWmj8oEBPARak3jS2GnSJ6lC9ssakKDi8ntVaFSNItPwN99R7g_NgPkoRoLgYRfUfUDjBf1qkdvEz742rVLS_TJVYGfR11FscRFVPCnyP6kvSilcej5IWEN_9Tv7yHkQgvtgyiXzy-ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67588" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67587">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=VSdKsZNyYoPUPzk3hPGc56r4Q0jlI5IHSIxU6YO_LO_OzCJi02JWliZa7sE_uqpPunc9pvyJnfp_1dVT9sbM0aViwhH4FjoX5BnecYvcOjtNJcQKKsQLKbez2f_pBhoYNQeY95SGAuAZ0l5CMAay59LEKOYsUvlzfOCsi9y0MRnCkuRqTqMjQC2mOZO0MGqANj8acG20xZYLtZ46IXHbIeXkNPRWXhYg0Q_gW1W_f2FUf64viWYI__Xn6vHOtpOKF2kft1lnnJSl5rVFRjZhZsAjEIEjI2VzA2WMXNY6R31ArG6mlmYt5yyxTtPQso79csIcWfSA5tGh1oHIfsX9Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=VSdKsZNyYoPUPzk3hPGc56r4Q0jlI5IHSIxU6YO_LO_OzCJi02JWliZa7sE_uqpPunc9pvyJnfp_1dVT9sbM0aViwhH4FjoX5BnecYvcOjtNJcQKKsQLKbez2f_pBhoYNQeY95SGAuAZ0l5CMAay59LEKOYsUvlzfOCsi9y0MRnCkuRqTqMjQC2mOZO0MGqANj8acG20xZYLtZ46IXHbIeXkNPRWXhYg0Q_gW1W_f2FUf64viWYI__Xn6vHOtpOKF2kft1lnnJSl5rVFRjZhZsAjEIEjI2VzA2WMXNY6R31ArG6mlmYt5yyxTtPQso79csIcWfSA5tGh1oHIfsX9Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67587" target="_blank">📅 00:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67586">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره ابوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67586" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67585">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=vpwIswlQ53Inac1bRDJPiHAgm7xO9GamNa_s8s5VLVl_1eKh_2mRq9vwKv8GtlAXqKoyT7raYVrGjV000-YMfFjwP01KbU7fg7UTwArqp_m928fbDaALk7hGX7puBglHqcI-4_hiPK5DL-PQHvjphk7zAObMP9G9w6-d7n4tlomrcy46wu_2gxf_kQ5qUmxBJrWv1eThLco4khp1u_TtSSoNqkAgpTuqAm2_Qm83zCsrHJ95uNptVIdCCioYlXBNitIEq3-1rWIribdriT_2U6D_aboKjBOcpsU76jdCQzCyCYaxUd2HfkIeO5QqJdPNfSD936iV0I9GfBAEL1C-sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=vpwIswlQ53Inac1bRDJPiHAgm7xO9GamNa_s8s5VLVl_1eKh_2mRq9vwKv8GtlAXqKoyT7raYVrGjV000-YMfFjwP01KbU7fg7UTwArqp_m928fbDaALk7hGX7puBglHqcI-4_hiPK5DL-PQHvjphk7zAObMP9G9w6-d7n4tlomrcy46wu_2gxf_kQ5qUmxBJrWv1eThLco4khp1u_TtSSoNqkAgpTuqAm2_Qm83zCsrHJ95uNptVIdCCioYlXBNitIEq3-1rWIribdriT_2U6D_aboKjBOcpsU76jdCQzCyCYaxUd2HfkIeO5QqJdPNfSD936iV0I9GfBAEL1C-sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هم اکنون؛ آنتن زنده شبکه خبر
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها بدانند پاسخ کوبنده‌ای به آنها خواهیم داد و امنیت را در  هر جای دنیا باشند از آنها سلب خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67585" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67584">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=fb93HiJEsDTkzxiEK9T0Fe3FUUrI0PEfwz_yE5hq9wuYcBV-BZPI-qkQRM4GJfbotD5ypIZTVqVa012SREhF1pmQcmwGrIBGW4gTG1v1_MFEM_7Mg4FhTI42tmpGDObeim3R_JjdL-0Tx8NWLkdYoGrzdGZBkuOC0HgCu0Vnu9XHCDOTQNFK7L23tzHQJ2l1izUh6MWxvhjybqSdtrFPHGyQEk2qWKmS8ARfWpImbw0G4M3Nm3Xxi9RoMxFNDh4K7rg619v9UE_8lc_hOG3c1If0Gw7Qe7G2_WHzk6cHNVzOogINzfufbja1IPmkBlpjBLVKx5w7r60WFaUQPczrRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=fb93HiJEsDTkzxiEK9T0Fe3FUUrI0PEfwz_yE5hq9wuYcBV-BZPI-qkQRM4GJfbotD5ypIZTVqVa012SREhF1pmQcmwGrIBGW4gTG1v1_MFEM_7Mg4FhTI42tmpGDObeim3R_JjdL-0Tx8NWLkdYoGrzdGZBkuOC0HgCu0Vnu9XHCDOTQNFK7L23tzHQJ2l1izUh6MWxvhjybqSdtrFPHGyQEk2qWKmS8ARfWpImbw0G4M3Nm3Xxi9RoMxFNDh4K7rg619v9UE_8lc_hOG3c1If0Gw7Qe7G2_WHzk6cHNVzOogINzfufbja1IPmkBlpjBLVKx5w7r60WFaUQPczrRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67584" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67583">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02d221609.mp4?token=lRCAu_PeCdiYVfXGfxNcQWErdoFsXQu_kSHt-Bitszd1KV3yAPU1ltYb2gl1VIx7STfG8MpclvU_TzxCgZoPngR6MDdTHvwKGTLbiC0v5tOVlowe_6uNdTxttDAGbIa1RcHcVsvnQLO_hb59r9w_-CjhoyNL1wa0zXm78KMQzszWBxwHtc3xbny4-qcPvZoqEHB8C5080cjsjp7Fgx8rizkVuyWl34SSpcEXcZej77Db8AtzpE_kJAqIaP744XB5Ak3VgCKOd4jCB-ADVe6pJnKfPDxt4KHdyUmf1uMSoLKP7hWackCHUfLheW2mKQ_iich_agxWO5ZZDSh1D0oYTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02d221609.mp4?token=lRCAu_PeCdiYVfXGfxNcQWErdoFsXQu_kSHt-Bitszd1KV3yAPU1ltYb2gl1VIx7STfG8MpclvU_TzxCgZoPngR6MDdTHvwKGTLbiC0v5tOVlowe_6uNdTxttDAGbIa1RcHcVsvnQLO_hb59r9w_-CjhoyNL1wa0zXm78KMQzszWBxwHtc3xbny4-qcPvZoqEHB8C5080cjsjp7Fgx8rizkVuyWl34SSpcEXcZej77Db8AtzpE_kJAqIaP744XB5Ak3VgCKOd4jCB-ADVe6pJnKfPDxt4KHdyUmf1uMSoLKP7hWackCHUfLheW2mKQ_iich_agxWO5ZZDSh1D0oYTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67583" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67582">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
نور نیوز  :
به زودی حملات ایران شروع میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67582" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67581">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=dFFmDSa3FTfkg5nZrJlTiVdzyFJxlEOoXvbKam5S1KlH2IAzYO6wIkK5teL_BmDK3PcD7wpIHaFZAPVccQMvaC8NS17zPYi7OeDr2TlXtNa4hNAYStVtR20XggLRJlBf4s9o4MMuArGzxVQAbEQjJPNm2_fq6mobUdak6tHPRZfo-SK2sFGYjYfzQbxeTvw_lday-p8S29FT0GeifFE1ZnMrpdDelh-w1UC96UPkR09S9jWOd-xPdc0uZCFitCzeinN2WnJn0y3Z927KN8WfaKrtHUS6beFOIrmGz8obB2V4hZgiCBDybhoJsJDZdfSlClxlfZQTLABdh_XJpjsKcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=dFFmDSa3FTfkg5nZrJlTiVdzyFJxlEOoXvbKam5S1KlH2IAzYO6wIkK5teL_BmDK3PcD7wpIHaFZAPVccQMvaC8NS17zPYi7OeDr2TlXtNa4hNAYStVtR20XggLRJlBf4s9o4MMuArGzxVQAbEQjJPNm2_fq6mobUdak6tHPRZfo-SK2sFGYjYfzQbxeTvw_lday-p8S29FT0GeifFE1ZnMrpdDelh-w1UC96UPkR09S9jWOd-xPdc0uZCFitCzeinN2WnJn0y3Z927KN8WfaKrtHUS6beFOIrmGz8obB2V4hZgiCBDybhoJsJDZdfSlClxlfZQTLABdh_XJpjsKcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ریشهر بوشهر دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67581" target="_blank">📅 00:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67580">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=lXRjYg_-0XPpqM9QCUpbwGt0SKgJY6_9GTtDfUbuMEyS-XudDNycHgWPg5fDX34Ee5PhfBz3pkCAwVqu4Xutfp4kZwW7cp6zQogfseFbqgYGuLN2p5ii3ksZ8E3R8DUoVY1g1MugFDwR6xhTCbJy8_-tIJwKB0C0NSS3QlMEjkFdC0BqN_YKkf4I2Mq1ZqL1tpH95iK0OQVh-j_jnu44OKCK1DMLlafjr7fNNyyiO6x6cZgWNFj2Cd5cp89Mntok6U0_rThnNg9sNlRMhPPrO0_Y-EZKke0qcu1j21rViKzMJMTlOzuVIKgbkvrNJib3o_Lr7P24mjO0WX2rq37Zkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=lXRjYg_-0XPpqM9QCUpbwGt0SKgJY6_9GTtDfUbuMEyS-XudDNycHgWPg5fDX34Ee5PhfBz3pkCAwVqu4Xutfp4kZwW7cp6zQogfseFbqgYGuLN2p5ii3ksZ8E3R8DUoVY1g1MugFDwR6xhTCbJy8_-tIJwKB0C0NSS3QlMEjkFdC0BqN_YKkf4I2Mq1ZqL1tpH95iK0OQVh-j_jnu44OKCK1DMLlafjr7fNNyyiO6x6cZgWNFj2Cd5cp89Mntok6U0_rThnNg9sNlRMhPPrO0_Y-EZKke0qcu1j21rViKzMJMTlOzuVIKgbkvrNJib3o_Lr7P24mjO0WX2rq37Zkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظاتی از حملات آمریکایی به شهر چابهار، ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67580" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67578">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qh0jhceNws4Ifp9G2MqwwCvrOXcu4iGatVYzUleADteWsjSwXOktFXDYlQx2q8nzi4_R9X_8IBAeN5UdNbaM80xCZRpytCHRTPQxiH9Lj1wifCU_k16nrLVuCDpvtdK2nX8PxwfqQO5EE5XPlHCEFX-a9a-1zHdC4TpAfzlH9vEcW91d_wft4wZRu3q_t5Mp71inOx4DSdFoMEIj7-nodUGaUCG_TEG3FugvITE7mDC-qTUb4YrLIiN8-7Aqkru6x8djjMgiGHeMiGAyegZiE3Fd2uypxnLO8NdNY9BwSZmnm0x3PGwCBYhdjEMhbk5AbT1eOd6EX8K7A-juvg2aRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ijw8AUeyo-9nNYC5-8clJ_LZy_Ki61WOXJ_8qQeOOz8lKLEscu8S2sqP41YHUO6f0Lah61yOdsEraM0Zfp4KAw9JN2gNMpiI07LfJlSmgkT-XRGRgpZXiP18rUiBy5b0hft0Ud6YQ3HiOICnoodiIVBom1p3HY7-zlE1Iryl_pb-5ibPk5hOC2qV-HCzCk81G2ISI0ZNDWV3BgIzemN9tRY5mtGK023wB8ZFf_yhMOkcdWKG0RWgax5TK2cIuE7nN_N9a6aRz1vlHnbC_9RIzaGSwNUydVjzOwHrN9r3h4K-ze1GNpSJyUNzQAw2Aj4rRhxlah8op-gvCFOP0mWdUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به نیروگاه برق پایگاه نداسا در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/67578" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67577">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=Xq5xkBT4hDCXg2o4gAK7aqKTXgLqdxzfWoWu1qm8k_WlW300c8mjw-eDhMxlkrag-PPXmkWAwAccJUs8rswAPoYTDkNqFw3MUMNYKgrIKcIobLJemahd9R1o7jBe-8-GHFwJy3NTwmjs3XgMBv4sGyHEaH99UJc725WsmOckOzNAE_xKHQT3Adz62iWJvhG010RItzVOfL3-d0T0KSm9aCRbAQRlGz_fvxhB8nNIHbtvuhtExn0hL-KfrYliASjWcGUHxNN_A2CHMoIOaartnTchvlStPg6NYFEGqQ0WxfD79sZwfMd0ln_8ka70T0cLUKo61JaJWUXNZnLdRidzOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=Xq5xkBT4hDCXg2o4gAK7aqKTXgLqdxzfWoWu1qm8k_WlW300c8mjw-eDhMxlkrag-PPXmkWAwAccJUs8rswAPoYTDkNqFw3MUMNYKgrIKcIobLJemahd9R1o7jBe-8-GHFwJy3NTwmjs3XgMBv4sGyHEaH99UJc725WsmOckOzNAE_xKHQT3Adz62iWJvhG010RItzVOfL3-d0T0KSm9aCRbAQRlGz_fvxhB8nNIHbtvuhtExn0hL-KfrYliASjWcGUHxNN_A2CHMoIOaartnTchvlStPg6NYFEGqQ0WxfD79sZwfMd0ln_8ka70T0cLUKo61JaJWUXNZnLdRidzOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش سوزی در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67577" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67576">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
گزارش‌های اولیه حاکی از آن است که هدف آن‌ها نیروگاه‌ها است. قطعی برق در چابهار گزارش شده است.
هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67576" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67575">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
انفجار های پی در پی در بوشهر و کیش.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67575" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67574">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مسئول آمریکایی:
حملات به ایران، رادارهای نظامی، پایگاه‌های موشک‌های ضدکشتی و سامانه‌های دفاع هوایی را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67574" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67573">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
❌
گزارش‌های اولیه حاکی از آن است که یک پالایشگاه در جزیره لاوان مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67573" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67572">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJzlQauLq3B6HPHSO5mJezgszNUyAsccr1OzpqspdpTlfpfWsVkVzYvs1VXXpXQIKqj8bW6344I_tFLkL0LnGKlJEVmcjpkVGr9RY43KSmFSMRc4cdN-X8F7ce9ptyZS6B99XHQN2VwvB5qcVObP4UidM8F55DV9_e4TovO76RS8m-m_1XPdrd4VBsbtCkK36WV297fF8Q-9fDK3wtpRT28tgpy36L5RUda45DYG6y4tdXtFra0onMKxz4oGjnhNh4zPe-U1UJxQGXsHm66lShljkDQxb3L1qRUUMY5xdwy8tpTFsEu-UcruWc7W5j7C-2jtuDRfB5d7P2SX7_zwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
حملات آمریکا به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67572" target="_blank">📅 23:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67571">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
انفجارها در بوشهر و جزیره خارک
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67571" target="_blank">📅 23:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67570">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67570" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLAKxht-UjSSTmyOVaYsfgQt46OO0FqbHwUe5wKJJUWZYEXJHxdVPSLc2RmLPBkqmf-QKlZlKeenCraPZJ-tVzvrvVjOVOveqn9CyaP8hQ4Op81nL4RISm55fWa9lIVLfPkJQ-XNcUGPTP4lH-eLDd0jbo8E7TRnG0Kq8dZtBbd_HOjIDHTzqFjUIt91pGQpJCyyNGEQjf1_v0p_krfbOdZjqxKcHYHoyrKgo8QKZZSrfoQfk4M4--FoWR_buTarVa5zMHNnhrghLyIqLM_7mOGF5OpWEn8yaZ6lljl4CrIUSChOA8f5kr4qTnuEBOmPFBWZywGSq8rRH0hnOC3gRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، عملیات‌های بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند.
ایالات متحده، ایران را مسئول اقدامات تهاجمی اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67569" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67568">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
صدای چند انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67568" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67567">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مقام آمریکایی:
ارتش آمریکا در حال انجام حملاتی علیه اهداف نظامی ایران در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67567" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67566">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
پادگان ارتش در کنارک توسط آمریکا هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67566" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67565">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره لاوان
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67565" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67564">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=raQcf4ksnVP-qGb9b0yqG_mKhoAX--H4BwdHZuYlhvxW6Ouva44QMp0ghaANVlf5WCPLa10wzcIhnnWjI-r6wkrhtHdwzbFf4xoRj3t8v8hNbPC4LFldp05KvSoSk78biJCQF-9Jz5fxZOOA81s32Kb9J9QiieylP2AjDl3WZs7Wsz0bGwqjIw9VzdSdiofg2YRITdHp5OUIMQ9ymdu2wtC4N17BDuNutXUxvXBhD-zSWYXbkA-mrWmu8vH8SERMzAPfCz8k8rpxKBBVsLvrcFFeWosLQceBVof2P2QkvDJL39pNUEpRXHITv8LocSeE81PDKBzBr1anU11FkzC3Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=raQcf4ksnVP-qGb9b0yqG_mKhoAX--H4BwdHZuYlhvxW6Ouva44QMp0ghaANVlf5WCPLa10wzcIhnnWjI-r6wkrhtHdwzbFf4xoRj3t8v8hNbPC4LFldp05KvSoSk78biJCQF-9Jz5fxZOOA81s32Kb9J9QiieylP2AjDl3WZs7Wsz0bGwqjIw9VzdSdiofg2YRITdHp5OUIMQ9ymdu2wtC4N17BDuNutXUxvXBhD-zSWYXbkA-mrWmu8vH8SERMzAPfCz8k8rpxKBBVsLvrcFFeWosLQceBVof2P2QkvDJL39pNUEpRXHITv8LocSeE81PDKBzBr1anU11FkzC3Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات سنگین آمریکا به پایگاه سپاه در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67564" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67563">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به بندر کنارک در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67563" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67562">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
گزارش صدای چند انفجار سنگین در بندر چابهار
به پایگاه امام علی در چابهار حمله شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67562" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67561">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
خبرگزاری آکسیوس :
ارتش آمریکا امشب حملات بسیار سنگین تری رو به ایران انجام خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67561" target="_blank">📅 23:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67559">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgOjXHdIgq9tfpLYCWtQHgy4x-glpU3GRAVOTiUSt5-MMofEtpx2TOv5sW8Mps7hXRb8XLieZqP1T60msBXIsK1nb8yk9G0zgZoPYu74_cf2mTIx66E4b7g7PoYiur9u1iDGP30dxVuCCuTQt2edz2KfBy3zh0OImBjDEo1eHMqFGBI3eFDcqedhWh94G7fvWjZYytadc9uho63W8IM9xXfvCoGxR_0lGGPN109NT63OM95DgK4PGFyDsY4gWC5c8_-9dQ3mXewp3JR-1mjmfFu1romC56G7NKJbWS_h3gofafNRTJj7BXlxOrznd2wgDPUp7n1CgNZJxFpET_-ARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDBXJCT-BplNzxAGPgske1L3xKj4B6usbtJusKoqiZbX90ogX3AhD33trTlTaRsWnf0fK1L8pg_PoO0kZYSJ7jaJEKEnHQqp2o4Dw_y__dtEbf2-EIOvkGjfNXgPgdboFHIqni6C6vLgYr7WGxQUHZlwWgwXcR1DjvH3CMvmjuRF1qYv6CYi5od4s1vUloS2Y8KE8RvzmrcoKm_0D8GI0U70Q5z8so8IqNBn-VqmpT4eGyC1Q4whhG_czPMfS5OpH0Ovh4Gx1Y0kBVcBI07KvcYuymurdup_PGvMJQsTVUHq3NgsUk_XegxcwZZuQYRFI-lm2H7ZfpeMnk0CAxzYIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
بلند شدن سوخت رسان ها از تل آویو و امارات به سمت جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67559" target="_blank">📅 23:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
فعال شدن پدافند در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67558" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67557" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
