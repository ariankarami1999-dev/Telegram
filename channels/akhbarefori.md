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
<img src="https://cdn4.telesco.pe/file/YHQZN0z1707El812QT5YjPaelTgvKnaV7QdqERTlfoZ22OW5IGIvK4TyHKWzy0OA-6jCJ9SGjiGTCFCc_9HT0qbYEj7ep7jInbB39dCQAQPLe9xYmxC9E8Mu56BG-WYa-DYgq-Jvt7t1pOYaHoVdp8xwEh9Y6lFSLCjIT5JYpHVXexTSYic-YXxV1VOCa3xQfHfmUXAsRZA_gA7SPx9GVVQjpJ7DWE4e7dnoZw3lVBq4KSiFgi5kZYNNpSOo5XWc1dpXqOj44DPDNLIsZ64QD-dtmaCpeoC0EwBSUv0zHZgO67hxf9RUw2EEEUP0YLN4cQNolsDC9gu--aNb1NjAHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 00:25:11</div>
<hr>

<div class="tg-post" id="msg-697345">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad06787544.mp4?token=WBx0n5mENjRxlP3AiYtDSM5YETO-JFBIav0Hexqjd1hodHZ7eXvG3HejouYq5WLdlt-SkaRTV6F6uX_AaiU_Qydxe2EAipefq9t21z2CatNxTOOTImD7kathhcRK7bqG04tdNDIcgUVGmStg4uji6QSJM_Z9jHQlHFrzPdE4x-zgRRS0Ww-0Ixh7KdIl0bfTOsHzUifFWxnvcrFOpfjKhk_n4fM5dvx98pOL4mItaEMR7Qn9G6Pz_ziUTkE2c2PONVd0ftdC1ddLM1z3F2izkJxX6WLNBWBP1NE8YNsReXdMCbYlbccYuu-5sprbm6by9LSRsTrI4Dx1n6Y6GwE3yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad06787544.mp4?token=WBx0n5mENjRxlP3AiYtDSM5YETO-JFBIav0Hexqjd1hodHZ7eXvG3HejouYq5WLdlt-SkaRTV6F6uX_AaiU_Qydxe2EAipefq9t21z2CatNxTOOTImD7kathhcRK7bqG04tdNDIcgUVGmStg4uji6QSJM_Z9jHQlHFrzPdE4x-zgRRS0Ww-0Ixh7KdIl0bfTOsHzUifFWxnvcrFOpfjKhk_n4fM5dvx98pOL4mItaEMR7Qn9G6Pz_ziUTkE2c2PONVd0ftdC1ddLM1z3F2izkJxX6WLNBWBP1NE8YNsReXdMCbYlbccYuu-5sprbm6by9LSRsTrI4Dx1n6Y6GwE3yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روش ساده برای خشک کردن کتونی و کفش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/697345" target="_blank">📅 00:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697344">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=T7dpEsEcht9sVB5Pe-jnq3mPKAkHgz1LVeKBtN3INs7iWMv_rSwP1mRW1CggyzY9ZdHl7XUjtK0fjGTwGHbJ_6LpWQD9C868-7O4m8upN4Ojii79r30c3AaVwEWW3nhBXy4J3uRHKpKDeXpfhJ9EXlpH4eAVb25VSp-p_VImaabA0jR1tGYDlRXFfa4VqnQFXLAfWNK84vpLa3ZBu-VdaFljKne698vf89ZkOxolsF0cP_rd-uT40B1P11KUC_gmQ5Z-t56AfRd0gxpFoFqDUFAvw7akob_lfyQnoeEBhANsLxpSL_3OW7K3iljbTSUm19AS9CXyfmmFw3OTP8-ijg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=T7dpEsEcht9sVB5Pe-jnq3mPKAkHgz1LVeKBtN3INs7iWMv_rSwP1mRW1CggyzY9ZdHl7XUjtK0fjGTwGHbJ_6LpWQD9C868-7O4m8upN4Ojii79r30c3AaVwEWW3nhBXy4J3uRHKpKDeXpfhJ9EXlpH4eAVb25VSp-p_VImaabA0jR1tGYDlRXFfa4VqnQFXLAfWNK84vpLa3ZBu-VdaFljKne698vf89ZkOxolsF0cP_rd-uT40B1P11KUC_gmQ5Z-t56AfRd0gxpFoFqDUFAvw7akob_lfyQnoeEBhANsLxpSL_3OW7K3iljbTSUm19AS9CXyfmmFw3OTP8-ijg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم برای هزارمین بار: ما در حال بررسی این موضوع هستیم که نام تنگه هرمز را به "تنگه ترامپ" تغییر دهیم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/akhbarefori/697344" target="_blank">📅 00:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697343">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5bf2df414.mp4?token=SiXKT5vi5xEkjNzUfLuuWm3vUcS8Qy_KtlOg5-Te_CQ09zTdjJ9COxj0bNP1d2ZcsWGEpe2wE-nLC4jJcftwTA0x3dTneLgqnUElS7TLwgDQymSWdPs4H0Ks7M8f2u4DyWjluUuQjK7HELSKphpQoVmYyLNhctguogVDQzOBYXaABeJGWfNOI9xqqWE93ozDXDtqURNWkLPXhdk14p9OpByecQy4s5MY5Db8kvnNrP4vUy-HuBAPuDS-CnIcV1oHZ12JErs-BiM7Tdx3InxhG8UIs907HtDruNUZSxyQy2MVyabOMVONTi_5IkmlJXilCR6SsxliomeXFsKD2rwR6kp6mz_hEnidDfZucAddmKMYheC2u-b_qIf-mFZxMQHYI6MUukK-2_DBDlioPU1-Jqj8NL1C3x4vz3PuB4gmy98E5cnYHGxDt4v5Z5r9IEcAlo4-jTDpNBVryR5ucKlWd9DAAZINagcHkViPWT5Kqs0aS-zvuVNCV-ioCA9qHq_Nnn1Z6LDg0Ke6f_0ZZihn2krm-26HqN1kjohmWESmbV9_my-ARxMYzu2oZvTQxa73HxzMRlAPl8c-advw8Qt69-zVA0MMfUHpRGB3eLxX9Mi71GG6PBSTEJn-fkWUmnNHIoKybZXM_ihQfhpP_vWJBpDqQHPJ_WyaXeQAiTtQ0dI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5bf2df414.mp4?token=SiXKT5vi5xEkjNzUfLuuWm3vUcS8Qy_KtlOg5-Te_CQ09zTdjJ9COxj0bNP1d2ZcsWGEpe2wE-nLC4jJcftwTA0x3dTneLgqnUElS7TLwgDQymSWdPs4H0Ks7M8f2u4DyWjluUuQjK7HELSKphpQoVmYyLNhctguogVDQzOBYXaABeJGWfNOI9xqqWE93ozDXDtqURNWkLPXhdk14p9OpByecQy4s5MY5Db8kvnNrP4vUy-HuBAPuDS-CnIcV1oHZ12JErs-BiM7Tdx3InxhG8UIs907HtDruNUZSxyQy2MVyabOMVONTi_5IkmlJXilCR6SsxliomeXFsKD2rwR6kp6mz_hEnidDfZucAddmKMYheC2u-b_qIf-mFZxMQHYI6MUukK-2_DBDlioPU1-Jqj8NL1C3x4vz3PuB4gmy98E5cnYHGxDt4v5Z5r9IEcAlo4-jTDpNBVryR5ucKlWd9DAAZINagcHkViPWT5Kqs0aS-zvuVNCV-ioCA9qHq_Nnn1Z6LDg0Ke6f_0ZZihn2krm-26HqN1kjohmWESmbV9_my-ARxMYzu2oZvTQxa73HxzMRlAPl8c-advw8Qt69-zVA0MMfUHpRGB3eLxX9Mi71GG6PBSTEJn-fkWUmnNHIoKybZXM_ihQfhpP_vWJBpDqQHPJ_WyaXeQAiTtQ0dI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توهین ترامپ دیوانه به ایرانی‌ها: آن‌ها یک کشور دیوانه هستند. آن‌ها این را می‌دانند. من همیشه به آن‌ها می‌گویم
🔹
من می‌گویم: "شماها کاملاً دیوانه هستید." و آنها هستند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/akhbarefori/697343" target="_blank">📅 00:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf28c3f20.mp4?token=bJuh-o25xwH1wjrghUCRaq5sc3aDMf3uTmRqrOvMkpKAQ6ywoX-HEjm6dokUPF5ZqJTpOVBzObpUKlu5uMvzAfXw1B-AEVjAbkkyWragWJrfJ7r0OautfENC7BdLsuXMUi5E45rgy8zn69lJVB9yKsTn_bGXpj3-LtogCFSwUmrkHifEIrfS7yoCd6XquziKm5dmboaIT6ggamCAt2PCnNtf6kHx03Axu6Qkp5lOp8yXbLy8I8tkp9YiT8T6Zh4Mj8w_MHDsqfoOi-Gvigr7ZCIRGjKC5YVlBKb_HrNcBtH2yXwSrf66-BdWn0deoMroIYp5Jyswig4Lz04MvR4J9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf28c3f20.mp4?token=bJuh-o25xwH1wjrghUCRaq5sc3aDMf3uTmRqrOvMkpKAQ6ywoX-HEjm6dokUPF5ZqJTpOVBzObpUKlu5uMvzAfXw1B-AEVjAbkkyWragWJrfJ7r0OautfENC7BdLsuXMUi5E45rgy8zn69lJVB9yKsTn_bGXpj3-LtogCFSwUmrkHifEIrfS7yoCd6XquziKm5dmboaIT6ggamCAt2PCnNtf6kHx03Axu6Qkp5lOp8yXbLy8I8tkp9YiT8T6Zh4Mj8w_MHDsqfoOi-Gvigr7ZCIRGjKC5YVlBKb_HrNcBtH2yXwSrf66-BdWn0deoMroIYp5Jyswig4Lz04MvR4J9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
التماس ترامپ به جمهوری‌خواهان برای رای جمع کردن
🔹
ترامپ: اگر مرا دوست دارید، بروید به من رأی بدهید!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/697341" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qee9A6fmwVYU-aJ4_d-pGV920HHNiQj1Y74VeTP4vpITHJ69VrdOho5KMSTsao5fYuMMSt7oLMdz4f7JjljshtpXHWB59LbAF62szw-BHRwBL3Y74H-uXdQHfkHpQSULR8bG5ItCM1tzq-wtSyhgWPguTQtpHNoz0iTIG_mhFIQxeeiFJCCJirt23_SGR9zU3bAEl_vVnKrNUwIN2LLeYtKG_sNOkoA76uPWY59hinnU3WQ3tjB0rAnDikR6ASpgvH_jc1m1NE25Nw4JXn_ClpnLTuX-6LzgLwxHH8aIysNBvoGURnm_g28uLkSvrXgmF52OWVQEdiG17sFV8EH5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/697340" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697338">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ جنایتکار: آن‌قدر محبوب هستم که جمهوری‌خواهان پیروز خواهند شد!
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/697338" target="_blank">📅 23:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697337">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6364787c11.mp4?token=TBmYbJ2HZHmlGFL3S3oiaUn6J8X7goyP6x8Mv8PebVtsVO2C2bE-hKVK_hwgB7DpOF1bACkgGX3OriGBSiwJZwpdaIChe5EAGvM9ePuPPXQx8oZGrNATmT3ZwQd9zS89uk3ctyFHP6TFbq52meMFvJuc1UbNCPdlPj3QajxKUzp-1rcsqX0xq_SAdRSUpwFvYUp9ILVVJkhATC8mvFlSEges3ClaL5pjR5GobH-3wsDGPB_XfnheX1WRhPlalS31sEZ9fiW-8TDfLcloIbWdExIuATB2-F3J4nvzD4Y6UuCvSCM2X4sgmojuahtBcaZVXjUzSgvapKxXQzWF31Id3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6364787c11.mp4?token=TBmYbJ2HZHmlGFL3S3oiaUn6J8X7goyP6x8Mv8PebVtsVO2C2bE-hKVK_hwgB7DpOF1bACkgGX3OriGBSiwJZwpdaIChe5EAGvM9ePuPPXQx8oZGrNATmT3ZwQd9zS89uk3ctyFHP6TFbq52meMFvJuc1UbNCPdlPj3QajxKUzp-1rcsqX0xq_SAdRSUpwFvYUp9ILVVJkhATC8mvFlSEges3ClaL5pjR5GobH-3wsDGPB_XfnheX1WRhPlalS31sEZ9fiW-8TDfLcloIbWdExIuATB2-F3J4nvzD4Y6UuCvSCM2X4sgmojuahtBcaZVXjUzSgvapKxXQzWF31Id3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیگه سراغ نسخه پولی هوش مصنوعی نرو، از این سایت استفاده کن
🔹
این سایت تقریباً همه هوش مصنوعی‌های عالی رو داره و به تو اجازه میده که از نسخه‌های پولی و پرو راحت استفاده کنی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/697337" target="_blank">📅 23:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697336">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6bbfd36c0.mp4?token=jWvkOHWNPNLTeUoAFGJxMkiIWDs0tW491Ad0VPMCbWDvHRqTbg5h3qTIiVXIQvGX8Ren65foVfBBui65CY54RlgG__2PtNmwx9wYD4txpPNiusqIbs-EGrkr0z_K00JrQlaOgnSnR_0WATAsjrOptuvURJVk9KERLRoDY38IDVebaYmLnbgZZHaKP6U0Os38hgTd3xMJMdkwYDaZeXhT8WMaxLvvtGfPxHkv_r4k2XMOgeD3AePPFwQt_ScCsY5KFosVVe6ig6ekg_Gz7MyAxULHoX3LIAERhvvMyCLDtVeXspysu9_fnx831Ki1TPAXqOtpmeSlLmJdEP4jkp2Y5QYNXrzkyHxI3zDp4uMSYAvUSQAzWGuo1hMeQnVXgXyRGIFBNHVqtUKQlB9Co9Hvgq9p4v5wq7HulOiJ5IFs_L8va7B6lsn0saEu5E7i06-NKhIiOwWnA_Ozhc4J0H5Pnid6zvcQt6tD_my0XA5P7IxaXZBNyHrJDTTfSrIk32rF174wmMWvtItpc8FeNf22a57jJo6p_tWRNYI-ffGkgQRQczojklYx2K5FhB_fzTvnejdNoO-29sMugcJ8OMLzTdWAjuAUY_uyB0Yc3sKgaskBjd2yGToQ5Mzh5kvE1We67M90SY305wvs3hUd0E2nR6tjYZSvC26nF7X2MQxQ3a0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6bbfd36c0.mp4?token=jWvkOHWNPNLTeUoAFGJxMkiIWDs0tW491Ad0VPMCbWDvHRqTbg5h3qTIiVXIQvGX8Ren65foVfBBui65CY54RlgG__2PtNmwx9wYD4txpPNiusqIbs-EGrkr0z_K00JrQlaOgnSnR_0WATAsjrOptuvURJVk9KERLRoDY38IDVebaYmLnbgZZHaKP6U0Os38hgTd3xMJMdkwYDaZeXhT8WMaxLvvtGfPxHkv_r4k2XMOgeD3AePPFwQt_ScCsY5KFosVVe6ig6ekg_Gz7MyAxULHoX3LIAERhvvMyCLDtVeXspysu9_fnx831Ki1TPAXqOtpmeSlLmJdEP4jkp2Y5QYNXrzkyHxI3zDp4uMSYAvUSQAzWGuo1hMeQnVXgXyRGIFBNHVqtUKQlB9Co9Hvgq9p4v5wq7HulOiJ5IFs_L8va7B6lsn0saEu5E7i06-NKhIiOwWnA_Ozhc4J0H5Pnid6zvcQt6tD_my0XA5P7IxaXZBNyHrJDTTfSrIk32rF174wmMWvtItpc8FeNf22a57jJo6p_tWRNYI-ffGkgQRQczojklYx2K5FhB_fzTvnejdNoO-29sMugcJ8OMLzTdWAjuAUY_uyB0Yc3sKgaskBjd2yGToQ5Mzh5kvE1We67M90SY305wvs3hUd0E2nR6tjYZSvC26nF7X2MQxQ3a0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش علیرضا خمسه به کلیپ معروفش در فضای مجازی: به خدا من بادیگارد ندارم چرا به من فحش میدید؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/697336" target="_blank">📅 23:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697332">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sg1J4y8n1u09mGs2iwyEeb-9OgLYziXDoDyw6CHqDZoKAjTcdBBEkngePXrjgHlToPKgGK4EIs2DLVWk7tphzcW_xta6yzysN--lJfC8-t4xAdKpLLtYhUHDPIIRq6y7B1Z6r7ILQ0OnXKAsv1SzjdwtSuh6Kh3DJX8bUeFkhYIvJpixcpyEhPegjKUvPn_fuZZeKL85fkQqZHsXblWPMfzJ-WupHkuheq_mOsDkYemuOvFIp0LEUPz5OvLzcYITLXl5G7UzODRTxuHM0AmYk5W55pKKWqHJovs0jm2f95pImYi0FP_VSUbQDIRg6yiYUZMDEVvrqVhAtMjfI3U3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWrfWpig1CH-fVhh7k-US75tpFM5TpoCexc2YcD9Y_HMuxFzTysZ68X3WwG5VgEp_IK815Y8ll8cIclmQwLgku5-jFPv7GmGzFz7TahVr-Ct3WKGWhzG6nt8-KpRyhIcFFNBCU4hcx-FjtnbRUIykLBn9L7KlH7Il_dzZqh5VICMj16umy-kw_Pr51nr2h4jvVumBt6agQrZFyStZtMQSZihIV-D-Y_5yiF4_HJFp4yAuRFQE_KFO0Pfnkfjx_N39919d7EOM8-E-CqLkfMm02945fQigXiE5fDCt3zRA-ucHz-1tphip5ss2j2MIB_78E0g_65PHpN5HV09aT2SQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcCKpf_xdGD9fIRhL9pPPZ39oF5Uz_kgFxosux2zhL06rNeHxA57WYS3NtCFTM33QDnC3r7VZ3x7B2MDwHkNTBdSLxQsWTloLQqWV4UkaUrmeT90PUDonG-8-d_hU0tgww_IlJyeZ0DYRVjrlcM8uLKXa0fBwrjk4EcuCm4t-9nKz5KYNyZ_a2XmfmHyZh8tAK4-7ZIyLzp2FlHbfBcBPCTj9XqU7DGcO1yQ-faGAXgyuKOapRYJckDRajUCOCfmQFQqoODa3l9JG0bqtgrTVVNbIs8BqyS8833z6cfIxQr6G4oV2YG5IgS4XG5eMoO0-46kEuMe8LcMuR4essf_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUGnNHHCVfo7icJYGXU9PaBMw5YGRrfV9yThF3QkPgaWdi1SWMgv4oCzH9DEDZz8OuYhGS9g71eahj6xbI-tTGhijEFOuIVl9jMF8O3E23uPu9JO2fS0rWvi1Rwd6VkUsEgwjwvi5LfhTF21-iMvnvJmcTw5dNYKvUuCJJ-jh_kqnxWCR1olZxgCkLzJp0lg5j0OTgdFC1pESdVe4a_H73VX3TjA6eZYIQ4FYjYz-OsZKEQwFkQ9J5XLgoG6nY8doGl46R4xrqCO91ufiD5OQJjA3bLbRmYDTBTsqGAn5h5xqrAhYEHYCMPiC0BJTfKzsvXoViCUSkMJkKLB2hkkbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نام‌گذاری خوابگاه جدید دانشگاه تهران به نام رئیس این دانشگاه!
🔹
خوابگاه جدید کوی دانشگاه تهران که کلنگ احداث آن سال گذشته زده شده بود، اکنون به مرحله بهره‌برداری رسیده و در اتفاقی عجیب و جالب توجه به نام «دکتر محمدحسین امید» نام‌گذاری شده است.
🔹
محمدحسین امید هم‌اکنون استاد تمام و رئیس دانشگاه تهران است.
🔹
گفتنی است این بنا، یک خوابگاه خیرساز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/697332" target="_blank">📅 23:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697331">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
خبرهای منتخب هر روز را در وبسایت خبرفوری دنبال کنید
🔹
🔹
آمریکا و اسرائیل چه زمانی به ایران حمله می‌کنند؟ | حرف نتانیاهو به کرسی می‌نشیند یا ترامپ؟
👇
khabarfoori.com/fa/tiny/news-3251392
🔹
جنجال «ستاره داوود» روی کفش دختر رضا پهلوی + عکس
👇
khabarfoori.com/fa/tiny/news-3251299
🔹
آزادسازی قیمت خودرو؛ خودروسازان برنده می‌شوند یا مردم؟ | بازی تازه با قیمت‌ها
👇
khabarfoori.com/fa/tiny/news-3251284
🔹
طرح ایده بنزین ۲۵ هزار تومانی؛ نظر شما چیست؟
👇
khabarfoori.com/fa/tiny/news-3251426
🔹
از ادعای تقلب انتخاباتی تا جنجال قرص سقط جنین و آلمان نازی | کیتی زکریا کیست؟
👇
khabarfoori.com/fa/tiny/news-3251302
🔹
صفحه ویژه اخبار داغ خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/697331" target="_blank">📅 23:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697328">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjW5ybzjjmqU1VeKTaIDwhdSLCplQxlg5kn7_WggEs18KbSaYSYzHR0lXIRGbQ5wMGh4IZTQwY5uZiENHFNyMjIv740GaGQUXkMTozs4Db-QfyjlWq0TJ5p7fxzd8lhYnB8IUQZZ8HbJ3uTGkv59t_CpHQAjl5AFfufwN3H6JhYD3g1_zZv3flhAkHfGvE8PlPRimkb66WCRMHEVEIipzHcsl65ZXSOSzVewuDPOe1ko_ce1IRDK74M8NbpOoNhsiVmvztlyYjPlFQtjlaVn5Lr4J0dkv1VFtHu0tEb0vxX6MOIDwKxjK3mPqaCq21K-ClJSz19bcSyBBRT1SwbU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBDxSbXLoXxB3N-G9aJX2J4aIcwFpOoARNof-1y-t5n6-j4N2Te46q8UkdasTW1yBoR3EoYhfUGphtG8-vBTZWOYxzPKcY0HuiqIJpZLfT2atcsmO5hqLHLTG3w2Wx41lfKaRdsWiQN7y4LFF8ZACZ61k9fk-QoYhTf6ehaHY5vlMHS6GAq3hY60hlw8zc9Re7u4oXGENM9Blb3JWliqJ_yD__GQLDQU-_YUqxkFMybzYrFaa4zYPpdv7S8Uy8fBhSHiST2TPV7JYgaHHIFJTJiGoptP3AMiqaeMGwVnLmoAXKNctBxw_XZvNdiWOiUqHwTqlmWuamMIS1S7IikXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYGRG27tDR77sarD2r7zG6W2zsAT16OqYUhQ2ouFbAFMnNgKI-8gY017Z0nK68w383dhTU-rioTV1iaIe9zjhctThyC4ecXRF-pcY1HVdhcnVf4GY52cuQ2wh5_KlcSy63hIaK1160ETFtW9bsaMjwoK5eiU2jor_sAypxBsR-ZCgUfxyPDjnBra7DFwZUVeYKEtmMl1nNvOm-SytOTXTjOuN07GVx-q0s1uj5FyTjJn-3aT_2QtMY1Gnr1aaoAwFXGBPhnCw6CS_V8D4zi9sui_kP7WLC6iSLEyMtQZ0r69aZiKgW5_51e8C0un85jFcFHGVQOUzqIfM_tNpqvfFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
زنگ تفریح چی بخوره؟
۶ میان وعده ساده و خوشمزه برای مدرسه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/697328" target="_blank">📅 23:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697327">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
بقائی: دشمن واقعی مردم آمریکا مسئولین جنگ‌طلب خودشان هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/697327" target="_blank">📅 23:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697326">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
منابع خبری گزارش دادند نیروهای مسلح یمن در حال پیشروی در ارتفاعات «صبر» هستند که مشرف بر شهر تعز است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/697326" target="_blank">📅 23:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697325">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541deac5ff.mp4?token=npEPi7mf7gC_YIKzq53W-F2ydWeu05c3ClYVywfskJDwpj84aE6d-Tyi0W9DXIrSaHvodxX6xHM6RuRI9UGFgjeJCz7xtbEMvw0cUVlCD393rSrVZuxmZp3yPEaILaHPh59NadxNCXgkEjzwCtkXngAl0RE4UuG87JRuu3j0larWqqJEHe8pjnrEPajfJmMWEoktRyoAdgTB9ETR7zD-G_Z3yjGj2NQv5RF1DQFAJHw2W--CW9C-1_DvxWKhLF3XOhExds7Zc9A1qub_RKLvJc0Z4ZbdFQBUxUa-Iu40gzQxbdR63csDirdTKeGO7TElZnGMK9Y-TflUuv4y0X9Nww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541deac5ff.mp4?token=npEPi7mf7gC_YIKzq53W-F2ydWeu05c3ClYVywfskJDwpj84aE6d-Tyi0W9DXIrSaHvodxX6xHM6RuRI9UGFgjeJCz7xtbEMvw0cUVlCD393rSrVZuxmZp3yPEaILaHPh59NadxNCXgkEjzwCtkXngAl0RE4UuG87JRuu3j0larWqqJEHe8pjnrEPajfJmMWEoktRyoAdgTB9ETR7zD-G_Z3yjGj2NQv5RF1DQFAJHw2W--CW9C-1_DvxWKhLF3XOhExds7Zc9A1qub_RKLvJc0Z4ZbdFQBUxUa-Iu40gzQxbdR63csDirdTKeGO7TElZnGMK9Y-TflUuv4y0X9Nww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا تاریخ هنوز نفس می‌کشه؛ شکوهی که قرن‌هاست پابرجاست
🇮🇷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/697325" target="_blank">📅 23:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697324">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc894d84a8.mp4?token=DkbdPxgF3ayq9XJMGq_z8CVcSDjFxLtQ3aNbC15tzJ3QyMiU17BVSaPNVspkDYIn7awndUV0dX5WAqR8Cmeq8vyiRGpXYgKU5Lr0Y9xG-TlDBySjDd2fuQCe9wq1MFE-9u6461Pf94UeyppFxWXsZb_KAm3rmVLiKvtmvgts98maM6ilcLxHVSFGpi_03BEbjtV0XV-uJ6eoiCAw-VGq13Y1zJNi3tTmvowkPV-T8_50ik2bJo4wEeeSxhL-yIUfC_G74UTnth101l3GDwsxrxnwHUH-ur99IZ_PZtILiWIeey-f3mzDgDKilg9AYWX_tp9_H0WGRUZegbDYC1doyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc894d84a8.mp4?token=DkbdPxgF3ayq9XJMGq_z8CVcSDjFxLtQ3aNbC15tzJ3QyMiU17BVSaPNVspkDYIn7awndUV0dX5WAqR8Cmeq8vyiRGpXYgKU5Lr0Y9xG-TlDBySjDd2fuQCe9wq1MFE-9u6461Pf94UeyppFxWXsZb_KAm3rmVLiKvtmvgts98maM6ilcLxHVSFGpi_03BEbjtV0XV-uJ6eoiCAw-VGq13Y1zJNi3tTmvowkPV-T8_50ik2bJo4wEeeSxhL-yIUfC_G74UTnth101l3GDwsxrxnwHUH-ur99IZ_PZtILiWIeey-f3mzDgDKilg9AYWX_tp9_H0WGRUZegbDYC1doyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط ۲۰ ثانیه؛ تمرینی ساده برای استراحت چشم‌ها بعد از کار با موبایل و لپ‌تاپ
👁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/697324" target="_blank">📅 23:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697323">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrPQRgd6Kkq9KXM4E47vXKyLnKT6H-iB7xpfwUCXAMdxtqSeau5PBy-zwwIr_XWq5IojYFFO5uYCbFfKqCjCKrHuLyYSwmSvqQ-wwMz4znUIipm71HnaChp_2c4lDrCYmpPL0DpjzaiuHxGR-MWbyQDhu3amNdLK9C0PHQcUI5CjnSGoMeb0Qiw3u2lpA4Ce-ArC_ZJs8bVYvW2-5MAoAznZ2j2dLoodIC2oY7bN-WjeFjALAo9rFWrrTXfZDw5YMvIVLwnuLK_uERDJ9OwRx3_SC7cCoqCADhe6rN7fQ1E-xZgH8k-FSK22CyJ_46xqRYpvV3O0CgxRTapv_JVT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نظریه پیروزی ایران | تهران چگونه می‌خواهد آمریکا را شکست دهد؟ | سه هدف بزرگ ایران در جنگ با آمریکا
🔹
ولی نصر، پژوهشگر روابط بین‌الملل، در مقاله‌ای در فارن افرز استدلال می‌کند که تهران با وجود خسارت‌هایی از جنگ، خود را در آستانه شکست نمی‌بیند. از نگاه ایران، ادامه مقاومت، افزایش هزینه‌های نظامی و اقتصادی واشنگتن و فشار بر بازار انرژی می‌تواند آمریکا را به عقب‌نشینی وادار کند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3251365</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/697323" target="_blank">📅 23:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697321">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DHpcgf0VIK5YypuD9PkNixL0LJNEq7Z6HF-GCuPktJ52gsdUtiILhheVpqj7955EnuW_e-xKvXp_EvWfLS1KSX7zxW_BBXAUSFPvZZPQSkFkiCUn6iaQQVc0Q9oPQDtyuvikwt0uvyGLxS_8bw5PwXMFoP2U3XS4BZW_SJNp_5X4QecHgJuNceIPYwDNewod6ZJTSOITMdEUxTCL7EDzA5oA_kDso_YW2-ELY8TQT-R7ojDfPJD19hzYYU6WBG9KlGy-Or4ncb8HfldgdpHEAwJceVn1_BEnVuB1tiw7zflzzEpk7-mr2WYJgwH69Cas6Ii0UZhnNr46wDce-DK24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7aoiy9vt-AfjbR_UWBmv9Q8WhD1Jo82aZ7tqOnbxVHg4Tn6HJa8VHN8Zqe5VHYY0ri5Mmy8rxdrL5dVBjGBYyNNuaSKeIlPvFIEpd_AFHhQleif-2ajad1epVQaUO7wW5kaxCDVt8xV-KKvTBu-sXvAgK9yeMxRGHMDGbEIJTfTPbSaXhEZ_58LErxpwwjvKrIBbQVfHtt6iKquQfJCVxHoW8yspSsYHzIpaUZ2JWS1egKnF9n125xkBDqUQWJOm0JcdX6Moul-sVimSyZ3fSnXfSXPbA44Bi83KwEhQ2_Gk_AVDrAi5pD2FaHXBaq68ccpdMZmBnZ7Z2qiXeO44w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نیروی دریایی سپاه به شش کشتی در نزدیکی رأس‌الخیمه امارات، هشدار داد و از آن‌ها خواست لنگرهای خود را بالا بکشند، فوراً منطقه را ترک کنند و به محل لنگراندازی کشتی‌ها در دبی بروند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/697321" target="_blank">📅 23:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697320">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 11- میدان یازدهم، محاسبت</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/697320" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح کتاب صد میدان خواجه عبدالله انصاری
🔹
میدان یازدهم، محاسبت
🔹
در نهان انسان هوشی قرار دارد که یاری‌دهنده‌ وی در شناخت خویشتن است
🔹
اشتباهات زندگی و گذشته‌ شما تنها راهنمایان بهتر در راستای دست‌یابی شما به تعالی هستند، بنابراین بابت هیچ‌یک از آنان احساس شرم و گناه نداشته باشید
🔹
لذت‌هایی که شما در مسیر خیر و نیکی حاصل می‌کنید، باید مشخص شده باشد که در راه شادمانی خداوند است یا خودتان!
محاسبت را سه رکن میباشد:
🔹
جنایت از معاملت جدا کردن_نعمت با خدمت سختن_نصیب خود از نصیب حق جدا کردن
🔹
حیلت شناخت رکن اول: هرکاری که دیو در آن نصیب است جنایت است_هر معامله که در آن جور است جنایت است_هر عمل که به خلاف سنت است جنایت است
🔹
حیلت شناخت رکن دوم: نعمت‌های ناشناخته همه خصمان است_شناخته‌ی شکر ناکرده همه تاوان است_در معصیت بکار برده تخم زوال ایمان است
🔹
حیلت شناخت رکن سوم: هر خدمت که بدو دنیا خواهی آن بر توست_هر خدمت که بر آن آخرت خواهی تو را است_هر خدمت که بدان مولی خواهی یافت آن قیمت توست
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/697320" target="_blank">📅 23:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697318">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/697318" target="_blank">📅 22:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697317">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68624ed81.mp4?token=Tp0BQUWbolPc48POwacXvc5ZFVLfX4ajT4E11jQw5_9seVpc5qhR0OVMrQH6HtA23UXQGYSkVYq5fTeNVOz_jznaPBEx8ILNJVLCW1QOd1Uui4210wjzfJXHRvxy9WlQvXwTw3j2N-ilAaUxDg6aqIXAZv2J1x8u-SAaKhYWe9GUwXY-y_BdNv2d3RafNNjadxhoKhBgt3scGPqi-A8lKgUCjXTy28bsInvXTi_gYD0HfFqnaZdrrq9zhRed-EdemmvfxRj6xqwzuaB6IYj_-7YKN3b7nCon8RqRsEQsMD_QjK3cs5qUzicCDHv8PZyFMNlaYFAn4jhoUXG7mYValw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68624ed81.mp4?token=Tp0BQUWbolPc48POwacXvc5ZFVLfX4ajT4E11jQw5_9seVpc5qhR0OVMrQH6HtA23UXQGYSkVYq5fTeNVOz_jznaPBEx8ILNJVLCW1QOd1Uui4210wjzfJXHRvxy9WlQvXwTw3j2N-ilAaUxDg6aqIXAZv2J1x8u-SAaKhYWe9GUwXY-y_BdNv2d3RafNNjadxhoKhBgt3scGPqi-A8lKgUCjXTy28bsInvXTi_gYD0HfFqnaZdrrq9zhRed-EdemmvfxRj6xqwzuaB6IYj_-7YKN3b7nCon8RqRsEQsMD_QjK3cs5qUzicCDHv8PZyFMNlaYFAn4jhoUXG7mYValw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت قاب ترور هاشمی رفسنجانی
🔹
پشت پرده‌ یک عکس از هاشمی‌رفسنجانی که کمتر دیده شده، قابی که در فراز و نشیب‌های زندگی پر از اتفاق هاشمی، کمتر بهش پرداخته شده.
🔹
جزئیات را در این گزارش ببینید.
#پشت_قاب
@TV_Fori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/697317" target="_blank">📅 22:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697316">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOF0mY37Xn6B1vN_OQsL_ttC9f1cDd0iYcDdi5WvEla67CWi2sTFDBjUxrKTmiXBh0B9wJO8Yal4O7EnJ0xigLfoUt210M9ks4M8NPtYpDYhwrqwXsgM1DScUTFEXtrGplSEyKQbeJtsKZY_pNFz-zpLMS1zbJAy5r6JbdX1uMFdmrdL_sldOQRIU49taN4be7deFJSdAXSX64A6FlmwCdSsxnzmS7tnRpOrSpwqrnNfWB4gIPGXGVRYoKd2hv1UcDTcTj-_GxQOiYgKbkvo-2VcFHdihmTEr2mt4tRMq3vuSuj0sZCfKOnTM2C-o-mBwuV3bkJcCt35PO4gy0cpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ گل در یک نیمه!
شوکه‌کننده‌ترین ۴۵ دقیقه جهان فوتبال در نیمه دوم دیدار دو تیم سوئدی در هفته ۲۳ به ثبت رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/697316" target="_blank">📅 22:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697315">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-M1qW4QTezC3EXzVon5SuPY-PBGiOrX8Aby3kr_NyHw0KYRZbKGT6Y4fx3xynhOaUQEfS5DaJk31IN3nuJOuzXid3jzeHBoVG764YTfEuYfeggt0yyUDx1n7GYNEVN40KiWkm9GZK8tcngIKn2lZnIsotmtVC2YkMVFgHrP-gxDPtQdJCak1SiQ6sllzKdVhD0xDwmJ52992hYuOQj2jWAQBPesXAJQna_KMGEcfg20la69_9Tp5WJioLUzmF8AL-B7zn5G5yoc5bK9DKEyyWSGBg-rYhsDYS_OiCm0nEdICxscyuBt3hKRyoGMMFWVEq1yBKZNvKHJ3tHVloBY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/697315" target="_blank">📅 22:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697314">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
لحظه به آب انداختن یک کشتی غول‌پیکر در چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/697314" target="_blank">📅 22:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697311">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری سایبربان| Cyberban News</strong></div>
<div class="tg-text">⭕️
⭕️
نخستین مصاحبه با سخنگوی گروه هکری «جبهه پشتیبانی سایبری» منتشر شد
🔴
سخنگوی «جبهه پشتیبانی سایبری»: جنگ سایبری ما مدت‌هاست آغاز شده و تا نابودی کامل رژیم صهیونیستی در سال ۲۰۲۷ ادامه خواهد داشت.
#جبهه_پشتیبانی_سایبری
#جنگ_سایبری
#رژیم_صهیونیستی
#محور_مقاومت
📄
🔍
@cyberbannews_ir</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/697311" target="_blank">📅 22:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697310">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2otabUI9ZeLiu8bZeXCiV8wjEAXWAwaMSWbMjpG17o9fV8RAFWzLUAR4PCD6yM79dq0kIy9XoBBD6mdCr02QfJdhsYqRJi4DkchHR49lesSL-heuzbUS_Jqae8U2gqEiJXnGGyV8TfLwF1t44AJJ-voAciosy5sC2X_Mxh9R5X3tok2WkSytwyTpJrqVb8tK32dzd-I2TWyqCZOaVloHZ6FRbvC17dQU1IoGbYHNyZsRaBG8mGX6S0UrTe4eybxzzuClwYd0m5yPldTcNg9NPgQRc7wzIHFIt6KrcLHU4umNcg7rQsTss-Gxu4ZQScAjoeJJTDbHQFgzOee2ee7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبری‌که همه‌منتظرشنیدنش‌بودن
❌
پژوهشگران موفق شده اند ترکیبی را معرفى كنند كه مى تواند سلول هاى بنيادى فوليكول هاى مو را از
خواب چندساله بيدار كند
😳
😳
✅
این تحقیق روی ۱۰۰۰ نفر تست‌بالینی گرفته شده و نتایج فوق العاده در
قطع ریزش و رویش مجدد
داشته است
✅
🔴
حتی روی کسانی که ریزش‌ارثی هم داشتند اثرگذار بوده
رویش مجدد مو به همراه دارد
🧬
در حال حاضر در ایران این روش بالای ۳۰۰۰+ نفر رضایت‌درمانجو داشته
به زبان ساده، موهاى خاموش را دوباره زنده مى كند!
دریافت اطلاعات کامل و نحوه و هزینه درمان روی
لینک واتساپ بزنید
👇
https://wa.me/message/F4D4OKDJSSCFI1</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/697310" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697308">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
کسری ۴.۵ میلیارد دلاری در تجارت کشاورزی ایران؛ واردات ۴ برابر صادرات!
🔹
تجارت محصولات کشاورزی ایران در پنج ماه نخست سال ۱۴۰۵ با کسری حدود ۴.۵ میلیارد دلاری مواجه شد.
🔹
بر اساس گزارش مرکز ملی مطالعات راهبردی کشاورزی و آب، صادرات این بخش به ۲.۴ میلیون تن به ارزش ۱.۵ میلیارد دلار رسیده است.
🔹
واردات نیز با ثبت ۸.۷ میلیون تن، ارزشی معادل ۶.۱ میلیارد دلار داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/697308" target="_blank">📅 22:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697307">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02434f7786.mp4?token=iuSUqY-rO9k1NwszifUTuKkiki_qlgT4yFxs3shS1D4Wsyj4-wV8FOecybZux4GrtvRUKnvcpQtadFuZrwCAVJYc_XEKzmqMLUcMH_RPLjgXfny6kyhFJBVdGg3kLJKCcwBhSfumD6jIx8V07AfcflD1Xc7BCsacTYNm1_SfbEylsIKricbxzPonN6ACa3UT8xP2jOgdeKnRhkAEeHu6usOnmiPntr8m72ReI7ZJ4c6-KMnT6uyZutVKTUQPEcp4Pc8sJImeTVJaYD8i_Ho_EEGcbnQeAh9pgJz4g2YU0ejUdW7svEJ301qB1ZpPVJL3QcIrVl6qvEB40xIf8F26BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02434f7786.mp4?token=iuSUqY-rO9k1NwszifUTuKkiki_qlgT4yFxs3shS1D4Wsyj4-wV8FOecybZux4GrtvRUKnvcpQtadFuZrwCAVJYc_XEKzmqMLUcMH_RPLjgXfny6kyhFJBVdGg3kLJKCcwBhSfumD6jIx8V07AfcflD1Xc7BCsacTYNm1_SfbEylsIKricbxzPonN6ACa3UT8xP2jOgdeKnRhkAEeHu6usOnmiPntr8m72ReI7ZJ4c6-KMnT6uyZutVKTUQPEcp4Pc8sJImeTVJaYD8i_Ho_EEGcbnQeAh9pgJz4g2YU0ejUdW7svEJ301qB1ZpPVJL3QcIrVl6qvEB40xIf8F26BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی دختران آمریکایی با پرچم ایران در قلب آمریکا پرچم‌گردانی می‌کنند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/697307" target="_blank">📅 22:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697306">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kd6Yy7bK9K-TprEHG--EM6F3EhW9xCwhskaH6VwuP29wcA7O-D6M90jGu3-dwD6Mzqam_2UM47GpbOvO8Pk0nkEW-bNFmpIYVMMfN7wkM9NKPFscEgEFsAVwRfJ6QR04oEOSXwYgzNpWA3eJVZBSLrTWo4WaKQzYvNPbP_83bhm-I3wmMSMEgEHR0d_f0RvwXqrj3qrfCoAzktcoDE2a35uCSVexENQQmXF0gK-OJm_IhdXvYC1AQeHJH96F1Y7Be2hVUdRCdfRt5jPVdNGi8XtFteqJNQnD6uFRKlI_IJr1zs8T7PklvfnXp8CY3eNb4jfm9sxHD1_Jq4uHUDn66A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لکه ننگ
🔹
مارکو روبیو، وزیر خارجه آمریکا، تلاش کرده طی سخنانی تاریخ ۲۵۰ ساله آمریکا را به تمدن‌های باستانی یونان و روم پیوند بزند، تلاشی که می‌توان آن را کوششی برای پیوند دادن تاریخ چندصدساله آمریکا به میراث تمدن‌های کهن ارزیابی کرد. اما وقتی سخنان روبیو را کنار تهدید ترامپ به نابودی تمدن ایران قرار می‌دهیم، چهره دیگری از جنگ آشکار می‌شود، اینکه جنگ دیگر فقط در میدان نظامی جریان ندارد، بلکه به عرصه هویت و تمدن هم کشیده شده است. در یک سو، آمریکایی قرار دارد که تمدن وارداتی‌اش کمتر از ۳ قرن قدمت دارد و در سوی دیگر، ایران با تاریخ چند هزارساله، هویتی ریشه‌دار و فرهنگی که از فراز و فرودهای تاریخ عبور کرده است. این تقابل، فراتر از قدرت نظامی و سیاسی، به هویت تاریخی و استقلال ایران گره خورده است، اما تمدنی که هزاران سال دوام آورده، با تهدید و جنگ تضعیف نخواهد شد.
🔹
هشتصدوهشتادودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/697306" target="_blank">📅 22:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697305">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
تصاویری جدید از وسعت خرابی‌های ناشی از اصابت موشک یمنی‌ به فرودگاه ملک خالد ریاض
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/697305" target="_blank">📅 22:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697304">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzYCz6k3R6KxiEoMPqA91FTYvORCxbO-93W35ugSJVN7lwcYuX-vNzZpYZHUj3ykpOMDwReeXb3COKIgRyClVWgD5L6SP463fRHE13PoAmaRfEVLM6k26zpC8aiGxg32f65l-nP5uILCeLLMnjplnlqoAVS0YpNWQGGjsh8Kv2m499OCS0lnYs_CfU0t89GMIdgVi6ZR3XZhn0Q0z0XjpW-RVIAMI3Zas9Kh3OSdLoeChGa8_IXgsJwp5xfxutQUFkxhQUty5uk5prrLV5oW4l8huiXSqndjNdx73i68EPv_J99xhC9VPmy53O7fvwrSH3OnVbuGLmNBLKZimU5vyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود سربازارن آمریکایی و خوک ممنوع!
🔹
توییت سفارت ایران در سارایوو در رابطه با قوانین تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/697304" target="_blank">📅 22:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697303">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71402ffc94.mp4?token=QlWE8ISf5wK0BEYDAP5CF5EXhemMoPl2rsIEdrqY7zJXnjb4ElnyB81C7SRi4GSDri0kDKlBmhZa6j2ueaM5MgBUmen_7sKveNTNbmOMsEMEJTdhIMFth-F4bF9RwUM6E1oX2FppcLBdKmG8AGy-MMi5OgPFSj8pI1bXQH_7D_l5IpuBzdeXkQvbD7EOyCVqIVuCV6jK-WN2qAASgi3GKwX5b4juLzZCLRuuveZunJRmmkokSQqerywNqZEmC8NIEB_2Fen5wXiWgQNnRGqp8L_NXgdrozuSTOnW2odEDsvR22cUNjqeav32O6j8I14dIQCqMrYSEJdSaN7sFnBGAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71402ffc94.mp4?token=QlWE8ISf5wK0BEYDAP5CF5EXhemMoPl2rsIEdrqY7zJXnjb4ElnyB81C7SRi4GSDri0kDKlBmhZa6j2ueaM5MgBUmen_7sKveNTNbmOMsEMEJTdhIMFth-F4bF9RwUM6E1oX2FppcLBdKmG8AGy-MMi5OgPFSj8pI1bXQH_7D_l5IpuBzdeXkQvbD7EOyCVqIVuCV6jK-WN2qAASgi3GKwX5b4juLzZCLRuuveZunJRmmkokSQqerywNqZEmC8NIEB_2Fen5wXiWgQNnRGqp8L_NXgdrozuSTOnW2odEDsvR22cUNjqeav32O6j8I14dIQCqMrYSEJdSaN7sFnBGAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رپ برای سردار رادان هم ساخته شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/697303" target="_blank">📅 21:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697301">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyG74Y9GnN0uoll8NzhftYxFF3NYRo9fydzCQLJQIGaPZ6qDPv6DG6sXC3l1ZzpYz40D_i_oQ6p8ZDQmRvUOXkC8opXF-7IxdNqEYZyr_3pTVNtSuqIG7tEL1VWBcdxF1GK7XWRh2hagoyBUnK6eN-JyDmLAxIi0xCznilP4WJpdtgZ-_6nlsnqUPeVs4wNJ9TJVNmT1qJ-3gLBzjKpUZYAf0l_1eFLiH4hIAWvQjfMOOjbX-xR8-_nqy9LnJ3lX0Qf1xH_P_Er-LqPjrravu1XjBGeFlJ29AGFeFzclHcEAxn1PGwYq0BjlM1SxXlo-2hHZ-2LqBdMjN90LdM_oYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206afe920c.mp4?token=QIf9fhZafAWLpK4mj8PxL4LA-Vh87nj7YPfGov5noM3kpKd56bfJge0-UHmTV30XwDzC-WcxrT2_ejXMJuxmkJ_W4T6mLnfsvexBhXLzAhFbwJ33IufKwlMIt1mGarajLMZiKX99qwIlXg43XfbKF-YdL277H5sQg4mPyFfVI8GIRjuwFAFiD0FOg3fPRd2S42DY4G6Ncid4DcuLMqczsejR9r1NccWD-KMDVAmuYO6y1nJj81mqKPCKyOP5sbjcXQRz0BAUv-U1xD7Udd3EmlERBCZGrze0V1SzGbYMifmSfHrV0hwM5dgHdSItLOYr2nWNNxX0_nsYg1NqiDTjeCPL9vHIMxGXQj7HyNiHO0xkTR1net5XCc2qqMevBJE2qDWVbi_y67E9awsJzJmCaTE87Y1JQD8i73HuZ1AkdY-rrbbSmf37qe2HCE6CwOXrvNm6Isact80AYeYpe8_HqQyjs8EFovlnO4c8PuuERPR44BB5Klq1-KG0GzkMgwhnkeGVMfBIZnCVzZAw1_Z7O41piKG_Ce0-gOkRhS0wro2ffTLY2L03n8ljXt6ZiAJtwIwi0SPrA78ZpEnja8Y1fZkpP_J-TF9fBFB4vNttyV1AlIzdpy7T8ZkEfwvPdjR_LzhPorGfGQCZ1-9zQAkVZXt2HkSCRxLdobPXvzQbGBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206afe920c.mp4?token=QIf9fhZafAWLpK4mj8PxL4LA-Vh87nj7YPfGov5noM3kpKd56bfJge0-UHmTV30XwDzC-WcxrT2_ejXMJuxmkJ_W4T6mLnfsvexBhXLzAhFbwJ33IufKwlMIt1mGarajLMZiKX99qwIlXg43XfbKF-YdL277H5sQg4mPyFfVI8GIRjuwFAFiD0FOg3fPRd2S42DY4G6Ncid4DcuLMqczsejR9r1NccWD-KMDVAmuYO6y1nJj81mqKPCKyOP5sbjcXQRz0BAUv-U1xD7Udd3EmlERBCZGrze0V1SzGbYMifmSfHrV0hwM5dgHdSItLOYr2nWNNxX0_nsYg1NqiDTjeCPL9vHIMxGXQj7HyNiHO0xkTR1net5XCc2qqMevBJE2qDWVbi_y67E9awsJzJmCaTE87Y1JQD8i73HuZ1AkdY-rrbbSmf37qe2HCE6CwOXrvNm6Isact80AYeYpe8_HqQyjs8EFovlnO4c8PuuERPR44BB5Klq1-KG0GzkMgwhnkeGVMfBIZnCVzZAw1_Z7O41piKG_Ce0-gOkRhS0wro2ffTLY2L03n8ljXt6ZiAJtwIwi0SPrA78ZpEnja8Y1fZkpP_J-TF9fBFB4vNttyV1AlIzdpy7T8ZkEfwvPdjR_LzhPorGfGQCZ1-9zQAkVZXt2HkSCRxLdobPXvzQbGBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این‌ ماشین احتمالا گرون ترین ماشین پلاک ملی شده ایران باشه
🔹
بنتلی کانتیننتال GT؛ قیمت ۴۰۰ میلیارد تومان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/697301" target="_blank">📅 21:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697300">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6726b774fe.mp4?token=BqMPzWJeUJgK2Tn0rNvsIzjs_r0BlL5IgHcBgZ1ytXId6CBsehq1I3hmoOs1P5txVIRAKkHLdxoV-KEiDjm2tdq96-_0QskR8n2XQLohl_n_PxuafR0DjOEvR9JmCEvC5yXD8v9AtwsoRXEV7Na0LHdFiFnCMRJWB4d_sSq4Kpvq2SqvCON8YZwh51_FkGL31c5tfFDcJXoODgrqaun-W9xxuCZTL6LPgkGXH6l_gw-uKj0Hgkm8G0vYSCiMlrOKFKhR85kj3Cn2uK3dezaECyZWz72uyX-UHBJmVZfA6Lkk0qg9Bxj1w-ZYHO21PGaGj4uxtPH6WjLH6LXxDG5bVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6726b774fe.mp4?token=BqMPzWJeUJgK2Tn0rNvsIzjs_r0BlL5IgHcBgZ1ytXId6CBsehq1I3hmoOs1P5txVIRAKkHLdxoV-KEiDjm2tdq96-_0QskR8n2XQLohl_n_PxuafR0DjOEvR9JmCEvC5yXD8v9AtwsoRXEV7Na0LHdFiFnCMRJWB4d_sSq4Kpvq2SqvCON8YZwh51_FkGL31c5tfFDcJXoODgrqaun-W9xxuCZTL6LPgkGXH6l_gw-uKj0Hgkm8G0vYSCiMlrOKFKhR85kj3Cn2uK3dezaECyZWz72uyX-UHBJmVZfA6Lkk0qg9Bxj1w-ZYHO21PGaGj4uxtPH6WjLH6LXxDG5bVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی وایرال شده از یک مدرسه پسرونه که معلم داره درس میده و دانش آموزان دور هم جمع شدن و کله‌پاچه می‌خورن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/697300" target="_blank">📅 21:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697294">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fIbcMVFe90mvE_R3_D6Y5gNfpE5Mg8bIvEh3j7JfjCiysGAKCSx5gSuAHNu9IQV0dv7dPMFnxyGF0D5upaGBTZ_rHcyidbYLf4_SJG5I7pcHCbvr3_zx-b6zY67YvnhTfhr-AfiiOU68gNDvCIOnFxI_Si8Ocp-c6gI9T70xm68VWy0g62zRFEAWJvzqXNe9YPAd__ODDLydA8fdpNDzBwgn9uIExCoJMmDxlTkS1P983e9zGf6ohvfyEzVXxeuDfTHlz4LhYXCHVz1tfCKLpi5c6sY6BUTHKgvgII-h6tBw08KXnvJ8A_Fi8jy7XLs_HPulsdmtUIimj3BLSTakaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5Nz_ppYaYkYsNsDM4-cig6vKdFpgVzBrNTUOa0IYUSxYkVJYxXIrv0n-mdUxIAjQEzyc1tvY_90ubpCMSsnc_VOt7eWi1EECBYBk01oSTqHVAZKxl47dnNREQUSf0cyAXMCS-y-9GszkcLmIj4akMukYYTi-jDzKqv4IPxmNpAkXdXrACj2veW8hV2HD3xOXfG_bySYvJVYqJowI3r3s6jAkdkHalKX6OSUipd3RWaEe-yBQuMoLEo7491s-zdJKo6iO4dIf3xpGj342iUjSio3YqcHwcUJEuW9XmMm-ChLQZl3RiSutBriT_xAPOVAB9jyJnAlPU8HOZAPKRrBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vG2TJ9ACSHkiiKbPrR2UR_otaBUh6bA5S6_b1-wMuHfxLywRtzJLwmPhsMh-RtU7A5Fs4wZS9Jkh2qp6OFP3iU4zSwpJ-Sc4f0MO7U66ZEmnSE2GHRZBRuInLqOAbyBIBuGuEkG-dgDHDWxGDmnHE2_3N1AKmyjVsLavJysP54TAXhEfJLi6IIo0SsTxHnt4egBOTDx0THzYtz3Nn_5cK9amvb4Ewx9E32p3h0zzKDNZaRehkVImnIHvAxIS4Mztaahk1_5u-XuxHAzfwUoAVTYBXyaUHOQDOt-Jmn15MxCSv9lHzCPyjDP9FegF7HglAaOrrQejyRn2mxU_JAWvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWfkW0QI4OKl5QYdUIsZlZF_pZd83fG-aqylw6eng4T5l1wLKgwN4oR0XeaCud9iJNYvGBo4z5nJ7wDhig_GDQ37md8BJDpf4lJyMjRDEXuXyD06d3YnXREd6YsXEDWlHU-DYEKy1M7Aw_DHPvGlInad3UyuL4nizxYXDvb7onj1mJyvhzzO9XvvKikkbWyPf3AivRka-R9T1uXpSrCHde0dtqPSEUXnCLMb4rx9koa6K7_TiseZUAlln1hTu_xLQYjNQv7uAEQ666Ghl9od9-22eTtPPWHPEL040DxViMGcsDBsgxqG7pzniqNhbj-1Udh7LTck8rJYpa6uLH-VBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvG3uELcSCYt2osfymNCw54mLNHSSQZ40T4dIj3RbQq0N4P5N6klJ9Jye6Wuii4cDoya1uTHTN9h1DjUkTIgL_H73PwpdEMm8pqolVBCY2DCNAuYX3niFtu2LuPpUcAsRACFgjqvx9-6Exzz380PkwQhgWuDiGSBNjGEVGspdJj6a0Uuplgh7kYAQPyYXl6fD8SXes6tJeO0wqI40atMLXOZyazEjxFf3Txb6Ghy32PN_buEH_77tr_1E8w54X2Hc6ZX683KlBPYxyrTwFtSQkHD5lxln-xRawnpV_jyK_8Tc7efdtjq6cEiMaOHQu3wcfZ6S_dxy5Tl5FG5sYQ_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFWdtM3QOmox3DrfaVEyzdXxV0EwhkGdUYPlTHRb_rV8Q64DgeKCsKXtCfOG7BcnJpy5g3loehOaFLdo4QzvrCAZCH5rJOcMAYc1O0q6zm_AZKYhMRDNXbLiEa-acHR0vadjV6NEpJ8IIeGsXGxo19-V6nH7x85Us2H4HPstqNXccZ-Iay_ibdIt_DG8WV79Pqk4tPusHYP9PaJstJcb6qPZXnKDZ_cunBDBypzUkPfmfKTIAMISxyiVy6ToT84e0XRQ8mnXPjnCBjUv7lEVuW3vFRWMX68l4vf0tDpXOZaLDVOa6SFSpUSFOFwoZjA1d134HWpdYYQdrdiMia5cCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیش‌بینی هفته؛ این هفته بازارهای مالی چه تغییراتی رو تجربه می‌کنن؟
🔹
از بورس و سهام تا طلا و دلار؛ کارشناسان از روند احتمالی بازارها می‌گویند و چشم‌انداز روزهای آینده را بررسی می‌کنند.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/697294" target="_blank">📅 21:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697293">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سود سهام عدالت ۱.۵ میلیون نفر واریز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/697293" target="_blank">📅 21:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697292">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZGnAxO9mIFzj2r89kuyn6qXCTTIvsqCnRy6prVyLCC85R1jGQaxalTrSf8WdOxsZNUH-nMWs_yvFqQ0_9cxEaeygYxm3OSyFxhQZikzUKIdNgismlyVlKlTStjHvZXM9jEFFExpw0evShGzEdiKNbzlEy5LE3GTMGb0KRjcfehotFtZLlNQT-ZAfqDWzyXlUXaJnCn73QaiHtmaeactBLvxojbq23jXLIJ-0csrp-3Qu0Y7IyoIBcCX7Ysjk3PKr9Z12Oeu3eckUpFMUjFxa9FEes58V1AGehTSN9jqUb-mfSeurs0wDJOqTW-x48BFXp3vf-X5Gvw-2awz-5UOSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو زیر پست لیونل مسی: لئو، سال‌های زیادی برای کشورت جنگیدی و یه میراثی به جا گذاشتی که برای همیشه موندگار می‌ مونه؛ بابت تمام کارهایی که با آرژانتین انجام دادی، نهایت احترام رو برات قائلم. یه بغل گرم رفیق
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/697292" target="_blank">📅 21:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697289">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iKydMo7EojIbtwKSlPH3N2XjYCLz1MTqI5KxikqM2blcAMU-aSkqDd6jOTwjNAa9gegHMYBBtBxQWw0mBHMFZHATho_lWGO52rUJpryL3_sv8AZ1eMwNyYkI3SMIKU7XX2AKP1uVmEHhXb0y8X2NgAofoWkjxaP8sxZdvCX6LI7tS_CzuAmMOOmDyjbykRKFn3XJzyQTPfGl3ZKFZ_J622q7dthodLX_CLO4qKOVOL9bPxx3YWlOvXUGf5Pr7eQA2kda5WVXD5dNWWh1aVbTqlj3U-YLsHE8ghxZK8ZFn0A29llnn6Qb25tfbSdc7xlIAaTL3Gk7WrJ2WbTKdjONWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q8tkxIq97aMD8XXpN7Hrvm4_hZU36MzZurZTZDp3DBZrz_Eb8DRyVfhvqnd2KkskBwnVo2uOAPIvaokpSxObntcTMqTy37anJ0ABl7XM_mVewLIEiqOT-2rL8fWiLVyWnP3yPeoE3C8kAXzynxxaFpO5LNj5lo0TezO_TUA42UUqYA0lzDvN3HUsDPIGhWyB5rIDE7K5k_ai5fpUAs8HKMqnRRvgpMy0iaytiAgmoVqZNfTrkCxQNWe_4KHYuQs1dVaHC2N4aq5ei0r9BkyICpaAwqC-19rWTMVSVZNxxpXhrvzdRu1SIu02HmWEceZxdHAaNDYSJBn8maJ66_Zvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ukO7C8Au_Htpp4CVHEutW4PuS6mSFasXGl9zLsRLN5nc1ZQvEeE0ngUTfciudh6bb_9lwtdG7EeKaz45665MqsZCavnT7vfpqP9KyGkmVxoWMnFl0jG07XJSI3I3WkB7k0iybNWHkimSZ_F9n41XFOUBEfNEZVry27weXjbyPWjGFcQZSw0NSL8QN9YKmtIKsPEC4X557kuxap_HsLmgg6NBLz067U7FxbRaJpxm947sUFJ61s9KhVuhgMLzuVmIt6rIFZ3F1Zi95iU9LPaB14qk7ArJSKjTQlue_F95D4oXaoj9MBdBqcYAuyR5SukZugcSp3-c9YoXnHdQXVulDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این بچه‌گربه به‌دلیل چشمان و لپ‌های خاصش به‌شدت وایرال شد و توجه بسیاری رو جلب کرده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/697289" target="_blank">📅 21:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697288">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
یک مقام ارشد اسرائیلی به شبکه ۱۲ تلویزیون اسرائیل: اسرائیل پیش از انتخابات پارلمانی ۲۷ اکتبر، حمله پیش‌دستانه‌ای علیه ایران انجام نخواهد داد
🔹
همچنین کانال ۱۳ اسرائیل نیز به نقل از یک مقام امنیتی اعلام کرد: اخیراً مذاکراتی بین نتانیاهو و ترامپ در مورد حمله به ایران صورت گرفته، اما هنوز تصمیم نهایی گرفته نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/697288" target="_blank">📅 21:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697287">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXuQapPAx684hFTQi6fZ6y-avFT4QAZvQdY2oggK7z8tOi1pLDNGspnik8vtf6bX-9_yDAWq13tRNJwOf_YEZHX4T_RDNbemj9Ght5rQb7V1z-f6P8BoILEuPvV8JsbzbmdFH-xeFrjPDnGEyTI9LPgcKgBe3_Py9I0Uz-UPx1uyIHTBkDQvAP9op99RVEm75-RgSRwTjzQU7c2M-tFFVOQMBcy9N-BYcxqBpifgNNCrsbjgklyc_NOeFoCJ5OvFtqUU3_vzRM8nmZLGn4v6btXMQe08I_--ep-NmAR0nGGt2QWdXy2auqLYyrPTh-nncG-n0jsJYeyJ5TkZz-gMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی همکاری‌ها با یک جلسه شروع نمی‌شوند؛ با یک گفت‌وگوی متفاوت شروع می‌شوند.
در گراد، ما به فرصت‌هایی فکر می‌کنیم که هنوز شکل نگرفته‌اند؛ به ایده‌هایی که می‌توانند به همکاری تبدیل شوند و به ارتباط‌هایی که شاید مسیر تازه‌ای برای کسب‌وکار بسازند.
این بار در شیراز، نه فقط برای معرفی یک برند، بلکه برای شنیدن ایده‌ها، شناختن ظرفیت‌های تازه و پیدا کردن نقطه‌های مشترک کنار هم هستیم.
اگر شما هم به امکان‌های تازه فکر می‌کنید، شاید این دیدار آغاز یک مسیر مشترک باشد.
گراد در Shiraz Expo 2026
|
📍
سالن حافظ | غرفه‌های ۴۳ و ۴۴ |
| ------------ | ---------------- |
GERAD | G NEXT
www.Gerad.ir</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/697287" target="_blank">📅 21:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697286">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grNgkiPGR3NU-61Q5aXJK0G71rFSHRvkmHMy2n6SzXZKbnXI0jrqvLhRkExDvCo2wocJb-QxmxO2l0An-Cbu_4wCm73jHVLYG7kGARtY5AfmJmE8NKus6OihR02rKdUE2DppMD7LBAkJklWt9sk50coObTE9oG21xcQrOg1Vz6GfPKAlviQbsvpFdf35TYbTWIHbDNsXR0-UYXJyWF105g1D6BC7Aav1iycyp24Y9ICbkoRZhJN6ooVZbuRhdiTNPhwayYwGiPmVfhviR25ja27mQblWh6WzOy0u6J5AplhxZr_FIQ7QHxfMc9fFGDeclgspDb4Rzf1N6TIHbHgsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
قاب فرش اشک حرم حضرت عباس (ع)
یادگاری نفیس از حریمِ وفا و ادب.
این قاب، جلوه‌ای معنوی و چشم‌نواز از حال‌وهوای حرم حضرت عباس (ع) را به فضای شما می‌آورد.
✨
مشخصات محصول:
▫️
ابعاد: ۲۴.۵ × ۲۰ سانتی‌متر
▫️
جنس قاب: PVC
▫️
طراحی شکیل و مناسب دکور
▫️
انتخابی ارزشمند برای هدیه و یادمان معنوی
💰
قیمت:
۱.۳۹۰.۰۰۰ هزار تومان
✅
قیمت با تخفیف ویژه
۱,۲۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/697286" target="_blank">📅 20:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697285">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b7e6e16e.mp4?token=d7Y4m5HBUKmx1MYUx6QSuCuDQxWLiksFqKYSaY6ZS6LGoWfpvhYtj60eM8ea3G1IsPaoMmSpisFY3Oa3bwS42xDuZIplzKgF2lP0tlb-G9Vnp_vleVnbd8CcW4IWuDeUHUYUu0L5GTMxfvnrz-xw8f3Tqqg3TscH47X0lKbwv_0i3Xvz3WyLB1Nza2_tQTybsjEJbR6OjTEZQOETTC4tcDfWWY8MPWOfblVZvqVajJF8tyYDAU3JAYlhn9dRtdn_Nt_jGHFv07A-IBOSySaj1OlCgDJlCfauOToLPLXOlEsGDZLoAH3zxhdNVeJu0Nt1dPYbmMHfvw7WeBTrVn_cUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b7e6e16e.mp4?token=d7Y4m5HBUKmx1MYUx6QSuCuDQxWLiksFqKYSaY6ZS6LGoWfpvhYtj60eM8ea3G1IsPaoMmSpisFY3Oa3bwS42xDuZIplzKgF2lP0tlb-G9Vnp_vleVnbd8CcW4IWuDeUHUYUu0L5GTMxfvnrz-xw8f3Tqqg3TscH47X0lKbwv_0i3Xvz3WyLB1Nza2_tQTybsjEJbR6OjTEZQOETTC4tcDfWWY8MPWOfblVZvqVajJF8tyYDAU3JAYlhn9dRtdn_Nt_jGHFv07A-IBOSySaj1OlCgDJlCfauOToLPLXOlEsGDZLoAH3zxhdNVeJu0Nt1dPYbmMHfvw7WeBTrVn_cUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند کاربردی رب‌پزی بدون کثیف‌کاری!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/697285" target="_blank">📅 20:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697284">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: من همین الان از حمله به فرودگاه ریاض مطلع شدم و تصمیم خواهم گرفت؛ شاید به حملات عربستان به یمن بپیوندیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/697284" target="_blank">📅 20:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697283">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/349692f31d.mp4?token=ulsTVNaZXUbr98roUfbtH1out3TskY4sWl0SFZaZmov8wu_e-mkWeSlVwnO1iiDOlg2HSWnrxVP5gBdmb_6RnAuMS9vOltz2AA-kqGEhumD8ULW89xxYCJz_aYd6NkHmYzqb6XRgRl57fuG9BgHKMUr0Ki9e8hacOI5bAx6BrtT5oKUYLYajBC6-XcHYUjejocv6cZlMJ5yrSB8RNM3i-OY5l0LOS2PEE1GYLKsDFbn4eBlrzURgFBM5MbH6p4jwhL2QYCT8UWyFyOvUxLkju7EM5yWXAO8e_QDnWiGmxkLB_PMrZ3EvhwwqW2WcSxlVEnG7_kHUpb-TG25VO-uVvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/349692f31d.mp4?token=ulsTVNaZXUbr98roUfbtH1out3TskY4sWl0SFZaZmov8wu_e-mkWeSlVwnO1iiDOlg2HSWnrxVP5gBdmb_6RnAuMS9vOltz2AA-kqGEhumD8ULW89xxYCJz_aYd6NkHmYzqb6XRgRl57fuG9BgHKMUr0Ki9e8hacOI5bAx6BrtT5oKUYLYajBC6-XcHYUjejocv6cZlMJ5yrSB8RNM3i-OY5l0LOS2PEE1GYLKsDFbn4eBlrzURgFBM5MbH6p4jwhL2QYCT8UWyFyOvUxLkju7EM5yWXAO8e_QDnWiGmxkLB_PMrZ3EvhwwqW2WcSxlVEnG7_kHUpb-TG25VO-uVvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقرار نیروهای ارتش یمن در اطراف تنگه باب‌المندب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/697283" target="_blank">📅 20:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697282">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133220ceea.mp4?token=qWQYAzA2fx4YgvIYiulSE6sjqr03CWTdYwWu__7PijF7mo1d-L9EnaBEZMYtV0mq35EutcM8swK0FanHwrpAOHDPZSFo_KFAnxTcmq6iosVKgHRbUuXKzM4mFPd-8JiaVMrCfSvTA8pBhjXRc_DEZRiiCXPNasPAHxTCqUf9M57l6b443KIDBhHc9W5yLQHqm06sNLznoH0rCGGQXwH7vJCys5RCVlUHPLzLp2uZ4ttoFtG5QaicrxoUGdncSB1EUMrEQwazD-W726pp1jLqrl4xZJvNC3Ht-lRfMp8mnzQ-MNXheo3ZCHk6FURCJDGnZyLG_RnsPYqJTFQVIprD5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133220ceea.mp4?token=qWQYAzA2fx4YgvIYiulSE6sjqr03CWTdYwWu__7PijF7mo1d-L9EnaBEZMYtV0mq35EutcM8swK0FanHwrpAOHDPZSFo_KFAnxTcmq6iosVKgHRbUuXKzM4mFPd-8JiaVMrCfSvTA8pBhjXRc_DEZRiiCXPNasPAHxTCqUf9M57l6b443KIDBhHc9W5yLQHqm06sNLznoH0rCGGQXwH7vJCys5RCVlUHPLzLp2uZ4ttoFtG5QaicrxoUGdncSB1EUMrEQwazD-W726pp1jLqrl4xZJvNC3Ht-lRfMp8mnzQ-MNXheo3ZCHk6FURCJDGnZyLG_RnsPYqJTFQVIprD5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره اوکراین: فکر می‌کنم وقت آن رسیده است که اوکراین رئیس‌جمهور جدیدی داشته باشد!
🔹
زلنسکی بارها می‌توانست جنگ اوکراین را پایان دهد، اما نخواست.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/697282" target="_blank">📅 20:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697281">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5100424818.mp4?token=VS5zZugJ6Fa7ltl2GoHF6v7sElrSTxQkXVs4iFv8CSN8vDrS3P06dtBoa2ouosK9UCLrUEm7imckBcg_kgYyia3BtUbcqmz1RslI1HjjgerfuQhm5p0PGlECnNGzet9qJvB3sGcln8UCBiyRnyZoLeZBFF8U-jUOhN2m41ZckEpzQ4TfTie3ujGccJk8kkjQT93gKTszvRp0EX8wEqux9iepIJNTYOwAzhAUPQbXeshupQz1W8_EXdf95F_rcBWEYu4BlbbMZPwXN8u3qSM_DD59vq7u8691Vy0ye4KPn-jSZSJLHhan7Eqz0H1akWTUuCjJlQp-JbcQ9J59LkHpcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5100424818.mp4?token=VS5zZugJ6Fa7ltl2GoHF6v7sElrSTxQkXVs4iFv8CSN8vDrS3P06dtBoa2ouosK9UCLrUEm7imckBcg_kgYyia3BtUbcqmz1RslI1HjjgerfuQhm5p0PGlECnNGzet9qJvB3sGcln8UCBiyRnyZoLeZBFF8U-jUOhN2m41ZckEpzQ4TfTie3ujGccJk8kkjQT93gKTszvRp0EX8wEqux9iepIJNTYOwAzhAUPQbXeshupQz1W8_EXdf95F_rcBWEYu4BlbbMZPwXN8u3qSM_DD59vq7u8691Vy0ye4KPn-jSZSJLHhan7Eqz0H1akWTUuCjJlQp-JbcQ9J59LkHpcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سپاه: سوپرنفتکش متخلف در تنگه هرمز با مین برخورد و در آتش می‌سوزد
🔹
عاقبت هر نفتکش متخلفی که قوانین تنگه هرمز را نادیده بگیرد، همین است.
و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/697281" target="_blank">📅 20:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697279">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f9a72d14.mp4?token=nP0pkMdTjV8VSH3_mD-oSyrZhemVmz4sr2pvTwtwGK-7d2YEx89eDCwiLU7_S84imYSuXKy_-tq7ByERC6nBihia8Vnul5Rc_T5wTiLoXexKbh45bTSwyepFPVrGbE8bvt9SbCGz7gLZGNcGpX9AjOyhc4XHwugnTqsRG0Osnk_ydiYcNolS4wHMg46-cHRCWwIZ1v5J9rj2w4PGXg4TiuDmMso5wL7lAGryP7s3DRxXFLYBukj0rIHIemhCOXNDk3cMDIxSsvLUZU6xNThFfu6_Nw3lMitlrJ9cU1BEjbseO6LyX2-kFHbC81IfJftM9151Zc6KKHulTCWmhSV1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f9a72d14.mp4?token=nP0pkMdTjV8VSH3_mD-oSyrZhemVmz4sr2pvTwtwGK-7d2YEx89eDCwiLU7_S84imYSuXKy_-tq7ByERC6nBihia8Vnul5Rc_T5wTiLoXexKbh45bTSwyepFPVrGbE8bvt9SbCGz7gLZGNcGpX9AjOyhc4XHwugnTqsRG0Osnk_ydiYcNolS4wHMg46-cHRCWwIZ1v5J9rj2w4PGXg4TiuDmMso5wL7lAGryP7s3DRxXFLYBukj0rIHIemhCOXNDk3cMDIxSsvLUZU6xNThFfu6_Nw3lMitlrJ9cU1BEjbseO6LyX2-kFHbC81IfJftM9151Zc6KKHulTCWmhSV1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش صحیح نجات نوزاد از خفگی را یاد بگیریم
🔹
در لحظاتی که نوزاد به دلیل پریدن جسم خارجی در گلو دچار انسداد راه هوایی شده و کبود می‌شود، هر حرکت اشتباهی می‌تواند فاجعه‌بار باشد. هرگز دست خود را کورکورانه وارد دهان نوزاد نکنید!/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/697279" target="_blank">📅 20:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697278">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای
ترامپ جنایتکار: من همین الان از حمله به فرودگاه ریاض مطلع شدم و تصمیم خواهم گرفت؛ شاید به حملات عربستان به یمن بپیوندیم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/697278" target="_blank">📅 20:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697277">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0708ab3095.mp4?token=qB1rwn2Ht0_TQ4S0toiJezoyfs1sibLyfSiu4YC0x2vr_cp1ZcA2df0gp5WU3v--7fNTwGHRESLKedbd25s79wW75ykn7VMmR51SpuUvAA2d_xJLEna-ZVzdw8aXRABTqqLxuSEL_qw61h3esKIy9h2UpkPg-x_qFWdLM5dIlRwoZKXJV8Ta1ND3ujKlKj4aqJEjhoqvOnSXgiyvI53cKfZj8Bbk3Gpl6L7OwTUHvb1sJzG9SChph5ZR5PatyWXce35h28iBT__YknFJShQ32DNok9SG3X9S3KutQfHkh3xUyoNsuRsbB1dyKsFpIrjII-U6OXhp9DtQvuYIRZqgzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0708ab3095.mp4?token=qB1rwn2Ht0_TQ4S0toiJezoyfs1sibLyfSiu4YC0x2vr_cp1ZcA2df0gp5WU3v--7fNTwGHRESLKedbd25s79wW75ykn7VMmR51SpuUvAA2d_xJLEna-ZVzdw8aXRABTqqLxuSEL_qw61h3esKIy9h2UpkPg-x_qFWdLM5dIlRwoZKXJV8Ta1ND3ujKlKj4aqJEjhoqvOnSXgiyvI53cKfZj8Bbk3Gpl6L7OwTUHvb1sJzG9SChph5ZR5PatyWXce35h28iBT__YknFJShQ32DNok9SG3X9S3KutQfHkh3xUyoNsuRsbB1dyKsFpIrjII-U6OXhp9DtQvuYIRZqgzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکسیوس: تصمیم ترامپ برای لغو تحریم‌ها علیه صادرات گازوئیل روسیه، اوکراین و دولت‌های اروپایی را شوکه کرده و باعث ایجاد یک بحران جدید بین ایالات متحده و متحدان غربی شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/697277" target="_blank">📅 20:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697276">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f25bd7935.mp4?token=dvLNkHh3rvxWZoOARnG6zr4O4IUNJ6t_NowXNssEMZkzfKd9UsScl3E9SWaWUuBQ-H2r3n1B6sCMK_f9cMCXug20ikWGNEJWOkQ89pH_ZKtRn_MHt61M489USlLf-4lKDc3Us9q--TzphN20gjJkEW1ylIb1Wh82pWZKrl3zvjPKdPxDGrb-KbQMgNT1_0WbcmJJBZRfs8q1I7P76-TEHv94ccjKG1SgV0JD5FJXfViOZXVxiBZR8W_nADHpE-iR5E57MvYmGUmy2E153CsTR5LsEmPNZUlqJBDZ5zIkWv0TNPdqOSKhSm61UWrmth-CHh6aXLdlUBf3ugvnlSfRew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f25bd7935.mp4?token=dvLNkHh3rvxWZoOARnG6zr4O4IUNJ6t_NowXNssEMZkzfKd9UsScl3E9SWaWUuBQ-H2r3n1B6sCMK_f9cMCXug20ikWGNEJWOkQ89pH_ZKtRn_MHt61M489USlLf-4lKDc3Us9q--TzphN20gjJkEW1ylIb1Wh82pWZKrl3zvjPKdPxDGrb-KbQMgNT1_0WbcmJJBZRfs8q1I7P76-TEHv94ccjKG1SgV0JD5FJXfViOZXVxiBZR8W_nADHpE-iR5E57MvYmGUmy2E153CsTR5LsEmPNZUlqJBDZ5zIkWv0TNPdqOSKhSm61UWrmth-CHh6aXLdlUBf3ugvnlSfRew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وال استریت ژورنال: مقامات سعودی به طور فزاینده‌ای نگران هستند که ادامه حملات یمن می‌تواند به اقتصاد آسیب برساند، گردشگری و سفرهای تجاری را مختل کند و ذخایر محدود سیستم‌های دفاعی موشکی را تحت فشار قرار دهد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/697276" target="_blank">📅 20:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697275">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUs1tgBmXkZO4wAlVlaSweEmBwFsXF4otnriIySMj_pdFsaCpAqs6XbeWkcjqPnigYroKijP0G1cnz6j_BsXH7c0lNUlNU1HaxnZPpxVEZ3G0pQtd4EZIb6YM8GJYZLftJo1qebQ-ByzPBathJsNNo4QcALr3UE4cmoUdjvCMboVN4UpEK0cvyLzFguGnQsVII6RCjA62YIPvqbPPE_STsfcW_3q5OXAi7bpE_-vXIlVNR45Md51VOfFV_PpjJ0h0OmtXczpju_cQNZ6s1i-Lm1ix7zwkuhLggfYeo0w5efK6S5U2fUMminUsDbXadd2JPMkU9CnMgfKS3q7wn65rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریدور عمانی هرمز تخلیه شد
🔹
تصاویر ماهواره‌ای از تخلیه کامل بخش عمانی تنگه هرمز خبر می‌دهد؛ ایران در دو هفته اخیر، بیش از ۲۰ نفتکش متخلف را هدف قرار داده یا با هشدار از عبور منصرف کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/697275" target="_blank">📅 20:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697274">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPHFh6Qhuy9tDcTniphNDsncaPJzw9gJUkwqnAjyWSPXLgK90tVRQDbz7HJSnA9mfPK2bRfrhpP-gg4EYun-FqiO_QMjTKWfRZW8hNEubPsgMfi4QPKZLdWuJ10ULxB097FIWLDuFBNCYqANtzhU0lFi-IXW6IhCdUdvqKjM4J22rsZIrSFK7kDJJRbgpEZuhK_XR3rvqYG19cXkIbWC7WPUMrQpr8TVje-RKrQG6Vmg6sfH87FK5UxxU3MQ8BLFqjzG_5U9jqE3pJDh2Sc9hrDn5V_Qrnnw7qoh6sLluOdpkI-CwHmrMVktXy_2DNLz-tFqcSyXEEmv2M34T7avXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا و اسرائیل چه زمانی به ایران حمله می‌کنند؟/ حرف نتانیاهو به کرسی می‌نشیند یا ترامپ؟
🔹
آنچه این دور از گمانه‌زنی‌ها را از دفعات قبل متمایز می‌کند، وجود یک شکاف آشکار در زمان‌بندی مورد نظر بنیامین نتانیاهو و دونالد ترامپ است: به نظر می‌رسد نخست‌وزیر اسرائیل خواهان حمله پیش از انتخابات کنست باشد، در حالی که رئیس‌جمهور آمریکا ترجیح می‌دهد عملیات نظامی پس از انتخابات میان‌دوره‌ای انجام شود.
گزارشی تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3251392</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/697274" target="_blank">📅 20:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697273">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8df2c609dd.mp4?token=lmm6iIYnr-BJFTyTGQvhkMtrb7XnXjc0pM572XO2CD_b3940eLZ0OPiLqZMbFibGGWwZRpo4nhBu_PrUcwXiB6cKlxqeU9HPWxD5CzhTb0yw_-lpjbkDBiRbtkA4toZBkqHgXeXqDXqiR-Gtc1erlfgbOWW0wTJ7qFWJ01hvMnX3MebNyS8yDtDJ2MD1H_Y4eOzk-mLRTxfDAiGA9e4vPhTPzWIZaUM3z3JRQ280wCGFMvmj7DCSamVAhHy2_jIs9FTfwIdVpiznTPotGZRcLHEFDEt7hnUtom6p5PG7pe97ouzN_vmSTobAcw3fhaAFZJzezyzbedKdcdovTirpHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8df2c609dd.mp4?token=lmm6iIYnr-BJFTyTGQvhkMtrb7XnXjc0pM572XO2CD_b3940eLZ0OPiLqZMbFibGGWwZRpo4nhBu_PrUcwXiB6cKlxqeU9HPWxD5CzhTb0yw_-lpjbkDBiRbtkA4toZBkqHgXeXqDXqiR-Gtc1erlfgbOWW0wTJ7qFWJ01hvMnX3MebNyS8yDtDJ2MD1H_Y4eOzk-mLRTxfDAiGA9e4vPhTPzWIZaUM3z3JRQ280wCGFMvmj7DCSamVAhHy2_jIs9FTfwIdVpiznTPotGZRcLHEFDEt7hnUtom6p5PG7pe97ouzN_vmSTobAcw3fhaAFZJzezyzbedKdcdovTirpHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فتوسنتز طبیعت زیر آب!
🌱
🫧
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/697273" target="_blank">📅 20:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697271">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">24-2 Ane Manaee (1404-02-13)Mashhad Moghadas</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/697271" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وچهارم؛ بخش دوم
🔹
افشای پدیده نفاق در لباس دین، روایت چهره منافقانه یک منبری مشهور! [00:00]
🔹
آزمون ایمان در میدان بلا و جلوه‌گری باطن انسان‌ در لحظات سرنوشت‌ساز  [09:50]
🔹
تبیین اَشکال دوگانه نفاق، از تضاد در ظاهر و باطن تا کتمان مکنونات باطن!  [14:05 ]
🔹
واکنش رهبر انقلاب به نامه تاریخی امام خمینی در سال ۶۷، مصداق خلوص و پا نهادن بر هوای نفس  [18:55 [
🔹
خطرات دل بیمار و داستان‌هایی تکان‌دهنده از عاقبت برخی بزرگانِ مبتلا به بیماردلی و تلخ‌زبانی. [24:28]
🔹
ضرورت فدایی شدن علما و مراجع برای اسلام و خرج شدن برای دین در روزهای سخت.  [38:04]
🔹
"تسویل" و "املا" دو ابزار شیطان برای فریب انسان‌ و عقب گرد از هدایت و بازگشت به هوی و حیوانیت [42:20]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/697271" target="_blank">📅 20:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697270">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d005002ee.mp4?token=Y9zqQyUBSmd9tPY43rbsLm1WqA8ZIxJR5znVkImAE3PUe64lglOw-kom2kL5uutQEls8SwXan_XBu4Fcc6r6-Oof3CoXuWJwV0gkAagSbP0cpXVYDfncqailOKbj1vWL-THvh6-LXWDD7PFqADRlFpyvmwuBoJdAB_N5-39XsgJzlb2qc2p-VfmQWWfk_uHosNwHinZ4jYwlxI0njtHARLsdOPRk-k9YWjAC3LnzywvDRTx-Wx3njE1LImQus97fXPHHObEJnYvm0gAAZ3YCq1qTGYz3gYNWZw4OunQj_c0szze8no7qoajOc3BHoq4zflNUaFgKQadwAIkjf19mPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d005002ee.mp4?token=Y9zqQyUBSmd9tPY43rbsLm1WqA8ZIxJR5znVkImAE3PUe64lglOw-kom2kL5uutQEls8SwXan_XBu4Fcc6r6-Oof3CoXuWJwV0gkAagSbP0cpXVYDfncqailOKbj1vWL-THvh6-LXWDD7PFqADRlFpyvmwuBoJdAB_N5-39XsgJzlb2qc2p-VfmQWWfk_uHosNwHinZ4jYwlxI0njtHARLsdOPRk-k9YWjAC3LnzywvDRTx-Wx3njE1LImQus97fXPHHObEJnYvm0gAAZ3YCq1qTGYz3gYNWZw4OunQj_c0szze8no7qoajOc3BHoq4zflNUaFgKQadwAIkjf19mPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از کودکی که با زدن دکمه سرقت، مه‌ساز و آژیر طلافروشی را فعال کرد، در فضای مجازی وایرال شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/697270" target="_blank">📅 20:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697269">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787d451d8a.mp4?token=JPjiR9qkZ2a-Wd_SZB8ErcLQS1NoXtiOIwTQFXVf-SeayiVpkfFMlmhWruDR_buS6kh0PCa_pnvvjKsBx34Anj0OnWfUi8Td3aTJ544RHsFJriHW2jr3n9WsrTpX5kH9wWVcdLjNCFswGzM79NciXGtoxU-6BDCCAkpNXaMIHc1jQkKg16eHCIKMuEaDnY_KWu6ByvJ-E8cCiQyhGIL96LB2mbTzhj0NDKgrPZic2ml3I1lRuH1MgoWqZ2TrKimnnhhysObsAMHKgP-l5_7Bri7vtx66woPt-B_4xuLbE8s836_dswrpYVRMbEDuhMPwSyuz2fwoym54hge8-Zqf4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787d451d8a.mp4?token=JPjiR9qkZ2a-Wd_SZB8ErcLQS1NoXtiOIwTQFXVf-SeayiVpkfFMlmhWruDR_buS6kh0PCa_pnvvjKsBx34Anj0OnWfUi8Td3aTJ544RHsFJriHW2jr3n9WsrTpX5kH9wWVcdLjNCFswGzM79NciXGtoxU-6BDCCAkpNXaMIHc1jQkKg16eHCIKMuEaDnY_KWu6ByvJ-E8cCiQyhGIL96LB2mbTzhj0NDKgrPZic2ml3I1lRuH1MgoWqZ2TrKimnnhhysObsAMHKgP-l5_7Bri7vtx66woPt-B_4xuLbE8s836_dswrpYVRMbEDuhMPwSyuz2fwoym54hge8-Zqf4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وال استریت ژورنال: مقامات سعودی به طور فزاینده‌ای نگران هستند که ادامه حملات یمن می‌تواند به اقتصاد آسیب برساند، گردشگری و سفرهای تجاری را مختل کند و ذخایر محدود سیستم‌های دفاعی موشکی را تحت فشار قرار دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/697269" target="_blank">📅 19:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697268">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
دادستان عمومی و انقلاب شهرستان ری: یک مهدکودک در شهرری به اتهام ترویج عرفان حلقه پلمب شد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/697268" target="_blank">📅 19:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697266">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlyMc2n0hRpHc6dyJ9RENdXBKLIlWgAdJMRuQiUbcSi16sWXZQRUY8XQxT4BoxtL1SuV28gELETH1oiHb767KKMGnJjgNMTjERbBE-c-0dRiTaQUmk94Izch5Pb0ffoCq7iHpWpUL1SQG1FinN9VChcNcYjvC9UcFE-pS9sfMyO6gdo1rgfPrw8t9TMT76fjmjdFG7E1Nu0wUNK_BeSUQg10BGrlxU7_rtpxBOlY9zr-w6IhYUGNxtjrRhjl5UzJ9O7yLDnwydmRmZr6pFqoto8Bcy8_DiJjxk98v3Z0dvPQz6SA4R3R8f0YSGfKYIVS_4yw8NzUsExwAL09Z2ebQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9SeD8eMylPvrRXUA7x4TWRKS6BngMnKvGhCrgKWNrOrptiL-kH9s7FYqTq7fZ64Rks_YjffKGkFz72UcsNxiuxZGzZwhp9-ZpwnF4yPyXq8P6--VqvAHOuQ32w8YE1nScvwsevDmZoIhaEQSJKC1RLkwOHoAWVNI0CfnB0VWpuPkHpRUaMaa9sBKxeWjlWr0StRgz7edD3qCHujCTAXSjq03zaWNW3Dhd09TJBH6Qct_pP7njyvRXdmrut8LRdz-k0etYKGgHK5erwqrxRw8xg_nltrTvKYnUuHmy0cazhxdLEs41whgkkLkLV_Rcm--8yND2Eba1wyYGFR6TOrQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پرامپت
تبدیل نقاشی کودک به دنیایی زنده
🔹
پرامپت زیر به همراه تصویری از نقاشی کودکتان را در Gemini آپلود کنید:
Transform the child’s original drawing into a charming, magical scene. Preserve the artwork exactly as it is, including its original shapes, colors, lines, details, and imperfections. Do not alter or redesign the subject. Only add a beautiful, softly lit environment that complements the drawing’s childlike style, making it feel alive while keeping its original charm.
✨
#هوش_فوری
﻿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/697266" target="_blank">📅 19:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697264">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318768b4ca.mp4?token=BD5rM29l4eb8tBFZK2SHf6fJ02xzX11OyprBNsMEKexHnsDOtVPH25UvnQ8EQWIB4b6sq5f2sTvjB4I_mbdlaiw8WNs1WnLMdmX3mb-IGAOV0P66MPNhEwYR0xrFbo541neofISz1rNzgutc8dCHdljnIPG5Nrp1RbTI3lrHpDw1RAGY_roSNkZw6RBRMaBdkR1aB-1oWtWhDb5T1TqvPG0oWQWenTvZrNoBdQsZSxT6fhPj-CjQmAtoqWnNZSXSAU4UQqR3NQH2B8Jmd4jF2ttcx9ZOHGYToyTGw0mcG_o86QFFE0XsAM8WkYmxZxYcE1yopoyXohNLbWTZvooyZ1EXcq3KT7E05LPWiCJ6LdfbNOhKHW2PWIQIny1TYg3Q3NFn5A2LlMk0VRJsoRT1nfswjTtoXbkxHi1XEteGqanfFeXygAjCTspEDpP9q_QW787oXlsLB2i_AUZx_46CwIcvQlVI7jgQze8Gjp-2izi6JfKRzMH4ndjff_NBSQYxk6u3CDvdEs0d1OFhdk6f75eUKk276erkSHU-Y1V73KLUIaoqm1yri9U1eut2_iqMql2u1BvNBFi4nJHPv6D74HkX6DAr8OTIwYnz3WBlFGMFd7Zg7zO1skDKDQiXfbLtkDQ0a-UDZ_3pQQI-EnBpZjCM_ER7WoD7x_Jra45iy1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318768b4ca.mp4?token=BD5rM29l4eb8tBFZK2SHf6fJ02xzX11OyprBNsMEKexHnsDOtVPH25UvnQ8EQWIB4b6sq5f2sTvjB4I_mbdlaiw8WNs1WnLMdmX3mb-IGAOV0P66MPNhEwYR0xrFbo541neofISz1rNzgutc8dCHdljnIPG5Nrp1RbTI3lrHpDw1RAGY_roSNkZw6RBRMaBdkR1aB-1oWtWhDb5T1TqvPG0oWQWenTvZrNoBdQsZSxT6fhPj-CjQmAtoqWnNZSXSAU4UQqR3NQH2B8Jmd4jF2ttcx9ZOHGYToyTGw0mcG_o86QFFE0XsAM8WkYmxZxYcE1yopoyXohNLbWTZvooyZ1EXcq3KT7E05LPWiCJ6LdfbNOhKHW2PWIQIny1TYg3Q3NFn5A2LlMk0VRJsoRT1nfswjTtoXbkxHi1XEteGqanfFeXygAjCTspEDpP9q_QW787oXlsLB2i_AUZx_46CwIcvQlVI7jgQze8Gjp-2izi6JfKRzMH4ndjff_NBSQYxk6u3CDvdEs0d1OFhdk6f75eUKk276erkSHU-Y1V73KLUIaoqm1yri9U1eut2_iqMql2u1BvNBFi4nJHPv6D74HkX6DAr8OTIwYnz3WBlFGMFd7Zg7zO1skDKDQiXfbLtkDQ0a-UDZ_3pQQI-EnBpZjCM_ER7WoD7x_Jra45iy1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وام گرفتن برای خرید طلا، خوبه یا نه؟
🔹
این تصمیم می‌تونه یکی از بهترین تصمیم‌های مالی‌ات باشه یا می‌تونه تبدیل بشه به یک بدهی سنگین! چرا؟
🔹
جزئیات را در این ویدیو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/697264" target="_blank">📅 19:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697261">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
معاون وزیر ارتباطات: در صورت تکرار جنگ، احتمال قطع اینترنت وجود دارد؛ نقش رئیس‌جمهور در تصمیم‌گیری می‌تواند پررنگ‌تر شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/697261" target="_blank">📅 19:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697260">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f4ab0908.mp4?token=JzxU4KS7ZJe3neAMbyWh5zH3aMrOFL-Vi4AjRFVQOgXzCpFgv2wLaLHW4_dfGWQZISDc8ZZoKsS-51sDElkOoByJCXX6sR-WqMQVKLo4TFyHm4j_sqdt-P2Snasnj5J4pX-04IadYNO_FdAG1BBPGSPBiJOt9JDP4bDAigPIbkpcb_xCxhuvewEVG6r_aKLMFt7wJyX5wAaYEerbkLHYzYQTAQ9AvBRJ7ld0UH4mj9WjqgD8ip-5BZJktES0qbRj-Zd-YKIWMUZbQTYbEGDgA7Fw7pu69IwD72Q_sEaSZnVdFS5VVAb3-VrsryXU9DEa25NdZZ60UvoBsi9XwYsk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f4ab0908.mp4?token=JzxU4KS7ZJe3neAMbyWh5zH3aMrOFL-Vi4AjRFVQOgXzCpFgv2wLaLHW4_dfGWQZISDc8ZZoKsS-51sDElkOoByJCXX6sR-WqMQVKLo4TFyHm4j_sqdt-P2Snasnj5J4pX-04IadYNO_FdAG1BBPGSPBiJOt9JDP4bDAigPIbkpcb_xCxhuvewEVG6r_aKLMFt7wJyX5wAaYEerbkLHYzYQTAQ9AvBRJ7ld0UH4mj9WjqgD8ip-5BZJktES0qbRj-Zd-YKIWMUZbQTYbEGDgA7Fw7pu69IwD72Q_sEaSZnVdFS5VVAb3-VrsryXU9DEa25NdZZ60UvoBsi9XwYsk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چراغ‌های مخفی‌شونده؛ یکی از طراحی‌های خاص و خاطره‌انگیز خودروهای قدیمی
🚘
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/697260" target="_blank">📅 19:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697259">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20e545737.mp4?token=ggg3OYfp__zsea6X7ANa_xJL_PwDVu86FI4Ut3tAxJ3ldxYOfQ3PBQVQogHbGos5xkKqMjzflv4DhMhn63IzzVssd1H0ORUKbnYeEvzsGe-HkjB0WN80KuWawpPV5ORIhpNam0671c35L2iMcBjxjf1_mp7lALvxOREF6Y95E1WB_t_L7tp581XkAxC8-oxJcp1Myf9BfogE3M56SslTSIQvTbqUt07lfpItUqa16a6TkT8QPqr_tmOnMhGJRrANSE6uTa3GtuO12AWtZ5P66Uih4wjDHwTxsuAp7SzyfSnAMXXJXzgub7_2dkvd5CXuDo23UCtTuYPQzKBhOxMS1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20e545737.mp4?token=ggg3OYfp__zsea6X7ANa_xJL_PwDVu86FI4Ut3tAxJ3ldxYOfQ3PBQVQogHbGos5xkKqMjzflv4DhMhn63IzzVssd1H0ORUKbnYeEvzsGe-HkjB0WN80KuWawpPV5ORIhpNam0671c35L2iMcBjxjf1_mp7lALvxOREF6Y95E1WB_t_L7tp581XkAxC8-oxJcp1Myf9BfogE3M56SslTSIQvTbqUt07lfpItUqa16a6TkT8QPqr_tmOnMhGJRrANSE6uTa3GtuO12AWtZ5P66Uih4wjDHwTxsuAp7SzyfSnAMXXJXzgub7_2dkvd5CXuDo23UCtTuYPQzKBhOxMS1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات جدید ظریف که با واکنش کاربران روبه رو شده است:
وقتی موجودیت کشور در خطر است، شما به دنبال بقا می‌روید. چرا عهدنامه‌های گلستان و ترکمانچای امضا شدند؟ چون دشمن تا پشت قزوین آمده بود و درصدد تصرف تهران بود و موجودیت کشور در خطر قرار داشت. در چنین شرایطی، توافقی صورت می‌گیرد تا بقا حفظ شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/697259" target="_blank">📅 19:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697258">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33076f3269.mp4?token=tbh8H_JchzNg67nysULc1QJMYB3NJypSbDOU6NyOI_hfW-Wa_x2KNqf7-TzTzj7pssltMFbwSFgqidfvgnLI-F3PxuCoMVjSTmU6MD4peO7kru2n0nZy7cn20rMWvJDN8zH4VWaXV7_W0EG0k-Sv8_1A1VPL1UQu_qJ5K6htJJuuNkn7x_guIQdcqp-ZrwSxiL9fl1A1NKnYVkJ-v3jjbM241rYGCL711kBvk9Rzukhos_Nj6TXOJCVCrX5okEhHeaM3_FOw3T04e0Gt72avP0ccV9PEFsgaEnKhIXf4JKHJFVT6fg5imVKXsAPv2CUNEGruLv79k7Jh3xJjPFQo_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33076f3269.mp4?token=tbh8H_JchzNg67nysULc1QJMYB3NJypSbDOU6NyOI_hfW-Wa_x2KNqf7-TzTzj7pssltMFbwSFgqidfvgnLI-F3PxuCoMVjSTmU6MD4peO7kru2n0nZy7cn20rMWvJDN8zH4VWaXV7_W0EG0k-Sv8_1A1VPL1UQu_qJ5K6htJJuuNkn7x_guIQdcqp-ZrwSxiL9fl1A1NKnYVkJ-v3jjbM241rYGCL711kBvk9Rzukhos_Nj6TXOJCVCrX5okEhHeaM3_FOw3T04e0Gt72avP0ccV9PEFsgaEnKhIXf4JKHJFVT6fg5imVKXsAPv2CUNEGruLv79k7Jh3xJjPFQo_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار نماینده مجلس درباره تبدیل کنوانسیون دریای خزر به «ترکمانچای دوم»/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/697258" target="_blank">📅 19:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697257">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a6d63389.mp4?token=Qr8svuAOeHcf4wtk_MTuwVgEKtD1hQ7SH6WHsqKsD4jXBKdjtWQthkjQwRZvNczJh6QC9CU34Ldgg_D2tzEijUCTeJ-YZkDrV0Xd1okocF-LddC16ynifr9Un94KJD04_atyTaqBbrfKzeFQhWFecim3mdHQzcV1-nSyveuabOtqeVcXrRaL-mcF2U703_eEgUhtUlrJiwu4L52XelzAiRtTHGGBrCQxc9ZR8mtJS9GfaQFUt9MoBi74Q2asBH5oPVoTcZ7Xr_QwjZO-S0jTFf6OxQjwPBdMiZcgBbZXGfARES3BcUkX8BUhL0c3ddwxmlD1zes_2lVSYttrefOoZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a6d63389.mp4?token=Qr8svuAOeHcf4wtk_MTuwVgEKtD1hQ7SH6WHsqKsD4jXBKdjtWQthkjQwRZvNczJh6QC9CU34Ldgg_D2tzEijUCTeJ-YZkDrV0Xd1okocF-LddC16ynifr9Un94KJD04_atyTaqBbrfKzeFQhWFecim3mdHQzcV1-nSyveuabOtqeVcXrRaL-mcF2U703_eEgUhtUlrJiwu4L52XelzAiRtTHGGBrCQxc9ZR8mtJS9GfaQFUt9MoBi74Q2asBH5oPVoTcZ7Xr_QwjZO-S0jTFf6OxQjwPBdMiZcgBbZXGfARES3BcUkX8BUhL0c3ddwxmlD1zes_2lVSYttrefOoZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بایرن مونیخ سریع‌ترین گل تاریخ بوندسلیگا را خورد؛ در ثانیه ۷ بازی و در دیدار با اگزبورگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/697257" target="_blank">📅 18:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697256">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgqLi9RtIPf-sQMncXxBpum9QgBai2QJhOiWAuLON_G5kAflRusHuuIKp2v3VoNp5ODsj7bhjPzwTyeR-z1b3PmWp_0qnLadesRP441rgPR8IXVHVSzokp-PjaefHc0FEseK1NkVpik1HtGqhGJEtdWzhoNVVz8DUvVJPF8uDieC5wlHW2iXrp_nwCaaHwOgTSffY7aAJhSC3zcCde-goZOD0s2spb-Enap1BprCWPfQFlh9n_GYG2bt3YHSu95urTG6qb5ZeknDl2tj741gqHugFGKQHQt9K_thvL0nS2YNa5Sm29ol9hEJnRzNtLX-d4SGuVNswRxNJLtpuaND5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیلم منتشرشده از محوطه خون‌آلود فرودگاه ریاض
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/697256" target="_blank">📅 18:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697254">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
فیلم منتشرشده از محوطه خون‌آلود فرودگاه ریاض
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/697254" target="_blank">📅 18:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697253">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meKV0jnYKkyh_lrrI6I56ajSjDdoHm19EG0IvD62RWiGuiw0Wl5CZzOQOF0qbyJ2GzbsJdy8lFSDjkg24imLdYy5tufTVdxYGbdynhr2ghgYUZee6U6k5j_mEGOesu3GD_qdbeYUq5HL16cy3Dr4w863ln7m00ODETZbcINDI1ZSt876iOjhibD_pTBGdBAeDQ_OZk43r2RHwjwNlaiJ0-jEcvEShiHHDxviR3nbHvnhHBhBD9ADvV0qdHts95CwT7pHbmjCmABZ7HnPLVCaW6HqlfUdzOLyE7joAevdJ0YI07gI_LGjykNiIGiRp-FO0I7uqW6xnnPiKszMB3z7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴۵ درصد صادرات کشور در اختیار ۸۶ شرکت
🔸
تنها ۸۶ شرکت شامل ۱۳ شرکت بازرگانی و ۷۳ شرکت تولیدی، حدود ۴۵٪ صادرات کشور را در اختیار دارند.
🔸
تمرکز بر همین ۸۶ صادرکننده بزرگ و رفع موانع فعالیت آن‌ها می‌تواند بخش قابل‌توجهی از صادرات کشور را افزایش دهد.
@amarfact</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/697253" target="_blank">📅 18:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697252">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYZISNgOHlPFMVRo4AkZiDrzVKpHFFBQjsx7KstfiMH58eZO59EKoa1zY-VCo0FFf92Vr9JIOIvXEsRRqLwwBrdexjh0DOVC6-0Cd0N_o7wk7Jlt4rIReSUFjiCQ4stcLs0xGMDYgqLol55NNSd4s5gMiBEVzXwXYxC1HHsY_19AWcLq3sM7V4sK9mN4TdRhTeiiXi8yRxIm6jmiTjGUCG6tWIZQw8CT3ZEELHAlFDGDK6BZ3o3L87Hv_dMsxvI7r5XiyvUDdNcoazc2W6G2H5geoleSqogXK8H6DOC5T8Z8Mk7juI8-y3QsoEMer5O_YX6HtDwIAYFpNHzYqzQ7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری محسن‌ تنابنده علیه روبیو: آفتابه ایرانی ۱۰ برابر کشورت قدمت دارد!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/697252" target="_blank">📅 18:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697250">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJCWK4LdCDJHd2WnOmBO95PvKrunMv2Sk3Ft9TV4CH2B2ByyvoXIGF_pIjq7GQb4b8AvnQn3qYnvQbxa5wpeO2uLKLEjRi8co0FOm4lpWdZIUvm03PQboUZqaf4zzSqkqA59mZdB0BRAHsTQSbchj4Ha7cJi2nbQtfPVDc_dpYnMbIVzf-K-2ACRwNGTXvhWdjQL3Fe6yI4GzXrNGNAE3_WDOqBOc7w6AYl4oXImt7PD_HPgTWjLLEl9THa8JcKjpX8iIzaxNCHx8UDcF-HwH2fp0rC5_10o6hu12bepDueugTfxaW6UBrFik-FSF9uWYDQbXNY7FcL30VMYhKLCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسیر روستای گرزلنگر، ایلام
⛰️
🌳
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/697250" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697249">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895582443e.mp4?token=Lk_5yFfE9DJXPgPOG498iuc9IuHZZDEIfuJLLCFnFLd_PsE-_A1Dogt5Abtd9cSO_BVjgyIHY9mf0LADl5LnFs1aoPZrGzv0JX3N3q5h5rFCMdxKsV5nDhis0-I_xX-WAGh57go8dETFgxTwDRkiKtCMwdi0WvQX7VUHvSVzg8EstNmdXlfafdk_Fw_KPhQX75YGlxVu2SKDTd875xhLVQc9R3M-q2DGRgAElYzynmr_qSB8wY9_kYQEpeONytWNm8RxtSIV1dUfTgRes5aSVuFQNPr89lTnsejzByb5W_Ww2Nnt3JYEYKTOSRnhWWptz5rfKtJjqJQ4rF_3hV-WWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895582443e.mp4?token=Lk_5yFfE9DJXPgPOG498iuc9IuHZZDEIfuJLLCFnFLd_PsE-_A1Dogt5Abtd9cSO_BVjgyIHY9mf0LADl5LnFs1aoPZrGzv0JX3N3q5h5rFCMdxKsV5nDhis0-I_xX-WAGh57go8dETFgxTwDRkiKtCMwdi0WvQX7VUHvSVzg8EstNmdXlfafdk_Fw_KPhQX75YGlxVu2SKDTd875xhLVQc9R3M-q2DGRgAElYzynmr_qSB8wY9_kYQEpeONytWNm8RxtSIV1dUfTgRes5aSVuFQNPr89lTnsejzByb5W_Ww2Nnt3JYEYKTOSRnhWWptz5rfKtJjqJQ4rF_3hV-WWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های آمریکایی: تردد شدید آمبولانس‌ها در نزدیکی فرودگاه ریاض. یک شاهد عینی می‌گوید: «همه جا خون است.»
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/697249" target="_blank">📅 18:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697248">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/952e11e567.mp4?token=SNHi9cHrADuSfRMOqgFqjIStLueKRhCFaCQIx3drwjSZ9lw_IR8cxo5WwpmwitEip03YVwUtdWQLdhGHc_X2KD62CST1MKfScfIGl1gR4oJsZUxJVq1i77-OsswXi-ni5sTu5WP9RxOCZDZ_6RdUfq-rzoyMsREteP33Xn_bl3uKN-z_4VzwVWm4jSpyaeIvp3LocNhYSLImZcMGykoyZWaP_M9z6P2-gnUmpzj-9sooFjEB82yuMuoEL0BAfMnMgETQPq14jT2DJ8mt-rkEy8QyIQ8QC3Fqcpd8iDZ7W6JAqnVJFs6mHRayNX7YB0-gglf_PsEpdlRc-tOehXkq9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/952e11e567.mp4?token=SNHi9cHrADuSfRMOqgFqjIStLueKRhCFaCQIx3drwjSZ9lw_IR8cxo5WwpmwitEip03YVwUtdWQLdhGHc_X2KD62CST1MKfScfIGl1gR4oJsZUxJVq1i77-OsswXi-ni5sTu5WP9RxOCZDZ_6RdUfq-rzoyMsREteP33Xn_bl3uKN-z_4VzwVWm4jSpyaeIvp3LocNhYSLImZcMGykoyZWaP_M9z6P2-gnUmpzj-9sooFjEB82yuMuoEL0BAfMnMgETQPq14jT2DJ8mt-rkEy8QyIQ8QC3Fqcpd8iDZ7W6JAqnVJFs6mHRayNX7YB0-gglf_PsEpdlRc-tOehXkq9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسارت شدید سیل به منازل، خودروها و احشام روستاییان شهرستان گرمی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/697248" target="_blank">📅 18:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697247">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7155a17b87.mp4?token=DXJA1nM2NmXprZSSqGZ6SO_2lugDhET1nBS26PVylt-mmztJ5D5i2G9dXngvQTdBHyRPdwzHyyTM4PLqCY4FEPMJPDgZCffsyT6UxmbtldVXGEr267cBCy6zfABIviQkfbZbwrs1mlbnwSVvMKDnImx9VfBVYDED3AYk16xX9R-Ek43gob3v_x90XgvfNlCdBAso-OduXMYOnrMy2W9ajR0sP_5duXup2vRE4i3bcN1ECdSbrvwMET9RxOlweqLm7hEEcC1sxYjLcKAo8dCiANSDcEsw9FT95D8Xs1nog_k6DRD5wft1MsvVFohSf5XDjbvydlpwGAwbmG5ZSETMtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7155a17b87.mp4?token=DXJA1nM2NmXprZSSqGZ6SO_2lugDhET1nBS26PVylt-mmztJ5D5i2G9dXngvQTdBHyRPdwzHyyTM4PLqCY4FEPMJPDgZCffsyT6UxmbtldVXGEr267cBCy6zfABIviQkfbZbwrs1mlbnwSVvMKDnImx9VfBVYDED3AYk16xX9R-Ek43gob3v_x90XgvfNlCdBAso-OduXMYOnrMy2W9ajR0sP_5duXup2vRE4i3bcN1ECdSbrvwMET9RxOlweqLm7hEEcC1sxYjLcKAo8dCiANSDcEsw9FT95D8Xs1nog_k6DRD5wft1MsvVFohSf5XDjbvydlpwGAwbmG5ZSETMtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتسب به سوختن یک تانکر نفتی در تنگه هرمز و پرواز یک بالگرد آمریکایی در نزدیکی آن، که گفته می‌شود توسط ماهیگیران ایرانی ثبت شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/697247" target="_blank">📅 18:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697245">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03c0d7418.mp4?token=efSuJDh1Y0HM_fxgV-25HoeGgVn11Fbqvjbt-ZAnPyzMWdFt3Q_wFMRssXe-k98TPXb_ytxyeDtY_C44qMmceG0nwM8BxPJ32DPDckSxS3wqAFAAgYgMDtMIKlOUe_mpuvoDGydFD_5_-O_8QwsTm1ZFR0ODHD15zzlFhumnRAKz9-2aTZqDkeoXho-aE0DVsz1vO-j0qbQ6IKMll-BlFF-WR9PRAWG-FGxkPtwvlbR827lU3JzkwM6fAG4l96E8yR5vWgHpEWXThD9yJgPKNA3Xc85sQixh3xe1MI-f3EEhNG-ZNwd2vorEyHzR03P1L1Vqq1doR546fSeNt52KVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03c0d7418.mp4?token=efSuJDh1Y0HM_fxgV-25HoeGgVn11Fbqvjbt-ZAnPyzMWdFt3Q_wFMRssXe-k98TPXb_ytxyeDtY_C44qMmceG0nwM8BxPJ32DPDckSxS3wqAFAAgYgMDtMIKlOUe_mpuvoDGydFD_5_-O_8QwsTm1ZFR0ODHD15zzlFhumnRAKz9-2aTZqDkeoXho-aE0DVsz1vO-j0qbQ6IKMll-BlFF-WR9PRAWG-FGxkPtwvlbR827lU3JzkwM6fAG4l96E8yR5vWgHpEWXThD9yJgPKNA3Xc85sQixh3xe1MI-f3EEhNG-ZNwd2vorEyHzR03P1L1Vqq1doR546fSeNt52KVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی گلوله به جلیقه ضدگلوله برخورد می‌کند، داخل آن چه اتفاقی می‌افتد؟
🧵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/697245" target="_blank">📅 18:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697244">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRgRKFG4C9r1fkPO2kkKB1iE9HKKvv96yE6WKaM2aQpF4RHhnNZHEDZhuAxjpf76MELpGOMxHDWhLo2MehjllFgWEzEaH9v7uFvFzRI7AzXWjINPFRNcrnsj0ctitHenBuHilAvtUaZZlyw6gDI46IOFYT8RVpNP5D93rdt1FYpjdXn_H1fQEHfBHZN3dc45ksAPHwsddq0vF07JXalBlvQl80TER7L23-e3sAsKY_Xw8yoJlyxhL-yFH_gJfN3NxRztPvnenDE1hXw49O_YSqAlZFpH12wjN_fewIdHyYXahNFakrK6sG92WDWfaZoMa0UmEe00Bc4rxAse345R5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ازکارافتادن کامل فرودگاه ریاض/ ۲۲۱ پرواز لغو شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/697244" target="_blank">📅 17:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NqWs7N8VsSx0K7qs8O89abhZL6QCmMejpkNlyvY1siSoTzd9DP8b-L7914bBX3R_m_gzB-7aedDs8xbKXWqIcXyJfGPQGzwuizR9Fik8hwXw9HC5AtkHhXlQZk2SY3Gk00exP0Jt_4XKv56jWubAtMDnUY_3mQMP11cPrqCYbfrjosaVuL5s6IKWlLMigEvQnzeaOnK2Qtw1AgNEnrmKP0SCsms-DdProXPONY0XBo4N4VaP2Kl1mQWLdbdyfjZKF1L3h-E7UyDvqMPBCDbMbHHr2yyh5gb3OoUCPG3QjbynjVkPN1cyh3k5x4BITODBpJ9TCczju3zrdsiJB_YY8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNz6OFO0b4IErx2UtxTOOMmCAbWF_qPODkltFhaUfYHuyK0V72h_wiN8Typ2IpJPSHhNcKQrGNjUhjuWjmLr_3HCETT2o5vqeloV8xRujhUA6N_ruOpi_7ZTvSAwbBKEqeKCjM-Lvv1I1yjXDT6RzgYgyHH1jhlQekC1cz-tze_E2Ipqj2oK-CsKpP9otBqYhnY2v4bDx_8HMVc4glM3yuKGKgABRqbBDihs2QicYD1aCrJpps41GgTKsJDgNiWTo_nB_CN7jYtaUSZ1l-HfbxKEFN019O6nZTX9pWxANSKw8giRvcwvmyZJkUqHwzVWjr2FO96dQcOZYAqmEIFiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikDcKT_FXwKOan72G7O96pVKfkj9t6oYfi_IsM0WTlNqeTfkzkVTvTuGz53VcppWTkGoTVJrXfd0HJ3XR_FzGn4NRqoCoLvrcmSSGrFnPeHkk9kwvGIqv26ox1v-k41y9kr4g2f29ypl_WqQKlvmuItyxWmMwf-hWb6xe01YIjB-bDZcUNGQdY1vicwZ_Hfslx0pKpVjUga3_Mo7I5blpRQM7k4rR3qfok3dxUrxpYKuoSPNyeGCtold4l4f34r6oi3oEULuAeszWlK-Ly-Hm0t88lP3p97JRQKXmN3K4R-U-vnzhp5UlJhtq6C6EPxZ4K51RYDRz9crb5eo5jp4hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اسم تمامی وسایل ضروری سفر رو به انگلیسی یاد بگیر! #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/697241" target="_blank">📅 17:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c8ec8d20.mp4?token=nNASKaSFfnQlErrzOc9x3I_YatkDC89B6S1x6XaU1zC58cbqTtKglUjpRNcZsR_3Y3FVnPaaAt01e1AqYXmYzfC9fURFVhTWS8k1KjyeQEsmLwaVUelsMJEjJCOwjemHDc6cvNcLfGMIF8FyElyotyk8szmfkQW0wAdZ6D8ds86kuAzfzerd20H_Fb-Yx0VKVDNcfDjm0Zr2m_kGwwdReZWFZumPPg9ciykLiIiHnAceNrhvi6rW3Y0cviaOQtJNqsI0zsjwJ0_Il80JiWLvx09BEprmehuTHUAR90nM4kc_yKy6Zn8nSJS3KG7ILNq-MFywRRgISBw444xWc_Z_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c8ec8d20.mp4?token=nNASKaSFfnQlErrzOc9x3I_YatkDC89B6S1x6XaU1zC58cbqTtKglUjpRNcZsR_3Y3FVnPaaAt01e1AqYXmYzfC9fURFVhTWS8k1KjyeQEsmLwaVUelsMJEjJCOwjemHDc6cvNcLfGMIF8FyElyotyk8szmfkQW0wAdZ6D8ds86kuAzfzerd20H_Fb-Yx0VKVDNcfDjm0Zr2m_kGwwdReZWFZumPPg9ciykLiIiHnAceNrhvi6rW3Y0cviaOQtJNqsI0zsjwJ0_Il80JiWLvx09BEprmehuTHUAR90nM4kc_yKy6Zn8nSJS3KG7ILNq-MFywRRgISBw444xWc_Z_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند می‌گیری نوبت دکتر بگیری؟
🔹
پشت‌پرده کسب‌وکاری که از صف انتظار بیماران، ماهانه ۴۰ میلیون تومان پول درمیاره!
🔹
ماجرای نوبت‌فروشی دکتر رو در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/697240" target="_blank">📅 17:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b76f8139.mp4?token=HY7yGI7ae_QAqR54iVk3qFRhiu3P9vUMoNvkiGBeiRGmQzB4uzC2wRk1p3mWzHRLdbAFz2xa08Ac3-NxVlF87iXXEq9jA68RUPWj7X4Q9B3VYZgJX7tWBIiT3Wm9f8KDxoRH9l2MGtCeyaZ2-EV9a6j6V00EcmkBtdMi-R5mPI_GcDIhYoUZEcyJ5_45Xa64tYXjRbJ7c82bo3WVwFT1hFIB_nfAYwe5LtKkTr0qSJUJC_-JVZmj42qdfjMntKLnQhS0OvFhf4RZ25hM0Lm8heYdoOhQ0fGlz1MZb2fxPByG5OsGIbtDalExNigH9LuP9dMk7umIScH7J19HcFaGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b76f8139.mp4?token=HY7yGI7ae_QAqR54iVk3qFRhiu3P9vUMoNvkiGBeiRGmQzB4uzC2wRk1p3mWzHRLdbAFz2xa08Ac3-NxVlF87iXXEq9jA68RUPWj7X4Q9B3VYZgJX7tWBIiT3Wm9f8KDxoRH9l2MGtCeyaZ2-EV9a6j6V00EcmkBtdMi-R5mPI_GcDIhYoUZEcyJ5_45Xa64tYXjRbJ7c82bo3WVwFT1hFIB_nfAYwe5LtKkTr0qSJUJC_-JVZmj42qdfjMntKLnQhS0OvFhf4RZ25hM0Lm8heYdoOhQ0fGlz1MZb2fxPByG5OsGIbtDalExNigH9LuP9dMk7umIScH7J19HcFaGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های آمریکایی: تردد شدید آمبولانس‌ها در نزدیکی فرودگاه ریاض. یک شاهد عینی می‌گوید: «همه جا خون است.»
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/697239" target="_blank">📅 17:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
بانک مرکزی: بانک‌ها دیگر اجازۀ فروش طلا ندارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/697238" target="_blank">📅 17:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697237">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن چند انفجار در ریاض خبر دادند/ در پی دستور صنعاء برای فرود هواپیماها نیز فرودگاه ریاض تعطیل شد و چندین پرواز تغییر مسیر دادند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/697237" target="_blank">📅 17:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697236">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ff2aa89b.mp4?token=GOWLLdcghhUt127WnH0Ds_OxmRjPD66YDaKJuNdbQoueVCrz7Kx2s3CuZmDgU7c0BbjJ703pS-jToNkgxkzRcGLMYaQx1U42ijphIQOqhdFqNACCHaeLXm-B6gSC2l_r9FjxSxTaqs4I085S5703gAXF1Ga8PsxwUupCvBitA8g518CmiAglrr9WmbKxmIS6714k3I-rW9mbZ3OGqgA8_VdKvjjK1jNcjUuzMO6hz_CKvj1GXH7J5t4mJsgj3iPUO_bY1hizf7pQdZWop2l2pHASTG4yOaqclYcG415xyTo1OgvLRkexcTtMYhBql9R0LlreksnQeyWSMN5mEL3qqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ff2aa89b.mp4?token=GOWLLdcghhUt127WnH0Ds_OxmRjPD66YDaKJuNdbQoueVCrz7Kx2s3CuZmDgU7c0BbjJ703pS-jToNkgxkzRcGLMYaQx1U42ijphIQOqhdFqNACCHaeLXm-B6gSC2l_r9FjxSxTaqs4I085S5703gAXF1Ga8PsxwUupCvBitA8g518CmiAglrr9WmbKxmIS6714k3I-rW9mbZ3OGqgA8_VdKvjjK1jNcjUuzMO6hz_CKvj1GXH7J5t4mJsgj3iPUO_bY1hizf7pQdZWop2l2pHASTG4yOaqclYcG415xyTo1OgvLRkexcTtMYhBql9R0LlreksnQeyWSMN5mEL3qqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی از ماشین‌ها دقیقا صداهایی مانند صدای حیوانات دارند!
🏎
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/697236" target="_blank">📅 17:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن چند انفجار در ریاض خبر دادند/ در پی دستور صنعاء برای فرود هواپیماها نیز فرودگاه ریاض تعطیل شد و چندین پرواز تغییر مسیر دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/697235" target="_blank">📅 17:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای الحدث: نیروهای انصارالله مین‌ها را با تراکم بسیار بالا در منطقه باب‌المندب کار گذاشته‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/697234" target="_blank">📅 17:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/828c66f5ee.mp4?token=km6GV_Sd5nHdP0bc7a4To7UAb40Keqy1wX6PHqB5AYjTAaAvxMrVnpAyZc7JViA3L7iycugCvISwUlOWExMJ3fN2Np9KzugUVNq7vAKe41qQ0R1KRhjOQGzo-LAd7G4RAIesf7HZjy-D8238fYYp0y6WBWC8KcWM9M3X37gGIFCeLsx1YsnenHCrTNlwi7QG7k6JyH09fSA4T5enxLcZvCiuVfYr3WRsWOu94k0dsHSoulNAHjHAW-HpWg6weM6TamYUGbwudIVJDOF3blPkffqK4EKHhF_ZwG69BqL8rCdXptkI7fWB1dahFhjBJBoTJce_8JTnxq_vhI4HUHC2xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/828c66f5ee.mp4?token=km6GV_Sd5nHdP0bc7a4To7UAb40Keqy1wX6PHqB5AYjTAaAvxMrVnpAyZc7JViA3L7iycugCvISwUlOWExMJ3fN2Np9KzugUVNq7vAKe41qQ0R1KRhjOQGzo-LAd7G4RAIesf7HZjy-D8238fYYp0y6WBWC8KcWM9M3X37gGIFCeLsx1YsnenHCrTNlwi7QG7k6JyH09fSA4T5enxLcZvCiuVfYr3WRsWOu94k0dsHSoulNAHjHAW-HpWg6weM6TamYUGbwudIVJDOF3blPkffqK4EKHhF_ZwG69BqL8rCdXptkI7fWB1dahFhjBJBoTJce_8JTnxq_vhI4HUHC2xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خطای دیدهایی که مغزت رو به چالش می‌کشن!
👀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/697233" target="_blank">📅 16:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxBL06YNbyFFB8c-FKpEXCjBpD9XphDuc4K6F_v9bfFtZKfjxlezWtSnyV8v7JKvkdRPjaKM17aw5sjSR9nHP1QuvruNLOR4YN9lLu4H3hqNV_c2L5PLMz8b0EjL_N-xWfl6g37swHXcluHaknUn1S0CsP2nsdLEoqWknaPAVHsnzIA6DK0j40imdb2eJx8a6r_r_MtMr6Se0CWXUvUFlNb3fWfOsW7rEL8SU7Wtm2OtsCwuP6ZgyPGO-P1qW1SA3NMHvE9ev-D4M0rmN49ATGZDa7VgaB5h8s3MTcxfxt5WVaMZOL18EWXTIyoTXBlDhfgAlTrG1aRCLdWDTGSpXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری محسن‌ تنابنده علیه روبیو: آفتابه ایرانی ۱۰ برابر کشورت قدمت دارد!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/697232" target="_blank">📅 16:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جامعۀ مهدوی/ج۱</div>
  <div class="tg-doc-extra">استاد علیرضا پناهیان</div>
</div>
<a href="https://t.me/akhbarefori/697231" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جامعۀ مهدوی
🔹
جلسۀ اول
سخنران: آقای پناهیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/697231" target="_blank">📅 16:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697230">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
پزشکیان: اینطور نیست که اگر امثال من را شهید کردند کسی در ایران نمی‌تواند مثل من باشد/ همه می‌توانند مثل من باشند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/697230" target="_blank">📅 16:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d10f0225f.mp4?token=KfQX2yYMkn12lXb9hL2rhZIRxDGM966RJLRcxsf_P62PV_Dq68--iQIRey5u4W9fdj-pWth7iS1ryB3DgDtBhjINcpxq0SpzkF8vAgu3bLGZnpc6yJi3eR_oFLLaMRsr4uH7ydPqJRz845UTSpXPUCTNeCg8uZFKcXEzDqp1llgN15FEXLk5wpznrg5hbDj0zTP0-e7HNMv84nBhHS44Yk0Q15ymGEbZLDKhGQ1lIPg1zJYDntZZewbVXQHNzifKBhaYru-CsJgXzaxuwD13X-XzejmcrSJ8aNicMI11-JOCt5jDhScziMEpQFUkcYmNme4iE1_wtUiUiw7aWlNIQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d10f0225f.mp4?token=KfQX2yYMkn12lXb9hL2rhZIRxDGM966RJLRcxsf_P62PV_Dq68--iQIRey5u4W9fdj-pWth7iS1ryB3DgDtBhjINcpxq0SpzkF8vAgu3bLGZnpc6yJi3eR_oFLLaMRsr4uH7ydPqJRz845UTSpXPUCTNeCg8uZFKcXEzDqp1llgN15FEXLk5wpznrg5hbDj0zTP0-e7HNMv84nBhHS44Yk0Q15ymGEbZLDKhGQ1lIPg1zJYDntZZewbVXQHNzifKBhaYru-CsJgXzaxuwD13X-XzejmcrSJ8aNicMI11-JOCt5jDhScziMEpQFUkcYmNme4iE1_wtUiUiw7aWlNIQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با سرمایه یک ماشین و راه انداختن این کسب‌و‌کار تا ماهی ۳۰ میلیارد تومن پول دربیار! #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/697229" target="_blank">📅 16:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697227">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
پزشکیان: اینطور نیست که اگر امثال من را شهید کردند کسی در ایران نمی‌تواند مثل من باشد/ همه می‌توانند مثل من باشند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/697227" target="_blank">📅 16:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697226">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9825915b6.mp4?token=KAC76vnfgHWayE1KCNIqcn2ZEWFPtPRzyT_xqYwi1dVbsB1SshuNZpLaIcQZz01wdi34B31KAM47WIZSqr7flm1g43AdgfIa6RGC9i8TYB874yL0njusou-Vx0OCQYeon9VRcf_BmB5dvjKDQ53tznOfS7tBQu3OE3H7_FVSMyxXxycWBWeuO05Ygi3Eael_bZDrK4ygGg34TTzwj6-CAgcJNzcOhhF0ekSEE6R4l6Id9FXAbJK5FlswU_YlsPbCk5gNRtfArObA6AXTr0i6_VCiL1sTEUmn0DzMsX3lrSHkS9U9DTirvDf2s6DASL9yiTKor2qgGBB6aAMSvy20cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9825915b6.mp4?token=KAC76vnfgHWayE1KCNIqcn2ZEWFPtPRzyT_xqYwi1dVbsB1SshuNZpLaIcQZz01wdi34B31KAM47WIZSqr7flm1g43AdgfIa6RGC9i8TYB874yL0njusou-Vx0OCQYeon9VRcf_BmB5dvjKDQ53tznOfS7tBQu3OE3H7_FVSMyxXxycWBWeuO05Ygi3Eael_bZDrK4ygGg34TTzwj6-CAgcJNzcOhhF0ekSEE6R4l6Id9FXAbJK5FlswU_YlsPbCk5gNRtfArObA6AXTr0i6_VCiL1sTEUmn0DzMsX3lrSHkS9U9DTirvDf2s6DASL9yiTKor2qgGBB6aAMSvy20cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به فرانسه خوش‌آمدید!
🔹
جایی که ایستگاه «شاتو روژ» در پاریس، شبیه صحنه‌های فیلم «راتاتویی ۲» شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/697226" target="_blank">📅 16:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697225">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1949049c9.mp4?token=X3HkWKpBxCeFRjbtQat4v9cbY9Mte8KHzPgI6wWmpdT7kRZKf03oNBzwznscMscULyJ7p5AgMmUQWsXP4fpAc5t3GNpavB-ZNd4H3vBg7LOqfaHkvpTfrpiZ6_lL11RdwMIpEreR4Ns-rn8a5aOGGeAZa7aTILlwENG-eRX69eQcc4rq9XS8mhe8xBq6vgja1LLiNZy3AE2GTB3YZ2lSp--PcV-9aPO0MW1iEKJf9XEhdgNBOtjb9XXD04sgNS7AKmIRxVeWRwVgIhyQE2pr-wXz96x0XFNvNtDDR8FwoMGtULtu3t71dUiqtuOf72eVbPce1YeDeoCjeYIGdYJ3I4Ljd4JOVpkl0ZJsM9DsU7eUSYrzMGI5Kxwlmyq5r8gDP3lDma2VJ2c7LydOphB82wsn10f7WW4Eoa0O9aQ4u90z1ZC0FAJfCvrNixZcFTcOaMbxcGPygSjqzx0cmPrTrAuJCuvbWlbeb-d1p-3iXbW9yY_Kw8czkhdYUwmcUj3pOgSogamAVyJlmT4f3kpBFg2RpLh24c8s-BaZ9xbkSfVPFoJvan5kHF4-SJjOoCdlNaaGBygP0PX1pgkbt0X_eHNaWsFBWGTf4ScxyFMlYf0ue9jqffCG2GzAAP_kIg0Ovg9J0eTKXpEPvYNsccRrid_yI0OatpqVr8UkvfexQXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1949049c9.mp4?token=X3HkWKpBxCeFRjbtQat4v9cbY9Mte8KHzPgI6wWmpdT7kRZKf03oNBzwznscMscULyJ7p5AgMmUQWsXP4fpAc5t3GNpavB-ZNd4H3vBg7LOqfaHkvpTfrpiZ6_lL11RdwMIpEreR4Ns-rn8a5aOGGeAZa7aTILlwENG-eRX69eQcc4rq9XS8mhe8xBq6vgja1LLiNZy3AE2GTB3YZ2lSp--PcV-9aPO0MW1iEKJf9XEhdgNBOtjb9XXD04sgNS7AKmIRxVeWRwVgIhyQE2pr-wXz96x0XFNvNtDDR8FwoMGtULtu3t71dUiqtuOf72eVbPce1YeDeoCjeYIGdYJ3I4Ljd4JOVpkl0ZJsM9DsU7eUSYrzMGI5Kxwlmyq5r8gDP3lDma2VJ2c7LydOphB82wsn10f7WW4Eoa0O9aQ4u90z1ZC0FAJfCvrNixZcFTcOaMbxcGPygSjqzx0cmPrTrAuJCuvbWlbeb-d1p-3iXbW9yY_Kw8czkhdYUwmcUj3pOgSogamAVyJlmT4f3kpBFg2RpLh24c8s-BaZ9xbkSfVPFoJvan5kHF4-SJjOoCdlNaaGBygP0PX1pgkbt0X_eHNaWsFBWGTf4ScxyFMlYf0ue9jqffCG2GzAAP_kIg0Ovg9J0eTKXpEPvYNsccRrid_yI0OatpqVr8UkvfexQXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداداد عزیزی: ۵ بار تا حالا فقط سگ ما را گشته‌است/ دو تا سگ دنبال مهدی شیری و بچه‌هایمان افتادند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/697225" target="_blank">📅 16:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697224">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA_KwjOJCn84X4GTtTM0-c-FTpoVCgKHsY5yIU94XNSH-4xWFdHsyzBssqg3q_LG9hMayoLPB7bcgo-BktnAmkt0zGuhuwoCYscTIe1n41P-r2pmEIxF2QnnfQlL0gUxsAigsyJrKsfi4-uXhNUN__QqNG7MYnBeM6KmmyT5rxCHyh5t_A40EjGv1LmhiuXm_WBWayrRC0eGAAPQBs2-Lm98dR3g936RhMst11V_r4G0z0S6kEgaSp6wcpHC-Tmx9kfOoIA1f0bHIbNccIoDgU1tLRratghcXwJwTKnt4zvovi5xM7HGrukJtbdPEzvPraHd3g-U-_SxCo3xQTonDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
شهرزاد مشیری به ترکیب هیات مدیره بانک کشاورزی پیوست/ قدردانی از خدمات ناصر سیف الهی در آیین تکریم و معارفه
🔻
طی حکمی از سوی سیدعلی مدنی زاده وزیر امور اقتصادی و دارایی و رئیس مجمع عمومی بانک‌ها، شهرزاد مشیری به عنوان عضو هیأت مدیره بانک کشاورزی منصوب شد.
🔻
وهب متقی‌نیا مدیرعامل بانک کشاورزی، در آیین معارفه شهرزاد مشیری و تکریم ناصر سیف الهی، با اشاره به سابقه طولانی حضور مشیری در این بانک، تجارب ارزشمند و عملکرد درخشان در زمان تصدی مشاغل مختلف مدیریتی به ویژه معاونت بین الملل بانک، ابراز امیدواری کرد؛ حضور وی در جمع اعضای هیات مدیره، منشا خدمات ارزنده، تحولات سازنده و تحقق اهداف بانک باشد و مسیر رشد و دستیابی به موفقیت های بیشتر را تسریع کند.
🔻
مشیری پیش‌تر به عنوان معاون وزیر جهاد کشاورزی خدمت کرده و سوابقی چون معاونت و ریاست اداره کل خارجه بانک کشاورزی، معاونت بین الملل و عضویت هیات عامل این بانک را نیز در کارنامه خدمتی خود دارد.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/697224" target="_blank">📅 16:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697223">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A58bQLBq8lQOe4wg9MKnFnh0zlzY0mwlfWVbzBn2oxIKEARqOCdtbVnO0tzWWSUoLpzNlBVVkEbiWRwh2ElF9Voy6nuvW5R2-zKwh8MnlP8QuYktoimhpQIoAKGcMdVhP8_yGtUWExxTk0odx4RJYS0VGvUz4g-m2EJa6DCHQ6jzoglM3SLXPb8QqQhWllE9JCTX8WTq-4NZnl7fmswfMYZYVHvsSi69vgK98zaKmFWI6-SCDqL6PZd4KJFlakWA5m_OGXAaCz0YX9SMtd6IqJB3qCTottmVSLRx3cQOncp3VbQ1qygDvi8GdiNd7gh3dejg1MTc9tecD6oC2u8tAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع بسته های حمایتی لوازم مصرفی خودرو در سامانه جامع
شروع طرح از ساعت ۱۰ صبح روز شنبه ۱۸هر ماه تا اتمام موجودی
امکان دریافت نقدی و اقساطی
هموطنان گرامی می‌توانند با مراجعه به سامانه رسمی ایرانکو اقلام مصرفی حمایتی خود را به نرخ مصوب با محدودیت کد‌ملی دریافت نمایند.
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/697223" target="_blank">📅 16:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697221">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOChQ2VIyFNJaqA7a3tlyDKSdDMcP1Tibx7wf4D7geOY93vZwLBm7WkR0R_QoBkA7C0yw7CVrCUATSEI18Il6jTLg91AesCUt5UAFI3bv60MjIWn7W4hbLKHxT0BKmhfTnN5Gi-re80q6p8EwBWJnlmHkejT-ecEXcBuMM-WxDpQ88y2Z5ngGyKHGFeF2Sm3DZXehT84X213DArPVCsqKwNCNxawGj91uIhM17HLwIkj5YdO8XfpxS2khFQ4OUuEDuTzpkrkzh4_VHcEjMbD6qeAVn95AqaYNdje51zB0MUiYVJRU9iBnutBunLIoHy2s0ez7WEbivvh4ajAK7SBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه‌گویی معاریو: ترامپ از اسرائیل خواست پیش از انتخابات میان‌دوره‌ای بدون مشارکت آمریکا به ایران حمله کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/697221" target="_blank">📅 16:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697219">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
پنتاگون برای جبران کاهش ذخایر موشک‌های رهگیر در جنگ علیه ایران، قراردادی ۶.۳ میلیارد دلاری با شرکت ریتیون امضا کرد
🔹
بر اساس این قرارداد، ریتیون طی پنج سال موشک‌های رهگیر SM-3 Block IB را به‌صورت مستمر به وزارت دفاع آمریکا تحویل می‌دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/697219" target="_blank">📅 16:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697214">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZsFH4gIMYL3UxmYU62nSkJz33D3Kmr_dbzmC6--NcURpLyMFfs5kw_fFaf7Px8hsDnNBJatWC_8v0K748d4WDKC_ZVxQ86MuDBLBBTkppWwK6xfxmCf7oMooFmrdLMjF2hRowPzMzGhWY5Gvdc2btq2tDYQX4D4m7VcfsQ28HAaRjz-X3G3C7LZKHlt3DXhP7iNuK14s8FN84Osi0KWgRcwIEl4AZgiP48wPinef19fJww70GkjWlXzCiSoriMqwdCGV54u18c9QIxCD2bxatgPS1hTMvttRS0GGOxnuDo2C4oSQKcFQsHTK1bqmLylhNEhRAXywl-Ww1uf-wM0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mID3a5Fk5FvQVU3ldi7SXnpcO3qck5mlw-ajUsOv3VZ4t7hbxP52iw5tdxowUyz_nAOEoY7ZhWfcrbGem2EH4yCy7Aor5FM9Zmg47515cYR8bWEyiLY4x5NkkaY8cnCRXs9seAXr4GxVE0QwebTpnhg9aBzayhR_8AWaJDtafet4ThbiWvuA7FpV_rIzohN5K7WqFCGrzK7Z1OrN8cohQNVAu1z0Jrp9rxFe6nfsSR98KbLF-WgbSNOpEwL1SW93BanbYZ-IqeQdxl05HRqEXI1I7kCXIW7ty-x3BdfxVeUxIz_8NFL1v2W7vrJnzfhCM-arffktonqZL7JEFhoTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUx8_O4J9hjgw0Bj8T9LqkenKN0nFrqQmARlr9iLYuC4RPtj44VxsPQRLVSZN0D3uPAe7BzqF4A5eaHpPUZtF4N0f3mfSAEJvKzGr1p41X3E7LpBDic-sqaCRoF0owjX2wvNBiyH5Z14zxN1BwjfLUXx3JCOXTRhOEaolAL1u19zPeC08GJWZYcpDPB5uVNqXCuu7d_tt8mP-chxXuJvRRrY6SwB9yAwPvjFq_F18Ieliw81VjvbyD7SRYaOdAogLER8jPLjYChkHRVAw9XTpR_md6WhzTzw2CU64L5gxqI8RZyvqdHPJd_p_vtWIMXXWch47a3v25-4C5rkoI2ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFmLY9W2o5d81Ewvm6kobi_XKCDw2a6-IOLjV7P-zTEfYHarX4BKA44nOXt0GpOXE-DTjckdoXPHwQCGSDCnlVH7I7pWVuZ2a4ZsSQxhYcIm-8-obYDOi3AlNVXbAV0IwGazZrhCIPcMWVGg11S6sh7V2GCAObM0rf71nU3CeW_Y_aYDcuEjQ_-TCqwBfN6MlTPmP78R8P15jOghUg6wqRWRjOl40EWedl0TOdoxU0yKY4eTrM3QSulkKfVX8OO9C4Q6ekvF2sFaH3xKuQ60BcwaApuo7K5Fyo0pq1SEmaJh0K0pLOBwtiOVZun86-z_oLxMF1jVZHHELfwt3MuUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHrFRbn8MWEyXEyNV_kipNN1hYHHeh2n0ERmvA0CdD7sBhmJ9qVblj6ABmeuPoMraiatygfLxqS2qJBvfK3FgMzv-BmCm0ruHn5ovzVRqOz8YzvPcwoo7STtoOOi8eotSMr4dA2mtfYfa7Spkjol1Up0926fpCxpUIDYloiA_hoZ9EXERQoMFIHJ1Pr2JU_tix9HwtauynEz5bG9leyCE3d9wU4fjKQSFxNSqfXejx-B64u-4aEks1tBNfRObRbfRmECEnibalGAP8t5Y8QioyBXUDwg0K1OG_s3Gy0YpPEookrBRtnUWpOliRrdrnfUEGgsASUgeE3ZsiPG_k4_pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برای هر بیماری، چه تغذیه‌ای مناسب‌تره؟
🥗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/697214" target="_blank">📅 16:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697213">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
لطفعلی بخشی، کارشناس اقتصادی: تصمیمات جزیره‌ای، سیاست‌های ارزی بانک مرکزی را تضعیف می‌کند / سیاست ارزی زمانی نتیجه می‌دهد که هماهنگی میان دستگاه‌ها وجود داشته باشد
🔹
تصمیمات مربوط به تخصیص ارز نمی‌تواند صرفا بر اساس مسائل یک وزارتخانه گرفته شود و باید با سیاست‌های کلی دولت و شرایط اقتصادی کشور هماهنگ باشد.
🔹
وقتی برای تامین نیازهای ضروری کشور محدودیت ارزی وجود دارد، اختصاص ارز به کالاهای لوکس و گران‌قیمت نیازمند توجیه است.
🔹
سیاست ارزی زمانی می‌تواند نتیجه بدهد که میان دستگاه‌های مختلف هماهنگی وجود داشته باشد.
🔹
اگر وزارتخانه‌ای تصمیمی بگیرد که با سیاست‌های ارزی کشور در تضاد باشد، این موضوع نمی‌تواند صرفا در سطح همان وزارتخانه باقی بماند.
🔹
نیاز ارزی کشور فقط به یک بخش محدود نمی‌شود و اگر منابع موجود به یک مصرف جدید اختصاص پیدا کند، نیاز سایر بخش‌ها همچنان باقی خواهد ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/697213" target="_blank">📅 16:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697212">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
اعزام زائران عمره که قرار بود از نیمه مهر آغاز شود، به‌دلیل نهایی‌نشدن جداول پروازی و تخصیص‌نیافتن ارز زیارتی به تأخیر افتاده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/697212" target="_blank">📅 16:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697211">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL2a4sf8Ss4j8FBFqNYX1pyAYjRaHZzYygHCV_rcpIhPSEoySdDS9x5If8gNjxMqdofo2ZutQgrQ6wxTceOj5DruuZVl94Drcw3IG16uUKDpFQ8EgbaltiNQrStDaNJPyuhJk1mdEK0V36C0ogWqYtQXHnpo9wEcAotJefy3BrUNTxIjSASga_c0sDUxUqG7CtX0TbFLfAF9JYH7mpl83ok7dqclcHg8XtvuqcTMONVADR82j1e4nqj7X6yd17ZLStePc7q7ssRkjO7f34n3UxUWnSGYK-1lE3CAtvH5sIiNfNqDKyZyqytz1be9Is3tkscyug52ddrPg7HKjd2QWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم اکنون؛ رنگین کمان در آسمان اراک
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/697211" target="_blank">📅 15:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697208">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/503f0a9d2e.mp4?token=pw6sh9gm7TW4buyfJAeaz8ZiA5tRYflQS6pU_xQW4NPH-hlrmgNOkqmxOh5KaC5XeWu05Oqlp0OZ5mFEGC8IIhYhczAbeWKRIQqZczmS2mA7osfqyGMSQj7QiP7GUBmxNYSZlJMxp5RZOPpK83kGB7kzPCG2FZ_2R_eZFVSmNEhN4PYxgAWT0EwcrPjFX7aCPY3cY_iTY4d_YjGjbA5TiZgBWXsrPX24o4bquuVdktGttzbXvLfwZ3cQrthHeOOhGWhs6k24pEN0LZq5MN90qehlsANSlheVRRSUBOsSvRW3o4ovEifGwwnPIrRDXh4g1SVh3oNR66vh9EQkBfNZhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/503f0a9d2e.mp4?token=pw6sh9gm7TW4buyfJAeaz8ZiA5tRYflQS6pU_xQW4NPH-hlrmgNOkqmxOh5KaC5XeWu05Oqlp0OZ5mFEGC8IIhYhczAbeWKRIQqZczmS2mA7osfqyGMSQj7QiP7GUBmxNYSZlJMxp5RZOPpK83kGB7kzPCG2FZ_2R_eZFVSmNEhN4PYxgAWT0EwcrPjFX7aCPY3cY_iTY4d_YjGjbA5TiZgBWXsrPX24o4bquuVdktGttzbXvLfwZ3cQrthHeOOhGWhs6k24pEN0LZq5MN90qehlsANSlheVRRSUBOsSvRW3o4ovEifGwwnPIrRDXh4g1SVh3oNR66vh9EQkBfNZhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بعضی وقت‌ها رگ‌های دستمون برجسته می‌شن؟ #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/697208" target="_blank">📅 15:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697207">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngWZ-jp0TdXNpsiR01uPp2fTqJ7ONUxZXgMV-4izXUa0PqAhCt0Uj435P8rqKtBD2Hp-6zcHSXlPMnrmbk5yXF2QsvFD5xOPOowuWhKvl7Tn3vr6f6hDNfjc_Xe4QF2zFD3u-UJeXMRv_oQIy7Jd6P70HBMr4eHBIZcJl7UVxAmES5vt-OF1o8yk40khOmhMpwUJtmA6jfdTzvlYjZoIhiJqld_iv6v7QaV3dWFiqPs9A47E8hACzhIlXcyGR439vm2tTK3E_d3qXtG_DOQ3Xf1cjMmkby-o9ScqKuwus9urnZZnPTBSIPsLBbdeCl2eYYS83v0dhTs3PkgcbJ1LSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ سفارت ایران در بوسنی به اظهارات روبیو: آفتابه ایرانی ده برابر کشور تو عمر دارد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/697207" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697205">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ظریف: آمریکا من را به‌دلیل حمایت از رهبر شهید انقلاب و نیروی قدس تحریم کرده است؛ سخنرانی اخیر بازتاب‌یافته نیز مربوط به دو سال پیش است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/697205" target="_blank">📅 15:29 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
