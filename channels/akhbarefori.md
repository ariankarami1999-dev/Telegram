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
<img src="https://cdn4.telesco.pe/file/DglKu2MKBPRGxrPo1lOlfAsttA1y2jDYXKZOTmWm1AyQMc6b-GU9AnS_IFJXz0jPoEJEA_xJp07d9YueqW_Fw-KuIKMeg3AGgd8xjSNAfR8imPqCYmQzVvrK9Ta2WrfcjWF-KdBDBQAllJbre9ibXT8iI7kjHSoCFdH79MNeygau35F3qWtddf3aJUfSVh-o1l4KsnRmtPEAkioBP9VMJEpCFUwG7yVQcKIvO5_w7eTykrVBlBRRZsvAJBstjg7RLOpyl4GBJE8M17Cr6tH4sXfPXo11USI_RVrZ8j9ZCl7FNoPH3VaQmbTaW401V272latSiU-OxC3tagkasKvMHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.12M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 19:16:49</div>
<hr>

<div class="tg-post" id="msg-682020">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99c0d9fee7.mp4?token=beDMz9UqaYnyQEWPZoW9FYMq2KI2W556A54GR1xrgG94pArQmyIr09DP1ennXTMk1lWzAsfnsDwg451BSdvrfip26znavhqxc-qcSNcEM4TNN718xPISYjuAJatRjmVij1wikneTOUJqK1ULwCTY8Jylj8ZaGGtxR_uXfd3pqPm4sabDasSUaPhkT4U1DvdwRd9rKdv0FFxRC7s2ynrg9RrSWyTtrn84uEU9SorThM8I8c4kZoZS6a5uBKHhpVsGzqF22wC2sH9Wdgx9cZJh0PT1Cj6jW0QOXSEARJI0i0JXL6mEuxS_AvJTXD3kxUHRgQ_lEmVWWGlRET2Lgxxc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99c0d9fee7.mp4?token=beDMz9UqaYnyQEWPZoW9FYMq2KI2W556A54GR1xrgG94pArQmyIr09DP1ennXTMk1lWzAsfnsDwg451BSdvrfip26znavhqxc-qcSNcEM4TNN718xPISYjuAJatRjmVij1wikneTOUJqK1ULwCTY8Jylj8ZaGGtxR_uXfd3pqPm4sabDasSUaPhkT4U1DvdwRd9rKdv0FFxRC7s2ynrg9RrSWyTtrn84uEU9SorThM8I8c4kZoZS6a5uBKHhpVsGzqF22wC2sH9Wdgx9cZJh0PT1Cj6jW0QOXSEARJI0i0JXL6mEuxS_AvJTXD3kxUHRgQ_lEmVWWGlRET2Lgxxc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکاف هذلولی؛ جایی که هندسه غیرممکن‌ها را ممکن می‌کند
🔹
در این پدیده، یک چتر یا میله صاف با زاویه و چرخش مناسب از شکافی با شکل هذلولی عبور می‌کند؛ نمونه‌ای شگفت‌انگیز از اینکه هندسه سه‌بعدی چگونه می‌تواند چیزی را که غیرممکن به نظر می‌رسد، ممکن کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/682020" target="_blank">📅 19:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682017">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8Q_OIiBzQqUjV6DmKZGUSMsKFvESMKKBmHIkMThFJK2RFVtB0XRFsqqtybgakqcP_jK6jMtDyKVGhgPdZm3T4C2AzDHZiR7lFhKWW9TeOJjxNYD4Xt19Uf66ofoeBrTtGIJ5Ofz2iBsxoyJD_zRET0I0xqipc__nDt7Pk8eSMHrmsaTVkM30J_ksqkiFbx9X4hoaqW5YOIpjbQigGoDVunY_ZlCmjgzSVXCB2tOz-4fAs_2Vo3NJW9iPamXobWTVW93Yxh7f58eZ7JQw-EBiImuOoz0jGuCJzqtgGxWLD0GgWy2tLHlHIH2S7LuZfvY-MtPnHtphhnhQe2poWg41g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhV4bzAwebCnJ2R80kILAL9OUaGyM78NLoqqh4Zojv1AGYGpdI46HnWG2FvsA0EiqeLdWAJEsYlMAtz69pxsD67_HKgRdB5bpDc1aFzIN4W3IsBRhO_GPm8m_w__hveDGHHkIhOBbt66Gh8hkK-ILjqpY1zy7zC9CV6uEsZ6o9a8Vc0C78vrydpbSf-lcXTzIPEEjoCBD_fJL5hckj71c1MmtJRLjz9_bWd1MkMxsa21jN9hL8X2aGu68BPrmGzFgEX6Wh-6IMn-_E4HcSVinTGFHaf0sp3MWoD1mnXNSKzTkph5N78_lg_X3CgKeZMEzhu7hakul6WgfxHCh_7DAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آتش‌سوزی مهیبی در یک انبار بزرگ گاز طبیعی در گلنپول، آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/akhbarefori/682017" target="_blank">📅 19:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682016">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b13ccc88d.mp4?token=a2Copt5VI2KNIpkGS8-eU1N-GLD0_LW3EEi0M4ayT0vF4v_IUuQDzborfOuNs2-qSbw2N5A6XbPpKLS1c9l5k-ZjTEDItoie8tXcImuGkxhJ3iipH41bEjCRYnm2y7ox4n32RY1fPRrc2JEm3nJOjFoj-G7ku8jrIOXteaFGElivPj-DGw6_NVQtg_8yET6lWF1ZdMK6FeV4NcVIhkzv274gQVCLz4bkoLSU8u2fEZzPG3I4fqnzZn1Z-OoV3sSXybqqs-3qopgimnmfRLymNXSg1FiTaEY_rHyl-yJJCoY5wV_7WsOS0y2dyLBBPsk1X8ihBKk4Vir6iog48N6ivJ8u9mt4-FcYhF0RCIaWkZpdl394a4FzVVpBRc2lsrBTAYKeB73DY6Cb_eixzNzZd5s-Frm8nV3UJlUVX4AypmCvjkbkrjDaYpXUa4gO9yJuN00FQubjdAo4skM8rF1_VzxPsI1tE6QxQosfImuR0swrhVi6hhtqrQ7b968bivC-HRf3mMoSedCF24Na8Tmt2fNdhbDpVsq197-rdxPdvmp_CUwct-dEBs_VBl8847VWumf220CYW9fhT3JUMLcVXryZhP12pb69vqKEnTQr3E6UNir3rTNCEnSUhIovly14Zf0BfCXss30JXbAsOqcriigF0awiJTfQ6QkYBdqTFYk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b13ccc88d.mp4?token=a2Copt5VI2KNIpkGS8-eU1N-GLD0_LW3EEi0M4ayT0vF4v_IUuQDzborfOuNs2-qSbw2N5A6XbPpKLS1c9l5k-ZjTEDItoie8tXcImuGkxhJ3iipH41bEjCRYnm2y7ox4n32RY1fPRrc2JEm3nJOjFoj-G7ku8jrIOXteaFGElivPj-DGw6_NVQtg_8yET6lWF1ZdMK6FeV4NcVIhkzv274gQVCLz4bkoLSU8u2fEZzPG3I4fqnzZn1Z-OoV3sSXybqqs-3qopgimnmfRLymNXSg1FiTaEY_rHyl-yJJCoY5wV_7WsOS0y2dyLBBPsk1X8ihBKk4Vir6iog48N6ivJ8u9mt4-FcYhF0RCIaWkZpdl394a4FzVVpBRc2lsrBTAYKeB73DY6Cb_eixzNzZd5s-Frm8nV3UJlUVX4AypmCvjkbkrjDaYpXUa4gO9yJuN00FQubjdAo4skM8rF1_VzxPsI1tE6QxQosfImuR0swrhVi6hhtqrQ7b968bivC-HRf3mMoSedCF24Na8Tmt2fNdhbDpVsq197-rdxPdvmp_CUwct-dEBs_VBl8847VWumf220CYW9fhT3JUMLcVXryZhP12pb69vqKEnTQr3E6UNir3rTNCEnSUhIovly14Zf0BfCXss30JXbAsOqcriigF0awiJTfQ6QkYBdqTFYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف یکی از فرماندهان ارشد ارتش رژیم صهیونیستی: تهدیدات ترامپ علیه ایران برای ما هزینه‌های سنگین و وحشتناکی دارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/akhbarefori/682016" target="_blank">📅 19:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682015">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای رئیس اقلیم کردستان عراق: دفترم هدف حمله پهپادی ایران قرار گرفت
🔹
مسرور بارزانی، رئیس دولت اقلیم کردستان، مدعی شد دفتر شخصی او در حملات پهپادی ایران هدف قرار گرفته است. مقر رئیس سازمان امنیت اقلیم کردستان نیز هدف این حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/akhbarefori/682015" target="_blank">📅 18:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682014">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
تلفن رئیس دفتر ترامپ هک شد؟
پولیتیکو:
🔹
فردی با جعل هویت «سوزی وایلز»، رئیس دفتر ترامپ، با اندی برنهام، نخست‌وزیر بریتانیا، پیام ردوبدل کرده است.
🔹
مقامات لندن هم  احتمال هک شدن تلفن رییس دفتر ترامپ را مطرح کردند، اتفاقی که قبلا تایید کرده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/682014" target="_blank">📅 18:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682013">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4b9b8fd26.mp4?token=f_00MMGL0_twgQxxW33x4BO0SNbqTNwYQEXlE9r6sm1UN4wfQaLyXdV2R1n5ZhTSY0SytBFNzdRLQAdM4_ajsCkRs4qhw22VY8k5_Kk21nKmtKiCgux33aCHgJ1SF1mn6qI2bQw-_ee0NezI53DgRYjS6gikAHGrsnUJzMswCxYn8bwY2fyOBRp841jy3j-KM0CJJXWh5ygMRUNuR9m4hKnH9uLBi7j0hGNkLwtBfQO9HsELwY6SW-Zll1CAwZlaT6O5ANeuMxeg8537M-vybX2wQjvg1hAy7CCRMa4sEuS4SaVwIfKHrt7sYp3C191fbaz6P730b3P_92gSDi8dmgoKx_pCBTzn2EvAlLYSysnfoSEg7ERkR2qgeYYTopgH2GdIW30aDr39NHwGCtLxuc9je5AUui3n7tia3XQ-sRFVio4437rDMYpoHueHq9MAVh85B6235Ug4RiQph7M9h4pDxWnmvo5dTlF5mnQVlrXLcwJrSCkkTGyi6XRmbSdL8R_XwxseRNzE0eH-Nmbmx1rfkvUbOzWeyDjjUMOHxovlqs59QGrPm8SggJjGza9sGs61vQz38hcTb2We8WEuPe0lmpFsB3E00UmqYAZ6sIF0L76-7sGaBDau-2p3of_aseFLJ9eCKGvBC24dwUj2YeTF5QdsumRrlUjovtUErfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4b9b8fd26.mp4?token=f_00MMGL0_twgQxxW33x4BO0SNbqTNwYQEXlE9r6sm1UN4wfQaLyXdV2R1n5ZhTSY0SytBFNzdRLQAdM4_ajsCkRs4qhw22VY8k5_Kk21nKmtKiCgux33aCHgJ1SF1mn6qI2bQw-_ee0NezI53DgRYjS6gikAHGrsnUJzMswCxYn8bwY2fyOBRp841jy3j-KM0CJJXWh5ygMRUNuR9m4hKnH9uLBi7j0hGNkLwtBfQO9HsELwY6SW-Zll1CAwZlaT6O5ANeuMxeg8537M-vybX2wQjvg1hAy7CCRMa4sEuS4SaVwIfKHrt7sYp3C191fbaz6P730b3P_92gSDi8dmgoKx_pCBTzn2EvAlLYSysnfoSEg7ERkR2qgeYYTopgH2GdIW30aDr39NHwGCtLxuc9je5AUui3n7tia3XQ-sRFVio4437rDMYpoHueHq9MAVh85B6235Ug4RiQph7M9h4pDxWnmvo5dTlF5mnQVlrXLcwJrSCkkTGyi6XRmbSdL8R_XwxseRNzE0eH-Nmbmx1rfkvUbOzWeyDjjUMOHxovlqs59QGrPm8SggJjGza9sGs61vQz38hcTb2We8WEuPe0lmpFsB3E00UmqYAZ6sIF0L76-7sGaBDau-2p3of_aseFLJ9eCKGvBC24dwUj2YeTF5QdsumRrlUjovtUErfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنرِ کفاشی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/682013" target="_blank">📅 18:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682012">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یک عضو ارشد مقاومت عراق به دستور آمریکا بازداشت شد
.
🔹
سازمان حج و زیارت: سفر عمره از اواخر شهریور آغاز می‌شود.
🔹
الجزیره: عربستان برای دور زدن باب المندب به انتقال محموله‌های نفتی کشتی‌ به ‌کشتی روی آورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/682012" target="_blank">📅 18:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682011">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88583c85a3.mp4?token=Q90xLEniRRhLtealaFO7xwd1ZIpdms1gzvNd8NMj9B9wZEz3E0y3vxY9a_3xGnFYlolnKb5d4ovMnmJolY6Iwr2cPrfg6ENQR_evVAi6miAA4PVgw0jnGO4BStF6ImxJGkG7BzzMa854UWCahuellxPF2f7eiaKF4qEMjENPInYy1w0vVbgU8d_U7R-78t_BjBEHjjloldxOZhMWrYnpbqkU6J8pSmnxRFoc2xAEpVj2Ht464YBCYuynfCrr669GB-JdLj1Cdw_vYeR-q9qWGzqBhZbA6rw8A6d_bt0qd6ChzRGexBCgtSLt8IYV2u_o7O9Q09r8P97gQgTZnBFuM4fCbuf7iMHZPLrwIZK0lVr3mi7bnkSKq3rfxFdJr3Sz2LsX-LCUDBMaVAUlnjNciwDR3UST9d40-1nYjFOmal3-Czjvoz0lq3Q9__KCmwNmq-N_i3UrGTcXC8p6NvZZH2r4eH6sswU1JppDhhn2qCe2kKIdqJ0zF2spS_ZysLIKTDm6uilK_zztDX9AZs4WjbcJdIjSp6FW-rj11MdFyju8VFcu7AXu6bZJhGSMjcfM3_bpJEv_7QLdUK_2Uc2jmF4uMyVIVyBCy3HbBjAyLEMlTme5wCiZTrUPYE3sXIkS9EnUDvU2u0TvUGge-lWRITxH7DuLftUcgtaO7T2fgNY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88583c85a3.mp4?token=Q90xLEniRRhLtealaFO7xwd1ZIpdms1gzvNd8NMj9B9wZEz3E0y3vxY9a_3xGnFYlolnKb5d4ovMnmJolY6Iwr2cPrfg6ENQR_evVAi6miAA4PVgw0jnGO4BStF6ImxJGkG7BzzMa854UWCahuellxPF2f7eiaKF4qEMjENPInYy1w0vVbgU8d_U7R-78t_BjBEHjjloldxOZhMWrYnpbqkU6J8pSmnxRFoc2xAEpVj2Ht464YBCYuynfCrr669GB-JdLj1Cdw_vYeR-q9qWGzqBhZbA6rw8A6d_bt0qd6ChzRGexBCgtSLt8IYV2u_o7O9Q09r8P97gQgTZnBFuM4fCbuf7iMHZPLrwIZK0lVr3mi7bnkSKq3rfxFdJr3Sz2LsX-LCUDBMaVAUlnjNciwDR3UST9d40-1nYjFOmal3-Czjvoz0lq3Q9__KCmwNmq-N_i3UrGTcXC8p6NvZZH2r4eH6sswU1JppDhhn2qCe2kKIdqJ0zF2spS_ZysLIKTDm6uilK_zztDX9AZs4WjbcJdIjSp6FW-rj11MdFyju8VFcu7AXu6bZJhGSMjcfM3_bpJEv_7QLdUK_2Uc2jmF4uMyVIVyBCy3HbBjAyLEMlTme5wCiZTrUPYE3sXIkS9EnUDvU2u0TvUGge-lWRITxH7DuLftUcgtaO7T2fgNY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در یک مدرسه در غرب کابل
🔹
لحظاتی پیش انفجاری در شهرک مهدیه، واقع در ناحیه سیزدهم شهر کابل، رخ داد.
🔹
شاهدان عینی گفته‌اند این انفجار در یک مدرسه خصوصی، هنگام خروج دانش‌آموزان از مدرسه، رخ داده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/682011" target="_blank">📅 18:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682008">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d93c2708c.mp4?token=YA3Z5K_becNH3yCgB21g3YKgLX65wC44QXhOt7Yhc-l0pmpyBgh4gO_iWQmwEJrWk8DenG3_-oEUwvkODnqOsdqaH1higUxBGCJtRzaCSVQWrYKGViLABjBz5XmBoCX77MgEZcshplHsCL_qyj2vANOSxMV9G9N-kTXDo8xsrrL-9nN4m0xNJRwQ5l0ItBUs0S53_CWoDzeyai7eDgwA4cdS5dVtdbLwJztNfu9Rj6wShjIV4QrRoAJk_gmWXhBL7GDE4Rllh2f2gF0VYKqa3dj_sh7MNk_OdSDadD8YyftxwszCR9Qy-ACpSvlYjawT9oWFDjFlwMRlUOlGOrsD_2ILiPF3qsrfcSGZhedHuAsIwaMVCfaVfHZtB5vMx75Z2UjbGnmpFP55PvT340dobgPq5GGDrsq7bRoAn2Hr4VilqVoJVqVlbz0wS_Ps0gTAOtorHgX4x2y6T5_karLDpvb8b6u7QNu5r8AEhGV9dT49bh7DwVbe2sDCNP0cNsYQOx8p_V2r3ZmCrNrvPzBXQDMsFT9airre0z1P3Yzmyosu_p4dyVx2RhstnywC8nPRTdqVFFp5WPfrLabuTNjVD9n8Lkh4vOeMfaT2iLlq6Q1qnFng-SqARvj3b1BXWJmVP1ZvXZAt-Q5u4GNnrVe7uwlGGszMEknvPIKbPMRscOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d93c2708c.mp4?token=YA3Z5K_becNH3yCgB21g3YKgLX65wC44QXhOt7Yhc-l0pmpyBgh4gO_iWQmwEJrWk8DenG3_-oEUwvkODnqOsdqaH1higUxBGCJtRzaCSVQWrYKGViLABjBz5XmBoCX77MgEZcshplHsCL_qyj2vANOSxMV9G9N-kTXDo8xsrrL-9nN4m0xNJRwQ5l0ItBUs0S53_CWoDzeyai7eDgwA4cdS5dVtdbLwJztNfu9Rj6wShjIV4QrRoAJk_gmWXhBL7GDE4Rllh2f2gF0VYKqa3dj_sh7MNk_OdSDadD8YyftxwszCR9Qy-ACpSvlYjawT9oWFDjFlwMRlUOlGOrsD_2ILiPF3qsrfcSGZhedHuAsIwaMVCfaVfHZtB5vMx75Z2UjbGnmpFP55PvT340dobgPq5GGDrsq7bRoAn2Hr4VilqVoJVqVlbz0wS_Ps0gTAOtorHgX4x2y6T5_karLDpvb8b6u7QNu5r8AEhGV9dT49bh7DwVbe2sDCNP0cNsYQOx8p_V2r3ZmCrNrvPzBXQDMsFT9airre0z1P3Yzmyosu_p4dyVx2RhstnywC8nPRTdqVFFp5WPfrLabuTNjVD9n8Lkh4vOeMfaT2iLlq6Q1qnFng-SqARvj3b1BXWJmVP1ZvXZAt-Q5u4GNnrVe7uwlGGszMEknvPIKbPMRscOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک تکنیک ساده که همون ماه اول خرجاتو کم می‌کنه #چرخ_زندگی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/682008" target="_blank">📅 18:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682005">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaUrgS58pneg8jg1-8P27TY__FOMwoa_EYo2VdaNczuOAomNTbj1C1cP6sXyg7Q2zSGum-0RO7I5T4tVMuaLhLa43cTmJLH5MWtTAq9CNBxKATlfg188cxeNY2H7TQ5c0p9_zYh2nn02Z8zjpHEiJariE6nFIv_oz0hKYG0lJsb-qmkiyhiKlTOdDTrSaI0AujPRpb1acMziYP9dZMxAnq-ibd6XzL020utuJOK1eN_mDQDWXZePQdjgIf-R5y1JHFcrBClT_S5lTlw7Wj-NQYkrgCMevNChW_uaik29vMl-4L1zIClDYoQqhJ9Qd2zAwqf1jzV9ZwW1Q2WCAOKpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۰۰ میلیارد دلار زیان در بازار سهام امریکا در معاملات ابتدای هفته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/682005" target="_blank">📅 18:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682004">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aae993a9f.mp4?token=o9bZoNlJfvbcR40Uc8tHygDujs8S_m-IkRAnCsGLL2douIIfGU-Jx_oKgaVOamFWcx_DLvFoQdlnBVqkNm7neW24vWd46o3DvNZVHkegAKXIEC6dhNCqd9s6D8JEl8Sb4mDbNl3g-Nc7mUW-uk08aG1-f_JLMgbdqowieDZhzW5WAWNSDwPoaQeJCog42dr4YInwdhQRQ1RjLD-O0gP3opGlwobMCC2RCrGO3AqpDT4oky_IHjaa91Tipee2-7xLFXQSuzNESwmpLHl09k1yXj4_zHZ0NoDYpM4QliDxJ-cvaK3a-6nR07WglinAnQtzTsgHzsiM7GmFVp15bAR7IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aae993a9f.mp4?token=o9bZoNlJfvbcR40Uc8tHygDujs8S_m-IkRAnCsGLL2douIIfGU-Jx_oKgaVOamFWcx_DLvFoQdlnBVqkNm7neW24vWd46o3DvNZVHkegAKXIEC6dhNCqd9s6D8JEl8Sb4mDbNl3g-Nc7mUW-uk08aG1-f_JLMgbdqowieDZhzW5WAWNSDwPoaQeJCog42dr4YInwdhQRQ1RjLD-O0gP3opGlwobMCC2RCrGO3AqpDT4oky_IHjaa91Tipee2-7xLFXQSuzNESwmpLHl09k1yXj4_zHZ0NoDYpM4QliDxJ-cvaK3a-6nR07WglinAnQtzTsgHzsiM7GmFVp15bAR7IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری تازه از لحظه وحشتناک وقوع زلزله کلمبیا
🔹
تازه‌ترین آمار از آن حکایت دارد که شمار جان‌باختگان زمین‌لرزه ۷.۵ ریشتری در غرب کلمبیا به دست‌کم ۲۸۸ نفر رسیده و بیش از ۴ هزار نفر نیز در این حادثه مصدوم شده‌اند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/682004" target="_blank">📅 18:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682003">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqjfTOxGikAarDEVgvjobzj4oZFMCuEIVIPwzLXVUPQ4Zc0CXxYz-dxGFl-02BESnirPazl9YPivHUtHicxkAFupswiG1Su82Rn9NrxV2jSt5R5DMF0WUr-ux_qO6rJ_r3GoHjyYfhBuwUa7UckmtcpEIIDjMqk_s2NLZse7bu1GlQk2Bt9w-81RWqZsMxo7_b-VurEf9h9T7SZQwu30UzLIX43-DynvPGO-O4hxydDhr-WYhfGO5bxrSkpR-6llFUer3C8rEVN7-9YDIRZA2dR_lDyfT5i2UDkDJlIPVj7bLbkEVoN8DuOzAWg0DXVpVQ3R1VOCrdjPP_X6KNM8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهرمانی که نامش با قدرت، جوانمردی و افتخار ورزش ایران درآمیخته است؛ جهان‌پهلوان تختی
🔹
غلامرضا تختی، از بزرگ‌ترین قهرمانان تاریخ ورزش ایران، تنها یک کشتی‌گیر پرافتخار نبود؛ او با منش پهلوانی، احترام به مردم و روحیه جوانمردانه‌اش به نمادی ماندگار در فرهنگ…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/682003" target="_blank">📅 18:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682002">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
کپلر از توقف صادرات نفت عربستان از تنگه باب‌المندب خبر داد
🔹
داده‌های شرکت ردیابی نفتکش‌های «کپلر» نشان داد که عربستان سعودی در پی افزایش ناامنی‌ها، ارسال محموله‌های نفتی خود از مسیر تنگه استراتژیک باب‌المندب را موقتاً متوقف کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/682002" target="_blank">📅 18:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682001">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9DBlp22yQzFZReDOFfa83TxkjHIm2wUOMBYP69bmNL87w-SGsXVHlLWCOLFN8FKwl6Crwp2ixKeq3GkqBcYlUm58yaYyByMQ2e2WICz-_FfT_qKCZHj8V-ahSvJiZoXGo9sQXwXityApPbZd0Y607Pu-hMpd3XXVaI4YtQK45neKt-VAzBb03DKb_QFz6pmukj_2IKNPoRymLRpoJkFniH86axbqMMMCEd9-c5Hr0C08i8MIhAolOiWhry2o2w8Q_zrqtWNXdyIyJbTN_zS-6qb0obSCUViS3MiftybIiBnWkOzvA4_7GkgECmSZtYBeziowEWK82S7Mf0eKTpVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۹ سد برق‌آبی ایران پُرآب‌تر از پارسال
🔹
بررسی وضعیت ذخایر سدهای برق‌آبی کشور نشان می‌دهد ۹ سد مهم کارون۴، کارون۳، شهید عباسپور، مسجدسلیمان، گتوند، دز، مارون، سیمره و کرخه نسبت به مدت مشابه سال گذشته آب بیشتری در مخازن خود دارند.
🔹
سدهای برقابی سهم مهمی در تامین برق تابستان دارند، با این وجود در روزهای گذشته، قطعی برق شبانه و خارج از برنامه در بخش خانگی و همچنین قطع برق صنعت بیشتر از گذشته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/682001" target="_blank">📅 17:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682000">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
انفجار در یک مدرسه در غرب کابل
🔹
لحظاتی پیش انفجاری در شهرک مهدیه، واقع در ناحیه سیزدهم شهر کابل، رخ داد.
🔹
شاهدان عینی گفته‌اند این انفجار در یک مدرسه خصوصی، هنگام خروج دانش‌آموزان از مدرسه، رخ داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/682000" target="_blank">📅 17:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681999">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: کوشنر بیش از چهار ساعت نتانیاهو را تحت فشار قرار داد تا طرح آتش‌بس ترامپ برای غزه را پیش ببرد
🔹
نتانیاهو در برابر این فشار مقاومت کرد و با اشاره به انتخابات اکتبر، تأکید کرد که پیش از هرگونه عقب‌نشینی اسرائیل، حماس باید به‌طور کامل خلع سلاح شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/681999" target="_blank">📅 17:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681996">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999d8e8665.mp4?token=uE5W7NhoH8JuOoANWVP7K_u4Ou4Nupf5KLcBn2qsTKIzHxsa-mcg4ElzGmIWXivxWSiafBbALhyFPfbdBjFb3a6xA0eTKu2dz3eOsPxN0DnTNQEE9bbmaCPXYR-qASxq_EJCBE8C0XF4lD1vmzxU2UH5nlgYvaG1FCqNXy5Gw_GUIuZQVIyfiZIzDe7Lv64TqtAofQAQlpJ_M8AzPGTEXe8Z83tRIHVgMRBY-5KC-ArUpIbJnsR1MxSHvC8fZ-yz9Yb48k0SrM-DG1tjsBRoJUfdc399vAAWuBi59BRAAri0_zW34_IO3nZrzLACtwOlZG2R8ecdWi0yHj5oeG7c5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999d8e8665.mp4?token=uE5W7NhoH8JuOoANWVP7K_u4Ou4Nupf5KLcBn2qsTKIzHxsa-mcg4ElzGmIWXivxWSiafBbALhyFPfbdBjFb3a6xA0eTKu2dz3eOsPxN0DnTNQEE9bbmaCPXYR-qASxq_EJCBE8C0XF4lD1vmzxU2UH5nlgYvaG1FCqNXy5Gw_GUIuZQVIyfiZIzDe7Lv64TqtAofQAQlpJ_M8AzPGTEXe8Z83tRIHVgMRBY-5KC-ArUpIbJnsR1MxSHvC8fZ-yz9Yb48k0SrM-DG1tjsBRoJUfdc399vAAWuBi59BRAAri0_zW34_IO3nZrzLACtwOlZG2R8ecdWi0yHj5oeG7c5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وان‌یوآی ۹.۵ سامسونگ؛ انیمیشن‌های روان‌تر و قابلیت‌های جدید
🔹
اطلاعات فاش‌شده از One UI 9.5 نشان می‌دهد سامسونگ روی روان‌تر شدن انیمیشن‌ها، طراحی جدید حسگر اثر انگشت، تغییرات ظاهری دوربین و نوارهای جست‌وجوی جدید کار کرده است.
🔹
همچنین قابلیت میرور کردن اپلیکیشن‌های گوشی روی لپ‌تاپ ویندوزی نیز احتمالاً به این نسخه اضافه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/681996" target="_blank">📅 17:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681995">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Csi1xyF9mL8i2t_gMlqbzg-txGYjfJQb2FZ3I6t9i6IKfUsxJEi5AcqIr1vRlIqrAPKXsWoR9Etum_8PPrj1coO0x2qrUYNELtOmrRNDjhyoBzKkI4u8XLUPnKi41DxToC2f3f0nt5Snhhqq79sxvlgJtX0iAW8TOSmYvEo5AeBxzkpxouiKfi1Zc1-V7L9wlpEtvUJVRBN-rK6oXExekHT4q6bgwEmMi4Js-tlAPn1f6Yv2BnJnIg6E-TzbGy1Yxm2uaLlCx-_mY5YAN76I00eKgBO7un2kOhSHE_XvU7o2vHlAXwF73JYnX-OynWqn02ypKZm5_O-ySgc6C1ScXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار ۱۵۰ هزار اسرائیلی طی ۳ سال
🔸
بر اساس گزارش فایننشال تایمز، بیش از ۱۵۰ هزار اسرائیلی در ۳ سال گذشته اسرائیل را ترک کرده‌اند.
🔸
حدود ۱۰۰ هزار نفر در سال‌های ۲۰۲۳ و ۲۰۲۴ و حدود ۴۵ تا ۵۰ هزار نفر در سال ۲۰۲۵ مهاجرت کرده‌اند تا برای نخستین‌بار مهاجرت خالص اسرائیل منفی شود.
@amarfact</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/681995" target="_blank">📅 17:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681994">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
آمریکا برای جبران کاهش ذخایر تسلیحاتی، «تاماهاوک» سفارش داد
🔹
در بحبوحه تلاش واشنگتن برای جبران کاهش ذخایر تسلیحات دقیق خود پس از جنگ با ایران، نیروی دریایی آمریکا قراردادی ۲۲.۹ میلیارد دلاری برای افزایش تولید موشک‌های تاماهاوک امضا کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/681994" target="_blank">📅 17:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681993">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای ام‌اس‌نو: پاکستانی‌ها می‌گویند مذاکرات با هدف بازگشایی تنگه هرمز و پایان دادن به جنگ همچنان ادامه دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/681993" target="_blank">📅 17:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681992">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfc3d46d0.mp4?token=q94Vab6jZNiBUJAxoDeL1kc6wyMB_mshI8CwaiB24Kii-Y17SEFWly1j5ALFN_YtCNkbKDhGkkoaGgecETOIwpyqRcBIDwvy2FMwE1F2zoPDKhR85guogVsDRfZggvsTDBgeoQQU6FNLBH1304POO4QbSwHStT83-ySMIj7w2_egeNGhpACqBuKfYl71lokuUixi-61-rPTq-D-utIMprZlBp5USUHkr5rlZbVNpQJ2JzujVRGBqnc8AixShECy7P5dc2kZGqlyjuUh8puBI38EH9-ZxjG194Jp8WwD0kWP7HuxBmiXz-5MxSo-pnZso8yhn0RQ1miNkCL0ur989_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfc3d46d0.mp4?token=q94Vab6jZNiBUJAxoDeL1kc6wyMB_mshI8CwaiB24Kii-Y17SEFWly1j5ALFN_YtCNkbKDhGkkoaGgecETOIwpyqRcBIDwvy2FMwE1F2zoPDKhR85guogVsDRfZggvsTDBgeoQQU6FNLBH1304POO4QbSwHStT83-ySMIj7w2_egeNGhpACqBuKfYl71lokuUixi-61-rPTq-D-utIMprZlBp5USUHkr5rlZbVNpQJ2JzujVRGBqnc8AixShECy7P5dc2kZGqlyjuUh8puBI38EH9-ZxjG194Jp8WwD0kWP7HuxBmiXz-5MxSo-pnZso8yhn0RQ1miNkCL0ur989_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجرت هزاران غاز برفی؛ نقاشی زنده در آسمان
🪿
🔹
هزاران غاز برفی در آرایشی هماهنگ مهاجرت می‌کنند و آسمان را شبیه یک بازی عظیم وصل کردن نقطه‌ها می‌سازند؛ صحنه‌ای شگفت‌انگیز از طبیعت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/681992" target="_blank">📅 17:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681991">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یمن: هرگونه تشدید تنش از سوی رژیم سعودی با واکنش متقابل مواجه می‌شود
.
🔹
رئیس سازمان تعزیرات حکومتی از تشکیل قرارگاه فرماندهی نظارت و بازرسی بر بازار خبر داد.
🔹
ناوشکن آمریکایی «بنفولد» پس از نقص برق، ۴ روز در دریای چین جنوبی سرگردان ماند.
🔹
یکی از اعضای شورای شهر رضوانشهرِ گیلان به اتهام دریافت رشوه دستگیر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/681991" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681990">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
تمایل به تردد از مسیر ایرانی در تنگه هرمز بیشتر است
مارین ترافیک:
🔹
تردد دریایی در روزهای گذشته در دو نقطه بحرانی کلیدی به دو مسیر تقسیم شد.
🔹
عبور از تنگه هرمز ۱۹.۵ درصد کاهش یافت و به ۹۵ رسید در حالی که قبلاً ۱۱۸ بود، و تردد روزانه از اوج ۱۹ عبور در ۱۱ اوت به تنها سه عبور در ۱۶ اوت سقوط کرد.
🔹
از کل عبورها، ۵۱ عبور از مسیر ایران استفاده کردند و ۴۴ مورد مسیر نامشخص بودند؛ عبور از باب‌المندب ۶.۷ درصد افزایش یافت و به ۲۵۴ رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/681990" target="_blank">📅 17:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681988">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fac94c09.mp4?token=lIwnJa1Tc9y7jPZ0zWYJLrSEDMxrQWY7lD4SfR61sg3M0fiwQcjAYrT6uRg4kX29BXuA69IkPhKo6ZXUP3PZbKdklnmzBDUUR3arut2zczch78xCUBPL_dioo2J6AMqCzFpN7ma6fmoY_s9z4U_WMLQF29OQXJ625BuSHa_-tqb2dNoo6dIttlNR5vAvlLKCq1F2FXH75EeAlbjlo4xUsvl-4n1thLaBttB8ODYwpusBaRaWgxaqUCXKiGbmQXXq5mSv4M3JDPxp_Sdq9ZSWvq8qPpe7pTy1cpwT6gBcQFQVe8ezTRlyviW78kBwqnfqGFsMXsLEafV4KLKzrsDirQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fac94c09.mp4?token=lIwnJa1Tc9y7jPZ0zWYJLrSEDMxrQWY7lD4SfR61sg3M0fiwQcjAYrT6uRg4kX29BXuA69IkPhKo6ZXUP3PZbKdklnmzBDUUR3arut2zczch78xCUBPL_dioo2J6AMqCzFpN7ma6fmoY_s9z4U_WMLQF29OQXJ625BuSHa_-tqb2dNoo6dIttlNR5vAvlLKCq1F2FXH75EeAlbjlo4xUsvl-4n1thLaBttB8ODYwpusBaRaWgxaqUCXKiGbmQXXq5mSv4M3JDPxp_Sdq9ZSWvq8qPpe7pTy1cpwT6gBcQFQVe8ezTRlyviW78kBwqnfqGFsMXsLEafV4KLKzrsDirQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای سربازهای آمریکایی در آمده است
‌سرباز آمریکایی:
🔹
ما وارد جنگی شدیم که هیچ‌کس آنرا نمی‌خواست، جنگ با کشوری که تهدیدی برای ایالات متحده نداشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/681988" target="_blank">📅 17:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681987">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b10a7b718.mp4?token=YUcDmyMfATkk-wJvGhgmLlG1Vy0T24XMFmILvzLyrLca51ttMlSym8QdFUL-knFeaatfycKwIOgvQ4Mrv-BIH-Y1ygsKxwk0C18Bm7bej0qa59DMXtde7xeBn0_jksZ2h21DN5mDfnculvIN-yPifyfSkZymoaqGyv8-cXLX6EytGoW2OTHVaMRsZJKOHbr475E1Y3-Ui3qIvAUSVbWL2WZG9CKHzEvV4OVQc8RSR23KD31Q_aSiIwxoLrjp9YkilIDpSAvZ1Y-AjuJBG9Ia1bGCWILIot3-XAnQG2AozA0hJ8i7oEHN3mNZj3WblujJrnECXxmiPM0SFmkhw4CjGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b10a7b718.mp4?token=YUcDmyMfATkk-wJvGhgmLlG1Vy0T24XMFmILvzLyrLca51ttMlSym8QdFUL-knFeaatfycKwIOgvQ4Mrv-BIH-Y1ygsKxwk0C18Bm7bej0qa59DMXtde7xeBn0_jksZ2h21DN5mDfnculvIN-yPifyfSkZymoaqGyv8-cXLX6EytGoW2OTHVaMRsZJKOHbr475E1Y3-Ui3qIvAUSVbWL2WZG9CKHzEvV4OVQc8RSR23KD31Q_aSiIwxoLrjp9YkilIDpSAvZ1Y-AjuJBG9Ia1bGCWILIot3-XAnQG2AozA0hJ8i7oEHN3mNZj3WblujJrnECXxmiPM0SFmkhw4CjGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ترفند حتما به‌کارت میاد؛ برش دادن چسب‌های پهن بدون قیچی
✌️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/681987" target="_blank">📅 17:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681986">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
رویترز: تنگه هرمز قابل جایگزینی نیست
🔹
جایگزینی مسیر تنگه هرمز با خطوط لوله در کوتاه‌مدت بعید است؛ خط لوله پیشنهادی عراق از مسیر سوریه حداقل ۱۵ میلیارد دلار هزینه و حدود ۴ سال زمان نیاز دارد و سایر خطوط نیز با چالش‌های جدی مواجه‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/681986" target="_blank">📅 17:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681985">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
قیمت نفت افزایش یافت
سی‌ان‌ان:
🔹
برنت با ۰.۳۸ درصد افزایش به ۸۸.۸۵ دلار و نفت وست‌تگزاس اینترمدیت به ۸۲.۴۲ دلار در هر بشکه رسید؛ همزمان با پایان پنجره ۶۰ روزه مذاکرات بدون توافق پایدار.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/681985" target="_blank">📅 17:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681984">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سرگردانی ۴ روزه ناوشکن آمریکایی در دریای چین جنوبی
🔹
ناوشکن آمریکایی «بنفولد» به‌دلیل نقص سیستم برق، چهار روز بدون تهویه، آشپزخانه و سرویس بهداشتی ماند و توان حرکت مستقل خود را از دست داد؛ در نهایت با یدک‌کش به فیلیپین منتقل شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/681984" target="_blank">📅 16:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681983">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee7e5ed0fa.mp4?token=fO3sZA6URjgocisFwAssox7CqFvglIJnoeT16ml6t-OUvwm7GJyqvAycSKBxqCQRPAjjO2XIs0cyDz87BPqGO3vCgga0HT31Aa5_RK1_4DH620rwn5PluXgmYU_EasOdO9KLG4meJErImF7hAWJ2t2UccwRmq5EOd7nuroqk8Rrp0gaVYlxMwOeYpQQJGrm6mVlhLak4t0KlHRDnujNZnknkCZaRqv9lvGvGbQvYy5Kjhfg6KgYqlu8AWakQlfH4bIfoIhywbZAXOlQcYgCHL7hx-dvDNVH3NNxG-E4mUDANrARGm1A4yRlMVe3kkBVuwaqRxKlS8RUyXxs5sBmU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee7e5ed0fa.mp4?token=fO3sZA6URjgocisFwAssox7CqFvglIJnoeT16ml6t-OUvwm7GJyqvAycSKBxqCQRPAjjO2XIs0cyDz87BPqGO3vCgga0HT31Aa5_RK1_4DH620rwn5PluXgmYU_EasOdO9KLG4meJErImF7hAWJ2t2UccwRmq5EOd7nuroqk8Rrp0gaVYlxMwOeYpQQJGrm6mVlhLak4t0KlHRDnujNZnknkCZaRqv9lvGvGbQvYy5Kjhfg6KgYqlu8AWakQlfH4bIfoIhywbZAXOlQcYgCHL7hx-dvDNVH3NNxG-E4mUDANrARGm1A4yRlMVe3kkBVuwaqRxKlS8RUyXxs5sBmU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پل ورسک، مازندران
🇮🇷
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/681983" target="_blank">📅 16:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681982">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoJbQpDZjB-3RI08IZvEnNgS5U0SLqcotfNfCqJRoyh3FdsRQeAJje4SakpYfQdFnA4NvhpLcHHzDBN0a0m8XCgLV9QHVTSniVGZCH95Ot6wPJ8xLiTNUW4p2MNlckEnJxsjqEX_lVCvKycY0BDp5Xdpv4OCfM2nV9XCmFfhclnPwfce8LyyoVLgsib-s_TJ7mtluWTkZgXUOwnWL_JA6-cBS2ZEz0i_yapNZhaxTQdtSUfGlFDdoXWDUyDZaYxEWiGALHvycBA0CW0EB9MsUnLxG3tpfamAjsBIOVD5iJX2jkWvdry3TuQ2L4Bg3apXxuFstNZfL0aVgyJh3VDJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثه امنیتی برای یک کشتی در سواحل سومالی
🔹
سازمان عملیات دریایی انگلیس امروز از دریافت گزارش‌هایی درباره حادثه امنیتی برای یک کشتی فله‌بر در نزدیکی سواحل سومالی خبر داد.
🔹
این سازمان در بیانیه‌ای گفت که ۸ فرد مسلح وارد این کشتی در فاصله حدود ۷ کیلومتری بندر «ماریئو» در شرق سومالی شدند و کنترل آن را به دست گرفتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/681982" target="_blank">📅 16:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681981">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: ایران برای گسترش جنگ آماده می‌شود
🔹
ایران در دوره اخیر، ضمن افزایش تولید موشک و پهپاد، نیروهای سپاه را برای هماهنگی با گروه‌های همسو در یمن، عراق و لبنان اعزام کرده تا برای احتمال گسترش درگیری در منطقه آماده شوند.
🔹
این روزنامه همچنین از تقویت ساختار فرماندهی نظامی ایران و آمادگی تهران برای یک درگیری طولانی‌تر خبر داده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/681981" target="_blank">📅 16:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681980">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b64e1686.mp4?token=Rdeqx72AAMZvxYhKZTYgQkl8fBTCmLQppyvBstCDbZmMSyU1MmX3Z3XaWNbSBIhrDe2XyGIq2skL6MTDCE10TcNuPee-pGDSGKk32fQfrUrSQYfs1LVhIBsjsT16drqvUph3FORsQy-_bKiPoAhn1G4EqmW-ZoKFEBeMO_g8Vt-XU90IsoN4miOpEIprMYs3l32PDcQ0hAIeGvKOBUBwn9zKu8tI_rVqGcQjYhSeCC4V0VVhUg8vV47dgDJPwgn916bzjhW3n7LUFDFAUH-LSaiyaYo7elvMrNel5bqZI_eBhn8iMSMOZkpNEE71s3ntucd-0tX8VgMdx3cmJ-E-BIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b64e1686.mp4?token=Rdeqx72AAMZvxYhKZTYgQkl8fBTCmLQppyvBstCDbZmMSyU1MmX3Z3XaWNbSBIhrDe2XyGIq2skL6MTDCE10TcNuPee-pGDSGKk32fQfrUrSQYfs1LVhIBsjsT16drqvUph3FORsQy-_bKiPoAhn1G4EqmW-ZoKFEBeMO_g8Vt-XU90IsoN4miOpEIprMYs3l32PDcQ0hAIeGvKOBUBwn9zKu8tI_rVqGcQjYhSeCC4V0VVhUg8vV47dgDJPwgn916bzjhW3n7LUFDFAUH-LSaiyaYo7elvMrNel5bqZI_eBhn8iMSMOZkpNEE71s3ntucd-0tX8VgMdx3cmJ-E-BIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعویض پرچم های عزا به مناسبت اول ربیع در حرم حضرت زینب(س)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/681980" target="_blank">📅 16:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681978">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای ترامپ: ما مستقیما با مقامات سپاه در ایران صحبت می‌کنیم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/681978" target="_blank">📅 16:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681975">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d9bf50f4e.mp4?token=OFbwdI3gMrFiFz-Ioxbbb4DRlGN3wUs5nkoqeqnP49S26Z4Mje07LktQ2jKOkL0r6fcU6HoWMAS3tfNWAcCxLbrOCrEaxT-bHOWbcyKWt6XQwg7vgQ_cjbye7ogUwta3GDFQedVH0dRGc2ZVLJemA5ZgdnV7vWPjeX1AYb8zNYlEj-KG3h0pU3SNB0YayRr-MtigzYDD-ezJafvx3mnGrswGd-vVHG-G3nWrLcY56dYkZ3vxOD0v715RkflHQ4A1ulrDzLbnloSPxjUmu58m66cXUle0lcyjIr_cs4N7ZIGZyTFZsPhwfptGsc6tqvbrBLa4x0bBcOQFmeJ7ZjDzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d9bf50f4e.mp4?token=OFbwdI3gMrFiFz-Ioxbbb4DRlGN3wUs5nkoqeqnP49S26Z4Mje07LktQ2jKOkL0r6fcU6HoWMAS3tfNWAcCxLbrOCrEaxT-bHOWbcyKWt6XQwg7vgQ_cjbye7ogUwta3GDFQedVH0dRGc2ZVLJemA5ZgdnV7vWPjeX1AYb8zNYlEj-KG3h0pU3SNB0YayRr-MtigzYDD-ezJafvx3mnGrswGd-vVHG-G3nWrLcY56dYkZ3vxOD0v715RkflHQ4A1ulrDzLbnloSPxjUmu58m66cXUle0lcyjIr_cs4N7ZIGZyTFZsPhwfptGsc6tqvbrBLa4x0bBcOQFmeJ7ZjDzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفری فراتر از زمان؛ ایده‌ای جذاب سفر در تاریخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/681975" target="_blank">📅 16:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681971">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0633a32c.mp4?token=YZ4pGqqqv3zW3MdMF-X1Zi_52wWaD2C6ySEveIvVicSIV9_tLq8pkev95NXggpoR1a3L3DdnDuHhNgKpMKxtBJUFhlcF5Ir9YwAYXPDFJ3Wm8c9hj3HRzt3ezN0PQrv-R0yjzXjXX93RaiWRJD5ptIZMAvPgYKBiCtPUrOqPATpOjIt6bm8l3_tbOvNN-T9YFQG3ifJz-jUp3kAqLldR_j35-XecKe0CFoveFdf7qWiXEAE76V46txOtM_llUo8GmWfn0TRMyjKxhW1ZZ8CWtsyrG5clIlcvfDRgcbYefPG-7r_G1xb5QeRUYgZrEndYGQuNDupidElNsJqKsGKiqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0633a32c.mp4?token=YZ4pGqqqv3zW3MdMF-X1Zi_52wWaD2C6ySEveIvVicSIV9_tLq8pkev95NXggpoR1a3L3DdnDuHhNgKpMKxtBJUFhlcF5Ir9YwAYXPDFJ3Wm8c9hj3HRzt3ezN0PQrv-R0yjzXjXX93RaiWRJD5ptIZMAvPgYKBiCtPUrOqPATpOjIt6bm8l3_tbOvNN-T9YFQG3ifJz-jUp3kAqLldR_j35-XecKe0CFoveFdf7qWiXEAE76V46txOtM_llUo8GmWfn0TRMyjKxhW1ZZ8CWtsyrG5clIlcvfDRgcbYefPG-7r_G1xb5QeRUYgZrEndYGQuNDupidElNsJqKsGKiqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این چند عادت، ناخواسته‌ شما رو پولدارتر می‌کنه #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/681971" target="_blank">📅 16:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681970">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpO-U-yL0h_pZT2Cql_o2Y8Oui23hCQbgmeaM67LWfo8VNTHxKciDc71By0JWmBx--YjmY7zKRitkbp_qnWkF91bY2Rvpolk9ZeRy1vj4V6cN4ed24IsQrw3WsSxtpIHgXivjWVzgeHNOdN_rfkp6PdbxpjlYoVwxQMXRnptjT7CWAOae9c-obPBvW95vEP9X4UuvfH3G175xguAoRnYqJml4y0T4xjxtDmXE3JOQPgM43bZ9IroscbUty8cF5L_By_TKQdpVfa2j2coFfw2QQDtlYfdYMgrL2rGHqpNKyke3BAVYvoo7XbqpdYVQVqT1fmv17fcKzLj4Uj98g218A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر جنگ رمضان بر افزایش جهانی قیمت گازوئیل
🔹
پس از آغاز جنگ رمضان و بسته شدن تنگه هرمز، نگرانی از اختلال در عرضه نفت باعث جهش قیمت گازوئیل در بسیاری از کشورهای جهان شد.
🔹
بیشترین افزایش قیمت در کشورهای واردکننده سوخت علی‌الخصوص کشورهای جنوب شرق آسیا دیده شد.
🔹
این جهش قیمت، هزینه حمل‌ونقل و در نتیجه هزینه تولید و توزیع کالاها را افزایش می‌دهد و می‌تواند به موج جدیدی از تورم در اقتصادهای وابسته به واردات سوخت منجر شود.
@amarfact</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/681970" target="_blank">📅 15:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681968">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f238b08db4.mp4?token=Gyo8hFSfz-RJNlA7hSSkWiuCjYJpMTJwUg9X1xNTy1T6QG3V2y1Po4VyHhp3Y0Eb1dVu2W3ZPUQllDqN_kGgSoXC5qspaNCq7cdoLwA9GkWWpaBtaBvA_JG-_AmlCoQmvMmbNIyII3GSXCsyDce1hxM9GwILHYI2loxy4wueW-RX18hwfXxz376hVP-G5a8ZBcOmlnvkp-8AIH4SjkCE0L8nd_wCCXwWn1Hf3XZjr-pRrx4PDY42YPS1jBBTyVxIDi-Q666xvJgFHKyLyzMYSQppJtvPFj4DoOQVANbhe4o3pgJUfwoQqQBN6OROQvvFET1aMYN7gh8SFCUYyTtf1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f238b08db4.mp4?token=Gyo8hFSfz-RJNlA7hSSkWiuCjYJpMTJwUg9X1xNTy1T6QG3V2y1Po4VyHhp3Y0Eb1dVu2W3ZPUQllDqN_kGgSoXC5qspaNCq7cdoLwA9GkWWpaBtaBvA_JG-_AmlCoQmvMmbNIyII3GSXCsyDce1hxM9GwILHYI2loxy4wueW-RX18hwfXxz376hVP-G5a8ZBcOmlnvkp-8AIH4SjkCE0L8nd_wCCXwWn1Hf3XZjr-pRrx4PDY42YPS1jBBTyVxIDi-Q666xvJgFHKyLyzMYSQppJtvPFj4DoOQVANbhe4o3pgJUfwoQqQBN6OROQvvFET1aMYN7gh8SFCUYyTtf1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این روش پوست ماهی‌ها رو راحت‌تر بکن
🐟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/681968" target="_blank">📅 15:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681967">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای یک نماینده: مدیریت عبور کشتی‌ها از تنگه هرمز به ایران واگذار شد
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
در آخرین توافق با عمان قرار شد عبور و مرور کشتی‌ها از تنگه هرمز با مدیریت ایران انجام شود و عمان فقط نظاره‌گر باشد، همچنین قرار شده عبور کشتی‌ها از ضلع جنوبی تنگه انجام نشود و مسیر عبور را صرفاً ایران تعیین کند.
🔹
تصمیم‌گیری برای مبلغ دریافتی از کشتی‌ها به عنوان عوارض عبور از تنگه، درحال انجام است که مدیریت این طرح بر عهده ستاد کل نیروهای مسلح است و وزارتخانه‌هایی مانند وزارت خارجه نیز با ستاد کل همکاری خواهند کرد.
🔹
عمان نیز از این عوارض دریافتی، بهره می‌برد اما سهم ایران از عمان بیشتر خواهد بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/681967" target="_blank">📅 15:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681964">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079fc18e6e.mp4?token=DJseTqY0Mf9kg2lhAcAITMrKOgUC4v-7q1kxzkXA4e5cDf9Hrzx_jKmyTbsrPW5FZPV9ns-Qj5svgRPDR8KtzlqLMqhw7Wc0MXkz96zVnshs1SyTcFjcSL5x703NDLjYd0Mu67cnL0AZXYF4MKOCs8ZuhJS6j9FRnUgqgZKLTnQCqj-szxCj9OY7ohUCR3XKrLHaJ1cxQ9RmyXMP2TrRPNbYbs83LgQBHRuv3OTpsQr9BDuYErtWywmwYWZX8UdMR_QUzfu5QO3qwjkjmv-9H5fvzcBNLAldjc7QX8XfITT4LzLqA6f4zowIIdOAW77pCayDj6DKoYQGhjBy8a6CjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079fc18e6e.mp4?token=DJseTqY0Mf9kg2lhAcAITMrKOgUC4v-7q1kxzkXA4e5cDf9Hrzx_jKmyTbsrPW5FZPV9ns-Qj5svgRPDR8KtzlqLMqhw7Wc0MXkz96zVnshs1SyTcFjcSL5x703NDLjYd0Mu67cnL0AZXYF4MKOCs8ZuhJS6j9FRnUgqgZKLTnQCqj-szxCj9OY7ohUCR3XKrLHaJ1cxQ9RmyXMP2TrRPNbYbs83LgQBHRuv3OTpsQr9BDuYErtWywmwYWZX8UdMR_QUzfu5QO3qwjkjmv-9H5fvzcBNLAldjc7QX8XfITT4LzLqA6f4zowIIdOAW77pCayDj6DKoYQGhjBy8a6CjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران حسی عمیق، شبیه افتخار، شبیه دلتنگی، شبیه دوست داشتنِ وطنی که هر گوشه‌اش، بخشی از جان ماست
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/681964" target="_blank">📅 15:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681961">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
جزئیات طرح اسقاط موتور سیکلت‌ها و خودروهای فرسوده  مدیر ستاد نوسازی ناوگان و اسقاط خودرو فرسوده
🔹
تسهیلات این طرح از ۴۰۰ میلیون تا ۱.۲ میلیارد تومان با نرخ سود ۴ درصد به متقاضیان پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/681961" target="_blank">📅 15:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681960">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa44eb4ce9.mp4?token=FHVWm7f4_N6Bp0aof2C7EQsmxY7B6sPIzYgk8cS0gc5qXtRZljw_ZQWomkaw0JAJbSM2_5Lszjw1X72_rcN5OJHOtJy-rDaGqlWXVAxlee9p9IsUDYC4Bx1d6IQy2byj500s3OvZDLwLMFLnlxxFjiH4WbtSmZqfQGkKUKSK2rszx69hAQadScGNzCIKVptfECXOIJ0mWuZFE70JtEphrQIT82zoOG0hJrN4GJHhrk5BRYgqed9RuigYk2DWYAlXjtvrW2F1MjHzWipz4m5_ltB5vqDnudp8Cvfs7fcZY6lUfRWbX1-keu3ZiaCWjyu9glXNsPwD8KKu3Dy8NWQ7WXlEXgFotpTa0pBmPRAqdFqNTgzyw_lOidppSpItvxmlAlIB3t4wkKWPV5OswVNdTQ8-6WY4fw6TZZI4fUa7eunsL-oNGmZwlWeEHLuI65e5jrDOk9e84BLXRmTvpjwG4N1f02msH9tNk1eJJtkgDU34GeEKkiowOvST6Zt8lfS4qeQE003HNRRKXoLD4J-H61rqd1t4zF6g_8swWnIn8ScjMbn99c7eOQ00EmIZ7g4skvrTbo3mNdkYqC6XPSMEuoipI3Ky9VO0J1h-daIdMABHFGJTHbQ9EB-mPBatZahecu9WuJObu-rI-AQFeiVCAn_y1ZOZ2nIwFkda2d0aoFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa44eb4ce9.mp4?token=FHVWm7f4_N6Bp0aof2C7EQsmxY7B6sPIzYgk8cS0gc5qXtRZljw_ZQWomkaw0JAJbSM2_5Lszjw1X72_rcN5OJHOtJy-rDaGqlWXVAxlee9p9IsUDYC4Bx1d6IQy2byj500s3OvZDLwLMFLnlxxFjiH4WbtSmZqfQGkKUKSK2rszx69hAQadScGNzCIKVptfECXOIJ0mWuZFE70JtEphrQIT82zoOG0hJrN4GJHhrk5BRYgqed9RuigYk2DWYAlXjtvrW2F1MjHzWipz4m5_ltB5vqDnudp8Cvfs7fcZY6lUfRWbX1-keu3ZiaCWjyu9glXNsPwD8KKu3Dy8NWQ7WXlEXgFotpTa0pBmPRAqdFqNTgzyw_lOidppSpItvxmlAlIB3t4wkKWPV5OswVNdTQ8-6WY4fw6TZZI4fUa7eunsL-oNGmZwlWeEHLuI65e5jrDOk9e84BLXRmTvpjwG4N1f02msH9tNk1eJJtkgDU34GeEKkiowOvST6Zt8lfS4qeQE003HNRRKXoLD4J-H61rqd1t4zF6g_8swWnIn8ScjMbn99c7eOQ00EmIZ7g4skvrTbo3mNdkYqC6XPSMEuoipI3Ky9VO0J1h-daIdMABHFGJTHbQ9EB-mPBatZahecu9WuJObu-rI-AQFeiVCAn_y1ZOZ2nIwFkda2d0aoFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاید عده‌ای به‌خاطر بازار فیلترشکن بر تداوم فیلترینگ اصرار دارند
نخعی، نماینده مجلس:
🔹
بسیاری از مشکلات فرهنگی حاصل مسائلی است که پلتفرم‌هایی مثل اینستاگرام ایجاد کرده‌اند./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/681960" target="_blank">📅 15:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuD7qrWYbRiS2vSAHyGYSI1KfNZQd5whnrKOHkEJCDg5RzpS20Q-fXcACMbB2FWoDYdNlXYyNwLqZqnzKbykVZK8XKAvhSoBpDwBgEx2f27_Nrx0P053brJAH7ufXfbsDMru2azKoxuNc2w2220H7Ly_3cDrp4e6TSiCZB_Bx1OMAzMfBn9hLTvE_OHFS9VYfM8giKX2NaU7XmVxdOK-75hwa0O0HIyzYUzEWhzcQNHkHdmws1NsI5fe4qB8BDVye8ET5txkvf2T0K41lC_znO40ac2Wms6pjCYazVW9xV0Djf2bfKMXPcElIZeJew-dqsuV8iPSnDPuslRzq2M_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
خرید اعتباری آهن‌آلات با LC تا ۶ ماه
⚡️
مزایای خرید با LC از آهنگر:
* تأمین انواع آهن‌آلات موردنیاز پروژه
* امکان خرید اعتباری از طریق LC
* مناسب پروژه‌های ساختمانی، صنعتی و عمرانی
* تأمین از منابع معتبر بازار
* پشتیبانی از استعلام تا تأمین و تحویل بار
برای دریافت شرایط فروش LC، سقف اعتبار و استعلام قیمت وارد لینک زیر شوید و فرم را پر کنید.
🌐
ثبت درخواست</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/681958" target="_blank">📅 15:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681957">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a0d5787d.mp4?token=Aprie9L-kaam4iHXFUa43vFfIfD7ZQaIejBtaI1y479AYqDw-FvGpO0B_WkGZ4SVMnPgHmxDpYzFrTIvX_Ju0FR2ILxvfV9Un27zbFbTE2jaXgbapt8wCmHrlIGKbSDfVnxOYZVZnYZzd6JtQJWw2JgQmTq2V-9UN-UBpZKI_CHsDYEuSHcGaN3EiWNCalzCZ4iGe6OjEVvvblqSElr2vuErAKR73_6D4He_TMGV7Uk6JWCZrKgZSnYECFYqyKP9KMtOT7YLLhPt_lNrx3on26JRo9-RIrhrKPyda5o84aCjQNIDu1AktJwFvzgl2Q_yZe8rlKZQUJoTUX7tIUBXvk3PSEtCYSC1r0lg6XF5OJUpGHqB4tcwbkneCUmJLDlqRpi_P97T8jJOfJ9xWtMnZVz8fGikzYvCIO9geJsmQP4tJ8oucAlqMk9o3evhEziJvtA0u53N7sZKjcxiQStmKHglNmoHgxzrfR2u-fhN8_cKTY-cwy4myYpqqOuwSIc24gR95YHiR5bwzP9f--R1ArqQ9iBDg01O6d2dOgj_paNj_JtX4DwHYyVlMMSvP8AkxSayVdxavkmEQatdPXLKGqaSVhboR_jNE6VTfUqsjjPhab3NPDiyeot84bsTfuLJL0ByMNVQ67_YZRbZtp7ujdgeWGfDFfFfUblFIqgBz4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a0d5787d.mp4?token=Aprie9L-kaam4iHXFUa43vFfIfD7ZQaIejBtaI1y479AYqDw-FvGpO0B_WkGZ4SVMnPgHmxDpYzFrTIvX_Ju0FR2ILxvfV9Un27zbFbTE2jaXgbapt8wCmHrlIGKbSDfVnxOYZVZnYZzd6JtQJWw2JgQmTq2V-9UN-UBpZKI_CHsDYEuSHcGaN3EiWNCalzCZ4iGe6OjEVvvblqSElr2vuErAKR73_6D4He_TMGV7Uk6JWCZrKgZSnYECFYqyKP9KMtOT7YLLhPt_lNrx3on26JRo9-RIrhrKPyda5o84aCjQNIDu1AktJwFvzgl2Q_yZe8rlKZQUJoTUX7tIUBXvk3PSEtCYSC1r0lg6XF5OJUpGHqB4tcwbkneCUmJLDlqRpi_P97T8jJOfJ9xWtMnZVz8fGikzYvCIO9geJsmQP4tJ8oucAlqMk9o3evhEziJvtA0u53N7sZKjcxiQStmKHglNmoHgxzrfR2u-fhN8_cKTY-cwy4myYpqqOuwSIc24gR95YHiR5bwzP9f--R1ArqQ9iBDg01O6d2dOgj_paNj_JtX4DwHYyVlMMSvP8AkxSayVdxavkmEQatdPXLKGqaSVhboR_jNE6VTfUqsjjPhab3NPDiyeot84bsTfuLJL0ByMNVQ67_YZRbZtp7ujdgeWGfDFfFfUblFIqgBz4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی می‌گوییم یک نفر ADHD دارد به چه معناست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/681957" target="_blank">📅 15:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681956">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP5C1dBHwfEyyDMx-7VTmxciwpheH1pmTNvUbfyN8MoR3dOvrmfWdKpHiJQj1p1xLXqCOlnx3eaCB2BJcko9gDVVYewGWquIdMWfnuhhdflxdvC9QSApOBnYnjERicZF1MVCdrAVpPb9EGpAjLrXbAPnFrktkatgb01ULHiVhHmaUftKo7AcXpGYKJ77rbjfJ-gupqy6pbof-bUV7GsKMhbk4M2lTnFYuH7osN9o2u4rnfQSyJ3j88iVMs7yYdweF9qm7mUGeJ-JOn1QsDCC3Vd20s5wSuc6YR0_Q9cvXdFZ4i4LZnGoxiL16iZl7V9GbJD1NXHb6Kt3rWjTd6RNgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش ۵۵ درصدی ارزبری بازار تلفن همراه
🔸
قیمت موبایل در سال ۱۴۰۵ بین ۳۰ تا ۸۰ درصد افزایش یافته و ادامه وضعیت فعلی، اشتغال مستقیم ۲۰ هزار نفر را تهدید می‌کند.
🔸
ارزبری بازار موبایل از ۴ میلیارد دلار در سال ۱۴۰۰ به ۱.۸ میلیارد دلار در سال ۱۴۰۳ کاهش یافته است.
@amarfact</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/681956" target="_blank">📅 14:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681955">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9189453b.mp4?token=IuCqHIYZXIt5dXslSVHhZfZoaKJ887kcZkLE2a-6utahSlfC0KI9gu1u8AZKHJi-zdA6lhrObE4jby0B_ULnHWamC6Re1fWV_JYZxzf3ZQyCx9Et1NYxQsLpRe9GDLkOa886YTKkKMrk4V7WgCOxVDCVkatcC1zvZ753GpsDz5ZuFUs3rENfg76655yQiPpV_J8Q2kvv4wZMPTGn87Hhkg1N8oUtRLTjXHXFbKNJ26kNF61eTBfZeRg_uan_x_M6fwicYR-zGbiPtyXthKBsmSX9BMkGOByuCNyz-tNKT2uDGOCGrGZZyf37xg5vBtyd8t6HdDAxpx7aZGBJnQOVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9189453b.mp4?token=IuCqHIYZXIt5dXslSVHhZfZoaKJ887kcZkLE2a-6utahSlfC0KI9gu1u8AZKHJi-zdA6lhrObE4jby0B_ULnHWamC6Re1fWV_JYZxzf3ZQyCx9Et1NYxQsLpRe9GDLkOa886YTKkKMrk4V7WgCOxVDCVkatcC1zvZ753GpsDz5ZuFUs3rENfg76655yQiPpV_J8Q2kvv4wZMPTGn87Hhkg1N8oUtRLTjXHXFbKNJ26kNF61eTBfZeRg_uan_x_M6fwicYR-zGbiPtyXthKBsmSX9BMkGOByuCNyz-tNKT2uDGOCGrGZZyf37xg5vBtyd8t6HdDAxpx7aZGBJnQOVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ما مستقیما با مقامات سپاه در ایران صحبت می‌کنیم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/681955" target="_blank">📅 14:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681951">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8966be94.mp4?token=XmNWRVPwoNocZnbd-LnY4ZeCQP4DvZwFf5T-LTqb1duXQjggptpkD0g3H5XOH_wA6sM2-j2XKW4oXZ3C1Ro43tO8AbMURdeWQHTlyADkAoJmBPrl1DsHi2ANWyUkZrwnnsyCdTKUp7m4yaZ8LQ3Kil5XzmBMNxknzNu-n9dyE3T4nyf1egAYHZIdD1IxgA8ODHDXmB36ZBJiuFthVohLvsjC0lHfBlgmvo9wWqAWHN1IrEGD7clQTLwzpQ6wC6lPNu5VeLwC_gAGVsDMZTENZuWJqFZTF-JtkgzIYwiP4EaMOTNGtNWdyxjgirLbQfADdDySHJNtm4pFv5Y-8NEJOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8966be94.mp4?token=XmNWRVPwoNocZnbd-LnY4ZeCQP4DvZwFf5T-LTqb1duXQjggptpkD0g3H5XOH_wA6sM2-j2XKW4oXZ3C1Ro43tO8AbMURdeWQHTlyADkAoJmBPrl1DsHi2ANWyUkZrwnnsyCdTKUp7m4yaZ8LQ3Kil5XzmBMNxknzNu-n9dyE3T4nyf1egAYHZIdD1IxgA8ODHDXmB36ZBJiuFthVohLvsjC0lHfBlgmvo9wWqAWHN1IrEGD7clQTLwzpQ6wC6lPNu5VeLwC_gAGVsDMZTENZuWJqFZTF-JtkgzIYwiP4EaMOTNGtNWdyxjgirLbQfADdDySHJNtm4pFv5Y-8NEJOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هفت بخیه ساده، یک پاپیون دوست‌داشتنی؛ هنر گلدوزی در چند دقیقه
🎀
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/681951" target="_blank">📅 14:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681950">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
چند خزانه، یک واقعیت: انحصار خزانه در بازار آنلاین طلا تمام نشده است
🔹
بانک مرکزی سرانجام امکان استفاده از چند خزانه برای سکوهای آنلاین طلا را پذیرفته و بانک‌های ملت و سامان مجوز خزانه‌داری گرفته‌اند؛ صادرات و کارآفرین هم در صف‌اند.
🔹
اما مسئله اصلی هنوز حل نشده: سکوها فعلاً امکان استفاده عملی از این خزانه‌های جدید را ندارند.
🔹
یعنی روی کاغذ انحصار بانک کارگشایی شکسته شده، اما در عمل پلتفرم‌ها همچنان با همان ساختار قبلی کار می‌کنند.
🔹
گرفتن مجوز خزانه یک مرحله است؛ اتصال به سامانه ناظر، ایجاد زیرساخت فنی و امنیتی و فراهم شدن امکان قرارداد و انتقال واقعی طلا، حلقه‌های بعدی این زنجیره‌اند./ پیوست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/681950" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681949">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اگر عمان سر راه ما قرار بگیرد، آن‌ها را حسابی بمباران خواهیم کرد
#Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/681949" target="_blank">📅 14:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681947">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d621b4d8d1.mp4?token=jPspYxMjPzl67-gomILyO8njKTovF1zoh_X1bHanCZsSNJY1OEFWOWTuyDlovyPfCY92nLhsLF8W6WyTsgiRbvliS9l43nIBooPFYmyFB3DIn7KfYBgIHldz9etLWvzQ9o_cu9wT26Rj-bOUzXPSrhhASwJmyJYjhB9hCQAuIIgx9HUUD4vvKTACne8_l3-VhmN_4rrZpkaeaTXnugsG9MiG49qqaHUwG1q2Fd-19mGqJYPrWKcO_VF1zVAJTQ3J671Q_aZTKTP__7ONbakp6NNjb-ddsMpPrYy4m1_SEnCJkA6ufRjbd59XTHxc66rjdN6x0IYi7acJ02o_R6HFloWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d621b4d8d1.mp4?token=jPspYxMjPzl67-gomILyO8njKTovF1zoh_X1bHanCZsSNJY1OEFWOWTuyDlovyPfCY92nLhsLF8W6WyTsgiRbvliS9l43nIBooPFYmyFB3DIn7KfYBgIHldz9etLWvzQ9o_cu9wT26Rj-bOUzXPSrhhASwJmyJYjhB9hCQAuIIgx9HUUD4vvKTACne8_l3-VhmN_4rrZpkaeaTXnugsG9MiG49qqaHUwG1q2Fd-19mGqJYPrWKcO_VF1zVAJTQ3J671Q_aZTKTP__7ONbakp6NNjb-ddsMpPrYy4m1_SEnCJkA6ufRjbd59XTHxc66rjdN6x0IYi7acJ02o_R6HFloWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خشکسالی بی‌سابقه در هلند؛ راین به پایین‌ترین سطح تاریخی رسید
🔹
دبی رود راین در هلند به ۶۱۵ مترمکعب بر ثانیه رسیده؛ کمترین میزان ثبت‌شده در این کشور که منابع آب و حمل‌ونقل رودخانه‌ای را تحت تأثیر قرار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/681947" target="_blank">📅 14:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681945">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uClQ72cj9dAx8rOzIVOXcGQ3SzxfgphTyx_vVNvCPc0ITaSiiGZM5WUEMyIoclFhvUCRB8Lf6pAEA5AUTJj6gINW5Thk6k-0xo_sFr1OusT4dsY4qL_FN3U7sM6lFYadlyEDAjmLt6gPhf2jOpX9taCdhAoykuyTD6vavKFdB0EmHyzB3ZitTlsbXKrM8b2EXSKkRH77iQtt_7uvhYN4UOJjPSTq-UwlIFuEJgSGBDoLPCcC7iDn1ZihPeLU6cPxk0-GUi9sv6Z7_Y6l_3XRaoss1kPbDBSC0mSSWYDaQ97q37lAC5wskesgvnM9GIy7mROozafO00PCWYFPWipDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش توییتری بازیگر مشهور نسبت به سکوت در برابر نسل‌کشی غزه
لیام کانینگهام، بازیگر مطرح سریال "گیم آف ترونز":
🔹
اگر از خودت می‌پرسی چرا دنیا برای متوقف کردن نسل‌کشی در غزه کاری نمی‌کند، اما خودت تا الان در این باره حرفی نزده‌ای، بدان که سکوت تو را به‌منزله تأیید تلقی می‌کنند. فرقی نمی‌کند دو فالوور داشته باشی یا دو میلیون؛ حرفت را بزن، لعنتی! سکوت یعنی همدستی.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/681945" target="_blank">📅 14:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681943">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7399b39d67.mp4?token=NP-YToJkVMValSmliS1lSceHck3jDHNyXO_trNXKTESSX7BCyOkhpOml4vRx0rBcP2UGySZ4e0yyBjjmZz6nAoX7no-tYOEiJ5AacEiLd2-2PiyuzQk3lRPMZw_Gj-uy6Jj-wXQFeOzfzqHGctPZWsS6AU9-a70KtgikwPF_9-Juxz0h6-ucENVXvAD_9iUbkcYgEgCvUtgrbzt7tp509psV1g4J-EIscBc3AssORja_0RWiwXgyx6Vx8202lMgX5D37UP8WrT7omeTAQU8t6G_4PyCSztc2OCogpd2yjljP_ckHjW_C1VnwpM41dShuiSGxYp2cYNBIBP2pFyfDXgYAc2oh231J2VEFtTqG3dItMIPfnU0LnC5KW-mlRf9wyvBNYuoQrOIExHSl81ul-xuKTTBhlOWfIfjKxCGt81_jUYlexrqrJkijWz4s6Bwi0kpQ27ZJax94WVePrp1xNmXOd_IWc2gNXO2wimEqT6AC_KECQ_m4GU74pCqNWQ3bRei9vkH7jg5vrUdF3K3v8L1FpNUnDn8aIEc1xl8KGHzSdluWon3n72Ri2W-sMPgeqTl0TKUwlwFjG-e6p3uEQe3zxhFv6EB-z_6U53yAatAt9XQbx8LYVKqqLrUQRcULcMkb_2YNR_4kgXX7p4IEznW9jttSQ33msLeml1WpzgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7399b39d67.mp4?token=NP-YToJkVMValSmliS1lSceHck3jDHNyXO_trNXKTESSX7BCyOkhpOml4vRx0rBcP2UGySZ4e0yyBjjmZz6nAoX7no-tYOEiJ5AacEiLd2-2PiyuzQk3lRPMZw_Gj-uy6Jj-wXQFeOzfzqHGctPZWsS6AU9-a70KtgikwPF_9-Juxz0h6-ucENVXvAD_9iUbkcYgEgCvUtgrbzt7tp509psV1g4J-EIscBc3AssORja_0RWiwXgyx6Vx8202lMgX5D37UP8WrT7omeTAQU8t6G_4PyCSztc2OCogpd2yjljP_ckHjW_C1VnwpM41dShuiSGxYp2cYNBIBP2pFyfDXgYAc2oh231J2VEFtTqG3dItMIPfnU0LnC5KW-mlRf9wyvBNYuoQrOIExHSl81ul-xuKTTBhlOWfIfjKxCGt81_jUYlexrqrJkijWz4s6Bwi0kpQ27ZJax94WVePrp1xNmXOd_IWc2gNXO2wimEqT6AC_KECQ_m4GU74pCqNWQ3bRei9vkH7jg5vrUdF3K3v8L1FpNUnDn8aIEc1xl8KGHzSdluWon3n72Ri2W-sMPgeqTl0TKUwlwFjG-e6p3uEQe3zxhFv6EB-z_6U53yAatAt9XQbx8LYVKqqLrUQRcULcMkb_2YNR_4kgXX7p4IEznW9jttSQ33msLeml1WpzgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوکیا N93؛ یکی از گوشی‌های پیشرفته زمان خود
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/681943" target="_blank">📅 13:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681940">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f17673114.mp4?token=qiefUymhhDeifHw9GVj-gC-iuDBwSUNUE0ao662NoymezxFoNPB7FMyql6xK35gSPzipK7ZKXeTqgMt9MJlB3pI7FG_T7Bhl96IsGhyn4iYKZ7HMtbKrxGETNIqsxPffAMoskv59kGsvkowDqbd9SOU836_gKvuxnkY9MEEUgDn9ivUxOmYG91iibmmw1N0wXRyPkvrJRx2keuALKlTH4_YL7TYZO0ajhOz-W-vpEDPFYsb6p529m0mmoWkVaYsh2J00v3wJ2mqSt9wV24ezwWvuhnI12yeOqbnfAlOfW0eqgM46deqjBKSrKOXa0iqjBE02-iU1kP6OK94APO1SzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f17673114.mp4?token=qiefUymhhDeifHw9GVj-gC-iuDBwSUNUE0ao662NoymezxFoNPB7FMyql6xK35gSPzipK7ZKXeTqgMt9MJlB3pI7FG_T7Bhl96IsGhyn4iYKZ7HMtbKrxGETNIqsxPffAMoskv59kGsvkowDqbd9SOU836_gKvuxnkY9MEEUgDn9ivUxOmYG91iibmmw1N0wXRyPkvrJRx2keuALKlTH4_YL7TYZO0ajhOz-W-vpEDPFYsb6p529m0mmoWkVaYsh2J00v3wJ2mqSt9wV24ezwWvuhnI12yeOqbnfAlOfW0eqgM46deqjBKSrKOXa0iqjBE02-iU1kP6OK94APO1SzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن اولین عبادت یک دختر ایرانی؛ ویدیویی که در فضای مجازی پربازدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/681940" target="_blank">📅 13:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681939">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF9o7FaWC_98v7zRVnGoyvnOmPLUAER1Bou6Tpfd50PPUNpbsOra4_9AfYvJH9sJMOGZz_XKW4YKmiCK6MeC94aBQ7Fn09Gf9UnzDX8JACMbgp3TKzpJH2sW0YAqStkCib8Rdi7xvytyFS-CVOznHKXl8lvOda7SeWW0H5xWqQjoF6TYKYW76ybgZ--nUgcpb3bIzXcBLxEjOH_OuhfMNQF1qhUhNN4ZTl-KA_lOqhQ_IR9vGdUEvDkN3bQsrXb-tes3LvyLHSzGEFVJNMXc9ifrNAWrwDzIkA2-q10VSyv54m5QAElGz7-bTMr77fVsWHrLw_wQejVPz0zok7tpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکسی که یک ملوان آمریکایی از کشتی جورج واشنگتن به اشتراک گذاشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/681939" target="_blank">📅 13:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681937">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf402f74e.mp4?token=B016RPaOguSIKoULvcQwivYXo1EufZa8OVkGLNbqPVoX6tz9g-_v20H-VBHiq5vx97uCNIFlgLlkqvyDGEDq7f2RvMSaztdjGBofWjMNzrjXqZni6qVoJb4hkjpZ28rcbphMCqGRTUguFrhNrSRfPUcvV3B3eKp6Pum5kwG3iiipqx-U42sUJWIaZi1BH_iV5eYdDu43RbLX4FIB3Oaw52_uBb3yrwIswUPyI-WKje1no5xrgtiB0vjxuuKv_-vCS_R31meXxEW4PWs83xz55cMjSiOHQTdq7uty0BwOaZXJIafJ1ekEKxR-7wlQTH3FBZb3sDLyXFtqqYgYFXSvDYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf402f74e.mp4?token=B016RPaOguSIKoULvcQwivYXo1EufZa8OVkGLNbqPVoX6tz9g-_v20H-VBHiq5vx97uCNIFlgLlkqvyDGEDq7f2RvMSaztdjGBofWjMNzrjXqZni6qVoJb4hkjpZ28rcbphMCqGRTUguFrhNrSRfPUcvV3B3eKp6Pum5kwG3iiipqx-U42sUJWIaZi1BH_iV5eYdDu43RbLX4FIB3Oaw52_uBb3yrwIswUPyI-WKje1no5xrgtiB0vjxuuKv_-vCS_R31meXxEW4PWs83xz55cMjSiOHQTdq7uty0BwOaZXJIafJ1ekEKxR-7wlQTH3FBZb3sDLyXFtqqYgYFXSvDYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«چند روز مانده به کنکور؛ بخوانیم یا استراحت کنیم؟»
محبی، روانشناس:
🔹
راهِ درست در روزهای پایانی منتهی به کنکور، یک جمع‌بندیِ هوشمندانه است: حلِ یکی‌ دو آزمونِ جامع، مرورِ مطالبِ مسلط، و تمرکز بر مدیریتِ استرس، تمرکز، حافظه و تکنیکِ آزمون./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/681937" target="_blank">📅 13:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681936">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde605370a.mp4?token=HL7MK49qhmIR-1JpIVRam4jYWPSuFKATohiO6DKLf5uxPhegD03oACBnzbkUWswbZvc0u9lTAhA5opYG00x1rheU9oUofsGt-DB7QDRe4_wfgifsHBgXUcG8rvXLldXpMIhhWv-TXrqPMUDE93MRYo81DKehhxZxWw9d8v_9QMIGmdHMZvHsMej17ULFcsoAmeTVLe_3v-Miv8tkuRJ-JzOzR70au_ZDXkEYmepQuENuHqULl6EoqpPOuznbHdTtEYc9poSUxw2prTIvIkKnXAloROT8WBzF5dlCEA8DUzi_7ZFoxf8kAA9tD-7KThtjzlSU6uWinbkknA5HeAjzlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde605370a.mp4?token=HL7MK49qhmIR-1JpIVRam4jYWPSuFKATohiO6DKLf5uxPhegD03oACBnzbkUWswbZvc0u9lTAhA5opYG00x1rheU9oUofsGt-DB7QDRe4_wfgifsHBgXUcG8rvXLldXpMIhhWv-TXrqPMUDE93MRYo81DKehhxZxWw9d8v_9QMIGmdHMZvHsMej17ULFcsoAmeTVLe_3v-Miv8tkuRJ-JzOzR70au_ZDXkEYmepQuENuHqULl6EoqpPOuznbHdTtEYc9poSUxw2prTIvIkKnXAloROT8WBzF5dlCEA8DUzi_7ZFoxf8kAA9tD-7KThtjzlSU6uWinbkknA5HeAjzlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز ناتمام یک مسافر صهیونیست
🔹
یک شرکت هواپیمایی آمریکایی یک مسافر اسرائیلی را به دلیل اظهارات نامناسب درباره غزه از پرواز خود اخراج کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/681936" target="_blank">📅 13:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681935">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe61f8ddb.mp4?token=S5aFDMU8BLSJ1Wf1JWWOZcmCr6MBHVKpEDJssCOYF7EYOaD63bo_pJHQuOs8isW1GBC2ceK2fKns0CYTv2ZPkXJ13RXNZP_0UlFYVSd2am9JdkLUW7ppp5dOAAUjeAv3irTbtromOPif4f5-sbOsX-jpYyI30r_WJkjbx_r6SMmTuastqWJGHUz-uBz82ehLDbIseXWGls9fELQuTkk5keG8a58ensMkwCyDERMD3x-dIOKQGeqBSpC3Mpa-iisGmTFXPpM35x-pgxCfUAPMhyOn9_YgXTDos3hbFKzgSff_DEP9akTw1p8p_KxXoKi91iQ9L0FbqybRWA7xn46I6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe61f8ddb.mp4?token=S5aFDMU8BLSJ1Wf1JWWOZcmCr6MBHVKpEDJssCOYF7EYOaD63bo_pJHQuOs8isW1GBC2ceK2fKns0CYTv2ZPkXJ13RXNZP_0UlFYVSd2am9JdkLUW7ppp5dOAAUjeAv3irTbtromOPif4f5-sbOsX-jpYyI30r_WJkjbx_r6SMmTuastqWJGHUz-uBz82ehLDbIseXWGls9fELQuTkk5keG8a58ensMkwCyDERMD3x-dIOKQGeqBSpC3Mpa-iisGmTFXPpM35x-pgxCfUAPMhyOn9_YgXTDos3hbFKzgSff_DEP9akTw1p8p_KxXoKi91iQ9L0FbqybRWA7xn46I6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی پربازدید از تلاش یک خرگوش برای نجات دوستش
🐰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/681935" target="_blank">📅 13:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681933">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI9jx4yGPcsX_lUWKs0IyQiEtO22kv4g2mZvvH7910C7zbdb0ZpnCyVuut80cbHl27L7KpxgeI489W66hFZe95XfQKotLIQtCRuZFkTnppwmbiXh1t0_MZ7PpYeUcEqYjZafBjtZYyfjZNGrikKAVq82rmQDFwMTa2HueG0K8oq2Y_H4100Ug0A1HuwiEsGjO78h_o1YFmrh4X_-3fsci8_89ojLxDpPQuSWxMnWIGPGmjyJ3IGfmLkvbOzy55pdwGhihmqtDfUDARKF0LpBlYsR8LUQ2fd7khP82D7fXS_LDDOSxVD7Y8VE8gSMFktGS5Af4IOmpgAnoVOVYfELKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رئیس اقلیم کردستان عراق: دفترم هدف حمله پهپادی ایران قرار گرفت
🔹
مسرور بارزانی، رئیس دولت اقلیم کردستان، مدعی شد دفتر شخصی او در حملات پهپادی ایران هدف قرار گرفته است. مقر رئیس سازمان امنیت اقلیم کردستان نیز هدف این حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/681933" target="_blank">📅 13:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681931">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch8y43Nge8g36iVmrpOKCukFyLDAvnT2a3KaKZgJdeLjsx0StXQBobdTdD5iCHoOX0p5f8-64LhGf_m9hD1mbyLEllAV7i8S7_vg8g_S5P3_-ptJwnGYccKvpJysTanuxQk2LzGmg1dvBr5cC-0um_N8jKjebezPiRFs250mBV_24ecxxJorFnzCc72HDaVYMhlYGwTjgv7dU9mtDDyEIjfJl8vKiY-BAoIjaJ6x7fASEfqkhyL8rluev8P7rbWGh2-5tTPQ5S2Ew484zlPzh-BqFkhuI7exSlvPF37BE_xxZNaX3NtYo6pjmHSgLKnqf3z3iJheN7_slxAWFNJmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۶ مرداد ۱۴۰۵؛ ساعت ۱۲:۵۰
🔹
دلار امروز بدون تغییر روی ۱۸۶ هزار تومان ماند و پایان آتش‌بس ۶۰ روزه ایران و آمریکا هم واکنشی در بازار ایجاد نکرد.
🔹
تحلیلگران این بی‌تفاوتی را نتیجه آن می‌دانند که در دوران آتش‌بس نیز درگیری‌ها کاملاً متوقف نشده بود و عملاً آتش‌بس واقعی برقرار نبود؛ به همین دلیل پایان آن هم نتوانست نگاه معامله‌گران را تغییر دهد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/681931" target="_blank">📅 12:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681930">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af73a7afe.mp4?token=LqEMezyrOvC3RhaFW2NUxRt9Qj5B73MhYEbMpr7wO1lBLt-r4cjv7HKhkC77CfDBf1I8V9hbEnHBICYGCS_oTvqKeE2XpRDUrgyl4oWd1dvTnB5yU2aptGf0YYAv1V2C2Mgs0UwfrwiitDt5kILP_GwCMwIc3FJAujk_tllmVyXENchZXbg86p3JkgJn6pjQgnKdxRNtfE5AEYZx1GWRw-GVskc4JPsCcS-52b9xcXX9XMIfWBqTDjGisjr4NX5JhwnhaXiLKQtHQJWZjks7QNh3zmRY4GyE89K8obDWMU2YFI6k8aVfa4pN663uMnHTiqjPhu1up64aipc4zRZsvAMjmhpGOopMpHl5_-TretbEKEWMSgVCtyY0n4twvB_HwBlK8UWSAaSy0joC60IqCGOz3kCruWCAcFuDmBZpbREuj4RiveKD8Bmp-pQCkFZQxz6G8sWehMr22OqWh-AmgKq3ovqs3aQQUHlSApplmUWK02MJQdhr_IMkIpbIcOCLIOYd71GAcIemTwxrhEXUbM0AHnhTOw5ukMOXPPEEe3zIg_3tY8PlgrEGpH_rjvemanH-V5DVaQrl0V6988yw23oi6jdfmqzquR4u9seoEkB6MPNQFbjns9yB9rAK6ZjYkxRObdxJ0T4OMon3pH7P3PMprIRQN9Gnjub4pNGc0KU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af73a7afe.mp4?token=LqEMezyrOvC3RhaFW2NUxRt9Qj5B73MhYEbMpr7wO1lBLt-r4cjv7HKhkC77CfDBf1I8V9hbEnHBICYGCS_oTvqKeE2XpRDUrgyl4oWd1dvTnB5yU2aptGf0YYAv1V2C2Mgs0UwfrwiitDt5kILP_GwCMwIc3FJAujk_tllmVyXENchZXbg86p3JkgJn6pjQgnKdxRNtfE5AEYZx1GWRw-GVskc4JPsCcS-52b9xcXX9XMIfWBqTDjGisjr4NX5JhwnhaXiLKQtHQJWZjks7QNh3zmRY4GyE89K8obDWMU2YFI6k8aVfa4pN663uMnHTiqjPhu1up64aipc4zRZsvAMjmhpGOopMpHl5_-TretbEKEWMSgVCtyY0n4twvB_HwBlK8UWSAaSy0joC60IqCGOz3kCruWCAcFuDmBZpbREuj4RiveKD8Bmp-pQCkFZQxz6G8sWehMr22OqWh-AmgKq3ovqs3aQQUHlSApplmUWK02MJQdhr_IMkIpbIcOCLIOYd71GAcIemTwxrhEXUbM0AHnhTOw5ukMOXPPEEe3zIg_3tY8PlgrEGpH_rjvemanH-V5DVaQrl0V6988yw23oi6jdfmqzquR4u9seoEkB6MPNQFbjns9yB9rAK6ZjYkxRObdxJ0T4OMon3pH7P3PMprIRQN9Gnjub4pNGc0KU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستور پخت کنسرو خانگی آمیش‌ها؛ روشی از سال ۱۹۳۴ برای روزهای سخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/681930" target="_blank">📅 12:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681928">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeNjQv60XlKuEcEGIFwShpSe2WdiwsK1aFyORnNMTNFAXxxiAqhBGX2zqD5juEDznXf-eNN8Lu7fvGVy0-ADv6RXEFb5Jfv803zs5ssCoiarfPNKET8rdRLE1xnx4X-ykwsshpWY1b9bI4Meij1mRHM2sbGbLqBfjU5Pu3POOXKLfJcYItv4NqatK_zgvwBa29On28aU88WtjE7ZideNekyTdLuXsZ5zClu1ZE4ipPz08ohhHkM8vp02_wfv8by4BvbUQQF3K-11WxWa9SNLzFzXfkBAPFhf8Zux4PXhsvaAtU1ZNYHpCsrcw1OK3rv5OKfLulTAb7oopImmRnwEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراحل ثبت شکایت در خطاهای پزشکی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/681928" target="_blank">📅 12:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681927">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d313518a9.mp4?token=Yu3ig4MbO8YhrZ9rvdII6hm4If64LOhAPA_hLsaMOg8lJcXNhMISSJjXJzp56oaLN1_jW4Uhm5bZ_362BG_mkzCbEp2Zb_E3pN6A_T4io4J1rTVr1V3WQYorMrHZUhLYPKKg7JSGmXOfEEwbUIj2Aroe9cZeiEZXvEu_3v9vwmPT3GwWPQ9s5liXYPyXInuo-WyP8s-lXg_IUoSecCxWXqweSXqDriVHLkh6ssAwDZ49TRdkOPVDoZAfJM1RRe0w6fj5rShHT7N5vZesdRwq1vko-15omzxVd-w5Qp3ppP1ZMdtvQnB3GrVc3iOkgFSjZ9M3WEViVH3D_0ncMyVHlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d313518a9.mp4?token=Yu3ig4MbO8YhrZ9rvdII6hm4If64LOhAPA_hLsaMOg8lJcXNhMISSJjXJzp56oaLN1_jW4Uhm5bZ_362BG_mkzCbEp2Zb_E3pN6A_T4io4J1rTVr1V3WQYorMrHZUhLYPKKg7JSGmXOfEEwbUIj2Aroe9cZeiEZXvEu_3v9vwmPT3GwWPQ9s5liXYPyXInuo-WyP8s-lXg_IUoSecCxWXqweSXqDriVHLkh6ssAwDZ49TRdkOPVDoZAfJM1RRe0w6fj5rShHT7N5vZesdRwq1vko-15omzxVd-w5Qp3ppP1ZMdtvQnB3GrVc3iOkgFSjZ9M3WEViVH3D_0ncMyVHlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهین به ترامپ جنایتکار؛ مستقیم از فاکس‌نیوز
🔹
نماینده دموکرات ایالت ماساچوست و نظامی سابق تفنگداران دریایی آمریکا، در گفتگویی با فاکس‌نیوز حمله‌ای تند به ترامپ به دلیل عملکرد دولت او در جنگ با ایران داشت.
🔹
ترامپ فاکس را تماشا می‌کند، بنابراین اینجا مستقیماً به او می‌گویم: آقای ترامپ، تو تنها رئیس‌جمهور تاریخ آمریکا هستی که یک جنگ را خودت آغاز کردی و خودت هم باختی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/681927" target="_blank">📅 12:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681925">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6209fb52.mp4?token=MWA8YHy6LA2XQLroTjEzXaKOrXbzU0uausO0D2faLXhBl44IB34Loi6rlWilDamaniRjwuvRNIgXimdCuGWsTwOKKH8G-6ayGtpSTB8Rgw--fnIydSLrVlo6C9h30orB2IbETPg-JJkHDpK4rerH-5cz9Gbs29Clk6h8NeaGKg9Az_w4Sp1rzrHBnWscJavAZy2aZ_hPo1PPBTMXyJI7f6QIQV5Q0cWeT0TUMlKM8FjavsKh1QoBD2FSLG94AVamyY3u_OKl1XDPy8RN-GklY76pnQtd-ol0X6jkLVl5H_-RT-HwdEM9jlIL-imsri39OWILvV8ISA9TbT5Gne66PFS8aXc765SJ8rii6zG8QzgiNDE3mSvP4JM9Om0tApzwAtjQjIwSOpNmr9ME4_MKrekopE17z2z6U567coQj9rQ4jdx1dUCyYwse3oOhF2sLNL1XVHjYxaZ23JSQDKohkFsYU9Cj2QxvaxSQdJ6E_okW-PpAaGOI_9ZXicGbjR5mUedIhhaMfO96PVWQPvOuxGzuRQmru0PyJr007xMzdEbNVeRjfDZ9Dc4_v4Nnf-2LRVwZsljWsI2RVlYb4WAdAt-BOOR5rRWFiqQGR1_99C2h5S5lWhjB7uAAOQyw2eX3XBscbwq7i_bfDoCNWkV4dep-R0TD2TxgegU2QbYjPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6209fb52.mp4?token=MWA8YHy6LA2XQLroTjEzXaKOrXbzU0uausO0D2faLXhBl44IB34Loi6rlWilDamaniRjwuvRNIgXimdCuGWsTwOKKH8G-6ayGtpSTB8Rgw--fnIydSLrVlo6C9h30orB2IbETPg-JJkHDpK4rerH-5cz9Gbs29Clk6h8NeaGKg9Az_w4Sp1rzrHBnWscJavAZy2aZ_hPo1PPBTMXyJI7f6QIQV5Q0cWeT0TUMlKM8FjavsKh1QoBD2FSLG94AVamyY3u_OKl1XDPy8RN-GklY76pnQtd-ol0X6jkLVl5H_-RT-HwdEM9jlIL-imsri39OWILvV8ISA9TbT5Gne66PFS8aXc765SJ8rii6zG8QzgiNDE3mSvP4JM9Om0tApzwAtjQjIwSOpNmr9ME4_MKrekopE17z2z6U567coQj9rQ4jdx1dUCyYwse3oOhF2sLNL1XVHjYxaZ23JSQDKohkFsYU9Cj2QxvaxSQdJ6E_okW-PpAaGOI_9ZXicGbjR5mUedIhhaMfO96PVWQPvOuxGzuRQmru0PyJr007xMzdEbNVeRjfDZ9Dc4_v4Nnf-2LRVwZsljWsI2RVlYb4WAdAt-BOOR5rRWFiqQGR1_99C2h5S5lWhjB7uAAOQyw2eX3XBscbwq7i_bfDoCNWkV4dep-R0TD2TxgegU2QbYjPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکوردشکنی MSI؛ گران‌ترین کارت گرافیک RTX ۵۰۹۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/681925" target="_blank">📅 12:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681922">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa81ae3723.mp4?token=mHyjpxq2t0bh7MXjdR0gxUBv41Foy3mpglcRhScPedzNs40we4-AT-l_VGRcpju0m13P_cs5mw4QjructrbFft4kJEyvq8i2ouXD7vK6bT9Ro1LBDxFosvDmDsuDE0RIjC7RjharrnREUNQJaJnx_CzctzSoy_m3EGvOy-jSbpsP0bVx9iRf5_3xyPph4T6KTH2MCPmUd8jgw-Ro9JbyIyyIGi6jdqwBuTG-N1_UF3sCo-CtGwZvlSe0OOth9-sc8YpHiTLLsVfHAPBalebcq5r5P8WvElFrbT-s9wvlPOquFY7IS62gfWDqgAWAva-g_p2IzzAjcIjQ9f6zQgTdqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa81ae3723.mp4?token=mHyjpxq2t0bh7MXjdR0gxUBv41Foy3mpglcRhScPedzNs40we4-AT-l_VGRcpju0m13P_cs5mw4QjructrbFft4kJEyvq8i2ouXD7vK6bT9Ro1LBDxFosvDmDsuDE0RIjC7RjharrnREUNQJaJnx_CzctzSoy_m3EGvOy-jSbpsP0bVx9iRf5_3xyPph4T6KTH2MCPmUd8jgw-Ro9JbyIyyIGi6jdqwBuTG-N1_UF3sCo-CtGwZvlSe0OOth9-sc8YpHiTLLsVfHAPBalebcq5r5P8WvElFrbT-s9wvlPOquFY7IS62gfWDqgAWAva-g_p2IzzAjcIjQ9f6zQgTdqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیمه گمشده واقعا وجود داره؟  #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/681922" target="_blank">📅 12:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681921">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dm3sAKeXz7lYEUpouhRTSP9yHXgLcdrnAyEYhj4bZ-FiA6wI_9ApoFAPvr3bBLTgbynuQDlpwUtcMN5LoxgBa0Wux1rfNKfXlCNvDX8YnK_m1JfiRz9sjQVx5Ut93E8CW7bALjkCoVjieu29CYS1l7uS-N8RsSvNWH-VQCfr-a7SgSsDz5g4kDLqBKalxcbfowwv68p9NaS_CfeA_GyXvASouZgzN6lBA-Kfx2TpvjSRYHx6s__H82abbIa3F4YjyAM0AOVrGbPsbvQx4GcazShp7pVVqi2THeB6fcsJwY6iGC2JPGDrAaxgw3z-dOZWhx5E3X2fzrixh77N3pGmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏥
کلینیک ایران نوین قدیمی‌ترین و بزرگ‌ترین مرکز کاشت مو
کاشت مو (Nanograft) با ۵۰٪ تخفیف جشنواره تابستان
💰
قیمت نهایی: از ۳۷.۵ تا ۴۷.۵ میلیون تومان (متناسب با وسط طاسی)
شرایط پرداخت:
۱۲.۵ میلیون پیش‌پرداخت + ۵ قسط ۵ میلیونی (اقساط بدون سود)
⚠️
ظرفیت این جشنواره بسیار محدود است!
اینجا کلیک کن
👇
@clinic_irannovin</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/681921" target="_blank">📅 12:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681920">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867a2e48ac.mp4?token=CM7tEggiU09FAQdAOamejqFUlhshJGfbkAZWrChrgLZyvudu0m2sju5vJRo-hbB-MyBXVW6kBkaJNhf_iZRRO-WSrVZ1jqKKrYIn4QZUgZopebeI_UCyDvadbr6ETs1Lw4DLsHLMiZ9fPBGemXFdC0qGH19FxwXHw_hcu7OCmQ9iSzf9YAXy1NWjMcqpc6IItqAlJAhhslYS82nWeoGU9q7vgzgWMzvYFvBlLxDyTxKIaR4yFVPJ2g7JT5J91z6DI9zUyzwdVGa0dQNKnpnoBWQAKfjsdDG7jY9NwSrtZC_m0_txdNU4zifyrSH1BsJXFIc9advXB8W48UeayMU-Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867a2e48ac.mp4?token=CM7tEggiU09FAQdAOamejqFUlhshJGfbkAZWrChrgLZyvudu0m2sju5vJRo-hbB-MyBXVW6kBkaJNhf_iZRRO-WSrVZ1jqKKrYIn4QZUgZopebeI_UCyDvadbr6ETs1Lw4DLsHLMiZ9fPBGemXFdC0qGH19FxwXHw_hcu7OCmQ9iSzf9YAXy1NWjMcqpc6IItqAlJAhhslYS82nWeoGU9q7vgzgWMzvYFvBlLxDyTxKIaR4yFVPJ2g7JT5J91z6DI9zUyzwdVGa0dQNKnpnoBWQAKfjsdDG7jY9NwSrtZC_m0_txdNU4zifyrSH1BsJXFIc9advXB8W48UeayMU-Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شگفت‌انگیز پرواز کفشدوزک؛ تصویری جذاب از دنیای حشرات
🐞
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/681920" target="_blank">📅 11:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681916">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c373cc23.mp4?token=tfSN-NzzVUG3T4W_nXd4KOUU1aMGMPJi3mPAFhXUXdEf-0vh25O3TlIIHoSPCu3MdoXGJOkGQ5VhYzTou9xW80FlVTHN49pW-eX_FvDCG1KR6uM7VUBBKhQ6obH_VM1H9Hi92zanvvBRMxNiHMAefXZKuzJ193KaYxX0ElnPKoayn37xLfzgz1BmwnDDhPPkScCnEa2EuLD8yGyaXs01TgerZF-zjt8j1STHSGSuE7oTw2HiCBK3YNM38MyxJmOK0QB6yJNEQDm8qjrkDrr7vQ4ZT185FhsbzmiQMGr_U52K-NLUw3LsfOMPdmIEYOZNncSd5qBCbpD53a5jbitz1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c373cc23.mp4?token=tfSN-NzzVUG3T4W_nXd4KOUU1aMGMPJi3mPAFhXUXdEf-0vh25O3TlIIHoSPCu3MdoXGJOkGQ5VhYzTou9xW80FlVTHN49pW-eX_FvDCG1KR6uM7VUBBKhQ6obH_VM1H9Hi92zanvvBRMxNiHMAefXZKuzJ193KaYxX0ElnPKoayn37xLfzgz1BmwnDDhPPkScCnEa2EuLD8yGyaXs01TgerZF-zjt8j1STHSGSuE7oTw2HiCBK3YNM38MyxJmOK0QB6yJNEQDm8qjrkDrr7vQ4ZT185FhsbzmiQMGr_U52K-NLUw3LsfOMPdmIEYOZNncSd5qBCbpD53a5jbitz1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هزاران مهاجر مراکشی تنها دو هفته پس از هجوم گسترده قبلی، دوباره تلاش می‌کنند وارد منطقه سئوتا اسپانیا شوند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/681916" target="_blank">📅 11:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681911">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSm2uZanxW2Tg81W7UuJX7fReHcLR2ukPnw2NnD_zr6w_QlNNkulOc1hbrVAOBBM0qK6UpfyMOtemoeSUIJoujzDbB2DzNenRoOyKYodGNRbj6w-Ik1OnhIckcSdKXgz1GMDAn25MEh0UsUSxLmIzxmBqcvRW5tgbz6pelocUa8HKcPlQs45BgjC4lAyc_JxsAPQ3CZoN3YLYykZtNOdvLH9N99b7p9jlkf_kL1T4M20YwER_k5ExXQpkkTCzQnRltu3j5G0zngwXcF1IpbN15Nk2_lAAEUIQrvkznK3X6xbbi2dTK3EIAmcnP1EboSx35QxgR4O-6V_Ry5r2UhwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پارسیان ورق را برگرداند/ اعداد ۱۴۰۵ چه می‌گویند؟
🔹
آخرین صورت‌های مالی بانک پارسیان نشان می‌دهد در شرایطی که درآمد تسهیلات ۸۸ درصد، درآمد عملیاتی ۸۳ درصد و سود خالص بیش از ۳۷ برابر شده و همزمان سود ناخالص بانک نیز از زیان به سود رسیده و منابع سپرده‌ای، سود انباشته و حقوق مالکانه نیز افزایش یافته‌اند، یعنی شاهد تداوم تغییر مسیر در درآمدزایی و سودآوری بانک پارسیان در سال ۱۴۰۵ هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/681911" target="_blank">📅 11:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681910">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7044d99e17.mp4?token=DZezobq7BPCuFju1Qhowk7R7OeA3tkJYmJA5GqfOKfZdlyxJ-Fb8W3DYro0gk2MeqHsQLY1FBq9YkP9swNNwWy-Hr15aaot4_P9EDs92HlVDgHaZ7HKASrBoJbh-Jenr_UT_903QlOcL8KYndFT6VAju5wvgX1pcSBDo8CZpis-ZVTy4lBkVNrUC6FdOQsB3YnW2r8wn-27RfPf3rx5wyBmLan5ovl6kxqiGDOvIvfuVPURfinzRnHFcfSh5wpyMMIjwxpJhO-Zz2Zft_-lqeSC0TaVnGa_78FNPVPPMFnON4J0OtQq7TqCXfqMU041G-houyjd7blR-As81QiyoSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7044d99e17.mp4?token=DZezobq7BPCuFju1Qhowk7R7OeA3tkJYmJA5GqfOKfZdlyxJ-Fb8W3DYro0gk2MeqHsQLY1FBq9YkP9swNNwWy-Hr15aaot4_P9EDs92HlVDgHaZ7HKASrBoJbh-Jenr_UT_903QlOcL8KYndFT6VAju5wvgX1pcSBDo8CZpis-ZVTy4lBkVNrUC6FdOQsB3YnW2r8wn-27RfPf3rx5wyBmLan5ovl6kxqiGDOvIvfuVPURfinzRnHFcfSh5wpyMMIjwxpJhO-Zz2Zft_-lqeSC0TaVnGa_78FNPVPPMFnON4J0OtQq7TqCXfqMU041G-houyjd7blR-As81QiyoSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/681910" target="_blank">📅 11:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681905">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5ca0ffc7.mp4?token=jGlNiH3SMxgDQHg2Gml47rRxk-C4JSeOiD6K9AYjNHkxhJMHKc_fkotAVJoma81-UxMUYcA7zMY21Beb2PIEJXQVjjxismWBjfAVg5Cj3h_RkmUMpCOfAME2yovQwoN4ItA1Z6DSobOPl_4HGgTF8z3peS7-OWK3v2fHldaLJ504uzltaQ-hTv2kCNJPBE5bZ0W-0QcusJlXO88lEVSpZoKCXSUt_DNMG0UfJLNNsBgur_5ku7--Pyy4JiJ8Da0ibdPF5IyqaM6yx6mXrdxO_4cbD3gbSx8NFdNgM947aZSpPSPSWPOiOru3Ep2r6aTWw1P7Hd9YsBhkIvZXTp-o8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5ca0ffc7.mp4?token=jGlNiH3SMxgDQHg2Gml47rRxk-C4JSeOiD6K9AYjNHkxhJMHKc_fkotAVJoma81-UxMUYcA7zMY21Beb2PIEJXQVjjxismWBjfAVg5Cj3h_RkmUMpCOfAME2yovQwoN4ItA1Z6DSobOPl_4HGgTF8z3peS7-OWK3v2fHldaLJ504uzltaQ-hTv2kCNJPBE5bZ0W-0QcusJlXO88lEVSpZoKCXSUt_DNMG0UfJLNNsBgur_5ku7--Pyy4JiJ8Da0ibdPF5IyqaM6yx6mXrdxO_4cbD3gbSx8NFdNgM947aZSpPSPSWPOiOru3Ep2r6aTWw1P7Hd9YsBhkIvZXTp-o8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشکان خطیبی: نمی‌دانم تا سه ماه آینده بتوانم اجاره خانه‌ام را بپردازم یا نه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/681905" target="_blank">📅 11:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681902">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivSbWcdT-gTylUljp1xHcZloIy04RpxynxP6fPGjUB4_Z485zkYAgEaPNNwjUnx7jZHitnVjvbHa0NdHgHvGwK6qPoVvm1L0RyeJSq704QQQ7HMhMSMwPDJtF83bfMn-2se-sWcZxC8ppyTv0McnXBuWvP5XcZx4R_rfMA6Klu2aATZq_6y-E_GH1BKyB41xK7m1g2Tu1hkM_hq55qE9S34FDbO1i2RZc7eceWexh6ug-N-26Op3Xn8EyrrvwyxjY8udvRWYqmZveqkyvcXHkHpk6fqEvsX5gN2PItMZHt2pkmLv5K3TTroMoI0QmVe9cVn84jihzjSataIag7aAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/681902" target="_blank">📅 11:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681897">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b678ed152d.mp4?token=r1kS8fWZIN9eOUZebaaM1tgAFqdgH5TrEoxqVxYZdM3t1K-OYOHiwrhIhkTkouBRPRdB-6JVgI5_RLKBGRX2vgFNX0tVX6StvZPqd4CCBVHbbMt0SRyx4SXs0htU72Cxw-eTXSDI4j5XmAtii5yIdEWCSF9Xyd5OT3zEg_0Gfx5wr4glCrctrPvrIlyliVTIYIHS8Igv4OuTD0K2ptb1eK9TpsZnXMMkOlEAAs7RELNPqAXGlYHDizgKFozKhjCklqA4ByR6TvhT7MGnzGi7wyY5yx_d9UuIdJEDEQjqCyBWx6HyA5S0KGuPVxKCkNgpFO5aflFaY4XN4qpifvzUJTHib_GmbyS5-wLAEm-flmXoAei6PXGqoAxLqos7vepwwq4cicMU_ezRPaAR4ZalYKdvrLk2jQW3Pr_-dagvN3O7Ej0tyOAgy9-Y2XnmymhY-vmgejf14ETxGfnYEzg9TOwoaqpYJ4DbPl_gjIunEYiZXFq6dcvPuTsD7R1uYIaMtXKTz8nUE6NOtA9d9DSUlqhHTKJFdkzTrp-f2U3KY0WqZtZkAPUhgxo-wf-7ATVKNW3w3aoJ92ya323bgILUEAT02iz7IYzniL_vP1R2aB7egxVyy31l3l7KwhtnfJjAu9O7rMrZhtMfDwOBevZeWZfW0jY3BvNJDWOMNpj1yHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b678ed152d.mp4?token=r1kS8fWZIN9eOUZebaaM1tgAFqdgH5TrEoxqVxYZdM3t1K-OYOHiwrhIhkTkouBRPRdB-6JVgI5_RLKBGRX2vgFNX0tVX6StvZPqd4CCBVHbbMt0SRyx4SXs0htU72Cxw-eTXSDI4j5XmAtii5yIdEWCSF9Xyd5OT3zEg_0Gfx5wr4glCrctrPvrIlyliVTIYIHS8Igv4OuTD0K2ptb1eK9TpsZnXMMkOlEAAs7RELNPqAXGlYHDizgKFozKhjCklqA4ByR6TvhT7MGnzGi7wyY5yx_d9UuIdJEDEQjqCyBWx6HyA5S0KGuPVxKCkNgpFO5aflFaY4XN4qpifvzUJTHib_GmbyS5-wLAEm-flmXoAei6PXGqoAxLqos7vepwwq4cicMU_ezRPaAR4ZalYKdvrLk2jQW3Pr_-dagvN3O7Ej0tyOAgy9-Y2XnmymhY-vmgejf14ETxGfnYEzg9TOwoaqpYJ4DbPl_gjIunEYiZXFq6dcvPuTsD7R1uYIaMtXKTz8nUE6NOtA9d9DSUlqhHTKJFdkzTrp-f2U3KY0WqZtZkAPUhgxo-wf-7ATVKNW3w3aoJ92ya323bgILUEAT02iz7IYzniL_vP1R2aB7egxVyy31l3l7KwhtnfJjAu9O7rMrZhtMfDwOBevZeWZfW0jY3BvNJDWOMNpj1yHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: ایران وجود هرگونه مهلت ۶۰ روزه در تفاهم‌نامه را رد ‌می‌کند
/
نقض فاحش تفاهم‌نامه از سوی آمریکا گفتگوها را متوقف کرد
🔹
ایران حقوق حاکمیتی خود در خلیج‌فارس را با جدیت پیگیری می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/681897" target="_blank">📅 11:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681895">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d904e99ae.mp4?token=CDX9bRWIpT2ky5j4CqkDh0bZgaW5n8XPoV3Co9UimslTP4Fo5Jso_LP_RKz2EOgPV0OQ-5YNnmMjjumi8BpKyPAyzI6i14iiIYViXaMyJsa0uIEhjSR48gfRbJmQOr-Kxg9O5SS5seYOX5OqEeH_4YAX1dqptD09wjBOwWsk7lSbbKDH0_omABmZfbTLWLnReb_qmE81GxrpfBI_McEWf4jnCBKVFVxhwN2suxh8zJnxcVU1-7k8dlIpfJxaHUrlEiyjMRIMfWshpqjrSv8Ph9iKmk186-yKyirU7M7Wo-hwgGw_OTTuqYY9l1Ii9iCdS1k0FKO1-Mdk5I5hw214lrivy8RFuZBQ_QeoFgqkYxBEvzX-RCNVvR1F_-rK2XNi_mJuNCjI51eWUfQdOJhGyNfTnNxIanBfT_mekmzos10pGplfBHzDWqA9xQE9Y_IEwVKrDxgFUbjt5K9J9ExZ6o1SU1czX7R7Wm8uahIwOUTYks_c85fgQB4JETxsP0d4WR7oSIbQD8LGtJSCYT3dlrp_FVMzqAvSkt9HqdVttpw3x1Yyo8KDKmAJbllTBlGuM2kFrtgPj3f9AslK1T1UCKGAeG0fGdEwjpzGShqRS8s6GkZktKThwaGjdtqBC3KF5JIgvqumrUcaKti4zczdR5gX9fVCCRJPpAfwJz9iJ5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d904e99ae.mp4?token=CDX9bRWIpT2ky5j4CqkDh0bZgaW5n8XPoV3Co9UimslTP4Fo5Jso_LP_RKz2EOgPV0OQ-5YNnmMjjumi8BpKyPAyzI6i14iiIYViXaMyJsa0uIEhjSR48gfRbJmQOr-Kxg9O5SS5seYOX5OqEeH_4YAX1dqptD09wjBOwWsk7lSbbKDH0_omABmZfbTLWLnReb_qmE81GxrpfBI_McEWf4jnCBKVFVxhwN2suxh8zJnxcVU1-7k8dlIpfJxaHUrlEiyjMRIMfWshpqjrSv8Ph9iKmk186-yKyirU7M7Wo-hwgGw_OTTuqYY9l1Ii9iCdS1k0FKO1-Mdk5I5hw214lrivy8RFuZBQ_QeoFgqkYxBEvzX-RCNVvR1F_-rK2XNi_mJuNCjI51eWUfQdOJhGyNfTnNxIanBfT_mekmzos10pGplfBHzDWqA9xQE9Y_IEwVKrDxgFUbjt5K9J9ExZ6o1SU1czX7R7Wm8uahIwOUTYks_c85fgQB4JETxsP0d4WR7oSIbQD8LGtJSCYT3dlrp_FVMzqAvSkt9HqdVttpw3x1Yyo8KDKmAJbllTBlGuM2kFrtgPj3f9AslK1T1UCKGAeG0fGdEwjpzGShqRS8s6GkZktKThwaGjdtqBC3KF5JIgvqumrUcaKti4zczdR5gX9fVCCRJPpAfwJz9iJ5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: ایران وضعیت خلبانان ارتش را از مجاری دیپلماتیک پیگیری می‌کند
سخنگوی وزارت امور خارجه:
🔹
از روز اول که مطلع وضعیت خلبانان شدیم پیگیر آنها هستیم. ۲۵ اسفند اولین مکاتبه با صلیب سرخ در خصوص پیگیری خلبانان را انجام دادیم
🔹
مطالبه روشن کردن وضعیت خلبانان ایرانی بسیار جدی است. مادامی که وضعیت سه خلبان ما روشن نشده، به معنای این است که به اسارت درآمده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/681895" target="_blank">📅 11:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681894">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVaxDGG-OG4NA17uUWBJSmzkkLuDQu1TC3053Hjqi8PqIHJxFROFl2-pe3qMfv7i7p7BLNOlD_6wX18W2xHINS9hpZHXDhuIQQZS9qW61cQHVtpJAbBUVwNBw8wjHNDYangzkdv5iaM8lYOWmDUcwDGio2OBKkPBcTjGSwKZkdO7xgDfgJdXQ1lu_xZmfnkSt0yhH9Rftw9SPw3XBHLGLU1vErdffFuWLyZG1JMzwaMGnqC0okH2MD4C2ZKeTF2AZ3gAnySc0_dxl02aQQ80ucWtdA4fJM75CUDeHfv2wbH-mE-i-e7RoUGxRG2DLDIwOlsBgzYnGFVlMT3yTAUHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩺
سلامتی رو به شانس نسپارید!
فشار خون بالا معمولاً هیچ علامتی ندارد، اما می‌تواند خطرات جدی برای سلامتی ایجاد کند. با یک دستگاه فشارسنج خانگی، هر زمان که بخواهید در کمتر از چند دقیقه فشار خونتان را اندازه‌گیری کنید.
✅
اندازه‌گیری سریع و دقیق
✅
قابلیت تشخیص آریتمی
✅
تشخیص فشار دیاستولیک / سیستولیک
✅
حافظه ذخیره نتایج : بله
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
💰
قیمت قبلی: 1,698,000 تومان
🔥
قیمت ویژه: 1,398,000 تومان
📦
همین حالا سفارش دهید و با خیال راحت سلامت خود و عزیزانتان را زیر نظر داشته باشید.
https://memarket24.ir/product/fast/37832/180124/</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/681894" target="_blank">📅 11:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681893">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
تصاویری از بقایای جنگنده اف۱۵ و پهپادهای منهدم شده آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/681893" target="_blank">📅 10:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681890">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbS3lri4guEmNg8Ki7BFvWreUtGryf8cHnHNc_85VIoO7eSdGenaMsg5VahaLFu__CQdwMJh50o7vmlPZdPHy8iWATTz04kca20LS9jDwkblHv2zR8_tQGUg5PEm-Ix7ECCmdemuNNEK9axGAp_JpX9pSaNPckH1qBbS4muvDTi6zXreKo-Dh0GzdSY4-kNjWBqU11a3DhY8_42B8d96zcraTte25qAFqeJSZU3Mu_oT6420fOqKbkt0a1rbsR8LSO565NzPQldBcwrCk1hOyyqoaxWbUtHGszzDwQXJA7n-HikVKqVJeT3bVno9YEAIe0IRRqOPtCONgN2yX8EDbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا و رژیم صهیونیستی در جنگ شناختی، به دنبال ایجاد «ناامیدی» و «درماندگی» با تزریق اخبار منفی، بزرگ‌نمایی مشکلات و القای این حس که «هیچ راه حلی وجود ندارد» هستند. در برابر این ماجرا دو راهکار فوق گره‌گشاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/681890" target="_blank">📅 10:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681885">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b679be5bc.mp4?token=m0V1vClKjWYr8D5t4-_CSuwJ6zXzB08YlvfsEqqsTLeyzBBRK5P4QaHWsKOK1fPm9O3rjk2nrqrduxcT_4gGTdElXjt1ArmjGjjBuqyvN4Gww2KzGNPkOG4JWxd-fWdpmvEmhS6CJQx_FZ-HBMuXlOpqmKXOhqjzZo8Iz6LNdcFMVn4Cq_pAQKlu706wUI7OWSXCBlYNxUMivfXHVL6jZW1q4SCJqGL_WIYATmCqpgS--uZTIpj_WpPubDBFuApARTRPaouly05oapISs4LlEBWVsJc83FzDvDeHI6jUWCfvbdJ5atXUdLHiBNHcCszpf0UO5K5my6_8tNOowQQBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b679be5bc.mp4?token=m0V1vClKjWYr8D5t4-_CSuwJ6zXzB08YlvfsEqqsTLeyzBBRK5P4QaHWsKOK1fPm9O3rjk2nrqrduxcT_4gGTdElXjt1ArmjGjjBuqyvN4Gww2KzGNPkOG4JWxd-fWdpmvEmhS6CJQx_FZ-HBMuXlOpqmKXOhqjzZo8Iz6LNdcFMVn4Cq_pAQKlu706wUI7OWSXCBlYNxUMivfXHVL6jZW1q4SCJqGL_WIYATmCqpgS--uZTIpj_WpPubDBFuApARTRPaouly05oapISs4LlEBWVsJc83FzDvDeHI6jUWCfvbdJ5atXUdLHiBNHcCszpf0UO5K5my6_8tNOowQQBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من چطوری می‌تونم پرچم وطنم رو پاره کنم؟!
🔹
۲۶ مرداد، سالروز درگذشت عزت‌الله انتظامی. او از حاجی واشنگتن و سکانسی می‌گوید که باید به پرچم ایران بی‌حرمتی می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/681885" target="_blank">📅 10:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681882">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73abdba8be.mp4?token=Cuu-LDL9UA-B91VSXAGwAuHME76qGgK2Q6p39ZiG3Y1G1s3nEGL_McO7Mo3V6zIj3fl1ShjcvbepfWgRz39e6Yw7NqifxhSjb3lNIdsL6Mn0LDQ90ajg2-7ajwiCXen2qUyS05rFRal1R2xNSxswG9LCo-bI4ftfJUH5EZhyHyJhL_vObruYqdKY6lgAIxWjqObT-50IF3lvcGKYqkEtNYeIOooiWT3WlnsnEv-oFCtRo_B685KV2DAfDwaqXc5lfHOGIWed4lW_Xe4eg6g63ZIwiadPTX6s90fJam5Dn7OJlmav46JfIsgo4h65RTPOciPX9PoOBoHGUr1eAVrdSKj8fMYntcdTXABPDmCslcFCpqU-7ri55EDSOXZsn4Av8O1atmDqzZpx4Pzzf9zqHpsKa4BgNnYop-9jtzgtEMQ4HNyHAFdG_Qb-JbgChL93X4wjE2Zjy-CFXVzOsewMDjCue5ilpMrr_dnFMbLA5_O3QQRm8NtQQfgsQsAwl-PV7Pp11Ox1zOhYW9Oix-_S91OUxyR_L6wu88c1QlycieSRtKh332wIfwFYME8xvRjQsuciiBK1FH7uuTAzJoDoWOzzB-ayUbB9Q2UtAKiIkk1KQIAKY-4sXiFjt5kI2P4BofbMxkvJl6mFYb1UBKPh6HJ3_wn8ZSYbXtSPsm8GZaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73abdba8be.mp4?token=Cuu-LDL9UA-B91VSXAGwAuHME76qGgK2Q6p39ZiG3Y1G1s3nEGL_McO7Mo3V6zIj3fl1ShjcvbepfWgRz39e6Yw7NqifxhSjb3lNIdsL6Mn0LDQ90ajg2-7ajwiCXen2qUyS05rFRal1R2xNSxswG9LCo-bI4ftfJUH5EZhyHyJhL_vObruYqdKY6lgAIxWjqObT-50IF3lvcGKYqkEtNYeIOooiWT3WlnsnEv-oFCtRo_B685KV2DAfDwaqXc5lfHOGIWed4lW_Xe4eg6g63ZIwiadPTX6s90fJam5Dn7OJlmav46JfIsgo4h65RTPOciPX9PoOBoHGUr1eAVrdSKj8fMYntcdTXABPDmCslcFCpqU-7ri55EDSOXZsn4Av8O1atmDqzZpx4Pzzf9zqHpsKa4BgNnYop-9jtzgtEMQ4HNyHAFdG_Qb-JbgChL93X4wjE2Zjy-CFXVzOsewMDjCue5ilpMrr_dnFMbLA5_O3QQRm8NtQQfgsQsAwl-PV7Pp11Ox1zOhYW9Oix-_S91OUxyR_L6wu88c1QlycieSRtKh332wIfwFYME8xvRjQsuciiBK1FH7uuTAzJoDoWOzzB-ayUbB9Q2UtAKiIkk1KQIAKY-4sXiFjt5kI2P4BofbMxkvJl6mFYb1UBKPh6HJ3_wn8ZSYbXtSPsm8GZaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا فصلش تموم نشده حتما این دسر لایه‌ای‌ انبه رو درست کنید که خیلی خوشمزست
🥭
مواد لازم:
🔹
انبه دو عدد
🔹
خامه صبحانه: ۳۰۰ گرم (یک پاکت و نصف)
🔹
پنیر ۱۵۰ گرم
🔹
بیسکوییت پتی بور دو بسته
🔹
پودر قند ۶ قاشق غذا خوری #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/681882" target="_blank">📅 10:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681876">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a70be46871.mp4?token=hXYG9Zoh9YdTq38OPR1heBHr-uBpVECoO30WBXo7gYrOA_4v1i6giQo5PTHzpPHlsVx3-JW3V55entitc1ySAJ3WaVCXADsQv3_2zA45clXqBFFN935ZRQmVb-Xwzic6PWLVKbuA7RRb04mw-AWp7f0EZI6HY8PzcgLiu7t_3VplKERAstzMZwK6cobcOekzlC-mLPoyV9f-ELaIM9yA169lFV-k3tqfbjCdlv-6J5hdGSlDKMDXgTm763wvc24IsSmyEJXprHrJhw-16BOLYMVqrIek5tSxRtu4uW_Tj7Wn_Ovm4eg56W-7Ko3FikoM1MJP-DLN1yrtj8ZlyP-ZTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a70be46871.mp4?token=hXYG9Zoh9YdTq38OPR1heBHr-uBpVECoO30WBXo7gYrOA_4v1i6giQo5PTHzpPHlsVx3-JW3V55entitc1ySAJ3WaVCXADsQv3_2zA45clXqBFFN935ZRQmVb-Xwzic6PWLVKbuA7RRb04mw-AWp7f0EZI6HY8PzcgLiu7t_3VplKERAstzMZwK6cobcOekzlC-mLPoyV9f-ELaIM9yA169lFV-k3tqfbjCdlv-6J5hdGSlDKMDXgTm763wvc24IsSmyEJXprHrJhw-16BOLYMVqrIek5tSxRtu4uW_Tj7Wn_Ovm4eg56W-7Ko3FikoM1MJP-DLN1yrtj8ZlyP-ZTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از ۶ متهم پروندۀ قتل حمیدرضا رجب‌زاده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/681876" target="_blank">📅 09:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681872">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcaYcH-7AjisJUHn6mLTVupuFO7taZLDoQmwlJH0t0ilON6zBHtroxnH7UR9IZSLSDC__L3U86amtq8PVRRh-w8Aoio9TsCDlWGXpXibmvUH8anXE43lbzvxKDiUtWPh1fQRDGXL2UWSuXVw8lVmqnwsEqIpgKblvSV3rbQA0qRgzgm4mZW2I4GxsgSGDKTBiMWC4N-3vXlnN2oLaYYrp4J6WsZu9Ogot-xPkfUIJWn39j7Go38TsyAkOgqLizkHJhvnyMfJQkrmBbP8XKPjOgUKGFWIGxbzk9DFB5D2K-_lZwkS5bC59iEOl-uCXNvcvUVQH4UBmKvvnegzuTkF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دریافت کارت ورود به جلسه کنکور از امروز / چگونه کارت آزمون دریافت کنیم؟
🔹
توزیع کارت ورود به جلسه کنکور ۱۴۰۵ از امروز آغاز شده و تا چهارشنبه ۲۸ مرداد ادامه دارد.
🔹
داوطلبان باید مشخصات فردی و آدرس حوزه امتحانی را روی کارت بررسی کنند، مسیر حوزه را از…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/681872" target="_blank">📅 09:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681871">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH37QUxeXoCk5V4iFGjiXkS9VnxeYgAjswyBpZYsQA4VB95APxQPPFYvkpUs0A5CWnRnb9K4Wxyv0HYak4r1m976bbkBT2s26tfAqC1TH_I_JvhesPgivMvEbstXnivRxFyfxmCx_jgBY3G2ijIK4Zg2sd3hPbnvVD3CzFAW8XgNwL9z-RO5roLlJ1XvNGeXSG1gvzeJ-b5SuWp0d-z13JM29o0633I1ioIs2j-tc-aPb7UY6acx1a8Bu28l4Cv-FDGEfL3DqJUzBC8T5cGl2oo0TsD6_gMG3pJLkixtNDDQgsJyGX7apPoXvYVpnCGNtgPSoIobnLLqmomZL7183g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم ملی المپیاد جغرافیای ایران اول جهان شد
🔹
برای نخستین بار در رقابت‌های جهانی؛ تیم ملی المپیاد جغرافیای ایران در بخش Poster جایگاه اول را کسب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/681871" target="_blank">📅 09:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681869">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
شمارش معکوس برای پایان آتش‌بس ایران و آمریکا/ جنگ به «جنگ اقتصادی» تبدیل شد
نیویورک تایمز به نقل از منابع آگاه:
🔹
مهلت ۶۰ روزه توافق اسلام‌آباد بدون نتیجه پایان یافت و جنگ وارد مرحله فرسایشی اقتصادی شده است.
🔹
واشنگتن خواستار بازگشایی هرمز است و ایران آزادسازی دارایی‌هایش را شرط آن می‌داند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/681869" target="_blank">📅 08:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681868">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9a854ccb.mp4?token=Exf2etM0ZJnP9gZP-2Xq_1qVjy7CVcxS5VoE0KMdeJBmtIhLSuLaWhLlqG_2NwSIJ2BniKttrFaPX3n0kFe_rXNXv4MK38m_WBk4Yj1NHjcU02qdni3n6yV9yRNSgWiB7sOn67i4zM4P5GDuWKTjYPZbWvWilGq7QoTidTZAMLsJ9O2SXOtsd_xjy8RsTz0NXkSoFi-7u5PReWIWsJZmZjfEb9oip73689sncmgPgBpf2VyYoPmy6bMt9tFbnUFy_Jg8Go3GgJ_BFpJ9ZQnlj1GkLgdaBG_naQzW_cAtGBa242xQIcCEjoZ8fWyNhiHt2V_cNPcqF3fhMfCwJF2KNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9a854ccb.mp4?token=Exf2etM0ZJnP9gZP-2Xq_1qVjy7CVcxS5VoE0KMdeJBmtIhLSuLaWhLlqG_2NwSIJ2BniKttrFaPX3n0kFe_rXNXv4MK38m_WBk4Yj1NHjcU02qdni3n6yV9yRNSgWiB7sOn67i4zM4P5GDuWKTjYPZbWvWilGq7QoTidTZAMLsJ9O2SXOtsd_xjy8RsTz0NXkSoFi-7u5PReWIWsJZmZjfEb9oip73689sncmgPgBpf2VyYoPmy6bMt9tFbnUFy_Jg8Go3GgJ_BFpJ9ZQnlj1GkLgdaBG_naQzW_cAtGBa242xQIcCEjoZ8fWyNhiHt2V_cNPcqF3fhMfCwJF2KNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اردوغان، رئیس جمهور ترکیه: هرمز باید بدون عوارض و هزینه قابل تردد باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/681868" target="_blank">📅 08:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681867">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947f25d0e6.mp4?token=bQ4B5tdQQbri_AMPhv-YbAMdeBt-lwVR3yTH_bgi5Vdj-VnUncTtrgRzSrMnQqc3BhjoTdpntFeOT4rSMh8v0adx-X7l385n2xfpEmTSd6C0__yBJ6zB43Zlop2l_YpHm64ICfuSV71ptkCoGdNVFQ_LVB5o4u2BoR2lGF5I5Kej3NODaOrq2s8BNGpLLw6hP2kB2pewjqEsQ2CdLGr3jfpTdY2lF4e3hCUcENpUpfkPzD7xPqVUv_rdoSOCK7frdSnsUzI44XjRpk0GTGVN0V7mXiCQ0uPsihCj40NZZcSAtc6OFQgRmlmg0QabNX9hAYmQ6uRcdtR0OGsL1RHFZqxTe5V9PetpxqvZxw5v5j0VxjmrnYF7cn5lkgF47B1rp5ceknJ77yjyzFCrugoiLswUFPelwRSpyF0KfDOGGwVXzbk0ZUBsczfo0maH4o20QfUp08IMnsBTsSahYaLwSOGgSmF6XcrEa61APxaLPesD4WSlS5NdgFTSu1hXHJ4N11san_dXQcSoe2lwxwGvvRC175dmZXtXHbL7HjBEgtvmScUauEcnQQtBPUzOxA-BQx-iS_7Ej05MFtCIMvuwWL2wzuKZrcb2hdUUvzQ9ftz3WqZWNpuEfwwFUqFRIsMn787MyZ_WacKVzb-IjeQHIA4zNBQe6CsHPoTGygVdUgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947f25d0e6.mp4?token=bQ4B5tdQQbri_AMPhv-YbAMdeBt-lwVR3yTH_bgi5Vdj-VnUncTtrgRzSrMnQqc3BhjoTdpntFeOT4rSMh8v0adx-X7l385n2xfpEmTSd6C0__yBJ6zB43Zlop2l_YpHm64ICfuSV71ptkCoGdNVFQ_LVB5o4u2BoR2lGF5I5Kej3NODaOrq2s8BNGpLLw6hP2kB2pewjqEsQ2CdLGr3jfpTdY2lF4e3hCUcENpUpfkPzD7xPqVUv_rdoSOCK7frdSnsUzI44XjRpk0GTGVN0V7mXiCQ0uPsihCj40NZZcSAtc6OFQgRmlmg0QabNX9hAYmQ6uRcdtR0OGsL1RHFZqxTe5V9PetpxqvZxw5v5j0VxjmrnYF7cn5lkgF47B1rp5ceknJ77yjyzFCrugoiLswUFPelwRSpyF0KfDOGGwVXzbk0ZUBsczfo0maH4o20QfUp08IMnsBTsSahYaLwSOGgSmF6XcrEa61APxaLPesD4WSlS5NdgFTSu1hXHJ4N11san_dXQcSoe2lwxwGvvRC175dmZXtXHbL7HjBEgtvmScUauEcnQQtBPUzOxA-BQx-iS_7Ej05MFtCIMvuwWL2wzuKZrcb2hdUUvzQ9ftz3WqZWNpuEfwwFUqFRIsMn787MyZ_WacKVzb-IjeQHIA4zNBQe6CsHPoTGygVdUgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعمال قدرت ایران در بحرین!
کارشناسان آمریکایی:
🔹
حمله ایران به پایگاهی آمریکایی در بحرین به یکی از هاب‌های اصلی پشتیبانی و لجستیک ناو لینکلن آسیب زد و کار به جایی رسیده که برای مثال یک ملوان در پیامی به همسر خود گفته فشار شرایط دارد مرا از پا درمی‌آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/681867" target="_blank">📅 08:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681866">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/271fec4550.mp4?token=AOZSkrZOYO7zc1RVZG1JDKsTdH9Qnx9FoazjptRM5VljARY-Qd2dwasMqOpihQcX2xaR8QhztsXF1Y-wsiBXGvupsjvUTdFmKI5Dq_sR5peWDguWmkW2Vej4fmi6vQVKAJuRqoxDaaEWtygnQwgp7YSTR-ZAIHFWt85dq3OrQcbrdo_ruV0Hbo327Tmh_XpkQzKDIOKDqK4o1vRR2WcWw07iP8XKkKVCCxScMA1Dzg4Nj81LpSG_znwk7ZTFW37LHcBRMOizR750cvCn__oKt68MSJy6km1pUbLwiV_rEcChtg69bL17QQPV86RLOde3oeYOp5BHFWx61k8AyyHu8CSxvqMSQoMHdjmQkqfHznQzKdhKOPPDomlXHko0b5ObV1NGdLGBFGYo1HU31Cw0zmSVb51Z-FNGqr3vjInyA-fKmP_wjqxCv5D_11nVYuH1JMcINbk-yogg_x88McRN7xcguc1EYlF98XZyci4E9I-JHh5i0q69bFnoT1ld6XW3Wsrhy5PshuOZRiuUATH1Bq4IrNoXj-6ufe3O5o4w62AA5UBcEnMyi7wGudtSI0S_5Ixcv6y4aLHNIRhPKyqpIxxcw166mx0DTZr7ADyah6c3wANVaKZJNgflDkXSEqII0uNn1-01DsCWp0TXbXd0BaZLZOXsa5VmEVXTrvCabc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/271fec4550.mp4?token=AOZSkrZOYO7zc1RVZG1JDKsTdH9Qnx9FoazjptRM5VljARY-Qd2dwasMqOpihQcX2xaR8QhztsXF1Y-wsiBXGvupsjvUTdFmKI5Dq_sR5peWDguWmkW2Vej4fmi6vQVKAJuRqoxDaaEWtygnQwgp7YSTR-ZAIHFWt85dq3OrQcbrdo_ruV0Hbo327Tmh_XpkQzKDIOKDqK4o1vRR2WcWw07iP8XKkKVCCxScMA1Dzg4Nj81LpSG_znwk7ZTFW37LHcBRMOizR750cvCn__oKt68MSJy6km1pUbLwiV_rEcChtg69bL17QQPV86RLOde3oeYOp5BHFWx61k8AyyHu8CSxvqMSQoMHdjmQkqfHznQzKdhKOPPDomlXHko0b5ObV1NGdLGBFGYo1HU31Cw0zmSVb51Z-FNGqr3vjInyA-fKmP_wjqxCv5D_11nVYuH1JMcINbk-yogg_x88McRN7xcguc1EYlF98XZyci4E9I-JHh5i0q69bFnoT1ld6XW3Wsrhy5PshuOZRiuUATH1Bq4IrNoXj-6ufe3O5o4w62AA5UBcEnMyi7wGudtSI0S_5Ixcv6y4aLHNIRhPKyqpIxxcw166mx0DTZr7ADyah6c3wANVaKZJNgflDkXSEqII0uNn1-01DsCWp0TXbXd0BaZLZOXsa5VmEVXTrvCabc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این نقل قول دکتر لیلاز از شهید لاریجانی هم از جهت تشخیص و پیش‌بینی اوضاع هم تلاش نظام برای جلوگیری از جنگ بسیار حائز اهمیت است.
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/681866" target="_blank">📅 08:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681865">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScYmwk3_56i3MaGKJFZEoEReCDOhr5vWLsKzBoxvVfiJ6D0VI0ynKkjko_9AvLvnERQCma4ZI2Vu-x2PNE_jQm5D9KAwg5qBZCdJuL-feVPG0ZZag83cQT1jINh8ly-tGHTlV2rx72354WRPOrkxPpGKri-4cwZWh8pDGoSMbVUzmjGIQh411SYuJNagfmOoK3dX55OaDqQjfkusfoNXT0GNhLj-lO30MTOB-ZI0tqdBvYhPW0cMMvny1pgce2GBSV2i8zyHpx4oAafZSiJbkY7XOGF5WSxbTQmtefVqNIYIupo02EYjGoZEwd3hyge-8aClTSAFZVoWb_rZdXw7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دوگین، نظریه‌پرداز روس: ایران پرچم‌دار مبارزه با اسرائیل است؛ ظهور مهدی نزدیک است
🔹
الکساندر دوگین، نظریه‌پرداز روس، با تمجید از آنچه «وحدت و آمادگی ملت ایران برای فداکاری» خواند، از کشورهای اسلامیِ در تعامل با اسرائیل انتقاد کرد.
🔹
او همچنین با طرح ادعاهایی درباره «جهاد علیه دجال» و «پرچم سیاه خراسان»، از مسلمانان جهان خواست از ایران حمایت کنند و گفت:
«معتقد هستم ظهور مهدی نزدیک است.»
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/681865" target="_blank">📅 08:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681864">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b5d98ea0.mp4?token=RM4vpsW_4vi5bzFyVF5GdKjDhtWIcQza7vijfhA9l6n6onIejmiFmucCu2UL6qvOUVU-XC4UCO2qKty3fDn5-H_BalfapwQYRvOVed6rSLr0Ecq2jdNd3OEoUTxEQuITv-LIHgEk8vJnWUf1hHtsYcc-a8TSfpPz56X4if-nUexaaKg06jncam8rUruJsHzJ07oI0CHX2zNnrJA7yAlJxeCK-fCZt9xx2gxpu0tPppK07yUl7IaL2nEU5-GMyrH3XXWV1rDBv9g4qIPEERHw5l2MH4u3c-MD3dsNpvc3sA8oRk2UY0LBzaUrhDsY5CNX_EGjepLfvsBovxUl0fIdNXiYfPVMkR0hUTYPMgZ1K4DioHunTpboZyJVNnuTt07BkuuE2lxxeOpmAWdc6Ws4rsBHppywDb1I6ESNz1LhRug-SU2B3PTFHdISOaaAKKY603t-EwgFehW7xOSez0UxtwjJwAoll_Zx6lmX0OiJe1W6XU2R19kRyeQLeTdyyO6-k7Ezo_07GUEAzfkuD6WJXEhxRCLgEFFsYCVgEoZLvKaM_t9NdqrTdyoGJ3wWp3CpnALPQdSRcwXfeNEIopqjBcssqgrG7fH6lWveKZrh_urDURaK9LCSaCmcHa_eLFq9UhVHWJjvyu0GygTL_Dp7xHwwGgs6KvPojACkZtO2yNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b5d98ea0.mp4?token=RM4vpsW_4vi5bzFyVF5GdKjDhtWIcQza7vijfhA9l6n6onIejmiFmucCu2UL6qvOUVU-XC4UCO2qKty3fDn5-H_BalfapwQYRvOVed6rSLr0Ecq2jdNd3OEoUTxEQuITv-LIHgEk8vJnWUf1hHtsYcc-a8TSfpPz56X4if-nUexaaKg06jncam8rUruJsHzJ07oI0CHX2zNnrJA7yAlJxeCK-fCZt9xx2gxpu0tPppK07yUl7IaL2nEU5-GMyrH3XXWV1rDBv9g4qIPEERHw5l2MH4u3c-MD3dsNpvc3sA8oRk2UY0LBzaUrhDsY5CNX_EGjepLfvsBovxUl0fIdNXiYfPVMkR0hUTYPMgZ1K4DioHunTpboZyJVNnuTt07BkuuE2lxxeOpmAWdc6Ws4rsBHppywDb1I6ESNz1LhRug-SU2B3PTFHdISOaaAKKY603t-EwgFehW7xOSez0UxtwjJwAoll_Zx6lmX0OiJe1W6XU2R19kRyeQLeTdyyO6-k7Ezo_07GUEAzfkuD6WJXEhxRCLgEFFsYCVgEoZLvKaM_t9NdqrTdyoGJ3wWp3CpnALPQdSRcwXfeNEIopqjBcssqgrG7fH6lWveKZrh_urDURaK9LCSaCmcHa_eLFq9UhVHWJjvyu0GygTL_Dp7xHwwGgs6KvPojACkZtO2yNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک مهاجر از شوک‌های زندگی در اروپا؛ وقتی واقعیت با تصویر «بهشت غرب» فرق دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/681864" target="_blank">📅 08:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681863">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
کالابرگ مردادماه برای ۳ گروه حذف شد
🔹
از مردادماه زمان شارژ کالابرگ تغییر کرده؛ گروه اول پانزدهم، گروه دوم بیست‌وپنجم و گروه سوم پنجم ماه بعد می‌توانند از یارانه غیرنقدی استفاده کنند.
🔹
در نتیجه، سرپرستان خانواری با رقم پایانی کد ملی ۷، ۸ و ۹ کالابرگ مردادماه…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/681863" target="_blank">📅 08:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681862">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
آغاز دریافت کارت ورود به جلسه کنکور از امروز / چگونه کارت آزمون دریافت کنیم؟
🔹
توزیع کارت ورود به جلسه کنکور ۱۴۰۵ از امروز آغاز شده و تا چهارشنبه ۲۸ مرداد ادامه دارد.
🔹
داوطلبان باید مشخصات فردی و آدرس حوزه امتحانی را روی کارت بررسی کنند، مسیر حوزه را از روز قبل پیدا کرده و وسایل مجاز آزمون را آماده کنند تا از استرس و اتلاف وقت در روز کنکور جلوگیری شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/681862" target="_blank">📅 08:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681860">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ad9c2ab7.mp4?token=G8njM0GLLn1Qy8HxZIzDZLNQBxuZovdHyDFE5bVu8l4Na8HABub7mrF4HNYT6rswp0LdfmTdquxqAUbVhUGiSyCN18VwtNFCV4MKhd4yFqBlm6n9syWTK-0aXe1XIvzIr0833bly0HWSxx9IkX-BObFwb3KB3I7O2bs8Sjt9UdjU1cVpHKb6hgToF71etgNa7ZSLzIJLC7DwoysnmoOw_q0BbctC8_v1hlM2VwE4VHNQdafzoZJZ2FNv1OVSjCcf7iPXh5nKK985OEQ_lu_XCavor_IllliE4t_3nlNr5EGZ-_yjhX7ER-s5lXySriU6CQUJIuA0q5A3ke-ltj66KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ad9c2ab7.mp4?token=G8njM0GLLn1Qy8HxZIzDZLNQBxuZovdHyDFE5bVu8l4Na8HABub7mrF4HNYT6rswp0LdfmTdquxqAUbVhUGiSyCN18VwtNFCV4MKhd4yFqBlm6n9syWTK-0aXe1XIvzIr0833bly0HWSxx9IkX-BObFwb3KB3I7O2bs8Sjt9UdjU1cVpHKb6hgToF71etgNa7ZSLzIJLC7DwoysnmoOw_q0BbctC8_v1hlM2VwE4VHNQdafzoZJZ2FNv1OVSjCcf7iPXh5nKK985OEQ_lu_XCavor_IllliE4t_3nlNr5EGZ-_yjhX7ER-s5lXySriU6CQUJIuA0q5A3ke-ltj66KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌نوازی متفاوت مهراد هیدن با نوازنده آثار هانس زیمر
🔹
مهراد هیدن در حال نواختن یکی از قطعه‌های فیلم
Interstellar
در کنار راجر سیمور؛ نوازنده موسیقی‌های این فیلم که توسط هانس زیمر ساخته شده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/681860" target="_blank">📅 08:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681859">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bf7ebe59b.mp4?token=hFtndmPpC3EKSXRL_Ek6xuH6pJCx5PWt9Yv7ei5r_-nDneEUaEYBkqfs-l3E3wEbBZ-M4dpQc8BBrJ1OJJPtgEnyx2BPz-Ky-BCKpR57XpDPHa7lHqZqGGHUaUt41ICkSrN2rdtP6lQGcsWm455AUXnUz5h-V7vDSzYIPYBfDAiOKEiksGT2MbI9guIps9-XHRNwyWOjXNgOgzlb0ysfbuOB2zpUhVu2al2e4JkWOAdT2wyifWVgc2EayWarHtILV1M79RVjvRsHgPEiFknDL2BpEscGBsD-kLB89JLiAVOiq64TKi-fqsFflgnkXQitKMiVbzYxXfTbXzaxEPL1dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bf7ebe59b.mp4?token=hFtndmPpC3EKSXRL_Ek6xuH6pJCx5PWt9Yv7ei5r_-nDneEUaEYBkqfs-l3E3wEbBZ-M4dpQc8BBrJ1OJJPtgEnyx2BPz-Ky-BCKpR57XpDPHa7lHqZqGGHUaUt41ICkSrN2rdtP6lQGcsWm455AUXnUz5h-V7vDSzYIPYBfDAiOKEiksGT2MbI9guIps9-XHRNwyWOjXNgOgzlb0ysfbuOB2zpUhVu2al2e4JkWOAdT2wyifWVgc2EayWarHtILV1M79RVjvRsHgPEiFknDL2BpEscGBsD-kLB89JLiAVOiq64TKi-fqsFflgnkXQitKMiVbzYxXfTbXzaxEPL1dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر روز صبح چند دقیقه وقت بزارید این چندتا حرکت رو بزنید و معجزه‌شو ببینید
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/681859" target="_blank">📅 08:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681857">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omsSvL1EsqibtiHrEcThrKZO2dkTgC3kZe_0w103Ll3PyDbF4XwdhG625i7PxH5EHEySvTjTmlwgpGwaWCSTfsnV4_QmZyHBDrz9NWFgRZIG4idflNLvRILSvrrN-T8f-AZ4gTXFMx-MIwndC8ZPGve3Z_s-dRXUP1ir6U7bGfxGg_ESEiBB7AZryw5LRCBBsl81DvUoiJT6vO_j7exWLGQX4K4r0vCyTNGYZRFXc19WdSDk0AklYw_PX0FgRfLm_goWCqxIizmukjmj_mQZkN6KC0weUblAXGjLdkwzdfUiE-hNZ1u1WC5vwIiIqJpaJ8A2cRHDgVJK7mULycU3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با کنترل این ۳ عامل، مغزتان را سالم‌تر نگه دارید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/681857" target="_blank">📅 07:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681853">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
۱۲ میلیون جوان در سن ازدواج؛ ۱.۲ میلیون مجرد قطعی در کشور
🔹
مجردان قطعی؛ زنان بالای ۴۵ و مردان بالای ۵۰ سال
🔹
تجرد قطعی طی دو دهه حدود ۷ برابر شده، فاصله ازدواج تا تولد فرزند اول به میانگین ۴ سال رسیده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/681853" target="_blank">📅 07:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681850">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1jbnmy4R0huHoM4akPrHnG6hcJhn2U6nf7hAdGzd7RScHjZsTdslPT_bUadH1h9K1sX3ulOWaYgJen1J3QS0wyymYH7J4HqC5SmlTp0v26OC2wjavEe2xbjxl8XZCJt9grpKU9t0yTjHOvGdLk2jmuQKmv-87WFk3DFTdbgUyD8WYYmLGgAE3OpnPDOKhTkK68tRVU1bCPKczQuFk9_787oK4O6H_EbVbPv2GkFOneVwsxavUcVVN3Iyz1r0zUN9o9dBF-0MnH3FA2M4uxfC6_P4Q1hYD3qvZ6Xz2zmZdT0_xMsKyitEv1t9bBkEysimjZ3ECoynUVji83HrTMBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲۶ مرداد ماه
۴ ربیع‌الأول ‌‌۱۴۴۸
۱۷ آگوست ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/681850" target="_blank">📅 07:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681849">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taXJDbgsCzKZZBj_XcbH34yzo3MBTFzsQvVoQn0hNGLer4EyhS4lvzbx5VMNH0fuB66AWx1x1j2WMMevs4PZ-quvt6a5OE5YPgCAjXIKJJw9PVdOxTmnK7CcjtfWZH8DIvBgcH9XLd2bSAZP86xhervhBJ1eKGQIeRAc0h1cvfEHK8i8fYZe2hXQfXrn0chgVSU8LwjvtadYMkPinKEW_hBtioWFxAyu8rb-NcN1j2d-ZQOad4W81VcSrwQ_XVKbWNDXZsC4fFD_Q15gazqYFWBRJm_WM_Hu11u7wHQRcXkxUaDB69qQlz4e10huuCxNq1eYxQ7q9A1RYbokYrct5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
هر خانواده یک وام تا سقف ۵۰۰ میلیون
✅
بدون سود
✅
بدون ضامن
✅
بازپرداخت تا ۱۴ ماه
برای انجام ایمپلنت و سایر خدمات دندانپزشکی
برای دریافت اطلاعات بیشتر کلیک کنید
👇🏻
👇🏻
👇🏻
👇🏻
https://t.me/arameshdental
https://t.me/arameshdental</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/681849" target="_blank">📅 02:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681848">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار درباره ایران: اتفاقات خوبی خیلی زود رخ خواهد داد
🔹
دونالد ترامپ در خصوص ایران مدعی شد: اتفاقات خوبی خیلی زود رخ خواهد داد. در واقع، آنها همین حالا هم رخ داده‌اند، چون یک کاری هست که ما نمی‌توانیم اجازه دهیم انجام شود: ما نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/681848" target="_blank">📅 02:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681843">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
تسنیم گزارش می‌دهد: تراستی‌ها؛ ابزار دور زدن تحریم یا گلوگاه جدید ارزی؟
🔹
واژه «تراستی» در سال‌های اخیر از یک اصطلاح تخصصی و کم‌استفاده، به یکی از واژه‌های پرکاربرد در ادبیات اقتصاد تحریم‌زده ایران تبدیل شده است؛ واژه‌ای که در ظاهر، از سازوکاری برای مدیریت دارایی و انجام مأموریت مشخص حکایت دارد، اما در عمل، در اقتصاد ایران به شبکه‌ای از واسطه‌های مالی و تجاری اطلاق می‌شود که مأموریت اصلی آنها فروش نفت، میعانات نفتی و فرآورده‌های پتروشیمی در شرایط انسداد کانال‌های رسمی بانکی بوده است.
🔹
شکاف در حکمرانی؛ اختیار در دست کیست؟
ریشه اصلی بحران تراستی‌ها را باید در دوگانگی میان مرجع صدور مجوز و مرجع پاسخگویی جست‌وجو کرد. در سال‌های گذشته، بخش‌هایی از فرآیند صدور مجوز یا واگذاری مأموریت‌ها در مسیرهایی انجام می‌شد که لزوماً با سازوکار سیاست‌گذاری ارزی بانک مرکزی هم‌راستا نبود، اما در زمان بروز مشکل، این بانک مرکزی بود که باید پاسخگوی آثار ارزی، نوسانات بازار و کمبود منابع می‌بود.
🔹
راهکار چیست؟ برای اصلاح این وضعیت، نخست باید اختیار و مسئولیت در یک نقطه متمرکز شود؛ یعنی بانک مرکزی تنها مرجع سیاست‌گذاری، صدور مجوز و نظارت بر این‌گونه سازوکارها باشد تا امکان پاس‌کاری مسئولیت از بین برود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/681843" target="_blank">📅 01:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681840">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c501c9e4.mp4?token=vpJWFTekccdnp3eDzZb61EvGOlqLaRokVnXXzghmTlbh-HUGkEgCnNApO0e0KIJd9KLc9m9h1FYeFJoZF6zDe4prbFZrUfGwNbxHWkHA3b8ou-KNTDRohYpQ9yh1mr9IUl1b4buUWBjhSfZj-I1dbTpmHqoWdiLpke86dyOPZAXi3bcUxDWwv2JCtjp2zU4pU4yDRbN8wQL6l3qBUAQGVxY8N4vtBFOkbgnFgM9FfVslUizHN8BlbqPgQpH2juHPKjHoxsuyHVeKhL4y7EzXYGfgnxEdrTcYUZL0KB3s_sllvddXSLf_J5sEW0qQL3igb_iuw5MRS8gvUnwIiQbdFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c501c9e4.mp4?token=vpJWFTekccdnp3eDzZb61EvGOlqLaRokVnXXzghmTlbh-HUGkEgCnNApO0e0KIJd9KLc9m9h1FYeFJoZF6zDe4prbFZrUfGwNbxHWkHA3b8ou-KNTDRohYpQ9yh1mr9IUl1b4buUWBjhSfZj-I1dbTpmHqoWdiLpke86dyOPZAXi3bcUxDWwv2JCtjp2zU4pU4yDRbN8wQL6l3qBUAQGVxY8N4vtBFOkbgnFgM9FfVslUizHN8BlbqPgQpH2juHPKjHoxsuyHVeKhL4y7EzXYGfgnxEdrTcYUZL0KB3s_sllvddXSLf_J5sEW0qQL3igb_iuw5MRS8gvUnwIiQbdFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری شگفت انگیز از تصویرسازی ابرها در آسمان نیوجرسی
🔹
ساکنان ایالت نیوجرسی آمریکا، تصاویری از این پدیده عجیب را منتشر کردند که ممکن است نشانه‌ای از بادهای شدید، باران شدید و رعد و برق باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/681840" target="_blank">📅 01:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681839">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک‌سوم مبتلایان به آنفلوانزا زیر ۱۵ سال سن دارند
قباد مرادی، رئیس مرکز بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
بر اساس نظام دیده‌بانی عفونت‌های تنفسی مرکز مدیریت بیماری‌های واگیر، ۴.۴ درصد مراجعان سرپایی و ۵.۷ درصد مراجعان بستری، دارای علائم عفونت‌های تنفسی بوده‌اند.
🔹
تست آنفلوانزا در ۰.۷ درصد و تست کووید-۱۹ در ۲.۹ درصد افراد دارای علائم تنفسی مثبت بوده است اما هر دو بیماری در سطح پایینی قرار دارند.
🔹
۸۰ درصد آنفلوانزاهای در گردش از نوع B هستند و نزدیک به ۳۴ درصد مبتلایان زیر ۱۵ سال سن دارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/681839" target="_blank">📅 01:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681838">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11395e9490.mp4?token=dN7qRlxQGTot_on_Ef_HFFEcdnzaIGHyqOZr2H-e-jXMgGtgz-XvJ5_oHtqeZeWuiUDzH4plERYbv6QHo0a9EnmwE5VzVAnjWz_E7-88SdPvfNKNL4MDgSydU8x1UPT4v2aKPLJHM_-FqtcqLERiefhHvGQ-WsH-rg4KQwqFcBEHoiYX9mRKtN4MiZgFGgUVoCN8sm4vEUX-G7B-izt12AsQbahfxkaiK47IPLrk28R94FKGjFdXwD_Z_qEBuwETb-ckhXPvpuffClHT1mnAbZgfZcZK8aE8bgUAqV9enydvcV8Dzd1CkapMfvNzW8-i01a__eOG0CF_PdYFm65AZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11395e9490.mp4?token=dN7qRlxQGTot_on_Ef_HFFEcdnzaIGHyqOZr2H-e-jXMgGtgz-XvJ5_oHtqeZeWuiUDzH4plERYbv6QHo0a9EnmwE5VzVAnjWz_E7-88SdPvfNKNL4MDgSydU8x1UPT4v2aKPLJHM_-FqtcqLERiefhHvGQ-WsH-rg4KQwqFcBEHoiYX9mRKtN4MiZgFGgUVoCN8sm4vEUX-G7B-izt12AsQbahfxkaiK47IPLrk28R94FKGjFdXwD_Z_qEBuwETb-ckhXPvpuffClHT1mnAbZgfZcZK8aE8bgUAqV9enydvcV8Dzd1CkapMfvNzW8-i01a__eOG0CF_PdYFm65AZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: هنوز نمی‌دانیم چرا با ایران وارد جنگ شدیم
روبن گالگو، سناتور آمریکایی:
🔹
ما از سربازان آمریکایی حمایت می‌کنیم که تلاش دارند ما را از این جنگ بیرون بکشند. اما رئیس‌جمهور هیچ طرح و برنامه‌ای نداشته و معلوم نکرده این جنگ چقدر گسترده است، چطور پیش می‌رود و چطور قرار است تمام شود. مأموریت ما دقیقاً چیست؟ ما هنوز نمی‌دانیم اصلاً چرا با ایران وارد جنگ شدیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/681838" target="_blank">📅 00:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681837">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hv2HkcIlK8S7TMtzOLCmoSOaWiD6KWrOegwC0a64yxQs_UNhT3QvTrEir2612bNPjgwuGYo-Oz6n2uNNj0PUHdTnPx2PAIBER3SGDtXEiPcAGf5A3NGGcXZ2wQWY8-lFAfg9I-BFKq2Xg8xkezmA3234sOKS6dXWDElURddtOX-pmaVA05JOt6muAE5KWFCYo_op5SC3omRlGYH9Ls0M82rCTNN6dJzWC9D8Yd5DQIa0oB1wcFF95RkXLXMT1736BgoHGKQJ0z_uSWO-2O-p3mSOdLrCkvKG091PaE1ukcHDLNd6BH6mpvp5lX-0yim3fdHfnza4J8l2XKHCSO6X_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناراحتی ترامپ از رزمایش مشترک نظامی با کره جنوبی
🔹
با توجه به روابط بسیار خوبم با کیم جونگ اون، رهبر کره شمالی، از این واقعیت که ایالات متحده مدت‌ها پیش موافقت کرده در رزمایش‌های نظامی مشترک با کره جنوبی شرکت کند، راضی نیستم. این رزمایش‌ها نه تنها پرهزینه هستند، که بخش زیادی از این هزینه‌ها توسط ایالات متحده آمریکا (طبق معمول!) پرداخت می‌شود، بلکه پیامی کاملا نامناسب و خصمانه به کشوری می‌فرستند که تا زمانی که دونالد ترامپ رئیس جمهور بوده، غیرتهدیدآمیز و محترمانه رفتار کرده است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/681837" target="_blank">📅 00:55 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
