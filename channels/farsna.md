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
<img src="https://cdn4.telesco.pe/file/tYkMKLnoeTD2sPHGSgQ6IzpU7WrzTjRsZouFsViv-qLAO_q4Yd3MWP3mX4WBY2S-u1PYwIBHtuIs57s4vpttsRQ_p55LLkcXXJEh2LXuQFwKJxLgd4D2YFpZSwOyezPAz7ZLvIC-Ug7_KqlowaGCYQ0cXLCbwaM8Jo_4yMBYGNY-htPE0raHtx4U3U6MjpryskmfFcfDnBZVjehMoGYJtZ7S2jvocnj-oU9PqT2iVYq9OpKR8ncVee9kcqa7J1WUWO0hKPKiODRdL_XP7rb4xiXEexytWUzMlBnzDMn-CNhmreCyJbsx5yzD5yMN158ChXBIE7_0t6OK7MerRGsznQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 11:50:28</div>
<hr>

<div class="tg-post" id="msg-461974">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b699798088.mp4?token=HdhBOewiktUy6hhGZ4_v2-CQuHNnIjN2rXtKBihwiMIBvyCicNiQilBGo4XahtYZCqkpX-2FBYhwpeJEm8EN0_oOabGVmrxVEyR7gbzpFaPUIiV4DGceOcKplpgUTReMte-s5agP6NUQky0CxKT5w6TFMoNjzTsX3AN5VGP-uURN1RJlaYre5EAOXxzMiW0hpCGZoRTPHMqU7bfRBsp2HY7bdjTreH7pIsfwPOwfwlm9VY6-Lm0z0Z9lgR53ooG-XXVTqsh7SlYPmZssa8WrTOsLBco0WsiaJNvv2iXYL0a9aa-O1mAfer91GAHtxclcGo5ZJx6VrODZcYkdwYyvVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b699798088.mp4?token=HdhBOewiktUy6hhGZ4_v2-CQuHNnIjN2rXtKBihwiMIBvyCicNiQilBGo4XahtYZCqkpX-2FBYhwpeJEm8EN0_oOabGVmrxVEyR7gbzpFaPUIiV4DGceOcKplpgUTReMte-s5agP6NUQky0CxKT5w6TFMoNjzTsX3AN5VGP-uURN1RJlaYre5EAOXxzMiW0hpCGZoRTPHMqU7bfRBsp2HY7bdjTreH7pIsfwPOwfwlm9VY6-Lm0z0Z9lgR53ooG-XXVTqsh7SlYPmZssa8WrTOsLBco0WsiaJNvv2iXYL0a9aa-O1mAfer91GAHtxclcGo5ZJx6VrODZcYkdwYyvVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پزشکیان با خالد بن محمد بن زاید آل نهیان، ولیعهد امارات دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 683 · <a href="https://t.me/farsna/461974" target="_blank">📅 11:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461973">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b29b6427.mp4?token=miLciB337M1l9o96Hs9atpf37sMD1wYbelUWYyAv8HtfSUnduVXaO8IxmwPlPJPEswvB1f_fd2qiRPDh7Gn_tpocHCrpfAFhblaoGi-RAPVL238JUXrs7BcPON25QharlExhZ1C4I5ZOjDBW5iwbX12IQfaWOjjKdhZG1fW6b2WY-4Y_mscDCmux-YYonoLvc3cqKUXrvxfdpoWHPz_Y3gEcC7sbVt10zSf3c8ZF1_iwVePk19HPfOUH4F_POT_PDmY6LI2T0CCydhGpCFAiCOAES-TeI5vCzeK8hB9bxCFS4uCYSru7Vr0u4ZbrHqz3zqcFwTqU2R-fw8XBGcR7aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b29b6427.mp4?token=miLciB337M1l9o96Hs9atpf37sMD1wYbelUWYyAv8HtfSUnduVXaO8IxmwPlPJPEswvB1f_fd2qiRPDh7Gn_tpocHCrpfAFhblaoGi-RAPVL238JUXrs7BcPON25QharlExhZ1C4I5ZOjDBW5iwbX12IQfaWOjjKdhZG1fW6b2WY-4Y_mscDCmux-YYonoLvc3cqKUXrvxfdpoWHPz_Y3gEcC7sbVt10zSf3c8ZF1_iwVePk19HPfOUH4F_POT_PDmY6LI2T0CCydhGpCFAiCOAES-TeI5vCzeK8hB9bxCFS4uCYSru7Vr0u4ZbrHqz3zqcFwTqU2R-fw8XBGcR7aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: فلسفهٔ وجود ان‌پی‌تی زیر سؤال رفته و همین باعث صحبت دربارهٔ بازدارندگی هسته‌ای شده است.
@Farsna</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/farsna/461973" target="_blank">📅 11:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461972">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of8vHz8ebQ_M9QAkMF_8hUglAgHEn1O88NSs83SG35iOR9pARRbPdQCRcONBe1w_NCC0J1XPvL_EeAu1vS6Fs-hD41ufCfdbKe_anrqQc078E6E0UJ137jPrFrPm1BDStsY7gInKyhTjdT8DXeFnrsf0i69Mn6DHcQ6_SjQCU503oF9kbOHleWwnWecE7HHQCc-E7gLJmgscFh_ZcGMJKkXaUNd7ynFvAk8e1qktDRXYI0mca3PFXKXJvmPcKWS6DvCGmT7vWV8Smgb1EGW5Zf65S3rmyo5_JT9cETujgvhmUzi2rHF9aE93XiarQay4IQkiyRyJ6Gcpo-yYB_2AHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: با ده‌ها موشک و پهپاد، انبارهای هواپیما، رادارها، باندها و انبارهای مهمات را در پایگاه خمیس‌مشیط هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/farsna/461972" target="_blank">📅 11:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461971">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280a7022a.mp4?token=W8Xjd45_ztLosiXmOI8KeTOzRU7hCZj5qpXAPVQGj_VuQ0K43R8r2EbY0UbfdT6XAGpSY6B7bix96dqmXeqzSCkPeDLvyIlNFvv-XR42VYzXFwRk_YMeVZTt2oIm5_9sqeprtICMxZtV6C-Z63KIho-GND5wap7DZiOHtJAGTyx6mAZxVMc-IO_Fim0ilWl7W3PSz1WF6_WjTVAg4cRijz9SKE7CjoXwSTn0PZ6ILRglpCfY-Owy3Ll5OoP6lHrsNQ4_4Rf3pnf-BGX2VDdBlS7XAWKyyQVssfD46xokhJjcVEEe9Lol_d_sYBsT3vGIf9FFcAKDLYq_v20WhQDN0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280a7022a.mp4?token=W8Xjd45_ztLosiXmOI8KeTOzRU7hCZj5qpXAPVQGj_VuQ0K43R8r2EbY0UbfdT6XAGpSY6B7bix96dqmXeqzSCkPeDLvyIlNFvv-XR42VYzXFwRk_YMeVZTt2oIm5_9sqeprtICMxZtV6C-Z63KIho-GND5wap7DZiOHtJAGTyx6mAZxVMc-IO_Fim0ilWl7W3PSz1WF6_WjTVAg4cRijz9SKE7CjoXwSTn0PZ6ILRglpCfY-Owy3Ll5OoP6lHrsNQ4_4Rf3pnf-BGX2VDdBlS7XAWKyyQVssfD46xokhJjcVEEe9Lol_d_sYBsT3vGIf9FFcAKDLYq_v20WhQDN0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ لحظه‌شماری نخبگان ایرانی برای کالبدشکافی زیردریایی به دام‌افتادۀ آمریکایی
🔹
کارشناسان حوزۀ نظامی معتقدند غنیمت واقعی ایران از شکار زیردریایی هوشمند آمریکایی در دانشی است که از دل این سامانه استخراج خواهد شد، و آمریکایی‌ها باید نگران روزی باشند که فناوری…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/farsna/461971" target="_blank">📅 11:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461970">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a955b41d1b.mp4?token=rQ5q_kq_38vSD8KWKc3rdEJFDWfZU-EWAD7i4eWdNZjWMlA4crIrr9LjJwgIDG-q7tBn4w3Hiqq6jJbGGZMhwo2a945DywLNGQu4_exiz7-N1eIvtKLIvnMhZfzn2iHrfCBy1CVjkqZNiaipTg7Q4vHstXru7RfRzxmXcIt3KkMltFAD7X2ArnUAZtFtvXaa22lpqEq_p3MhUWmJU9IIqSBRWjG0UmmYQ7YQe-8dgoiV1ZfIDDHMNhZczXCePQ781lY-lbbgNQWFtFDFAVaFU7pZJ-qDMs5a5m-iYULBIJKClDGJ-2lRBHWyWIuMtleaDxxMwG-Y4YTLWJrDkU4ciA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a955b41d1b.mp4?token=rQ5q_kq_38vSD8KWKc3rdEJFDWfZU-EWAD7i4eWdNZjWMlA4crIrr9LjJwgIDG-q7tBn4w3Hiqq6jJbGGZMhwo2a945DywLNGQu4_exiz7-N1eIvtKLIvnMhZfzn2iHrfCBy1CVjkqZNiaipTg7Q4vHstXru7RfRzxmXcIt3KkMltFAD7X2ArnUAZtFtvXaa22lpqEq_p3MhUWmJU9IIqSBRWjG0UmmYQ7YQe-8dgoiV1ZfIDDHMNhZczXCePQ781lY-lbbgNQWFtFDFAVaFU7pZJ-qDMs5a5m-iYULBIJKClDGJ-2lRBHWyWIuMtleaDxxMwG-Y4YTLWJrDkU4ciA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلومبرگ: آمریکا مانع شرکت اسلامی در نشست آژانس شد
🔹
به‌گزارش رسانه آمریکایی، دولت ترامپ با اعمال فشار، از سخنرانی رئیس سازمان انرژی اتمی ایران محمد اسلامی در کنفرانس عمومی آژانس که قرار بود امروز انجام شود، جلوگیری کرده است.
🔹
طبق این گزارش، به نقل از یک مقام…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/farsna/461970" target="_blank">📅 11:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461969">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f17bf073a.mp4?token=Pn0pRB-qC8LPrUnnf0yHq5zv37IvTECNKhSeqvUxssrEIlK-2Fiil2gbpgHpvcmiQ2KA8QFktznsO8ZSGtAte0Dqm3a2SytLjF_KlPFdUYbguodxZAmbtAlOv_TW_7x4FbvBVdqOOIJFiXlH-n2ll0NxMwDwsaCN9wMfWQnYsILPWG_Ue9wbOL-47MtTsNb8nP8g9hvl5DazdZn-cgGsxEDvpcojoPspMrNorY27qI8R4luLFkcJhTdfEP3Qn7zcoPr6DTn_6yEqiv8HfmlVcj7djFhMqOH1gXpx2y_T-9KUTVYqtuUG5I9OIcajJOOuZgpR33lLN7RfLh2hoLdYZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f17bf073a.mp4?token=Pn0pRB-qC8LPrUnnf0yHq5zv37IvTECNKhSeqvUxssrEIlK-2Fiil2gbpgHpvcmiQ2KA8QFktznsO8ZSGtAte0Dqm3a2SytLjF_KlPFdUYbguodxZAmbtAlOv_TW_7x4FbvBVdqOOIJFiXlH-n2ll0NxMwDwsaCN9wMfWQnYsILPWG_Ue9wbOL-47MtTsNb8nP8g9hvl5DazdZn-cgGsxEDvpcojoPspMrNorY27qI8R4luLFkcJhTdfEP3Qn7zcoPr6DTn_6yEqiv8HfmlVcj7djFhMqOH1gXpx2y_T-9KUTVYqtuUG5I9OIcajJOOuZgpR33lLN7RfLh2hoLdYZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تأثیر قطعی پایهٔ یازدهم در کنکور ۱۴۰۶ پابرجاست
🔹
دبیر ستاد علم‌وفناوری شورای‌عالی انقلاب فرهنگی: درحال‌حاضر، تأثیر پایهٔ یازدهم برای کنکور سال ۱۴۰۶ قطعی است و شورا مصمم است مصوبهٔ موجود را تغییر ندهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/farsna/461969" target="_blank">📅 11:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461968">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجار کنترل‌شده در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/farsna/461968" target="_blank">📅 11:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461967">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbaa79b50.mp4?token=YgDuylvNMNcBgztZ9KFF5bZELZXTIbqk0nYM74X2EQNiDaDV-tjrarnYEHllhTDVWCKstgawix83UKCHcfrjTMvWc7y6xd8tcmIBPJQSvJC6KLR4VrbSfIdLv7ijBvCEdjbBgNcu2a5D7VdmxgyZ4H6lZ3JIDPhYIFVhi_gQ6LZ46UnAaBC7qQdDGDAwyVIKslSjvN4sfg4jmvwQmgfKTGj68sFfVdDSEprAd3rJDHzsYaR6k73d4GGsESWtamdOtqWMBZPLpXzET3yJn_TtSVdpaIH9e1qtaV10CjfS3BC1fTkm4JLPjMgvJNfETeWvQwYIALHIYux0mM0m7ZpnpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbaa79b50.mp4?token=YgDuylvNMNcBgztZ9KFF5bZELZXTIbqk0nYM74X2EQNiDaDV-tjrarnYEHllhTDVWCKstgawix83UKCHcfrjTMvWc7y6xd8tcmIBPJQSvJC6KLR4VrbSfIdLv7ijBvCEdjbBgNcu2a5D7VdmxgyZ4H6lZ3JIDPhYIFVhi_gQ6LZ46UnAaBC7qQdDGDAwyVIKslSjvN4sfg4jmvwQmgfKTGj68sFfVdDSEprAd3rJDHzsYaR6k73d4GGsESWtamdOtqWMBZPLpXzET3yJn_TtSVdpaIH9e1qtaV10CjfS3BC1fTkm4JLPjMgvJNfETeWvQwYIALHIYux0mM0m7ZpnpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مذاکرهٔ جدیدی با آژانس نداریم
🔹
صحبت‌هایی که دربارهٔ فعالیت‌های هسته‌ای در محل‌های جدید از جمله کوه کلنگ مطرح می‌شود، تحت‌تأثیر سیاست‌های برخی کشورهای عضو این آژانس است. @Farsna</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farsna/461967" target="_blank">📅 11:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461966">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18a153e034.mp4?token=I-ATwQywx0TkkuXKBw9Lq8h82fCepigKAZwfIVqbc33Z06gj_7x2g2Onij7QfANc1tcT70UWgPToUouX74X7yDLBe6gznfZy_o0CKhxdZGbMi6oOKsEyZu6kvHfrrDj-PuUMQACAhJE944PbmTK9SheiwbbgHByyLgrKWK4C63Z7aNSFBK0J7KbXUWC3DeYwm-G-Huu_nBl-3KcVaW_OCM6woOUzMfgRgILJLXyU4Vn4XUor1sP-C5_oIjFiPxvUjLHnJ8mFN4Im0npGg3JrCnj4mS7CpNXSRtXxtrNc1vaKRvUqKjbvV0OfOiGRNypb9omx8YfRO-DZLI7DVML-_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18a153e034.mp4?token=I-ATwQywx0TkkuXKBw9Lq8h82fCepigKAZwfIVqbc33Z06gj_7x2g2Onij7QfANc1tcT70UWgPToUouX74X7yDLBe6gznfZy_o0CKhxdZGbMi6oOKsEyZu6kvHfrrDj-PuUMQACAhJE944PbmTK9SheiwbbgHByyLgrKWK4C63Z7aNSFBK0J7KbXUWC3DeYwm-G-Huu_nBl-3KcVaW_OCM6woOUzMfgRgILJLXyU4Vn4XUor1sP-C5_oIjFiPxvUjLHnJ8mFN4Im0npGg3JrCnj4mS7CpNXSRtXxtrNc1vaKRvUqKjbvV0OfOiGRNypb9omx8YfRO-DZLI7DVML-_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ مدیرکل خلیج‌فارس وزارت خارجه: تعویق نشست تنگۀ هرمز به درخواست برخی کشورهای منطقه و تصمیم مشترک تهران و مسقط صورت گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/farsna/461966" target="_blank">📅 11:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461964">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liVNzrNZno55e8P_wcSTmjXxiGAebR7XANkxTXXzZC4w6hzraP_d8mURbe_vMdJXIErmNRBubFWcMSTLExxiAv8Q_WeMY7e8mll5o5J-uihOuazdxyV1aXuOZWZa6QcdrGjeWh0G6ZTpJRfMFP5holhtVCFj7d4vIbryHUrcaSuhiyo5uv643q6-pZ4OjPNJpz6dMgVBRg_D8iwO_pIpjOMXI6XmGuGqgi4N6x46fKFY7MXk-GyuSQvGF8lxTYNOwfaTuhQF6k1PyhK1XEJpZLvf85Gw2XA3-UIASwQPcUJdEcut9siZsBIPbhEIunEXruFMcNSK8xg8_oxZyF-I3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: آمریکا مانع شرکت اسلامی در نشست آژانس شد
🔹
به‌گزارش رسانه آمریکایی، دولت ترامپ با اعمال فشار، از سخنرانی رئیس سازمان انرژی اتمی ایران محمد اسلامی در کنفرانس عمومی آژانس که قرار بود امروز انجام شود، جلوگیری کرده است.
🔹
طبق این گزارش، به نقل از یک مقام آمریکایی، جلوگیری از ورود اسلامی به اتریش پس‌از آن صورت گرفت که درخواست معافیت او از تحریم‌ها که از سوی سازمان ملل مطرح شده بود و امکان ورود این مقام ایرانی به اتریش را فراهم می‌کرد، در پی فشار آمریکا رد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/461964" target="_blank">📅 10:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461963">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8Ksjyfk3YqP_clD071NoDnzEavHh2ZUFv5DVmxtTeTbyv20fkJJBIBdtJHMSoDtoIuUQlei52J4RF0X9AwtBFblknuAssV2NONWq_2tjY52d99jdotWLGEhdYE9eL75se5-KZMIXOwvRdqywP07YnOAPKviy7HUAVMXTqlM8Zl3l_9Ca8RFbdpR4UsbW7FcvBd49vZ-OEIBY6wXSvAqIRZtMGUmzQjXRR1mlySVKLb_VvLL0WnYHHfVgObnUcm96AuQ5CgcOFuSV9v6Jrg3HtHDqovnuUFNqCrdA2RkJXXzCr7RNc3JN94LMMrUpTa5BDOi75kUwzEhD4RSzGRpJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز ذخیره‌سازی مرغ تولید داخل از امروز
🔹
شرکت پشتیبانی امور دام کشور: درپی تصویب مجوز افزایش ذخایر راهبردی گوشت مرغ در ستاد تنظیم بازار کشور، این مجموعه از امروز فرآیند تأمین و ذخیره‌سازی مرغ تولید داخل را آغاز خواهد کرد.
🔹
براساس ضوابط تعیین‌شده، مرغ‌های با وزن ۱۲۰۰ تا ۱۸۰۰ گرم، به‌صورت منجمد و شیرینگ‌پک‌شده و با نرخ هر کیلوگرم ۳۳۵ هزار تومان، تحویل درِ سردخانه از تولیدکنندگان پذیرفته می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/461963" target="_blank">📅 10:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461962">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwz37Q69-dQUzx0faQFR1PqMqbpOf--m2JV3cP-L2UtTjXX8cG0gWplpFlrLJkcFz079KEgJWos4zOMpZvXhAGS_iC2x6ZnMqXfV-EPJmGMuPKTron16cR7Qdc9v8W2KAeKlKTbcGWMrcgZo-CWEBIZsshl8OkDQNwPY1uiYG787LW5weFhup1Mlf9YfQG3iHFX7X1-r_24BPCrIvruFhWzVyjx2dW7qFHFRck_8mIUcm8MA4ITRn5kDyDTNf0x9dV4s9OMYkOxQDi-NXvOa4noMXnZdnmKWhWpv1pTBg32M-ridbGAJI4NOGbH4Jn1U4kjy90HweRPRbjYg_lZGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت رسمی افزایش سرمایه بانک پارسیان به ۵۰ هزار میلیارد تومان
براین اساس، سرمایه ثبتی بانک از ۳۱ همت به ۵۰ همت افزایش و شاخص کفایت سرمایه بانک به رقم ۷.۲ ارتقا یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/461962" target="_blank">📅 10:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461961">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h65vnLP-L7CakynTv6TfjLqnU0aLatlgQPPYnoJ_Iiqfz1bzPfKI7TN__uwAuezbpVVnjSooINRSh0GVJQoRKjsim-EaSjYiXL5C8d0nXj2RPX5OZwvrv7OakP8ApOkMh_w-5xl6Nidzy00_6_ujX-bLJcjBZ3cfvCaPXq5WejaNDZq8MkkAlAicWisCoxLU8eUkuACeHyAH35p3tFfGYxLbkv9tFDd69v_a-oDJ1aOe74J6E8VxjYF1f6NtB3hNx4H2ETJcvjBekG47i4Rk3tVE7g7o84qxov85SyroIDap4OJ34-1Hne2d7-fINU77D5YoJWBKff-XOYc5FMofgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مهر تأیید اهالی بهارستان بر عملکرد بانک کشاورزی
🔹
بیش از ۱۰۰ نماینده مجلس بر نقش کلیدی بانک کشاورزی در امنیت غذایی کشور تأکید کردند
🔻
اهالی بهارستان طی یکسال گذشته با تأیید عملکرد بانک کشاورزی، تقویت این بانک را بخشی از سیاست کلان حمایت از تولید ملی و صیانت از امنیت غذایی دانستند؛ سیاستی که تحقق آن نیازمند افزایش منابع مالی، رفع موانع ساختاری و همکاری منسجم دولت، مجلس و سایر نهادهای مسئول است.
🔻
بیش از ۱۰۰ نماینده مجلس، با تأکید بر ضرورت افزایش سرمایه، تقویت منابع و رفع ناترازی بانک کشاورزی، این بانک را بازوی تخصصی تأمین مالی بخش کشاورزی، دام و طیور، صنایع غذایی و زنجیره‌های مرتبط با تولید می‌دانند.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/461961" target="_blank">📅 10:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461960">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/461960" target="_blank">📅 10:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461957">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6512c993a4.mp4?token=ATd1kRpZRxSRTbSsHcGeh1mjTEjguPT60Y0oTMyrbautkPrHkZSFwqBLt2C8aEX3kBn_ppKl_mzrVribTrGfNge6HYFFSGergk1qYuhiaWVm_rIqPi4QDnugJCp7u9M0Un0fZ3B2A6lEn32aQTBYOMPkqdWbTW4TMig2vM2Itv_62hXDlstx6hOmdc_sbpX1PsmaQupABp7dPE6ZEa54stiHcK38yw1WBwhTAb_z_pUuypXVBVEHXTEgJQD_aCgDt-8OCXSr0etHyVZhksVP-E0szS1raMRJinJS9zo_BgGSlTKO37G5GqOKv9FVIQC7wD9We1wPAmVOhABbxHVpHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6512c993a4.mp4?token=ATd1kRpZRxSRTbSsHcGeh1mjTEjguPT60Y0oTMyrbautkPrHkZSFwqBLt2C8aEX3kBn_ppKl_mzrVribTrGfNge6HYFFSGergk1qYuhiaWVm_rIqPi4QDnugJCp7u9M0Un0fZ3B2A6lEn32aQTBYOMPkqdWbTW4TMig2vM2Itv_62hXDlstx6hOmdc_sbpX1PsmaQupABp7dPE6ZEa54stiHcK38yw1WBwhTAb_z_pUuypXVBVEHXTEgJQD_aCgDt-8OCXSr0etHyVZhksVP-E0szS1raMRJinJS9zo_BgGSlTKO37G5GqOKv9FVIQC7wD9We1wPAmVOhABbxHVpHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پدافند ایران قفل F35 را شکست؛ هواپیمای آمریکایی مجبور به فرار شد
🔹
آمریکا پدافند ایران را هدف گرفت؛ اما با واکنشی غافلگیرکننده روبه‌رو شد.
🔹
تنها چند ساعت پس از حملۀ آمریکا به رادارها و سامانه‌های پدافندی، یک پهپاد ام‌کیو-۹ ریپر سرنگون شد و یک اف-۳۵ نیز پس از قفل تسلیحاتی، مأموریت خود را نیمه‌کاره رها کرد.
🔹
پرسش بزرگ برای آمریکا؛ چگونه شبکه‌ای که تنها چند ساعت پیش هدف حمله قرار گرفته بود، توانست یکی از پیشرفته‌ترین جنگنده‌های این کشور را رهگیری و از ادامه مأموریت بازدارد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/461957" target="_blank">📅 10:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461955">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjoRk3QzrhG_sPs8vllltx6N-4VqAbUjJtN3UyDuZqHxs9UfYNBom-pQfe1-ihSpRKUh3bDNh3Di84Dk068phayVbVpNR8uLgzMxrjzfdf4mz9L88e-JOGnUL7-M-ne9S4YE0g9qKmjdTi10ntbv7Qad--8odl6sZBn1zPZkw9iWWptXrLo8yqdr5TWDW05HlKEk3oSGUK-9PXFfJG-LAr6ID0ISxrDYtAbDHZckoggvIQBwiQpFFJObhOR75IEtWYg6BzyutMiCkRfIN6fDOJQzorR2igtE2-t4RZCvIOiBrSyF6SINWdjuD4_r32i2v7MuCvSc0gn8SREZ6Ns4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/461955" target="_blank">📅 09:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461950">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7eecd9a2c.mp4?token=iMgESKwkoVHLHwHwxCHVAWPJHKYwwnHVpz3ZMwKx-xYFD9zCCLPPC9IZ5S6zy45UDs8DSWXz2VImnPtQ-3pe2ZpWT1GjACw9Ec9erNNIMfCWtLyvkqABjz_e3vttpV3PGj7d5bJd0BWkbYa-dRtqsT1LYeYLL8DVp02osNfeK-4JNoA8VQOK1AxJ0ry4KwU4o9-W7C_4j5oyc6bLZhGQTkpjJweuLaj_7IvehpF1iEaY1TVGeWm79uE0C40DULOIC44CvHs7DLH16e2ZAtkg9p7sDNe63X2cK6bA2C7Ox0bn1SCKetPvpr_D_0Fw55DSO_7d71IogiWtxX2p4hKpAiSEGkx8aJaByohxPoo4yEsSrcwUA46lC-8xx3r0vUBs63Ptgs6EsYjisxzxl3IwFU64cXjZq_nYQtQVCkIcZBFrp9maW4wc6d5QDBhTPpCxr426elyCmebuae4CSwW2wQ_nhK0wq7A2lAD7GoPPzsXCsX4QZO7oyCuE04uGYS_fetuvr8FuHuUvuqXtEwfqZwe4WOvZdsGOyYMGylJ9qEsQEHn0mWlj2ZOk8ziSvKALLDPxG6e_wR5-V_GM-mppaWln6T9mbPd_zvzH9FMjRwMG8UJUgDlvVo6excBcl1d5kXy_MFOcBnjPqyVGTO3SFyZVVWq_4rI-nM6u746OUjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7eecd9a2c.mp4?token=iMgESKwkoVHLHwHwxCHVAWPJHKYwwnHVpz3ZMwKx-xYFD9zCCLPPC9IZ5S6zy45UDs8DSWXz2VImnPtQ-3pe2ZpWT1GjACw9Ec9erNNIMfCWtLyvkqABjz_e3vttpV3PGj7d5bJd0BWkbYa-dRtqsT1LYeYLL8DVp02osNfeK-4JNoA8VQOK1AxJ0ry4KwU4o9-W7C_4j5oyc6bLZhGQTkpjJweuLaj_7IvehpF1iEaY1TVGeWm79uE0C40DULOIC44CvHs7DLH16e2ZAtkg9p7sDNe63X2cK6bA2C7Ox0bn1SCKetPvpr_D_0Fw55DSO_7d71IogiWtxX2p4hKpAiSEGkx8aJaByohxPoo4yEsSrcwUA46lC-8xx3r0vUBs63Ptgs6EsYjisxzxl3IwFU64cXjZq_nYQtQVCkIcZBFrp9maW4wc6d5QDBhTPpCxr426elyCmebuae4CSwW2wQ_nhK0wq7A2lAD7GoPPzsXCsX4QZO7oyCuE04uGYS_fetuvr8FuHuUvuqXtEwfqZwe4WOvZdsGOyYMGylJ9qEsQEHn0mWlj2ZOk8ziSvKALLDPxG6e_wR5-V_GM-mppaWln6T9mbPd_zvzH9FMjRwMG8UJUgDlvVo6excBcl1d5kXy_MFOcBnjPqyVGTO3SFyZVVWq_4rI-nM6u746OUjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از خسارت‌های واردشده به عربستان در پی حملات ارتش یمن
🔹
تصاویر ماهواره‌ای جدید منتشرشده از خسارات گسترده به چندین تأسیسات نفتی و نظامی عربستان در پی حملات ارتش یمن حکایت دارد.
🔹
براساس این تصاویر، ایستگاه پمپاژ خط لوله انتقال نفت شرق-غرب عربستان به‌شدت آسیب دیده و آثار گسترده آتش‌سوزی در بخش‌های مختلف این مجموعه قابل مشاهده است.
🔹
تصاویر مربوط به دیروز همچنین دو لکهٔ سوختگی احتمالی را در یک محوطهٔ نظامی در شهر «شروره» در جنوب عربستان نشان می‌دهد؛ منطقه‌ای که به گزارش پایگاه تحلیل تصاویر ماهواره‌ای «سور اطلس»، برای استقرار نفربرهای زرهی و خودروهای نظامی استفاده می‌شود. در فرودگاه شروره نیز آثار اصابت احتمالی به یک انبار مشاهده شده است.
🔹
همچنین تصاویر ماهواره‌ای سنتینل-۲، انهدام کامل دست‌کم ۶ مخزن ذخیره سوخت و آسیب‌دیدن چند مخزن دیگر را نشان می‌دهد.
🔹
تصاویر ماهواره‌ای از پایگاه هوایی ملک فهد در طائف هم از آسیب‌دیدن یک آشیانه هواپیما حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/461950" target="_blank">📅 09:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461949">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e53cc7089d.mp4?token=UVpo-jbmPurzPtyXfd6gXAkOgQNOaAHGcQwmMSfR2ZtXX_enxa2IH-hZL8m0Yo9oFBNx9I3l7tPaCOPyxGPAMtlNN_Jn2ESR6yYk1GdHmEGrm9qfEQzjvGlIUC-ib9Lg6r23Bwx_9040RoZKegUkKdIAiVFDO4ifqkMgjxgESvVPXq-ZTpWT0GmhzSt2O87UolMy0DFvlsNMyAhnGSfrvKfSJwUPOrw3VA6NsGjlG7PIBzzabzLvt5U2SLG2mlb_tm57OGFUOodX22bPKyDpoG3M686HVtawUNbozD6omB3jdKr8CEgWlI321x62S8f8ZM3KIfS7h41bccGI4IQV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e53cc7089d.mp4?token=UVpo-jbmPurzPtyXfd6gXAkOgQNOaAHGcQwmMSfR2ZtXX_enxa2IH-hZL8m0Yo9oFBNx9I3l7tPaCOPyxGPAMtlNN_Jn2ESR6yYk1GdHmEGrm9qfEQzjvGlIUC-ib9Lg6r23Bwx_9040RoZKegUkKdIAiVFDO4ifqkMgjxgESvVPXq-ZTpWT0GmhzSt2O87UolMy0DFvlsNMyAhnGSfrvKfSJwUPOrw3VA6NsGjlG7PIBzzabzLvt5U2SLG2mlb_tm57OGFUOodX22bPKyDpoG3M686HVtawUNbozD6omB3jdKr8CEgWlI321x62S8f8ZM3KIfS7h41bccGI4IQV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ مرزهای عراق باز شدند
🔹
براساس اعلام نهاد اطلاع‌رسانی امنیتی عراق، تردد مسافران و تجارت در مرزهای الشیب(چذابه)، شلمچه و مندلی(سومار) از ساعت ۶ امروز از سر گرفته شده است.
🔸
عراق به‌دلیل آنچه «ساماندهی اداری و امنیتی» توصیف شده بود، این مرزها را از روز جمعه…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/461949" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461948">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLXbvX1z-Dyn3k5MS_LXcVhxksj5_muSq5Klm3EdD1OAcQkMK1tpl5EwxhTUgv1CS2dOIt36_0hO9mbBB0FHLR2vHp_QrjmhNXKl18rkOnYjOEPPGKj8TXa-7RTjUNwRhnAdUPl-WnltUFpbkqybu2rmGrAIU5IehSzQs_hgiL8GxSiAlcONvIhiCK_xQPQ8S2WBQg2iBAjF8Td8VjbS9aH9SSxCVKlOZNV5vyfFJVR2jIGheKapiwoULntLuQTGV9bnCekNYewXwlmrfkMeTMMkvwRVgS0JmekWQGNYfmZizjANtDJ1UZxIpeYZFgpp0LbEN4ZeJ5mepGvc-NKSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک فروند پهپاد پیشرفتۀ MQ۱
🔹
روابط عمومی سپاه: لحظاتی قبل یک فروند پهپاد پیشرفته MQ۱ توسط سامانۀ نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور بر فراز آسمان تنگه هرمز رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/461948" target="_blank">📅 09:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461947">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌ چراغ سبز سعودی‌ها به افزایش سهمیۀ حج ایران
🔹
معاون سازمان حج‌وزیارت: برای افزایش سهمیۀ حجاج ایرانی در سال ۱۴۰۶ با سعودی‌ها مذاکره کرده‌ایم که چراغ سبز نشان دادند.
🔸
ایران در حج گذشته سهمیه ۸۵ هزار نفری داشت، اما به‌دلیل جنگ رمضان و مشکلات انتقال ارز، حدود…</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/461947" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461946">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎥
ویدیویی دیگر از انفجار در ارتفاعات علی‌الطاهر لبنان
🔸
شبکۀ ۱۲ رژیم صهیونیستی: بیش از ۱۱۰۰ تُن مواد منفجره برای انفجار تونل‌های ارتفاعات «علی‌الطاهر» استفاده شده است. @Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/461946" target="_blank">📅 08:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461939">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPNW-WDhfwrgAitcutS-dfbCteBTi3nFDSckyidwfx-pUBTHTUkgb93EYMxOUZbTnD0tkttAZilNkdbRHkRVFvRdOvwIAbAO56bw3wfiXeQVydDV9QMSGXCLSL0AN2vTcPYlIGreQkEJ5MVUWJM9fUYwAcGzEJsJC95mQ67U0ceG1xwMqIMCtr2eYNCAZCUIEoAmP_8nsgKJEo6vz74Y769J7UFocuG0Y84aBA_VUu8OSGUso1KUrRMB6NoVt_LqEAn1m3NQsk-_VeeC8JXm5oTeMKs7a3_N3WxV1S1rBBN7iEHwm0MH0JrX3vyuzPGl-OXotk8SYKc6ohJUVLstKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnDHpqP_cxJd_Xxwr4rm7D5Vjn5zIzABDiA-dD_S_shBkdExZhT-_6h3OeAR9QjgZIAsc1N9_aG4Y6ALJJqQEErZ7G-Xv7lH85maKHwFvj3gqj9wslNOhB5fmU4W3lgpPZa6b8i5rOCGrSos3Dvjkq-svNA9z1wtnmeqaoybJnBODWt0slcHW1fj5Ee8Tb8Y1ZOlXTtCGdniYhc0w76EqljPniaRUYwsGR33MkGn1zsRSTxIvaj2T-9LTy5UYnjOZyxgSM7Cjfmh0v6iwf7ZXbO6tCiN2rcBTXR49-ykNojJvM7EHV526TEqibD9GxWntY_tEVuAcnX_WRDPbmi77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlcvRB5I5RRgQrb9KTCo22esLeb7TPBQhgjhpAPRx8iCVYKp68CG9ryl6pLlrbDpUMLAg4kjHj43bJeQDn-hJxpJVW2kLtimYqo7w-XR7sDLb4QsS7b7NEZulXZtL95byIBKysSMAp6j-SU2xlquHC-Ha2uGMXgMYwCoigwUNIeUMpJE0tUQTzpd6wKXuBjccRKdNSD8I1sSP7ZXazwTjO9cCbdLqdC1Gb_LndhaOkBITgu3l9Vkt3BPpurnsopU__wRasKWCc8V0Wgk0YBM5rJlrCa-_Ue_i1NTZf185SPzxN9EdHC1af_0DBObgyxXwcnG4C0G4YgOOQLc1T0pFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uy6jTxY90PA7dpvMaKv3CSJqYFgvvf1c8bRUhbUUksQTHoRFwaySTwdDHEXQ7Z-BYq8hj_lmG8YKatAxn-FWsy9fJv-8eCwIwhFiuP8H18_pzxEfn2nQ7JcskM_VfyQFnrDNeBt8HbELZTWM3_PXToG6MrVZAPj_89YMiKxWmvsryuhJE4faiZC0xLDZ7HwqbICDXCuvz3_mFEocqeLCypkAA6g1fWsieE_DpauMlB9Eh64NdypqFaJ6hSea3JOReT66bpqVbM2Id2YboiHgIrq2lAHrXdnXnFh8VSRcHTWWyP_LD6iyliz3dV1Xyk4sRfrVovXr-Wg9E_6jiFSFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fa9c6cLxaRAZin1JqGTPf7KJ0auk0H0yr5J-v-hZfwuYGoPmIXqre4BZDrfgINgxRO5Br-5nd94ucsIKJEi5tujootP4VKOMKe0TOfs_Dhxb-WonT8yv8MTSjDIYBqc6WnRmvdmbnb019U9EKMu1ygYN9ib8QlZoDAIrhYQkdgBZxuR_6iLFUJU46y6ZmR6W4og-SXo9XzSWQ8PGWtbe7tpE8ZoVLBdlkuG1pVLwhqAIQvCDcclgsBUQm-ccItEn31gW9ktvXqYH_rrbQJW_swHmuyVqTL7mslG8kf9RtB6UjNOg53fmosalDH2qgXLjYghrFwoJWLWg_oTbYQOpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVB34Zn6yupmDRS69LCwDbjtf5DApV0E_im7014yE9XCs0tgpPAkSSqHnvAPG35-FEwjKIC-QWZPCB-ljVgiS6ZtD3-jnYA4m9fsI6FG0zHTheAbOnxO-unIt3RTnD1el0PoasIrLAPTqPFlC27GyCoaARuPW3ksiYOT6REXBKm5QQ4Zdv0YVDj7rnPWKkIAT5gu87EjqIH1U_QD746MasbPfFn-3s86XZ2ISLP7q3-fAQ7_Y7G0BkTGU2LxdcmalXwopy4XEEA1LTFyYHw2XUchmiCfPtRfLroMYrc_UmyJkR-0LpbVzaAcQEWQMoAndCN63sYlgiTcR9luF2hl6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptkq4m1-4YLTygap5gP2ZoL4NP31BCojIENYlLFBdWo7Wh65SqBNMNiLjaOK4OXwT586a9SEx6kOGoYPJEPqIftR8aMb06lPzy8ravqiFlZnTr2H6MNtb9Edmf19mshzO1n4Qh4UGuFdsZ7-rI9ZveDO32ynZukIkW6R8Tx0Gh26T4qtW5ejQv2FBbgQjxAJTe_f0DkN266s6Y-URTRpo2PmpVl9S413gmezHNnmxCG_bjrAjjbPDsYWXAIcjANN0LDCZORxIIruPr5OfP17RsW6enJpoTT_kwSxqaeiZy-cWQTvvKJDTTGGEt0CHSe2O0p5AVdg0QjC3M_s2DrkVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جاذبه‌های تاریخی جلفا در منطقۀ ارس
🔹
کلیسای سنت‌استپانوس و کلیسای چوپان، آبشار آسیاب خرابه، رود ارس، پل تاریخی ضیاءالملک ، پل آهنی ارس، مزار شهدای ۱۳۲۰ مجموعه‌ای از جاذبه‌های طبیعی و تاریخی جلفا است.
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/461939" target="_blank">📅 08:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461938">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قوۀ قضائیه: توقیف ۲۴۰ مورد از اموال خائنان به وطن به نفع حقوق عامه و مردم
🔹
مرکز رسانۀ قوۀ قضائیه: در ماه‌های گذشته با دستور قضایی اموال تعداد زیادی از خائنین به وطن و مردم که از عناصر وابسته به رژیم صهیونیستی و کشورهای متخاصم هستند، در راستای حفظ حقوق عامه و اجرای قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونسیتی علیه امنیت و منافع ملی به نفع مردم شناسایی و توقیف شده است.
🔹
این افراد در همکاری با دولت‌های متخاصم موجبات ایجاد خسارات گسترده‌ای به زیرساخت‌ها و مکان‌های عمومی نظیر مدارس، دانشگاه‌ها، مراکز تحقیقاتی، مراکز صنعتی و... را فراهم کرده‌اند.
🔹
قوۀ قضاییه با جدیت به پروندۀ وطن‌فروشان، خائنین و افرادی که به کشور آسیب رسانده‌اند، رسیدگی کرده و طبق گفتۀ سخنگوی قوۀقضاییه در این خصوص پرونده‌های متعددی تشکیل شده و در برخی پرونده‌ها کیفرخواست صادر شده، حکم صادر شده و پرونده‌ها به نتیجه رسیده است. اموالی نیز توقیف شده، تضمین‌هایی اخذ شده و اقدامات دیگری نیز صورت گرفته است.
🔹
به گفتۀ سخنگوی عدلیه برخی پرونده‌ها همچنان در حال رسیدگی هستند و پرونده‌های جدیدی نیز در این زمینه تشکیل می‌شود؛ این اموال متعلق به ملت ایران است و قوۀقضاییه پیگیری خواهد کرد تا این اموال در جهت جبران خسارت بزه‌دیدگان مورد استفاده قرار گیرد.
🔹
بر همین اساس با اقدامات قضایی تا کنون ۱۴۳ مورد از اموال و املاک خائنان به وطن که اقدامات تبلیغی یا عملی علیه کشور وبه نفع دولت‌های متخاصم داشته‌اند در تهران توقیف شده است.
🔹
همچنین ده‌ها مورد از توقیف اموال وطن‌فروشان و مسدودسازی حساب‌های بانکی در کل کشور صورت گرفته که در مجموع با اقدامات قضایی ۲۴۰ مورد از اموال وطن فروشان و خائنین به کشور با دستور قضایی توقیف شده است.
🔹
در بخش دیگری از این اقدامات، ۱۸۲ حساب بانکی متعلق به این افراد در بانک‌های کشور مسدود شده است. همچنین بیش از ۲ هزار استعلام نیز از بانک مرکزی در رابطه حساب‌های متهمان گرفته شده است که در حال پیگیری است.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/461938" target="_blank">📅 08:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461937">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a27685e8.mp4?token=oPPgXgGSsg8Wx1g6r7LnFroJuUfu3lFrXYRdmF1LAKkqVaUUoL2UUHi2w3S6bz3z2-WWTw7PCmMFXHnUetX3UE_JrBW5N8NET7ibBCZUykOsi8puTSVD4OGqv-IMEVUkx6Zh647hctmu6riHwLogkbCPe1D16pN0ilsr8aVdwq13FYqZKN-1bzGMIXeLy4B6HHOFgvwkElXCRcbvIHjZhmuCxyMZmy6nDWeUADEmQre5fnNWeVTtOsv36BHixt2COOhYkAzaJKsyhK-A0C5DQN64eE2Ii9oE-lRRQ-ZrrsnDOdi3dffgB_VEbmdeTlXHL2tnUNNMePA0k-mns1DDpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a27685e8.mp4?token=oPPgXgGSsg8Wx1g6r7LnFroJuUfu3lFrXYRdmF1LAKkqVaUUoL2UUHi2w3S6bz3z2-WWTw7PCmMFXHnUetX3UE_JrBW5N8NET7ibBCZUykOsi8puTSVD4OGqv-IMEVUkx6Zh647hctmu6riHwLogkbCPe1D16pN0ilsr8aVdwq13FYqZKN-1bzGMIXeLy4B6HHOFgvwkElXCRcbvIHjZhmuCxyMZmy6nDWeUADEmQre5fnNWeVTtOsv36BHixt2COOhYkAzaJKsyhK-A0C5DQN64eE2Ii9oE-lRRQ-ZrrsnDOdi3dffgB_VEbmdeTlXHL2tnUNNMePA0k-mns1DDpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ چشم به نفت ایران دوخت؛ «مثل ونزوئلا»!
🔹
رئیس‌جمهور آمریکا در طرح توهمات جدید خود، صراحتاً از تلاش واشنگتن برای تصرف نفت ایران پس از پایان جنگ، آن‌هم به همان شیوه‌ای که در ونزوئلا عمل کرده، سخن گفت.
🔹
ترامپ در جریان سفر به ایرلند و هنگام حضور در مسابقات گلف آزاد ایرلند، در پاسخ به پرسشی درباره اینکه آیا آمریکا پس از جنگ ایران را ترک خواهد کرد، گفت واشنگتن در نهایت ایران را ترک می‌کند، مگر اینکه تصمیم بگیرد در این کشور بماند و «مثل ونزوئلا نفت را نگه دارد».
🔸
اظهارات ترامپ در شرایطی مطرح شده که ادامۀ جنگ با ایران، بازارهای انرژی را با اختلال مواجه کرده است. قیمت نفت از ۱۰۰ دلار در هر بشکه عبور کرده و قیمت گازوئیل در آمریکا نیز به رکورد بیش از ۶.۲۰ دلار در هر گالن رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/461937" target="_blank">📅 07:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461936">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5zRfJ7pG9UlFTK-1plAwW0HlSI-WSJGZ9x5LovCQ-tpQhjtT3l_6GhguRPYeT1D0X2BagBujpX019mrnMHuDBP1HrA40ecPtpi0gWo4wASrl21z0I7xHxhAhoRBush9shvHxyPCrpSX0fxrr2g7Dh-eVAkC1x49CMMmQRPEUQJBI4E1jNhf70kSmVX21Qo3Uoog8pYEtdBqJXcFi1WRIQmUgKeP6_ks-H1aebiJULr-k3P0RThUfLStVRepSono7VC6r9iw3nfMCpiCR6RlLaAfk_o2axXoEOHAIlAJRZ8I8b6A9d4i9Fyn7E5LdX-Wv65Y4uJAfxQvbxG-AGkm0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازنشستگان تأمین اجتماعی چشم‌انتظار معوقات اردیبهشت
🔹
با پایان پرداخت معوقات فروردین‌ماه، حالا مطالبۀ اصلی میلیون‌ها بازنشسته، تعیین‌تکلیف و پرداخت معوقات اردیبهشت است؛ موضوعی که در پویش‌های «فارس من» نیز بازتاب داشته است.
🔸
بازنشستگان خواستار اعلام زمان دقیق واریز و پرداخت مابه‌التفاوت افزایش حقوق و متناسب‌سازی هستند.
🔹
معوقات فروردین پس از چندبار تغییر زمان‌بندی، از ۹ شهریور پرداخت شد و تأمین اجتماعی از تکمیل واریز برای حدود ۵ میلیون و ۳۰۰ هزار نفر خبر داد.
🔹
حالا سؤال بازنشستگان روشن است: معوقات اردیبهشت چه زمانی پرداخت می‌شود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/461936" target="_blank">📅 07:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461935">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هوای «قابل‌قبول» در پایتخت
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۸، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/461935" target="_blank">📅 07:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461934">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-text">🎥
معنای اصلی مومن چیست و چقدر به آن نزدیک هستیم؟
🎙
آیت‌الله جوادی آملی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/461934" target="_blank">📅 06:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461933">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b19dfeff.mp4?token=bZjGpFhisj44-u40Kf6OsPK4Y_JYZwC7X8SaXFgHd7imNaeLnCPT50LEljmEruVR9KYj0ZxdI9FiGVdMzH_ZuJji7PQQiywL-gWT1pa8w5RKNRf17k0uzfxppAAVUhBq3UiuvV_j3ZHseJkN_SCg-BvzBuzqtJOLJPmk5xHxwPEMA7ItsRkW5uV2wCwQLrev9ESp880oRJfL6bwm_K3e9VgW1JYnOcsf3UTIRoPF3H5MZAxhDYTvNMvW9UhYxP53h7im6xg2YZoJIgm4rc9zy2m-arnyYUvt0XU70VEzP9B4Y_r0Vmd0d-DdlVsES6K1wwauGu_yiLU8rKD3uuAurw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b19dfeff.mp4?token=bZjGpFhisj44-u40Kf6OsPK4Y_JYZwC7X8SaXFgHd7imNaeLnCPT50LEljmEruVR9KYj0ZxdI9FiGVdMzH_ZuJji7PQQiywL-gWT1pa8w5RKNRf17k0uzfxppAAVUhBq3UiuvV_j3ZHseJkN_SCg-BvzBuzqtJOLJPmk5xHxwPEMA7ItsRkW5uV2wCwQLrev9ESp880oRJfL6bwm_K3e9VgW1JYnOcsf3UTIRoPF3H5MZAxhDYTvNMvW9UhYxP53h7im6xg2YZoJIgm4rc9zy2m-arnyYUvt0XU70VEzP9B4Y_r0Vmd0d-DdlVsES6K1wwauGu_yiLU8rKD3uuAurw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارهای پیاپی در مقرهای گروه‌های تجزیه‌طلب کُرد در شمال عراق
🔹
شبکه المیادین به نقل از خبرنگار خود در عراق گزارش داد که صدای انفجار در مناطق حلبچه، شهرزور و زرگویزه در جنوب سلیمانیه در اقلیم کردستان عراق شنیده شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461933" target="_blank">📅 04:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461932">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">منابع عراقی از وقوع حمله به مقر تجزیه‌طلبان تروریست در سلیمانیۀ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461932" target="_blank">📅 04:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpGTnqspprJci0bAO2Zl9I0Xvdgmsdw6vOyK13nmYXudldTBmQJdvb_zjJFazzvy5BV2F33wK-z7m8L32XcbvBAmENzOEA5XcDPa-4TeQ33WcNiFE5eNyI4yl_uyDrUnPTsf2LYqLMK3QAWY-gmJRQ1RyoVuen2iz3yiuQIZDjhupupOEtCTV2hh-SDydh2suv0UT1QwsDLKsZRBIp8eyrrXzNGe5hQpUCEPiJETiyCX6ktOX3XuY_aHKNd_YXgek-JwThETrGoLBXwrdcpJ9nUfBAaqPl4Gxnayh10GgEgz5fILHYCfwASoC2OrWIuDQ1cauqNnPIzkZOKi_xzhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزمایش کروز و بالستیک، پاسخ کرۀشمالی به رزمایش آمریکا در منطقه
🔹
خبرگزاری رسمی کرۀشمالی از رزمایش ارتش این کشور با استفاده از موشکهای کروز و بالستیک یک روز بعد از پایان رزمایش مشترک آمریکا با ژاپن و کره جنوبی خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461931" target="_blank">📅 04:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دفاع مدنی عربستان سعودی برای خمیس مشیط، نجران، جزان و ابها هشدارهای اولیۀ خطر صادر کرد.   @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461930" target="_blank">📅 03:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gK4w2zBKlW__FRRio_t5QTShsx-eTwXkP8c278I6iFUxfsWSkgRzLc6NwuyZoiA6RgW_YbsGgvFFXa3n43lU1S2-xwtF6rtZVmev8zvk9FCKllIndah2__nSuIkxRnozeinyjaDS9AF3qHrRDhrhiWZsE1BAVfDmXZo7sfy82D-Gd3dpbKzBegqZ_p0nSH8AfoJSICC_sVvOL-Q9MAupfAkobGCPUcygi9Q9pyOMvpULIAlDGBPm3mIUDkBS4blfngra869PmrPFd6ijAjlXwVafM0q3GM83HgMDpMXBj2FXfKvXT_d-azDaZKcynadxd9tWZYDXt0UpY-XFfxhAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل غیبت رضا جباری روی نیمکت پرسپولیس
🔹
رضا جباری، مربی تیم فوتبال پرسپولیس، که با حضور مهدی تارتار به کادرفنی این تیم اضافه شد، با وجود انجام ۶ بازی در لیگ برتر هنوز موفق به نشستن روی نیمکت سرخپوشان نشده و مسابقات پرسپولیس را از روی سکوها تماشا می‌کند.
🔹
موضوعی که تبدیل به یکی از نکات قابل‌توجه در مورد کادر فنی جدید سرخپوشان شده است.
🔹
شنیده می‌شود تارتار در همان ابتدای حضورش در پرسپولیس تأکید داشته که ترکیب کادر فنی و مسئولیت اعضای آن بر اساس برنامه‌ریزی خودش تعیین شود و حضور یا عدم حضور مربیان روی نیمکت نیز در چارچوب تصمیمات فنی او انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461929" target="_blank">📅 03:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461928">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دفاع مدنی عربستان سعودی برای خمیس مشیط، نجران، جزان و ابها هشدارهای اولیۀ خطر صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461928" target="_blank">📅 03:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461927">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رویترز: قیمت معاملات آتی نفت خام برنت در پی حملات جدید به کشتی‌ها در تنگۀ هرمز، ۳ دلار افزایش یافت و به ۱۰۷ دلار رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461927" target="_blank">📅 02:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461926">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkkFgO3JSGjlXzrpGHdLggUStLwUQLoXf1z_TQvhQ-wv6wIwqnynNhYbVZutlCNQ7YieK4MrR8BRNJU_FMp2OyjW8GqQUQ5l0FxTVlyOo2n3ZCEy4APWutQlBiLtmMLHQHUt3McIkX5QlsHOe1rGm-fiJFdtNhosmqIMohpbhxyQyKhe2WoWQNSc7rWJ_1mMswy2bisa3vKv-ff6t4x4jXnlRRUrbk8Tp_iAznNifjEQcZOQoFR_-9v9-5t-ViHlajt59OoZ4OMIr0e9SUntnj2JCzWcFwNQUsoJZC1Au6mHz2F5nKH7ndbk2LDgf5FcjNdQ3DpL3Eyoj601F0pLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ینبع عربستان متروکه شد
🔹
بارگیری نفت از پایانۀ ینبع عربستان واقع در دریای سرخ صفر شد.
🔹
خط لولۀ ینبع یکی از خطوط دورزن تنگۀ هرمز است که مهم‌ترین سهم در عبور نفت حین جنگ ایران و آمریکا را برعهده داشت.
🔸
روز گذشته انصارالله یمن به خط لولۀ تغذیۀ پایانۀ ینبع…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/461926" target="_blank">📅 02:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461925">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4UWzHsl0Q8rZoRFLrt0K9FTAjFOmq1fw06WaYxZvI8satW_gZ1Yiu9Td4YaBxyjoF4kxVYTTsUrmNcou4N8Ieh5ddtkEuPzRPXHRAadtI-VxA4w0EUx1Qdy7xogy6sRoksv0ninLP0ctJ9JXUGmmJ4HQO1IBRl9blTx3luBU8WvEVPLvHtNWa-3e03RACQ5cQ47JShCRjwN6YPwzx7t1c_FJtOkQkjpm6sWPpNHHw9suqNCSNbZSiFAmAX4bQcL6ez2qdAaFjphAf_N6UT8VXIeS86nh2Wp3uCdbO7U8qaL9HNozSI1OZVmwC8URyMue0ZQOKEyHNPR8SLoMcyC2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودروی آبی‌خاکیِ شکارچی پهپاد
🔹
چین نمونه‌ای از خودروی آبی‌خاکی تیپ ۱۹ را به یک سلاح لیزری، حسگرهای جدید و توپ خودکار مجهز کرده است.
🔹
تصاویر منتشرشده نشان می‌دهند لیزر احتمالاً برای شناسایی و مقابله با پهپادهای کوچک در خط مقدم طراحی شده است.
🔹
این خودرو در صورت حفظ قابلیت آبی‌خاکی خود، می‌تواند هنگام عملیات ساحلی همراه نیروهای مکانیزه حرکت کرده و از آنها در برابر حملات پهپادی محافظت کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461925" target="_blank">📅 01:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461920">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG7QEON4UX7Mnb92Ac9i4CGQn5Bs4DIS6JhS6NV657FHM6BlraZy23Cq2FfBsLOF-02KLoXWdG2PWX5GPXXegleC8l5Z6k1a0xB6TI6zRqquZWpEJuJ7aJRlPPotLdhljJhw87j2H8Qg6gGU0jh4KFiOb3FwHS8ZkjITNQn5W-StrOrMnQnyIoOudiwE0lG_xRzkiBbQ2mOugbJHKaYsQ8q1OXc9wewmXuNcdyfUECzrY9Aqgv6rSSIFohFK20j3jDTqF6aSgqxtsb0kN9Wu2lAot_WObYbiJO-3NmrF1VOafNWJAdAwG4Nfsj3Qk_eMjVhK2wKdVY1SSlg7aWSHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEuCrKkQempUmZcLpm0HmBnrQf1YTB1Q6jLcCPXK3U0pwzdXpwivC0-1C0e-J1_UhkZpLkUBmNeCL04sRrJY50r7WzvyWVm_eaUxuzPF-jLtkimy3eiYPxth2HrWGJzWVjz1DbRPZkfnYnt_ycxo7m2h94tQEA7qR_-_2jcPq52_Ro-d59FoEQCCXgGXkrqL8lH1k92hZlh8o8JrV3W5S0VveoJYeY2mPPByW4Bqb-AtsCj9eGCycdgMu3pbBsfi3mn5c8Y7LqoRIymadIHG3mqiiU8XomYCvEhCGv9NZt1i0UPHlAamuur5DTPM71s5Q2aTnGh8TuIYi2gi6O34sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXBjoCHwskTUXkv1rJhcy1xt8-IkqaDz6LSxmrAQTiU1t7W5IOx3c8w2U1hbiR6JV9UnZ6_7mImt6O5xPUga5akW9gJ90YU260hlm8oxcL7RZhZ2EMPS4yKpQ4U_cWHReXaaWuLW3282JO3wfKvvOYPdrz8AMLB5DFmP_UtUiL1PKsAjAWv7efiKUdNT_hE5VHlddWZ6-jQTJ4XcgHMv9XT_E2T8lQTz2aR_hfDXKpt_2c8NGn0AhYLclIZYYQ01quVINWRJ832K4IQfCJmoeU0XBEa-vjdqIAOUDzOi4biCrkmedANMgvVy5pJ0D1JEc7dC3xvRVPw4IuhnZK5YYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hywOQ-A8w-tgGpRBkw9s1LwRoXoAGqhaE-sr_IC4Ay0yZMBs7XthGlYv8ePbclstqXnuzsRpYcMSd-bHpyNVN9rHCrwWawI7QIU9eWt5NqujUDZVuqoMZICfZDNxeU76X0m3rN5CTb_wDo8PxYo_3hk0ByaUjBeoqn6vwa2ij93pQtcd1JDlPcCo9hNnuItOlHfh5GfPF9gc-P5tv9iC_jbbXQDHzBUkjl5FtIWYEUfnM-d181QC5_x1BzlbfQZ3_eUWj4bipOn0jPQYujrE1AyH6_Gp6ZMgny7pfQ1qC8CmgVPbydqJY4XX6zOmTPwcyVImmZUhsaiqblwO9AtE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-nvzSEQZmrFCL4dKfKZ-ks6NGZgO2ZBPqPybPg20keF_Si4Y8nge6BUq_SZPSKEp1c-TyruuKv1M_De_z8Vayzm_OTB4_2xSOz0CnpGqZ_u-8AsS8QFByK0mRdcrBUpxAPV9gy6-8tzCqaQE5EOUHHazw4_nTIltpp4oDGWu0Z_3yyfu_bmgMDruhnfJJO63PmrFYeSscOxsNN5Ic5O7LOWLmpTM96YVDoftRVwuVslb6vdd9mXriNbEIVE8aGZsVueoJsTqS8N_FPiLy_8v4S5iNRwCIoHWxC3VQsQ7nt5EesvmwC_mYBpDxJXgO56Fxb8beeu2VVw9VMaTTPOyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۲۳ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461920" target="_blank">📅 01:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461910">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujxrbbNRcNDyaj9mD2-ZDOJ6qrFI0FdXsOZIfqoCDU5m2tO-oP6JTyvDRmZeSWJiyRgV5Hll_5YJkcsitbYyDjgVlj5BMzQTRO98jyeOh8Z6ygWfxH0Q3dtF9Lz72OjnoRyeJuVKDSK6t-Brx-UrvaL4bFzyhjiXsA2JuCKo5Y8gXCB-Z_jucomO0i8NGY3a0CzTBhIv1myX7U216FzwS4rgTuyi2PNMGmDu1-oiDhC2a_FIsui9gXmb5ONV16U1ThVn1ihzESlwAfGeho_M8i1UoVeEFEn3nc2kwF9_jdo5MXMK9jnJt0VA3p3Af8nH_MzOvbGLafOXcdwpqsjWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/setDM3IIa55JGVvXLOfVLh-YNKwg5CZp_UCdlL0I7Pn7R4ZjxG2pDsSh05aP3rC_mGR7eDgz59Y4M7E0Mr8bAARfg57EHurT1hy8DPZDkuXDJLOC3HRa3hJkkmPz32mS-BxQUYI9cVohikvXyOjDpUfyvGwpfEbkdJOoKTjSqn9Lqv1Q9a9pmwT1Lv_hm7iEh5Pay8nnTrrNfBbQO0riy7TcSrf6l2t9wLQkuFPgMBcNcJ6vbDHMDhuB8UVFNJ96xrRHaRDY3oS5fpXL6BrvKekaj2JduU5Dj5o2TCL3xvm49hdVyGNRXjskGGoa7HrOhiVShG3P1FI74nmS5KuyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCNJh5w1e43gV9WK-lCMcZWjQsheF-7amA8b9hG4vWUyTUEAEkQHwvHj87b7jybEb_On1v0VeNKeSQ4dgM8mLy7UjyXsklgvX6lLWRM0-tovmhOKagcD32QNM1xoiJ57nctGWn9ONqdk4sgvTr6Wi9WjuOXF930dnuyMhQnz_yhaZpuSIhR5wpJwNs2xQxbVf-qN0JTcjHKwiGxc8abDqirTMZPwDdbWcv2SPJA7kQfZtp6xD9d3b2g56Irre5ZwokZCvws_VNzeeXceRcJK9k-JfVVuf0cfZTUgoqVSr3ZrfP0eFy5cL0dsuecc-rwV0gj7XvPCBmxcgLoW3bITeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eV0evw1plHVKeKoPtGDYN_7XfxoxgvkseB8rleNN2IBF8NZwnjR6ldC11ZiH5x7lrPVRyEAq7Ym_6nE-YE8yUdeUDFgLY_D_fUnu_-DuBZHoyGJAAXhF8ywct5xZxT1TKJ_jJT9uUXIPLAAr51Zd6bYNZ1NtdecsING9xB_Fc-puFs4ovIgFk2p6UG0_0a3LKaP4-8xivr6SZlGx-YlWg8OKiytCaf7YbCWwt4bf4jRjVf_nNXUGGrSs_kNIG-jjM51NaBW_HisDPcGvMrsGccRnWqBog_MtMmgsgLDpQCzJCpfmRW-Df-piYIQSMV7tfszDf81S4cHt6NOGk75G8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VeZbUlG18M9IoSwehpTvcJBbn1kO7-Stz7f8G89_UE1BBTaGDW6oWJlCj0t-jKZz3sY8ANGOafTipDnhEDX_Boe9RPLGTlRcpkhstj8OScs9zoytxVOtPFHOuXrI9kP_KyjBnhFf-sNlqGUQh41I_kXNcfK0kwZyBhT8Jtx5_JLzuQmMI29-6Rb8B5vNwTijovouOp1FdwKJ9ibRXVQlcBad6K_KjcY5TYia4Z641vxWmn34E8Tl-FIDtVr8Q2hpMBRJQSh988M-GcxLL5Dxi4JUcNjP12_2eyouJ_6c9i5FI4tw0RwIxUPltNuCU6QqkUzkJD5p26SWitAkyTdW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaejtZm9uBQTOQcmp-4jPcp4k0onvwP-Kzzbv13xLze-fN9_WPFA6KQEYymoQVjfMYJNbR4AvcXq9PyABdScA5LAEQ5cTMkWSyRUZpaspmrva66h0w1dWGGEXhvph2Pb4pUtXxQ_Yl0MN4v_8mk0SsQt8jmZNu_1iqqrYp-ixG_XJdRfnTLFdndzRbabzysg_EGr1BKJx91CE-MbDrUB_V3UHss2UxqieXelNQAXSeJN-2SNQxWES6AncUSKayO8vBkDHFNNMOm5VeG9btqs2660evgCimVSlWWKWl6OyKk2nUu3_-KvqS_IMgIbl-CvaZBJQCbaXEkxH88osQGr6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WcI9tDI0XChP4cJhxVPDl6hdnXxL_Fv4h4wmEbJ5mxIAwk0W5xnc5Gf7Pn98-ilCH3E7sqGtoAZpkGsDTtZpw28umzAj54m5ohwT0m8CaW6xdPzWPgu5ZsX2mdgLPvfFFnCCV4nFxWBMU2U1iaSyBwooy3slJEHYfKgKuJc0SvST1PuFPF86fLaCEZmZmDbVhWqKUdbj8pSUiR2FP2VmG4pKJllC2uD6UdjmvjqgNDnDgJpKG3J1UQJ2q74zv-tsyI98neRKIzkT1_6EbOU_lTmgcU8DCVJOjXy1GM6Z7D6iwqocznJGbG0HTGd4KyoGQfNpvEQ-gTLpeaegh-TOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbtvDQ91v8i_GMmvtCnOloEX9OPoH6A0XFoWlZ2B-hcpGvqPG7NxB47lBf85OpDeWboYespeW-irR8qldtV3DfY4sMGrrHE0RB1xo0zy8bUzvTU0K-6Ky5HLzJigjyv_l3tGrrr3IjM-SDKe7QU-tAhwXcCN2XZoleVhQQjfbRn8qf-loNhcaSAA9c-3i0dGiVjgcj7ZN_QXnAYyHbm_G01qVKcpoLxkC596Q5h3WoH-e2vI0It9YZu1Y-C7E8TZBXyp-e3iVvg8Gce2iPfBYHR6MicH9FA1CzG9pEvJBfjUu3TIlvGS57UdoiLZVzStfsLCtR8rptlPXGincxRtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AAYNZovxdLcOo0XSyOEe02nShXxncSdQuBIIwAHxIcY0HEIoza67e40Ju5pHK2YqJvKu6VGij0_TJK5kBHWXIErKWr9k95uAOuBmtpjfpfaoNGB5MhvACnkD4KIruK6uNnI8wzdyU-xRuavQjUumjG-Vg8vbaxvh5LJINjpa7McqP6oUIFr0Y5MdKfHG2rlpcctC3TiBcOtmhyndj6VcYUKhjeuMRgT0pfFcCAMLKjexQKx2Ty4UkanzsZFxHF1TrorVYAGHDVChz1NAUNmEdyjOqedR4NhFtA5EWtopB0riZImqJs9dxxTobAkuPhL1OaNHEAGK2awp082vgdH1zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cpadd2IFNN7xLlLylblQKdAk5o4YQe-cIniZHL2nR3dEtIgpgVFvknOk7TLGeEPePOKIjCWoRssUdnYqLFxSS84KA5v7FjIlYLMduQbewx3IcUpm1EyW4v_TdsB4y8ExmN94yjYk01y0UiTC1HzYlR9DyI8k2n2kTlZBLnEHE-85n66y84SNFTfxMrSfCG3b3-yHMdAlt_oBiOwH0gjvAp_v7IQohBOpzXSvwpponymdZy4WnpeZel3R47v8qWmg4fd6kNxdDhjNrMV0YyaLgU2z69vUS493x09MYju7eekiZeLyI50r4EddePgA6FNV3OM_mNH_IizmOR-L6gxtkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461910" target="_blank">📅 01:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461909">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvDjCZFYKPhmqjF18RrHX4A6qFJeLEA0wRpiocDzF_qxLEIjIbWFFucA_HNiv97esqJDioUHX5WSxc6q79CKz2TzPsnIHiWtEunHiNxsqlgdEKDvb_HKXVpKJe8zu4clA51CUX5SYkXDuJCkJT6bQUsRNJC1ohQtj5aT8pa9e9eT_v7GqlDIB_CPQW_BxNIIa98CXW6ewWyax8vjNZ6I9CSxSy9JBZyvjTUMeM7vtsg-gseHCRWvD1lie1QCb88rmxpReJN8wxoLQys984kCZf7zo7ggbsiBKgnB2suD22Uslse6v0vnQ1lURnhpPOhOBTo6MDs0xeaahd-eeYCMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشارکت کانادا در وام ۹۰ میلیاردی به اوکراین از لج ترامپ
🔹
کانادا در حال مذاکره با اتحادیۀ اروپا برای مشارکت در وام ۹۰ میلیارد یورویی این اتحادیه به اوکراین است؛ اقدامی که در چارچوب تلاش‌های نخست‌وزیر کانادا، برای تقویت روابط با اروپا و کاهش وابستگی به آمریکا انجام می‌شود.
🔹
مارک کارنی، نخست‌وزیر کانادا قرار است هفتۀ جاری نیز در راستای تلاش‌های خود برای کاهش وابستگی به آمریکا با رهبران اروپایی دیدار کند.
🔹
این تحولات در حالی رخ می‌دهد که روابط کانادا و آمریکا، به‌ویژه در حوزۀ تجارت، با تنش روبه‌رو شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461909" target="_blank">📅 01:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461908">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjgViBfdcrnCGJF37R0lVXbVtz2WwtpnSBnn5DD5KMxBUHGSWf8W1nHJamn_86ny1eGXgzUTD9tHFmuSV_VjKuueoXEOoPWizcgrbS6BTMSkYv15bOHzYXOK-bPj1cFDTXUx6N5YK1cDFQtN30W4735dddxVWmM-eX7_syR-bPxh3LD2Vfj3pPTH8U13t5BrmnfWmrHe8gNdSRZ84gtj_wIx9ZoRODbI8OzVUweMe3J9hEiP3BW0qw3fNwuBYQ9trCp93_6sN6sbpwTvcwd82Rppz1OiRHHxFVVjwV_ZmiOikamoiW-L6Kn5NeIe-ZIzs4MvwwQLoHpJqgu0a3oZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۱۲ خبر خوب از ایران
🔸
از شکستن انحصار خارجی‌ها در نیروگاه‌های برق‌آبی به‌دست متخصصان کشورمان، تا بازگشت ۵۴ هزار دانش‌آموز بازمانده از تحصیل به چرخۀ آموزش @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461908" target="_blank">📅 00:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461907">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزیر آموزش‌وپرورش: مدارس دولتی حق دریافت پول از مردم را ندارند
🔹
هیچ مدرسۀ دولتی حق ندارد از مردم پول دریافت کند و برای ساماندهی این موضوع، اساسنامۀ جدیدی برای ادارۀ مدارس تدوین و در شورای‌عالی آموزش‌وپرورش تصویب شده است. @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461907" target="_blank">📅 00:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461906">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e5fa97ae.mp4?token=NS4fcZ35JTLe1Nl9gdJgnVzu6RnPaa66VNNNCd0TipUaq02Kd-iVsPgh1FH7zOUYc29sX2lOVC4otsdqlf2NEf5TqIDpdnzg0m1-ku9lUAxcQYLD4L0zfchBdIP8HrqWZ5xl5NF3pXTXqr4EpJhn_8zFXL5dPkGMv-e0P9_kFW21OErvb5zV1qCbkTN2pKkOaupvq5nThRiYud8UVlp81-q2Y3mXrt-d1xuDzJv5YRQxL-bDDIk6bK8YWI5xIvojZ9p0xK5R9V4fBFtggoXf3LC0bX-1xJfn_i1DPp4scNmbLh5YJLTYPKh1UxbNmkQo1drujizWQtFCJ2ueXyffiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e5fa97ae.mp4?token=NS4fcZ35JTLe1Nl9gdJgnVzu6RnPaa66VNNNCd0TipUaq02Kd-iVsPgh1FH7zOUYc29sX2lOVC4otsdqlf2NEf5TqIDpdnzg0m1-ku9lUAxcQYLD4L0zfchBdIP8HrqWZ5xl5NF3pXTXqr4EpJhn_8zFXL5dPkGMv-e0P9_kFW21OErvb5zV1qCbkTN2pKkOaupvq5nThRiYud8UVlp81-q2Y3mXrt-d1xuDzJv5YRQxL-bDDIk6bK8YWI5xIvojZ9p0xK5R9V4fBFtggoXf3LC0bX-1xJfn_i1DPp4scNmbLh5YJLTYPKh1UxbNmkQo1drujizWQtFCJ2ueXyffiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سپاه: ۱۱ جنگنده و بالگرد آمریکایی را روی زمین منهدم کردیم
🔹
سردار محبی: از ۱۷ تا ۳۱ تیر نیروهای مسلح ایران ۱۱ جنگنده و بالگرد آمریکایی را روی زمین و درحالی‌که در پایگاه‌های آمریکایی در منطقه مستقر بودند منهدم کردند.
🔹
همچنین ۱۷ پهپاد شناسایی و عملیاتی،…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/461906" target="_blank">📅 00:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461905">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da22e4ebd.mp4?token=meaonIS-VAp4SnN6Bp7ZqTUdeXRvE2OLCbupwR8w2pTdQqo86QW7dZRbJIrDsLloNhop5brzcs0ZWUCThOZHHZjpxmYLDwSkVHs5GtEjJ8Qj-HR4AvbTiA1vlsHUvGo3UjkYdZC8cBqbKBNzXOld4Zqk9zmu3yMstmOIeVlz-VoTeZp1nHhMidR-5qpKSdlzwimUVE6V2nvLw0MBw5ePIvMtgZN3AkGSS3R-KAsdRO0TctkVz3E2cH0w6sSB-73NCk85pC67SpSVCuHHMqU9Pb2QmcoZQKD0HO8L_aCh0a5IB8PqLH8WygJjGPHHbdsDMIXvpWe8o-UlfoWE-QLOar6VIu0H3OnOlSt--2GSjImYHRsioGcIWQRR9NoHwWmQ8kXVgzTHEGKrvKxc1zzY1ZvxniLD0wjFWKSo0OIWFD0SJHcmIbjOSxmue1k5tUgrzubMcUWH7dm5XiGeOI5xzowhM6zoke8u-Eu0iRshaaYAgS_nRqw-tWN1eZkQGDEC_61JcQB9rqobl4zngupLrF3GUbtS_QgN438VGOvfUwjOiNYb-mDo2vUb716H08luU7R2xs73hktNDWB73okrDNkeL4JbXnEWImkzI07zGPefGG48pcH8o6ccG9_slWImWeEGzVGNDsUV8_jfidPXsAAFbfQ_mNUKOOYAK1DVad4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da22e4ebd.mp4?token=meaonIS-VAp4SnN6Bp7ZqTUdeXRvE2OLCbupwR8w2pTdQqo86QW7dZRbJIrDsLloNhop5brzcs0ZWUCThOZHHZjpxmYLDwSkVHs5GtEjJ8Qj-HR4AvbTiA1vlsHUvGo3UjkYdZC8cBqbKBNzXOld4Zqk9zmu3yMstmOIeVlz-VoTeZp1nHhMidR-5qpKSdlzwimUVE6V2nvLw0MBw5ePIvMtgZN3AkGSS3R-KAsdRO0TctkVz3E2cH0w6sSB-73NCk85pC67SpSVCuHHMqU9Pb2QmcoZQKD0HO8L_aCh0a5IB8PqLH8WygJjGPHHbdsDMIXvpWe8o-UlfoWE-QLOar6VIu0H3OnOlSt--2GSjImYHRsioGcIWQRR9NoHwWmQ8kXVgzTHEGKrvKxc1zzY1ZvxniLD0wjFWKSo0OIWFD0SJHcmIbjOSxmue1k5tUgrzubMcUWH7dm5XiGeOI5xzowhM6zoke8u-Eu0iRshaaYAgS_nRqw-tWN1eZkQGDEC_61JcQB9rqobl4zngupLrF3GUbtS_QgN438VGOvfUwjOiNYb-mDo2vUb716H08luU7R2xs73hktNDWB73okrDNkeL4JbXnEWImkzI07zGPefGG48pcH8o6ccG9_slWImWeEGzVGNDsUV8_jfidPXsAAFbfQ_mNUKOOYAK1DVad4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه آفرینی مردم سرخس در شب ۱۹۷ حضور در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/461905" target="_blank">📅 00:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461904">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c57jGqmYcjXV2jVYpZN_ESJn2EMOduzo_Ts2wMazVvLEHvZsCQ_fBe0wk0wY8SbuTkvOHC2aBxHP9wb4jbaEy_7KI7KiAB83FUT1IH5oNq-qyTLsjZmlYiKhzx3mLeoH9kIA4iePlpgSht9E2azhSZcNzsvP-I4F_G2NpgW1h4DppxUT0JthbotEFYL7fS4RrMT3fWZ1DtTBI7Y_-BcFlTFOSSyxu0kYfB9fpXx9ttYE3vo25DB8q2pMuYCykCC6ZZqdv7Yj57qv2UDzpYvQwms33fcVRmW_2OgJt5DBoWP6wnqVPOhIdScGEk-UGMYNNLjJ7ut-biRw4FeamshJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایی که حتی ناگفته‌هایتان هم فاش می‌شوند
🔹
دیجیتال‌ترندز:  پژوهشگران هشدار داده‌اند که فعالیت کاربران در شبکه‌های اجتماعی می‌تواند اطلاعات حساس‌تری از آنچه تصور می‌شود آشکار کند.
🔹
پلتفرم‌ها و اشخاص ثالث می‌توانند با تحلیل رفتارهای ظاهراً معمولی کاربران، اطلاعاتی دربارهٔ دیدگاه سیاسی، گرایش مذهبی و عادت‌های خرید آنها به دست آورند. حتی اگر کاربر هیچ‌کدام از این اطلاعات را مستقیماً منتشر نکرده باشد.
🔹
هر تعامل در شبکه‌های اجتماعی می‌تواند بخشی از یک «ردپای دیجیتال» بزرگ‌تر باشد. موقعیت مکانی، فعالیت‌های آنلاین، ارتباط با دیگر کاربران و نوع محتوایی که فرد با آن تعامل دارد، در کنار یکدیگر می‌توانند تصویری گسترده از او ایجاد کنند.
🔹
این داده‌ها ممکن است توسط خود پلتفرم‌ها یا در برخی شرایط توسط اشخاص ثالث مورد جست‌وجو و تحلیل قرار گیرند.
🔹
برای نمونه، کاربر ممکن است هیچ‌گاه به‌طور مستقیم دربارهٔ گرایش سیاسی یا باور مذهبی خود صحبت نکند، اما مجموعه‌ای از رفتارهای عادی او می‌تواند سرنخ‌هایی در اختیار تحلیلگران قرار دهد.
🔹
در نهایت، پیام اصلی برای کاربران ساده است: پروفایل شبکهٔ اجتماعی شما ممکن است بسیار بیشتر از آنچه خودتان منتشر کرده‌اید دربارهٔ شما اطلاعات داشته باشد.
🔹
پسندیدن‌ها، تعاملات، موقعیت‌های مکانی و سایر رفتارهای ظاهراً بی‌اهمیت، زمانی که در کنار یکدیگر تحلیل شوند، می‌توانند تصویری دقیق‌تر از علایق و ویژگی‌های شخصی شما ایجاد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/461904" target="_blank">📅 23:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461903">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb50b917a.mp4?token=TdW6ZboygMGmfIu1arVoAUZKvmt19gzuUoUaOaSHUVsWnyaArOccCxmuXinWzwZC9JGRS0R0R2ndV7ioNLENWF9hfH_uFaCNY8G-8qFx6LU0cqxLq7RaGLN4rhly_2kjTFpewRYCpea7jRRZyibGWYTDn9gG8NTqGVwFA-zxJOKRlRZQmJe3EE35ODGjMnfkIxhfMd1BM6G5bW-7K8HQBBTRbSsom5BSHuMznOiDwjrrGf84Sxadjww351BX0LhGBfUtEmXWFViQRh47XK0UHbroWGc_AnU6IVsXW_5RM3-KhiyMZUgyH3l3g2yixRaU3V0ZtoDtNnriqjNB3gpOBaT4wgMgjcRKKU0xdG31ioUayJ5lNJhGziPnL5Vi4Lp9Q8i1LDgZ3KqcCzrLqK5Npsr1cDwE9uklvzD5TQTX6oqCx8MHbWNvN2qWo8ft5bCACp3UunMCQ0Tgn-WAkO2NwiGPXldKLnl6gw_cSLu-S_1SBwv608xhRjN0iYb00Lsgz2vABFtdRpWXpNvPtSZkFQGcqA3xM0u8X1RWE5KkFyCvbh-L_3X1m_cZc_7Tw_WNILWys5IGynpqQ03-imlU7YoObeMOubVLyOeVhJuU1ow7f7e7nKeDhwlVQDzVAiy391cRXDC8FoDw_DrIoHBJPVZKrjnxiCLh3Q6juaJsrXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb50b917a.mp4?token=TdW6ZboygMGmfIu1arVoAUZKvmt19gzuUoUaOaSHUVsWnyaArOccCxmuXinWzwZC9JGRS0R0R2ndV7ioNLENWF9hfH_uFaCNY8G-8qFx6LU0cqxLq7RaGLN4rhly_2kjTFpewRYCpea7jRRZyibGWYTDn9gG8NTqGVwFA-zxJOKRlRZQmJe3EE35ODGjMnfkIxhfMd1BM6G5bW-7K8HQBBTRbSsom5BSHuMznOiDwjrrGf84Sxadjww351BX0LhGBfUtEmXWFViQRh47XK0UHbroWGc_AnU6IVsXW_5RM3-KhiyMZUgyH3l3g2yixRaU3V0ZtoDtNnriqjNB3gpOBaT4wgMgjcRKKU0xdG31ioUayJ5lNJhGziPnL5Vi4Lp9Q8i1LDgZ3KqcCzrLqK5Npsr1cDwE9uklvzD5TQTX6oqCx8MHbWNvN2qWo8ft5bCACp3UunMCQ0Tgn-WAkO2NwiGPXldKLnl6gw_cSLu-S_1SBwv608xhRjN0iYb00Lsgz2vABFtdRpWXpNvPtSZkFQGcqA3xM0u8X1RWE5KkFyCvbh-L_3X1m_cZc_7Tw_WNILWys5IGynpqQ03-imlU7YoObeMOubVLyOeVhJuU1ow7f7e7nKeDhwlVQDzVAiy391cRXDC8FoDw_DrIoHBJPVZKrjnxiCLh3Q6juaJsrXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای فرار معتادان از کمپ مشهد چه بود؟
🔹
مدیرکل بهزیستی خراسان رضوی: در یکی از کمپ های ترک اعتیاد در اطراف مشهد، ۷۰ معتاد متجاهر پس از درگیری با نگهبانان در زمان استراحت و هواخوری، از مرکز فرار کردند.
🔹
دستورات لازم برای مدیریت شرایط صادر شد و تا شب گذشته و با همکاری پلیس و مراجع قضایی، ۶ نفر از این افراد متواری، پیدا و به کمپ بازگردانده شدند.
🔹
کمپ‌های مادهٔ ۱۶ در اختیار ستاد مبارزه با مواد مخدر می‌باشد و بهزیستی، نقش نظارتی دارد. به همین منظور و پس از بازگرداندن نفرات یاد شده و تا پیدا شدن دیگر متواریان، کمپ مذکور تخلیه و مددجویان آن به نقطه‌ای امن برده شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461903" target="_blank">📅 23:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461902">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d93bea865.mp4?token=REAfpitQh0tgsOU1RgzCvslB83Q5s5nYb9VlbKlee7HZRMUVVSXQW1TS9V-2G5bzA-1YRBPPYG6llLhfRQQHpQvjhoa7jOCFaf9-NyrIZZ3d4tp_m2vomyDBV48Pl6MoZZz0ORwCbZLEbk_rVcR8B4JBomstVK23IxqYlTCJ1ih1LFidXMdiKwyjfLcuXbKUZTU3vNQdDf255-tijpJh7V5LKOyVlQ71W2oUIUZeI9dxNdT-_PW0xeTcZSzxJDAV4IM-0IOrTub0L2ZSUYSyeDW1rV2oCLZYLlSUMbHOUBOsXaEAgHDOOGuq9vnBtv-jginBKqnnANMELk-2kZYpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d93bea865.mp4?token=REAfpitQh0tgsOU1RgzCvslB83Q5s5nYb9VlbKlee7HZRMUVVSXQW1TS9V-2G5bzA-1YRBPPYG6llLhfRQQHpQvjhoa7jOCFaf9-NyrIZZ3d4tp_m2vomyDBV48Pl6MoZZz0ORwCbZLEbk_rVcR8B4JBomstVK23IxqYlTCJ1ih1LFidXMdiKwyjfLcuXbKUZTU3vNQdDf255-tijpJh7V5LKOyVlQ71W2oUIUZeI9dxNdT-_PW0xeTcZSzxJDAV4IM-0IOrTub0L2ZSUYSyeDW1rV2oCLZYLlSUMbHOUBOsXaEAgHDOOGuq9vnBtv-jginBKqnnANMELk-2kZYpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از کشتی ایرانی که امروز در نزدیکی جزیرۀ هنگام مورد حمله قرار گرفت  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461902" target="_blank">📅 23:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461901">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bc2aaa2c3.mp4?token=rartuoRP5zRiPmkWu7-cX0kVytRIw_JsS5FB57wknmpBBdIXCONWrdCRNI43lWUn4PVtvpnd3fqdFZ6hPpcMhMMEthOCWyqGvFUC4t355dKkd-jsZjwKSeGVskO3VKOraKGFhsDG0mlyiUQB5p-fQlQ_Xqe7Rw1srGrOHKZzQGrNdOKm2g0MRHj9kXpvYSk4qWqARDayAnoj_WaSoFg0xMoSFrB0sqNZCAmicrdoB0Asd14ajgSUCUUSNQONk7lV5xiKrYZr9jk_rtkHcOKuDbCp10O_OOQh2RjCbEe9lXroMoeAMB_mFlDoxk8tsIU0AOOdGUKuyXqc0LC2yDn_fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bc2aaa2c3.mp4?token=rartuoRP5zRiPmkWu7-cX0kVytRIw_JsS5FB57wknmpBBdIXCONWrdCRNI43lWUn4PVtvpnd3fqdFZ6hPpcMhMMEthOCWyqGvFUC4t355dKkd-jsZjwKSeGVskO3VKOraKGFhsDG0mlyiUQB5p-fQlQ_Xqe7Rw1srGrOHKZzQGrNdOKm2g0MRHj9kXpvYSk4qWqARDayAnoj_WaSoFg0xMoSFrB0sqNZCAmicrdoB0Asd14ajgSUCUUSNQONk7lV5xiKrYZr9jk_rtkHcOKuDbCp10O_OOQh2RjCbEe9lXroMoeAMB_mFlDoxk8tsIU0AOOdGUKuyXqc0LC2yDn_fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع شبانهٔ مردم ولایتمدار شهرستان زرند به ایستگاه ۱۹۷ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/461901" target="_blank">📅 23:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461899">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae0abfabb.mp4?token=P8MkgI1_PMtEnOZBEFN6MKJ-rzJr7fOTqzouV1yy4txCIMRO1ArXER-Axazf_EaXqOP_36IfX_vTTzjHzjXkGTWVKZZ-jPrqdAgoBRB5b9pNOMgkWlWv1dvMi7q3AGTKGTJsLSBabH-AU8t7be8BGayk8Fjn9eibd9bfu8s141DR-x3pAKoJKNi7gbJkeNqSQTEQWnrDkyd9pFOEg3FYESMxrHBxn-XeAQcW9GOI17cplfTHuklvdPoq97a5zt5Y86mLSg-sZPauMsFwoFkB51YfJz_Xy6emPgKyU2RUs979y3O0e5jWkXidfcQ4gb4PvsMTtY1gjmxy3oWR9rtLeG4oobOQoLOaMSuZzF3OKCjlW13If0XDD6N71rkIv_c_ouP6Q1FH1eDR-oxWKmyP5Otsx84A--pQEyIHPe0ooUWZsFteMIbtTA86FtGqzFA5FcCwALGiqMR9Qfj84Pchn8jYmOhL_wGo1sfAw6uYwCn5iNGulS3Cwn-VK_hox661oWzv_Al0tNUMlxwtBozZR_MUii0GxyERJLA1NlEXcpuh5NWvLRxjVkOyllMhKMfWoRzje6xAGU8fMny58uF7qKk2PnMJUTJapqv7Z7T_MQKf4iAvxokisp-2UlgL5SenKVy6xIaz9qxfi5vSgCCft-WWdnXI2CDBQFv9W7N8kto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae0abfabb.mp4?token=P8MkgI1_PMtEnOZBEFN6MKJ-rzJr7fOTqzouV1yy4txCIMRO1ArXER-Axazf_EaXqOP_36IfX_vTTzjHzjXkGTWVKZZ-jPrqdAgoBRB5b9pNOMgkWlWv1dvMi7q3AGTKGTJsLSBabH-AU8t7be8BGayk8Fjn9eibd9bfu8s141DR-x3pAKoJKNi7gbJkeNqSQTEQWnrDkyd9pFOEg3FYESMxrHBxn-XeAQcW9GOI17cplfTHuklvdPoq97a5zt5Y86mLSg-sZPauMsFwoFkB51YfJz_Xy6emPgKyU2RUs979y3O0e5jWkXidfcQ4gb4PvsMTtY1gjmxy3oWR9rtLeG4oobOQoLOaMSuZzF3OKCjlW13If0XDD6N71rkIv_c_ouP6Q1FH1eDR-oxWKmyP5Otsx84A--pQEyIHPe0ooUWZsFteMIbtTA86FtGqzFA5FcCwALGiqMR9Qfj84Pchn8jYmOhL_wGo1sfAw6uYwCn5iNGulS3Cwn-VK_hox661oWzv_Al0tNUMlxwtBozZR_MUii0GxyERJLA1NlEXcpuh5NWvLRxjVkOyllMhKMfWoRzje6xAGU8fMny58uF7qKk2PnMJUTJapqv7Z7T_MQKf4iAvxokisp-2UlgL5SenKVy6xIaz9qxfi5vSgCCft-WWdnXI2CDBQFv9W7N8kto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مینابی‌ها هر شب پای کار تجمعات خیابانی هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461899" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461898">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
نشست ایران با کشورهای عربی به تعویق افتاد
🔹
وزیر خارجهٔ عمان: نشست منطقه‌ای که قرار بود فردا در «صلاله» برگزار شود، به تعویق افتاد. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/461898" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461897">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5K9NAprLQL3kYpZTiwcPMlhkja7e4xjOGF7UfVADFN7tD8PZgBqi40EpW8-Cs-kk73Br15nojBPyyjIRR77JJJ-CcAsklEi-HrzxahSAQdYEEPCLwHgye2fuNcHaPgywJA34NjqBxOGL49Wk8y8H0WVxUOwuMN9pMJnXGuAGZnQpbV_hN2JdwQXtqgLwTXyU791b87BJ07v8FLqGhRxJI4uufiR9qOkDRvXAsQ-UitM3XpuHQyf6-Fu5uI7ptkpPFqNe-e9jmQTwu2kl1z_8Q6hAtaQkU1xMeJjO7dGqHYrzguDSyxQ2z1NSlLaFThgMxoMlOO01CEX6_PqKUPugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشست ایران با کشورهای عربی به تعویق افتاد
🔹
وزیر خارجهٔ عمان: نشست منطقه‌ای که قرار بود فردا در «صلاله» برگزار شود، به تعویق افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461897" target="_blank">📅 23:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461896">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c1883a9c3.mp4?token=ELKNvlEBuJY5JIBxGfUgPLFHIfjCfm5vJSPNSY34enVvtYYi9YGggDDp9NksEIFcBuRISiZmjs-gXwl6wo4V3pq43n0xqIXg8jXJchHF9nBXGFxW9Ikt1qwkFWYQvu_tby-la7CZmk7h0kmzViegqiLWFP9KYWVfe-z4MngbIv_DnF_FazXRkWEY-YdZ7WqjOq9_E2FUk7TAjtfwTRxOG0I3EDSrMspGBr0hZhH9uC1tDouzfOytulWcIYTfvcdq-ON1WJXvZvdA-0aXr1q6jLL29cJ4RDzsk_VOzmMszqacFFkZzEcNLhbQW2lnheIBvWttC63AX5E7mrXKIbW2AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c1883a9c3.mp4?token=ELKNvlEBuJY5JIBxGfUgPLFHIfjCfm5vJSPNSY34enVvtYYi9YGggDDp9NksEIFcBuRISiZmjs-gXwl6wo4V3pq43n0xqIXg8jXJchHF9nBXGFxW9Ikt1qwkFWYQvu_tby-la7CZmk7h0kmzViegqiLWFP9KYWVfe-z4MngbIv_DnF_FazXRkWEY-YdZ7WqjOq9_E2FUk7TAjtfwTRxOG0I3EDSrMspGBr0hZhH9uC1tDouzfOytulWcIYTfvcdq-ON1WJXvZvdA-0aXr1q6jLL29cJ4RDzsk_VOzmMszqacFFkZzEcNLhbQW2lnheIBvWttC63AX5E7mrXKIbW2AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت صادق محصولی از تلاش سپاه برای ساخت موشک ضدناوشکن  @Farspolitics - link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461896" target="_blank">📅 22:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461895">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سرکردۀ مزدوران سعودی در یمن به ریاض فرار کرد
🔹
یک منبع دولت عدن (همسو با عربستان سعودی) خبر داد که طارق صالح، برادرزادۀ رئیس‌جمهور معدوم یمن به ریاض فرار کرده است.
🔹
طارق صالح، فرماندۀ شبه‌نظامیان موسوم به «مقاومت ملی» است که سال‌ها سواحل غربی در جنوب استان…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/461895" target="_blank">📅 22:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461894">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc8d5a7c1.mp4?token=BWIaiyg3yJnY6D_E-TueeDho1dc2DYvdxz-eNNaVKy-gBOT84-xfU8wWXQJ5fhq6Nibr-0Db7kASRN8aV5cpNzQ0iN0eZ57-E_kBt9Fujb80xHNyxvtIbE-djZvBGyxFJPee5APny8n_AK7HjKDYNAtSW3i8cqZcKx8Uvg4PkjKL5C06HzYETk2yLCraHWD4hkl8_rIAvHMkRndQO96368UfmaRjERW0WAK7L8JRn96Gc7JvHRtmR-EzPogIJy5WtsY3xo3ag4NJ69g3Ds3_rvzfp7li60Xqu8vUIroTxSf6BZBEjydIDbRbCD8q9f4lvpebRlsijWGmjFONrdXMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc8d5a7c1.mp4?token=BWIaiyg3yJnY6D_E-TueeDho1dc2DYvdxz-eNNaVKy-gBOT84-xfU8wWXQJ5fhq6Nibr-0Db7kASRN8aV5cpNzQ0iN0eZ57-E_kBt9Fujb80xHNyxvtIbE-djZvBGyxFJPee5APny8n_AK7HjKDYNAtSW3i8cqZcKx8Uvg4PkjKL5C06HzYETk2yLCraHWD4hkl8_rIAvHMkRndQO96368UfmaRjERW0WAK7L8JRn96Gc7JvHRtmR-EzPogIJy5WtsY3xo3ag4NJ69g3Ds3_rvzfp7li60Xqu8vUIroTxSf6BZBEjydIDbRbCD8q9f4lvpebRlsijWGmjFONrdXMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: دشمن برای چهارشنبه آخر سال ۱۴۰۴  قصد داشت مدل دی‌ماه را پیاده کند اما مردم نگذاشتند
🔹
جانفدایان ایران پیش‌رویدادی هستند یعنی قبل از این‌که وطن‌فروشی به میدان بیاید در میدان هستند.
🔹
انگشت ما مثل انگشت عزیزانمان در سپاه و ارتش برای حفظ امنیت…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461894" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461893">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff0f87d1a.mp4?token=YvAsZ_wB9xgc1GuHe-v2TLr1N5OPBxENddiXg-Wy_G4wbVlZPJfAAVE71YHWVvK94whHm2rFr9Ev0XiW8Fmvi97tO4S2swaKG6c7beAslY-yujk5tp21PkLZOsoKZy3gbtGQGasHesdAPpmsJC48xTCOyCsHqBpsmKMe7IbeQez0PScL1Zlw6QMGF48ZosaJrKb_moqv7EMDwlAow6x3uOMFrAds4VeR-awUIo_6AVodpx3f0GtjQrAHGki7I1rHRIVeIL7JJndd0cJX6OcSAwJiFVuyKeXF9NcZMgGFtdUcWHexGxDnbcdy9PomcH05zYOGxMr6M7Mwiv1Re4_EWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff0f87d1a.mp4?token=YvAsZ_wB9xgc1GuHe-v2TLr1N5OPBxENddiXg-Wy_G4wbVlZPJfAAVE71YHWVvK94whHm2rFr9Ev0XiW8Fmvi97tO4S2swaKG6c7beAslY-yujk5tp21PkLZOsoKZy3gbtGQGasHesdAPpmsJC48xTCOyCsHqBpsmKMe7IbeQez0PScL1Zlw6QMGF48ZosaJrKb_moqv7EMDwlAow6x3uOMFrAds4VeR-awUIo_6AVodpx3f0GtjQrAHGki7I1rHRIVeIL7JJndd0cJX6OcSAwJiFVuyKeXF9NcZMgGFtdUcWHexGxDnbcdy9PomcH05zYOGxMr6M7Mwiv1Re4_EWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: با وطن‌فروشان مثل دشمنان برخورد خواهیم کرد
🔹
اگر وطن‌فروشی قصد ایجاد ناامنی داشت با او برخوردی می‌کنیم که با دشمن باید کرد.
🔹
در حوزۀ مرزبانی و انتظامی از قبل از جنگ آماده‌تریم و در امنیت مردم شوخی نداریم. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461893" target="_blank">📅 22:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461892">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWu3UXlNDrs7Jnlur3MQJyDumRwPNoqdh-F_q2sxb2vyy89NHM-__h-mk5MkkqToTnDa4ffTGWU7LX6fCajZyM4pORew0fV7kc7fbYXmrSs-uS3nSoojnH_K1ZLFxdLz4Kn-urCE_6Iu_oUcfa8n86XMXuJoIzvvmRDBwRGCMMf2XC711mJ6QaJqOqOttq7A3kPnWt3h1OIYjw-pqnv0TKpwIwt85sBS4ua8SCR5kduDbKczZJr8zrKg5wkunha9d6QR5h9CHaQJc11_SXtPIsbsrNrajfdBcJFJrjTIET6c1crEiPYMRx2Mmzr-fbjBxns-gGFkf1Naxx1mY2pNxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصابت موشک به یک نفتکش در تنگۀ هرمز
🔹
سازمان امنیت دریانوردی انگلیس خبر داد که یک نفتکش با پرچم پاناما به هنگام عبور از تنگۀ هرمز مورد اصابت یک موشک قرار گرفته و از کار افتاده است. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461892" target="_blank">📅 22:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461891">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ded472086.mp4?token=i_Q7GxpFmR-cPVB1Hj8wttBUdcE65zpziW1r3eyqBCDtdl6NfxxkTKjgP4F23MoktFaxv84xcQiN6OgSjaR_65v1o9rGAGXc-I-A8vWLi7eBz7hIfCwnKeVxGAQiKKoOFRsC9zgt7CtSUmOMbfudWBP7ngYo5ctZwzPF5rMFisgS0SgU8-g-xuhS4zJGK5PxJ669LQXk0Be-o2INovDSMAXrkpoKziJP3RCWG6q6qftqqR9MwnBAMzEjZSSH5i2OLLKtReNdHpiJ3ZBtEqAlPEm4Lwj7e9iFSa05sKZC-hhOJbRhROvOba_aQj7OjprJuGDOzrMfqCkTVk4Y4As8Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ded472086.mp4?token=i_Q7GxpFmR-cPVB1Hj8wttBUdcE65zpziW1r3eyqBCDtdl6NfxxkTKjgP4F23MoktFaxv84xcQiN6OgSjaR_65v1o9rGAGXc-I-A8vWLi7eBz7hIfCwnKeVxGAQiKKoOFRsC9zgt7CtSUmOMbfudWBP7ngYo5ctZwzPF5rMFisgS0SgU8-g-xuhS4zJGK5PxJ669LQXk0Be-o2INovDSMAXrkpoKziJP3RCWG6q6qftqqR9MwnBAMzEjZSSH5i2OLLKtReNdHpiJ3ZBtEqAlPEm4Lwj7e9iFSa05sKZC-hhOJbRhROvOba_aQj7OjprJuGDOzrMfqCkTVk4Y4As8Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: در سال جدید ۶۰۱ میلیارد تومان که با کلاهبرداری  از حساب مردم برداشته شده بود را بازگرداندیم  @Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/461891" target="_blank">📅 22:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461890">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac367f1a5a.mp4?token=kuI_IORlXs3jHPAmTX1RW_HiE4EjV1C-I76dHd8aPCne1giOPnouc2EI3katL_fBfAJ30Yaoz3W78TQOg_42G7SKEU2ODybImpugCFaGHK726XRMrl0MvXymfqYEB625-RDRWvghx1YIMaN6rXFIJKRDVGuS0PE0TQNkprsU6Lh7W0r8tUbRz4ApPCeV9nMlmR4AVGSnPvr3tdQy-mB_2KIsfDQF7qlk2-rEr_qFLjy3cBtLiXJ6RdnuwOHAM4yFmpA_HQV83YRg-SLU6fOkI-otl92THOm7TrzsB_7RdYQgpWlTIrXqNSW2K7OVXmjDAL4ypcEbyibP3FrDLquowA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac367f1a5a.mp4?token=kuI_IORlXs3jHPAmTX1RW_HiE4EjV1C-I76dHd8aPCne1giOPnouc2EI3katL_fBfAJ30Yaoz3W78TQOg_42G7SKEU2ODybImpugCFaGHK726XRMrl0MvXymfqYEB625-RDRWvghx1YIMaN6rXFIJKRDVGuS0PE0TQNkprsU6Lh7W0r8tUbRz4ApPCeV9nMlmR4AVGSnPvr3tdQy-mB_2KIsfDQF7qlk2-rEr_qFLjy3cBtLiXJ6RdnuwOHAM4yFmpA_HQV83YRg-SLU6fOkI-otl92THOm7TrzsB_7RdYQgpWlTIrXqNSW2K7OVXmjDAL4ypcEbyibP3FrDLquowA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: ۱۰۰ درصد قتل‌ها در سال جدید کشف شده
🔹
پروندۀ قتل مجهولی پس‌از جنگ نداریم و پرونده‌هایی که از سال‌های قبل مانده هم درحال بررسی است.
🔹
صحنۀ جرم را با کمک فناوری‌های دیجیتال بررسی می‌کنیم تا به واقعیت برسیم. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461890" target="_blank">📅 22:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461889">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLsIZG-OIAOc_1ygi7ivMPIpGIn1qepvbbQuHQ2jJ8mrAZrp9kzBT08iZzteMuJXTiAzeP76vc1IjwLXwbcUplxGIRPbSuQVFgpc2tp34BzndnNpyB5vVfhAZaqFG4CWagdnFxsaYJm51b7_bpAKg8VqcjHCgoaNlVT00mm9Yk-TqizQo-tjwbbKwTnIqH9OAo5uSXpyhIP38viHsjTKvsm8ZEPUW7caSQvvr6k9xbx7AnkEFZMfCFoEluFFBd8ZREsRaXP2DfhUU9C_fxPRXiTZ7SXZYLB9wjYtNhlZOiBly46zEGe3F_UFqQSW_OTHooCb0msSyqrIv0zyZf84ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باند حرفه‌ای سارقان خودرو در آذربایجان‌ غربی منهدم شد
🔹
فرماندهٔ انتظامی آذربایجان‌ غربی: مأموران پلیس اعضای یک باند حرفه‌ای سرقت خودرو را شناسایی و ۳ سارق را دستگیر کردند و ۲ خودروی سرقتی از این باند کشف و توقیف شد.
🔹
اعضای این باند ۱۰ خودروی سرقتی دیگر را نیز با شیوه‌های متقلبانه در مشهد، اصفهان و تهران فروخته بودند که با اقدامات پلیسی، ۸ مالخر و عامل خریدوفروش خودروهای سرقتی شناسایی و دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461889" target="_blank">📅 22:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461888">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e754c1c6.mp4?token=Bwj2KOeVr9PxcDlFYp3Afod3M5AB7JeGTphJ_IR9L2avX3UTeAH7U7GPwZsYMOyZcVfyWOLNUJTKNcrp1s_E3lMx2q5LBoe5blDSWFuP_7BPOCynDcLTpKPc6dfYFK_PLDQo3Jl_dnyx-anhOvYKkY53Wk0dN1RqWwzINT9EA94LYvSg23P_xsc1yihqCkhNmDWItkXjF4vMJ2mReVctEEv2_DF-BYwAEqUh6dZFyBQEKKKEdUbqXuv1sHkVIkwCw1PCZbwHv54Mqs-1HwXIoVVYEmwvbYxpECIi33qfI4voLweisEy32_tqQZFxutnxF41n4R3Hdr1_WmRayCIQng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e754c1c6.mp4?token=Bwj2KOeVr9PxcDlFYp3Afod3M5AB7JeGTphJ_IR9L2avX3UTeAH7U7GPwZsYMOyZcVfyWOLNUJTKNcrp1s_E3lMx2q5LBoe5blDSWFuP_7BPOCynDcLTpKPc6dfYFK_PLDQo3Jl_dnyx-anhOvYKkY53Wk0dN1RqWwzINT9EA94LYvSg23P_xsc1yihqCkhNmDWItkXjF4vMJ2mReVctEEv2_DF-BYwAEqUh6dZFyBQEKKKEdUbqXuv1sHkVIkwCw1PCZbwHv54Mqs-1HwXIoVVYEmwvbYxpECIi33qfI4voLweisEy32_tqQZFxutnxF41n4R3Hdr1_WmRayCIQng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: ۹۹ درصد خودروهای سرقت شده را کشف کرده‌ایم
🔹
گشت‌های آگاهی زنده شده و به کمک این گشت‌ها بیش از ۱۱۰۰ خودروی سرقت شده را کشف کردیم.
🔹
در سال ۹۸ حدود ۴۰۰۰ سرقت خودرو داشتیم اما در ۶ ماه اول ۱۴۰۵  تعداد سرقت خودروها زیر ۱۰۰ مورد بوده. @Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/461888" target="_blank">📅 22:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461887">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82b0b5bfd.mp4?token=Fgnk6hG4W1RcnjMw4IBRoEFBF0w6oUcQiBkuEZohmem1bELgfALtGZ2heI0DLSfkKm_2tcMyP2qWJeA3vgpOCC7x5Zj3MCe1YFnmM4WS24eJdxctsQKkEpn2z2gEyPVMcIgKBo5KZZFTq9JCX0QXY_NjylpN83TAPJAj3nRQ5c-gMWq1oJPsXUvpGD85XqSWSTkc67t2gUybwvuZp8DXbQqEGWhI8iYcx6GIKu84kdizgY98F5-BtFq1vIdF_aRRhl6BkWZycdczzeG0_JxLS_btjTm-Ui1N0pM-dEz8ag2NVHUiVbM4dviXW1syzNpegSpBE2s5SJ7oHP0rRtMgQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82b0b5bfd.mp4?token=Fgnk6hG4W1RcnjMw4IBRoEFBF0w6oUcQiBkuEZohmem1bELgfALtGZ2heI0DLSfkKm_2tcMyP2qWJeA3vgpOCC7x5Zj3MCe1YFnmM4WS24eJdxctsQKkEpn2z2gEyPVMcIgKBo5KZZFTq9JCX0QXY_NjylpN83TAPJAj3nRQ5c-gMWq1oJPsXUvpGD85XqSWSTkc67t2gUybwvuZp8DXbQqEGWhI8iYcx6GIKu84kdizgY98F5-BtFq1vIdF_aRRhl6BkWZycdczzeG0_JxLS_btjTm-Ui1N0pM-dEz8ag2NVHUiVbM4dviXW1syzNpegSpBE2s5SJ7oHP0rRtMgQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: بیش از ۵۰۰ سارق را با ضرب گلوله متوقف کردیم
🔹
۵۶ نفر از آنان که در مقابل ماموران اسلحه کشیده یا مقاومت کرده بودند هم کشته شدند. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461887" target="_blank">📅 22:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461886">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75d753ba1.mp4?token=rF98LOh8lbZRXWq5jwrGVa0yr436HwwXG2MB2Ga0vS5W8oCAi0wS0H4IMqs3SsiZ5sg3hXxcljjZtAfI4w6owWZvgeY3bTZfp-bIGJ7qknjFBebY0meJmonBHx0yxZ7vu32iKw-5u4-DrFKK2pExs4PkLRVJjUo2leMDqBKYFxuHsH0nsG-rybTiEUxQOzz58nlr8mKkJULHCSg5DCqQ5sRkqJBZDnN-IIwvk65kJniEtKIsFC8O6H0_XD_j7ZxAa2fz3EdkiTT6XcewwF_MiN0dX1CENdH6Subh7gxq7rdOvrGUJDzab5HEsgt3wffcNGCBwV1g9Nl4nsDb7PJIFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75d753ba1.mp4?token=rF98LOh8lbZRXWq5jwrGVa0yr436HwwXG2MB2Ga0vS5W8oCAi0wS0H4IMqs3SsiZ5sg3hXxcljjZtAfI4w6owWZvgeY3bTZfp-bIGJ7qknjFBebY0meJmonBHx0yxZ7vu32iKw-5u4-DrFKK2pExs4PkLRVJjUo2leMDqBKYFxuHsH0nsG-rybTiEUxQOzz58nlr8mKkJULHCSg5DCqQ5sRkqJBZDnN-IIwvk65kJniEtKIsFC8O6H0_XD_j7ZxAa2fz3EdkiTT6XcewwF_MiN0dX1CENdH6Subh7gxq7rdOvrGUJDzab5HEsgt3wffcNGCBwV1g9Nl4nsDb7PJIFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: با کمک مردم سرقت برای سارقین سخت‌تر می‌شود
🔹
برخی سرقت‌هایی که صورت می‌گیرد روی اشتباهات رایج مثل نگه‌داری مال در مکان‌های غیرایمن و استفاده از در و پنجره‌های ناامن است. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461886" target="_blank">📅 22:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461885">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3901d6894.mp4?token=Z9gHdVPw1TNyKJbK03zW60D843m5-AvOyrPklMDUU9D91JZHDNJeYgaN2RKaMmvx8a3MLda5TQDfsbZRJM2rt72NkY9z6fz0E-dZoqfyMG-jv_WDiek_YtBP0wbHHtEoHehg-QgpcxZYhtUYB3qKvr92FJdtobo43YiKb6lV7z2tnR2YfzEdeCPEIxrmlN6dJvrHaRKqyOQ6kGk1-878J5oSYZGR8MmGAeE9wCD_kV0JRQ7yqBmGABfUt4TRl88EisBux3Yy-P-Qcjc2Na_YFzeMM0go5lplfcPsqw5S4heqUxPT-feOcflCEaNZ-t2qnHAvWtvjV2x7LCQiG1TINA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3901d6894.mp4?token=Z9gHdVPw1TNyKJbK03zW60D843m5-AvOyrPklMDUU9D91JZHDNJeYgaN2RKaMmvx8a3MLda5TQDfsbZRJM2rt72NkY9z6fz0E-dZoqfyMG-jv_WDiek_YtBP0wbHHtEoHehg-QgpcxZYhtUYB3qKvr92FJdtobo43YiKb6lV7z2tnR2YfzEdeCPEIxrmlN6dJvrHaRKqyOQ6kGk1-878J5oSYZGR8MmGAeE9wCD_kV0JRQ7yqBmGABfUt4TRl88EisBux3Yy-P-Qcjc2Na_YFzeMM0go5lplfcPsqw5S4heqUxPT-feOcflCEaNZ-t2qnHAvWtvjV2x7LCQiG1TINA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: با کمک مردم سرقت برای سارقین سخت‌تر می‌شود
🔹
برخی سرقت‌هایی که صورت می‌گیرد روی اشتباهات رایج مثل نگه‌داری مال در مکان‌های غیرایمن و استفاده از در و پنجره‌های ناامن است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461885" target="_blank">📅 22:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461883">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgbWpuFva53-2AaYMqsEz3J509hBOm2mz37VyJjqU0PgPtxzAWLJXfJ7KbV7jSM4fKszUJtadSgKZhQ8ffEI_WAEN_OqY3hy8YzNeSzknamdjfn4LdKZe60NyyKjsd064NFlb1oFGW35EmLmGRiOH6DrUu-_e8vQgqtMIiOtCt1gUjTS2-HCvQTjVgswpx6aMzD7Bcm3iAAOqN2JAy2_AfSEmWfPsKlSMR2Dc9oT7bX1UioWcskagNWTB51PT1SiAow1z88eQqLLnTHxBnXQpkb4g0NaovIc_1sxP3Z7XKDTmdpJeXV3ycKqcL-qx_lM2ua9cOG59DAfYw4RV6ajFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۱۷ تن طلای عربستان در آتش پهپادهای ناشناس سوخت
🔹
رویترز: در صورت از سرگرفته نشدن فعالیت خط لولهٔ انتقال نفت از شرق به غرب عربستان در روزهای آینده، ذخایر صادراتی عربستان در بندر ینبع تنها برای ۵ تا ۷ روز کافی خواهد بود و این وضعیت می‌تواند به از دست رفتن حدود…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461883" target="_blank">📅 22:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461882">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
بنده کشاورز هستم و یکی از هزاران گندم‌کاری که صدایشان به جایی نمی‌رسد.
هنوز بخشی از مطالبات گندم‌کاران پرداخت نشده
و شرایط معیشتی ما واقعاً سخت شده است؛ باور کنید گاهی پول خرید یک مرغ هم نداریم. اگر مشکل ایران‌خودرو و صنایع یا پتروشیمی باشد، صدای آن‌ها سریع‌تر به گوش مسئولان می‌رسد. خواهش می‌کنیم این بار صدای کشاورزان را هم به گوش مسئولان برسانید.
🔹
دو سال از برگزاری
آزمون استخدامی کیفیت‌بخشی آموزش‌وپرورش
در سال ۱۴۰۳ و اعتراضات مربوط به آن گذشته است. با وجود پیگیری‌های فراوان و اعلام مسئولان درباره بررسی اعتراضات، هنوز
تکلیف حدود ۲ هزار نفر
ی که در این فرآیند حقشان تضییع شده،
مشخص نشده
است.
🔹
در طرح
مسکن ملی
هرچقدر پروژه‌ها با تأخیر بیشتری پیش بروند، هزینه نهایی برای متقاضیان بالاتر می‌رود. ما سال ۱۴۰۰ ثبت‌نام کرده‌ایم اما هنوز مشخص نیست چه زمانی واحدها تحویل داده می‌شوند و هر سال هم به‌دلیل افزایش هزینه‌ها
مبلغ بیشتری از ما مطالبه می‌شود
. عجیب است که تأخیر در انجام پروژه از طرف مسئولان و پیمانکاران است اما هزینه و ضرر آن را مردم باید پرداخت کنند! چرا مردم باید تاوان تأخیر و ضعف در انجام تعهدات را بدهند؟
🔹
من از شیراز برای اعزام به
حج تمتع امسال
، از سوی سازمان حج و زیارت به یک پزشک در دارالشفای شاهچراغ معرفی شدم. پزشک عمومی بود، اما در زمان پذیرش اعلام کردند هیچ‌یک از بیمه‌ها را قبول نمی‌کنند و باید هزینه ویزیت به‌صورت آزاد پرداخت شود. وقتی اعتراض کردیم گفتند
سازمان حج و زیارت
تصمیم گرفته همه
زائران به‌صورت آزاد ویزیت شوند
. برای ویزیتی که تعرفه آن کمتر از ۵۰ هزار تومان است، ۳۸۰ هزار تومان پرداخت کردیم!
🔹
امنیت شغلی دهیاران
را پیگیری نمایید.
🔹
لطفا مسئولان در مورد
بازنشستگان کشوری
چاره‌ای کنند با این حقوق پایین و قیمت‌های سربه فلک کشیده چکار کنیم؟ پول درمان پرداخت کنیم یا پول خوراک و مسکن؟
🔹
من یک
فرهنگی بازنشسته
سال ۱۴۰۲ هستم.
رتبه‌بندی
سال ۱۴۰۰ تصویب شد ولی هزینه ۶ ماه دوم سال را واریز نکردند و الان شهریور ۱۴۰۵ مبلغ ۲۵ میلیون برای آن شش ماه واریز کردند به نظر شما ۲۵ میلیون را اگر آن سال پرداخت می‌کردند چقدر مشکلات یک معلم حل می‌شد ولی الان این پول چقدر تاثیرگذار است ؟ آیا نباید
تورم پنج ساله
را حساب کنند؟
🔹
متأسفانه
یکی از بانک‌های کشور
در اقدامی
نیروهای حفاظت فیزیکی خود را اخراج کرده
و در آخرین مرحله، بیش از ۲۰ نفر از نیروهای استان سیستان‎وبلوچستان نیز از ابتدای مردادماه بیکار شده‌اند و تاکنون هیچ خبری از وضعیت و تعیین تکلیف آن‌ها نیست. خواهشمندیم با توجه به شرایط سخت اقتصادی و وضعیت موجود این موضوع را پیگیری کنید.
🔹
ما جمعی از جوانان و پذیرفته‌شدگان فرآیند
استخدامی وزارت تعاون
، کار و رفاه اجتماعی هستیم که با وجود گذشت
بیش از یک سال
از آغاز این فرآیند، همچنان
در انتظار تعیین تکلیف
نهایی و شروع به کار خود هستیم. سؤال ما ساده اما جدی است: یک جوان تا چه زمانی باید برای آینده شغلی خود در بلاتکلیفی بماند؟ طولانی شدن این فرآیند فقط یک تأخیر اداری نیست؛ بلاتکلیفی شغلی، فشار روانی و آسیب جدی به برنامه زندگی جوانان و خانواده‌های آنان را به دنبال دارد.
🔹
در منطقه
خاک سفید تهرانپارس
وانت‌های میوه‌فروش تقریباً تمام خیابان شهید زهدی و چهارراه‌های اطراف را اشغال کرده‌اند و با ایجاد
سد معبر
، رفت‌وآمد خودروها را با مشکل مواجه کرده‌اند. در پایان شب نیز تمام ضایعات و زباله‌های میوه‌فروشی را در خیابان رها می‌کنند و می‌روند و این موضوع باعث آلودگی و نازیبایی محله شده است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/461882" target="_blank">📅 22:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461881">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQOCPghppQwhWzBxXq1Y6At71l_Xoza2gaOvpQp8FluuLA3QeqNa_9g4txjgVPQPvtn85ekjHwwFRrpcJ7sw3UVvJpL9DoUohaL-l5YoaI3f7LDRlyZ_n_UQbtd6g6xE6DwMop6wm4dmUBsjDK1rUtkUvEhXM0oN7wTLofKNn4gyqnOLRTGOhmKKAZU0_AF75Fclzci_ZNiO24jzyxYY6tAVmBHFmyY56FIwNKj7raz-tMA-Hb1maiivX_g33a8aBTIpRYiAp83DG2JjtggFBH37nSiTbsoQqF2ilK8IC1UERkACp3pJHihn9YGmlpIVZRcAFRtz04KZdvaEDJc9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
🔸
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند. @Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/461881" target="_blank">📅 22:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461880">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7305e36237.mp4?token=qLRNkA5eLsu-BXAavCCv-ebiPSDm1NfZBXFx-BfBB7rF0JoAaMDSm5awPIDABzjCrXWE-_hAvSvtseLSmwCih5gTgAPmAKkB8jxzRPJ6fdpyx_bbAyBsHnZOkQhL-IpRS3wg0KNLF7BlPN75nQt2vEnOPcYmyJ5goUC5mq91vQbrU-ICoJJM_YjOd1_-AYmrJClgK7LfmDCmHgvN3N_YM3Pw1-9muXKcVoHE-767TtXTP7q_O3ebNF6AkbjqBn7NRbEyWFQpC5Iwxv1myB0ay5XfKvIQ5nVb3UWGg3ycWxEVJZzyb7T3wRN45RO3TfQRhFeKGcqMBzR7ASgM58fS3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7305e36237.mp4?token=qLRNkA5eLsu-BXAavCCv-ebiPSDm1NfZBXFx-BfBB7rF0JoAaMDSm5awPIDABzjCrXWE-_hAvSvtseLSmwCih5gTgAPmAKkB8jxzRPJ6fdpyx_bbAyBsHnZOkQhL-IpRS3wg0KNLF7BlPN75nQt2vEnOPcYmyJ5goUC5mq91vQbrU-ICoJJM_YjOd1_-AYmrJClgK7LfmDCmHgvN3N_YM3Pw1-9muXKcVoHE-767TtXTP7q_O3ebNF6AkbjqBn7NRbEyWFQpC5Iwxv1myB0ay5XfKvIQ5nVb3UWGg3ycWxEVJZzyb7T3wRN45RO3TfQRhFeKGcqMBzR7ASgM58fS3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاپیتان استقلال: برای کسب ۳ امتیاز مقابل السد به میدان می‌رویم  @Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/461880" target="_blank">📅 21:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461879">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5f9fd56a.mp4?token=aYPAlRXPRnBs3lObCOhUy-r7n6YtCZnymr4xheElE6aPa9Z2hKYKwsI87WHbbJgkiKKMrLS1ET81L1cKPBnvOBqv0YxBguPuc_EGi1cjA--miQNQo1yvHrdlQ8MPkBnZp7g21yUTp_VjYNhrICA7kEWLZc9d0ouWokj0XVQ5gzfsi-AX-d2bKJ9kz_MrHcWvwKqitex0lWDt04HztyYw4REVstYIKq0N72keVBJXI7io8NA6MW3CVoaVeQyZc3TefS36l4aE0m6d0GQQIT_-ZmtFfQ1A_N6t0eNfGM0ujLJh18qazUoms6wXM9IGHQ6XYqZyce9rH0ZcXo-yQzDKfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5f9fd56a.mp4?token=aYPAlRXPRnBs3lObCOhUy-r7n6YtCZnymr4xheElE6aPa9Z2hKYKwsI87WHbbJgkiKKMrLS1ET81L1cKPBnvOBqv0YxBguPuc_EGi1cjA--miQNQo1yvHrdlQ8MPkBnZp7g21yUTp_VjYNhrICA7kEWLZc9d0ouWokj0XVQ5gzfsi-AX-d2bKJ9kz_MrHcWvwKqitex0lWDt04HztyYw4REVstYIKq0N72keVBJXI7io8NA6MW3CVoaVeQyZc3TefS36l4aE0m6d0GQQIT_-ZmtFfQ1A_N6t0eNfGM0ujLJh18qazUoms6wXM9IGHQ6XYqZyce9rH0ZcXo-yQzDKfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر سقاب: ادعای بلاگر اقتصادی دربارهٔ شهید رئیسی کذب است
🔹
مدیر حوزهٔ ریاست در ستاد تحول دولت شهید رئیسی، در واکنش به اظهارات یک بلاگر اقتصادی گفت: او را نمی‌شناسم و اسمش را هم نشنیده بودم و تمامی اظهارات وی دربارهٔ دعوت به ستاد راهبری تحول دولت و یا تهیه…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/461879" target="_blank">📅 21:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461878">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62060f15d4.mp4?token=f55YVcBGc439uXyPHnQDUFu43cIgJGFt56SC5GhvRLYobKyq-Q9SZVt3b6WJtO2arTU1fXYZfSlN00e-8d1GDdkI0AHpzxedGTfStEisT9fWU_N7a_QcyueFo2IMGGHdMgHfnDLWLi89S_3tNaFf9oKd8uaTrE_PDytTnuAZyq-b_-KxKPnTVSEtFGI2tXrHd9V0Ivjg3k8alE2fQVfzcw6rv9rwj3HtJ7715TNlKRXWpTYEAb_bojyvdv2B6dwgugmINnHa9ESPrPgD6PmprJKi5xFErAbxIhOVNFaBgvvplz4YpsKM_W-QMQ3pgTcy5MB0uL42rk18D9kyDy-gcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62060f15d4.mp4?token=f55YVcBGc439uXyPHnQDUFu43cIgJGFt56SC5GhvRLYobKyq-Q9SZVt3b6WJtO2arTU1fXYZfSlN00e-8d1GDdkI0AHpzxedGTfStEisT9fWU_N7a_QcyueFo2IMGGHdMgHfnDLWLi89S_3tNaFf9oKd8uaTrE_PDytTnuAZyq-b_-KxKPnTVSEtFGI2tXrHd9V0Ivjg3k8alE2fQVfzcw6rv9rwj3HtJ7715TNlKRXWpTYEAb_bojyvdv2B6dwgugmINnHa9ESPrPgD6PmprJKi5xFErAbxIhOVNFaBgvvplz4YpsKM_W-QMQ3pgTcy5MB0uL42rk18D9kyDy-gcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
رونمایی از لباس استقلال و السد برای دیدار فردا
🔸
این دیدار در چارچوب هفتۀ اول لیگ نخبگان آسیا،  فردا از ساعت ۲۱:۴۵ در بصرۀ عراق برگزار می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/461878" target="_blank">📅 21:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461877">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/930111983e.mp4?token=An-v1JUmVuWJAx3ekyTDEfnln_sq_1jfF3KTMKCCnlLkxprTE6g2SiiRRd-A0hwx0HqyW13pWmlhSGLSlN6F7uguv7COnx6CRo7Tvp2lomPJGcQSuTAeRD2Ec6hmamUltowznrPX-jGboL7t9uSnZ9ERtrglbisou3sKadZjRrd_uBy6304vArTAS209vRqnTOGlYswHSt9_iwVV9uKjHBnaePSgCcbP0cEtaAzP8gYm8O6MJ7caSuUopIYu-QjXrajVExyepLZ4ADBJjg7jnIY8lxslZ5uvtMP-olVS7TxWOPRejO2J_YLOJaAi811m1lf4J_bLQNC9840xcQAU_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/930111983e.mp4?token=An-v1JUmVuWJAx3ekyTDEfnln_sq_1jfF3KTMKCCnlLkxprTE6g2SiiRRd-A0hwx0HqyW13pWmlhSGLSlN6F7uguv7COnx6CRo7Tvp2lomPJGcQSuTAeRD2Ec6hmamUltowznrPX-jGboL7t9uSnZ9ERtrglbisou3sKadZjRrd_uBy6304vArTAS209vRqnTOGlYswHSt9_iwVV9uKjHBnaePSgCcbP0cEtaAzP8gYm8O6MJ7caSuUopIYu-QjXrajVExyepLZ4ADBJjg7jnIY8lxslZ5uvtMP-olVS7TxWOPRejO2J_YLOJaAi811m1lf4J_bLQNC9840xcQAU_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۹۷؛ بافقی‌ها باز هم حماسه آفریدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461877" target="_blank">📅 21:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461876">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfcb2c70ab.mp4?token=NvNh5uFuVIh2WwKalf0hjWoHM7MqmbjFqPYLXMNd6i7-nfdgaRe9jrxheyM_lnYQjpqul06OWbH-4TUjKs0hXbBlP-bEdeIAYWU8dtO-AKXLnkseRecMbPFmivHQiEYRhx4UiJgREoOkAQTRohbzdXXy-Ebi4bc2Ga0FimtMRZKXzV1xkuFrDpGgEVxR6kqUP92JT9_wUIsOzrTZMCBHN0z3hQu8-6LBF1rzSPtmuPmSpATIZG4jhxw94H3LaS18Vw4ZkAxGoluE-Z4vX4lCDRCrM0YszYL3by2w8W7qreI9ZQEwQuw0pI4yDKkQwHQk8gmN7-3w0RtmOGBK9qfqeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfcb2c70ab.mp4?token=NvNh5uFuVIh2WwKalf0hjWoHM7MqmbjFqPYLXMNd6i7-nfdgaRe9jrxheyM_lnYQjpqul06OWbH-4TUjKs0hXbBlP-bEdeIAYWU8dtO-AKXLnkseRecMbPFmivHQiEYRhx4UiJgREoOkAQTRohbzdXXy-Ebi4bc2Ga0FimtMRZKXzV1xkuFrDpGgEVxR6kqUP92JT9_wUIsOzrTZMCBHN0z3hQu8-6LBF1rzSPtmuPmSpATIZG4jhxw94H3LaS18Vw4ZkAxGoluE-Z4vX4lCDRCrM0YszYL3by2w8W7qreI9ZQEwQuw0pI4yDKkQwHQk8gmN7-3w0RtmOGBK9qfqeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه کسانی کشور را به قله می‌رسانند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461876" target="_blank">📅 21:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461875">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f55a40f9.mp4?token=Hx0uzLwBiVOBq9ke8hlZCD0CeFBbkcOteOwznLZgjZHQ09wv3-Vb-fnnIM9TndqGTdBGzo53QLtn5Y4D1JJj8ZJIBb4GpfncIO_ilrVqsr1KcSLUihcKngUfdCI7oO_idOicZi_FROodeYNEb0bO9URdcLeOBxArspFO-Ki6QMYlxGqPZ0-19VJPAIyu0dWh1LOXjAESHV4P8nSxDOEpgrteLxNF9MvBCjFUiS4kQAytxwRPMuE1tsOdLIWRYD6_v3eQW1nc9XyiyEHW92ZBpBowP_A44M_A0Xp6wY_5GNf4TPPEdm9Cyqbkqr-2iU1BIyRObAdS3EQefo4eW4JFsAvmkyAnQ6KnFVxUJ9Gr5mhH8Mtdj0j6mOH1LMKkp8LiyOzOmuAO6J7oLbdXW68z3_FR7-rUEa5-I_coLDYbyNuLN03jRgz25F9qUh638JI9LFlu-yzjB99AqIQnfplrWPKCz0myJhkTMNBXEI1j8DS9wC7-lKAJvSKBTlZos-Eq6TLTzsRr7ufNUBMWkmjwTrf_a3ve7XYXEw3y92SpkqNQHVR9OGZq3XWTDyexaaZTUfQsbNbCVo7Xa_M5jnbnNPUJT4Eua4t613kpRm7Dlo4l-YyXhEmO_WQzhSSvxtQPPasYbA4J2IYUB876uYhtic6sgDVm1S6aLA1cnX8UJ4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f55a40f9.mp4?token=Hx0uzLwBiVOBq9ke8hlZCD0CeFBbkcOteOwznLZgjZHQ09wv3-Vb-fnnIM9TndqGTdBGzo53QLtn5Y4D1JJj8ZJIBb4GpfncIO_ilrVqsr1KcSLUihcKngUfdCI7oO_idOicZi_FROodeYNEb0bO9URdcLeOBxArspFO-Ki6QMYlxGqPZ0-19VJPAIyu0dWh1LOXjAESHV4P8nSxDOEpgrteLxNF9MvBCjFUiS4kQAytxwRPMuE1tsOdLIWRYD6_v3eQW1nc9XyiyEHW92ZBpBowP_A44M_A0Xp6wY_5GNf4TPPEdm9Cyqbkqr-2iU1BIyRObAdS3EQefo4eW4JFsAvmkyAnQ6KnFVxUJ9Gr5mhH8Mtdj0j6mOH1LMKkp8LiyOzOmuAO6J7oLbdXW68z3_FR7-rUEa5-I_coLDYbyNuLN03jRgz25F9qUh638JI9LFlu-yzjB99AqIQnfplrWPKCz0myJhkTMNBXEI1j8DS9wC7-lKAJvSKBTlZos-Eq6TLTzsRr7ufNUBMWkmjwTrf_a3ve7XYXEw3y92SpkqNQHVR9OGZq3XWTDyexaaZTUfQsbNbCVo7Xa_M5jnbnNPUJT4Eua4t613kpRm7Dlo4l-YyXhEmO_WQzhSSvxtQPPasYbA4J2IYUB876uYhtic6sgDVm1S6aLA1cnX8UJ4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب‌هایی به رنگ غیرت و وفاداری
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/461875" target="_blank">📅 21:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461871">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Obbun7Jas24_3xRj-wgHGvBdaHx6gg97CNgptDBp_zOEYWXr3tdSKwLVonhf_bRmynvnmhyG5eFkEk4Zb3i8yinLwPd_8YMyjvLyP6eVeOSEa2IzO_C8U8FS9ZBuLDNwZct9m80THjWMUqAVzrvT0hdg7-lFRXCu29Wrrg5qNrhnY1yrZsw8P3gsOzi40CQcBzFqjNtXA6frS3UwMLiHy0hybc8IMEEu0siQPVFA0yWznTmiY7GVfDzMuHxdNjLRgRWxlea6W9K6FYTtappeLId5iSacIMAbgomqGvJ3A7Z0GpLwW4mgXrPbQzx46ixzJJG4NSCdHB6tDMJlnDrbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4ifBgBaMhnblAm2UeMPjoCi-zkJMVYfDI2z9X47gHnNNjOoAHsRtBlZK4gGGTzHgtxn18zGD90BVi-06qZh4syW3ujJeU7EOo0UFXVKaW3glKPJtfGMOYsDH1eeeVvIUoOyOnys2WAgKPcal2-hCiujt1Ycc7Cv4WJtNXePH1iLpZEztw0RkdAd2oc-axy0gImiK-Skx_vHicLXfDCGvy2ohxWzX9vercwi8cM6HsUzIqkp_G5vcfI59lGHjL2BnUucK_EI84ZUw_0F18PkMfTWX7FZCp9Q_L_vhVV6WLEhAeQdTLYEvStgqSCLaSqhMw1INtbescXeHDSZm_VpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hL3tF2-tlVyDinz59fAF7BzJJ7UC-UZ2CroaiGdJksrNnTuGfbQRljUlhimfANMm8gFh9bgHB2jDbzhrph_pTPRdPQMG1v8VMK5FjPQC8sIZrKMYoh3bRH6aB7bAQreTKSdS2001Vi2X40_ifLfqMm1NcjD50Xpj1AMJDG-Jyw0zLH-LqP9QoM3qHWWVkMKoKQHucGs6eRE691547f19dvVub5xOoDS4gYNFbBiAvAI2Li8c_oAzQ0hpHlCo13M9synExxa0VRQ2kL6Z6aoiDuPfK0yV5MC42sYlZdNccWhVlNP_7HYh82Zg4pWMvIxBd75sgI0I5gFyQLgGnNEDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjGzB3QVOZPGF_l2ACN6aWzlT5Irgim2Ia6gPuQsDPMF5Fk1DSjUfjNboS2TUAvAqLm_Yp0oQeaMIRM4SowjedG-_pk_0Cvcq5-JQNzxiOl2RzTIiQgn8cLxHptU6NMoY2C9TvV0GERIJHXX1MllQ8jop1o0DeC7BHVnwZbEFGPPUIRWbTSw4JhCDyPXKIJ_y_RITC9PoXgxYcHfU-C5KJXSclgzvmFIKdaiFcNFMWbFRXr9H0lnAqhCTCJuAL5meEgBLEFnqDtL49NVPvxGuA7hH99D449n2HgWwoEd4WWxlQ8C9DcIQ-3He-m9K6R0fVyrY2_vVBNmVI265FmGoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تگرگ تابستانی در روستای گل‌بلاغی در استان زنجان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461871" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461870">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace70d5693.mp4?token=GY_B5-zetBuzFSmpgC-absq22kT4C1HVJjq9cNUea8OMioC4U-cQpVPWXumDZDGkbm_BGe5Zk_QZhViGVOTSl2Xi_7_H05UO8c1btGOdG1c7Q2RU4NIFofvp1RHDX30GsNQWYrRYfIRO-pm_lvMkDBYP-lo0wyaPW89MJsTkqRWiUZ2u22lwNg6wtWCQgIThzrli5wysEuUHpyRnCL1GnMD1EttqOEf6S_Ioqs2t8VsisLYBHy_xVWn_EJL0KuH4y8Ikt27vR8cYx8w0iGhQNDjXlwdgfitez6qqsntUSFpdUys3MqcPMl_VJDcmDeXEqi8HhdpvkQ59rjJBaXtQ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace70d5693.mp4?token=GY_B5-zetBuzFSmpgC-absq22kT4C1HVJjq9cNUea8OMioC4U-cQpVPWXumDZDGkbm_BGe5Zk_QZhViGVOTSl2Xi_7_H05UO8c1btGOdG1c7Q2RU4NIFofvp1RHDX30GsNQWYrRYfIRO-pm_lvMkDBYP-lo0wyaPW89MJsTkqRWiUZ2u22lwNg6wtWCQgIThzrli5wysEuUHpyRnCL1GnMD1EttqOEf6S_Ioqs2t8VsisLYBHy_xVWn_EJL0KuH4y8Ikt27vR8cYx8w0iGhQNDjXlwdgfitez6qqsntUSFpdUys3MqcPMl_VJDcmDeXEqi8HhdpvkQ59rjJBaXtQ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۹۷ قیام مردم بروجن با مشت گره کرده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/461870" target="_blank">📅 21:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461869">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اجتماعی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADa9pBg_sLudATmruGAsb1qW6i71xWHNYIGWHM8AlYhMzCtUgPrH1mZSTVB3tlyEoJzpIicFdGdVYb4ZfBpZkd9Te4wgzxieXWHJjpFV-2XNZy1LFOqCN7XlSpWf1k_9JnRNkch3EtZynLlyKe4BpE4XdFErRbL0kR3pjPg_HXrsGF9Wkt3iKSe-MjFAet6-nVH8jKOCpOWwNnwoivsgfA4XlgicU6dXxZXyi97a9eXPUmIf9lZX1TF7LdumXP9Nu4jq7JJln6qu3fNVe9CVeUZA3gylkVVTjJ3rc-7GWKWvvb2lF2SDngbe1Ktklso84-_crujN9GUmY1Ux_IXB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست «آموزش و پرورش و اقتصاد در اندیشه رهبر حکیم شهید» برگزار می‌شود
🔹
خبرگزاری فارس با مشارکت اندیشگاه بیانیه گام دوم، نشست علمی ـ تخصصی «آموزش و پرورش و اقتصاد در اندیشه رهبر حکیم شهید» را از سلسله پیش‌نشست‌های همایش ملی «آینده‌نگاری رهبر شهید» برگزار می‌کند.
🔸
در این نشست، موضوعاتی همچون سرمایه‌گذاری و مشارکت در آموزش و پرورش، خصوصی‌سازی، روش‌های تأمین مالی و نقش آموزش و پرورش در قدرت اقتصادی کشور با حضور جمعی از صاحب‌نظران بررسی خواهد شد.
📅
زمان:
سه‌شنبه ۲۴ شهریور، ساعت ۱۴
📍
مکان:
خبرگزاری فارس
@Farssocial</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/461869" target="_blank">📅 21:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461868">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759f26ce05.mp4?token=Xv1uCV8dBsnKNV73uOhQqYCbr1a4vkXV1sWjavX6Kvw9HJJKRxNLBC-HgIn_oJQcIYcjAQF-th6kty__oxY0_u4yPQebf8Y51qVAjsJc9uIUCgQDGN0DJN6Fl9_qhoc1b59XJHZvQRMm_PELJBehdBsz_devisaot7SsUB5C-BWbcJNuDrRKCHNWiQGGWsZ9uL4pEpf378t8DyprNTkAY6-YoCsNyPyQYQwVuYuFIRB429XhMx2lcG3HEzAh9TOFfFIlNEH1nImqI6lSNau9G_APwtXpHU_hs9l120bKFzH_HI1jLfie5-J-ocO5jekD-IR_GVvjF9kleodG_x6r-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759f26ce05.mp4?token=Xv1uCV8dBsnKNV73uOhQqYCbr1a4vkXV1sWjavX6Kvw9HJJKRxNLBC-HgIn_oJQcIYcjAQF-th6kty__oxY0_u4yPQebf8Y51qVAjsJc9uIUCgQDGN0DJN6Fl9_qhoc1b59XJHZvQRMm_PELJBehdBsz_devisaot7SsUB5C-BWbcJNuDrRKCHNWiQGGWsZ9uL4pEpf378t8DyprNTkAY6-YoCsNyPyQYQwVuYuFIRB429XhMx2lcG3HEzAh9TOFfFIlNEH1nImqI6lSNau9G_APwtXpHU_hs9l120bKFzH_HI1jLfie5-J-ocO5jekD-IR_GVvjF9kleodG_x6r-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باب‌المندب؛ جایی که قدرت یمن به رخ کشیده می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/461868" target="_blank">📅 21:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461867">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308494cf81.mp4?token=jLQSFAMqw7c68NNav8ETLzkMZR3cz2tXRm1hpFdmzFHhEy-_3uD80AuuwENxZi-Ofu657Hu2e7Qg96CLrPhKnShUir7-7MLjdo_vJIWEu_ZYqOfrWVkqWM9aHLC4RASzQYsSQQMlbm0lsbTjhHcnTO2V75qik1QC8wOQKOJ6mZV3CJ0plcNnaKiIEZHuWt4PZHvLbfgv9lNcCGowguHsdofQT0_eUPfI7Qhmjy745Hf9HxUg39YnC2N_SRamxtWzHMTMRKkPARnWAjIu0mmZol_UWr5gtI67Z20mYXJ7-Xd7LYzo9pcS_dfZKl2TjlMhk9TcFXqVCjZ8rqw9Xf1_sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308494cf81.mp4?token=jLQSFAMqw7c68NNav8ETLzkMZR3cz2tXRm1hpFdmzFHhEy-_3uD80AuuwENxZi-Ofu657Hu2e7Qg96CLrPhKnShUir7-7MLjdo_vJIWEu_ZYqOfrWVkqWM9aHLC4RASzQYsSQQMlbm0lsbTjhHcnTO2V75qik1QC8wOQKOJ6mZV3CJ0plcNnaKiIEZHuWt4PZHvLbfgv9lNcCGowguHsdofQT0_eUPfI7Qhmjy745Hf9HxUg39YnC2N_SRamxtWzHMTMRKkPARnWAjIu0mmZol_UWr5gtI67Z20mYXJ7-Xd7LYzo9pcS_dfZKl2TjlMhk9TcFXqVCjZ8rqw9Xf1_sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیمت داروها بیشتر شد، پوشش بیمه‌ای هم بیشتر
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/461867" target="_blank">📅 21:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461866">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3511e6b655.mp4?token=uh3sFbvjVUooRYeydM6cHTz8RFt01BrxXSFlXYMNK0BlrilNAIJYL5kIjp9Hz8p2Dg5MgSsnuKa0ifyRxW472bXQG3tsdjFtEJtCHhLX6VYSRFAemiUGNqfEVsep5y98tcnKlNhsa6GgIeN_TVJ18aZESjwYFB-qeJuYmUP9hYelfKrNaQt3GIKkCEIYXyR96Ed0kVBpHP0OkK17ypm3KIIMF62K-fgMT3IyGQ4LGqo404eVV3Xk6i0nbQqYk9lTz9Uq3Y9fu5uGLqXzaoUxmd6PCfpuYpA1TIAXHFA1V7wrFckDNDr0nlAO68zyXfZ8mpZ7XDzz1K3Zsxn3DR2mBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3511e6b655.mp4?token=uh3sFbvjVUooRYeydM6cHTz8RFt01BrxXSFlXYMNK0BlrilNAIJYL5kIjp9Hz8p2Dg5MgSsnuKa0ifyRxW472bXQG3tsdjFtEJtCHhLX6VYSRFAemiUGNqfEVsep5y98tcnKlNhsa6GgIeN_TVJ18aZESjwYFB-qeJuYmUP9hYelfKrNaQt3GIKkCEIYXyR96Ed0kVBpHP0OkK17ypm3KIIMF62K-fgMT3IyGQ4LGqo404eVV3Xk6i0nbQqYk9lTz9Uq3Y9fu5uGLqXzaoUxmd6PCfpuYpA1TIAXHFA1V7wrFckDNDr0nlAO68zyXfZ8mpZ7XDzz1K3Zsxn3DR2mBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنایۀ توییتری قالیباف به ناتوانی تابلوهای بنزین آمریکا در نوشتن قیمت
🔹
رئیس مجلس بخشی از انیمیشن سیمپسون‌ها را به اشتراک گذاشته که در آن شخصیت اصلی انیمیشن پس از ۲ رقمی شدن قیمت سوخت و ناتوانی تابلوی قیمت از نشان دادن آن به طنز از «رایگان شدن» سوخت صحبت می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/461866" target="_blank">📅 21:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461865">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6daa8b0d6.mp4?token=VsTHCDo9vOtWv5QP9NTkST1TnB4FyIeE74M8Yv5yDmsfcL2_xmeXIB6cdavKT6XzX8L3UJcSKiuoVzylIJPAs3-GJK_knicWH9tGlxi-ytTUg5gCTPSYS35jic9a3qNi3E6DVOs-irgTZ8rlwj78VhNFOZ0JXKxomQO_99qgoIHQSkv91ZZbcli6pNyEhB-jQo3KjMztA5A-cV0jJQesnevCaHgEI0BEVJ_o4cwfe_jb81DDaLiXYfeWsI-Xm2avG6IqcBE2Gt784-7zbzon8Pira-mA00VYXdZSRRDW7kw-2G8OqvVBZ9iqdVo8VHigSK7su0oPXNix9zcSZQDesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6daa8b0d6.mp4?token=VsTHCDo9vOtWv5QP9NTkST1TnB4FyIeE74M8Yv5yDmsfcL2_xmeXIB6cdavKT6XzX8L3UJcSKiuoVzylIJPAs3-GJK_knicWH9tGlxi-ytTUg5gCTPSYS35jic9a3qNi3E6DVOs-irgTZ8rlwj78VhNFOZ0JXKxomQO_99qgoIHQSkv91ZZbcli6pNyEhB-jQo3KjMztA5A-cV0jJQesnevCaHgEI0BEVJ_o4cwfe_jb81DDaLiXYfeWsI-Xm2avG6IqcBE2Gt784-7zbzon8Pira-mA00VYXdZSRRDW7kw-2G8OqvVBZ9iqdVo8VHigSK7su0oPXNix9zcSZQDesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰ صیاد مفقودشدهٔ هرمزگانی به خانه بازگشتند
🔹
مسئول دفتر وزارت خارجه در بندرعباس: ۱۰ صیاد هرمزگانی که در امارات مفقود شده بودند، روز گذشته وارد تهران و امروز از طریق پرواز به هرمزگان بازگشتند.
🔹
این افراد قرار بود ۱۶ شهریور به کشور برگردند؛ اما به‌دلیل اینکه…</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/461865" target="_blank">📅 21:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461864">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1a408f8a.mp4?token=DxjPZQ323obALXD8uAunkW1GIzUYutZQ7Te208HWXbx_QM8J17XGu9ABG219ZgawIiY3K2i4yK5ZdjYR4mreRk--n4fHH_jaHyfJ7ix1fSdncCRpZXRNxl_uO7kxLyTZ0Bs8FExDc76VrDYydgmSS-ZUGQZCW4QrlL126FT4B7jiWbnFPTIlAaw8NxSY7jYDR-xNMdatB_Ua3NLRllLjO9MwUfzOQ1Fszc_AMoRHwPCJ5GkFtwnfLiBcFEYsCbebqkht_-6mMxNfT1Dm3ZucED9pzPjljabJHR6Z6cFXDKaI1VGEERjBbMl4sUs50B_DnNQ-YxlEkt93lBKz1wag5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1a408f8a.mp4?token=DxjPZQ323obALXD8uAunkW1GIzUYutZQ7Te208HWXbx_QM8J17XGu9ABG219ZgawIiY3K2i4yK5ZdjYR4mreRk--n4fHH_jaHyfJ7ix1fSdncCRpZXRNxl_uO7kxLyTZ0Bs8FExDc76VrDYydgmSS-ZUGQZCW4QrlL126FT4B7jiWbnFPTIlAaw8NxSY7jYDR-xNMdatB_Ua3NLRllLjO9MwUfzOQ1Fszc_AMoRHwPCJ5GkFtwnfLiBcFEYsCbebqkht_-6mMxNfT1Dm3ZucED9pzPjljabJHR6Z6cFXDKaI1VGEERjBbMl4sUs50B_DnNQ-YxlEkt93lBKz1wag5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات حمله به کشتی تجاری ایرانی در نزدیکی جزیرهٔ قشم
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/461864" target="_blank">📅 21:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461863">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dbebd2130.mp4?token=KVJt01dzVDrvMyVsZynWZbpgHeRHack3xIxNrVrL6U1idb5S-mTkspZH8syp6ZjBSVQK33ElCixMHQ_xIbwheBux6VJdEXDvTWgzW6tRsHXOtq_QbCK2mo-xaJpOkEPX1oKsaYSQRg56pui8Rzg7OG-tGUUseD4dilZnePRG3oU5VhTIhwfchThRYnbkDaK9YlbGIbcwStzhsksPNL8Irt-L4Qi7lhwRZVcSptIrVLY3EjF3Pe6SDf6YOXyzXRx75giNHfyZj9IsE1_9kjbcAa6yxUkPSz2cb6bHMfyeluqIIlwir87XwHrxakq-zkHAc26dutMaTDnGIJym1Z-VRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dbebd2130.mp4?token=KVJt01dzVDrvMyVsZynWZbpgHeRHack3xIxNrVrL6U1idb5S-mTkspZH8syp6ZjBSVQK33ElCixMHQ_xIbwheBux6VJdEXDvTWgzW6tRsHXOtq_QbCK2mo-xaJpOkEPX1oKsaYSQRg56pui8Rzg7OG-tGUUseD4dilZnePRG3oU5VhTIhwfchThRYnbkDaK9YlbGIbcwStzhsksPNL8Irt-L4Qi7lhwRZVcSptIrVLY3EjF3Pe6SDf6YOXyzXRx75giNHfyZj9IsE1_9kjbcAa6yxUkPSz2cb6bHMfyeluqIIlwir87XwHrxakq-zkHAc26dutMaTDnGIJym1Z-VRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس مسائل بین‌الملل: یمن به سختی قیمت نفت را به اینجا رسانده و این دستاورد نباید با خیالات از دست برود  @Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/461863" target="_blank">📅 20:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461861">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5df19509.mp4?token=kY0Xx10CRoIHQFPlKoa-QnC1MMBsRy-7hT9_MpIf5nC5YtJm87z_2HwztvMrGuN58xpp4W1Fl7bpiMk-fAnKv6LZQ8fCCwXOqhRjxKUztszjua0LWayjJhhPwzsGp2k_wBVKImfN32EZQ_uOqbClkn8LwU6g7VyYoyjLjTxD4N4aVVwo4fvsMs9ptzGOdAIU6J4-RKVh2gPxMMpRWeo1dF8s4-qp3iD1vpdiQHKKWVLgGQVq0-MJsM-Xsso2wz3nJGjvzTaSRdZiWNkWzDVNq4MnszwXLTNNDNFr8gKXGpYyuYh9AlP5dC8ZWGgvrZU9oW0NX7IwSX3HdE_NCFwJRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5df19509.mp4?token=kY0Xx10CRoIHQFPlKoa-QnC1MMBsRy-7hT9_MpIf5nC5YtJm87z_2HwztvMrGuN58xpp4W1Fl7bpiMk-fAnKv6LZQ8fCCwXOqhRjxKUztszjua0LWayjJhhPwzsGp2k_wBVKImfN32EZQ_uOqbClkn8LwU6g7VyYoyjLjTxD4N4aVVwo4fvsMs9ptzGOdAIU6J4-RKVh2gPxMMpRWeo1dF8s4-qp3iD1vpdiQHKKWVLgGQVq0-MJsM-Xsso2wz3nJGjvzTaSRdZiWNkWzDVNq4MnszwXLTNNDNFr8gKXGpYyuYh9AlP5dC8ZWGgvrZU9oW0NX7IwSX3HdE_NCFwJRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابت پرتابه به کشتی ایرانی در تنگهٔ هرمز
🔹
فرماندار قشم: یک کشتی تجاری ایرانی ساعت ۵ امروز در حوالی جزیرهٔ هنگام و در محدودهٔ تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناس قرار گرفت که تاکنون یک شهید و ۳ مجروح برجای گذاشته است.
🔹
هنوز نوع پرتابه‌ای که به این کشتی…</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/461861" target="_blank">📅 20:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461860">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
منابع یمنی: هواپیماهای دشمن سعودی با دو موشک یک بازار در شهری در استان الجوف را مورد حمله قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/461860" target="_blank">📅 20:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461859">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a204e443.mp4?token=XAXj7bSZbmNqfP6CeqEvzRntmITnmzzHktoV2eZuxaSOwOG2bntoSrBuAExFFYmYAUUkoA1Qz8d5glvm7Hrg9RhyP1QcYx_cIlEewHEDshAiJPd1eFuoDR-ZDYvxY5508uGU7wB15NDNvq_A06V8jcsslCrm-HP7IXViDK1tyWoT8bOkps97j_DLycpEPCuIKnIBFA2wbTJf4k-xz0MxrRprwXpbv_D2c7LUqAh2zsHsALZ9llCpu7yN8H6qP4uAXjoaTI5Ki9e8Zn-dFnOt87woI4WMnBJKw5ngCllwUcXuI4gjLLcHygpr5QemRrrf2-eFfXs4SU3YWfRJMWqXMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a204e443.mp4?token=XAXj7bSZbmNqfP6CeqEvzRntmITnmzzHktoV2eZuxaSOwOG2bntoSrBuAExFFYmYAUUkoA1Qz8d5glvm7Hrg9RhyP1QcYx_cIlEewHEDshAiJPd1eFuoDR-ZDYvxY5508uGU7wB15NDNvq_A06V8jcsslCrm-HP7IXViDK1tyWoT8bOkps97j_DLycpEPCuIKnIBFA2wbTJf4k-xz0MxrRprwXpbv_D2c7LUqAh2zsHsALZ9llCpu7yN8H6qP4uAXjoaTI5Ki9e8Zn-dFnOt87woI4WMnBJKw5ngCllwUcXuI4gjLLcHygpr5QemRrrf2-eFfXs4SU3YWfRJMWqXMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس مسائل بین‌الملل: بازار نفت آمادۀ استفادۀ ایران است
🔹
هر بی‌احتیاطی در نکات ریز دیپلماتیک می‌تواند جریان بازار نفت را به نفع دشمن تغییر دهد. @Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/461859" target="_blank">📅 20:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461858">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns3jS9V-pCzdyCQFyJguNLvO4gDz0l7wUns_8oJGXtvmZveAQGvXAc2duJyAf_Mp2ZE_ZUF66SCbqy161q2MA6SfV23AIUNBkoMcB6cYDAE6yBplEY5EzFRSp_t5Ze1EcyA2poT7WrtuBn61jiSFeKT6yooJUwwq2L_mkM53mZnYJCFVUvSLlMAWAchf7mTw5_PzfU7IgXrfaxXg7Eb2Z0BcpTBgrBmhlwIyFtvqFrktbIkjIzRjlvDd44ysxjbljtYsy01Gce4H6WJeUsIHdICGoufRh44dnXM1wWKtMKQ7ZBoN9ELsxhj5SXyvDgO7yc_Sft3yh2DxfLZKD_WTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن‌سلمان برای مقابله با یمن دست به دامن صهیونیست‌ها شد
🔹
روزنامه عبری «اسرائیل هیوم» گزارش داد که محمد بن سلمان ولیعهد سعودی از طریق آمریکا به این رژیم پیام داده و برای جلوگیری از تشدید تنش در دریای سرخ و باب‌المندب به دست انصارالله درخواست کمک کرده است.
🔹
این رسانه عبری افزود که عربستان در پیامی غیرمستقیم گفته است: «در جنگ علیه حوثی‌ها به ما کمک کنید.»
🔸
بر این اساس، دستگاه‌های امنیتی رژیم صهیونیستی در منازعه کنونی قصد دخالت در یمن را ندارند مگر آنکه این رژیم مورد حمله قرار بگیرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/461858" target="_blank">📅 20:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461857">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1FbIqCQgNC2SYP0VrOmd6QNwYScI0RoS5F5NB9MoCZHH_I0x2Zr_pbRCR-4H5nS5zoo3V5Kn5Y_EHA6mDez4-3NhJjEPIgKfZn5zR4e9fX2wG2ebKM15yt-dyU9u0TJHQLKWyqocs1Ic3AuhbyuZdO1loL4P7jGKYkWU9NZiD7iT4cJmcHmlnysXMi6QTEuL5XvW80EuL8W-1r9B2RTcR1myHzi7HX4rZLM_3ifKI74GCsiXJV5p9K5n3sgcaOxwVJeOJHObpB9uF7eDJWaNs3kCZGYUUltNBA1VF1cUqwL6gt2VxuOv5mS9vAJEwBbPDjBIkDu2rwaHi_ns36QuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حملهٔ روسیه به ۸۰۰ متری مرز ناتو!
🔹
همزمان با تشدید درگیری‌های روسیه و اوکراین، پهپاد روسی به یک کامیون در فاصلهٔ کمتر از یک کیلومتری مرز لهستان اصابت کرد.
🔹
این تأیید رسمی پس‌از آن صورت گرفت که انتشار تصاویری در فضای مجازی دربارهٔ سوختن یک کامیون، منجر…</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/461857" target="_blank">📅 20:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461856">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a0a841cb.mp4?token=j8ND1IPRoQ8gUTbozLxKdAkfVzc4B4QJyNNYHG-lLfzCRQ1tinz9JxwzAS2bTvdhKbLZclSmNCoyR9tgg8LBFtpaNbuT8Jt6YJlt2YTjwgMdqFuFADiuLgvB5HDVHkT3zVOGye7IV5OOuEahunXiYgzb0OLhJlTI6Q39OzUzU8ru7tce9I3eO2_O_XRaBBEHXwU3fRNsGjEXn8EvzIFkPdv1sok60oYQHE4gkQGfPl6bRaSFVNgUzfkFLSJxIjqXb_ueKHKLyhQMHoZ9qkmWfljA0bygmL6O1GiFv9H78Bj--XBQRFB9g9sAOFxOmn0e9WEWCNnmoHbjGsf5DaV25w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a0a841cb.mp4?token=j8ND1IPRoQ8gUTbozLxKdAkfVzc4B4QJyNNYHG-lLfzCRQ1tinz9JxwzAS2bTvdhKbLZclSmNCoyR9tgg8LBFtpaNbuT8Jt6YJlt2YTjwgMdqFuFADiuLgvB5HDVHkT3zVOGye7IV5OOuEahunXiYgzb0OLhJlTI6Q39OzUzU8ru7tce9I3eO2_O_XRaBBEHXwU3fRNsGjEXn8EvzIFkPdv1sok60oYQHE4gkQGfPl6bRaSFVNgUzfkFLSJxIjqXb_ueKHKLyhQMHoZ9qkmWfljA0bygmL6O1GiFv9H78Bj--XBQRFB9g9sAOFxOmn0e9WEWCNnmoHbjGsf5DaV25w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا در روزهای اول تفاهم‌نامه چندبار آن را نقض کرد؟  @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/461856" target="_blank">📅 20:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461855">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0mdIiuNyPCWyEGjjh495wyXG8-7fh_VeSv6iUfyW46pXR6l1zzyp77E75qX_JOAt_q8CxAfOdadRIu-G7Ii2YKmiacC_2VEibczJbjbKgck-Qukq0PGRxQ0GXhQBuyMn49LoS8OfvXDwQaUsiHBRo-Abgvh2KigPq0wpHkVXG1ccfNkJQ1XXTzI44pdf5G6qTuB0U8dq5Wd3XNlURJl4THQnDTWX6a_nqQtYx1Fxnl4jAtSFVRRA7YC1cfLlJCuLa8lFJCY0lW6SMMeCO19MzcTfLRWmuYgEeFy5Uuj3XhYv4XS21ooHPuAoO-GmhKnf5cz1huk2H59QjxTrB1YWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژیلا صادقی خطاب به بازیگر زیرزمینی: چرا از اون عروسی حرف نزدی؟
🔹
صادقی مجری تلویزیون در واکنش به صحبت‌های لاله مرزبان در فستیوال ونیز: «خانم مرزبان! شکر خدا زنان سرزمینمان آزادند، اما کودکانمان قربانی شدند، جوانانمان شهید شدند.»
🔹
او همچنین با انتشار تصویری از کودکان شهید میناب در کنایه‌ای به مرزبان نوشته: «تو وطن فروشی، وطن‌فروشی که فقط جاویدشاه گفتن نیست.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461855" target="_blank">📅 20:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461854">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJCi2mxldAvEKkTlW3QUjWNAXbt3dG9VH4nlVJiW-LklVctMUNZenqk6o6cMD48IaJ4SfQWQYCVT8I9WcWBu-75cz6y4a1qgxuI_rfj32zss5ivH9nPsVxgDR2n9gNJM_7fsPrteh7Eg0X9sb0L8_jf1KjvvHdLj9X92ZWUsGOjEQWmYUYMJD1xkxCm-H4RGIP4rA3BJFLneqkpVJnNYTs0t5_dayelHcud-_kMYP_7e15w1-icaWX29OlXhQV4lPc1vxRmtSuqkL-IVUokzbMo63KoQnlTFWLkL381Vze7Vs1BC7QqQkBLhMM1ejqX6HTTsSy5C075di_b63iwBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قوطی‌ دنیا را تغییر داد
🔹
در اواخر قرن ۱۸، هنگامی که اروپا در آتش جنگ‌های ناپلئونی می‌سوخت، نیازی فوری به تغذیه سربازان در میدان‌های نبرد احساس می‌شد.
🔹
سربازانی که روزها و هفته‌ها در جبهه‌ها می‌جنگیدند، به غذایی نیاز داشتند که نه‌تنها مغذی باشد، بلکه بتوان آن را برای مدت طولانی بدون یخچال نگهداری کرد.
🔹
در این میان، آشپز فرانسوی، نیکلاس آپرت، با ایده‌ای ساده اما انقلابی، شیوه نگهداری مواد غذایی را برای همیشه تغییر داد و کنسرو را اختراع کرد.
🔹
این اختراع نه‌تنها سربازان را سیر کرد، بلکه راه خود را به آشپزخانه‌های مدرن باز کرد و شیوه زندگی ما را برای همیشه دگرگون ساخت.
اما کنسرو چگونه از دل جنگ‌های ناپلئونی متولد شد؟
🔗
داستان کامل را در
گزارش
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/461854" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461853">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be10a4e8.mp4?token=W2UbXMdFrsaXCeABAmsUYgoL_6eqeqVvr4ThkrmdDPxf2VT5OUW9k3d9dyrO0yiqcKZ9NCadMxjBywD8FcPX1VT_xWsA1Zbcba7W2EhubwttvRBiyzAuNR2YBI2SA0gbu4jpwHhQSCUGeC3XWPO6eUEabJxFvEpzhxbh6ZTziOoT2ru60I5FX-ECldF-S2t_e9hN4Si0YxL6eVBRgn2Lg8VTIz6HtVea2TldNZYNvMpoLUGvu19l-vjz3IeoJ0K0GFLObzoqgD8oZ-k17ikMQAQqIQBG5qL0uzNuaHRNkJE-pTqCH0dz_kP28A7bP6hizBy47qT9IWr-Loe50JxnjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be10a4e8.mp4?token=W2UbXMdFrsaXCeABAmsUYgoL_6eqeqVvr4ThkrmdDPxf2VT5OUW9k3d9dyrO0yiqcKZ9NCadMxjBywD8FcPX1VT_xWsA1Zbcba7W2EhubwttvRBiyzAuNR2YBI2SA0gbu4jpwHhQSCUGeC3XWPO6eUEabJxFvEpzhxbh6ZTziOoT2ru60I5FX-ECldF-S2t_e9hN4Si0YxL6eVBRgn2Lg8VTIz6HtVea2TldNZYNvMpoLUGvu19l-vjz3IeoJ0K0GFLObzoqgD8oZ-k17ikMQAQqIQBG5qL0uzNuaHRNkJE-pTqCH0dz_kP28A7bP6hizBy47qT9IWr-Loe50JxnjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاکستان هم فقط حملات یمن به خاک عربستان را محکوم کرد
🔹
درحالیکه حملات نیروهای انصارالله به خاک عربستان پرسشهایی را درباره فعال شدن بند دفاع متقابل پیمان مکه ایجاد کرده، نخست وزیر پاکستان در تماس با ولیعهد سعودی تنها به محکوم کردن این حملات بسنده کرد.
🔹
این…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/461853" target="_blank">📅 20:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461852">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jriHspiG7yxJzFH4bSjDqD655PnYomhHuD_7gcBf1w6gGK5XDsBO6J3nUi746jpUui2qwZbApvR82atLrEeV-LPkPopEVuUSuPolK3zAudDjmOXhXQ8nnK_Wsax_fv3vw76HrjyhxXtEXYo8bir2COLMvSjAnhC4jFj3jA_wvFl6pIim38eTfENluQj0N8gtnm5mCG02_O065_yafkq7Kn_ZT3cJsnTk9XbPGZHAG34OL4QE2cfH2ShMHC7L9p93DPrumsY-ZAkNUnyvP1y0gitrHyJ2ovNpEJmWE5jLDb20eXA6bdJb79-colzrk7uNQrAmb_D3QZd7FWBciDAopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خاطرۀ سردار علی فضلی از حضور رهبر معظم انقلاب در جبهۀ دفاع مقدس ۸ ساله  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461852" target="_blank">📅 20:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461851">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d7804b6d.mp4?token=lnQkzObKHv-UBfxrMgyumNQIQOgaeKizt469RAIr7Q3q7EHtI1mfKZA0cCXHyR2Mu-Ui0pN4S2y3F1iTHh_LJBfQmreG5J0Ex3ClM3Wa1dnbTn7hlZdH5PxgDSSRidnSoI-YdE504bZ3zA5Oe4K5v0hiSJXRpAw_0lrDowuAz41ffPXhN-PiE13Gak4BqpTPdRkW4rQxgU-rHHjyIghAtKW4q7P_GiVSzUhbAzhTg3Ep11U3Q-15W1fycO5T4IMouxAgoyO2S5a6Oo5x5epY7NDwJA1TZ_OPlsSrPpz1RnyLm7EotFibRY1gatDj6QLDwxXiwjIYXWvF4T17jDA34Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d7804b6d.mp4?token=lnQkzObKHv-UBfxrMgyumNQIQOgaeKizt469RAIr7Q3q7EHtI1mfKZA0cCXHyR2Mu-Ui0pN4S2y3F1iTHh_LJBfQmreG5J0Ex3ClM3Wa1dnbTn7hlZdH5PxgDSSRidnSoI-YdE504bZ3zA5Oe4K5v0hiSJXRpAw_0lrDowuAz41ffPXhN-PiE13Gak4BqpTPdRkW4rQxgU-rHHjyIghAtKW4q7P_GiVSzUhbAzhTg3Ep11U3Q-15W1fycO5T4IMouxAgoyO2S5a6Oo5x5epY7NDwJA1TZ_OPlsSrPpz1RnyLm7EotFibRY1gatDj6QLDwxXiwjIYXWvF4T17jDA34Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش شدید باران در مکه مکرمه
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/461851" target="_blank">📅 20:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461850">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa2d1e303a.mp4?token=ov8fHvj9WLDhYhn-dJd20gL5wQ7q_AL97azrpCblzyOQp8-24bCASY8FLsSyPj9pjdb0lj1UM7ietfDjWJPvem1g4-JXV5a7J07LjQmNme560OYr7IFSElP_UaVhmEpDPdI3qK1SGI2WHV-zhpIWV3IUUTyqMgl5-yPXRVxio2eSEbV1cTimqQmj3y73Bowcgyz_wPOfkpGE6h6WpYeLzvmWa0TIRGovKG0QitbBBHlgX5Kn9ZjbWLPnrpoE8CIwLfADIiTEgmUT6jMWs_DSJmrvOxiGM16JAFI4Ze_5bUW6SdF-3KJiJOlNMzWgMW9BoENYSuSrtlOnFVgzMkthag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa2d1e303a.mp4?token=ov8fHvj9WLDhYhn-dJd20gL5wQ7q_AL97azrpCblzyOQp8-24bCASY8FLsSyPj9pjdb0lj1UM7ietfDjWJPvem1g4-JXV5a7J07LjQmNme560OYr7IFSElP_UaVhmEpDPdI3qK1SGI2WHV-zhpIWV3IUUTyqMgl5-yPXRVxio2eSEbV1cTimqQmj3y73Bowcgyz_wPOfkpGE6h6WpYeLzvmWa0TIRGovKG0QitbBBHlgX5Kn9ZjbWLPnrpoE8CIwLfADIiTEgmUT6jMWs_DSJmrvOxiGM16JAFI4Ze_5bUW6SdF-3KJiJOlNMzWgMW9BoENYSuSrtlOnFVgzMkthag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا در روزهای اول تفاهم‌نامه چندبار آن را نقض کرد؟
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/461850" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461849">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_HiEkHjm7G7K8Qcw7wKU3AwFGW0uGHBMVWTt-byaX6lrmQC5M_nbc-9zTlhnGNzBCt4sf3l7K2Al7jMyQcyxzFNKt3EdVFVsm-Gh-2CkgSWAV0xQYbz-tFWNukoIH0nBCRnoE1e1bcxD78Njjgw-N4upAe0AtCW2z5Iu_Ckv4YLnMv9IiMEvlpa3a2DMW4Zt9ZL5XkVMSFArfLaVaHbqz7xyOS4kXHeVpUYsp4fxy6vLhh-H2zqU_N5qy1S5kaIiF8R4j3iLNuOycgqX7Vfog8QZHxjBE2tQORhKVrIaJfg3_G8nn_A90r-NIDn_nwvGF-nslTz2eNHAExgvJa_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلهٔ طلایی پکن برای دلار
🔹
چین درحالی ریاست دورهٔ آیندهٔ گروه بریکس را برعهده می‌گیرد که هم‌زمان روند افزایش ذخایر طلای این کشور ادامه دارد.
🔹
اقدامی که در کنار تلاش پکن برای گسترش استفاده بین‌المللی از یوان و توسعهٔ سازوکارهای پرداخت مستقل از نظام مالی غرب، بار دیگر بحث کاهش وابستگی اقتصادهای نوظهور به دلار را مطرح کرده است.
🔹
اهمیت این روند زمانی بیشتر می‌شود که چین در کنار انباشت طلا، سیاست بین‌المللی‌سازی یوآن و استفاده بیشتر از ارزهای ملی در تجارت خارجی را دنبال می‌کند.
🔹
آنچه در حال شکل‌گیری است بیشتر شبیه ایجاد یک شبکهٔ موازی مالی است؛ شبکه‌ای که در آن اعضای بریکس تلاش می‌کنند وابستگی خود به زیرساخت‌های مالی تحت سلطه آمریکا را کاهش دهند و سهم ارزهای ملی را در تجارت و سرمایه‌گذاری افزایش دهند.
🔹
اگرچه نمی‌توان با قطعیت گفت چین به‌دنبال راه‌اندازی «یوان با پشتوانه طلا» یا حذف دلار از مبادلات جهانی است، اما اقدامات پکن نشان می‌دهد چین می‌خواهد نقش طلا، یوان و سیستم‌های پرداخت مستقل را در اقتصاد جهانی بیشتر کند.
🔹
این مسیر در صورت تداوم می‌تواند به کاهش تدریجی انحصار دلار در تجارت جهانی منجر شود و یکی از ابزارهای هژمونی آمریکا را از دستش دربیاورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461849" target="_blank">📅 19:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461848">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJYtguJVR7y2Boj0baCTMc4cj5Y6VtaCnh3rHLLlJvd5OOR7zbwJDTZkWUskSBDhxmSVr11MNdi3T_5YuGPYxdWABrIUdR90Z7zUAf61sa26eviNDgP6hi54b28ux8xzsm2X9u_58-ANVkHObPBG6XuLLRXTA3KhzoF2Ta8_VgT-Pa_sSnm4WkN0QPL8f9ubw5ZpI9zjRve9R2gLFqdN6gK4Q0A9wpgQ6wtpUv854HeBmGsjr9cSoVzrS3uoyXjychppIAnMOzdM5DluL1IkB2-PNhjjOqgttKWVzBnrHh0X1WH0kD_-vQgUkqYKbVc5PNtbHkuKtQPQ3CuOm2gnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت سرباز صهیونیست از قتل خبرنگاران در بیمارستان غزه
🔹
رژیم صهیونیستی سال ۲۰۲۵ در یک حملهٔ دو مرحله‌ای به بیمارستان ناصر در غزه ۵ روزنامه‌نگار از جمله حسام المصری، فیلمبردار رویترز را به قتل رساند.
🔹
مقام‌های اسرائیلی پس از حمله اعلام کردند هدف، یک دوربین…</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/461848" target="_blank">📅 19:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461847">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۳.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/461847" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۲.pdf</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/461847" target="_blank">📅 19:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461846">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2PrJT_WLea068eRw7Lbygy1rC4FuMEKJlx0CjwoQSBkFREw5_4Mve3ht0OLrzBi7m6vR77ZoWGaeNzcUctasS5qG8a-PRIgsi6IkWFe_w3Zvh8_yLhPcYgcAL9nQ4BBiVzNovWkc71Tea3lctlSkz56VdrmeVfWSJVrNUQ5acNiZkqyiy1-wCgmJRlE0yzPdBI6YNQ5MSCpXzxkiCV1I5A9bfWBKPGLEGJL8g_VEIfrUzIpIgnB3HlHAAUdf-sCXNjXixe6A_nRR4Acq679peUrHAnKdwjSNWQgWYuyUZr9ijh0_ALZst32wHDfbiQXR5ZCNpsWhxlDNZsIRK7VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سردار رادان: بیرانوند از اول مهر سرباز است و شامل سرباز قهرمان نمی‌شود، باید بین ۲ تیم ملوان یا فجرسپاسی انتخاب کند.  @Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/461846" target="_blank">📅 19:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461845">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTKsren-PZSpNBXCoOSkYtP83yL3kXafg2w3Hq0SjrnFPLlKCHkpgQRNaWvIpID1jfZGQ6oyNN1iRaL5e3-xdYkBi1D8oQEHmUwBYC8Fla6kC5TT_egh93T0AwLH5oMcg7iHG8qcxnmjsjGK9Cd8PAnu9TvVlvQaYGpaeuR0bXHYDskTjNuNxf7aViH5zYY3dsPmAnPty0PimhWdA8HoIsjdJ5egyHU-E8El_VpaVfbOjLQ9XIdcuc8PtAhap2tUylGtn67cALLbxDkiOiMsct8h5mCLLxYewy6M6TYEX5SDwPwvmg7haJwoHRfKv_3oc69AclxaP_ovUkJauDxfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخلیۀ قطار نخست‌وزیر اسبق انگلیس پس‌ از حمله پهپادی در اوکراین
🔹
مجله اشپیگل گزارش می‌دهد که چند سیاستمدار اروپایی از جمله «یکی از نزدیک‌ترین مشاوران» صدراعظم آلمان گونتر زاوتر حین بازگشت از اوکراین، یک حمله پهپادی را تجربه کردند.
🔹
علاوه بر زاوتر، مشاوران امنیتی از کشورهای مختلف اروپایی، اعضای بوندستاگ آلمان، دیپلمات‌ها و همچنین نخست‌وزیر اسبق انگلیس بوریس جانسون نیز در قطار حضور داشتند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/461845" target="_blank">📅 19:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461844">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewq10XHReVBnVtT9B5ZnL9UZVyuTl0A3ERHdfx7WwoTxVXM9L98195GIFsbYNJ9DG1cHeHeUlMqJCvpZ2OkJzRrnFgT8yizddKLzVkwWBvB67-d_p4E0StVvkAqytVIpSRIagCJKNJFQZ9QGioZqhfP8L6v4jzL2mTScayYi1aXl75nd-NS2z_UWgZOCMVsLyPwhQRRsiP3AYCILSjkXwNQiAST9JSoLf4FRruxSodmC93d3uWK_XpIhxgE1uk_FXLrhSf8pLaDUAArfWZYnAeFWWVeAVjPltdPA4hx7t-XdnV8ZCP_fyhcS2xIVX2g_qX-QYYoTpJ-AHJ6LKICX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رونمایی از لباس استقلال و السد برای دیدار فردا
🔸
این دیدار در چارچوب هفتۀ اول لیگ نخبگان آسیا،  فردا از ساعت ۲۱:۴۵ در بصرۀ عراق برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/461844" target="_blank">📅 19:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461843">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یمن اتهام سعودی دربارۀ حمله به یک مسجد را تکذیب کرد
🔹
خبرگزاری سبأ یمن: یک منبع نظامی ادعای رسانه‌های دشمن سعودی دربارۀ اصابت موشک‌های یمن به یک مسجد را بی‌اساس دانست و گفت: تأثیر موشک‌های یمنی بسیار زیاد و مشخص است.
🔹
به گفته این منبع نظامی، علت این حادثه سقوط موشک‌های رهگیر پدافند عربستان در مناطق مسکونی است.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/461843" target="_blank">📅 19:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461842">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALO87-p8WHNfK68R2xE4SnH2-lFsEKx8PtJL2g1mUF8WcWUawGJLd2XJgBChB03E3OgeG46Ix5dPFlWuLrjHhYv7G7iV9YxlAxgX_uTQLUa6DGJVYjNnWIxKSbfeztPBNKmgesu6anvsYeSZASHyoaffX57P4EJ3QXet5mpn-_Em4GAbu6Eg2YXfJFCaGuwrDA_JWyqcOrL_FqsazWNJacAtAXuBggUOxA7BzGUsm2Rq9_Gh4mOHgVsRXOBPDVtK0Zm4F_PuMdU1Es78b5paBjDL929QFJd6htWoQ1jPwe_8Sc8VLOv5gxcLoaFv9PzM3aHXsb-TaXp3IWmT-MD_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک شیر دریایی بر اثر آنفلوآنزای مرغی جان باخت
🔹
ادارۀ محیط‌زیست استرالیا اعلام کرده که آنفلو‌آنزای مرغی باعث مرگ یک شیر دریایی استرالیایی که گونه‌ای درحال انقراض است شده.
🔹
کارشناسان می‌گویند گسترش آنفلوآنزای مرغی H5 می‌تواند باعث مرگ‌ومیر گسترده در حیات‌وحش شود.
🔸
مؤسسه پاستور فرانسه پیش‌از این گزارش داده بود که آنفلوانزای مرغی درصورت جهش می‌تواند قابلیت انتقال به انسان را پیدا کند و یک «همه‌گیری شدیدتر از کرونا» ایجاد کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/461842" target="_blank">📅 19:07 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
