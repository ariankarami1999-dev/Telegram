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
<img src="https://cdn4.telesco.pe/file/jzgVPbyU1DDeXZwZWIyF5-IMwSOTVweNrNxilHDNV0X7BZijn-0TFUQIkPDeuaBbrfth20WjyxhxfYv7gY7r3DvzPG3YhrzvsPvtQEzSGnUmBYw3Gw2-oPu10ETEGq0FGMJFFwPJbTmmDDUO5493H0sKSBgg50J5SI880HlQhCBST8Dci3vC-CcEWaHdKjQ73R946UNXs0JTlS7dGw0SUHl9wusA-nBxnCzPOXeRUtPy-0G6FuIvYZBFD4SvQfpS3lCEcskI_420-4oIJRNvTZqZeUa77cKrHmsq3-0uPEo70p5-_hOcmKJMhA5ET3f1mbpwF3lOp5VpvMFQY3FG8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 987K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 14:51:53</div>
<hr>

<div class="tg-post" id="msg-138873">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
استانداری هرمزگان: دود در شرق بندرعباس ناشی از آتش‌سوزی انبار ضایعات و درختان نخل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/138873" target="_blank">📅 14:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138872">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
تا الان در پی هجوم مهاجمان مراکشی به اسپانیا، ۱۸ نفر از مردم این کشور کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/138872" target="_blank">📅 14:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138871">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-Mez-nn3NtWZ91ZWeEjfdurV6sLvCj3IDQrMH5jKPIawaatf4sGjEaAjH7Ekp6KrioX_owLGXm9_mRNqvtPIqk-j72UR8jEhYrm4eoQw_MkHi3Fs5LFWCA6xVyBbAriaKblpUerEBDxfIkNQOtcnooy_9ErF7mZOyzvooG3goTYSImiNXJ4TU2M67wM2Au83TnhGFRXXlf9mhFvaawC-4D2cWfTD5uSPUhcYlTuqu9g5UP9f_fck0JiDSfGX5gckKXOWhnnYLOy3CBjMw9iB6UIS7e9zh0ggOio2K_uj-o0Sg67mro2NyUtRGndrx60AtowGNetoFMUSEO_ArdANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت ترکیه احتمال داد کودتای صهیونی آمریکایی(اعتراض مردمی) شکل بگیره و اینترنت مردمشو قطع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/138871" target="_blank">📅 14:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138870">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ قرار است امروز در میان تشدید تنش‌ها، جلسه‌ای با کابینه خود در کمپ دیوید برگزار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138870" target="_blank">📅 14:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138869">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9Mf7MB-fc6Q2TKXfusy7fsM5yR-XTE7EWs8dgEcjAXdsw8xrHRKss2uN1sQXypStU2T7T_KZ4P5Ut-txWnF-1aQnO0DfL7UnjHQMQ6wiGlV9XMDf7cbI9mpBD7DfmWlNAXSPxNF-cPh3OJrWQpMtj63okYqGDRRmhMPRkK0ejo-s3CmLQyDzeixgXcNL5YB6uqOtGX6Rgr3njiZjsGxnTp8pn9faL9ZX08zTug3LfTSi6IdQ9nLYaCqRoC92zLFJab5UuQYChZUakpXuBqNJNqVOJd4LJoG9v0Y6p4IdORV6uwKp23H_1B-UWKvTGRDUF6vlP2eVci_8fi6kercpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله نیروی هوایی اسرائیل به غرب شهر غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/138869" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138868">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کویت : از صبح امروز چند پهپاد
وارد حریم هوایی کویت شدن که نیروهای مسلح اون‌ها رو شناسایی و منهدم کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/138868" target="_blank">📅 14:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138867">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0HU3YhjIGc1TudVbe4YJMNy71pdm0EWY170eJQTMnql-vFZxEyCQsOamWWxGk5lTEmROCV-iOmgUPBrx9beHSm6QdHo0BMKjRiEyubTe-IO32gPa8YjpcFAcAL2Idsf9fzaujB55DfhwumScf6EmJeI66-fpInHIUYmA38knPB6b68hDiQYpIqm269hdlnNhvbQdr3Idi-OdN5u1PrWPWIDxCh06s3Xze-5TIV2syPKZKq45WRLlZdCdlhhL4O_T-oL3qPbuTRZhGjmLO7jwN4i_Uj7VXmQhyako0P3azPhZeGkP5fv3CO9ebBMyQXOmbkASk9o0wrEOjVC5zRU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در یک مصاحبه، از یک مهاجم مراکشی می پرسند که در کشور شما جنگ نیست، پس چرا دارید به اسپانیا فرار می کنید؟
🔴
‏او می گوید چون در مراکش مردم مرا اذیت می کنند. من همکارمو کشتم و پلیس و مردم دنبال من هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/138867" target="_blank">📅 14:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138866">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل :  اگه ترامپ از ما بخواد، به حمله علیه ایران ملحق می‌شیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/138866" target="_blank">📅 13:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138865">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی آتش‌نشانی تهران:
دود مشاهده شده در آسمان شرق تهران، مربوط به حریق ضایعات و فضای سبز در محدوده جاجرود است.
🔴
حریق در دره است و آتش‌نشانان در حال اطفای آن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138865" target="_blank">📅 13:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138864">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4La_MtauETFjOTDWWCg_cYyi95BqYiv7aBWR9Ingk5vXAc3GZf9JkKUX0O1ewVj9n9KvtntOoT3ik_TqK2FFSYOFYTIWXHvhmwTLlaeWTGaPuzwVfnay23U-XlRf8Br9aDaYGqsoeHpFH1HDPVe0UwApfRBLAGDvHkGGgUAbfX-k334eXQ7N-yMj8Zptdbx6-V-SA5aUsJyT4df9c3JI3wGKcEUzXutkTEoWu74iufcGJdxaUDpP3v9rEjwp_0vL5emCBOALAt0UI32As1QpCw1bQaMTWbHFxIjslmxxDkTmmZoBJ8uJBviggInEpdeI4vxuPRolr185jZVwn13IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت در ترکیه دچار اختلال شد
🔴
بزرگترین ارائه دهنده اینترنت در ترکیه در حال حاضر از ارائه خدمات باز مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138864" target="_blank">📅 13:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138863">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
عباسی، عضو کمیسیون آموزش مجلس:
چون کنکور یک ماه دیرتر برگزار شده است، سال تحصیلی جدید دانشگاه‌ها نیز یک ماه دیرتر و احتمالا در آبان‌ماه شروع خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138863" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPDQ9zkiMpHBqR4LlnyvO0hhLN-o-OVkOUUnvo6iGPEYjLr5b-IWheVefM97uYaycXlggP9KQuPTrk0meuq8PkEDY8hu9f9fvuu_BhjNKFIwznBikwNc7zaEQNMSRHDLLGTUZUaVLNhQTZlBj-gWDfnStE1sCjqNoI-GXw8vtkE51puu_pOtSVLFO_uzDVOLlb9gRi4683nF1hq-D-rRLIMxd9Xj1qOSlLai4KX4AoG1RyrQBqocgbLSvYoamnbxj3T8r-ukHPAWFzI3G-sYsUf-dl0AZPDPyM28PsEd2ujyceARoCjXLg6jYQuYcl_wrB1SopCTpNHuGMnuQYjX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعتی پیش انفجارهای در تنگه هرمز رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/138862" target="_blank">📅 13:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
منابع عربی: ایالات متحده، کشتی قطری را از رسیدن به پاکستان منع کرد، زیرا این کشتی به جای مسیر مدنظر آمریکا، از مسیر ایران در تنگه هرمز استفاده کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138861" target="_blank">📅 13:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138860">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c38ab5a46.mp4?token=C0h-zFc4ewlO33tuz-bdypYmJqEuxvD6bsMMmxlFIv-TTZOjqGqvwXuLx7_qY3ARknjvNrq7GeexJcdN6ZfksV-t0zQ09Vi2x-fKH98RGKFPGTmJs7fJI4kHrPRExjAslasXNbwtnYcPTq-D9CfHLu-fhO3UCux2Z-wQ6bfLHhsch4_isQLrG05dpQzMp2uAQKuBjDhMw3S3RG58MUv5oRi_phfE17ClWPyhBgNLSDM1nFITSzBU2gc--QMndR8ck3sO6v6_CqhgVdH5n4fl8dEB6YqRC3Dw18vZwfI7eZf4Rd1wrvMHVSc_6w6KdfB99b6SwLUTfndireIvVaqqJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c38ab5a46.mp4?token=C0h-zFc4ewlO33tuz-bdypYmJqEuxvD6bsMMmxlFIv-TTZOjqGqvwXuLx7_qY3ARknjvNrq7GeexJcdN6ZfksV-t0zQ09Vi2x-fKH98RGKFPGTmJs7fJI4kHrPRExjAslasXNbwtnYcPTq-D9CfHLu-fhO3UCux2Z-wQ6bfLHhsch4_isQLrG05dpQzMp2uAQKuBjDhMw3S3RG58MUv5oRi_phfE17ClWPyhBgNLSDM1nFITSzBU2gc--QMndR8ck3sO6v6_CqhgVdH5n4fl8dEB6YqRC3Dw18vZwfI7eZf4Rd1wrvMHVSc_6w6KdfB99b6SwLUTfndireIvVaqqJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه در واکنش به تکذیب‌های سنتکام تصاویر انهدام یک نفتکش در تنگه هرمز رو منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138860" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138859">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
تلگراف : آمریکا و اسرائیل درباره احتمال تحمیل یک محاصره زمینی به ایران بحث می‌کنند.
🔴
این پیشنهاد، یکی از طرح‌هایی است که رئیس‌جمهور ترامپ و نخست‌وزیر نتانیاهو برای افزایش فشار اقتصادی بر ایران بررسی می‌کنند.
🔴
چنین اقدامی مستلزم آن است که آمریکا و اسرائیل از کشورهای همسایه ایران بخواهند مرزهای خود را با ایران محکم‌تر کنند یا ببندند و تردد کالاها به این کشور را محدود کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138859" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138858">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=H0aNX9E_I7SWQKuNXlvXb-CTIjs_C12JRt2SgRyMgy1Wi5BDkJPcyLIi288SVsASxQefD91MdiRipTjt87RFBmShAUHtHk1wd8PexFz0n0r94oNHQSEw_fDjqifx5sV18NnKwO3JVgris3ADrj64EDua2Fc7eTCtdcBLHW1HAOZgv1sKzLVkzG7wQfltw1aL5ICyt2g4EEQLxQcyZ5WOhiUVbkn8NA3zMB7DeMCFZad-Xc6-qtEU-NjrvFFIwv5oomovF8RP-AAy3bYNXLooSHwXruX567hWwfzvlf39OybOW9YH3sHwfv7edN6i1zKFJaC-pz3gZswMecT5OhtT7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=H0aNX9E_I7SWQKuNXlvXb-CTIjs_C12JRt2SgRyMgy1Wi5BDkJPcyLIi288SVsASxQefD91MdiRipTjt87RFBmShAUHtHk1wd8PexFz0n0r94oNHQSEw_fDjqifx5sV18NnKwO3JVgris3ADrj64EDua2Fc7eTCtdcBLHW1HAOZgv1sKzLVkzG7wQfltw1aL5ICyt2g4EEQLxQcyZ5WOhiUVbkn8NA3zMB7DeMCFZad-Xc6-qtEU-NjrvFFIwv5oomovF8RP-AAy3bYNXLooSHwXruX567hWwfzvlf39OybOW9YH3sHwfv7edN6i1zKFJaC-pz3gZswMecT5OhtT7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رائفی پور: بصورت زمینی میتونیم بریم اسرائیل رو بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138858" target="_blank">📅 13:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138857">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f540d88d.mp4?token=flMqQ6OjQdbJEqTlD74prO-bAm3FV9Zw8Hw-zD7KN6CfPZRsaGjISeuNH461ataZV93TvjdIQcBbzRoAoForvJlXi3iBoGFxNvwrvdKNuV8egQHCvYDVuHmvsF1yBq-7MbzXYdsAa_COvDkkmddZ1ZHFixXeTrZ8eAFxjfYSHlqzxHDStQNyf0cbACNphZ-IpOR91m8knGRet-ZazHGkUaXVbc1dFroopL0g5DDmIAsG94aiKwZUpF5xg_6A7PtNIPMij6MxHZMoSOpIqXMP-TSS96lOpOLXd5eM6TqVh0vOn_WYFBb14fPzuQpTghaWmRuufoKJH6QPmKy-IIxxJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f540d88d.mp4?token=flMqQ6OjQdbJEqTlD74prO-bAm3FV9Zw8Hw-zD7KN6CfPZRsaGjISeuNH461ataZV93TvjdIQcBbzRoAoForvJlXi3iBoGFxNvwrvdKNuV8egQHCvYDVuHmvsF1yBq-7MbzXYdsAa_COvDkkmddZ1ZHFixXeTrZ8eAFxjfYSHlqzxHDStQNyf0cbACNphZ-IpOR91m8knGRet-ZazHGkUaXVbc1dFroopL0g5DDmIAsG94aiKwZUpF5xg_6A7PtNIPMij6MxHZMoSOpIqXMP-TSS96lOpOLXd5eM6TqVh0vOn_WYFBb14fPzuQpTghaWmRuufoKJH6QPmKy-IIxxJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستونی از دود در میدان نفتی الاحدب در استان واسط عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/138857" target="_blank">📅 13:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138856">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmMUmw3Qr8zE9_waObvwPi_MKRcx4skI3EgeYQ4I96WJ7ER4ChmXWhCdgyYdIr6yzfhdfZoJ81nxfIilt7N7GlHgE-UoFy_fhv6WBSkYVULLDtjDvTrUSdfrzjGfUEjbs2R_YBLkt3ErK4VYxoIMuwe_fR6eQ9c9o6xIXQWvyoMYbmq6IzekaLOmu5P43eOHRbhyVN43aTIHLna5_V02Rhz1O0Yx4af72eKZMFd7Ddom61A-j7IyQyruVPHONNsx_3soe1wTiPmVFeH29S6RqNMXc2QW6_RQ2SwX0ohd0QvAmHUupE-91o_nHpj5hT3WCGsswG05pcsRk73Uvef_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک سوخت‌رسان هوایی KC-135R نیروی هوایی ایالات متحده که در یک برخورد هوایی کشنده در مرز عراق در مارس ۲۰۲۶ درگیر شده بود، برای اولین بار پس از حادثه در فرودگاه بن گوریون تل‌آویو روی زمین شناسایی شده است
🔴
این هواپیما با شماره دم ۶۳-۸۰۱۷، در برخورد با یک KC-135R دیگر آسیب دید و با بخشی از دم خود که گم شده بود، فرود اضطراری انجام داد.
🔴
هواپیمای سوخت‌رسان اکنون در حال پخش کد تماس "RCH564" است که نشان می‌دهد تعمیر شده و ممکن است به زودی به ایالات متحده قاره‌ای بازگردد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/138856" target="_blank">📅 13:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138855">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAIJj9LS26Mtp1ekMKn0jUOPd_ucGG3RiRd1wEzsoQpQQF9h2eMzfmYtljcC-FEqR_1ZtfYvXsZ2fI8UYoA4ByIxQAmicGYl2bIOa_3WKuEcenraCBegB9nluHPHg23-jjANWY01_9XiB0vu0W3C2tJg5tpeWGIQyDcfr-kXcoSdIggkkA5RPXyAxm5GMOZlf8ujvgi8yjwV6wCE6cykJPzyoSJxuyRGondZtCjPCRWxzMh4G2vfElpwG_HlPkwU4Bw8e7A-nDouWvuGZVjw2dRyvXEIhY1ccHqgYjTGqXJeJoCDo-L1mm1-_OA3P98R7kflJeEFHJH4XtZ2Y_f74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده ولی فقیه تو‌ سپاه:
آقا مجتبی خامنه‌ای رو
خدا
انتخاب کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/138855" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138854">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی 4.6 ریشتر، ظهر امروز منطقه دیباج در استان سمنان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/138854" target="_blank">📅 13:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138853">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
روایت سی.بی.اس از رقابت نتانیاهو و بن‌سلمان برای شکل‌دهی به سیاست ترامپ در قبال ایران: سعودی نگران است نخست‌وزیر اسرائیل به دنبال تشدید بیشتر درگیری‌ها باشد
🔴
نتانیاهو سه پیشنهاد به ترامپ دادن، از جمله ادامه محاصره و اجرای حملات علیه مسیرهای زمینی انتقال تجهیزات
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138853" target="_blank">📅 13:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138852">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a7007d893.mp4?token=PaBscM-lo_S9RQlCndXAx86W28ao_H_gNXpWgVNJOM-IsRiVx_X_J1CPTT6DHMc0F-74z38MeMRM8Qck52sf4ptcl8FBi-EchmpLMRyYtY6jks_ubPi4gFM6PTfsNRZy0dMpmbfleKxL2dxF16e9YBV-AI4fPAA89dO3CA_xJrDb1s1lwXmGnwduSOc5gZpGgTXaO4xNrORKtKh27-2thQShjQIYaJE44LViGRdswso4IJMn1xw_ovuK7heAGGua8M5By7cFKjqCWEDyl3bpCLTSVgga4bVlrp1q4WcjRDh5jLbc92wElx5yik-7cLbISs43-h8-TWnJfPxgx2Xa4XwqhROvlDNzYAdoBIQFf5Zsd7k3LzSWVhWh960yM2C_TeZlBqaojB_ATjWIVGt7XyW9s843yYF9yp3l_hy-uxzolRgHaxdJilGL7tw6dGyE-hKEFfHMjPqPbB45IjWEEcS_9gv0hAvH5eehX6sj-ZLRmMO_HKlMY4egvdJsLdblqcKOSpplVRuPVTFldIrOSAWuQMw4W4aM6ggUYocP-OXMTSWSIfmN75b_-wapz848z-LF9ukYLjKZshaJs_vcITpJX60vkXBEitUAxJJ22I39CRAX9PxMB1rOf39UzenH809ufqxaQ5JTmbDdqxKiDJXmQWlFXnFtK_lUHvG2lJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a7007d893.mp4?token=PaBscM-lo_S9RQlCndXAx86W28ao_H_gNXpWgVNJOM-IsRiVx_X_J1CPTT6DHMc0F-74z38MeMRM8Qck52sf4ptcl8FBi-EchmpLMRyYtY6jks_ubPi4gFM6PTfsNRZy0dMpmbfleKxL2dxF16e9YBV-AI4fPAA89dO3CA_xJrDb1s1lwXmGnwduSOc5gZpGgTXaO4xNrORKtKh27-2thQShjQIYaJE44LViGRdswso4IJMn1xw_ovuK7heAGGua8M5By7cFKjqCWEDyl3bpCLTSVgga4bVlrp1q4WcjRDh5jLbc92wElx5yik-7cLbISs43-h8-TWnJfPxgx2Xa4XwqhROvlDNzYAdoBIQFf5Zsd7k3LzSWVhWh960yM2C_TeZlBqaojB_ATjWIVGt7XyW9s843yYF9yp3l_hy-uxzolRgHaxdJilGL7tw6dGyE-hKEFfHMjPqPbB45IjWEEcS_9gv0hAvH5eehX6sj-ZLRmMO_HKlMY4egvdJsLdblqcKOSpplVRuPVTFldIrOSAWuQMw4W4aM6ggUYocP-OXMTSWSIfmN75b_-wapz848z-LF9ukYLjKZshaJs_vcITpJX60vkXBEitUAxJJ22I39CRAX9PxMB1rOf39UzenH809ufqxaQ5JTmbDdqxKiDJXmQWlFXnFtK_lUHvG2lJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو سرباز روس هنگام حرکت؛
با (ATV) روی مین ضدتانک رفتن و انفجار رخُ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138852" target="_blank">📅 12:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138851">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02807afcad.mp4?token=kBGAAH-fDqPDHnHeC9OHdoVVTJUJLF95menqiCgf6izCSEMC3FpI2zKORnh57gDcomKjND5QQR-FnibJZrGg4IoUB50zz72uOwiKz0Orlq94AL7UzjIuR9CospjGp7tcD7YiQRPKPsNhxxrg0hrLfy5_CU4ONGDj7vZ9C60KVfO1IO8RwJXrfmwV-dyx3k4NrsHmzDs4cVGJKtGpVeuC-v4m5td4UJLGjOsrD-KsPV2yNQFXWbm1VtnScBjyIranUOzkIgrG7Smu_PYqsq-HiipZ7_X5YHxc3eXms2LnDTUzxlaeLPKrRBqkWBrzDn7H2HUPe4aEGswtpl0ygS3UQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02807afcad.mp4?token=kBGAAH-fDqPDHnHeC9OHdoVVTJUJLF95menqiCgf6izCSEMC3FpI2zKORnh57gDcomKjND5QQR-FnibJZrGg4IoUB50zz72uOwiKz0Orlq94AL7UzjIuR9CospjGp7tcD7YiQRPKPsNhxxrg0hrLfy5_CU4ONGDj7vZ9C60KVfO1IO8RwJXrfmwV-dyx3k4NrsHmzDs4cVGJKtGpVeuC-v4m5td4UJLGjOsrD-KsPV2yNQFXWbm1VtnScBjyIranUOzkIgrG7Smu_PYqsq-HiipZ7_X5YHxc3eXms2LnDTUzxlaeLPKrRBqkWBrzDn7H2HUPe4aEGswtpl0ygS3UQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آزاده آل ایوب(خاله نرگس) مجری برنامه کودک دهه ۸۰ و ۹۰: تک تک بازداشتی‌های اعتراضات رو باید اعدام کرد و نباید به هیچکدومشون رحم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138851" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138849">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d9b65cfa.mp4?token=eQSQIXsR7A5CfeHnSkz6km0cQIabTSBUD2Lc9iu8xBKjQNkHt1RRYLpI3oo73z4p31RmviW9ibGA3nFCuvZ6NYUgqutKzKPwQv4Dp7NX1l0JyfGI8HlujSvCX5gilDm6NJHKwrnVjwkJVNBOvD55kX83MoA5_jy4l4QdyytnAw7n1xCBWyhzKgieXNYT9UQCsudqaH1FhNRb9GvpZJmhyLkgJa7Ak7M4PjIHAgSf9mK2i1o0yLwaQMFN3kWM0hEYBzdbZ4UvhD_m6XODmYKPtg_2ROOCxJfa7ZBV_a85UfYLQxtpabli-pmq8aR2J5DneA9zVRWuKml2egvBPr9AcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d9b65cfa.mp4?token=eQSQIXsR7A5CfeHnSkz6km0cQIabTSBUD2Lc9iu8xBKjQNkHt1RRYLpI3oo73z4p31RmviW9ibGA3nFCuvZ6NYUgqutKzKPwQv4Dp7NX1l0JyfGI8HlujSvCX5gilDm6NJHKwrnVjwkJVNBOvD55kX83MoA5_jy4l4QdyytnAw7n1xCBWyhzKgieXNYT9UQCsudqaH1FhNRb9GvpZJmhyLkgJa7Ak7M4PjIHAgSf9mK2i1o0yLwaQMFN3kWM0hEYBzdbZ4UvhD_m6XODmYKPtg_2ROOCxJfa7ZBV_a85UfYLQxtpabli-pmq8aR2J5DneA9zVRWuKml2egvBPr9AcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بخش هایی از مصاحبه محمد عرفان؛ بازپرس سابق جنایی:
ما همیشه از اعـدامی ها میپرسیم آخرین خواستتون چیه و هرچی باشه اجرا میکنیم. یکیشون گفت آخرین خواستم نیمروه. نشست ۱۵ تا تخم مرغ نیمرو خورد و بعدش اعـدامش کردیم.
یکی دیگم بود میگفت آخرین خواستم اینه که با خانوادم صحبت کنم؛ هرچی زنگ زدیم تلفنشون مشغول بود. ماهم دیگه اعـدامش کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138849" target="_blank">📅 12:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138848">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b1eec1722.mp4?token=ZTTChgtycse8SpSiGpEAfx5Oce7y321ZdXalIGbZ0JVcJGsBeu0zvug9pr8aV7Kn4u1bv_rb2htzHcy9siKl7S-fyyjtB1ZPVgbLYEoEYRpARjhqDUBtzvFOg0Yv4DoSSrzUvYZids8nBbZrzT-ynHxnw8B8Bq8BpLnOn-YT6mlOXSHH-QyxDvc3ib0xA0Dip2Kedl-fFBIDLKlwv4z9YoPUhh6Vz-FivKHfB6xV0NOjZV2-AwapkSQFAYIcHIHxAkE5ck5RF0zM1_vKQ_U79BNHSq8soeTjxJ0huDWC538zdCcr5dpcZxXS3DcTCJs76-gmZuuLsY2WIGNcfk_2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b1eec1722.mp4?token=ZTTChgtycse8SpSiGpEAfx5Oce7y321ZdXalIGbZ0JVcJGsBeu0zvug9pr8aV7Kn4u1bv_rb2htzHcy9siKl7S-fyyjtB1ZPVgbLYEoEYRpARjhqDUBtzvFOg0Yv4DoSSrzUvYZids8nBbZrzT-ynHxnw8B8Bq8BpLnOn-YT6mlOXSHH-QyxDvc3ib0xA0Dip2Kedl-fFBIDLKlwv4z9YoPUhh6Vz-FivKHfB6xV0NOjZV2-AwapkSQFAYIcHIHxAkE5ck5RF0zM1_vKQ_U79BNHSq8soeTjxJ0huDWC538zdCcr5dpcZxXS3DcTCJs76-gmZuuLsY2WIGNcfk_2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهروندان اسپانیایی در بارسلون اسپانیا، در حال نصب سیم خاردار بر روی بالکن های خود از ترس مهاجمان مسلمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138848" target="_blank">📅 12:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138847">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سپاه : دو نفتکش متخلف تو تنگه هدف قرار گرفت و متوقف شد
🔴
۴ نفتکش دیگه هم بعد از هشدار، مسیرشون رو عوض کردن و برگشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/138847" target="_blank">📅 12:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138846">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU-QY2X4YXtZq8oq7_5YRuUHQQ28rVXG6gjIJwoGamIpBVuW0LIsdsPv3xr_fRsisRtpjQTxtKAIp0X58xf7xvhMN9eSA8RyjhcNE3sElO4zDhXrtjbAH6o_TItYkNl3Q4VJeADtQYgBVfDUbu4t3H5MNfDj6LIUROwZ3TlhpTXAuxawD-2GeRyWjBJb6QzQo0w_cbvepKan12HfvfBgA7tQoTU1PLXTJjKPoys01x3Sjw-TWuwDxMOdVJ1CMDVpE9OrT0F7SyF4O1JHd3KMMx7ZOjzEN27zvtvWsYeoKQ3FFQ6yzUDOWjrTn0nPpWvPKq30ILJ9JMIPrEMkfAYaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مسلمانان مراکشی به منطقه‌ای خودمختار متعلق به اسپانیا در شمال مراکش حمله کرده‌اند و تقریبا این شهر یعنی سئوتا را فتح کرده‌اند
🔴
سئوتا خارج از خاک اصلی اسپانیا هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138846" target="_blank">📅 12:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138845">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDC9BI6cYFLw0KWVJqOgP0glrXYebVnylptieSjwTNSixkeXyd2H7d0Qt2xLDFgyvVPmIa_U4QikGrIp8hasCB1-PWduikeAWPl_L_z5zuT0fMztOOdlVrVP-sIbVTZZl-h3O7nqLDmJMnzkiJZzjNZVN52uAV1oyJyzMVxqJK1gncObpokb7HOge8aN-ZeWC6UTFixPPr-zdncFRTwJbtgrxoZVCZjHkGm5bT9n7MSuQn-f73IkS3SKvMUgybXJGGY1xLFDWmCtOWTLiH5SAeeo9Xr8RMZGcHW-t359m0Yhts6dMN0fnWnSEpoXsyNDt1WxTmI_Hx1EGRikDTEPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از پشت صحنه «مرد سه هزار چهره» به کارگردانی مهران مدیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/138845" target="_blank">📅 12:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138844">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1225749b49.mp4?token=D66rxxH8s5unHRB6UcUqcGxTX5GQGw6OJ7lIxaIlYw6yQ02N_s0q1eG0EKn-4etgil8upNqa2_zVKjGMKqa9BbujtpWubxG_zrfaaQSbIUssKu-RufTAeIK27vPmQ_1-8id3f4t9FBbpo9rwBCvla7vEj-XaW9nkIxHEw2a44wYNV-8i_QhG5R7s2tEWtFD4gGTwitmI965veOB71hvfx98w1OSVavjp8zqZqrGz3_wUF-uwb4VONCFLVk_txXwmOviGylCS4BLcp5dP2xz5BkOvPQRMci9Bz4LbWsOsT0arUVW0alAMRPJXD6rf7mW2JZJNUPOajcYjM1jSePR8JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1225749b49.mp4?token=D66rxxH8s5unHRB6UcUqcGxTX5GQGw6OJ7lIxaIlYw6yQ02N_s0q1eG0EKn-4etgil8upNqa2_zVKjGMKqa9BbujtpWubxG_zrfaaQSbIUssKu-RufTAeIK27vPmQ_1-8id3f4t9FBbpo9rwBCvla7vEj-XaW9nkIxHEw2a44wYNV-8i_QhG5R7s2tEWtFD4gGTwitmI965veOB71hvfx98w1OSVavjp8zqZqrGz3_wUF-uwb4VONCFLVk_txXwmOviGylCS4BLcp5dP2xz5BkOvPQRMci9Bz4LbWsOsT0arUVW0alAMRPJXD6rf7mW2JZJNUPOajcYjM1jSePR8JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هشتاد جلسه‌ی دادگاه برای اثبات جرم حمید نوری از جانیان شکنجه‌گر دهه ۶۰ در زندان گوهردشت در سوئد برگذار شد که این حرام زاده محکوم شناخته بشه که البته بعد از چند سال هم تاختش زدند و به رژیم جمهوری اسلامی برگشت.
🔴
برای حکم اعدامی که به محسن شکاری دادند فقط ۱۷ روز وقت گذاشتند.
🔴
حالا چطور میشه که کسانی که در دی ماه خونین بر اساس گفته های رژیم جمهوری اسلامی تعدادی از نیروهای انتظامی رو دستگیر کردند، شکنجه کردند و بعد آتش زدند ، بررسی مدارک جرم فقط در مدت ۶-۷ ماه انجام شده باشه!؟
🤔
مردم به وقتش پوست از کله این حرام زاده ها میکنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/138844" target="_blank">📅 12:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138842">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6414829db4.mp4?token=bm_16AGLk8TWi09895ZMAZJsTA_kkemtEhSGtXES76VktjGM7SBP5kKcDsGXHAw1-FGgtBnC9n2XWTj39Gl9g-zZZniZQmSDWRmprOWCjvYbyGt70jAoeRgU0TpI80XXzkW6h8zkA6A2t6QTjtrkl3_SPuFexKfaNkKfBfXxXHe-IgKvhAtsIjdWIfAd-JS1UA_OvnY_41YsxF80dREo-yftpHh5tCJiq6zaKH8Nd2mnhqKpPqJAkHZj3xqW7Bte2jpnaEjj1EC6rnpO1yqFKJ3YyjjwojIdO9ev5boZqUKyQH4Fxa8I4cytjXycJ_fRV87-YavynWEEc8dsqBjHQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6414829db4.mp4?token=bm_16AGLk8TWi09895ZMAZJsTA_kkemtEhSGtXES76VktjGM7SBP5kKcDsGXHAw1-FGgtBnC9n2XWTj39Gl9g-zZZniZQmSDWRmprOWCjvYbyGt70jAoeRgU0TpI80XXzkW6h8zkA6A2t6QTjtrkl3_SPuFexKfaNkKfBfXxXHe-IgKvhAtsIjdWIfAd-JS1UA_OvnY_41YsxF80dREo-yftpHh5tCJiq6zaKH8Nd2mnhqKpPqJAkHZj3xqW7Bte2jpnaEjj1EC6rnpO1yqFKJ3YyjjwojIdO9ev5boZqUKyQH4Fxa8I4cytjXycJ_fRV87-YavynWEEc8dsqBjHQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اگر براتون سواله چرا این همه وحشت؟
🔴
چون دیشب مهاجمان مسلمان که تازه رسیده بودن به اسپانیا، ماشین های مردم را به آتش کشیدن و آهنگ های عربی را در خیابان های اسپانیا پخش کردند و به خونه مردم وارد شدند و از آنجا دزدی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/138842" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138841">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=MI-dX3SpRnl287hZECMqKiO9ffTpb0GPD7wwh9CFdRdRE7OXfDv2xWniD4xeiqdv6z01mrJZdXBcGu2Gchc42d3CWWi3g02V5d1ds5d0Qrbtjg_K-GCxIfD2sSWpd_huo0veTXi2lHAJBIR7wXwwp18so9ppL4BhEmE1AMQfeYxG0iGDY3vGSarPZ9xRSFHciDidaRG1ike8durxjso2PK7gGKc-WO4BfqFxsvreVnuEIJg9GtotbYXmnV46RwfYOEEK-CVOFinCNaMW4yinMGVM8usfO_z8CRFVfy1dGFKgMgaebCKoi18rFOxc1WD5Y13xBCbR70bf49xyq-1gNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=MI-dX3SpRnl287hZECMqKiO9ffTpb0GPD7wwh9CFdRdRE7OXfDv2xWniD4xeiqdv6z01mrJZdXBcGu2Gchc42d3CWWi3g02V5d1ds5d0Qrbtjg_K-GCxIfD2sSWpd_huo0veTXi2lHAJBIR7wXwwp18so9ppL4BhEmE1AMQfeYxG0iGDY3vGSarPZ9xRSFHciDidaRG1ike8durxjso2PK7gGKc-WO4BfqFxsvreVnuEIJg9GtotbYXmnV46RwfYOEEK-CVOFinCNaMW4yinMGVM8usfO_z8CRFVfy1dGFKgMgaebCKoi18rFOxc1WD5Y13xBCbR70bf49xyq-1gNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روز دوم تهاجم مسلمانان به اسپانیا آغاز شد.
🔴
خیلی از اسپانیایی ها از پادشاه اسپانیا خواسته اند پدرو سانچز را خلع کند و ارتش اسپانیا را به مرز های جنوبی بفرستد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/138841" target="_blank">📅 12:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138840">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr0zqmSQMeMMgAa5cYG7YQ4WFgfHhK-kQi7uZpdMQhq9-sTLjob55ylFMFdnSvYMq1-StB6ta_ewAm_EfN8mY68fe-fGT3WqZuAy5pQEW6x3hHmrm6AGJjMWe8ySEX1_4M30V2vIspU83xaccsFc6dc0wyi3pDRaM3sXPlHdb617pJjO--sCY3_JIThBfAaw1Hb8UXSlkRLR_rNgSspp4eMIvXNgXfVFoQmgUpMNlMkEEhxxKYdiUnBPhtnXoNX2giwt4mG6BKuhPVaqe2WQ_vL6To1IfSDC-DHC0DBdKS_t0PyuFJnLGY8K0wBoPI3T5b2LfG4uNNQYomn9hnLhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار بلومبرگ: جالب است که سنتکام هیچ حمله شبانه‌ای علیه ایران انجام نداد. خیلی زود است که بگوییم آیا ایالات متحده به الگوی اعمال محاصره برمی‌گردد یا خیر. و اینکه آیا این نشانه‌ای از ادامه مذاکرات دیپلماتیک است (یا خیر)
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/138840" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138839">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DITrDiAFZB0xu86-3fMQGmCKO09pt-byGvoG37rRuDcX-lyi27429ZU3UGpGcfSndkgZk6cJj6wXhQVR9rDoZxDxRN-o_odI6csbHuA6G2zXCLIVbRH76cztQbx0FLmi56vWzDSm7Ku1kz5ZalHjqbMNwg8MMZGgaDPRrYXgmoHM4Vzy-rkthHDC4mLsrBxk5fR-wpOEJlCF3g6dSMgdE6cVjkVpNM-5asCkxGVIemtb8UEQIhtsb7mBlGobpcUIFBQOhJXU3VXj-BBFSE1LkQv2lJWjj_5ij_J8b6Ec2-LUQrCY48_-XQDnMI-wgG1LZki_hmiCHVug6uwAAF4JkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138839" target="_blank">📅 12:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138838">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
حادثه امنیتی در اسرائیل /منابع عربی: یک سرباز، سلاح یک نظامی را ربوده و به سمت سربازان ارتش اسرائیل شلیک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/138838" target="_blank">📅 12:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138837">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
بلومبرگ گزارش داده شش نفتکش سعودی پس از تهدید حوثی‌ها علیه کشتی‌های عازم بنادر دریای سرخ، مسیر خود را از تنگه باب‌المندب تغییر داده‌اند.
🔴
دو نفتکش بسیار بزرگ به‌سوی جبل‌الطارق و چهار نفتکش دیگر به‌سمت بنادر آفریقای جنوبی می‌روند؛ مسیری طولانی‌تر و پرهزینه‌تر که نشان می‌دهد ناامنی دریای سرخ حالا مستقیماً مسیر صادرات نفت عربستان را به هم زده است
🔴
یک تهدید، هزاران کیلومتر مسیر اضافه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138837" target="_blank">📅 12:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138836">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
بر اساس گزارش‌ها، نیروهای سعودی مشاهده شده‌اند که از مناطق شرقی یمن عقب‌نشینی می‌کنند، که احتمالاً در حال آماده‌سازی برای یک عملیات نظامی زمینی علیه حوثی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138836" target="_blank">📅 12:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138835">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a16a391bce.mp4?token=OWxbxFW05EWruZLI-2wsBKTF0UgSPXWM3qjoVn2t8oAZT2XsU-Clllivpg3bdT6fy8UJaa43hxgCOB747Xh3_UgvJGAiLVvz_-qFteS4dZQN-qSlvoLliyGK88iGWV0jIrAwvb6I5PhwvNchjYvYPc2Ce4AySKtEGUeYACwdah0DNjZO7IuzUpjPQqFOTRpLm7BWWrcacyQFhwqEMqvhzApRU17xt79kpk3H-mM2ITpREXs3WxC-tBLIpI_eKpKCGWr-6aMlInrc7VzRgPXL37hX9FheoLQZqIbSCB1Y4gtckWY9uBRIv09WK9ROACHsKtVoH_qQJeTuw5rrpCoE4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a16a391bce.mp4?token=OWxbxFW05EWruZLI-2wsBKTF0UgSPXWM3qjoVn2t8oAZT2XsU-Clllivpg3bdT6fy8UJaa43hxgCOB747Xh3_UgvJGAiLVvz_-qFteS4dZQN-qSlvoLliyGK88iGWV0jIrAwvb6I5PhwvNchjYvYPc2Ce4AySKtEGUeYACwdah0DNjZO7IuzUpjPQqFOTRpLm7BWWrcacyQFhwqEMqvhzApRU17xt79kpk3H-mM2ITpREXs3WxC-tBLIpI_eKpKCGWr-6aMlInrc7VzRgPXL37hX9FheoLQZqIbSCB1Y4gtckWY9uBRIv09WK9ROACHsKtVoH_qQJeTuw5rrpCoE4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک عبور مهاجران از مرز و ورود آنها به شهر سئوتای اسپانیا را به آخرالزمان زامبی‌ها تشبیه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/138835" target="_blank">📅 12:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138834">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/094c83504a.mp4?token=VCGYQ61Z_Y8Z3JrlQVAFrIKxTon4aDZa4b5E3Yg8KQaxEHHLqA2bSBInu8T-fmL-KKQOeQZUBNNYasSnYzHh9wA7XAA5YFQHQbrlb_61cNXN9ujR14lMVWPCd2bgQ5cAiG6IOUh11xymMgmKBPKXEp5svrckRWZscsdSM35gxVbCcqQbkFlmd3tO2Dfnk1K6iY0NLrhcJAEh8VpYgLslfEGglfGgQjQ5EKrrLwKymfii3vSt6zelz0YHNP5BREqflnS8i124xRcGUbzXkds54bedUNbCTK_rEPNt2vZfl2SRPP6Tb5PGLaLp1PajjemREJrN4XLsxj236xshFM9-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/094c83504a.mp4?token=VCGYQ61Z_Y8Z3JrlQVAFrIKxTon4aDZa4b5E3Yg8KQaxEHHLqA2bSBInu8T-fmL-KKQOeQZUBNNYasSnYzHh9wA7XAA5YFQHQbrlb_61cNXN9ujR14lMVWPCd2bgQ5cAiG6IOUh11xymMgmKBPKXEp5svrckRWZscsdSM35gxVbCcqQbkFlmd3tO2Dfnk1K6iY0NLrhcJAEh8VpYgLslfEGglfGgQjQ5EKrrLwKymfii3vSt6zelz0YHNP5BREqflnS8i124xRcGUbzXkds54bedUNbCTK_rEPNt2vZfl2SRPP6Tb5PGLaLp1PajjemREJrN4XLsxj236xshFM9-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوال : می‌دونید تا الان چند نفر از روس‌ها تو این جنگ کُشته شدن؟ آماری ازش دارید؟
🔴
زلنسکی : طبق برآورد ما، مجموع تلفات نیروهای روسیه به حدود ۱ میلیون و ۶۰۰ هزار نفر رسیده
🔴
از این تعداد، حدود ۷۰۰ هزار نفر کُشته شده‌، البته این فقط یک برآورد تقریبیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/138834" target="_blank">📅 12:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138833">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
وزارت خارجه چین کشته شدن یک شهروند چینی در کویت را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/138833" target="_blank">📅 12:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138832">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
بی‌بی‌سی: در ۲۴ ساعت گذشته ۴۹ هزار نفر از مهاجرین مراکشی از طریق دریا وارد شهر سئوتا اسپانیا شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/138832" target="_blank">📅 12:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138831">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgL-dGtmiSAveieYngbyiBwgZ-b-_-1gQlcZRWdQp6uMB6IHwMp3I7GwHFbKMArSQrlCFLBU88bsXglFtSn2skx9DF_HoEhjLQCygzbe-s5GVG6-5-EqXYF5kpfPFKG4taD4vPPk2dAzxkaKEBMGExutnwKfE8VYLvdfcU01cUo5Ilm0o8Ss23_SjjjEMS2uq_6c3iUe6sGM6owUterm6fPaDS513uVXdVdAE9PXfcYV3eX496JiXVKrWCJ8mFrw4aoVcL2ANgdzMPkiFbay4NJgUsJwpulZOq3HmhBjiy_N0JEInPkRZLcPxtRjGYTIN--MKpDwEXak_dA_Q8XOmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووری/زیرنویس شبکه خبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/138831" target="_blank">📅 11:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138830">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2b5c3f0e5.mp4?token=vUGvwX3Ck7R7daZ6SPMaJslk4YcYa3CqSDhxFjpDBtK7QwEY82HfMEI3g_BbnQxbFSeHI0hycjDFCHFtBZzO6_CSk0eJI2ACpGIljLzZitx19YtXKJNyiWdR6-FzoA4VJzHePGcNLIKIV5vWz0aGpd-xU-xkcw17_MVrA5zNEl1TBUEvVkf6YA-XxTXBwL2Y28cTJ5UrIJ2Qkjw8V8uaxm3WpD0vmtFyCUx-7Ft38ycPTBFEwCXOuXWwF5aCeAfwoVNAlESH3PBraZQxZNm1v6njT67XUEpVI5t3a00gbDy45on9QcTioLD1pP9nc_uDivgx8x6GDtPzlLFgbScKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2b5c3f0e5.mp4?token=vUGvwX3Ck7R7daZ6SPMaJslk4YcYa3CqSDhxFjpDBtK7QwEY82HfMEI3g_BbnQxbFSeHI0hycjDFCHFtBZzO6_CSk0eJI2ACpGIljLzZitx19YtXKJNyiWdR6-FzoA4VJzHePGcNLIKIV5vWz0aGpd-xU-xkcw17_MVrA5zNEl1TBUEvVkf6YA-XxTXBwL2Y28cTJ5UrIJ2Qkjw8V8uaxm3WpD0vmtFyCUx-7Ft38ycPTBFEwCXOuXWwF5aCeAfwoVNAlESH3PBraZQxZNm1v6njT67XUEpVI5t3a00gbDy45on9QcTioLD1pP9nc_uDivgx8x6GDtPzlLFgbScKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی هجوم مهاجران غیرقانونی که حصار مرزی را در ملیلیا  شکسته و وارد خاک اسپانیا می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138830" target="_blank">📅 11:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138829">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
بی‌بی‌سی:یک شهروند بریتانیایی به اتهام جاسوسی برای سپاه پاسداران انقلاب اسلامی ایران، دستگیر شد. او به جمع‌آوری اطلاعات درباره یک پایگاه نظامی بریتانیایی در قبرس متهم است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/138829" target="_blank">📅 11:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138828">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وال‌استریت ژورنال: آمریکا در حال بازنگری در حضور نظامی خود در کویت است
🔴
ایالات متحده در حال بازنگری در سطح حضور نظامی خود در کویت است. واشنگتن روابط مستحکمی با کویت دارد و این کشور را شریکی مهم در حفظ ثبات منطقه می‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/138828" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138827">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9Xq11_J_6S9-CkbaV3Y-QZ7yZPUrasBFWwV06vJIQz78AkjLbLHx2sQjfiATG_YqAiZJ8XLLmft-aaYVlHplxaXzD3WJ3fgua9QNOzrfeuyjI1_ACmxAug0jyrA67y7qHA9-_AqCUfPDYxyYaFuPahAO3KqGE1_1gL2U0klt3MQsJTHl9jQl8KoFH8_LjRz4EDwhh57PmGeDh5rd0PZYgzZuQHAd7flThq37hp2oT2euKub0A6Aw3C1JZfHHN2-TUzqUQFBtf3i5fC1M2tsUJBoKvaqNZ_hrVKhEXM6GDnkLz_m5In7adicSooJtCOzuTM0DhAAqU11XlOBJ5-IbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس: به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم تشییع جنازه علی خامنه‌ای، رهبر سابق ایران، به این کشور سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکند و وقت‌کشی کند
🔴
یک مقام ارشد آمریکایی ادعا کرد که ایران سعی کرده حماس را متقاعد کند که توافق‌نامه را امضا نکند، اما این گروه ترجیح داده به حرف آنها گوش ندهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/138827" target="_blank">📅 11:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138826">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
یک مسئول حماس به خبرگزاری رویترز گفت: توافق غزه باید به صورت مرحله‌ای اجرا شود، اما اسرائیل باید نیروهای خود را از این منطقه خارج کند.
🔴
پس از توافق طرفین بر سر متن این توافق، اسرائیل باید اجرای مرحله اول را آغاز کند.
🔴
همچنین، گروه‌های مسلح مورد حمایت اسرائیل باید منحل شوند. اگر اسرائیل با این توافق موافقت نکند، ما آن را اجرا نخواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/138826" target="_blank">📅 11:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138825">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=D7_as1YvZTPge_pNCbrbQraNyxt6YzRcxYDcpf97fp3PHj63eKWjdSqaVGvPKv60eVTfqDcWf-FS36rYbuUDbke55eDirUEYe_9FMiZUn8K4h15vzRAHRnIOAWmVxnjGnngMcd8BqOfhkleyIurtvokG-46UQlnX3KBwx6aajBA7-sC7q_bxWcoSnmqeg0WcfkquOhSU44lKCo9sJPvvrffjsFgJpncmAsbwcPJOy15Lv98tB_nwIA6k-SiIzrSB-6vzmRAF-teTJkzc6uPz_eC61-gumNzSrJA0hX63sGstTc5e5U0XUjmxHpkOh0pESNzXnX_TSMgyw4bZh5SRqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=D7_as1YvZTPge_pNCbrbQraNyxt6YzRcxYDcpf97fp3PHj63eKWjdSqaVGvPKv60eVTfqDcWf-FS36rYbuUDbke55eDirUEYe_9FMiZUn8K4h15vzRAHRnIOAWmVxnjGnngMcd8BqOfhkleyIurtvokG-46UQlnX3KBwx6aajBA7-sC7q_bxWcoSnmqeg0WcfkquOhSU44lKCo9sJPvvrffjsFgJpncmAsbwcPJOy15Lv98tB_nwIA6k-SiIzrSB-6vzmRAF-teTJkzc6uPz_eC61-gumNzSrJA0hX63sGstTc5e5U0XUjmxHpkOh0pESNzXnX_TSMgyw4bZh5SRqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جواد موگویی جای همه رو لو داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/138825" target="_blank">📅 11:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rctaq5prVhaeaPR7tuj_AWk9Cwm-uFc3OrGrI_gEtZ_7QytZEDSu6mxB2BSOT80lFFHTGxDiRHCsxICCIKSnxz3UO2IJtvkpLyupKLoOo2pZS9NONPXXc_mYnp8GwAUH3uUAuisnZ52qH4QKowclydysULTA3cSGlqH3XFKyirx4iofmJ5slHPPTMF9gb88Mxoq_t503jJCMZkNYJGo1m8bLq9RxOEeiy670cXnTVzFziVTDAczAdf5HGL3WpEIQAFDztSsv6Yhg5cr1SRaw0LpfZ1zh1P060l_ivMLddOgvBI6LWXC0FsEp9apKjk8PnVYzNRPVS3QFWXM36sRtXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: فک نکنم‌ جنگ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138824" target="_blank">📅 11:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ارتش روسیه به وسیله کوادکوپترهای انتحاری، تعدادی از پمپ بنزین های اوکراین را منهدم کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138823" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hsnf-MACyQJoRr0xPnE28rgxuFHvZfg5iDblUEVwp4iN7CP1L4Sd-Xreb-vGL-5eR3Mrj3mFQfZilQsVjORbGY5TthfsOE-c4QKg1R6paKy1fTdxnYWwgL-oyC_yOQQ9zhoZC-fonNNzn9rZTtklXmzaTOEuLhxqb1_4rc0UJLFRcyQD-wCQfnJyn9UK2nQhhlHS05UPM7ld5bQvV3pzL_LBlcu_UzkoaQXnEGDyz7z0hxftsfdmJ3La7bRjT8bnyZhOjhYeznfszKoyuHJS2cNwaYFGe-JFBiDTHK88a2nV3dWn1jn3yCmSFX3H2V-EsD1dWJe28PVGULS6sq6rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پسر دهه هشتادی رئیس بانک سپه، معاون بانک دی شد
🔴
پ.ن: لابد اینم امام زمان انتخاب کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138822" target="_blank">📅 11:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
روزنامه «الاخبار» نوشته اردوغان در گفتگو با عون، رئیس‌جمهور لبنان، به او توصیه کرده در توافق با اسرائیل شتاب نکند زیرا اسرائیل هدفش صلح با هیچ‌کسی نیست.
🔴
اردوغان به عون توصیه کرده که سعی کند با سفر به دمشق و دیدار با الجولانی،  روابط خود با سوریه را تقویت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138821" target="_blank">📅 11:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138820">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
هم اکنون منتسب به یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/138820" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5451fd068.mp4?token=XFoNXzT3NUdHgrxEd4ZXDAIWnTYieVLcE-4CZ6U6MGG56jLlJLonVBghfFWUkPIIoFD18kil7HLmfsnrKq7XKW_Z8f5Ho9Abz1BNOaII0aaTnH1f0V35JDAbqqEt6ZzhkF-A0I5zYY-DGfUuwALPlLNUdui22U58QKVkO7PzctXh9SsRd4BbxUHGoaBY1oG9BBnr0uytHc5Bv57j82i65x0jWK51J3kI_9gSW534TlFTx8LkQx_g8DVKW0VVU9fFubsnft5UFJtdZQiPJeZFOxl9SNRJ72KftxV3zH5LJ6HDABwCARLJg9CEiCOkZjwAXSyMB6zv81e9B01-5-0oVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5451fd068.mp4?token=XFoNXzT3NUdHgrxEd4ZXDAIWnTYieVLcE-4CZ6U6MGG56jLlJLonVBghfFWUkPIIoFD18kil7HLmfsnrKq7XKW_Z8f5Ho9Abz1BNOaII0aaTnH1f0V35JDAbqqEt6ZzhkF-A0I5zYY-DGfUuwALPlLNUdui22U58QKVkO7PzctXh9SsRd4BbxUHGoaBY1oG9BBnr0uytHc5Bv57j82i65x0jWK51J3kI_9gSW534TlFTx8LkQx_g8DVKW0VVU9fFubsnft5UFJtdZQiPJeZFOxl9SNRJ72KftxV3zH5LJ6HDABwCARLJg9CEiCOkZjwAXSyMB6zv81e9B01-5-0oVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون منتسب به یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138819" target="_blank">📅 10:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138817">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
الجزیره: قیمت نفت کاهش یافت، اما در مسیر ثبت رشد ماهانه ۲۰ درصدی قرار دارد
🔴
قیمت نفت روز جمعه کاهش یافت، اما همچنان در مسیر ثبت رشد ماهانه نزدیک به ۲۰ درصد قرار دارد. نفت برنت با کاهش ۱٫۰۳ دلار (۱٫۲ درصد) به ۸۸ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138817" target="_blank">📅 10:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138816">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt-lpZpjBJIvLmsOW6IDTVWLyBL5sd1m8Ehp5KLHlKA1kqYjhFxRuogY_R47HF6hf_hq85R15aBRQMdWNk4CiF0zw7Q6u113FtgkjjrXlwhIJ8zkZhJLbXjNysm-kn6Jxl0RYO8biaNJAdZTGScHHpok1TZ3VX-1FJYG5TJmtxB5JqejQGCDEHm1MK--vf3w5YcZ3TrpWkpf4Fj1Vo6rZuNcduoJCPb8Ydw4OY-FaBWzVnRg4cCGZcduztbYFRTfPhJS3XE3zze22h27spWcmXykZBO7jjvb8AngGjLb3Er_7yDItWXHEjNk7khCg-iYBSoVIRUMUuNdEdMc8uk_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بی‌بی‌سی:یک شهروند بریتانیایی به اتهام جاسوسی برای سپاه پاسداران انقلاب اسلامی ایران، دستگیر شد. او به جمع‌آوری اطلاعات درباره یک پایگاه نظامی بریتانیایی در قبرس متهم است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138816" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138815">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmrWlHz_r4ldo_GuuoJ6gwa1xrX9eCWwhv6AawzfHoRBzJTUhQ-_mO3JCksTQoJHFdMHExhCqYm_M1i49lJT4oXX30SZkiL29sfJwPsTZkhLpL8mAJrL7R1fe5B7UwROU-Gje_ohFZhtixQOQp6qR_6ABIowXUb4CsFj4oXOSXbfgIE-NfY1_Kwk9p55kBurt0FA-jYxccqDNO8nwQ3s1cJWDHyZ0hthf0IMG_Y2po4lyIL-7i_n9dQcBfkydRNbYG1oBmW44FVsPnI9BeWFhAc2mzcdkwc0XIpl__1dQfy5SEWA5o6d3XEZ2TVNmSU9lfSMUDM1v9SlaE6qW-aIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مطهری: ممکن است یک آمریکایی انتقام خون رهبر را بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138815" target="_blank">📅 10:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138814">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
شورای صلح غزه: حماس به‌طور رسمی متعهد شده است یک برنامه اجرایی برای واگذاری همه سلاح‌های خود را اجرا کند.
🔴
اقدامی که در ادامه آن، خروج نیروهای اسرائیلی از غزه انجام خواهد شد.
🔴
این طرح همچنین «نویدبخش مزایای قابل‌توجهی برای مردم غزه است؛ مردمی که مدت‌هاست در انتظار آینده‌ای بهتر هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/138814" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138813">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4lugapgqTliluPWjyNq6pCcBX-nYYJRvAYlnsXcrTMges7mh4lqBsElqZVJmLS1e2pWqfVvgCq8p6NmUZrI86TobSOsEUnMjjFLMgFrBOBVxptZTPFSAPtl3bfH5xhRZm75xTE41NpK-nHjEiutXa6526ldsIRGQ48vmqn8rtsANcyz3Gu4RBUaNT5flDateznYF2BFOGayGKTB9rzRtVMJgFaTULZhbRWxbnyEBoTgv-nBoVjzn6j8_Il7OnxZT_fR5lIpCwIhJKlngZrPv7xNZ-1xJMQim8MI5ILbr836chRcVW4WzlKzYNgps2sA9Z5UNK8OsvSjt0QeF9WP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آپدیت بازار کریپتو ۹مرداد ماه
🔴
مارکت کپ: ۲.۲  تریلیون دلار
🔴
شاخص ترس/طمع: ۳۷%
🔴
قیمت تتر: ۱۹۳,۱۴۷ تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138813" target="_blank">📅 10:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138812">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1510e3d07f.mp4?token=NYr5IcJFXQnph69WeSmLRYkpN1BvvJz9iUNJ0qIFsRXu7zsCxxwHauV3slFLHV0CI4qpFFsoiGSRT9otrf8kMw6ZTdnKniXl1ShfvKphHtfxGJ8W4EKWl-ecF-dsPyLiChw7lCjHgbfYi4op4LffuuAKL_IUR8-BIhWOi70zTJMK9QP9z7aIsAJ2C7xORXvc9ZSGcoG1phUZ2IGCE3FvoGmvgnCaN8bowkbAOA9P_e3mRoSvMEI0nKxutUP6KgZvshU5xIKR_dlxQtelz1bB_8DvtG2soT9pLDnUZHfaOBPJBwqTO-EoI4HmV_g6kWPyRUBmn7L-ywFg5sCPXwAhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1510e3d07f.mp4?token=NYr5IcJFXQnph69WeSmLRYkpN1BvvJz9iUNJ0qIFsRXu7zsCxxwHauV3slFLHV0CI4qpFFsoiGSRT9otrf8kMw6ZTdnKniXl1ShfvKphHtfxGJ8W4EKWl-ecF-dsPyLiChw7lCjHgbfYi4op4LffuuAKL_IUR8-BIhWOi70zTJMK9QP9z7aIsAJ2C7xORXvc9ZSGcoG1phUZ2IGCE3FvoGmvgnCaN8bowkbAOA9P_e3mRoSvMEI0nKxutUP6KgZvshU5xIKR_dlxQtelz1bB_8DvtG2soT9pLDnUZHfaOBPJBwqTO-EoI4HmV_g6kWPyRUBmn7L-ywFg5sCPXwAhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: در نیمه شمالی کشور دمای هوا روند کاهشی خواهد داشت
🔴
برخی مناطق جنوب کشور و سواحل دریای خزر با رگبار و رعد و برق همراه خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/138812" target="_blank">📅 10:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138811">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7007c9b457.mp4?token=p98TOAQB7ws-MqP7ulsRZLEW2mZ0kHqxCdkCS0xwGXX70BTtKvNNSkfJjolgN_-fyVNBQ2tMhzfc8_RLlYGv7ua21oGSNwp_bRoQQ1OdwaNH_Vi0YgycOyI7CZJIuF3hL8VoK_KNBLfmVVHmhF1Hpqc4ZjX7EcTbMTumeeR2KhR8qn2i5KrTOVvWeA7ECIXWnCz1fREp9VNuSj_0wv678pEYQSli__tLDsHwLNUPjilYcfpRP5ZTrUdm2tTsLd53Hg-b-N9BlSJV4Fv7t1Aku1yMuf6qVuy1y-iAAa_MsI3dg--biFUCQewcIyt1WR1O9wutPNLpWLQhQ-D0t1gaJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7007c9b457.mp4?token=p98TOAQB7ws-MqP7ulsRZLEW2mZ0kHqxCdkCS0xwGXX70BTtKvNNSkfJjolgN_-fyVNBQ2tMhzfc8_RLlYGv7ua21oGSNwp_bRoQQ1OdwaNH_Vi0YgycOyI7CZJIuF3hL8VoK_KNBLfmVVHmhF1Hpqc4ZjX7EcTbMTumeeR2KhR8qn2i5KrTOVvWeA7ECIXWnCz1fREp9VNuSj_0wv678pEYQSli__tLDsHwLNUPjilYcfpRP5ZTrUdm2tTsLd53Hg-b-N9BlSJV4Fv7t1Aku1yMuf6qVuy1y-iAAa_MsI3dg--biFUCQewcIyt1WR1O9wutPNLpWLQhQ-D0t1gaJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای Sentinel-2 نشان می‌دهد که پس از حملات اخیر موشک‌های بالستیک ایران، آسیب‌های جدیدی در پایگاه هوایی علی السالم کویت ایجاد شده است.
🔴
در این تصاویر، یک اثر سوختگی در یک سوله انبار که توسط نیروهای آمریکایی استفاده می‌شود، مشاهده می‌شود؛ اثری که با اصابت مستقیم یک پرتابه مطابقت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138811" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138810">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da03a51b1.mp4?token=aEbkDhvQyLhFHL9gQ2UC3gLYQlrhy7gT2X6M0nUCMAT9r3icsjg0Svwp9uMIbGOxr1Qb4Wx_8GRVlFgQJ6J2U3acIXb0KKB-D0s92FIqa2it3Vf5RkhsXhcBatlGYDluNDbr2Z_3Mhqqhjn2LB9k_ul2blua4n1r7TlCTM5c7n0VsWH3XR5wxV6sdXXJwUEntjAvY114qhTF7qFyZwKZjDV3nKNvNTRUKxOdKVfcyrjukASTd5VnyPNRGY81-pVxGEe_jihANIVrW6Nos1exiG7nFIULKQMCLiVAYjKKAPbFFXvKUsrdp_smuF3Ci11ws94Lm7XRsW11cbwIPijgcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da03a51b1.mp4?token=aEbkDhvQyLhFHL9gQ2UC3gLYQlrhy7gT2X6M0nUCMAT9r3icsjg0Svwp9uMIbGOxr1Qb4Wx_8GRVlFgQJ6J2U3acIXb0KKB-D0s92FIqa2it3Vf5RkhsXhcBatlGYDluNDbr2Z_3Mhqqhjn2LB9k_ul2blua4n1r7TlCTM5c7n0VsWH3XR5wxV6sdXXJwUEntjAvY114qhTF7qFyZwKZjDV3nKNvNTRUKxOdKVfcyrjukASTd5VnyPNRGY81-pVxGEe_jihANIVrW6Nos1exiG7nFIULKQMCLiVAYjKKAPbFFXvKUsrdp_smuF3Ci11ws94Lm7XRsW11cbwIPijgcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظاتی پیش، یک اردوگاه متعلق به گروه‌های تجزیه طلب کرد، در اربیل مورد حمله قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138810" target="_blank">📅 10:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138809">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نخست وزیر و وزیر جنگ اسرائیل با صدور بیانیه مشترک گفتند که ارتش اسرائیل در حملات شب گذشته خود علیه جنوب لبنان از ۷۰۰ تن مواد منفجره استفاده کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/138809" target="_blank">📅 10:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138808">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پاکستان: مذاکرات میان تهران و واشنگتن ادامه دارد
🔴
سخنگوی وزارت امور خارجه پاکستان:
اسلام‌آباد نهایت تلاش خود را برای بازگرداندن ایران و آمریکا به اجرای تعهدات‌شان در یادداشت تفاهم پایان جنگ به کار می‌گیرد.
🔴
مذاکرات میان طرفین با وجود درگیری‌های اخیر ادامه دارد.
🔴
پاکستان از طرفین می‌خواهد که حداکثر خویشتنداری را به کار گیرند.
🔴
گفت‌وگو و دیپلماسی همچنان تنها مسیر ممکن در میان تنش‌ها و خصومت‌های جاری در غرب آسیا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138808" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138807">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
مدودف: روسیه در مرحله‌ای مهم از پایان جنگ قرار دارد
🔴
مقام روس گفت: مناقشه اوکراین بدون تردید با پیروزی روسیه پایان خواهد یافت و اکنون مرحله کلیدی از پایان آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138807" target="_blank">📅 09:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138806">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
واژگونی یک دستگاه خودرو سواری پژوپارس در مسیر دهلران به اندیمشک، به جان باختن چهار مسافر و آسیب‌دیدگی یک نفر دیگر انجامید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138806" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138805">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBBCppgzG4B5pcKwRBHYay_Vjuy4z5Q0xdRnACn7Qqje0KUBJ8iSEmqnCFZ_cmCMCAnkY6P-QHBiRErHaqpKENRogwWy5D85WQHCHt4fAhdWQaBdM1YNIN5He9z_obOKEar2o64zqaMEE7z8L_b66fNsZCClARWOoLT_GO3S0x2Hxi1FzeDscUaUE168I_2FyqCHcZxVP4Nps-K7vhx0CxQY6oFAAzTmYyp6LnjVp3Xgj9Y1HPw7Wgj8HeVWFQo0mEaJPfi_uwNE6Zg3HwjxmDk5ONPcuHgHsZEJpATokMLjEg7l6AKdJxWk7TtLURtNPDM3s95uVgblTfnsZ2eg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخستین رای‌گیری غیررسمی شورای امنیت سازمان ملل متحد درباره هفت نامزد دبیرکلی سازمان ملل برای جانشینی «آنتونیو گوترش» دبیر کل کنونی این نهاد بین المللی، روز پنجشنبه به وقت محلی در حالی برگزار شد که خانم «ربکا گرینسپن» معاون پیشین رئیس جمهوری کاستاریکا پیشتاز این رقابت بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138805" target="_blank">📅 09:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138804">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b065ff04b.mp4?token=h9RQ5N7LheGzYvxg9mS_2XmUoUBagG7r0C6ChDMm4yNOIapCFB8yfqmX62pYzQtAErVQG6MJCr2R500dlux9nqF04oGU5VithCThrT5yVRiszdow3bSwpjFlbzkATk6MR3EnrsG6meogonPOfUmJx8BQPzBOyyGOrmNgR6AV7STxVXLLtgbgBsNRDSUHLT1U0f6bjWeFmUz8XbhXqDfi916JnT41aKtyxAu8Q4PpecuxzP6vxpb3pABn0LjFob5QODpAEfF41GJowZWfwIWMadYLroVM23JcwZwL5yzPF5YZwdeDbYy2LIFOQV9lWVwYBaDMo01YL_OKkRpzC2ORSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b065ff04b.mp4?token=h9RQ5N7LheGzYvxg9mS_2XmUoUBagG7r0C6ChDMm4yNOIapCFB8yfqmX62pYzQtAErVQG6MJCr2R500dlux9nqF04oGU5VithCThrT5yVRiszdow3bSwpjFlbzkATk6MR3EnrsG6meogonPOfUmJx8BQPzBOyyGOrmNgR6AV7STxVXLLtgbgBsNRDSUHLT1U0f6bjWeFmUz8XbhXqDfi916JnT41aKtyxAu8Q4PpecuxzP6vxpb3pABn0LjFob5QODpAEfF41GJowZWfwIWMadYLroVM23JcwZwL5yzPF5YZwdeDbYy2LIFOQV9lWVwYBaDMo01YL_OKkRpzC2ORSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش : پهپادهای نظامی، مراکز استراتژیک آمریکایی را در کویت مورد هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/138804" target="_blank">📅 09:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138803">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCtfy6_iWdWlLKnsSPX3BpUBR007AEzokEJkO4hA0AW8p2Dr42BeiZ_zviv-7Y5HnGhgorCnc5CjdBFv3jvR5P1YjbsjeB2vH0DXGlLW6553jV_cPMFuKp9SvBnCpohIWKShwvk7lQFcfKF8g2T66VVw_gKb7ZzReactw3-STqd_gCht6tIveZkWvpwsdI_p8AgS0MY580pQbyWHM6YBaectmzOCrklrqxL3VmcMvS3gM3xsTjN_shu3R-MwYUHho6K1bySE0LTzOqfIVxvwScpVxaWIw7h5wedYLR_gOKyAg3Jg85xoj4OoCcOzZvMxJ2ThxiTJwqKuk_7hz9qU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: ترامپ از ایران «خشمگین» شده است، زیرا مقامات ارشد نمی‌توانند بر سر یک استراتژی مشخص، به توافق برسند
🔴
رئیس‌جمهور در جلسه اخیر خود با برخی از مقامات ارشد امنیت ملی خود به شدت برخورد کرده است.
🔴
او از عدم پیشرفت در زمینه پایان‌دادن به جنگ با ایران و همچنین اختلاف نظرهایی که در داخل دولت خود در مورد استراتژی وجود دارد، ناراضی است.
🔴
برخی از مقامات از ادامه عملیات نظامی حمایت می‌کنند، در حالی که برخی دیگر هشدار می‌دهند که حملات طولانی‌مدت می‌تواند ذخایر تسلیحاتی ایالات متحده را کاهش داده و اوضاع را وخیم‌تر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138803" target="_blank">📅 09:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138802">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W32ajk3Lh9E0ldRNBD2Mp2F1ZWW_I9CyV7iv0GXMeGUYuNJWtk1nVlE-dLEVzAvz-2bYmc2XPKHJLecGfQrgtUGeGSHuzT3T3DCABJUQ3w1t9nOeEQQZIhfDUKUdHHbcS89cyxPLOjhWgrd9vGUuEJ1bAbIduBTxm_LEdNr1Q5OPrnLul2--JF0-BT6zGw5rX-KSEi1PhLsJtN0bol18NgNMgCEypqFdp0W626_GgyekxTYoWGyv-WQgnIe9AN1Al1mlckYLvRfH05_ceYqwtNoePBq7TI3nWMEj3Ge9EOAJvPfB88QdKN6sWATVd30GJdAMMnE4MPRmmy1bZMMBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
@AloSport</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138802" target="_blank">📅 09:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138801">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
مقامات آمریکایی به وال استریت ژورنال:
«پنتاگون در واکنش به حملات ایران به پایگاه‌های ایالات متحده، حضور خود در کویت را کاهش داده است تا خطرات را به حداقل برساند.
🔴
پنتاگون پیش از شروع جنگ با ایران، در حال بررسی امکان کاهش نیروهای خود بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138801" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138800">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0085b8d38d.mp4?token=oF-YIWqIxoN5e3_G6-LqTN_IZNtiuU097GYda19E89H2ye7u4ImhHngKUVw4EaDdt7_X3kjQdUqnCi4_y55D1woLQszprQysA8V34YqqSloRGB_L7a4x89wQeDFhoRnmZHQ2AejkKTxwVNMjaXEGpGpItk2fCbGEK0xUCKkLLdyp6T8lsn-6R8BFyJxpePyZH98wMK36YQFr_dnQkyjvMQmHza-DjVr23hhwouhW-aS0hZP1bec-WmQRPzO4hxk250sR8Wh0QFcUAgHctr2M1Jq9g4cjktF2zicbkM5j1d5OkL-ifOm6peCfKJfrDhsSYIvrkw_dKVaRb53vUNc6JwSBM_niMTq_R5DpEaFPQbZckn90mq-vSpU3x1eLLzs3ZkcLDb6DBhCTdGLIwuHCRUu21QyqAJJ-uLh1KtQXMmylNdiCn_XBKO65zgF5IuRsaFhO9wQiewoMDWg1XJvnPulipWPwWPcYnEbVaDJe9qejQrl7I7TyD6B5mWnsflTafkHwLWn94dgsBLe0udppaxRgxywweVJVneeR_HsHvmwFlw8XykVxSApsENMDfyTTeOzArB94eXbobzfsCLW5sLLLcoKrFzWbMJwVbo28jlsTri3QjK98jWFf-wtOwI9DoMFyKJjjQVNYpdseVTdq07zxVaBfrAUeLwHuTDh1Bao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0085b8d38d.mp4?token=oF-YIWqIxoN5e3_G6-LqTN_IZNtiuU097GYda19E89H2ye7u4ImhHngKUVw4EaDdt7_X3kjQdUqnCi4_y55D1woLQszprQysA8V34YqqSloRGB_L7a4x89wQeDFhoRnmZHQ2AejkKTxwVNMjaXEGpGpItk2fCbGEK0xUCKkLLdyp6T8lsn-6R8BFyJxpePyZH98wMK36YQFr_dnQkyjvMQmHza-DjVr23hhwouhW-aS0hZP1bec-WmQRPzO4hxk250sR8Wh0QFcUAgHctr2M1Jq9g4cjktF2zicbkM5j1d5OkL-ifOm6peCfKJfrDhsSYIvrkw_dKVaRb53vUNc6JwSBM_niMTq_R5DpEaFPQbZckn90mq-vSpU3x1eLLzs3ZkcLDb6DBhCTdGLIwuHCRUu21QyqAJJ-uLh1KtQXMmylNdiCn_XBKO65zgF5IuRsaFhO9wQiewoMDWg1XJvnPulipWPwWPcYnEbVaDJe9qejQrl7I7TyD6B5mWnsflTafkHwLWn94dgsBLe0udppaxRgxywweVJVneeR_HsHvmwFlw8XykVxSApsENMDfyTTeOzArB94eXbobzfsCLW5sLLLcoKrFzWbMJwVbo28jlsTri3QjK98jWFf-wtOwI9DoMFyKJjjQVNYpdseVTdq07zxVaBfrAUeLwHuTDh1Bao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روایت حمله به خوابگاه دانشجویی اهواز از زبان یکی از دانشجویان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138800" target="_blank">📅 09:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138799">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
عبور ۲۵ کشتی تجاری از باب‌المندب
🔴
بر اساس داده‌های شرکت ردیابی دریایی Kpler که خبرگزاری رویترز به آن استناد کرده است، روز پنج‌شنبه ۲۵ کشتی تجاری از تنگه باب‌المندب عبور کردند، در حالی که تردد در تنگه هرمز همچنان بسیار محدود بود و تنها دو نفتکش از آن عبور کردند.
🔴
از میان این ۲۵ کشتی:
۱۸ فروند وارد آبراه شدند.
۷ فروند از آن خارج شدند.
🔴
این کشتی‌ها شامل چندین نفتکش، از جمله: دو نفتکش بسیار بزرگ (VLCC)،
یک نفتکش سوئزمکس،
و پنج نفتکش آفرامکس بودند.
🔴
در همین حال، هیچ‌یک از دو کشتی عبوری از تنگه هرمز حامل محموله نبودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138799" target="_blank">📅 09:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138798">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
واشنگتن پست به نقل از یک مقام آمریکایی گزارش داد که واشنگتن از اسرائیل فقط می‌خواهد که با طرح ۲۰ ماده‌ای که قبلاً به‌طور اصولی با آن موافقت کرده بود، کنار بیاید. این مقام افزود که دولت آمریکا اطمینان دارد اسرائیل به این طرح پایبند خواهد بود و اشاره کرد که اگر چنین نکند، دونالد ترامپ، رئیس‌جمهور، «به‌شدت ناامید خواهد شد».
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138798" target="_blank">📅 09:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138797">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
یک منبع اطلاعاتی آمریکایی به شبکه نیوزماکس گفت:ایران از داده‌های مربوط به فناوری تبلیغات برای ردیابی نیروهای آمریکایی و هدف قرار دادن آن‌ها استفاده کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138797" target="_blank">📅 09:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138795">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb5776e72.mp4?token=GwzdLQYz2HkBQo0VpGCVyR6kk7XTryzSzfe8z5xpHWlu39oy8JEg6RU_3msH2OEKFggVQfkIckMHIaA-6lPAV49y0whhHQxgGanhuC3oSgnPL9i2NSX78xe_aPr9yrHz65vj3tukbvcU8EiZIbe0Y24ReoomhogKdURafgutz7IsZ4L8abbBGon40iVbeWwDmCHFVL_g90TT8YZ_r7oEo0uQFXX1EwI27cN6arJPqAdls82nkhV78GUIahqfu7DinHEqwVw7Pe3vWVZj3pfh-qlxWiR6OsXtAthJ3CEQcJG2UDCIK5477XEUvcF4ku-NWkyzlf_y8CTOa7jNZk80Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb5776e72.mp4?token=GwzdLQYz2HkBQo0VpGCVyR6kk7XTryzSzfe8z5xpHWlu39oy8JEg6RU_3msH2OEKFggVQfkIckMHIaA-6lPAV49y0whhHQxgGanhuC3oSgnPL9i2NSX78xe_aPr9yrHz65vj3tukbvcU8EiZIbe0Y24ReoomhogKdURafgutz7IsZ4L8abbBGon40iVbeWwDmCHFVL_g90TT8YZ_r7oEo0uQFXX1EwI27cN6arJPqAdls82nkhV78GUIahqfu7DinHEqwVw7Pe3vWVZj3pfh-qlxWiR6OsXtAthJ3CEQcJG2UDCIK5477XEUvcF4ku-NWkyzlf_y8CTOa7jNZk80Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات ایران به کُردهای تجزیه طلب در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138795" target="_blank">📅 09:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138794">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
شمار قربانیان زلزله ژاپن به ۳۴ نفر رسید/ ۳۵۰۰ خانه هنوز برق ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138794" target="_blank">📅 08:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138793">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
اکسیوس به نقل از مقامات اسرائیلی و آمریکایی: ونس و نتانیاهو عصر سه‌شنبه در یک دیدار دوجانبه در واشنگتن، گفت‌وگوی «مستقیمی» درباره اختلافات خود داشتند
🔴
تانیاهو با ونس درباره انتقادات اخیر او از دولت اسرائیل گفت‌وگو کرد
دو طرف توافق کردند که به دنبال فرصت‌هایی برای همکاری اسرائیل و ایالات متحده در حوزه‌های دارای منافع مشترک و اهداف مورد توافق باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138793" target="_blank">📅 08:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138792">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزارت جنگ آمریکا در به‌روزرسانی آمار تلفات اعلام کرد شمار نظامیان زخمی این کشور در جنگ با ایران به ۶۵۳ نفر رسیده است. بر اساس این گزارش، ۱۱ نظامی دیگر مجروح شده‌اند و تاکنون ۱۸ نظامی آمریکایی نیز در جریان درگیری‌ها کشته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138792" target="_blank">📅 08:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138791">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: مطمئن نیستم به اوکراین اجازه تولید موشک‌های پاتریوت را بدهم
🔴
این یک سلاح فوق‌العاده است و باید کمی درباره اینکه به چه کسانی مجوز تولید می‌دهیم، احتیاط کنیم
🔴
تمرکز اصلی من پایان دادن به جنگ روسیه و اوکراین است؛ کوشنر و ویتکاف، برای نخستین بار طی روز‌های آینده به اوکراین سفر خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/138791" target="_blank">📅 08:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138790">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2C8eO9gU72ndfeAezUpv_Lsnoy1vhHk8vuFGpCtekh9W3nDYvy3pzDMzmAiVRZ6sT6V9ySRdrwBdt6EIMMaVj6YziOoID-CaVinJwZNQosCmKmjXmkZIDkwrshNspXVIL0NTew312PxQJF6gAvrljc0JwPYdOAbLpTNEGU7pZ7lh6VKGKyLjydmZKB9qpRIM1Y-WYcJevnJkrBUaIrJEwpWFG-dLUlfHewWV4dZqiQiHvJm0o06j1WagIsDZIKoSrQ4JbVrHfa4KfQ-TaI5XnqOLpPHU1TtneCqJE4hBUfzcEjltIBj_M20BFXETgQoWJUKUj3nTIQ5Q6dfwksSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت اینترنت استارلینک در عراق چقدر است؟
🔴
یک ماهه سرعت ۱۰۰ مگابیتی؛ حجم نامحدود: ۹ میلیون تومان.
🔴
یک ماهه سرعت ۴۰۰ مگابیتی؛ حجم نامحدود: ۱۵ میلیون تومان.
🔴
میانگین درآمد مردم عراق: ماهی ۱۰۰ میلیون تومان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/138790" target="_blank">📅 08:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138789">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuUMU4P-pvNCIudpb_U9N7dKMHKB_iK1aPDwMSuDVVQPOengmCvuIHmhFYpfTwMprVvJNbK3qSpUTMn9oSD1C-w-IRitB2EQbGj3j3RN43k1GDbb15sDEhMGhk5CSgkyISA921v0PMxdLeKUjNTJAN4tyxe_zTT7_LWqUXGybT9wyLJNu-W2jald_TCLb07V2b-r0CgzSBzAwuPGtVRiHX2kj0hinwpAw5j24dX-SC5AWsWHIqNXxvXtUdIszDdWdnAr9UTczfiqldY4DdiiJ4n90EmoOe75zfGL3yyTYRbX5L08xjPti2rb0z2nWRtMRxh6J14d_tG5F2KbmZ4iig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: حماس خلع سلاح شد
ترامپ:
امروز، شورای صلح به یک توافق تاریخی در مورد خلع سلاح کامل حماس و تمام گروه‌های مسلح دیگر در غزه دست یافت. این یک گام بزرگ به سوی صلح و امنیت پایدار است.
این توافق، یک گام حیاتی برای این است که دولت فلسطینی جدید، که با شورای صلح برای کمک به مردم فلسطین همکاری نزدیکی خواهد داشت، سرانجام بر غزه حکومت کند. در عین حال، اسرائیل امنیت مورد نیاز خود را به دست خواهد آورد، زیرا غزه دیگر به عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
این یک نقطه عطف مهم در اجرای طرح 20 ماده ترامپ است. این توافق به صورت مرحله‌ای و با ساختاری مشخص اجرا خواهد شد. با تکمیل فرآیند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و نیروهای بین‌المللی حفظ صلح با پلیس فلسطینی جدید همکاری خواهند کرد تا امنیت غزه را برای ساکنان و همسایگان آن تضمین کنند.
یک سال پیش، جنگ وحشتناکی در جریان بود، بحران انسانی وجود داشت و افراد به عنوان گروگان در اسارت وحشیانه نگهداری می‌شدند. ما به پیشرفت تاریخی دست یافته‌ایم و هنوز کارهای زیادی باید انجام شود.
می‌خواهم از میانجی‌ها - مصر، قطر و ترکیه - به خاطر تلاش‌های مهمشان تشکر کنم، و به ویژه از تیم برجسته‌ام که تلاش‌های بی‌وقفه آنها، این پیشرفت تاریخی را ممکن ساخت.
تهدیدی که از غزه در 7 اکتبر ایجاد شد، دیگر فرصتی برای بازگشت نخواهد داشت.
در چارچوب این توافق، غزه سرانجام به دست دولت فلسطینی جدیدی خواهد افتاد که به مردم خود خدمت خواهد کرد.
به همه تبریک می‌گویم برای این دستاورد شگفت‌انگیز که، همانطور که همه می‌گفتند، هرگز قابل تحقق نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/alonews/138789" target="_blank">📅 02:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138787">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCr3j0tZP6G6zshzRt9ErmlS4yWqE3aESY7Ap8T8O5zaFo4gv-yRQEgM8Qq83l4olbvvM6UwRGh4YQRDmNbjwPYW_GJvNZ1W1g8z56WjfnNnT_8ddimSnVUk5ZD8Rn88EIWVNZdXaWddUxTEl_B12mdTtMzJ9nbVrN8cJyZUO5Ji5tsA8ppEcXAY7whwf8ilf4uWF02H2ycYF_FxczMvb8v2DK5ZkZbNtsMR3ktnpT3-CUqHbNqIuolNY5QMbsJzySf8J9_7jIxHvf_OLweE4YTAGrMghn5ZhXBA3kPkJtxIxkfAn0fEy1ztOo9CM8QDXw2J48ijyhGPmFqe8O-0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=v9f32ZroOqYdYNS_Vq9c9gRgj8XoAHkoJZrybIspJmjiHuZbjhPrfBAmuG-HUS0X-r2_GzS_Ua-EHN0TG84isogCeKWVHUtwX7Bqobz5zSSP8AfpApfHw0aR3OeYg8UeALeWsasaMtJ3ZzPqgf1M97uVcYrULSC9aasmeGt8_1Dcx6hwqaXo936FOUozK7HpM_fiN9u5gjPsD02hgmd_0jQe-BTJ8K39n_YfleEQzOKp5Wsht_LzARvawsCCcJDI74Cg-3PdHQZVcJtOrvRnrr-YnH-iQcof_iKtX7gSTd-LgRY2ZCmYUQHO33CLN53Ns8n5EtJCVj8vffW5hwVwBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=v9f32ZroOqYdYNS_Vq9c9gRgj8XoAHkoJZrybIspJmjiHuZbjhPrfBAmuG-HUS0X-r2_GzS_Ua-EHN0TG84isogCeKWVHUtwX7Bqobz5zSSP8AfpApfHw0aR3OeYg8UeALeWsasaMtJ3ZzPqgf1M97uVcYrULSC9aasmeGt8_1Dcx6hwqaXo936FOUozK7HpM_fiN9u5gjPsD02hgmd_0jQe-BTJ8K39n_YfleEQzOKp5Wsht_LzARvawsCCcJDI74Cg-3PdHQZVcJtOrvRnrr-YnH-iQcof_iKtX7gSTd-LgRY2ZCmYUQHO33CLN53Ns8n5EtJCVj8vffW5hwVwBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار عجیب نتانیاهو با یک سناتور!
🔴
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/alonews/138787" target="_blank">📅 01:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138786">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
دقایقی پیش، یک پهپاد در آسمان اربیل، واقع در کردستان، مورد رهگیری قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/alonews/138786" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138785">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8935b48fd.mp4?token=BXLsWcld--_c9dly4KXQL7Bcjmp8Z3lV0t3x_UJhHRdOXknUi0I7xQ54BRaiuzFQv7svoKyFte3RTo0C_KcXZ_rQccDafkbd4OOEBnnEPGBh4-EiAPdTvvNdn_6qAyNPU6HxF7WuyDhsV-pFlKIvZvvf3hVyno7Ydc99U3x4DkdyJtvhRqOuH2xJq5RRw0RqrYouxcq6Anlb5FSQFw9YCcqkEeBIHf0Y-nGcUTHjNecGQMXQ76PFIgLZa_4p_hvSzNT_fp9N3n8g4wsA9TUC7CVa60q6yJma3sW1oRlB0LhQXC4WuxFce4Ur7k2I-NNLj1PY2VvtX7VoL0oKCMJ-HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8935b48fd.mp4?token=BXLsWcld--_c9dly4KXQL7Bcjmp8Z3lV0t3x_UJhHRdOXknUi0I7xQ54BRaiuzFQv7svoKyFte3RTo0C_KcXZ_rQccDafkbd4OOEBnnEPGBh4-EiAPdTvvNdn_6qAyNPU6HxF7WuyDhsV-pFlKIvZvvf3hVyno7Ydc99U3x4DkdyJtvhRqOuH2xJq5RRw0RqrYouxcq6Anlb5FSQFw9YCcqkEeBIHf0Y-nGcUTHjNecGQMXQ76PFIgLZa_4p_hvSzNT_fp9N3n8g4wsA9TUC7CVa60q6yJma3sW1oRlB0LhQXC4WuxFce4Ur7k2I-NNLj1PY2VvtX7VoL0oKCMJ-HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل: تونل‌های حزب‌الله تو منطقه بوفور جنوب لبنان رو با حدود ۷۰۰ تُن مواد منفجره منهدم کردیم
🔴
این عملیات در واکنش به نقض آتش‌بس از سوی حزب‌الله انجام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/alonews/138785" target="_blank">📅 01:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138784">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
دادگاه دختری که از پسرها سواستفاده جنسی میکرد و فیلمش پخش میکرد بزودی برگزار میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/alonews/138784" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138783">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/138783" target="_blank">📅 01:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138782">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e924ddde6.mp4?token=MojGk_nXmqRfgrTr1S-KbY-8Io2XJzBa01UkrbK5OXsS0JTU8nADmRntd8u2-E6PlHacP5Z7_PUYmw2QeyPFtjpDxxKuc8lPi9s2S-Aude5YOcLDn2DimnezruYKxSzxQIALXagk2ymGPR0egSR1ehPFv0G2JFR7GaKFECcVY2Z1U7GZI1dTmQXhHhYbM8UmiN4crcd9Nxv9W3D5wZSLGmsMLPjMVhDhBFcD0fo-m8o8ur1Gm36Ebke7uL_VAxTr2YeiIV7w1Qe8AIlBxwNTNHjdiZw8XuOtgGA40iKaT2VSL9E_XJNdzcPvVL2zEYBdCu5QL_UhDxtgBQKrhqxD5YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e924ddde6.mp4?token=MojGk_nXmqRfgrTr1S-KbY-8Io2XJzBa01UkrbK5OXsS0JTU8nADmRntd8u2-E6PlHacP5Z7_PUYmw2QeyPFtjpDxxKuc8lPi9s2S-Aude5YOcLDn2DimnezruYKxSzxQIALXagk2ymGPR0egSR1ehPFv0G2JFR7GaKFECcVY2Z1U7GZI1dTmQXhHhYbM8UmiN4crcd9Nxv9W3D5wZSLGmsMLPjMVhDhBFcD0fo-m8o8ur1Gm36Ebke7uL_VAxTr2YeiIV7w1Qe8AIlBxwNTNHjdiZw8XuOtgGA40iKaT2VSL9E_XJNdzcPvVL2zEYBdCu5QL_UhDxtgBQKrhqxD5YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین جنتی شاعر: سال ۸۹ تو بیت رهبری شعر خوندم و کمی نقد کردم. آقای خامنه‌ای علنا تهدیدم کرد و فردا صبح مامورا ریختن تو خونه‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/138782" target="_blank">📅 00:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138781">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
دادستان تهران:هر کسی از اعدامی‌ها، چه به صورت مستقیم یا غیر مستقیم حمایت کنه جرمه و براش پرونده قضایی تشکیل میدیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/alonews/138781" target="_blank">📅 00:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138780">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YspEc9VnXbLcb8ozMjwaeCAOCDIu-7SIu_asr0QJBUvbMNreApfkiIpKK1Vdb9qDsjQlSRq-beb2V4sBCjp1Y-W4Rd_bt4l2OccPq6Pfbj6IdJVq6wduRDPGSTLKzLN7rO_3pFenPxhVc-dIFSTGSD9O1w_EvxcMoRD0_YjOkwFVzHyqv1pn4uWaERsUef6rBdIHMag9XROwCRRV3yCJ0NrjLaRhbNVdH5EVk1QUOzH1ycUmfs1XTO2hYCwRzN1Zv2CAc22vWYanXXrvxbibcATrfn6xpNAXhPh93nYB_2lNYExoSuLQJ9Lsotc10AzZaU5C2O43d2HDn22Mx4QM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رائفی پور رسما تریاک کشید
‼️
🔴
‏استراتژی جنگی عوستاد رائفی‌پور:
حمله زمینی عراق از شمال و یمن از جنوب کار عربستان را یکسره می کند
🔴
‏عربستان بجز توان هوایی که با هدف قرار گرفتن فرودگاه ها و پایگاه های هوایی اش در همان ابتدا فلج خواهد شد هیچ چیز دیگری ندارد
🔴
‏پاکستان هم به دلیل نداشتن مرز زمینی با عربستان کمک خاصی نمی تواند بکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/alonews/138780" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138779">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
واکنش عادل فردوسی‌پور به ویدیو جنجالی که امروز منتشر شد: ویدیوهایی از گذشته من رو گزینشی منتشر کردن. کاملا تصادفی وزیر ارشاد کنار من نشست. اگه قرار بود من چاپلوس و دست‌بوس باشم، الان صداوسیما بودم و نود رو داشتم. چرا باید دست یه مسئول رو در مقابل جمعیت ببوسم؟…</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/138779" target="_blank">📅 00:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138778">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t81pf5opezJSvIFLRv2BaS-lhRJOB312DPaAejxm4ezVshZkVPNENnRcwlTh_19NSiCDfpzw3ADc7mPfS1Pqs3erc_5OoNpX_CQYA8ju-J1qwzprd8F4OZAdj0Wni8r_X-nSYJ6z2kYHaZEjvRGuKE5yEvWmg5GYSFDq8P081US84ORh3ur8FE0G0VtadrR4fhYsPAXgpfbXjhcW9tIzpZ73RhR0tl6yjmplLvQgaqf9ee__HIH1dRr7yVDTrh3tqOcN5I2f-dz8dJTNSO12a58PZRg76Lw3ZWv3542pTknSnqpoU9Ktiap2x-uYHFoI8pOW5-LenWFOnT4x9BcaFKpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t81pf5opezJSvIFLRv2BaS-lhRJOB312DPaAejxm4ezVshZkVPNENnRcwlTh_19NSiCDfpzw3ADc7mPfS1Pqs3erc_5OoNpX_CQYA8ju-J1qwzprd8F4OZAdj0Wni8r_X-nSYJ6z2kYHaZEjvRGuKE5yEvWmg5GYSFDq8P081US84ORh3ur8FE0G0VtadrR4fhYsPAXgpfbXjhcW9tIzpZ73RhR0tl6yjmplLvQgaqf9ee__HIH1dRr7yVDTrh3tqOcN5I2f-dz8dJTNSO12a58PZRg76Lw3ZWv3542pTknSnqpoU9Ktiap2x-uYHFoI8pOW5-LenWFOnT4x9BcaFKpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش عادل فردوسی‌پور به ویدیو جنجالی که امروز منتشر شد: ویدیوهایی از گذشته من رو گزینشی منتشر کردن. کاملا تصادفی وزیر ارشاد کنار من نشست. اگه قرار بود من چاپلوس و دست‌بوس باشم، الان صداوسیما بودم و نود رو داشتم. چرا باید دست یه مسئول رو در مقابل جمعیت ببوسم؟ چرا اصلا چنین چیزی رو باید باور کنید؟ دست هیچکس رو نمیبوسم. هجمه عجیبی علیه من اومده. همیشه کنار مردم هستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/alonews/138778" target="_blank">📅 00:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138777">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bL9lDmg4r7X47vmN1S3yPCHwRFE7b5xZnNozh6cygbd3CZuZyofzPACeN3JHCh-qrT8RvPnzULGwWlfg8Mm-7fsGtUmysofPGMKGPpZbP58ROUWGFN3uncV8f3k226ITE96xUiGPOQ8PQKlkdBzSs9I9Qzs_JPOnqcAb3OpLEEqe1YVo5w-0e2rqwBupjbMz1ZZy6jvA3eQ4s5KZ7e3JsyEfbmaiavgu9KPXhEN8FvOvGwQ_yxWvKein3aWl8n2T2XYGqdJczi8r_wSGHULgROnPdqA-iNmKjUZU7RzTzyhphFRG7Z5Qwxdrv8dSskd6tI2ubjybLdr0cCxRqtE36w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جایزه بزرگ شهر هوشمند
🥇
نفر اول 500 دلار
🥈
نفر دوم 250 دلار
🥈
نفر سوم 200 دلار نفر چهارم وپنجم هم 100 دلار جایزه
به هم پوک بزنید فالو کنید
پوینت کسب کنید
🎮
لینک مستقیم بات
https://t.me/POUYAM_APPBOT?startapp</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/138777" target="_blank">📅 00:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138776">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
فایننشال تایمز: حملات پهپادی اوکراین ۴۵ درصد ظرفیت پالایشگاههای روسیه را از بین برده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/138776" target="_blank">📅 00:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138775">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9I0nABIKTdjQpy99skSIqhXSx055cEnKXcQ2xFG33MjafqNS4ZhNRLZjXXDq8c_kdTj6JgfTrSBGGTRXPbQmTqMOxYzS3Ef-q-15K9vT10QYM9k1KpHaiWFWgccq7DSFl6MsjE-d6-8yJYMv9BWeM-o190Kfd-L2rABojCyuJdbjS040TV22ZM8MM7WJmVDHQGurmHwKmdPGfnUHbfnhNYHZyQg_dX1Nu3G3_JBo2Xk2JV4knUER6uDPV4giv8bqlyJfV278fhBFv8yr3i6mKjqjWPNNNeLurBFuHgQJaQzcvogW0UNmt3woO7lT9YiZ_lb91OLmqg9654NB0VThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی : مصر برای ما یه دوست و شریک مهم توی منطقه‌ست و امنیتش اولویت داره
🔴
همه باید حواسمون به نقشه‌های اسرائیل و عملیات‌های «پرچم دروغین» که هدفشون به‌هم زدن صلح منطقه‌ست، باشه
🔴
تهدید مشترکه و از اتحاد مسلمان‌ها می‌ترسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/138775" target="_blank">📅 23:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138774">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWSJRE-qwUu2q2zDLj8j9jpPnYJ5qe6WkmLXloV9bHUdGOOVJ9lOmQc8ZMuF1lAprmH5KjNMrIhx12QYJgZ_NSBHrC1c_DeGDUHRgvImURVeTHqY-YBh73hDy36LE4iH1gIcqt22DosA4wDZCaNmCjns1bO9z_YnNLQlsvT9lcc-ojA0jkcJKW_wFoWZ0HP7U4YfhUFlSsbepympiUGydTWDR-qbchE0varbbRmwI-5B1tUGNJ9csdp1x4X5Nc3bHBqBWDLI8mz_y1E3nnH6cEvPHAq7SSIPYL-18DhhX4M2Z704U5AGPgFsagX0ul_qfg-35oGY6N2dCC7c7JFLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابطحی: احتمالاً احمدی‌نژاد جاسوس دوطرفه بوده است که کاری با او ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/138774" target="_blank">📅 23:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138773">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqWyrK55Dt6Vb77tF9FD4_QDs4tXPaY_9nleb2yi_yk-2T0XQi63PqDMnUZvRE9gnS6m6Vu9If3oXhZiujERmlaMAozBFbXa5M77pwooPyMSGwOOHv6FiAiCL4K8HYlMjCTLIuTzV-D6zARFdxdbMZv4IJAK7LA5blhhopDuwKVkymwmG-PCoMmTZPBkVSXqBcw74mE6zNgu2fbxcWNvATh5Y7eYcyjbB_F6IwN2z9yMqVEX4zUiNaykWnTOONfBvAQxeg20Vj0o8ZrJVOAQCX95SXhSh5sYZstLzZr2-iZ4ZGAsoWtCLjhMfdUd6KlMreDi-MQk19ki2splF4hUpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۵ماه از غیبت صغری گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/138773" target="_blank">📅 23:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138772">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
آی۲۴ گزارش داد یسرائیل کاتز، وزیر دفاع اسرائیل، به همراه ایال زمیر، رییس ستاد ارتش اسرائیل، نشست ارزیابی امنیتی برگزار کرد. در این نشست، آخرین وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای مختلف بررسی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/138772" target="_blank">📅 23:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138771">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
اسرائیل منطقه المنصوری در جنوب لبنان را بمباران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/138771" target="_blank">📅 23:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138770">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فرمانده قرارگاه مرکزی خاتم الانبیا:
آمریکایی ها متوجه شدند تابوت هایشان بخشی از تجهیزاتشان در منطقه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/138770" target="_blank">📅 23:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138769">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bce6KCX2IXjKe5eUEihqjikkx9iILSXgQoXMwDr4sTJavaXhzwj8uUZoB3Y2Or5jvcjVJQ1E-jwNkFygHxtQC0WyX1ggPWPLVN4I1Kb1PVOrLdIwIMsG5rrPq5s63SX17CuDw7w5bR3Q99K6mIuE_i5QwcGB9r8yTISmWaTcy0UCsAHnA0MNdj9q45SN8ixD4E9v2kEO3igsIBp6g257BMJ8BucWPom58qfR6IMjoG3kLM343VF4YFoN1HQEENvhg1tP7IPw5ZJCL_o7ICd7C49U0zgyVNQos-hqLkKx9iCVMKiGdbcS0T9lfPTIxYi4Zx9iXpcvOwHQE5MNBB-fBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: تنش‌های آمریکا و ایران ممکن است همچنان مهار شده و بخشی از یک استراتژی مذاکره باشد.
🔴
مذاکرات با مسقط در مورد تنگه هرمز متوقف نشده است؛ نتایج آنها آینده تنگه را برای سال‌های آینده، فراتر از مدت زمان تفاهم‌نامه، شکل خواهد داد.
🔴
هرگونه توافقی در مورد تنگه می‌تواند راه را برای لغو محاصره دریایی و تحریم‌های نفتی هموار کند.
🔴
خوش‌بینی محتاطانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/138769" target="_blank">📅 23:29 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
