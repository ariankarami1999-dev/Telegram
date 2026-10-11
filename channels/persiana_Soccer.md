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
<img src="https://cdn4.telesco.pe/file/K0qX30OC7phT48fjn7687RXAAkWzZ5LKuOEqJIEpCmAfdIUlc4TihmqTWyXaq2zxDKMtgiysQVxvbv3GY0TNS8lTU048qiWxy3APzN0ASFkr8vN8u9FO9xqNifZzTpT4sB410sFEQ5L27rP4z1Wu9VV__hikT3MInoTZp0vxQPFcEG69L_W2rJmzMAHrUyUa1YtXeAFPDdXeaGhTjZbLq5ZIdSQmGshYjwykIMBfCQnHhVZGRJIT8CI8leXoUffyYAmPwpGfoGvwM555n1HMHBIKks51_g9nDWMLlrUErFwaTdFlyDibr30ka3uSTGz_i1hQFp_6pRdDD5Yrr5MlkQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 484K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 16:40:45</div>
<hr>

<div class="tg-post" id="msg-31374">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB51KmheiSB7uxT-4CIlER3YR_G6KNMbU58hOfnAeN4EJDbVtvj47KlmzdJUEtMWEoAL8e7aQhpjh8LxIgsYigaoYNPXYyy7JTiDvzLVktUKFWQZUti8R7sK6IhQoqlu3UxX9b3iMAH4HChEGFUTS7sLTAISSSLsZHtKzTyEiHmud2sL2eQIhHMPZKXuGcJHJbgn90TJXp8t2K554PYsOeO9cGS9foh04dOx6fKlJdXrlvCLmyhcXTnaCpWEx3xFKB5Fqk26z_SjWJHNvFot1vTx9nLMevWQvfZuGauhxLyjHoaz194__4RMtARiurRj54mJI6JhqIt2CK3jhvQmCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته ششم سری‌آ؛
تقابل شاگردان گاسپرینی و سسک فابرگاس در ایستگاه ششم برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/persiana_Soccer/31374" target="_blank">📅 16:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31373">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwij_VzuFrPs4tjydVjJnGHUzybHFFpFs43d5dkKr3iey56FGpm82wUJWqJk4qHEVWdCTV7wSesUmO_tNDRzXG7_WC27frL7K8xz7LX76KBYe6M9vGf-PDyRS954UHH4yjf7mmbMDlExgCP2-tgr8ACBOFRwYJGp2GhXP1tTpeaQXjtIvCFJ78mtl8wYuS1u7VKI-MTdTXhXJnzOpj15QblxEdasXpAYjrpPn7zRk2IU1138aOre-ufTGF9FU8RcOK3yxs22CeJfgpXz1Jdw9xgR4i0bYrc82VFLxFzGhtuyZBLL0EZAZiIKD87s-76vOQtRia-BdmfVGrPyI74zxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهراب بختیاری زاده پیشنهاد حضور در کادرفنی استقلال رو به پژمان‌منتظری کاپیتان‌سابق‌آبی‌ها داده. منتظری گفته بزودی جواب این پیشنهاد رو میده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/31373" target="_blank">📅 15:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31372">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrSw4aXtgBLqUAJrWOsacK8yPgt0vje165gHIAUhj08yOPEpf1yTQ9XSXY_qmUPQq7lTwnVYI2JFD7Maibt4nppzZbVb9UGH9-8KF0K7LNL7K-Z0zLuk5pnO9dVEPSKFrLki0WNnm8UJLqctcLDx0KnBOVRjS3k_97Z0-0MytAmljZfgK307jvZUJuScYT78tEwiLLpWRBr0zSZ_YIRxuLv9eWILNwyAyHTYCx9BH__tAyFmR_I6G2gxs9H8sDjPJBU2MV0h7K5TOGvNY_-n7p7fS0oMMy_lGySzss5rk_kk8KiGn835-yDeCqGsJfeXonXSoYty8Vw8kYk1wg63QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روایت مؤدب‌ترین و باشخصیت ترین مرد تاریخ فوتبال ایران ازسفر۱۸ساعته کاروان تراکتور از تبریز به عمان به دلیل محاصره هوایی ایران: پنج بار فقط سگ ما رو گشته. اینجا هم فک کنم صف روغنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/31372" target="_blank">📅 15:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31371">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRLwwgfTNoOrCen8PXoSV7vso5GgF9GO4BHY1aZDZcRMqcgya-zCMWqc5pVXBnSxfiVatJdvu8pgdE3_qQZEkF4PSgrht-hmniRw2JorNx9ZkKUqiNxTSZep525faXWrcK_CJB32GLuZU7vOCtCyVlKyUtG2GoZvvqeq8G_JsVrkxicq2AvV9Rzh_jEzQAPu5Q1_APjS9JxLaVyoSRXyKfvLb-3K3EIRFteHGhQa7E57vwi2MiY-KEQ5kWdSX82aZq-lDQENNZGcHSj3edvv_myc65vW29021_cl6V3jQak82vSYlZwAIsljTKFa66IPj4TYLw1vJ4OrCj4S6rJAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/31371" target="_blank">📅 14:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31370">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85d440852.mp4?token=Hi7mVSfRVqKDohsjKcao-AIB2cclGFEP03QfBDn2DJX5NAMiHx7tijYgKC4JfqkbGV5W3v5j5MuA9ss9ogMFoYC8irPxnRgQUds2FzozFhd8PD8vlTzmNvsXMYM3rBHx2pP20Qp-HHj9-I5kaZFiRFcdt306nQh3VNbkWURt4EiVCCXSDwKfxIdYao-F8H312KM6nfkBgwiQnTH_qWGCArlSBdAP_mzMnNQD7iWBks01UN6BJ9MB0uQLkxvMxeUCQmt-x9O1XLi1jYr710T_YUavOWBPHEBeXrNBsdQjqLNzmchwhUmU7RidfoNh8rU1bZEuwyiXSG3nXZZGHtYxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85d440852.mp4?token=Hi7mVSfRVqKDohsjKcao-AIB2cclGFEP03QfBDn2DJX5NAMiHx7tijYgKC4JfqkbGV5W3v5j5MuA9ss9ogMFoYC8irPxnRgQUds2FzozFhd8PD8vlTzmNvsXMYM3rBHx2pP20Qp-HHj9-I5kaZFiRFcdt306nQh3VNbkWURt4EiVCCXSDwKfxIdYao-F8H312KM6nfkBgwiQnTH_qWGCArlSBdAP_mzMnNQD7iWBks01UN6BJ9MB0uQLkxvMxeUCQmt-x9O1XLi1jYr710T_YUavOWBPHEBeXrNBsdQjqLNzmchwhUmU7RidfoNh8rU1bZEuwyiXSG3nXZZGHtYxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
ویدیویی از پاس‌ های تماشایی پل پوگبا در مستطیل‌سبزکه‌منجر به گلزنی هم‌تیمی هاش میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/31370" target="_blank">📅 14:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31369">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azbJqf7em49RGQ4pZYiU1ZryBZBM96PGiY-iUAb0dHulImsEBoJE8HElA5EhFO4-Sggoca9ay_qN7BU0hLmmNx_oju47KutJ9wLRokFqmV-eD20VcKdk6ilTwnySHuLgpCL28HFXip9ktJVkSVcC_vXk-arMDEartm4YP-dr2nJNaGVgSsQ8Q1F41yrFWYeE7hISphb3Jo3utGd8SjvjqKKmAObn_OUkvQr4SNdzfu-8W1CMVWYDuixnWxeZe_-M4nly1gDOWoy1Ykezq245V5IFEK63PKfsOtLmNGM7Z_FKM8c3nKozpjN4XbU-KCY_A7JiHvSGVCy_95y8DICdaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/31369" target="_blank">📅 14:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31368">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3XmSRhTt7zzhuHzFPwVBXVH0chTYeQiK3JvTVc8pO1YJoAEk6US1vml3qpqGnn96xfO9jm0AJ-9c3iaDAUqwbjvdiE7K34rgJhI5Bly9tIouPM4fP3hhxExFf2zJ6dkT3QKiqb4B70q92_Zm0dccaTnzAdjKIYFfkNfSP76IamcmFIUd8LXHm2L4-zZS9jtRzXgDoHylQpeAg2wRgTyVgMCQJAC4kcOLiFcfpXi5YxqotQMxoy7IKeLsiMCI2DhTz39wTFT3XvaMMHWr24mJnA-D8T2Jag_JKCgcHa8gOryS0aE94tOYep9XK9HRSw7-mmMY4pTSvJOswlMxc9ylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار شبکه DAZN ایتالیا و از طرفداران تیم آث میلان که گفته روسونری با روبن آموریم به جایی نخواهد رسید و باید او رو از این تیم کنار بزارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/31368" target="_blank">📅 14:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31367">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Odhq2xI7vEz2EHHN4dQfWjXzJauepUIjp6fToiJ-hkBxcOJ0GNOwl4AYq-MRQb00fwczAB2YA7e9bsIE95DWs8r7Nq1mm9JBznJyLwS5ggraBVOgkmaQ6SYQKaUUtvOM2FU5ivIluM3FOgsJm7Z36BHc6w0LUOX1GUWo7haatrmRSbDsAnGUOWWvFt2hhAbRZVz_1BYtJmoO_KhPCCXxZFhjLzcZScI6QyrGd9UDRYliN5rjpapVuQjEmC5n-fZaCKpnDH86mkwBKE47fV-UeJ2smQPxmFt1MHP7zpy9nOJEEIY3EL1mvR1JqW3cN2unxyMaCLcLSH-mhZpgnF4wCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ساکت الهامی سرمربی پیکان قبل بازی با شمس آذر: من‌دیگه‌اون‌ادم‌سابق نیست و دیگه دست به زن ندارم. ساکت الهامی در بازی دیروز با شمس آذر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/31367" target="_blank">📅 13:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31366">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv57vaI7ZRX1aVsI1qDse5wH3U1v_2Zn7nZ06sRJ2ijcbz2Ws2DuVvZ_5hWPvqDksId6yAZ7mtQ3o_-FmkJo0Jc0vd1d7ot5tjmBTAWr5e5OBb8HTphBjTD_Eh2iG8vnRSl4c8v5Nod-wQtcuGwVKRzmtOXzFWrr702-UgugP5lm1tzk3WO3Y2bgepCfta5DKojvG_XORUM5yLYsNLwimZ8pXMv3HmaUIvyTIqMR2lgNW4H-Wjqw4n7hQNvShsap_9YA-0nbmkt4dAtRSJWQ9_oj_nGRqPTtUdvjreZuZRzNpVwkIHJ0Uyt_b5AL66JbLvK5P2ichipCFT50Xf97cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ عملکرد درخشان کریس رونالدو و لیونل مسی در بازی‌های این هفته تیم‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/31366" target="_blank">📅 13:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31365">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9b16df533.mp4?token=ugK86nQ-vyPdk7UVYmp5NKc2scdB_XRfv8T9H-dV8L808Vh95Zdm8g7zcMUytWvD-CDq-blOpMU1fj8kJ140FHnlIuIRgYLHSx_vONRwvllbuKeFpa_xfoazJppVM66eZePVsB1ILw3prXs3oTyDrgGjl6c1UKzhkGEr8PaUuqrAFv2bwGcWqDbhSohDGUwX37cPyskPg7zQWYHeeSAq0FQY7Ne1UgDjLL75SYsTyMig5UmBza_YVvxPZZmgPolvZ4kewb0ZI_OLVnN_RnfYxiZUmgvA8rJBDc9X5TDqUxcVN79NRVSrcBJ6GEAGSs6pX5g3SrdZbZKetWbbkFGkhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9b16df533.mp4?token=ugK86nQ-vyPdk7UVYmp5NKc2scdB_XRfv8T9H-dV8L808Vh95Zdm8g7zcMUytWvD-CDq-blOpMU1fj8kJ140FHnlIuIRgYLHSx_vONRwvllbuKeFpa_xfoazJppVM66eZePVsB1ILw3prXs3oTyDrgGjl6c1UKzhkGEr8PaUuqrAFv2bwGcWqDbhSohDGUwX37cPyskPg7zQWYHeeSAq0FQY7Ne1UgDjLL75SYsTyMig5UmBza_YVvxPZZmgPolvZ4kewb0ZI_OLVnN_RnfYxiZUmgvA8rJBDc9X5TDqUxcVN79NRVSrcBJ6GEAGSs6pX5g3SrdZbZKetWbbkFGkhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساکت‌الهامی‌سرمربی‌پیکان درپایان نیمه اول بازی باشمس‌آذر اینجوری رفت سمت حجت احمدی و یکی خوابوند زیرگوشش بابت اعتراض به کادرفنی حریف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/31365" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31364">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b580b78a1.mp4?token=RUOdZMQDpyQpezmLRbQ1uj840Sjxkx3XY67avgDHDPSPyZ-eoSxxAUyU0idtx_N-ah8HBlJsEdQlV7TmpX0TnVKcr67Yw7ZDIa4vfiHjJTSrYPiegSb-XYh-NfW2FDaLtnMSDwrkoInwE1PUBNMPKuHb-reHc8kYKeiSZifG9TfJ8LZFJrtRyrsmODFMBOQL7gAyFqfOC0Af-j8FlUaUGWkAde3X2a4XrTDzDcFM5AV3Rv6DqNTkma07EVPGOv7YQ8ZdSxglPEXGWuqBrVSgestKmkoQmxPxXsbBMLIIuxcPu95y2fKPyeZE8_VRF5qyRgP9X__GwsyUtKe65v-4_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b580b78a1.mp4?token=RUOdZMQDpyQpezmLRbQ1uj840Sjxkx3XY67avgDHDPSPyZ-eoSxxAUyU0idtx_N-ah8HBlJsEdQlV7TmpX0TnVKcr67Yw7ZDIa4vfiHjJTSrYPiegSb-XYh-NfW2FDaLtnMSDwrkoInwE1PUBNMPKuHb-reHc8kYKeiSZifG9TfJ8LZFJrtRyrsmODFMBOQL7gAyFqfOC0Af-j8FlUaUGWkAde3X2a4XrTDzDcFM5AV3Rv6DqNTkma07EVPGOv7YQ8ZdSxglPEXGWuqBrVSgestKmkoQmxPxXsbBMLIIuxcPu95y2fKPyeZE8_VRF5qyRgP9X__GwsyUtKe65v-4_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه سانسورشده از مصاحبه چند روزپیش رضا گلزار سوپر استار سینما و تلویریون با امیر قیاسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/31364" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31363">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOfrKsBGQAJohauRuSSm3epkY2-Plotp_sn2M2ZjCU7vZvcWfwVNVir5YSH5WJg-TbeIWYIrNFWUSTMjb1AAb75_jTp_6MoCtJVESyYjQaGfd6uj9aJaAvQ5s8JxAg4iLf3es1ZXCc6QClJjtQV0lSNYxlJ0ITBTFg18WmUvNvgYE7r2SQV_ydbP8MfTHzgg-AFwL3qUOxSEq0zQasUgQod_Mb-unF3DjlRjHCrOmndvnvGPY-3TbyCKMK1Sl7y0bkrRRiuRB8L3DCFts3dRWgcPNB0fcQal-9jRb37gv3tcPjff7m0PfLtdFAY8kY_tzMj2XtU5uLv8aH0pgfFoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
لیورپول  - منچستر سیتی
🌎
ساعت ۱۹:۰۰
⚽️
هال سیتی  - اورتون
🌎
ساعت ۱۶:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r19
🔗
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/31363" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31362">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b124cde064.mp4?token=eH-ZWdAIm2SrcE00NifBBXL6Af4Yhejt5JiWjxxQ8Li9skZvosnvTRrvB-CKgIuJ16MjmDavYYS8u44pmBz3HqzqjybEZ9IpDfCl_f_lrMHT3PUsqArXq_LmVVRHwfrCKJ-59FEEraA6Mc7CLrET54j1G2ISpLuhF907Z4J3N9Q8SsRwVGloFgVIPVy-YYFnUnPTrybrsuhtlmgHFxuPAtxGgkubBMsPAYFZEOCMRoJEnpjoOArTcks7uZPReDCsT8hUl4nOynZm5R6ihTCCjB5KisQ4AFAj1GcIlL33O7nKqRgpk_l7LzxevTnPFkcRCz1y8D9MYkV16wf8Kp8TBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b124cde064.mp4?token=eH-ZWdAIm2SrcE00NifBBXL6Af4Yhejt5JiWjxxQ8Li9skZvosnvTRrvB-CKgIuJ16MjmDavYYS8u44pmBz3HqzqjybEZ9IpDfCl_f_lrMHT3PUsqArXq_LmVVRHwfrCKJ-59FEEraA6Mc7CLrET54j1G2ISpLuhF907Z4J3N9Q8SsRwVGloFgVIPVy-YYFnUnPTrybrsuhtlmgHFxuPAtxGgkubBMsPAYFZEOCMRoJEnpjoOArTcks7uZPReDCsT8hUl4nOynZm5R6ihTCCjB5KisQ4AFAj1GcIlL33O7nKqRgpk_l7LzxevTnPFkcRCz1y8D9MYkV16wf8Kp8TBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/31362" target="_blank">📅 12:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31361">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230f3b6f7c.mp4?token=RtLg969Z1pnC__gaYU-9kMbARXoNKOoz1F1aPmmn5EeAFyO-1Dhmaeg37EKsLPWCcZ2SWkGRZ0UAG7ZXnz8o4y7h7USC7EsfTTz-iv6KnzONuIc45cOE6ZbYBfatYIfRjXHzfIh9lVBQAJX5Wmip-m9ptTDdJWURs5I9cvYDjzfgqij8_hF6ZYhNZZ1c6BmgtwbgT6zmZi71zvLvjwTBtR7R0descoXB4igAGuT1ETzmXm5NPtIqn7yr6bgp97ws8C9wJdUi_mGM7pi6vnlG2AjTiXekzmMFAFqOIqzcTGrVH5dNwrqRBVno5t75k7k5y14Y83k_GVb7RNmZbJR5mB2MwvXkYlwO3Mh-jdxWATfh5Xp275QoYY-9GXnaAi3xvQqsc1Hi281itkrDNESy7btqERArUg2dgxU96DpdNjw6EF0LDd2Fbe8vFNh94ip9RXsTUVRqnw0thO9Y0BaB6TVem3zGTfXlaJtiRGyChA30-cIAX26YVyJF0xDcCw8SZxQ0DDH4uIBPgHgvn51FUecQaVU-jhYOC5jiCSdOQe-QbhcwJvUUZQVazXje8xA1WH4eDrU1gTHnQXcLoEmyVk6PMNiTgR3Kl9exxKntCnKlpiCxD31qMFzkX9LnChMcOGddssYKQYo0Mk-k8-icDJi-9P-XcZyz7JFIkzb-GrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230f3b6f7c.mp4?token=RtLg969Z1pnC__gaYU-9kMbARXoNKOoz1F1aPmmn5EeAFyO-1Dhmaeg37EKsLPWCcZ2SWkGRZ0UAG7ZXnz8o4y7h7USC7EsfTTz-iv6KnzONuIc45cOE6ZbYBfatYIfRjXHzfIh9lVBQAJX5Wmip-m9ptTDdJWURs5I9cvYDjzfgqij8_hF6ZYhNZZ1c6BmgtwbgT6zmZi71zvLvjwTBtR7R0descoXB4igAGuT1ETzmXm5NPtIqn7yr6bgp97ws8C9wJdUi_mGM7pi6vnlG2AjTiXekzmMFAFqOIqzcTGrVH5dNwrqRBVno5t75k7k5y14Y83k_GVb7RNmZbJR5mB2MwvXkYlwO3Mh-jdxWATfh5Xp275QoYY-9GXnaAi3xvQqsc1Hi281itkrDNESy7btqERArUg2dgxU96DpdNjw6EF0LDd2Fbe8vFNh94ip9RXsTUVRqnw0thO9Y0BaB6TVem3zGTfXlaJtiRGyChA30-cIAX26YVyJF0xDcCw8SZxQ0DDH4uIBPgHgvn51FUecQaVU-jhYOC5jiCSdOQe-QbhcwJvUUZQVazXje8xA1WH4eDrU1gTHnQXcLoEmyVk6PMNiTgR3Kl9exxKntCnKlpiCxD31qMFzkX9LnChMcOGddssYKQYo0Mk-k8-icDJi-9P-XcZyz7JFIkzb-GrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌فوق‌العاده زیبا از جشن فارغ التحصیلی دانشجویان رشته علوم ورزشی دانشگاه شهر اهواز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/31361" target="_blank">📅 12:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31360">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ پیروزی سخت شاگردان مورینیو در برنابئو با تک گل دیومانده؛ اختلااف 6 امتیازی با صدر حفظ شد. وینیسیوس ممکنه به خاطر کشیدن موی بازیکن ویارئال دو جلسه محروم بشه و الکلاسیکو رو از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/31360" target="_blank">📅 12:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31359">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCFGSjjgQYPQJa30EAR1mhtxrVlK2Hm4qH_veOhEZEltw6GhgY00MmJibk3NNNqYjmIAGJbYCzOMJpTw9exggze1ZAHvLFKCHKJsNazgiu6wXTQPz6Cxdxqx2eYhYN-w1F7xYD8wxLoUnvhQhCGiaF99BvUXFiN6qzIxX6c9UaPvLMHU6Hvt-wduucil6Ql4VxAQXshcDdfl3pkY7p7FGa2l863qL2-Td_s1jPByYP06Wnbc_ryx2PvTYrmIvrFk2zTQEJm7Fb8XvrFF7mBFQWgWM77xwS-JQIICQ56Mtt-_Wj9aLTB-xDViZ20u3BKsBAoau3qmf10LWCtCDMPXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس هیات‌مدیره استقلال: با علیرضا بیرانوند هیچ مذاکره‌ای نداشتیم اما درآینده هرچیزی ممکنه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/31359" target="_blank">📅 11:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31358">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brqjCc11o80F6rrZQnIXIRB6T7gaoDAafn4WwmaGMrGBEdWL-_gXbq37kLmAjGH3dYLoHZvbFq5b1STcUXBFPsEHPNOJ52S62iBs747BbEH-DIx6xGnQya0nPLJi4ZK2lRClZXo-o9dO-hG-AI9jUQ8Em6x_M6KcyPPW5vqF0QE897OgAlLoUT8ETShZRDIx6dgxwrIXZOUyVxd0jWNcC-VnIzoUGjDotfiZq1mqZ8VXhGddVsofKg3eDLxG_l6GA47AK0GtsvVUdt__n3cpYP7eEfA9KhLmJoZcPRaMoE7LLij6Pt77HJXKssT2I-ChAb854Dmes_-LTWMSzk8Lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
گل‌های دیدار امشب دو تیم منچستر یونایتد و تاتنهام در هفته ششم رقابت‌های لیگ‌جزیره انگلیس؛ مایکل‌کریک سرالکس‌جوان‌نشد و در آستانه اخراجه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/31358" target="_blank">📅 09:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31356">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rz-R4MT0Zmdcx_0a4mmjYB08kZXyRlzUpPOJATEEcFkvI2jX1412DXcQBX-qIqDekgEBSSSHweTjfUDyZRxFPSFpwo5fsjhHZDCbCBMLOSQrdCBFrsravDy-TmA5uIP0LZpN_pjUKLVE1Ui0NCRZPwXpmyRo8TF4zCTNcrQDcxuKU05dwpoa516-f7qh_Bsyg-xS2LYWy-JZ0sQhZz3d5sCIPwoLwo_CEFFXO-asxGXS6ID6n2HbUoz-pJVNZs1GpsvX5vShiMlEhTZxenU2ruj4uryfjcP5DAVPTSeQ3CeKJZ-HktcFjSf5Yq--KYTIxEORTL9nlBpw_JapLvXJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSGVwhhNtISP6TA_Yv9saJyK00G6BDazDvV_d8YlUrEpIUd2-JCRJlpATtYEUfkCgHjWYE0ZtYxc6KiCrKhuG4tzCqVRHMI1F54p8TV7jjTaMomuOUiE3GARhlIC7LX-_Ic_WunNPoKIcXWdFXBkaRHhan0pQK2IkiCuL51s6S-p8e8B6m88a4X6I1DCzea4QMENRAN_yFqeVmAdtjRqMUkNdQ2HDERmtRZDDc0NZJV0jezNlPsu5Az5PgLF70CuXugYP7bTSBGVPrDafUmXoZS1asDF6cQy33Hgw1ItwdqjJdGbpzQ41g6B6x4FTy3L-jn5fP_q08liwTMcdm7crA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
🇦🇷
دبل‌تماشایی‌ومحشر لیونل مسی فوق ستاره 39 ساله آرژانتینی اینترمیامی در بازی بامداد امروز این تیم در لیگ MLS؛ تعداد گل‌های لئو مسی در کل دوران‌حرفه‌ایش به 934 رسید و برای58امین بار از سوفااسکور نمره کامل 10 از 10 دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/31356" target="_blank">📅 09:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31355">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNrkb6BuHVNcrao1bdFVB5uWj-gF30bsOhIHJcqHimrMLr6oi9kIua75tvgenCy-sZnbVZDEK-DPQlA5KrasVsNErinYgGgyqUYwSLUHnzz3aJXB4aHGnr5-rDpvx81OoJwOidCwhzKKRN0mK8j3sPHXp3qRzMO5tXXdwCrP5eQonqs6RMmE_-iMvUAG5j77jMuxyQrDEVUrK1GKcHh6WpKrXkrnEYPP1B2hRjzvVH7drehXoyZeyXtiLqMbryKN_lyC3OsRlS0jN68sywGnfD_FaQ3mYhoDUuHrWE1ZG3ATVyFXcpnK3AJDXCcJqxOi5nstAO_Nog0hgT-FDJQcNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بارسا فلیک تو این‌فصل: 9 بازی. 0 مساوی. 0 باخت. 9 برد. 39 گل زده. میانگین 4.3 گل در هر بازی. بهترین خط حمله دنیا. صدر جدول لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/31355" target="_blank">📅 09:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31353">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa22c27bfb.mp4?token=aDr2jm2U-Gqg8Eu5GLPYGsGWgWXJXWtgM7HMhZ0gBTSjiWOx_vEbsNZwH1csLHc88X6Scp7SeEkcVCp3dTlgCbEpEBznsPiX4VWODH-d9h8bI-b7Ixog36IkjV6LUK3TB1IN-oPEoC3T-3Qe5pu8VmByyVXywEiCy40VoSIuNUovakMVYZMlixnqTJYrGrYgAPV_75RU0YfeqNCxxzAWKpMvqkWIa2Cmc4rJpICMhMoFp21ycynzlwoGolijT-hODbdpvCBkoSP9K0zJxtpPbEysgDJvWhSTBjGqmMyyVN8WC3UP4kmk64vaTA7mszG5n0BtyXMOUPKR_nPxSe1dUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa22c27bfb.mp4?token=aDr2jm2U-Gqg8Eu5GLPYGsGWgWXJXWtgM7HMhZ0gBTSjiWOx_vEbsNZwH1csLHc88X6Scp7SeEkcVCp3dTlgCbEpEBznsPiX4VWODH-d9h8bI-b7Ixog36IkjV6LUK3TB1IN-oPEoC3T-3Qe5pu8VmByyVXywEiCy40VoSIuNUovakMVYZMlixnqTJYrGrYgAPV_75RU0YfeqNCxxzAWKpMvqkWIa2Cmc4rJpICMhMoFp21ycynzlwoGolijT-hODbdpvCBkoSP9K0zJxtpPbEysgDJvWhSTBjGqmMyyVN8WC3UP4kmk64vaTA7mszG5n0BtyXMOUPKR_nPxSe1dUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/31353" target="_blank">📅 09:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31352">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDk-OMtMilRZRO98zzEHrSvafG375sZ8fUji665fDPWTe9wTI24IIyRrhBj-u9GqpUPIrkua9rG6RxFNpii2KH6YbYnkO0g1sDHds2U54xB2mrWgCQ9hjZb-fAaNpf6-JNsA1MiW4QNK9Oy4WCNQ9ZoScDcJCtsKStVQSAqPUVfcM7ETrkWx8yQ2I78lSx3yc8pKXNbTeFAdZkETvAFwrvqmoVAuKq-41i1f-GHUfxfub1WTiI8KUmRCQSBT1C8fobECUQLtDqtKHbdf3KLETuXdDGtXahhpGtRzsmwSEFve3aFV_lzdj70WEjB9gEyDTDKAnOzkQumA-1dtDaZK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ دوئل حساس لیورپول vs من‌سیتی در استادیوم آنفیلد بدون حضور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/31352" target="_blank">📅 08:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31351">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8zj70A_6nWf_2HyZzCpOuwZv6ZJhYJWOln2gK_Q1Y8UgqWalr_ytOHCHNihqQVQjNipaQqgkD7Vj6VyX-VxhC6Sw5grfmuaSPzLSiNgbhROI3_A69zp4JHbTpNsMYxMXdSLyWBGBJrpprbVwv3ICC2dU3U0q9JnnehEsmtmyXL3ItvLMDmNMzSaBhMkCCdfLUV-IcewLEQf1QGO9jPI3Ru4bVVHk8OhphEK6vwWPexrWDfIqHJJM-0CQGrcCJG5Lm5ktB00btf4pBGWzwFWRsxczWcmJVuHkZShkyR5FjChT23AnElguMc7ZlnQmck1KClk3OA9a80f_GLvnsYD1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از برد خانگی بارسلونا و رئال مادرید تا دومین تساوی بایرنی‌ها در این فصل
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/31351" target="_blank">📅 08:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31350">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1KzKlBUCaWcLi_RqYRmB9V4ILL4lovaR_QtrULVOpjkcVtxfCYa6pX88b6zAx35VeaAEufl4LS0IM6Lrgk6Vh6VHAsh31jiqFScWVgxL29XPSD3On3imjaxGdGrNYnvungB1KLitCpV413nZCCDnRnsFIWgfp7363QoQoYpY8SsSPjMLViktOGdP3KLIsrGfRXM0wwLmHTY1_t1aZxsON939YScC2UzZiZ7Y5FCn42zztJ4vtNvRbSrJ7oYE_zVYjhbWaAJ6_CqLjzAdxpOZE3Zd65B6VBET095pQtk2fbPQAOLreS7l87E1L0Ho050OYX_NnOQVe2KqhRWNIvkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31350" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31349">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2B_LIbMtgiMIDdLM4DBOXWB4eJ3vrnYZX2yS7d0Eqh55ii08X7GlGnzZXlgEk9IFTBifLDGnFNUV1Cc4sMLlli24uvyMhBgJ4aEsoQFm5HMUyx73Ym-_ZMmrGRWsvp9uzjbkCeWwCp2mWZKIIwyGqP9UwETQzLO9-MKD1PWzqFCxejj_Zi9DCPMGsyySv371wOo8D-AOV9afFX10iyiE7L3xehc06SJLQKqJpz6wSE19bUZGrsfV4qtwN7XMdFde72zJsfT13zxaMuyfcPSupaMA1R6Wdw-__9ckvmEL2tvkL9-UpytJTQEyVnK8LIVQLTzGRaAy4avGDfcxfh2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ پیروزی سخت شاگردان مورینیو در برنابئو با تک گل دیومانده؛ اختلااف 6 امتیازی با صدر حفظ شد. وینیسیوس ممکنه به خاطر کشیدن موی بازیکن ویارئال دو جلسه محروم بشه و الکلاسیکو رو از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31349" target="_blank">📅 00:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31347">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEyp7TP50v1m6cikBHno_wvn-tChoYA21nxkQ1T9T63ebEYOpoT_IPP_ULmAIYinZNmvtOrb6_DoHbhlAb6NLi6D2eKr69CLUjNvWzIoWo5C14c3dylW4iHJznmqpQ3k16JDJe8UGdYU_MRHAp-djGEh9jjCXOpdFqYTltq9-l61BFzn4kU9dSQJxsbzqsyWmnOdQNVsQ0vFcOUemjNoY3QEDi4-JNCpw8cvvyejUdcoj54gtQ9JdGxWiHtSv6VYlpJdX9LiVIzTGBZYcueu6TC0oy3H8hrctHPoa47klsvW7rfltQFN-njQPFyt7UQoNRUlrLh8iGlQjeI5f0AQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEW-F1teniccTQIalmSv8yC0vYyTis3LBV_MOst-veO1pp7pio5p5XUheLVywL-XadFOTxyPRZOFUtG9aeQc1h_0QVIuKQmfvRlwiJiLdqMQOCFmnD2loEPzxjymYmgOyhGuegsKrhxD6avALF6_3bDcCYqUrs42BfCtEUf32PePNsmiRgBUX2SSx_kYVnvB0xlLXDhidQDbXTCE5jKf1pJMWBMsTiZyt0y-vp5eGMmCk_sxhAnWYzHaxD77egoM7X7hC4sO7tf3S-UZ572TMI9_RXfRUkdD9ck45z9MW2g5T-4gHBwE8GdEqlkIUQi8-7nbQ-uEaG8kphIjbQeThQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31347" target="_blank">📅 00:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31346">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJToj18fGQb4bfg0DGxxgu__gT-8PvH-fcqi3GRD8s5DGEkc7u2pm9QlTWHK-KRKg-kXKJvLHe1xjIv-_qe8R7jFYGDPGgd1gfnCn58sznErk065JyUNCCSmb5gXZWg30BbIXQ5m5ShczZVqnQADDIisn207eL7CaNbKDrGMmXDRHi-5gcF9kgPv0KyXsOF-dIqoADQZQT0NPI86sdJCVjVdVJARkyfq0IQLmYaej3qvZC0r91d_y9YbE4fmFgMtXAqtuWqmllc2Of-QwM6gGO4KvgQXFIf-Mqi4dFtP6fihMUkzL1fktOVJup0POdJjohNoQcfnXuh8Uj7CmXz58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31346" target="_blank">📅 00:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31345">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izOxtscBt7p7GGaq1kQEEZWnLhELm_JcTjNiJ-G-CJ7rBfdOgFuBAnPbDrx3m86v3KVsCL5ZzErpuTFGFYekLm8OSfT6id84hl_L7M4Ccg0NW496wdeIcwYDLZfrxweJLpaStNDC06qMMnJQwBH-FB4720UItPy7TuD5LCMuTnxOFM7wy1MX2wQTD4uJYhofdoAzpBcDvlp_NMbUyCdUjmzhRYkgXUrhj9Hz4inT61SfRY5LhmJepuDGG1gABaAhxT8v4RZKp9YQv6IOEUEWcR0nPNnWNpgoWWAQqlum0n-W6DXQtsyplyDyNDiAPFpJO7Km2cMO5BuPqjIMouVtIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31345" target="_blank">📅 00:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31344">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN89HUu3DMVERX9P80G9Ztl6vEn7ju6PVih2GKz3KT_5xDudX0yYWvft2vnVNL4qFR_kW0hzkFcesD8eUNV4XFtgOWaC2CHvlHAy8DMLaUZc_VKkJRhdWDWySrTinp436rHv_F91RsqQZl9qu9IiI_6kTCzWVZjVu2mM0aWBFdKMYvnR3njTXE1YQKZ-xK4ORpbrtenVPfYkLxOz3OO0JHCX4OZ1otagcmrTYP5HzMjTTrcRf530OQRpYGBU0CgsnhXwm11eMElK81mctH4e9eoqShGtIH5_RO1r4vU-MTMDP9wU0hSIVU2IInrxrkpgdHsqXgYG00fX9eC-BIu9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31344" target="_blank">📅 23:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31343">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31343" target="_blank">📅 23:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31342">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcrZf7IqLkAtHHNQ2fGlG1dkAfBrhydiEeWZArS1QYAeC2acE1KlyisjWpeax_6jj84g8RCFxyk8bgPncoTacqwWfrmhBi7X6A2mVbe8gZbfNlQ6cm5e4mZUgtLJVVTS_J3075A2X-x6mz2AvQwxkNwoCYz0p05RxFdSkLl2zEv8zsXPecTcyMCDvcMlHZ5zo-AG_BjDIYWqSIIUSEfb6kEUsxIIS70DrZtIuv-4UcwdgDDS0vhNJdKhmJyA1EccX2B8z1QAlMO_2TRaa2UthqpQUmYW6VfUWgJeyR1LKKX8d76gCHtxjYCz4jBBKpRUqeEHq3I4lYT0CGR9var1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31342" target="_blank">📅 22:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31341">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ece2dc9b.mp4?token=AGeG7c83AHa4hCjv594FIeXhx2YlPW37dPwuditpCeA_yFjpi5VOQXZAAJc_fXXAFFVOZu5WlbaISChFgdOFatOBUfL3m_76Z7EUHwbofJ5JOIII59l5HPj3UAuth2WZZQuTSD2gt8x1fVXydEV7h54JYia6uZAYIWFau8cf1Tn1WX0wcsTeJxlLTqpZ3haqg0HBEQp__FqwK128uMQ7ogUyA7UwMe8q75yUG3tANKBwDa4aHmfcmeX4DsIXeuln49Btxpk_oHVTxMx3YCCsnOW4KpRBXRpC5fosX2dVRJBUGCaP0ybhR8gRj8YD42be-_Hvsp989-7_rZ5ZNwESBALu_hTf-UJxsDbUJCJPrhOPV2L6ED8YPBzOhpVlPLHqN7aOy8NXiZqiCyRSfyPHSC3TksQ6s98B2oTctLL8v6Zdmz4dVrJHA7YY_h-hgJmPzZThtW_u7Gq9MbkZn22Jgr83yKgvwakit4wYrg4BEBt-BJYQaPxa41qUyQWYx57SHKTn5FGALu4WwBovLj9H3n8CI5kq6gdqm3AUz1I2uCAWb1VKYDiNz-y9X6fIWel16d5T341syGlnlA6BuYEoz4MbKP8yGn7a9HyeVRcVjoB4k-JDqV2jI1CFyhF5alvCkioou4uMh4Yl9IiTilogpdRKE5p5aqu837p5QJpw2Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ece2dc9b.mp4?token=AGeG7c83AHa4hCjv594FIeXhx2YlPW37dPwuditpCeA_yFjpi5VOQXZAAJc_fXXAFFVOZu5WlbaISChFgdOFatOBUfL3m_76Z7EUHwbofJ5JOIII59l5HPj3UAuth2WZZQuTSD2gt8x1fVXydEV7h54JYia6uZAYIWFau8cf1Tn1WX0wcsTeJxlLTqpZ3haqg0HBEQp__FqwK128uMQ7ogUyA7UwMe8q75yUG3tANKBwDa4aHmfcmeX4DsIXeuln49Btxpk_oHVTxMx3YCCsnOW4KpRBXRpC5fosX2dVRJBUGCaP0ybhR8gRj8YD42be-_Hvsp989-7_rZ5ZNwESBALu_hTf-UJxsDbUJCJPrhOPV2L6ED8YPBzOhpVlPLHqN7aOy8NXiZqiCyRSfyPHSC3TksQ6s98B2oTctLL8v6Zdmz4dVrJHA7YY_h-hgJmPzZThtW_u7Gq9MbkZn22Jgr83yKgvwakit4wYrg4BEBt-BJYQaPxa41qUyQWYx57SHKTn5FGALu4WwBovLj9H3n8CI5kq6gdqm3AUz1I2uCAWb1VKYDiNz-y9X6fIWel16d5T341syGlnlA6BuYEoz4MbKP8yGn7a9HyeVRcVjoB4k-JDqV2jI1CFyhF5alvCkioou4uMh4Yl9IiTilogpdRKE5p5aqu837p5QJpw2Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31341" target="_blank">📅 22:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31340">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31340" target="_blank">📅 22:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31338">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q385B7eCReLr8hhsLpGHRkfPsUFP1Giy23NBPc8Qz14LvRWcDCgTxfTcJ-s_XcYGkYdLj33qXVGTPf7n4sBRR-n4gvvJIOQ3tOTDS6cE3emLS7eBuYoKNih3VxQQinOd6Xp-NLqdjQn1jgb6SjvQHT0HEDyzBOL50uxMEj6m4GTDVO56-4WcVb5d-QF7L9t6ZNbvluqCxlb9L1kGqm8crPXQYlaKxUlrOWGw0pMTEnYjZVWnOzeCSevcJnmhA5V2HerXgq8aFiDmgHuexmM8JO-uyoYvMiSS44YFXlAf-oxyTBjTZQuQI8jl0Stc1rT3ImyHvdd2hl7Tu3R8p3fCMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AyXO2lWyC9GIV9f2iHrnR9aWtMb_ZCUZ-eFavh8vfDMJc9SHZmDE1gGdBvHJSf906MK2ytHq6y2mFiWU_oLQu0xswIVnTxl1bJQi2RzEAJdE8mtz3d5Wtzn2WGzF97aO0pxN5o8vZb72mOlCfYdUi3dSrCEfObf2zhpnvtnr4YEMWdrt24PmiOANhNwr0Ne6sb0yPXZ4My4p483LhmJJhkvLpfU2YY3piXp3_UFXbhPm5Lg0mrEewArFkF3FMATL7rRYvgJVSiYVAx3tAjbPSZNEh6CIw1pTO4iBGTd-Rhimlhd-6AkVfhn7LVd-vmjI3v9umlHy4qKmwAWEkur6UA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امشب مقابل ختافه؛ ساعت 20:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31338" target="_blank">📅 22:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31334">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnakVsX54f5CgpU4ScA33ZjJmOI1ZL7e9RX1YqjLikPNfb67HCZvpIqg06BwwGF9YTmYVNmdJbWgX6pgwKT6sjQMIPsjWO7DcEhhS2ytqtqbF5Z83-LyAjTg9JhgyXdKUVfZMiux84Pwcm5aTvhC9uDMD2B8Lz3z8aOLxsl4iXVY-_SSUNkcUQh6lBLn65DUVXh7XLfgmF7XLt6qXlMVBJp82Y_1sCgqbkIbO22lwIZMWA2OLh4Gv5J67s98UFhNaaM-tY9C0vwCdqaZ4atpgE7ahQyXbVEghU4DXV_0PMvPFkGqDCNNkZB_Ops1bmKCTFy59ElOoqqZpMBby73lLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwUeXD36pCaJZD29SiBmghppFKKQqJ11EFJhDTvyFYCoFffjcmZaEMc9YT5up0gDXzWXnn58YjMRbOez8cxhbLXdco7T_reo_gYgHt-NkhCA_eNZ3if36psSgzGWKllFOYUnAjn6LKz9QgbHxn9IWyRhqVw6xnVnNMacdFmIBwqykJHVGHEYqP3-BajeYiiXUsnXs5GHMrYdrC7xiWMPBZHqt_sqOWNroVa0lNpvgdKqaJmmr41vNDZ8jg8c6yf5rwx_oXAai7t8g6iNpILRqbpTNoC6YTPj3qUej4c8JHeVus5xtBxerXqsRrBHLMminDs7FqeFTT-jJ79qtUvhgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31334" target="_blank">📅 21:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31333">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoWu7jUaEOmIOZAUNw1Z7PM01kyT9fbmHpKXKnAN4LI543JRNO3v77LH2v6g2n7QojWCGIV_y64NelElZVZQD53N8hxcVrE1D8A1-tUy6sDN6jTFB6dm1hNNJh_XFx1kmtaFDLPZgwcZVPBJPKpAxquuB279wDwYN_qY4ho_tkE4W49sAS8w-YYje2kdcjcDKvyqoD6mvGzgj74-Bnx99vZjp3YbU-03IvAFUnCxUkKdagv7e1PsljgnbTOUXz9gkZwVGtv28CpWX_UVCXa_Ks0sIzhJKKP3q8cuHS28ASHKsv3rQ9F_TV7Xih-k7TxrtZjtxx4plG30QcO7_mWl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسول‌خطیبی‌سومین‌سرمربی اخراجی فصل جدید؛ بعدِ شکست‌سنگین فجر مقابل سپاهان مدیران این باشگاه با رسول خطیبی قطع همکاری کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31333" target="_blank">📅 21:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31332">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APe0LFjIUp8G9C-yvS0Pg-Z_AUQzW1yC4ate5w_ufcc_O6BX3LSjOMKrv5unPcvIZN-hGJm6hXjKwnEYyo4L2FAlAWswTGhj2IDaMHbsIbqucqamFYUD5_EGCnBBO6Xy5PcYu0Mq9T8KiPtjzDO0-rhwv0rTpSNdVQg_5kiUIIGDA7vVlTKZK4LR6Dsv9Alnc03qWPyaQ_Fm77AOm5d3T4cOWticqZ1LL7aQZNMp3MQgz5sVg402beuO-VvoJScbfh0neqvSurjz65wM_ofVwrNfrzaNM4HCO2xa7d2N3Ue957Gzfa9YJLukvGzJI9EdK-dIAdWklg_L14-XWDQ9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31332" target="_blank">📅 21:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31331">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd28a51cb.mp4?token=TLooItTLnYM7_mPrkPtf50Mz6Miy7ZBvEkDq5SROwaALIrFLJoljoq9YJG70aaOng3CQ8xSaugsoN1je3s6cKQPv-NIBX5C4THWLjyYXTWhMFWUm_LatyTJP_8OJ8Co-Uhhn5X0wHtclCJjleMSsFR8QrCium3Xw0lQJhhQBFbCKTkcLsNj9kxYGCNBahNavtsfbFlDeRtF4IaTU-D_rJ1X0cn-H-IX_lErfjEDflzL8O28VbwriNOQU9teY_9ZtplC441QMxj44i1EwsxIG0_fAkMDs01b5SBUvrrDzq0bavfZ-Uk-0PdadEJ9meJdyGIhv5C2VDdM_5zg8cEMOqTFpmugXS6hPMalnZnSVszUzerwrmds52_H2bSE9b9ruu3wuu4pWzFafe8Q6ECEJrNCmwtK9LMeO00FP_E4J7nm6AEzks5q3h28BhyG1bNGqMv_2nXkpFCGRBI93fUx08jrlJNjtz7fBRUVfEY2acD6xeOuKszz8jPmX2qMo3uP_6_ppnGOHGb5SRdiqz98X5mUd4x3ppCyfUQ573WB01bXXojov7QL0jQqusfJLT0Dyw65WAFvyA6jg-Z29XhIjkm6s1dTQeGDNM8xiOxjlRUl5S0_aLB3v269yb_TTjYgY8Fo7VnaSjFgTthBlTqiJB6OjvdQwe-ENhEkBYmo2D_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd28a51cb.mp4?token=TLooItTLnYM7_mPrkPtf50Mz6Miy7ZBvEkDq5SROwaALIrFLJoljoq9YJG70aaOng3CQ8xSaugsoN1je3s6cKQPv-NIBX5C4THWLjyYXTWhMFWUm_LatyTJP_8OJ8Co-Uhhn5X0wHtclCJjleMSsFR8QrCium3Xw0lQJhhQBFbCKTkcLsNj9kxYGCNBahNavtsfbFlDeRtF4IaTU-D_rJ1X0cn-H-IX_lErfjEDflzL8O28VbwriNOQU9teY_9ZtplC441QMxj44i1EwsxIG0_fAkMDs01b5SBUvrrDzq0bavfZ-Uk-0PdadEJ9meJdyGIhv5C2VDdM_5zg8cEMOqTFpmugXS6hPMalnZnSVszUzerwrmds52_H2bSE9b9ruu3wuu4pWzFafe8Q6ECEJrNCmwtK9LMeO00FP_E4J7nm6AEzks5q3h28BhyG1bNGqMv_2nXkpFCGRBI93fUx08jrlJNjtz7fBRUVfEY2acD6xeOuKszz8jPmX2qMo3uP_6_ppnGOHGb5SRdiqz98X5mUd4x3ppCyfUQ573WB01bXXojov7QL0jQqusfJLT0Dyw65WAFvyA6jg-Z29XhIjkm6s1dTQeGDNM8xiOxjlRUl5S0_aLB3v269yb_TTjYgY8Fo7VnaSjFgTthBlTqiJB6OjvdQwe-ENhEkBYmo2D_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت مؤدب‌ترین و باشخصیت ترین مرد تاریخ فوتبال ایران ازسفر۱۸ساعته کاروان تراکتور از تبریز به عمان به دلیل محاصره هوایی ایران: پنج بار فقط سگ ما رو گشته. اینجا هم فک کنم صف روغنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31331" target="_blank">📅 21:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31330">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiESbK-pnhGqoNnZ2INY6UTri5YLNGSMpC1Z04PlaeKITaZULJubp9g43gLJO5jO0KIoUh0cUrHxqBJaMeMhJEJrK3MvQyKQInbjaPLdMCUZU2t2aNbnF88syguEe7X6DzTiOz8GZl07d6n-ejp56NMpZf7OvwMpx0-gqn8FAMSLE32E6hOKD0SHt6204P2ZWzosYnsztWOJc4PpzBAxXHQIK8BLe9lS9BFyNLL-rccCH3yWBnG3FeTRpjcWmHbpkPKZPfW13PmtUkeFh9SUFpmZLnUIyktnzy4bfjPXyiEvnb-VsVd9O4JqKDa3ayhE14S8AfRLglwq_E_UUIJHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فدراسیون‌فوتبال‌پرتغال موقتا کریس رونالدو رو بابت ترک اردوی تیم ملی این کشور محروم کرده. گفتنی‌ست که کریس رونالدو بین یک الی شش ماه از همراهی تیم ملی فوتبال پرتغال محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31330" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31328">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHRtYxq1o44gWiiM5qX9PcaaY46z3zBBX4uLMeFGc5Tbd1VnriQhiRGU-Vc34WjodMVdtW98CRt_bhOxROu_ad18ASmhytZNSpxcnhgFAEU0dh0JNyZK2eukmZlSHvPLLzscFW8BjQXmIZvxBmOSDEwTeoXssuDqrkIcWQWs4lrMbQevn2gKZm_ODtE6AtvaxcxuurOcUQj5tZJJyvJXioRp3V1_UD3hf8B5x9pMd5EiKqJ8XVLIfmNWeqXxci19T0TMuhyKndvie500LSeS1GmeHeLtKdmQMtDTZ2rF8tyzbFAwFujecOlj4Rc9aV4gqDUZXFHswlAUR-tMmDg0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgylKVGbAkvqjbd1alGsZ_ATuaTaS7_3Jxxaf1YgocYgXtRDMI-14QDn6h3y06Ys3QYNSh_3qAWlMqwGBWf5CrLpr4iWRY9ODYCxdKK83LmNxHhzmUAhpmMfcHbwBYG0Hn_luSeWJYRHRWs-pmxq-nUiCoMRvzZ4NdIxvXjVoEDzQ5R4aehRHkgmONt53Ag25H7DDp4V9hkvuQnrTBE7p5Xa5BHF710xjMvbPdQ7YsYzY-9Ltb_EQi3IKnGytKLj-VgA6zFdi1MzZtcffdE-UwVvhQwM6d5Q0qsq6OsCs2SG6pM6keEh3U2fZQtidugmldAa7VbgPz2vlDPVXW8oyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سیلی دوم در انتظار مهاجم سابق پرسپولیس؛ درنیمه اول دوم بازی امروز با شمس آذر رضا شکاری به این شکل پنالتی خود را بیرون زد تا در پایان بازی پذیرای یک چک آبدار از سوی ساکت الهامی باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31328" target="_blank">📅 19:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31327">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31327" target="_blank">📅 19:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31326">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmxAEBr4vPJeAVKLaWLwUhq1mTiYDcgjgiHENzj_wAZiUE1GTcGtnUUVeRIktBMnwO0F0_bMvhWVqY0I7Z7rROz-AlPtMi42erL4UDvICRbYdcfDurS-cmA_EkRWLSYdDTSZb5jZFL4VC4F2j2PdpQzym6n-4Y5AC7MJ_lycVmxCqK5z682sabZOfZ_AiX4243KLQvxVY2H9MBsTeXZUkAZPRGbSXYc0skTFPGphwcUiH9yYhkv5QO2nQPB43KYnKAUc3LXQfUpo8gaOPtVxv-QbztY4Q9bc5cb_LvVjmxmPcxlx3SwopCijm_QoxVI2_pMLjN_9dOBt_sGUem_1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلهائر زننده‌سریع‌ترین گل تاریخ بوندسلیگا؛ گل ثانیه ۸ رابین فلهائر به بایرن مونیخ با عبور از رکورد کوین فولاند، تبدیل به سریع‌ترین گل تاریخ مسابقات شد. فلهائر، ثانیه ۸، فولاند ثانیه ۹؛  هر دو گل سریع تاریخ، مقابل بایرن و مانوئل نویر به ثمر رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31326" target="_blank">📅 19:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31325">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6tq6r8HDnD1SfSuYAOX_nAosZaeGLsdDhgHfJqnMd3vh4gA1td5d51ieL276W0heIMSMN0wKDlvQf6QWNp8f5KHhiiozt1nn3YyJECbnLE6XpN80lYqxkCR0q9uItWzoPmAZNKgRKdzro5s0jW_c5cGEOwHHF8jXigZE8U5eZo2_3L_rMf2Rk2l65uvCvR5-9cb3AzgriIaGRr9sbmmWwlW0pWisjurdebT5kCYvfKTPJEJp0j7R5zhjsIQgy3qwpwAYNEQLh_8KK2RF7fPY1RDNs4dRcLEit5JP7LESVd6XmDzRHTTQEoBl4hmbroONX9e3di4EZmW-hflN-ysMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31325" target="_blank">📅 19:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31324">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_Vy0Kqu5M4iu1VoUJsGaOgW6IPAUTIE24EiqEdGSJU-a-3_8BsuZxvu3VJpRRLQFWTUmr1EREC2fp6uuCzDeWS6IhZno0K3MswR-pcV22bnRYf-ZwkxKwyUwkhl0VhiUmzsc437glsyfFg3d_Xzew6zsp4sSPS9bwytHzqkt8dsSzFReCBXXEGaKp_inmMX1Lk0R-htGNAC9jM7-R2o_iEEjuUWtUjKsr0J7KOET5DkYHyIC4f_gGnVz0t_u3PNrpzi9m3cciFvwX6pnRLuvVR-U2bj7cK5tnRXPC3WMrCWqLvXvMvrVUrplDuWd7kbMqE7h_OZzZZcgD1AcGvIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31324" target="_blank">📅 18:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31323">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5837e5cdb.mp4?token=iC8-J0wI9YuqcYoAXezTkWIzvm_nCl2Bjpr-7M5x9duNqHOo9FPzEUYfOqHa2hdXzyBiadmM2iH-D8PPIS4-GulsD9MOfjeLd8qVM6sWF0JsS-b6G26_9zSMEVerJX4K7Jnr6ahmGfz0l2WjGOVAJ0E6ENJtza1K9aVmmw4wlRhOm0K_bMpafpSIGkhY5Na9dYnn26ixj7otF8vE6B-o3FPTSQv8nfULT5D_E6XG2xGIO7uo0XLXYy8DfV0bx-3tlLbPtTSh6Tp9QLsZbx3-S6B1jz86v06qGgLaLcMMTR5SXUvG7mvJVG9gfsLqBKahhZGy_e0hv9Xh1qV3_zp0rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5837e5cdb.mp4?token=iC8-J0wI9YuqcYoAXezTkWIzvm_nCl2Bjpr-7M5x9duNqHOo9FPzEUYfOqHa2hdXzyBiadmM2iH-D8PPIS4-GulsD9MOfjeLd8qVM6sWF0JsS-b6G26_9zSMEVerJX4K7Jnr6ahmGfz0l2WjGOVAJ0E6ENJtza1K9aVmmw4wlRhOm0K_bMpafpSIGkhY5Na9dYnn26ixj7otF8vE6B-o3FPTSQv8nfULT5D_E6XG2xGIO7uo0XLXYy8DfV0bx-3tlLbPtTSh6Tp9QLsZbx3-S6B1jz86v06qGgLaLcMMTR5SXUvG7mvJVG9gfsLqBKahhZGy_e0hv9Xh1qV3_zp0rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساکت‌الهامی‌سرمربی‌پیکان درپایان نیمه اول بازی باشمس‌آذر اینجوری رفت سمت حجت احمدی و یکی خوابوند زیرگوشش بابت اعتراض به کادرفنی حریف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/31323" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31322">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prNI5DVHldP5VZUhyNSZk1Xu3o4pGY_OWeL_LTTn-TsNZreeHCgokO7r4E86Y4K579vedAEOyaqotnlumdANDc0jmU_vYC8kYDyPjl-IqWSCCRkEAKsaXDSl9cPvO-8AecwA09oGV03y7GUa_Xndx_ifXvMN2ow2d3856he7JTR9F7ySNp4UoQV3_jN1FJbe89nyihNjoIWNE8hcf0asTW_rmkKbIv_vIVAQ8Dr3reKzeEJ9gn6bQtHUbyQ4_ftJrzKXG-1BU37_5JQKCEaMFznTLugsxtekMh0v3lgxTbBYdmMV-PJx-4mKal9PK57Xk0lv9gdvlGLxQyVlRKXzYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31322" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31320">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW7KuERxfXJ_N5HnA5LurGp3VkPQ9zlLFIVmZZm8wDrv-86kNV3uA2RZK9iL6HbHuGb_QVE6_X4Jf4YTehG3x_3wZ_Q55EZ02RAzo_N3Qn-7S5IIFVRBcAKVMECS2GvhTpqx5w-mxPBT5_wRZfTIeqTFsSlYoNul_u8AY1RKCiZ0-SyUZSiYFeT5JIkXeEJm3ul7lffQEA3jXLpeqsx3OKiV4yFoPA9U45J3PcF2QPgWzQN8JN-SdCGBTGHU0QARCmS4w89uutDL-j3Hqemm_9-zWjX9uqgqGubyUZtcswUKVXOaalDMGbWvG5gjwtYCGXMy2PcOqEcrWokxpThKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال:
به‌مامانم‌گفتم تو هرمحله‌ای که دوست داره براش‌خونه‌میخرم و اینکارو انجام دادم، قبلا تو خونمون آشپزخانه و اتاق خواب یه جا بودن و زندگی سختی داشتیم، ولی الان خیلی خوشحالم که برادرم اون زندگی‌مرفهی روداره که من آرزوشو داشتم.
تو زندگیم یه ملکه دارم و اونم مادرمه
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/31320" target="_blank">📅 18:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31319">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17a54f38df.mp4?token=elaHN6_TIZzePye6qVxA4KRrl_8zwihaBwUo6vbfBqBbM6sCktWMr_bx6QN3VvZUdmfoJO9iFhHw9YrqnWu4yAqc128tmn-b6YZxHYOVHcp05r6Nf4_AOikejjFRpWACeggKRaJ76VuS8DqnMaAosP8Tplw9e5ZTnc5adau1bsOAiX01heDehHXmOTDDZs_peMUG7IbWycb_Lgt1jj7LhV-d2W2pQA6aikc4mXtYe0wTpV5Hr8SQxjlq2xBN4Y28IsRNW-AjDojdeIUgHaMgsNCjtTTQeUYn9Jd8ffu_Nl5_R9ufMXuczZuf3Dx1RbWuJMZfNz6Vup0hI4Uk2oqQQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17a54f38df.mp4?token=elaHN6_TIZzePye6qVxA4KRrl_8zwihaBwUo6vbfBqBbM6sCktWMr_bx6QN3VvZUdmfoJO9iFhHw9YrqnWu4yAqc128tmn-b6YZxHYOVHcp05r6Nf4_AOikejjFRpWACeggKRaJ76VuS8DqnMaAosP8Tplw9e5ZTnc5adau1bsOAiX01heDehHXmOTDDZs_peMUG7IbWycb_Lgt1jj7LhV-d2W2pQA6aikc4mXtYe0wTpV5Hr8SQxjlq2xBN4Y28IsRNW-AjDojdeIUgHaMgsNCjtTTQeUYn9Jd8ffu_Nl5_R9ufMXuczZuf3Dx1RbWuJMZfNz6Vup0hI4Uk2oqQQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
واکنش‌ابوطالب‌حسینی به صحبت‌های اخیر ساکت الهامی سرمربی سابق نساجی که گفته بود در زمان حضور دراین‌تیم در رقابت‌های لیگ برتر حدود 10 روز در زندان‌های ساری تمرین میکردند.
🤯
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31319" target="_blank">📅 18:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31318">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e05ef0c40.mp4?token=aktKZypw1r5N67dUr9LPCBBlXkJy07eHCZVCkNlT4zXZpNSPlk4kJqAOrKOd61OplDfA-XnC59lCm9YvsXrXOn_vjOKthYK3vds4PkgIw0KYW-bDamI8fcG5l739ePgbM5ksftdCsxI3ulD4pcqZTFhIudQy8RCJLrkmafG5OozqfZNVz1Nh6KIS3qySyJO7cbtwelYtFBm19FZ60GGKTygT9faxnrSdKHfH_zskFVYjUvbo02qZ_QWKtVLP84R3cUU8peWrNER9towQ9YJn1vBiXwEtPp3ekIN7_OPu8F0Jm_r4VmfGddqe5LJozBRjy38XRAMzj_t3qPM5wp1G7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e05ef0c40.mp4?token=aktKZypw1r5N67dUr9LPCBBlXkJy07eHCZVCkNlT4zXZpNSPlk4kJqAOrKOd61OplDfA-XnC59lCm9YvsXrXOn_vjOKthYK3vds4PkgIw0KYW-bDamI8fcG5l739ePgbM5ksftdCsxI3ulD4pcqZTFhIudQy8RCJLrkmafG5OozqfZNVz1Nh6KIS3qySyJO7cbtwelYtFBm19FZ60GGKTygT9faxnrSdKHfH_zskFVYjUvbo02qZ_QWKtVLP84R3cUU8peWrNER9towQ9YJn1vBiXwEtPp3ekIN7_OPu8F0Jm_r4VmfGddqe5LJozBRjy38XRAMzj_t3qPM5wp1G7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31318" target="_blank">📅 17:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31317">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IshyaaDqIuMqEDCAoexvdaAdab11Dk6CmKMeb_pjV8AYezwbAZE5FGM74Ja_Y0B5Exp2P2L_MVBOAvUKTW3QLRsedBD-Yu6K0jEVTmB0NbunplKDCtWErrTHLq14DJYG_J8s0ixZfS2JqtO_atuPfPvjk4GCCQ7r_xOi6jxCXMw_TNvNeY5MVpqbvGLhhLbdLgM-wUIiv1rnxYXV8SoaI17AcF7r1YmmyAYuZjbb8d1VLSNnhNaNnkKj8eAB4EruaqRlsXFyqeUAPypSMmeeiaPa8oY5HKzIhm7SOkdKWBKJkvfn7O01XCMnXrKOZWaHpdEw0_HQjT6qJF207cuxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31317" target="_blank">📅 17:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31316">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrKOmqiZ1HLG2zuttMi1SquPJWB8e0Br4cZbY_26xlLJGT8KtPcFaELre4ekL1TMjs4iMXKXaY3morBjyco-U7u8QK9FPn19KE69ut2O4Rf3laZEYpFl1qj2K6WDlV7dwJUJh4Ceq4bSTHglJ0TTnYyr8uwvdaq4BYqZdRATdhmoEHsrSQFfjxby-0WrtHhK-xX4VzNsxp-MH1enLe_XXuou7LIe5LjpRmRVvNtHOM7_tq7ZMsd2fFWgiW2t3Cs_Ni8-euX_Oy5HlOgR-m-Vbozt84QB0dMF_gvS9LfaWmin7N-Zq2MSfiNshN62k-DYNeNUrtl1VBHpKwHsIvP6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31316" target="_blank">📅 17:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31315">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31315" target="_blank">📅 17:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31314">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxZ5aAtJEA_rkDXTFllrFGokyS664k0T9s_BaRdhAZ7DUGF_7UUnL2DYfXVLSFxoinXoZnwWO8IUj2jvgL-0Fi7yuEJPGgUNpD3grvOjbWcxvEKhi5HJhbqjr2blDBy9GgOxXbjKUMUIICFduOdi18d1E0DlL_bmRiUTi4pfA9xKEpZQrfALksjJw6N4zVW18Q14TbMqg3Frmrd5BTDfjdDpdM5qDJS9lcQgoVTnQe_6q_h87quRgp55W1hetmo1rz009V32Upbm_TZCJyXkLGR166FmU_h9sb61D2eQ3R5aIiSpniLdwsqCiSioqDXflJJBL05LJDG0v2xqlOZP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31314" target="_blank">📅 15:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31313">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl-qfDX8iLhclQhpaN3PU0PyT8LSgLdsaCFGQbR8T2im33FS0F0Rf2Tkb-M-su8kZa3owo_iy8H4l-BZNqzadbJiw5cI0PkaZoBes-bV_Tb-yj5A1L4n3y50Ofh3JA866FaStqjFHxW5OhvArlJ9rP63x9DXE9qmzhdtUf4c48j_04cQNfhteiwVBggOPgWjLzNqmIeefy06C5D7ShazP9gA2S9RZCgylV9HZCXZH28xHVenHm2dGXvYa6DZAVAd6G_o6WVmXDtDNwuRuYtqo9RTRoPvaEvUU-MB-3GBDBo7nb9swOENEUHXumDhiD7sxeWZ7o_hFZJTAalXfKiGfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31313" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31312">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5r3fZgBUHsFvYeF4Y4pajd8hgnT8LpZAA7VmQ85ElSpBWKy-wA-eaKC_Y1gvcFMRGjCeH3y75qY4t446UFRq89S-rl9bOtOlb_P-7J8XFcX-AdxVvihmHMPBJsdCxJ2kkwzs2d7da95azzt_KCJErirgZDym9h8OG-VIrMuYH6-T8hhDdliqju2Z77MSppfiDQTcmGSNkhGNzl7IcXxzQYdEaJzq7oLAOmcPSsD3lcMhyvyoKMI0bQUIddggswlcmiPljabiXB1WhjWCiZGzetOiEUIJrByhtw2tqEe2EKojzZdVzCxprsg5SAOajUDGoA0_qHXFtQztfUl-Uro9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه‌های پرشیانا؛ علیرضا بیرانوند ساعتی‌دیگر باحضور درسازمان لیگ قراردادش رو با باشگاه تراکتور فسخ خواهد کرد و راهی سربازی خواهد شد. او از اول آبان سربازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31312" target="_blank">📅 15:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31311">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJiV-bBcmcJ5q5hhPZtzS1TVu4ZX6IRatrsC-XwyMp6dFe2d3SymTx_SwpVp8eF4GTekZOicSsgq_sG0iZOM0tD2HU7L2cNV3g9hXjPYz_ioYXEsgnwlMV43eJV8Yz2583SYZ5qvK3fFx74FIElAIR_USbVLAVJLJEoOVIyAxbcFRJvhFlkHyQq8oLKTUtsaFEG5NDRzTZlgWqvq8vDrH6-AXkpG5Fc6ZTQcC6p8nbO6kyxqZuMtgc02L3QSXjp-HRMT2bCgogfzJZXTzC_at3-NeUGgith0qAw51BhnwaFS6i5Gxl3_uP8JYPS5O5O4lIbu5-6_jLL4qGlU_ICpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام‌باشگاه چلسی؛
کول پالمر فوق ستاره انگلیسی آبی‌ها قراردادش روتاسال 2034 با این تیم تمدید کرد. یکی از دلایلی که پالمر در چلسی موندنی شد علاقه شدید دوست دخترش به چلسیه. پالمر از منچستریونایتد نیز آفر رسمی دریافت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31311" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqmksOtNlarbt3iYMVmr9IGywzWiGtVIvBm1mZd1MwnzWQdGipI9YsOVAHFG26aQvJaSHn9zGfZbdTCSH1O7zECmUE_58Cvl8hCjS2MOMFX7HU1pljoJGF9xt-WG1fxt0DmfpsfSd1ueCNPiozGtjTjRnkxg4NA6hOAqKttvEMh7XjRtJR115PVyiX9N1DQQQHIMGsm7XWA4k_VIYXc5Ol80eDf-N6stD06vT1RmlDrSwqdNU4WKimQGI-6ST7VSY9G2C2phrbctf6wJYNPGOcE8UC7d0fmMI9Cut9QYNXpc1M5esBOOC1tKzCDMWbr9xnkx_aDPT-_QgGeUlHlwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ سرمربیان تیم‌های لیگ برتر در فصل بیست و ششم؛ محمد نوری دومین اخراجی فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31310" target="_blank">📅 14:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31309">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMD_ymA6bGyQU2zNXe4FLs2gDCNME3JrXhVN6eU8LWvG-VWzXWjBtbI51Ww2c92LdRkyWEItu-_tAoXvwxVSFv8wX69jXhgG3299OnTySNNFMZT04KFCWYOWWpLIecV2FFUlVrl6IakqzHzcJiKNYbVmK_Is3gcwXEYWGRmwcm16s2AI594BsEaiJ6xk7-dhRbWzsiBwEfFygp3Hccj_JmgfiCggod-jtkBCj0KmllIbftODC5EXc8joHdVcHyCOUyP51FMv03vfGxhhT3uwTtjRdVVuP7n05IvFT7EhWQJMHTfsbCb-a3ACKz8cYvAJaVXjug3mZYBx7MNNEoTxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
گل‌ پلی‌استیشنی‌وتماشایی پاری‌سن ژرمن در بازی شب گذشته روی همکاری دیدنی عثمان دمبله و فران تورس دو بازیکن دیپورتی و سابق بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31309" target="_blank">📅 14:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31308">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYJqnuswR9dmqhpUfrA0k7LBxT0EeFyDV_dfa9bZ934wlrLUgnPjTbmfRAIhgMM7F1BWtvizT-q7gXq2yw5c6i4x4jZVEdBZE0HMKCeEiQyWdr8Mf_hQR1CtaOq_PIgEPGNs3RQWuhL99_RSOj5yL0IJ1fjyYO4PBwASDJm6zBdb36yxt5N7ND6EP0z7PqzEEXDbL4VDNzGaF7mOJqr5Yqn-gEAKnlfOpS5acoGxLhqksBuwtFNijeyfMC-UJs3qyhW-kqTSwyA6j-YNlKu8YShseZaj6w-6ZP_uNI18bIokFdOzcVrGAEwMO8-ozoMNZnS5wWTxWN_V2tABwoszzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31308" target="_blank">📅 14:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31307">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFMO3mb1UKSsdroERMcgmsyzjLQuBAcWPu6aEwQUnBjLVsTG81nUv0f3SJPNCyXFmQVT6lHUkJ_Af2zHuACF8E36JHPtUxiK4-K6kPAWHhX23qdfKYmkIWdc7tufYv-h9rpWNJ3_6DoDLtjPw4DdQTa648PXwubtiGraEz2tG5R5J0P-bE0utoO3WO1_3zVN6gw5IA22VyNmTDuZ3QVEJ2LHOjfHduBd1r3nGJ0vhgFD2at-ry5aZzdmDhPb_2rU-bsfh5N7I38b1aKGDvv6fCyW6KLEoaRwJCiLFn46lk6tL7UdKnmYXabmKR4bfX5pSOP_eEw0u9a4vMp4LVuVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31307" target="_blank">📅 13:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31305">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujLnH5-ov9dQI4IW-gfYH2V4A2kgTcvmCWTXwbeOLMJm0KAGncV8H6n5UBKKqBV9mzPx6TRa8REbEiX0ycA2e14_oLULGVcm45COkC9FapKOAO95uRLUJ0XcIucM_nPJV8a8k7Vw31C3dKX73YXvtD0tkbb3FVIlrbN1QQ1CtY3pxoU9wMZq4WfKGNudo7wQT4nL58_1gDgUHumYTBAotZBi02bv32J2VCKsUG1qti3oV_G_2VEX34Wfz9QHZxWKW5Q2aC_yqc9xbmTDG-4imIEgCHcQTg5kxdXVRIVpxMWcH7P3sVzv5ERSBaoQ5QPcTi5zJ0iVamdOmrZ2XA7Btw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u82UdgM57qNaiwe7FTuJ97ABGeFT9kXL92TKpf3qWtQdwPdkMjA9k-k4IU7hymTK9tLivZ-oe3XDrMRqySYhu3ChA6yoDIuxWkhLm5KC1sQJrdFi2LW7pP16SvGTn2RZEWEsJyhJZhQ8tQ4nZ5Ae-6FQBGB7yR_Olu1eQtWzw8r9QvQEI-wBK2CQYkYniUWsbuPgXJTM0secfKCHOqXBmsWeQfTre8p-2oImmB-01RBAtcrWDnwKRzs4LVAhIFG_64IT0fTZmFdqd0nO59HHZPxyjmB7x5DQwd4xFqPw1yNks6EIehtgk7_FDbB1O6XEyMO7fc7ZOhuY9e6CNni-wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31305" target="_blank">📅 12:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31304">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7a-zIqIb4azXLhdV91T8Q3_C8I-fY6bQNzZsok_jkc4clqQ2859a8DYBoz-TDKjTW1JPmCW_K6TGQ4XYAXNz4IT3PlMpacgaNeitjQVYrLU3xTkOCump6qUricxrtH5n0JIqYu46TCJ5PaE8nA_bqiM2vXsmPmzokipfTaKTh5EDd0O_yP7wMVQhh6ZbS4LJEDcgi4US_1ekbFkjL9DV_z_P--ReAdTG-kjjvg-6y7j1wj4msoMU3M1klFHbIUHHcZCeqW2f7wjP96uCkAzicSONKXh9tx4zu1dSg_FGPl9QxbKkdsUBJfkdE2b8kB0VlEiE0AJwMTVw0oQNCgg9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31304" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31303">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2K01edgYUcbFoEXqtfgcC2AQ38j0lHgcI6tj61XT4obt8d7AnTEJrFdgmcMYR42PkxGsK3Qy1QpOoS6tzBRTeP6eGZF_28VYIznuhpRTdHFZS1ZYZvhRtJ6PXLD-geFlPWTdnxgTjAm5MPOvj_DoIOY1d6cQeA-nRoROZ34X6lIifW0UojcQHR_Mt07EBShL1HRX5jwMMWgmnwJroCvuUMyY9gzNdX_Rh_Rg_u84rX83qxswGk3stUigNQzi7zDgTfYHVHPGXXY7CoqpuNoeUZWzaiZOSqz31GdF8SlR1UNjRzp7Eity-xq0dCx61J22s0eQCCs3fAM70itRIAaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گزارشگربازی‌دیشب‌النصرلحظه گلزنی کریس رونالدو: دردوبلات‌بخوره توفرق سر سرمربی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31303" target="_blank">📅 12:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31302">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ratB_wUNbOjoBDoNHnJ4xxExsTza10h6Qbgp69n6Fo7DGkCfw3zAMMunNDNQOTHb8I7tsTjK7lS1OwNHFYn0EsZ4ygqfBqnVdHC3MC-h8To_cKmh44yl3mkeM44IRKWLduF1FOmNSNQP4Tr_Q4J3qowepw1a4aCdC9KbSqqXm85IGSiKoVAt3VH3dktgx1R2rkvspTLQ6eiY9hnqCgSoO1ZLDsPcIGV-AZolyFJf-aINxR8KvM3kq2e_YNQfLIlYZzbCHT7zBvfk7ZVgmru59OMIR-aUM81HGJIGP84FaX6tDh67erOyeCbMEz55kmOlfZNv97hB5x5qe-3f7I5QAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگااام! مگه میشه؟! صدا و سیما: مرغداری ها برای افزایش وزن‌مرغ‌ها توی‌غذاشون تریاک میریزن، برای همینه اکثر مردم بعد مصرف مرغ بی حال میشن!  نمیدونم چرا حس میکنم هرروز از این چیزا میگن که مثلا مردم از گرونی مواد غذایی غر نزنند
🥸
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/31302" target="_blank">📅 11:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31301">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhTaPgnVxXLY7r3OxVTHEArjccen77zWQDVOPwhc-ebR49JV062C_DRZu2eFAeU5zkU6Hv_ROQxS7EAS4P_K8xf2k_aOps2bg4cDdlBrOTbjvtXDemrwlq9or42GYTACvGEmS09XLl-HOY7an6UWNKDofo5jkQqffmKH204qGIOIO6bcZfhVzpt5ywAdlckJdtUq0S6BgQQwOCp-2o5-fw8HiTM01ykQWTTElNUj282mqYIXMOgSSPPJnhrZabSuKuWWEsk7BEvZkxa9A-igj7VIJ3oBohYP_X2wnkrP_4DWi1wJnWH8WeUfywVLISIjamATtYaFRv8GTFC7iTYOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ایکاردی‌بالاخره از وندا جدا شد؛ درخواست واندا نارا برای دریافت 250 هزار یورو نفقه ماهانه رد شد.
‼️
ادعای‌واندا نارا مبنی براینکه اون «شغل خودشو فدای زندگی‌خانوادگیش‌کرده» ردشد.  مشخص شده که دلیل‌افزایش‌شهرت‌واندا نارا ازدواجش با ایکاردی بوده‌که توی‌ایتالیاخیلی معروف بوده. همچنین واندا باید دو سوم هزینه‌های دادگاه رو هم پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31301" target="_blank">📅 10:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31299">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=CQs8p6AsNefibF3OceHUdnOIV_rSBl6cIhIBqfxbmtoh6j49GoGx32_NNTlRpktPdKO46V6jxJPyUgboIZX2qazFU7vWXTkHUL8FVgIkMbifWvfH7RwUGAongqSZ3raptDTvAjFPsMx-5JqJ-Zq81StKC8K-8-1taPDebzvLLFYy-18ec3Mtn_-8bnjnq6UV39AQ0QwXPYNpzow_ltn2pyFlEK7sv2yoes1tz1FU2bUDAj9n9qBTGDwyUq3YI952rYgPc9-dWIUdOR7r0BwEq4YszHO7diaPWRY65lz5CsW--umoeBE0D8B4pDj8Vn3XST5Bs5Rd2gJ92IEXuTig-V6m-7kqxA16vMd89iHlNFi2dblFgTL7-BQdDZ6H5Vx90bKtMcyqCef_abFtm4wFLJLBalhMEvtWCIc_kYJrtO3lR0I2Ywk5EGwZcunag4M3fyiDhFg0e0XRDupmjAJg90_2XJUDrn7MBm38gHuRyF3xRBgAJ1wSURAIXKgOUSbho1oM3Y0Y4YlowXZO5fKuMcUBU3715RQKmWV44AtHiaqbkvat_0oaeWw-aefIxBAGiyb2s0eZfTbK9eqrgymeNO_H2EmffWpuhQFpZUAhQwqvefXulwXDfdSNkJlXUAUlRd4R4WE885PgK8MRXnneRsNEAH-EN0vBcCG6Vp3CFnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=CQs8p6AsNefibF3OceHUdnOIV_rSBl6cIhIBqfxbmtoh6j49GoGx32_NNTlRpktPdKO46V6jxJPyUgboIZX2qazFU7vWXTkHUL8FVgIkMbifWvfH7RwUGAongqSZ3raptDTvAjFPsMx-5JqJ-Zq81StKC8K-8-1taPDebzvLLFYy-18ec3Mtn_-8bnjnq6UV39AQ0QwXPYNpzow_ltn2pyFlEK7sv2yoes1tz1FU2bUDAj9n9qBTGDwyUq3YI952rYgPc9-dWIUdOR7r0BwEq4YszHO7diaPWRY65lz5CsW--umoeBE0D8B4pDj8Vn3XST5Bs5Rd2gJ92IEXuTig-V6m-7kqxA16vMd89iHlNFi2dblFgTL7-BQdDZ6H5Vx90bKtMcyqCef_abFtm4wFLJLBalhMEvtWCIc_kYJrtO3lR0I2Ywk5EGwZcunag4M3fyiDhFg0e0XRDupmjAJg90_2XJUDrn7MBm38gHuRyF3xRBgAJ1wSURAIXKgOUSbho1oM3Y0Y4YlowXZO5fKuMcUBU3715RQKmWV44AtHiaqbkvat_0oaeWw-aefIxBAGiyb2s0eZfTbK9eqrgymeNO_H2EmffWpuhQFpZUAhQwqvefXulwXDfdSNkJlXUAUlRd4R4WE885PgK8MRXnneRsNEAH-EN0vBcCG6Vp3CFnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
تفکیک 980 گل کریس رونالدو در کل دوران حرفه‌ای این بازیکن؛ CR7 تنها 20 گل نیاز داره تا به رکورد فوق العاده و تاریخی 1000 گل زده برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31299" target="_blank">📅 10:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31298">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfMFS2IBEM_ZJhloYZN_H5L8coQoxiDOv5d9knRCvZPChZlrB3-loIm0UlnqWM87nJVTN4oJFHom6MODBIKG_LU7RN4upE_WY08T93fksK6BK4ZguuvQxyth2NFHs5JTT2ZF3gvoHAYo5t7yUd8YJI_XQCpnG6WrwCbsWrZm4wDKy4g7lrZIirYIgq_EdODxo8eBevHKYSOnuRha3C3toqq5e4a5TfrAxeaCFfnjebrS-khaV7MqGHOix-1wXVctLk-vp1CKbozn6-72BpLN1E5qeDWqAm-BQhzYWfMA3B97j4rrqoqnluZC6u9LK3tFwIxlDfWWgiBJuERf3Bgj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31298" target="_blank">📅 10:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31297">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qD2KnAIfD48nK_NTwXnyDiJEjmD-3p82AuivUdXlwvYEkU_rsWhqga1FInSmxV-9lMv0uLajLYHfj9pNuTTu93viMdJ3egSA8YWE8DZGfQ3_zp_DyFWn9vyvGavIP83XwCT9HinA7UnvIzKE3_LbR44OmgVgOdEPQC8xcWbE0w6V20ep5ShGaehlBn7ZRXaYOPq44KOzvTHoxyNGvE1Hb32owF4hisyA-fXLsn42EI9zIPK6TNmrDhulXatt8NoFP0OCNXygTASx5PpGPw3EIPBkFW--5rpdvGBdFak0lQrmcK3Htm0YxP-8KWiT7_tmpPhllJBZ3zHnWuUQlaelfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31297" target="_blank">📅 09:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31295">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYySfnK8HLeE8YtX6Hoe1W01JeQM8IdqdG49G-ExWvy_D4PRfT3WHVKPmZcdau6s-kKPIiatH269rTbjCM_XhRzEdBg2nYm8LCEVc-bIL6qpeEs6hOifg2qYFttpp9mTvq06VWZYSAIS3wZM-w06HrXWJgBCYvSGDMBXTrbdsX4DLeMqXqNbGUo5LUxA2DAOAUJHknaqpFWgBjbP_JDT-r6SWHpJdicDQOCcfh_y4RucxRp6CfohlWshIuKWBdWf022pVsd_fZZmk0Qv0IifKMRaDiuTRuyuKE9ApG_C6gPGS4oisHf4It-ii5v1q10FUjv8uuTKCAOHdY7IGR9sBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31295" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31294">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AowzWwWqqqREy-fdDffR5sPNbXi5t34lzALyoRXNGKx-NwzrxId_wCF2ewxXqnuaZLayxx1GSmoyeFyzcLIGkPSOur2-JWOTJOHM84PDn7VnsZ7ivGS1f25NQI0uM0InTqRV1ap-gB_FOd6pJ8ieQcfwxwxVoqdtvdxi3gLQufKQiBHKyGu6yK39BJZm1XscSYABd1E_j2J1J8APAZm4qDWLIPOHcw2LJA18gP_9UHJiZxKFGAB2Tt8dnk2Gn_EgIQEAqJlgeXL-hc4NCDPXqJ2mDzj47RT5Rk_Lwxidx0gJIP8RH-3LA-Ze8Kx6Fl8b72qwEBwRLDGlURNEDqyWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
نزدیک‌شدن پرسپولیسی‌ها به‌صدرجدول‌لیگ و برد النصر در شب گلزنی رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31294" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31293">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HELuyvFb-XNXiP0gh7I6UkmD04_flN-x-IUMXd45f-4yoUXnMOkaT6_hE2x5PAFzS8W9NdFBoYC4acawX6IOOOvfu6KKk4HVYE7-0VzwpzQ5YIFnNKyWRP6Qi0L-w_xX1MihTw16nlZ1GER5VBLJateqPb2Qb-SCA20KafxVPMUNRI_gQKC0qlyFttTbUi3QFN9QoOTvLOei-Nn6lbcgAHj9_6MLWNWtG-WoMr_CE4Sp3kzW_KxCQLMvw59HDqA7Mh1qabRYlAByYOE5ndNuNS48ADngsrR7f9nJLQRqhC5mRWgKQRI5KN9IFS6d2vI4JVsX7fOv9t7PWkejc9u6yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛برنامه بازیای معوقه هفته هفتم رقابت های لیگ که روز سه شنبه و چهارشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31293" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31292">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7ZWdbQTNMPko2FrMZY20NnDnSujNDbq7M8EkG4Zu5XLWJ3JAvoLXnZktEKG6wHrJz5I_IqE4sfsjRqlZTdsFt9YkTGGtAH-TGGsqiQaRFA9P1v_4XEfqAOQ5ryko3CEJJBlMCDrTTT0ujJVr26AFD5WxFxt6-8SrODmfCMoWugu1e3uLe7X2KGFCdcHce8lNMX_9O78iaocw-lcPdpmAftVO1l53elDdwNfTuVyM-p7-KYxoFZRqsA0tA1GphWfF7dor9zvRmMg9snpdpCwfL6Oq6Io4wt_yasXZApgrOPrFEaiNiPfwwn5uGGP9Dp0DByvaxpamF1EFJz4h3ZmGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31292" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31290">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf6Q1Xf8ok20SsbYKTh59-LAJuu_4O47dQSpEHIdfu3xoW0DCy_fgmrLC3VBkzt7FsmyX1XwvXZTCxZaloLluX4Qv4TvN_F4T7Bhpt6ABNxOzqQ7EQEpEY5yEIViiLifBzulavrC3owgDFrW2l4MVejU1GgAK_84fQrb348q6fxI5Q0DOnwtefBMGi_6z7rk6lkyySLtEmI9k9suVn724bn96-tCcWmadJdP7c5hXVKrJz8qd30t-Y_0XvBlZ3ikI3wZln4DcMNlsj5DB1XyORUr4v2z7RPIKSQtrAerrR51TcqMX3iTrNRsx3Fn4iceAUyA5yyZa9cCFzIltqbzIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گلزنی کریس رونالدو دربازی‌امشب النصر با الدرعیه؛ این 980 امین گل کل دوران حرفه‌ای CR7 بود. همچنین رونالدو به اولین بازیکن‌تاریخ‌تبدیل شد که مقابل 160 باشگاه مختلف موفق به گلزنی شده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31290" target="_blank">📅 00:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31289">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urEmPrUlvlUt85fWxiblFobjtao-WREgPUMVYir-OvqlstzlApuXLNB4giy3u2GbVlDoDpsJodSo5wtySd0MvRvKbHU0U9qsxkycyoktX9zN-b1V2BiWkWGExKmCrlZRifBfFSF0Y8GPmLqOuMwDJA7Jj_gdk8On8io8nH7dP1XT7ND-ZwZQQ8gfJyPVxDgNUFYFS9W_LVq4wYuRAZu3E6mbbLYYGhkDkR2WOAITIjVmjLOBroadjdGOQRRL9-USCtJr_uLU66iV3uwqDvFAXY1SzEvf9ai_n2vN6pDDUdSRHSYDVik--qZv_1msAAmc_1VYbay10JZ49e36-HQAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دختر خانوم پا اسکولز اسطوره باشگاه منچستر یونایتد: جود بلینگهام بازیکن مورد علاقه منه. بنظر من او در حال حاضر بهتریت بازیکن فوتبال جهانه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31289" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31288">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgH0WqyM1aDQLrygZtfL6LRAwKFU2oICxbe_QbMsWWX8ugMx0Xvi6kWg0FMRH6efG6NOCZWu1MGhyPLDJpPZTlw4SYSONeYOob-uU4h8a7zV-caWQofqJmdnza8OGge86cYaC-YkJRLbAU2WLDYPXU-BwRXxtc1URPEuU6TNDuwBe56FraWkJJsqNwSIFA1OT14ru7Wfh2i6BrQOUZi05t9iH5Tf1iC-dNM8vGgvhPwypGRA9vMJqCMmgv98lcZHPvA325tKLzFgG4ePsg6-bCdypLXT9Jx_kx6D7KZP90iyqSUR5Sqx_TUa3Ys9kMrFFw4kL9_ohz_Lrvv4rn4klA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31288" target="_blank">📅 00:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31287">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31287" target="_blank">📅 00:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31286">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLx8LXvkp0ttAJdfb2PBpouUWELhyFW-RkgeST3Uuq6d47cJr60AAySkah8I7PhVnAvRO24a6vRjjgalVMiWQ1TPuagSIFqlkYH2_XDKcrh_VsfDRKB4gK8p3HLGLqeCHEPwxj99nw6ANbMyJEk3NR_wbW-BWCWX6rCDlfxjhERF3qsNBOBIH0j7yDaKY6O-rtzwOsKmiluFN5QjKxjKuoCQBT2ElSZn0IUOrObPEzPdEjj2OWuwuaFZtNXvS8c8f2FBzAzO7fIJRZEXzQkQ22wPdF923pWvrx2yyICUHZfY_oHk3xGxJcj7TMxav6mHOLIHckB8aoyub0vyJVi3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ علی رضا بیرانوند از هتل و اردوی باشگاه تراکتور تبریز اخراج شد و با صلاح دید جواد نکونام برای همیشه از این تیم کنار گذاشته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31286" target="_blank">📅 23:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31285">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7nmn8fMT-b0Jkv8X7GyJCaKby9Mi1zReZpBmLHnRkBKlnM-s2iPa0NaoXEpGZvf679MVK2_WEGWKUOm97iFeCFkd_LD4v53YX5ywWNNGuSQ9r1OChXTrZwZGUhHSbFVUPAsGT8-ttw3L9v6iq3EuldGsCTqHfpNbU1SQ9WawNQkEAfcCWtzWNxZb7-VlPYW6AtgE2GFos3e7TVt9kvR27cx-UXpvFA4SCCG1wEH7RwYESux3nDNCVSyYqivtUH4HfXGduyvQ16QAFJYkfr2aaZkYmD0xmK1qpwYlqx-JZsOFjp9HdHWwpSjRvekPbllssgIVLr6sEFZf4Lf1IQ74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جوانگرایی‌بسبک‌تارتار؛ حضور پویا اسمی بازیکن 16 ساله به جای ابرقویی نژاد در ترکیب پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/31285" target="_blank">📅 23:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31284">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2hmsGxIBcE6A4COJFFDB4rXfzkvJozCDpSgoT4fsvwwoNQUkccL97_73Z232Dn3i1XchFOodLTmd8mYFRihtViddhK_6x57zQLUNTA98PAGpVxglShELtgdzkztKUuFWntVM3pKKW-wb-DP3Vf6VCnUegsHnlJnE7NLC_sKhPF2OZLnHWnoxfmzhSlBdh5Ts3qq-K1547_P4uea0lGaVkBUUc-TJNJVHDwzSRNJwyQnx1acMTNwWZCZuRxRTHDDf8r6xzvLnSq1PHDYJFVYoufd7dGVp0mGouR2kbX7paaZ1UmY9C2xdhwW0meOubtUPInVBwBnzLUZKfU9Gfy1Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/31284" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31282">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPDzhd5dr4yooTx5uStcauKZwJmZHo80u2CfaHMx5uRtM4CfihhMDGdeoWwNw9gKow5NQrRynKsKgmJHD8wdMMttAQKeutD8_iicmuhMNsRYSMgyc5Cv6QqyON8LjjENhqHkwtrnwdD-OAXOL1Y1MNwi56L2M32680phAtzd8CjrAkyXGg5GGf-Lc3x7K_L4JCePYsxkZUnORiSb5ShtRYbUMdt30Q5XxAM8hh-TeCOCS7-INze33vvMtn2w12qvJite5RD2_suAAuVzIbafkWRBqMJvABt7IiLpFRkP-Ur6bTUKiHWWJybzzWoZ1YRry3hD4dHEFWX-sUQ_z7YdeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lh389X4JirSUegRyZmzk-M5VRPLrnonhepQsH063gT-K82OsYRIN4nW2990Mh2uxvllrYe95lQX4rUPD_5ZOxSlybsNgfMiRqnrF8tCxirum6LnJs-WWFRNk7tkvOmYLd2RK20vur7d5HFgkH87upgj-sAK7P8kSg9c86XFWVcHlD9YXq3I6I1wXEsuFzLfO8QDDwzvoeMTvMma79UuNyP0N1E8h7fbOrTq-i_oyD6oGV0K0z660TJpy8GXx6zSeaXUmkomVTn6Z5lEV4h31y1srOopcS9UHiXdjyTGnSZdrLzOMveidYTf_okXl-nKU5FG-lx6T9p3VVlejyISGyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/31282" target="_blank">📅 22:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31281">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqUPrjqASBKeub0Ijc6wgKZF7qYRMzCwoY3qfKdXZ_kCbjzgkw9HsNN0T5BGucM1a2USlixlnfjcskOmKlo8RLBB67bfhDVeLNcUo_9wwvaGnvQ_2kSXAwyhPNwPiReeKlxDpT9zdG45hJJ9CfL8LjbLAI0F2svi_-xSRTsTxUBfvIQYiNXYxHZdslw6l1qNXTyYLRPBKO8p_hIE4cqgn7CUbigNebdYeMxokzXywP1uZMs8bgxmvYMqulD7rNRwAzATcLv9JHROpFgsyrNsTULBqTq9sb6kPpkmYRDhiLfK_33z_9lZA-_f8qjiCuX8VaUfOR2Xs7LS0oh7jfxO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/31281" target="_blank">📅 22:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31280">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GToEVfr8QRY09Go-Vt9TWGwaYLRwwvLt_cr6NRGn3ESwXWNfYr99mXc2E3GuTr41IzS0YJFtadlZ-Bnse0jXRNVbacRrrAEFzGZhPyBu0p56Cm-oKH_cYX7rg4OQgCuVxJrjn3RbS21YYIgQoPWBtK1Pc29MbDm9NsSMb8-cgw2qstwL9Ux-JNMXKZ3DCkgtW3dNQJozhXAT36yrcqpQykFpeQEoDT-1j9_K5l_0wz_W3ju2AAIP1f_khAklygL4fee-eZbbchxCWp8lGHQk_ovafr6bNORI5hecXxnYCG8x-EGhuIQ7Kc4ynaKYo7tDfxYJ009vqVK1i35QCqNF2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/31280" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31279">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/31279" target="_blank">📅 22:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31278">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/31278" target="_blank">📅 21:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31277">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpbQzVgX3Sw3QRoCMgNP8e94SNMySJHTk-rayPqafIisZLNrXtHqIs9TrG64unDyQZxg65JBErlxGDk8L6HpRqtalEa_pIblP_byJi7d3Hr9jt5MWt-tKKOa5fNOJvxhAmbqTuNtKbWmdthFM0DW6v77IzOikqa2zXq-oQu09r9m7JpGTaDPD4T56BoM__JxKedXbU3a-B0HHQeKFMV1uyyRdwafgPBwSv5iYsNv7POVqpOj4ZN611OnU5jwsKZ3ffj3I8I_1P0oxK_JEcvFB077AQV4j8ANHjiqwLQKkls8TUmTcrWpCjbEtHt8numKlY5JWZbXMlhhJ0clmZOpCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/31277" target="_blank">📅 21:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31276">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpdG0TjVKr8VZT93lkeIOtbeJHf3Ao7rZryQh5cZfvFFe-1dt2AgwM07m8d5OPiP-ghB932_kaNPmvbVV4gV2Gy0-RqC-r5fggrrsyxsjL88Zb3N8bLlr00deGSpeXIJTiP2KvTzuhs04HeAuxF7czva67sA4Y6cvXplHsxTRlCEbt0d1QSXNtkiHq6j2NwVqx9YzNuA4ByFvSJjl0EFUTXjiSuKIs6IyreVgLEXM2-xdSy-Kg37F7wLRJyfpQ5jzXGLuhIehYSitPXaxRb9q7O4powIOqjaYX7HBOebpkJmfMk5MALDSLS6_fSzlI_6Gzd-PC4VliXDx0dcvXimmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وزیر آموزش و پروش؛ به احتمال زیاد مدارس بزودی و در روزهای آتی تعطیل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/31276" target="_blank">📅 20:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31275">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de2exaAw76MSZkSs_Ctf7Sh1zb76kXvnym45sNkA__1jumgDYh29pSl1PIhRWbj2OMrF3T53FJJYs3By3EbEascFnd0XzDc4HO_6XNQ4grWwinLf65_-AUTsUkbOFJ2eHFbjumlmQ2wvu78bAQOZLD2AMRsWaE1dR9ZA62bReYRdmmvn5_njuQzHpcyOoZgDkZjN3Gm1y49VobqR9ap_Atqr8jNCY4mxPmt1cUInE_m5E3E9yfzIR1zZhRJ1PtkcOIhh_omEvOlDp8BCf-xk14auHC8JLoDheu5lL2Z3S-QpI44apMD19yB-y6zWJiyBSTi7eHPiOW2QCvtMWYjoMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/31275" target="_blank">📅 20:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31273">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAiImjZrbLPCVz_HRq5bOEDXZdtOBFJMcth2pSg73ZTUU8BGV87YizeqMjCSA-48_51gZvmclgAy019Hcpgu3PuoPWJxEg9Zkx14UILXl64dJs7DJvfexbEO8s8ZJJClXjvorNq3Rg6YUnY3OoL-8GWN_w-hbZQjGMQ_NALhVp4PixWE3OL4Ytda80RsW6smPChMT6bQfig6CN7anE7CR1TKUAcr0MbArVtpju-JouAvoHh5Kiiy3AmlO3i_bfTAJQciYHuE-3324og906LsQAPx7-8PkuRgKR9LlQd-Viu-G1ylgxKgNxkc3O9140GyEDQzu7XxoKqHGd_Arzr4ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Am3sHJUnCMQ3EujMJ8CVb9D5o2g_WRwwtiIWWzVPEMKy4JlQbf-5wPW5WdbED5BoUKPafXIM54U4QYbN7rPsVMt6l7BDTlp6l6zyo7tpnghI7oz4HBS6YJ3Y-vL55aoyYQr3nC8AVCYvOFy0-7Ik79IQYKYxlh1hrCsel16iNmYOypBU7k-bFyciDgVlk7a-JGN732QKYwdUrTLnN37v6EV0E45cWc7U1XvfoDnnShB81Xu07SjhTmqxWyCV9xBKO1n_lBZ8d6-JBpG5o-9m7lxXwRLEv2QHJuiPzmTqgVZBmy2qKv000z5ETEK-F3U7wgnPw6RwYsNw5atpJRkNfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31273" target="_blank">📅 20:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31272">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=h14wE7ny7tcShUq774XHPt484_Oy2gBIFTupBTtiVu9Oe9K6hMVbTZgrQKukPjGH6GIX5buwqJy8IBhrDXwKFEa_iIuku350TrBM3JN3PDf_h5JmEMjf8147FyVjLLP3VeOYEZ2YzHGB2p4b7YpsaBZnwuurDtw3p-b_yMPzHGKKUFKvdSdUcPuBMHJC3xpO8_-lcIyrhj-4D4vo2G3VMzm5dKE0hnEYJYGcYg3I83wk4L8wkRKeEJ70kukjSMpMdqpaSzioZbspq4uxl4nzDgFLZPBGw_yY_TZZyuUJu8kbZdgkfGEWjthe_6eiabQz248n9_o1VY5HHyBRImJTDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=h14wE7ny7tcShUq774XHPt484_Oy2gBIFTupBTtiVu9Oe9K6hMVbTZgrQKukPjGH6GIX5buwqJy8IBhrDXwKFEa_iIuku350TrBM3JN3PDf_h5JmEMjf8147FyVjLLP3VeOYEZ2YzHGB2p4b7YpsaBZnwuurDtw3p-b_yMPzHGKKUFKvdSdUcPuBMHJC3xpO8_-lcIyrhj-4D4vo2G3VMzm5dKE0hnEYJYGcYg3I83wk4L8wkRKeEJ70kukjSMpMdqpaSzioZbspq4uxl4nzDgFLZPBGw_yY_TZZyuUJu8kbZdgkfGEWjthe_6eiabQz248n9_o1VY5HHyBRImJTDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌های عجیب و غریب دروازه‌بانان باشگاه‌ها درهفته هشتم رقابت‌ها بعد از اتمام فیفادی مهر ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31272" target="_blank">📅 20:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31271">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne1jM43Tv_Lvh8YLGgHR1pvKByAoBP3Iqjir31GX4HB1pfQcJbqifJ3AC7V2ET9cO3nqLrhkwkk5NnRmVaqDTjTzP0t2FAmWh1h5otxUKJUJydXIfmCnj5XVnVOyF9HLHBXLt01pJkUCot3_K1xAnPNHrQFn1TW141UW2dUCgjxVxgDvTsdprrO4gBRLeKsByGwHAI6v9s6C0QgLSH26pn_nk9b3FsDB1-XECdQO4Ugp-jGvPEC7errQZMH21mAMZfsPltstjuGT40vz5YrFWiYvmE2Q0TM2gFpnioOvxrk1SN_0LHrOgMvmgwgNgmQY5wKhijXLRxbGx1FSgAJ7Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ کادر پزشکی باشگاه‌استقلال به‌سهراب‌بختیاری‌زاده سرمربی آبی‌ها توصیه‌کرده دربازی‌روزدوشنبه استقلال مقابل الغرافه ازآسانی استفاده‌‌نکنه‌ تا مصدومیت امروز او از ناحیه ساق پا کامل برطرف شود. بدین‌ترتیب‌به‌احتمال زیاد آسانی در…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31271" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31270">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31270" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSFSzxB9fIdqpMlEQ8ltZYSm6Z5japFqkWx8Y9OI-Vra9TDfS02EMM1pORI0djZMTNF8NZarswmCSS9WF6bej_RhBUNFg73UH7Sel7A0aiM7I6QI89_6Io6Zopabl3T5XI-d16gEFQqnNS5o27XOQ8y_yRCoSa4SaS-056MXmI97I49hR1CnZpLP8h0tNOyCJ8NsUU8YEm9UZfqQfFKfJSs4fvp1-g-URElzL3RwB8vifVprjGMB08MTJd56pcWRq1wAyRZG1Q1FO52BIl9fhpwXRAD8mDHsD-vmWQHyOG2UQPSbsKZPT-vvWhSefleF1wOZZ2CppB23Eduf2e5NDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ وزیر آموزش و پرورش رسما از تعطیلی احتمالی مدارس به دلیل تهدیدات جنگی خبر داد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/31268" target="_blank">📅 19:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31266">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDSAxrxFaEaiwVIuSTOwyFngFs91yTAyyUSF-3Xvv5NrTIWOp6F_WiuSCRopn_-6nT2sZibIWz4vPaBrgtyoJykfTdARIwnDDy-2mqpPciHJoPc8-8rJqz7CguB1TcoS4V1xNm-m6-Ul3R34pxVkQMdwLCu5dEsfcKVm5VkG96OLkRlRtyRciz8Nr11QYMXEzcGkHP995WsAyTkhK8SzW895231uOeWZOt-aZB_yiWlur2HxV0Xf6DO2FFlVV-94KHcW2jJEXzgYGDE3ji4sd7fU4yAv6lp1pLT7Pn5ExYTHgC0Om3uUJe6omT71B5MRIcfQvAKzQQzzIlCxt2dP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG7zqqyfMyBGZEeV9vqMNswiVXtlsKes6eKGZC1HVHCC5ub8kFl5vHR56VZzLJsQaeVI3yr7KU6mCONfY75SYdir2F92a2M4k-d1VGfPj4unSJ7zbHGOPq-INqec-z7uRK2bbGy8pFwINDzQRrkSNcRrv705-DZfWvW7e4dU6GdI-BU-KuFWN-LPqBtGKxovkEHXQ9jJwzspTGvI044DjJ8mQuJ8LHzz_30HUhhfGjjv1hCFATU7wwpJI3eTNv2qYPZKs1luvr27EcioZFSHPfPwxA6b83L_g3msDnnGWJ1Hx_cyUGDwM4l7KIyIzLMI8_qYCZJFbO-CTLeb8U6Qlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بانوان هوادار پرسپولیس درقلعه‌حسن خان.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31266" target="_blank">📅 19:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31265">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un7ZvHD4QZ-vQ66x90o6MeJQqrF-Kgu0X1JziWIad_G1ChnwWKaH8blDwUKvGDetdDpqI08x4ZWHvRMQssS-wvgm7kfHNWf68CMKtYyR2On6TLz3XZvfF4BlU-kPWlb_C2eqmwJO2d-E1_hCpayZRkoqc50CxRMV3WRdl36qUmklK1bx223Au8LnFtoSv5MYKTOnREXPq627UqoWpT4NO7tSr1IWhU04besIf4Ka_l_NXMm7wRcu6hLSFpeC2NbX2Vxzir5rrgbfrpCk3fzQd9oROokjG_dnCYlQba4T5m-X8WfLAjyetoRMksOlzPfMKQXn7-pLswUaGfJkkk38NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31265" target="_blank">📅 19:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31264">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tr07a6iHuCh-enGtRtDyQ11WFn-L_x_ImL8IAic0b6KYxaKyWDFMoQ9FgvwGzHyMFw6WZwUvhF38qVtz9Oq_3h7v1TKpzdDJO0Xm2ZqhCV5gydQ41nCAYUmMVcl2R5wTRrrfEJEuBaXjKoSh53HYh_FNcxdRkWDLd49MWorZVXgKaC_ltbzKb0MwbwTpsYcIN09pVvDbZR3XvaK-oWAS8RsMFylLt2Z8DlhSSSTFDqSoaJij3jQEXhstvL1CgpFCbpCQ5XielFFM8jFZTfY9dkuImhJmtFwT6m5mwYl2C6rRAE2UdJ1VcnhCfzBrKaGFh1KrfLG4Q0WSjmmtpqTRSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31264" target="_blank">📅 19:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31263">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjA1NGXvWiCYdH8LzTpVGk5h5aK4M1fAh3yfiD4wpeszgGGScc-ZynQi2jlMZ-sd2CWkk2muNTH_QHPR2L5fLkLUzAlqOXpmvdimyamdOrWDuUi0mHY4gx8JJUxBd_Uzn5s_E5W_rtI1Kr759KYveYmaJypeyLhpASsKEKKvbPQR0xe9sU_kSumPJ81aCUuNXgxiGdLcDTGm-aXmA7rA0qHLq-zM8Nv-poRr_Y3UuSfkY6M_DIpWbtpSOcDh2SmEgEYxn0rwEpsDB_O17QJnuGZvvV3ivTVpMw64eb2ykgnnEdbJ1HtZiAd8obrHEWHqf2G0ZLoOPY_WKxtezydfVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31263" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31262">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866119f609.mp4?token=NDBwY86NigECazRnL_4MEE9uNNfn-Ad1DQF_sCAsDSdT-YbIt4pdIJr70kIurKKhVtj5Ys6f58rzV9zvQvNZcQZDxiA63v8pl4TsOQyuiZ7xoBYz-IRYfM-dgBXdzqhvEFxU3KJOH9Lizz0ILeXIAAvA0_DXsGn9AzPnlOIgMZ_6BQIoqkcES-eZH2PEI6tDzd9yJ5hHJ-CaGaV6zPBlSDuCquByAXYpM9VnNZFmq-4V6eIU36nCuIxbV0ghIYSpi2GARWoSGNt5VK7Ikmn_dUu4BEUszKlaNJq2iR8PxjWX0BvlM1mc_MeLWVnZzhKRb1kG1Z__Y1Hg9O3iL6g26g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866119f609.mp4?token=NDBwY86NigECazRnL_4MEE9uNNfn-Ad1DQF_sCAsDSdT-YbIt4pdIJr70kIurKKhVtj5Ys6f58rzV9zvQvNZcQZDxiA63v8pl4TsOQyuiZ7xoBYz-IRYfM-dgBXdzqhvEFxU3KJOH9Lizz0ILeXIAAvA0_DXsGn9AzPnlOIgMZ_6BQIoqkcES-eZH2PEI6tDzd9yJ5hHJ-CaGaV6zPBlSDuCquByAXYpM9VnNZFmq-4V6eIU36nCuIxbV0ghIYSpi2GARWoSGNt5VK7Ikmn_dUu4BEUszKlaNJq2iR8PxjWX0BvlM1mc_MeLWVnZzhKRb1kG1Z__Y1Hg9O3iL6g26g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31262" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31261">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=mtKT3w1Nu6V1XMOAKgrFtNyYvPvgm3P5fyChf7g9YEx8PIwvfB76iEhC83cWQXkYUTQ68VSWawXfA9ROPRNUooJrcby7pMpy3C-4shkcz7PEDbFeU_fv2psxSgKSCce_tgWn_6SMF_0Ewtn8Loo16eYthWjEyXP2K8F3FOQxmJX4HvUzmcfCuQmiB_6LnQbghO6Jtu4OyimZUsciU4tIcSms596vU3NV_8tfH2b0tbd5Zs6BVpP10E1vunCSuvl7pCscjgX3fdU1m_4MAZcWBVInc5HziOYajMSifPzgjITa_V9xMZygMNNv7KQ7mqqlPYfpkPMCKddaL8w3-5iA7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=mtKT3w1Nu6V1XMOAKgrFtNyYvPvgm3P5fyChf7g9YEx8PIwvfB76iEhC83cWQXkYUTQ68VSWawXfA9ROPRNUooJrcby7pMpy3C-4shkcz7PEDbFeU_fv2psxSgKSCce_tgWn_6SMF_0Ewtn8Loo16eYthWjEyXP2K8F3FOQxmJX4HvUzmcfCuQmiB_6LnQbghO6Jtu4OyimZUsciU4tIcSms596vU3NV_8tfH2b0tbd5Zs6BVpP10E1vunCSuvl7pCscjgX3fdU1m_4MAZcWBVInc5HziOYajMSifPzgjITa_V9xMZygMNNv7KQ7mqqlPYfpkPMCKddaL8w3-5iA7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31261" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31260">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=cQuRg2QhMpORkb7vB2SAropnKJj0k4QXyiARlZJ4sZ_Et26U2o87dMns9FbmS-5OPo6pq7tUNTWmRjyXwI3lXQIeX6eebp8GuVdwUISPtCbOfAWOY2pLO2S73n7oBO8xRddE8xapVvWOhKCppKmL7pUIaPdFTmK7bAhkXeSvIvz8lHqjUITz5JprExhZH9EaoiAsfyHXzPbf8wF1xQ_lXR83SiqVzItOWq7P58yY_8kvfUHpj34ebRgbJULuH1DuqdwRdhO8OT5S_jPoVVcdkWwuEpyDrDerbWhZBs9MYcmNqWvvIhOmMntYqkckDkaJWivW4iajSG-HK6-f4YFPsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=cQuRg2QhMpORkb7vB2SAropnKJj0k4QXyiARlZJ4sZ_Et26U2o87dMns9FbmS-5OPo6pq7tUNTWmRjyXwI3lXQIeX6eebp8GuVdwUISPtCbOfAWOY2pLO2S73n7oBO8xRddE8xapVvWOhKCppKmL7pUIaPdFTmK7bAhkXeSvIvz8lHqjUITz5JprExhZH9EaoiAsfyHXzPbf8wF1xQ_lXR83SiqVzItOWq7P58yY_8kvfUHpj34ebRgbJULuH1DuqdwRdhO8OT5S_jPoVVcdkWwuEpyDrDerbWhZBs9MYcmNqWvvIhOmMntYqkckDkaJWivW4iajSG-HK6-f4YFPsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تثبیت‌پیروزی‌خانگی سرخ‌ها؛ گل دوم پرسپولیس به صنعت نفت توسط علی علیپور در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31260" target="_blank">📅 18:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31259">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=NcBitycvszMh1ED3nQQcCj1WGBbDPeB2Ilbhctbgod_grGce1guq_S3c8xP5Q8MkCWXdw_8KLnwMP9UpqTD3i0bSbrABONhIaDQUiMCTWncYAFfqNsJD_ioA32MSaRDChxwWMrjVdqwXPzl2QDxgpXbhf5v2WWcORbCQrUoY7xXj03IJoj1uy7r9Z2Ur44LxIUy9Xtpkms7UnIwcswnwynufo5rob6UjQGm0EKZhTgllGfEfsBHc29xr2DmDfvCpQ-uUfTMvxdodRDE6cG4R_iGhWsq3BYAi0UfNAMJBhjzY0UVZ7oznzQB9j0_J3kCGX-Cub9hgSl2ZxLPNLYZ6RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=NcBitycvszMh1ED3nQQcCj1WGBbDPeB2Ilbhctbgod_grGce1guq_S3c8xP5Q8MkCWXdw_8KLnwMP9UpqTD3i0bSbrABONhIaDQUiMCTWncYAFfqNsJD_ioA32MSaRDChxwWMrjVdqwXPzl2QDxgpXbhf5v2WWcORbCQrUoY7xXj03IJoj1uy7r9Z2Ur44LxIUy9Xtpkms7UnIwcswnwynufo5rob6UjQGm0EKZhTgllGfEfsBHc29xr2DmDfvCpQ-uUfTMvxdodRDE6cG4R_iGhWsq3BYAi0UfNAMJBhjzY0UVZ7oznzQB9j0_J3kCGX-Cub9hgSl2ZxLPNLYZ6RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شروع‌طوفانی‌شاگردان‌تارتار؛گل اول پرسپولیس به صنعت نفت آبادان توسط تیوی بیفوما در دقیقه 5
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31259" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31258">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJVKb2vzis6LS1KclatE8oz1JPoRMOLtxP-oP9hN9AxrcCOex71iYEay2Uk0GsEjOjT5ZxUhF3cFAwzuRWwqALUpSJa4eGuD_UVuydhBsCjWcbI5POZSHA3NRMyEu-cp2vKIrPKtrvRGyu4tcf8gm76GPN_nNE32KuW8msxR5mHeq24MXPaiVT5luK6w7nIqm8AghStn_Xd1yuB5l8f2Eyqzq0Jm4pSlTX8eZ7-uObQAyf6OgM5RhZa5a1sgR8S4r1MU8thsFFNjn-0gKYyxH9gg6YZSZhML7UGXAUqBQCgobshaO0URBEs51AXkAu9HnIHkBw0zWO7K2hIoBhUgDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تصاویر جدیدی از بازی GTA VI؛ این تصاویر در بخش موسیقی وب‌سایت بازی قرار گرفته‌اند و نگاه تازه‌ای به فضای جهان GTA VI ارائه می‌دهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31258" target="_blank">📅 17:48 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
