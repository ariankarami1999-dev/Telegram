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
<img src="https://cdn4.telesco.pe/file/Z78h1wQn5tDrchqtg4Yz0Bkx-wMdPgIuOTETZtTWt11oMJ0Kufl9pM7lg3uGAxuswBPeWK6vFvVNZmQQQ9V7DM2omv_27kdRwiraMHI2scF1WFLxZjakyrdxiboz5fDOlexAF7dDp_m7R0vAaIw3y_fQAJk_Hpw9SWH1p40huxq6HMBtrBmYCisBZ-II7FCBpdMnacDA3AKnt55Nubbw4QLC3FkI33fiP9raoVOVZszdC2pV1nPcYKW9DJKZERnyGG5tWyl5g-_6tdOxsD7uXfjLIf0QrDIEQWlmZEevWAQx-56cVjgymZRJELk_A3tQUJiB_NUHCHhkx_HFxUfocA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 422K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 13:38:29</div>
<hr>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=XCjyf-_PHk-bnHvYW9ZRNJoZtbuMqWKCGqABa1ftUVcHaCoCFgQFlyHxogKv-SXEZmmPbpswlDonAb3gDgEesMQGCwflDzrfV1pn_eY9bgE7I5ERKysszhbFoNXSx5GlGQ0_fL4bai0ZLUWCK_ICtEHoyPSNWjZzuI23WR2iNn3rIt16Ie98qKbaT8ZMMVOAWPF6WAxUcF-Zb4FQ6UU3gNG5psqEWHM0gGnJmvECf9pqcJnV8gZ0BwI1d019YppgaeIBP_ta1TChJmP8h4IQ_TM1VBXU0mjIfCgejhg_NGqJxtwTx7BI1RYy2ojCI4F9CS9xgdPBbBcENCRYyd7pRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=XCjyf-_PHk-bnHvYW9ZRNJoZtbuMqWKCGqABa1ftUVcHaCoCFgQFlyHxogKv-SXEZmmPbpswlDonAb3gDgEesMQGCwflDzrfV1pn_eY9bgE7I5ERKysszhbFoNXSx5GlGQ0_fL4bai0ZLUWCK_ICtEHoyPSNWjZzuI23WR2iNn3rIt16Ie98qKbaT8ZMMVOAWPF6WAxUcF-Zb4FQ6UU3gNG5psqEWHM0gGnJmvECf9pqcJnV8gZ0BwI1d019YppgaeIBP_ta1TChJmP8h4IQ_TM1VBXU0mjIfCgejhg_NGqJxtwTx7BI1RYy2ojCI4F9CS9xgdPBbBcENCRYyd7pRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو ساق پاهای مسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=m-raVWwDxo6kCN4gWi0ztKQS0ILostn3NGg2043KawJFkBDRgsC68M6O8xYO-e4o8XhW4xmEZawxM-_YOHxfgH6p4G7EITywSsCRr0diKdm-bzG5gWcJDViTtHfQ5AVxAROtQRgP4pwRfrXw267lUd4FF2q_JkDMovS3yBLTa-hkHrr6VE9vfMHdxvK2O-1_wxM51j0ZNmTiogN9VBUWXrDaPQxmFEyC-nMYeAnZuPsGX_vuTMj8QwzVw-emK8EbJMBhufR4_OYL_wdH2Vug0CooRJdFztOQse-it9iA90bW5WpJ3mfIN46LII2B-_r0592Lt3ZLmJw59kVOUQQD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=m-raVWwDxo6kCN4gWi0ztKQS0ILostn3NGg2043KawJFkBDRgsC68M6O8xYO-e4o8XhW4xmEZawxM-_YOHxfgH6p4G7EITywSsCRr0diKdm-bzG5gWcJDViTtHfQ5AVxAROtQRgP4pwRfrXw267lUd4FF2q_JkDMovS3yBLTa-hkHrr6VE9vfMHdxvK2O-1_wxM51j0ZNmTiogN9VBUWXrDaPQxmFEyC-nMYeAnZuPsGX_vuTMj8QwzVw-emK8EbJMBhufR4_OYL_wdH2Vug0CooRJdFztOQse-it9iA90bW5WpJ3mfIN46LII2B-_r0592Lt3ZLmJw59kVOUQQD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
محمد صلاح فوق ستاره 34 ساله مصر در پایان دیدار با آرژانتین از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqXsfHkEIUSLEV6Cs7ln8GHLoP9PL-abFSVLQ_myZQsATigIsO5nIbCYmouyNV8roiugJvgsZvicPAEJvmqcGDOiQB4Ifu85BoA4SPgobnhtK5JXlZTd1GKw3bRj3G3zSTaXc1CjPErrqC0KH6v7iLIutyMWSTGVwnSFy9l7mG7L6qYjzDP2USptayGC8qZ8ROHSLA25xiIEsxVU51BafcITJzktxgfDqQTIOCvl3cQvYUqnJEuCJy5NKOjFg0wwpmAyk8RhDgnBsoYimrnUDoRSdFOwSCj2TdSiugavWb2lEpBMBtj-yybebvnto6NpomVJCYXbDvI8mjY5jyyT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEwDv0T2aKMSk6TqUnOkbQj9SrGNjOlU5zfJsp1kcWjbmozhx-i6030CBZB-bRdTfEFXueiepyNaDQJNsaoILHn8fQPn4bNNwhSGp-60CwOJo2o8bfMmg8QhiQtw90A_FOTyNcKdJ8dJoCVTl_lh1IaYslYl51MuXZqkDVhjYCalITPA_amgDQMn8vSmH3As-K9IIErrR11WGBb6SxOuY_4sRYTum8kEAo-AqRc441mmciiKTmiF4gNXoB0b11n7it9zc2bjzYUg1-LYbIOK8xwNeWk8w86l_PKm8e108Sh-uRbJGZEm0LLAZyvOQhcFTpAN5bZV_JvaFnC53AJSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP3HpIq2JsDxDBJk_F-344YxVP-dnsub8-VSE9BNxH-7VQHq9UWdeVQKkMrRtYDB-6Gkp2I2t-nT8nzZQu3ePn8G7OjON9ynlz5PVPfS_-yLRi9q0nKsf3I5OVddKPc8Z1h_WkjiKdpymEWtc8YRZ7CY_B76B1cZMS0Dz-vT0cTRANwjW21nASYunhFBDbmm73kBJvYMP6nAfkWNPleSHLBybLIKYoYONe8goXNRVtwRqI8-xSY95qKDMWlSbwWEVUEf4oTAElYyndwDYYhITi34VYGfZoJZwiYOc-QIIvkcKA4nBEk4hTtFrd5l2SJqKT7z6JXS5X_jDhbtWcAX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=RBKSJD9aIMHMsrOY6YOBi8IgwOEfpaptv91N9GYOwzaok0Jbgkgn-sj8BIVy_kaBCtgErjsmH0wXANeoygLhPRHz1ZGDjSFz6UZxTejMh8gOJywg6zX9QPMYR-fIf3CsQUWXpeUcsANDUkUVflWTGOoMDDXcqQC2CC-nWebg5FALBvesf7qU_eJ5EToWw9NY5PhlZdPxy9fnsoCnhQmnRQ7KoJg6m-GwK-g7OHkWQaGn-fKBF3b6Zz6Qq3T9labuLD4xqAuZhTAuruSf_vnrJRVSgO7Dv85xCZ4I1t9cgeAvNy9nDWwX6FHf0NWtySrKZSLkvSRkwpF9Li0-pk40ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=RBKSJD9aIMHMsrOY6YOBi8IgwOEfpaptv91N9GYOwzaok0Jbgkgn-sj8BIVy_kaBCtgErjsmH0wXANeoygLhPRHz1ZGDjSFz6UZxTejMh8gOJywg6zX9QPMYR-fIf3CsQUWXpeUcsANDUkUVflWTGOoMDDXcqQC2CC-nWebg5FALBvesf7qU_eJ5EToWw9NY5PhlZdPxy9fnsoCnhQmnRQ7KoJg6m-GwK-g7OHkWQaGn-fKBF3b6Zz6Qq3T9labuLD4xqAuZhTAuruSf_vnrJRVSgO7Dv85xCZ4I1t9cgeAvNy9nDWwX6FHf0NWtySrKZSLkvSRkwpF9Li0-pk40ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=C-Klz2NXWpVxmbbFJjQXoQTyA6yRI7j2tSCIW5gIwIf1mofC4IoJTpIxr_aIxCjtkK_hDQcYrvFVycJcQo8EDyLdW9_AiGuxtlabSL9L4kxmLnOd3NeakqAPS12cyy6LoW73hlB5VZzG54-o87ltWyk-hnIvubJjbnyZlvyTMuWLEbDi7ttajGRwKOfwjiUNvlU6duisL0M9QFg2bdENeLvO8hpLyOPaabrj52dy-RIcMKdZahZJuO-2Q-I8Z3ZnlNrux5jony3i-qL0r-jXv6sIwB9hvEMoz5hcdaSxKXloV4O6kr7H9DlzT6tkbjxtEvIMHuDuu2_Q_SEH3JoF_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=C-Klz2NXWpVxmbbFJjQXoQTyA6yRI7j2tSCIW5gIwIf1mofC4IoJTpIxr_aIxCjtkK_hDQcYrvFVycJcQo8EDyLdW9_AiGuxtlabSL9L4kxmLnOd3NeakqAPS12cyy6LoW73hlB5VZzG54-o87ltWyk-hnIvubJjbnyZlvyTMuWLEbDi7ttajGRwKOfwjiUNvlU6duisL0M9QFg2bdENeLvO8hpLyOPaabrj52dy-RIcMKdZahZJuO-2Q-I8Z3ZnlNrux5jony3i-qL0r-jXv6sIwB9hvEMoz5hcdaSxKXloV4O6kr7H9DlzT6tkbjxtEvIMHuDuu2_Q_SEH3JoF_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای آلن شیرر:
یا هر دو این‌صحنه‌ها خطان یا هیچکدوم خطانیستن، نمیشه برای یک صحنه مشابه دوتصمیم‌متفاوت‌گرفت. مارک کلاتنبرگ هم گفته هر دو صحنه خطا بود و پنالتی رو صلاح گم شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/25196" target="_blank">📅 12:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCID2MXxy6zHk5YObNzRAS9QdqDZt483EukimwDwT5be-8RwBrp33tZ8iqov8umcUGZTlR0aoockA-T6jpQ7AYdpn5uX7QTS7K0RDuulAjU_OaPX0qASqOibbenDhL484n4DGrq7rITrkWkF-Wo3iMIqo9pUx8jGaYv6Vs5ksJTKt3Dm1H8nsepEQPSh-oI23pIm0e1Cer8UYhyBHdJmMDyy7XxsY705JKc_k8NdIAiu-ZQoLO0NKV0FqyadKM22U7hVlIT-R2QKSDhwAnUOcAPpABDaxDynq2vMLjXe8WEDcWWjW-4rQT7y7-sqjBZ1U3_rTvOEPzID2xHxscdUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/25195" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQSMf-0ClGK8NOdkR-E0SEzhmhBkqTaJouAtvkqhGcVB3_8PlvYbvbnU1zqOW5m5_bgoHCaDqgVSuVm7MYrXHlRGr2f0NDjZuwNYS4Xt41vMqufWNajLd96EHEL090mkCcp8viAk-2ugT0eEuHOrbTdYT0uwCI3vEK3-V1TwqIuBZK4bRYSMMuStha_PSVdNiFsh7zh1ZA9_fzWtRRLEYdqkeQspK-McDg02kNyoflIrZPNptyXGZmynw57QnmJ1UOfhVwyUu-OP8SY8F1dMsO90BGkwJbyabj0ZsYYePCy3LrzRMkeQ87F0shm4gkr5HvVed_wiqBO0WVzhs8JX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛ ترامپ:
دیگر باایران توافق نمیکنیم، آنها فرصت خوبی داشتند ولی آن را هدر دادند. آتش بس بین ایران‌وآمریکا تموم و داستان به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/25194" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chHr-gE8c7xKyDlrMhKADzTPz3XUwSqH_gVxP_wPsOf-2XvUGXcN4HK_mU8WxfvFtsgJwI634RYwU-KZGVIhimRM895Dca9SWvaaIq2EdKd4FiK8lbDfday3jdX_tCc8OGmOauHDRwmfo_D42uWNzOdcPffmJKj32AjX5ngiin189fb-tADZbL7IeywnFYOQu67vph50mLIqsDOkn87eOyxnnB2hdGbC9xyb-SqMoGTjrzB_e_3O2-E1P_Laz_SguvSPTJ1oailfjHiA1cJ_F74KwiSeBeZYQIaUHNFy9gZ2eDJL8_4FvuwPCxFxfp7OT-3f9cgMW0b_7F1UUMycoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/25193" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB5iNiIITrLGHX7CHeKk1xpzwn_D6SMmmnPSwLea41fjV08AUu-fNIWvM84NClXgkhPyJ6Gzc2xYlncPdUnMS7fhTyf9KI4NhnfVjbyUK4LpMskQV-G7pZNC4yzH993U3xDhSX24FU0WklNnq677KU9_4v1HKOnsZVaqLToQMHWTbFmZdOYd-GHy_JJpkEPlO6ocxHl4BCyqCoMZ9RwpaYBOFG4KtFGhHS_gn8uR4pd2pdZ_ospjjQTnTyAXrBOY8WKS4EikjZiSckp3FNs4pQpOyvo5hVwvpO0e3HJUYW9_K8QXqF5FnLAWNOCM0rfwiznFDfgFpIIk89RSlQvkHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
#تکمیلی؛نشریه‌گاتزتا:سران‌باشگاه آث میلان به دنبال جذب فران گارسیا مدافع چپ رئال مادریدند که در لیست مازاد ژوزه مورینیو قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/25192" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwkMYG5uWb3yXqLq2ZWSBOZL5pz9Wd0jDNsHRKOhXuzyuGo5kwIieryGyYn81MU4tz8_sta3vfScxSN_RmsCPLq6f6zF6dSizLrvwNuWnBIUEyc2CdTyQD4mgeKa0VoHB0lw_Ou2PFzNL3Dvde8-FGXHtDdiVzhfH9oZ1jTI7xfuWFR79hPBZoTC3GBubNzyeUlKdj9oRfwb9rr4CfTmQozIh-t4UZwUbrZscszEeF2pPLCgLb1cnjiJZEyMHfN540iDmDHXjOJxwCmHFrlR5Ixleen4LEvzg6qIma4RDDCb5Buh23ycqKLWKuUa9rtD0oO0ZcS-9GgoywjASx5YPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAMCtsOKFAneuywziLtQw_-YL8SmVMUt-Igh74AdVUkVxALgncYEn8p-v20wJzCQahy97rWisjAbmzOf9csNUqxT3r91BVqxv2LejNGNiUJV5Frfp1g9is69nbfNUnxuXifNorud9vHeEzuWLxc2MAycntr5Bv1XXzHZTXg1RZpJegxFA15ep63iGKA7DVLqr5mAwZMoEGB6LLCvfcJUBKGEqzh_mDAfEgYFv4tpqx1aataQtDkKLE9Sn42_ZHWRtIMQ3K_fEaa8-o9iPCWYYYPi9EHpmtdgqlCZG7tl8nYzbMp7bGnwiknaDvNzm5Ip35v9HraCpNGYlOV0VGMLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/25189" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYROZbdDK_NxMC2HyUbQvOf_qT3p13ltJTvVyE_a7yLuE0urp9TFh-t2R1hfBxLiOOhoZoCXKDUB2_53yNAdodTb6GyLbssibuxMozQboLN6APB3FNbB2USyBftbFoxeSFfjcuc3E0VYP_oI9MeAaEKTdagFUfzEOQmeY58DJGYzTAzIz4IyIYT1aAJVCpS1ZsB5lYPCh2z-KyG8uxgHfoMKqRqlj-x1a1LB8kd_iJcUE8DedeEWt45xzdLB1jJxq_NPjOWxK8GXJIFjbPnDJn0BlCgOlNrU1QcCE6ufqMGzVwHwol_Ti0F-4F6cY3K0OmMJukmGkR9W8MGbzCBzog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مونیر الحدادی ستاره مراکشی استقلال که قرار بود اواخرهفته‌پیش‌به‌تهران برگردد بدلیل شرایط بارداری خانومش و هماهنگی با مدیریت باشگاه استقلال روز دوشنبه هفته‌اینده همراه با همسرش به ایران می‌آید. منیر الحدادی دو فصل دیگر…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/25188" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGgaRuVbRi6f0hNF49iILqfBBmbHFbJGO8DBNrP6YEe_2Mln_KAAEcKh26egBlQPS1QGw6Ykw2gTUI-5quIH_Yup81i0uyEEHZyuQj46LsP6m4nZhMs5Yqpus0mmAURu620W7-GaoFKdizNcQXYFPV2rJiKmQCZ-R9J6RGtn5l6hwXPWRpbXycqMd7DYrWxhPFPjcCLGlrguUhAUIEB1KbCf9Zbq9QAHHhZoQSVLcGfFpu5pU_3uWGLa_dbXzcJLuuFKR0TuAQnyRbnT3O03JSiIoF3UhOliWzn0J7q4L0VuB6vzzE1AkQ7t-Xar974lymqCIXUCgVhe7bBypVZyMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/25187" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=axqS-ADnNxhav6IAehisNgBTo4DxyqTmOjPfOpqCT3IXPg0BssEnqqdcdz2DkHFbv5eeYj1caFEld5x7-tv94vtwvSTQZAOGXBspaP5GjPgDc9E9XEyOaGH7NI2r31CPtsWyvdQEkFvPU3ZvnTjg3883GvrdZ-0wt2IVsNyNQlzM2l64BDlYBi2S1V3WvfEwmZsy39eV4rOFXHnL5W7HqPgOj810FKAnbzcp_K1X4Xj9aVUmKo5WtmQLx1E0_BjBg3iOsZS5zajEBNPTzQXpkkqQ29Y2stAAYosmbWmdk0MOD3LmDMIgfVJEX5mp6G55TaMEmbLfL4FdjKdxz-eikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=axqS-ADnNxhav6IAehisNgBTo4DxyqTmOjPfOpqCT3IXPg0BssEnqqdcdz2DkHFbv5eeYj1caFEld5x7-tv94vtwvSTQZAOGXBspaP5GjPgDc9E9XEyOaGH7NI2r31CPtsWyvdQEkFvPU3ZvnTjg3883GvrdZ-0wt2IVsNyNQlzM2l64BDlYBi2S1V3WvfEwmZsy39eV4rOFXHnL5W7HqPgOj810FKAnbzcp_K1X4Xj9aVUmKo5WtmQLx1E0_BjBg3iOsZS5zajEBNPTzQXpkkqQ29Y2stAAYosmbWmdk0MOD3LmDMIgfVJEX5mp6G55TaMEmbLfL4FdjKdxz-eikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی‌از دیدارجذاب بامداد امروز دو تیم ملی کلمبیا
🆚
سوئیس در یک هشتم نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=WxAkFusHBrF9pE3Pg6IGhnPbJNkb7kiizwovFazQGB18JgATtsNqWzEFIKrGys8G1ZfmMCrI440AuQoVCNo5cajMff3OBdEm0OsCaBuiWj5wtXFZxih_5iGzFvSWZC1ZS8PdteK5YacYha8Lg8dYSNqKhhlSARAHCl5CIboepXed83a7ldDSiNd_SSPdx2gVOQzIxeX2srDswhO_Or72pB3kdukQPwCDTkfu0nw4HS9jRs2Aka_oeqrN5dUcNDbHAplXDJb6xGwZ-kyiNI4mks2qWDx2-LT62tWmSUngXlhcxgQkUKR3Q6ZVuHVUKxN-g34m17OlBbt-RrOJHkk8yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=WxAkFusHBrF9pE3Pg6IGhnPbJNkb7kiizwovFazQGB18JgATtsNqWzEFIKrGys8G1ZfmMCrI440AuQoVCNo5cajMff3OBdEm0OsCaBuiWj5wtXFZxih_5iGzFvSWZC1ZS8PdteK5YacYha8Lg8dYSNqKhhlSARAHCl5CIboepXed83a7ldDSiNd_SSPdx2gVOQzIxeX2srDswhO_Or72pB3kdukQPwCDTkfu0nw4HS9jRs2Aka_oeqrN5dUcNDbHAplXDJb6xGwZ-kyiNI4mks2qWDx2-LT62tWmSUngXlhcxgQkUKR3Q6ZVuHVUKxN-g34m17OlBbt-RrOJHkk8yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی از خلاصه بازی فوق العاده جذاب شب گذشته دو تیم آرژانتین
🆚
مصر در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjMYdaezMOmA7S1kV8SQmfmy9o9Yt7kPco8f7bNgw-i5hq7CMV5hNLZD4mUcrBBymUylFt1BQeTjVKQd-17s-oZviY-gmFMVGVM1ziDprzTy_WSvfdWVKqtzDeY9OyUVK2ZhqnXxQaTCV9zBIGrXigWrWn0pUFWbJgP15YWeRjj-UmZW7AHGAv2eyRpqnhmeQf0TgBk7dLqvjhb5HcAyCbS2nVZQvwnPOe2FCicQogqav9dD9XnGegCAzhcK0gDxp9t2HXDNGAmlNGw-RukVpZRczhcoLJ-WCvFYevezMA1ObNPT1V57QxAY5kyC7Tu2sQ5I3ZyXcmS177d6ffZSMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_YCvpSJO7psqko0jc87T4B-kgA7FDZ-Bu5QRngCa43alzva7RNcp8RlheTGAD9zK8Wi8IBUyKW_pbyizPgavZsv3KU0SFmBZqyxYBnjqu7d_T8adjOaXGkRzT3VYs5U14v36h-GJ6NMkeC-vR2w-b4aAw9Mry9YxMChzdOjefT8nhrTjihY_qR6hpN0FpQK__x7q8wP8E-w2aipMCwhzbzdzjyO93xKJwsAT3rAWpjnxw9egBtoustmwQ7XcJeDk2Ambwzey0VruakL1ATbH1uC9SlRaaYic1maVseuGtHCuFOtkiX-nj3DlvGlpSCG2z9w0qPfb-tFXCCgGTBnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a56858395.mp4?token=kW_JlHVP64hbYAPTGzLuo_gchOAaDfSIz2y6IRWDzjnyrWMIAMeZmEQLjHOr0ruHWu2GjoqDlje_QrZBW2Up1MOqgQSjHJO_TEUCICP1Z8LHs3hw465XVIF7PHHM-oUVeYr2Yu-cm1ygLsIIImJWn_CAGUFU0MNXVA5Bafs1xC3E0jwd879RPbgvpleI_FZ10bvgnaMhEWPkzzYz2x6A9wvY59lJtCNfw4w-JyrUQWtXpoOmmcZktN2bMdhDFByPB-UzBMWxUp1-j6w-MK4XkdoEzFqXOE6G8E1U4hCr9fCDHDdtxUwjLqM1wPg_mtqz9XgLpGQdulKKe5yw6RXmjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a56858395.mp4?token=kW_JlHVP64hbYAPTGzLuo_gchOAaDfSIz2y6IRWDzjnyrWMIAMeZmEQLjHOr0ruHWu2GjoqDlje_QrZBW2Up1MOqgQSjHJO_TEUCICP1Z8LHs3hw465XVIF7PHHM-oUVeYr2Yu-cm1ygLsIIImJWn_CAGUFU0MNXVA5Bafs1xC3E0jwd879RPbgvpleI_FZ10bvgnaMhEWPkzzYz2x6A9wvY59lJtCNfw4w-JyrUQWtXpoOmmcZktN2bMdhDFByPB-UzBMWxUp1-j6w-MK4XkdoEzFqXOE6G8E1U4hCr9fCDHDdtxUwjLqM1wPg_mtqz9XgLpGQdulKKe5yw6RXmjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دو ویدیو متفاوت و تامل برانگیز از کریستیانو رونالدو
🆚
لیونل مسی در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk_NIDdoaCiuxuUvVA6yPdnC65rpVBrA4sXkJg8k8u9t22Yz30CFx32Q4Uk1eS43p1ugY8e_1bSitRUxGyNXispfedPFD6AeSjz9ZA5C22DGiXZSCPcLx6StP87sbdcCidESzil672JO_waScvrz_gsgrspD7OArzGUTfzksOAkPTTqZ7-QyhWcbe0aR0bFHN4FSxepAOT54hlz43K-ghgmAQStESC76q09Yvph1S1c_AQUp5M50HCrYa_XL4sUt2wKwc6uSq4YqfLodFoP6lC6ghxEyBjRq89XQ_GFqxCV_pdwFghRbsQVkhsGiLdvf0VIIf1c03mhEqan8MXx_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU1uswUELUJkxt2JVXs3dEvCKxnaTzR9QhTZfrI4gIXwtPMN5y2_Sk5zTJioi8c-GcZP-0veotoHwJwZBtnN_y4rdE76JIj347eERATu-xvVSYvgewJ2hq88i8D9_sBXhvkTUAw7WOcBZ_ZMyF1mKe_T6TgJoqOpIjnDEkijKrsm6P1BR_ODc9IlMfFN--40l5wcj7QcKRXk3w-8nAQvpGP-Ky6qvtTm29crg4rrwKVWk8YSNl7MwzMy1-LAQk7uMP8RbFXdFOyi6qMXpTK8WHC-XZr8bptfMRAfVp03Q8dWIujMB8xVRAqd_WIGgN1FrGWNjSBGuJ3hQ73LQJyQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25180" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lutGogflxoDdJpAfyNdOUlv1FwATUMUEOM502Q3OPp-Ds-C90-TdXg-bvo4up33B_nbKR__gPTrDdTsKSDx_v3X4HsP605_rjG_d-l_Jx0ODpclxvjKQkzt7m9USCot8jMOKQEaVv5-HQuzFkSas4S0OfK2s9CZVbT_F6h-azhvgmcwPAUQBQJI8Ztk_Jwfm2NXzV_CmrJFYI34ruaFweR3lIOk8gFQMslFyjV2u1B3HwHcc5xh9v0PG97d6pOZCg8J45ydvmNqvHjdk1SlMWYMbH-ByhSO94yo9rRn_QU48vzdXVqZ-A9Sx1Ao0wCbujsTacCgGlJ1PjZW4VSIqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای باور نکردنی باشگاه پرسپولیس: دراگان اسکوچیچ برای یک‌فصل سه میلیون دلار میخواست. حالا این رو داشته باشید بزودی اومد ایران رقمش با سند منتشر میکنیم اگه بیشتر از 1.2 میلیون دلار بود کانال رو پاک میکنیم. فعلا دارن باهم مذاکره میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25179" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCG9v5fdWmLM0vY6qUfv-TRON_7EhKOnP1tmKnQE0scQP6-PPQ4RtDqTxmsxRtbh-MQP_7xfrp3iIBQsuIVBNWS5rPgqNvrnnHLrG87AxcBWq0zRA1pisBOoilbEZIKhhv_JsLZafV77j4tPx52CP2DdPj45l46EHCot0L2VA-c_-gXFAJygq3OilwL-FuX8nP_pdtSFRMqgXJ1kLlq89mCVT95_hULnh7zJP-Cff1ZxkGJSdYlvpxMF-ZQowwDfkONSr7wqyB1WCep1l140MGxiWp8iQeM9eoVgDVkS3akzkK5zCGFSBNG5Le1LElsXgjM5S-qFyiTGAjJGmJhvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25178" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25177">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNKgtdNihLT1mWdloNuBY9I3JTvudWyMSdDMsIyLhhcYUagBfYsu_ilZihVTvvSADPZ03BqpfLJkr6_LlJLw526yWE05E11-uDYyieeWqvgxE7nAw27ccNetAJMR4s6eEO1ZGVNlb7PQmgdFiK9uyD_9t2PI8EAAtlxLfL-HEhfNc8snCnmlAT93ffMo5PFRc9jQQAtn266jphqg1NJcVtk2SuH8OXYGJCMXGLSUOCHMtLbBoBVLeHVn0Ylst2oaptzyukrQXFrK-fhVpiLH73n1TxGO-AlWZLIV6BW6cSduArmDi_YvF2RmKqGSVNnV9tH_z5p-G5Vm2PBmUTP0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25177" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBSaCDvVU_dZ1bbQs9RPPwEQZ0vQM-TOLJH_R1hTjX2Fyeohjrfv2Cm0L1GVI6OBpGZ3CP9F021aeBDS49VT21RSWGg6zM1ky5Vs6SxNbDlWIeaLNTVST84XWaDaZPXnVgFLVqZxt4n-avolVwVhtfTgA36G-a88JBGNyCn2JBBNvgExuz8W7t390iLuklae5Dm8MfEWJ_BOM6saRqLPDRG4YrbSDUzMYjmfa4CHA1iJaJ-L2YAB4P0s8QY3LN3MLAGbwJIamgf_06Xx_NqGHZQuxztINeVkqmmp4A3-Gx2G_Jh2Uf6OrjA_hOGo44s21vrpKcarZ8BAW4cdv4ZNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu6nBctNXkuVfC7PRwhvv3V__Tmk51WTuWxPupeDBxAGrIRfgj0Rhn8ZUxSDu12sB4U9vdC4MkUrzzMjxtt1S8qJJ95aqsq8qisKlHMgTaQIp1m4UqhU9plt6Nu2MxVy3aSPLf2akV6ucatFW4jJS8Viudfxs29N-0jd0cwezse7r4RgxKBFLK3QSDwVX1xSRPo4grqSPLFtRrI-7uclioa8EF_JH7itOqFSShye_xQUDagqJZt1UpN5_imI_yfGTUbYY4bQ8HgMGw1t7usQZo6BRkxw5-2ns11C5r471nSbRyS-CWGQh0DH41tJEpfp4hXkcF1GG_0QXp0f3LZezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdSogmpwQvoPWoF__nmzXljdB4AmDKV4QQg7w6Ij0Q2gv5ErTFhsbKyAsyCaACuHUw7iPQxOr-AvFI71_-elpqNDyUk_0gAUz281-VzMYm4INcSHllTXufA1jHrNvlTKmP-EJmp38wpWc3jn-N5Rj5Q_YAk7F6DmGm-VJZF9D_WBshHv0_wTs_MPt8t6CWfP2IzGAV9LqAhCzguQOlhAUkXwL3zMbQn6oZam2wT7Na2np8s9wycNIL1J-vKcQ4H5FnazwLbVWRMU5W3GKWjGPHysQdI-xseMk9qDakxqoPHcCgK36JwlfR9-LCsyTGq71Iw7AZXgUpFIvqAxwmtUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXoACGSJ4KA2dHO3RvYT-LdbKJiPfZbvAgBpir1Fa1ObuTtVRtMorRwJh1Gdgfr-jRQfm0jsOivDSI_aKGvTqGlvX0dvJ5hIqZ09c79BxA1VHZ4G6OapT9dutu3l1R_Nel1uK1DsVxPhj5c9DCguCKQiZgqi-3Eqb1pEh9-nQsXKAl1ABcYeB_nX8jdQEMkGWRrSssTGBij4-3lSfxYCOjGMIPZry0cITmk2fbqGtftKA_wIAsgWfI4a6EjBIIYpV12ih-crZF-krSaeuMpn46ulhnjw7vpNqJ8mgpxSYv2r8hf6wgJE5yQngYzMbSFFBibIPY2iSsWwUyKmrWOlfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl5Bc0tUmuT-_bLjOpNx7rscgVe-ubT1-pEwVMIdfk5KAMz34fmXJVk5OdX1y3eXK_MsVJVkxjWM-npvD3kahWkIt6w7HUx2PfO6GHJ32Aq2d3daiS2znH-LNgzY347QO1hmhw1zw0PdEFU1IVWltOZ0W700jKf5U6QO0U1hLR8m2U5g_AL4uPAp9nC0UH2jcaM2LFvgXPfmDKa11hYk_3pJN3iUsl5w9cGSYabKoOJRVB1mvDfTfKvPtijnwzBMsCtm2LL4ajzAhitoXg8xZ37k3UPETlesrkYgCvfx3FJ_6RwdaWgIOskzhoXDfC7bWW_9iM-JHyQUr8mqZeYPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No11dj0ObpeD9FHa7t9YXDcgWfoOpKQclTqCWgwyiLETra84i2EtAN3uXehU9PjyLcXQlb9ilBJJNPu9NsTNUiPvghbrGpKK5PN_n6T-b0PHy5GydX1Tp2VJqmYUfIlVVBTBnNTn9-xVI8nQp8f-m5Mht4-LSK-XM4J2-smH23sPiLgPGqdXXkpEmrq9sgeKFBuQ0UMtRFgykjQt4wv0V4StOOfKJui8lI4r6A4fgMKMkNRUDDGLBlF12zabPyEpfli8zh9Az5vzteVjUWb3LFosMwDLwuPEmcOzNVKGK6my2TrK6DiMijRIUEFIkarcrb3qUyqnqV0ie1gFbIaFLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0uMJDpNcrN5UrvSH0vtkH56DQgz8woy06T0b0S6aR4tyMJV6SX2p_lfSGKTt3KHK9rw4PA9DiS7XXb3ucQDP5ss7I6HiECuz0Rar-S0dkdMU-vezyUei29eCh-V6pcb1hFfPtnpveJ4trm952Cs0ABwPVgBdTXLGbb4xb09cQzVDi9_kv6XpFVjJyBufkGBzgh13g0qxRw8-_52ToVx6_G3lt1DtVPefRSa02hN6kubA2aAoLsyYeotfZB45oUP24xznDYwDrFZ39rYiqFotDnEUWSGZI1hxtl8P5UaIkF5VHt4eCdgBgR-QiSX9mRunddpU_EYRBuAD0-hz17WMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZGZ64jq6wTdRMfItnMveCJO0vhXo-n1FqBteDytEKd9R0cRJL_0V90h3sqNv1CWdHl6c6vOQ48sghVe7_2tuITDvkmoMMjxMIvctHLqhwwFSIVCntQVBXfso3cQSKRQumF7f-iZ6jyDAzb8rsh3qOtuI4SytIx3MG7ggLI3H42UZ_JgODgbUyxYFueC8rJ_yariBWMv1N6-xxrAIGvyYzRIZNRaR3ds1dGmft9HLCCMdUkCvMjAI_Us1rekNuXs-u7VFUqsuwE-uNXTwY4ToyWt4uD4vUlCZVtu7NVJCfHXqPiyTqFHnBrtmPMJvb2O9sNg2_4L-4vYKrb9dCQP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJhJHZNUzP28UG4ITsPsycSPtjDvuNrvfbF8dYs2G6gJGaZV0tPidY5sV0WVpwfcDLB6DwWuyxTRJI3BwjYUTN3hzKDeMsfSPnSblLnLCOz2mX4WD_iBPG19gaockWUr7p-LqQyRRFKNf2UcYlyK9AQBhpLY6YJNxNKMRdRabn2MlqojbjaOND_7wGzfZtC4ET-Ra0FGNB9dlxDvfaIG6enEkTzZFsSiDUddEK48UhjND2KdiRDuWo4ifcw9vjgLAvdKTz_9VX8fzBtO4SIK266zwe_yS-gFd6b1HO2wdzTFQ4YSO6_nAq0F7sjcvSmjaXZv4cAmWfaWlI_2Ua8-5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Go77RYcIgWCvVZQ_TS4jOvg-3dAn1p5AZScdfeHMenKVPRIKGaYGTeaHUWygGvb4LrK_4fxwzfrHAlBox-vaj04jkF_tRZgV4I8iGygtD7amBn16snv5Nc-C9bInY2VBM4MkLL1onKtx0ZZBQFxnbGF9iDFifzK24a-8r4mE0y4KT96gDOqXjBBTBa6k9CGKzi45a7UmoWrS3JdpNU_h8iba5j2T8V0Jw5KJHsA60Z8ys8_IaJV4BTomJOEr7J9LqBYIwR_aX5XNLafFfBXLFJDCmaU-5lJseFgN7DxdhUWvIZbqSxxaPRq4euXp2F1ySjgpebtwxMtmnTeD3PDqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oC1NpzQ9xcOd3oqyqkVrk0nS6oxIxq1ujzusRj85PxSy3WR4Oi1FFrVsm34jLbYEOvtcNgT68aTwM6yQRle_8wId6Gs0uopMQJhK_R9PqKsoxjjtYf_YovZe79CVZrevQLIL5uphGlguKgoAIfP3fG6v3EF85sufAmjrN_BKevmL_oxQj5_YcU_bIFOqwCInIXp98fsEbnnYWh2xjggWqtArchZBoHBkqPpqxMVLbunrtEe7gbmKv6PpQeFO3ZZ9GCvAdycHHFyxoBbE3AZnHQv72DRBg_XDIJt9gOret04fEjv-Sc7s5NpPUKl6z6OGKnhiDvejbzN1D_FKIL_mrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpD9HmXF-dMdaKRIbx6Vp5uPGXtBbA1l_OY9W8eB6GBpCtVIRJQzDQZVPHaxVnEprR2WyrmauWikGZi4mu8Liy88fkS_N-BwotyRAqTS1YtjDRZBdzQMS30F-1n9-IVnGwhxyE1SI3QFH7QGVWt2OJ2p09wup--qX1I-9bVto_xyV_f_dJpJR7ShtFhDUkhjdPpxCbaxFC4SjB4P4ULchus2aR-McBLczipFyGn-5NcvgArHv27V_JsIULhwU2Adra2w2tcAe5XbA9mE6_AX7EVjQeA043UMNMWJd9ixK7Twq2D63BjvECs_BQ1sU2mwR9WUm72kBR3_zWbcHr9o_80g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpD9HmXF-dMdaKRIbx6Vp5uPGXtBbA1l_OY9W8eB6GBpCtVIRJQzDQZVPHaxVnEprR2WyrmauWikGZi4mu8Liy88fkS_N-BwotyRAqTS1YtjDRZBdzQMS30F-1n9-IVnGwhxyE1SI3QFH7QGVWt2OJ2p09wup--qX1I-9bVto_xyV_f_dJpJR7ShtFhDUkhjdPpxCbaxFC4SjB4P4ULchus2aR-McBLczipFyGn-5NcvgArHv27V_JsIULhwU2Adra2w2tcAe5XbA9mE6_AX7EVjQeA043UMNMWJd9ixK7Twq2D63BjvECs_BQ1sU2mwR9WUm72kBR3_zWbcHr9o_80g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8U2Y-KrSENCC55PdfTo8RyIvgNWDzUgjuxsn-j0wNr49BWVdDgU_hxjh4GVo1vF8oOrZ5qNWyhY_QamwyYQNsPbgOc1rkyYitGQCFwlLKku3x1pwFrSLys5YMRH--J5dnO7antUxCyZo01IciltjQNzV8gwKO_epjlNCNB51zn54AbSs4ebTw39Ani6ExzrgquWdJWZey13m9yJ-1Cj1PAkXkcI8735NWScXZa70YvQUI92Z9mhO8FunlMdjOcsRTmnH0dHi14mqHIiJ5nVB7A4wqUdvoAV_LerJSM1ef4-CxcQwkJBmPJHQZ6nAAw-IvUgCViuaGp9leo-2_Nl7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMrZjTbWYlecChUfBL_P32bwT3jIzOudImtmVL_EfpU_vY_v14fkXL0VTEPBXZcVgDts1rLAlh8y2pvNzmE0tPrpn-tjNl6n7EcLvsLBZp3k5R8Lg705Yz1fvQ47VD5z0WCKhfmz6ISVU1ulWTwQNPgqUcVx18JkJ5yyeReFpJINx-RPXndWT8UCG2iImIADPvR9kCL9cRv_s05pFqB13TUvxKCs9k3iOlazPmLxNG0R0KDlk1eoWVn_R0fC9E36uHsICzxrpYbKTof51Uz9sE5_zL_IHIHLksdaE8hKvDGd6rAgSC2xrUWAqDC1m3YFm0fp3f75twNR0_hXYI9K5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NryNUUr9_MMi2AlV-GQPXhwE0mhmMS8abYcr9wkuq85fjXTdFpqVayGmHUBB55XgnIMNUiQP3BTWk3vlvfkVJ-Y3Jcy2c9iGibRBcC04BiuSKkNNNVufaVRxdLsaRekk-za7yC685rvwG_2FL6KvF58e5PLPYS84v-II7GAiS-dqxrKP3g6Uxgpgq_hNzAMyXfpYK9LCJbWfnbKCvTNNjhj8B0v8zfaNQM51C2m_YW-lXiX0rtElfkFDqr_aFChL0yvTk2uuJYqDZJZmMsXPLpmzSIWVxoLyOfqYv61UjeriKvofPcK6Edxt6RYQAdMiDpDsrF6gYxsqej2tdGUYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=fhAgnM3y0M3hHLOb_Izy3lPVqpD2TzVHgwAZeStRWzCd_wF8ZzjOBWzQG8vGjK2LUq-JYLaWmj-gRKBYOGP_nAQbLbYCmgg3hhxboFNpzVyLf3GN9X6A8Z-RBGsAqFJaksEQGaGE02dNIjsXeO-_1ch1tUBsXiuz7J4j6Sy0XUp4tgBZoBhGitavpBDfqMoEunbT6XGjtw4nqoWyjdrFi6B1foSEVRCMhkVehYu4O7GTXXHFok0CU3I9Shlu7tVkwWKlUIY_YBz6mnIGAYNDZDR23u2R-71LVjLQBZA51tFyA1Vg8EPkPSBXaKR5QDZAE9XtQJj4FIz6L_c2Wr15OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=fhAgnM3y0M3hHLOb_Izy3lPVqpD2TzVHgwAZeStRWzCd_wF8ZzjOBWzQG8vGjK2LUq-JYLaWmj-gRKBYOGP_nAQbLbYCmgg3hhxboFNpzVyLf3GN9X6A8Z-RBGsAqFJaksEQGaGE02dNIjsXeO-_1ch1tUBsXiuz7J4j6Sy0XUp4tgBZoBhGitavpBDfqMoEunbT6XGjtw4nqoWyjdrFi6B1foSEVRCMhkVehYu4O7GTXXHFok0CU3I9Shlu7tVkwWKlUIY_YBz6mnIGAYNDZDR23u2R-71LVjLQBZA51tFyA1Vg8EPkPSBXaKR5QDZAE9XtQJj4FIz6L_c2Wr15OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=Udqk3DEpSvNzF8QSRAqV1iHHulut4DyZH5Eir_w6yANwedugJtKPqPvy3aEvux2LaT0aiqVKKU72AE0XMHWtT_6pMnxj8Dkr3dg1eViB8AxleZIxMYp3IQhUI6y-vpAQsE-Snd49XXgSx0iQDlxD2p3_e3YWM8v5nV6tadUkcJIvjlJpTf_ZiehZNlMXPo18Zp3ejoPv2l2EfKmZ8S_EI2rbxpAfX_Qru4wyhUca56CBqhg6c2HkrR7PkQ3bYoNqo8xcFJ-HB0c78ALP7D-mF60fiajqNQpxK6xiSkv1XNvwpVggSFOeCBCotuBYV3sck0cZKD0frCqEz1t2SSe1LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=Udqk3DEpSvNzF8QSRAqV1iHHulut4DyZH5Eir_w6yANwedugJtKPqPvy3aEvux2LaT0aiqVKKU72AE0XMHWtT_6pMnxj8Dkr3dg1eViB8AxleZIxMYp3IQhUI6y-vpAQsE-Snd49XXgSx0iQDlxD2p3_e3YWM8v5nV6tadUkcJIvjlJpTf_ZiehZNlMXPo18Zp3ejoPv2l2EfKmZ8S_EI2rbxpAfX_Qru4wyhUca56CBqhg6c2HkrR7PkQ3bYoNqo8xcFJ-HB0c78ALP7D-mF60fiajqNQpxK6xiSkv1XNvwpVggSFOeCBCotuBYV3sck0cZKD0frCqEz1t2SSe1LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9Z-MQz_kkjG0xLB0HIwN012a_aUhimGkt0LhHlsQM_1eNTgdi3wwjnff13Jcvue1qP3XM-tjQI_5hGyDU16xE3_u_Dn03LGpuxFoSXjnEBlIxUJs5HKN0Nrjg9Hru7Kt0b1ArqyR_V1l6K6WBhTPwn9v7zAwRyAJ7oDgddhfOyEeYEyIt_c_1T-OJDtxMxSEkp3f1Ndw8uZuHbLTisu5iXJCmOywN6wFFk6C_m0jloCgT4trqs_s8uxepGN5BL0xTmzjmuxGrx6Dou9Oowwqm8kRaJmyZWnodEiSPcElzt4-jBeie3G3PCQzE6HvysaizOZu7CYC5T-MTUDb8_fvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ut7xbT9-EqG55dezm13cpDN_rVzW30HAH34R3wuHkgHqzJClJwx1ob9ssLZPhwjtBjS-Q--2mlP6dzVr75zH944HOOh0erGdXEWncXOS_MhwWI1mONuSZSsAaPOj2Gfk2W1KrhHhbjezduIV1QgBnlUpY8W6i36eNdEBF6j83Xn2_W95-F0Ywq6fri_JGPAleulq1ymVnjzdadS9hH4oZFzKLWAncZzwPR3n115uaq5QaNd34wS0f0nuxV_A177mBsTwTywebAYBech2O11N76-vuXS-Q_ZRRZ6-UBf1kS9BYy0gJuOJjR5vMEompCy3ArMthjGO6HJN6evEPm7hYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohu0SQSJWc1zZa5fWxJprK07zcM4nM9iGDg58uDsVv8t6XZFGD67OOAM_xKTYChuNexNqHfUOFhoSxSzEN3oBcptkMAa0CCv3Z9BuiejU2ETvVTyQgP5YghoziLgZqkk7_7uFMe7L8mLUcM7hpJI1Vo3CI_ND5lZP4lUg7L8F0dh6cKcHZX-NGpS2YPg7Y5Qv66jnWUo7PHiqaUMHWHD-O7OL3sH7wkonuY1scj_VPilNkL5Nfa-Aqi33mcbUs_nB_vgxNHDyNhWIUpuMmGg5AEsgVNivCibdn3u8VWrZLxjhXo7Ou5nGScL2yXBfCxudfqAMjNZS-wRlCmiaLQ7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZh_nmN2laAnubj3bGK-O724ZbtgLw6MF-dnsshuFT_ijSZrpBMoUhT-snBAUcTDVqZU7pv5ZDijE7ZTd8ukIHB-KUQzegE6xKQ7pVZjJSUhqxw7hXZFbV6eX_wVF7YutTDpJZONTAsNfVlh9LXQdPhNEJsNgJCO7SJPe5w-MJ_vgJYyLp7g-T2V6ipCedbuxhoEEZwEqbbfImNvS750OVzHMyMztbXmefdPAsJ0pWLIldSZdyxRAx0fIF8U4pII0A0EMdqSd-a5nG0xuDVuwl1tpzETRY1u_o80-r2KWoqkNoxozlBVh3s3DvZIK7s-7NMVIIlJBNprM-7rLryB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmDfaMEZ7A2F8teiGOLKEsAyOVHgPt-COt3thKrBecWoJz4JlQiq6JhLMHoXxWyX4_n1H6ujwkzN32ks4AkJPQ86zdbkRGq4CKcVnkxTTz2Oq_HNFv1QQKVrJLiU4e-V2LsieRcWeirdwjsb8Yf2KM5bjKClt5dct-4M0KEDFEJ9Dgt4A0wEId5m_PgNQ6Av1AQxJKemWGmngwWAWJL3WU0w34WZQ1eghfrO73nyd6eKeuJ4sHcwDMnnDM4ucLU3nWoBjwvYNE8ls25g4D56SuvX411v5XxiPioIy40dIr5AU3xeAVClAL6BWXx8amJzPJhN7XTX99CwSBZZbc0-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU3nsKEM5hGatPJFodxEZFAemyKd3wUTq377zl83xSzlaku6ZyI4vdqSpPv7dv8lJjqJK1C_JWvIi4cn_azicy7TeekxAWdHpLY46skdlkLyjbe14bouC2wXW5CiFtaHhQ93J5CbBp51vpbZ8nTfiCi9t2HHjaHFgami8p02356tI5mcG7Rx48BznEX73F1RY_YCPWWViB_p9mHEvDCuQS1AdQ0qyX-OBAJtjb9QPCLlxILwoEVaa2cjXDk_azjMX5_ZJYlqQn1phb0YvbfSs3fDswjsKpsBwZ6xNcpcaHgrXVdDfEpyQjaMhTDXe6xc846cX6Fa98OsXBVNmsQ9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuaP9TazHbkGyYPazknyaVZpLei4ohKzeGJByGaeOzcjVHeo8C72Sufif8SxKbeqSPc-enX_MwzdpX-V1QuOXOQKJeTt0Ufhepw836mR9ubzuSg1bhFtncsZbuIvWSjpeGc0-tgo25jgt7FOTsDsgGUtWQ9raO1Q_Qea4ub1qAIrJXgaO7jriSA5LM3lU1N4MvDSWhJ9w0mbHs23D8idKytQlSB81wlHMmhdwlQqbIBWTwX-CGKgmHduwFPVEq2HGl-1XW0l-kIQnCjTO_YSguB5o2ajV3vCNcQdIytvI6p-gJrF3isLteAX3jTs4NHXvwS2DSa4VN7shb82-XA0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25152" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgZksXilsBxUFdTghLvrodwoWJvfzuctHCf0uELF1Nn-7J_seYi1LPqr4tN-VzRr9y1pqcN-QHVIbvgGKf4SJr74A7e2TW-0JvV_xMyBcLHWQfsfRHPrwb8dUzaR6ZrEClnB8Q7aSYO53Rtt6aHCj0mE9QBfHmFJRJ3cfrmEPF_WsbUBuCQKlIKXvqyHmsu6phYRER5x0z6h1DmBpP-7FjBgp_btTwAIL9URZX9gzyoxAN-OErzxIy8YxZsb7LQhz2VrC08tb72bKBviDBb2FywtMyFo25Vx-zb9YNU-6UHx_mh8r-Ryq-TOKGXRfWJaFfEqTJxeMpScu8Ew4QNL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7q4AGBEuLO2tkryXzd4o-siak3ZuSh4JnoY87ep2krGdcGkjyD1PdTer2oNyh-XG6ZQ2_yGuMekqYxnUqInderFQkgTt7vZWIwTpws5gFpN8tr4wbwFbzruZCbb85q-CHANKUAMPdinN3XdVC3xu9NwWGgRSkjgp2clQeNKjI5Poha4PQREsJUFOhMHGYQObAoyphdZGAg4pEB1Pchys2Qf8LuXQsmmsWLTBAwrrn015JWcUt5Zo_4mGkh3PQ_f5eIjXA4FF1k2I_BNije3uOwvFrrMCxzpXIijUNEYjz-vg-wTLSWFBmW7FKHOMO9dg9FH2pkyrywhO15she1ycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG8pYoWrs_ElZ5Lsyah8B1MCzo2xO_O5cT-aVakeZXR7oVWf3BwG3TXdC5aBCk9WaKr0x7EnK9UPfyWKJwq2e0KRobLF8GliY7mhH5XJh1GK1aF2yEj7PCvoQGBBCmH1HRKuh-fkriYowE2l7qNWqgr9EH_wpasEy9Xyy-WrYhWIo9hZhiZkIi2aj7Ue6qzkrI_5-OPsfzSvXtHHCQvVs-jR05lZ2wkiCeaQoCNzElJ13HupfxQF6Ea_khGUXn41gRzMP2QUbU_DlGTJvmtUNmPdCi2LEVcV4iZYL3xFNbbZEGnleIZ6Jg21B_yTMI3cnCEbOzyHYfqSbk_ZX0bjqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhTj32iDDhfjlR9gJ0F1WChKyRgMclMDfeunJZREkl7QcikoDfBuNyOGw-EVtV5NID53ClohWDygfnOTAURUYDAXRDAfr94O2Y8YLmRUNIDTA6q4K2sKOTrar8Lnmlg0QL4S2Hk5x6NnRMyec7kSgiKiGs1DQvX1IpNDMyV7yRn4lSEYMShic1Gk7_J62qGIGZBx_X5BPM-nzHA784-jn1coOo9ToW6638CQ5mgj4n5VuJxMgb0DEeTFwbFLArEIfREyEkZo_M8ANMZE2lmfBsrjIP4kzi1YfxcqVv39m-0Q7xClkM5lDz6d0U2cou72H0Jt3-kx6YwZtJBkUQJfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY144qEmrl30xTJq5XrM_RYM3jqGEZAdElfVIyv0GXMA82qZ1zqjrFwoT99-a8u2Y_BqIlC0nlVnEZF_bWYmn57P4vfSF9ogb0b_P3pzzhZUMbzmLXQWZRyyxgbx9EfFOQKKAnPeHuDQw29Jcw9irGknLMVVJptMYAJxM1FxjXM1O59RyD7E4RwMJFN8EHqP1YoSIiCmLqGxZ6MIIEcb9A0v-DJzWUj_0J2We4oM1X6tw4_1wVCdcxahWa12kQIk0WsAJ77MMfuhXbPqKpdaHsdPHW_R_gu3jqXMMeaDD4Pb2-nRB46D_CaLqnVlQK4VGD3cLrqzjo8W06tNsob3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZF5Xt-RFWlzZ3gTxpM7ylIE3eoXYew9fUbTlIGdvScMspjQz94V1c2CMkwjsvajvtbc4YwbjYzN-rXKHd3b9AtK2II70IFVjLvM3guUcO3IQLH_VKWzUfV1H16y1Blp9CqCrxyFb-pUDtWZyyGLlhtfuCyDlgY9yjJYObkNmn3sidCOlm8rSqMI-gTyCB6gefWhqoZpvHoOmciN7m9pCfHVUrWdr_x-J4__XzUPOUR2MO1XP-zutIa8gLjj5JBGKYotn6HZBa6iZYIxHV-XRBvoHjwUjR-_eo_lm-B3BQrlUJytDoGlND6nFn_6c6IZya7KbYtrHjVSgM7Fz8ryUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1gCn1kctr2bsau16GZ9DQwPo_tB4fJWT2PnB40BZzd_8B46-j_p0BoxAZGhULNx5YjQZHwWCW0AFvxtdZ3nRQDz8sJLkHFgcJy_71KV7iHOZpQqQTxU37SrRO-Nwmi3axy_-R_XhufBS4a4-mCI63zBEGaVQiDKUarWVrlprOJO9fzKs8fkQPVJRQuX6BWKdPTjAzBWlCisfQZW80CdfLVglk2g0tw3uNlxb8VeXi-Pm1sIvP6etmik2kxvvQqTmL3uLJHPrBkKOciU4abYkT0bBVM0znXBipOw-3d3Geg93pL_usbh0jy7OeCo4MVmYEeaGvzHVmOOiZMI_G0IXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cImh8t_lHvrLUM9eZ6ofg9jbKCacP1-wsx60u9T2mOXh5GZvi7FR_omKAtQhz_ahuWPhyk6F7-AOfWGR6Z6AEdVOfgFB0rlubzMN6IZl0_WtrutyDwTfnvaHKZyZebV2Ep9RWIwvLAL0d2dxv7Qpk2U4iHyTeX75WXKtuDI4hctlPXm0GDQ5O8AOo4T2uuImCHy8zebKkpOUN35ChjyOKTcpUOmxCv5BYGMIxjOKkz7PB1ZCVeTf73UzEg8MpdCv6dglgBcKwSo7TguNAcYySdt0u_P2yF-IA_IxoWlNtuUHwbwAsFO3R5sVEnUEXR_2UeF0_XPWBxYQ0Jmbh-hmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQqfVfIrUxTJujw3B2Kb9WVKriBhlKtIQfR_wOjd6CzTKwtKCo1EQ7vREsu2OXhbpJkJ0_MMCuoFaHzBo1naxKVW3VIiwRyneJLsRkDalxythFTy_abhjo2LmO0iWrWg-f1zN6QwjIxYjBP0unBZCinV9eH3_Vs9ZD-MrmHROz-UItqKcyW8M1s080eqJyQmX8auVCRg7c3-nDmwzTmL-aMvm0ougCbY28L68tJXR6rvkxMIJRrgG3UgOZZDG5N0UFBf8bLFeAydDpKCv8wxprh7lpWX_ZBNC6ERaJ1Biw45MR3K-IlD2X-a9KmH3zwUXo3ORhZRxofFmEvdcplhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C94LTbCevpz-posREnUKWYVec0v6XAFOwlV8VcM9hF2VdCi8EvKxpt3RSPsX2sdqPHeNi8SnVN1QWJ31_V_ZTZ7EP_yTt4RJfyEwrdHvmH45_2AVrvjEyXQqxyh-DHZT1AOMi-jrw7YAxi3WxcuACL-VhuWDyjknjDFeXE3FWL8LughbanP1ZdsQypS20wyOHuGGh3ftNVKs6ZY2qPy4eadwxLUIjFfZRtjtnFzHsoCo6GdFM0hVdoAUz2-K81vh1ptJIY0KuZYUlI7qfqR1baz9Ph_1oCT_pTPMVXqpXStuSbe95QlPIlP4o1kEGX9J4Qso0Sn2rlMg7DlXgfFYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmaPdaOdoXbOEfKDrp3sNZUFFssIhh3TRWGCkfqkJNNWrX5Aeun0iZolRcjq-hhMeBKyKyHABq6LQISNmFJiZ3h0V1AUUNE9HtBmvXaZvRVDgXEgenjCEnX_u4ERZwG0STSJE60qnDpGqLtle0h6MO6gR8vBtXnhIx5l1sb2y_7JV9EcqNP7VMRZH1Fl11hZiLd3J8S1t0DO3YsIMW7ZPj_YbazEJH8Whpox8foYXu4eONQQ-Bfqxmwyfs0jrFGkJkYB32vfqiCpcqa30s1qfcb23TBP0AykfvlNFrtwdgQ8SZ_i3DLezwVyHVWfEzbCIse2dC8LyfnVOYO15J8bYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUYFdwN8TdTmTtQUKDjOumrpoKK92fSu9RpQzGu0tIzSpqhDcA3q219EjcppRGTTZJdgHbQfqCqn8V2wlRCtgTxdv9nNbIX_Yh_8FqVrM6SbzznMbo3HsMPsTFhxeLHJFVxhWibUMuYlbugeufFEVAKwFdyF7Ed6wKqXE67LqlYvy_JcfpEr7P6UtsVFdDJiVtBRmqnTaED6CvQIt0ibqHv5zslz9Pt9_fOKU6Q8p6AAfhN8yaJE_wu4NxHGZw7Owu_shhf6bO3_lzbTE3SRUKSyPXgRZoV7L6RRiH1ggOZRQ1a488Z1SvrG_8DaBN_2HRFJuUOfKnUOcsPLbmpFTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5t2CntkFtmqN5KXWEFAQMHfchcANwAKSbndCzq2rR8IwPMyFRXCMTclui-D_f4SW_IXaTxRZY4y9bqOlM2NIS--4G8s3X22Uju40LjFdbtj6LFnSOBcHFEVGIX2NsjXVpZA558yDzi26nt6dkEjoiJ0FxoFjEQ_ja1oO1EQxzTDmkW08LQbjUNHpqI9T9k2bXIw-NUU9hePl-uzD0uA35kePnf7him2blNDfkQ_6uNOOspkKTCIss9B-DwTAqfEHE4iPcPEI4D3YbWhQ97oi7qCBknIsazzqDz3AsxalZtkeefMNqeMPbntdamQ4ktsDeyXY2oiselNLEToeo87Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHmBcSd9BD7Ez3EeseBJjNE95MNjo4PVcvBqcVuZeMKNtBPSV5KYuUDvtRtBM1qlclZI-nDN2uTEj2xVArY_SfIWjRRNWPjjG3U8LlWtSDWyfkKSsESNFXkiDrTncCRb_fNhwSFOWM2v4x9yjFFfv-Vv5kAwHwISPNM_YBNZACZqVA3-P9vTQKAeh6_2O1ACVTcY2kW3GW01wMi9XuMhj6HbyaoJJK8Tg0TZZw6JU_odwbzi7SBsFm8nYPOiC-ym7GZWGirSIf9JRRvEwtAseA7zFR0AU53IS6bmFU5zuJMztxpdPWe7nDjY-xOFGBPZUXBkUNiPLKtfWzAHvRBjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=pgLL5UDpbfX27tpq-ddFtceMOWofuY1ticgMwTvgFhr7GegCQBQl68pXJaaupKKoAwdKR5oBG-8gy9fyJX2DEoGdhO_mmDaRB0UC0HZbFdQu0bEIUuoDz-ex_4d6Ys1e9Gy846my1FLsBUpxCmM6AldbVYwUlK7DBPejeGvaHRfZQ6ONcn_eby17kpjb5O85l0Fl_1HFr6isuGg8u-DJtJuLbjyUwLtwl1VGW1sd4vsQMWNB3p3gk_MTL64ulTv_XNRUNXdrnNaSYfjwZ7gcEKR9t895_g0FlPid94QaIF1vOT1lV8qyONf49YSmcl3bnrwDstxX81QkbA53CXmK0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=pgLL5UDpbfX27tpq-ddFtceMOWofuY1ticgMwTvgFhr7GegCQBQl68pXJaaupKKoAwdKR5oBG-8gy9fyJX2DEoGdhO_mmDaRB0UC0HZbFdQu0bEIUuoDz-ex_4d6Ys1e9Gy846my1FLsBUpxCmM6AldbVYwUlK7DBPejeGvaHRfZQ6ONcn_eby17kpjb5O85l0Fl_1HFr6isuGg8u-DJtJuLbjyUwLtwl1VGW1sd4vsQMWNB3p3gk_MTL64ulTv_XNRUNXdrnNaSYfjwZ7gcEKR9t895_g0FlPid94QaIF1vOT1lV8qyONf49YSmcl3bnrwDstxX81QkbA53CXmK0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOqJVZPRrsB57FogcqNPNCJ42y--mhaWInphwB_SFEPnmaP6LszdNxAvFbGmv9SVA68MbpLi9ZMbYPxBuE7AXW5Dx0Uq77BZ-OvHoMRUchl0y0dS8jYGDdqcV1wBZi5KfhCqRaLqeHgImio6aaWWE3EpUWp3g7esLaZLgOr4Zl5pL4zMsayjbnMhCyCpA0629A7P6r3VOPfeHQLNHos1S1tnGwzWoF6jV9AAVYLMaMySDEwedilpv7fAye5guoDP9Sv4S-IGrUqbxTeac_LP4VpPP-1D4719Sr4sZwQCgWjS_df7lZg8PDlVwWPbbpJO6vZPzEqdbYKc5ZlTwbsW5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvMn5kRa84Bwc9NsKvFSEpEVwo0kHQMI1QA90XWCEOqjnCxdxjiqYFEWJSyImBZ52kywnJkaQHp2tgPQ9sru3NiSqUJP2Odzz-HcbpeisVi3StYi4RW0qpneSjxza8kT3rA2KsNFq6lQ72kKB-CgE6KnfgKEV4i0alxh30Kl2f5MaNwz68SJBsTZZLnrZoOgAcmlnzV66LvuCJB6bFr_K303iYll5ytanm3zCDMCqpbYt5EFBGPRNROgeSw9Q_ZwFjZCOMu7V03Dluz931B2A7967GEZFJjtqvCThuatFx9F6VCQwE2HaCT2i8yh_Nd6HdyKQKLTDnRGDlxj5-lKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJMCvkzt-bsP_cypJV-xOJ2x3To1gGoj9CikoO_cZw8ioFVONsSYCemKIVLNGiCtvxb6xVm6KyA1HmX-0Uf8A0gk1O7DurDN62GTNzhaF57uF7lXv4jwdofrFLbEMkl6pHlg471t4mNZas1mLfS9rhJ57Sen3YlOhHdAeFjAGjtKGrBF-DHy4iSFSO9YMXKmDiR55eBHHa9Esgqy2SR5T9JNE9LLjparDpoISuLIN9EF54i6_2ifUFTQCMyuMRG21EIo-Ge1JLL6hOCHLq0jiXMuX_IYqWOHUh6wf_7fMZfJ25HJgVYKki3MM3psYHTaiJISbp59eqCs_0Evw0Kr0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25133" target="_blank">📅 12:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9FQ2NFbcTk0-qOa8tjbGSrFzEoypEZX2VuXAe16R-D7JDbuLRL-M2nxJ2EtC6BMt9yka8d7LECvjfavZCbdqO0e1BOoZ-iLgAT7O4-SxW3NuY_rXv9QRF6CkLIYJF27w7-04eyYbHqtByXNOOmBY3GwDYCKSxKxSLQp4zMoHu4fO9bTTCG1BWuQcjxmC_Bi_v7mGw4ANFZSPL-sCeY8Fh1mctJSgxBo3_xv4R5xnFpQUSaSYrs2laJfACW9y-05f-2tEkL_v2yTCynEvkVl-bbggzwJn7D2DNlw41LYA8ooVw3nNJDI7_ACn3S3ajnGhgXk0AhNM5BmCBBaLPsRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیر الحدادی ستاره آبی‌ها: آماده بازگشت به میادینم. بزودی در تمرینات استقلال شرکت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25132" target="_blank">📅 12:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcXixGDUppCKh8a3231VYK43FRC2bDyHiWIF8CBPaDddnoe8dwpSn-_KVOb58pjFwrehvITbtz6x3tjS1U9F9StJ9CgqxkbmTWaWWWgkP3o__U7q3_GiYCWghAIoftD8dRshPkkED-RwU9Y1V6AJWzzEGqzhfhUE19OBFpPXD9qvArWdEzPgm74zd2n7QmNQ9M05QPHDS_h2Fl8yDFHI1g4IeenKF98VYAc9DbXTU3rFq_IvV-iqFllxer-y1U4-8oA66R4NcWxNxt-HFLmiZxguhQf_4r9hHf16I-_T86RNslEFhuUCStaqB8nJ12viafl6nGmvJe7cHhDXfU7GPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
مقایسه تعداد جام‌ های گرفته شده تیم ملی پرتغال قبل‌وبعداز حضور کریس رونالدو در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25131" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rk8vFmvqkub4ae_yNjS2PDJeyHlVou4pzJHw0bYvmeNHEuzIe_2KRipdWGqX0ezzkME6jAkNP5Ts6NAX07o5Wv7C3lseD5F55YnVBkURTIrx4MSul4gvjNfOB4CFDg3eMFhG6UX0R1sqeOXIey7gxHp1F5I-FXuDyBWY8TKX2oBVqrjuC6ByLTkqCAMrlztHDDS-lvJPBoTQkXrTmKdxoM84f3P0YWNdbevlNMMdqeS4XtjWwGgcc_s15OZawWwfxPygFelSKcBLcG68oXY-a2LpIK0WbRncd4iq1a6gA8CcZqV8rIXB6RT4OdsdyaAcr0cDyYY18IlwdE96rlLD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25130" target="_blank">📅 11:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6oFLVpmKDHSFAbDKbj36b6GmKhHc7Baet5-CzGTNVlzc7wXdF_o1JWgPqzttF2-nnRfuG2VvvmMYYxjCDTQnj8E8CD_zygDyK07bkcRfDAA2ED5AVZC5ceMpMMoXRRZMVvg9z2qke1yQvsNU_4mdKox4Bwuj3BdGOhzxVb_JLwQOGQRFE0aYSCpyoEP3sjIdK3D9cWcl_HtUsmbSkIjjQdhrQ4F-vS6lDWASw2WiFddkCLctcqcIz0DMU2veT4tOlvR05LDMeqgWiEWeL2S0n2dU-evp8G0NrsRIwvyq67RZoOVJIpwQ16GT6T4kqCqYnbKqmtjLAMpV6QhHYXAqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsp1d9aANIyag6NMec1ofhLS50CXGfcPgJn8XpBatFfWC-_6QgbfpGFfKZN4M72tNl3aUlwBM8csIcNJftc1wOZOlAPMauicEU-Tl7agiBLCbNeXlO0DsFz_a8-pNaZXfu5XgtyiTGpGXtkDUxZFDgJMJKfWGvIzPi1DzLcZ7gNqW_oNkexaZGDaeZG5paSHVbNNYuF1EcfqtGr8JMdsRoZljY8EQRuIVcWLOhTZlyXLiLCaDcutHYOgLpFMcIwnOfG4DAkfJD1w__SAWax1z974XVfd7yD503uHaBYnsF4HX4DhJFvOL7TOCBxbIXtk0NMHQaRLPgCb6vvffwGRvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=ZajQ2VNbaWFl5nvBYKclUc-DiA2499iQKVRgK6M5aUciH8vz0USv5CDbgUhe4yONY5b8kLcnT0VKgLRDeJxv2XZDwvL7PseozxmSzH_BPseuPvhHA8upy5AQRQKSwLcM8FAJKHffJVgWB3dYoI6sNb7Sgvvw85cA2HwRuywNVVTw9WmoLyOGOqbLs9_iqVwIb1uvlsqBdCNMOI_AASMo7U5m4QmsmVoIE1iWzUZ5MQAoRu35t2BPGitvRtMsg07uQN9Uqa_CCemqARq6FBh8g0HqlXWU2pljjRTEqjvtsUN8xmzcawgkzFaolt5clKuVghw03o3v97izrpU6klG3JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=ZajQ2VNbaWFl5nvBYKclUc-DiA2499iQKVRgK6M5aUciH8vz0USv5CDbgUhe4yONY5b8kLcnT0VKgLRDeJxv2XZDwvL7PseozxmSzH_BPseuPvhHA8upy5AQRQKSwLcM8FAJKHffJVgWB3dYoI6sNb7Sgvvw85cA2HwRuywNVVTw9WmoLyOGOqbLs9_iqVwIb1uvlsqBdCNMOI_AASMo7U5m4QmsmVoIE1iWzUZ5MQAoRu35t2BPGitvRtMsg07uQN9Uqa_CCemqARq6FBh8g0HqlXWU2pljjRTEqjvtsUN8xmzcawgkzFaolt5clKuVghw03o3v97izrpU6klG3JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmr7ejnvExEfgyqTtAUhm6FYKUUV5pJFx4izCexCU3V0RRfD6uASysPk7euabzN_6fw6YOAkD4njU7iuv0J0lclZEFTcVUzoS18xnpdfH1FwKZQsc-X6FAXcxceFal_C63DOXTIpAGenjMszQkBwy9UIgbskYnBIaTSp2UzK624P2TsdUVyopzgDJX1AFt0dX34wQBHz0j6DK0W8P_3YH7abvDvY6a-6xd4K5VdEP33sF8EIY0TMRneH2LPyqwm4X5BPOFHBnuYBCRZ5uBI_Rcz3vnp5HhA6kzvADYEQcRnF1aeY4G4idVzikGUJCNnQc5rrrkpU6F-__1saTa237w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلاتی‌از دیداربامداد امروز بلژیک
🆚
آمریکا در مرحله یک‌هشتم‌نهایی رقابت‌های جام جهانی 2026؛ حالا هر سه تیم میزبان تورنمنت از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25126" target="_blank">📅 10:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=Qq_sEYFBgPVrHkW9hPfqUFKHp82TKd3aT5ReLicewvI1wPdfwdKBnYeGlAvVhy2e3qF3quCNcTvDQamtlSOVeheGxICKmYTmNTU9_aIqteQU6QtNmr42t45K_oOcGN3jA5sJMfdh_Rm31nbmNkFqeW2yDcMZ3Bxm13J7h7uDoV0DlDjkp30oKRgqNoz6Qy3OIx5gbIqt1c-y5y19ltmlV9ugQ3owbZkdcWZranDMZLyG7zwF1MxHZnj2wSN0Q4ySZV9YCtwYQ2Z_WE5FNEdwsNKQQ6XaMwbcqjUcC6md38MmJb75mFKXVxIYoDRp7wPa3Mu2PZHARkZvIurjwrvrFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=Qq_sEYFBgPVrHkW9hPfqUFKHp82TKd3aT5ReLicewvI1wPdfwdKBnYeGlAvVhy2e3qF3quCNcTvDQamtlSOVeheGxICKmYTmNTU9_aIqteQU6QtNmr42t45K_oOcGN3jA5sJMfdh_Rm31nbmNkFqeW2yDcMZ3Bxm13J7h7uDoV0DlDjkp30oKRgqNoz6Qy3OIx5gbIqt1c-y5y19ltmlV9ugQ3owbZkdcWZranDMZLyG7zwF1MxHZnj2wSN0Q4ySZV9YCtwYQ2Z_WE5FNEdwsNKQQ6XaMwbcqjUcC6md38MmJb75mFKXVxIYoDRp7wPa3Mu2PZHARkZvIurjwrvrFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25125" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=fl_Vzdq1m-Im1qLlLG1BpUBOVjA3GpDo3SYq4zaV2a2EWJmNHPcKJfqaYJMh5xdiRmJRStqSrKh6hwBCdfGG-JRLEnirkJmrnDhSX-W5p0pPMdhyD2PYaoQ6rqig-mEbapfk04aO7XyePYYA6JuzLF4QVarljRt_Wvl_GZK6qRqHCCsMaKbYFhjDnbWsYA_WsXzvtIO9_2OukJ5GllGAIWHQV12EwQZU9rzsxxUmPAfP5dKyOhp8-dNrzMqEfDG2C8WxUw09QDpM1AbXan_FZVr0g_LN3zxDw3Ht-fHGhL-dn08L7IY0irH263dj_SGBE-vLrvt2H5DHCicohhNnK4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=fl_Vzdq1m-Im1qLlLG1BpUBOVjA3GpDo3SYq4zaV2a2EWJmNHPcKJfqaYJMh5xdiRmJRStqSrKh6hwBCdfGG-JRLEnirkJmrnDhSX-W5p0pPMdhyD2PYaoQ6rqig-mEbapfk04aO7XyePYYA6JuzLF4QVarljRt_Wvl_GZK6qRqHCCsMaKbYFhjDnbWsYA_WsXzvtIO9_2OukJ5GllGAIWHQV12EwQZU9rzsxxUmPAfP5dKyOhp8-dNrzMqEfDG2C8WxUw09QDpM1AbXan_FZVr0g_LN3zxDw3Ht-fHGhL-dn08L7IY0irH263dj_SGBE-vLrvt2H5DHCicohhNnK4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25124" target="_blank">📅 09:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=ijEOWoxD-ccsKsABbUOxgFARuPQDtE-mHe81-JalDB1T5__VyiOT498aS9VCjA6eVW-fyau2GKej77t1_MHm3iAgaht1ypZb-7KimzrmA5Fg1W3Z3aVKlJCZPxEKliHjc3NQ9DFkuTL0M47w_EtgfOO4WRQgVEBYwY2PELMSNevjEHP5NMXjFqXlruCNYY8bXAFiuQOxnEtRYubme2EDOAa6e1GECwW0YPHMF2FhUaR-4hjo9c4fEsuqL9OtiPDiulDBN_41SJXiYqJkGFJqO7dv5Ij9xDeW_srYvjfXg6ukgTxgcGI0Fv4bJJ4_FvzZRCCchsR7zEJcSVT5J3Q12w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=ijEOWoxD-ccsKsABbUOxgFARuPQDtE-mHe81-JalDB1T5__VyiOT498aS9VCjA6eVW-fyau2GKej77t1_MHm3iAgaht1ypZb-7KimzrmA5Fg1W3Z3aVKlJCZPxEKliHjc3NQ9DFkuTL0M47w_EtgfOO4WRQgVEBYwY2PELMSNevjEHP5NMXjFqXlruCNYY8bXAFiuQOxnEtRYubme2EDOAa6e1GECwW0YPHMF2FhUaR-4hjo9c4fEsuqL9OtiPDiulDBN_41SJXiYqJkGFJqO7dv5Ij9xDeW_srYvjfXg6ukgTxgcGI0Fv4bJJ4_FvzZRCCchsR7zEJcSVT5J3Q12w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داداش دوست دخترم فوتبالی و عاشق فوتبال تماشا کردنه؛ حالا دوست دخترش حین فوتبال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25123" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMALTt4lA2uOPNdmtU0jDqcLTUx9kMG030osMMcQJk1v5xNf_dWgyHIpFqC7N27fMf8CQlqFiwAhq7u32ON4i6ZdUDqozq4L0JgGM8r60YhCkbxnP3Po3OU7O2-Ef8CGCpEQ_JNuvNRKI1Hf2xAVY9COQIgIklMzp5L0H5-w68OFCIJUNYUTscW1INV3cqx6w80UZ-ccVCFPw2ciQb42LcEcnOU1gdGBlH9vTQNKpdtIZwQbic5wCKU1HYRqtl6tHZTbkLmHujSl4t6w6cc5dOXLfAhN_2EOoKDDH1EKJ7hL1ewIu37KvYDdsMcUyq3ys7x2jgxHde2zp1KM9nXg0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25122" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzL7AlCbPFUeo76-CnBoGrSMyZhU7uwPf1NxED_Ovz_8qF_wOTVN0i4Wyi-72M3SYNMe2Ich2km65Q8ejzr6aB_n89sEHgQvNFfImQEH1zhD63DC7o5L_z4Uj5xK3rxkidpVLoIJevgBcpHNkj3ElY9e4ruUEyM2IyrKiloRCiOxOYX4uVg0fs2GtQInJAzAzF4ZySrUVOiV7t8EyGr9gnOXrwDlXrRZczOEcbw6J8VQwEJ0nO3NldRWLWE8LgzH0F1M3HWD765585vkn0pqekIAn-hvwvjZIl1AS19C6jAouUx5vxl54JtnMXIDTPAv4q46RqJ8uRhZ4okLEM_I-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25121" target="_blank">📅 08:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMrPC27nsQsHL2gMjKZGiFTRkxj3z7_9Ry7kuOCvyPm2fOLcRuoxWGmJA2l5MvIF_dRQPZ13nOzX4ae5O_m5sgf0hWBqRRRrqit_S9uSQMRBHgBy1A4MSd_D45K-s68fTO3hwfGXvYMOmk2W9RKSTIUcWq5uurphhpWMMTvPKWEYP5hwSrWshlf9W_WjioCxtO0m-Lt1g8h_YeCfIzFtaEV_y-KgjtJsuDOf1ljVJWr6fV8gyTOewcSYDf0SGEHX_xIht03a_eidBzw1SkuBpqcUjJ6AvuWJRKMaXebUahosKQK1zDzwarS7OKN0_nqNjt2VhcpVesXTFQkMDh6IMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25120" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzZ0Nt8K9RQ7ty9FctrKkjPubofYIgLauvWmVNVsSpfmVHBcXgCxdw7eUTR7r7nQAXB_OOcaU-e8XWxVx01mlNdWh1ryxnTF4eswH4_Zxs1LKD7dP85cN6jmtFDqt9bjcU-TV9_27a7U173aHvIPrG_s7SMX0PD5TaZ8T1bcp8w3FcqCDgADjbmr5rMl8G8SM-L5Y8xsL_ByntMsG5gfYmtTFhcc3C66LAJsharcCQXCt2lOPiGDYNCe3me1u9WdxCxtnpyEgDCcjzrcP7SnRvdgAn4VfaXBiY-udxBWBno9LC6ViPUT-4IGUrAH3fFYCp6QvwaTaP7dCHuGTAYIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو ویدیو از کریس رونالدو و صحبت هاش در پایان‌بازی امشب: در این سال‌ها تموم تلاشم برای موفقیت تیم ملی کشورم به‌کار بردم و سه قهرمانی به ارمغان آوردم‌. وجدانم دیگه راحته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25119" target="_blank">📅 03:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=jXP-xCyzBz_L1tyhiEabWRB1OEk2M901SzFEjHDoMT0yWNIOiwYQRwTmjsQKiFDyH35nmdpYO9OegiRFzv7mOjCk2oibDT2aZLI2AOv6mgWqUknYfULM5kg3Csn-hJHIE_9GTOY3CWSIzAExOxYGfw8uoVNdZpjwBnBPaxlBhTLpom9QVWD1VsvmT_QSyZ8wONWWY9tRE26HWPzUbgWOygjnzfZQrk6D9v4dm7LqY5zs9UVmUX3kOjze3Ihuc-GvUqMIEEuaWGRYkJJJCfW_zmdP09WwQCgrG1dq4NpU8h6C_P4DqOwU9Rq7ja1GdYvTk2Bf0iQBHDdnvGGIOR10Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=jXP-xCyzBz_L1tyhiEabWRB1OEk2M901SzFEjHDoMT0yWNIOiwYQRwTmjsQKiFDyH35nmdpYO9OegiRFzv7mOjCk2oibDT2aZLI2AOv6mgWqUknYfULM5kg3Csn-hJHIE_9GTOY3CWSIzAExOxYGfw8uoVNdZpjwBnBPaxlBhTLpom9QVWD1VsvmT_QSyZ8wONWWY9tRE26HWPzUbgWOygjnzfZQrk6D9v4dm7LqY5zs9UVmUX3kOjze3Ihuc-GvUqMIEEuaWGRYkJJJCfW_zmdP09WwQCgrG1dq4NpU8h6C_P4DqOwU9Rq7ja1GdYvTk2Bf0iQBHDdnvGGIOR10Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: من تموم تلاشم رو کردم اما خب نشد که بشه... زندگی ادامه داره. من یه قهرمانی تاریخی دریورو 2016 دارم که ارزشش برابری میکنه باقهرمانی درجام‌جهانی. این آخرین جام جهانیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25117" target="_blank">📅 02:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mespLtPh0NlsyAm2nxC_0_awoQIHtzTPMm1Ta8QY38y2FRR0RL6SF95veQsKwCz0s8GDt0ZSGtJbiBgIsWkyAjJvzWURarOzWiaU8SnmiOggH8728vNsAUTq2XTFNeXFMUVlKd1E_rPKMaA4TfhKiMa5P2uRoNjVXgDK7lFfRbCg2vQksH673zf2DrfEcVudSxVjINIr28BNw5N7g1IGvFKRLr8hNh_OJqveeK55LyACDFr0rZ1Etmyds5bYPwRS9-BZYvZbIyhId5ay0GwpWwjDN41Ng60vuTRc9x_9Y60qLuR9iKWVFMxfiM5xRLIJliIs3XMmLDHZJcnfu-MDSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25116" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xpv2YPZgQq8LrYsp6x26-0Ijtqjc99K-0vafZYqda6TYmo0s8vTG2Hursk8F_NUiCM1bPEIa5hivwjlMtn6IBOANt2sy0t4mmYaEPrO8Eo19nJi0tkKNvcXmu36yCK9m8vJRybSozRUx0JCNgiYkPMpXYMZlsnqi3SXmzOV9cNVs_nUZHqZ8cuVBEMkjMh1DGf6Jt2_-IqauzOpLP8dbbKCffJIulEdRp_5Dzdr0re1KnwA5B8_aQpE35-Vp_KQIxW-QfscXu1j4vKlJucq__v4sTd-S1DxgJ7T2WTHJEC0PIPQNCfgR4V8iWZeLtDIiPWj16Xz_Kuelw4OidGaL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم‌ملی‌اسپانیا درپایان مسابقه به این شکل رفت کریس رونالدو رو در آغوش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25115" target="_blank">📅 01:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va_WcfnfcmP4xSrUi3NAEIk7uXtXz9m3cNW5mBw9VHKUaQClxgXELk7puhDKCZMCFnt_CsKDV7Vpn9I9NemMfN6PBeQptosXKyiR0-989pyPbOvlBLxUABVoj41wNr3xjbe8Ye987i1Y_uKCiVnrN48fDlPWU1AOIoJ5Ay19AJlEOKgQfSONoOuD9kkm6x5L6kCJFnrdj6S5Dx5BXTWMtIMG7jwewKJW1ag9Sz18jNl0y2cCWwGlyE9yiUmd8ivjnboR1LIzczBTFpSIgwBurrsE1tQhSdyrYMDQ6dLmB6BvIcuxerttKlr_Y_GdleiHsA3zfk-6deccDR-WFKLtjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال درعین‌ زیبایی، می‌تونه همینقدر بی رحم باشه... در آوردن اشک دو فوق ستاره محبوب فوتبال جهان درکمتراز 24 ساعت؛ روبرتو مارتینز هم بعد از عملکرد افتضاحش ازسرمربیگری پرتعال استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25113" target="_blank">📅 01:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHXC-Oxu7gjg1bm4xSSeWEs4vx8HCz852d-1535MJ7q4nZwQ3BT0ZIi1BbeMEV3OKOdeimkex_Z8-5HfObTo7hYwsVpdQFPauYe8OSGjYRNC-B_N877pK0KJGgcEMzjSRk1Zt6i4BR8YgKQdVvqCXyzeST_PN8byvbfT0SITma_qjxaV2sgcRCQ2Bov0SAD-rvViIsuEaEFVqd2W8liydm-ktlUEec9oPzSPY179tXF_F9EHtd2GxJquE4otvjZGqIn9faxlHs6WBdI51D89YE53Y_O9N2zb_qQmo4MAgOWR-QzgsP7bwJU3Uh6Q6nm7Uw4vRjhN3YZiYSos2W5_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25112" target="_blank">📅 01:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5OjAiK1FbNBA9f_5M8r2bBOBysr1iIutB33893iCDGhWhCw3K6LpEv6gbIMbXccDpThB95qEkwWGOEdZis4ISy4_V5WsByRhQ8xEV0ReiuQ4vkU2uIgqjA4BuC8lEx2QAOsbZQG51Mig-irZWngflBptrhJN7k-bEi6c7qwciJWQM4krtp75vik1y-199Z-KNiEH2bggYyR4QEn6Ha_KFsC6dRsSPLXxCoydizfeLAgf_fhGBTF6i6mUb2R30mC8hNtHb8XY6sT0D_dEdMCxyITMmF51xPppGWvs7gXu-M6GERUO846vVyXlx4YLzmCDehD4psjrHOgBC08J5oW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25111" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFglhBEdY4MxeeVG10EePW1aWJHCR9MtwZnmbEkFCoEKHMPoTEmOoCg2SoMuVH9UFTvwsJfPFZ5-G8cdv7MWdG3WB-6-P0p7IErkQoeipAxTmU7KgO4czrRa2qR8M0jrkC3RrKD7Njrfkm30OYPhvZ-tbqZfGIi-hI6ccnQfkIZ1J1w47kSLbpOkKKMKuxV2iNKQixry93kzC8c9FkXm0Dn8QSa5muLqrchSp2by9lBNGM_ASfrwtBexaxFGYbpje7unZ6gknQRMMoLKpweTuoAR-aamoQNBJTJ8t3haghoMWr1tO5_6iOvaWMqrT__AorTsg8LJAMbgtEeSNJffdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
صعوددشوارماتادورها با گل دیرهنگام مرینو و برتری انگلیس با درخشش بلینگهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25110" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=lGFyzdO5ozdbLBvvmi_Av3PP1HsgYRat-9shuTYlGVsYXYU5f-983_qVkOfRwPy0EJYd2g8RfuIt_qU0DmiTPieT7eom0YdsNt-DqSLq--lLT0nFwl3duPs8nAl4AEG9T_K-5wtfQFfIMLHnHzpW1AgnYE2qETDI8SS4gxAiVqXjgQ1Hn1c09oj3vBG1aUaZw6mM1N-TOuc1gX4CEZn280FBxeih9VP7yCvgskOfsZXYJK5HUBdyTLIH-Ud25nC-YX_dGVAzOl5_RVFRW3MdmkYlt3UFPd3gM5v90VJ4qV58juguDeYypi2ksNCfQ7yRubY4cLLQ3vZGCj3fs0LYpr714yILSfJ0FDkWH6JP_kp2d-_Mo2pc8_t6bjV0qg_3BSZJcoosj8GP0g_H7-LJMrds67WG1fclFfyRhaQiFv07-rCjDwF6UDkXoYcppolLRXaGfhXuhJkMhk0JH65eYaD6zbmCyKP2aMPD24eLG27g8joDiuTzYBXz9zPoHaBo6Q7UMoQ36NE3QrtVEDWgg3bvVJKxTdM9o5pxpUhfZW2-u7fY7msV3UNrIJ5CECS_wbn4iJYiT2nkVtLUn9SXkGQwlfhxp-JHodY3M1W4guyLtOGV1FeRflcxyT42XqTroS3NciyZZzSpXLDQTYxzf0ZGjuuxTLC1zYGiCeWkOI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=lGFyzdO5ozdbLBvvmi_Av3PP1HsgYRat-9shuTYlGVsYXYU5f-983_qVkOfRwPy0EJYd2g8RfuIt_qU0DmiTPieT7eom0YdsNt-DqSLq--lLT0nFwl3duPs8nAl4AEG9T_K-5wtfQFfIMLHnHzpW1AgnYE2qETDI8SS4gxAiVqXjgQ1Hn1c09oj3vBG1aUaZw6mM1N-TOuc1gX4CEZn280FBxeih9VP7yCvgskOfsZXYJK5HUBdyTLIH-Ud25nC-YX_dGVAzOl5_RVFRW3MdmkYlt3UFPd3gM5v90VJ4qV58juguDeYypi2ksNCfQ7yRubY4cLLQ3vZGCj3fs0LYpr714yILSfJ0FDkWH6JP_kp2d-_Mo2pc8_t6bjV0qg_3BSZJcoosj8GP0g_H7-LJMrds67WG1fclFfyRhaQiFv07-rCjDwF6UDkXoYcppolLRXaGfhXuhJkMhk0JH65eYaD6zbmCyKP2aMPD24eLG27g8joDiuTzYBXz9zPoHaBo6Q7UMoQ36NE3QrtVEDWgg3bvVJKxTdM9o5pxpUhfZW2-u7fY7msV3UNrIJ5CECS_wbn4iJYiT2nkVtLUn9SXkGQwlfhxp-JHodY3M1W4guyLtOGV1FeRflcxyT42XqTroS3NciyZZzSpXLDQTYxzf0ZGjuuxTLC1zYGiCeWkOI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25109" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=IyYHJaapgxIyg07Zm6bnx3x_KPfp9rbs4gju4zzeQzbnFkdEEue8R49yarypkK69ZWkIAIYl3Qcope1Knoz53YDoU-JTejq5V12Hnmfj2nhWo-GJhT5fEoCUwK6YbdQDi8S3VySCL5pT1xFa9a8ZTIS75zK-xup8WUdcYJTW9sbOX3p13J5tmMVbxVfW1La44n4QNVywn-4HE2YCI_k5pLDfi9Kldnzik5aOwdFID5eQkyIEpoRnjwxg-Nikp_xpPz3aLqQu-WtGx0YmIsQdMsPy1FiULEjkTWlhPASRPAQFM3rwf1-jU8VzGb-rjTCyd_GNq-p1dq_oafP45eH9UYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=IyYHJaapgxIyg07Zm6bnx3x_KPfp9rbs4gju4zzeQzbnFkdEEue8R49yarypkK69ZWkIAIYl3Qcope1Knoz53YDoU-JTejq5V12Hnmfj2nhWo-GJhT5fEoCUwK6YbdQDi8S3VySCL5pT1xFa9a8ZTIS75zK-xup8WUdcYJTW9sbOX3p13J5tmMVbxVfW1La44n4QNVywn-4HE2YCI_k5pLDfi9Kldnzik5aOwdFID5eQkyIEpoRnjwxg-Nikp_xpPz3aLqQu-WtGx0YmIsQdMsPy1FiULEjkTWlhPASRPAQFM3rwf1-jU8VzGb-rjTCyd_GNq-p1dq_oafP45eH9UYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
مرسی کریس‌رونالدو بابت‌تمام‌لحظه‌هایی که برای ما فوتبال دوستان‌ساختی تو مرد تموم نشدنی فوتبال هستی دهه‌هفتاد-هشتاد باتو خاطرات‌زیادی دارن
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25108" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0fUwNfhUpshKj9j_x1hQedfIqT7PTththypT8KOkcsAkx2M-lJGyqdWH0qwYsYegzj9tIfcesw4pqmVBnuoeezC1p2MvYZoxtTToDZAF-bMn9z2QJJ9Ck3_A7pItx1jsGcBTsq_uQjhTFJFSrnzGeU7X0CzIEHWSYcERL7Bn74URe1cavbQ2buTIss2eG8DOLtjyMbXmbDIhYSZ978yU2wUqZZdLelPm8JVXZVUi6p28SvGaAHXNIpb6GfK1D5Uka2zznSisZOU3TbBzMx3-cOklHNyUoXLTlKEJKEt1a719_HTeVjfGdQj2yx1GDjxDqUWA13Xoy1O7hvyGcDqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
اشک‌های‌تلخ و دردناک کریس‌رونالدو اسطوره تاریخ فوتبال جهان پس از باخت مفت مقابل اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25107" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvLRDd557h2YrNPienm9tYV7T0KvFcWIwhz6RNWk-CTXaQMAxmtke75_ovOd7jF50yJumi610p9LlFnPJcWiiHyvDAL6Pf1D01IqjrFKt7oialRegnzCIXxBGtBbculd8DLWhgteglfc-3S5ZQjnm5hn9RituoVPd4EfrQTD6GK7n5BZi8jCi3YjKMlFZ-A0abuGgUNozMB9kf02tDBST2ec9Oh7DiBRnecWDkZZY2T-xfciNotx0PamlOjerBCVNUQ1QGqt9RIEOHNekM963GLlxZUN68T0lYb-_XpIMhYMbaBrCz3mDuAFf7_77Qds9KqXT34yVWHLpFMjRgYLBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پایان رویای تاریخی قهرمانی در جام جهانی برای کریستیانو رونالدو 41 ساله؛ نشد که بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25105" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5vOTnSOiCKQ1Klr9dU8eqUVBTGJKYB6lnStFN1WcwZBO2n5vAWX8PnijeEVFYuViML2URfuYP30aiA5utiSmKwJsJfQL8_p0MlgW3efYIXn_joniAoWDR1lRC99ixhSYv3JwGpS7cY7LEgzUozT41DwwoQt5ljOGiaSvu-avz7-8Kmom4XE19IXv6JAntrptF1BOytPHz4eETmJbWFptZIgz2TCXNuYC5fvs2gT64n5J8WR04MXnkJ0ishARBnTvyEcKOx8ulJlUd90Z-s5BNiYJuOatHQHRsifQ82n6XtpWfHixDX0qL8kG-RkPtBxK4qYSPz3m1EEkAxCCA6NvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25104" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwzyKO6nC63RjtFzimCm_SmocPKoI8tdQfey17bqZR_a2dsKHb9Bnfll03cAwMsmugFTMjN71kd4kfKPR_IJBFmwm6AH59mgvgOiOSJeYIbITBjuhqJv9UkgyfNVyYhJ0yyO3qzSwMNyRl03EB4zKhBWlrRAD4hGaOUNRu5GIeNYiz58MPADMXTqCZzJPqYB7lk281CkltGE-aF1sc0Q_3S8NSeEcN-Ys-l22jPfXLcfSvR238KVNZKCMISriLIYwAPl_3DDK35L17-ToZq1fNPXu4hUkzzIPjjSr1Wt6BT-PyKraEiaoEInckIeLt-2xdqh9rBJHNyoLvdDASlhig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
آخرین تقابل دوتیم ملی اسپانیا
🆚
پرتغال با شاهکارکریس‌رونالدو اسطوره پرتغالی فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25103" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sewEuWs2QoXtTdyOJU1Pr6D_rz6tfX0DxYyd2w4mvzalSth9xDmkK03ETfyhIamlaCxYVOHO5XssotusuewYzuC3axpjQWwiuSQPvIcyRSau-xqlZBnCljSwZKWDkqLiZmvqsUmU7cjwjHTwu3fliUyToPObj6sSm5f92xNI9wgX2Ian9fbfRFMfdLgekJjPLKNZnpEAi6_RhEIt2KRdQvhl49vEZLogRW0fbV1dQCYLPlHsLW2GydSxEpQ0QcKpJnUs9LTBCHvpgrqG90GSzWStma75TMPZPD_CVKFB12r7PYCAxK-OdaCRheAxlUmYyTXDOW_1_aqIGLOZUprMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با رقم 65تا باعلی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25102" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXNnIon8ZSJzAj52l9u9Xsl0Hb88Byo_zpplbRy6_C74ypD1c-xR4fVxX5GdL8t4zyQ4MwcMIbN6hROhp-oLz8YiaCelS1pDglThWv9GAHlOKI0TbPglts5Dn5CescK4A-kjUBpVaC6RTyfyq9uNomFbjZ3G31yd7g5Pu9SWDlhWqBBKD74Q7jsK7RH8ZqdZ6RzoF4yJubQTD07qDPeZClJhOY8Bt008LGK2NCTYcXMZrKUL_VCJD2g6ig6axw_2DwhMCtsk6Fl64C8AdXXm7938JWNJGeqMp04SeqeFMu89HXUf1xCKVk8Pe1c5tVlxE-S77ffB_lIcLj9Dr2VthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25101" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYF6FqZhkzHdobSk8t-P4iJ3jEBYfsZq7waUdDDufiLSv_fatbS0sBUJkFq7oCrp9lpd_bQjEtIqIhtMspAtJw-ITtcSB_eg5pWALf55_m9OUN_ui93SgILqyPvjX9Jcyk46no6xbWSPNzRIoJltf45bqcpumeoE75o96AkdspTQLlG3QlaLmof1Gl1VzZmm4Wvkv_WX3hxv0gAxDiAbAZuOLS_OvVu7uhfkdv8q-PK2iFH9DdhEP-1dWTobd62AyfGKQDGVPtZPUcHQNOIciLEGGCFTkh7ie2_LTSOcxPOJxocN08DltMd2ClIbKsfjGmqVMQgdiBjfX9z8Db0Jog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ آرمان اکوان برای عقدقراردادی دو ساله با باشگاه‌پرسپولیس 80 میلیارد تومان خواسته که نسبت‌علی‌نعمتی رقم بسیار معقولیه و پایین‌تریه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25100" target="_blank">📅 22:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RngMLUwb9IU5VT09vDFVrwSwcBwmT37ta-Ms6VAxMQ52eX4p6r4gHu2-8IkHNzTX8J2YXPmM4H_Skl8In11sMHqxb5sQMXfIiqxq7or88CrFWKYgW2K_iP49pWZGmfFM_OV4BoIa7fB46eGmBCwIERcg2r1TfPpU1Lc3boRPzjzuJndgUaVwSNzsYpxetHrWVhj8T1QCJPXSakI7hQPPyKebpNRCbzNSmeU2Hz1YSlMtXlCUoVi5o9pbOsvda5DMVuE0GuNaQLbHHYfGkzQ7uknunMRhuVpjrpFaVp7xafxzLwyBa7us2oWB5Z2cAZBpdCyTN7cDCY3I_iYcy2XwFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیو جدید تاتیانا کائر پارتنر ویکتور فورت بعد از عمل کتف این بازیکن و جشن سال جدید 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25099" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_Vy4JiidCE-R47dRNKyTqW6wWGJ6miOtDJEeKLwLs7gnVeIGoWtNNh54KD-YEOqNLJnVHXlmuvqaDz8fxD-_sz3rLk0c6RPZ9Jc3V4BevcfjMMqT_Ui9pb7k-MDgULwWIj4wDwnkvBAGtTn4xOU9zftNvxZQQ-CWUI2f5Jfz2pNmwfgT7Fm7OiNEWuFMP4f0p2f0lEid-1apnlDZpEaoojRG2LKrtqO_v_gV2DNf3nFVUe4dNbwabWaY648px_7stqX45-J2AmMvgkVsmW7_weFVPqI8ZCe3ox1oVrpGygcX6DeAuaFKerif8izan2c-sEXKRUcSvD7239cB1SfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25098" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkGWscAjRYAQmgjq4xiLTJrVVRHINo8R6VRva_OoRNjFhW3IOGH3WNJfWOLhFSQZs7nGHAWXia8Pdq5pDQnM-EoIGp1m3Oa90aK8CK5iCb2DS5yExX7alUXaY_JnK-xSrA5NPIDt29Ndc4vGkDytInrkd9hJ9QXxH3OfZo0LFgaA_5SVkJFZ25LRPJnNqqQk5pGUWUvxFZPdsFp_T2w2KVUMSkRP029-eNSOYp40S1hNOcyZTJA3mRnWYAZW0sur10f3xME2NqC849TSnn2KHPf8pV6oiu1wOrOjriGZ4R5riN3WpiV6izVfCc3LGjUc2D9tjiHgR40P93mHyx7chA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25097" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgcSuO_s96pJw4rSDwG1NZR0bx4pu6Pl0xvx1Hq0grxvz1B0QVUtvLpCqmgcvzikdD6lqmaEn_WvlJho6tdLDimtqDXvg5wtG_0_c-nk82mKEdo3Y8qsyROv5FoLVwlNTPOt14ceI2X8784678xIT7AO7hjIFYaU2e5o81AQz57KaUusizz8Q2ZCciKkBojf6RpfJHLzvAl3O3yCnfFVs2iKQw4XjcnILfV2rOlIgquX3XAfDwTvVO4V-JWL92wkh6NHumXWTmtm07xko2JioMFcoJ_Y0RTj7SO47djEEIDwL42l6uxtcsjtwQe_qRdg2L3MNZvOpa7VNDzaZUBrcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25095" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp76UTbFq_7GRXrJzl6XsgzhUFX954dGSjhr4ZAIyqwZ_vfyR_YcgAjNcBuBysoL8WtfzflxCwLUsy7PaAeKDDerTNSTJFxrNP1MN0CLDdJ05Topxzhh-ILCYvLzahqwj_MnjGAfsIP4fhLHQb_nFQdGME9VpAoRE7qKPBjI5MwBygNkkWbSJXNqwsWC42UP5OzNLsulbpAKIvWVcDQqQyRo1NVdQaEFSRYGVaVPzGZhsya2LRXI6rUFTu6Y80iNropAgDw98139VSLnLyT0jJT48cjC1vWKjyHmU5lwtQGrM-cHwPVpBCuEOHLZC3HxVcsRaw_dShVztheoniq_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25094" target="_blank">📅 21:31 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
