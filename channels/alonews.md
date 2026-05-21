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
<img src="https://cdn4.telesco.pe/file/GH370c3CoXfxxNOC_9z81wb50K6ayQ_3evKGfxtXiDv1_rvqF-b45Yp-8xjtB9z0ruJAaI_DXJzQ6eMQ17ZkyaSyaWwhkgDuOD5fM7wjVsDJbyampl6_ofJUxN1Le77qIgppXOXodv5EYvJ9iRqztQKo8fQ_QGb_y9ZG0468Ysn-5pz78RGerWQyZGEsyIOZT1HzQjeSWt5fgXcUMUNixH-QgoPuDbwfHcuf3cc_GjdtQg2TcXJudnGiKqmwH8s5lkFIg41KqgDktoxHjiAV7nvRjKt6klU0k5nMk24fo1qYnVq0-GJ6IZdMFVUbtVvvG_4QOcJ-YEtKS_RjIumGtA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 944K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 06:03:30</div>
<hr>

<div class="tg-post" id="msg-121450">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یدیعوت آحارونوت: مقامات اسرائیل از اقدامات ترامپ راضی نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/121450" target="_blank">📅 02:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121448">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
کانال 14 اسرائیل: ایران و ایالات متحده امشب از طریق واسطه‌های پاکستانی نزدیک‌ترین پیش‌نویس‌های پیشنهادی خود را مبادله کردند. هر دو کشور فردا جزئیات را بررسی خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/121448" target="_blank">📅 02:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121445">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bqm6RKpAU51IeRzBggxARZzQn3uhx76XQVPlBap_DqWyPNZqKLeik6umV8CeBhx19TTMOCIeDakbLdq9RXQU_b4WBPOmTeha2NflvNh6qI8EJhkKZ_cYUk1OgMk-QLjtRNMD5xFvLZACa3vJueCdbmGBsjtkzjZ3hstoQn-dkvitxiiHqAxymaatOHjQnO-XDT43TNpdKLlBFzPnd2ybzCOGcGGCVsNN52xiq4DVj00O7mm9kDg_YvYvDSrnPkeB1Lb90DbQo7ZRDAUTQgyLwtB1UwH6sc5kUyQTctgG498ApbjIsLpuAiUWWSUhVLiU5LG0tS_qOzt6AWQn5CQtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mtyv9eINrp8YVOHsbhv-k5OeaBMQxdV2hVGSYEmj01rVPotzJbUH15vPDzAzkpflmR6ZLGatdbJvFZNhPU7jVDzU4tT5CQj57fVlBtejovGuCanlVHev1fLUzFl5foWIRWW8n8y9Zo6GOdCRfHk9GAXe3JuLavxvtv5pRDIiNH_FduX8C_aUwmWaAeT1pXFc5DoTdFqVebRsAWiNlC8Z6du3F8MLoAz4ek_zpjV_HpgY5RVfrZr5DB9u9erG_WkU2fYW1baggZlnB2Qw3ARrjZqv5dBg7Xj4CaNGPojTZeAtDHFkCKSR3KWcFn6SVIKNhWx-iYS9jm-XWXD9gIiKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqs__QyymFh1wf5ZUgl9DGZpZI0dWO3Lb7kt15q7qDhvNJw8QD9NsBdEzmh_hpcX3uP7BNU4cc36l1uSQATAXLvCv4lNuxqy75L4f8IKLO-oF6ayljP6HwSnGXWbskc8ovDIDOU4oRrw66xMIEsaN_p_2SVghysrLHpprZ7-Ycbkc6TuOxERlbv4vUkQqa0mRq8wRRVx9652_2Iq2gh9xfba1GidEab3SENYByT5-DT-CsBTq6LEtKt_4dCB9pEdC42KwydMyaaELeRk2kTb_ZIq2MxnEm0rjnRZDwlbfw_4F-Mjl_C5LbcMk-KR35ams6xg30v5a7po2SblWzqUjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کلاهبرداری صرافی
#رمزینکس
⁉️
🔴
پیام مخاطب
:
با سلام
من در تاریخ ۶ فروردین ۳۰۰ ملیون معامله اهرمی در نماد تتر گلد صرافی رمزینکس داشتم در عرض چند ثانیه قیمت از ۱۷هزار به یک هزار سقوط کرد و دوباره برگشت همه معاملات اهرمی پودر شدند با پشتیبانی  هرچقدر پیگیری کردیم آخرش میگن که شما ریسک معاملاتی رو پذیرفته اید یا بعضا قبول میکنن قصوراتشون رو ولی جبران خسارت نمیکنن خواهشا اطلاع رسانی کنید تا بقیه تو دام این کلاهبرداران کثیف نیوفتن وسط جنگ از این شرایط سو استفاده میکنن و پول ملت رو بالا میکشن و هیچ مسؤولیتی رو گردن نمیگیرن.
🔴
این اقدام صرافی رمزینکس مصداق بارز اخلال در نظام اقتصادی و سواستفاده از شرایط جنگی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/121445" target="_blank">📅 01:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHATzKZWFOYhMMyPM_-mxHYCp6gnaavZvtO8uTIL-lf8TSn7CE9P-XvWfigHQ-bO7d47oi6cHkJSPelDI2dRc8SizKwCPw0XZRIYTPwNyzN8nUq2xe7UAd9zH95kMhswPG7viBVKzFVX3dAKyDuA10OC3uVOlPYMCUibRcNm2qyaHpnt7-H3jAEcJgnRScdwmFFnLSu-WmBoiTT-h6Bsg7Z-z2eKLXcDlHy1lnSRWLfQfBncm_6FcBbJoOQ9t8an0qA3pqrN4mGLQVZpe7eEhgm49tGQuhy9yaRrlTi3e00Xvc67xa3Aw__84WdA3YPZH_69DOiiVn9l5N8LkoFLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوستان این تبلیغاتی که پائین کانال نمایش داده میشه توسط تلگرامه و دست ما نیست و  کلاهبرداری هست و فریب نخورید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/121444" target="_blank">📅 01:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121443">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc4cff02f6.mp4?token=Jemw-fORjgnJHLDit5knD8aFJp8wV4F6bv1HH-qKcdxldsfo5dx-xgD7Pil5893xrGmZw7nB60hiyGW6eY5dPgJHa4dgj1jXaBstn4L-Gadb3xJr0kFIXryIxgjcR3kuXs4ktG2kylMLvDxxBOxGK9HD0jQSpyq-s36agmNhkM1ast6yY3pQCpGbUznK_JM2M7ekEefJ2kyQqKcHq8k-Pi1wQEdZhCPl8TQKjFrRTDvyKOMeoZuBc4Qc90amWkKp8s5NrH8q5WcYU9V_KWTt_e3577V0iiTjzAe-Ljcnp4Ap83oltLTindHMbwhp5-rqyD_6dRrGQEGlDN8rV3QIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc4cff02f6.mp4?token=Jemw-fORjgnJHLDit5knD8aFJp8wV4F6bv1HH-qKcdxldsfo5dx-xgD7Pil5893xrGmZw7nB60hiyGW6eY5dPgJHa4dgj1jXaBstn4L-Gadb3xJr0kFIXryIxgjcR3kuXs4ktG2kylMLvDxxBOxGK9HD0jQSpyq-s36agmNhkM1ast6yY3pQCpGbUznK_JM2M7ekEefJ2kyQqKcHq8k-Pi1wQEdZhCPl8TQKjFrRTDvyKOMeoZuBc4Qc90amWkKp8s5NrH8q5WcYU9V_KWTt_e3577V0iiTjzAe-Ljcnp4Ap83oltLTindHMbwhp5-rqyD_6dRrGQEGlDN8rV3QIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شاخص پیتزا تو اطراف پنتاگون رفت بالا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/121443" target="_blank">📅 01:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121442">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41972ea087.mp4?token=IjMIOaU4mffFQbZZ6OLUuRcMvWL0O3DyeGh-ONSqxHlHACfwnPUZO6o1-8BCWCN-aaV1vbwxjnfizY7ujUUKK5PBWJpH7OrRn3Jsd7TY3GfLRabAy1njj8tk57CrJkhCWacYqZpNrAEu7u96QN1LkcbTElt0pF_mEyIz51qZ2QSSmtrcpZFanm7FNvVNVDgIy8-2WBGVpysdsv_v9fHDMMkfVt_G0hWiGYr0YUN5gE5zRm5enkavM6xPqiglPv4QjwDvZLSc9nthKYfpcEcTQRA2iUBmY9pGhtnhaV3jiODqOKg4zG8cfzaALzvcEGbX_pJxsyu8olXdhgxPZc2Q6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41972ea087.mp4?token=IjMIOaU4mffFQbZZ6OLUuRcMvWL0O3DyeGh-ONSqxHlHACfwnPUZO6o1-8BCWCN-aaV1vbwxjnfizY7ujUUKK5PBWJpH7OrRn3Jsd7TY3GfLRabAy1njj8tk57CrJkhCWacYqZpNrAEu7u96QN1LkcbTElt0pF_mEyIz51qZ2QSSmtrcpZFanm7FNvVNVDgIy8-2WBGVpysdsv_v9fHDMMkfVt_G0hWiGYr0YUN5gE5zRm5enkavM6xPqiglPv4QjwDvZLSc9nthKYfpcEcTQRA2iUBmY9pGhtnhaV3jiODqOKg4zG8cfzaALzvcEGbX_pJxsyu8olXdhgxPZc2Q6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: پیامت به خانواده‌های آمریکایی که از هوش مصنوعی می‌ترسن چیه؟ اونا نگرانن بچه‌هاشون تو آینده کار نداشته باشن.
🔴
جواب کاملا مرتبط و منطقی ترامپ:
ایران نباید سلاح هسته‌ای داشته باشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/121442" target="_blank">📅 01:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121441">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56cea8257e.mp4?token=ZDZGsUsF1i4zil71NKh3crtiCgCnPtnaQtRxqL4JGxI4DGGVNYz9yiiRNUPyegKOzk6HsZdgFz7IUjaD7jYfsuLrh5lhEXidO5ivr2El6R4DlH_he9H9Lv7Y7wyerTQhxZEqZUW1tR12JfM0sR3pU1PqBtyF1YvM4bFKG7Od9DPORVMpkzvhobn-xQM68YRkFLooNFyYthoMEpgi0P9WmbZ7QCH9uJj1YfVh4bI_97eq_DmDsvJk6kw_a73Bv80Sou-dwMVfcDlwIEKmC65eAeniCl-V_9TRoCOlasTQZ5MsZRF_fWRlt5OBedEIXO46MERtAwFOZG092WJ3j1_SKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56cea8257e.mp4?token=ZDZGsUsF1i4zil71NKh3crtiCgCnPtnaQtRxqL4JGxI4DGGVNYz9yiiRNUPyegKOzk6HsZdgFz7IUjaD7jYfsuLrh5lhEXidO5ivr2El6R4DlH_he9H9Lv7Y7wyerTQhxZEqZUW1tR12JfM0sR3pU1PqBtyF1YvM4bFKG7Od9DPORVMpkzvhobn-xQM68YRkFLooNFyYthoMEpgi0P9WmbZ7QCH9uJj1YfVh4bI_97eq_DmDsvJk6kw_a73Bv80Sou-dwMVfcDlwIEKmC65eAeniCl-V_9TRoCOlasTQZ5MsZRF_fWRlt5OBedEIXO46MERtAwFOZG092WJ3j1_SKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر بهداشت و خدمات انسانی آر‌اف‌کِی جونیور: من همیشه در اطراف دختران جوان زیادی هستم و همه آنها در آن بخش از زندگی خود واقعا دیوانه به نظر می رسند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121441" target="_blank">📅 00:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121440">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2BiHwMG-jDoOM0_tzBUQyFvyfJHH_j180Ex6DSaG1hQp7aDeecIt-Wfsz_7SUN3PeJrGD5k2z8n6B1cUbWEJoxHqXGyYD6OvaAbrPiEDnFrvmSbKQsun4SzvGAyvHw_mWs_niKu2Xubg3lJXAiwlpfUyB8Gdziao_Ny_aCCuaRMpaYaRFedQJyHDDFpJcYXEOEF25pHmEzQGpDAXWvRySk4pTfBKqbUNudcZDdTiJwxjC5mz25UXPI_08ZC_3Uy1F--3Cmwc-xckU5QhkcTFHzR-sOu6gE06UtgV1UZJl-7E-3W5I5V94nIbabmGxbk9qYmAB0prf6pJMZTlUYITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بزرگترین کشتی جنگی ژاپن برای آموزش F-35B با تفنگداران دریایی آمریکا آماده میشه - USNI
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121440" target="_blank">📅 00:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121439">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjlE6GiiDrpD7ToWqCdyqyHe4VVAP5xxu33RkTptB6KyF8yRQsRtaQmNF1MTqdvb53iaWvVrhbjPeV5EknD8ydYuN9gT844UfZXQxDLhE12_vJAHY7XyDCA6qlAgTsKCNO0F-2AAeQ4lis5SA7t7ucbByYA7c5r5JF2KTb_KiRa727rqCkdbF7GZYx0yOqSPHv4QSKKdnyUxj3U294aR8mjK7PQT1nxjk4kG9CoUm2iBFyuIcuPq0FBcnFVtx6cAXA_32gE-y7E9pEL-kYnL0P6sB8OobMbMNo7AVPcHoNQExj2jaWEGBiIzCtLFc6vqbNeMm6iKBkAwbuKOBLlkIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه مارکو روبیو:
اشتباهی نباشد: ایالات متحده به طور قاطع از دولت قانونی و قانون اساسی بولیوی حمایت می‌کند.
🔴
ما اجازه نخواهیم داد که جنایتکاران و قاچاقچیان مواد مخدر رهبران منتخب دموکراتیک در نیمکره ما را سرنگون کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121439" target="_blank">📅 00:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121438">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
زاکانی شهردار تهران: آمریکا ته زورشو زد و دیگه جرات حمله نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121438" target="_blank">📅 00:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121437">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5AanDcQDzlK9DFxDI0WP9Os6MWCPEfE-hPdQ3qJtkCMbP7lFhfibEdqGaEIdf0224_1tHwlzaOFvizsk91fJl4VF3X-A0Dgy6oc8TkapuX181H2gwWyKjeusRMWK7xtjYcGs3hYqWuF2A8lyUD6fRdDsRvlEUfrnI_06acNbyZJLstBMy8gkFmNz_hRE1pQk98seRB4KpUPvFIyfuGimkAiCLd3ZeVtOQEQqWpNAVvNTzpDb26iQpq1jmrq3fMuN8EJnJ1RN0rlOXoW3HYOQSLZvx6WY8FqofNOmzQVUtkmQZ-ebvfdySQlR4XPnRd4Z0g-6e_XDXtjtpDyPqpPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تعداد زیادی پهپاد به سمت غرب روسیه و کریمه پرتاب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121437" target="_blank">📅 00:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121436">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ادعای «میدل ایست آی»: دونالد ترامپ، حمله برنامه‌ریزی‌شده به ایران را در این هفته به تعویق انداخت، چراکه متحدان عرب و مقامات دولت خودش به او هشدار دادند در ایام حج، جنگ را از سر نگیرد.
🔴
به گفته دو مقام ارشد کشورهای حوزه خلیج‌فارس، به ترامپ گفته شده بود که…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121436" target="_blank">📅 00:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121435">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فرستاده ویژه ترامپ به گرینلند جف لندری: زمان آن است که ایالات متحده ردپای خود را دوباره در گرینلند بگذارد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121435" target="_blank">📅 00:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121434">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ادعای «میدل ایست آی»: دونالد ترامپ، حمله برنامه‌ریزی‌شده به ایران را در این هفته به تعویق انداخت، چراکه متحدان عرب و مقامات دولت خودش به او هشدار دادند در ایام حج، جنگ را از سر نگیرد.
🔴
به گفته دو مقام ارشد کشورهای حوزه خلیج‌فارس، به ترامپ گفته شده بود که حمله به ایران در ایام حج، بحرانی را در میان کشورهای عربی حاشیه خلیج فارس ایجاد می‌کند، زیرا این حمله باعث می‌شود صدها هزار زائر حج سرگردان بمانند.
🔴
منابع همچنین گفتند که به ترامپ گفته شده بود حمله در این ایام مقدس که منتهی به عید قربان می‌شود، بیشتر از این به جایگاه آمریکا در جهان اسلام لطمه می‌زند.
🔴
یک مقام ارشد آمریکایی که از بحث‌های جریان‌یافته در دولت ترامپ آگاه است، تأیید کرد که این گفت‌وگوها انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121434" target="_blank">📅 00:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121433">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbr5YoF9cZO-8xgChg1N2po6iaditFhTe58vC4loNnzI1_E2k9XsvKZBrkFI7L8zk899t8PcHprPQi-szSqxl97T7cjeeArKmw7gC9u0MrDxB1B3mGf6iggTfA0SFnKoUmOeTonb04eTlIN9ZGiV-bv19mdQRezHJjAAqL3qwKCHPZFwBno5YUR_NYksmVEbonXcg3mIHqjWJJmNAqmQngppjr1nhVqPidfEE2M45FViZAe2DQ0GR8fEXwM-7mTkg8UXTzdcgihbArerMjGfqRBn8VdVOButk9B-QSekYQxfpP3j1lzaE6SjSB8FWkXVD26dEaVoCNIECVxKjw6hLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرستاده ویژه ترامپ به گرینلند جف لندری: زمان آن است که ایالات متحده ردپای خود را دوباره در گرینلند بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121433" target="_blank">📅 00:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121431">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqP18i8po6iUyxzZGsOKyDAkIOf3p4FOY9NVq6c-5jAoJm30iaIifsaf7UmaRe3qF89u-j5HaCf0j4OEYZXByxC8TPrmJk-pfcaDR54IoOztlDJx_yMta1VWULzUMDW8xzd37s-kmK-xqao6BFp-tnV1xlo0S6rT_TKdaG6eFExGPWLGaaxFa4TW-USn4y_wmALlgSycC74QXlhZ7HGjtk2BhoDtZUjsaJB767-id78H2_NVW0dYPUlD3UnR34Xs5L0MqBX6IicPzH90h7uFZ0IC4DNv36OnvpTFAzEBMtLGz5jjDI2Ez7p28YQDF1PTjeBkZffQBvSETKmQlG44fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ToTWyqRQl78IRGBmJDsfPtEi5iFAfP4ze_T3wYu6XKos5_DmDRQjGGkWWYyiLpV1e_tcfTxiH3V8XxTVI0_ko3swOAKR_Ypjc_mvPMmFfeyXb92BjpTl2KdFLZIdycRgUpfsEN4VhWxh7GuJ0rRy2SMvA6MSs7_kMO_17lGWKiVUhZOX8WuRlo8cAMd7O_8nMhIecw0ODaFgpQumkTns4W6QD4mj9ZeTJUn-wgGO8KMrQCEmXWv3r9XNTnxs5QU3QfLG4jPKiX85OjWAXHW8YlpqUMUP9XLJ9Jsz5PgSDfXv-yxgRq8rI3N3KIsZ7LVCYmQpdR14Jb5b41ofFgdAxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لکسوس LX600 غول ژاپنی با قیمت 110 میلیارد تومان ناقابل!
و حالا همون ماشین در فرانسه به قیمت 124000 یورو که میشع چیزی حدود 26 میلیارد تومن…
شما فقط اختلاف رو ببین
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121431" target="_blank">📅 00:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121430">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atJJNPu5g7FRTj81Kyvnghz0Fig53YDxZr7pnGNqr7MLKJqm91cAVZXsBPTKkagSf9QDEdB6p2U5yCLVUz-eYGUQg22o6Ii_tDxFmma6ulrjPnmbL8VHCLKzP_nOeY3GBKs1susfDbqrXTvYqbpm9LqosIi8qJeqhIakmniK1MqxxNgz7Njl9SfRB3AQqeAPYzBmW2xtZbRuQY-UfOHRx8irrGq3gxhJDBFkZbQdQfgOyY25bFjomt_YkTkVWcSHJ8aGJzYcsKvy7YFfawznHHZDSF1pZ8yqjizB8ZJ8Bo7du9XgsCF8i9FUVrVzjbMZdjvMWsB2mhN2uGO9tmO3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت آبراه خلیج فارس محدودهٔ نظارتی مدیریتی تنگهٔ هرمز را مشخص کرد
🔴
ايران محدودهٔ نظارتى مديریت تنگهٔ هرمز را به این شرح تعيین کرده است:
🔴
«خط اتصال كوه مبارک درايران و جنوب فجيره درامارات در شرق تنگه تا خط اتصال انتهاى جزيره قشم در ايران و ام‌القيوین امارات درغرب تنگه.»
🔴
تردد دراین محدوده برای عبور از تنگهٔ هرمز نیازمند هماهنگی با مدیریت آبراه خلیج فارس و مجوز این نهاد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121430" target="_blank">📅 00:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121429">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/121429" target="_blank">📅 00:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121428">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نخست‌وزیر اسپانیا: فشار می‌آورم تا کل اروپا وزیر امنیت اسرائیل را تحریم کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121428" target="_blank">📅 23:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121426">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R757crf25Qi7-KvP_DT63IvScZe_u6hdzgehsdOZox1pyvtn0-Ch4qNsaY7Fcwks1PJFN55sDLcOere746Qyyn1VHA6wfi4pQhzlGyWbheMoeh5vrSg623Ab6JX7pNUqddQ7ac_aKURd7ZJXhDkALo2oKgAbwk9QPFCnJZ6nJsDFFYzZFdLVqPOa8HkTZ3a_IqDuASmaNG93ENq2OEVEgNaEoUMS5brs3ybwfq9ioJTYsy5nrkEfcl-cNDq304N5wvIOl69Xm_Fq4gG4t9y_ZC-HbHOuNYu0yHD4ky39aJChIMlqPp2K_nfJwa6v8cVbC-oQez5C0XYABZEZmMacww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۵.۰۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121426" target="_blank">📅 23:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121425">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYvl7qjNpfEUcEIxQ7v455BmoL52o1h-FvKhhu0gD2xx9IaG_dnStzNFbOtF2lGz3FsIFFKYZYXTB9Rzyoolu-eJcQ4eJLLn4D1X1fK-Mkl21VgR8gOzVuwGqGji0O3fjmKc-Km23SyezwGZqvGurbnHhlduYRTkbBcM5Xa80pznjoANs3ye7_Q_mr43euRjqVBHinRweZas9tU6JKHDzvfc7_IU00GLwaj4wS_cAe02w5IfKc6-UZzZ7657MUuxfEC2FoFAqOkLNcNk1bwbFAg1ASw2KM1rwuB66R3X7dE7Q-FGfE0vqDk1bVVSVd1Kn3SbYP9uI9-QLiKipLU36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: یک منبع آمریکایی که در جریان این تماس تلفنی قرار داشت به من گفت: «موهای بی‌بی بعد از تماس آتش گرفته بود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121425" target="_blank">📅 23:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121424">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ درباره کوبا: مردم غذا و برق ندارند، اما مردم بزرگی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121424" target="_blank">📅 23:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121423">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NYdpH0Ovy0RdOkfCmKJFXaTq-9aejQs3XUZqsBGl2B6F6InHCfqEmjCPIPndRLgIpP9x2oDeD5tQ0zRh2Czxq4ZFGdC81LkIsP2oA7Q-o-YNJwDRtg9zXedJcJftb5H4yKkhfZLbJQvbhSv5b_wwPgN42l-fr3CHrm1TwxPzegtCLlIyv43jmmG2XGJrLz4tD7vIJhF7wigGozA1-LFkg00iVxKX2w0ymcX9GyOnxSMAxvP-k7GEte4DkOd0j_6BfXjYKYHdpKRmeExs_ra7RlkPFl5lHVbKt1_r3QZLED8PNyz9zlTopyerl1EvkOwvjZdFDU3FARzlj065D-JMdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر اسپانیا، پدرو سانچز:
تصاویر وزیر اسرائیلی بن گویر که اعضای ناوگان بین‌المللی حمایت از غزه را تحقیر می‌کند، غیرقابل قبول است.
🔴
ما اجازه نمی‌دهیم کسی با شهروندان ما بدرفتاری کند. در سپتامبر، ممنوعیت ورود این عضو دولت اسرائیل به قلمرو ملی را اعلام کردم.
🔴
اکنون قصد داریم در بروکسل فشار بیاوریم تا این تحریم‌ها به صورت فوری در مقیاس اروپایی افزایش یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121423" target="_blank">📅 23:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121421">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cWUDbq-Qso-bZeaICDw28NMj9dt9vU5WI_1tXQYrYPkGKPEp5TLTvko-bwP2vQzB_d36Yb2jeaJP5LnrFjm4ezD0N4O7AqNbVn7OpIuu21zdWSJYFWLCZq4-YonGlOEm2DWVJnW-4UxzzLlp7u9QIaFVHdRrhlv3DgqIFIvouyhcoj_A7-Z-m6draVww3uEcp8zB2wlQSej_KkWbyjyuQfevU5QuybqIPy-W70YXs6O88rcK_bCQncSsGsg2AxPId2wpFMpJOlUjJ4eyLizJMOVkDDhbGJoXGa5JlmiTkaGNhu0zCpDkvrKyxwNAVFGHLM69Dn0CoMWiDLfPSapppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dvr_KBXz5ukevM0TVGuldc6Mrlmdoes6sj9wxvS46cKZgJn8atZvMzex8GcCtyZJEbQrJcff4ndwuukgm1X-oRm0DrzGK3SQYOKsmq2K1CDq6GYYNSjE0JvpguG6Fe8UP42ql65sBF6GITggj3LnNG71jsvtccoktQD17ure7xHe3LmxTTMDVvJN0IAcCl1gcAqtYY9xLiyYGp09VCcA3adihgcrnZHTvop9LAMExjTBTAAYKeUt4p2hSJd5nesu_abScbqw0g3_bWTW8Pvb-hISoHnWLLfZ0N1Ry84kT6SHqp9eujso0t3Poq-hikaT9_ve0V42yooLAePq_0eMeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یونیورسال پیکچرز بی قرار است فیلمی درباره نجات دو خلبان آمریکایی در ایران بسازند، پس از اینکه جنگنده F-15E Strike Eagle آنها در عملیات خشم حماسی سرنگون شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121421" target="_blank">📅 23:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121420">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0624b84a4.mp4?token=aZ0UxAEbTz-jsFDM_zMjjrofJSPu3ve2yStPvfc2gfZMaSvgvBwZp1hfJhh1O0JW4p-C_p6XZ0vANUUH-rAEmAHSMp-jI8MrKwKfPP04Gc08twYrmXvdDAy6oKJHJJdlZmEvti0SYd7I2VxnBhxv__T-_eXwTWI5G7FVJeV-QbhWmfZNNQb8lQ5dnlkw8Uowm2ZpNVit8n3U8v-H5LRWKRksKpfJ1QIormVaDfmt859cOlDa4M8ulzzwNf4HlH5GkW1etZ0XHGgfMaZgp5j6UE1QaHGdQjKBLMZ3VnMT_Lzx51rpA4YszKpGpaRFXIbGfzJghDFCV7NPtWCN3iS_DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0624b84a4.mp4?token=aZ0UxAEbTz-jsFDM_zMjjrofJSPu3ve2yStPvfc2gfZMaSvgvBwZp1hfJhh1O0JW4p-C_p6XZ0vANUUH-rAEmAHSMp-jI8MrKwKfPP04Gc08twYrmXvdDAy6oKJHJJdlZmEvti0SYd7I2VxnBhxv__T-_eXwTWI5G7FVJeV-QbhWmfZNNQb8lQ5dnlkw8Uowm2ZpNVit8n3U8v-H5LRWKRksKpfJ1QIormVaDfmt859cOlDa4M8ulzzwNf4HlH5GkW1etZ0XHGgfMaZgp5j6UE1QaHGdQjKBLMZ3VnMT_Lzx51rpA4YszKpGpaRFXIbGfzJghDFCV7NPtWCN3iS_DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از حبوش، جنوب لبنان، پس از حمله هوایی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121420" target="_blank">📅 23:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121419">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c0740884.mp4?token=KTAdXc05uJXJbKl8YN3FGuGPP6OV1fiaG26sIyWc3-bKXaT8EK_2txKN2EayS28sipj_-3lunfipv5ctkzDv4FsE0SptWxkGXc4QEGcbIeHrLr9wloVQ72W74KTXijlYAB38FBXIFmM45Z0FjW8w34YlLxexcvxPsyumgh-EW11eB773HHgetGlmQeRqYgla6k_7IjfOnL62YSnL1cFYDuOT136MwUdIQMBJ-eETxzlJ6-N11dCs6tVYBF2nywTYLAcW6giixfBY7WklXRUPAaAnpfWMe0tr7uZu1zxqwzauFn0TXRebEV1X8fDBPQh3N68M3hycI8p3WI74tKYJ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c0740884.mp4?token=KTAdXc05uJXJbKl8YN3FGuGPP6OV1fiaG26sIyWc3-bKXaT8EK_2txKN2EayS28sipj_-3lunfipv5ctkzDv4FsE0SptWxkGXc4QEGcbIeHrLr9wloVQ72W74KTXijlYAB38FBXIFmM45Z0FjW8w34YlLxexcvxPsyumgh-EW11eB773HHgetGlmQeRqYgla6k_7IjfOnL62YSnL1cFYDuOT136MwUdIQMBJ-eETxzlJ6-N11dCs6tVYBF2nywTYLAcW6giixfBY7WklXRUPAaAnpfWMe0tr7uZu1zxqwzauFn0TXRebEV1X8fDBPQh3N68M3hycI8p3WI74tKYJ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مخالفت بنیانگذار سپاه با تسلیم سپاه
🔴
محسن سازگارا که خود از بنیانگذاران سپاه پاسداران انقلاب اسلامی است و سال‌هاست در آمریکا به همراه خانواده خود زندگی میکند، در این مصاحبه با تسلیم سپاه که ایران را اشغال و زمام امور را در اختیار دارد، مخالفت نموده!
🤔
زندگی و آینده 90 میلیون ایرانی به خاطر همین سازمان تروریستی به فنا رفته بعد این آقا از وسط دل آمریکا داره دفاع میکنه ازشون
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121419" target="_blank">📅 23:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121418">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ادعای کانال ۱۴ عبری درمورد اظهارات امروز ترامپ: باید به یاد داشته باشیم که او یک تاجر است و اظهاراتش با هدف تثبیت قیمت نفت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121418" target="_blank">📅 23:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121417">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a113557850.mp4?token=Buk3dKyF76uD6c60Ju6f2E7Kuvc4cbUDP7UIY3G9d-y3aeuLiArSsr5eK7pXANTKWJdbsogD4vFxU6f0L1Sem-4yg7OmMUBjaP-A_iifEQ2cfBRPlFd7qD9Zyr1U0YeVDGVvFscGTF-ByXokTRYsVlN7uLIT11OvXxGnZ23ZVXFud0ZDJ-yJ0JYvNvhUAtkqM21SF4hCBHM1ZNf-lITNqN0bvYnD4QqGXiCuVPvkGo0Xg7T44s_8vDBmuh59zcrBxrRnFAGbW1UUUTvi_g2Z7m0-BzGclH92JBxr3s8FpZU0ip88Jyp_PrFhuWogJpRXVDKi-MVSahpvWflHEu4oZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a113557850.mp4?token=Buk3dKyF76uD6c60Ju6f2E7Kuvc4cbUDP7UIY3G9d-y3aeuLiArSsr5eK7pXANTKWJdbsogD4vFxU6f0L1Sem-4yg7OmMUBjaP-A_iifEQ2cfBRPlFd7qD9Zyr1U0YeVDGVvFscGTF-ByXokTRYsVlN7uLIT11OvXxGnZ23ZVXFud0ZDJ-yJ0JYvNvhUAtkqM21SF4hCBHM1ZNf-lITNqN0bvYnD4QqGXiCuVPvkGo0Xg7T44s_8vDBmuh59zcrBxrRnFAGbW1UUUTvi_g2Z7m0-BzGclH92JBxr3s8FpZU0ip88Jyp_PrFhuWogJpRXVDKi-MVSahpvWflHEu4oZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زاکانی : تنگه هرمز حق طبیعی ماعه و اصلا نباید درباره اون با آمریکا مذاکره کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121417" target="_blank">📅 23:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121416">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس:
عاصم منیر فردا حامل پیام جدیدی از سوی آمریکا به ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121416" target="_blank">📅 23:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121414">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade9e3bc09.mp4?token=MJCj5aEq2Vq96msh1OIB7q-97kf0-8Ls6MTxQvEQPm31gedCPsYatu53IHS7Nbze8vMSHRX9wxFjzSEh_gzDunRPd5kmVFlDecRtckC6wHfRqv20L9ONGL4XAEqfmn9yTKbnn9TsfJ5Jtbl_KxWkOUDCnjIJGNS1kA6-Cke_0tTwspQFF1mnMtPwnQOG6PPUyZRjlYrS_Bfk1C214ZclLsdtjYjjkZVfOvxT2yFtXeaj-FOwZZ74KqywRm2FGPDwwv3xV4Wb4xQcNkTzkpT32pMlICn-_2fMoCEjlz9aZwsyYscna_E6hLf5rcpF8RYqKLqpUNSM_qvrKBjnVYXNdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade9e3bc09.mp4?token=MJCj5aEq2Vq96msh1OIB7q-97kf0-8Ls6MTxQvEQPm31gedCPsYatu53IHS7Nbze8vMSHRX9wxFjzSEh_gzDunRPd5kmVFlDecRtckC6wHfRqv20L9ONGL4XAEqfmn9yTKbnn9TsfJ5Jtbl_KxWkOUDCnjIJGNS1kA6-Cke_0tTwspQFF1mnMtPwnQOG6PPUyZRjlYrS_Bfk1C214ZclLsdtjYjjkZVfOvxT2yFtXeaj-FOwZZ74KqywRm2FGPDwwv3xV4Wb4xQcNkTzkpT32pMlICn-_2fMoCEjlz9aZwsyYscna_E6hLf5rcpF8RYqKLqpUNSM_qvrKBjnVYXNdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل، چند نقطه از جنوب لبنان رو زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121414" target="_blank">📅 23:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121413">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ادعای کانال ۱۳ عبری به نقل از یک مقام ارشد اسرائیلی: در حلقه اطراف ترامپ، بر او فشار می‌آورند تا با ایران به توافق برسد، اما گزینه حمله همچنان روی میز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121413" target="_blank">📅 23:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121412">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: نتانیاهو کمتر به احتمال رسیدن به توافق باور دارد و خواهان حمله است، در حالی که ترامپ می‌خواهد هر راهی را برای رسیدن به توافق امتحان کند؛ همین باعث تماسی تند و آتشین شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/121412" target="_blank">📅 23:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121411">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🌟
اشتراک v2ray استارلینک
🗯
گیگی 150,000 تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید پیام بدین : @v2safeBot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/121411" target="_blank">📅 23:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121410">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX1kEW-ysYoiC3sWxhYic_IPrOT6lOpBQpjJcz7RqUEdna87WwnJHDDswTOrW9pESMXEGiVaFWS-Vsbu4OYig1oShG6mGApRIbujkQL7qvlXWbaAqhgqLRTucFwtQQamHaJN0hoqGABZnjM8mz6e6dk_Fk9n3k29vc6avBwqI8V8p0tUaEMDKr8xWvfZ6a8_bSROjyZhN_COSH6s3OzpbcpO6psu4XIkXJCMEXhas4ZlGqylojYB4yNrVh3J2ecgV8rLg_VZloLby5dFGWEeZuLOryQ0-rj6Io8DUQw1gLKszonLVNGXgnn-XM2nOeVRyMn82Yd5-fgxxqqv9feAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اشتراک v2ray استارلینک
🗯
گیگی
150,000
تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید پیام بدین :
@v2safeBot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/121410" target="_blank">📅 23:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121409">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/121409" target="_blank">📅 22:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121408">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/121408" target="_blank">📅 22:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121407">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ درباره ایران: «شرایط در نقطه حساسی است، باور کنید. اگر پاسخ‌های درست را نگیریم، خیلی سریع پیش می‌رود. همه چیز آماده است. باید پاسخ‌های درست را بگیریم، پاسخ‌ها باید ۱۰۰٪ کامل و خوب باشند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/121407" target="_blank">📅 22:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121406">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff021af3e.mp4?token=PBAqVef9mlpGZD2T0KFfopPMlVh4VDOyzxMpFJUQmg1aEZDIzc50xwB7zcTjGw0vb6qMZT9htdN9rEdv3tvnmAbFTQdPv_u1Jxr6u0muUrAaRXgiaV7IahuHErK8O8WKJSJ-PucEwIG1ADUmWOTPJpmCCl1eZ1yYLdfLhUTLhvnbn8lwcbX9nps-HquRFOkeeqswoIkjDj_hZlTBwYjZR1rxtGc-QDJbKCw3rI6JR7bRKLgjhsb6OWuOmJLMWi5ZIf4suoDfvVc03Z7MzFDGpn-H9t01JCZTccbdByaNUMPngwlAtevsbK_cnOZUjVsCJRRnVK-jYVfe1AcXo0GZdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff021af3e.mp4?token=PBAqVef9mlpGZD2T0KFfopPMlVh4VDOyzxMpFJUQmg1aEZDIzc50xwB7zcTjGw0vb6qMZT9htdN9rEdv3tvnmAbFTQdPv_u1Jxr6u0muUrAaRXgiaV7IahuHErK8O8WKJSJ-PucEwIG1ADUmWOTPJpmCCl1eZ1yYLdfLhUTLhvnbn8lwcbX9nps-HquRFOkeeqswoIkjDj_hZlTBwYjZR1rxtGc-QDJbKCw3rI6JR7bRKLgjhsb6OWuOmJLMWi5ZIf4suoDfvVc03Z7MzFDGpn-H9t01JCZTccbdByaNUMPngwlAtevsbK_cnOZUjVsCJRRnVK-jYVfe1AcXo0GZdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : قصد داری به اونا ( ایران) حمله کنی‌؟
🔴
ترامپ : چرا باید اینو بهت بگم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/121406" target="_blank">📅 22:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121405">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3755e8a6.mp4?token=gHJR17B-vy5lhmaL2TFMWjw9OpXjWLKNB87cjO0Om4M7hCBMMbSZUjWIUjPxGex08wnbf4bENi2woyfw9l3n7rFdz01NeRiioSClmUS5XU4NVtC-axU3oY1JRl3KX3mYgB87o9ZWIjE1qp2npKGzpmNhqLOAme3J6vbKYOvZbdH55tVyIVIN7bv7sblthrsCHIZeN4JsiD2KycqB2HB_Dcl611T1KwTK8ylDxuHY7YrzeRNRTIS3Wtkg63iX9mT5PGvX3VhMODeMQ0PKhvVOZkJOPGRtuuMN_UtGQe8ScEiQ9csmzoa2LyfXPMpasLqT0hO87HGbs2OWyODwyTKYsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3755e8a6.mp4?token=gHJR17B-vy5lhmaL2TFMWjw9OpXjWLKNB87cjO0Om4M7hCBMMbSZUjWIUjPxGex08wnbf4bENi2woyfw9l3n7rFdz01NeRiioSClmUS5XU4NVtC-axU3oY1JRl3KX3mYgB87o9ZWIjE1qp2npKGzpmNhqLOAme3J6vbKYOvZbdH55tVyIVIN7bv7sblthrsCHIZeN4JsiD2KycqB2HB_Dcl611T1KwTK8ylDxuHY7YrzeRNRTIS3Wtkg63iX9mT5PGvX3VhMODeMQ0PKhvVOZkJOPGRtuuMN_UtGQe8ScEiQ9csmzoa2LyfXPMpasLqT0hO87HGbs2OWyODwyTKYsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : از این رفت و برگشت با ایران خسته نمیشی؟
🔴
ترامپ : من هیچوقت خسته نمیشم ولی اگه با چند روز صبر کردن بشه جلوی جنگ و کشته شدن مردم رو گرفت کار خوبیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/121405" target="_blank">📅 22:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121404">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
امروز اوایل روز، بحث داغی در داخل کاخ سفید درباره ایران شکل گرفت، جایی که جی‌دی ونس، استیو ویتکاف و جرد کوشنر برای توافق اولیه‌ای جهت پایان دادن به جنگ تلاش می‌کردند، در حالی که پیت هگست و مارکو روبیو برای فشار بیشتر و احتمال اقدام نظامی استدلال می‌کردند - گزارش آکسیوس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121404" target="_blank">📅 22:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121403">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056387d54e.mp4?token=AhiwQOeb4MHiZJJOHzldZZ_9wjxtz7fT7E-0i-9ZyWrK3cgAL-Ul0TBDYPvVjfJxdLe3G--09T93cOlsBvc-0-QM_Kn9iEuJv--ouIgwz54tq9XtJ9W67cSGkfLdbEcX8FKD8FlGBVlbzMmz9lL2zg7yET6CXFGUHnS915d9DRSleX7nadWGVBPV9OMgeJqkbE_Ay1m89siq7Z9t0vN_nxGSmWJboZHUt-SeWKdK3o7pbwYgPhlMfU88q5_Zh6E5QuNbMjLcdYlIyCtoJy9V0J-J5Uz9z8Nt6D_h_aqzxXFm7S--79pXWNp1viKy38RVuUyn57zOi-Gm2wofb-f8Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056387d54e.mp4?token=AhiwQOeb4MHiZJJOHzldZZ_9wjxtz7fT7E-0i-9ZyWrK3cgAL-Ul0TBDYPvVjfJxdLe3G--09T93cOlsBvc-0-QM_Kn9iEuJv--ouIgwz54tq9XtJ9W67cSGkfLdbEcX8FKD8FlGBVlbzMmz9lL2zg7yET6CXFGUHnS915d9DRSleX7nadWGVBPV9OMgeJqkbE_Ay1m89siq7Z9t0vN_nxGSmWJboZHUt-SeWKdK3o7pbwYgPhlMfU88q5_Zh6E5QuNbMjLcdYlIyCtoJy9V0J-J5Uz9z8Nt6D_h_aqzxXFm7S--79pXWNp1viKy38RVuUyn57zOi-Gm2wofb-f8Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در تماس خود با اردوغان ترکیه: من تماس بسیار خوبی با رئیس‌جمهور اردوغان داشتم. ما رابطه بسیار خوبی داریم.
🔴
آیا خوب نیست که من با برخی افراد بسیار سرسخت رابطه دارم؟ او فردی سرسخت است، اما من رابطه‌ای با او دارم که هیچ کس دیگر ندارد.
🔴
او در واقع کار خوبی انجام داده است. او، می‌دانید، من فکر می‌کنم که بسیار متحد بوده است. برخی افراد ممکن است در این شک داشته باشند، اما من فکر می‌کنم او یک متحد عالی بوده و مردمش به او احترام می‌گذارند. مردمش خیلی به او احترام می‌گذارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/121403" target="_blank">📅 22:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121402">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace87a5520.mp4?token=rBu2CD4br4gNcRXAWDcOjse5QpqIcyagchOYhhos0_7IMPLst2cn7wvrKq_7LQn1z_OqFrBDKbaF2GECCNOyRL6tH60puNg00GClj_Ez8sFq0I0oCdqLB4VWhPrNIuMsgsi_QhskWnDUtEmVjn9BdS2AHQds6zFBGeaXdW1LVCM348t0aoqDKsdkrky8T_aBjVevsNS3LRxXbxtZpwo2wCzfqIj52Sji20vU5M1PeQFIpo59piEE_Aoa9jslSSVkqnut1zXr6EMv_pYTy8fuirF_ObxDqDSaio2BC8k0Lh0kPZrgLqZq0NT9U7VKchA9DPZpR5aezZP4Ir8SPOK1yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace87a5520.mp4?token=rBu2CD4br4gNcRXAWDcOjse5QpqIcyagchOYhhos0_7IMPLst2cn7wvrKq_7LQn1z_OqFrBDKbaF2GECCNOyRL6tH60puNg00GClj_Ez8sFq0I0oCdqLB4VWhPrNIuMsgsi_QhskWnDUtEmVjn9BdS2AHQds6zFBGeaXdW1LVCM348t0aoqDKsdkrky8T_aBjVevsNS3LRxXbxtZpwo2wCzfqIj52Sji20vU5M1PeQFIpo59piEE_Aoa9jslSSVkqnut1zXr6EMv_pYTy8fuirF_ObxDqDSaio2BC8k0Lh0kPZrgLqZq0NT9U7VKchA9DPZpR5aezZP4Ir8SPOK1yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا آمریکا در جریان مذاکرات صلح، لغو تحریم‌های نفتی علیه ایران را پیشنهاد داده است، همانطور که رسانه‌های دولتی ایران گزارش داده‌اند؟
🔴
ترامپ: نه، من چنین چیزی نشنیده‌ام. تا زمانی که آنها توافقنامه‌ای امضا نکنند، هیچ لغویی انجام نمی‌دهم.
🔴
وقتی آنها توافقنامه را امضا کنند، می‌توانیم آنجا را دوباره بسازیم و چیزی داشته باشیم که واقعاً برای مردم کشور خوبی باشد.
🔴
اما نه، ما هیچ پیشنهادی نداده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121402" target="_blank">📅 22:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121401">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0858601f8.mp4?token=oJJgcQNMNa7uOg6TTP5HXzvATiIWwGOYTe-wczNRZDjjpYgpnjYTN8Y9BkBXhAFDnkm8FIvt7EUjL_BZa2bQjW4OjW38fs8izejvuchB9WKu_WZDsCgmXHnlhF5SszFffY1JHwXUi_LAu1zG1ChCb1Pke5EtNpaZBqgVRKbLjWjYCru4E2rxoiLRkmR94PLSbO6iMXAHhL7thN3oB-TgZeMs_DbKI-TWl_LPD-iPD72E5YkESBcW_h8DrgDwC7LAIgBBrvW8yQwagfJvRqFYOjZ2njNAg51FncCfHYx_8G6hcfM__PNb3MPX1AZXbfOhdo0fm0H--EFyH5hDmtxM4JG8zFTyXeQVK3o9ARFCPobpYHT0qXeJ6m2XWR20nAWVNdDM2RZZRB7uW_7spM4Hm5SNAB7IBukq4h0sWP3sT1tKUocDyFfgDem_SjDNnyfB3HaBqJ1nGJfiqPN4GU7yzxmwiJdsPeubTUZGRKaPFMJk64iMwfKxY0GwDdBvAk1n3DD94qUJX3-6aPxuYF_XZf5ADmDJOrasHN1OlTPDwq1scxoPey7fgOJY3v11LPsKlv5AZm3p9ufF_nO1cSUFF6i0-hGILhEEBy6E2FJ_tECngTPwZZG2D_o3jh38LnHbCmS5T6c_qbJfBj98pWfYBFqFOZCE0uK99jmqxcV5e30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0858601f8.mp4?token=oJJgcQNMNa7uOg6TTP5HXzvATiIWwGOYTe-wczNRZDjjpYgpnjYTN8Y9BkBXhAFDnkm8FIvt7EUjL_BZa2bQjW4OjW38fs8izejvuchB9WKu_WZDsCgmXHnlhF5SszFffY1JHwXUi_LAu1zG1ChCb1Pke5EtNpaZBqgVRKbLjWjYCru4E2rxoiLRkmR94PLSbO6iMXAHhL7thN3oB-TgZeMs_DbKI-TWl_LPD-iPD72E5YkESBcW_h8DrgDwC7LAIgBBrvW8yQwagfJvRqFYOjZ2njNAg51FncCfHYx_8G6hcfM__PNb3MPX1AZXbfOhdo0fm0H--EFyH5hDmtxM4JG8zFTyXeQVK3o9ARFCPobpYHT0qXeJ6m2XWR20nAWVNdDM2RZZRB7uW_7spM4Hm5SNAB7IBukq4h0sWP3sT1tKUocDyFfgDem_SjDNnyfB3HaBqJ1nGJfiqPN4GU7yzxmwiJdsPeubTUZGRKaPFMJk64iMwfKxY0GwDdBvAk1n3DD94qUJX3-6aPxuYF_XZf5ADmDJOrasHN1OlTPDwq1scxoPey7fgOJY3v11LPsKlv5AZm3p9ufF_nO1cSUFF6i0-hGILhEEBy6E2FJ_tECngTPwZZG2D_o3jh38LnHbCmS5T6c_qbJfBj98pWfYBFqFOZCE0uK99jmqxcV5e30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : کوبا یه کشور شکست خورده‌ست نفت ندارن ما اونجاییم که کمک کنیم داریم کوبا رو آزاد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121401" target="_blank">📅 22:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121400">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769642d28f.mp4?token=UHVNLCDRxZC1zEaHeNmzns6JkduC-G5HlxHASqI5oCBcveI_KkaDlPS7bPqpZHJXEe41utunxQD9DcPRsIk5vcuDicILqudqBPc7OO_EQi3j9HNKEs2k1E8eUVn5mlIiSfyJZagKTyCwFuY2QpNt3Ui3tsSW_dJmgmkosxlAZBrGwsZSPr5_29iEwAionMELuC3fX790rnK84TC7LEQK31_GTz8jyhbgJBPa34bGXWOrrH1VCGMMsTJg4oP6U-y9tck5-0cLclhAkyvfBsDDqAoZusZrWfSkhI2RVhHEO0-slhnnB2emw9R8hj4ovnswzv4jPVNg1Vu1_NYeCCODsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769642d28f.mp4?token=UHVNLCDRxZC1zEaHeNmzns6JkduC-G5HlxHASqI5oCBcveI_KkaDlPS7bPqpZHJXEe41utunxQD9DcPRsIk5vcuDicILqudqBPc7OO_EQi3j9HNKEs2k1E8eUVn5mlIiSfyJZagKTyCwFuY2QpNt3Ui3tsSW_dJmgmkosxlAZBrGwsZSPr5_29iEwAionMELuC3fX790rnK84TC7LEQK31_GTz8jyhbgJBPa34bGXWOrrH1VCGMMsTJg4oP6U-y9tck5-0cLclhAkyvfBsDDqAoZusZrWfSkhI2RVhHEO0-slhnnB2emw9R8hj4ovnswzv4jPVNg1Vu1_NYeCCODsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : پیامت به خانواده‌های آمریکایی که از هوش مصنوعی می‌ترسن چیه اونا نگرانن بچه‌هاشون تو آینده کار نداشته باشن
🔴
ترامپ : هوش مصنوعی فوق‌العاده‌ست ایران نباید سلاح هسته‌ای داشته باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121400" target="_blank">📅 22:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121399">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb46c8698f.mp4?token=AHThwfKQ_2K9QwGv3Uq-D9psGybO26LuZauDKizTorUpP-f-sqzLnuB-QxDLyeimaPurJombeh8roywGHIHRe5RlABwOHw8Cd4Sykuuw2BTQng_F0vtWM5frro4Y9tRcTHI3qw6vNOp7pQGO0cqh0CAcwc_kWCVlHEktsQxr0-q7U9zc0fPbsZ93mr_hWibc8V5arpklMlOcaQ9ZnaH0owHObDirNVJIK_x4qYDiou_RrqHSZd-2SUO9tl-kG-uBVgYYi6mSFx6zNBMziQZx8Obhvtc69vJtE6iL-znIsQ9mHhTjufoxdCoAFdgMVlKN0p-DoOQYE-XQlmTpFK0cbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb46c8698f.mp4?token=AHThwfKQ_2K9QwGv3Uq-D9psGybO26LuZauDKizTorUpP-f-sqzLnuB-QxDLyeimaPurJombeh8roywGHIHRe5RlABwOHw8Cd4Sykuuw2BTQng_F0vtWM5frro4Y9tRcTHI3qw6vNOp7pQGO0cqh0CAcwc_kWCVlHEktsQxr0-q7U9zc0fPbsZ93mr_hWibc8V5arpklMlOcaQ9ZnaH0owHObDirNVJIK_x4qYDiou_RrqHSZd-2SUO9tl-kG-uBVgYYi6mSFx6zNBMziQZx8Obhvtc69vJtE6iL-znIsQ9mHhTjufoxdCoAFdgMVlKN0p-DoOQYE-XQlmTpFK0cbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در واقع با برخی افراد بسیار خوب سر و کار داریم.
🔴
ما با افرادی که استعداد و هوش بالایی دارند، سر و کار داریم.
🔴
ما بسیار تحت تأثیر قرار گرفته‌ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121399" target="_blank">📅 22:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121398">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: اگر پاسخ‌های درست درباره ایران را نگیرم، سریعاً اقدام می‌کنم؛ من به پاسخ‌های کامل و صددرصد خوب از ایران نیاز دارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/121398" target="_blank">📅 22:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121397">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agAccQmS9ez1WPJg8TQwvA7lH9l1G2hV6U_uWMNd-ezBIDlqg--dbYz01gAgnOgAQWz-FCrlH8WVaEledf1-GhoDh_KwgInsSQZsgKol8SFJ4sOQXIBPNbn5pzpZTJUvbiJkzGhB8tJEPe9QVWJvyXm-7vFbEy5b4WZnuw6Sm5OkOlRjiqX5jv8uDpEvDhFrsGr3r0clvNsTdCHY7ETpU8B74rp9jueT7cLzF6SNpNgPC702kuMRsV9RfKAdBFUsbaPnWYumT1Urw8pJAsjbfDHwTFrI7q2FtITejTtdy4Wpq2ZXaBDJt46Sd57xcfiXtXh8qJVLvFkS-vpyrfmYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پولیتیکو: جمهوری‌خواه‌های مجلس رای‌گیری درباره اختیارات جنگ با ایران رو امروز عقب انداختن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121397" target="_blank">📅 22:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121396">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
اکسیوس: منابع گفتند که قطر و پاکستان با مشارکت دیگر میانجی‌گران منطقه‌ای، یک یادداشت تفاهم اصلاح‌شده صلح را تهیه کرده‌اند تا شکاف‌های بین آمریکا و ایران را کاهش دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121396" target="_blank">📅 22:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121395">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyJbbPqlaGbtJwYT3Ycz6FhoE3Q8TZ7Un8tI_tq1VzExc4bnaREmjzWsIdddv6DkapsHVMfARDsSfT0-hkC57PfRrGrk_BuwSoB6PSdV4a166hy-nG_z9N2tUjoDsg4fymcjWh6zbGxsM7EgvMlV5RSLo6hXIF9R4ixjLP2AdEyfTNk1uczLUOe2AG8dwxEkLD_dpm3xbjwKhWipokC62tDCvHkB97IxgVYFHiOaJoRS3fZ1fEg2f-lo-xA9GenTZqquUHNdkqmdlzDsAVe5CgRtca4m9MkDxSezgz5vCc4TK7wDvKCdAliRVpaLNLsXNKQn6P5YqOSRvECFNndadA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مسعود پزشکیان: ایران همواره به تعهدات خود پایبند بوده و هر راهی را برای جلوگیری از جنگ بررسی کرده است؛ همه مسیرها از طرف ما باز است.
🔴
وادار کردن ایران به تسلیم از طریق اجبار چیزی جز توهم نیست.
🔴
احترام متقابل در دیپلماسی بسیار عاقلانه‌تر، ایمن‌تر و پایدارتر از جنگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121395" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121394">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
عاصم منیر فردا به تهران می‌رود احتمالا خبر مهمی در راه است
🔴
روزنامه ابزرور پاکستان: فیلد مارشال سید عاصم منیر، رئیس ستاد ارتش، به عنوان چهره‌ای کلیدی در روند دیپلماتیک ایران و آمریکا، فردا به ایران می‌رود. در طول این سفر احتمالی، انتظار می‌رود اعلامیه‌ای مبنی بر تأیید تکمیل پیش‌نویس نهایی توافق منتشر شود.
🔴
این سفر می‌تواند به عنوان یک نقطه عطف دیپلماتیک سطح بالا باشد، جایی که تکمیل نسخه نهایی توافق ممکن است رسماً اعلام شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121394" target="_blank">📅 22:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121393">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
امروز اوایل روز، بحث داغی در داخل کاخ سفید درباره ایران شکل گرفت، جایی که جی‌دی ونس، استیو ویتکاف و جرد کوشنر برای توافق اولیه‌ای جهت پایان دادن به جنگ تلاش می‌کردند، در حالی که پیت هگست و مارکو روبیو برای فشار بیشتر و احتمال اقدام نظامی استدلال می‌کردند - گزارش آکسیوس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121393" target="_blank">📅 22:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121392">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کلش ریپورت:  اردوغان در تماس تلفنی با ترامپ درباره روابط ترکیه و آمریکا و مسائل منطقه‌ای صحبت کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121392" target="_blank">📅 22:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121391">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری / تسنیم: آمریکایی‌ها متن جدیدی به ایران ارسال کرده‌اند/ایران در حال بررسی متن است و هنوز پاسخی داده نشده است.
🔴
میانجی پاکستانی در تهران به دنبال نزدیک کردن متون به یکدیگر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121391" target="_blank">📅 21:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121390">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E4qust81IvR-j5QI72yvWNGEESO1DOTp0ZFTlHu2tn2yYEhn1MR9YMRwN42RN09wN7_ByEU5UIMDR7i4fQke6_WBKkno8w0EI9MepVJDJiamwsxuPLzBITgdUqMUK5H5mNme7yCvz15QVRo2dWN5S8dj_PDOK-KxQspBHr93d3S0DOq9GKvYZUBC7BeNw5ksqpK_XKNISmbVadjuijQrwKFzuww_RqfpN0SNKrTbdbWv9qwaSa_v9lusN4Whd6ckRY0w1uED0zEeoBu6ANoy9LgbQvTo5qHKTVPKlPZPe-r-HCMyAsG3NpfrdUStw4-EnMDCzf-WqXh6Mb6tyH1QTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش پولیتیکو اتحادیه اروپا برای مقابله با کمبود قریب‌الوقوع کودهای شیمیایی که به دلیل اختلال جنگ در حمل‌ونقل هرمز به وجود آمده است، به کود حیوانی روی آورده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121390" target="_blank">📅 21:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121389">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر نیرو: معادل مصرف چند کشور کسری برق داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121389" target="_blank">📅 21:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121388">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
معاون رئیس کمیسیون اروپا، کایا کالاس:
ادعاهایی که می‌گویند کشورهای بالتیک اجازه می‌دهند اوکراین از فضای هوایی آن‌ها استفاده کند، کاملاً بی‌معنی است - و روسیه این را می‌داند.
🔴
تهدیدهای مسکو علیه کشورهای بالتیک نشانه قدرت نیست، بلکه نشانه ضعف است.
🔴
روسیه در میدان نبرد در اوکراین شکست می‌خورد و تلاش می‌کند ما را بترساند تا حمایت‌مان از اوکراین را کاهش دهیم.
🔴
پاسخ درست عکس این است: حمایت‌مان از اوکراین را افزایش دهیم و دفاع اروپا را حتی بیشتر تقویت کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/121388" target="_blank">📅 21:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121387">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
آکسیوس به نقل از یک منبع آمریکایی: ترامپ به نتانیاهو از یک دوره 30 روزه مذاکره درباره برنامه هسته‌ای ایران و تنگه هرمز اطلاع داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/121387" target="_blank">📅 21:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121386">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1M7pFDiWYesQbsUybhrfOfAaghJ7lR2mPqVeTT-RP7oPqyPl1s4R9ghxASSL9lqqgK1h7TLw7JWeOVEwrYLLQl3Z9V0YEYUsmJ-y3IxZhuFl-yjNKBahqzeaDFswS3OaVKfsduLBjk005xSMHxRxpu5o798Fav2ueAC8faSzdv_V3iqRKOUZ8T6H3boDFWgRk9NdotO7CLF3U5t8F_IKD8cKcAntC3FFXl9wH1yc2gzvKgis0m-N6qF-hM-zeN4EB0vF-rih6icJmy-RmdeYDY2PEhidLUSimvHanF_A9Dm541xmW5pm6DECov6KbeBQAlDKWxEIkbZMvNqEaadng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید آکسیوس: ترامپ و نتانیاهو تو یه تماس سخت یه تلاش جدید برای رسیدن به توافق با ایران رو بررسی کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/121386" target="_blank">📅 21:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121385">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c38dde7e.mp4?token=fSZT9Jf8ToAjLDJt3nhlp8x60PZEB2qREmWz1GQ9jBsd78XJCvrpOT9c42XiGRD50g3ThqO6TfEl1EwOfnctrzuKNVeA5Y7zpGfiqT8qx_6yaThU7LpSTGnAundCp6Pq0yOzF7Lr5fOrYoMIIy1nU6HHL7LnNKj3O2D28xMlVwIC-CMG1a5d2emkcyk4snQqIGkLL6YKDdRl1zweAWv0boOXqWj5qYIuZW6Wrchp4p_W9ftGyHBbX6O28vTxQ0UPXwy_NSvBrzGBpwMNfrWedCMbseJ5WPOf0mAC5SgmYOy2a6WfD7rIDT0KLH9Zj59pYdkT_GNMhj2MNd913zrsIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c38dde7e.mp4?token=fSZT9Jf8ToAjLDJt3nhlp8x60PZEB2qREmWz1GQ9jBsd78XJCvrpOT9c42XiGRD50g3ThqO6TfEl1EwOfnctrzuKNVeA5Y7zpGfiqT8qx_6yaThU7LpSTGnAundCp6Pq0yOzF7Lr5fOrYoMIIy1nU6HHL7LnNKj3O2D28xMlVwIC-CMG1a5d2emkcyk4snQqIGkLL6YKDdRl1zweAWv0boOXqWj5qYIuZW6Wrchp4p_W9ftGyHBbX6O28vTxQ0UPXwy_NSvBrzGBpwMNfrWedCMbseJ5WPOf0mAC5SgmYOy2a6WfD7rIDT0KLH9Zj59pYdkT_GNMhj2MNd913zrsIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار محسن رضا نقوی وزیر کشور پاکستان با پزشکیان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/121385" target="_blank">📅 21:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121384">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: در دولت قبلی یک کشور مرده بودیم اما اکنون بهترین کشور دنیا هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/121384" target="_blank">📅 21:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121383">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در این مرحله متمرکز هستیم بر خاتمه جنگ در همه جبهه‌ها، از جمله لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/121383" target="_blank">📅 21:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121382">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
طبق گزارش کانال ۱۵ اسرائیل به نقل از منابع، پیشرفت‌هایی در پیش‌نویس یادداشت تفاهم و اصول بین ایران و ایالات متحده وجود دارد، اگرچه شکاف‌هایی باقی مانده است.
🔴
در همین حال، اسرائیل هماهنگی نظامی با آمریکایی‌ها را در پیش‌بینی حمله احتمالی ترامپ حفظ می‌کند، به طوری که نتانیاهو مستقیماً با ترامپ صحبت می‌کند و گفت‌وگوها در سطح نظامی با سنتکام ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/121382" target="_blank">📅 21:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121381">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQjYH5vVTzBlyTSYUWeNLe03o81kfnZPYk15pmdKNNiUDSRTdL67_P1oC-aBkMJ4f5UtyNrWnwwl5Ow_C7fa96MZaZwoeX1P3g1xstWC9iD4QwtlG0OqPcxBXbRhHdeIKxK6hd6z2I5MfzYXyJmuPwtATvZE3VHKsazFPIHgrUfErKcVU7xZzInoD3Bn8hX5SWo3hxe46FqzQ36kuUGNZL3mtNGd_Bp3LJaR-882uncmqS1oQ9qMtrJSpjFSDiULJ5h3TJORY-gORsbOOUWNc8mIphvqgOevXzVa5bfaGGDt2REc-VxwjvcLdXjMxF3E5WNY_mhTj3qAgrkt2-TjKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش رئیس کمیسیون امنیت ملی در پاسخ به حرفای به ترامپ: ایران شگفتی‌های زیادی برای آمریکا دارد؛ برای هر سناریو آماده هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/121381" target="_blank">📅 20:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121380">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et2PRqFjZHB0AaVtRNHzccumAgEOb0TRwad0Iq_mHel0eAwVJzzB5jQHMCkNdQBMbRo4_ad1se_dXO2DYdGDJzxn934X2pRKKYRRKJGF3D9lpW9Ylyr3A30VqD32i4CrbWNyriEU6B5hMX5HTXwC_h0FX5JEMfPxSv0iFgYPLGXZSCGpc3PBIlDWjR-x-bc8Q1v2gZ96g84C_Y1Yt_VifXHv2ZVMV8U6wQt0knFqvSHfo-L1BFhKqCLl4f7G01tG0bkB834NIOpQkgXYIN8ojP8mzrb5p3LsBd4ZbQmBmYXzUjyvGPQT__O1rMq2EINv0UgLDhLn1fiMCShbL2kTnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور لیندزی گراهام: شنیده‌ام که فیلد مارشال پاکستان ممکن است به ایران سفر کند - چه چیزی ممکن است اشتباه پیش برود؟! شاید او وضعیت هواپیماهای نظامی ایران را که در پایگاه‌های هوایی پاکستان مستقر هستند، گزارش دهد؟
🔴
مانند بسیاری دیگر، من از نزدیک شاهد اتفاقات مربوط به تلاش دیگری برای دستیابی به توافق با رژیم ایران هستم. برای همه افراد درگیر آرزوی موفقیت واقعی دارم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121380" target="_blank">📅 20:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121379">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
یه مقام ارشد اسرائیلی : اطرافیان ترامپ دارن روش فشار میارن که به توافق برسه
🔴
نتانیاهو هم باهاش درباره این موضوع صحبت کرده، و از نظر ترامپ گزینه حمله وجود داره که فقط بحث زمانشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121379" target="_blank">📅 20:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121378">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سازمان رادیو و تلویزیون اسرائیل: نتانیاهو تلاش می‌کند تا ترامپ را به دادن چراغ سبز برای ازسرگیری حملات به ایران متقاعد سازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121378" target="_blank">📅 20:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121377">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
اکسیوس گزارش می‌دهد که رئیس جمهور ترامپ و نخست وزیر نتانیاهو دیشب تماس تلفنی پرتنشی داشتند و در مورد مسیر پیش رو در مورد ایران اختلاف نظر داشتند.
🔴
طبق گزارش‌ها، سفیر اسرائیل در واشنگتن به اعضای کنگره گفته است که نتانیاهو از مکالمه مربوطه خارج شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121377" target="_blank">📅 20:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121376">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده :
اوایل امروز در خلیج عمان، تفنگداران دریایی ایالات متحده از واحد ۳۱ اعزامی دریایی، نفتکش M/T Celestial Sea با پرچم ایران را که مظنون به تلاش برای نقض تحریم‌های ایالات متحده با حرکت به سمت یک بندر ایرانی بود، توقیف کردند.
🔴
نیروهای آمریکایی پس از بازرسی کشتی و دستور تغییر مسیر به خدمه، آن را آزاد کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121376" target="_blank">📅 20:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121375">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: اگر روند [مذاکرات] بر اساس مطالبات به‌حق ایران پیش برود، می‌توانیم بگوییم که دیپلماسی توفیق داشته است.
🔴
در غیر این صورت، اگر طرف مقابل کماکان اصرار کند بر زیاده‌خواهی و خواسته‌های نامشروعش، قاعدتاً توفیقی نخواهیم داشت
🔴
همان‌طور که مقام‌های مختلف کشور نیز اعلام کرده‌اند، از جمله رئیس محترم هیئت مذاکره‌کننده، دکتر قالیباف، ما برای هر سناریویی باید همواره آماده باشیم؛ در عین اینکه دیپلماسی هم، به‌عنوان ادامه مبارزه مردم ایران برای احقاق حقوق و منافع ملی‌شان، باید حداکثر استفاده را از آن ببریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121375" target="_blank">📅 20:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121374">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
واکنش سخنگوی وزارت خارجه به تهدیدات اخیر ترامپ: اولتیماتوم‌ها در برابر ایران مضحک است
✅
@AloNwws
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121374" target="_blank">📅 20:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: درحال بررسی نقطه نظرات تیم آمریکایی هستیم و حضور تیم پاکستانی برای تسهیل این پیام هاست
🔴
استفاده از ادبیات «اولتیماتوم و ضرب‌الاجل» علیه جمهوری اسلامی ایران مضحک است و چنین فشارهایی هرگز کارگر نخواهد بود.
🔴
ایران فارغ از رفتارهای تهدیدآمیز و انواع فشارهای سیاسی و نظامی، مسیر خود را برای تأمین منافع ملی و احقاق حقوق حقه خود با جدیت پیش می‌برد.
🔴
تمرکز اصلی تهران صرفاً بر اهداف و منافع ملی است و این‌گونه لفاظی‌های تهدیدآمیز تأثیری در تصمیم‌گیری‌ها و سیاست‌های کلان کشور ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121373" target="_blank">📅 20:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121372">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: مقامات اسرائیلی معتقدند تقریباً هیچ شکافی بین اسرائیل و آمریکا در مورد خواسته‌های مطرح شده به ایران در مذاکرات جاری باقی نمانده است، اگرچه شک و تردیدهای عمده‌ای درباره اینکه آیا تهران واقعاً می‌تواند تحت فشار قرار گیرد تا آن‌ها را بپذیرد، وجود دارد.
🔴
ایران همچنان فقط به بخش‌هایی از پیشنهادات پاسخ می‌دهد و در مورد خواسته‌های باقی‌مانده تأخیر می‌کند، و اسرائیل مذاکرات را تلاشی از سوی تهران برای خرید زمان و کش دادن روند می‌داند. بازگشت احتمالی به اقدام نظامی به طور جدی در پس‌زمینه در نظر گرفته شده است و گفته می‌شود آماده‌سازی‌ها نیز در حال انجام است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121372" target="_blank">📅 20:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6cb439e9d.mp4?token=ninHUS6OFYu4mt5p4s6hlapMy_7yzjJ1OGIa7P7jv6Qz7Tx4IDeNMpR5QMKEuC6VjzIlN_vp0gKibDFnMdiZ9GF_6FyECFyMn7lyI6vIFhX2CDFWHk-ncl7_4auC8oswRY1-quTfnYiGXWgRdyZ_W41evfp6KKLyZtVywf_AAVA3qB9K0cPFdp-zP1VxR_F0noH6WUisCLN-jFR3EHzEcebogEupUSghPGTYZSayclQs04ofR2mj0sb9jyuecCmLzZ4m-psiGkiRsXghD6y68h68aoC3XKNCfS-uhs8wb3ZWt6TBiUwIJLRqoNdevhnXo90iNYLS0xrEXHhh3tug-BkNzHoskJlQNFLzAlw5ozn7MR347_0WS26Se4_gG3gO3hpMxIOzx_Jr5MctYbE0rv2iq81bqSRnLL7Xh3CIJLcG-XAqhAnz1tjPfWm65yt0r0kkkJ1MLmiQWEHrhv2qe9Mv55XbBy7bSEVeETdq2OCEbjVVcMSUYhajSGiXMgVo6NpXkRg4IzSYrdLxrXFGCaiCo1LkRCxsPDe9qcRNPBLs0MF6DyYpETPig5nyomaILpNMTdXriOe0_YOiXi_chAuBvIHXP8IVnPabFWmNOlXAX3Y82oiG25Ye5SwfTTX83Cr1_iMXVXKGEj4_KKU39wmnQd1GRcRpSe4xV30aVXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6cb439e9d.mp4?token=ninHUS6OFYu4mt5p4s6hlapMy_7yzjJ1OGIa7P7jv6Qz7Tx4IDeNMpR5QMKEuC6VjzIlN_vp0gKibDFnMdiZ9GF_6FyECFyMn7lyI6vIFhX2CDFWHk-ncl7_4auC8oswRY1-quTfnYiGXWgRdyZ_W41evfp6KKLyZtVywf_AAVA3qB9K0cPFdp-zP1VxR_F0noH6WUisCLN-jFR3EHzEcebogEupUSghPGTYZSayclQs04ofR2mj0sb9jyuecCmLzZ4m-psiGkiRsXghD6y68h68aoC3XKNCfS-uhs8wb3ZWt6TBiUwIJLRqoNdevhnXo90iNYLS0xrEXHhh3tug-BkNzHoskJlQNFLzAlw5ozn7MR347_0WS26Se4_gG3gO3hpMxIOzx_Jr5MctYbE0rv2iq81bqSRnLL7Xh3CIJLcG-XAqhAnz1tjPfWm65yt0r0kkkJ1MLmiQWEHrhv2qe9Mv55XbBy7bSEVeETdq2OCEbjVVcMSUYhajSGiXMgVo6NpXkRg4IzSYrdLxrXFGCaiCo1LkRCxsPDe9qcRNPBLs0MF6DyYpETPig5nyomaILpNMTdXriOe0_YOiXi_chAuBvIHXP8IVnPabFWmNOlXAX3Y82oiG25Ye5SwfTTX83Cr1_iMXVXKGEj4_KKU39wmnQd1GRcRpSe4xV30aVXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
اوایل امروز در خلیج عمان، تفنگداران دریایی ایالات متحده از واحد تفنگداران دریایی ۳۱ام بر روی کشتی نفتکش تجاری پرچم‌دار ایران M/T Celestial Sea سوار شدند که مظنون به تلاش برای نقض محاصره ایالات متحده با عبور به سمت یک بندر ایرانی بود.
🔴
نیروهای آمریکایی پس از بازرسی و هدایت خدمه کشتی برای تغییر مسیر، کشتی را آزاد کردند.
🔴
نیروهای ایالات متحده به اجرای کامل محاصره ادامه می‌دهند و تاکنون ۹۱ کشتی تجاری را برای اطمینان از رعایت قوانین هدایت کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121371" target="_blank">📅 20:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121370">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان:
حضور وزیر کشور پاکستان برای تسهیل تبادل پیام‌ها و ارائه توضیحات تکمیلی جهت شفاف‌سازی متون ارسالی میان طرفین انجام می‌شود.
🔴
ایران با وجود سابقه منفی طرف مقابل در یک سال و نیم گذشته، با جدیت و حسن نیت مسیر مذاکره را دنبال می‌کند اما نسبت به عملکرد آمریکا «سوءظن شدید و منطقی» دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121370" target="_blank">📅 20:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121369">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEuGxHOKuGK6urovPxyRFH-17ShVwq4P7EjI4V6KUgr1dzU2Bl1xv57PdBsxf_sztjwnjPIOrfUmR-aKUR4825bOCJN6a8-h4Vb6nOnI7ElJY01agp8zoNVIvx9GXm05SlnWNVjvWpxq76KaPNsXhS0ubochfFGcT5nIPtAJJzudfSGHe51FIddOBZYpptuIwzsfTiyfqVufkmD3Pq_9PTmXuFcdD0kKeDgGmbJylBeyrjTnPWyQMVjw8s0YekFds0efMFt9cyGGOBNNTJCgbFHoBsk6ouiSa2aw25OsVEszfpIm-UTh9DDsQjnWBL5zGJi7t9T3p0RX_ulIvKgQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های تازه کلودفلر رادار نشان می‌دهد ترافیک اینترنت ایران طی ۲۴ ساعت گذشته افزایش محسوسی داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121369" target="_blank">📅 20:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121368">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تبادل پیام‌ها بین طرف ایرانی و آمریکایی براساس متن ۱۴بندی ایران ادامه دارد.
🔴
حضور وزیر کشور پاکستان برای تسهیل مبادلۀ پیام‌هاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121368" target="_blank">📅 20:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121367">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ادعای ای ۲۴ نیوز به نقل از بک منبع آگاه: پیشرفت‌هایی در گفتگو با ایرانی‌ها درباره «یادداشت تفاهم و اصول» که زیرساخت مذاکرات را می‌سازد، وجود دارد. اما اختلافات هنوز زیاد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121367" target="_blank">📅 20:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121365">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c28ce6a5.mp4?token=Nx1Y19YT2rchiC-yvWrhdBNaLH9Y4iWwP9t1Cg31LJjauDS_tHfRMKE7FlXDBIO4TINAflqWPxy_KVA83S1tPmtDO77GyjEwBXJpsZhGE0rpmGFq6Jt00lr7WnCSt9Qn_VAr1ft6s3rNWfsWC7zejqEQlvUryZlCn9aWlQvnuNa3xvkQfjGHXmp8CLPGoYZBZH5_c_psx_yEgFy0eR1oRp3DBzvtLWUWRUL3zCYAsMHQKxTGyG5Zv6qcpBPnpQv4SagFy3BqseqlbhMqcYthUPo0uNMb4sSBYQUJEVrEf3XIZdZuZOYwl6cvNKyfQmgPJv_te6OIQnKoXY3tCZ9pCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c28ce6a5.mp4?token=Nx1Y19YT2rchiC-yvWrhdBNaLH9Y4iWwP9t1Cg31LJjauDS_tHfRMKE7FlXDBIO4TINAflqWPxy_KVA83S1tPmtDO77GyjEwBXJpsZhGE0rpmGFq6Jt00lr7WnCSt9Qn_VAr1ft6s3rNWfsWC7zejqEQlvUryZlCn9aWlQvnuNa3xvkQfjGHXmp8CLPGoYZBZH5_c_psx_yEgFy0eR1oRp3DBzvtLWUWRUL3zCYAsMHQKxTGyG5Zv6qcpBPnpQv4SagFy3BqseqlbhMqcYthUPo0uNMb4sSBYQUJEVrEf3XIZdZuZOYwl6cvNKyfQmgPJv_te6OIQnKoXY3tCZ9pCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : جنگ های بیشتری در راهه مگر اینکه ایران عاقل بشه - گارد ساحلی سه تا کشتی ایرانی رو گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121365" target="_blank">📅 20:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e8faeb92d.mp4?token=ShyKbDmaHXx2t7QBQTY7_CJt7sXAnkL7rm-z5w7qFx0_9kj6fvJgq_cro0v-bF9m120lvOg_aW6ljwm1X89FX3710gfIbV64lgSPiOtuVJfEuCYbfdQP801kOhod8FriyxRO2YVAWD2LVfuonm1KkJ3KWFYFb-qe1kwKI1eynt88xFWrkOU-OQhCXcoY6mjqa2AWdIM4MWCueOkQpuIlEqwH9R8PHgTKfdrvXGmxxITLp0WBqwcVPedSGAL-R4Hprz0ThZSIZY5u2MLvKSBhnxzTSPdIXqYUllh7uAyxeE0Z3XLH6l4EEWSKkFyGGCaa0bQYJuCdbrdOrMcoT3-5qTTP9hYFmUpwDvivZhTUcuy-myzO9eUljwUyzUKoBNJgoGhdveXk2Yp3KRbt_nDEaXM3JPFE-bruqafJ6F6ZU980cSDnF_G7vYpAeTUn6k70meBPGTgiA7s-wadtxHOUTySehYP____BRQUIAelXW2OpbomxTW1SFiVjfjgiYQYT-OEw1eVD4q-f0wtm0PXJwq0hzlaJnZRpsRJCwBQBKilmpryN5ag4Uyun4X53KXoW-tzZcPlgxUXBIhpasVEwcySdcHQBHIeRH2bdUdZmrL5JKs8RL2VKl2jWYzB6ynRXchlrRGYwvoIepuz8qPtRk-7Kpkp_umwZmiPpabXKi10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e8faeb92d.mp4?token=ShyKbDmaHXx2t7QBQTY7_CJt7sXAnkL7rm-z5w7qFx0_9kj6fvJgq_cro0v-bF9m120lvOg_aW6ljwm1X89FX3710gfIbV64lgSPiOtuVJfEuCYbfdQP801kOhod8FriyxRO2YVAWD2LVfuonm1KkJ3KWFYFb-qe1kwKI1eynt88xFWrkOU-OQhCXcoY6mjqa2AWdIM4MWCueOkQpuIlEqwH9R8PHgTKfdrvXGmxxITLp0WBqwcVPedSGAL-R4Hprz0ThZSIZY5u2MLvKSBhnxzTSPdIXqYUllh7uAyxeE0Z3XLH6l4EEWSKkFyGGCaa0bQYJuCdbrdOrMcoT3-5qTTP9hYFmUpwDvivZhTUcuy-myzO9eUljwUyzUKoBNJgoGhdveXk2Yp3KRbt_nDEaXM3JPFE-bruqafJ6F6ZU980cSDnF_G7vYpAeTUn6k70meBPGTgiA7s-wadtxHOUTySehYP____BRQUIAelXW2OpbomxTW1SFiVjfjgiYQYT-OEw1eVD4q-f0wtm0PXJwq0hzlaJnZRpsRJCwBQBKilmpryN5ag4Uyun4X53KXoW-tzZcPlgxUXBIhpasVEwcySdcHQBHIeRH2bdUdZmrL5JKs8RL2VKl2jWYzB6ynRXchlrRGYwvoIepuz8qPtRk-7Kpkp_umwZmiPpabXKi10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هرگز تسلیم نشوید. هر اتفاقی بیفتد، مهم نیست کجا در زندگی هستید یا در چه وضعیتی قرار دارید، به پیش رفتن ادامه دهید.
🔴
همیشه به جلو حرکت کنید. هرگز از پیش رفتن دست نکشید.
🔴
به مبارزه ادامه دهید و بگذارید دشمن اول تسلیم شود. بگذارید آنها تسلیم شوند. اگر شما ادامه دهید، آنها تسلیم خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121364" target="_blank">📅 20:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121363">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634f6fb417.mp4?token=hLzR-1-LAZRIFQl1FU-9es5EgL7X2ViTOscDdbkc84dpF3krm558gFOcDGMWG_FHR9DRcUMhwr_MGR5r0WcQom_Om7CqSC8rjdr7cvJDE4NzJspmNrF6vv1WVv5bBbuxxdTYqd3PV4sEXSneQvOYzLRzVOQbjKroTLyfK7cUYwiiI79GSfqCLxn_ibch92Tep2FGE9BBOkqELnswH-NtxXq628_yq8HsM0Iu_zyqpGvoswIalVzQOsT8jwmq6_ywM6vk6ekHkF8fAwtbxFLsViUbJKMzMvEJnK4lDybWP3w4VQnPULz8zFpyv8hcUhSzziZ-SNNXc8mYNS6Pe4c8JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634f6fb417.mp4?token=hLzR-1-LAZRIFQl1FU-9es5EgL7X2ViTOscDdbkc84dpF3krm558gFOcDGMWG_FHR9DRcUMhwr_MGR5r0WcQom_Om7CqSC8rjdr7cvJDE4NzJspmNrF6vv1WVv5bBbuxxdTYqd3PV4sEXSneQvOYzLRzVOQbjKroTLyfK7cUYwiiI79GSfqCLxn_ibch92Tep2FGE9BBOkqELnswH-NtxXq628_yq8HsM0Iu_zyqpGvoswIalVzQOsT8jwmq6_ywM6vk6ekHkF8fAwtbxFLsViUbJKMzMvEJnK4lDybWP3w4VQnPULz8zFpyv8hcUhSzziZ-SNNXc8mYNS6Pe4c8JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ونزوئلا ۲۰ سال پیش کشور واقعاً بزرگی بود — اما مسیر اشتباهی را رفت.
🔴
این مسیری است که آن‌ها دوست دارند این کشور را به آن سمت ببرند — برخی دیوانه‌ها می‌خواهند این کشور را به سمت چپ بسیار شدید ببرند و آن را نابود کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121363" target="_blank">📅 20:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121362">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521ea7f530.mp4?token=nAVROhWi0N7To8CnPp6GI-fd1ZGOA-7h8gIqTSx3pUqNx_W27G9OkfJ0w121Npo8qR_r8BwaWSuXDJoXnjdMV2KNLEIK7L9KGLHwJUToJCfKt6Fc0kQ_rXjt8wDN-sfPn8Ef3Rnww-eLoAd3gI90hd8zEkwzH2V8_tlZW6xhMOGwK3_rkUpxlo7qeXk5ubSAoNKAKo6D1ixtHit6DkzEWxWH2qI7ruZjdoPXRiV1q-aYA2TcQfr0LIKxwVKdcqBhoQqgkoMKd_5Pm9pLwi-twFtKeSEh2KSiwOrdnDqzM2lrajW_jdJRmaKWUIkBLJRjmiJ2iiRmodiGsgTOMpxczg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521ea7f530.mp4?token=nAVROhWi0N7To8CnPp6GI-fd1ZGOA-7h8gIqTSx3pUqNx_W27G9OkfJ0w121Npo8qR_r8BwaWSuXDJoXnjdMV2KNLEIK7L9KGLHwJUToJCfKt6Fc0kQ_rXjt8wDN-sfPn8Ef3Rnww-eLoAd3gI90hd8zEkwzH2V8_tlZW6xhMOGwK3_rkUpxlo7qeXk5ubSAoNKAKo6D1ixtHit6DkzEWxWH2qI7ruZjdoPXRiV1q-aYA2TcQfr0LIKxwVKdcqBhoQqgkoMKd_5Pm9pLwi-twFtKeSEh2KSiwOrdnDqzM2lrajW_jdJRmaKWUIkBLJRjmiJ2iiRmodiGsgTOMpxczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما عملاً قاچاق مواد مخدر از طریق دریا را متوقف کرده‌ایم. و حالا بخش آسان‌تر، یعنی زمین. این هم به همان سرعت انجام خواهد شد.
🔴
قاچاق مواد مخدر ۶۱٪ کاهش یافته است، اما ما می‌خواهیم آن را تقریباً به صفر برسانیم چون این مواد خانواده‌ها، افراد و زندگی‌های زیادی را نابود کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121362" target="_blank">📅 20:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121361">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ed4a2ba7.mp4?token=aVIJFTmKT_h7q2ijUNuILkjCSmOW9ah2o5XluIvhOBZoyCbLwBuknGx54lhs0V2D77Pptly736LMLSXe5SbGlI75511MymgPXc0eKxzXWwxFvP0orvMp_nOgefs8qY4jrGA5H6o45VEMHjkvoX0N4LECwlW7e6_Gc5eOhmDPxCHR_vAmvqH3sK5daSLeDJQS0NWl3ffVqaTHAyAokch-XIMH08n43-0UdH6nKxd3XGBplBuObTY1uKWSdYe3jMjBBoUmnBp-ZPwAp5w0vT4ES05_OiEU64vuZGQAovN6EDtqXAeQnJg7qlROdnQ-l66wK7NQu2pysc51qHNKIM1wTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ed4a2ba7.mp4?token=aVIJFTmKT_h7q2ijUNuILkjCSmOW9ah2o5XluIvhOBZoyCbLwBuknGx54lhs0V2D77Pptly736LMLSXe5SbGlI75511MymgPXc0eKxzXWwxFvP0orvMp_nOgefs8qY4jrGA5H6o45VEMHjkvoX0N4LECwlW7e6_Gc5eOhmDPxCHR_vAmvqH3sK5daSLeDJQS0NWl3ffVqaTHAyAokch-XIMH08n43-0UdH6nKxd3XGBplBuObTY1uKWSdYe3jMjBBoUmnBp-ZPwAp5w0vT4ES05_OiEU64vuZGQAovN6EDtqXAeQnJg7qlROdnQ-l66wK7NQu2pysc51qHNKIM1wTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ببینید الان من میگم آیران من اونجوری نمیگم چون تلفظ درستش مشخصه ما برمیگردیم به آیران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121361" target="_blank">📅 19:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121360">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ebe48c29.mp4?token=amKTme57mgrHmoAbeOJqoXQNsxMN5EG126KLdLx-6t3IDDVfeY6PnocnH2fS2hqMQH7sagnvJVediysk2rTKHGbj_oyZ8uEpd5JcIfpquKyX72sks3HJH05OC9rCTf5QIXYMcmswewzmhQshLroeVEKrETyr1Im2Cs2d23YL-BrYzBoFXvgUDqThBy-SJp1QOJPH-nPXUdPyXGOOzfkQOtjuN9G63F2Mx9ukLfeY-ViOFqaMMiyxkSscy-ZVib6R9AWWYhYIU-uXeutet2O1DpEQKKr4dQSNpWYDomUlIWPvuDzNmLvWzZvHwdJJbG34VFcTesq6rjTKEVQQZWHbzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ebe48c29.mp4?token=amKTme57mgrHmoAbeOJqoXQNsxMN5EG126KLdLx-6t3IDDVfeY6PnocnH2fS2hqMQH7sagnvJVediysk2rTKHGbj_oyZ8uEpd5JcIfpquKyX72sks3HJH05OC9rCTf5QIXYMcmswewzmhQshLroeVEKrETyr1Im2Cs2d23YL-BrYzBoFXvgUDqThBy-SJp1QOJPH-nPXUdPyXGOOzfkQOtjuN9G63F2Mx9ukLfeY-ViOFqaMMiyxkSscy-ZVib6R9AWWYhYIU-uXeutet2O1DpEQKKr4dQSNpWYDomUlIWPvuDzNmLvWzZvHwdJJbG34VFcTesq6rjTKEVQQZWHbzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما خیلی سخت بهشون ضربه زدیم شاید مجبور بشیم حتی سخت تر هم بزنیم ولی شاید هم نه!
🔴
سلطه آمریکا تو نیمکره غربی تحت هیچ شرایطی تهدید نخواهد شد ایران هم هرگز نباید سلاح هسته ای داشته باشه
🔴
ما اجازه نمیدیم ایران سلاح هسته ای بگیره و کل خاورمیانه و اسرائیل رو نابود کنه و بعد بیاد سراغ شما و این اتفاق نمی اوفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121360" target="_blank">📅 19:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121359">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db7d50a7db.mp4?token=kAfBW12u-cEi0CHesKE0ukpXdtI1S1CMjon7ZckfDGMGPdVbBR8NO3Uc7yC1FTuBGHxxJnTjUBK2fQZUySByUcl217kTERLZD_VHFwiLtGXcae_-GWIpK7Uz1SD5zjQxMcbHh-QhBeYoeb1vr5UjEcKJ47OACc54Twoy3oJxxO-OusJhkO_FvUhslCWOHuQLKO2xjz88qlsSGu7G7I5nHT452SHrcWWC0RHgc_ualHrc7vI7s4-dHugKP3-iwaE7p4RPsmrjnyxJLtjc55GiAhWERh13bkR8lw7cdn9x_knYypsDeqaSrja2tpX7ZThwhFV1TDcdP5L86CyAZWZrgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db7d50a7db.mp4?token=kAfBW12u-cEi0CHesKE0ukpXdtI1S1CMjon7ZckfDGMGPdVbBR8NO3Uc7yC1FTuBGHxxJnTjUBK2fQZUySByUcl217kTERLZD_VHFwiLtGXcae_-GWIpK7Uz1SD5zjQxMcbHh-QhBeYoeb1vr5UjEcKJ47OACc54Twoy3oJxxO-OusJhkO_FvUhslCWOHuQLKO2xjz88qlsSGu7G7I5nHT452SHrcWWC0RHgc_ualHrc7vI7s4-dHugKP3-iwaE7p4RPsmrjnyxJLtjc55GiAhWERh13bkR8lw7cdn9x_knYypsDeqaSrja2tpX7ZThwhFV1TDcdP5L86CyAZWZrgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : صنعت تراشه ما توسط تایوان برداشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121359" target="_blank">📅 19:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121357">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0da6120d.mp4?token=io8CgwUwA3ZVo71EObTAjn8BUkdIal4sGJLc2NVYtzH8JGBn0qdj_t1-g8Uutd1_BTBm7jWEtSQm6O6AT1E0XzapPZxXy0HHrM8HKGTmtw-8U_XJI9wbVn3JTNG2qQo8wRiE1IK1NslDqnQmeSA3SA3R4wbYo8y06gp7vHxDeoTS3dpkC5EjKBzdwWfglvBdOEEgjMLZgQ1XCX9K5laLkcbfyzb6D5SvQp9fs0uEkrPGqbkQyUAm6nAOjou7j-1RxZxdhjNGmmHGr0hFykZXvX2Xxd2qDN4C_Xkkcvvh0cOlIqrkBrsSRL2Akg2D6FDXCc-tWFo0quo_E1eu4AHpyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0da6120d.mp4?token=io8CgwUwA3ZVo71EObTAjn8BUkdIal4sGJLc2NVYtzH8JGBn0qdj_t1-g8Uutd1_BTBm7jWEtSQm6O6AT1E0XzapPZxXy0HHrM8HKGTmtw-8U_XJI9wbVn3JTNG2qQo8wRiE1IK1NslDqnQmeSA3SA3R4wbYo8y06gp7vHxDeoTS3dpkC5EjKBzdwWfglvBdOEEgjMLZgQ1XCX9K5laLkcbfyzb6D5SvQp9fs0uEkrPGqbkQyUAm6nAOjou7j-1RxZxdhjNGmmHGr0hFykZXvX2Xxd2qDN4C_Xkkcvvh0cOlIqrkBrsSRL2Akg2D6FDXCc-tWFo0quo_E1eu4AHpyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ بعد از دست دادن با یکی از دانشجوهای نظامی:
🔴
از مردای خوشتیپ بدم میاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121357" target="_blank">📅 19:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121356">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0799862f1.mp4?token=BzOIaxh43D5c2VoRf4A9QM_CVyIesM2GXKrwgvGsvsCF03ydh7vnmCPFf4qqngvMKKFR7pxnFfR9TzTLeegYSq_ADdb0RZIFXfThUAkv3cFKE0h_y__maQZtsmuTqxWaLzAz8ssR7Z4LTw8spMOQnwYKYdUt2pz7cnT8h0IqFW9X3-squ72R26f5OnSs7ITOl2hvE62lmSqf4wY_HAIPeq3TCU-vG3pe-T7zjlwBbFIL_9B5FTDFE6ok3lTIOdwZPrIpJ65gW0dFxQ-W0-Y-KYtVCmWLkahH7ePI-JijMvZQaSVKnuE6krCeMdzsYg0GicjGcrgKjTj7Pbxa6RH7Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0799862f1.mp4?token=BzOIaxh43D5c2VoRf4A9QM_CVyIesM2GXKrwgvGsvsCF03ydh7vnmCPFf4qqngvMKKFR7pxnFfR9TzTLeegYSq_ADdb0RZIFXfThUAkv3cFKE0h_y__maQZtsmuTqxWaLzAz8ssR7Z4LTw8spMOQnwYKYdUt2pz7cnT8h0IqFW9X3-squ72R26f5OnSs7ITOl2hvE62lmSqf4wY_HAIPeq3TCU-vG3pe-T7zjlwBbFIL_9B5FTDFE6ok3lTIOdwZPrIpJ65gW0dFxQ-W0-Y-KYtVCmWLkahH7ePI-JijMvZQaSVKnuE6krCeMdzsYg0GicjGcrgKjTj7Pbxa6RH7Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : برای موفقیت هیچ وقت احساس گناه نکن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/121356" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121355">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
افراد مسلح در خودرویی به سمت یک خودروی پلیس در جاده‌ای در شهرستان سراوان در جنوب شرق ایران تیراندازی کردند که منجر به کشته شدن یک افسر پلیس شد، گزارش تسنیم.
🔴
عملیات امنیتی و انتظامی در منطقه در جریان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121355" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121354">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58dc1edc3b.mp4?token=E4MSV1-asszmvBsA6kMKaE-ogUqkW4Zs9QEIvBzSSikITCHRu5ymZ6Ypo4ZbnxaMEyxVL4mduYUP0vNd8EFdFF1TcZA-O0TzXjrMpuj33GlsAkyy2oYaTgDTWesVMp2GfO0Vd1bVSpjoidyV99dVu3OqCaJn4WDTb2kQT4UWqhZ5uJlui3PND71o4UtzYT1WaHEa4Vcb36PM6HnhdZlXAM5mzUyE0pXEW9CUBzuBGKW82W6367Z8COhlYABXd057Z-1k4Adl3ssERjyu7nyCJSrX7d-K9ouk-ka1m1fgpq_zzkWCY6e3MUMkJlsRecK41eDGcMvK7qXRlJhLPzG0UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58dc1edc3b.mp4?token=E4MSV1-asszmvBsA6kMKaE-ogUqkW4Zs9QEIvBzSSikITCHRu5ymZ6Ypo4ZbnxaMEyxVL4mduYUP0vNd8EFdFF1TcZA-O0TzXjrMpuj33GlsAkyy2oYaTgDTWesVMp2GfO0Vd1bVSpjoidyV99dVu3OqCaJn4WDTb2kQT4UWqhZ5uJlui3PND71o4UtzYT1WaHEa4Vcb36PM6HnhdZlXAM5mzUyE0pXEW9CUBzuBGKW82W6367Z8COhlYABXd057Z-1k4Adl3ssERjyu7nyCJSrX7d-K9ouk-ka1m1fgpq_zzkWCY6e3MUMkJlsRecK41eDGcMvK7qXRlJhLPzG0UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: همه چیز از بین رفته است.
🔴
تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سندی را امضا کنند؟ ببینیم چه پیش می‌آید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/121354" target="_blank">📅 19:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121353">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
معاون وزیر خارجه روسیه: مسکو آماده است برای مذاکرات بین ایران و آمریکا «دست یاری» دراز کند، اما قصد ندارد خدمات خود را تحمیل کند
🔴
سرگئی ریابکوف، معاون وزیر امور خارجه روسیه، می‌گوید مسکو در صورت لزوم آماده است برای مذاکرات بین ایران و آمریکا «دست یاری» دراز کند، اما قصد ندارد خدمات خود را تحمیل نماید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121353" target="_blank">📅 19:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121352">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بن‌گیور، وزیر امنیت ملی اسرائیل، از فعالان بازداشت‌شده در کاروان جهانی صمود غزه در بندر آشدود بازدید کرد.
🔴
به اسرائیل خوش آمدید، ما اینجا در کنترل هستیم. این همان چیزی است که باید باشد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121352" target="_blank">📅 19:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121351">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
الجزیره به نقل از منابع دیپلماتیک: تعداد کشورهای حامی پیش نویس قطعنامه تنگه هرمز در شورای امنیت به ۱۳۶ کشور رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121351" target="_blank">📅 19:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121350">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سفیر اسرائیل در واشنگتن: هر توافقی با ایران لزوماً باید بر پایۀ اصل عدم اعتماد باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121350" target="_blank">📅 19:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121349">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miqWJDyGJEXTLFE4wcw19pzLZGuMbJVbfIjU2UdGPiDR-NlXYCIWVH0DU5y_YXYrg1i5b-pzo3-5nqyKZ0tOL15IuA-eRQTX1163dWghQgCJR-g-_cOsxN3rX2Fx0uzRbIab1ZZCHdJI-foT5iQBusH_BpXNQ_iR1Z_hracuprvOr50w9g2MvsIvqBV6KTPJ2SLXXc90p4YY4dZuOSbWlf6M-o9uj4gjybpn-10FOYNPCWvpOvKbMASADGzmKyz68CZ-jnJDOyK6lMvJYUpMheEoZnzkR7Qz7UH86t1ddGwK6cmuW9O0uHbdSLEibIo_itbQ3dXPUlQB8RtGH77w6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور سابق کوبا، رائول کاسترو، طبق گزارش رویترز و به نقل از یک مقام ارشد دولت ترامپ، در ایالات متحده متهم شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121349" target="_blank">📅 19:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121348">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
لارنس نورمن خبرنگار وال استریت ژورنال، با اشاره به خبر العربیه: حس من این است که اتفاق مهمی در جریان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121348" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121347">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
فروش کانفیگ استارلینک و VIP با سرعت بالا و اتصال پایدار
💎
پلن‌های VIP
📍
1 گیگ — 200 هزار تومان
📍
3 گیگ — 600 هزار تومان
⭐️
پلن‌های Starlink
🔸
5 گیگ — 1.500 میلیون تومان
🔸
10 گیگ — 2.900 میلیون تومان
✅️
آی‌پی ثابت
✅️
پشتیبانی ۲۴ ساعته
✅️
کیفیت تضمینی…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121347" target="_blank">📅 19:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121346">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uts1tosu3cv01nQnOwA4jJGr6h7hpFdCb4flCb_DElN-cliHDEMoqoGBAI-LbOiSXEj80LTaVghVOds6N_hW8i65bptlh8nO3tFG5wDhfiosKu1Ve9nSTW9lFPUv4iI6oYgiJ8MQ0YdetqtHs-bgpQA_-eFZc4njRvrRVMFBZ9eBLudNqXGX5gr6KRuiZT13lllj7A4B-omTCDU7p2kS1ePEGe9Hijtp8AKsD_Ymqgq4G9eOWghdeBEf3tYpgtC6it--feKkHLvSZD2Jnnna7g8h31jvpWqb2HTfAg8lZXyyOnPbmj68V12AKXT8BvDt7qywxepzAynqVO7LXs5Nzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
فروش کانفیگ استارلینک و VIP با سرعت بالا و اتصال پایدار
💎
پلن‌های VIP
📍
1 گیگ — 200 هزار تومان
📍
3 گیگ — 600 هزار تومان
⭐️
پلن‌های Starlink
🔸
5 گیگ — 1.500 میلیون تومان
🔸
10 گیگ — 2.900 میلیون تومان
✅️
آی‌پی ثابت
✅️
پشتیبانی ۲۴ ساعته
✅️
کیفیت تضمینی
✅️
دارای ساب باقیمانده لحظه ای
✅️
متصل در تمامی دستگاه ها و اپراتور ها
🛫
خرید و پشتیبانی:
🏠
@expressuport
🤖
ربات خرید:
💻
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121346" target="_blank">📅 19:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121345">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ادعای سفیر اسرائیل در واشنگتن: هرگونه توافق احتمالی با ایران باید بر اساس اصل بی‌اعتمادی کامل و راستی‌آزمایی باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121345" target="_blank">📅 19:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121344">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ: شگفت‌آور است که جمهوری‌خواهان موقعیت بسیار مهم «پارلمانی» را در دست زنی به نام الیزابت مک‌دونو نگه داشته‌اند، کسی که مدت‌ها پیش توسط باراک حسین اوباما و دیوانه شرور شناخته‌شده به نام سناتور هری رید، که مجلس سنا را برای دموکرات‌ها با «مشت آهنین» اداره می‌کرد، منصوب شده بود. در طول سال‌ها، او برای جمهوری‌خواهان بی‌رحم بود، اما برای دموکرات‌ها این‌گونه نبود - پس چرا جایگزینش نکردند؟ افراد عادل زیادی وجود دارند که برای آن موقعیت حیاتی واجد شرایط هستند.
🔴
جمهوری‌خواهان بازی بسیار نرم‌تری نسبت به دموکرات‌ها انجام می‌دهند. این بزرگ‌ترین عیب در سیاست است. دموکرات‌ها تقلب می‌کنند، دروغ می‌گویند و می‌دزدند، به‌ویژه وقتی که موضوع آرا در انتخابات است، اما به هم وفادارند، در حالی که جمهوری‌خواهان اجازه می‌دهند الیزابت مک‌دونو در قدرت بماند و بی‌رحمی ما ادامه یابد. ما باید قانون نجات آمریکا را تصویب کنیم، و همین حالا - و همچنین باید تعلل را از بین ببریم، که همه چیز را به ما خواهد داد! اگر حداقل یکی از این دو قانون را سریع تصویب نکنیم، دیگر هرگز رئیس‌جمهور جمهوری‌خواهی نخواهید دید. دموکرات‌ها دو ایالت اضافی، پایتخت و پورتوریکو، و همه پیامدهای آن، از جمله
🔴
۴ عضو در مجلس سنا، چندین عضو کنگره، چندین رای انتخاباتی اضافی، و همچنین رویای خود را برای دادگاه عالی ایالات متحده با ۲۱ قاضی مورد علاقه‌شان به دست خواهند آورد.
🔴
دموکرات‌ها در اولین روزی که فرصت داشته باشند، تعلل را از بین خواهند برد.
🔴
جمهوری‌خواهان این کار را نمی‌کنند چون می‌گویند دموکرات‌ها هرگز این کار را نخواهند کرد، اما جمهوری‌خواهان اشتباه می‌کنند. هوشمند و سخت باشید، وگرنه خیلی زودتر از آنچه فکر می‌کنید همه‌تان دنبال کار خواهید گشت!
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121344" target="_blank">📅 18:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121343">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری / ترامپ: آمریکا در «مراحل نهایی» مذاکرات با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121343" target="_blank">📅 18:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121342">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUMqteHUIJhD_ZuCpumt8lSK6w9-eghy4x4kJftl177pCC0PWRXdQ-ZmAQwQYAuJZHARxfPQuA-umGen4jNhrMqOUutEFYsIgwCpwVfpT3dhYIDvEbR57yzViOHvOq7ObzbEDN3NFT4tqzS7iYQStwkxATDQYXV2ZyvQ-OId5SZWLDjXy99xuqlDdrO4oYwk_GzQFl2MPosuBRxcOgpcCIFPnw0Bp2KD0X8WJP8gefD9N1I9fSPpVk232qpOBpFGwByhsQvEP49SZxYxOSglJjrFHhP11DAP2fangJd4BDWVdhI1TaeN40nWCUBLJWdJdC1FRhYNQLc4MIsGc0RD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تحرکات سنگین نظامی آمریکا به سمت خاورمیانه همچنان ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/121342" target="_blank">📅 18:47 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
