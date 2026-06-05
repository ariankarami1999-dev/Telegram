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
<img src="https://cdn4.telesco.pe/file/azJYVzDI5kLT4r27UEBmCaLniOZTvgoIfPljZygJCDJpsdHju-13ZvX42akG-74Acv2F8rhHxbtXJFUNFmZxMNDAdiUPBKqwaDF8GyAaF-GYEf5jeDBAeEGSxhm3ZtmMOCb7jpCamN9fKIL9zukcVgs9-fL7GLsNTxpABJJJNgJLW4cXBJfpxuTuIfIQw9i4zYqNC7O60mcL_Jz4FQnP_OPYmfW6yFHFDVQyacd2A5y1MViMs1XKaw_wq2vD9kuwJPyd3LZfwNcg-4iYsvtXiFojgU_DUmCDFW76pdfVHNtG_79mZcZIXVNiDoXxjWX8iyH7nOcV4ciwik0Ij0Bc1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 15:12:48</div>
<hr>

<div class="tg-post" id="msg-77083">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ايران تطلق صواريخ تحذيرية من طائرات مسيرة على مدمرات أمريكية</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/77083" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77082">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31294dea6.mp4?token=Ts9ZpjVdkfLDLXMd1dTma4DU-NwIt8c4iECrcpTMzKV9-HOTsppOrENb_BWh4z6wqcDtv-kob9a1dmZ4jbFm4kLEgwscr6o8pb0C9Jea_OcJypIr8afTkKDIrTU76Fwo5nTROFDrgdsVBv-HVYDE_5jJbyfaMGimmhE_ymA1Sa0giRBbmCGjiqd_8xQ2vbv1AGutiKtDxmLlwFBkQpWKt7Fp2MOv-XeA1Pw_gIEscRULJJgzdLM2DAYPMKXoGsyZEfwW7Lyb8Vcw0upU7b3neQgstBPotVsx9GoHVLhl4zZhTehIBH1xfdQ62imNnMeqVTl-3lfoyFe1fEbFzo-Cjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31294dea6.mp4?token=Ts9ZpjVdkfLDLXMd1dTma4DU-NwIt8c4iECrcpTMzKV9-HOTsppOrENb_BWh4z6wqcDtv-kob9a1dmZ4jbFm4kLEgwscr6o8pb0C9Jea_OcJypIr8afTkKDIrTU76Fwo5nTROFDrgdsVBv-HVYDE_5jJbyfaMGimmhE_ymA1Sa0giRBbmCGjiqd_8xQ2vbv1AGutiKtDxmLlwFBkQpWKt7Fp2MOv-XeA1Pw_gIEscRULJJgzdLM2DAYPMKXoGsyZEfwW7Lyb8Vcw0upU7b3neQgstBPotVsx9GoHVLhl4zZhTehIBH1xfdQ62imNnMeqVTl-3lfoyFe1fEbFzo-Cjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل عنصر من عصابات الجولاني واصابة 8 اخرين كحصيلة اولية بعد انفجار عبوة ناسفة بصوامع الحبوب في كفربو بريف حماة الجنوبي</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/naya_foriraq/77082" target="_blank">📅 15:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77081">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPz6JD-_8SdwEr4bhC-t67b0hwOKkFFLqOw1_vb7KPPHSqkUApHeYfBr-0wFiHG-n0XK2Agt4HFXCp5leaWOG2V59GtHS6YLq_KguPnx50Aa05O-gTGr1senUqNZjfqnrolE_ouHo-giV_z_7PXJk3EvKdrwxUXM2-wC2h7ODpXshYYH_fFZl6vsbxbp0pn0o9bgQwDocfmQIRXqziGp-Ic3e46lGePxBVJivs2w_SrfhF1YPMgThawO8f9Q4W_XTTde3xF2T8nl5PK4C4qOKMUPazJ71nnnskcSvnFM8w58DZPI5yjxGmSMCewz0SCrqpq1TbklyqKq-d6mVydt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مالذي يحدث في بغداد   ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/naya_foriraq/77081" target="_blank">📅 15:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77080">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مالذي يحدث في بغداد   ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/naya_foriraq/77080" target="_blank">📅 14:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77079">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مالذي يحدث في بغداد   ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/naya_foriraq/77079" target="_blank">📅 14:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77078">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نشاط يعتقد لصالح جهاز الموساد الصهيوني في العراق   ربما يسمح بالنشر …</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/naya_foriraq/77078" target="_blank">📅 14:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77077">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مالذي يحدث في بغداد   ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/naya_foriraq/77077" target="_blank">📅 14:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77076">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مالذي يحدث في بغداد
ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/naya_foriraq/77076" target="_blank">📅 14:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77075">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
إذا صحّت تفاصيل الحدث الأمني في لبنان، فهو صعب للغاية.</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/77075" target="_blank">📅 14:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77074">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 01-06-2026 تجمّع لآليات جيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة العديسة جنوبيّ لبنان بصلياتٍ صاروخية.</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/naya_foriraq/77074" target="_blank">📅 14:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77073">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجار مخلف حربي في مقبرة وادي السلام بمحافظة النجف الاشرف العراقية يسفر عن اصابة ضابط برتبة عميد وزوجته</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/naya_foriraq/77073" target="_blank">📅 13:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77072">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682a69e92d.mp4?token=SnHGFMoioqn9G3xzRGKwRfnLvC_qnvci7B_Li-u2_tkhhMPfIGWh8yJNlCRlWfJA6YsgoK-7mXrFgibKhrcALYo5nzBpeMbOFWOHTayK4rfzeWsXJxeUQVReavSNwfpjgf-j7twSN-hYG2ZoFb0lr-RidsEkypFYUPl9q4OSW0I0oDtVfbvHrrVrL-f-MawqDeFYHAAYRPFX0zoo8VKfu9mMnQZFo7kG3mLw4mKG4phuUSI65g0nmG39N8VbHfVQugeiHONk_U4F9gQuELia3eilVwx1Ec1jKLsa4ICn7wS5R9V77MEGkxCTDI-dE_qLVYRE8CW1EQAILrya-d1jmx7BCxj7n6nXBshhB7QvgK36P-5WpxC3BgmgQWXrt2_tBPTfn_QJuF7DP-OfaD6sqmnz0JH6nELGQZW8HQVZY566MALJVXarTOhS3nOeQl7tFcZFq3w16FGS9XNrWt57FvUl1-5z8A2FFDi4VW2HBdAD3rD2PhahuYzxkCmkWVf8zvB8hlyzYBldIb6vX5v5xw1-6LuQ4VC5RCXwf08hK5jpr2mZgAXq6sOUQd5Ny0VLwlLFZAXNAuEz42-_AI9HuO9jTIJJJ2tVpycGQI--4YnHvsBrZPJrNtkAHvvOhR764PuCZSCSFBkDJ5cd99523opIukhtasAJOS6cEQt0ZX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682a69e92d.mp4?token=SnHGFMoioqn9G3xzRGKwRfnLvC_qnvci7B_Li-u2_tkhhMPfIGWh8yJNlCRlWfJA6YsgoK-7mXrFgibKhrcALYo5nzBpeMbOFWOHTayK4rfzeWsXJxeUQVReavSNwfpjgf-j7twSN-hYG2ZoFb0lr-RidsEkypFYUPl9q4OSW0I0oDtVfbvHrrVrL-f-MawqDeFYHAAYRPFX0zoo8VKfu9mMnQZFo7kG3mLw4mKG4phuUSI65g0nmG39N8VbHfVQugeiHONk_U4F9gQuELia3eilVwx1Ec1jKLsa4ICn7wS5R9V77MEGkxCTDI-dE_qLVYRE8CW1EQAILrya-d1jmx7BCxj7n6nXBshhB7QvgK36P-5WpxC3BgmgQWXrt2_tBPTfn_QJuF7DP-OfaD6sqmnz0JH6nELGQZW8HQVZY566MALJVXarTOhS3nOeQl7tFcZFq3w16FGS9XNrWt57FvUl1-5z8A2FFDi4VW2HBdAD3rD2PhahuYzxkCmkWVf8zvB8hlyzYBldIb6vX5v5xw1-6LuQ4VC5RCXwf08hK5jpr2mZgAXq6sOUQd5Ny0VLwlLFZAXNAuEz42-_AI9HuO9jTIJJJ2tVpycGQI--4YnHvsBrZPJrNtkAHvvOhR764PuCZSCSFBkDJ5cd99523opIukhtasAJOS6cEQt0ZX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناشطون على مواقع التواصل الاجتماعي السورية يتداولون مشاهد لعدد من الحوضيات العراقية التي حولت وجهتها من مضيق هرمز باتجاه الأراضي السورية مؤكدين أن الوضع المعيشي بدأ يتحسن مع وصول النفط العراقي لدرجة أن بعض أنصار الجولاني أصبحوا قادرين على شراء ربطة خبز كاملة بعد أن كانت تُعتبر حلماً بعيد المنال مؤكدين أن استمرار الإمدادات العراقية قد يفتح الباب مستقبلاً لشراء دجاجة كاملة بدلاً من الاكتفاء بمشاهدتها في الصور</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/77072" target="_blank">📅 13:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77071">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مشاهد من الانفجار الذي وقع في ميناء كونستانتسا في رومانيا.</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/naya_foriraq/77071" target="_blank">📅 12:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77070">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835fba7d0d.mp4?token=Oq60zRQfrhAVXu0j8VJdQYrzk-mZBxi86OustfUI46VsVrH09WRrfRYE9JqyOpebATge3Rf648JqqwReoZdOg21Xi0YBFGeq2wjP6VtXvDbylHR2863NlTDEexEXCLmG7tviXxkEP5d0LHKLkwNOG5dRboKCzmIKUCcpMoGNAyoNbW7a5hlMGqaFqGhiRMt0FmggUV6UJJeRDix0SGEr6Qvn7WGu2IDhJlQeYny7K8L1pbHUy_wnuEbvXt_mgI4n_erVNqSuVHcvH9ZX21Me4VxByPOGE1Zzww6wfnWsevYIwa2avyi_5j1eIUEFJFiakthiHK1NiQXj9a5MMaLiRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835fba7d0d.mp4?token=Oq60zRQfrhAVXu0j8VJdQYrzk-mZBxi86OustfUI46VsVrH09WRrfRYE9JqyOpebATge3Rf648JqqwReoZdOg21Xi0YBFGeq2wjP6VtXvDbylHR2863NlTDEexEXCLmG7tviXxkEP5d0LHKLkwNOG5dRboKCzmIKUCcpMoGNAyoNbW7a5hlMGqaFqGhiRMt0FmggUV6UJJeRDix0SGEr6Qvn7WGu2IDhJlQeYny7K8L1pbHUy_wnuEbvXt_mgI4n_erVNqSuVHcvH9ZX21Me4VxByPOGE1Zzww6wfnWsevYIwa2avyi_5j1eIUEFJFiakthiHK1NiQXj9a5MMaLiRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مروحيات إنقاذ تجلي جنود مصابين من جنوب لبنان وتهبط في تل هشومير وسط الكيان المحتل</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/naya_foriraq/77070" target="_blank">📅 12:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77069">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">إعلام خليجي: الفجوة الأساسية في المفاوضات هي الإفراج عن الأموال الإيرانية المجمدة</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/naya_foriraq/77069" target="_blank">📅 12:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77068">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-o23b8cF862B-U_lXSZT4GlDqCNtuXc6P8i4gamSgmVx8_LokseMLez2tEFfFmMV5gVe3WPCCzkpGVkpo_aOUaEYLMybswRRv8o_gFPZcoZEbw7-Aob_Gj7RsI3O-g-VfGUYUyI80zJY5qsVrdw427_JXgCUbLllcqJzSfs7utUSdYmHpvZDW64ShqTtjuaEyohzZ0JfIlN9LCRxaALPQzRW-zz6cdlicGXe1_j47etkE6s5maQRhcMVrYQluF9lAzxLJ517c3RmrpFnxnabmQdjkkmYAmex42tG8R14vbZW8fszF5XS-OMmfoBzpru9Szg0-ef6PEd9qoQ7qCDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من الانفجار الذي وقع في ميناء كونستانتسا في رومانيا.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/77068" target="_blank">📅 12:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77067">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c17006916.mp4?token=oMSNvGMjfRNRV2YRL_gctjxXjJmNRBPXTkjWbOPhAOg3BdSRVJKO6op63U9DYxbxJTsU69ZglS7_66YuJ5NFrw6V3LWGh-HiMYmyCd8kmejoEQvLgDnMGs0qRFIJXDitxYPJL6JMeW3yfkl37F2kfhjgPyaqcBpHxlZudxfmHJou2sGtxBX1XiAQ4iXC6vQsgkckwEmspHR75wKC1yCDLZzfWr1dKYbgcGYNfNd2Ws6tUd1TgqTFfAcpPReL3qjUc9-8khH-1_K4-W0OJb45u0Y4V2q5A288bc2MlbvHw_ptxr9GOND2vgs9S6GAlvxE7YNV2SahaMAMaaBFG1p8MjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c17006916.mp4?token=oMSNvGMjfRNRV2YRL_gctjxXjJmNRBPXTkjWbOPhAOg3BdSRVJKO6op63U9DYxbxJTsU69ZglS7_66YuJ5NFrw6V3LWGh-HiMYmyCd8kmejoEQvLgDnMGs0qRFIJXDitxYPJL6JMeW3yfkl37F2kfhjgPyaqcBpHxlZudxfmHJou2sGtxBX1XiAQ4iXC6vQsgkckwEmspHR75wKC1yCDLZzfWr1dKYbgcGYNfNd2Ws6tUd1TgqTFfAcpPReL3qjUc9-8khH-1_K4-W0OJb45u0Y4V2q5A288bc2MlbvHw_ptxr9GOND2vgs9S6GAlvxE7YNV2SahaMAMaaBFG1p8MjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الانفجار الذي وقع في ميناء كونستانتسا في رومانيا.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/77067" target="_blank">📅 12:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77065">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e0827fd9.mp4?token=OAnAfVvraprm8BH88kS-GLBQJ9iYVxk2M3cFRCF4ywwuAYUuiqXnZ0TwODuVSJwvvynGRRfUc9YAPKfzjt9HRxs2I5VvShn197GV2OyTL1zpsjDrBmr9wZk1jyZJYnO-TbTV0dW2wK4RqrTICRVuLnAOmAvH4V_B4jtvILJEsx3yBpUwAN6pP_Bns-S5RS-ZA_tF-HzndAl3H5WO4PUHikl6GBFcN_uXlE7SX_wm3g25gMWNEAGsLRJ_pSXPuDn7CjyhvgHJ9XwDTcHk0uFvZNduNgBBx89Y37DYAGs_mY2xMkOScA37Vg47l4na0qXDIgQFpysavDR2Y3pWSEyNAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e0827fd9.mp4?token=OAnAfVvraprm8BH88kS-GLBQJ9iYVxk2M3cFRCF4ywwuAYUuiqXnZ0TwODuVSJwvvynGRRfUc9YAPKfzjt9HRxs2I5VvShn197GV2OyTL1zpsjDrBmr9wZk1jyZJYnO-TbTV0dW2wK4RqrTICRVuLnAOmAvH4V_B4jtvILJEsx3yBpUwAN6pP_Bns-S5RS-ZA_tF-HzndAl3H5WO4PUHikl6GBFcN_uXlE7SX_wm3g25gMWNEAGsLRJ_pSXPuDn7CjyhvgHJ9XwDTcHk0uFvZNduNgBBx89Y37DYAGs_mY2xMkOScA37Vg47l4na0qXDIgQFpysavDR2Y3pWSEyNAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
استهداف صهيوني لعجلة قرب اوتستراد كفررمان جنوب لبنان.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77065" target="_blank">📅 11:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77064">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🏴‍☠️
حدثين أمنيين جنوب لبنان  سقوط محلقة مفخخة قرب قوة عسكرية إسرائيلية.  استهداف دبابة صهيونية واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77064" target="_blank">📅 11:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77063">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
حدثين أمنيين جنوب لبنان
سقوط محلقة مفخخة قرب قوة عسكرية إسرائيلية.
استهداف دبابة صهيونية واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77063" target="_blank">📅 10:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77062">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-v1KA-rMTiHoTJSC-fFkis_PyZuuRI-6VLmZthhEAkzU9q4khe5-gmt4GWbUVGHTr7g83qpbyRbrHaxNhS8oZsz_vxzglRXlz8Bl03kGqnTxfiHIh6dSiRXecYDN-uAT4OgAnIxAgxjSAEvbrBYAaZIsuN4-Pnk9AZy9_J4HUm0X8pyQ7pDR40iqmWDoFVqCE0GkF-3ZztYHvGPfyp_eVmN-2P24OUr03WgC0vxlWQVNpVGHrW0OL_Fb4v87n1vlDZt6iWk_p1XMGTFUrW_ZkPEyqcMizZFbz2DaEmWUOUQPttBkZXD4-YmV9qewEspygeCYpA9eS5eP-bvfpKdzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
قاعة الاحتفالات تسير على نحو رائع. إنها في الموعد المحدد، وبأقل من الميزانية (على عكس مبنى الاحتياطي الفيدرالي، حيث فشلت شركة "Too Late" فشلاً ذريعاً في إدارة التكاليف والوقت!)، وبجودة أعلى بكثير مما وعدت به، بما في ذلك مهبط الطائرات بدون طيار، وجميع العناصر العسكرية الأخرى العديدة، والتي تُعد جميعها حيوية للأمن القومي، والتي يجري بناؤها في جميع أنحاء المشروع المتكامل والمتماسك. إنها مطلوبة بشدة، وستكون مميزة للغاية! المرأة التي رفعت دعوى قضائية ضدي ليس لها أي حق في القيام بذلك. لا ينبغي أن تكون هذه قضية أصلاً، وهي تضر ببلدنا ضرراً بالغاً. إنها كثيرة التقاضي، ومدعية متسلسلة، وقالت إنها شعرت بالانزعاج أثناء سيرها بجوار البيت الأبيض، لكنها لم تذكر مشاركتها في أماكن أخرى بعيدة. فلماذا إذن تشارك في دعاوى قضائية بشأن مشاريع أخرى في أجزاء بعيدة من واشنطن العاصمة؟ هل تسير هناك أيضاً؟ كيف تسير في شارع مغلق تماماً عند مبنى الخزانة - لا يُسمح لأحد بالسير هناك؟ لم ترَ مبنىً قط، لأنه لا يوجد مبنى هناك</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/77062" target="_blank">📅 10:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77061">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b2abbb67a.mp4?token=n9_32ryTtiODRr02taAOtn6Kqf-WUFX6PLMVWuC_NOC-1xhBnUXMsN8M2Py4y1SaThxY3PRVEmmoIgFV2FSBfF2SgdQQb5bqLJlKyj6UoZb8n4E16xqOv0W9M6B6HMKCsKthLhLJUsbugv9UrnxllRVw4jTw9FggL2H135MQU_4yp_pnpNey8MEXkn7_sYhhE4X5Q__G0miyEWKGION7P7-g-k2lvOiy4SfU9AxmtTeIJSgCnctxoRFno3pvFkVrlnmdKOMGlvSUOkArspE3-oCaDw8won0O_P8cNY9aNsSqhOqLedOs6N89_TbV0twcSm3wSsg6Y3chg5A2zbIcFEj7Ra9JJEV2fyWmKUzemuDTCtzNEv2s6A99Wpjk_XklCR5ZFJy0albNBRn43u0c1LFZfeyu9sco2OnBNR8ESWA7HKN-u9Kp33GuKrci7503FqYi__L2cxavkPipENpUNQtNY9-57bSE4DHWsCOYtHwTZBRy6f-1qXuS57uFCFBn8WFeukYlIW13SSTR_gCOcHDKZXqsckjciCndyvFI4ypEt1r7W2t8_a30jMItvvXtSrrHzCpvzIiuSVTNWVD5LQPMO9t_NWJo-Q_P_MGO2VX_qZf4znksXAdX3l1bnIIdNhmQM3VYHAf05QovSd3bQguPZlZyYC7Ycyv0V2OjckU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b2abbb67a.mp4?token=n9_32ryTtiODRr02taAOtn6Kqf-WUFX6PLMVWuC_NOC-1xhBnUXMsN8M2Py4y1SaThxY3PRVEmmoIgFV2FSBfF2SgdQQb5bqLJlKyj6UoZb8n4E16xqOv0W9M6B6HMKCsKthLhLJUsbugv9UrnxllRVw4jTw9FggL2H135MQU_4yp_pnpNey8MEXkn7_sYhhE4X5Q__G0miyEWKGION7P7-g-k2lvOiy4SfU9AxmtTeIJSgCnctxoRFno3pvFkVrlnmdKOMGlvSUOkArspE3-oCaDw8won0O_P8cNY9aNsSqhOqLedOs6N89_TbV0twcSm3wSsg6Y3chg5A2zbIcFEj7Ra9JJEV2fyWmKUzemuDTCtzNEv2s6A99Wpjk_XklCR5ZFJy0albNBRn43u0c1LFZfeyu9sco2OnBNR8ESWA7HKN-u9Kp33GuKrci7503FqYi__L2cxavkPipENpUNQtNY9-57bSE4DHWsCOYtHwTZBRy6f-1qXuS57uFCFBn8WFeukYlIW13SSTR_gCOcHDKZXqsckjciCndyvFI4ypEt1r7W2t8_a30jMItvvXtSrrHzCpvzIiuSVTNWVD5LQPMO9t_NWJo-Q_P_MGO2VX_qZf4znksXAdX3l1bnIIdNhmQM3VYHAf05QovSd3bQguPZlZyYC7Ycyv0V2OjckU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفاة المرجع الديني آية الله العظمى الشيخ محمد إسحاق الفياض بعد تدهور حالته الصحية.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77061" target="_blank">📅 09:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77060">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">استئناف العمليات في ميناء الفحل العماني لتصدير النفط الخام</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/77060" target="_blank">📅 09:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77059">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRugNrxQbCrpNbOQrg7S_gh6qmyMk0rn3XBvfOyBnx7mc2qySZQFy71IWQrFJYOKmsnZu-_yQAPzofSDG4mGfZSc4gHH01Crh8lpuFl1s831drSN8V-1Bij8_YvTWruohmbTCEsvemVfUHaYGvtzWE85OU-msmxTM8lEac8hfT96Baa1XPpykLH0InMNehkYJv0REH85BFb-hOOBA-F4IvsNQMXH1-ke_liW9mzHXw18xxjWxtoXa-wI_Zw0OEvBijmO-R6O_fBfKQMQhtwIOBQZQbjcPA5A8bimI9glHV5RWgylrw9k-y8wvDUjjLSyQ0gw-oBP8JL6AVQCvuNk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر صورة مولدة بالذكاء الاصطناعي لابن جو بايدن وهو يرسمه مضيف إليها عبارة أعظم رئيس.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77059" target="_blank">📅 09:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77058">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGzusmXVoTSddh2vCl-cF6q82qC5WYWRClUI5Sk7UNzFaNqdrEUN45N4S7sbRlFq1MM4hbZRzyKrzTbZXBxOGyyrZA7vquYR5TL2o6h4ZaevqkKB2xtD66MMj4G1p6kiGFWeuzTMd-UYdUeSe7HHvSQhxiNUivDvUyUm1OcwoEpFNP6JFnxcZJqxf-n1r7nJjOK0PVwgVy6nED9yKwV-dLMUJ6-hfy9QVpD_zn46gAlYOAJUhnBg04JwevhrArykm7PCzdLj1Z8Znd6NIKi6X7q30VvkDPRd6vPG-CRiejhjGd0myj-Tg0d0StyS8NUiHrl4t19vlHnThEgcLmiPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
الدفاعات الجوية الصهيونية تحاول اعتراض صواريخ حزب الله شمال الكيان المحتل.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77058" target="_blank">📅 08:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77057">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXXz_fKQUQRp0retMjUZpiD7TUK_Ed3wIuRpc-8LSM_MOlNlBGAIBduvorrNGm4j-GzMYjzKHEhDJTxUUdK2yy5PsyXDZs3UjzZhOkqzn5BchjJggWt4qkDtishWvJrj7xC6xeirEwJw2fJnmSEaMS7Xz3KKlSx3bssCI7Lit6dDXGLb4BQrJa6vHFlbKrxS4pAYNL_nfNj4c1mZd-Yxm_wUPJ2fzweZHLGKxu8UNWcYpwWzQgv6XZVYpMrAajdP1mA03MqZ1eRPYHDwy2BHO_z9XdQk6WHqIzyJf5N_paBmGmAqYd-QaPj1q2j538Qt0tCBLTjMtaA--5pAGm4dNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب : انتخاباتنا في كاليوفورنيا اتعس من دول العالم الثالث</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77057" target="_blank">📅 03:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77056">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwLPvRrys84HQp8aI17VwBqZ35nIE4th-lT1V8IbG7FVRwK0WNV6FT9V0C3ZUQqvQCnjhWD62ZMa8Nb6YrsXn2hOKXH5UveBkPa1M1dz7U4LUqLwWReXNSHfbT3gis8jkuK5NT1AckV6xulMZBP7-QP-Gj-08nXwbMmGVVwdcp-l70U8waiCv5VDleq10gtLu8h_z6sYWwLxk4fV_YGNRZUL5Wvx0o8PfW10mcg1b1iG6jBrzp1Mlhr8Z55ohIXyeSQNRMb1alh7mL65cgkG2SEtDq2JvQhLEDR_Ic891Jn--PKLoSfI4CMzml3pmlJW9qqcS9MP1BrWWep51fBb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد المكصوصي : من
كنت مولاه فهذا علي مولاه ؛ تسليم ذو الفقار هو خيانة للبيعة ..</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/77056" target="_blank">📅 02:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77055">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">استهداف هدف معادي الان قبالة سواحل جنوب إيران</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/77055" target="_blank">📅 01:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77054">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/77054" target="_blank">📅 01:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77053">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6-gcuOuzyqlPqAalFxmvw8J2Uinj0eer1MwcJwNLcr13wP7Z4hAQq7rNLvqfuNq3UAIadQKrsz0lUU5ej9SHbBnCGtpiZXlRV-ehMpM1cMtMS-jxDe8iEcf2lW9p9FuBeWSTc3q0AdANaaMheVk93HDtMR7LrdF_8Y0OFBBuSm_NNdfSs1dy41YBGSFu_GatZsVRpjIDBR8v_U4YcOoDM9rdA4KkCYfFXLSw2W4400DejITCbFkp1UiRV6xNjav9UUndUC4mj8D3rpdInDUQQpFIlOd0raFUZ-HmC38X1znqYkr_r53p6aNpiKDplNwsp01dd7SQxNAjPxJZkGr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأمين العام لحركة أنصار الله الأوفياء الشيخ حيدر الغراوي رافضا تسليم السلاح: بنادقنا هي الامتداد الطبيعي لـ"ذو الفقار".</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/77053" target="_blank">📅 01:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77052">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727569b896.mp4?token=GnDSRUyJtqGT9oDmldJCUUol1o5KmmRqfMhoSCj2Ntn0LB04_z1tS984Ajj9weRCESPvD_idKnQtj71Mm6S3ERHYPg8Rnrcbayo906PEdtgFSgKVNhqGaDFTC53GiSfwGhqgtgG7QkkwpFHASM2p7g6H-SybBugePTCtVzYR4mfM0ZF5OJbpActjIBp-lvJ9dmSrjcgIoh6bG-15n42SonJb3R9diPAf5SLIV2T378MasHn-NM6r7eEexjFDsrnspV6t32U8k0yhsmlRQRgZNbxgEBMDkfivVcJVRfDle1PdDn7QI-IhOSlRGTa_SXS2QagIbXuFj46vM1zaXbqZjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727569b896.mp4?token=GnDSRUyJtqGT9oDmldJCUUol1o5KmmRqfMhoSCj2Ntn0LB04_z1tS984Ajj9weRCESPvD_idKnQtj71Mm6S3ERHYPg8Rnrcbayo906PEdtgFSgKVNhqGaDFTC53GiSfwGhqgtgG7QkkwpFHASM2p7g6H-SybBugePTCtVzYR4mfM0ZF5OJbpActjIBp-lvJ9dmSrjcgIoh6bG-15n42SonJb3R9diPAf5SLIV2T378MasHn-NM6r7eEexjFDsrnspV6t32U8k0yhsmlRQRgZNbxgEBMDkfivVcJVRfDle1PdDn7QI-IhOSlRGTa_SXS2QagIbXuFj46vM1zaXbqZjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطنين يرصدون ظهور اجسام غريبة لليوم الثاني على التوالي في سماء ناحية النخيب غربي العراق حيث مقر القاعدة الاسرائيلية المكتشفة مؤخرا</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77052" target="_blank">📅 01:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77051">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شبكة CNN: الحاملة كلفتها 13 مليار دولار</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77051" target="_blank">📅 01:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77050">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شبكة CNN تبث مشاهد لحاملة الطائرات الامريكية "يو إس إس جيرالد آر فورد" وهي مدمرة بعد هجوم ايراني رغم النفي الامريكي</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/77050" target="_blank">📅 01:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77049">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cb994ab4.mp4?token=KWlYN2vkK7-uIYCwTFCxNgSL4Y9uIsJ0YBaT9iS4bH6RZusHrVN0VqoSp4QGg2KntuXFQxAfukBPseWPV12hPn97c65UziQlQAp-PCJHSHPYTUPZ9BgqttcJKm9lzqJzhJ6PqL8UeJb4GLa5IHXGB_AMizwSYMp8ki1bvmPubTE1joXXfQgMbRQ_F8RxbMWA4fXy8aGbVBkbgVEIb1NM4XXbmJ_AqdXPmlpGL19d3Iv-Xm7gav1fwyNeUfGaWInhLNAZT3G2sN70HF7cobiDzMFB_2DARsTZi_Qj_U7Ndho22OB0nVWWGq9qTHYRgZal6FAQjD0A9Pin77h_JBUGsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cb994ab4.mp4?token=KWlYN2vkK7-uIYCwTFCxNgSL4Y9uIsJ0YBaT9iS4bH6RZusHrVN0VqoSp4QGg2KntuXFQxAfukBPseWPV12hPn97c65UziQlQAp-PCJHSHPYTUPZ9BgqttcJKm9lzqJzhJ6PqL8UeJb4GLa5IHXGB_AMizwSYMp8ki1bvmPubTE1joXXfQgMbRQ_F8RxbMWA4fXy8aGbVBkbgVEIb1NM4XXbmJ_AqdXPmlpGL19d3Iv-Xm7gav1fwyNeUfGaWInhLNAZT3G2sN70HF7cobiDzMFB_2DARsTZi_Qj_U7Ndho22OB0nVWWGq9qTHYRgZal6FAQjD0A9Pin77h_JBUGsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبكة CNN تبث مشاهد لحاملة الطائرات الامريكية "يو إس إس جيرالد آر فورد" وهي مدمرة بعد هجوم ايراني رغم النفي الامريكي</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77049" target="_blank">📅 01:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77047">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVJzHi4cZ9m89knXXHp27Yve4etDHg_WtFyxNHM95nonWjAR4IMRksCjZ-H1q19T3WtaL2KeakNl5AmoZxklMn0J1ZzYju-WO6rDDje1Z447b1IYfITT3E9h6m2dtsBXa309JBNYxgvQ-thtekZ1eAspHfYbpxn5_-uCYk6nDZQQ_QT8cLeSxFxugBQfkuxEYqhizad6HGV4-u8h7QtqKvd1TuHuFw3qDmHH0PDD6s5-kJvpOb_CDgH63wAxqoSrI5NxZRZoC7GJcDeJHdYPBqiM1Lz4DH6FbiTe8RLvDR9kTqMAbWx47VSmpOo4oWCSZaPiopwZDxem3Iz_y3LyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZycoF17onRuPylS_xIzuWlz7Wz6fjd7UfRgtI-SyauKuXi2kCb8C_I5yaKhx6Ca0G5bLieWyAq5Mr7GNN0g1qNSXeQCG1-Pi-IwiUiSn7pRHNsHEdjoA-2vrg1XKGHZ77NooYYcz6HLmrE6UIi_puIeqUvynbUGyd8RgbCkP7FZUW8tz4r71TAxe61I9vEG399lM5QzZjw3aoYdukuvWtbJ5stMIcPgeb90gfgkDh-I0ZW_8cxWmFho-3y7y8hP1Uvmo7rhfRHectGOnmkwUeauwBYXSbi8eHcyRmluEgjlRuOKBGI814h4rKvLkIWGSradB1SasxZJ1uo7QmaTNUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
شبكة CNN:  عندما اندلع حريق على متن حاملة الطائرات يو إس إس جيرالد آر فورد في مارس، أصدرت البحرية الأمريكية بيانًا مقتضبًا قالت فيه إن الحريق قد تم احتواؤه، وأن اثنين من البحارة قد تلقيا العلاج الطبي لإصابات "غير مهددة للحياة"، وأن حاملة الطائرات "جاهزة للعمل…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/77047" target="_blank">📅 01:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77046">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0TE69xSMw-4sopYcYHC3y5uMPt1_XuLyaybka2cciEjVvIzfTMN8yfYIn6u2DXG7X880LV7I6X0EejBlRJVQsS4KSjzkf1QSMwBlUknhtc6LZpxAoFxARpthbLRupVNMK-sfJW2vM7diou4FaCWQPIvOpsoGqIaL_xB6NtiwbeYwSLmsxux2yeUzjsJVAtTxUbcXtd7m_jEpVQ3THjRXHqDym5UCnd-THHvt2NFe1udVCsJuRasPD8FAfwYfHbp8xyRRZRraaUmOs7haXVTcrtocTjDdwao7rxhwVhdqYFy0IohYQpF5QwBsllVCGRlnJdXLM3zha8Y3cXaZwhu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77046" target="_blank">📅 01:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77045">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77045" target="_blank">📅 01:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77044">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الاعلام الايراني:
‏تم رصد حريق بقوة تزيد عن 300 ميغاواط في جزيرة داس بالإمارات العربية المتحدة؛ ويبدو أن شيئاً ما قد تم استهدافه أو تفجيره. ‏تُعد جزيرة داس واحدة من أهم مراكز تصدير الغاز الطبيعي المسال في الإمارات العربية المتحدة. ‏الحريق عمره حوالي 12 ساعة، مما يعني أن الحادث أو الانفجار أو الهجوم المحتمل وقع خلال النهار، وليس في الليل.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77044" target="_blank">📅 00:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
مقتل أحد ابرز قادة العصابات الإجرامية في جنوب سيستان وبلوشستان والتفاصيل لاحقا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77043" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏ترامب عن السيد مجتبى خامنئي: ‏في الواقع، يتمتع بسمعة طيبة للغاية في بعض الأوساط. ‏يقول البعض كلاماً سيئاً عني، لكن الكثيرين يقولون كلاماً سيئاً عني. هذا غير صحيح على الإطلاق، بالطبع.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77042" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77041">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e18f8c0b54.mp4?token=hLET_7rT91fGWn8UDNp-jymxF1CjK2VsW8-hvu1cyT0Qrb5oHMsVgnoQJ3CM2Me1xlN9pNPs3DnyG7ZKCARh7CpdsJPL_MILaPK70Gev2rbad9aUOpJ9EeWosubS8qo74BknPVQPCGhE5KCjAkeqI30ZeeKJ462HevnAa3AZWggQS9455WCSul2cafOBdvZbUFHGK1bVukt8G9fLgSZEzKk-ePMzjXi6V29WcXcPvR-B0yH5Ta6t-TBkF2AMmXYp0l4MNkW6IrGjPJ_qOXLBvd91uYTr5cg8c8PIBegQD0j_9ZPstIsfgPSkpNzWQ04PtSFSAXFhtaAfPLNw9DTWwxp0l-WxgQxD6X3fRFEuIVgGtH9iWXrIHnugDyS3ZUy_HO41-Uv4ESV0NCdYHOqZX1D1Jb0LFniaHDDP-MY2vHofNAbBIOggTn3KAGbAv8A4HCF3MnT5RrpII0dmfR40L7MX8uv9vMnA7TJqNOOrAp3cCx8Rr0UCXsJ9n-WHVjMY-wIeYuAHQGBc9PR3A_p9DzK_v9esdz8m-IrWKoaTrUqnt66Zz-6q1PIC0xGmC5Gy8bJ0g2w1_UJvz2PYRojdyppOjqnUxFqG98BEYmVyRLRRaSfXeSSxAdb2h_x8OgFMuNGeSxq7QelZ4GPcps85SC5L0LwGFJiE9goF9vc6I64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e18f8c0b54.mp4?token=hLET_7rT91fGWn8UDNp-jymxF1CjK2VsW8-hvu1cyT0Qrb5oHMsVgnoQJ3CM2Me1xlN9pNPs3DnyG7ZKCARh7CpdsJPL_MILaPK70Gev2rbad9aUOpJ9EeWosubS8qo74BknPVQPCGhE5KCjAkeqI30ZeeKJ462HevnAa3AZWggQS9455WCSul2cafOBdvZbUFHGK1bVukt8G9fLgSZEzKk-ePMzjXi6V29WcXcPvR-B0yH5Ta6t-TBkF2AMmXYp0l4MNkW6IrGjPJ_qOXLBvd91uYTr5cg8c8PIBegQD0j_9ZPstIsfgPSkpNzWQ04PtSFSAXFhtaAfPLNw9DTWwxp0l-WxgQxD6X3fRFEuIVgGtH9iWXrIHnugDyS3ZUy_HO41-Uv4ESV0NCdYHOqZX1D1Jb0LFniaHDDP-MY2vHofNAbBIOggTn3KAGbAv8A4HCF3MnT5RrpII0dmfR40L7MX8uv9vMnA7TJqNOOrAp3cCx8Rr0UCXsJ9n-WHVjMY-wIeYuAHQGBc9PR3A_p9DzK_v9esdz8m-IrWKoaTrUqnt66Zz-6q1PIC0xGmC5Gy8bJ0g2w1_UJvz2PYRojdyppOjqnUxFqG98BEYmVyRLRRaSfXeSSxAdb2h_x8OgFMuNGeSxq7QelZ4GPcps85SC5L0LwGFJiE9goF9vc6I64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجنرال رضائي لوكالة فارس:
إذا انحازت الإمارات والكويت إلى جانب الصهاينة، فيجب منح أبو ظبي وبوبيان للسعودية والعراق.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77041" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77040">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">المراسل: أسفرت عملية "الغضب الملحمي" عن مقتل والد مجتبى خامنئي وزوجته وطفله.  ترامب: لستُ الشخص المُفضّل لديه، لكنه على الأرجح مُحترف.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/77040" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77039">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100efa8385.mp4?token=WkD7fDVWiNtykdIOzJWcsd_FxnnzciMoFniHAmP1GdBdY3YLqtS6CZt9zO6rl_I51pO1KgCUf44lnN4ooxoLGQpHDF7FYbVSn4JyAR5KOMb3J_P_qCDkUnaAgItzSEffDtVKvD6lFA_vgjf1P6Putf5kehPTTqpi0YkNLIJFUJKcvgS6G5ZZGwFQtrO8-VbWYjDlB4y_QUDt_pu6CFCw_Au2PzDLq8M8yzbMxiU5nbx5TVasxbnSMHG3e41zpM8LINOIs0BwdXXnttPIcrTDx4MfHQuDArQvi5iCFLR_gaCV75q8loFGwhKvf9hYm9guNeHoCqji6YNhyfGayCZNMIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100efa8385.mp4?token=WkD7fDVWiNtykdIOzJWcsd_FxnnzciMoFniHAmP1GdBdY3YLqtS6CZt9zO6rl_I51pO1KgCUf44lnN4ooxoLGQpHDF7FYbVSn4JyAR5KOMb3J_P_qCDkUnaAgItzSEffDtVKvD6lFA_vgjf1P6Putf5kehPTTqpi0YkNLIJFUJKcvgS6G5ZZGwFQtrO8-VbWYjDlB4y_QUDt_pu6CFCw_Au2PzDLq8M8yzbMxiU5nbx5TVasxbnSMHG3e41zpM8LINOIs0BwdXXnttPIcrTDx4MfHQuDArQvi5iCFLR_gaCV75q8loFGwhKvf9hYm9guNeHoCqji6YNhyfGayCZNMIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: إذا توصلنا إلى اتفاق مع ايران، فمن الممكن مقابلة المرشد الأعلى لإيران. سيكون من دواعي شرفي أن ألتقي به.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/77039" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77038">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامب: الدولتان الوحيدتان القادرتان على الحصول على الغبار النووي الايراني هما الصين والولايات المتحدة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77038" target="_blank">📅 23:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77037">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇨🇺
🇺🇸
وزارة الخزانة الامريكية تفرض عقوبات على الرئيس الكوبي ميغيل دياز</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77037" target="_blank">📅 23:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترفيهي اخر  ‏ترامب: ‏لم يرفض حزب الله أي شيء. اتصلوا بنا وقالوا: "ما رأيكم بالتوقف؟"  من تكثر شرب بالصالة الجديدة مال البيت الابيض
😄</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77036" target="_blank">📅 23:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">#ترفيهي  ‏ترامب: لا تزال بعض الصواريخ موجودة في إيران، ولكن عددها قليل جداً.  من دمرنا كل شيء الى بعدها موجودة لكن عددها قليل
😄</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77035" target="_blank">📅 23:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#ترفيهي
‏ترامب: لا تزال بعض الصواريخ موجودة في إيران، ولكن عددها قليل جداً.
من دمرنا كل شيء الى بعدها موجودة لكن عددها قليل
😄</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77034" target="_blank">📅 23:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇷🇺
‏الكرملين عن رسالة زيلينسكي التي طلب فيها لقاء بوتين: الرسالة وصلت، زيلينيسكي مرحب به للقاء بوتين في موسكو "في أي وقت".</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77033" target="_blank">📅 23:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c38afa62c.mp4?token=KFk26EZmsNOz8Yc-vUx-21Z5HfipCvVPMhGgTkthGxkO1D4S8DkssAVA0y6fXMgOnnu6TLmHV4V4F96m13G6NKgTTokgQGMJtGRP8mL58hKt2jg-1EJ5vC8Bm7R9AgslsAvqL1214cUv1juDN78e3ri6RQgA7oe4Wlk9dscCQMOCTbRM8BWtQsdvid23sTkd_fFboGMJ2AgY2YePI6nj7cR3k2I1btM5HngqytdHE6R7OPHNRCq6jwQHOZw4cKw-lWPaTFzBisT7PrcaFSKBd0KQEd1OtJEVvMSst2ZqsrsjEaGkUmcdbnF93fnERKWlXXC3jCO-mJ15RBnzumEm8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c38afa62c.mp4?token=KFk26EZmsNOz8Yc-vUx-21Z5HfipCvVPMhGgTkthGxkO1D4S8DkssAVA0y6fXMgOnnu6TLmHV4V4F96m13G6NKgTTokgQGMJtGRP8mL58hKt2jg-1EJ5vC8Bm7R9AgslsAvqL1214cUv1juDN78e3ri6RQgA7oe4Wlk9dscCQMOCTbRM8BWtQsdvid23sTkd_fFboGMJ2AgY2YePI6nj7cR3k2I1btM5HngqytdHE6R7OPHNRCq6jwQHOZw4cKw-lWPaTFzBisT7PrcaFSKBd0KQEd1OtJEVvMSst2ZqsrsjEaGkUmcdbnF93fnERKWlXXC3jCO-mJ15RBnzumEm8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المنتخب الاسباني يسجل الهدف الاول على المنتخب العراقي ضمن المباراة الودية التحضيرية لكأس العالم 2026</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77032" target="_blank">📅 23:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇷🇺
‏الكرملين عن رسالة زيلينسكي التي طلب فيها لقاء بوتين: الرسالة وصلت، زيلينيسكي مرحب به للقاء بوتين
في موسكو
"في أي وقت".</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77031" target="_blank">📅 22:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
وكالة تسنيم الايرانية عن مصدر أمني:
- أحد أهم مستشاري رئيس الإمارات محمد بن زايد مرتبط بالعمل مع الاستخبارات الإسرائيلية منذ عام 2015
- مستشار بن زايد كان محل اهتمام الأجهزة الأمنية الإسرائيلية منذ عام 2007 بسبب طبيعة مواقفه
- المتابعة الإسرائيلية لمستشار رئيس دولة الإمارات دخلت مرحلة جديدة بدءاً من عام 2015
- اكتشاف أهمية مستشار رئيس الإمارات بالنسبة لـ"إسرائيل" تم في وزارة الخارجية الإسرائيلية
- الجهة التي اضطلعت بهذه المهمة كانت مؤسسة "ماماد" الأمنية التابعة لوزارة الخارجية الإسرائيلية
- مؤسسة "ماماد" لعبت دوراً أساسياً في اكتشاف مستشار رئيس الإمارات ثم توجيه مواقفه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77030" target="_blank">📅 22:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77029">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حدث أمني صعب جديد جنوبي لبنان... التفاصيل لاحقًا.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77029" target="_blank">📅 22:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77028">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByXzMENXbtrWpXEdeKkizcchSsm5_xYyc-KT4j-ZN_bpEIMvQPGB8VMeTdqZuT8VDYea5vQr5nDxa4aEF8SUSbcg4qWv6pl04UqfACXVkbE2tcsYjCMtc75dXR1j5kiI0f_LwF5oEIwjz1_s6aUE0a_8dks8EM3YJ2OtfPk7bNj-eHR1ilDV2VAUQ3aaCqwDQLcDHrPb8EdjZX8RvWSNAYqeDZjpJPhLmP4Zapyk3pNs7wi_2zXrh2bSQ7h0hQnFYTG1tdfX1rjywoDrGeowi2bAq0oPSOBPxo-8M6MuusNuWkQuGHX43Y7EknXf4AyQxcQB5ReQ0QL678vgvde94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش العدو يعلن مقتل ضابط برتبة نقيب من الكتيبة 75 التابعة للواء السابع المدرع في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77028" target="_blank">📅 22:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77027">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الإيراني:
لا نعتبر أي ورقة مع أمريكا نهائية إلا إذا أخذت ملاحظاتنا ومصالحنا بعين الاعتبار. نصر على وضع 50% من أصولنا المجمدة تحت تصرفنا فور توقيع مذكرة التفاهم مع أمريكا</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77027" target="_blank">📅 22:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77026">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇱🇧
بيان صادر عن حزب الله:
يمعن العدو الإسرائيلي في اختلاق الروايات الكاذبة وفبركة الاتهامات وإلصاقها بالمقاومة زورًا وبهتانًا، ضمن سياسة التضليل والأكاذيب الممنهجة للتغطية على جرائمه المتواصلة والتي باتت مكشوفة أمام العالم أجمع.
إن اتهام العدو المقاومة باستهداف مقر قوات اليونيفيل في بلدة دبين والتسبب بمقتل أحد جنودها، هو ادعاء باطل وكذب محض. لا سيما أن الاتهام يصدر عن العدو نفسه الذي لم يخفِ يومًا انزعاجه من وجود القوات الدولية في جنوب لبنان وسعيه الدائم إلى الحد من دورها، لأنها تشكّل شاهدًا حيًا على جرائمه واعتداءاته وخروقاته المتواصلة لسيادة لبنان.
إن حزب الله يؤكد حرصه الدائم على دور قوات اليونيفيل في جنوب لبنان ضمن المهام الموكلة إليها بموجب القرارات الدولية، ويتقدم بأحر التعازي إلى قيادة القوات الدولية وإلى عائلة الجندي، متمنيًا الشفاء العاجل للمصابين</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77026" target="_blank">📅 22:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77025">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X574XYpuPWUvTfaaRdLFmihdGXThYyrKsdPpGqqF-o6t7qtlPkZ15VibipKodBe14iFM9RIoPtP8_heVs8iWxuN5LpCsQ2aIBXSXPzCeP79prIrIxak-9RXc-yQ4eEpAXA_TtRjP0u-hjH-a0e0kepxoXSNMF21JOlqOtuQe1Wxw7d8demwYXyW9213Uf7DJ2ALlm4CKaz8nGIs5ACRh9szSDAfbZ0uVm_X-MQf6DFATCBjHGJQGs86-WqVTLz9V0hp1AGAvk3vJkK4CX1-iMLsZaLyMOBi7vih2Z7Lw2wDEHzevSbH3RE0Cni6kfboe4UVA13YCaBWBzbdBAFU3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
أعتقد أن لدينا أكثر الانتخابات غير شريفة في أي بلد، في أي مكان في العالم!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77025" target="_blank">📅 22:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77024">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇷🇺
‏بوتين: الحرب على إيران صرفت اهتمام الولايات المتحدة عن أوكرانيا</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77024" target="_blank">📅 22:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77023">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الناطق باسم القائد العام للقوات المسلحة العراقية: تشكيل لجنة مركزية عليا تضم ممثلين عن الدفاع والداخلية والحشد الشعبي لحصر السلاح بيد الدولة</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/77023" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77022">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇷🇺
‏
بوتين:
الحرب على إيران صرفت اهتمام الولايات المتحدة عن أوكرانيا</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77022" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77021">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 02-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77021" target="_blank">📅 22:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77020">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:  - قطر دولة صديقة لنا ولطالما جمعتنا بها علاقات جيدة جدا  - يا للأسف استُخدمت في الحرب الأخيرة القاعدة الأميركية في قطر ضدنا كذلك استخدمت الأجواء القطرية  - لقد أبلغنا الأصدقاء القطريين باستخدام القواعد الاميركية على أرضهم…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77020" target="_blank">📅 22:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77019">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
- قطر دولة صديقة لنا ولطالما جمعتنا بها علاقات جيدة جدا
- يا للأسف استُخدمت في الحرب الأخيرة القاعدة الأميركية في قطر ضدنا كذلك استخدمت الأجواء القطرية
- لقد أبلغنا الأصدقاء القطريين باستخدام القواعد الاميركية على أرضهم ضدنا
- نحن شاكرون للإخوة في قطر الذين بذلوا جهودا وساعدوا من أجل التوصل إلى حل عادل بين إيران وأميركا إلى جانب باكستان</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/77019" target="_blank">📅 22:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77018">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇸🇾
سماع دوي انفجارات في مدينة حلب السورية.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77018" target="_blank">📅 22:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77017">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌟
🏴‍☠️
مجدداً.. أستهداف دبابتي ميركافا في محيط قلعة الشقيف بجنوب لبنان من قبل أبطال حزب الله.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/77017" target="_blank">📅 22:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77016">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇷
🔥
بوتين: روسيا ترتبط بعلاقات وثيقة مع إيران ونحن قادرون على المساعدة في حل الأزمة .</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77016" target="_blank">📅 21:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77015">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c6ea7cab.mp4?token=bzT5ysBAE8PPE3iG_oxWD5zoJ-nNOTXlAiuRvAHwic90C7jFEuPbEmlDN7zKEK1IYFX3QG5ltQX6KJ3Cs-01i3VZElZTNdZAWj6g1CbiB2piPPFJANj7HFTKrc5HNNi4WO_bqCWsR7NsEBvgtUsnIBb_Aql0fT53Z6SSlvEc4CAflG49u12ISdDvIiHnixPcyr7K1Aa5voqb985LU9CHp0wh7q1voj7NHFVJTSp87KIrtTX3IkwbLK8PvOgoopD03Z_jipW_GAzxkHBRT_kfY7JqlZWVAcvHc9X3rDzaN-MYeQsNF3AgPpEz951Ue7zNVUzYOWCKNEvQXn7k7-Klag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c6ea7cab.mp4?token=bzT5ysBAE8PPE3iG_oxWD5zoJ-nNOTXlAiuRvAHwic90C7jFEuPbEmlDN7zKEK1IYFX3QG5ltQX6KJ3Cs-01i3VZElZTNdZAWj6g1CbiB2piPPFJANj7HFTKrc5HNNi4WO_bqCWsR7NsEBvgtUsnIBb_Aql0fT53Z6SSlvEc4CAflG49u12ISdDvIiHnixPcyr7K1Aa5voqb985LU9CHp0wh7q1voj7NHFVJTSp87KIrtTX3IkwbLK8PvOgoopD03Z_jipW_GAzxkHBRT_kfY7JqlZWVAcvHc9X3rDzaN-MYeQsNF3AgPpEz951Ue7zNVUzYOWCKNEvQXn7k7-Klag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إندلاع إشتباكات مسلحة في منطقة عائشة بكار بالعاصمة اللبنانية بيروت.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77015" target="_blank">📅 21:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77014">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇶
رئيس هيئة الحشد الشعبي العراقي:
الحشد الشعبي منح القوات الأمنية فرصة لإعادة بناء قدراتها بعد هجمة داعش الإرهابي.
الحشد الشعبي تشكل في الميدان استجابة لفتوى السيد السيستاني.
لا يزال العراق محاطاً بالتحديات.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77014" target="_blank">📅 21:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77013">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402d45f5a9.mp4?token=W9XJSrawugCbVk0gwKqj_8OHP3qjTG8EEHCwPwBHR9HPnNzmyTmtsPdljisVQkSOYFe-y0mwGWTB2b4Yk5NqREc6coWlJaRDOz31tJD1bJfsmuzXBQaFuHl8rieFgSy6eIukbHYz3bhDQxPGE3tNqrr2PC6jEHuiWNMOFGWQkcXEaPrtVgQKQ-17_tCY4eIjltE0P3U1maoJrrcaCF5tnwe8MOrcaeVS-qdqXkMghHnLZt3wkJJXWFchVHD_BonvkqujEfKDsH0s4wcnNyk2qvGGvjz3PtbYfxgoLyoqUAcT5BcOvif1vkYJojl7n3cyeZX6kBazSSG2i2oZJETR5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402d45f5a9.mp4?token=W9XJSrawugCbVk0gwKqj_8OHP3qjTG8EEHCwPwBHR9HPnNzmyTmtsPdljisVQkSOYFe-y0mwGWTB2b4Yk5NqREc6coWlJaRDOz31tJD1bJfsmuzXBQaFuHl8rieFgSy6eIukbHYz3bhDQxPGE3tNqrr2PC6jEHuiWNMOFGWQkcXEaPrtVgQKQ-17_tCY4eIjltE0P3U1maoJrrcaCF5tnwe8MOrcaeVS-qdqXkMghHnLZt3wkJJXWFchVHD_BonvkqujEfKDsH0s4wcnNyk2qvGGvjz3PtbYfxgoLyoqUAcT5BcOvif1vkYJojl7n3cyeZX6kBazSSG2i2oZJETR5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إندلاع إشتباكات مسلحة في منطقة عائشة بكار بالعاصمة اللبنانية بيروت.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77013" target="_blank">📅 21:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77012">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LU-_cXvJUmcJKfM8-MNMheHyFcHnZiU-2Z49t8LrfMEBK79sAM39l3NG-WiYU5JsvXTQREiXPcUXTBjdkYnl_QUpPF8vcvM-SJd9Qj9h2_n6rn__LGI1WYlIpRdYfbtZS0aS_GQJcmBTOWn1Z6FMiN8CH3QRMJYjSTwkgr1p1UpbLALQXvRJ7CPwLfWIyYnlJllTr00pcYadWA9YHF27Yvma0spPwBxIV_9Z02c-sNo-wywmos9ojUV-U7JYqCmJ1DH6UiaNenpgwBLhHzZC-4E1F-omkdDmTkmgmWhRRtu-v-9N8rg4jnnYQTZ3qQ21QNsgLpZLugVcKN2a_qwXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: الرياضة الجامعية، وهي مؤسسة أمريكية عظيمة تنتج العديد من الرياضيين والقادة والهيمنة الأولمبية، هي "فوضى" كاملة، ويقول الجميع إنه يجب إصلاحها.  بعد الدعاوى القضائية التي لا تنتهي والأحكام المجنونة، لم تعد هناك حدود تقريبا، وسرعان ما لن يكون لدى معظم…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77012" target="_blank">📅 21:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77011">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909440813e.mp4?token=IG7d2qFDHD8RJdFIwCF5mhEDTl8Kcrh7ZVUQPy-xIYN6GTGUwBru9aia0cDOkB87KLf0ne_qwfqryF_K1WjxbdKAWXqQKDKpxuJJd6pPyI0sY3sk8RmjRCo66ZMOO1j7324ezudYPZiJHXeeQ1NPtQ4ESbw8vTTgqqOkk9Ri7tPK9OEZ-uFwfFyKWu6kLwd6r7iPv0t7GXfH9DNm_bp0PlMlMT-d4sC0qbAkbh3-zSHaC4c2G5A4gzmI9qWjgf3CvYFslOH6mvfqEqdn9r50cotT0cnClQLiHhs3unjuJEna9Re_Ts2WSiJKnHFIwwHqswHoMyeOwVmo3HFKIGF_3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909440813e.mp4?token=IG7d2qFDHD8RJdFIwCF5mhEDTl8Kcrh7ZVUQPy-xIYN6GTGUwBru9aia0cDOkB87KLf0ne_qwfqryF_K1WjxbdKAWXqQKDKpxuJJd6pPyI0sY3sk8RmjRCo66ZMOO1j7324ezudYPZiJHXeeQ1NPtQ4ESbw8vTTgqqOkk9Ri7tPK9OEZ-uFwfFyKWu6kLwd6r7iPv0t7GXfH9DNm_bp0PlMlMT-d4sC0qbAkbh3-zSHaC4c2G5A4gzmI9qWjgf3CvYFslOH6mvfqEqdn9r50cotT0cnClQLiHhs3unjuJEna9Re_Ts2WSiJKnHFIwwHqswHoMyeOwVmo3HFKIGF_3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
والد الجولاني يتحدث عن الدول الحليفة لابنه ويتهم السعودية باحتلال صحراء النفوذ وينسب مدناً تركية منها أضنة وماردين ومرسين وأورفا وطرسوس لسوريا ويتساءل ساخراً عن من يمكن إقناعهم بالتنازل عن هذه المدن.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/77011" target="_blank">📅 21:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77010">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
🇱🇧
🇱🇧
ايران لا تترك حليف لها
رفعُ الرايةِ العملاقةِ لحزبِ الله، والبالغِ ارتفاعُها 500 متر، فوقَ برجِ آزادي في طهران .</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/77010" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77009">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇷🇺
بوتين:
لا نستبعد في المستقبل اتخاذ قرارات بشأن الاستخدام الكامل لـ "Oreshnik" ضد أهداف، بما في ذلك في مناطق البناء الحضري.
نمتلك جميع الموارد اللازمة لتحقيق أهدافنا العسكرية والجيش الأوكراني يعاني من نقص كارثي في عدد ​​الأفراد.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/77009" target="_blank">📅 20:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77008">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
واشنطن طالبت طهران بتسليم ردّها قبل نهاية الأسبوع.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/77008" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77007">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔥
🇮🇶
سوالف الگهوة
رسالة رئيس مجلس الدوما الروسي السيد فياتشيسلاف فولودين إلى رئاسة مجلس النواب العراقي .</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77007" target="_blank">📅 20:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77006">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الصهيوني في محيط قلعة الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77006" target="_blank">📅 20:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77005">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv12KRLC-op5qTGE28Iu6cMBOagmIImJ9QCY2VzBznfonnp2LQgnm--CTz8LnhNzCbAsFeyTTpPxnlfgad4xnbEB2FxPA2O6sviuGdXBd1-tuA8yBWwNfotXsAJ_pUK59bv5vyWKeDHj6ml2VHN4znz8v3L7frdKwo6V7tQNyEYTRKYoU6L7gmPH7NKu_FkAp7yUrc_movuu9NBMtVK6Ton0FjwQ3sHUlav4Bu7fCJSYH-DeItvbyMVPNeCWqS44TGE9ORHSFAKTL7ka04LJlYpCXD84sgrGBHXFDhpaCw0EIaZk04cvVNFGj9PjWzTmNl4XVP9obx1JuYSNbd4LRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
الرياضة الجامعية، وهي مؤسسة أمريكية عظيمة تنتج العديد من الرياضيين والقادة والهيمنة الأولمبية، هي "فوضى" كاملة، ويقول الجميع إنه يجب إصلاحها.
بعد الدعاوى القضائية التي لا تنتهي والأحكام المجنونة، لم تعد هناك حدود تقريبا، وسرعان ما لن يكون لدى معظم الكليات رياضة لأن كل واحدة منها ستكون مفلسة، ولن يسمع عنها مرة أخرى. الرياضات النسائية، والألعاب الأولمبية نفسها، هي الأكثر خطورة من هذا الوضع الكارثي. تتحول الرياضات الجامعية إلى رياضات محترفة، إلا بدون قواعد على الإطلاق، وهي نتيجة لا يريدها أحد. اشتكى لي رؤساء الجامعات ومفوضو المؤتمرات والطلاب الرياضيين والمدربون والمديرون الرياضيون من أنها أصبحت كارثة، بعد سنوات من عدم اتخاذ أي إجراء، وأن المدارس كانت تخسر مئات الملايين من الدولارات سنويا. لقد قارنوه بقطار شحن لا يمكن إيقافه!
لهذا السبب، قبل بضعة أشهر، عقدت مائدة مستديرة جمع فريقا عالميا من أفضل المديرين التنفيذيين الرياضيين والطلاب الرياضيين والقادة السياسيين في بلدنا. كان الهدف هو إيجاد حل من الحزبين لحل المشكلة.
بناء على هذه الاجتماعات وخبرة السلطات الرائدة، وقعت أمرا تنفيذيا، لكنني قلت دائما إن الحل الأفضل هو الحصول على قانون الكونغرس من الحزبين إلى مكتبي من أجل إنقاذ طريق طويل ومحرج عبر الجحيم لهذه المؤسسات. أود أن أشكر أعضاء مجلس الشيوخ تيد كروز وإريك شميت وماريا كانتويل وكريس كونز، من بين آخرين، على تقديم قانون حماية الرياضة الجامعية. يحل هذا القانون العديد من القضايا الأكثر إلحاحا التي تتحدى جامعاتنا وطلابنا الرياضيين، ويوقف الفوضى، والأهم من ذلك، قد تكون الفرصة الأخيرة لإنقاذ الرياضات الجامعية، والكليات نفسها، قبل فوات الأوان.
لقد عمل مجلس النواب لفترة طويلة وبجد بشأن هذه القضية أيضا، وأنا ممتن جدا للمتحدث مايك جونسون والزعيم ستيف سكاليز على عملهما لحل هذه المشكلة الرئيسية للغاية.
أحث مجلس النواب ومجلس الشيوخ على الاجتماع معا لتمرير قانون نهائي من الحزبين، يمكنني التوقيع عليه هذا الصيف، يعكس آراء ومدخلات كلا المجلسين. علينا أن ننقذ الرياضات الجامعية! شكرا لك على اهتمامك بهذه المسألة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/77005" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77004">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c605ae8ccf.mp4?token=Mq8l_KERObjiaEhfMy32_y6s65FpcIGvldHithLEN1XTu15UuFUHN9lTHrMKQoPBPEQ4xZVfAxmmIW7S7wf9cIicovX3pAezv0Y44WqHwIsiBhSCPRefZWj7OyNg_zn1ovCbk89xtk-rrjCn2C3cj99Q4WvvkhRsmwYpE9fldtk0MbBe2r2SD9rcoynQIOXY7UXCOWl8Rql9J1GR_x0cnkpLLKgiB32kTtoT3azVMCBlEwToi6qd-MbJkk8G-GCGFSlyIllxfO0nnfImliBs86DXqiBxyHEzvZQlQRvUINPhHewOaqK-adm4LJoyUAtssPgd5LN_e7Nfvrn923fppg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c605ae8ccf.mp4?token=Mq8l_KERObjiaEhfMy32_y6s65FpcIGvldHithLEN1XTu15UuFUHN9lTHrMKQoPBPEQ4xZVfAxmmIW7S7wf9cIicovX3pAezv0Y44WqHwIsiBhSCPRefZWj7OyNg_zn1ovCbk89xtk-rrjCn2C3cj99Q4WvvkhRsmwYpE9fldtk0MbBe2r2SD9rcoynQIOXY7UXCOWl8Rql9J1GR_x0cnkpLLKgiB32kTtoT3azVMCBlEwToi6qd-MbJkk8G-GCGFSlyIllxfO0nnfImliBs86DXqiBxyHEzvZQlQRvUINPhHewOaqK-adm4LJoyUAtssPgd5LN_e7Nfvrn923fppg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
غارة صهيونية على منطقة المساكن في مدينة صور بجنوب لبنان؛ إرتقاء 3 شهداء كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77004" target="_blank">📅 20:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77003">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4d0cbb1a.mp4?token=IiTcAAtvkkDAabl7jZId8yf_EVVYc8hx-lA9kGjnLiDqJWhJGa7tNV970Bq5dMqQicrhIMmT8C9p19uvyXb5gQ6KOMTeWeaIlythLLSubPhIWvp__HlDfVmSRskHurwFj6SF0FPH5JKZwzg43BujBVnvVU11SqI-d_1rtyNs6QEGTCGARixK8K_5lih8ZN3w5o7y-9qFzU0FgeTEZ0T-ygDAuaSlK2DYIkXwF6QQurUp9uWZO_NayEaVW5yW0M-mWjX9Yf4MmfzyjmJvLGKWLmrlow1LMu1K6jH1FWdBgXM5p0tNIbUFjCw76gc7z17Ry4b4fI1Q3OTE7o0SKZPOFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4d0cbb1a.mp4?token=IiTcAAtvkkDAabl7jZId8yf_EVVYc8hx-lA9kGjnLiDqJWhJGa7tNV970Bq5dMqQicrhIMmT8C9p19uvyXb5gQ6KOMTeWeaIlythLLSubPhIWvp__HlDfVmSRskHurwFj6SF0FPH5JKZwzg43BujBVnvVU11SqI-d_1rtyNs6QEGTCGARixK8K_5lih8ZN3w5o7y-9qFzU0FgeTEZ0T-ygDAuaSlK2DYIkXwF6QQurUp9uWZO_NayEaVW5yW0M-mWjX9Yf4MmfzyjmJvLGKWLmrlow1LMu1K6jH1FWdBgXM5p0tNIbUFjCw76gc7z17Ry4b4fI1Q3OTE7o0SKZPOFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
جيش الإحتلال التركي ينشئ نقطة عسكرية ومهبط للطيران المروحي على مرتفعات ناحية بادينان في محافظة دهوك شمالي العراق.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/77003" target="_blank">📅 19:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77002">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edbc444708.mp4?token=JamnYx_XDEkb_hNTxykcDxIaTDvTzLdV6_Dmktr6vOd6bmlnevC85Xr2zq2eX5VLOIGQT7D8CUVP1YixolySqLLjz8yh45pthRB-wycc6GhzM5YJiLExIW0O7YdF3ZgPI_ML9XLXHzmHk2DszyhBClufGpry2DMDBl60C5ZD1sjYfKw_dSN_F6BqgrUsh5rfF5-w4yBWHXUEc65Bn2T44ivh2P5G1r42Jr2QhupBp9-0EJmq_SYBMX51GiMgJsKQcwYmNyizLgrWIaX4DLQiWZ1uKZXiyW8L1zgOPBXnRJmxWHJwzTzZ2E75J10l555M7x1vyLIm0dQhzHGHBk5wrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edbc444708.mp4?token=JamnYx_XDEkb_hNTxykcDxIaTDvTzLdV6_Dmktr6vOd6bmlnevC85Xr2zq2eX5VLOIGQT7D8CUVP1YixolySqLLjz8yh45pthRB-wycc6GhzM5YJiLExIW0O7YdF3ZgPI_ML9XLXHzmHk2DszyhBClufGpry2DMDBl60C5ZD1sjYfKw_dSN_F6BqgrUsh5rfF5-w4yBWHXUEc65Bn2T44ivh2P5G1r42Jr2QhupBp9-0EJmq_SYBMX51GiMgJsKQcwYmNyizLgrWIaX4DLQiWZ1uKZXiyW8L1zgOPBXnRJmxWHJwzTzZ2E75J10l555M7x1vyLIm0dQhzHGHBk5wrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
الله أكبر.. تصاعد اعمدة الدخان من دبابات وآليات جيش الإحتلال في محيط قلعة الشقيف بجنوب لبنان بعد دكها بالصواريخ الموجهة والمسيرات الإنقضاضية من قبل أبناء نصرالله.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77002" target="_blank">📅 19:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77001">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581c1b2139.mp4?token=svnXVrP50pl8gpv8EHJJ0sfmz36sFAVDUkIY8P_OvcyVn32hg4Fli8r7WKJDOrdmqdp-8Bb04qPVqFNB-xCs62OspeEPSa0Szc582-CQ0INDMw4wXJhvLh-8SnuzoysObDmNkFXNYTdCPcXpyErO0mSdX_RsigpZWSgHSu1gDnmIpnDVGW858W9T_yAnY4wpcEKJ2oMGJ55XBQ5YW8HmEorfVC0_zVc-FnMSSTewKwdQChhsHWGMgvREPRHmUWDZuHUaPuouPmeoeXinQRk7VqRv_kcEtQ4h4C87sv8vdmymlZX1j9iiAVTs_lWUGxmUPTlE7R4mN-jCpL-j6U-yycAa59DOQYf8c-P97FR-XSV21Oin_OSTINu09jPxLMsgXUoBlebEdDWtw58LdT3v3d4p4_SNl1JIue2I_4uOOqX-90spYjvHRCOI6v0TLo4_o0_e_dhfHLEXrLRDjYV3bZ-QfCc1MzpyFZ7adjIwcGGwIBhAsaWF_Z5Bjg-wBSA9L4d9gQQ8SNPBbUXNxki1js-t99-FAStQbABnIBGYjWW0ruARsti-nXoxStC2Bo3ImQBjTZRcBZtH7QyFmhogsBu3_lKEY8mmkCi8cLpYkaipmqMln4yFxHQVTvy9zm8l6x9ePBwK-sw7aoRK4z1ZrzlM5S6ENROaKYL8GqykAMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581c1b2139.mp4?token=svnXVrP50pl8gpv8EHJJ0sfmz36sFAVDUkIY8P_OvcyVn32hg4Fli8r7WKJDOrdmqdp-8Bb04qPVqFNB-xCs62OspeEPSa0Szc582-CQ0INDMw4wXJhvLh-8SnuzoysObDmNkFXNYTdCPcXpyErO0mSdX_RsigpZWSgHSu1gDnmIpnDVGW858W9T_yAnY4wpcEKJ2oMGJ55XBQ5YW8HmEorfVC0_zVc-FnMSSTewKwdQChhsHWGMgvREPRHmUWDZuHUaPuouPmeoeXinQRk7VqRv_kcEtQ4h4C87sv8vdmymlZX1j9iiAVTs_lWUGxmUPTlE7R4mN-jCpL-j6U-yycAa59DOQYf8c-P97FR-XSV21Oin_OSTINu09jPxLMsgXUoBlebEdDWtw58LdT3v3d4p4_SNl1JIue2I_4uOOqX-90spYjvHRCOI6v0TLo4_o0_e_dhfHLEXrLRDjYV3bZ-QfCc1MzpyFZ7adjIwcGGwIBhAsaWF_Z5Bjg-wBSA9L4d9gQQ8SNPBbUXNxki1js-t99-FAStQbABnIBGYjWW0ruARsti-nXoxStC2Bo3ImQBjTZRcBZtH7QyFmhogsBu3_lKEY8mmkCi8cLpYkaipmqMln4yFxHQVTvy9zm8l6x9ePBwK-sw7aoRK4z1ZrzlM5S6ENROaKYL8GqykAMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الصهيوني في محيط قلعة الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77001" target="_blank">📅 19:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77000">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
🏴‍☠️
إصابة مباشرة لصواريخ حزب الله في وادي الحولة بشمال فلسطين المحتلة واعمدة الدخان تتصاعد.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77000" target="_blank">📅 19:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76999">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
🌟
جيش الاحتلال الاسرائيلي يعلن اصابة 3 جنود - أحدهم في حالة خطيرة، نتيجة لعملية لحزب الله ضد قواته في جنوب لبنان تم إبلاغ العائلات.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76999" target="_blank">📅 18:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76998">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAa07NFDK_zXets0Zi6NTfoE47eRNNmyj2RUKZ1q_JDzV6vFlYikoCoP-5CvN67GZRb7bWo1alpQoaPI7gF3UD8Oes4lrzmGOljFK4xhIhTJQyMAkBRkQrF1lkg9Jyw1JIDdJFPmRD3licInbFnYvGAh2UNc3-hw00GDBTHroIfASWlkYfsgTxKLM6-tI_1SP9bIBSRCJn2e98hTSAjGfi9dr0UNg0d_qzTLKub6iNNabGJQOXYnwItCC6cmI-iISc_UEFOsvTDxnP7Rbgq2KNDCYfMuvfsGFgtDvcxwVBbb6F314s3cH3Gq5mf2Dv3Tj2pxCroMhGD8_j4iuL8anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
لبيك ياشيخ نعيم.. حزب الله يدك الشمال المحتل برشقات صاروخية وصافرات الرعب تدوي في المطلة ومحيطها.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76998" target="_blank">📅 18:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76997">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ec8e09d4.mp4?token=V3uuXuDRdMz4coZTiCnVesHlNvEodPjpDEkx2GtrEIEdgwd0DoYu2GPsBn5M_g205CfwVaRM4iw7PC0jrrVmJLPdlvaFMhaoF0SkR-ZNddf-zoFxlALdioFtWa7Rtd5yW48FdfV3dNod5pcr0hwp3l-CHJoVwIThd2OycPsYI18Wixn0c1IlTwsAHYDjcQS2Ax9cTz7nUtAi2qp5eZETxp_sOAcyOSL6WkNjYXK8BFbR9ICiwj42550vBzPe76y_cVHAYu-neEHQgymyR7jWCN7mqJR7KZV4RXhVLVMcyHx4TGBwWMrIGZTowLvjgjSyod864nvwGxIyNfwsb7FbeXCw3AQ5znwdaSMjMrfSSdaBkzv0Jn81ln1fXm9CBUYz0AsZxFiDoldfod6WmE4AVcgTApi7SU1oKQzip2cgiM5NcTc4EpX8hV7jGlgUAadD2uXCc4TSuBqD7fjVFmoyRyI8UPFM6asIe4QBW4HIZAcYgYsCvtICnK5kThc7hMPeyhryw-7H0gdpTQRSD_-Lx0L75EhaLzpY9eW7HUHEbrmhVeeUsVibdo2OAvqAlUdaUksWcLh6KBuxncHuvgqv0YIvBH4zuFrng3JyLhag7NTdOm91xvjG21fx_E4l8ul-W0h1CJ1Gw3z4eDcEvzAuqr6Hfd39r_h9D3n0stJfYCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ec8e09d4.mp4?token=V3uuXuDRdMz4coZTiCnVesHlNvEodPjpDEkx2GtrEIEdgwd0DoYu2GPsBn5M_g205CfwVaRM4iw7PC0jrrVmJLPdlvaFMhaoF0SkR-ZNddf-zoFxlALdioFtWa7Rtd5yW48FdfV3dNod5pcr0hwp3l-CHJoVwIThd2OycPsYI18Wixn0c1IlTwsAHYDjcQS2Ax9cTz7nUtAi2qp5eZETxp_sOAcyOSL6WkNjYXK8BFbR9ICiwj42550vBzPe76y_cVHAYu-neEHQgymyR7jWCN7mqJR7KZV4RXhVLVMcyHx4TGBwWMrIGZTowLvjgjSyod864nvwGxIyNfwsb7FbeXCw3AQ5znwdaSMjMrfSSdaBkzv0Jn81ln1fXm9CBUYz0AsZxFiDoldfod6WmE4AVcgTApi7SU1oKQzip2cgiM5NcTc4EpX8hV7jGlgUAadD2uXCc4TSuBqD7fjVFmoyRyI8UPFM6asIe4QBW4HIZAcYgYsCvtICnK5kThc7hMPeyhryw-7H0gdpTQRSD_-Lx0L75EhaLzpY9eW7HUHEbrmhVeeUsVibdo2OAvqAlUdaUksWcLh6KBuxncHuvgqv0YIvBH4zuFrng3JyLhag7NTdOm91xvjG21fx_E4l8ul-W0h1CJ1Gw3z4eDcEvzAuqr6Hfd39r_h9D3n0stJfYCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله ينشر:
قبّة الطيور ...
כיפת הציפורים...</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76997" target="_blank">📅 18:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76996">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5e868ae6.mp4?token=HOV9c_CSqi8NTVA1QBVr42XAK9nCpaWPZxPbLiY4rxIEuAKY_fO-lBtWcn7wHkz5EnAw0mT3vKpO8Us9QNwvsSjh43EVLyh_RZBF6fKeekbh-wyKgrLOGNjbKyUu1v0Gov2Gv3wOuPTo5gFBIiKVcINOAOMYN8aghDHha3LUZehyQ2WgeMM7G4pGx1Egw2xnFtrD7Y1DUvtGuY0k32kQF-kvcGF951e-6--KhwDMlIhNGN_VcR2-FmHCQeuRDZZONjUVXyXY8CxtyaQM7HkwYO54fFL1Y_e5w6tDm0yRSz1l6SjDq5MeR33-wAlMHY-r1KjTkpn8NJ5a_-TpAAeGNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5e868ae6.mp4?token=HOV9c_CSqi8NTVA1QBVr42XAK9nCpaWPZxPbLiY4rxIEuAKY_fO-lBtWcn7wHkz5EnAw0mT3vKpO8Us9QNwvsSjh43EVLyh_RZBF6fKeekbh-wyKgrLOGNjbKyUu1v0Gov2Gv3wOuPTo5gFBIiKVcINOAOMYN8aghDHha3LUZehyQ2WgeMM7G4pGx1Egw2xnFtrD7Y1DUvtGuY0k32kQF-kvcGF951e-6--KhwDMlIhNGN_VcR2-FmHCQeuRDZZONjUVXyXY8CxtyaQM7HkwYO54fFL1Y_e5w6tDm0yRSz1l6SjDq5MeR33-wAlMHY-r1KjTkpn8NJ5a_-TpAAeGNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
لبيك ياشيخ نعيم..
حزب الله يدك الشمال المحتل برشقات صاروخية وصافرات الرعب تدوي في المطلة ومحيطها.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76996" target="_blank">📅 18:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76995">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الصهيوني في محيط قلعة الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76995" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76994">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
السيد عبدالملك بدرالدين الحوثي:
نؤكد على جهوزيتنا للتصدي للأعداء بمعونة الله وبالثقة به في أي جولة من جولات التصعيد أو أي تطورات في إطار الوضع الراهن.
نحن على تنسيق تام مع إخوتنا المجاهدين في محور الجهاد والمقاومة والقدس تجاه ما يحدث في لبنان وفلسطين وتجاه الإجراءات الأمريكية الظالمة والعدوانية وما يلزم تجاه ذلك.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76994" target="_blank">📅 17:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76993">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇨🇳
🇩🇪
الصين تحذر ألمانيا بشأن تايوان:
نأمل أن يتمسك الجانب الألماني بمبدأ "صين واحدة" وأن يمتنع عن استخدام قضية تايوان للتدخل في الشؤون الداخلية للصين.
سيكون هناك بالتأكيد ثمن لتجاوز الخط الأحمر في قضية تايوان.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76993" target="_blank">📅 17:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76992">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
🇮🇶
رسالة من الشعب الإيرانية في مدينة الكورة جنوبي البلاد خلال الإحتفال بعيد الغدير الأغر إلى عراق المقاومة والشجاعة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76992" target="_blank">📅 17:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76991">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⭐️
تقرير الوكالة الدولية للطاقة الذرية:
لم تتلق الوكالة الدولية للطاقة الذرية أي معلومات من إيران بشأن حالة المواد النووية المعلنة أو منشآتها، كما لم تتمكن من الوصول إلى أي من تلك المنشآت لإجراء أنشطة التحقق الميداني، باستثناء محطة بوشهر.
في ضوء استمرار عدم رغبة إيران في معالجة قضايا الضمانات التي لم يتم حلها، فإن لدى الوكالة الدولية للطاقة الذرية مخاوف بالغة بشأن احتمال وجود مواد وأنشطة نووية غير معلنة في إيران.
أن عدم قدرة الوكالة على التحقق من مخزونات اليورانيوم المخصب المعلن عنها سابقاً، لمدة عام تقريباً - وهو أمر متأخر جداً وفقاً لممارسات الضمانات القياسية - يمثل مصدر قلق بشأن انتشار اليورانيوم.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76991" target="_blank">📅 17:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76990">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
🇮🇷
الحرس الثوري الإيراني:
لن يتحقق الهدوء في المنطقة دون انسحاب الصهاينة من الأراضي اللبنانية المحتلة.
لا تزال هذه الأرض ترزح تحت وطأة العدوان الوحشي للكيان الصهيوني الغاصب. لم تُجدِ معارضة المؤسسات الدولية ودول العالم وتعبيراتها عن الاستنكار نفعًا في ردع حكام تل أبيب المتعطشين للدماء، ولم تُسفر تدخلات النظام الأمريكي المتعجرف، الذي يدّعي إحلال السلام، إلا عن تفاقم الجريمة والإبادة الجماعية.
يُعوّض الجيش الصهيوني الجبان العاجز، بكل ما يملكه من عتاد، هزائمه على الجبهات بقتل المدنيين وتدمير المنازل والمستشفيات والمدارس. هذا النظام العنصري، رغم الدعم المتواصل من الولايات المتحدة والحكومات الأوروبية طوال تاريخه المخزي، لم يستطع حتى كسب قلوب سكان قرية محتلة، وفنّه هو حكم الأراضي المحروقة، ونشهد يوميًا تدمير منازل الشعبين الفلسطيني واللبناني المظلومين على يد هذا النظام المعتدي.
لن يسمح الشعب اللبناني للنظام الغاصب بتحقيق ما عجز عنه في الحرب بدعم من النظام الأمريكي القاتل للأطفال، وذلك عبر اتفاق مفروض.
كان شرطنا الأساسي لقبول وقف إطلاق النار في الحرب الإقليمية هو وقف إطلاق النار على جميع الجبهات، بما فيها لبنان. يجب على العدو أن يوقف هجماته على الشعب اللبناني فوراً، وأن ينسحب فوراً إلى ما وراء الحدود الدولية بإخلاء الأراضي اللبنانية المحتلة، وأن يعترف بوحدة الأراضي اللبنانية.
إن الشعب اللبناني فخر الأمة الإسلامية ورمز شرف شعوب المنطقة، وسندعمه جميعاً بكل قلوبنا، ولن يتحقق السلام في المنطقة دون الانسحاب من الأراضي اللبنانية المحتلة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76990" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وهذا يعني ان اي مواجهة مستقبلية على غرار حرب رمضان فان المقاومة العراقية المذكورة أعلاه سوف تكون بنفس الوتيرة السابقة ولن تتغير اي معادلة اخرى على المستوى الميداني ،، فلم تكن جبهة لبنان بعد البيجر صادمة وحدها ؛ بل كانت مسيرات الحميداوي والكعبي والولائي والغراوي…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76989" target="_blank">📅 17:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
🌟
ابو مجاهد العساف المسؤول الامني لكتائب حزب الله: ما يخص فصائل المقاومة الإسلامية الخمسة، بالإضافة إلى كتائب كربلاء، فإنها ستبقى على تماسكها، وستنجز مهامها ما دام هناك احتلال للأرض.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76988" target="_blank">📅 17:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtQfFVkUXhRjjYd5UfuHtVOxTnJ09i7L0Waj6Wx-kvgh1xEjX6IEpc6Nq6CB4pR6mQVQbMhOlaCDW-g6aB-9CI66pe1aO99PIDtFHR3Wtxor2anEpsfYn0OqBnUJUHxFYMZ22zFaTEltuFLAJwctMQWoWnGRiJ22_U8VoMTBb8R_GuaK51yumLuDK0R-CM1htEYRZ-BmJWoQaHzLWJ88G3tc8ojXWfCL4HEYwcPau_gPpklgRB0oWdri7Yyxg6mF-XzKifpX9hqlt7YFlV3O2LNqXPFK9tiJAKJTNqeR7aH8Wxge7u1fQIwzqjS7aL67Sa5N9sY1hDvzvS2d3H-nEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
ابو مجاهد العساف المسؤول الامني لكتائب حزب الله:
ما يخص فصائل المقاومة الإسلامية الخمسة، بالإضافة إلى كتائب كربلاء، فإنها ستبقى على تماسكها، وستنجز مهامها ما دام هناك احتلال للأرض.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76987" target="_blank">📅 17:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dgbel5uKSPP6QwJ05WpzX3B2_IwygiG1L424tdDkcgvPd-cu_z0IIc5xRfB4hhaSCp3Jd8PeSVHVkxTCPPyFB4cu2FiyRhYzkbW3BhSDdLf3eiKeFoQp30J_owVOfBy7o1MZEh-njEMf037J2FP8i4UyJoXbPlDaPpo9ddbQMt0ZYOml-He4gEHfWFy-sBrZj1hn97RTT2JPsM0KHeiX8rb8xG1NOyWigpsXexaQrxHamSD79n7lV1Mx1rxnxt1evHbtsoyoYRCF9AZbXEq4xGbw0dzvKcezqFg5yVn4IkMB61z6-zVkAO9nPss3xBu_nSD36Wv6R1h99ImildYmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
سلطات آل خليفة في البحرين تعتقل عدداً من الأطفال من أبناء الطائفة الشيعية
1.سيد سجاد سيد فاضل الموسوي
2.سيد قاسم سيد ياسين الموسوي
3.سيد محمد سيد ياسين الموسوي
4.سيد حسن سيد ماجد سيد فاخر
5.سيد عباس سيد جعفر
6.سيد حسن سيد حيدر
7.سيد ماجد سيد هادي
8.سيد محمد علي سيد نجيب
9.علي حسين جميل المرزوق
10.محمد علي صالح
11.علي عيسى
12.علي حسين جارالله
13.امين الحواج</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/76986" target="_blank">📅 17:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU8EALQqnNa2oHtYMZW7lTib-sGJg_uxtFuiakHAPH-tBA84CjhDJkRpK7sxhFPJX8dDenAiMw0Y87gvBicRvj_InEV_FZXq2f0d7w8uwBTeV0__m_SxplCqX7CmW2e2r7j3T9mC3Pgx44vZS3qoC5iZ5aKYngxlNC5z4r0x72OGoGO83M1IiVXYUxQQ6mkRm2egU9W1OWLHWMgquZEPqvK0chfhObTB4th3fumV25REZy1qArGyK8Zq_XaCcNiOpPg1r_e9w9XBLxWFMHrcPuPZm0PrbMFIIv7oe5-dSvDRkwp6-y9QkGDgpJ8rlNgZ3GuV6y_2vo1x3f7qyOxzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بزشكيان
:
لقد كان الحفاظ على الوحدة والتماسك والتضامن هو الإطار النظري والأساس للحكومة التوافقية.
‏استناداً إلى تعاليم الإمام الأعظم وقائد الثورة الشهيد، وفي ذكرى صعود الإمام إلى السماء، التي تتزامن مع عيد الإمامة والوصاية، نجدد عهدنا مع القائد الأعلى للثورة بحماية وصون هذا الكنز الثمين.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/76985" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e658e4f43.mp4?token=kqOIWeJ4ktGBwJ9pcW_9eYoQp2JZKHA-KdSP9FzqvV1L5hAlXn2wjZY0kpDpV89FtTV40dnvudeHFs22jmTExtS_g76w5zcr09_Npbc7mi8ITubS8lCA5aMBHULQEjb1nmj39r1f1DC3P-40_S_JzJTP5sIOHp7DOLImK7BxPUa2DjMKk10TasYGM76ooyf2QJTk_ZCPDdJtQ_D9mo9fM71xAJRk_Mbc06s7SsVIAKloG_OqbmheG8Xi84yFcsdPm90g834AlTS4FxOfAk16USyVWxHAvcFeNe_u7Cy8s9kQvO6nJXEzDUKQZWoAgxNeC6ajszU2YHg0pCL-135QhJZ0HbAjl2rWSS4PDNLfrZv2fAXFVuIkdAEPqTGzP9PHgNdu27-Ixj7Kzu-Oc0ydImRQ_rrJGti9SXpYtuaP1TNWYythN4OaPC7NUCuA0xy_RGClv69Z81EvKdWlnLvA6MIPczcHcGi_xqqxfysFMJXZM9yltcx6HoMzyW04awEXLCdbhCWWbNoZJW7dMU5o-UodoCk3eK3w3n5pzw95tsIomJONxoy8YtDeOg7NOboAyCFj70mNYJc7z_vMsTwdZZIQhJU-nIfLwGanALLfvtyNrgvqgfqy6ENN-HdoclTJ19ZtNdTD1l6OdK_6dh2Umx4dskogeiq9YIE2T9etDL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e658e4f43.mp4?token=kqOIWeJ4ktGBwJ9pcW_9eYoQp2JZKHA-KdSP9FzqvV1L5hAlXn2wjZY0kpDpV89FtTV40dnvudeHFs22jmTExtS_g76w5zcr09_Npbc7mi8ITubS8lCA5aMBHULQEjb1nmj39r1f1DC3P-40_S_JzJTP5sIOHp7DOLImK7BxPUa2DjMKk10TasYGM76ooyf2QJTk_ZCPDdJtQ_D9mo9fM71xAJRk_Mbc06s7SsVIAKloG_OqbmheG8Xi84yFcsdPm90g834AlTS4FxOfAk16USyVWxHAvcFeNe_u7Cy8s9kQvO6nJXEzDUKQZWoAgxNeC6ajszU2YHg0pCL-135QhJZ0HbAjl2rWSS4PDNLfrZv2fAXFVuIkdAEPqTGzP9PHgNdu27-Ixj7Kzu-Oc0ydImRQ_rrJGti9SXpYtuaP1TNWYythN4OaPC7NUCuA0xy_RGClv69Z81EvKdWlnLvA6MIPczcHcGi_xqqxfysFMJXZM9yltcx6HoMzyW04awEXLCdbhCWWbNoZJW7dMU5o-UodoCk3eK3w3n5pzw95tsIomJONxoy8YtDeOg7NOboAyCFj70mNYJc7z_vMsTwdZZIQhJU-nIfLwGanALLfvtyNrgvqgfqy6ENN-HdoclTJ19ZtNdTD1l6OdK_6dh2Umx4dskogeiq9YIE2T9etDL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية
آلية هامر تابعة لجيش
العدو الإسرائيلي
في
محيط بلدة زوطر الشرقيّة
جنوبيّ لبنان
.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76984" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IF7WHre-C4vjo73kf1w2lvikGNJ6ecuemLUFW1jvgNU8siYxThikOp_-6W8GJEIA_mxSn1ilxr-ekIgXRIDw1xVMF2ssCC7TZxBSUNPF2MXCXq_rskqOY4RW95gabO4N5q6fjhBhjnYzxh3M4miYKwPSYD6g14sbuwYcZBxRkIF2yiaLUqJfn39zY31ArgtlY0oikJz7Au7bw-FQI7xlonDjFEv4Zt61eCChEGdc0BvViWTXnx-rE74jzXgCqkGMmBtQWeuT3vrVTK6VoeVtItkVCx4I39IArfuOehZKtiAzu9oTSewfhVwY4F9g4A4mU2ssuzklxVvRPxLX95I33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
بالتزامن مع زيارة نتنياهو والنائب سوخوت إلى شلومي، أطلق حزب الله صواريخ استهدفت المنطقة بشكل مباشر، ما أدى إلى تفعيل صفارات الإنذار ومغادرة المسؤولين الموقع قبل وقت قصير من القصف.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/76983" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKhUjrzCpKxadJU-mexkOrYsFapdpfheAYR8qotA3Npxjc_3teK5qxb6PL5YjkgP6e2DhwB8nVMhXNchy0l1YwL1N7jqdb4m2ZFX-rnsNFggrRv_KTK-ahQhB6IckCnNbNuDB9blh14FthLlovjIPKwMeByD985jjKGpRy69i5yojucgcTK8XGNvz5caiGeDmHFQO1vwq8jK8wUfXjL_DSbjxTO6TLoU0Yvqz_k3Zf6DwR7wymq4qUyW2olBDci2WlVkGMbj4EZPgtfTlRf6rfUwcnC2EfkirirOfq0jnul4advOlK5muSIU9TclJOAj7csvHRGLklXE0HGpQp1h3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
بالتزامن مع زيارة نتنياهو والنائب سوخوت إلى شلومي، أطلق حزب الله صواريخ استهدفت المنطقة بشكل مباشر، ما أدى إلى تفعيل صفارات الإنذار ومغادرة المسؤولين الموقع قبل وقت قصير من القصف.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/76982" target="_blank">📅 16:57 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
