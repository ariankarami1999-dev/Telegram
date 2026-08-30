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
<img src="https://cdn4.telesco.pe/file/aZ4WC0Qd41_uZPlFkFonY_ELRs-Y_U9phNYSuq540lw7Lif9W1Z1d-PYp0CaJloPua3dHUJYtPXUWXwglAYquHqVcwuZ6PO9CVAyRil0URHo3cvic4r47myzvvgW7Hq6fNICz65mhZlAJMaaeAUTgUqH0w8uVoItedvOBoWQXj5mzLEpresAAoDgXrcY7MxOOLuwD1iinXBQItHyBvIG1TPhJ9ZEhqPt42E7QiOqA8JFAj2CuUURnRFiltO73PcDR6-JHN0YzjOalZakghnDI6AVFtT-vqvZriziRjVjgiHHnusQVplTNDhAepBnMoENthBEW21iVVuROIyzJ_7iIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 963K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 12:13:41</div>
<hr>

<div class="tg-post" id="msg-144520">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/447286c66f.mp4?token=mMnTnPg01evb3n02LdyNy7PXvqI7wpP1If6KTS4DD0xfNr5wWmVL-rYz3pmTQSVgTb9OoojW7LkTMWe6MrLTlsC7LNSwqeJCG71Gn16m1SQNBPjwK4j1McZoOLVBoew_vQoFEEHZ_4SGhk2HPuby3kqnvLqTVyiFchUK2Mt9SBKGYqXn1sKlOxIv7Xbf-4OssTJN0x38I77p9GjHi8J4hl0HylKwCm9yO764X3HopqZM3d14Z5eDYvhqz1Ief2jen816qiMxoy9x1_MqFbA9kLInbcfu9RkYPpOKwkOiqR2YYLC3QJ-h8Fpxd7Li2rUf-tm4VVpULUVx-p5qFGPT1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/447286c66f.mp4?token=mMnTnPg01evb3n02LdyNy7PXvqI7wpP1If6KTS4DD0xfNr5wWmVL-rYz3pmTQSVgTb9OoojW7LkTMWe6MrLTlsC7LNSwqeJCG71Gn16m1SQNBPjwK4j1McZoOLVBoew_vQoFEEHZ_4SGhk2HPuby3kqnvLqTVyiFchUK2Mt9SBKGYqXn1sKlOxIv7Xbf-4OssTJN0x38I77p9GjHi8J4hl0HylKwCm9yO764X3HopqZM3d14Z5eDYvhqz1Ief2jen816qiMxoy9x1_MqFbA9kLInbcfu9RkYPpOKwkOiqR2YYLC3QJ-h8Fpxd7Li2rUf-tm4VVpULUVx-p5qFGPT1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از طوفان در مالاتیا ترکیه
🔴
تصاویر منتشرشده نشان می‌دهد که شدت باد به حدی بوده که تابلوها و اشیاء سنگین با سرعت بالا در میان آسمان به پرواز درآمده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/144520" target="_blank">📅 12:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144519">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prjkJowjSQV9L2ix77HaMNOuY6AY4Nb8S7ExpnNLpVaVF5gOuyo_oVTtvjc_AqDMppgsEWtE_qnFgvmgPu5IVeHEq7BQeVMXZvevG1DO7mQ3m3cckeZN0-xsdO7Psuoat3_Ftvv1lb2GnmyG2yNASkKnmbvDE79hCOuzAxjDPpB5D0lTyhmRgBo08gxWKpZEiR7ul4XYvLt8pGn6YVg5UAIHmbYv5HfHrTDKwvUDBN4IaqOuTMTeh0cqjUxIPu6f2X9hv2BOXLwEKkLeJhIp2h9uS-fA0SXkjRqWca5wpV7EE2q2oMM5oyV1xHupobS-SlcJo5sPkvWIUv8-X2abow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو اسکادران جنگنده F-16 به همراه تعدادی هواپیمای ترابری نظامی به خاورمیانه اعزام شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/144519" target="_blank">📅 12:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144518">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
مجری صدا و سیما: آمریکا و اسرائیل فقط دنبال این بودن بمب رو مردم غیرنظامی ما بریزن!
🔴
دوستان تایید میکنید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/144518" target="_blank">📅 11:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144517">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
عراقچی: ژاپنی‌ها آمریکا را بابت جنایاتش پاسخگو کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/144517" target="_blank">📅 11:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144516">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رئیس‌جمهور چین وارد پایتخت قرقیزستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/144516" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144515">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ثبت احوال: ۷ میلیون و ۵۰۰ هزار کارت ملی هوشمند به مردم بدهکار بوده‌ایم که این رقم به ۶ میلیون کاهش یافته
🔴
بسیار امید داریم که تا پایان پاییز امسال، این بدهکاری‌ها تمام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/144515" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144514">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=Jo1XMEwzd7rmd9-b2fjse2Ev1DY2FLts8yOKV-d5cTUEuDzishrBzWtwFgQ11rM_RUNpMyf8ECojfk_2Cq8hQ4wH-thYzda7L4uooQGSdG3ry2HZPscMSc7FohTLvhB_momx9APkpCZwjux98AwMnYF8WKPwhSWlQ7OZ3CNvtjN3Az15rFtldYDt1lDBVgmIJrWON_0IC4KImhXW6WJmH3S-q3k6LAq_CvASeqJTAOjrQedswb5VQZ5yZHWkWkZTYfIzQfcbO9sDFU21LFdAWVKBV273z_vfg2ysavHE27Ou6m6wsKXeAewNuQd4pc_9A6RHsVM3H98nqSXsrBVusg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=Jo1XMEwzd7rmd9-b2fjse2Ev1DY2FLts8yOKV-d5cTUEuDzishrBzWtwFgQ11rM_RUNpMyf8ECojfk_2Cq8hQ4wH-thYzda7L4uooQGSdG3ry2HZPscMSc7FohTLvhB_momx9APkpCZwjux98AwMnYF8WKPwhSWlQ7OZ3CNvtjN3Az15rFtldYDt1lDBVgmIJrWON_0IC4KImhXW6WJmH3S-q3k6LAq_CvASeqJTAOjrQedswb5VQZ5yZHWkWkZTYfIzQfcbO9sDFU21LFdAWVKBV273z_vfg2ysavHE27Ou6m6wsKXeAewNuQd4pc_9A6RHsVM3H98nqSXsrBVusg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدویی از روش جالب روشن کردن مشعل گاز فلر
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/144514" target="_blank">📅 11:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144513">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de36d36926.mp4?token=KwdBzI3XEvFNmCRfRflt5LJZQeXhRFbW1S23MOqHMmd_JyzPuhabBDH8cR0zCJqDvfV5fL2NRUtnW2KOsPWM8cSiZsXtZ5Oku7UtFW1Lw4PelfEupppNd8G2t8FwubPoa2ExRw961iJ1U-JQkbbLEFOqiA8jFaZO8cqO94-hucSdoi1OQ9FI2vqa2M_i8dbWru-LB0vn0hkINL7LYrDTdM1Un0_uVWDYk-sS3394ldcA1aLCuRhOWAOKK6pV4peAawEd3ynihdIN0JlBkoKjn13k3D8In6RjCec_nPesrV9sxtTEjHG23KN-lUtDyx9RxrTDT2yuiDhuesSEh_0fMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de36d36926.mp4?token=KwdBzI3XEvFNmCRfRflt5LJZQeXhRFbW1S23MOqHMmd_JyzPuhabBDH8cR0zCJqDvfV5fL2NRUtnW2KOsPWM8cSiZsXtZ5Oku7UtFW1Lw4PelfEupppNd8G2t8FwubPoa2ExRw961iJ1U-JQkbbLEFOqiA8jFaZO8cqO94-hucSdoi1OQ9FI2vqa2M_i8dbWru-LB0vn0hkINL7LYrDTdM1Un0_uVWDYk-sS3394ldcA1aLCuRhOWAOKK6pV4peAawEd3ynihdIN0JlBkoKjn13k3D8In6RjCec_nPesrV9sxtTEjHG23KN-lUtDyx9RxrTDT2yuiDhuesSEh_0fMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فوت ناگهانی، هنگام سخنرانی شبانه!
🔴
نعمت‌ الهامی از چهره‌های شناخته شده منطقه مغان و کاندیدای دوازدهمین دوره انتخابات مجلس شورای اسلامی از حوزه انتخابیه پارس‌آباد حین سخنرانی شبانه فوت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/144513" target="_blank">📅 11:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144512">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d179adfd44.mp4?token=pAuWrQ1GItJzm-tDL9dcD9a_7vXlQCBxq5Bz305KmeWTo9e3AmUbnafESII9oeCkJTRmpI9ZUlpnl7Ji5Mt5wLI92VIoNW63vxdgyqGTautfioHuHIcxFz888wqNqG4DWrG_iKCEuLZIFBa4M0oYizjq6YCBHhOGKO5A7Mz1Z-y83bSqzSilVIxZhpzdGxHGnIkl3tLknrKXuwlLWCKQrOdtjKKHOGHCjXa-CLwU-7gdO-zleE-39lplpJTTz0LqP53r5gYImzpJ41a9oEl2uFpbV6U10nJXRJDRk3i4M8Sf7zUEtMyqblIE7fUvNnm_Vb-taRVoR7usN5AmzPb6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d179adfd44.mp4?token=pAuWrQ1GItJzm-tDL9dcD9a_7vXlQCBxq5Bz305KmeWTo9e3AmUbnafESII9oeCkJTRmpI9ZUlpnl7Ji5Mt5wLI92VIoNW63vxdgyqGTautfioHuHIcxFz888wqNqG4DWrG_iKCEuLZIFBa4M0oYizjq6YCBHhOGKO5A7Mz1Z-y83bSqzSilVIxZhpzdGxHGnIkl3tLknrKXuwlLWCKQrOdtjKKHOGHCjXa-CLwU-7gdO-zleE-39lplpJTTz0LqP53r5gYImzpJ41a9oEl2uFpbV6U10nJXRJDRk3i4M8Sf7zUEtMyqblIE7fUvNnm_Vb-taRVoR7usN5AmzPb6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک والتز، سفیر ایالات متحده در سازمان ملل
:
دونالد ترامپ رئیس‌جمهور صلح است.
🔴
او دیپلماسی را در اولویت قرار می‌دهد و شما به یک مکان در جهان نیاز دارید که همه حداقل بتوانند آنجا بیایند و صحبت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/144512" target="_blank">📅 11:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf358072ce.mp4?token=SiKgUElhN9L-pTwVfIpofj2dByvHYk-5b1Ys6roPefXrjDSvub_whnK3DkJZyegPLSWtN2V96Yv1k3Agp0FA0iWxF2m3Fl6ph-YFzmKEumHCTT9VUhmzYe-qRdsezpBcIB1iAZ4xjMHeKdaLPtchn59k7rlx-PQE56LhQkP_0tPGlOICksl4qolm8yZrSgwUKMS91rvFFcWbtaxI6y0AUgCNO6cHIGn9WUYDQu-9ZG-16HwEij1GG8jc5CcwQulkAG-_g0g-ThKQDAqfwnxiA0XU0imzzIPERiBlsfwt_IhOxXFIjO_uPQ4mCQ3RZykKwgyeCvDzdcVg7b8MhZ9KBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf358072ce.mp4?token=SiKgUElhN9L-pTwVfIpofj2dByvHYk-5b1Ys6roPefXrjDSvub_whnK3DkJZyegPLSWtN2V96Yv1k3Agp0FA0iWxF2m3Fl6ph-YFzmKEumHCTT9VUhmzYe-qRdsezpBcIB1iAZ4xjMHeKdaLPtchn59k7rlx-PQE56LhQkP_0tPGlOICksl4qolm8yZrSgwUKMS91rvFFcWbtaxI6y0AUgCNO6cHIGn9WUYDQu-9ZG-16HwEij1GG8jc5CcwQulkAG-_g0g-ThKQDAqfwnxiA0XU0imzzIPERiBlsfwt_IhOxXFIjO_uPQ4mCQ3RZykKwgyeCvDzdcVg7b8MhZ9KBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک والتز، سفیر ایالات متحده در سازمان ملل متحد
:
شما یا با ما هستید یا علیه ما. نمی‌خواهید در کنار ایران بایستید.
🔴
رئیس‌جمهور ترامپ جهانی را در نظر دارد که در آن فرزندان ما توسط یک رژیم اسلامی نسل‌کشنده که سلاح‌های هسته‌ای دارد، ترسانده نمی‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/144511" target="_blank">📅 11:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144510">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b826c1015.mp4?token=piF0Su8dHOrtPRpu3KvA3pyK7JBrlfQ0r0mnY69tkRa0GbLHgLXzHZbq8n0au4yxsg4OT-u-md-D7bzU_NNzJ5D9j1rHTQ1Mb1oSR4zpso-NTXgq04N1_ejhbnmQji8MeKrnRophODkfHS7vbK0W3zJW9xbu39vD7IAtSY3LXVOQhXsG_6SrM5DTEWkEjnyrIjy5UURFYg2m7TXwuH9MW7QBEhFjoLsQli0IAkHczlVRP-Ade_iQxi-hLIB9_A8zgMwT9VD4mujwphPIr0CFx9efeEol3r-cgKmBxTPr7UDNENrjYoNNQGnn8j-mNRxPNzvnZdIgjCyM_eNzNlUqCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b826c1015.mp4?token=piF0Su8dHOrtPRpu3KvA3pyK7JBrlfQ0r0mnY69tkRa0GbLHgLXzHZbq8n0au4yxsg4OT-u-md-D7bzU_NNzJ5D9j1rHTQ1Mb1oSR4zpso-NTXgq04N1_ejhbnmQji8MeKrnRophODkfHS7vbK0W3zJW9xbu39vD7IAtSY3LXVOQhXsG_6SrM5DTEWkEjnyrIjy5UURFYg2m7TXwuH9MW7QBEhFjoLsQli0IAkHczlVRP-Ade_iQxi-hLIB9_A8zgMwT9VD4mujwphPIr0CFx9efeEol3r-cgKmBxTPr7UDNENrjYoNNQGnn8j-mNRxPNzvnZdIgjCyM_eNzNlUqCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیفون 17 پرو، رکورد سقوط آزاد رو شکست؛
🔴
این گوشی با استفاده از قاب محافظ RhinoShield AirX، از ارتفاع 30 کیلومتری رها شد و بدون هیچ‌گونه آسیبی سالم موند و تو کتاب رکوردهای گینس ثبت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/144510" target="_blank">📅 11:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144509">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3784a4f2c0.mp4?token=Eew-sdJHcvREpLBO0eUDGJJ5qhFg4q6nw0lN3vfDrEOQ7BP7NK4lDTs3dA6ohwehHUztrgRlBqgkC6s9m-cNtCXbFRQB0rCqXCyPZqPITSizogcBBHqlT9JZvgK6Bu4K95mnCUgjbqVwTxfsOX_5KtlsjR139S2yCLkoTqla2-OqJXPz1N0GSoEDF5jZ8mYuuSnb4_0bOCUhRExIsNCB4XHE2sVP2AK19-F2brQ4k6LADuV3N-BetVejbDE_VqyYAyJxVTZMjmtP-8v-1WFNMkKkP5VL9Bc7i2mwglF9KlpRNqc3WpME5KeRYWdQmU5R8WNH6TzbAvpQydxNBfd7Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3784a4f2c0.mp4?token=Eew-sdJHcvREpLBO0eUDGJJ5qhFg4q6nw0lN3vfDrEOQ7BP7NK4lDTs3dA6ohwehHUztrgRlBqgkC6s9m-cNtCXbFRQB0rCqXCyPZqPITSizogcBBHqlT9JZvgK6Bu4K95mnCUgjbqVwTxfsOX_5KtlsjR139S2yCLkoTqla2-OqJXPz1N0GSoEDF5jZ8mYuuSnb4_0bOCUhRExIsNCB4XHE2sVP2AK19-F2brQ4k6LADuV3N-BetVejbDE_VqyYAyJxVTZMjmtP-8v-1WFNMkKkP5VL9Bc7i2mwglF9KlpRNqc3WpME5KeRYWdQmU5R8WNH6TzbAvpQydxNBfd7Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیلی به ارتفاعات الدبشه در جنوب لبنان هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/144509" target="_blank">📅 10:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144508">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
جنگ هوش مصنوعی به مرحله تازه رسید؛ OpenAI مقابل ایلان ماسک
🔴
شرکت OpenAI اعلام کرده قصد دارد ارائه مدل‌های هوش مصنوعی خود به Cursor را متوقف کند؛ شرکتی که اکنون تحت مالکیت SpaceX قرار دارد.
🔴
رویترز این تصمیم را تازه‌ترین مرحله از اختلاف فزاینده میان سم آلتمن و ایلان ماسک دانسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/144508" target="_blank">📅 10:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144507">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
اکسیوس به نقل از منابع مطلع:
رئیس سازمان سیا در جریان سفر محرمانه خود به روسیه، پیشنهاد برگزاری یک نشست سه جانبه میان ترامپ، پوتین و زلنسکی را با هدف پایان دادن به جنگ اوکراین، مطرح کرده
🔴
مقام‌های اوکراینی می‌گویند «پوتین در حال برنامه‌ریزی برای تشدید عمده جنگ است»؛ این موضوع مانعی بر سر راه تلاش‌های دیپلماتیک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/144507" target="_blank">📅 10:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144506">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از منابع غربی:روسیه، هواپیماهای بدون سرنشین اوکراینی را تصرف کرده است که ممکن است از آنها در عملیات تحریک‌آمیز علیه کشورهای عضو ناتو استفاده کند. این در حالی است که هشدارهایی درباره افزایش فعالیت‌های روسیه در اروپا وجود دارد که شامل نفوذ با استفاده از هواپیماهای بدون سرنشین، خرابکاری و حملات سایبری است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144506" target="_blank">📅 10:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144505">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c0f6ac56.mp4?token=dH5-AYHHspCc9pThjP4ZOzjVvQqhOVliQnW64M42CA2VpqW7ZvJzrjzj5g-3xxyHbOJPGyf3vMkHEE_mdw2_aJenHNHzBW9M_cd5A0yU4aDW-_plJFjn-ZW6b1MwyGKFTn52zvuUpLl9ch2r1E4iKOtNVNzOYuQzsC9ze2LcNI3xFYzAvLM7yLsHg88cVNMInrX7o8qx-ABQk7340NHCudAxxZyVonf2mFtmB_YzGcOizC3CZPtwKY95URWx80WmRi1KqJSD47z24jDKY2OOU5tA5MsG8nDRYvVZcolAyu3OqmF1PwNs0RJJ4UioEr5jedAA2ebAo4qYBW-JZQ2Kbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c0f6ac56.mp4?token=dH5-AYHHspCc9pThjP4ZOzjVvQqhOVliQnW64M42CA2VpqW7ZvJzrjzj5g-3xxyHbOJPGyf3vMkHEE_mdw2_aJenHNHzBW9M_cd5A0yU4aDW-_plJFjn-ZW6b1MwyGKFTn52zvuUpLl9ch2r1E4iKOtNVNzOYuQzsC9ze2LcNI3xFYzAvLM7yLsHg88cVNMInrX7o8qx-ABQk7340NHCudAxxZyVonf2mFtmB_YzGcOizC3CZPtwKY95URWx80WmRi1KqJSD47z24jDKY2OOU5tA5MsG8nDRYvVZcolAyu3OqmF1PwNs0RJJ4UioEr5jedAA2ebAo4qYBW-JZQ2Kbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد اوکراینی به یک هدف در منطقه برانسک روسیه حمله کرد و به نظر می‌رسد انفجار که در نتیجه این حمله رخ داد، ناشی از انفجار مهمات بوده است.
🔴
گفته شده یک سامانه اس ۳۰۰ روسی آنجا منفجر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144505" target="_blank">📅 10:22 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144504">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
دیلی بیست به نقل از منابع آگاه: ترامپ امید خود برای حل‌ درگیری با ایران را به جای وزیر جنگ، به وزیر خزانه‌داری سپرده
🔴
این تغییر رویکرد پس از آن رخ داد که ترامپ با عصبانیت هگست را درباره کاهش ذخایر مهمات ایالات متحده مورد بازخواست قرار داد
🔴
دولت آمریکا به این نتیجه رسیده که تهران با فشار نظامی، امتیاز نخواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/144504" target="_blank">📅 10:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144503">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزیر دفاع کره شمالی به عنوان بخشی از تغییر در رهبری نظامی این کشور، برکنار شد
🔴
رسانه های دولتی کره شمالی گزارش دادند که وزیر دفاع این کشور به عنوان بخشی از تغییر در رهبری نظامی پیونگ یانگ برکنار شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/144503" target="_blank">📅 10:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144502">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
بلومبرگ: تلوزیون دولتی روسیه نحوه نابود کردن بریتانیا با بمب اتم را بررسی کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/144502" target="_blank">📅 10:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144501">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febae98a7f.mp4?token=D_rTLnQVEjY78JgcikXEMNYARrrLD_ECW3_c2Azr2E89pX8LcEsIN45rg5ZkEt72qRMG9jlnY3OCm-QBOV9RZigD0CX28Q21meg5l_3b-TCnPSivUqNTUAAQWHF1GTiWjwKuTbwrYZNQT6uZE0SuAYXEx85kv1tfOGMyGE_oXUUlWi4CFDIZOrCoZHPOKBw0BMy7SGY_6Jv8PSi3pIDA4wMKevC5lfD40ATDOpCienjXWtNv0QWronVeDNSnXSHssXbxZDnnKCohfVuP5WvPJNHw1HN--T44rxFkAHWkzEA1CYR-vkiCH4IoLCPMMVsAWV6IenLjotbi1Yj2ycBHjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febae98a7f.mp4?token=D_rTLnQVEjY78JgcikXEMNYARrrLD_ECW3_c2Azr2E89pX8LcEsIN45rg5ZkEt72qRMG9jlnY3OCm-QBOV9RZigD0CX28Q21meg5l_3b-TCnPSivUqNTUAAQWHF1GTiWjwKuTbwrYZNQT6uZE0SuAYXEx85kv1tfOGMyGE_oXUUlWi4CFDIZOrCoZHPOKBw0BMy7SGY_6Jv8PSi3pIDA4wMKevC5lfD40ATDOpCienjXWtNv0QWronVeDNSnXSHssXbxZDnnKCohfVuP5WvPJNHw1HN--T44rxFkAHWkzEA1CYR-vkiCH4IoLCPMMVsAWV6IenLjotbi1Yj2ycBHjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ ویدیویی تولیدشده با هوش مصنوعی منتشر کرد که در آن تابلوی دریاچه انتاریو را با تابلوی «دریاچه آمریکا» جایگزین می‌کند و سپس به ریتم آهنگ «ای‌ام‌سی‌ای» (YMCA) می‌رقصد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/144501" target="_blank">📅 09:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144500">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سدهای خراسان رضوی فقط هفت درصد آب دارد
🔴
آب موجود در سدهای تأمین‌کننده آب مشهد شامل: دوستی، طرق، کارده و ارداک نیز فقط ۳۸ میلیون متر مکعب و معادل سه درصد حجم ذخیره آنهاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/144500" target="_blank">📅 09:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144499">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvzihKQfx0FtjsS_SXm0VHup29D6zDnUEWVohx-9leQV4e5KR7xASO-QSh7_u7TD2ZCxDKfskxqRJ6L9VOHGNT6yAGxEYJA7BiDO7FgzW7OQfzfh2TEVEGcAdsODtAW0EnspW6QNUOtBpUqU-YQ1vfZ8VmOB_4pHfzrVML4So_p7o0TAcNEExx1PNSgSD11Ydn0SFp8ceByRfEGrm55_18YPYR8ku2I5pIwhDOR-mADAiRxf3pR8yEZGFg4UfAlgLJRHEfx2xA1nNRwCDY_0sbau0VF1N_OEWsl0BAyuVsE6Dd-DdjQZ9BEW-Cr3x5anW4zKwUKFAf2OCA1LM4YYAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سال پیش جلوی واردات لوازم خونگی رو گرفتن که قیمت‌ها بیاد پایین
🔴
اما الان قیمت کارتن لباس‌شویی شده ۲.۵ میلیون!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/144499" target="_blank">📅 09:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144498">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLh5cVRwEroB3Ax3x6eV1ZKrQ3Yp1FkGO-oYnLDADUdljuLSCsk2pN7rsw_9wJTwOP-w-jfD8XEkQzVAUkYTgpBBB9f3zKGByWncWcwuXVlHLXRl8aI4xIkIe_NEmSQGIfZdHar3ABKlExyWKohisJ1UDa6-I10exAnys6PFYbAfntE49Mnq3DK7IfqASQJnJFM0my-iMNlw3KBSE0YkRyZ15UVSdOqAzVvI-xumz-gLFCttrHEK4LeEoAxeF7GF9-8iC46YN-ebE2cw3fiOsk9PnnX81ExzhXcKRtD6q5gchayGx1aZR1FVgHtwnYDtQRgJKtVIEYPQk85Hr96lrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مایک آدامز، نویسنده و فعال رسانه‌ای جنجالی آمریکایی در واکنش به صحبت‌های ترامپ در مورد نفت ونزوئلا: ایالات متحده تقریبا همین کار را با عراق هم انجام داد و تا به امروز، تمام درآمدهای نفتی عراق به بانکی در شهر نیویورک منتقل می‌شود. این همیشه یک عملیاتِ غارت و چپاول بوده که امپراتوری علیه کشورهای جهان به راه انداخته
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/144498" target="_blank">📅 09:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144497">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
شبکه اسرائیلی «کان» مدعی شد که عربستان تلاش کرد آمریکا را به اقدام نظامی علیه یمن متقاعد کند، اما واشنگتن درخواست ریاض را رد کرد.
🔴
طبق این گزارش‌ها، عربستان اصرار زیادی به همراهی آمریکا داشت اما واشنگتن «لحظه آخر» پشیمان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/144497" target="_blank">📅 09:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144496">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9394581bae.mp4?token=hQh9cOd9EJ65n17TBTaWadstqGe1uoIj8iu6mvrxhLptY2lG-kHiDieVrj3bHzJqED7h0eCXf3I0jingEVpL6e7v59vQGmfZ3uYsBxSPBR93kfeURrhKwlwWBbfnOS1pr5APmFT7OqZLs1DmBMwHpe0_NLkiEkIuaW2DpySodxHVJFgPvo_0ZbA_YphQjw_eXGUxuY9E29H5gOx3FNQXR_zrkhjfdtllDestFMNsjPwYaFGO0ZqALdGhOEBFXG2Qy6PdwumiAArFmEq_qCSQSUZBUxJFex9899dkIsI4o_neqbNIEphUijotz7nXyA6cRMmRfgfLFwVnHT0OFeJx_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9394581bae.mp4?token=hQh9cOd9EJ65n17TBTaWadstqGe1uoIj8iu6mvrxhLptY2lG-kHiDieVrj3bHzJqED7h0eCXf3I0jingEVpL6e7v59vQGmfZ3uYsBxSPBR93kfeURrhKwlwWBbfnOS1pr5APmFT7OqZLs1DmBMwHpe0_NLkiEkIuaW2DpySodxHVJFgPvo_0ZbA_YphQjw_eXGUxuY9E29H5gOx3FNQXR_zrkhjfdtllDestFMNsjPwYaFGO0ZqALdGhOEBFXG2Qy6PdwumiAArFmEq_qCSQSUZBUxJFex9899dkIsI4o_neqbNIEphUijotz7nXyA6cRMmRfgfLFwVnHT0OFeJx_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ورود سامانه بارشی به غرب و شمال غرب کشور و صدور هشدار نارنجی سازمان هواشناسی برای برخی نقاط
🔴
هوا در نیمه دوم هفته خنک می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/144496" target="_blank">📅 09:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144495">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
حمله اوکراین به پالایشگاه ۴۰۰ هزار بشکه‌ای روسیه
🔴
پهپادهای اوکراین، پالایشگاه ۴۰۰ هزار بشکه‌ای روسیه در کیریشی را منفجر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/144495" target="_blank">📅 09:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144494">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: سازمان امنیت داخلی اسرائیل می‌گوید پس از اینکه تهدیدی جدی علیه جان پسر نتانیاهو شناسایی شد، فوراً از آمریکا به اسرائیل بازگردانده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/144494" target="_blank">📅 09:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144493">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏
👈
۳ ساعت تاخیر تا الان در پرواز کاسپین تهران استانبول
‏
🔴
پرواز شماره ۷۹۰۲ هواپیمایی کاسپین که قرار بود ساعت ۶/۱۵ صبح به مقصد استانبول پرواز کند، به ساعت ۸/۵۰  دقیقه صبح موکول شده است، اما هنوز ساعت پرواز تایید نشده.
‏
🔴
هیچ مقام‌مسئولی در باره علت تاخیر پرواز، توضیحی ارئه نمی داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/alonews/144493" target="_blank">📅 08:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144492">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وال استریت ژورنال: فعالیت‌های تجاری و بانکی ایران در دبی، با وجود هشدار‌های آمریکا و اعلام پایان روابط، همچنان به طور علنی ادامه دارد
🔴
وال استریت ژورنال نوشت: اسکات بسنت، وزیر خزانه‌داری آمریکا، هنگام اعلام «روز دی اقتصادی» (Economic D-Day) به‌صراحت گفت که آمریکا دیگر در برابر کشورهایی که از فعالیت‌های اقتصادی ایران حمایت می‌کنند، چشم‌پوشی نخواهد کرد. اما یک گشت‌وگذار در دبی نشان می‌دهد که این فعالیت‌ها همچنان در برابر چشم همگان در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/144492" target="_blank">📅 08:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144491">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
عراق: تلاش می‌کنیم پلی برای ارتباط میان ایران و آمریکا باشیم تا به توافقی دست یابیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/alonews/144491" target="_blank">📅 08:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144490">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
یله نیوز گزارش داد: فنلاند به دور از توجه رسانه‌ها یک یادداشت تفاهم‌ محرمانه ۱۰ ساله با اسرائیل امضا کرده که شامل تحقیق، توسعه تجهیزات نظامی می‌شود و روابط نظامی دو کشور را گسترش می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/alonews/144490" target="_blank">📅 08:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144489">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏
👈
آکسیوس به نقل از یک منبع: مقامات اوکراینی گفتند که اطلاعاتی در اختیار دارند که نشان می‌دهد پوتین برای تشدید بزرگ جنگ برنامه‌ریزی می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/144489" target="_blank">📅 08:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144488">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
جروزالم پست: اسرائیل فردا توافق‌نامه‌ای را با یونان برای فروش یک سامانه پدافند هوایی جهت مقابله با تهدیدات احتمالی ترکیه و ایران امضا می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/144488" target="_blank">📅 08:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144487">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVmFvZjK6rzbbICp9CiinM8OlFKeKirGRNG-2Ei9QchgiES6CXE-8BM9E1BJPe33RtDDMPuYDO_sa7hDdLimzvzmJVEkl2aluRbqPAazwEhFgwaeFBcAgV0N-BvowiLq2m6QYpnvJOfXd9LMTsJk_sVMYMi3_bzad7KdSOgYOXXYVW_oHdARFqVsAqqxQGj2UYauDSkDNHboOHBZg2YnMbG2j3SrdiWbke-AqhD8JfbuDWq0Fhl0iMqTQI6nTT7-6Uw7QSzKtki2-7zRfCD5RA9VKpjaY2usEmqrzmkDROS8ui5pjsJgOk1OezATk5_0M09cVm6BImRDoNc3KWHBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش کان نیوز:
ولیعهد عربستان سعودی، محمد بن سلمان، از ایالات متحده خواست رهبری عملیات نظامی علیه حوثی‌های یمن را بر عهده بگیرد. این درخواست در جریان دیدار با ژنرال براد کوپر، فرمانده مرکز فرماندهی نیروهای مرکزی (سنتکام) مطرح شد. واشنگتن رهبری مستقیم این عملیات را با این استدلال رد کرد که حوثی‌ها کشتی‌های آمریکایی در دریای سرخ را هدف قرار نمی‌دهند، اما موافقت کرد تا از عملیات‌های عربستان علیه این گروه حمایت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/144487" target="_blank">📅 02:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144486">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSrm1hN4rTzGDk0IMF1MpkKv_Yc5gPBfjx_YinFOrRyQ1oUbcLYywksyyJRX39Rnsl75pvcTWpZpNoff1D3xoP5t1tFDpKl4WgV01ccVdRd2sJNo6bK6tNHioosmaeEVAd1mrcIHzulgPtetUJb1bnwZofe8fmEEjqua_4QW6vVouPIFGQbWqnoeXg_Df55Tqr51vjDtRQd0K0jM41Ewv_cXhhcgDMvc5BhNfQD0Gj3ZfyI1i7rqXAkSxd5dr58V-W98_Eo3GTBpPIYpjDmDx8tJUnHCs0lBqNtfJJXrOcBvb8PQKpTcQ87twn88JJztbZT1SrTbvTXTpmxzLvp3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادای احترام جامعه پرورش اندام به جاویدنام مسعود ذات پرور در مسابقات کشوری اصفهان
🔴
مجتبی ملکی، رئیس فدراسیون کچل خایه مال هم این اقدام رو محکوم کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/144486" target="_blank">📅 02:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144485">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f066db6043.mp4?token=YecAIl82dTXAf7LBR_SNEJJVwDDGV_NoQyDD2RZA5c69pJTALedweWRco7fvHwjghJP_7iRmS_C6Z6g0UoCs07O_98b_WRt-4e6OIeOz6Af-gjcDsY7K2nLaw4WQm2Hp5IveB7vqOv7JcVkJ0YX9b4SHe3yK3nRNfwz2o5cOLWcY-io7VShwvUsdZr0T6isQalUWNKoXoFcgv1ofCiHFIoNh99YmrfaltmHx9p7q5c_9NEvLSbHn-aMbGHmznzQsnxS2s9Ffhii5XiACJXcc4qPpdN9Mj2HvetmTqgAsFxUdKgHFIL6pb6CyK1fd9pF9a3suiHiNTJwhuuc1Bwm7bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f066db6043.mp4?token=YecAIl82dTXAf7LBR_SNEJJVwDDGV_NoQyDD2RZA5c69pJTALedweWRco7fvHwjghJP_7iRmS_C6Z6g0UoCs07O_98b_WRt-4e6OIeOz6Af-gjcDsY7K2nLaw4WQm2Hp5IveB7vqOv7JcVkJ0YX9b4SHe3yK3nRNfwz2o5cOLWcY-io7VShwvUsdZr0T6isQalUWNKoXoFcgv1ofCiHFIoNh99YmrfaltmHx9p7q5c_9NEvLSbHn-aMbGHmznzQsnxS2s9Ffhii5XiACJXcc4qPpdN9Mj2HvetmTqgAsFxUdKgHFIL6pb6CyK1fd9pF9a3suiHiNTJwhuuc1Bwm7bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام جامعه پرورش اندام به جاویدنام مسعود ذات پرور در مسابقات کشوری اصفهان
🔴
مجتبی ملکی، رئیس فدراسیون کچل خایه مال هم این اقدام رو محکوم کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/144485" target="_blank">📅 02:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144484">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q3d8xihAQ_LClPHr1YClAap9OnErVkTWl9u8vo0eaM7HHDia4Gi-kjRpPgQGnVAOz7nhVXLI51Xbi4gkBcA5UvTDgK_zEDnHWRifi8OZhrasYG3f6w6sXIy2O4JB7wU_V2JuBDHMi_-njCaQBR2oKh_9OppAv9NCyVia_c1SpZ7PE_5cok4AnSPhBqZ9fTzJgb0yPy3ZRkyyu1RLAxP3V855F8lI0M3RQC2I-CrhW_eFT-ipDwyMHxDV02Rg_OPVvx6h7ytWid7Ba31RWovc2DsLODxLHAuk3k2Fx95iyC6c3ixBzg15QjC7cNXN0cWcIPZFvvoZjxCdQkdJLZYvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمد لواسانی، رئیس سابق کانون صرافان ایران هست که حدود ۴۰۰ میلیون دلار پول کشور را برد و پس نداد، که دیروز بازداشت شد
🔴
وی همواره بر حفظ شعائر انقلاب تاکید داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/144484" target="_blank">📅 02:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144483">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
طبق گزارشات تو چند روز اخیر، ماشین تعدادی از هموطنان به مشکلاتی مثل "خاموشیِ یهویی ، لرزش یا سوختن موتور ، ریپ زدن ، بد استارت خوردن ، دیر روشن شدن و..." خورده که بعضی‌ها بنزینِ بی‌کیفیت رو علت اصلی این مشکلات میدونن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/144483" target="_blank">📅 01:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144482">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KThovjbt_bVAemKSjSlDt8nwYiD3K-s4DNrLBgapeDm1_iqu4Ptf_I1nT6XqDk5J_MwyttdMGZ_3CJJVvCBbr3r6PPTXt5uG1cuob-Wlt82NvVKAdXarZ1DBN6ReSPnZN1J3nbpqqBLPz9jmAGvU_PT7IaAsx3k_CgCpLEt6ug34ikl8_xJwJIE8MxqDosUgU1ps-B5Kxt3ZAXnd9yXcZtgSp2VaVtDVH_l8vOJo1h9-Rj1hOff-i-XJaZfByJp29cvfR4PWUEutxEeb5E8CGOtHpP7kawiDisojVKdqJrUwrhfvq6ISCdW5ujifTaw4uvviZPM0nNl2Au1eP9YWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مالی، خبرنگار:
چند روز پیش تو یکی از بیمارستانای اهواز یه بیمار تو ICU به طرز مشکوکی فوت میکنه، خانواده بیمار از طریق پزشکی قانونی علت مرگ ناگهانی رو پیگیری میکنن که با بررسی های پزشکی قانونی معلوم میشه چند نفر از رزیدنت ها و کادر بیمارستان خودشون مریض رو کشتن، تا تخت بیمارستان رو برای ی نفر دیگه که پول بیشتری داده بود خالی کنن، الان اون کارکنان بازداشت شدن و وزیر بهداشت کمیته حقیقت یاب فرستاده...
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/144482" target="_blank">📅 01:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144480">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfNA8MekEBA3vMZNUaIDtLUURzZdUzRjvsvcIPsTfpHekbUfvgF1oyknzV2CR9NVst9rLgZ-G6AEvCng8E0ag7hyCOQItcZE52eEv1He0cSTZih55TKcpA-O55PNUuiR0PS3Z4gq8FWl1db88P4UzFIdvcQMowtpWoG3mVGzxKm2Nf1B0lqZWNMblsdHvMrOLDP9GLYHepuwDdUBGeZ-Xxja9AOFNFwC6mgdy-aFhmlyExeFJsNIgCsR1zzSD1LRe3U7wXStocCmL75BWe5oBWdcGkATSRYgRuE-IyBF6xSsZ0EnMcBgiihp6HewcP-a8MvvJvsa_hgFmNNKsMqX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5d94A8uivDZSBo8FY3LwIErNM0OcqsCxBwILoFL1xGT5KlCZ6NepQhQ3YPXKVNIuo4tL6Pfwmyo4jE3mrkw3Oy4vxpQp8aGuMZceLDVI6nvhhOu9BxGR0z12qU4kLdngmyPScmAaSFlYTa1ki3f3vm4GSmWBh5ey7TBhMf0gWJTFWauLwDnUaDgpYuL54uTGX0ZKU6qEvE-5_DtfpfPY7E1RG7s-r4ZJQkmGxuZtcZz0yV9C_vpDFMaoaD9fVXkpohscE65DVCxE9LDOpewzM4WFk5GURqdlanhyG-7X5zbwBMUizlMvExOFV2jBJCIHPwTLYcJdoqFsckRjKC4Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مجتبی ملکی، رئیس فدراسیون بدنسازی: مسعود ذات پرور یه اغتشاشگر بود و نباید ورزشکارها اونو تشویق یا عکسشو تو باشگاه بزارن!
🔴
جوابتون به این شخص کچل چاق چیه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/144480" target="_blank">📅 00:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144479">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بانک مرکزی امارات متحده عربی، بازرسی فوری از شعب بانک مصر در این کشور را اعلام کرد، این اقدام پس از آن صورت می‌گیرد که ایالات متحده تحریم‌های مرتبط با ایران را علیه فعالیت‌های این بانک در امارات متحده عربی اعمال کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144479" target="_blank">📅 00:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر علوم: خیلی از اساتیدِ اخراجی را که از کشور خارج شدند، نتوانستیم بازگردانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/144478" target="_blank">📅 00:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
موسسه گلدمن ساکس: روزانه 15میلیون نفت از تنگه هرمز خارج میشود و فقط نفت ایران صادر نمیشود
🔴
ایران با دست خود، خودش را محاصره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/144477" target="_blank">📅 23:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144476">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ddaa4078e.mp4?token=VA6CY99RDTfwNvA76COynA7Qzea-nL6whfRLSFA20C_YWsxl2JZ4xqyiIZ5APi1CHFUUCc8YZVv2_lDy4ekq3d3-LiTWpwkZIue9RsBwcJMyM5vQ6HHFyUwFGgW-A16yenz3D_Wu464zLwR1T4tb9g3MSg6Q-uTWKb_YG4qgLFZybN5xSp2zFuwopQDKTsGHcLuDafHMq2MsDBO4iw8Po9hTgK62Yu-u_dFGobu1UJBeQitgpWa-nIQk7GssHGUtJLJPLhyHOI80zv0CxNGpH_q8Keh-TGhDsSENGX8-rEElQfsETKzBL2y-KMomkyyvcQmaqROQN7CqXM0Nq9V8enqL6_tWj0VFAuLUnh_Ru-qqFsu1-TDq0XUTDA56mPGn-l7qVos0-MtHkrOEmxyofdGTIa0dYpWLrFJWcO2o02sN2Ui2SSr5fWnMtkF0ScgVpkpJ_5RT-1GCUtFWZdZzds7fyH62NJ_Yy3HUBhg8dBkzOjt8zDcqxblcHw9PUvJM8rZ09vuT4IazuH3Q84hGF3HOJOyRfpIWKdsA8ctER9e8206Hn3xdwKBbbeXGO2ALXETPSMnv68kEUHqi-JOV--e7I5LfFd7WRmmPnV4zPaOKvE5X9DAaqrX1Hk0vPxT6VR3BGuvcQGzsNkqS9iFspdULRm0Xcwr-PvEAn2NzhDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ddaa4078e.mp4?token=VA6CY99RDTfwNvA76COynA7Qzea-nL6whfRLSFA20C_YWsxl2JZ4xqyiIZ5APi1CHFUUCc8YZVv2_lDy4ekq3d3-LiTWpwkZIue9RsBwcJMyM5vQ6HHFyUwFGgW-A16yenz3D_Wu464zLwR1T4tb9g3MSg6Q-uTWKb_YG4qgLFZybN5xSp2zFuwopQDKTsGHcLuDafHMq2MsDBO4iw8Po9hTgK62Yu-u_dFGobu1UJBeQitgpWa-nIQk7GssHGUtJLJPLhyHOI80zv0CxNGpH_q8Keh-TGhDsSENGX8-rEElQfsETKzBL2y-KMomkyyvcQmaqROQN7CqXM0Nq9V8enqL6_tWj0VFAuLUnh_Ru-qqFsu1-TDq0XUTDA56mPGn-l7qVos0-MtHkrOEmxyofdGTIa0dYpWLrFJWcO2o02sN2Ui2SSr5fWnMtkF0ScgVpkpJ_5RT-1GCUtFWZdZzds7fyH62NJ_Yy3HUBhg8dBkzOjt8zDcqxblcHw9PUvJM8rZ09vuT4IazuH3Q84hGF3HOJOyRfpIWKdsA8ctER9e8206Hn3xdwKBbbeXGO2ALXETPSMnv68kEUHqi-JOV--e7I5LfFd7WRmmPnV4zPaOKvE5X9DAaqrX1Hk0vPxT6VR3BGuvcQGzsNkqS9iFspdULRm0Xcwr-PvEAn2NzhDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدر عبدالاتی، وزیر امور خارجه مصر:
ما شاهد بحران‌هایی در تمام جهات هستیم و در شرایط بسیار دشواری قرار داریم، به ویژه در مصر.
🔴
به طور خلاصه، ما در یک منطقه بسیار ناپایدار زندگی می‌کنیم و این وضعیت غیرقابل پیش‌بینی است، به خصوص پس از جنگ با ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/144476" target="_blank">📅 23:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006470b470.mp4?token=sdXTdAyp_o7VyLxrmSMhgCvA5nfJRAtKsKuCcQRf6XZsc_SMwlGQxWINgQ0hOSs88yD-SEKJ4XvQuiKlDKoKoA5dCS2r31MqN5mOHAZFPsT_sooDpzVoamXxE2SaNFW5pz5cKMIO3ty3-CqIzzRwdWO7gBQ7uG_kHNLUkIypdIDBbei3tDfkpXXyIL83s3gt0MBM92h_yXHYQ-18a1UjAxR6dzf1VXk2TK5kTGrdqWeqKR3WK-O1GaUbIiUvGtnipX50n3cSmb_hBSF93n2hUPC7LH6wOe-1E2GrdSyMoc-vT6l0pUZ6kKuN5CSkczeiNOHEv8AYG_XTZDq50_aD-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006470b470.mp4?token=sdXTdAyp_o7VyLxrmSMhgCvA5nfJRAtKsKuCcQRf6XZsc_SMwlGQxWINgQ0hOSs88yD-SEKJ4XvQuiKlDKoKoA5dCS2r31MqN5mOHAZFPsT_sooDpzVoamXxE2SaNFW5pz5cKMIO3ty3-CqIzzRwdWO7gBQ7uG_kHNLUkIypdIDBbei3tDfkpXXyIL83s3gt0MBM92h_yXHYQ-18a1UjAxR6dzf1VXk2TK5kTGrdqWeqKR3WK-O1GaUbIiUvGtnipX50n3cSmb_hBSF93n2hUPC7LH6wOe-1E2GrdSyMoc-vT6l0pUZ6kKuN5CSkczeiNOHEv8AYG_XTZDq50_aD-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی تجمعات شبانه در میدون ابن‌سینا خانی‌آباد، یه سامانه پدافندی رو گذاشتن وسط میدون
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/144475" target="_blank">📅 23:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
حوثی ها، مواضع عربستان در استان الضالع را با موشک و پهپاد هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/144474" target="_blank">📅 23:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144473">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP_PRVMN2TGNR-RUpAJP9EM2SKxC2HubGAsPVFQFB0mJIxjGwm67nDmQKBOPf5lttAKA5-1LvAYKPhQnps_DDRHfghq4-0EvSUbSsxnxWjJmEYKy5d_m2NAG0SC2ov6tVqb-7B3zmwBvzww-B9RSWjI4Mkv_VmxEBgx-WcmXlMXKCbytupB1I8JF9wt3DXOYae5b1P1Dh6MC9MqxXjsUPtGoR5md9hKk_Dvi7Ag51mRN4uRcvPGck3tnDo8w_AwzOmQVSXe1J34BkDTUxW7VPIm5OXg0egZzX4Jp2iqiwtxlXqGLypkFxN0SyR5hxbG-9FEGk6dwmjegYO_U4PBPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در یک کارگاه در بزرگراه آزادگان؛ یک کارگر جان باخت
🔴
در این حادثه یک کارگر 21 ساله جان خود را از دست داد و یک مرد 30 ساله نیز مصدوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/144473" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144472">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بلومبرگ: ترامپ باور دارد که قدرت غلبه خواهد کرد و با سرسختی او انتظار نمی‌رود جنگ پیش از انتخابات میان‌دوره‌ای در آبان پایان یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/144472" target="_blank">📅 23:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144471">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khIZ2Yhe-0hQmOiUNRzzrDMv2NlrOYS7AmCCe5CdKOTpbipDobCDK9Lh-mm6YCiPqvuUvWrXusIVGB8EYrONNHSG5CY-XIGsayF0hKgk1cAwAHPUPbkD6Q4Dzda-YN3UBMTMkOkkK7etqeSIbFerQdNFLz1FWLfThId8b9YeB3YiXiMyNHDoJPwZ9p2B33Prqmg40pjoZwB9y7c63vUYqhDyQOkloFjwp4MUOOngXEUL2la16HaIizVfJ5wYPkHm1KSisaxzMbsBwieb9uitE1WKBn1Z8ERzBUk55dx5bBNf0bV8SKnP0kmfFRRCVhO4shVDt5SGTO5Bx9RfFU13iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتیوپی خود را با امارات متحده عربی و گروه  RSF همسو کرده است
🔴
غرب اتیوپی در حال تبدیل شدن به یک قطب لجستیکی برای امارات متحده عربی است، زیرا آدیس آبابا به طور فزاینده‌ای خود را با گروه RSF در یک قمار خطرناک بر سر پویایی‌های در حال تغییر قدرت منطقه‌ای همسو می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/144471" target="_blank">📅 23:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144470">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
اطلاعات نظامی اوکراین اعلام کرد که پوتین به برنامه‌ریزان نظامی روسیه دستور داده است طرح‌هایی برای حمله زمینی به سمت کی‌یف آماده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/144470" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144469">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a636fbbb.mp4?token=izRUbO4EHM2sQGBtDOqh-NTtKa1ASWldRKLGm1hr-sdMLxivhpq6QgBiuThaX8dPsjODiLl36ZErNTaBmDXZUS-hfxkTdM8ob1Zn9WB3SWT4q5V0-__2IQEcYwdYqh06k1Cl7njDPauIrQDAVRPXtwVt6z4mNfegDeade6QMnyFaTJ_f5f8IO_ciucFNOGATaX8orj6ddil0jRbk2POIlS-Nk-9NGr0F8e6_gLn6iIlZmdGZJGHa2fuh9LPjMB2tAcJ4XQ3LegNEjFkSHY49J-LXhQaLYNm47Uz82ioS4fz9huKoF5mgd5KWkuYeiho89g_A0_-bSNzCOdL2HKHs3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a636fbbb.mp4?token=izRUbO4EHM2sQGBtDOqh-NTtKa1ASWldRKLGm1hr-sdMLxivhpq6QgBiuThaX8dPsjODiLl36ZErNTaBmDXZUS-hfxkTdM8ob1Zn9WB3SWT4q5V0-__2IQEcYwdYqh06k1Cl7njDPauIrQDAVRPXtwVt6z4mNfegDeade6QMnyFaTJ_f5f8IO_ciucFNOGATaX8orj6ddil0jRbk2POIlS-Nk-9NGr0F8e6_gLn6iIlZmdGZJGHa2fuh9LPjMB2tAcJ4XQ3LegNEjFkSHY49J-LXhQaLYNm47Uz82ioS4fz9huKoF5mgd5KWkuYeiho89g_A0_-bSNzCOdL2HKHs3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده مجلس: ادعای عدم فروش نفت، یک دروغ بزرگ است/ در بدترین شرایط روزانه ۳۵۰ تا ۴۰۰ هزار بشکه نفت فروختیم!
🔴
محسن زنگنه، عضو کمیسیون اقتصادی مجلس گفت: تحقق درآمدهای نفتی نسبت به سال قبل ۲۸ واحد درصد افزایش داشته است/دلیل این حرف ها در وسط یک جنگ شناختی و ترکیبی چند لایه چيست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/144469" target="_blank">📅 22:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144468">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
غریب‌آبادی: هیچ کشتی‌ای بدون هماهنگی با ایران نمی‌تواند از تنگهٔ هرمز عبور کند
🔴
تنگهٔ هرمز کاملا بسته است و اگر کشتی‌ای از تنگه عبور کند قطعا با هماهنگی و مجوز ایران است.
🔴
نیروهای مسلح ایران کاملا بر هرگونه تحرک در تنگهٔ هرمز اشراف دارند و به‌هیچ‌وجه ادعاهای آمریکایی‌ها در مورد عبور کشتی‌ها از تنگه درست نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/144468" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144467">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
مارک لوین : قطر یک رژیم سلطنتی و اسلام‌گرای شیطانی و نامشروع است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/144467" target="_blank">📅 22:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144466">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
غریب‌آبادی، معاون وزیر امورخارجه: تلاش قطر و پاکستان این بود که بررسی کنند آیا امکان بازگشت به اجرای تعهدات تفاهم اسلام‌آباد وجود دارد یا خیر.
🔴
ایران آمادگی خود را از طریق تفاهم با عمان درباره تنگه هرمز مشخص کرده، اما اجرای تعهدات بر عهده آمریکا است.
🔴
آمریکا تعهدات خود را متوقف کرده و برای بازگشت به مسیر، باید اقدامات لازم را انجام دهد؛ پس از آن مسیر مشخص خواهد بود.
🔴
ایران آماده حرکت در مسیر تقویت وحدت و همکاری با کشورهای اسلامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/144466" target="_blank">📅 22:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144465">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=XwhEnbwJP_v-IWYYyuXM5i7cHEE33m5E_UMTg_NV-7jnobwtJVdUxIrPoskRHDf-5-ux1rnA6GLeoTobm8PU9Y7XYscudfWVVCBIT_4e2wUqnYpnJYQhhW48DoDNVIWoJSJEE8hsu8Etl0RmwgF_T0ys4nA6fThE46yC9izQl5p7dzTuSAVL4P7gUnpcLgzlzmIYlk-OziDEHg2eBsbov1LBlUeJEQ-3ua5u788dAvjZNe0qPI7q0_mQOR26qq8Vd9KR8gnD9SHZkO6h9jBmbtescdeEiaGEGwskMtdwjDsR9Dpf-ER89lVCotsjDeY1OUg6ozNg9UpBgvpxF6Fppg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=XwhEnbwJP_v-IWYYyuXM5i7cHEE33m5E_UMTg_NV-7jnobwtJVdUxIrPoskRHDf-5-ux1rnA6GLeoTobm8PU9Y7XYscudfWVVCBIT_4e2wUqnYpnJYQhhW48DoDNVIWoJSJEE8hsu8Etl0RmwgF_T0ys4nA6fThE46yC9izQl5p7dzTuSAVL4P7gUnpcLgzlzmIYlk-OziDEHg2eBsbov1LBlUeJEQ-3ua5u788dAvjZNe0qPI7q0_mQOR26qq8Vd9KR8gnD9SHZkO6h9jBmbtescdeEiaGEGwskMtdwjDsR9Dpf-ER89lVCotsjDeY1OUg6ozNg9UpBgvpxF6Fppg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
مسئولین شهر مراغه سر چاه: با یاد رهبر شهید پروژه رو افتتاح میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/144465" target="_blank">📅 22:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144464">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
قیمت دلار به ۲۰۶,۰۱۰ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/144464" target="_blank">📅 22:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144463">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyZqDjXqxi59vykkkgyftZB5AU9HPV3x1NVTOsc20eaeoAzFtLCqHtuxt_MhIDuobMb8Nfsewh4VDOLTQ1AFovUj64xeJ6bg1eTIOH9rSd1KDL7bFfSQ7DI69LX5cJDQHxVggQN-3peDHnF2IEoSnnUYjQmii7xdjAKOeGx8ufip48T6Z9pyHsM9Seg7AEmYfPWM8Vb4jSO41WCUvKpC2_IUb7ARYxo3xKRgvYfKQoBKaEKAw9AxulLhYqpYWswqbA4PAFZ3NnMv-GIomow6GPr_3cfxx2RR5AbjQZRr8Uy4p5vtYx56jXnwdaVXvO0WVyXgE4WkKo-d778seNl89Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آنتونیو گوترش، دبیر کل سازمان ملل:
آزمایش‌های هسته‌ای اعتماد را از بین می‌برند، به رقابت تسلیحاتی هسته‌ای دامن می‌زنند و خیانت به جوامعی هستند که همچنان با پیامدهای آزمایش‌های هسته‌ای گذشته زندگی می‌کنند.
🔴
از همه کشورهای دارای سلاح هسته‌ای می‌خواهم تا به تعلیق‌های موجود در زمینه آزمایش‌های هسته‌ای پایبند بمانند و «معاهده منع آزمایش‌های هسته‌ای را لازم‌الاجرا کنند.»
🔴
بیایید بار دیگر بر تعهد خود برای پایان دادن به آزمایش‌های هسته‌ای تأکید کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/144463" target="_blank">📅 22:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144462">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07f1cca6d.mp4?token=gKTZwwJuCpvtj9aMqKMTNhtjMy5J6SIIE1qrbccCzg-d_qxy0XWcgp6hP6RJC6da1Nw6Kc8wGOadA_iFOvehSpjuk1QE2uecpnpCCrpw-ffbZzOtMt1EaUDz5wpx80FbWxdBx5E2pAZsPlhr929BddXGHLVKDW9Z1aDucvj9fLKPwFt4hPOMU4GxSU0MOOYTzP6LlYShtPnItMowHrNpKr54meouCt7djus47KyijNIAABYSsFWiisFQYfuaxsN-zf_OzC3vqq1SWZGbit7FmeGBoBxEw2Z5UdmFj2WeiWpxZJCJs7Vb5cV3YKuWMYWBSHBaOR4Jqe2LfRs_HgLrkK3C99F8F-Yp4_KkkWwlkC3SMdWWHUNUdCjhUGFE6jFnRh1wMCASF142-7YOcQWP-83VGx29J03wf_FewCsqgvaKwbyT2hpFlmKdkMXJLfI9xAa2modMvzrfFG99KwlWydqRnNKh540qtDmnZefxPPHlet1yTzncSR_-ScMrbI1evnMJpb0tMHxdbGwtUi9zyKd5JQsC3YEK_bYJWXEYpRkG-FH3627qgzf2M5RtPiUZYO0F3hB9FbDmJJTxJ0UnCJAV61qfUK_ZBYNbSLPsxHInOCn-FEs0tI9WEGMmVL96LNUoWO-RgWTgNv25bWYsQHLKpnj3J7TofYBA0MddjUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07f1cca6d.mp4?token=gKTZwwJuCpvtj9aMqKMTNhtjMy5J6SIIE1qrbccCzg-d_qxy0XWcgp6hP6RJC6da1Nw6Kc8wGOadA_iFOvehSpjuk1QE2uecpnpCCrpw-ffbZzOtMt1EaUDz5wpx80FbWxdBx5E2pAZsPlhr929BddXGHLVKDW9Z1aDucvj9fLKPwFt4hPOMU4GxSU0MOOYTzP6LlYShtPnItMowHrNpKr54meouCt7djus47KyijNIAABYSsFWiisFQYfuaxsN-zf_OzC3vqq1SWZGbit7FmeGBoBxEw2Z5UdmFj2WeiWpxZJCJs7Vb5cV3YKuWMYWBSHBaOR4Jqe2LfRs_HgLrkK3C99F8F-Yp4_KkkWwlkC3SMdWWHUNUdCjhUGFE6jFnRh1wMCASF142-7YOcQWP-83VGx29J03wf_FewCsqgvaKwbyT2hpFlmKdkMXJLfI9xAa2modMvzrfFG99KwlWydqRnNKh540qtDmnZefxPPHlet1yTzncSR_-ScMrbI1evnMJpb0tMHxdbGwtUi9zyKd5JQsC3YEK_bYJWXEYpRkG-FH3627qgzf2M5RtPiUZYO0F3hB9FbDmJJTxJ0UnCJAV61qfUK_ZBYNbSLPsxHInOCn-FEs0tI9WEGMmVL96LNUoWO-RgWTgNv25bWYsQHLKpnj3J7TofYBA0MddjUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کشوری به شدت منزوی شدیم
‼️
🔴
حتما ببینید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/144462" target="_blank">📅 22:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144461">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/144461" target="_blank">📅 22:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144460">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c661cdb96.mp4?token=KrPsPigFtZdotyDAdEjMJ7_k5aTQ4Q6et64G-IVovFNmB6Vy0vvGyYBrYTPiiWoGTQglNL3LydIGdEcQMn7OWp_RyJejfnftRw62qHhpKBWDH4gwA6LNrwP3SidFtU0YdEHHykApB2jGnYi42cL4Mx6x3RvvM-oAnvpLCEh5RQsmFlVhPeFScUzvFF-Mut6IWgWEyB4ENyrF-ZkYOtzl1Xi2uZlVIxaGdyzl5P_n355RLT1Dy-_DWvKGKiYvmzMwlxa0jBWErsXT3SV0cyqXs0l85fU-IhR5sHCUoN0xL-l_BmsP5lkbsWZEMe12TVWD0CvOvt4rlm3dsF1esX0GLIq3RMVzltXpXW8KYjMPbfd6ZaYEybR2Xjiwtu-9qIK9ZgIySxs5FUB7XQwtkyM9zqT3VK5ttlCsLk2IRkiM6sl_6fb1bx9rx4oiACIdjo2iv6___BPRVA09W5RfPL-hxBtqBnWynd3_ZhpTwkkQROyNEiiVGY4PpteL2oHzEHIa8a6ZvniyRt_KtDn-NDZK-QX79r_ePwcWjQu5pbTLWtNggZl5US-rI6uVMjbsIvq55rJX7sbygfLriuByWP3j22WGEom3xRWOblSr-nN55AjjdYYbPTf4totxyY5dWq-URooVwhmyMCOQeMqeFG4A1Q8iVOeUqnu_IEo_1TS6Btc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c661cdb96.mp4?token=KrPsPigFtZdotyDAdEjMJ7_k5aTQ4Q6et64G-IVovFNmB6Vy0vvGyYBrYTPiiWoGTQglNL3LydIGdEcQMn7OWp_RyJejfnftRw62qHhpKBWDH4gwA6LNrwP3SidFtU0YdEHHykApB2jGnYi42cL4Mx6x3RvvM-oAnvpLCEh5RQsmFlVhPeFScUzvFF-Mut6IWgWEyB4ENyrF-ZkYOtzl1Xi2uZlVIxaGdyzl5P_n355RLT1Dy-_DWvKGKiYvmzMwlxa0jBWErsXT3SV0cyqXs0l85fU-IhR5sHCUoN0xL-l_BmsP5lkbsWZEMe12TVWD0CvOvt4rlm3dsF1esX0GLIq3RMVzltXpXW8KYjMPbfd6ZaYEybR2Xjiwtu-9qIK9ZgIySxs5FUB7XQwtkyM9zqT3VK5ttlCsLk2IRkiM6sl_6fb1bx9rx4oiACIdjo2iv6___BPRVA09W5RfPL-hxBtqBnWynd3_ZhpTwkkQROyNEiiVGY4PpteL2oHzEHIa8a6ZvniyRt_KtDn-NDZK-QX79r_ePwcWjQu5pbTLWtNggZl5US-rI6uVMjbsIvq55rJX7sbygfLriuByWP3j22WGEom3xRWOblSr-nN55AjjdYYbPTf4totxyY5dWq-URooVwhmyMCOQeMqeFG4A1Q8iVOeUqnu_IEo_1TS6Btc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر کشور: ناترازی انرژی برای ما نگران‌کننده و ذخیره ۸ نیروگاه صفر بود اما انرژی‌های جایگزین وارد کار شدند
‏
🔴
امروز ۶۵۳۹ پروژه شهرداری‌ها با اعتبار ۱۱۰ همت و ۱۲۳۷۱ پروژه دهیاری‌ها با اعتبار ۱۸ و نیم همت افتتاح می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/144460" target="_blank">📅 22:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144459">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
دو مقام اسرائیلی به باراک راوید گفتند طرح بستن تنگه هرمز از سوی سردار علیرضا تنگسیری، فرمانده وقت نیروی دریایی سپاه پاسداران مطرح شده است
🔴
به گفته مقام‌های اسرائیلی و آمریکایی، در ۷۲ ساعت نخست جنگ، ایران اعلام کرد تنگه هرمز را می‌بندد و سردار تنگسیری نیز دستور استقرار مین‌های دریایی در مسیر اصلی کشتیرانی بین‌المللی تنگه هرمز را صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/144459" target="_blank">📅 22:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144458">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca9c5cc09.mp4?token=uqpD7RyLjXu61-ruellw5MFzYQIHg_KHLFf-SwVm03ixS0_2dJavC9Zk8KlqtHYepDmeagPiaXRtEzyn8v1s4AfX8Da98Q3iVe98yaVdpUrf4uCXOULE7KnC9FKxz5Cxf4UWPZoPJP-JUuyYU0bCl1sIpsD4HQNu9Dy-Tuynx-WLZ76dhjxHljTSHiFcGYc4EOSjaDSoHFnjG21IZ0FoV4QsTQDRKx7CA5Y3vi1EMnJckg1SSqRJuwZolWXMhzb6HJxFryLmXOl2yAz6PgZymsM7_s5iSDwAEjjHnbLmHUYl1ZaNqhCPJYwmUXeVFGiFMeE0VqsWB_yi7HmQ_RyFmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca9c5cc09.mp4?token=uqpD7RyLjXu61-ruellw5MFzYQIHg_KHLFf-SwVm03ixS0_2dJavC9Zk8KlqtHYepDmeagPiaXRtEzyn8v1s4AfX8Da98Q3iVe98yaVdpUrf4uCXOULE7KnC9FKxz5Cxf4UWPZoPJP-JUuyYU0bCl1sIpsD4HQNu9Dy-Tuynx-WLZ76dhjxHljTSHiFcGYc4EOSjaDSoHFnjG21IZ0FoV4QsTQDRKx7CA5Y3vi1EMnJckg1SSqRJuwZolWXMhzb6HJxFryLmXOl2yAz6PgZymsM7_s5iSDwAEjjHnbLmHUYl1ZaNqhCPJYwmUXeVFGiFMeE0VqsWB_yi7HmQ_RyFmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهرک منصوریه در جنوب لبنان چند لحظه پیش توسط نیروی هوایی اسرائیل مورد حمله قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/144458" target="_blank">📅 22:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144457">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff4ce022e9.mp4?token=e_I4X5WysMOVXS389TsaaQ8KUIpsdQ3rROYxqlsxTGvtW4hIS_Fo94R8mrwZbRaL0hdc8CfX39g2yc1vjXZAAic2sSxVqj1iwKW1yIfOLf2ZUO5hHhWPq5PIwbbzuWDtWcxy3Pm7T19O6_2Q8srVR74PX-TtusupExZmdIrzLBT_u5AFDsq0OEpfy29oRZiUVJkaWR2WiGr5UD5L9WXrfoT_AgBelFF6WmcwM7pESMXeU09J1MP5CeWCDrmBxXTlUCnJzL91q_wu583F7yJ8TXfzOb5jiVCTx6M3ANv1kzZEGfAVGNmH7MuETCJTrcpUEO1L2CgyiCe2ycl5wtVNTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff4ce022e9.mp4?token=e_I4X5WysMOVXS389TsaaQ8KUIpsdQ3rROYxqlsxTGvtW4hIS_Fo94R8mrwZbRaL0hdc8CfX39g2yc1vjXZAAic2sSxVqj1iwKW1yIfOLf2ZUO5hHhWPq5PIwbbzuWDtWcxy3Pm7T19O6_2Q8srVR74PX-TtusupExZmdIrzLBT_u5AFDsq0OEpfy29oRZiUVJkaWR2WiGr5UD5L9WXrfoT_AgBelFF6WmcwM7pESMXeU09J1MP5CeWCDrmBxXTlUCnJzL91q_wu583F7yJ8TXfzOb5jiVCTx6M3ANv1kzZEGfAVGNmH7MuETCJTrcpUEO1L2CgyiCe2ycl5wtVNTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دیوانه‌وار، انفجارهای ثانویه مهیبی را در یک انبار مهمات در مایلا، در منطقه بوچا در استان کیف، پس از حمله پهپادی روسیه در شب گذشته نشان می‌دهد.
🔴
در نتیجه انفجارهای ثانویه، ۳۷ نفر کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/144457" target="_blank">📅 21:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144456">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56c151b7af.mp4?token=lf5ZSAVNRIKue8tFQ_7H-ijNq3gJXB6-glajy7r07adMruYgk3WgGwirraI5KQ2xl77_noVXo6Rk1LvLTsZyKNvrcbregtpbdBa9tAnDFD31hx-ZALXNNIXzCum-SI8eqeelyMzIjZJ-c2QfY1VeUGFO14bq4gRWV-I9DBJCvTqoplEI8O1nOLPrmYTmI4SCXZweJl9RWaIU6IUAtTbwA3GtrGfBC_HTHaOJzP_evFIlhgpRWBFamQvs9SyH1ewCht56Z8phsTQCEJEesiWA3WPAd45vwFeC4hNVjDUPsjjMyasOuPxMvEpopGiG7KBLvnmrSmKzE9okfgLR5iCm3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56c151b7af.mp4?token=lf5ZSAVNRIKue8tFQ_7H-ijNq3gJXB6-glajy7r07adMruYgk3WgGwirraI5KQ2xl77_noVXo6Rk1LvLTsZyKNvrcbregtpbdBa9tAnDFD31hx-ZALXNNIXzCum-SI8eqeelyMzIjZJ-c2QfY1VeUGFO14bq4gRWV-I9DBJCvTqoplEI8O1nOLPrmYTmI4SCXZweJl9RWaIU6IUAtTbwA3GtrGfBC_HTHaOJzP_evFIlhgpRWBFamQvs9SyH1ewCht56Z8phsTQCEJEesiWA3WPAd45vwFeC4hNVjDUPsjjMyasOuPxMvEpopGiG7KBLvnmrSmKzE9okfgLR5iCm3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات عجیب رئیس ستاد امر به معروف: زباله‌گردی در معیارهای جهانی نشانه پیشرفت یک کشوره؛ کشور فقیر اصلا زباله نداره که کسی بره زباله بگرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/144456" target="_blank">📅 21:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144455">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
عراقچی: ملت ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/144455" target="_blank">📅 21:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144454">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f57eb5399.mp4?token=DxrNtiXVAGFihzUqh8JC4jqHXnHIGgSRVPVmJ3ft9ycN7_hH6ZSwH1hix1N8HJe2qjlo4OGIFCn6wS-oB8I-NB4gGDCQWSSeUMqNP8BLFrFDBDmXEkM-1wabbXttqbOghJ8OE-Kv9oI3eXFGsrxFERiS0yY5U4w0t49KtudAhkCGfQ4mml4UQPEK8aGWT3otjqXThGGBHUYSmKLKuceLGHCWS5jObf7v9Dd3Ij0YPzwOJY5RZDlZCqMmETcTicbiAsLTuGNujULG-STdXu2oCHxKl9KyiLgEm1AEpyR3gfuhecr4ViiPqMLaID-X34NS1jURqH-Qwld_itQmnB6r8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f57eb5399.mp4?token=DxrNtiXVAGFihzUqh8JC4jqHXnHIGgSRVPVmJ3ft9ycN7_hH6ZSwH1hix1N8HJe2qjlo4OGIFCn6wS-oB8I-NB4gGDCQWSSeUMqNP8BLFrFDBDmXEkM-1wabbXttqbOghJ8OE-Kv9oI3eXFGsrxFERiS0yY5U4w0t49KtudAhkCGfQ4mml4UQPEK8aGWT3otjqXThGGBHUYSmKLKuceLGHCWS5jObf7v9Dd3Ij0YPzwOJY5RZDlZCqMmETcTicbiAsLTuGNujULG-STdXu2oCHxKl9KyiLgEm1AEpyR3gfuhecr4ViiPqMLaID-X34NS1jURqH-Qwld_itQmnB6r8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
داگ فورد، وزیر انتاریو کانادا، در واکنش به فرمان اجرایی رئیس‌جمهور ترامپ برای تغییر نام دریاچه به «دریاچه آمریکا»، یک تابلوی بزرگ با عنوان «دریاچه انتاریو» را در طول خط ساحلی رونمایی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/144454" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144453">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9Lw2UGm297TwcQAkAIcCuJjVMiZFA9dHF51vwoXC92ikDok0txpDZBlNkmPuyZQZ0mbskWGEDseoewXzy52yfT4LVjL8iSQaT1thz91jTpsECwJ8AkYPOCu16E7EaUVDU1UL9pdYUbGGc3BgflJENMQBndpX5QTB2jFcE_O4kQ7fsSWqPT2cx3v7V1Rk5hI25yjUwOEVnCrQA5llr4xq_TjqCTNm4rV5quV_3YstpK85vywSaEuA-EMD5K7780VmPVnMH5TiN71HGKGLszfydkBqNX3xHC8UEmbpT-b-uEViMBL3iLBw3EMx0-G17wuWuy8VETd_Cf-RDRXk8QbfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: من اعمال خشونت‌آمیز جنایتکارانه‌ای را که در روستاهای قصره و جلود توسط مشتی آشوبگر انجام شده است، به شدت محکوم می‌کنم
🔴
این آشوبگران قانون را نقض می‌کنند، بی‌عدالتی بزرگی را نسبت به جامعه یهودی قانون‌مدار ایجاد می‌کنند، در انجام ماموریت‌های ارتش اسرائیل دخالت می‌کنند و به جایگاه اسرائیل در جهان آسیب می‌رسانند.
🔴
نیروهای امنیتی به سرعت وارد عمل شدند، سه وسیله نقلیه را توقیف کردند و در مدت کوتاهی به این حادثه پایان دادند.
🔴
ارتش اسرائیل، سرویس امنیت داخلی اسرائیل و پلیس در حال انجام تحقیقات جدی در محل هستند و من انتظار دارم که مقامات انتظامی آشوبگران را در اسرع وقت دستگیر و به دست عدالت بسپارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/144453" target="_blank">📅 21:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144452">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b35ada18.mp4?token=C3qK4bcZB5-bMQDmIW1p3WCAU4wSJ5CHY8a0MirHaYSwyBpfjISGI4__5sW-AkeOt-66E7uUbcT17SxWwbEbwiUtWhvBkrIVuk52eZPtHYGYIjNlbxyNdDcBGLELu5wGcSGKoMqnBUMTDHe19ni19yQ61U01vJS_gc4LfZISw8JUtLUibvPzL8EkagaJYm_PElSjxmpyAdhozLWw18WQIMmHeow5Q_EXvNcPz0AeWnZwl9vxxz_1B0FigxDQKol641j30q58rmNpAVZ5o_8XXCxaV3AR_KoGcxhMHZ6ih4mQJPQ8RvB44lUtd26w7QJuITp8mHouyVmcVuDfWZT3uQngKGp_GKgpxckAUnm7qiYqVnQ2sK31ctHViSjo5MnA_UH4imx-zqJRdFzYVabJLvBof20n6vSH5Xe7L2IWtHzpSpy-XR3ilRaXAIqFBcLpAGZP5XnVM3sxk52zoasc2rNjY8IYUxMxIM87vt3VLT1P8U7enhn5xjZuNkJ2cingQp8NYmqe_qBNcvbNS2PUjqp8xBbs7LkwZ8ce11ckHwlNr650mXia2W-3-uxKABjJkicLJvgcq3unFTgTxD_YTMZPY8_MW9ydgJ2kywR_3_RZL-B1PBqQyWTUUqYOZ69cXPUoPbIA8VpG6aYX6nP2vAhdI5YzIH_EbI-dag8AJMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b35ada18.mp4?token=C3qK4bcZB5-bMQDmIW1p3WCAU4wSJ5CHY8a0MirHaYSwyBpfjISGI4__5sW-AkeOt-66E7uUbcT17SxWwbEbwiUtWhvBkrIVuk52eZPtHYGYIjNlbxyNdDcBGLELu5wGcSGKoMqnBUMTDHe19ni19yQ61U01vJS_gc4LfZISw8JUtLUibvPzL8EkagaJYm_PElSjxmpyAdhozLWw18WQIMmHeow5Q_EXvNcPz0AeWnZwl9vxxz_1B0FigxDQKol641j30q58rmNpAVZ5o_8XXCxaV3AR_KoGcxhMHZ6ih4mQJPQ8RvB44lUtd26w7QJuITp8mHouyVmcVuDfWZT3uQngKGp_GKgpxckAUnm7qiYqVnQ2sK31ctHViSjo5MnA_UH4imx-zqJRdFzYVabJLvBof20n6vSH5Xe7L2IWtHzpSpy-XR3ilRaXAIqFBcLpAGZP5XnVM3sxk52zoasc2rNjY8IYUxMxIM87vt3VLT1P8U7enhn5xjZuNkJ2cingQp8NYmqe_qBNcvbNS2PUjqp8xBbs7LkwZ8ce11ckHwlNr650mXia2W-3-uxKABjJkicLJvgcq3unFTgTxD_YTMZPY8_MW9ydgJ2kywR_3_RZL-B1PBqQyWTUUqYOZ69cXPUoPbIA8VpG6aYX6nP2vAhdI5YzIH_EbI-dag8AJMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر جدید منتشر شده از اسکله رجایی در بندرعباس، بزرگ‌ترین بندر تجاری ایران، حاکی از توقف پهلوگیری کشتی‌های تجاری در این بندر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144452" target="_blank">📅 21:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144451">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4BVhWizfvztRB6BzXItgU3m5ly2qdsUVenmARf7plq4jtoiuMSMoZREDLj7vIgT38qYlWg561MU_gsHerVmdF0a7x-Kx12z-gk2_VNW-uIqhQjgxECsOjdH25mUDW6EKPs1MMPvy_XUiG1giabmT_T_EH9kJMSeWL-IO36CWvgzUPtzhfuI7QNjzQNK4GWcdAzvAEBlIl97okRk8AN4c59f1VvKPKBuIRFhojSTjlFCboxvcuHfS8TkNLgVAdXsIj2fNKCLL70AWBSkunNBJqJbz2a1gHrmt4SUu-HK-u1E8sXKUgs5HIxwGpHWgO8HNxjDlrH0yy8WlaMUbSxhpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخورد زیردریایی اتمی آمریکا با کوه زیر آب؛ کانتیکت ۵ سال از رده خارج شد
🔴
زیردریایی یواس‌اس کانتیکت (USS Connecticut) از کلاس سی‌وولف نیروی دریایی ایالات متحده، در حادثه‌ای کم‌سابقه در جنوب دریای چین با یک کوه زیر آب که روی نقشه ثبت نشده بود، برخورد کرد.
🔴
این زیردریایی اتمی که یکی از سه فروند گران‌قیمت‌ترین و پیشرفته‌ترین زیردریایی‌های تهاجمی جهان محسوب می‌شود، پس از این تصادف برای یک دوره تعمیرات طولانی‌مدت به مدت حدود ۵ سال از خدمت خارج شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144451" target="_blank">📅 21:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144450">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
از الان به بعد مدارس روسیه آموزش نظامی اجباری را گسترش می‌دهند و به بچه های ۱۳ ساله در مورد مسلسل، نارنجک و سلاح‌های ضد تانک آموزش می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/144450" target="_blank">📅 21:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144449">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
گروسی: نیروگاه هسته‌ای زاپوریژیا ۱۰ روز دیگر وارد خاموشی کامل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/144449" target="_blank">📅 21:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxUA8Pnd6U-czYfl1-wuGKa8g3v3VbC7aGtWl63c5B82LudtBxtQh25zS2yOpz86PV2rerVEL_A_8TgN2yId_7JGz5BXJ_zImMdEjLCfGGTD-fPuRcY_eViYYhSPpnI63FlKiHY4PorantxXVEHvj7OMnhqB5FUFShsr2SHeXdQZ1yqlaR0v2Gl1Jl2nfHn4kvY-uNqPSHuSxrUs3M35ggNLKSCR5ZjHLs2TTr58GqI4FGsS2CQq-XRQjjyE-jY79qSDogbC7hOxTTHMLjvTqz2YBSQf2MkdAPnF2SZarWVlRdnAmV40YGYpjIAhT9Rm_Xe3JTTthoHSUl_Oh2Queg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق جدیدترین تحقیقات تو سال ۲۰۲۶ بهترین کشورها برای زندگی زن ها و دختران از نظر رفاه، امنیت و آرامش روانی و اجتماعی : ۱-دانمارک ۲-ایسلند ۳- نروژ هستن
🔴
و بدترین کشورها : ۱-افغانستان  ۲-یمن ۳-آفریقا
🔴
ایران تو رتبه ۱۲۱ این نظرسنجی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/144448" target="_blank">📅 21:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144447">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52c1cd1de9.mp4?token=lx7Pax85HIOKf0HtsT99TZsc8I9wQOSAIMkALm8NQT4DCSixA5IYS8lG9nIh74idnNehP5p1_O4Zd5rH2GzK7YdF1CxYF9Xo4WX54cgF87Art0SIMfTsQQyPfJDbAFSJ0U2qCgmg3m2_7sPE_jFJyFj1K9275JNu391X6dnE2qaFBq2bLclA8cJp5bXGP6l5g9yTNoWsHCEBUQ2Z5rgARLMUHIkGXFFuDzAhrJKfyx8rBZqNVMv8sGBv97qB1RLp_LLIXPPcCtli2ScrBybkZaot3oeKmETgvXq-QsgLlLfIda54XNoUIFqEjpvSJXBmSvGedJwzeVPGWHNI1SLFMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52c1cd1de9.mp4?token=lx7Pax85HIOKf0HtsT99TZsc8I9wQOSAIMkALm8NQT4DCSixA5IYS8lG9nIh74idnNehP5p1_O4Zd5rH2GzK7YdF1CxYF9Xo4WX54cgF87Art0SIMfTsQQyPfJDbAFSJ0U2qCgmg3m2_7sPE_jFJyFj1K9275JNu391X6dnE2qaFBq2bLclA8cJp5bXGP6l5g9yTNoWsHCEBUQ2Z5rgARLMUHIkGXFFuDzAhrJKfyx8rBZqNVMv8sGBv97qB1RLp_LLIXPPcCtli2ScrBybkZaot3oeKmETgvXq-QsgLlLfIda54XNoUIFqEjpvSJXBmSvGedJwzeVPGWHNI1SLFMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) می‌گوید حملات دیروز در شمال غزه دو نفر از مظنونان به عضویت در حماس را کشت، از جمله هانی عبدالهائى فخری مظلوم که به گفته آن‌ها فرمانده یک گروه در نیروی نخبه «نخبه» حماس است، و حسن زیدان حسن دییری، تیرانداز.
🔴
نیروی نظامی اسرائیل اعلام کردند که هر دو نفر همچنین در تأمین و قاچاق سلاح برای حماس نقش داشته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/144447" target="_blank">📅 20:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144446">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سیل‌های ویرانگر در نزدیکی مرز چین و نپال دست‌کم ۶۸۲ کشته بر جای گذاشته‌اند؛ از این میان ۷ نفر در سمت چین و ۶۷۵ نفر در نپال جان خود را از دست داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/144446" target="_blank">📅 20:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144445">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pMN5BW3BuSdWpc03GcgDlqtE0zLu98XchwmTacLSVG9GfqCMkTP2HnQFPshE4Y-Wt_5U8w-MO3EPr--oTLbljhDPzmvW3NQ56zELOcU1Ao9qAbDwQz2z3XAsSHP-4UyCLWibb32VjhKFLB0rB8IkEvXiCUIjGPZl-mY-ZSDs1AIDT1tvtEutIB-nRvSl8Q_SqPs4cu8W7nQNPALPxegrYLz8-ZNFFtPQ9B3n-QVa4N3IAnvbkAJ8sB20ubatVwRZL11pIbBrxyB0K5hVYpQWT3HFEAR1b9FM4IavExSHZvqRSiQLP5BulWiIwTcwi1IUXJL8ewvZcfUTQdtqbZrJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) روز شنبه هفتم شهریورماه تصاویری از تفنگداران دریایی آمریکا در حال سوخت‌رسانی به یک هواگرد «ام‌وی-۲۲ آسپری» در یک پایگاه هوایی در خاورمیانه منتشر کرد.
🔴
«ام‌وی-۲۲ آسپری» یک هواگرد نظامی با قابلیت برخاست و فرود عمودی است که برای جابه‌جایی سریع نیروها استفاده می‌شود. سوخت‌رسانی به این هواگرد در پایگاه‌های عملیاتی می‌تواند برد و مدت فعالیت واحدهای هوانوردی تفنگداران دریایی آمریکا را افزایش دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/144445" target="_blank">📅 20:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144444">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9021f8047e.mp4?token=UaX81YT9YEWYvHphJuvXU27JyDLCfj_e5TA2GeqN3_ml15tAH7-V6DjSRQI9zfxE1-MeLrKY2l2OBCdSgy32fYBeK3NTBfD6u3DJRrAlXJ0Mt-G5yV4jkJNJmgqbQdVpbs8_do12WkLxmJxNU3N5G0hAsh71kOHhgaQbkgmFQifX5-SKTQt3ORxuBYUTpD5bbqvLBOCGvTmZfKccZMjJxKNQxvin1ZVdTitV9XRrOfJvprVCmgOHrJhHacc5LHaTQkhUTZIDdBk0cUJr-tDQb7joTK0Q0S592mopQRah8YTUm_5v_0o0pq_pIUNIwr0qRvTRliuaNIW3QWtXJPghEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9021f8047e.mp4?token=UaX81YT9YEWYvHphJuvXU27JyDLCfj_e5TA2GeqN3_ml15tAH7-V6DjSRQI9zfxE1-MeLrKY2l2OBCdSgy32fYBeK3NTBfD6u3DJRrAlXJ0Mt-G5yV4jkJNJmgqbQdVpbs8_do12WkLxmJxNU3N5G0hAsh71kOHhgaQbkgmFQifX5-SKTQt3ORxuBYUTpD5bbqvLBOCGvTmZfKccZMjJxKNQxvin1ZVdTitV9XRrOfJvprVCmgOHrJhHacc5LHaTQkhUTZIDdBk0cUJr-tDQb7joTK0Q0S592mopQRah8YTUm_5v_0o0pq_pIUNIwr0qRvTRliuaNIW3QWtXJPghEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صادق الحسینی، اقتصاددان، مدعی شد: کیفیت بنزین به حدی پایین آمده است که موتور خودروها تا ۳ یا ۴ ماه آینده خراب می‌شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/144444" target="_blank">📅 20:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144443">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
دولینگو (معروفترین برنامه آموزش زبان جهان) اعلام کرد آزمون‌های این برنامه از ۱ سپتامبر (۱۰ شهریور) برای ایرانیا متوقف خواهد شد و دیگه از ایرانیا آزمون نمیگیره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/144443" target="_blank">📅 20:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144442">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47148daf34.mp4?token=J5f0kOkrCKUnGPoWt1BEj3eOObfidO-Gt3_h1tUtWK5ncwIK2cGuTyydJkNHwCjWgE50msHUj3vWM6YLBQZrvE84bPN8DsnuRATdUMa2DarFLVFglwN8ZVUBlFCp5Nj2J2WaqJGny73jCwLA8G5jI5aIRiDEsj41lF_KAX-UA3fBhYOcecj7TwAwzwZWfFo5O74Hc20u85unDWxpAcHzSFtMyGdjSSYdLjYbBKIv3Dxt1yrFZGc7J3OqknSkxLqo1XfKft8UA_OSdscjSa-ObTQOPTJhGtjeEI5HkvRXuVpsDLE_KJn_uqCmTGD8Q-nUovqLHG0gjyrlRRg6nns-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47148daf34.mp4?token=J5f0kOkrCKUnGPoWt1BEj3eOObfidO-Gt3_h1tUtWK5ncwIK2cGuTyydJkNHwCjWgE50msHUj3vWM6YLBQZrvE84bPN8DsnuRATdUMa2DarFLVFglwN8ZVUBlFCp5Nj2J2WaqJGny73jCwLA8G5jI5aIRiDEsj41lF_KAX-UA3fBhYOcecj7TwAwzwZWfFo5O74Hc20u85unDWxpAcHzSFtMyGdjSSYdLjYbBKIv3Dxt1yrFZGc7J3OqknSkxLqo1XfKft8UA_OSdscjSa-ObTQOPTJhGtjeEI5HkvRXuVpsDLE_KJn_uqCmTGD8Q-nUovqLHG0gjyrlRRg6nns-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک بمب‌افکن روسیه در پایگاه هوایی انگلس هدف قرار گرفت
🔴
یک بمب‌افکن راهبردی روسیه از نوع
تو-۹۵ ام‌اس
در پایگاه هوایی انگلس-۲ در منطقه ساراتوف هدف قرار گرفت.
🔴
این پایگاه یکی از مراکز اصلی روسیه برای شلیک موشک‌های کروز به سمت اوکراین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/144442" target="_blank">📅 20:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144441">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: هیچ چیز به اندازه احتمال ادامه حمل و نقل دریایی هدایت‌شده توسط آمریکا از طریق تنگه هرمز، به اهرم فشار ایران آسیب نمی‌رساند. اگر این امر ادامه یابد، اوضاع را تغییر خواهد داد. اگر چنین شود، اوضاع بسیار بد خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144441" target="_blank">📅 20:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144440">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اردوغان: مشکل ایران و آمریکا راه حل نظامی نداره و باید فورا برگردن به میز مذاکره
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/144440" target="_blank">📅 20:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144439">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
تصاویر بالگرد چینی از  سرچشمه سیلاب مرگبار در مرز چین و نپال
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/144439" target="_blank">📅 20:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144438">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5638aa725e.mp4?token=VaDpAP7uEMi3tKAvCV7fWOnQAVoSFII0sBWq-8qMIPVG_gBN3IYRwKwxkpxpLXWKE5-_QvZLyV4RmjxvEHNs-D6qS9VkX0oGg6m8UiC_TpLtLVWACoePkFyO70MW2ixy0RARfD1d3U2sIy4BKyzx1JS-ut1-6_6xr0_1JZcf3-OZQ9BV_RNlR6fbwb3EUHvLN2bwa_MTmvuMxohAU9-mf5mr2A95hbgvSqk-3z23GrIlsUXTGTrdFwdRltkhqFlIhhHrLLeanZHt85JErmEOMRK9qmjBaES2SCMKOPMqdi5tolr24_axWVziPrhReLn0_4CQyqG-Mj5coukGhhBBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5638aa725e.mp4?token=VaDpAP7uEMi3tKAvCV7fWOnQAVoSFII0sBWq-8qMIPVG_gBN3IYRwKwxkpxpLXWKE5-_QvZLyV4RmjxvEHNs-D6qS9VkX0oGg6m8UiC_TpLtLVWACoePkFyO70MW2ixy0RARfD1d3U2sIy4BKyzx1JS-ut1-6_6xr0_1JZcf3-OZQ9BV_RNlR6fbwb3EUHvLN2bwa_MTmvuMxohAU9-mf5mr2A95hbgvSqk-3z23GrIlsUXTGTrdFwdRltkhqFlIhhHrLLeanZHt85JErmEOMRK9qmjBaES2SCMKOPMqdi5tolr24_axWVziPrhReLn0_4CQyqG-Mj5coukGhhBBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظات اولیه حمله به انبارهای نفت تهران در جنگ ۴۰ روزه
🔴
‌️انتشار برای نخستین بار
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/144438" target="_blank">📅 20:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144437">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
گفت‌وگوی وزیران خارجه قطر و ترکیه درباره کاهش تنش در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/144437" target="_blank">📅 19:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144436">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu2gyGX2Ql7v6Pkn5mNH0NN-fa79gvyh74U8VLTSbfr5RQs0U9Tph4QxG552sQmq-Ag7aEfQi4NNxcCvjEzWfv7YdrB6gRlKG2Fadibdozp4qZXAoo-BBj8lcLoV-KciUQfhSagi2K4JQLo5chSTPUebkvzsq9Nm4MjsdKDrwULYZ22P-JS11T6g_rJ2Jas2pVsuUdmIG2GdmKuurnhq3cwA7j0vuXCzVBCQP4MokKdV7mb8K8XolsfDhrjtRyuqZCglU1p-0maagxl0_002RxvSz6fkJ_RRMPnwOgUeVr2pUw7HJs-U_rwSzUR3w8EKQKv7UJhhEfHGK5tgPqv7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات توپخانه‌ای اسرائیل به جنوب نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144436" target="_blank">📅 19:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144435">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY0BBd1wUwlEnLmKb8J1KewcNDqYqHzsmNN4PT3Qd5HQn5xyw2kMNeRJayIygiYxis07M-hcKUxw___GZsDiPOiK7iXs46z34EFX3aaPnnKcJArVuvMTGfyL8pUMyUk_w7pmcbdUsrw8k3QIReqNGrD4Q3wT9kAgoj9BbmWPOdB5JU_WcxCuGIybWc9ovD_u4lgqEEk1xuHJLCXw9r00j_fzb6QN6_jqNQLRHj6J7rVw7UR1QclHKtEAAnIGMW70EbnN-5pmrJN8o098i7SEN3XFtcI7muq55rHlKM_j7TQrHhlhfsY3D6c0u_XckFr9w6cyR8V0YpWamTickVYy0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف خطاب به اسکات بسنت: دروغگو، دروغگو، شلوارت در حال سوختن است.
🔴
در واقعیتِ ۱۳۰ میلیاردی، به دستیار خود بگو گزارش مودیز را که هزینه‌های جنگ بیش از ۱۳۰ میلیارد دلار را نشان می‌دهد، بیرون بیاورد و از دیگری بپرس که جین استریت چقدر در یک دوره معاملات آتی برای شما با فروش کوتاه نفت بیش از ۱۳۰ میلیون دلار ضرر کرده است.
🔴
دروغگو، دروغگو، بازدهی‌ها در حال سوختن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/144435" target="_blank">📅 19:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144434">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
الاخبار: ارتش لبنان قصد رویارویی با حزب‌الله را ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/144434" target="_blank">📅 19:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144433">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59c74d913.mp4?token=hXwvnZkZQDTcHmU8xkGymAnZRvPOcNxGKc1Abn21AUlC66lorY-ARgkFL2kSn5HjCVUrde6LbVLefHNFZNAM1DbXOfy8QuYaX2jK0eC0V1dMkGcw_1KQwwgr7zfBAC0owqyB2uyTumTRBOdJR9vX_OVnGHWO9aawM_Iqiy_APsXGqp5YFijGA-NNwpQScQlhbQZaeGgi1TNB6AJ1d3TAeG8usf3dOLk_VLXg3Jr00w5jJvLgwhSVsRn61ItcpnNKEm-enmcphZu9Ql8DkyQLPEvG3FRMjBeqPJxcZa8-phr88EzTWNhLj_5RWw2PcrEMRWZiTtMIQ-GG7f0Qpbszcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59c74d913.mp4?token=hXwvnZkZQDTcHmU8xkGymAnZRvPOcNxGKc1Abn21AUlC66lorY-ARgkFL2kSn5HjCVUrde6LbVLefHNFZNAM1DbXOfy8QuYaX2jK0eC0V1dMkGcw_1KQwwgr7zfBAC0owqyB2uyTumTRBOdJR9vX_OVnGHWO9aawM_Iqiy_APsXGqp5YFijGA-NNwpQScQlhbQZaeGgi1TNB6AJ1d3TAeG8usf3dOLk_VLXg3Jr00w5jJvLgwhSVsRn61ItcpnNKEm-enmcphZu9Ql8DkyQLPEvG3FRMjBeqPJxcZa8-phr88EzTWNhLj_5RWw2PcrEMRWZiTtMIQ-GG7f0Qpbszcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر بهداشت ایالات متحده، آر.اف.کی جونیور: سربازان ما برای اولین بار در تاریخ، غذای باکیفیت دریافت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/144433" target="_blank">📅 19:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144432">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7t3KmcujNmaZt87_Z-tH93rztKU5TJ1Ab32CTv2F88cGeONMVKLG7fyqjiogmxlnjDgJI8PuXsWX0rtlTrXCY6-96fLzJ93Yp4iwBDUiHM0Qc2K9RmYiBxVetevPOvPxvLzSLeZ6_b8-yZGms_zGRtbaCOdDdavoyOOzVIuXxN6o5u9DDBntjvbHP6Futc986quqbCOKESt0l8tAyhuF1D2mEsv2lRiASVq85SprPc8Rv6C9nF4ar0ZKHTysPl-TjwGAAzTta9Ra76EFv297wMbKdlHs8eIeL58zN0zy8Gz8fihtGN_sTtAcatATWCBBV9m-k_6wMjewNL3m8VQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گوشی نوکیا ساده که همیشه نماد ارزون ترین گوشی تو ایران بود به ۸ میلیون تومن رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/144432" target="_blank">📅 19:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144431">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9238eeb8.mp4?token=axFkhfArKXdE_4QeflN1F69YsyFupJUi0mYo15Rpfw5GCDqcFo25zp79PJd8MWB2TlXZVdPrtk5QNQBnNLx09yEDiif_wo9r4_VmgQQxIUhZzHE8Vq5BoUHz1FGihZtYXGoPrqwX-6uwXQwLsvHu6Oa0hOhtcRXnPl5y5zWnKKYmGPHjKhi6ae656W1hX1-t7xqkeTPizePe0tvjHOmDCg3Vg_r_iQ1VuPu3fEgBF86cghQnU3mMSIL5cLAK2pHnI214o73GOEcpga7i3turzdFK6BgoNdQaesv-CyajOrlf05ApCTsyGWPCmeh_7kdQnXdFzYxs8m7VYQs1KftSGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9238eeb8.mp4?token=axFkhfArKXdE_4QeflN1F69YsyFupJUi0mYo15Rpfw5GCDqcFo25zp79PJd8MWB2TlXZVdPrtk5QNQBnNLx09yEDiif_wo9r4_VmgQQxIUhZzHE8Vq5BoUHz1FGihZtYXGoPrqwX-6uwXQwLsvHu6Oa0hOhtcRXnPl5y5zWnKKYmGPHjKhi6ae656W1hX1-t7xqkeTPizePe0tvjHOmDCg3Vg_r_iQ1VuPu3fEgBF86cghQnU3mMSIL5cLAK2pHnI214o73GOEcpga7i3turzdFK6BgoNdQaesv-CyajOrlf05ApCTsyGWPCmeh_7kdQnXdFzYxs8m7VYQs1KftSGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در تروث سوشال درباره دریاچه مشترک با کانادا: دریاچه آمریکا، محافظت‌شده توسط اردک‌های دونالد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/144431" target="_blank">📅 19:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144430">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d8cf7ba8.mp4?token=hdPJpd625GC-90R-eF1tlbQChCXjO8sii_v8_H08bardOONdt_QNZLKKdd7YShn2wHqxcbYDp7Cct0Shlmy_OlOZMbhj4qmjN5R3z9DAPTADtz3EvpOHaqdrab9E-I4XeftWQexkLbDt3Rk8AUDxIRsOwT5tEdhf93G_a7hWhzreSrKRtKcqsGt7zfC34jRy0MNxnRP5_rWJB4uWwtVDm4Bv_KjeFZ7Qfi-fSqKPSrj5mTD0mFt4qOskhXiN7q6OJ-UUDye3W6gjan-JvlmvEKBceCs25rGJpFcS7NwXsd7PYcQ8NLYMm-4_C402I4CPuf-cJ0s3_qLNtqVJ-26SBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d8cf7ba8.mp4?token=hdPJpd625GC-90R-eF1tlbQChCXjO8sii_v8_H08bardOONdt_QNZLKKdd7YShn2wHqxcbYDp7Cct0Shlmy_OlOZMbhj4qmjN5R3z9DAPTADtz3EvpOHaqdrab9E-I4XeftWQexkLbDt3Rk8AUDxIRsOwT5tEdhf93G_a7hWhzreSrKRtKcqsGt7zfC34jRy0MNxnRP5_rWJB4uWwtVDm4Bv_KjeFZ7Qfi-fSqKPSrj5mTD0mFt4qOskhXiN7q6OJ-UUDye3W6gjan-JvlmvEKBceCs25rGJpFcS7NwXsd7PYcQ8NLYMm-4_C402I4CPuf-cJ0s3_qLNtqVJ-26SBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از منطقه چترکوت در استان مادھیا پرادش در هند نشان می‌دهد که آب‌های سیلاب تا ارتفاع نزدیک به یک ساختمان یک طبقه بالا آمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/144430" target="_blank">📅 19:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144429">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
استیون میلر، مشاور کاخ سفید: تنگه هرمز برای ایالات متحده باز و برای ایران بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/144429" target="_blank">📅 19:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144428">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ea5004bf.mp4?token=jZ03K8hcWFN0_3Pa6otM_vrO14XnyNupdoEGv11uSWRaf2HyxoqMm82Ojr4jg6sSN_hGpJoz2N1hLjxFtJ8stKTltTXKukeu5LtmAb7Ifx_n9dIR4cbZr_wEUhgIkX2PW_Phh9wCF9Gf1TAtsUmZJLk5OMbshT40wd3wzZIbwgSnLr_LkWAJqw9JYHkIJwBDPQP_G7PFKW4hwgWR3pm-rQLjhBpXuuaEj7Zr34ixgw__QF5ZjY2iubTsVO7uvbPxzKn3DGTEaGSEeH_RtUqnFWaLlCX2d0pE63yZAUUrlcARX0wLnH7-R0YIUjQtdVsk1Xly2nmSi_QEHWyL9CQ88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ea5004bf.mp4?token=jZ03K8hcWFN0_3Pa6otM_vrO14XnyNupdoEGv11uSWRaf2HyxoqMm82Ojr4jg6sSN_hGpJoz2N1hLjxFtJ8stKTltTXKukeu5LtmAb7Ifx_n9dIR4cbZr_wEUhgIkX2PW_Phh9wCF9Gf1TAtsUmZJLk5OMbshT40wd3wzZIbwgSnLr_LkWAJqw9JYHkIJwBDPQP_G7PFKW4hwgWR3pm-rQLjhBpXuuaEj7Zr34ixgw__QF5ZjY2iubTsVO7uvbPxzKn3DGTEaGSEeH_RtUqnFWaLlCX2d0pE63yZAUUrlcARX0wLnH7-R0YIUjQtdVsk1Xly2nmSi_QEHWyL9CQ88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
تصویری جدید از ورود وحشتناک سیل در نپال
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144428" target="_blank">📅 18:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144427">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
الجزیره: قیمت بنزین ترامپ را تحت فشار قرار داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/144427" target="_blank">📅 18:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144426">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اقلیم کردستان عراق: شرکت‌های نفتی پس از اختلالات ناشی از حملات پهپادی، فعالیت و تولید را از سر گرفته‌اند
🔴
قائم‌مقام وزیر منابع طبیعی اقلیم کردستان عراق روز شنبه به رسانه‌های محلی گفت تولید نفت در این اقلیم از سر گرفته شده و اکنون بین ۲۲۰ هزار تا ۲۳۰ هزار بشکه در روز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/144426" target="_blank">📅 18:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144425">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کرملین: در حال حاضر هیچ زمینه‌ای برای بهبود روابط بین روسیه و اتحادیه اروپا وجود ندارد.
🔴
اروپایی‌ها به طور کامل منابع نظامی خود را علیه فدراسیون روسیه بسیج کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/144425" target="_blank">📅 18:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144422">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqHAZGIuKShZbFpkarzj6EYec6qH-a--oMYBTZW0vKNJB-B1I2ZakxLp2aCE_jEoduKBvPrgmgK2m-oEFvztsNfvisDc5DIJvSNkqyhtiuxJ2ik5SnD2n-c4qEYaBw7qgDbal7Drgze5fjDK9AEFJwCJ3M1tDRYxBb0MvkD7pM9f0GwvpoaELeL7prgazeX2Veg7YsynszPtoZ4hrGfRHaZkXz6z7FucRpMbar5Lzl0rb_uFsZou82QYO_1aIQOGgUt_BzmtIX-Mkc1x0qLBKxMqV7dJJd4hoi-tFuKwV76I67GczwXGtSD-ZC61tv1dhWrWIGreN9m6CPdkM81YUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fbHhn3q2RaD1Sd7PAwxEVzeE40y9Nn_qWm9YD_fzjO2pzQO72me-U_sozzxK4jX6nlBFQzyNUVSgAdHjC_pIBMTXgUWOBZaipZ-wEWNOi1q87omYylbgpyQ4q8YRK8OYJcqlyai0NQtcZ3JpkCAvuMDad2oPAdAU8we7Ox3wz7VbKjWZ4F6WyEZgpmwISdLeHf5uSgEyHeasIz5HAHd1RcRWxcQxSeMbD2kb_lnC9Ywp3HRhwsGAmq95YZF8Iz4gsrlOJC90lMZ-EOX3d0cIsjeyhzQItqJj2QTc2TJLG9vYORNbHvok3fNu5Y6an_4DfK8kNS7S-yIYufJn5UHEsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g31TNxkllOAleHnHeGeBWLmZ8Y9Y5FOk4FF6z05Dh6fGOsValmAhbHZ1D73Mu6G_pakD0eAWT0xm9fwDL9fUk5pPuqdllW5cRD80Hixl01u868DDAqL3A-XONsGZJBEgl-Ojk7PbHFylFdfqZQbAhInhwpR3Wpv6qGVJZW-_H5SnOUNxuhAmH5H17kjPqO9HR5MhfRxKLkibInvI0UU4k-UwDtUvW2hRx3b7db7J2S0yipN6lQxd_PFi2dljBRcYwykkkwDleLXEZlJYuAvSw5ZizE-Zrh0bNnetT65AKwoD98F5HPgXbTgoNMtQU4naaSfJnX2WjpEgZJkD7YoTxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون جت های اسرائیلی در حال بمباران جنوب لبنان می‌باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144422" target="_blank">📅 18:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144421">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
۳۷ نفر در حمله روسیه به کی‌یف کشته شدند؛ اوکراین نیز به کریمه حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/144421" target="_blank">📅 18:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144420">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ، به سی‌ان‌ان و ام‌اس‌ان‌بی‌سی حمله می‌کند و هر دو شبکه را «مارپیچ مرگ» می‌نامد و می‌گوید «واقعاً، هیچ‌کس به هیچ‌کدام از این دو شبکه نگاه نمی‌کند».
🔴
ترامپ از تحلیلگر نظرسنجی سی‌ان‌ان، هری انتن، تعریف کرد و گفت که او نباید اخراج شود، پس از ارائه نظرسنجی‌هایی که نشان می‌داد ترامپ «شش برابر محبوب‌تر» از آبراهام لینکلن، جورج واشینگتن یا هر رئیس‌جمهور دیگری است.
🔴
ترامپ گفت که سی‌ان‌ان می‌تواند از طریق «رهبری و مجریان جدید» احیا شود، در حالی که استدلال کرد که ام‌اس‌ان‌بی‌سی نمی‌تواند به همین شکل نجات یابد، زیرا «یک برند بزرگ هرگز واقعاً نابود نمی‌شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144420" target="_blank">📅 18:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144419">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فارس: ترامپ رو تحت فشار گذاشتیم و درحال پیروزی مجدد هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144419" target="_blank">📅 18:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144418">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06639a95d.mp4?token=mz0I8451s2KfjJqLsSe0VGa6JERbL6uAAikyiR6FoAah5OrchZ1hqoOKJm8jlZPblN0RwKR_q337SB3jlKCTwwHPRzG2nb_PvoiM-MiC2Khgk2Gw054kD7_dwCgjoYaqGJY695DOG4ABqtp89hS3Q4cqZzN0HA4NFhwiXnn8-kyj4RAEnbAHd_1aGhpd2YWaQ9qpzBc2a4U7GqiOiJqWHz-TocgH91Aq0-SLo3RJa6AgNI3hJSgaQDuKO7e58wxlmncerNgwr7oF6uSxOr_Oqy1rG9UHApN_CdDu4BgHH6Z1TfZF3hz7aS50eEwc2VMXh709I98LnCbEIEiNiRjCtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06639a95d.mp4?token=mz0I8451s2KfjJqLsSe0VGa6JERbL6uAAikyiR6FoAah5OrchZ1hqoOKJm8jlZPblN0RwKR_q337SB3jlKCTwwHPRzG2nb_PvoiM-MiC2Khgk2Gw054kD7_dwCgjoYaqGJY695DOG4ABqtp89hS3Q4cqZzN0HA4NFhwiXnn8-kyj4RAEnbAHd_1aGhpd2YWaQ9qpzBc2a4U7GqiOiJqWHz-TocgH91Aq0-SLo3RJa6AgNI3hJSgaQDuKO7e58wxlmncerNgwr7oF6uSxOr_Oqy1rG9UHApN_CdDu4BgHH6Z1TfZF3hz7aS50eEwc2VMXh709I98LnCbEIEiNiRjCtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون وقوع سیلاب شدید در شهرستان راز خراسان شمالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/144418" target="_blank">📅 17:51 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
