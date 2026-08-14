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
<img src="https://cdn4.telesco.pe/file/jqRLReb-Sf6T5r-cVPeX-o4MqvxanT6ox0uT7__ptx-MBmPzLmQJYZYVdbH251QaI-DInTg_DnxERcYOyWyRm9lw-8_8gR8PJB0mW0N6KqspXiXYdVbEQnzIjnnMndO9qqFJn0EG0ae1SWv6s6w-sAhLuvLHX5VaYTTbAHjKYUO9YnyKSuAfJRQO3puFWrWOpNvphXwlDFez9eCuLQi4URgANsPmEKsbDA3VX-LA1lZ6dtBzwEuKeoKlLPVwRaoxh5rxBzH-NXgTDIX8yqegHaIkoocn56cG0IbDQTRKD8NjOrJ5SCnq4scN7f2twXHnitmAnerJfoT2JIqWw3q79A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.18M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 18:42:49</div>
<hr>

<div class="tg-post" id="msg-681171">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzUFFqePNaUL8ztrvIDCRAVfJ3KpF0zuO0vi5aPHaclxKq7gfwEklKf5-xAW3SwDGH_FpGhJ7r0q5zkXhPuUCvqMrQ96wGZu_SV_eENEstRsnNciD8G_PWUd4xwe4iqvOwmqHRknzbQ6hEnqQxglUC1_4fEyPIRcxTmKO1qS5fUcBXc-kblrxCPxHPLsD-mSRps0em5NkuhqcufjcxZVg6IHb76_6dVHNRCgO-AZME3PYynLtbwJGKu0TE6R_de1n6YUyqobygyxBgrX28LDZCyR2YTYlIaBllA9I52NIvslMAOhRg6Ufp2CTN4Q97XlWC6mha6GvCJsk0YZAtX9Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کاخ سفید برکنار شد
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا در اطلاعیه‌ای رسمی از برکنار کردن «کارولین لِویت»، سخنگوی کاخ سفید، در پایان ماه اوت میلادی خبر داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/681171" target="_blank">📅 18:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681170">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z07TzBOPw3gi6YCAbBsLrH-ZcFa3afA0I_X2rta_J9dxPSOpa9mxO1LOvghX2TK4JW-35qbsVafEGNH36mVGJenTnMtK5P6s6tep_pGY7EEzrATXcqh1KsyBfEqR2TQ4W0k-kIfpo3C2OSEvS0xsDQ2vAc2qpaBp2cs13A4CktgAAO2ETK5tqwqOpoBPZyWuvOrudnAia-L4n7kIDmQVuIZEv227PzpchNmssiytMFmCP5IZr1BgPAc_87HvTv_otzp8i0C5nY7njf0YXONZyWxxlHIm3BMAE_NaSuus6q1-cm5iByXpI-8lrn_ynGHrp1uPGrvEAqy1gKanYCagoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوجه را ببوس! | نمایش آشپزی با ملکه پاستا | نادیا کاترینا مونو کیست؟
🔹
نادیا کاترینا مونو، که با نام مستعار «ملکه پاستا» شناخته می‌شود، یک سرآشپز ایتالیایی، نویسنده، کارآفرین و شخصیت رسانه‌ای ایتالیایی است.
#چرخ_زندگی
تجربه میلیاردر شدن با آشپزی
👇
khabarfoori.com/fa/tiny/news-3143141</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/akhbarefori/681170" target="_blank">📅 18:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681167">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UcCcokoF6PBB8WayfFQhVXpF0LzhRsajw4tLMcQwZClgRm4QNhY5zqbby175APhqs7QxFISvEvGD0EIaPcZ1XXm-EWEURewmawE4OfS8Mh_Z1RNYEXLQurz2zpqriPqqK_7WDfOnlEJw9BPzLDM1hy2XEFoQ9WZafre_Y2a_tAj9lwT1Tc36dUIbDZLlhGVWCPuFt5eNh-p-zCM4a3bcQtVly-q5BOe_YgoY-BHt6bWAORlE4v2fmH9vlkyxSW86ZzbSj7sREzOWK-Tq89SlbWtjzKdFHLQMV_pSATBJ1AqGet2rBxPDlduBrVKfkDWxe-P-aILU7g5L3fYCBBE_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpXUI0h1S7wrL_TBayxX61KsarmIAL2WnoboRlmGCgPtWGndoAcO4wQ4PuQQRl36FCgigWOOUB5KnoED7qNUrsYA5N_yz1AteKEQNO6FzhvEkfsFCswdDqCaSrmONe-HOYJJ3cfQi-5qr1I_yk9IeBOkY9vbJ0CnLNS6YsM4VVu7gQvnKPkNxhtswt_4G1Lihs6QvMqknf34HfxL05x4ptvlxIuVtw4LGtGvdCI1MGBUeHXec24KogJBBPS5Gjv261URtXYW9ciddJb3BQVIgKdpWOm9DzqYf4M2E1850D5VZv_hHgGteEDsqyADOvOlGQP-heD_dmDzI5kmlOAvnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جدیدترین تصاویر بارگیری نفت در خارگ
شرکت رهیابی محموله‌های نفتی «تنکرتِرکِرز»:
🔹
داده‌های ماهواره‌ای نشان می‌دهد یک نفتکش غول‌پیکر «شرکت ملی نفتکش ایران» امروز در حال بارگیری ۲ میلیون بشکه نفت در اسکلۀ آذرپاد جزیرۀ خارک است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/681167" target="_blank">📅 18:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681166">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d719e28752.mp4?token=GnPM5TuN1MfRughp_RKTumYPrBIJ0ZncHrM5QxDvNH1dALYi_brbj3DgsZMvR3nGAJHPWLxKt1gSpFzLER8ectZqRf5a9GzApSbk_q76rsoBhVDAN2AeL017xFslxk4x7Dfx9OIkNxwooIccn9TocF8HXB1WNCLhLyuCIKVD5D8WuKcsT51Ly9zAcr5dtnksCxo5fJu68mlLiGQbKPOkpIeeyTXko6AXj0lzPGSpmSszZvnPoxImckkbd89POYDFq9F7GKCLKCtG-W2yODcCaqsXfHbltFixT8n-t6tb8Wy6sJh24NDWFcpj0opIgVNGAeSIE3QhapD-8jiyMZmbZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d719e28752.mp4?token=GnPM5TuN1MfRughp_RKTumYPrBIJ0ZncHrM5QxDvNH1dALYi_brbj3DgsZMvR3nGAJHPWLxKt1gSpFzLER8ectZqRf5a9GzApSbk_q76rsoBhVDAN2AeL017xFslxk4x7Dfx9OIkNxwooIccn9TocF8HXB1WNCLhLyuCIKVD5D8WuKcsT51Ly9zAcr5dtnksCxo5fJu68mlLiGQbKPOkpIeeyTXko6AXj0lzPGSpmSszZvnPoxImckkbd89POYDFq9F7GKCLKCtG-W2yODcCaqsXfHbltFixT8n-t6tb8Wy6sJh24NDWFcpj0opIgVNGAeSIE3QhapD-8jiyMZmbZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا دبیر، تیم ملی کشتی را آبیاری کرد
🔹
علیرضا دبیر برای کم کردن گرمای تابستان، ملی پوشان کشتی آزاد را با آب پاشی خنک کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/681166" target="_blank">📅 18:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681165">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
نظرسنجی معاریو؛ آیزنکوت از نتانیاهو پیش افتاد
🔹
بر اساس این نظرسنجی، «یشار» به رهبری گادی آیزنکوت با ۲۳ کرسی در صدر قرار دارد و پس از آن لیکود به رهبری نتانیاهو با ۲۱ کرسی و «باهم» به رهبری نفتالی بنت با ۱۴ کرسی قرار گرفته‌اند.
🔹
در سطح بلوک‌ها نیز ائتلاف…</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/681165" target="_blank">📅 18:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681164">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c58a8ae1.mp4?token=UMslw3NQ7SGQeCAnSt7lZbOn_MJnpiuSdBNYmoWkw-nAMfYnYj8CInouLkKDYnrfgZOvQQZTHVRe6k_yuLgH81oDpqQVfCx7CaRBod_Y9wwjLgPSJd9aqQ-4TFJNHCfN2etsx55COSYN_i9ZvVTdCXaP5uvYhQpiscuyhXftvsQlUPGwovJ6u-nRgTn2us6d6d3jWFJ_dbs6pTirlCXV5R9NsC8Fvi1kO-jRCd6NPDUtJMn_EVLj8H-oN98tI_35jUjEsaRs898fKnIAUhY8B9kyOCvCnj1RWyblCDt-f5yX9LtzmucDmrcRJ6-i_UzmA-BLnOAEbbHVKop5AKP7kZYxYMwBkLJqY_hJSW-TCAOXhHyuqpW65LcCuXV8kwlifhCTJKsmakXXNsNzbrC7NaFn81yGoxlFbdslygNQX0cj4nVCmMp5vJjEGfGec1FKo4gC0joRxcI7OpGaZzPJsBdLdX67IxQQXegiAncI7c0-dwLDkGAsS9r33TGfgX17HFKqo83I5ampZTYemQNoFBJp7Hxk3poT5J3rhPviVT7RV1TAeD--Nqt2UC4AybJOzRLOW2fxJHa2s9hBKjSrDluO1GCJIFlzG7ipmgq_HOoenTRo3hw0t5WJPUCbQ9HuberYrVu0nVINS_qtlF9ha3WT2w7rctLtJpvXbwojzOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c58a8ae1.mp4?token=UMslw3NQ7SGQeCAnSt7lZbOn_MJnpiuSdBNYmoWkw-nAMfYnYj8CInouLkKDYnrfgZOvQQZTHVRe6k_yuLgH81oDpqQVfCx7CaRBod_Y9wwjLgPSJd9aqQ-4TFJNHCfN2etsx55COSYN_i9ZvVTdCXaP5uvYhQpiscuyhXftvsQlUPGwovJ6u-nRgTn2us6d6d3jWFJ_dbs6pTirlCXV5R9NsC8Fvi1kO-jRCd6NPDUtJMn_EVLj8H-oN98tI_35jUjEsaRs898fKnIAUhY8B9kyOCvCnj1RWyblCDt-f5yX9LtzmucDmrcRJ6-i_UzmA-BLnOAEbbHVKop5AKP7kZYxYMwBkLJqY_hJSW-TCAOXhHyuqpW65LcCuXV8kwlifhCTJKsmakXXNsNzbrC7NaFn81yGoxlFbdslygNQX0cj4nVCmMp5vJjEGfGec1FKo4gC0joRxcI7OpGaZzPJsBdLdX67IxQQXegiAncI7c0-dwLDkGAsS9r33TGfgX17HFKqo83I5ampZTYemQNoFBJp7Hxk3poT5J3rhPviVT7RV1TAeD--Nqt2UC4AybJOzRLOW2fxJHa2s9hBKjSrDluO1GCJIFlzG7ipmgq_HOoenTRo3hw0t5WJPUCbQ9HuberYrVu0nVINS_qtlF9ha3WT2w7rctLtJpvXbwojzOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با جان خودتان بازی نکنید؛ هنگام شعله‌وری سیلندر، با بستن شیر فلکه از گسترش آتش جلوگیری کنید
🔥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/681164" target="_blank">📅 18:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681163">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
نظرسنجی معاریو؛ آیزنکوت از نتانیاهو پیش افتاد
🔹
بر اساس این نظرسنجی، «یشار» به رهبری گادی آیزنکوت با ۲۳ کرسی در صدر قرار دارد و پس از آن لیکود به رهبری نتانیاهو با ۲۱ کرسی و «باهم» به رهبری نفتالی بنت با ۱۴ کرسی قرار گرفته‌اند.
🔹
در سطح بلوک‌ها نیز ائتلاف نتانیاهو ۴۸ کرسی و بلوک مخالف او ۵۷ کرسی دارد که در صورت پیوستن «خانه صهیونیستی» به ۶۱ کرسی می‌رسد؛ احزاب عرب نیز مجموعاً ۱۱ کرسی دارند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/681163" target="_blank">📅 18:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681162">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
پرداخت وام ۴۰۰ میلیونی برای اسقاط خودروهای فرسوده
🔹
رئیس هیئت عامل سازمان گسترش و نوسازی صنایع ایران با اعلام آغاز اجرای آیین نامه جدید نوسازی خودروهای فرسوده از هفته آینده، از پیش‌بینی وام ۴۰۰ میلیون تومانی برای دارندگان این خودروها خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/681162" target="_blank">📅 18:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681161">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lijzYkcyNz4taeOCWaUf9WypYMSVhKConhwkcg0TULLkOpx5VUukKeV6dELwzz_CARyywseKR_b1IzZybEWeSpYrsuodSrQkjxLdInT-fskfxWwI9-ot6gNveEQsNIidDht6qWJZjCrG8NL701uu-U28EadKhum4am7mrNpD0u2D5M0ZS9lSuKh6K11OX6AdQJEYg6tcolQhkn58Udbe05FfUMrmAp86w22qNOVoKL5FtOAnGQTbzcYRmmGxqBeTWil4EoVK1xkX6CtWihlH2gbSKtXZIeW7v8OtmzoBiNMA5WzFNfHnvAKJMtE9zs1hk1YadOo1VFPX9iFggOJDpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هرمز کابوس واشینگتن شد
🔹
بسته ماندن تنگه هرمز حالا به یکی از جدی‌ترین نگرانی‌های آمریکا در بازار انرژی تبدیل شده است.
🔹
واشنگتن که پس از تحریم نفتی اعراب در دهه ۱۹۷۰ برای مقابله با شوک‌های نفتی ذخایر استراتژیک خود را تا بیش از ۷۰۰ میلیون بشکه افزایش داده بود، حالا با افت شدید این ذخایر مواجه است.
🔹
پس از برداشت‌های گسترده در پی جنگ اوکراین و عرضه ۱۷۲ میلیون بشکه دیگر در جریان جنگ ایران، حجم ذخایر استراتژیک نفت آمریکا به حدود ۳۰۰ میلیون بشکه رسیده؛ سطحی که پایین‌ترین میزان از اوایل دهه ۱۹۸۰ محسوب می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/681161" target="_blank">📅 18:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681160">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPsHvI2CkkxKO8PAo8xQono2nyUfFZYgxNvuBAJgSgM6c3TFJvBPE6my4O43h0Gi6ishdd_Dpit-CNYksLBOZuJ_I7aDM3nDafwY_rZarI2b1wzzsQcL8w2jsmyuzltpy_eajl0pZP-Y_hF9ovJsY0nKFklcznErrAe5JL5RiiJRtS1x8e__Wz_MlE7wueglZhp9Gvcb3ZeV95dlrE3agdkA_VViF0dQwCVcqKRkwiiuEoiKlsZ5u2D2d_ibKeK3wN84ky_T9bAHETjyIeJmuoRtWP_PmKvU46RQ9BG3q7NshmaMNGRFSKmylDaKCnVsofDsjg3MvUcRSuWKekT6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لگوها این‌بار وضعیت بحرانی سربازان تروریست آمریکایی در ناو آبراهام لینکلن را به تصویر کشیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/681160" target="_blank">📅 18:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681159">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ورود خودروهای فرسوده به کلان‌شهرها ممنوع می‌شود
معاون وزیر صمت:
🔹
خودروهای فرسوده از تردد در کلان‌شهرها منع می‌شوند و نقل‌وانتقال، تعویض پلاک و جریمه هوشمند آنها نیز ممنوع و اعمال خواهد شد.
🔹
این قانون شامل خودروهای شخصی، تاکسی‌های اینترنتی، ناوگان حمل‌ونقل عمومی و خودروهای خدماتی و باربری است.
🔹
گفته می‌شود که برای اسقاط خودروهای فرسوده به دارندگان آنها وام ۴۰۰ ملیون تومانی پرداخت خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/681159" target="_blank">📅 17:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681157">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yyi8HT7kihALyeEBm4CvK3BxmLq5LdGkINV50S3GYSBiyqaElUasGMZRKBSfBgdY6QFA9dI73Ljt6_oD-H5VulmN-XIcZjGTUC0aRvOMWCcXZ6kbg1CdXGwgjYuZpdkSN5EV9WqsmRJ27FXA3k_SyHjnyxPjD6qofGhgF8IZutita_Tme4NdTLSurlJLgW9jnSSuvmshFVVdNQGuqHwpeyQwzAOcb0rIPr_RUNw_cGJ7GcAJ0VdoAydngMwFQwQS3pwT6sbp2ZeMgTLiIXSP2tCV7lktulkRVin3fN7Nqb9u4UQZZPatW20vNs5WjhlTQz2Ik82CIyoo3i-02skbmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این جنگ‌ها نشانه آخرالزمان هستند
🔹
در روایات شیعه، از جنگ‌ها و آشوب‌هایی مانند خروج سفیانی، ناآرامی‌های شام و درگیری‌های حجاز به عنوان برخی از مهم‌ترین نشانه‌های نزدیک شدن ظهور امام مهدی (عج) یاد شده است.
در خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3237515</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/681157" target="_blank">📅 17:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681156">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
عراقچی: اروپا فاقد جایگاه اخلاقی برای موعظه درباره حقوق بشر است
🔹
عراقچی در گفت‌وگوی تلفنی با همتای یونانی، با انتقاد از «عملکرد دوگانه و مزورانه» اتحادیه اروپا در حوزه حقوق بشر، بیانیه‌های مداخله‌جویانه علیه ایران را مردود و ناامنی فعلی در تنگه هرمز نتیجه مستقیم تجاوز نظامی آمریکا و رژیم صهیونیستی علیه ایران دانست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/681156" target="_blank">📅 17:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681155">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5tJE3aHmb7hx7JSM1jMbh2SRPg-vDQF8WhgpccPvPCy7ZpzPZAOcUduMmMXrjhi7xI_9I5Rd8xPQh8f-64y5RgCE6ICwFYj4cvlJHITUyZOvC0WyP3rjmQSHkzHEu45QQ38O_ZcKX7mSg0E3mZd23f78zqcFkiwZJYJUarTALLCz22l9fTpRjNwlGTjwjyWp22BrpMmhPf1J_L4O4YbuC4XrFOjVPx0k0yNfgmBBMOKu0XfnkG8XcmF7jmoKG0qVJrJd51TPQ2vTEI3jjzEKC3XhkjvDJSdXzks9j1QpE22QpyZ1GEA0qfbHrvwfIysxnvtF7oS0lAm7l3_w7PclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه چینی: در طول ۲۶ سال، این چهار مرد به بیش از ۱۰ کشور مسلمان حمله کردند و ۱۱ میلیون مسلمان را کشتند، اما هرگز تروریست نامیده نمی‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/681155" target="_blank">📅 17:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681154">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افشاگری نماینده مجلس: مدیر شبه‌دولتی ۴۰۰ میلیون در ماه دریافت می‌کند
مجتبی یوسفی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
یک مدیر شبه‌دولتی در خرداد ماه ۳۰۰ میلیون تومان حق ماموریت برای حضور در محل کار خود دریافت کرده و با احتساب ۱۰۰ میلیون تومان حقوق در مجموع ۴۰۰ میلیون تومان در یک ماه دریافت کرده است و رقمی که با حقوق متخصصان واقعی صنعت نفت و گاز قابل‌قیاس نیست.
🔹
در اقدامی دیگر دو مدیر در اهواز در حالی که به جوانان بومی خوزستان، سیستان، سوسنگردی و باغملکی گفته می‌شود اشتغال وجود ندارد فرزندان خود را بدون ضابطه در شرکت فولاد استخدام کرده‌اند و نمونه‌ای آشکار از بی‌عدالتی و عدم صداقت با مردم است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/681154" target="_blank">📅 17:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681152">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnce98jukoyB0AIL-JXOMlWOwdjNYw8zHNLLX-ln6THIiUOaWj625T5KNI9WNRh2mFHjaNEsnFKsA0xt--6ofpV830IL9DVQ729jAgoHwNyHvK88ZR3eNJuZYh7UciKwGn4A-Q87cPqdgAuH7eZ75mriXNww7dGKA8viaWOojjTWtFnzd6GS7P-1LC-Qcqrfmu5FwxFcmzp-igf0glopoE5EA4u5aBj76jGJN3SkeBvR3e7TdjO5GWnyrYclKCzLM6Cesvi_8kt1UacIkny4mqCaQb_qfTd-uiJOU820aHA6iESob7swJK-P3TZYVoCiJMDWy9Fi9hqVeloI3UmK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4M4RenPMoWc0LF0hH_7-DsoQOp8oiQ8-I99VSENgWmXvAijoPobi4jAKeIiQ9VhtbR3PkNLoHVNJ6_TUHwFCHLbGkdQwlPsI1j7ZrbFxRKLGh1WiY6ldcRoI6PGgRLw7uMofXQTooc-hpJbcRgrpKCgfxHA6qHjI1AFZaz4jWrZmZgnaWCP9wJoNlcR3fiRmwFr76Gsaecj-XXBnyXYLj8-EY3gHz3DhD_F4-K6uSc1p0JyuTe_VWEbW1We_kxlTT6zw05oJ39snJizmcPIhu4nOn1rv1cUE9MjOn4-1b4Vfg1X3qCDZ1JiXmybFKEWphWOrxv7r6OTDB1aql3XxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
یک روش ساده دیگر برای تهیه میوه خشک در خانه
🔹
یکی از روش‌های تهیه میوه خشک، استفاده از ایرفرایر است؛ روشی که برای شروع در مقیاس کوچک می‌تواند گزینه‌ای در دسترس و کاربردی باشد.
🔹
ایرفرایر به دلیل نیاز نداشتن به تجهیزات تخصصی، امکان تجربه و شروع این کار را…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/681152" target="_blank">📅 17:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681151">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سی‌ان‌ان: هیچ مسیر واقعاً امن کشتیرانی در شبه‌جزیره عربستان وجود ندارد
🔹
کشتی‌های تجاری در خلیج فارس و مناطق اطراف، با تهدید همزمان در تنگه هرمز و باب‌المندب روبه‌رو هستند و وضعیت امنیت دریایی منطقه وارد مرحله خطرناک‌تری شده است.
🔹
فشار در هرمز، مسیر بنادر دریای سرخ عربستان را تحت تأثیر قرار داده و همزمان حملات یمنی‌ها مسیر جایگزین را نیز تهدید می‌کند؛ حملات به شناورهای مسیر عمان نیز نشان می‌دهد ایران توان اعمال فشار بر مسیرهای جنوبی کشتیرانی منطقه را دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/681151" target="_blank">📅 17:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681150">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29eaab8d0a.mp4?token=kG5FkHiYd3TzJXP9cH_2hdI0E6IX2D2QiWCECfaYVO8fR6Ihiat0hC7fUv1pgh5k5MuZP_T5fzRwQHwzscEzu_J67UdDiLgDi4hXDyhSmm7ldNyPJi1VW11lBnigvqwsImKboC41Img1yjzyqkK6cCph26i_uoFmlHU6yi4gOZ4cyEYS61tvbBKw2FC1DBOMwDVnvP_n1eiRNNsGLM79cVD1ELvdF7odgJkJXa68xcEfgUtTdEKVlbNsQEwcTlxmjhVQKv7RVAlqSyLrs94dEW3vetcEliM2uCaa2Yi30cklDyIVbkCD11ponxwL4CLbVGmyNP6JU31Pn89iWL4J2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29eaab8d0a.mp4?token=kG5FkHiYd3TzJXP9cH_2hdI0E6IX2D2QiWCECfaYVO8fR6Ihiat0hC7fUv1pgh5k5MuZP_T5fzRwQHwzscEzu_J67UdDiLgDi4hXDyhSmm7ldNyPJi1VW11lBnigvqwsImKboC41Img1yjzyqkK6cCph26i_uoFmlHU6yi4gOZ4cyEYS61tvbBKw2FC1DBOMwDVnvP_n1eiRNNsGLM79cVD1ELvdF7odgJkJXa68xcEfgUtTdEKVlbNsQEwcTlxmjhVQKv7RVAlqSyLrs94dEW3vetcEliM2uCaa2Yi30cklDyIVbkCD11ponxwL4CLbVGmyNP6JU31Pn89iWL4J2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخعی، نماینده مجلس: بخشی از قاچاق سوخت، «رسمی» و با مجوز انجام می‌شود
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/681150" target="_blank">📅 17:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681149">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر ورزش: وزارت ورزش وظیفه ای در قبال ساخت ورزشگاه برای تیم‌ها ندارد.
🔹
شورای تامین استان خراسان رضوی: در درگیری دو هیات عزاداری در مشهد دو نفر مصدوم شدند.
🔹
ارنست مونیز، وزیر انرژی اسبق آمریکا: ترامپ با جنگ ایران، آمریکا را در بن‌بست انداخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/681149" target="_blank">📅 17:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681148">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ساحل شیب‌دراز قشم از آلودگی نفتی پاکسازی شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/681148" target="_blank">📅 16:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681147">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
طلا از ویترین جواهرات به قلب هوش مصنوعی رفت!
🔹
گزارش جدید شورای جهانی طلا نشان می‌دهد که تقاضای کل طلا تقریباً بدون تغییر و در سطح ۱۲۶۹ تن باقی مانده اما ترکیب این تقاضا تغییر مهمی کرده است.
🔹
این گزارش می‌گوید که تقاضای جهانی جواهرات به پایین‌ترین سطح از دوران کرونا سقوط کرده است.
🔹
جواهرات تنها ۲۷۸ تن تقاضا داشته‌اند، در حالی که مصرف طلا در تکنولوژی به ۸۰ تن رسیده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/681147" target="_blank">📅 16:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681146">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z66LeohsuY35PCft0wa3PrdGQvP96AOdMncZ_-kZP3zalLL1t2Gu1zCRillxk_pQ1a-gKZJXthQV7U9Y-NOJOBv_3IthRErlV10UsfJ_CdgpYb0DkOYIxbOng3xNcFLLzQ5_mixrPWIEV1hRn-C6LRbKDUMFc0SK3gTKlhMxVRSyDaz8dLy6JJAUGRL_pHe7gxxd4ISrbwhHKVQ1c4GboWdse0yvmwgMgPt9hLeIHEeeS1jybPGmDRXSspE7Ho9mN0B4kd-FoaMwUEzjrb6gWHDffItp9pbq3qpdnl1_AeYKJLD9uq5pNKiWnj9wDGFiTE9xuQmJDsKZYUlERAFFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان پروژه تلاوت کل قرآن کریم در مقام‌های مختلف توسط حامد شاکرنژاد
🔹
حامد شاکرنژاد همزمان با حلول ماه ربیع‌الاول، از پایان پروژه تلاوت استودیویی کل قرآن کریم در مقام‌های مختلف خبر داد؛ مجموعه‌ای که به گفته وی، برای نخستین‌بار در جهان اسلام با این گستردگی رقم خورده است. انتشار قطعات این مجموعه به‌تدریج در بسترهای مختلف ادامه خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/681146" target="_blank">📅 16:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681145">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e043d4302a.mp4?token=l0wMvotV6P7mCver6NtFCvlU3tM4Wiwqra-yfZmE04sYcrGXKr4O93BuP8IDjMSazQBSCBNcIvwh7YAFfkRT2nZ9CLUFY_9vhRkfvEOXazdWISbbzBi4FeJ4jDRMyyAFOTeQ0xzicMCNwcytBC0RuOZ6DWtceEbqzumb-CXaG2Jte0CIitDCKocrETq6Sl8UqgEuGwvdjb22YcL1tBESn4KP8teGfz6d4Wkv8QbI-mmnqMqllD4gzg6GJ98zVBEBS4qBv_cJ-eV7lrQdmM5lVbX84PlNsLo-LDbm0ExWJYn9CgPUfIFqYRzmioMKzfXxYbgH1WBtg8sA6HKxGC0ldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e043d4302a.mp4?token=l0wMvotV6P7mCver6NtFCvlU3tM4Wiwqra-yfZmE04sYcrGXKr4O93BuP8IDjMSazQBSCBNcIvwh7YAFfkRT2nZ9CLUFY_9vhRkfvEOXazdWISbbzBi4FeJ4jDRMyyAFOTeQ0xzicMCNwcytBC0RuOZ6DWtceEbqzumb-CXaG2Jte0CIitDCKocrETq6Sl8UqgEuGwvdjb22YcL1tBESn4KP8teGfz6d4Wkv8QbI-mmnqMqllD4gzg6GJ98zVBEBS4qBv_cJ-eV7lrQdmM5lVbX84PlNsLo-LDbm0ExWJYn9CgPUfIFqYRzmioMKzfXxYbgH1WBtg8sA6HKxGC0ldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسیر شگفت‌انگیز راه آهن دورود به اندیمشک
🇮🇷
#ایران_زیبا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/681145" target="_blank">📅 16:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681144">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
استعفاها در حزب نتانیاهو در پی رقابت بر سر کرسی
🔹
کانال عبری‌زبان ۱۴ رژیم صهیونیستی با اشاره به استعفای چند عضو حزب لیکود نوشت که تنها لحظاتی قبل از انتخابات مقدماتی حزب نتانیاهو، رقابت برای کسب جایگاه و کرسی تضمین‌شده در فهرست لیکود، منجر به موجی از استعفاها در این حزب شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/681144" target="_blank">📅 16:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681143">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سخنگوی کاخ سفید برکنار شد
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا در اطلاعیه‌ای رسمی از برکنار کردن «کارولین لِویت»، سخنگوی کاخ سفید، در پایان ماه اوت میلادی خبر داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/681143" target="_blank">📅 16:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681141">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH9apSm7QrcxKe8tRgtsQTvQjxXAdMf1DVZrNqRIdY6SnJsrjUnZHx_lIxGqSzIhenKh4BoJc1tshcdKb3Q4rQLjk6MGqls-pd-NDqDeXBxSU9G0Z-n7LnLgifuphY5fAjdVi5Uc3bjactfb_0Sgwr_uRKzj1B-p4W5umqkHICxPMBSRN9y4wjTvR5-QBAhmAUPuHK2HewiSvlAJDJkqkIcVs7A9ZX7AczjnD_-xz4vnqQmOBDBKDNS_UhALhHvCn1w_PxnZvQ-VNyquJE6S27yEYfqCubmnPbCtvQH3YA0gNImq1os3bzPJy0v_C3mWGcxtc9OlS4cAl4NjmH9h2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر برای یوتیوبرها؛ درآمدزایی سخت‌تر می‌شود؟
🔹
گزارش‌های تأییدنشده از احتمال تغییر شرایط ورود به برنامه درآمدزایی یوتیوب از ۱ فوریه ۲۰۲۷ خبر می‌دهند.
🔹
بر اساس این ادعا، حدنصاب تماشای ویدئو ممکن است از ۴۰۰۰ به ۸۰۰۰ ساعت و بازدید Shorts از ۱۰ به ۲۰ میلیون در ۹۰ روز افزایش پیدا کند.
🔹
هنوز هیچ‌کدام از این تغییرات رسماً توسط یوتیوب تأیید نشده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/681141" target="_blank">📅 16:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681140">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsVDZyQumAOv_8VkYcUqbPc05egb-LfuEbSB8rOPAsaVHu6h_kxdP3PDV9hsygbTlU6d1XiPRjlkU4Lc1Uo0bX9LezcgEdX5kltkBkYc0jHuC2785_lTSbjRK0CljVmccovlxbJeoVu21M8OTNkkvJz0UHcacIW86jJ09dChEpg8dRrSBELRgRsL7jHX8Xr6z3gxD1klJHUbfCZupF4HNLe2K85Cz7oCwAyVhdOipoIylDKYUQv-I4dnB9UcrMuaL_oXsBvBT-476E8eJY9AxpOyt1VA6GkZLSHdQeRY3oaFZK8Q-zBF9akNCkqGwAuVCQegQdPM1ECjdGvAOpZ6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصر، ترکیه و عربستان در رستوران تحولات منطقه را بررسی کردند
!
🔹
وزرای خارجهٔ مصر، ترکیه و عربستان سعودی در شهر ساحلی العلمین مصر دیدار و دربارهٔ آخرین تحولات منطقه از جمله تنش بین ایران-آمریکا، راه‌های کاهش تنش‌ها و تقویت همکاری‌های امنیتی و سیاسی گفت‌وگو کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/681140" target="_blank">📅 16:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681139">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی باشگاه پرسپولیس</strong></div>
<div class="tg-text">💥
از نسلی که ساخت،
برای نسلی که ادامه می‌دهد...
پیراهن جدید پرسپولیس؛
با امضای تاریخ
🙌
❤️
❤️
@fcpersepolis_club</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/681139" target="_blank">📅 16:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681138">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ_M0ktuP4muDWE_Z7G6BjgPeP2JypYYTlWKbZ88XhYu09t6PQYSiy8tTJJP4kSIif7VLId0YtEcjg0fuZZmMmREvqwZ7e-kg6H7DhtrSd2_Kgsl_8w8Tv3uTUTdpA51NAa4WgoLPbNgF1harmE0-8lTqU_s34-nkViEikDi2k7xLcjqP4C6QsErMCJTdBT3ctXBLzSNyPe-eo-dO4MxcpVNNNHe0HHLBRCd7K51urBMiwgofHiLNF91GNAEvn__2mR0ROlWV6ICblUk6hb89qFuDwMK9oKKeQCMZuHxFe2FEzlMWMbHPTSUQPCRaqIKFlibK1_Tmit1zIKz65NFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موضع یوسف پزشکیان درباره حملات اخیر به دولت
🔹
برخی شمشیرها را علیه دولت تیز کردند؛ آنها سربازان شیطان هستند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/681138" target="_blank">📅 16:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681137">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک بحران بی‌صدا در موسیقی ایران؛ به آخر خط رسیدند!
🔹
حال موسیقی خوب نیست؛ پشت این سکوت، یک بحران آرام در جریان است.
🔹
۸ ماه است سالن‌ها خاموش‌اند و هزاران نفر از اهالی موسیقی، بی‌صدا هزینه می‌دهند.
🔹
اما این فقط یک تعطیلی ساده نیست…
پشت پرده چه می‌گذرد؟ ویدئو را ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/681137" target="_blank">📅 16:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681134">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
عملیات حشد شعبی برای سرکوب بقایای تروریسم در صحرای غربی عراق
🔹
نیروهای حشد شعبی عملیات امنیتی برای شناسایی و تعقیب عناصر فراری داعش را در صحرای الثرثار در شمال الرمادی آغاز کردند.
🔹
این عملیات شامل جست‌وجوی تونل‌ها و مخفیگاه‌های زیرزمینی تروریست‌هاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/681134" target="_blank">📅 15:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681133">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اول اصلاح مصرف، بعد اصلاح قیمت؛ راه توقف واردات بنزین
محسن بیگلربیگی،کارشناس حوزه انرژی
:
تا زمانی که هزینه تولید هر لیتر بنزین داخلی حدود ۸ تا ۱۰ هزار تومان و هزینه تأمین بنزین وارداتی حدود ۸۰ تا ۹۰ هزار تومان است، نخستین اقدام منطقی برای کاهش فشار مالی و ارزی بر دولت، باید قطع وابستگی به واردات باشد؛ نه افزایش یک‌باره قیمت برای همه مردم.
امروز روزانه حدود ۱۳ میلیون لیتر بنزین به‌صورت مستقیم وارد می‌شود که سالانه نزدیک به ۴٫۷ میلیارد لیتر و حدود ۳ میلیارد دلار هزینه ارزی دارد. با احتساب ریفورمیت و افزودنی‌های مورد استفاده برای جبران کسری، هزینه ارزی تأمین بنزین به حدود ۶ میلیارد دلار می‌رسد. ⁠￼
این در حالی است که کشور تا سال ۱۴۰۱ بدون واردات گسترده اداره می‌شد و در سال ۱۳۹۹ حدود ۳ میلیارد دلار بنزین صادر کرد. بنابراین کسری فعلی الزاماً مسئله‌ای غیرقابل‌حل یا ناشی از کمبود ذاتی ظرفیت کشور نیست؛ بلکه بیش از هر چیز حاصل رشد بی‌ضابطه مصرف، خودروهای پرمصرف، فرسودگی ناوگان، تضعیف CNG و کمبود حمل‌ونقل عمومی است.
راه‌حل عملی برای اصلاح مصرف
🔷
احیای فوری ظرفیت CNG
ظرفیت عرضه CNG کشور حدود ۳۵ میلیون مترمکعب در روز است، اما فقط حدود ۱۵ میلیون مترمکعب مصرف می‌شود. استفاده از همین ظرفیت خالی می‌تواند تا حدود ۲۰ میلیون لیتر از مصرف روزانه بنزین را جایگزین کند؛ یعنی بیشتر از کل واردات مستقیم روزانه. اولویت باید با تبدیل رایگان تاکسی‌ها، وانت‌ها، خودروهای اینترنتی و خودروهای پرکار باشد. ⁠￼
🔷
اسقاط خودروهای فرسوده با منابع صرفه‌جویی ارزی
مصرف خودروهای فرسوده گاهی به ۱۶ تا ۲۲ لیتر در صد کیلومتر می‌رسد، درحالی‌که خودروهای جدید داخلی حدود ۸ تا ۱۰ لیتر مصرف می‌کنند. دولت می‌تواند بخشی از سه میلیارد دلار هزینه واردات را به تسهیلات اسقاط و جایگزینی اختصاص دهد. ⁠￼
🔷
الزام خودروسازان داخلی به کاهش واقعی مصرف
خودروساز باید براساس مصرف واقعی محصولاتش جریمه یا تشویق شود. هزینه تولید خودروی پرمصرف نباید از طریق افزایش قیمت بنزین از مردم دریافت شود. تولید خودروهای با مصرف بیش از استاندارد باید مشمول عوارض سنگین شود.
🔷
آزادسازی واردات خودروهای کم‌مصرف
نمی‌توان واردات خودروهای باکیفیت، کم‌مصرف و هیبریدی را محدود کرد، بازار را در اختیار خودروهای پرمصرف قرار داد و سپس مردم را به‌دلیل مصرف بالای بنزین جریمه کرد. واردات هدفمند خودروهای اقتصادی و کم‌مصرف، ضمن ایجاد رقابت برای خودروسازان داخلی، مصرف سوخت را کاهش می‌دهد. بخشی از ارزی که امروز صرف واردات روزانه بنزین می‌شود، باید به نوسازی ناوگان و واردات خودروهای کم‌مصرف اختصاص یابد؛ زیرا خودرو یک‌بار وارد می‌شود، اما بنزین باید هر روز وارد شود
🔷
هدف‌گیری خودرو، نه عموم مردم
سهمیه پایه یک خودروی خانوار، تاکسی‌ها، وانت‌ها و مشاغل حمل‌ونقلی حفظ شود؛ اما خودروهای دوم و سوم، خودروهای لوکس و مصرف‌های بسیار بالا از یارانه کمتری برخوردار شوند.
🔷
قیمت‌گذاری پلکانی مصرف مازاد
به‌جای افزایش قیمت همه سهمیه‌ها، مصرف متعارف با نرخ حمایتی باقی بماند و تنها مصارف غیرضروری و بسیار بالا به‌صورت تدریجی با نرخ نزدیک‌تر به هزینه واقعی محاسبه شود.
🔷
توسعه حمل‌ونقل عمومی
واردات اتوبوس، تکمیل مترو، نوسازی تاکسی‌ها و توسعه سرویس ادارات و مدارس، باید از محل صرفه‌جویی ناشی از کاهش واردات تأمین مالی شود. مردم زمانی مصرف را کاهش می‌دهند که جایگزین قابل‌اعتماد داشته باشند.
🔷
پایش هوشمند انحراف و قاچاق
مصرف‌های غیرعادی، کارت‌های سوخت پرتراکنش و خروج سوخت از شبکه باید هوشمندانه کنترل شود؛ بدون آنکه مصرف عادی خانوارها محدود شود.
🔷
برنامه ملی کاهش روزانه ۱۵ میلیون لیتر
دولت باید یک برنامه دوساله با هدف‌گذاری شفاف ارائه کند:
* ۷ میلیون لیتر کاهش از توسعه CNG
* ۳ میلیون لیتر از نوسازی ناوگان فرسوده
* ۲ میلیون لیتر از بهبود حمل‌ونقل عمومی
* ۲ میلیون لیتر از کنترل قاچاق و مصارف غیرعادی
* یک میلیون لیتر از استانداردسازی خودروها و مدیریت ترافیک
با تحقق همین برنامه، واردات مستقیم ۱۳ میلیون لیتری متوقف می‌شود و کشور دوباره به تعادل می‌رسد.
اصلاح قیمت بنزین شاید در آینده بخشی از سیاست انرژی باشد، اما باید آخرین حلقه اصلاحات باشد، نه نخستین تصمیم. ابتدا باید واردات را با اصلاح خودرو، توسعه CNG، نوسازی ناوگان و حمل‌ونقل عمومی متوقف کرد؛ سپس درباره قیمت تصمیم گرفت. نمی‌توان خودروی پرمصرف به مردم تحمیل کرد، امکان استفاده از حمل‌ونقل عمومی را فراهم نکرد و در نهایت، هزینه همه ناکارآمدی‌ها را با افزایش قیمت بنزین از مردم گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/681133" target="_blank">📅 15:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681132">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آمریکا به فرار خود از منطقه سرعت دهد
🔹
آمریکا را تا شکست نهایی رها نخواهیم کرد.
🔹
امنیت مردم ما را به خطر بیندازند، امنیت آنها را در سراسر جهان سلب خواهیم کرد.
🔹
آتش‌بس را در جنگ رمضان آمریکایی‌ها التماس کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/681132" target="_blank">📅 15:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681131">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سخنگوی آموزش و پرورش: آموزش در سال تحصیلی جدید به‌ صورت ۱۰۰ درصد حضوری است؛ تقریباً تمامی مدارس آسیب‌دیده در جنگ تعمیر و بازسازی شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/681131" target="_blank">📅 15:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681130">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای‏ وزارت امور خارجه کویت: ایران به دو نفتکش متعلق به شرکت ادنوک امارات متحده عربی در حین عبور از تنگه هرمز حمله کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/681130" target="_blank">📅 15:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681129">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📍
رستوران پدیده شاندیز
وقتی یک طعم، میتونه فاصله‌ی بین گذشته و امروز رو از بین ببره !
👑
⏳
وقتی پای غذای خوب وسط باشه، ماجرا هم عوض میشه!
😋
📱
رزرو و هماهنگی : 09153181815
📍
آدرس : شاندیز، نبش ولیعصر ۱۱
https://www.instagram.com/padidehshandiz.restaurant</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/681129" target="_blank">📅 15:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681128">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TslVcvz8559YgM-7qVGtB4wQNszUP7WmfhgObXsou5Sj20R_G0i8TQGZPYt1FAaVCSj13bIXn1iQfzAUuD-q7tld_wB8zGWj6ie37V-RXqqIRUFeO-7A5OJU4g728e8cvqIuuqZZGrUmeR1kSlo-DYJLdocK1MZTNVEbURl-C6PQjnMyDUv9YqdbzEj-olkYlfBEmc9EFb55YzEjF_tod0cgAb6vP_hjnFnseZxEIeMhVu_Jr2CNXDQgKZwu4-N4GvGtIglc_6cDBxLLCPBz3I1hCbQr1YVKT93Ed58a4Yt2ejIKYIa-fR6iOS8RBZXwiKIG5uYzANJEI2mH7Jshag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
منشاء بنزین ۸۷ هزار تومانی در کرمان مشخص شد
▫️
خبرآنلاین نوشت:
▫️
پس از گذشت ۲ روز از موضوع بنزین ۸۷ هزار تومانی، حالا مشخص شده این طرح مصوب شورای تامین و ستاد مبارزه با قاچاق کرمان و استانی بوده است.
▫️
از آنجایی که سهمیه کارت‌های آزاد این استان عمدتا قاچاق می‌شد و به دست مردم نمی‌رسید، استاندار از مرداد تصمیم گرفت کارت‌های آزاد را جمع‌ کند.
▫️
با جمع‌آوری کارت‌های آزاد، سهمیه این کارت‌ها در قالب ۴۰ لیتر سهمیه ۵ هزار تومانی به کارت سوخت شخصی مردم واریز استان شد. برای مازاد نیاز بخش اندکی از مردم استان هم استانداری درخواست کرد بنزین با نرخ پالایشگاهی در جایگاه‌های سوخت عرضه شود.
▫️
جالب‌تر اینکه طبق آمارهای موجود با اجرای این طرح در مردادماه، مصرف بنزین در کرمان ۱۲ درصد کاهش یافت و صف‌های بنزین جمع شد و دست قاچاقچیان کوتاه ماند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/681128" target="_blank">📅 15:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681126">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVmV-lIZtL7meSEAUktDDwD6X6NoAdykP-o48OEMPD7ZB4PHjagA6kWdOkEliCVrUiQ-RY93UOnyvEcw6qeNCbtp4wZhFI9mAtc09QnNMZA9itzURDlngAqGh-NitO4o_bxCakcXwek9gXIgodWjq3mhNkbT-yUp7YovHpGVLjfMSpOStD3zUMzrZf1-LuXxQjJIf-kO4tpjwvHDUQcWP6TgkwTH0lCUJQHjiBPvapcxjDgTHDDshhjvLKlOcUI7S7JygTrUD9SrYIul_aWA0ghaYoXEUnJbBdjbMJwpKwyK9IMwTND4ifsqHxYSiozVy5nyBpq9wGjdJFGJX4Z4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارس: روز گذشته ویدیوهایی از برخورد تعدادی از عزاداران در مشهد مقدس منتشر شد که در آن چوب‌هایی به سمت هم پرتاب می‌شد
🔹
این فیلم‌ها بلافاصله با آب و تاب فراوان در رسانه‌های ضد انقلاب دست به دست شد و به نادرست القا کردند که این درگیری در صحن حرم مطهر امام رضا(ع) رخ داده است.
🔹
بررسی میدانی نشان می‌دهد که این ویدیوها مربوط به فضای بیرون از حرم مطهر است. در داخل حرم رضوی، اساساً اجازه حمل هرگونه چوب داده نمی‌شود و محیط با بازرسی دقیق کنترل می‌شود؛ بنابراین، نسبت‌دادن این اتفاق به درون حرم، تحریف آشکار واقعیت است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/681126" target="_blank">📅 15:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681124">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mj8Rn5vLvpWApt8RB0PIbhP08rS9jTqz3jXweCwFHrm65WpAeSVq2lnMUFDvn7rbZBI8oVa1oXnXG4vbKgWHpibash1EuGI2YFMsH2hGLEsKlMyVDAnPGAtlIaGKzBS9OfcQikK3qAo-JmdNAvpU4v-8KLZarTe0BBdGe1aQONhYzOQjyCwIe5j8G5ilixYUjEhiL101Th8m3pYTRVKN4TVIKaqOFusGAg3Rrf0vuN-HrWcYnYYmjjRoXjhclFS2HjLRo7CrWlzNpVNDQt3Bu0B9wSkhAAVsN_mzrVbd6H3QJ1EFFNlheE7SBJm4R9PU9VIWufwQTF0ZymqKCY8uTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rR9lLTdehCauDrjV6WFjv6a1fzSHFwg-T8NaBB5iUvuJBEc3jE25MwZ-KqyyNCsaRCcuIhNWm0UY3Lw9edv83j_CV6lmMchyzR88HAHk69w-mgn8HZPERHpzG65uOaku2wUIt7DOzKjXOD0cCMSAb9kdjvX5PA_m6j-WTLaj4dMdw1so2bhs5LuMpC0JzxZFs02QEmop70ggjvbExY9lA_nw13-fYr6F9CVaNmWkN9H8hjkf3WJAGadfK-5P5XLHM-qN1KCKxXtCQR5qNj2EI7PmHUog0El6KhdsDdk80wVECMLMparbtheVaG2LeX3FpRmrJ6lAwcK8JZiTqz3vPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میزان استفاده و هزینه ماهانه کاربران ایرانی برای فیلترشکن
🔸
بر اساس آخرین نظرسنجی مرکز افکارسنجی ایسپا، ۷۴ درصد از کاربران اینترنت در ایران از فیلترشکن استفاده می‌کنند که ۶۶ درصد آن‌ها از ابزارهای رایگان بهره می‌برند.
🔸
۱۸ درصد از کاربران ماهانه کمتر از ۵۰۰ هزار تومان برای خرید خدمات فیلترشکن هزینه پرداخت می‌کنند.
🔸
در نهایت ۶ درصد کاربران بین ۵۰۰ هزار تا ۱ میلیون تومان و ۶ درصد دیگر ماهانه بیش از ۱ میلیون تومان را به خرید فیلترشکن اختصاص می‌دهند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/681124" target="_blank">📅 15:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681122">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNn-Y6KdaZXkkhdfUepz4YoITvk3VHPY9gyPyruB9icn9sAiiRMVisFCooqktrWJt1ZMPiIl0e1I27Tt2ENkXGevUsOdT_NcDz_3XWRFPO0w9lUvD0LbYqVuwwP6WYUwQb6WAbj-_CERk9D-1dfEJZxuKCcqHOznA4yzy-aj2cvPo5dyleYpji2aU2gLAVrv806_X2i00ePPGO2pHgfpD3MG_AACqdvV8C_61YwfJhKVdNizSyUr2ZBKTiCvXi4iwHRGvKKy6EYPHh-31w1jusEXgN2A9kbZgyAy4fl8o0moekgBCsoOX8wCsUIRBWEyuWy_iecPywReNXUYpSa9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: مذاکره‌کنندگان به توافق با ایران برای باز کردن تنگه هرمز نزدیک‌تر می‌شوند
ادعای وال‌استریت‌ژورنال:
🔹
ایران و عمان در حال نهایی کردن پیش‌نویس توافقی برای بازگشایی تنگه هرمز بودند که به تهران اجازه نظارت بر کشتی‌هایی که وارد خلیج فارس می‌شوند را می‌دهد، اما اجازه نمی‌دهد عوارض یا هزینه‌های خدمات دریافت کند.
🔹
طرفین در مورد نکات اصلی پیش‌نویس که یک خط ورودی در نزدیکی ایران و یک خط خروجی در نزدیکی عمان ایجاد می‌کند  توافق کرده‌اند و آن را با آمریکا، کشورهای منطقه و رهبران ارشد ایران به اشتراک گذاشته‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/681122" target="_blank">📅 15:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681121">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfLYzcHXrGcH7VjsTN6eqSgCNcqEu62csX2m9yek5vBcrOZqbD2dTRUjcDU3LfmchOijZOrW--9x93wavi9ec4iwhp85tqHQR6YMPwZL8pxsPBW2ZjAeG3bSZYIQeoCOQUGgftUHm2IfNrjAfk4NyyfvVqcezyuOqVq8yZxv6fMsnj5MnwUG6E0jdNdm-nE_PTh4N1X4zm-fXMNWvW6yIWK6egb0u50Nu2BYBewKdmvAmeVz4tXWayfbUBeWjaUUq24l-TP65DwCLp0kuS1OTdxKddCJbhrip-in6PQgI3jWEQzIIc9DGS5RI0AJSioGBR5qIBNqXgwkUdTDWBuvjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توضیح رئيس مركز ارتباطات و رسانه آستان قدس رضوی پیرامون ماجرای منع شعار مرگ بر آمریکا در حرم رضوی
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/681121" target="_blank">📅 15:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa699bdd56.mp4?token=j_VxKRFA2Y3Senk609xQn2k-fuUjes-xPp4qcFcPkkNl9Lc3Tq6HzShd-Hh4F6B_RxYEQlEsTe5gHmjS3Zx5thhmYO76GD35Axmb_IVeVixOfvOW1koyIOT-F8W7xjDkZw7SmWThaSytob-OWoamsEGs_AQTmoE6tn0oQyKO0uDLQoj_ay0xzdLPKKEmlgK6xOCg4vf1SOBHaRHdr4LRAfs8y55ob2rhdF9VOSL7hs5r8dTa3RtBNs3L3PwWgJg7N8wzXOzxQskachXvjFUrq8LhMOOVSwntjMnTU0Oyh4sgkhh0CtsQIHsxW6AbvvEUdm5OUsJ3STWEKM-4oEXWPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa699bdd56.mp4?token=j_VxKRFA2Y3Senk609xQn2k-fuUjes-xPp4qcFcPkkNl9Lc3Tq6HzShd-Hh4F6B_RxYEQlEsTe5gHmjS3Zx5thhmYO76GD35Axmb_IVeVixOfvOW1koyIOT-F8W7xjDkZw7SmWThaSytob-OWoamsEGs_AQTmoE6tn0oQyKO0uDLQoj_ay0xzdLPKKEmlgK6xOCg4vf1SOBHaRHdr4LRAfs8y55ob2rhdF9VOSL7hs5r8dTa3RtBNs3L3PwWgJg7N8wzXOzxQskachXvjFUrq8LhMOOVSwntjMnTU0Oyh4sgkhh0CtsQIHsxW6AbvvEUdm5OUsJ3STWEKM-4oEXWPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هموطنانی که در خصوص کالابرگ، پیامک احراز سکونت دریافت کردند تا اطلاع بعدی به دفاتر پیشخوانِ دولت مراجعه نکنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/681119" target="_blank">📅 15:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6549c7ebc.mp4?token=gkkNRFiB_zo1Pzq8krVuqjQo5RGKgcAaknIN8r8a88kfoNpnLtg3sPqNeTiHNq84QXkNWcSy_EIKfjaVMKo3LIL1dCG8z-K6fRU7KrrGJbCH62MQc5JLpRcBkGgj_K6Wt6fqtpjly0b1pvDwFwvOW1ANYvitQwPUY1AH8IgeQLVA75tnvRGQhvIjU_-JClJZ6oHoLAiq5GDeG-H0geYiK-UBnn5bXxA0xV9q33aKFgiJRpRCZZbv67DATt-5rpVlnh26zpe7dO0sgSESmY0KBSEKo_0lBOfa-DbeGdedH2oQx6WdhcATUawg0YxkkRQ6nW-3xXue7CyyIgfxdwPadg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6549c7ebc.mp4?token=gkkNRFiB_zo1Pzq8krVuqjQo5RGKgcAaknIN8r8a88kfoNpnLtg3sPqNeTiHNq84QXkNWcSy_EIKfjaVMKo3LIL1dCG8z-K6fRU7KrrGJbCH62MQc5JLpRcBkGgj_K6Wt6fqtpjly0b1pvDwFwvOW1ANYvitQwPUY1AH8IgeQLVA75tnvRGQhvIjU_-JClJZ6oHoLAiq5GDeG-H0geYiK-UBnn5bXxA0xV9q33aKFgiJRpRCZZbv67DATt-5rpVlnh26zpe7dO0sgSESmY0KBSEKo_0lBOfa-DbeGdedH2oQx6WdhcATUawg0YxkkRQ6nW-3xXue7CyyIgfxdwPadg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صندلی‌های قطارهای ژاپن با یک حرکت ساده تغییر جهت می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/681118" target="_blank">📅 15:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681116">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
رکورد جدید مرگ‌ومیر ناشی از گرما در آلمان
🔹
تعداد مرگ‌ومیرهای ناشی از گرما در آلمان در تابستان امسال (۲۰۲۶) بار دیگر رکورد زده و بر اساس گزارش هفتگی مؤسسه «روبرت کخ»، این رقم اکنون به ۱۲ هزار و ۵۰۰ نفر رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/681116" target="_blank">📅 15:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681114">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiM6YqgKpD8egFGBY3c49AGZZJvShQHQXwt7gXbx846mOtDLSkemoEBiLDf3FnINqFNZNJOVSybh7IBAFi6fgJXmlyTfERg8moyYf4KyykU9zyZMF-bD5edfEOZ-37P8sNPjIWdy-8_HN78x8JizAZgF-KlJ3nmINRLQE7H9bry8UtX3AFuqdOLVv0lzhbcsmkqWgN6EoGQHNphUwuho-AxBbX66sLv4Fxb0udRtR-2N5MR7zU4dOB3WiVJNOqMEr9F2ZljahQLoZR8J6_Mmmaa7pRCuU9c1CSXJ6M10fsk0FVHa-7MLzAE-08S3knbRhohWwbMNg109Y-PJuZ5ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشتی ۲۳ میلیارد دلاری ترامپ | جنگ‌افزاری که پیش از ورود به آب از رده خارج می‌شود
🔹
نخستین ناو جنگی از کلاس جدید «ترامپ» هنوز ساخته نشده، اما برآورد هزینه آن به ۲۳ میلیارد دلار رسیده است؛ رقمی که احتمالا توجه زیادی را در واشنگتن جلب خواهد کرد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3237298</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/681114" target="_blank">📅 15:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30566acdff.mp4?token=mtvIpPeTQbGUPaBW6sjpiNe73YSGHEWtFKQyoDPESiFTdOISwvLwl6o52Faa-OdwUULvNVF4aIzr6aSzN3bzdyK4ouLw4A6C3VBj2iRGUnuj18_Y7fcrxjjAMyggkfKIwOXYdYkiyoh05Zmn6wT3tHwtl_pUTNSjphQWoT-knvb-9_Jft94aQsN-4R7Sxa5oZ1gBe1bqkNcDLmhsq4EzM2m-iRSrNeO6xaZX8CHSrgFH8oKWtHpq3hpbmlKGxJ93y35xCQQoiNd7PtD7oGhia_kcTTzjJsKhEqzfqxGyKkyMBH3EDYkBL1Cg21ZRgmDOQwYj_shLCTG1K9IrSD3Zjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30566acdff.mp4?token=mtvIpPeTQbGUPaBW6sjpiNe73YSGHEWtFKQyoDPESiFTdOISwvLwl6o52Faa-OdwUULvNVF4aIzr6aSzN3bzdyK4ouLw4A6C3VBj2iRGUnuj18_Y7fcrxjjAMyggkfKIwOXYdYkiyoh05Zmn6wT3tHwtl_pUTNSjphQWoT-knvb-9_Jft94aQsN-4R7Sxa5oZ1gBe1bqkNcDLmhsq4EzM2m-iRSrNeO6xaZX8CHSrgFH8oKWtHpq3hpbmlKGxJ93y35xCQQoiNd7PtD7oGhia_kcTTzjJsKhEqzfqxGyKkyMBH3EDYkBL1Cg21ZRgmDOQwYj_shLCTG1K9IrSD3Zjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقف یک مرکز خرید در شانگهای چین، در اثر بارندگی شدید فرو ریخت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/681113" target="_blank">📅 14:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
انهدام پهپاد MQ۹ در آسمان هرمزگان
🔹
یک فروند پهپاد MQ۹ توسط سامانه نوین پدافند پیشرفته سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان استان هرمزگان رهگیری و منهدم شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/681112" target="_blank">📅 14:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e90965dd.mp4?token=ZINqA4-C04oc0THVLRh6gEgLXo044ZdFByJGSriFddcGyAFrdaRtb02g-H6T3yDbBsor1QVSFnXDGteMlTJFNN1EabqYhzdS2BEhiL-Jt3xVkbBxhWFfboMov5KdaPVBvLl5fIWcLrWKr6F_E03J6C6eW0zxkZqC4_2A0AWWbYfIE0cClJYBdFfO0f0jZUk8sgUq2Sj9SmgtlizdO8fpxXXPZa07ev7377gJTiNZS8YEOOTvaKNRWGXmmsuJKJy-NYvPwJTFYib-DA8OkRwVV7u_8_Z89zOKdwI-xzxd8338gJLHH_TwtFPULv7AfeNxnCftSsJAv7ufOmnXQZrlBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e90965dd.mp4?token=ZINqA4-C04oc0THVLRh6gEgLXo044ZdFByJGSriFddcGyAFrdaRtb02g-H6T3yDbBsor1QVSFnXDGteMlTJFNN1EabqYhzdS2BEhiL-Jt3xVkbBxhWFfboMov5KdaPVBvLl5fIWcLrWKr6F_E03J6C6eW0zxkZqC4_2A0AWWbYfIE0cClJYBdFfO0f0jZUk8sgUq2Sj9SmgtlizdO8fpxXXPZa07ev7377gJTiNZS8YEOOTvaKNRWGXmmsuJKJy-NYvPwJTFYib-DA8OkRwVV7u_8_Z89zOKdwI-xzxd8338gJLHH_TwtFPULv7AfeNxnCftSsJAv7ufOmnXQZrlBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر پهپادها و جنگنده‌های منهدم‌شده آمریکایی صهیونی توسط سامانه‌ی نوین پدافندی نیروی هوافضای سپاه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/681111" target="_blank">📅 14:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681104">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q3MKHeFQrtDsOhyGN6FFqqTp0rcdujIwBvlimbPWcILIAad_RTRrjDzK_jLDPDT0-67LehBMqcl2IdwIlRScp__nbqKdI71Lssa9VE-HXYmMCgAR-h6tw3DnT3Nci56muyFuHFZIXlOzPGsjpSXuslFvQmJwsPg3NoNAk6_tuQE_fT2_b15p0Xl9KvqMfRHYkRpwTph1Ly_le4yIKDxSMe2xhRLN5G6QyOWC6aYukoEaPXdu8-G2Hn2qq-1v5mD3gQ9UBexAoRjxP-QYQ20NgswtwFQkV-xwhgfyvyZ2ZL81VsSCZMGEPOwxJ7QBXv-KReX15rfqC-2gHG3uwZ0cVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kC3Od-VHZRINE_pYxk7SHsrRFdasKmC87PXQir5F8MvJAvZkvbFEQpwKwW4V0niJaKtx2P1y1ycDnK1gFiG-kJxyUFoXJaFoNx3D8wq521HPWGuy7ZcnpAg1pV6fBD1JamSECMA7aRYyf1fVXBZ4ra2PmY9DG-g1h9Lb2olsYFFc9nSMINyxaMZlaoShswZ3XA2UJCOtZ4afMHvPt1S4a1lVBDs2ywT8e4iD4EgYiGEnFze6meDGodtqPLVNDlaKSr6ymPAOvu0bCcMD2WzSHhc-rAPNH4R9qRgEgJ-d9lnx72wII__9DnRekDoJ0U_ezFcUOPoLXmS7XpPpt5Bv4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUBzXMuAT0PcXyYdckUF8B13-lRcbscrQ_IhxGF1qOA479wBjiwFY3Ju4lT4ABjzj8389Abudv-SnuM9u1-pRHEzGnP3W6igzU-jte4QMkN97ReLhyQG4QasiNo49l26demvKv_Fuptn-MmdfW9ozwT5LvfK8woR_21-LhWSy1kxfg7GZ-PvsEkgjlX6TffyztloupPptqiqMDovSbhg_KXEBVLl0qfYwlQ8DbHuPcljn8pq8NDPhoFKc-A3EXHp2OlBzUhgDW053ORw3wYx5o2t3iggG7xgeclJGSD-_ZxfH7lJSH_54PLda2cI4ElIvi9ttl-yT0YRkWrgdIAqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEIx4XJ1n3uNM_V5xDmrTn1976LrBXhA-2laiqzAB8ahVQS93E-8ev5fxsbhI-L7siCKiHTXJQmvtcaB7q-lhjkYDCMPhWdCq_YZMlK37nSWr_HJIrtJErH1572eF-fW-a1hlhwI0J04btKwzbbPvRwGt_a2ggTGjj_fBO2C7mYoCQEjhrtOX_raSXirwPZ6nOAK6Ej8kc5d6F8W8g4jCCxlPBkdhYAFXTZBEtuGqaxeLzQYXUW2OwgJ_AcN2JGNcmi1KDMJ3OVxqfihmhthUPcUi8ND0_oM1jdwd5jSp-TWg0uUuJ3xOz8IA60Y1OU04Elzp9RoiAf1L3WBoFEQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnnCza72_N8R8k81yiDdho6Xi1OBNUfm-0G1Q_HHnIoEt0D3oqnaty3G6Wmm357dkvUMUwWM2cGFVSZ8ALSp1EYlD-9zYeDl8WifKfNgZ3MEl-csyzodDsmPYIcI2WivUYYSxO0UZgGaMuuIsxsiRAWmnyU-SoW5-sQCFQoCx5Ac-N-zhWSCrm_Eh47yNAv0bFrcAi8FIzhQmNTPWWQI37LFK3wk2ef4vjxPM_KV8599e-QyO3uAak1glZVBCmwFyrBEKz6OZymv3vzfiqQikuNIjmsX4y5GmU6vsSx1-K1xKReczUll4Jkf5AGW-Z49wOZ5I0qLAdp7TOXinXTQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCLyMwMRAAkQM3NZTRZ7mu1w_XlR3A8GaMsD3XMLrio_cp1qalSONjvkwwirhdWKOoJFRblG4Gf96-7uf-_uNeptxRG3Rrn8-YTfD3_RocF34tlWISiHKMKW6lLccT0tLY3SRbSA-_3a4WGSWi8waqx82Ik33bzuK9dq6ToOn602_Gm5I6qpCAMTYGxVwyjOi16o2vKR9EkTdAJofRPiIYqvHhKF1zxRBFHvfLz3jZaXBznwRfY9ygd68hqCTmyLJ2cQHZ6eTD2tFlHXrKUh6i_mBTpAHEw8x8oeIUHu1wJ77NQfHlDOlxGDhqlR25giUAEnCkhMqHChw4aC0dKcgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsYLhf4iP-l6LDtnLIbLTYt1kzDvxfX5QBuJSn06lxKFJ0sJZaQ0XtlHE0cTb-2gzccdb1oVtAc7YlNoVpNMLLedogOxHXcI-V_ZXZ8Cybjf0LccLc22-N_Pt5BVbrbKdtXgCShgMpg4AHcOnE-WmMfqP2goVqRvg8GfKLlpNLXkLNIFT4ariqBa-ugjoNVyBc56JinciWD-70XqnzqjAD1ivHcDW_gM_ezcjPiaRrBc2yx-n62nL1KbgkNCwSWdBrscXVrlVBKTlkXY3aXGfJg2rhHbbd9U1HEIvwgoMsWoDe5O-7QSAn5yPP9dg9uBio2GuEmGa6a1UWYBIEsiSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جزئیات و تصاویر رهگیری هواگردهای آمریکایی
🔹
اف۱۵ چگونه و با چه موشک ایرانی‌ای شکار شد؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/681104" target="_blank">📅 14:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681103">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای جروزالم‌پست: ایران زرادخانه موشک‌های بالستیک خود را با سرعتی خیره‌کننده بازسازی می‌کند
روزنامه صهیونیستی جروزالم‌پست مدعی شد:
🔹
ارتش اسرائیل در حال مشاهده یک بازگشت خیره‌کننده و سریع در تهدید موشک‌های بالستیک است.
🔹
مقامات ارشد دفاعی اسرائیل اکنون اعتراف می‌کنند که ایران راه‌های خلاقانه‌ای برای تمرکز بر بازسازی موشک‌ها و سایر تهدیدات مشخص پیدا کرده است، حتی اگر بخش‌های عظیمی از کشور هنوز در ویرانه باقی مانده باشد.
🔹
اگر ایران بتواند تولید ۱۰۰ تا ۳۰۰ موشک در ماه را از سر بگیرد، می‌تواند زرادخانه موشکی خود را تا اواسط سال ۲۰۲۷ به سطح ژوئن ۲۰۲۵ بازگرداند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/681103" target="_blank">📅 14:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681102">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedea9bd1f.mp4?token=tyfC8LFD_qEaLuT1ltpNx0MU0NvIIVoBZHn5V279bz2csjE-waGUG87koUPI-7mZzktiu6R3Iccki4OoLlhJHmqHHUcqYtzSCH_ZLhB-xRuLGossxyzha8KJY2U8kX31D9HPy6dx73K8SwWpdn-59UOLI_HQ8R8ZBPagHKHLkTbz8jSkg0infaHEFS6Jo4x02DM7VsyEAsJtmLBfhOKZb-2HLr6R-yhx8a0gg0mIzz_J3qoy0O81PeCl0OFprBSgmjVeundr65N3Z0a0t2EsvNMUbhp__8Xsqtv3kR2xbCVz4Vgw3QEjMjuXoi40R0-a-Ng9pWhti25UewvRo7heqJ19_PzrmEzbOiRsMnheAz9OhkxA2-BXIqbSvjP89naoJCy2jriN6VffV0XLRMjilrhAW130tnR_Y7TCCGXzpLuNZh8F4j4hUMN4TIjx-h96doLnRt4uUDy8Pb1tvwPkaf0Ds_1Wa-gpJNmKSjJHc_q1Q2q9UHqPjYEd9ptHClsKBYvDRnns7I3hO_bg8E13DbucMiA-5phlGKvVPopNoPemQ0In4rQ3Tc9Zy2DXpCZmIVUOyORgbY8XtRmxW9Dao2XeyloNhFAxtYM9UhiySsAAuV65j6yOBxABYekXpK2ZPXGXxZa6Kf-0r3idHHXSBri0umzld9PQ0LS0W8wKEHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedea9bd1f.mp4?token=tyfC8LFD_qEaLuT1ltpNx0MU0NvIIVoBZHn5V279bz2csjE-waGUG87koUPI-7mZzktiu6R3Iccki4OoLlhJHmqHHUcqYtzSCH_ZLhB-xRuLGossxyzha8KJY2U8kX31D9HPy6dx73K8SwWpdn-59UOLI_HQ8R8ZBPagHKHLkTbz8jSkg0infaHEFS6Jo4x02DM7VsyEAsJtmLBfhOKZb-2HLr6R-yhx8a0gg0mIzz_J3qoy0O81PeCl0OFprBSgmjVeundr65N3Z0a0t2EsvNMUbhp__8Xsqtv3kR2xbCVz4Vgw3QEjMjuXoi40R0-a-Ng9pWhti25UewvRo7heqJ19_PzrmEzbOiRsMnheAz9OhkxA2-BXIqbSvjP89naoJCy2jriN6VffV0XLRMjilrhAW130tnR_Y7TCCGXzpLuNZh8F4j4hUMN4TIjx-h96doLnRt4uUDy8Pb1tvwPkaf0Ds_1Wa-gpJNmKSjJHc_q1Q2q9UHqPjYEd9ptHClsKBYvDRnns7I3hO_bg8E13DbucMiA-5phlGKvVPopNoPemQ0In4rQ3Tc9Zy2DXpCZmIVUOyORgbY8XtRmxW9Dao2XeyloNhFAxtYM9UhiySsAAuV65j6yOBxABYekXpK2ZPXGXxZa6Kf-0r3idHHXSBri0umzld9PQ0LS0W8wKEHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فصل جدید برنامه محفل ستاره ها؛ جذاب و مفرح و پرهیجان تر!
ویژه برنامه ماه ربیع‌الاول شبکه سه و شبکه نهال با محوریت قرآن کریم
🌻
از جمعه ۲۳ مرداد
⏰
هر روز حوالی ساعت ۱۸:۰۰ از شبکه سه سیما
🌻
از شنبه ۲۴ مرداد
⏰
هر روز ساعت ۱۶ از شبکه نهال
⏰
تکرار؛ ساعت ۲۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/681102" target="_blank">📅 14:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681101">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ca050c9c5.mp4?token=SkzUQMdS85O2ROhP4iD1I8Wzx8VJYKkrZlktoH_wDNe7EKQpWi6DYmFzDV4SWqYs2HIGb2ecQDLPDE95XjEyRXFcvdC3QMOENCDkzyBstI8lq6iOYmS2iExTpz7Tr1zvFAh_WXQIEa7ZOilQ7ms0Z-MQtejI0ltbaVJH_gvm5NMSA1J_0FLxTb7BFxQTrbjqT55Rq0M0B2APrbJ7rWrYcfU1FTu10cvU3ArNri70gaZ263ZxZwn_qn6-Tzc23jxnuOanm0dmQ0pdXALPByy7iWA1zQVWTaFXab50hRGgwU3yO5PeXUuS0Ye_G0cxqAh3p9vbG4QflAjtkef2CseW5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ca050c9c5.mp4?token=SkzUQMdS85O2ROhP4iD1I8Wzx8VJYKkrZlktoH_wDNe7EKQpWi6DYmFzDV4SWqYs2HIGb2ecQDLPDE95XjEyRXFcvdC3QMOENCDkzyBstI8lq6iOYmS2iExTpz7Tr1zvFAh_WXQIEa7ZOilQ7ms0Z-MQtejI0ltbaVJH_gvm5NMSA1J_0FLxTb7BFxQTrbjqT55Rq0M0B2APrbJ7rWrYcfU1FTu10cvU3ArNri70gaZ263ZxZwn_qn6-Tzc23jxnuOanm0dmQ0pdXALPByy7iWA1zQVWTaFXab50hRGgwU3yO5PeXUuS0Ye_G0cxqAh3p9vbG4QflAjtkef2CseW5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتیجه بی‌نظمی و بی‌اخلاقی انسان؛ ببینید داخل شکم این ماهی چه پیدا شده است!
🔹
تصاویری تکان‌دهنده از محتویات شکم یک ماهی، بار دیگر زنگ خطر آلودگی دریاها و ورود زباله‌های انسانی به چرخه حیات آبزیان را به صدا درآورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/681101" target="_blank">📅 14:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681100">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d47cc00e6e.mp4?token=ZqLGIduB-s_wamDzFXg-gekm_B-J3prTt3LSSvYHppubBz04vYWOX29sPNH8HKFs-vE3Ut_xlbXjotny7lKE2uJUTi1_qC3_VE5cdSM1Ygzfm3kkOvLGXlXoSygSvyT2jrV0GEre6w_duf3h_nf4hjfD6NFEOFJCkfdxZui58cCpgNk-XzMrtbmksgnB8O0hUUtuyAI4Rd8hoqN6YTFJinycNlgxGeujhMaLYFXiXtD7OTKY2w68Tzbh7Tv_WkF67oJQyJpU16Lo75R6xMEp5wwUldrXXTWG3pUwsXc1lFbPMPd4a9A8hT3MilIwKQkUYqbbsxx7cc2mn5wA2RzGaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d47cc00e6e.mp4?token=ZqLGIduB-s_wamDzFXg-gekm_B-J3prTt3LSSvYHppubBz04vYWOX29sPNH8HKFs-vE3Ut_xlbXjotny7lKE2uJUTi1_qC3_VE5cdSM1Ygzfm3kkOvLGXlXoSygSvyT2jrV0GEre6w_duf3h_nf4hjfD6NFEOFJCkfdxZui58cCpgNk-XzMrtbmksgnB8O0hUUtuyAI4Rd8hoqN6YTFJinycNlgxGeujhMaLYFXiXtD7OTKY2w68Tzbh7Tv_WkF67oJQyJpU16Lo75R6xMEp5wwUldrXXTWG3pUwsXc1lFbPMPd4a9A8hT3MilIwKQkUYqbbsxx7cc2mn5wA2RzGaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشدید بی‌سابقه بحران سوخت در اقلیم کردستان
🔹
صف‌هایی که پایانی ندارد و شهروندانی که برای پاک کردن باک خودروهای خود، شب را در داخل خودروهایشان به صبح می‌رسانند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/681100" target="_blank">📅 14:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681098">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0832b30023.mp4?token=bmfQpQh37r0gTTSS1BmR8m-i6emxWpw2ojohanX50vYDGI2gzd8nAFxo5rthUeKecA-4oVHjebfXBPNxASwnTCWUIweQjXHA2cwf57Gcgn0W_3hoBbiKv9e_ZnBHGS5QxntsvPSpG-vh17a1rgBYSCFoXOv96jyVHCpCWtiuQk_ZuR_glsUq_-ZQLjgsbYX7ZyKdUDBklHh-PeV6rwplQlEkIHuyBCReWkHHhdYo6biTq25UgOSmWQll54jFCCMTuGVGNISEtL60YExIK5F_M3jiB5AhtD4B8creZitocQMmCY23iMdICnubYejUlOdH29z3JfkWeQwDEECVRSjQlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0832b30023.mp4?token=bmfQpQh37r0gTTSS1BmR8m-i6emxWpw2ojohanX50vYDGI2gzd8nAFxo5rthUeKecA-4oVHjebfXBPNxASwnTCWUIweQjXHA2cwf57Gcgn0W_3hoBbiKv9e_ZnBHGS5QxntsvPSpG-vh17a1rgBYSCFoXOv96jyVHCpCWtiuQk_ZuR_glsUq_-ZQLjgsbYX7ZyKdUDBklHh-PeV6rwplQlEkIHuyBCReWkHHhdYo6biTq25UgOSmWQll54jFCCMTuGVGNISEtL60YExIK5F_M3jiB5AhtD4B8creZitocQMmCY23iMdICnubYejUlOdH29z3JfkWeQwDEECVRSjQlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوگل از اپل تقلید کرد!
🔹
گوگل مشابه اپل قابلیت جدیدی را معرفی کرده که انتقال عکس، ویدیو، مخاطب و فایل بین دو گوشی را تنها با نزدیک‌کردن آن‌ها به یکدیگر ممکن می‌کند.
🔹
این قابلیت با NFC اتصال اولیه را برقرار کرده و سپس با کمک Quick Share و Wi-Fi، اطلاعات را با سرعت بالا منتقل می‌کند.
🔹
این ویژگی فعلاً برای Pixel ۶ و مدل‌های جدیدتر فعال شده و قرار است به‌زودی به گوشی‌های تاشوی نسل هشتم سامسونگ و تا پایان سال به دستگاه‌های بیشتری برسد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/681098" target="_blank">📅 14:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681096">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ایران فقط نیم ثانیه به خلبان جنگنده اف ۱۵ سرنگون شده آمریکا، فرصت هشدار داد  نیویورک تایمز:
🔹
در آوریل ۲۰۲۶، ایران یک فروند اف ۱۵ ایی آمریکایی را بر فراز جنوب ایران با یک موشک زمین به هوای دوش‌پرتاب سرنگون کرد.
🔹
به نظر می‌رسد ایران از با استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/681096" target="_blank">📅 14:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681094">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6bcd4d0e5.mp4?token=sNT8v-RCqxg0TCrbMC3qZWsHl27HGHuvb5EPljMJCwfZlahuRiUOcDaUo1nCxQwFbXWNs_wvNtrGI32eOfwqHYZbcAtf8pAAQoKlzDXfUHwmnZQCgSpg4cQTw2xqWahHe9DXFJIeBjq0PAYlFpvhB48AIxYVeggkXvHZyQq4Fmh-82rtZRsrffIxMw3GLa_a-DR1nsdXjeJKIK2pvvypNosahhf5Mvd3HLUFeI_4jO6yfQ5mo0P2PGCAMU8fqFLE476QZ2MWGtBkmntUJYkfsyVaWXVjATvgSFJzeh_GCQrmIRsKOeRtPDw9ZcEhq-_0v6i3XTSio9-QBjwGCeV6GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6bcd4d0e5.mp4?token=sNT8v-RCqxg0TCrbMC3qZWsHl27HGHuvb5EPljMJCwfZlahuRiUOcDaUo1nCxQwFbXWNs_wvNtrGI32eOfwqHYZbcAtf8pAAQoKlzDXfUHwmnZQCgSpg4cQTw2xqWahHe9DXFJIeBjq0PAYlFpvhB48AIxYVeggkXvHZyQq4Fmh-82rtZRsrffIxMw3GLa_a-DR1nsdXjeJKIK2pvvypNosahhf5Mvd3HLUFeI_4jO6yfQ5mo0P2PGCAMU8fqFLE476QZ2MWGtBkmntUJYkfsyVaWXVjATvgSFJzeh_GCQrmIRsKOeRtPDw9ZcEhq-_0v6i3XTSio9-QBjwGCeV6GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریاچۀ ارومیه دوباره تماشایی شد
🔹
با افزایش آب دریاچۀ ارومیه، سواحل این پهنۀ آبی در روزهای اخیر بار دیگر شاهد حضور گردشگران و مسافرانی است که برای تماشای جلوه‌های دریاچه راهی این منطقه شده‌اند.  #اخبار_آذربایجان_شرقی در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/681094" target="_blank">📅 14:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681093">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7524a20491.mp4?token=jcOdUxRb4GYfRkbUz_riRNWHAS2X6mLFmLJkibkadeyMf8u0_78YF8hOPWH6BFneq_h-YzNbRbF3HioA2oAsl_JLVTHm5t0oPLNkZjpVGP-nSsNo3dN8Vw8HfbO_n2wUg7odrivEMgEjXr1RJQjy-pLz4plqv88Ugb2NkKVF6Q-r1rDCgKYjFTazuDuViYNOSWdtjuFH_3F_tR1IVakPqv7zF2IiuOsV9DYAcM4zyiYVacGQZ6DpWLwRaOo6ev5b5lBeCsERBz0YfdDk0i4WU3LD5aSTZx5TBegrIxib9wh-5QOOHXw46bSxxGR_jK5M1KFFpFq1evsxQ2cByURFYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7524a20491.mp4?token=jcOdUxRb4GYfRkbUz_riRNWHAS2X6mLFmLJkibkadeyMf8u0_78YF8hOPWH6BFneq_h-YzNbRbF3HioA2oAsl_JLVTHm5t0oPLNkZjpVGP-nSsNo3dN8Vw8HfbO_n2wUg7odrivEMgEjXr1RJQjy-pLz4plqv88Ugb2NkKVF6Q-r1rDCgKYjFTazuDuViYNOSWdtjuFH_3F_tR1IVakPqv7zF2IiuOsV9DYAcM4zyiYVacGQZ6DpWLwRaOo6ev5b5lBeCsERBz0YfdDk0i4WU3LD5aSTZx5TBegrIxib9wh-5QOOHXw46bSxxGR_jK5M1KFFpFq1evsxQ2cByURFYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امنیت خونه و محل کارت رو همیشه زیر نظر داشته باش!
🎥
💡
دوربین مداربسته لامپی V380؛
یک دوربین هوشمند در ظاهر یک لامپ معمولی!
✅
نصب آسان بدون نیاز به سیم‌کشی پیچیده
✅
اتصال به وای‌فای و مشاهده تصاویر با موبایل
✅
مناسب منزل، مغازه، دفتر کار و پارکینگ
✅
دید بهتر برای کنترل محیط در هر زمان
✅
طراحی لامپی و کم‌جا، بدون اشغال فضای اضافی
🏠
با این دوربین، هر لحظه از محیط اطرافت باخبر باش!
❌
قیمت قبل: ۲,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۱,۷۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
همین حالا سفارش بده و امنیت محیطت رو بیشتر کن.
http://memarket24.ir/briefcart/180124/g-en50734</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/681093" target="_blank">📅 14:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681092">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دزدها منتظر همین یک لحظه‌اند!
🔹
یک لحظه حواس‌پرتی، یک حرکت برق‌آسا و ناگهان موبایل دیگر دست شما نیست.
🔹
اما ماجرا فقط سرقت یک گوشی نیست؛ اطلاعات، عکس‌ها و دنیای شخصی شما هم در خطر است.
🔹
این ویدئو را ببینید؛ شاید دفعه بعد، دزدها سراغ شما هم بیایند!
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/681092" target="_blank">📅 14:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681089">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWyszFLg65B02M5LtvKeH0-D5eW_DUlTJlJt2XYzsgh5_cL7NPSwLuihSkgFCUXMNRiZe8DYGjF7M0QSiJfQG9flZ2Y_SiUIMM1BxiXQRASIWbR4MZ-2ScY5EwzNk3pt6uGhmjdAd37fOI-8sQHalDaEC7Nl9cU7vXezJ5z0_TDkuEqUwgkbgaUtY1umGZdb4xzhKRDDhWQFFRD40VYoUDhIRmhBGzNoH7P2yHKREGV6_1aknoZNrPzQ-2LBzTmDVlun3bM7Zo4PqBn2-e5QMtoH0VhUpEYRLzqkvsnvtqS1Eo4ObfHtsT6_2OjbobT2K3ZpU0aCtNRAcwfhaxmcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داعش شروع به تهدید علیه اسپانیا کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/681089" target="_blank">📅 13:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681088">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab9cfed555.mp4?token=cMz6uWk3JS4AoFxv0vlB8F45Bkuby9OBaJj3QhwKV2u28adfu0J4F8frAC4cdcOxv7LDzI309nXIZ-2cwNlMixVflYvdhsrW91NQzIjf73azxInIX4qAHezHDmufLT-0IA5_5DpDv8Dlsm0xgLcI515vlm_0Hh6lxHj3NLjx0wkfSf1klLx-0AfP0fLOFhV9xfehcklRB-UcquBHcIsvquZFaQGn--rlCdKpsec3ZnDaCVZGZWlJKCgDpx34SJUUV9GrABt0bCJMsyOZFNH0RDGZD1lYdwj6oivIma4iWuMtxSKgdiFZoorobG9WlUePanchig43N8sMjiUcKxgP4Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab9cfed555.mp4?token=cMz6uWk3JS4AoFxv0vlB8F45Bkuby9OBaJj3QhwKV2u28adfu0J4F8frAC4cdcOxv7LDzI309nXIZ-2cwNlMixVflYvdhsrW91NQzIjf73azxInIX4qAHezHDmufLT-0IA5_5DpDv8Dlsm0xgLcI515vlm_0Hh6lxHj3NLjx0wkfSf1klLx-0AfP0fLOFhV9xfehcklRB-UcquBHcIsvquZFaQGn--rlCdKpsec3ZnDaCVZGZWlJKCgDpx34SJUUV9GrABt0bCJMsyOZFNH0RDGZD1lYdwj6oivIma4iWuMtxSKgdiFZoorobG9WlUePanchig43N8sMjiUcKxgP4Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارتون هفته‌نامه نیویورکر در واکنش به مخفی شدن ترامپ در کامیون آشغال غذا به دلیل نگرانی از حمله ایران
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/681088" target="_blank">📅 13:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681086">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef1f6f636.mp4?token=CF8wnBgYVOyneYTHTBMTfqR5zIWfrSDa9RJdrVLgxiT9E2BF0Q0gC8Nk3fptVCi4gbteYbOYbPEJd7GEjuBncgRCvdjOX96xZSSg_Qnfgmi9SbAaEKWGAolV_96rBy4qD_sPBKh0jS-tB4TCokDtrW5R3K2ffz3YdwLZtUVb8PxB2QllhiHVjQOCMITsLPQMGPweleuzHtbWmZ1ce3fGI0Z-SnZVAczMC95roSeKvNf62ldQ9bvTxm986LcT6xldp8wK007VCENN-k_d-I6Ik_EhNhcZJDHk4jAejcGwELTNQ0qlfKUMdAII0l-GuiU7P5QJ7O52iTBFUrehpyvqVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef1f6f636.mp4?token=CF8wnBgYVOyneYTHTBMTfqR5zIWfrSDa9RJdrVLgxiT9E2BF0Q0gC8Nk3fptVCi4gbteYbOYbPEJd7GEjuBncgRCvdjOX96xZSSg_Qnfgmi9SbAaEKWGAolV_96rBy4qD_sPBKh0jS-tB4TCokDtrW5R3K2ffz3YdwLZtUVb8PxB2QllhiHVjQOCMITsLPQMGPweleuzHtbWmZ1ce3fGI0Z-SnZVAczMC95roSeKvNf62ldQ9bvTxm986LcT6xldp8wK007VCENN-k_d-I6Ik_EhNhcZJDHk4jAejcGwELTNQ0qlfKUMdAII0l-GuiU7P5QJ7O52iTBFUrehpyvqVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باغ شاهزاده ماهان کرمان، تکه‌ای از بهشت در دل کویر
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/681086" target="_blank">📅 13:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681084">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ترخیص کالاهای کولبری و ملوانی تسهیل شد
🔹
کالاهایی که در رویه‌های کولبری و ملوانی وارد شده‌اند، اگر پیش از اجرای مصوبات جدید دارای ثبت آماری معتبر باشند، حتی در صورت قرارگرفتن در فهرست کالاهای محدود یا ممنوع‌شده، امکان ترخیص خواهند داشت.
🔹
همچنین یخچال، یخچال‌فریزر، ماشین لباسشویی و ماشین ظرفشویی با ثبت آماری معتبر صادرشده بین ۱ خرداد تا ۱ تیر ۱۴۰۵ نیز مشمول این تصمیم هستند و تا ۳۱ شهریور ۱۴۰۵ امکان ترخیص دارند؛ گمرک موظف به اجرای این تصمیم شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/681084" target="_blank">📅 13:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681082">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59c86ec20.mp4?token=LaKf_Nj9aJ6r5J21gDjenik6r_BpH7vS67qzlOWfKvnI0JCWlnMMTO5DmCBn-x8cxWasNQEiyZH61nUruKGmnFDjk0EPSwue64I0Tt7FqATx_c82iXNruMslFdGMViyRmFNSrNohVJ69g5HZILkYeeURZIUa8-ebGawFZ7XbOQpldhPJEORo-5N41JYZGPezDrXdVYKlH88anRd-9VA_19RPCDsohZS2KpLR5oGBDEJxfmDa5MDgZYTxn5OmHEqBC_o3C1LK21Uld6sEQcFEGM7sNHEvv-vpFGLlDDMuihh6JgUdDAkWYUX51ku_0Ax8tZzYBh9v6U9y_SbZqV_llQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59c86ec20.mp4?token=LaKf_Nj9aJ6r5J21gDjenik6r_BpH7vS67qzlOWfKvnI0JCWlnMMTO5DmCBn-x8cxWasNQEiyZH61nUruKGmnFDjk0EPSwue64I0Tt7FqATx_c82iXNruMslFdGMViyRmFNSrNohVJ69g5HZILkYeeURZIUa8-ebGawFZ7XbOQpldhPJEORo-5N41JYZGPezDrXdVYKlH88anRd-9VA_19RPCDsohZS2KpLR5oGBDEJxfmDa5MDgZYTxn5OmHEqBC_o3C1LK21Uld6sEQcFEGM7sNHEvv-vpFGLlDDMuihh6JgUdDAkWYUX51ku_0Ax8tZzYBh9v6U9y_SbZqV_llQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان کامل تایتانیک؛ کشتی بزرگی که غرق شدنش غیرممکن به نظر می‌رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/681082" target="_blank">📅 13:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681081">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1975aa00.mp4?token=PTEas2rK01pqUaSbATKyoxf9hkUK7iebXzDWmPg5JK98BH8iY7bNhpm9H7D_pLz9_KQdKyjcE_z5coXu3wIBiCiBYTichNwUOJi2uFyKVAcXfbbG1yeQfCGUha1exPQmcTbS0Xkdrh_DF3z5b3nXQ2V7r8SPWql-C5lMG2RvS4QvpmkOFwgvxPOj5JRWrZqnfGBDES1YGaW8RxIaYDy0VPJntwZHdusE845rzP3-oTcmQtkDvx91IlgKXMoEzgAApoBCwCxFg-xDfqkc0bTLn4daXJAb7xplA8I7TgFiTXIZJKV-mWyrpvi4wvTBKLXLaQSg2c_ABvvGypWee7OuGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1975aa00.mp4?token=PTEas2rK01pqUaSbATKyoxf9hkUK7iebXzDWmPg5JK98BH8iY7bNhpm9H7D_pLz9_KQdKyjcE_z5coXu3wIBiCiBYTichNwUOJi2uFyKVAcXfbbG1yeQfCGUha1exPQmcTbS0Xkdrh_DF3z5b3nXQ2V7r8SPWql-C5lMG2RvS4QvpmkOFwgvxPOj5JRWrZqnfGBDES1YGaW8RxIaYDy0VPJntwZHdusE845rzP3-oTcmQtkDvx91IlgKXMoEzgAApoBCwCxFg-xDfqkc0bTLn4daXJAb7xplA8I7TgFiTXIZJKV-mWyrpvi4wvTBKLXLaQSg2c_ABvvGypWee7OuGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احسان خواجه امیری: پدرم عاشق ایران و مردم ایران بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/681081" target="_blank">📅 13:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681075">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مجلس برای گرانی بنزین به رئیس‌جمهور نامه نوشت
هاشم خنفری پورجعفری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
نمایندگان مجلس با امضای نامه‌ای به رئیس‌جمهور هرگونه افزایش قیمت بنزین را غیرقابل‌قبول و مردود اعلام کرده‌اند و این نامه با امضای اکثر نمایندگان قاطعیت مجلس بر عدم افزایش قیمت را نشان می‌دهد.
🔹
افزایش خودسرانه قیمت بنزین در هر استانی غیرقانونی است و استاندار و مدیران حوزه پخش فرآورده‌های نفتی آن استان مسئول آن هستند و باید با آنها برخورد قانونی شود.
🔹
چنین اقدامی تشویش اذهان عمومی تلقی شده و هم برخورد اداری و هم برخورد قضایی را به دنبال خواهد داشت زیرا این اقدام برخلاف تصمیمات کلان دولت و مجلس است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/681075" target="_blank">📅 12:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681074">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f8a6ab92.mp4?token=qo03Xqm82SfRISNp_UE7x5zTzDkeLHWyoHIGHKyV0vqGgSZRW5MjnD_jJdIrwvPOjisN_1czubYB57hl1jrkbfZCaURgMrnHNE8AdmtLG3W-vEv81hcGs0v2sUABn9io2H1uvAd_pRXpK8z3Usnu8OY04UjnM8VWBQL16XzfWT1bJXN3HMqk3ZneQ9eIHRtbC2CpHrC9UrRSnzALO7Ubi1sxRJDklo0T466CTyPWM2iN0wrJyDDsv4TGZ1CKuE0eBoRZ4t8qthLKx934k69U3XFDJNY55sMDs9xhC_bGZz2CQLekHE53LXXJ4Yh7sbvEQaUpQXEsaM9ynFTK8_uYpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f8a6ab92.mp4?token=qo03Xqm82SfRISNp_UE7x5zTzDkeLHWyoHIGHKyV0vqGgSZRW5MjnD_jJdIrwvPOjisN_1czubYB57hl1jrkbfZCaURgMrnHNE8AdmtLG3W-vEv81hcGs0v2sUABn9io2H1uvAd_pRXpK8z3Usnu8OY04UjnM8VWBQL16XzfWT1bJXN3HMqk3ZneQ9eIHRtbC2CpHrC9UrRSnzALO7Ubi1sxRJDklo0T466CTyPWM2iN0wrJyDDsv4TGZ1CKuE0eBoRZ4t8qthLKx934k69U3XFDJNY55sMDs9xhC_bGZz2CQLekHE53LXXJ4Yh7sbvEQaUpQXEsaM9ynFTK8_uYpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعت آبی مسجد همت تجریش؛ این ساعت بدون برق و باتری کار می‌کند
🔹
آب در لوله‌ها جریان پیدا می‌کند و با تغییر سطح آب، زمان را نشون می‌دهد.
🔹
البته تنظیم دقیق جریان آب برای درست کار کردن ساعت، کار آسانی نیست.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/681074" target="_blank">📅 12:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681073">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: آمریکا ناو هواپیمابر جدیدی به خاورمیانه می‌فرستد
ادعای وال‌استریت‌ژورنال:
🔹
آمریکا در بحبوحه تنش‌های جنگی با ایران، ناو هواپیمابر جدیدی به خاورمیانه می‌فرستد. قرار است ناو هواپیمابر یو اس اس جورج واشنگتن جایگزین ناو هواپیمابر یو اس اس آبراهام لینکلن شود.
🔹
قانونگذاران نگرانی‌هایی را در مورد گزارش‌های مربوط به شرایط نامناسب ناو لینکلن پس از بیش از ۲۵۰ روز حضور در دریا مطرح کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/681073" target="_blank">📅 12:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681072">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71c335c90.mp4?token=Fo4eqm_Y1nN8oUWDz5AJOVc9-kh2jrXgo6409n9DgE-BuJj14dWIgqBtRgzoxIGh5REPYvPT7lwX6JVLEbsLW-nc7y-uUV8Q0gtm6iotrlglTQOCghRjuDnwmvWVjbfAlj9B6-FpPT_2m5KlFAmTQJetgP8I9ya3ONt5ygTuRc0i074L4rEZV0efK31mrBYui7zHr4DQ2-VCDC7SQJ7q8og1RmdyPYSq-C6zy2OpCuQLRKH7URRi9NVypuHsW9kVTL4kiI1cs3YJMxC-Y36JAh-m_SjaKWbgboBbZ-wjWeVs2zgI17nMJmH6PZ-w3gpeWx_BXP05c4wLvWI_oF-M9SJCxyOAq86ob-cPqGQEw63nXoonD7MfFhKWUwGS-pbMg0zhZJCunFicwvH_iZwsZeNfE3LnO6uh5VMxoHkA3kRLUL6fCudeLkynB2TJvayz8V4i_onPCaKlJ0l1mssxoYJj6synBgF4Z8Xb2IfCYk2ENFTyYLngvAW1TEM3ti3wkIsR-n7nkFp92g6NodNQlujyXMcz1Nsd3mXBpPD91DNBU1FNL6ZHPuADGFyoySwoavuzYbcpxAHJB9bS45FsE8E12z2NQicLCFfzkBDUvuQ1Fm8PxCrcOWKJ2R5XhDR9YWRqyaLSYj0QynIxzUlx8bCmjPe6YRijcAWKki2lCGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71c335c90.mp4?token=Fo4eqm_Y1nN8oUWDz5AJOVc9-kh2jrXgo6409n9DgE-BuJj14dWIgqBtRgzoxIGh5REPYvPT7lwX6JVLEbsLW-nc7y-uUV8Q0gtm6iotrlglTQOCghRjuDnwmvWVjbfAlj9B6-FpPT_2m5KlFAmTQJetgP8I9ya3ONt5ygTuRc0i074L4rEZV0efK31mrBYui7zHr4DQ2-VCDC7SQJ7q8og1RmdyPYSq-C6zy2OpCuQLRKH7URRi9NVypuHsW9kVTL4kiI1cs3YJMxC-Y36JAh-m_SjaKWbgboBbZ-wjWeVs2zgI17nMJmH6PZ-w3gpeWx_BXP05c4wLvWI_oF-M9SJCxyOAq86ob-cPqGQEw63nXoonD7MfFhKWUwGS-pbMg0zhZJCunFicwvH_iZwsZeNfE3LnO6uh5VMxoHkA3kRLUL6fCudeLkynB2TJvayz8V4i_onPCaKlJ0l1mssxoYJj6synBgF4Z8Xb2IfCYk2ENFTyYLngvAW1TEM3ti3wkIsR-n7nkFp92g6NodNQlujyXMcz1Nsd3mXBpPD91DNBU1FNL6ZHPuADGFyoySwoavuzYbcpxAHJB9bS45FsE8E12z2NQicLCFfzkBDUvuQ1Fm8PxCrcOWKJ2R5XhDR9YWRqyaLSYj0QynIxzUlx8bCmjPe6YRijcAWKki2lCGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژنرال بازنشسته ارتش اردن از بحران‌ها و معضلات آمریکا در جنگ‌افروزی علیه ایران روایت می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/681072" target="_blank">📅 12:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681071">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BriBaspa62D_FBE4gYmQl9i3Ek0TRPIyLivvYmnzYTxsT7xrFgTY5dZIKs1U9jjtWrB0gtrpLSwXWBGP-TGetuip3GkEzQBIU4fvH9lcYeXXZ03G8lKPXwJwp2IkWTrli3JnQPWALCZmTdB8Wku95hjnqzD8wKVSTHDgLeQduohw5WWURk-fyGL29p_U4c9DNkev4l2wWtUCXY4XOzY5OPFt9y2urtR8Q7RUPpFcjGefeVN4juvVHCN8lQSkcE9REKUkEM2Kf8lzJnLZakVfu1NcFv9TWGbgfIUcgnvAyeVyisPlO9F-1UtkdQheiHNiKHfI-qIMrtzP2gHvVsh_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر نفت جهان با ادامه جنگ ایران تا چند روز دوام می‌آورند؟
رویترز:
🔹
برآوردها نشان می‌دهد از آغاز جنگ آمریکا و ایران، بازار حدود ۲.۶ میلیارد بشکه نفت از دست داده است؛ این رقم معادل حدود ۲۵ روز مصرف جهان است.
🔹
از سوی دیگر، با شکاف عرضه حدود ۵ میلیون بشکه در روز، ذخایر دولتی باقی‌مانده آژانس بین‌المللی انرژی در بهترین حالت می‌تواند حدود ۱۸۰ روز این کسری را پوشش دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/681071" target="_blank">📅 12:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681070">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
کاسبی باورنکردنی با پارکینگ خودرو در تهران
🔹
این روزها پیدا کردن جای پارک در تهران به یک معضل اساسی برای بسیاری تبدیل شده است؛ اگر سری به فضای مجازی بزنید با تبلیغات مختلف اجاره پارکینگ خودرو مواجه می‌شوید.
🔹
اجاره پارکینگ در تهران با توجه به محله از ماهی ۳ تا ۶ میلیون تومان و رهن کامل تا ۱۵۰ میلیون تومان رسیده است؛ داشتن پارکینگ حالا به یک سرمایه جذاب تبدیل شده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/681070" target="_blank">📅 12:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681069">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366aeedc1e.mp4?token=IRXeFQu0d9XhtZtwnPAySzn34ZHX2Ez-bxjzUMAqXur4gfZ3-SvTHSxoUvZ8QgzBkJd_JU7ySZVfWBoW0oySw8qQooZdB5y3LXwxrVP2Eia3ohwsXDvzh3H2L5hXJJaGMVujHFlZD0eXBpTQJX3Tq_NVzVy6YEchCZMBRkYa-61djpNv9fPxWL7BVyNJKQ7UwHjEetyjAZne5cIxltQsAVnqV8cME_4KzM4eY5az8biDdbWh5Gqjl7fdAa8l0oAZskEeWZBXLbmlkl7ewqzdrZg3oqbdagif7AGJX7CjTxKXenHlnv_RtFesKEFwV3aUUkLnzXdLa1XhfiBJnCX8Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366aeedc1e.mp4?token=IRXeFQu0d9XhtZtwnPAySzn34ZHX2Ez-bxjzUMAqXur4gfZ3-SvTHSxoUvZ8QgzBkJd_JU7ySZVfWBoW0oySw8qQooZdB5y3LXwxrVP2Eia3ohwsXDvzh3H2L5hXJJaGMVujHFlZD0eXBpTQJX3Tq_NVzVy6YEchCZMBRkYa-61djpNv9fPxWL7BVyNJKQ7UwHjEetyjAZne5cIxltQsAVnqV8cME_4KzM4eY5az8biDdbWh5Gqjl7fdAa8l0oAZskEeWZBXLbmlkl7ewqzdrZg3oqbdagif7AGJX7CjTxKXenHlnv_RtFesKEFwV3aUUkLnzXdLa1XhfiBJnCX8Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعر محمد رسولی در باب فرار ترامپ با ماشین حمل غذا
از ترس ترور نخواب که دفعه‌ی بعد
با خاور حمل خوک باید بروی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/681069" target="_blank">📅 12:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681068">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
تلگرام ۱۳ ساله شد؛ بیش از ۴۹ میلیون کاربر ایرانی
🔹
تلگرام ۱۳ ساله شد و اکنون بیش از ۴۹ میلیون کاربر ایرانی دارد؛ ایرانی‌ها بیش از ۲.۸ میلیون کانال دارند که سالانه بیش از ۹۰۰ میلیون پست با بیش از ۱۷۰ میلیارد نمایش یونیک منتشر می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/681068" target="_blank">📅 12:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681067">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2795f234d0.mp4?token=eQYjjVcM24pvjpVKitJJwFvRxEOogLBUz6qc0dLJ7R6cp5FrwPhUc3gkgVNxoBUxwcWJbmEXIIZytsFqGd96khczmoobWfgyhBEP6GJmnk6s0lAP9cmkz-FJU8w5rFxGLeVY6UXJUdOFd-ucnMbqgvsthQ6YuQ1VI87nvBykG6Bc8aTaccfH0MXx_8ERgp4uRW6ly514arT2UlW32OrYi-kw39OK2e7aVqoylz9vu1OxlVM3BC_GTTgqbxAu54nun9wJQdvSCpUzDiPZKuiLBFUmeWm091FnFtkyBhhrwya6T1D9zEzTpiXlCoFHEyeov_X3QQd8R4i5fXJO8YwqLGC7gH4uz65XEuBSGDfn7f2OR3Tj2SucSymnOMj1qTvjGzFUd5cU4PLiW5wV7_eXjC9T4A_O5m6pU1gRHIIYTKXYHxiU7EGhpbrVJU6Whx6K6QF9KE1nLd6waFyiLXwU5pU-MRIU_UdpEzGPxh0J3WlmV9YpGLPs6AS24aI4LcT0E5tH8BNzwpHQiiDaCD_gkhV2Qt8XZjuF09zzlB-kTZLwlOQ7AgAH2kTEXzcsGuYiOgWaQQNu8kknV9i-SoSiU_6alR7_CFS_kuQog35ziQmfuFTB-FTRl05WkPZFjgGz7Iea7Jh0K6ZaFHhcz3zLSkSB6hLAshL3GezFPipcdG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2795f234d0.mp4?token=eQYjjVcM24pvjpVKitJJwFvRxEOogLBUz6qc0dLJ7R6cp5FrwPhUc3gkgVNxoBUxwcWJbmEXIIZytsFqGd96khczmoobWfgyhBEP6GJmnk6s0lAP9cmkz-FJU8w5rFxGLeVY6UXJUdOFd-ucnMbqgvsthQ6YuQ1VI87nvBykG6Bc8aTaccfH0MXx_8ERgp4uRW6ly514arT2UlW32OrYi-kw39OK2e7aVqoylz9vu1OxlVM3BC_GTTgqbxAu54nun9wJQdvSCpUzDiPZKuiLBFUmeWm091FnFtkyBhhrwya6T1D9zEzTpiXlCoFHEyeov_X3QQd8R4i5fXJO8YwqLGC7gH4uz65XEuBSGDfn7f2OR3Tj2SucSymnOMj1qTvjGzFUd5cU4PLiW5wV7_eXjC9T4A_O5m6pU1gRHIIYTKXYHxiU7EGhpbrVJU6Whx6K6QF9KE1nLd6waFyiLXwU5pU-MRIU_UdpEzGPxh0J3WlmV9YpGLPs6AS24aI4LcT0E5tH8BNzwpHQiiDaCD_gkhV2Qt8XZjuF09zzlB-kTZLwlOQ7AgAH2kTEXzcsGuYiOgWaQQNu8kknV9i-SoSiU_6alR7_CFS_kuQog35ziQmfuFTB-FTRl05WkPZFjgGz7Iea7Jh0K6ZaFHhcz3zLSkSB6hLAshL3GezFPipcdG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش حرم رضوی به ماجرای جلوگیری از شعار «مرگ بر آمریکا» در رواق دارالذکر
/ تلویزیون اینترنتی مدار
گفت‌وگوی کامل
👇
▫️
https://aparat.com/v/rhz4415
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/681067" target="_blank">📅 12:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681066">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7db719237.mp4?token=LH8gtpYPOEe6zBPaoy3vYhKgegxQ4qaU4LW9I7UtxwVlxXjkfUhiw76XRl2geD6C6--kuZKHLzt8AHbFVssO6zqQ1pjQl6qeSZPawvw7kYOLbsd_gVrFD9DIub1sqqWsY8FuETWY5dh7HTMbh4YQCeqg_YJfkLWYIRUDpd-76MOc6FP2jcxL0-ax8DfDkaOskBfJPAQdpZ9AYe1SgRhLDgjalqkZHoDQ1tErKphriRwKN6vukQ6kdWHrCrEDdAOEGLvx99UmR2LtVMWmtABgE-JurZq5Og9xTcNRIas82JlHOKTBgci4tHpv4Dw5V1W9mBD9QHwxMelmE4hJ_J1LAHD_YcsQFOa0Uvg1TG32f61iYkIaKVFHY1ty32F_qxwxvcU-YP66YExfKJn-lLmL57SftnCr-nY3zuoPCZWL3np2nszXVoqtqTrE5X43ErtFE-_tMpkbsixq0AycmgszxtCfQvBL4Tp57vM_sFZj8RpwPxow7RzzkxYuq90H69xE2dIgl23_84jEpHvtckFsGdrj20iXbC97rq0ciFsdN-YfMsVcdeDHXYDBUrwA-BBy5DTr7kydnTUiTYkVjHqbDJP7-3JGyylx4hNUtQuZf8pkQo12Je6jKGfGPEv1sJKELJhFj_wdwi54qf7nWeMQP5uxCUmjx2NFOSs8GEKBGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7db719237.mp4?token=LH8gtpYPOEe6zBPaoy3vYhKgegxQ4qaU4LW9I7UtxwVlxXjkfUhiw76XRl2geD6C6--kuZKHLzt8AHbFVssO6zqQ1pjQl6qeSZPawvw7kYOLbsd_gVrFD9DIub1sqqWsY8FuETWY5dh7HTMbh4YQCeqg_YJfkLWYIRUDpd-76MOc6FP2jcxL0-ax8DfDkaOskBfJPAQdpZ9AYe1SgRhLDgjalqkZHoDQ1tErKphriRwKN6vukQ6kdWHrCrEDdAOEGLvx99UmR2LtVMWmtABgE-JurZq5Og9xTcNRIas82JlHOKTBgci4tHpv4Dw5V1W9mBD9QHwxMelmE4hJ_J1LAHD_YcsQFOa0Uvg1TG32f61iYkIaKVFHY1ty32F_qxwxvcU-YP66YExfKJn-lLmL57SftnCr-nY3zuoPCZWL3np2nszXVoqtqTrE5X43ErtFE-_tMpkbsixq0AycmgszxtCfQvBL4Tp57vM_sFZj8RpwPxow7RzzkxYuq90H69xE2dIgl23_84jEpHvtckFsGdrj20iXbC97rq0ciFsdN-YfMsVcdeDHXYDBUrwA-BBy5DTr7kydnTUiTYkVjHqbDJP7-3JGyylx4hNUtQuZf8pkQo12Je6jKGfGPEv1sJKELJhFj_wdwi54qf7nWeMQP5uxCUmjx2NFOSs8GEKBGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وازلین و خواص باورنکردنی
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/681066" target="_blank">📅 11:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681065">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e0c351ba.mp4?token=ENuiizpYykBW6vTh5IfVgnKUSLGm2yc4Unq6Wb0gOl8LkCtbTvMWr1TGEx4D6AqBBepLS4JpWOPZw-Gk49GK0Za2f3BmyA10m1ThBpQ2-B5CPkxgbZ8Y1fTsai7kesF2NPpuIx7szxyFsQyobkITKXApXx_9QtAR0vMjafI1dgFNFvYG287K4J5rP-QT5gxQcLD1Ozkh8kKHy9HzgSLMQ60vK6DsFzqAiueGXDmPyIgNfbkfGGIGJfER3dxKrG1dJ-XX3PVLLIK1Z_bFTPI5xf5QIpck6JMEoyfhOXrwntwz3kX0JODjNOBE7NryrByLrmeJ-5_9QOJ6xfodk8qLwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e0c351ba.mp4?token=ENuiizpYykBW6vTh5IfVgnKUSLGm2yc4Unq6Wb0gOl8LkCtbTvMWr1TGEx4D6AqBBepLS4JpWOPZw-Gk49GK0Za2f3BmyA10m1ThBpQ2-B5CPkxgbZ8Y1fTsai7kesF2NPpuIx7szxyFsQyobkITKXApXx_9QtAR0vMjafI1dgFNFvYG287K4J5rP-QT5gxQcLD1Ozkh8kKHy9HzgSLMQ60vK6DsFzqAiueGXDmPyIgNfbkfGGIGJfER3dxKrG1dJ-XX3PVLLIK1Z_bFTPI5xf5QIpck6JMEoyfhOXrwntwz3kX0JODjNOBE7NryrByLrmeJ-5_9QOJ6xfodk8qLwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
الهی با آمدن ربیع
به دعای صاحب الزمان
🌼
🌺
زندگیتان رنگ بهار
و دلتان رنگ آرامش بگیرد ...
#ربیع_الاول
#امام_زمان
(عج)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/681065" target="_blank">📅 11:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681064">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f023a6a08a.mp4?token=AQ-EjdEWBmhsxYHDaTm1ly4TEKnxUvqWxZ6CtnqijfFyPXljCFxx-swZh7lkTtlCHtc707OiTCNtgzVZUKEr1UiXo96XO2iKBnu0mAB-C2NPHl6gVnrJ0JTeThEc0CZJ2HN4nzumpIqBWnJVHjAV_LF1ytbk6iPMgOKTJ4o8Zt_HK2WLymKrxqUUwaw_WwWQwEXarxd6nr7AuqBt13YAhbVcHozrfyBmX4F9Y859wG-GOhXU35BrZBvoV3ENqkKMkQcH-xHqt0TGIdjNr-VTrc96Ql-wy66xREBVihwkZxDQwZaIarWmrXfco6ejYaBhgMoOr8P72hqlkenHQq4XZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f023a6a08a.mp4?token=AQ-EjdEWBmhsxYHDaTm1ly4TEKnxUvqWxZ6CtnqijfFyPXljCFxx-swZh7lkTtlCHtc707OiTCNtgzVZUKEr1UiXo96XO2iKBnu0mAB-C2NPHl6gVnrJ0JTeThEc0CZJ2HN4nzumpIqBWnJVHjAV_LF1ytbk6iPMgOKTJ4o8Zt_HK2WLymKrxqUUwaw_WwWQwEXarxd6nr7AuqBt13YAhbVcHozrfyBmX4F9Y859wG-GOhXU35BrZBvoV3ENqkKMkQcH-xHqt0TGIdjNr-VTrc96Ql-wy66xREBVihwkZxDQwZaIarWmrXfco6ejYaBhgMoOr8P72hqlkenHQq4XZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهسا بهشتی قهرمان جوانان آسیا هم شد
🔹
مهسا بهشتی که روز گذشته در ۷۷+ کیلوگرم نوجوانان با ۱۱۳ کیلوگرم در یک‌ضرب، ۱۴۸ کیلوگرم در دوضرب و مجموع ۲۶۱ کیلوگرم ۳طلا گرفته بود موفق شد ۳ طلای دسته ۸۶ کیلوگرم جوانان را هم به دست آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/681064" target="_blank">📅 11:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681060">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4f34d6e01.mp4?token=pvuXCGUeViIYB_xdRnmk_fP9W3mYgvIjasnJmoy9ApcWfhXnujmm7eUaUHq0Ta7ZpwnPlco-fqLspC75fzKSVNnxvyKMPDEwo0hQg5ZOlI4bG_tqVqV-uVtwWdOZKhYkt53FsuuQuC78jJ-lCUj7TY6Z3Zwmjhk1_PnX4wx7GAg1JSvQKCesvOfFJQYZohAdCXrvE-RX5Ip1ip0GoEgmsWUPWTmst7mJPGdAjQtDBMjlEaNDnj1aHk8TCv6Qo98_Z5ZeT50VFV6iF2b5FJ5lU2EVvn0TrOKoqHOehsyV_LDfurTcjylrQPefzqi6YrGKkfb-wdxNu1qxcuJXhWQuqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4f34d6e01.mp4?token=pvuXCGUeViIYB_xdRnmk_fP9W3mYgvIjasnJmoy9ApcWfhXnujmm7eUaUHq0Ta7ZpwnPlco-fqLspC75fzKSVNnxvyKMPDEwo0hQg5ZOlI4bG_tqVqV-uVtwWdOZKhYkt53FsuuQuC78jJ-lCUj7TY6Z3Zwmjhk1_PnX4wx7GAg1JSvQKCesvOfFJQYZohAdCXrvE-RX5Ip1ip0GoEgmsWUPWTmst7mJPGdAjQtDBMjlEaNDnj1aHk8TCv6Qo98_Z5ZeT50VFV6iF2b5FJ5lU2EVvn0TrOKoqHOehsyV_LDfurTcjylrQPefzqi6YrGKkfb-wdxNu1qxcuJXhWQuqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت رسانه‌های صهیونیستی از نادیده گرفتن ورزشکار اسرائیلی
🔹
تلویزیون اسپانیا هنگام معرفی ورزشکاران دوومیدانی، دونده رژیم صهیونیستی را نادیده گرفت؛ اقدامی که با خشم رسانه‌های اسرائیلی روبه‌رو شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/681060" target="_blank">📅 11:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681059">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f818b96367.mp4?token=TAf-SEjBRbTZIhxA6uO9B3IeZI9cHU_0QIbM4Skj7f_UMMgZ5GaAzsrWh3Ha4u6NNpUiYtwjU2kYe6PULfVQ4RhDmUtI_gC9GZt4CWvccCogISEBSMIqOYdCEzAZCT7H3g5qvj5g30Yj5Vlg73Er6nv89XgBlFuP2J1V8m2snhjv0NyrUx_9xXF9UQ612NWuYml2WuMrtWzXu6z-ZLPefTRNw2I6xvtW-MU5fTmGr81uoD8JLOkJ8yhAfWv1RIkgDG-4MZxollXvLYYexKYPfMfVv-a-ODOEV3q0BiI2YTBawHF4cyd6NGkVtTKHMAycGkE-XYcWr7I2ECo7VurUlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f818b96367.mp4?token=TAf-SEjBRbTZIhxA6uO9B3IeZI9cHU_0QIbM4Skj7f_UMMgZ5GaAzsrWh3Ha4u6NNpUiYtwjU2kYe6PULfVQ4RhDmUtI_gC9GZt4CWvccCogISEBSMIqOYdCEzAZCT7H3g5qvj5g30Yj5Vlg73Er6nv89XgBlFuP2J1V8m2snhjv0NyrUx_9xXF9UQ612NWuYml2WuMrtWzXu6z-ZLPefTRNw2I6xvtW-MU5fTmGr81uoD8JLOkJ8yhAfWv1RIkgDG-4MZxollXvLYYexKYPfMfVv-a-ODOEV3q0BiI2YTBawHF4cyd6NGkVtTKHMAycGkE-XYcWr7I2ECo7VurUlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عروسک‌گردان هنرمند خیابانی؛ اجرای دیدنی برای رهگذران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/681059" target="_blank">📅 11:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681058">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904302f9b2.mp4?token=v6rvxx0pG1ldBGBNXSu6FvYxsrhXSssLHbh7iIBTgrQ8qH_zXNfKVstR5j2ffbRkJ_aMlmIfNXHLlmZfMvGvDuXDuoPbPbpvV5_klmCcA9Xes__vw_ggbY2wR8u2beWb2DHAk5LklBeFVq0263rhkEffWWnLouxNBZt3-hXKIEDzMc4k0MBmYsXeZlsG76Zj6WbnPlc_9g_z_QfLAAaxM7bD0975kHh0L7jkSysNX4lIQMRRcEhn52Ib31LXlsmVn_sdM20CtqhgToUuESvxrOXj5F1ZDAZGbuPObFjnrpX7-qeorvAZ4-M6tYzfi5UuEIkM0OlRkvRjIFf3ZNMjurfyIuqRMnyg83oStpRc_8q0dYJDzr4O2UAMs6-8kNekklkUuGe4UTamIUJv2m2Tt2oGL_tUSU-6X4AAbFxZHdCCSqCsoOijTCaMoIrwZ3iOJIifDbOUVPBsT6HwjauuVZuX0EAdoKs6YAyDNpfdMVQo_47Lv42YYnPW9HK_vQ1ufl6V2Uw5bNU35-QI2wbDFkfEOVxpyykzKiGmXfQzH6a4xTJnr9ypIFZ0a4eH27-i2-eMxWX5PTjo9YhFUjsYaYd4MTFGN0kKQZltLEx6JzYYN0x-qYYULGxt39Eulei5Q-lno9wVUog8yCTDX_FpxNyRqjWEtWbiQysBii5TltI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904302f9b2.mp4?token=v6rvxx0pG1ldBGBNXSu6FvYxsrhXSssLHbh7iIBTgrQ8qH_zXNfKVstR5j2ffbRkJ_aMlmIfNXHLlmZfMvGvDuXDuoPbPbpvV5_klmCcA9Xes__vw_ggbY2wR8u2beWb2DHAk5LklBeFVq0263rhkEffWWnLouxNBZt3-hXKIEDzMc4k0MBmYsXeZlsG76Zj6WbnPlc_9g_z_QfLAAaxM7bD0975kHh0L7jkSysNX4lIQMRRcEhn52Ib31LXlsmVn_sdM20CtqhgToUuESvxrOXj5F1ZDAZGbuPObFjnrpX7-qeorvAZ4-M6tYzfi5UuEIkM0OlRkvRjIFf3ZNMjurfyIuqRMnyg83oStpRc_8q0dYJDzr4O2UAMs6-8kNekklkUuGe4UTamIUJv2m2Tt2oGL_tUSU-6X4AAbFxZHdCCSqCsoOijTCaMoIrwZ3iOJIifDbOUVPBsT6HwjauuVZuX0EAdoKs6YAyDNpfdMVQo_47Lv42YYnPW9HK_vQ1ufl6V2Uw5bNU35-QI2wbDFkfEOVxpyykzKiGmXfQzH6a4xTJnr9ypIFZ0a4eH27-i2-eMxWX5PTjo9YhFUjsYaYd4MTFGN0kKQZltLEx6JzYYN0x-qYYULGxt39Eulei5Q-lno9wVUog8yCTDX_FpxNyRqjWEtWbiQysBii5TltI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احسان خواجه امیری: پدرم عاشق ایران و مردم ایران بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/681058" target="_blank">📅 11:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681057">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
لحظه حمله آمریکا به بیمارستان شهدای خلیج فارس بوشهر در جنگ رمضان؛ پرستاران نوزادها را نجات دادند
#اخبار_بوشهر
در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/681057" target="_blank">📅 10:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681055">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
جزئیات نحوه احراز سکونت مشمولان کالابرگ
🔹
افرادی که پیامک احراز سکونت دریافت کرده‌اند و به دفاتر پیشخوان دسترسی ندارند، باید تا ۵ شهریور از طریق کد دستوری اعلام‌شده، حضور اعضای خانوار در کشور را تأیید کنند.
🔹
سرپرست خانوار در صورت ثبت‌نشدن محل سکونت، باید تا پایان مرداد اطلاعات محل سکونت و حساب شخصی را در سامانه ملی املاک و اسکان تکمیل کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/681055" target="_blank">📅 10:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681054">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b369c954d.mp4?token=KSqeLv7vf6vWhxrpENqZ87TuwUIxzQ3oRfc6AlHNTAdPBHiKKxM6XMG3kFBxCJ_CAetpuj1NW7r10foJK4aNKjQQSJhlntDpECx0gF9p1_LsucIrWN7wz3QNecw3QRbTxu0ml1NGxuSNrNSmBa0_VW6cLW9F8Nxqkvql4gKAelQ3NFbKOJhESVYIl99qhHH87SyospD4dPJ_HBovyE8l1GQJMGRzXkvMTFpZXjITy_zS5km5j94Y3Cjf2R93RZdPY6eIMhgD5lqQnyaeKHqpH-OOob8tagfJqD58FmerrD96UN6gBqLroU44098VTKxmEG1qP8wh4SplZXW3FfMi-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b369c954d.mp4?token=KSqeLv7vf6vWhxrpENqZ87TuwUIxzQ3oRfc6AlHNTAdPBHiKKxM6XMG3kFBxCJ_CAetpuj1NW7r10foJK4aNKjQQSJhlntDpECx0gF9p1_LsucIrWN7wz3QNecw3QRbTxu0ml1NGxuSNrNSmBa0_VW6cLW9F8Nxqkvql4gKAelQ3NFbKOJhESVYIl99qhHH87SyospD4dPJ_HBovyE8l1GQJMGRzXkvMTFpZXjITy_zS5km5j94Y3Cjf2R93RZdPY6eIMhgD5lqQnyaeKHqpH-OOob8tagfJqD58FmerrD96UN6gBqLroU44098VTKxmEG1qP8wh4SplZXW3FfMi-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امارات ثروتش را به آتش کشید
🔹
تصاویر ماهواره‌ای نشان می‌دهد امارات گاز طبیعی خود را در فلرها می‌سوزاند و به‌دنبال ناتوانی در گذر امن از تنگه هرمز، صادرات گاز این کشور به صفر رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/681054" target="_blank">📅 10:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681053">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423325cef0.mp4?token=lDZyi8b79Uu8PxiRH2gtQW8Asxb0ks58jqPaMPc8Hsbx0tN6botUuKBckd0Ksqk6uCt5UyCLSXmZ3L63btJIrNodP8qE_NLc3cwXTmGeo3ss333oBwe0a7o_Jk3tWzGWLWoRXtFhvRhVXzZS3CU3BGRMv7zliF_vOIkbz033bzR7RFdsWFtxzV9UcRQ6_yn00IdmQDYBGWJLuTh5ZL-uAg-KcVAb0iDV-JlzhRvgl10PJNIrX0_P1GC8uUSp9jCv-CTsENXvN-bw_JUon9VWvPknfTpHtRdci8e0qKZpQoRDL4Oz_8b-LBjxYPaUMwV0Ux2Vcnm0t9eBUDLpp33GiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423325cef0.mp4?token=lDZyi8b79Uu8PxiRH2gtQW8Asxb0ks58jqPaMPc8Hsbx0tN6botUuKBckd0Ksqk6uCt5UyCLSXmZ3L63btJIrNodP8qE_NLc3cwXTmGeo3ss333oBwe0a7o_Jk3tWzGWLWoRXtFhvRhVXzZS3CU3BGRMv7zliF_vOIkbz033bzR7RFdsWFtxzV9UcRQ6_yn00IdmQDYBGWJLuTh5ZL-uAg-KcVAb0iDV-JlzhRvgl10PJNIrX0_P1GC8uUSp9jCv-CTsENXvN-bw_JUon9VWvPknfTpHtRdci8e0qKZpQoRDL4Oz_8b-LBjxYPaUMwV0Ux2Vcnm0t9eBUDLpp33GiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاس گل دیدنی نیمار در جریان پیروزی دو بر یک سانتوس برابر ماکارا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/681053" target="_blank">📅 10:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681052">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHx0g5c3vAbDl0f6SxVpUL0JlZOwntbuYzCMKD3g-ZKumtjT45UEmkAD2VHCypESvrhIEJbducEvh7khj1P4StDB3NAzn0rUT5rdKmLHlwpBEbSiXa71yfWuJxG08ytKZj0zVeFzQvALs3R3BjN6fzuqr1YaU76sY-HVHRE-PXaAvcCIjxRMC9HaSkApowisHXBp6KE48S8TD_AWeUtSQXR_IGQc9FY0wBp2ICZz4jeu6MLAbKICxVMmuWxIfnSaBWejneUWYP4jlPNmrVP04WaT-wVAiF7zO7mbBlY8lmRpvTY9LD0JwUCRScJKXQkqiF3K6fpy1MvIan6kdj3qlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دماوند سپید پوش|طلوع امروز صبح
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/681052" target="_blank">📅 10:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681049">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3543f5d98.mp4?token=Sr7rtSzmeWoclEcdVEjcE4egiY499FsUN-w2R2emr-5nSbEsu9ZONee8uV3z1YmyIzXALEuHFqNFmp5gOJLTQPapEsSEgqlGVQhM2Suvv8TIDXiE7io6GXCxk79TJHPzRAfcO0u3_kPvfpuqqqs0LobDjKTd9ol9ibwp0EBBCrbbaioV_VTOKT84LyMSAopL7lnGv9tiUxQQ-0yJ6om8jrfm84yL56t04T1ADLIpwPjXrT1GzvJigLDD0l6PRt0wFRR4jgaD_xRijD999IXuH7t21E5_bFA1DPEOQz68iRunfzGxXSIJ-b7KFvHhCP2aZCAcwE3jhPoHraXqzX--LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3543f5d98.mp4?token=Sr7rtSzmeWoclEcdVEjcE4egiY499FsUN-w2R2emr-5nSbEsu9ZONee8uV3z1YmyIzXALEuHFqNFmp5gOJLTQPapEsSEgqlGVQhM2Suvv8TIDXiE7io6GXCxk79TJHPzRAfcO0u3_kPvfpuqqqs0LobDjKTd9ol9ibwp0EBBCrbbaioV_VTOKT84LyMSAopL7lnGv9tiUxQQ-0yJ6om8jrfm84yL56t04T1ADLIpwPjXrT1GzvJigLDD0l6PRt0wFRR4jgaD_xRijD999IXuH7t21E5_bFA1DPEOQz68iRunfzGxXSIJ-b7KFvHhCP2aZCAcwE3jhPoHraXqzX--LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظ پهلوان آواز ایران
🥀
ایرج خواجه امیری ۱۳۱۱ - ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/681049" target="_blank">📅 10:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681043">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8d9f800d.mp4?token=PPQ4B9vKrlQ0FIzT-erOg4wYHFcG5SjNL8fNkJpXslwIhMlAu6XnjWykAABxoOoP5mafOfqlywfB9RyVVheAKBIORAm_kMHsuXLud-Vb0JtZL34wf9fx4m88ePLYkDCtSa6u0a-KpKohNay5y27jKYMXKOw-F9pzIMpUsF2DS1qSVVMFCawnHF9XeemZ2oYyWHTXa2m1PjypFRWNPAG1-P5R1giLnulNZTO1z1W7meZfYs7KXJU_FcJ8jtWyNCcl0AgdydYIBDkZIkIrO3_U6y5WSA1ASMB_QMsxPxOWwRc8-traqCYr505k9mev1df1RhunKFBGoUE3wyVztMlHKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8d9f800d.mp4?token=PPQ4B9vKrlQ0FIzT-erOg4wYHFcG5SjNL8fNkJpXslwIhMlAu6XnjWykAABxoOoP5mafOfqlywfB9RyVVheAKBIORAm_kMHsuXLud-Vb0JtZL34wf9fx4m88ePLYkDCtSa6u0a-KpKohNay5y27jKYMXKOw-F9pzIMpUsF2DS1qSVVMFCawnHF9XeemZ2oYyWHTXa2m1PjypFRWNPAG1-P5R1giLnulNZTO1z1W7meZfYs7KXJU_FcJ8jtWyNCcl0AgdydYIBDkZIkIrO3_U6y5WSA1ASMB_QMsxPxOWwRc8-traqCYr505k9mev1df1RhunKFBGoUE3wyVztMlHKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر روز ناسا؛ خورشیدگرفتگی کامل در اسپانیا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/681043" target="_blank">📅 10:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681041">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e21c7e90.mp4?token=d9NcZvJ2PsihkTrrX6SUSOJsvsw17JfZuaITPCIoe96X13AW5TRY9wHNJWkqjI7M04Mtbsi9za0kYaSOTRXcFJNdO_D5KZ0gkraO8dnJI-lFFaYZWTulDB6JkCPIFzuXuusziJfB_AYNUpRlxVMJzV9HC-tO5Mtt90bsnpjdIMWgRq24begRWeHcZCOx9-6frO-sCfk7v4Z07LFRr1vGtnsmba75IUcPizOGey1lUHtl7v1x6LjQwofJ9IwZMfmKSnZ73a6M8MMrxTnUowWWh35nTfCZXjj9RjdZ6UFs49YiAC91MK4Iw0nEi0deNzV0chNryGgM1BmuDtrCUyPhIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e21c7e90.mp4?token=d9NcZvJ2PsihkTrrX6SUSOJsvsw17JfZuaITPCIoe96X13AW5TRY9wHNJWkqjI7M04Mtbsi9za0kYaSOTRXcFJNdO_D5KZ0gkraO8dnJI-lFFaYZWTulDB6JkCPIFzuXuusziJfB_AYNUpRlxVMJzV9HC-tO5Mtt90bsnpjdIMWgRq24begRWeHcZCOx9-6frO-sCfk7v4Z07LFRr1vGtnsmba75IUcPizOGey1lUHtl7v1x6LjQwofJ9IwZMfmKSnZ73a6M8MMrxTnUowWWh35nTfCZXjj9RjdZ6UFs49YiAC91MK4Iw0nEi0deNzV0chNryGgM1BmuDtrCUyPhIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنجکاوی خرس قهوه‌ای در جنگل‌های رامسر
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/681041" target="_blank">📅 09:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681040">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/681040" target="_blank">📅 09:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681039">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: در هفته آینده منتظر اعلام خبرهای بیشتری درباره ایران باشید
🔹
ما اقداماتی را اعمال خواهیم کرد که در تاریخ انزوای اقتصادی یک کشور تاکنون سابقه نداشته
🔹
این اقدامات ترکیبی از انزوای اقتصادی در سطحی خواهد بود که جهان تاکنون مشابه آن را ندیده و همچنین محاصره دریایی است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/681039" target="_blank">📅 09:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681037">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5ef514aa.mp4?token=mTNjBfLehQ7qxIQfGOKNHqxlgnpj-oZjZms19s8E4Z4WeqhWG7HDD_zLGn2qcCmGj7DLhpmm0vz9Cnl0pgYgEUC7kqK2l15-CiTjNf9TPKsEVnK_-WbKktO7iADJtNHVUiTm4pQNosEXSl-yNblYjM5VitEybSZmQ7BkxiPQPWRFg2pZLPw5AtsxOIjYqskQSxsKBsS_UWmJZZpICe_4XhKsCkwxS3MF742vZl5O4h9mf0-2fMkTFBuhd2vLo0JvQoaGJeUqcSHV8GBA-_bnLioe42tsmx6aFSel8WTeo8qt_s2XdNUnfWPJYicT25z-DHGI4q9Sb_I6ZbAkaTuMlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5ef514aa.mp4?token=mTNjBfLehQ7qxIQfGOKNHqxlgnpj-oZjZms19s8E4Z4WeqhWG7HDD_zLGn2qcCmGj7DLhpmm0vz9Cnl0pgYgEUC7kqK2l15-CiTjNf9TPKsEVnK_-WbKktO7iADJtNHVUiTm4pQNosEXSl-yNblYjM5VitEybSZmQ7BkxiPQPWRFg2pZLPw5AtsxOIjYqskQSxsKBsS_UWmJZZpICe_4XhKsCkwxS3MF742vZl5O4h9mf0-2fMkTFBuhd2vLo0JvQoaGJeUqcSHV8GBA-_bnLioe42tsmx6aFSel8WTeo8qt_s2XdNUnfWPJYicT25z-DHGI4q9Sb_I6ZbAkaTuMlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵۵۰ هزار فریم برای یک فیلم؛ پشت صحنه نفس‌گیر «بره ناقلا» که نمی‌دانستید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/681037" target="_blank">📅 09:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681035">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUozSpxrsAwT0vCfWq6s9ure7A9P-tO1u2eh2KW29E9OlZ794i_3Cvmj1QZdpox83x9xXMhGGae6XghHeigMyGzO6XRqZKza8gwMgNjQC2i112huOQNWsyvLXQRwCk2wgTWmVWkWncxHqzgwjm_FIqyyeRtce4kt3Qk5Qdf1R074kmnROAEpFzjYIFWBFJk5r4DSjqBjHOItTPmwsyuzrEk9TGVFY4avcHdcW4Vi2l0FeJail0jiQSCqh5LS56_DqDlGu79ldVoZQyq3OAIS4sVbTc2H2iHeWDXZZ60nf6XO0xa8n2LyJToD0tlShb5mBqy2Z94_HomADG0e9jOlOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف جسد «دنیل سیاد» از مرتبطان پرونده اپستین در پاریس
🔹
جسد دنیل سیاد، از چهره‌های کلیدی در پرونده جفری اپستین که متهم به تأمین دختران جوان برای او بود و قرار بود بازجویی شود، در پاریس پیدا شد.
🔹
وی دومین فرد مرتبط با این پرونده است که در فرانسه جان باخته…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/681035" target="_blank">📅 08:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681033">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ae3e26fc8.mp4?token=Ih1i8z1oWEHpjtp9h93oWBH6aPREuuv9jSzyyB13uxaptgqZoaHv-tnbXXpBTD8r-dpY68fAp6mdJ4HlRP309XLYte5WYNj7I2v4tpNpj4bRkW-MfGigcO9A-hytrS-TNKuvDbMfZMMvojILNOT4VI7CqvJS7DReVsvaXdBVPs1IehldgixORDaQcjRiGI3r7jZPM2Afu3Z4mY0bW96PcJzPWj0ofre7rBxPRArpjgITw6Szdt0FhC8Rn9t3624ysiPiwzZVmUiJrPL6lydJ-ZRL7GLTaEH2wHOC2KhBNT8bLnCajD3OZ_CNl2faMK95yLdo0UQFn6kcvCcmTRK1zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ae3e26fc8.mp4?token=Ih1i8z1oWEHpjtp9h93oWBH6aPREuuv9jSzyyB13uxaptgqZoaHv-tnbXXpBTD8r-dpY68fAp6mdJ4HlRP309XLYte5WYNj7I2v4tpNpj4bRkW-MfGigcO9A-hytrS-TNKuvDbMfZMMvojILNOT4VI7CqvJS7DReVsvaXdBVPs1IehldgixORDaQcjRiGI3r7jZPM2Afu3Z4mY0bW96PcJzPWj0ofre7rBxPRArpjgITw6Szdt0FhC8Rn9t3624ysiPiwzZVmUiJrPL6lydJ-ZRL7GLTaEH2wHOC2KhBNT8bLnCajD3OZ_CNl2faMK95yLdo0UQFn6kcvCcmTRK1zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رد پای موساد در بحران مهاجرتی اخیر اسپانیا
🔹
محافل اطلاعاتی و دانشگاهی چین گمانه‌زنی می‌کنند که اسرائیل بحران اخیر مهاجرت دسته‌جمعی در منطقهٔ خودمختار سئوتای اسپانیا را طراحی کرده است.
🔹
به گزارش روزنامهٔ ال موندو، در پکن گزارش‌هایی در دست است که بر اساس…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/681033" target="_blank">📅 08:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681031">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f277ac0c0.mp4?token=hvf-cwx-y0aRX-6YIpNxe7OXjeWWxdDm7UFViOEjocS-EConuZRZUazeMOPIlkNHwbMfRyzLyJFOSevSAHBEliRUGIqyF8ZvuTOAVyBkmjx9etB12JBpbZ6uh69O78684rZ-svc9yaT5OtMEznnDmcLrsC5s4wOxBHlcVUuzZEeoVLa-gpoIMR7GvSDRyNvwfBb6ojJViSZqA1uqY7shMkJdYKBcs9bU1b2oVRJVVsxiXxuvQ1X5HXTOSC6G0SypRwLDqXZcDGHr5iCWVk5KAkytWSZT8uNvPBa2AuatyB_5QVNFKHWiiw3vcumwaXTE0QaSYUOFE281517jMfsQioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f277ac0c0.mp4?token=hvf-cwx-y0aRX-6YIpNxe7OXjeWWxdDm7UFViOEjocS-EConuZRZUazeMOPIlkNHwbMfRyzLyJFOSevSAHBEliRUGIqyF8ZvuTOAVyBkmjx9etB12JBpbZ6uh69O78684rZ-svc9yaT5OtMEznnDmcLrsC5s4wOxBHlcVUuzZEeoVLa-gpoIMR7GvSDRyNvwfBb6ojJViSZqA1uqY7shMkJdYKBcs9bU1b2oVRJVVsxiXxuvQ1X5HXTOSC6G0SypRwLDqXZcDGHr5iCWVk5KAkytWSZT8uNvPBa2AuatyB_5QVNFKHWiiw3vcumwaXTE0QaSYUOFE281517jMfsQioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلاهبرداری با عکس یادگاری
🔹
پلیس فتا از شگرد جدید کلاهبرداران سایبری خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/681031" target="_blank">📅 08:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681030">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11d7aa7044.mp4?token=CN3ZX65AawCi5N9rdqwaELtvKOxqBcTv_tejIFCnNgH5U2nPLaMo8CpNQfqniCvHjnzDKygB8VmGh8Ph7GUHKLpbaoffTANZIRMPPZsx0FDr7Tkl5z9jn3fYRFt0T3LuiphKI2-QhvDzutfsFJyuVQLX_xH69DhZuv0x1N_8gsXVCzcF_8wCkosIivl1cOFxyF84_bQucV0UJyiocztpz2B6BzZ0VYKXm2Nq91c9YmuzDuVTQTZj8PX8EU09DePQ1F4nvjMV9omMLHR8LyRjhW25GMyxXqpGzCaVBwuhr2b8u3QTmJ1GwCsMPRL6ueVYN6av9kIb9HeJzHreUHiKSRJmE21l3xLhCPvg5XTDPYU4Ic508-WvVtrZtWM9O9NxeSjANN8ple9ZrwRarbxZduhtI3i89IPZnY5QQ8mp1cqiRZ8y2GZtDarM3V4zdSK4d6kg5pCEKJIhbgDKzWt_VSGrzKLRbQYe7oXxMJ5a1vYCSPf4959APj3f3Detw4uQ4SdZ7wsLT7H_zC5IGXK62qVqcLtWRIoArrIFlC_AoOaDkplLiUfDtioTjN3tYj59D1QzgCdxe475m33e6wVBjIzsUR_WulvYywHpH5J4LNIuozBzVntweGUoqlDVplsFd8v3q-wssv1FX_rEOjHyHRJVUxJnDsoT34k7zpTaDuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11d7aa7044.mp4?token=CN3ZX65AawCi5N9rdqwaELtvKOxqBcTv_tejIFCnNgH5U2nPLaMo8CpNQfqniCvHjnzDKygB8VmGh8Ph7GUHKLpbaoffTANZIRMPPZsx0FDr7Tkl5z9jn3fYRFt0T3LuiphKI2-QhvDzutfsFJyuVQLX_xH69DhZuv0x1N_8gsXVCzcF_8wCkosIivl1cOFxyF84_bQucV0UJyiocztpz2B6BzZ0VYKXm2Nq91c9YmuzDuVTQTZj8PX8EU09DePQ1F4nvjMV9omMLHR8LyRjhW25GMyxXqpGzCaVBwuhr2b8u3QTmJ1GwCsMPRL6ueVYN6av9kIb9HeJzHreUHiKSRJmE21l3xLhCPvg5XTDPYU4Ic508-WvVtrZtWM9O9NxeSjANN8ple9ZrwRarbxZduhtI3i89IPZnY5QQ8mp1cqiRZ8y2GZtDarM3V4zdSK4d6kg5pCEKJIhbgDKzWt_VSGrzKLRbQYe7oXxMJ5a1vYCSPf4959APj3f3Detw4uQ4SdZ7wsLT7H_zC5IGXK62qVqcLtWRIoArrIFlC_AoOaDkplLiUfDtioTjN3tYj59D1QzgCdxe475m33e6wVBjIzsUR_WulvYywHpH5J4LNIuozBzVntweGUoqlDVplsFd8v3q-wssv1FX_rEOjHyHRJVUxJnDsoT34k7zpTaDuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لگوها این‌بار وضعیت بحرانی سربازان تروریست آمریکایی در ناو آبراهام لینکلن را به تصویر کشیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/681030" target="_blank">📅 08:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681029">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/681029" target="_blank">📅 07:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681026">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d201298a.mp4?token=pOi5zaxc1-YUo0E2n7T6BpTCF0BL3ZiXkC4yhDyBm0IJszs0orofxc5bRP52n-NxUmZXMRV4ZRPohjjM2jzvwEq0ncNnhC2ZIIM-U3UmluQA39Vxbt7M9Cx4FO2btf5MGQMBKdTe_NdxYghL7xd9Vb6fGNtqqN-KDSjK_KF8BwvzyMH0GLDS2oANqIpwBfa8WPJE_p4K3SzORGkj0qWDxmEvkz0db4RfjeAA9FJ_Sh4tFyT7P5hZZp2wqN66RxWMjADh3BBxq0smC8EMPajuTd_8Ci5XJqrlNfcMTJSkxD-UxBTxokCEApNsfHxGQp2KpFs6wdmAGSg1EYpnfs7OuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d201298a.mp4?token=pOi5zaxc1-YUo0E2n7T6BpTCF0BL3ZiXkC4yhDyBm0IJszs0orofxc5bRP52n-NxUmZXMRV4ZRPohjjM2jzvwEq0ncNnhC2ZIIM-U3UmluQA39Vxbt7M9Cx4FO2btf5MGQMBKdTe_NdxYghL7xd9Vb6fGNtqqN-KDSjK_KF8BwvzyMH0GLDS2oANqIpwBfa8WPJE_p4K3SzORGkj0qWDxmEvkz0db4RfjeAA9FJ_Sh4tFyT7P5hZZp2wqN66RxWMjADh3BBxq0smC8EMPajuTd_8Ci5XJqrlNfcMTJSkxD-UxBTxokCEApNsfHxGQp2KpFs6wdmAGSg1EYpnfs7OuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریاچۀ ارومیه دوباره تماشایی شد
🔹
با افزایش آب دریاچۀ ارومیه، سواحل این پهنۀ آبی در روزهای اخیر بار دیگر شاهد حضور گردشگران و مسافرانی است که برای تماشای جلوه‌های دریاچه راهی این منطقه شده‌اند.
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/681026" target="_blank">📅 07:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681024">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Shs5NLzUsL-osizZprtz2p6eOxULs3plFI27EMueA0qblV-y0DpAQ6hS8xV4Go5XQCu_CnFdKu77yaRgBWp1392ipWncYyd_UuCoQ0jVxuK4yihRQh2wDPwdFkdDDt4fW5E9vzaF4Tsx0U5Q2n-yfaRexMG-N7LHTMixv3pF9B31wTB48Tt63yoAMnFEWMXF5-ni4cltgWH3VyQ66V0Od8GhRlNLN5-E6_PFYVFCOsi32aUV3IPxduubLgLEPjQd3osJ7cAlgvr4KqdmwD0i8yibAhReCObqL0CNJzTCB469OnDwR7H0gp5y28wFrYglcon3TPVrXqAvg8Eh0xdf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۳ مرداد ماه
۱ ربیع‌الأول ۱۴۴۸
۱۴ آگوست ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/681024" target="_blank">📅 07:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681023">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromربات هوشمند اطلس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlfDwI044nF45pLQPb3TuFB3KbnXJ0cDFu8BmstXWks1aWWOpSSt6gtrivsZEf9idT4q8eFxzzbruOga81VNNpKYc9xEwiHCIWlVm9__eiVbUvXtquyXPOdtN_EtdVYnxXaq-7-bA9BpwATSLHsQJz-N_YaTHT02vFRu9mi0hl2nPvTX61a1RQMAgjjTR6wTdpzEUNf6GB9DdpqGfE1c7C2Vv6a1DV58RQTdbztmhLnH-MHGz2pGeiQMUBaHnMofdl_ysaNll0mbwOygOHF_YpsGgqnBAN03JTq_s472UoLPzK2adSDoWdheA_zuTw3mUhogCYGzksDeuPQN3tschA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/681023" target="_blank">📅 05:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681022">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
عربستان: ۱۳ کشور به طور رسمی به ائتلاف دفاعی دریایی پیوستند
🔹
وزارت دفاع عربستان در بیانیه‌ای از پیوستن رسمی ۱۳ کشور به ائتلاف دفاعی دریایی خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/681022" target="_blank">📅 04:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681018">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb41d2dfa8.mp4?token=t-i6riqvM2vrMohx_OCOPJGiRj1JwcAuqiRsm3KbknYn3sl31WNRAHhAtPmnBcMKuBfeKRxIkw_x9f0b-jOp9-KIQUnPT-c0-W2glGcDQnlD9zsefmphFqXIqXcqe4rnYAZjWtKGq855XwT0WSn_oZRuYpBEcNmVe-Af5Cvv1qf7XPKx_pbyx7Z07XnYN314HjM8OPlXn9-GHdr5M90BwiDczSGAF-sHGennPz_X178IrKfpZQosIdGFFHI20xBzLRUKcpnIQDZnLknmMCJvCeb-V0bbywesQYiB5ZZ1FWjwoqAbBsCNvBugJmfRZdfOgLF-kvG3ZLY5k6azahkWdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb41d2dfa8.mp4?token=t-i6riqvM2vrMohx_OCOPJGiRj1JwcAuqiRsm3KbknYn3sl31WNRAHhAtPmnBcMKuBfeKRxIkw_x9f0b-jOp9-KIQUnPT-c0-W2glGcDQnlD9zsefmphFqXIqXcqe4rnYAZjWtKGq855XwT0WSn_oZRuYpBEcNmVe-Af5Cvv1qf7XPKx_pbyx7Z07XnYN314HjM8OPlXn9-GHdr5M90BwiDczSGAF-sHGennPz_X178IrKfpZQosIdGFFHI20xBzLRUKcpnIQDZnLknmMCJvCeb-V0bbywesQYiB5ZZ1FWjwoqAbBsCNvBugJmfRZdfOgLF-kvG3ZLY5k6azahkWdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار‌های شدید در اربیل
🔹
در پی حملات پهپادی به نقاطی در اربیل، سامانه‌های پدافند هوایی فعال شده و همزمان منابع عربی از اصابت چند پهپاد به اهدافی در این شهر خبر می‌دهند.
🔹
تا این لحظه به طور دقیق اهداف این حملات مشخص نیست و برخی منابع هدف قرار دادن تروریست‌های تجزیه‌طلب و همزمان مخفیگاه نیروهای آمریکایی را بعنوان اهداف این پهپادها عنوان کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/681018" target="_blank">📅 03:43 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
