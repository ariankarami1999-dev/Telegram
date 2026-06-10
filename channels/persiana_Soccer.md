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
<img src="https://cdn4.telesco.pe/file/S7F72QmCcMignJQwYJ957PtKh_B6xkSLNPTi-Xtw1sxwipbJDiawWGBOtKlnalxhjy-WbOgjouz1wX326XOknVklEk58MQA0CmmYz7XVfM0Hs3OSV3gk458Bh5olzdiwb3p71Hp61iwJxufpbM_gJ6e33-Bvh37hOawS4kcFRmajkPWRKjsRqDcZn7MmBE8dAIr-XyKm5YvKIjJUilx4UWrk3uYVPGFr546HVnd7n_yfuXi3VVxckwL-a53UqftUG_so_VqP0ZQN5EtLjLDMkLfjFPqT0t9K2dtrZknaC9qqlEBVSOyWvj4SJ_0pL2ic7bj0_VgFSKSB8Jz48wskqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 196K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 23:44:16</div>
<hr>

<div class="tg-post" id="msg-23144">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9VNgN-3F8BhGB6QbulZxPdQQuzyy0yXwc8Roc_TgHcy_om1xQHG2Xd8z9Kwher2utEUhNzb5vP21jovvIYuWBgwXt5CLDhF1YhPJc9ayf8berreAz8xiQRUsumaxv_76LghuCep4yJySKL69Al-Bda6lRfDPgc8EMbjwT4tGjQEw6gxNJQjH8ljen3Rp2FmPs1LTsH1od75FvUFyTuUnMEPSAIS8efYMJP1P3j6i12vztGH8kZA-n7yX_NVhibb3TXASTo6gxCVn1qdlFaKfkFjmadRM6F7YxhLfgCF0rt8hvo4V3-wnBS8xjYMd11rsbi_dQKzcfrKMpYdg8g5-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/persiana_Soccer/23144" target="_blank">📅 23:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23143">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY1cT6C4TyFsfj-d0FHWp1hxvNOU0X2jp5-Gm9fd6-dODNj3zSzX02XHDAK_CKXCb3dgiJm_VK75F2dDHwHL8SHLTpMjUcPEGiqd7EyOgVcG5fXiU-Qvxxub_IisMji4lJcO8GTYeSYAyuw2oVAPHOdcZ_zAr35dodG5WMktjC9NV9JrPqYIbYSfSyEzpeSV2KbY0NmdPaGUpDHap3UkeYnK2giE5nXVg4uVSayGqDV8dYgdPI4esLDd2IEeGAB9V6EqFaIyo_qWjRp8SL4LCeYSN2v1qWNL7u2E7-06ZmCH1RsRUALtITesfpTlG1Egbz2_5YPRCstS2GP7_AmwEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/persiana_Soccer/23143" target="_blank">📅 23:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23142">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GInGKkenhZiV_NACMmmUJSLpbFQah-7hxLeA8ENiDhxV5qf3ZoIw_HXsk3GN4MBCUObISVZamxlNEZBexzYKtZ3jMFQ18d5ss5sH_T6HcfRMqpHt329e04jjh0eT6CUf7GISiZiFb5sjJ3fQ4f7WoK_jEjIrxoQ2gedr03VZ0dIK1xRFyYhXxZz7PdLpq07vnkOkmD0rXVuFfa2TkaKtVqWv-6R9YYol0_1Mab0b7-OI9SEozP5MJUNgj9rVtBiLbqvMDokRlP8sKuwnEtS_gw2VJDW1QKgudXsDesdqv3-dRY74rmnhSIZ2NQzgPgig4dFUv1I3cvDxalD_UdHi7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/23142" target="_blank">📅 23:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23141">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy2yYeUWFrYFSLh4wQussG1jOmeqHR69evmfsgsNlwt0y1hVxR7LHFAdXLHqWKRsHMfjjin2IK3efeFdMuMvGY3k8uKI-3a02QdRNl15f3Gaer2Y7hqtvobBffy7JFE3bbkox1wo8ftoc64n5eD8yMOsf_7sFqBdX74Bk9YQtjO-cFcArnbmdRyDr5RWmZOUFZ6ndEFcSPXBlfFLB2kYpp45760WldebQXx5u5FoOZSvCMQ1ZmmhDkWC0XeznMhVSK8-0c6XbWh2QTBEP4S0IQmgmjAOd-rVATGDUBd0nQx6oyOYixbLfQEkkhc8wcU77U8GmFLqXj7eViHnTHr0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ متاسفانه اموال و حساب‌های بانکی و خط موبایل وریا غفوری توقیف و مصادره گردید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/23141" target="_blank">📅 22:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23140">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=dIgr-9L-T2m1TJjTXokXjetHb3WCgkmNlEPYRoqXke78eWMlTADWiFOZhmWpGY3TdREnnZ1k6ZLlDCsG-ZysKRsp-WPEQW6wZXEFIy5QALhtYW7BvImDZ4bwSrna0oQuAS8uJu525NHBmdA5Dk0JmjN-9eTtgvVhK5upsLfla6gy-tuaig7zRESx6lwVqZ1psrhLuRT3qT20txiNTOpj42BW6weOe_h5W0abr8jOx3UgoGQd5Y_1JC8AddpSd19fDg9l9F9U3JCUpb1pFCpMx926-sEq0EENbTlSM9SHoneG7ePDGQTiRXg6ZwX9AX3kqSEEB2SucF-S1iSqVVvcZxSzGqSBfEDU8Q3akQZWF1a42SlBzytLwOXoF4VRPCthSvgkFLBgPtytWR3a3luvUvkxS_D-uOwYDuO6CpaJPIY1J6w-aezAt9ayGHBvR1hUhkPS2FshRGRje5iQxlGQZrid0J0CIooum1e_I2VjDMYGe8mjvq7uPWGJdSO1THOsHDDB2J6XNg819UQnz05q82IOq7tTjUxKNjVbyJ7zcUBm0QYowAPyAXhw2U2C1Kkk996UB0Ud-w6eFOipYOYBsknC2qSoXymnlmobIM7D66i9XBZhmwi5UlMYkfdgZTKjgxuci9JYwoz2zeA3t8g3meWU0FpGbmzNyarGSmf_O4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=dIgr-9L-T2m1TJjTXokXjetHb3WCgkmNlEPYRoqXke78eWMlTADWiFOZhmWpGY3TdREnnZ1k6ZLlDCsG-ZysKRsp-WPEQW6wZXEFIy5QALhtYW7BvImDZ4bwSrna0oQuAS8uJu525NHBmdA5Dk0JmjN-9eTtgvVhK5upsLfla6gy-tuaig7zRESx6lwVqZ1psrhLuRT3qT20txiNTOpj42BW6weOe_h5W0abr8jOx3UgoGQd5Y_1JC8AddpSd19fDg9l9F9U3JCUpb1pFCpMx926-sEq0EENbTlSM9SHoneG7ePDGQTiRXg6ZwX9AX3kqSEEB2SucF-S1iSqVVvcZxSzGqSBfEDU8Q3akQZWF1a42SlBzytLwOXoF4VRPCthSvgkFLBgPtytWR3a3luvUvkxS_D-uOwYDuO6CpaJPIY1J6w-aezAt9ayGHBvR1hUhkPS2FshRGRje5iQxlGQZrid0J0CIooum1e_I2VjDMYGe8mjvq7uPWGJdSO1THOsHDDB2J6XNg819UQnz05q82IOq7tTjUxKNjVbyJ7zcUBm0QYowAPyAXhw2U2C1Kkk996UB0Ud-w6eFOipYOYBsknC2qSoXymnlmobIM7D66i9XBZhmwi5UlMYkfdgZTKjgxuci9JYwoz2zeA3t8g3meWU0FpGbmzNyarGSmf_O4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23140" target="_blank">📅 22:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23139">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba85793af.mp4?token=Nb7_Ac5DxUhf9EiCYZmPqOO96f2ap3rC4YtfOAlff5aLDYBQbCouhII5TlzbrSm1ku5EbvlZXRAdax0IrfN49wQXaRD-o8dPIJch7M512q0TqOkB1UELd2Wai7sZYicWsd2z40hD1iGpOkoFntQJUfNQ4nhWaEdW8CGTdk2gsznlsY4eeP3FyFe-OQAAdwgSBLodSrm2sEDs7KjHSY7XlOWJtzLkleIn-0IYDQE6PzM3VIIyQhCaevmCesWWgYW4hiAnEf03NuCS-mnDyWEQ7oT4NWTxQzK7wJEGH64Kd3P5NZylGc3OsSIeoPRV87Cg4sKqGJcCJhkIFZItCpj3RH7VI6wcgb3MnEwxoPAKTEed-HMz0p0yWXBPG73Fpuul9L3dZYjei9rbFvri_m_BH0dTZCKIA9HQqeYDqcEHwLKpCilPzVkBtkmG-ughANZ-DdZpvwrOSNQTAvWZJGHT100IjVBqt9DnCev5Ji_HkUJd9a-Ke2XLk6i-hla_khA1IkC7QGkgvGoGSomjYH0fqSGmkYV5tG53MeUQPcEkE82K96IZ94LzNQok5qe2KTk-idDx7L2rgdusYR1AWnA9tgMagln0f0I0C0o_LigTCvYRXnBxtlB0-oVv2cPHegElQhXcUOUgqal4yDXDb0op6m3TAnqOM-pEbbKC-rHO-II" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba85793af.mp4?token=Nb7_Ac5DxUhf9EiCYZmPqOO96f2ap3rC4YtfOAlff5aLDYBQbCouhII5TlzbrSm1ku5EbvlZXRAdax0IrfN49wQXaRD-o8dPIJch7M512q0TqOkB1UELd2Wai7sZYicWsd2z40hD1iGpOkoFntQJUfNQ4nhWaEdW8CGTdk2gsznlsY4eeP3FyFe-OQAAdwgSBLodSrm2sEDs7KjHSY7XlOWJtzLkleIn-0IYDQE6PzM3VIIyQhCaevmCesWWgYW4hiAnEf03NuCS-mnDyWEQ7oT4NWTxQzK7wJEGH64Kd3P5NZylGc3OsSIeoPRV87Cg4sKqGJcCJhkIFZItCpj3RH7VI6wcgb3MnEwxoPAKTEed-HMz0p0yWXBPG73Fpuul9L3dZYjei9rbFvri_m_BH0dTZCKIA9HQqeYDqcEHwLKpCilPzVkBtkmG-ughANZ-DdZpvwrOSNQTAvWZJGHT100IjVBqt9DnCev5Ji_HkUJd9a-Ke2XLk6i-hla_khA1IkC7QGkgvGoGSomjYH0fqSGmkYV5tG53MeUQPcEkE82K96IZ94LzNQok5qe2KTk-idDx7L2rgdusYR1AWnA9tgMagln0f0I0C0o_LigTCvYRXnBxtlB0-oVv2cPHegElQhXcUOUgqal4yDXDb0op6m3TAnqOM-pEbbKC-rHO-II" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/23139" target="_blank">📅 22:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23138">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6TnQM1QusLFHt8f7ZC8kidELtG54WUxA6T1f919EKKvRY9SE85gk3bm5UtrdAFKy0OTDcHv4YqUEaYXhgvshYZjfZoDGqOcCMnT3KH4OI7dgrxuMr3Jl4Ftv3y_yFVOky_wpteKSo3izxBJhyf_Vtd1IwMOThioBKbjI2pi68J7TQV_5X6-LBddBfPtyy8xVJHWhvtsTWJOLmI0MPYygWmDv2pNTYyL_hEGh75kKfZzdtyA4GoxM1ZlSF9YbillgGwQzxkLTEwLYntrtQ0972j9ye1EsxjanMSwihfyuhZ_g6ArgJC_5AHMsE_sLS4AAAMkw5oIsy55KFh_k9YbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ دیگر مجری ویژه مسابقات جام جهانی شبکه TRT SPOR؛ از هرجانگاه‌میکنید بکنید فقط از صداوسیما باحضوراون‌دومجری عنتر نبینید. از شبکه های خارجی‌ببینید از هر نظر واقعا فوق العاده هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/23138" target="_blank">📅 22:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23137">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ho8H080P0JIl7NIFTOtHW4rVtMunaq3Bt11CTYZL2zKRqbZ_ypalFNvCCYI2VuRcxphhYjKTAk_ZjJfiMrpxpTWGkPm08g4rTTkatQuYYkQZ1InkoKnl327dJaO473BiKlzShduQKZWOuHDv-YpdS7P88ny2i-dqAgnwdSqluWGb43CR7tXAa8PiOhGTyzXS0JwpWy7NkSv9WC0o6hckhJ_QWdR_VsVC0-EkbPheC7qpq81RxTu49Ln1HG4odFavs-CpFmGbCL_HElL-PMOQg904hlNLMivW07BdwJhnqT-gvT9UYQybdrEZ2umKwwtsy0bFPt92xFII305lxnbetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23137" target="_blank">📅 21:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23136">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmij3XhZs47TrPLIZco2LYSHr1xR4u5FSW-rS9Ng1iwuzmOwMAUPngkyesAcj8w4YtFqNw8DMs1LIgWTGPYVJ4cG3PxNpHfrVyVC2HhFig38TF3PfDuDkCBe_KA333yr1hyOyiZc1xwgU4duPk23-pIBsWhMMIlpeZdGjtZwU3BAXQHJqDfigMqVBra2PMNupzpHsgJ2jmWlQbaT0BVDWFzm0FBf0PRndvNiueFxWTMoyiXBBQpUzZa9WYxKSHkgDeE9jkKFPOBVhS6_sHsFszin5Bv0aFAUeSLxhprqYAedDpPLtPKPono8-W7J9SmnsL7f2Z6ydRsP7NWXhXy1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌اشتباه درطراحی نیست؛
پرچم لهستان روی پیراهن هائیتی؛درسال ۱۸۰۲ ناپلئون سربازان لهستانی رابرای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه‌ استقلال این کشور جنگیدند. پس‌از استقلال هائیتی در ۱۸۰۴ ژان ژاک‌دسالین به لهستانی‌ها تابعیت اعطا کرد. اکنون و بیش‌از ۲۰۰ سال بعد هائیتی با قرار دادن پرچم‌لهستان‌روی‌پیراهنش در جام جهانی ۲۰۲۶، یاد این دوستی تاریخی را زنده نگه می‌دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/23136" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23135">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2aARVeflnpt7xD7_eqyeIIhqGuzlHZyDRLn2IoLLZPNrsuo5hXiils-qc80246qW-GhWpkv_Xjnc5LqfoojqzvFWZIi9MrQR_vziBOR8adaQflEtkLpq78gJXxCzdyoYgRk-2hZITDEi-NGJCbCmAHzRvwLIDPd4Q7LdJYHbp-z37r6FuXWrlrgXE4fwv3WW6lddqHJFpYSGmBUPvcpqU1JwWEiuQvfcFGdUqBe0DZe77l3QLUCD_5B_r5sXGkF5PKhjif3P7GirmYg0S5mITr6wSX-Ny99hVSAM4_Ewah9GV81IgNhVYDj2KJde-n7A6AFCYb8DO9jf2U6i6-ztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23135" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23134">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpISbseG6uwieGEmI0IAeRpdvCYL3mklmookJjqxw5jUtVZeQ0P0DMsh1gQyj-8-IDxzI3PHfVDvnimEfkORdxD2WBmovTYqBqPA6PDsTBsFhBNPZwhZtu49FlJkgyqv5SXemgPK1qxaHAWaThNwidsuJhCIkuLrCAkKcDYgmPEE7fB3BLRWTohkJM8D-lWxpyQIRoKk1y4naN94SSq5Qwqt4R8YfBbUBo6D1BDNqnyLXRZFjIdIfTySBNcZNqJLPVn3qL7zZb-8X2lqpeIm4O75FXYBPdHfldFiMdey7dZkz-1iKLPEfg-xF3pudQj3bbnJWhz1aZ1v7z_3QqFPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/23134" target="_blank">📅 20:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23133">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rE8V1hLB6-GC3piF2Rq9i9L2nCsZcTyMpMQJa3HYCpea5aMlNdz-8-03xiTtO_JyY4pjNEym5T7-k2gFywZBlXryqnNNO5VNNLDNRJqIy0uQMdMhSoJy-EklcjUa28AKnNWe-dZ2bZh-iRzcJf6Z_ZxdRCNN31uWVyoa7a0aFpZf9n73O_lCzeYkwHq-hf6JIzEEiu7-M4F586DWpEcF4gnUS5vHbZ16rrlWInTALdHHyFnzbnFBkt-ISjHNYEdv8UglfB4sQQGVbU5-QQcJvYS8fpE24FZIfnssBOhFj6XUz4iWjUWV5AUFob82hpxYFMyd4qixolIw9YLUC1V9XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23133" target="_blank">📅 20:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23131">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keZqUI1Do89dJ_uJkfvBsPRWLY2qJArgivgt4SHSTai4S3b0-l64GtNVL9OG62usGe2YH7tcU7y9ghhD_i2GW9kpxO7zVdCgkAfxPAFIEvqf5ExgE1preRLNYIF4XTlNLLT107-jy6kUKF4JQhfIgjj_zuUmklqRGDEMirnKIwJB0Pcn1D2-CjG941S19cjsybAmT4Obqo49oddObIHL1Z-nuCZntZLKXE-gw86toL6zRugx1-SlalRlAHcOwaZClBN5Tae1QkpeL0h4nXYAt8hMD2Gdibq62j6E90aPjSocfxQRLb-HC74U7bobtwhzPzj2qhRLkirLvUZ_JuomSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-WrfYpMTcCOG9mIR-FfaXLWUkMP8dIfvl8IufvfIE8fQV81tExVosKcZCqUf2nRC0wVOs8-H_jNQS-GbNHpx1WXuj8j7PT8-hb7OXw5xXle8Kktph3ZnDY-FznKR6b4hMoffmQp8ijrfSqvISms2amezfe90cZM8jvL9BVqNSUX0KODLC1hywlflJB65aoS29B6W4l75_U0ztYaceTg0_FSoWFTx5u0ywZ5OoPflij_ruDjRCOGfU467FunbVLJmINPYtWAmpJIY54UlMAYs_VHQblKHP7tl7dKHddGYqi-OCASxW0PdrG3kHHckpBBd9Qd9fqLK_F-T2QM-IZrcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرخوش: تولد و بقای پنج توله یوزپلنگ در پناهگاه میاندشت‌. ‏«هلیا»، یوزپلنگ ماده‌ای است که در آخرین زایمان خود در پناهگاه حیات‌وحش میاندشت خراسان شمالی، پنج توله به دنیا آورد. طی یک سال گذشته، این مادر و توله‌هایش بارها توسط محیط‌بانان مشاهده شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23131" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23130">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=U7IsHC_u1AsPEAHkQbhcITBl3qVDuYsP9RCPFSyMEoNPSPrWslA2hNPvGTbLvXEHMcha4nb-qGkD54CC05rDWkXa16Uhmawh1xxHEHdQV30i6mdxtapYSXaW7lIzai16kHMEo8ud9qfVqcFk8BHyz9o_uHDIHmrlS-G1u1rojaayBgjMVDZZIlz9CapUlkzUNAtf5jtsWNUrp5lam1u30bmV8MGzMK5i-AQJSPe6zYTFWgDWzSDVgzmOwzbWA2F1fzY-2a7q_RQeJIvn4DDTgTvv9L4_110fKz-l33ZzWnKYJ0JwWAYLsfRerWtv58oaz-itE4Q-2CB5woo9yRrUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=U7IsHC_u1AsPEAHkQbhcITBl3qVDuYsP9RCPFSyMEoNPSPrWslA2hNPvGTbLvXEHMcha4nb-qGkD54CC05rDWkXa16Uhmawh1xxHEHdQV30i6mdxtapYSXaW7lIzai16kHMEo8ud9qfVqcFk8BHyz9o_uHDIHmrlS-G1u1rojaayBgjMVDZZIlz9CapUlkzUNAtf5jtsWNUrp5lam1u30bmV8MGzMK5i-AQJSPe6zYTFWgDWzSDVgzmOwzbWA2F1fzY-2a7q_RQeJIvn4DDTgTvv9L4_110fKz-l33ZzWnKYJ0JwWAYLsfRerWtv58oaz-itE4Q-2CB5woo9yRrUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇦🇷
حس و حالی که از آهنگ‌های تیم قلعه‌نویی و بازیکنان منتبخش و تیم ملی آرژانتین میگیرم:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23130" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23129">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJn8UyKIRy54n3hgY8coHmLVtW87xlqow3NzBkMijRUFtj6Dt3J69nbRa093IrtnLVz5QqLRscSD9C2x2FXbmkxJbiRtPoHaFaJpjEtIqeuQOG_9-2mBQGi1Vuh9TWktVCuOyZdrX9PPIUQBSPu3ItecdKkLL3bhEemFKpOVRVHWuUmg2NEuLxLOgxMOzPeATDWYFy2nwsMb5zhVGpshlUcijPTZwtjjctorAG1M9VcY-7gQL6T5v1sMkl5Myh3_7xpdoxCUzvWybHqGdd779TGR4ofdXQumzwuIK0Tjen6qrsjIUCu_O_gE0xjmWVMyDiGN-Fj6Gdn4ljvPAczqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg20
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/23129" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23128">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ-ggHNAAC4zyuMPWAuDmJCJQFvj4FoT1Jdk7HDX70HBzqiLQbHmcF_-d95hR2hatOAu-KNbmCcBvui5IKHr3eR98afp1HerdQsP01xOjPSCib7hEJ850ky97KUifrxSEnhrDIyzDibIEeKpJSohZbxEPmTynLeBy5a9CY7UVRLEGnHGiACdB2BxhrDl5xdTqwbyljwWohMLSami26ZgqUREf_jN6Ql3Kr3dZryzyrZ-7BLbL67adhb2g2DslTK7NdBqg4yOxdoSTfpWn3VyrbHnBROc2ncfLE8K7kDDp0CJJHgIl4xVjieYfOyperQ8fEiWNGpm_xI6k0-GRpTTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23128" target="_blank">📅 19:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23127">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVbcQ0nGdBSbbuYJOSoVDr9TylwJy9Mw_w_3AwA_fXsgUnKvRsZZWKS4Lot7In4QmJwNYfMVMS_KNSNipPdYtWbXh-iMzrlcg6YUoWkEwYYcM-jSxA0unppqSF-ghIlXo7wpCZ-V9ysDGenrGv9zJexo1I7LErilgTwVNvtxdzPrHzhmxpJQma4gNhqHDxY6dONaT1JhLnLSM75bkchEN3lEDeLuq_yL_BhoIPTWheSMR3WtHSfgSTWpJAeIX9BWyOv8iLBfNSS4A9t_zbuZ0fOOEtqm2V9YImgvlc119ZjOKQs3QD_Utp69PrTOaiX_lOWIKc1HS-8Ry44mUhBLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23127" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23126">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-tc1fid7QZA7WNLJ0R3_MBBbaezM0ztCbAb10Nau7z5MVEFIKMftHOQHFkWGn6M89mMxvNspecMdBK6q_VFH4PYQoSY_UvKYwDyummRpcvlzAqYYVgT5W7vJ2-x_M8B4I0teWl4gvVMhxZZ7rHEuQzLMxJ3OL_2b3SPyO30yaiT8Z3_l3vEUS3Kiq9Ax21S6uUcRZ4xj7Pjl8j9s_4SopgRIU1_AaI8m8Mwsrb6lC7WLQqtIAFsklSUIB-tgg-dufWFICAZsu6MvJj6jbjpZhaSTved0NWVpH_c-BFPWGNxUpnxc5vt5pJs1Ap_jfwnSxX8VZHShTHv21qhhylAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23126" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23124">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOkixufHAi4gRsE9yokVrcxsDU_IM1V_gteRx8EZJxAL0S24z1u-DtW0WGxM8eJb9d4SzYk9q3aRQYJLoAIhyPCacpfSm2g1ryvZZWCS9uVK753LUHDuXCPvnh0CZlqJaPop3_nS0oo-Sz2quAD0I6JfhBQSYjQ2gfKK7zcIG7LAd4_dI28-mb_DskJ9hEEnLEzHBdXBe8P4Y7MouKuBrrBDhrP5RZwZ_fgwhDohAXVYRnfX3QH8MxTXNRwCelfYQbsrOVgvrOy4rik3FLOxPWyiB_hFFFWBxXbrDIlTmO4k-Hh9JUgBCWZ9_YvsBKkxzILHxk-JISNI1UX3tPGn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aeqkWxonFAn5eypWDczGj3rcuElDpiV-3N56UIVKEppgWUGfHzlKDn-D1Ahqh7XdzPyJoUG_c_5j_-wpX5LVDDOoib7gxbjJ_BOk2gUGBkJiPVH3yVBYdFyipGfinVs7ZYif1OTkll5oCpQPWO8gXCchE5YLvVI10VmFn4gME6JXJjMiNPrBcWUCBK6V5MjvKneZGvNQANjHJsAueriYkqmrT5ym1_IZDlD29uUfpIVz4ktn_xDXRmMQn9vlCzBicyfgZMXmPTD-7aWRLWcTggXNTQEoB-hEzUM1suRRmfZ2jijQNK-LTqPzhYOSL5grdf20UGbH0pDzawHKQUIyIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23124" target="_blank">📅 16:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23123">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPvx_nKbp2P9Q9MGsJPV8hvjkvJ4Be-uiwSyApgpT4kI_EOlwKgwBPHgaAAQmkVqLYaoNGo6B_WNhV1VpWrtHdMhCSG51bIi0zHvXg2yDdCyHBNVGTMLDCMqMzvkMhWuP_hVSMo2RolvNCbEMN9qzNFm1FzTt9MO5DPcf1p1mV2a2xKaeYsG16xkCotvE9eooPH47NdPqRkTofOUb4tbYUK-YGtYHDHJ6ISL-7vbTY_xUCLhIHWHbcD14s1H0azs2qi4YvDWFKFByRjjXRL6XRLqiBIcc7VBYFG2qtnsSPeaqGG0xo5TgOwDknHprv3FtFdplkNtJi-aSU5MULA-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23123" target="_blank">📅 16:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23122">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میراث‌ترسناک‌ضدحمله‌های منچستر که بعد از یه توپ‌گیری آغاز میشه بامربیگری کریک پس از سال‌ها که توسط سر الکس فرگوسن اجرا میشد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23122" target="_blank">📅 16:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23120">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnZE6Qec2JeTp6BFB2Sh7vts2ctiTzuofh-K1Kkpb6rlBxoumPFdv5Tqb7SSFFurt_-wJBHar11k5bgSuG5XvrpJ4kyFOO2Kzo-RHImh6ZGTsD458uAceak3Xn72z57m2ZHKR3lJWWWZRtUdXqjfFUiWy-kt-BC4n1jYnxEFsb0pL95uR8WZJeNbua-4Q9HugdR1Opa7t9qZ6nBYS_v7aD9oikWWmRfVhLH_UnMNAkgfNYOgHWhGIZN4S0lvhz21DE2pf8aerzc59nf0WWs_tTYMa1IXnFYC-QkGu48E7r4esCmNvwzRtlwkMewMmn6NlFCM2obKunbyUf6Mf-hxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgEhGh4r8EQF82njjeWc_dTYSEBpr7QxfgpbI6vG6jiWCUkZ3SY2IkYvQobdoH0bSdNHF8ZSHYtV2XBX246HJfLGQgbS4TWopZVDIXlbkovSrjeZ5eq5SmALQbpX42EzNCXzDi68bLyAI-EduvDPgf7S5FzmTF5mhzSI3FJLfrfrBjGQOsv1cMeM5dnRlK1wibMaqMIjW4ES5M1tpQ_yjK3NngDqbuczDMX82iL9DoS176ovWZVSIb9FqT1nXdcdON1Qvg3cLLI9QvjA5BLQoqOq5fQCR0YvSpOHA6Of9DAYJflzDo6InX93v3sAXc5fCIYHuSNt2LLgw4anAzjc_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23120" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23119">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfN6yTPE5MWEgaj6Golc42wcTUk6w5Bcu759QnG8wdSwG0iQXUpGfgTU6bJmoR8YrVg2U-TxcP3W8nrwMAYEfAWBV0ugK7VZ6IflKvPn4odgkiAvvIq4eK0RVm-UuA9jdtZmoBugGJb00Hdu8_TTGcNMQn7JqpsAEIJu5GxCw4eDWlG68gKB-hcbplVgPvL5evbLBLN9_LSCSA1WJJ48D6TiersKrKqhXHaR9lMEpS_qu6Q8Leyrff8X8sjeTQqbZtNbvxYajFGYn2SvcpV0TmFjndJvWszUeo-WRjOeSV3_Gf17CSkLOyP9u_WAGH_vpDL0D8FSGEm5u1QZE4ikpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23119" target="_blank">📅 15:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23118">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C0uWg-WR75CbOEjoLnxSyj2oXkRoyyAk8f-xyYf4A24e9RTJ_W6GeQO-12UuK8HyRkypYVKUvyt49fEb3Hx5FxiO6gEd04xUDEd8hVHsgMfNmhy7p3RBARpVUoIGro-0z0NLLlZuvaHo2FOBjMrllcEETcY_pC8OQUtcl-jSMINcYU959nPHxXWxoOZ7q__BrrC4G8snAoZTLIWglKXcwLU2cYhkUnuscUOAMYmKnoRs1wPIqdvkPsYZdaYw9D-Omh74In0Zi_F_i3miynfFInmLWJxMF7fP4qXpwObXmeommqB2mwzvQfXXnsxVzzloKEfPzgKNyqHay-8vHgT_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
شهربرلین‌آلمان تازگی‌ها یه مکان برای شنا زده که خانوم‌ها در اون مکان حق پوشیدن سوتین ندارند! همونطوری که مردا سینه هاشون پیداست خانوما هم مجبورند بدون سوتین وارد اونجا بشن و شنا کنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23118" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23117">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nnv84wqOkAYFdNgOC2UQYf8u2ojnd4mPPbArxOK2LNf3fH6IRFacJg5k25JupKT80jt_DpfaZZPj3G9tgfUKasqAmodjUE90CHCEbERTTHzM8ISfjrPoORNDGgYvBMbZ8qbXbx08QN6GmSML-wDYSbsoeDHbwNk6H-ub6FO8MTt8L39b9-2_bbJeA24S5nND6k_XuH-cfjtEbcq_YeSBskTbAPPMCq6vdryHStnm_Tg8rXnGq--E5UcDvSlAZvo5SHFbcxeYWgxQFV4QYe2R9tSyTFbPuUMI7eXmLR3xt04nRoPaoSK2uMXldZMswDYpI21_fCcYid3MWrypcnr4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23117" target="_blank">📅 15:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23116">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMqACg9H5gcz0IdTKCbGQ2tyNjZbd2BmYJMbC5poGwv8GHARmKxsvrUwbWOMwo4CKQTmcP5eYRzuBRhd-U4jWIKLyz1gIo7vdc7xurq9OBtIkZPZC-W5zMlFQHUMr4uROgYYG_IY61eM0XhUBExqziUVofoxucGIp2BdAj_-Fhz84QvOk46D7MdR9cHwCZ1dQDfYISArav3egUpWYHufIZeBs1AQ_JrcFthjX1xf811tWqU0AH4W7bFIrjc6R-hO_IqQG80fldBr7gcNO2AV2jyyDW7TmkmAFkHIGOFn2TIRGcL1etoh0Ng-eGlQwjOAdbJoGE4inGxWhrn-Rlt8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23116" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23115">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng9ErlGwhxUjnhEJGw7IRwnF6Yx_FgiyiOfN48yspZGbiQnFUGzgT13qB5ejzoXoqDPumVMOW6nWQd5K55FuCxHsPq3YV4ZHgg3urNj5I3v69mA01DjLftD9wdJWsHx1qaW0ybRlpa-qwNjKWAtf0beDUt91t9ZIMHaTlW-hTMxUSXq0d_yFx39PMzuLBWs6hhELVwvMiHjZ-Neaok0OaGi9yEV8o1iU0RHrJxdsg3BPmjwHwV4G8b7buNK9qfT2kv1_p1-tczuTwPVmCDME8wOkRZbT71cPm4_8Izt-BgbE3xPMQFm8oAZCnFfLg5FLOs7TkBNmwnPd-kdbkjo5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23115" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23114">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUjd2hfbHJ8b7l5EGNDj-I4fLL_e-8DXnUl1LF9WIFsRGqet1WLxobKWNMmB1kbVWmc2wdFO4m3887kjVrQH9obriqkZh-6GLpRlnyR_Cmk1I1PgXkdZ9fhTxjoeJ2aowmPkGmogFqcVkcn81adPRNQ73u1z8lyM7wt3iLiwH3Q6jwihNVozjcWXBf8cSY06aN0U4wdUidTTtXdh-YLnE-NnNN5J9tBuHuCNMkAXUQpKtC87GHSKWEDlwqogqlWMoKYhWdXWn2qcfG5GKDzbQleRFAbNNhCn3AenCLVjukSj7JTMIHLtp5fDyaGxnZmOvB2j90aO2Rhr2yshfqYSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23114" target="_blank">📅 14:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=WJh_AAITxBWxxqch5PsbT_HTO076a-NvFE3Nr7fgUBBnGxLQwGXsCleW8LuBBbPhc4JJLnKznOxfcUlPmUqzAowxFqyWKNs4Q44kiK3GFbil9JoR1Gvo3V-28aQZhtggvtEY0Dwrag9v0BW72TyydTlv1aaaba25rqMa5wCb-W8VidSdrXZw8E5605fRScTco8JRqy1M7VE1pdZc07njX1yG3NGLB4jk_oaOHCfk4mVWfVRXC1WvNrh0IqY058iGW-k8CP0pidLhVsHxgU3q0UDjdNMSIws_mYwl9aExVNyInKR3xjh8TZ2LQ2SHN3OZMwGw0UQ4rGNHOe6vb0TXY4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=WJh_AAITxBWxxqch5PsbT_HTO076a-NvFE3Nr7fgUBBnGxLQwGXsCleW8LuBBbPhc4JJLnKznOxfcUlPmUqzAowxFqyWKNs4Q44kiK3GFbil9JoR1Gvo3V-28aQZhtggvtEY0Dwrag9v0BW72TyydTlv1aaaba25rqMa5wCb-W8VidSdrXZw8E5605fRScTco8JRqy1M7VE1pdZc07njX1yG3NGLB4jk_oaOHCfk4mVWfVRXC1WvNrh0IqY058iGW-k8CP0pidLhVsHxgU3q0UDjdNMSIws_mYwl9aExVNyInKR3xjh8TZ2LQ2SHN3OZMwGw0UQ4rGNHOe6vb0TXY4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اسپید یوتیوبر معروف رفته‌سرتمرین تیم برزیل؛ بهش میگن شوت بزن اگ گلش نکردی باید شنا بری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23113" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6HOawPerrZPfMTx4vYNiXTNQLK9tPKSxCcsPSdpYgA5jJDRTYGtMYxgN7GTAP_ZU7HwqZN6HHnk-HMIZ7kKz0dQcDxjXJsdZPNpPpWD1Nu5cRwC5Q7nmYjxlyz2LxNgxA249E3c_S9lhmXh7zqlsCAudaZ3QWSgxq4ZjBgH1JxwhZjKlkTOMvfcnQZqpv3wWY0Jyze2vvqWOdlRBz99aTRz2t3GKMFGFv9zP4Vdn6g4L5NgF1VL1qIw7ZgbGKxDWBHFe4WoOKxtM0My6RN_63nyJiE3FgahkGND4R7e49bxAyRZY0lhKCyLJVxs_SmrBOn44fqJXqmJh5hy18_x9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23112" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23111">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6k3-HzQ1yDJh1X1hzupuoJKY0Ka_cjUSONasUZurGvrUZuUbYKiBqRjQsk2Pvz9K9M98KVSaVtwnYDMqJb6KBbTTX9-EbfxdsBO5wjlcmepgAWAqOJE-TlgDFaScSfrH74MdjoIZFIRtI_2Y_yGYgOs2YUym_M_0sJS41WBBjggoV2ujUkWH-x4BhGFzgNsfFTuxxkM-ghVlOhXpDTgbscEbDjkKJHwwqfB_geCY53jt7lVU9_K0I8g06t1IlxJy4NVT5p-OdLbL4Vj_7u0UYHLvL9w9aEQt5oWHyLrvAM8cUwDa7FrqNbmIpuKxOhFC-ZsLE2Rn7aVO9OFAponFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23111" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23110">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=EcKm-FovBPcESmiyN1t7Ls5aN2dc9BBvRwxVk0RIg8GAsEuKdfW9HNtjmNFUTqbnGtK9bynsyCnw1F33uScfQ8YAPI02oYFyA7ZuxyhG9wAnvHtr_bYNFHD_e8QB9Zx9r7fKLrpNa3W62UI0G9Y-xJy9CXcXNVzVSlqc-2QDFO7S62NplOw0RkMkLpAt96dyX29cxbZQTdGjIktT7fpWakJzWQlZefTJzEdmAbmoWQ6-vjZfMaF7xTuJgRPxJgEsbMWHC0hx2IDUW0O_p3klX1AZCf3apZyQ8wSH72vbArU2WOxyydcxpOn_3p02V48XWzcQGchToL-N5yd0mEHAog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=EcKm-FovBPcESmiyN1t7Ls5aN2dc9BBvRwxVk0RIg8GAsEuKdfW9HNtjmNFUTqbnGtK9bynsyCnw1F33uScfQ8YAPI02oYFyA7ZuxyhG9wAnvHtr_bYNFHD_e8QB9Zx9r7fKLrpNa3W62UI0G9Y-xJy9CXcXNVzVSlqc-2QDFO7S62NplOw0RkMkLpAt96dyX29cxbZQTdGjIktT7fpWakJzWQlZefTJzEdmAbmoWQ6-vjZfMaF7xTuJgRPxJgEsbMWHC0hx2IDUW0O_p3klX1AZCf3apZyQ8wSH72vbArU2WOxyydcxpOn_3p02V48XWzcQGchToL-N5yd0mEHAog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌قلعه‌نویی‌وقتی میبینه باید مقابل دوکو،دیبروین،صلاح و مرموش کلین‌شیت کنه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23110" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23109">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcDaNK3taC1ZYNuGfuJz7M2svLFP5PqCRilzrqz9e4C4tPIk5YMQ6Ln6h_xrQJ9jdH1c9UOxN25SV6eotu3YQ6LpKV-qE0Bne3gG0vCtktl3pOK_y3ceNOLiIwkX3l1FKSc9TosXDCOtZ8uRvQSoUmZxlhxtBfdvTDq4tTGBzkVGMRoAMUj8HpFok1TO-YZyh6c_2gqnEjtvc8GYbTiIHFBc_EzeP8Qpm5K-tAuKY3H0BhxrGsgJM_c8NQjD2nFs4gB8DUzbqbHiFg34Nti_gvIfhEpcIGCuGIgOQSZFUjikN5_tYqDduu4zExiHgvHp35MT4vB809GT1m9BYMPatA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
دیمارتزیو: باشگاه رئال‌مادریدمذاکرات خود رابا باشگاه آرسنال برای‌جذب ریکاردو کالافیوری آغاز کرده. کالافیوری خودش برای عقد قرار دادی 5 ساله با کهکشانی ها با پرز به توافق نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23109" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23108">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5PupC4wtbyOz93KDI9R9jBQM17Lma7yX25I2KnpXLTD4gWJtiKRSEKLcMmVNTzPEtPUGbfYj7nsIGvYZNfG0UErY8pYY3wz4lUaP_DBbZQR5T-n4B04gxYD3SIsqlbu6woq_RzG5xe6Xtyptp97lVgiSeXGEh5-owAYRK5pIdNA0EzXfl6RsbHoiW0UtwqjacNDQDv_OsUD5x0juo8GUAzSmZ0kgoTY6ox5Ek8SVTO-koaykRYO7kU_LXmpeo8-QR1Vkzau0ryot7otttRYDRWv0H09EQcuyeZ9dVd_--0oHkB86b2oDGZCu4lpwIuPEeQ1uWkVuDJgSZpqdznBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea20
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23108" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23106">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgA9tVUqAWTQED8nnl8GI0-4j7_ardCYL8xmoD2uif902f5CEr4SYJxrLhmbPen5g_U6-Ae_HZzd_WvM8GCoUReN2VJLlNdZNxTQDUZo-ypatzGbeiNFC9p-Ietjg6hoHkuVBeqtFd0e7mz5tBZJq4lqkdER1jPT_HJ_Lpbh0n1B7RsromUaN5BtFWw_3T_XxwBDP8PP-SUxT_Utne2YBiss3xp_O3gsOMr1rE0GTVvemufWpi_wU7RPwtjlCzW6Kb802OYGB2M_0jY7D4clw-WECNK11zl26fa7tJKauJSbllXo2Sq8LYklafKkq829WuAiSVLpTbJP7BtWyfXocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23106" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23105">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb-KAK141NF6wz4xaFANOARqrfG9UNL2aS4QnOwTHcBrmJXFZeQFIPP8wqUpUvKmIbeKNvBQG-uv5wUELHcYlYi0GMuRhfFAaVYDs6MHDVRtHb3E4I2SzwzNC0d6CQ3xH7bl-izW5zFuJ-i576mWrSm4p1NVVR_wSccoa23oylCQrihHjWnwXb94g5Znm8rlgRIIJqbxQi_mR6Vy6FcnpPeG3jGXkmTS0W3HIAk97d83_8ES1TRnp1_xjBYIt-IyPG89-79wHZbZqcOLicrU8Y5LjWo-QAl6x_Y91eQQbZ10-uwp5PG-OnVNV0xZ19AbyGSWS0dXa1oX7OPKRkfuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23105" target="_blank">📅 12:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23103">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FIRdrJ844ohGOjm24hne8rR3T0i-KkLqW96Zs7hKhMkfxhHrpC6sdIGs8_BWcdXFSAY7MkyslTzYFd8XiS5Uvk6OTU_ZL3t6KcyzNTrdpQi9vhdVdwNtgFTSQnEBaNIzlm5TDfoCFD6ka3v-JIsF9acDNZgUrNDQ5nw17BkqQxibtjWmOd6xsFLT7hdaFo7UyS1MrxuUG5LIWpdslYPtOxLjL4RUNsguwPra5D0RQ8iMKx0rx8D4tjmXuWMnmEM16LSqSn_hJ3D_wD8SilQENsJhbvDnYcLV1LEC8Ee0F_jM028YdxclPTrJGREbnkh0bdSxiTEshGyE9EKUlwDPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_XKgLHrFrIp4n74INd_NnSPPhA7KvsF193JfZYUWI5ll8EGd5vZ6yBAdrr-W61Osnp-R53jsIaGfFuc9jhmT9QTuNZ9tOYxhQzlbWDJiSpgx7G_8iwTPS6OGzHZqNPpn9begY6798c3iu0dL5yaWmSuPKfPXssm5MfF2TSwrtaqlBc9Rueo0RNEy105VGeM3Pyl0v8F7oAt9OlfAFLX3e4CmrH4OpWEXXDtEwIQUvj8YjQihC3fk3LJv9gYI9cqKutTyj3TB1zMeU_7iD8Zakn2T_44E_e-IorErPokpPHiLJyNxCrHK7-11juaNHPgpxfO5sSzT-UKsoHAcIbLUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23103" target="_blank">📅 11:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23102">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmUrplKEmfmqb0Ad8u6CqgHT3QagmobxifkqTki0SP-LJgWnuSTAULDHe1cRwUS6RJL167rTpk9TeP1WSzSvqyEtW3ihNGN1kRhRSabEoGzTjdsRWzqnCgopiKexMtpc5siyfPdU8DKyzkzexVP5nlVXslrKTmcWM45cIWdWWqgh7rt7CfDYI78_5k6j7sJNWXEexe2NyA1ufe9PcXQTxqCrkkh6TbNdO-BR8xXVaITSjfS2wA8vdy7o1TbgcbhWG6Qm8wlCYbNhBa1y6BCBFSQ502b4OEvJg9213EzRb-eygqPzatE7wAnktHgs5rYR3zyIxL1Rf0APf8ZODipNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آب پاک ناصر الخلیفی مالک تیم پاری سن ژرمن روی‌دست‌مشتریان‌ویتینیا و ژائو نوس: این‌دو ستاره رو به هیچ باشگاهی با هیچ رقمی نخواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23102" target="_blank">📅 10:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23101">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuaPs5k84dIraFb3Oog_kUB9DeCgcs8qIC9fXG9dvloADfMOy9RpmYCZ9P8JYQS7ZYfza932Y8-LKcjZCkO628L4GJGlpjg0_089sqJXvQwFk16lKl0LbN8GVBHTFPMy2d8q2ydVG6WlyISb2PvhWPH335dINzq1yvI_hRI_9z_anqw5tLo3eoidur8Iw9t2GY9R1eW2mlACuJ2fG_i-DBSHuuK_7lX2s8qZa3ovp78TFiONkoXuZMbqwyRKW_KKGZpXaZV3C8JRVWS7Eu7o2KC_FI6JoNDparPIHozusawxSaMUyL8tA5UQq09i4xXJ0kJizcuMeE8W0h97xy1tFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل گرا مدافع‌تیم‌پرسپولیس با دریافت چهارمین کارت زرد خود، دیدار مقابل ذوب‌آهن را از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23101" target="_blank">📅 10:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23100">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=OTIwkwDvfVzr_ci_6k5w70bTFy4XvLwqoZecxh5ZbwXO6i0fHl1hwx2bjRyq8DOhbhNu6Ol20Z5lyN5sw6tfUHJ9J2vRAr3vvwBXxo3tp6nq4NBDLtJXGsBDf6aH51ZZzKd7ID71rP4DbDLJ3T7BrsqTayRrrep17eaJY8A056G_6dQ4NbLbhs_RKa3tcF5rAB5BxQ4feKB7uwKRaPWwecPaRC8wSLreWzFWPC7vh7J0td_Sylkm4DBByGDukgrEi2smmlDfa41g7m1bgWWtzr1BO-Du-c63_ifqwcfyxAu7GeJOlKslymHKsyLcu0UP3wcesHIc_SNbmy49pB2G3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=OTIwkwDvfVzr_ci_6k5w70bTFy4XvLwqoZecxh5ZbwXO6i0fHl1hwx2bjRyq8DOhbhNu6Ol20Z5lyN5sw6tfUHJ9J2vRAr3vvwBXxo3tp6nq4NBDLtJXGsBDf6aH51ZZzKd7ID71rP4DbDLJ3T7BrsqTayRrrep17eaJY8A056G_6dQ4NbLbhs_RKa3tcF5rAB5BxQ4feKB7uwKRaPWwecPaRC8wSLreWzFWPC7vh7J0td_Sylkm4DBByGDukgrEi2smmlDfa41g7m1bgWWtzr1BO-Du-c63_ifqwcfyxAu7GeJOlKslymHKsyLcu0UP3wcesHIc_SNbmy49pB2G3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
درجام‌جهانی 2018، آلمان، مدافع عنوان قهرمانی داشت درآستانه حذف قرارمیگرفت و در حالی که 10 نفره بودن کروس دردقیقه 95 این شاهکارو خلق کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23100" target="_blank">📅 10:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23099">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇧🇷
👤
به‌مناسبت‌بازگشت نیمار به تیم ملی برزیل؛
ویدیویی ببینید از شاهکار‌های دیدنی او در سلسائو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23099" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23098">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Al8o1Mo9M_vCcm25OvoH2JpZYD3gcrvuWDmY2SwPOYWd_2OFbj3kPWcY3i_84bffdviLXEVe10H7tXUJe8kxwEcJBu0CaYxM-YWmYcoofZKrLANR6SJNvZ4vIcfr77NFUAjpEVORQQ08_xPSGneXVZFZ-ckI6ZcZTwAVL_yqmq4jKVkEvCCQk8coWQQYWKihqKl_Or68xp0XMyn8NW0TW46PZHkS019VHvVPfRbBmfI5bSJ5i3AjCtYvNuYI9aWtHkhtmMUBlRnwGNHfuxEYjD95adQHQBh2mrG4-y5PhgU3TZoyDslfZd1pUrH-s-LRPH4hzsbbKIWkuGKqwhJy_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی جوایز تیم‌ های ملی در رقابت‌‌ های جام جهانی 2026؛ قهرمان 50 میلیون دلار میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23098" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23097">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhCDgghX02TipGZq8C4pppozAYUD2y5XysEXtzFqTIXo_Y9sdbDBdzU-ktie_m2OuxFhm4JoFI9nmmiJcQu_B7Qu1nIDNVe0IBcMcsnZkgfNLkJrAUcrZhUb-DHs8Dkb84aa54hlDcmCX0w3TKJUPK3IZp_YbJx8kwdcR7BNsinmSMtZY8YHSAp3HfYJAfHjyIXPuzKnQTImOMKlKLGtmX_t8amduHzNS3Vm2ocnJjnVMUD9WLX5WwGKvppojtPLEZAKgCQ1B3qbde5X92Nd3GOG6K6h_ZC6-qNCPj-8zk2lLOT95YyAo4aGvnJHcEALUmo4C8eSw7wTK9UKt-KesA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان:
بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23097" target="_blank">📅 09:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23096">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=hjgrcyhqy_Qxwebh_IspN9nQhD95PzauOArKajYaNusSQV998pUaZ1WFs3yuo2ao_6D5JAaE13scvfQ9YAllfIsYGOpOyrFP4OH3S-fFv7YpEWLn2w1Nb1C8v-_1B5UQZqkLTxCW0JwG1314Ezy2ro1Fl2SQIiR84j8-xKYPhJGKeYiACi_dkvG_J4pqKG3A4Uw07ti3jeG3soX8QYvpkUgq0wqZsgMETIHI40mLpDwt5IgFdkf2D3eJOlo9dh1yz_L96EvT8BQmTx28S2lf7BkzoLVT2NfB6VFAVOiWstEeeNYRxPxNYvApWHbecvo25f3IdxOV1Om1yHf4KRlsVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=hjgrcyhqy_Qxwebh_IspN9nQhD95PzauOArKajYaNusSQV998pUaZ1WFs3yuo2ao_6D5JAaE13scvfQ9YAllfIsYGOpOyrFP4OH3S-fFv7YpEWLn2w1Nb1C8v-_1B5UQZqkLTxCW0JwG1314Ezy2ro1Fl2SQIiR84j8-xKYPhJGKeYiACi_dkvG_J4pqKG3A4Uw07ti3jeG3soX8QYvpkUgq0wqZsgMETIHI40mLpDwt5IgFdkf2D3eJOlo9dh1yz_L96EvT8BQmTx28S2lf7BkzoLVT2NfB6VFAVOiWstEeeNYRxPxNYvApWHbecvo25f3IdxOV1Om1yHf4KRlsVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23096" target="_blank">📅 09:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23095">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=kJvDjboav21X6qRkv3IBFH6gEiub4JESa8NjgnIhfg7YrhXeHo0euWJhFYCd0Bfd1J2Auv6AxtZ2uyAZ543uZpK-iiK33CI3CVkJHPtVNNP8452TpCR5wGaCU3PtvtWpkVxLrLrpy1vLQHJVKko24JUJW8bE5m4BEHg4kBWgb70N_q9arfec338ZWYrnTL_Ib46TQKCCWwDIzwF3lat7y7jKUSMfGI5mg9ZuUu5Ad2ot7wNZOzN0BsuBPz4GojHie7FLxJOi31lwzLibMyBm7QJdOtFC4kTgDoNfPTpUAefuTSEnShTJhdigK5-AFH67VOeMZMQTd5P_FA-dhMfmFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=kJvDjboav21X6qRkv3IBFH6gEiub4JESa8NjgnIhfg7YrhXeHo0euWJhFYCd0Bfd1J2Auv6AxtZ2uyAZ543uZpK-iiK33CI3CVkJHPtVNNP8452TpCR5wGaCU3PtvtWpkVxLrLrpy1vLQHJVKko24JUJW8bE5m4BEHg4kBWgb70N_q9arfec338ZWYrnTL_Ib46TQKCCWwDIzwF3lat7y7jKUSMfGI5mg9ZuUu5Ad2ot7wNZOzN0BsuBPz4GojHie7FLxJOi31lwzLibMyBm7QJdOtFC4kTgDoNfPTpUAefuTSEnShTJhdigK5-AFH67VOeMZMQTd5P_FA-dhMfmFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحنه‌ هایی دیگر از موزیک ویدئو شیدا مقصود لو همسر ایرانی خوزه مورایس برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23095" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23092">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jH6wYkL7mA1f-f4w3sr8gbXRPoVqil333QEAOHGhwHB-IfBDILK5c6ZpZEpK0iTWxBKp0sl74bzfjmxvI7T40t5Jo7an1GEZRzobyVCdJTwAChspbsl3Qa_jBLqFKpTTgzyV48gARUt1uqSuTNlYNkvAvXAQnv0kgfj9bK2z0HuMs1dMeb6gih6KWb5L3kpE0-V5QzArvWlCqDbeSvMn8H8P2RaBZ--t-oWLc_tIwbpx9gVbpk_4KLaL6Hz5TWycbsVJILZh6E99PNzYfHuctXAoqiHTIlYDB32DOEDsYygjfaVpPD2dXSd7XEN44fzDd8J58-ER0LdlRJ4uctUAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltcnUofEIt1WW5gqWPEUl2oGcWoyHGIpR9q0VD0EPP2rn5vOgY9JQzk4_GFewC2KSMz84GOFEZx3pSz7YjTOYx8ipkoDTvnymzC5WIv2ulO8RPqGy8_MBP_HyhdAdAfrkBA__x1-bM6k8B2GKjqSv795OAvKEiphngaUl2xTk7g20KWf1ZFCB8r0z9LZg3aTfAJnKnHUzScN7ghsvbParrxp0buFKt4NlvTKjjo2HoHZQEJJsuVuwZafDU4AoSfiE1iHUIH5UiW1wMkIhPWDCHuYznQ4RtIsr-Ihn2y0F1rw_BhNu8Y3AXuzntrQWBvozpLs9UqnjSi7eGKiBVxzlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه تک دیدار دوستانه مهم روز گذشته + برنامه مهم ترین دیدار های دوستانه امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23092" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23091">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=TCR_GnN3mmkqgrw_Yfc88WdotH0B0_7G0CLAQ2I-P9M5JnT1MlD8BNl1jI38ySWq68Msi0Gqci9ElD6881S3rCN3D1yPuecnHZb11auEJhFFufuFqjpUKmPhNAatw8Z0frEmv-2G9RObfNY-PAdDJFoMiTTfjzeG4qclXh9FBO1GqOqScIKnF5_f7tUuJ-X8w0EX1p21Q5fA-Yh4PUaYdCNku9P46_oYaAb6l7mHdsjz58N9TrYTdwo7MO5Ryb2aU-6sNAjatY1dZbYMqcsvu83NHDTfmp6szfxv3G7aNq3dQXUe3mbPxUVmNlaHy_rz4BzFJwZDvpZNec_KKaSv0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=TCR_GnN3mmkqgrw_Yfc88WdotH0B0_7G0CLAQ2I-P9M5JnT1MlD8BNl1jI38ySWq68Msi0Gqci9ElD6881S3rCN3D1yPuecnHZb11auEJhFFufuFqjpUKmPhNAatw8Z0frEmv-2G9RObfNY-PAdDJFoMiTTfjzeG4qclXh9FBO1GqOqScIKnF5_f7tUuJ-X8w0EX1p21Q5fA-Yh4PUaYdCNku9P46_oYaAb6l7mHdsjz58N9TrYTdwo7MO5Ryb2aU-6sNAjatY1dZbYMqcsvu83NHDTfmp6szfxv3G7aNq3dQXUe3mbPxUVmNlaHy_rz4BzFJwZDvpZNec_KKaSv0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23091" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23089">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmekaT-ybnTzU9v8DyzfOcOvDjHyK2WxvXbr3t2RHppWXrECqyX_IH2iOrWdIxTYk5Mgp0UvIGLNQF8S9TxzexqlG7Nmyt5JDvtypHyalPNzh2-0u3jCESOUFXfXHAWgjvAZpIyc3tO_5Y2lZ85qAaLjw61GVrrCMhC1z5ppa0SNTRnafhwNOyR77opChUDito_diFvo3YJUBOO1vM9uxjE4WD6Vshlgo2ruky4YsC5h4xlMYhbWRb_gEGUK_xzR0veghHQj1vsuMQDKlpafDpjlgyNyLyt-3b7K4-5x5BQxlxu2oEPWFHLfgNOZD__DFiQmwIqOhcaWAp8a60DcvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CU24yN-H_D3DMxmSVvFAWYgc4ZkCOKopb7wXwBD1gBDCDRLerv0_CLT6oo6RYM4mprXcH1d96S69bADSquPkbaMchPMrOAsWrpi8fCn7bs7cO8-eAB_fraF9lMu6ve9llA3VYjfjgJ2NrxlL40Ms0zVyyiVP6DwDxqb8hiKrAfL4zmkikU6ucs_AaC396imCw7TqmfJRQrEsSkuina-PW_e3TQ_TtVAMGLaJzlVZ7X5-Ay_KwCzejaWerCnG16kmX4voCu0ASqG0WPAuULfYNydmNvzysGIn2LmTHbhGK2Bfo2K-KCBmhjIocaAt98UUlEmnNrVFM1UmIQ3vHRUcxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌باشگاه‌های‌برتر لیگ قهرمانان آسیا بر اساس آخرین امتیازات کسب شده در 10 سال اخیر + پر افتخار ترین‌ تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23089" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb4SUO0aFETIc2XASfkQvORnxx5AJsyLb90dTknfDpiuEr_xpMSpMYNUCCkfATsfWstn8PdyGGDDaBbGOSw761GdjpqGB572Lj_5RmBzxy0q-6futrHPuUVZYtett0QRWzhWtqIOsbtws4Yz0x0oTF2uJwi4y-pwbMg1Uo6Z71Rap0DSg-l9kbaiL_aw-nU16E4Bq-f2eBaQqcSqZib0mTFMh6qZxBMx4zd8eg7U6AHFYac1YiK4MEVMF4QH9KZit50dhEnGdwqiyQtWjgi4SV1A0pmMF6ph7Xk9H2iEayXzTTgBTEnx4M0_YMtsYRKuiUWS8MYLU7TLBoL8L60_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23088" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23087">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5366993444.mp4?token=Py-wmZTjsselFu18CvgxaFahp12Iq8jWncJiZTw4apPSuvehaIwvGEnYsgxwAHY0kRrxbSf7JkR_02cxDHQTCZi5XwlP7uxdNic7YsdIVpWMZeZqZio21nOlNXtl8KcX7JKyAEb1kokzlO4foH5--_d6-HiTtQU4vzNaQrOkEcrYSRp1PQTvUxZUe-JsjVt9zATt2_17WcpAayhHgtO7c3Td-ROeWGc496IKs0LPIAGtYoL_cmKSqo9n6495nhUKgZn4a9iqsHiGOlioKPPYKGmF0TOQoEJlK65OlCm1n5ZWoxbkjEI29Q516lvr27Marsq-DvjedEvayPxr0WJ-Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5366993444.mp4?token=Py-wmZTjsselFu18CvgxaFahp12Iq8jWncJiZTw4apPSuvehaIwvGEnYsgxwAHY0kRrxbSf7JkR_02cxDHQTCZi5XwlP7uxdNic7YsdIVpWMZeZqZio21nOlNXtl8KcX7JKyAEb1kokzlO4foH5--_d6-HiTtQU4vzNaQrOkEcrYSRp1PQTvUxZUe-JsjVt9zATt2_17WcpAayhHgtO7c3Td-ROeWGc496IKs0LPIAGtYoL_cmKSqo9n6495nhUKgZn4a9iqsHiGOlioKPPYKGmF0TOQoEJlK65OlCm1n5ZWoxbkjEI29Q516lvr27Marsq-DvjedEvayPxr0WJ-Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
جام‌جهانی‌داره شروع میشه اما همچنان با بزرگ‌ ترین غایب رقابت‌ ها؛ تیم‌ ایتالیا با شکست در مرحله پلی‌‌آف مقدماتی جام‌جهانی ۲۰۲۶، برای سومین دوره متوالی حذف شد و در این تورنمنت حضور نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23087" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIzV-jkTFqFzqtMgu0G1yNb8gZSffyYP9ehOcEK19f7BoNKNzNPTe7fls8MZ_0Z_G4e5eU1g3VkGOsgzxBJyzc9XMOTAHy9I-1bGbZDYaXFeJNEn81BmzZfHFtZHxua7Pwfn9rhurxl5eeIkKFuXAs3YkoWIVCvFL5MAiUD2m7xE1rQl0Q9m8MolHHl7q_-bIbrsX1_OlEYG5ahYOnnOiLYZpTrGxXoqsQI2LR4x8SFZ1fKU7DmcMZ3PkV40X8q0QcEmA-CL7hWl6VxoRKpEP56C3y3cGTzt-juuXIpNYR-K_UI8QZfoeVrBLCD418n74AkXaDfgAEfggEJQJZJUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصطفی پوردهقان، نماینده مجلس: بعد از رفع فیلتر شدن واتساپ و یوتیوب؛ ما سراغ سایر پلتفرم های فضای مجازی خواهیم رفت. رفع فیلتر شدن اینستاگرام و تلگرام نیز جز برنامه های مجلسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23085" target="_blank">📅 00:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cyu2zoNryJXFWDN-S19U63k4U6jXHpv_4fnLuk56cPA_tWKBPcUNmu63Gh4nviy0Iq5BL93lG5K0kaIylPkd6edgTtkAX2TRSiBvf9gYwRTYF8ygvOg9jNLDgs5Kw000itgWk7k-SkTdsuKE6mUfqlYPlzzMhyP_upxfWQpJcsbNWPK34Y0ighAP9j4wGCYSvEoGxW4yYsuAb4OXbcUdFIw3tv1O5Lky0356yL9vNgdpmL8p3XV9ZdrnnYsLhWp3J44zo5OZwghW010Mr_uT-FCjlCLuYPfpDiqzZpWn2KyUlBR2UJfTS6QtWMEZhYyciZHzlfYTdCvmVYxzFAJu6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
🤩
#تکمیلی؛ نشریه کوپه: پرونده پیوستن خولیان الوارز به رئال‌مادرید بعداز رد شدن آفر 150 میلیون‌یورویی کهکشانی‌ها توسط اتلتیکو بسته شد. حالا بارسا مصمم‌تر از همیشه به دنبال جذب آلوارزه. الوارز بارها به مدیران باشگاه اتلتیکو مادرید اعلام کرده علاقه‌ای به ماندن…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23084" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiQyrwgCzFDp4oum_ivI_NgUzPbFuRDPGRYY7EJujUWSgPgjqs26mPvknzHW2whtaHhh3Vs2equEM4g6vFkbpyIerYfc2WpumAUwXS18-Qh2GUR-SPf7_EwQ-aXHS0VhNdlDQGnJ1ESynU0tsWYw6L-32tenv-pF5xMlw4bcdYTMaCTLBt6u5og94RXryq41HjBSZGcdDC9vfRzdyEXr4RjkX9i9ekf7LWsRbeo9XayhAFPh4iD5Y_fOZEqbG9wwUqfJLckqwzVAS3I4lUXH_CRyTEPtsWhvXIysLK1Hiwnc5M7IInTiFXb1-asT5UuKXmR2NVPXJPUHjOl_te0cHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ لازم به گفتنه که نماینده و مدیربرنامه های آریا یوسفی و محمد مهدی محبی ستاره سابق سپاهان و فعلی اتحاد کلبا امارات یک نفر است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23083" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzC0bUKP8as8RMJBeGpPbBOm7y3QY4GytXU1pQjXEN39KmzWrKlkS0Txf4cRPaQpTlQ2eyIOKCWoYvTenk4Ud-3_HRoPZN-82ntYkTbRkaBetDCYjGTR49bYFAEWJNz6lJ2-swN_N7F5hh7vQM3139XA7CNq0V6t8SJHWMGCfb1ZowsxH7FXTdELCgrg1xNI9hIlYYuL2JXN3wHXd5u2Eb_ZZ2iq3nHBb1rP5RchcorRFWGxZXxjN9AMwpF_AFOugSNv2BsNs4lYL8xMfB5DdBDXMM-OvL1O4m73YMP-4v8-b5seaUHlc6JkZpF0i6z46KoZetydF61sSBkEyY7hIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23081" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drTWsbev-y6C7y8FgPIFxlg4guTPNVqgHOtY_07c4OxlrlDNCJTJk6bx2mMMEeCwq80LKgelkKLJZBjhvbiCBcmzooMLKEoYTmMYU_9uAQpoah8uLdxfKd1HrBx8Kin0seE9snwHez6I-yT3_Oya_Ou4LtjLnyshyFQLF3HQ9qwwxrHz77uFKIYJdThuVgoVOnmLX2VGG9WEq-dSKAVg8gYlFdINZLy7GueHDL_cb4unG_v-qD3dEXBq1jSfW_xAHDCl-8QRd6BzEmKdGj-wE33U7FW0R705C9g4rd8aLHt0F79xIao2LcwUXZJL8rGgGFkhPt4pldmgW7N2GJySsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق‌اخباردریافتی‌رسانه پرشیانا؛ مدیربرنامه های آریا یوسفی امروز عصر جلسه‌ای دو ساعته با پیمان‌حدادی مدیرعامل باشگاه پرسپولیس داشته تا شرایط جذب این بازیکن رو برسی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23080" target="_blank">📅 22:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HiugJfy8kjNDoPUj6uEjVA48yRz_Ywwz17jf6STBnFbdrSb7cBmWIIKfJ7yyUIW_2zkWBlgSHFp_66xDfgdCuVklhPEngb_MTQhp40wFFz6Uas_bpOMKh00jhvkQ-frzjJpGMvqgcMoFX_VUtZmIO6fw_ponMHgqOSMnemuqaq_lGZ6MmHWdgQsmJT7OUPHYYioMc7HPLq1Z9N1Mt8WnhNTRxLL7lRPoID7SWpQ6NgHLihYOu8zordC8kvWufCy7Lqe8xo72IhPAF5rRJ0Qeyp9Yutq7QIM6dMzNf2ug6kT2TBbjm8lh_Ct5zmAHtcBuRdZk6I3n1umZKBjE3zc0xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-miN9tC5VXsJKhD_JC9UZFbCgvLIRKtG0GoX5frm8ZgWQn3UaZrvJuhdLwfw7LIqm5FFdyE_aSMdyS88mypSlKTV8eExDFMY8sEtbrwSAZcUNBqfwJsR0oh0xXTJ0JJPT677iBrpFeclshLn0zpwqj2MnkFFeiXkO2l3FYjYC9xpKTyQXj1cy_jvZPdU5qmvhSm9IdGzHN2AQJSOmfD3HOtw8_zjmdHhrjqnkemv2qjV3HtV1kedWzFevZbwE_qixPNt4D3Popfcq3sRgI496DQIYCoUZp67pbWkdewN_SO0fT0Wa9EPr7aauuI1CzFD5LqlsV1rUUuVoTOgZRR_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
نادیا خمز دختر پاکو خمز اسپانیایی: علی رغم‌علاقه‌ام به تیم‌ملی‌اسپانیا؛ اما بخاطر اینکه کریس رونالدو رو به شدت دوست دارم امیدوارم پرتغال قهرمان جام جهانی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23078" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw8fJleftauuIlH5SVZz609aFa9HFGl5hlcFr-CfnL1_8e5j-eZhXHOU5foRUNE6HErk2RPpcEYhGh-7yKYMExu1AWSfEYUJXLA5JjyLcVXhuHwkQUJlV8BEkupTbG__VW-Wm5vmA-cunmDik-INucDSHwQQMiFSte119vGOZliaTfaMg8FpwyRdQE1ID5C8OHdbaT_0AZGCJ2EDKE4YBVKyMQegesPJsIQLG7YM-obMmhhJhBhFtuLcVzny5s1RDq9rDlsof00Inu2_l6GiV6ihDHAqQQeWW7rJkz6RVrRHxbNgFRhTTYvQfBqHO07Nh3iiyeUXqVw_mjxJ0Q_tWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Povn39pzwpwG2OwVt_3cTcvwbgi223BVqfACtPfyO92y2bCFn_J_auZMkb-7mwjgAQfxABFz7uQDR2tcopCgTK1hzAHMCl16pHwYmjvSj_c_XRZANRgqwBAyPLnIfrkEEwViPoG87IsDNOF0YSnzk25cWMjbWzZS-2gXAOl7_8_B9BBvWcLfUZyzvChWxYU-w2fiZSAwTBP7wjhi-3aELvA-rlugyuwkc1l-Vryddd3hg9Nl2NsRTb3spXhFl-_LE7EG73fxeUCGsetgHlZ6exrw_eu8j01nxg8StfmO7uVqdukh-Tw0lTAgkLUo0V7f_daMX1u9T5iHNp4vuiv0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23075">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twis_mncqaatHH7mvHYmpTBmsJFG0VJF-koZDdoIK08LS5zwwTu9aN_61yci-LxB50aKaX_oQphj6FbRiSsjOCT-_h2njlG6qMA7RfR7KGfAgtwWMcCLnLmv96QvrmDq-DgJlneoVV_VN_XhS1OPJVyeqRjvAleyy2leM4njIrhMtNhqPXpk50oFZ33zdugJlj0cszuXD-t-5vZ2dCHDh-684dmr2Wc0jEWPrrZwV7MvtNDKkBk58Nr_po2_GvkiGBiGx9iKBv1l7TwbNlcOKcaMjnW6VUMlKz9yCXMoak7FRqXykQ_Zegw9xRb6Po0yTNMHpAl4YfcLf-8iviwXKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتوجه به اینکه هوا داره روز به روز گرم و گرم تر میشه این جند مورد رو سعی کنید رعایت کنید تا همیشه خوش‌بو و تمیز باشید. در کنار اخبار فوتبالی چیزایی که بدونم مفیده رو براتون مبزارم
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srfqQMpjos09bGPgdOC0YvtOONQDMCTGfVq04FpVrFaVsSbJT6NnwEVGWn_x-N7P_WVgU-ZYrdipYHseI7xyAwcyxnFQ8FZRQtAlMCy_CSTCrhBHtRrJiXAvyUVG6mKOJnnObDekbQsRKQuHC39Bmbg1LpQfNakYHmyEMCOTLserVPPJTVeYVvtgRiW_6ms_S8E9mlS-pYtSVCuyuiM658Y-naNzSCwHfzgrP7OH4JO0AGsnjeeD2gzFb0-DN7rvKz8z8Ik8JOYDgpcwX4cpHCnDzTDyW0ro3GZi4MGsGuvfLFPbP16LDPvmoELGOWEQyYfXC1WAAKjqtppJfZf5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23074" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23073">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC4NmbtB6Olsw3q8d-umqXQ5c0iehr-otlwrq8FsWls1z6GryhXBrUz5FaloPeP2Kjw41ydlwbHDnRgO37YioIHCIplkKmLbvG8IxQiHozeymfkfjqiLIHX3_xa1VgVtgew6-KNzgSHfVoqBXlcZFv6KnZD_-XBvIff7p7oYixjq50n2corMwFM0Eky_e3PfR6mEDyew-ganaKsM2qwBeHSYAieVTCbf7unh_goOIvaoMjxK_0bwUplLDWblxGBdcMqletN5teJMke37WXQ42eY7fAG6aJwnHtn6x_deddMNgTNDMQBAIkPI0dk-hloLJf_82VBTrzfp32jaMLTuSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23073" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGuT-gjbYtrUhdf0ynQlol5oRaG6h8ys2S5G-O4Otq3Agk8NG3W-ECH5Vc2g89oflaLxGRO1S30-LrLa7w0YPPwL5PGiD-toqzdtbNDydByzrOpl2AyLwj1-M-hmz8PdSCmU03zJ7-prI6qhXxZRMGt0-vD3jWaK1Ah1ZpIAB1hlpl1rIR4xMzbb21L6u0X2PhRbxFg1EFlWo0fqTXmh2vYdzrqWCCVa4Vd4ctV9KH5Do4491a42ItVhxZxfxAi5_UqH0Ek76RtpBsPZlQJaRiibksMjxQG90XXJQl_YVq2niQw_YjKkjvdxhwfzJgO4_7GSwBG42jPw1Syes_3riw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
7 زوج‌برادر درجام‌جهانی2026؛ دراین‌دوره جام جهانی 7 جفت برادر درتیم‌های‌مختلف حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23072" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=XQawrV6JV27qv7w8tACMdbX67jAA4gRvgD7IFM8QETYW1T4TaylRMRA77WCwUm8thakY_7U2tPiAILT-jyWM3LLDFeP_zO5vLeIFTDZjHJ2VY4MpH8tT-Za8G1Cqm0wq4dAADUszPo4TLdCbzu3FzL6k8JCP2Le7oBDJ8UhqSacu_NwybhznbvjWK5UA5zp8iF_HBgfmoarhPS2qYXrExLmDsZTsiLswyODNoHkjxzDrVBJZOqyqUYN8e0IlV90rhQmwV3X1NXiB_poPog48zFqLawzVwvvI9geNoYsNZGDdUmez0Zhr3RyPxlctHFb8jfLqHJiNthse9REXZTWvXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=XQawrV6JV27qv7w8tACMdbX67jAA4gRvgD7IFM8QETYW1T4TaylRMRA77WCwUm8thakY_7U2tPiAILT-jyWM3LLDFeP_zO5vLeIFTDZjHJ2VY4MpH8tT-Za8G1Cqm0wq4dAADUszPo4TLdCbzu3FzL6k8JCP2Le7oBDJ8UhqSacu_NwybhznbvjWK5UA5zp8iF_HBgfmoarhPS2qYXrExLmDsZTsiLswyODNoHkjxzDrVBJZOqyqUYN8e0IlV90rhQmwV3X1NXiB_poPog48zFqLawzVwvvI9geNoYsNZGDdUmez0Zhr3RyPxlctHFb8jfLqHJiNthse9REXZTWvXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سوپرگل استثنایی کریس رونالدو به الخلیج بعنوان بهترین‌گل‌این‌فصل لیگ‌عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23071" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byntlRZ1bhreBVT0EHSa6Ayi9XrHzdUIwPZY-O9_AsSevN1xlcgtISNhbqmzeioNjpRuQzo-AvVkVThWi2tjShwGeD-JndSrKNth7mTu1lAQrDRzg3OyQf-ehr9C6RyMoHM4-f5y47D-ByXieT9o9UoOndx_pbeI7zx8uPAXTTPTGiaVElAvc9PEm7uPjLjfnMIzkDsj1b5SRKBW1bvU30UwiMTWSfqb5pnbRWZ6xijFWuVyrAnX9EbX9Wtl5nl7d9VUu2CkOa3UBvTIf3EKXt2XUp49GC-ZHsd3D_XGjOh2d2ciK3TdSsvSSfVaZ29eNVfGWF9cdRrzUHwbvzSyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: برناردو سیلوا ستاره‌پرتغالی به یک باره‌نظرش رو تغییر داده و حالا هم میخواد برای انتخاب باشگاه بعدیش تا بعداز جام‌جهانی صبر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23070" target="_blank">📅 19:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=rHKbDR5bLe1A7OAq2IrQ2rPUujETJVclxPLw7AcCrlCKtiVFZ3vCe6Sp65-yoO1HxKM6PD9KsUQ6tamSwEbBnPiCNtpTF5ttGDk4lunvrE7LQ_HeHsSPZeGbrAGGTU3fVZGUAF3UfBnjZUrCDE_rLnh_vq1Vus4_jINqOdjpNzXtGo8wUSBRB0XVQ_Js1-ZWyoECpoG2B2idxPwcfZ94zjFBFdYxKcD4njGaghC1cmNikwxc6CYzz6uODa4lsyP8QR-Mdn4O9AxH2eTfR9e5QzFViI9lNL-JdksJhYj7her5d6r4yP5KVw-sJ4k1tCCKpkwWxV_SE139C1su7M6Tzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=rHKbDR5bLe1A7OAq2IrQ2rPUujETJVclxPLw7AcCrlCKtiVFZ3vCe6Sp65-yoO1HxKM6PD9KsUQ6tamSwEbBnPiCNtpTF5ttGDk4lunvrE7LQ_HeHsSPZeGbrAGGTU3fVZGUAF3UfBnjZUrCDE_rLnh_vq1Vus4_jINqOdjpNzXtGo8wUSBRB0XVQ_Js1-ZWyoECpoG2B2idxPwcfZ94zjFBFdYxKcD4njGaghC1cmNikwxc6CYzz6uODa4lsyP8QR-Mdn4O9AxH2eTfR9e5QzFViI9lNL-JdksJhYj7her5d6r4yP5KVw-sJ4k1tCCKpkwWxV_SE139C1su7M6Tzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ؛ مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBlXF_VVZDg13LphI9gNLyIYkgQQT1On1JejBFUBUavr7laguGksI2V7D0cgqZOARQw2LhBVzZm_OiJq9b4GkgeznyxyjFZICWeY46vxagFU7c_tYRvKoOcDWCm1X_rsSjmomZ9DX14-meodvnZ14O0fCDiEQeGqOKeJsAw5_iAbMhI6SeMuiTt3Za0hc_01r7Zgs3MzXPJqd2KPihV95Pr8KznqFpLo5icUiWCLjnUPlvjVPwdviO6xnWvVEwxjCUb4FIB-FIJXJ_72zThKLl3gk9ooOuDr7W1PqGIKItriTmBvTvkNVBP6cqrvJHrXPI-uZu25MtCTkSMdzdTpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا: فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzzifVvIsBLbO3DbZ5X8UYUOx2ZWRA0sqRGpmRjs0_1zJuNZRX1dM6JZhNGuvGIdLGKs06J55Y5GcmWoorP5PeWuI2QINbHoKuhfxVCd8xk15hqZ7GhkU8VXudZRhU0DgzGyQZk54ORBBVqU2miQ1on4QBY4ErRzw0kUIhEgfJ3eoYEnMy0oudBoraN4q3UqltbLBeM7-C5XWBqpfo6BbTyTJwOmH-P8sOSSBRB3Htz_NDTH77FRnCVOX_c9IIiSvVwjwnXi8TxasQAULc546bmnaowXKz9xL1BBKqU5t-1v_qGpG9SlWOEoimYHlkROD2irjv2JgYi82-zs7BOHyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
با اعلام حجت کریمی عضو هیات رئیسه فدراسیون فوتبال: تا آخرخرداد اگه استیناف نتیجه ۳ صفر به سود گلگهر رو تایید کنه گل گهر مستقیم میره سطح دو. اگه تایید نشد، ۵ تیر پرسپولیس با چادرملو بازی میکنه برندشون با گل گهر، ۱۰ تیر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0V_0xI93N_Hb0mLIwAb48NH4VC6fAfsasiOSBS5gsDtFGYvAiueSI5ArW9Em5tnpqwCdNEoDIB5Y90rAcNRwaMDPpDzyKYg4dwx6hSehQFmnC5PHsgHnir_3RPEVEfU1_LtQWwmIhq4rRG2AG_SyBbg4wLg0syvb3n73F1rv2RUlc85uGlMIidJIbbugab7IoveKMRMUKsJonkqnq3_OnwhA32VD6XokfRl_dO8drgJWp1NxtcRdphOjHgewUwDAWu95aqhteQzjqW8MYqeMLa8k5-aF7fzctssF1gxiXnFrep0Ed46R4upcnKVwyWjznq5XS6OksMybQdrIa2eqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siQls7LdKbRL8fEl401g3yiw0xy6m_yq8Mr9gLTkkN-dHm2cIUssl-bjfwz6G3T-0ZrskSzK7lIjHFJKhgOFr1UPsu8-Z0LqrF41GkPWtCZLftJ3bOS6_EMJr6zpVzAThrNoDVqUqOmQ1wrr1K_UnS6pkhMkRnDo3iBgWqLMK7avFpRmZjCiC5aQaAGNljAzk208AYLoRtR9ZUDT7qZtgYSYmkc-EFXa9l9irWtiEjssk9ZSgXM7nzaDIdVYipwqo4PHyelzj4S5Vz0_9zLf_y2KQ4EVpo9vVwpLboqBLh_UzL_5SlRr7V8IqmzC4Dg0Ga-OagoTt0pnKorrtAsDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_JAp2dmqffNU8hKiO8pPotreN3Tx8-FpqRj1e54KGORJqWYamIQ3o7oD1DD3p9RsLbZJccmRbxsbHR1fywpzzsk0uXnzfUlPQ3iv7NV32dtzwQ5CcdSDd6Sd5PhZHztsWk7JHbodW6nawDHEyRTACIEaKUDwaZUh5kLXt2KX8IGkAZA9Ch6BqTORJ6yf0fYBjyUy6ZaNqkwczsaBMdN-np22HZwKgNMus_xlVYVEam-Mz-CPFNTv2QQWmQ6ppA5MsC-gbJ9tr3lqkCTCS6NYXiV9MtDkDOMw2lFmtWcRhTeNk70oCwY6tED64xiK-Cycd4yTKet8y4MQsy0WxLQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9vAzGJeeKcUwO70F0u8ssjJbP6vl3kmXWYCE2e95jF7vtFg9YlEQormm4Rq6QbbSFUP7yazkkbiMEvCfmGuAMewyh-JW32d577mRIk8Y3OIRjLU5tkbXzQ2VUc0Y-G5m81aZyZlesjVsMzvw29nyE5VdIuc9DKZt6PTSQ3MfC-xPYs-UYZ_oLb25nXrHAIdO9lP9rGefPKn9wzaWwBaDh-utAVLGWNmWVm-aeKUJx1xjcDEpus26B1sstBzBZKvryuj2pUTJmys9R3oxDlEMVjsY6R3r8XkQt2h248hoyLwCoDRRuZZ-9Jne8UJxKtN5_MRcO1Ygadt5HtN7zd2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49850c982.mp4?token=u1F3rlTBjdd-YfWsSPPR3uoX4XznU58kX81WbvQiks5KZTvcSPAuRZFRiZg14Y5gus1dIyInjBlALowWKfomntP-3TzOXxPyLpUTlzD3jx4cvUM5W_kHEmsbZrmVbnD8WIG7Z1NH5cG6xqWu2SPZgy4RBt5Xqs-O0s7cw3atXSYwXb3Yju-cUU4h53EPfZbAEbLSjmjWeGkKqBoJxJkMnvEM8i_zTtqH8e2fKVcL9qj7rYOmt8dznvtYU9zTr3njnkGFB-iey51aAPMKkkAPdKaMi6xqJK3AwAdrSLmfdk-aXVZea9_pxWVVRediT-ITOihMmKr6vCKT3qrQlOX5EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49850c982.mp4?token=u1F3rlTBjdd-YfWsSPPR3uoX4XznU58kX81WbvQiks5KZTvcSPAuRZFRiZg14Y5gus1dIyInjBlALowWKfomntP-3TzOXxPyLpUTlzD3jx4cvUM5W_kHEmsbZrmVbnD8WIG7Z1NH5cG6xqWu2SPZgy4RBt5Xqs-O0s7cw3atXSYwXb3Yju-cUU4h53EPfZbAEbLSjmjWeGkKqBoJxJkMnvEM8i_zTtqH8e2fKVcL9qj7rYOmt8dznvtYU9zTr3njnkGFB-iey51aAPMKkkAPdKaMi6xqJK3AwAdrSLmfdk-aXVZea9_pxWVVRediT-ITOihMmKr6vCKT3qrQlOX5EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇧🇪
کم‌ ترین انتظاری که هوادارای رئال مادرید از دروازه‌بان‌‌ تیم‌شون یعنی تیبو کورتوا 34 ساله دارند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23061" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3RXdcfdXjosPtLlwM1yEocz8elU1AVNRNUsPI4aHpA5hNB2Z7pgskoyvj98YbKTVd7vf3Ai1n-aP9tqFasZoY0Wf5tS_jJWvSS8vbQNHixTwLFoTtbbBhaANAwsH6LQIiPwySMOzaHHtOSLh8HejTpUQSfxhvcUIkwRSTIXm3-nDQktQJp2e7zKwZQyIzkkr9P0jLFgkjhqpJjMrxXo5ePP4fD7oJ2Q9jHnn-2Da0aE7D5Z2XLkd8zxFAWchA5FCmsbS1mkynReN32HDnQq0oD0i9kMaRLqt95mvCPRSEpt3RATcy33eyU4Qi__2dXFBfhVWoJ6Q0H3uLp-_qRpgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lm-mbI3zHytKp8nNm89UbbISKFTB0IdKSWLFbte_yzbkMZ9aq36c3aPFuuGpaiEB3fRPwmxZ6aORUm2QqfOamccDuuxIiphHGEXg_hebcpv5K7e6Wh7g7GEQCN3_RFZPC8MTswmEOAcqPkeWypBOnM28kvhWg0i8zlVYqYpRZhS_M7z6DjaOTdpk3-x5ecMI1PffkGxJcpfzgEs37Uaz6uEtjxvnEtyNYu7TWSF1PcRqjus6ce3BcQzlQcx148SW36ael25w4vwvIIrSE2602uvqGKNVruFv6n_b_KHl7cDeaHlaKry8Ot3I8doce3An_8DHashr_4_SbXQqfCdXgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نادیا خمز دختر خانوم پاکو سرمربی‌سابق تراکتور: از وصل شدن اینترنت مردم ایران بسیار خوشحالم. بسیاری از فالورهای من‌ایرانی هستند و در این مدت متوجه‌شدم که به اینترنت‌دسترسی ندارند. پدرم یک سال درایران بود که از مردم‌خوب ایران به نیکی یاد میکنه. برای همشون آرزوی…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23059" target="_blank">📅 17:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYLzoTorVxk0vSdtQTl2OhKTimDKdsept2fJ9odlPL0NSegMpw8ofKhjkpfp9YAayhqgJJCfLusGgETspyDqExMDJqAfSzWS8LDOu69_99_HKXWBAYYwI0yg2MAAwMlZbweBkyjgajbKBa3GqdTiIddBBTNardoS1ByxS0gP_tz1uRC74jzc5eHj2WzDygu9JD8EeIeX6C0GjbPrHdZCoH7yu6z8z6FXxdnEzq3n0bifvu20gf6YawG_VrCuCpLf4oRKdBewFyc4gnMqsiQdEJjBJvOcDruWxnXh3bpcD7os5Cw1zwhZg55Q_8X-YQnNvQbzwb7olJQkUJoDp6Z5pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23058" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsI15Ewjc-jEPbztrb2GZZYbISdzcDTlJrMdV278f8IwTF3-VgWtK15tYxhUscf1IGwEdXVLj_t0ApkS5oqG5fJmiL9sKawMpHVaNrjMIo2Hk0NsZkv9F6t5jNZDgJpVAto-mVnOeXUtu70Pc_gJcNHv6Sg2agXaMk2PCK9MFEefcTEqu2LuTHNzJS17biGTEbVLSh8W-vPEssBL6f63Vd7NDgxgdGu88iFLuFZvEMgB6vzoj5teKSTEHWTJcsK2KSpgBEnqu7R4Arn63LQaXwOSxWWnnmA2aHcFSRDS2FWiilRjDRY-DVHbLTkL9cS5DLyAM7F353ll0YkcZh6qhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بمناسبت شروع تورنمت داغ جام 2026؛ سریع ترین گل‌ها ور تاریخ این رقابت‌ها رو مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23057" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI18TgoZzudgx9gTFJAW29l0zf2bgLX-B3hHdFCUQS3As3FZfUnAxAGisho7VwaLK0oQvfCIG8BbV-v6wLmPwwYMDh1VH-Mfz-AChOkNBvbAeKTGi2VNxYBXJ7V88g5tUO-Rj4cgrmMold9dmsBm0YcRgPfSWLwgm4TxBbJBmxHjRZhGwMByM8uvf84QeZQPKqFtjfrWWh3wPilztvfuq0PTl6Uc445BcwlzSP4DHyeyQ3Slu2D5XhxENbwt1O6hw6diLJ2fSDxKZ5X5Xex7Y8CgS0fW4733yWWo8v7wkh5Io2-f50gihLujV1Y_zSakYgbpyevlDjiAcaWvzVkJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGSaVLoJdCML5FIK55BazbULeF7U1DimiBI6mJu-f3xvNsgdhHIUENOh_WytzHeTbaeAjAYYadOzmWNL20kHGDQSgI9T0UwFWOo_mwvWl3gQ2TKjWa3QhcQSO9ZOEMJ5a00DLVsTCzhDvHQgTxBhRr9EvKuz_0pbUVcdn1bRZb60dOE__S_WZIKguhu-2Ik7dZx4BxqtzWxGNoif2ierTQgz5UlttZM4T_zhroExyuOE4IlLr_Odj29fBDMEtjAAuFiQcWVJlP7QEOAI2YOFvKCRDGlSwCSqTSr6z4Z_B6st5C1kZZ5HukKC1plyRq9vNf3msF4q8NSsKVaGzEHLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOHAOhzSmwsfh6KEu6AcurCB4H8Czz4MiT53xdPhVltEx1O_4NQU35ikNm7FtNTJTDeRZMsvvV3ubpyH1bJoA3WkimgNrTdbQYWhn6lYtM3NOvmGi5nxHs6SVeeM12k-qM6wH3emu_CF1RNW1YqFovVM88Jk9ocEfTmCJ3W1Wf8jBxfTA1Xba2AkQUaVzfczwjivheqUDzaJryA3gjeSXNB6j3UGdulcL76lnHCiWBtmMmIgyDx1PrRuZqDoLmTQ0ii68Pd8W3R5xSfzLllXY29vwEa5eX_O8MTsCQje-gNojUjBuN3qo9ASCleKq4GSWn7rA6IAoOH-aSu3Q9hmQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=dyJjPq8LcoFeqPpeDi4yyI4oEjaj5bI9HuJzfoo9qXHbLweJHbwCg9s7Gay3tMTxUpPs24WwMbn8L9DH7O3xRjkpjBO6I4ShvXjK930UZ_VuqCOkXyq4CnNi1peZDAguHmOFsZbJNotqG5aNdCISZOA5PX4WZXx_pWYF2KNh-_MA5T6WWS9xm3Sm-1mkeX4slhrR2BJfATxnLABWLo1Z44TQxa32XcVv3XMe5uhmDEUxF98N5N8faC3-nW14Oz69sZhdAn-cFsvPSaSrjGN3x691obKMvIGyeoMauKxOtvWVz-pb1eRwfm-w_LDYq0s2AF3FD-mjYPG5h8bseEeJ64j_8A1OK9O68bvt9yw0bf8K_8F3w8ruhMVsGIAIYAtCH4z5vin0JaPFeqTONmNSucEtrUvHBn-kL6UrtVHbYaIgSjBgEqYTGOdvtWfBMrYGGdb50G3h5dnl4XbEqencGuHidfM8m_k2RF62tnA1WX-xAAYNsztNRGk0N9PhI94DrK_SUfcYwIV7a9k7wD5ZkMCU9KwfzIjtHJRxxmdWbw0ECsmPmt1BCWpLlnxoHGeEY56MSfPOP8vUxV_HZapaaGYku-AdUDPZCfVYpAY5gzCSsPGLJrKZ39lDl-W80W42_J7bmxAKmHTG7w8vwZInu_Auox5UfaitCmy9iOtCvGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=dyJjPq8LcoFeqPpeDi4yyI4oEjaj5bI9HuJzfoo9qXHbLweJHbwCg9s7Gay3tMTxUpPs24WwMbn8L9DH7O3xRjkpjBO6I4ShvXjK930UZ_VuqCOkXyq4CnNi1peZDAguHmOFsZbJNotqG5aNdCISZOA5PX4WZXx_pWYF2KNh-_MA5T6WWS9xm3Sm-1mkeX4slhrR2BJfATxnLABWLo1Z44TQxa32XcVv3XMe5uhmDEUxF98N5N8faC3-nW14Oz69sZhdAn-cFsvPSaSrjGN3x691obKMvIGyeoMauKxOtvWVz-pb1eRwfm-w_LDYq0s2AF3FD-mjYPG5h8bseEeJ64j_8A1OK9O68bvt9yw0bf8K_8F3w8ruhMVsGIAIYAtCH4z5vin0JaPFeqTONmNSucEtrUvHBn-kL6UrtVHbYaIgSjBgEqYTGOdvtWfBMrYGGdb50G3h5dnl4XbEqencGuHidfM8m_k2RF62tnA1WX-xAAYNsztNRGk0N9PhI94DrK_SUfcYwIV7a9k7wD5ZkMCU9KwfzIjtHJRxxmdWbw0ECsmPmt1BCWpLlnxoHGeEY56MSfPOP8vUxV_HZapaaGYku-AdUDPZCfVYpAY5gzCSsPGLJrKZ39lDl-W80W42_J7bmxAKmHTG7w8vwZInu_Auox5UfaitCmy9iOtCvGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9agMLMtKtbbfsqvYU6EFbNM-GDVbJjxFnS3YygbnoYP1jKOsIDch-YWgOzByqqBx4r4YHh_ZTcJvHf_ek1yIDzymEZ2F-b13CeMtixh9XUYmp7px5-pPiOK7a4mBKxDt77XbYap3X8wuKKvdlEjYiZvwPwVRq5PyeF0n99jM0j44hr3mbl6CiRgM_BGb7vIoTRJhM2lFliNRRl1YksNPRfjUVdEC23iQpELB1NPiOKMsEjgx6WHY13-cBjAV4zYtHZ4mRqhwDnplYDzcfYjACQE2sKIZVfKRZwCmxNdPySZ0l9BeTex66o5oPCQ-f3ONkzvGYN3GuPENHEU8UTorA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=FsypW4BYp4vlM-rYs0lVj9dvXlid6Z-xaIlzlEUx1ZS08NriXLlPJeroCXAXiFrJq-wPSBdJUHvJcJRigpYgepETvkxBhtwlJHxA6RZSORf4KngaLDQkcBRDkHyrmauLvKQHxsGAf50eYbtjTXDTrKlLlS7xVEg37d9ukrrhMeXT9_cpN0-KEsvpxMlw96-PNhJgPpmSJkwKED0e88gJQ28BTTxf2Q3t60dfOJp6CSgFj4fhk27RuSQhiFIhAyPkyv7MW0daa9g6jf9SIrr1_3VKZqIwrBlHOi2hFonC-YNNP6UdYdtYyktJBCS_fP4IdjXi726Uq8MX191g5EwKGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=FsypW4BYp4vlM-rYs0lVj9dvXlid6Z-xaIlzlEUx1ZS08NriXLlPJeroCXAXiFrJq-wPSBdJUHvJcJRigpYgepETvkxBhtwlJHxA6RZSORf4KngaLDQkcBRDkHyrmauLvKQHxsGAf50eYbtjTXDTrKlLlS7xVEg37d9ukrrhMeXT9_cpN0-KEsvpxMlw96-PNhJgPpmSJkwKED0e88gJQ28BTTxf2Q3t60dfOJp6CSgFj4fhk27RuSQhiFIhAyPkyv7MW0daa9g6jf9SIrr1_3VKZqIwrBlHOi2hFonC-YNNP6UdYdtYyktJBCS_fP4IdjXi726Uq8MX191g5EwKGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
تیم برزیل در جام جهانی ۲۰۲۶ با هدایت کارلو آنچلوتی و باترکیبی‌ازستارگان‌باسابقه و جوان، فقط با هدف پایان دادن به انتظار ۲۴ ساله برای ششمین قهرمانی‌جهان‌واردمسابقات شده. اندریک قبل از آغاز ماجراجویی‌هاش در اروپا، تمام دوران رشد و شهرت اولیه‌شو درکشور برزیل و بویژه در باشگاه پالمیراس سپری کرد. اون با درخشش در فوتبال برزیل به یک پدیده جهانی تبدیل شد. رسانه‌ها هم سر شوخی رو باهاش باز کردن و روز تولدش رو با پله که اونم ۲۱ جولای بود و ۱۷۳ سانت قد داشت مقایسه میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23050" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23049">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htCnhfuvctuLQ52zg7UATeTYXTm12gSS75pxTsYVtfRfkck0hQQm60zLGFkfjmIu0Q3DA64rV3eXWygBfpi9RQO2BD1GdB-t7ycVyr99WAWDmMS--ivVR3DkfjBS6Vjwz2BXLGuPgoDlR_qru60JA7Zhy2WKD_RQmdk8JUgIJKVx7pg1apBDaH53pj-H31hA7I265H3H1D-Tmo-JhKYi6Jw9KBmKgMZOFolsTXVUCmz_OWKvKZY6oyRBUREtvAgdZTFUkILBKg0c6ZZ14rOVGBiLkLJjrF3kCaAklqsfgYJg5XJZkTBttwzsv9qwNgZBSBPjyQHRpSDREzpC_TKMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23049" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23048">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meGeauY143l8WlMgI2i_rOuxQk8pfWtcV1diIjhTLiB8SbP-QrjRbMFQ_RKRlhN3txsFgcGETRR4_gGbpM2OTY0EINP9Ua4QsZ4pAwHgBr7uhE7WX63OgpttYx4hrgS558O6nLhW94zJNgyz7kG0xPGc5bYNcDeBy2WHeWZVo7RzaX9bQNBiKyV94kbTiT8r5MOcVtltZKINhoRbPy0lY_NqcArr1OxfGmJWauJwpi15t1veDM1RkMbYWMZlVBPeBBrZxYnB0s6IP9XHLBlKiwV0ffTXQ_y3_lUrEAXeEKLmwxSG8X-TeJ_dHQQETIDToJqs10B2FssGs9slPol4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23048" target="_blank">📅 14:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4akx278CcPFi3gC1UojXZruBev8Ae4G2RHKYMxnXtHHLiEDvEnnApVnGa1NogDansQwII15Mm7cj2vYR9OpYr37jSrIdNriho6WZGVwf2rp2D8XLM99xCie4-GVZesPgGVCkW04T_rdbmX2-wm9-kEHFmPKmRgPTYQCMZ26KV1DlI0wfrEF8LKBRVONi16-BN6DJtVscn-iJD-zWmZjQ6fNMPAY0eLePUeRTqvkIVpJcRmZ-fLTx3aVoJXn1_xgfw15G8XSgnyk0LaXkIxh-pEVW3bzKrXE_2lDJtz0zpghviRy8JjfDEqGOf2ORhoE1URSo4Bwy9eEM2x3UJVd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHkRImnFoKurp7_C-rxlMjWoOyUscwuuL39X6lhzk0z6a9-Vo1JFG13V3y5gyudEn9_LP6jFUdTBoaGXREQEC5MBHxRb9svgEwLtwjje2Qr9-78nVbmqJ-5-wjwbx59_nM-AGDdfVnEtBqhvN-J7WndPof7DGoTyYa7tiDnMKAIv2LNp3nC9e_iztNdaXpMT1zMJJogIpoGQVkFRdhR8oGc-zkYEsHd0rpidNUT54W1I29lkgHkoEmjUkc5aJaWUaE0WzoRbJw0IYcNpXyZk46LS108YaVMtkIkzF_P6dwNtsO8JuAAekV_oNBrFxhaj8Ef0Xc_DdfS3S9Y40BrHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=kQt9lHwWVuCzlD3NbX_qA2NechGJGVbDnF0XQWa43WVCXn6kF0zcsLwFdIeu1pY-S3gBwl9ZtCKEEyyX7s-NbVlfn7RzVbf6HlgUBHCp9HvFORohlXtapy9VwlhZem5QNc34l_aU0Y80EZIt-Y7tcSZ3C--fuDd7bAQkboggjhB6j-weUuTLV4semlS5w9WumOFfKwKt6geZH8kuVHyh2Y2PVBzIjKr3AtWtPyH1JMTYouSGdcGn7QFPPP3D6dQ5uitnXQ_D1Bm2fh2TzJEn3L1ObQPiuQ0SKaBuPgMxY3zK7IegzG9ah0FSCCAlfGoLHj-eFafwibcVxL15WY_Uqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=kQt9lHwWVuCzlD3NbX_qA2NechGJGVbDnF0XQWa43WVCXn6kF0zcsLwFdIeu1pY-S3gBwl9ZtCKEEyyX7s-NbVlfn7RzVbf6HlgUBHCp9HvFORohlXtapy9VwlhZem5QNc34l_aU0Y80EZIt-Y7tcSZ3C--fuDd7bAQkboggjhB6j-weUuTLV4semlS5w9WumOFfKwKt6geZH8kuVHyh2Y2PVBzIjKr3AtWtPyH1JMTYouSGdcGn7QFPPP3D6dQ5uitnXQ_D1Bm2fh2TzJEn3L1ObQPiuQ0SKaBuPgMxY3zK7IegzG9ah0FSCCAlfGoLHj-eFafwibcVxL15WY_Uqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
انتخاب آنتونیو رودیگر و لروی سانه بین کریس رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLW2nBxlp_T-8_zXK3HxzbA5PAu-kf9NJfHwYq-LqYnlz0IvvpqiHw23Y3KLYJEMYdxl0bs8_NZ7ZWKenzvzZMBHHjIfEAsQcon1fjh1n86Gx2f_nQGl9SkAiPGzWzvesyzeSYhVQlk27Okf9SdNMlPm-l18HUtr7VLz_8AjM5PDtKvOue2H66deWk6ZV489vJODBslZodfLAYIFcFaH1vGZjUF7zIx8a-RRimmlIhuLH2PzFuvXbN9xwllGdNYCEVdGsdueHERvxBCZnUtaG6mp_s7uXQnsq8HZxMZcoNck0IssCjBDJwIeIGE_Jk6uFzLNXEXwkqW_FrgGB0O-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb-XTD6Gzm_I4IkM7FRXW1FG9buQg5wxsrO2kqbGmIa3i8DxdFz_fLIPOsd8FEMi0_3g8hkBP8lcQFjXtjPFUQ2dG8JYvafdAHiRKmEWeX3rjlw0lILRaTxndpl7PxnlkYI5wKpLBb6ILBbFsZbGT37eBPlCAtUBfuqIUK9rO8comLmYeZf40RtDTojESdoKT1Ngy0W07rh4kkVqY9P7b1xuvpQneGMx_oTGapl4Dvg4nCSFEpezhBGVQChsgwgZRchJUleNwIUY6xBJPVjWH3M0HyvdD-p29zduEldax5iXWz28huxG7-MxfIToA672GPiIUWk5zNxJJzQ2iwJcXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23043" target="_blank">📅 12:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP-VRSUNYlL1eCgv-kKGKlsc8weBdZRFUgbrq-bKNMqE3C09A64PHtqsAB_WL9TT6KRA4qjfQhpdwJoZi7XR38vgomHYChAXRzjl9oFMfdRI9BZ5MUd8JlgUh0tNeZMvFu__L8Tftat2FvJQzsipt2rZn7n9fg4nLRgwXHRzGE1nFK4fi8E3gkYc_C2TBQFR1USJczvWtSLmQVSx0FVJ-_tB8shb575yevjESaBSX3tq8Ejm1uCWm70Ou7UbWa8h6Sr_eFRAy6PaBm11TTSKm0SjzqGTTnePjcbZ0TjEQaRh67trjVaJBB5Hf0s4jzNvxsT94t6SC0cgup6Dd6wudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23042" target="_blank">📅 12:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtqAeyBivVrP3ECUGMS9e6kkC2UIdObO2k8kXuseP2Ki0uMUhJb-5RySHDsUigLtiUadz5jyoGcZuvlE4uB2uIYgE8MKZzbWdFHttnlYLQd-VrAE7BJggYekKZKQ8iIqR3LgcxkcvcA1DDF4o7Qbl1y2uRGXyY1jEoS1t8FKpugkKUQfzaQhi9H1GMFoqcCzgrETwiZPSc2jkYZ-n0fS0cHMqkQnVv-uVRUE9uApjo0ii5fCTJKEZRtZ-tBD4oLInyZCiW9J5CGbBBl_SK0zm_UzveBq3ZvXZ7EnQH9rEPHh2QdzELHevoOREbC4cvnaKYxjI7EjTLZzemyucIOW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23041" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23040">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gh23odSsSZqFqzXRPKGCKRA0sh5hHS1FtDhtxgMzJpjOdYwV12XEphSlGYOL_IbquWwHSEaXhcd67IGm5nGAnfwXI255mxAgFJ_ebI3Q_FpPusVk_yjbkGDqn-PXhYr527hSrs3oa6W52mZEn18oH5GQTRFb8MBmStnyPJGNtz5dBTKPbuPG9swCmiOnbzpPwLGM-ZKS8u-7Zg3a7HaX9PI-xBqIJU_v9REsNPUtK6n3oIS7zW853dMu5OOCh_d4b0NGMJBerc5PcHq6gqmmjIScj58GHkY6jSzEYjUqvb_dYBkd0Q4WifBx237YSm9cl2oWDRA-7NUCvoziL9B9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ ایجنت کسری طاهری به مدیران باشگاه روبین‌کازان‌اعلام‌کرده که این بازیکن برنامه‌ای برای بازگشت به لیگ روسیه نداره و قصد داره ادامه فوتبالش رو در لیگ برتر بگذرونه. باشگاه روسی‌ هم اعلام کرده هرباشگاهی یک‌میلیون دلار پرداخت کنه رضایت نامه طاهری رو…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23040" target="_blank">📅 12:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4860b42130.mp4?token=iZpvMqghg7wPQA0rNRP4OEMvhgqJrDYXKAyl0eO-KTe9zRF2oC0ZonoF5oSl-URFNc3E1DXJs5AF1-R2W0kBV0NowqMbriVFcGpv8CqFVbf7huaojIhFAua6jK__uXljHHJ-ZrvxXx2KJPbkOUfZAUD3VmGD5DRvcRTz-d81rHyLg1OsFXegsILTT3q50TqGeNHQUgPjsLatsVESSIjZ0XhGkVvgo0PE5gN9I1RNgxtQa_zQ0ibZDSfXS6yaihMuA7El4kLudJhPplhdsKafSoBjKCLvzOUXvkH1wGVHUXM1siuxjEclW67Ba0kk0li2eSxzglvDcMmG34VLO-prMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4860b42130.mp4?token=iZpvMqghg7wPQA0rNRP4OEMvhgqJrDYXKAyl0eO-KTe9zRF2oC0ZonoF5oSl-URFNc3E1DXJs5AF1-R2W0kBV0NowqMbriVFcGpv8CqFVbf7huaojIhFAua6jK__uXljHHJ-ZrvxXx2KJPbkOUfZAUD3VmGD5DRvcRTz-d81rHyLg1OsFXegsILTT3q50TqGeNHQUgPjsLatsVESSIjZ0XhGkVvgo0PE5gN9I1RNgxtQa_zQ0ibZDSfXS6yaihMuA7El4kLudJhPplhdsKafSoBjKCLvzOUXvkH1wGVHUXM1siuxjEclW67Ba0kk0li2eSxzglvDcMmG34VLO-prMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویژه برنامه جام جهانی با گذر زمان؛
از عادل به یک مجری وسطی بازی بدرد نخور رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23039" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njQ-y646Y6wYu5re72wXZF2iGxgoP-Mre4b-Uuf1poejSmhdqwR8q7vqM0pu7WTl3lrlH_OoaUOgESht0i2XetSq9uyMBTv-lPO7yXwjq6JKKMqIoN22x_lBr2uZnd6zx0dr-ZuI9FWqTkkJGnY663ZeZ52eWAWHaMrQE6EYg_9NKBa-3Hi_aE2MLtLCvnA858SAhKL5ZGAJsvobQ8-EBxW1ws22QgEbuFnBqcdkHqYaLYewENq_JwGbR0LUJ7TiBqitbaDnqizH9Ci1728he0BCe50Ug-VPyKU4wyAopEPMF_eFcnA5VfmF9v86IkrmTGF_U8DWvyc6hEk0EYvtAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم‌های ملی رکوردار بیشترین تعداد پیروزی در تاریخ رقابت های جام جهانی؛ برزیل در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23038" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnMFpHoMarghco-Wj7UgFLkzWXSI-_9WmgpVR1yRLQt0WlZhLm-wkpscm8bHxIV1z3P-qawDNdC_5eUaaeTPFMsi81N8iee_IQNvFGTL5tsemHLUvPGM6FT1MqpgXI08BTtDkIpVQFKwUryYsH0OV6rXih0D6_YrlTja5MR0u5q7-IyZvFoE8sOehJjFYl-sYIUFg1Yl71vWbK98xjjebJ8pLbpAhZRbIznxGa7bdcFLYCPLpb9iDiOZowm3jtYkS735Ggu09BU_HTJUevtEK05JsqiT-VF8JhY2_6ch_1UZtyDQeYXCLmKiwuvvNvGL-Mesr1TEy55XIxh3F41v8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23036" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCqLHgxyKBoW-24Xt-TVbqW7isUkbwD92RYEqLbpS_J5wB1OaA3-aT_GWycsKWGnNX-uQY3pMs4qfTFvoL1MHoN4vJH3MlZXvvuWh8G0msBPnJYyWpi7AG2cCqQQCtYVs-vpUXYDHMGaNtadZ_xb9TUPGnWw5Elgsnz9mqL9bR1uIJbDYZ7Qdm56V2ZmpvCahjKK9EzLgYKV62ALJXeWTPrm__UF0GSrEMEzv08MSjnRXHEEsYxLTd9KjGkqz06Nnbd8K2ukoqYTuRyDJFB7aHFKaVNQPPKXv9_RnbwwkFEAv-q-Ow0HlMeN-ZEB4UuvVZzwAHjqQtk55Dinw3zPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AN-6571r-T4O8BndyQFbXLypS-spJAZBP6KCEUVa-dwQeSVrz2YwkBnEals7aks3eOff29Bq873f_EYIhNNhoLGPF0gLR74uL9dz9yQgTmDGvAZkKh-4aKOul0pcXlNMhn5G2rcEnsH8kGnZ-OmHMMP_hKP9GZmNXpAxDmcZnrMYHe00_s2-_dc-8OEn40Gmk_kPfmhNtvePOAlwYufmvrnpEKg77E6XttEDn0hmsPhNNdx1aTEgYEUtD5e8aAO6OPsxz4nHiiFCAQMpTzb6JqmM4RsgmFAWPSJsH5ug7iq0edmujLwc4Y1gvXetRPl2p7z7o1Dycd3-HBMHNA3U3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WV6yITzBU5Yn74h7DYg1F651CigcW-UbSiebN8zZTQ0NVoHviAzNmHRC2B0kFWb5blFk5p-GxRJ6BZCOHBhh4QOQOLB24wstdVJKx3deX3vv77a1ehSU_CnZtTcY75rEwvdgug45l8cjTj7gms3hj363ELazPFTGkbopH3uaF8r8hwB1ZjvmPKtUA_O1uCQV_b0lslYvX7aw3XDZdfCrbdPQzN5dnfCw-NWXbwaQkcgPj5r51yjH7F7VfNx5G3vqRQYyHNEGOphXNrXe9Ca6URcApS9LFFvqGW7ueDAzFKPBeJJAT0IOQVs6tiIq_k4kPFxRR6lxBhT3P4b5N5zoGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJQeT3xSHzex2VTaaqa5m3lawxkTWaf8_UFxBiXuN2Ws7LNhjm9WHurBGXMR_6sa2uRQ0Mnd3XtR1wKiwLNFS3IkUmyv3zVZIurHda9Gw7UyytTB5H3BehyPtMUsAHGyU_ze6zakO07vnJ2x4bR8bmYPHVz5RsoCAFAzvTlH9yupSGHmQ_Dp_09yKdby9ssWf7Pq8JSjC-BvCItmlV7d1QPkruz5DvE6VuSHgno94XURwgUwi9WszqyhEJGe9jlVXBBKWgOa9FwZf-GXewNpwbUELp_6jhLEkviMupydFIiZ2DuBB77jq3ENIM4Mu28kX6TM-LMIH5YPO5ud7br8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-NfVQAE62LuvgONppySyQhii9v5xXvQ0zDzHJI1E5g49JeXYgvCO4RUuU6Q0aJ2FQBSaC-xbM1LixOF46dNoVFq89VREyDTqaRqjLZTPKdQvvErOGNxgIxqvaSHZGktapob_hY-7x3LmLWnfPAqz-olLDB19guO6pWJjhK7zyRzb-j2cF-OTfgXQZrS1DxWl040RQBZZiQRoS0LSFo1pCkXlM5w5WP1WlM-d_4aKnqQ2dx5yzj-Xv7xkdsw0eroPq-lSSBrQxhBIjtElCusmlwerL0QTLiO1-hI0M79Fo5zKRdjyMJYWicVQQJhSk9cQSJCv1t127Nc1Zx6GTPjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnrcMCFeSfFWTSnKWGGMU9APyoST616cgG2roYH1JtzMBJkZKkvdGL4yZep-X1-2Tdz0mT-p_udiLyuTVzzoFXbWHygnJ2lnISQNM73nfViQ13avRquR16OkAYdhQqQgog5_FooGefdOqvs6KUOzYf8KJl99CVG1u-AmEGRkl67cUkRuDDWSyp_YJwj2Tfbntbr1HYzxHkDVriTKJfTyyPhWuaQx24QRry2wEY_6g8KJqbqHsKnM68B1ezNQq-t5ZyRAL90WxGESHXg1YVwAjPdicEKPDE207yz9KCKIOssEuPu4zucqbAl82KDTQ89gxAOft4Lx7nrR1VRlbU5rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
