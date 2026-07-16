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
<img src="https://cdn4.telesco.pe/file/p-hI0ly1lm7c1VTKhaMth0gzLXHUlV2A-BH9E1cVMZJK35nMFBEVenufJqyVytgmMiKiMhSZw-8PipeW0OL4AsvSVTv4DKHUa4RDSIxQCltaRSvTzgS_mK-Y_kttN_AMOMJgVfwjnaLvbwxmhK7t1rDAj2_jZRvwg05tfLR6AyFWyXuz17WZhZo_F_84oiu7uPfagKdlVb0YlG3Ot02ftgh_xjncFzG_IMKxnVuggt2plHyAvbNfbzX9HElO_Cmu7UKR-tRxw6i4kf0iuOQn1DKAVvChCu1ER4wvWlxjZQvUhQruY2DltzEUVWSErjShU8GgIe0tNHUhTPsuuDBAbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 396K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 22:27:32</div>
<hr>

<div class="tg-post" id="msg-18438">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رسانه های سعودی : شنیده شدن صداهای انفجارهایی در بندرعباس، بوشهر، چابهار و کنارک
@WarRoom
.
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/withyashar/18438" target="_blank">📅 22:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18437">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گزارش انفجار‌ در کیش
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/withyashar/18437" target="_blank">📅 22:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18436">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e346db66bb.mp4?token=Z8Yd_mObpHbtC7yChfT3TgpLhbkxsZr_se8ptr8gXIYZLPeDCQvw_9-pkunN62nfZ0LBY7aIRCVQEayRacs8DqLL7YLIxNDsh6QrAdZH5VZA09hUi_ljJqInRYKRJInb6G0U_vnRfwBiYxaePSCd_d2CaDgPH-sgPDitDnrTw-VNdq2fI_OdqOW8hOunpVeRTAY2ncXQ5FB-94DDm9WlWa5wRoHYsGdiii-WcLzWeVHVH-8ot3rXZUfeCi96F0eKoMczMEha4MQsbigQsT0Jj1YHg83rfPWDouvD3lvFqizy3keoeGH-tGlHub0oIxDN6fCQ19MH_e83sPL18VBwIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e346db66bb.mp4?token=Z8Yd_mObpHbtC7yChfT3TgpLhbkxsZr_se8ptr8gXIYZLPeDCQvw_9-pkunN62nfZ0LBY7aIRCVQEayRacs8DqLL7YLIxNDsh6QrAdZH5VZA09hUi_ljJqInRYKRJInb6G0U_vnRfwBiYxaePSCd_d2CaDgPH-sgPDitDnrTw-VNdq2fI_OdqOW8hOunpVeRTAY2ncXQ5FB-94DDm9WlWa5wRoHYsGdiii-WcLzWeVHVH-8ot3rXZUfeCi96F0eKoMczMEha4MQsbigQsT0Jj1YHg83rfPWDouvD3lvFqizy3keoeGH-tGlHub0oIxDN6fCQ19MH_e83sPL18VBwIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس هم اکنون
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/withyashar/18436" target="_blank">📅 22:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18435">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هم اکنون دوباره سمت ایستگاه رادیویی پیامبراعظم بندر عباس @WarRoom</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/18435" target="_blank">📅 22:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18434">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=Ans5omMdf9ayrMQlOrzQCFyFQIH2G4JRV_EbObEC8-KpgKu3jWD2Ut92N60tUAtM83eVliOD_b7JiU9jUWKNXQTK3Yj0b5hdy7SBbCroXk9PJRjW9Rr1O_q69_rViIHgXmIxKwPItiKh7afmDqeIdCLnSovkm2qAVpzN8QwdnHab-dxxbsu0wVgJ2KdNiqc7l-AhUHadAo3SOh24tb_yGky1Mq-Nbse9SRZZCZETz5Only3X8ko5B4s-jbNzlTsTrEaK6ah_Mzs1B_dgfxe2ejh7rlYi_skhcaJKpKEfQKGtjBGlGoAQbu7KTS8CRshrSGUXSXY5N5LoamsdQiJscg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=Ans5omMdf9ayrMQlOrzQCFyFQIH2G4JRV_EbObEC8-KpgKu3jWD2Ut92N60tUAtM83eVliOD_b7JiU9jUWKNXQTK3Yj0b5hdy7SBbCroXk9PJRjW9Rr1O_q69_rViIHgXmIxKwPItiKh7afmDqeIdCLnSovkm2qAVpzN8QwdnHab-dxxbsu0wVgJ2KdNiqc7l-AhUHadAo3SOh24tb_yGky1Mq-Nbse9SRZZCZETz5Only3X8ko5B4s-jbNzlTsTrEaK6ah_Mzs1B_dgfxe2ejh7rlYi_skhcaJKpKEfQKGtjBGlGoAQbu7KTS8CRshrSGUXSXY5N5LoamsdQiJscg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس
@WarRoom</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/withyashar/18434" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18433">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجار چابهار
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/withyashar/18433" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18432">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بندرعباس چپ و راست آمبولانس و آتشینشان میره سمت شرق بندرعباس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/18432" target="_blank">📅 22:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18431">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">غروبه هرمز @WarRoom</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/18431" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18430">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سنتکام : در ساعت
۲:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
امروز
(۲۱:۳۰ به وقت تهران)
، نیروهای ایالات متحده
موج جدیدی از حملات
علیه ایران را آغاز کردند.
این حملات برای
پنجمین شب متوالی
با هدف
تضعیف بیشتر توانمندی‌های نظامی ایران
در حال انجام است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/18430" target="_blank">📅 22:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18429">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش انفجار بوشهر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/18429" target="_blank">📅 22:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18428">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">لطفاً تا فردا صبح هیچگونه سؤال سیاسی اجتماعی و تحلیلی نپرسید. لطفاً در مورد اینترنت خبریی ندهید. لطفاً صدای جنگنده ها را نگید. لطفاً فقط گزارش صدای انفجار رو بدید و تصاویر و عکس. همچنین پیامها را فقط همیشه در یک متن بفرستید، نه ده پیام جداگانه.</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/18428" target="_blank">📅 22:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18427">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vff7fqWUCnMZ6Uy04y7_PHhN7DwDWqG2n98emQz-jINEel7OdapTCcWqeo8_HQAEYoQwHtIrcl9KxtCx6iqEuWk06OyiTJCZOxX1HHHfmcDRVHvMWiyeCRq0-T5JpzzhKDGdw26I9SP5j_hzIZAf4rVxYZYVWlMmxaHQJrd5M4UNsHP2V0aylhj2Ku98B9_YjIDY2Nu_AzP1bJ6oMecR_s4JnhL3thIdFgZbZa2zXUnuPKctBihALg5U8xpn5BRWfUptzHROHYvloeTTzw7gtau7YK9NNqbVU3cDRgY53IpriqUpJ0kwOXZkr8NHXgHX7wIerL3IxWi65nwa2AyNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون دوباره سمت ایستگاه رادیویی پیامبراعظم بندر عباس
@WarRoom</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/18427" target="_blank">📅 21:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18426">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/18426" target="_blank">📅 21:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18425">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ادعای ترامپ مبنی بر آزادی یک زندانی آمریکایی از ایران تکذیب شد
ترامپ در حالی این ادعا را مطرح کرده است که با توجه به بررسی‌های صورت گرفته هیچ زندانی محکوم و یا جاسوس آمریکایی با مشخصاتی که ترامپ اعلام کرده و یا با هر مشخصات دیگری از زندان‌های ایران آزاد و یا تبادل نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/18425" target="_blank">📅 21:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18424">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بندر ادامه دارههههه ۵-۶ تا شد</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/18424" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18423">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ولی باید ببینیم امشب به اصفهان میرسه یا نه الان مرکز هدف اصفهانه کوه کلنگ</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/18423" target="_blank">📅 21:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18422">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجار همدان
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/18422" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18421">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تهران رو شاید بزنند ولی‌ نه به حالت زارتان زورتان به همون پارچین اینا بزنند فککنم</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/18421" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18420">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">۲ بار قشمممممم
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/18420" target="_blank">📅 21:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18419">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قشم رو زدنننننن
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/18419" target="_blank">📅 21:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18418">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بندر عباس زارتان زورتانهههههه
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/18418" target="_blank">📅 21:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18417">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت منطقه (۴ سوخترسان جدید بلند شد ، تحرکات زیاد در منطقه
🚨
🚨
🚨
🚨
) @WarRoom</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/18417" target="_blank">📅 21:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18416">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
حملات امشب شروع شد
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/18416" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18415">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شروع انفجارات بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/18415" target="_blank">📅 21:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18414">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae627587b9.mp4?token=iLCeomC25M2qcPzyRzJof_XcoeG7oyeMmXO0nGqKNW4vc-2GhiUQhhiiL_54j8YCrcGe7QclVD-L2gQwE7In-msNcj7tRaNm3ApoWGcoHtqjhaLmXRuME6MA0WPuakielaSF5sOZgNCDqq3N5rvyt2CVdrRaH8wuM_BgywCPOOwN9o4NOZb6i1XyrW9NTP9tXH8Gyvua6k3zKZwfO5kFxCYu9nN8jS3SHEf4ahUr4qeClKttf3tFb_gsGWZWIIYDQoghPkFC0ZcSbj9T1ERIHqjo42VyUT0ZIrulIeMCmqJbmDSYFGMabLLBwWHVPDMvSFbdIOXklYromW24d4w_mLQQWyuxSuQP359P3CChZTSotX2_tTUkkBEh5aWs-Xe94yRh2f1k-oEhT8WG_8ddEdCvFAKW7j4g1o__0hLAGQNIiPkrK7OkLyIZSsy_5I7eMR225lRUGGMDiUsP-XqJ2UlHKh99ZlBaXut5o1sw2JWcHCOk3tEUHkwj8gz4WzndHmKe2O53urfNFS9c22qXNhlQpSjr52ceCu_hJENbVySlTMnoNinhIhL61o0UmdUXMHwDmg_ay56Cqbp-1qziM7BpqIUzam99nd5Tl6Ms1Jf-6eQZzL4qPJGBdUNrBRbDwtTSDW7-gsP67LhuFIlmR7Yi_-KncWbpp09Kt0DHNH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae627587b9.mp4?token=iLCeomC25M2qcPzyRzJof_XcoeG7oyeMmXO0nGqKNW4vc-2GhiUQhhiiL_54j8YCrcGe7QclVD-L2gQwE7In-msNcj7tRaNm3ApoWGcoHtqjhaLmXRuME6MA0WPuakielaSF5sOZgNCDqq3N5rvyt2CVdrRaH8wuM_BgywCPOOwN9o4NOZb6i1XyrW9NTP9tXH8Gyvua6k3zKZwfO5kFxCYu9nN8jS3SHEf4ahUr4qeClKttf3tFb_gsGWZWIIYDQoghPkFC0ZcSbj9T1ERIHqjo42VyUT0ZIrulIeMCmqJbmDSYFGMabLLBwWHVPDMvSFbdIOXklYromW24d4w_mLQQWyuxSuQP359P3CChZTSotX2_tTUkkBEh5aWs-Xe94yRh2f1k-oEhT8WG_8ddEdCvFAKW7j4g1o__0hLAGQNIiPkrK7OkLyIZSsy_5I7eMR225lRUGGMDiUsP-XqJ2UlHKh99ZlBaXut5o1sw2JWcHCOk3tEUHkwj8gz4WzndHmKe2O53urfNFS9c22qXNhlQpSjr52ceCu_hJENbVySlTMnoNinhIhL61o0UmdUXMHwDmg_ay56Cqbp-1qziM7BpqIUzam99nd5Tl6Ms1Jf-6eQZzL4qPJGBdUNrBRbDwtTSDW7-gsP67LhuFIlmR7Yi_-KncWbpp09Kt0DHNH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تناقضات میان ادعاهای ونس و ترامپ نشان‌دهنده این است که در یک جبهه هستند
خبرنگار:
درباره ایران: رئیس جمهور ترامپ اخیراً گفته است: «از نظر من، سروکله زدن با آنها فقط اتلاف وقت است. آنها دروغگو هستند. یک جای کارشان می‌لنگد. آنها عوضی هستند. آنها آشغال، بیمار، شرور و خشن هستند.»
سپس ونس، معاون رئیس جمهور، دیشب به جو روگان گفت: «من از آمریکایی‌ها - و صادقانه بگویم از مردم کشورهای دیگر - که می‌گویند نمی‌توانید با ایرانی‌ها مذاکره کنید، بسیار ناامید شده‌ام.»
خب، پاسخ شما به این تناقضات چیست؟ فکر می‌کنم با توجه به پیام‌های متناقض، می‌توانید درک کنید که این موضوع چقدر برای آمریکایی‌ها گیج‌کننده است.
کارولین لیویت:
رئیس جمهور و معاون رئیس جمهور دقیقاً در یک جبهه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/18414" target="_blank">📅 21:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18413">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/18413" target="_blank">📅 21:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18412">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427068d887.mp4?token=J2S7HITiRuaMZHvef2USbKjPKlniSUJ8sXSCXgW8N_UYvl_K_FstXCx-iXe8CCrBgz8GyIb0C7dfdRoGD6F87PabNEHOqil80WaDKzR-QWa0sKpCDs46yjQWoUfW1yCUMMNZB4Ux1yp6TsGVhEWAWtVRy50NLLY08Tk-k54RhfyvJPd3-jvga8fGeCXCpLz4yy5odLySyVSxjtp_fYof1J59FiuMymHgKgJ7ZGLL8YfcYthEKhAeWQ4zh9c1dBbanMfiOeHpsjnR0uGeHCL1OqhFTYus3Hxq4vj_aHFxHi-vDxYryPIHz_f25wgi-NS64Dw-5elazxgNkg54eMJim7qcCVGCu7lz09zjj08Y44Dh8b7jKzKCi-E2rOxxStPZEpp8np50XJ9CL0K2m2jslYG6dABmkPvad6PBEc11UF3kjqJjrOj687d-BxPBEQxDCxJFDY1lcqWr8tAxv10NsIS4TCLQuqpyAlr5NiGSe8WrbjJ3Y386YZed_9wHstgLdVki_aOLqqGR5tfpj7LBlcJD4tpO8BEsWJjsdYQXcuvYr-euy7fL37PjzhhIMGs-RxNBpa5zliKZ-GIqLdaEwp5dqdvg4OyA4ETU83WwRmwrwJlG78b4UWgR9tbNc4ZTa_l62xOQ-uC-XqxQCfV9s8enRxNGy4KDV2mCrXIvgvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427068d887.mp4?token=J2S7HITiRuaMZHvef2USbKjPKlniSUJ8sXSCXgW8N_UYvl_K_FstXCx-iXe8CCrBgz8GyIb0C7dfdRoGD6F87PabNEHOqil80WaDKzR-QWa0sKpCDs46yjQWoUfW1yCUMMNZB4Ux1yp6TsGVhEWAWtVRy50NLLY08Tk-k54RhfyvJPd3-jvga8fGeCXCpLz4yy5odLySyVSxjtp_fYof1J59FiuMymHgKgJ7ZGLL8YfcYthEKhAeWQ4zh9c1dBbanMfiOeHpsjnR0uGeHCL1OqhFTYus3Hxq4vj_aHFxHi-vDxYryPIHz_f25wgi-NS64Dw-5elazxgNkg54eMJim7qcCVGCu7lz09zjj08Y44Dh8b7jKzKCi-E2rOxxStPZEpp8np50XJ9CL0K2m2jslYG6dABmkPvad6PBEc11UF3kjqJjrOj687d-BxPBEQxDCxJFDY1lcqWr8tAxv10NsIS4TCLQuqpyAlr5NiGSe8WrbjJ3Y386YZed_9wHstgLdVki_aOLqqGR5tfpj7LBlcJD4tpO8BEsWJjsdYQXcuvYr-euy7fL37PjzhhIMGs-RxNBpa5zliKZ-GIqLdaEwp5dqdvg4OyA4ETU83WwRmwrwJlG78b4UWgR9tbNc4ZTa_l62xOQ-uC-XqxQCfV9s8enRxNGy4KDV2mCrXIvgvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت منطقه (۴ سوخترسان جدید بلند شد ، تحرکات زیاد در منطقه
🚨
🚨
🚨
🚨
)
@WarRoom</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/18412" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18411">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانال ۱۵ اسرائیلی: ایالات متحده در حال آماده‌سازی برای گسترش حملات خود علیه ایران از نظر دامنه و تعداد است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/18411" target="_blank">📅 20:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18410">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGq6hpcIV9-Qt4BWtmnDDs40F9_LKhjsehha3obVvnMokQgDygUaPY_BXoQRM0mDis69PEBF8rL4b2dpunJ2h95XViDXtIU6Y7eiZD4ZyvBO2jkuWjyngGsvGQyWHtRy46rXYlBtas_mJPYX9Zpk_iRnPmcrH0LE96K00kd7d3BT88guCQ4QE006YzVwiirniahYmK_18uZHgDy9uJaipKoQtRp93WHwCistUEQ0idk6CF_ZzNhqibdF11ZxTLDMDyaGoC5No2A-m-sc1N8NLV8WRuDeuuFqvnJ6zoXeqX0Sp3TI1GCU9xyG7xRUodvFX6PgQpqnA_uTJb_1DcTbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل : فرمانده اطلاعات نظامی حماس در تیپ خان یونس را با انفجار خودرو در جنوب غزه به هلاکت رساندیم
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/18410" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18409">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتوبوس …. ببوس
😂</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/18409" target="_blank">📅 20:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18408">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رویترز:حمله بزرگ علیه ایران نزدیک است
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/18408" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18407">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/18407" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18406">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رویترز رو تبر‌ زدن خبر دبی فیکه
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/18406" target="_blank">📅 20:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18405">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اتاق جنگ با یاشار : میزو بچینم برای امشب</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/18405" target="_blank">📅 20:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18404">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خبرگزاری فارس:حملات هوایی دقایقی پیش چندین نقطه در اطراف بندر عباس را هدف قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18404" target="_blank">📅 19:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18403">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شاهزاده
رضا پهلوی:
سرکرده‌های رژیم آخوندها در تهران و پناهگاه‌های امن پنهان شده‌اند، اما سربازان وظیفه را در پادگان‌های آسیب‌پذیر رها کرده‌اند. او با بیان اینکه حکومت جان نیروهای نیابتی خود را بر جان ایرانیان ترجیح می‌دهد، از سربازان خواست جانشان را برای این نظام به خطر نیندازند و از خانواده‌ها نیز خواست تا حد امکان مانع اعزام فرزندانشان به خدمت سربازی در شرایط کنونی شوند. شاهزادت همچنین از اقدام مردم زاهدان و مناطق اطراف در کمک‌رسانی و اهدای خون قدردانی کرد و تأکید کرد جوانان ایران نباید قربانی بقای رژیم شوند، زیرا آینده کشور به این نسل نیاز دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18403" target="_blank">📅 19:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18402">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حسن روحانی : قبل از آخرین جلسه ای که قرار بود تمام مسولین نظام خدمت رهبر برسند (رمضان ۱۴۰۴) احساس خطر کردم و پس از تلاش های فراوان و فرستادن پیغام های مختلف برای شخص رهبر و تیم دفتر ایشان، موفق شدم جلسه را لغو کنم
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/18402" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18401">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1dea65f9.mp4?token=kjMORbZL7DI0OdorQkHMZFDnppsvqOgO1v6wivBIc30Fi7WrToDEZ6W1RrfRevGXXfS7EPAfwZsL8MlpPcfkO7l2BJtL49GKzCWHMOBc3yJYJbe0KxhebysgStsEwlr9DMNKDBlvMZqdL_F0W692DErJ_0VYg4wWflbEHQ72RBhQu5f2bM_Xvi4Dn5LGwFtPsVg9WDwm1V1iVcUs19JeyROOdb6BeHgDxPCBeaKhg14uCf6s8474Ktgp26H_WkkbvzY_SkJPt1Rr8myfw97rw18nHEbCURUiUT4aylgV8Z0ztu8_xG2zxIk8AYRnSIucEgjGMlwbY8IIhiXK1a1QFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1dea65f9.mp4?token=kjMORbZL7DI0OdorQkHMZFDnppsvqOgO1v6wivBIc30Fi7WrToDEZ6W1RrfRevGXXfS7EPAfwZsL8MlpPcfkO7l2BJtL49GKzCWHMOBc3yJYJbe0KxhebysgStsEwlr9DMNKDBlvMZqdL_F0W692DErJ_0VYg4wWflbEHQ72RBhQu5f2bM_Xvi4Dn5LGwFtPsVg9WDwm1V1iVcUs19JeyROOdb6BeHgDxPCBeaKhg14uCf6s8474Ktgp26H_WkkbvzY_SkJPt1Rr8myfw97rw18nHEbCURUiUT4aylgV8Z0ztu8_xG2zxIk8AYRnSIucEgjGMlwbY8IIhiXK1a1QFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهبهان ، خوزستان
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18401" target="_blank">📅 19:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18400">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صداوسیما: عصر امروز یک پرتابه دشمن به روستای مسن قشم اصابت کرد
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18400" target="_blank">📅 19:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18399">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سی ان ان: مطابق گزارش سی‌ان‌ان، ترامپ در مدت کوتاهی پس از خرید سهام شرکت‌ها توسط مدیران سرمایه‌گذاری‌اش، بیش از ۲۰ شرکت را در شبکه اجتماعی "تروث سوشال" مورد تحسین یا تبلیغ قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18399" target="_blank">📅 18:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18398">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">@warroom
جی‌دی ونس</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18398" target="_blank">📅 18:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18397">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir chvaie</strong></div>
<div class="tg-text">نظرت در مورد حرف‌های مفت جی دی ونس</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18397" target="_blank">📅 18:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18395">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">@warroom
تنگه باب المندب</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18395" target="_blank">📅 18:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18394">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromK!YΛП</strong></div>
<div class="tg-text">اون هواپیمایی که هرجوری که شده خودشو رسونده به یمن چه چیزی رو حمل می‌کرد؟</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18394" target="_blank">📅 18:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18393">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">صدای‌ انفجار از قشم/تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18393" target="_blank">📅 18:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18392">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه جولانی به حزب‌الله حمله کنه، پاکستان و عربستان به حوثی ها، آمریکا به ایران و اسرائیل به همهشون، روسیه هم که با اوکراین میجنگه. پس باید به زودی ناقوس جنگ جهانی خاورمیانه رو به صدا دربیاریم. جنگ جهانی ۲.۵
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18392" target="_blank">📅 18:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18391">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داد نیروهای آمریکایی در پیام رادیویی به کشتی‌ها اعلام کرده‌اند «مسیر جنوبی تنگه هرمز باز است». در یکی از ارتباطات، یک ملوان در پاسخ به این پیام با عبارت «گمشو» واکنش نشان داده است.
افسران نیروی دریایی آمریکا هشدار داده‌اند توان موشکی ضدکشتی و پهپادی ایران می‌تواند در صورت تشدید درگیری، تنگه هرمز را به یک «جعبه کشتار» برای نیروهای آمریکایی تبدیل کند. این گزارش تأکید می‌کند ایران همچنان دارای زرادخانه قابل توجهی از موشک‌ها و پهپادهاست که می‌تواند عبور کشتی‌های تجاری و نظامی در این آبراه حیاتی را مختل کند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18391" target="_blank">📅 18:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18390">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کانال 14 عبری: دستوری برای سیستم امنیتی تصویب شد مبنی بر اینکه حفاظت از نتانیاهو و همسرش در طول زندگی‌شان ادامه یابد، به دلیل نگرانی از احتمال وقوع انتقام‌جویی ایران از طریق ترور او. فرزندان نتانیاهو نیز در 5 سال آینده از محافظت برخوردار خواهند بود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18390" target="_blank">📅 18:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18389">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رویترز،: یک مقام پاکستانی پس از واکنش یمن به عربستان سعودی گفت :رهبران ارشد ما به ایران اطلاع دادند که حملات به عربستان، حملاتی علیه پاکستان است و عربستان، خط قرمز ما است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18389" target="_blank">📅 18:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18388">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه جولانی به حزب‌الله حمله کنه، پاکستان و عربستان به حوثی ها، آمریکا به ایران و اسرائیل به همهشون، روسیه هم که با اوکراین میجنگه. پس باید به زودی ناقوس جنگ جهانی خاورمیانه رو به صدا دربیاریم. جنگ جهانی ۲.۵
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18388" target="_blank">📅 18:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18387">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رویترز: نیروهای پاکستانی در عربستان در حال آماده‌سازی برای اعزام برای جنگ با حوثی‌ها هستند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/18387" target="_blank">📅 18:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18386">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMeli</strong></div>
<div class="tg-text">یاشار من سرکارم تهرانپارس اومدم دیدم عکس شاهزاده رو چسبونده بودن رو دیوارا اینام داشتن تند تند میکندن
🤣</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18386" target="_blank">📅 17:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18385">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جلیلی : مردم میگن حاضریم تمام کشور رو فدا کنیم اما انتقام رهبر رو بگیریم.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18385" target="_blank">📅 17:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18384">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f54f24594a.mp4?token=Rb8xh-LU3zTQ4m2NT06LfqDLG75Yr_ZygD5SqzuskIej6A1-dI95kQ9tQpTS5gH7bjMLdf1mGHV6dpJN_eyr-GVvVultyldaOsxgEWE_49Dswz4-hUyMmqAzEAJluWb6WeaAiCkotI5hLzfLeyNwg0XSkYw-hmbaMpk4-miec6JMJcqt3WQ3JOheXYXiw1nHDd69217j1m2fdaQWLe1HpK1ShBg1vTiLXihYh8zNe7ezCu-QHfl1RsYGfRAXFL5UbHhKoSc8W9TOhFQIdGelrotGjSfbkGenidN62ayGnQ4QOnCiqc02ahaqm7X_DX__7ovZBzCdJLdEFO44f048qheoTN2tpB83fWSq4d030u35zoZDKkVdzVGShBhfIT-i-71AC69dbYTslqafSh-70GA2eYaWrAlrHH8NewV3rhG5Dc7gRdSbjh3BOz26p47fecdg9Px0hnuDPSvMSx-3M8GDO12D3sutzNzOJtxe7-mcSGiPjJNJuIgxxLfDkF_5tqW_VI6LxuvID64BMcCqrNVpKWtmXVXA6Hpxb2V8dB4a3O7JNJ_BlPkrLut6EWaI_Castk3tCxe1aKsHnB-UEhQctScyzwAytodzeFg0HUvHU9hwjaRI3r6TnZMSWKX2X3Q3KjQNlG0ZoCLbDmXNyQ-7kbm6qi_w9YKuHXJFR6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f54f24594a.mp4?token=Rb8xh-LU3zTQ4m2NT06LfqDLG75Yr_ZygD5SqzuskIej6A1-dI95kQ9tQpTS5gH7bjMLdf1mGHV6dpJN_eyr-GVvVultyldaOsxgEWE_49Dswz4-hUyMmqAzEAJluWb6WeaAiCkotI5hLzfLeyNwg0XSkYw-hmbaMpk4-miec6JMJcqt3WQ3JOheXYXiw1nHDd69217j1m2fdaQWLe1HpK1ShBg1vTiLXihYh8zNe7ezCu-QHfl1RsYGfRAXFL5UbHhKoSc8W9TOhFQIdGelrotGjSfbkGenidN62ayGnQ4QOnCiqc02ahaqm7X_DX__7ovZBzCdJLdEFO44f048qheoTN2tpB83fWSq4d030u35zoZDKkVdzVGShBhfIT-i-71AC69dbYTslqafSh-70GA2eYaWrAlrHH8NewV3rhG5Dc7gRdSbjh3BOz26p47fecdg9Px0hnuDPSvMSx-3M8GDO12D3sutzNzOJtxe7-mcSGiPjJNJuIgxxLfDkF_5tqW_VI6LxuvID64BMcCqrNVpKWtmXVXA6Hpxb2V8dB4a3O7JNJ_BlPkrLut6EWaI_Castk3tCxe1aKsHnB-UEhQctScyzwAytodzeFg0HUvHU9hwjaRI3r6TnZMSWKX2X3Q3KjQNlG0ZoCLbDmXNyQ-7kbm6qi_w9YKuHXJFR6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غروبه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18384" target="_blank">📅 17:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18383">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مصطفی نجفی، مشاور محسن رضایی : تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18383" target="_blank">📅 17:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18382">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">در اقدامی بی سابقه، وزیر دفاع عربستان سعودی و معاون فرماندهی مرکزی ایالات متحده سنتکام در 24 ساعت گذشته 2 بار با یکدیگر دیدار داشته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18382" target="_blank">📅 17:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18381">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سی‌بی‌اس: ترامپ از رد پیشنهاد توافق هسته‌ای ایران ابراز پشیمانی کرده است
شبکه سی‌بی‌اس: دونالد ترامپ در محافل خصوصی، واشنگتن را به‌دلیل رد پیشنهاد تهران برای محدودسازی برنامه هسته‌ای مقصر می‌داند.
او معتقد است این تصمیم، فرصت کلیدی برای جلوگیری از گسترش درگیری‌ها را از بین برده است
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18381" target="_blank">📅 17:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18380">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هآارتص : ترامپ در حال بررسی عملیات زمینی در ایران و حمله به تاسیسات انرژی است
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18380" target="_blank">📅 17:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18379">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">منابع محلى از وقوع درگيرى دریایی بين نيروهاى مسلح ايران و نيروهاى ارتش آمريكا در تنگه هرمز خبر‌ می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18379" target="_blank">📅 16:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18378">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">همه برای من زدن که میگن بندرعباس صدای انفجار میاد، ولی بچه های بندرعباس، رگباری کسی پیام نداده که بندرعباس صدای انفجار شنیده باشه.
@warroom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18378" target="_blank">📅 16:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18377">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjX5UTr6JylIsWZa8s-6HXJLp-e4uTXSv07JXWr1M6oX0ako_eFvXsWqZlpN24oZozP_rdnNzw6zGs2Ui5fTLkze4bWohqFTk1WpW9tepRUnBTsCJ9NvKYKHQZbqF0lGaHaIt3QLr2ABE_YfAFmAQ5N-1c43C60e120SVYxTSclejGFoILeZW71vplAvEBMiRvJqL0UM9tfvJ_TK2P320CVhgpk_Z3J5dNURThyuPZSdYxoHFcseur_Baj-h5AKUt6gikTENVVtOMyv49NUwQxtKDNKu3s0h9502DF8Rrt7H9na5SGUmLN0dbRcIFKWp8YfBK2vMYpFKeGKAbjY0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سازمان آتش‌نشانی تهران: آتش‌سوزی مقابل شرکت مینو ارتباطی با این شرکت نداشته و ناشی از سوزاندن ضایعات توسط یک شرکت خصوصی بوده است. @WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18377" target="_blank">📅 16:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18376">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFRbI1w1yz0BeL8n3CZA0eWynfn0sUtmxZDphs3Lb0u5f1HK6ENGGC7kEZ4Y9Hb_od4NH2_5KjFpn7S0F3GWOIt7edHW3iRpu-zSVtYRzBz2MvK58hS0hDqxxecQOIuUAHJYcTx85E5IelYG5WegI38m-rIKvszq-FjaIUpKUmKwqx3AGVsXorP-TUwsJ4qVyuAfxNWX_jnYbB8Pr925DGb1mfa7qNbLYyX_BVYrkeRBPlAjG5l9Jcf47P8o3R3s-jT4m5-npIITvct5SFsgH7C-DRpQ3goBA1IeFeaFnvFvcYU-Y1dOQM3yb6C5ohVG5TpCQwQrM2o-MZ7NQEWc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سازمان آتش‌نشانی تهران: آتش‌سوزی مقابل شرکت مینو ارتباطی با این شرکت نداشته و ناشی از سوزاندن ضایعات توسط یک شرکت خصوصی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18376" target="_blank">📅 16:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18375">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وال‌استریت ژورنال: ترامپ شامگاه سه‌شنبه نشستی برگزار کرد تا درباره احتمال اشغال جزیره خارگ یا بمباران کوه کلنگ گفت‌وگو کند.
ترامپ در مورد اعزام نیروهای زمینی تردید دارد؛ او بارها از بزرگ‌ترین تهدیدهای خود عقب‌نشینی کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18375" target="_blank">📅 15:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18374">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اژیر خطر سفارت امریکا در بغداد فعال شد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18374" target="_blank">📅 15:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18373">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کانال 12 عبری: دیشب، ایالات متحده و ایران با یکدیگر تبادل آتش کردند. آمریکا به هدف قرار دادن اهداف در منطقه ساحلی ادامه داد، اما برای اولین بار، اهدافی را در مناطق پایتخت یعنی تهران مورد حمله قرار داد. ایران نیز موشک‌هایی را به سمت کویت، بحرین و اردن شلیک کرد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18373" target="_blank">📅 15:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18372">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2488574cc7.mp4?token=PKJuCXAQwEDNluxnguDgeI71j_upZ8CrwAaZq3gek3ozmqIoHQgQJEw-OD6qY2iyJYNMUYwUtwXbN9FsZo1l4Xoxha5u0jqhieB76KBsnx86NxZpukokVrfTZUfIZnrr82kp1jzGbCT99i8gSvaNJ2h4mlcWDU8-yvyInd1H4q7Wg0e54ZvG5VG9JqXnl9aUPx2A4RyTsBCREx6ygGoZBqRyTRZo_7AUVlEu8bUwxCb-URuE_UnpPn35vquBN4r4BzGNj3d7llGDHz-QfAW6UHhkULLHF-RuPFaeDsIy0BSOo5XZQsT7_HgFF9IlKN7PSzct17HOPa5T-DUCpQ4gpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2488574cc7.mp4?token=PKJuCXAQwEDNluxnguDgeI71j_upZ8CrwAaZq3gek3ozmqIoHQgQJEw-OD6qY2iyJYNMUYwUtwXbN9FsZo1l4Xoxha5u0jqhieB76KBsnx86NxZpukokVrfTZUfIZnrr82kp1jzGbCT99i8gSvaNJ2h4mlcWDU8-yvyInd1H4q7Wg0e54ZvG5VG9JqXnl9aUPx2A4RyTsBCREx6ygGoZBqRyTRZo_7AUVlEu8bUwxCb-URuE_UnpPn35vquBN4r4BzGNj3d7llGDHz-QfAW6UHhkULLHF-RuPFaeDsIy0BSOo5XZQsT7_HgFF9IlKN7PSzct17HOPa5T-DUCpQ4gpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : جنگنده‌های رادارگریز F-35A نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط یک فروند KC-135 Stratotanker در حین گشت‌زنی بر فراز خاورمیانه.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18372" target="_blank">📅 15:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18371">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حمله هوایی اسرائیل به شهرکی در جنوب لبنان
شبکه الجزیره از حمله هوایی ارتش اسرائیل به شهرک النبطیه الفوقا در جنوب لبنان در ادامه نقض آتش بس خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18371" target="_blank">📅 15:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18370">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELGwkHD9HZAYhbp0RCpKtLZoUB57LFw2fz_LQTBvni87hKuB18bf5tKZuy0rqirX_Mx_2QffRfguFDtaJGdVixRlP6C6Ai_MHPMXOCtlVtWUTAkfGY9k-CU1IWntuGt1SX1X9kyDK6tsFsdtgGM7wjYT40Na2lU9gymHsh5prcHJUkgsKewj-X2zT7vTY6ckEtnrPrC9GWKU2bkPi7uvxpELgcxOAvUvs_RZ-I0p4hKN6w51C1ySsQqhID9uyd9MwaEuYDGptie6xf0oSnGSWjs3uG202O2zVuB-KG0LR1-orNsvD0OK3Q7kEB3s2LqfP6fZZM8KqZMILlTTTDUydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا فغانی به عنوان داور فینال جام جهانی ۲۰۲۶ بین آرژانتین و اسپانیا انتخاب شد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18370" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18369">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ارتش کویت: پدافند هوایی ما در حال حاضر در حال دفع حملات پهپادهای متخاصم ‌رژیم ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18369" target="_blank">📅 14:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18368">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هم اکنون موج حمله جدید رژیم به کویت و درگیری سامانه های پدافندی کویت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18368" target="_blank">📅 14:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18367">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ارتش ایران: کشتی‌های ایرانی به عبور از تنگه هرمز به سمت اقیانوس هند ادامه می‌دهند و اگر واشنگتن ما را تهدید کند، پاسخ ویرانگری دریافت خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18367" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18366">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتاق جنگ با یاشار : تمامی کودکان بیمارستان سرطانی اهواز در سلامت کامل هستند و حدود دویست نفر آنها به مکان دیگری منتقل شدند. این بیمارستان هدف هیچگونه حملاتی نبود. فقط چون حملات بسیار سنگین بود در اهواز و در نزدیکی آنجا، مانند تمام نقاط دیگر و تمام کودکان آن…</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18366" target="_blank">📅 14:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18364">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">استرالیا در بحبوحه جنگ ایران، هواپیماهای راداری Wedgetail را به خلیج فارس اعزام می‌کند
نیروی هوایی سلطنتی استرالیا در حال حاضر ناوگانی متشکل از شش هواپیمای Wedgetail را اداره می‌کند که به عنوان پلتفرم‌های اصلی هشدار زودهنگام و فرماندهی هوابرد استرالیا خدمت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18364" target="_blank">📅 14:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18363">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حمزه امرایی، معاون سیاسی استانداری همدان از حملات بامداد امروز آمریکا به نقاطی در شهرستان کبودرآهنگ در این استان خبر داده است.
جزئیاتی در مورد محل‌های مورد هدف منتشر نشده است.
پایگاه سوم شکاری نوژه همدان در شهر کبودرآهنگ واقع است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18363" target="_blank">📅 13:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18362">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مجلس نمایندگان آمریکا شب گذشته لایحه توقف کمک‌های سالانه ۳.۳ میلیارد دلاری آمریکا به اسرائیل را رد کرد.
رای مثبت 103 نماینده دموکرات به توقف کمک‌ها به اسرائیل بود. موضوعی که به هیچ وجه 10 سال قبل قابل تصور نبود!
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18362" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18361">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تلگراف: انصارالله یمن در حال آماده‌سازی برای بستن تنگه باب‌المندب است
حدود ۱۰ تا ۱۲ درصد از تجارت دریایی سالانه جهان از این تنگه عبور می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18361" target="_blank">📅 13:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18360">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انتخابات آینده اسرائیل؛ سختی را
ه
برای نتانیاهو افزایش یافته است
انتخابات سراسری اسرائیل قرار است روز
۲۷ اکتبر ۲۰۲۶ (۵ آبان ۱۴۰۵)
برگزار شود. در این انتخابات، شهروندان اسرائیل به احزاب رأی می‌دهند و نخست‌وزیر از میان فردی انتخاب می‌شود که بتواند ائتلافی با حداقل
۶۱ کرسی از ۱۲۰ کرسی کنست
تشکیل دهد.
بر اساس برخی نظرسنجی‌های اخیر، وضعیت حزب لیکود به رهبری
بنیامین نتانیاهو
نسبت به گذشته دشوارتر شده و احزاب رقیب توانسته‌اند حمایت بیشتری جذب کنند. با این حال، نتانیاهو همچنان شانس بازگشت به قدرت را دارد، زیرا در سیاست اسرائیل توانایی تشکیل ائتلاف نقش تعیین‌کننده دارد
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18360" target="_blank">📅 13:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18359">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromƁ۝۝M 𓆏</strong></div>
<div class="tg-text">یاشار قبر خامنه آیه آتیش گرفته کونش داره میسوزه
😂
😂
😂</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18359" target="_blank">📅 12:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18358">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC8iTX6FrKr8_tyXfiXH7U-YbtHzkb7QMP28yJv4zEqF5n-n3AvjAHddNJCwtlcr0WDNBhLDQBP_gm9MSGpAnxGzglmi9VYgxK1XoJrx_tgLctgz7P1ITCtOtF3VGVS3NZ-rVRFVFkLmyxPcND5J7B4nK7n5wqLffi5Fmigok8XW6xKYqHsatyJr9wSt9Ac8SR177PxlKR4H5UimY6D_B0N4qZMPunxGNKL6IrmmGiKyoUytojaGRXxEhzeW2-zTZQT0-GLOX-QcLWfWgTYyzkWoto7qpIZViSI7jLK1UPaIy3x3QPWW-IYI0P8CuV8l5OlGv4JNiIlxx57COKPBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارگاه عمو قیرینیاهو وسط حرم
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18358" target="_blank">📅 12:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18357">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/286e4fdb4e.mp4?token=lxnZ2N0D2-l6UxjMBng-mihdyHMtuabNetg9Myxglbqrr16k3RI5JejsreFm-9bGEWA1ZPnTcsvxDItkrc8PZkcJ8cdgipY-nQmeJeHmDQlKNIf-8K5C5ZwI-ky8eFVmq9WEM_2xWpFsiU3o_wjb8y-uHOIa8u0nllxA0J6V078he8o26V4B2pKwJVbhLjOi-FOzOuTnF3u9UiEnWGX5s0io5hbUhDaS8oqbDTwg4I3y5JokRS-jNo4n8yxsnfLCWyW60zFdd-I4KEUzkhbMq--SP3B5fhvS74jNNnZ_HPq5duRgdafk1iBLoIq10w-JU6gth-DksXIkFEmY0Yt64g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/286e4fdb4e.mp4?token=lxnZ2N0D2-l6UxjMBng-mihdyHMtuabNetg9Myxglbqrr16k3RI5JejsreFm-9bGEWA1ZPnTcsvxDItkrc8PZkcJ8cdgipY-nQmeJeHmDQlKNIf-8K5C5ZwI-ky8eFVmq9WEM_2xWpFsiU3o_wjb8y-uHOIa8u0nllxA0J6V078he8o26V4B2pKwJVbhLjOi-FOzOuTnF3u9UiEnWGX5s0io5hbUhDaS8oqbDTwg4I3y5JokRS-jNo4n8yxsnfLCWyW60zFdd-I4KEUzkhbMq--SP3B5fhvS74jNNnZ_HPq5duRgdafk1iBLoIq10w-JU6gth-DksXIkFEmY0Yt64g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارگاه قیر مقدس مگه بوده که وسط حرمه ؟!
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18357" target="_blank">📅 12:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18356">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سفر نتانیاهو به آمریکا، به تعویق افتاد. مراسم سناتور گراهام هم به ماه بعد موکول شد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18356" target="_blank">📅 12:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18355">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">استانداری خراسان : یه کارگاه قیر اتیش گرفته @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18355" target="_blank">📅 12:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18354">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آتش سوزی گسترده هم اکنون مشهد سمت حرم @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18354" target="_blank">📅 12:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18352">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qqel59GzUIyofrPngE_A5bstITPFqI5fdX5H2vgZCBOU5LqZuFttvp7qm64zwnnkq2Wbs84HYFtxU2D8IF2mLBFcQ5lrxnmOlRfULDMJhuU6VjNeNgrZbQXdWdABtpJWJ1-O9IQ0DGxXzLKlP1f11XFn2cncScv73p-XNxpIy6se0V3Tg-RhHCiUiN_Hy1etRFuZATurXereEeX5hFCIh0tbwXumzs_P5deBdSuTVNPlxiw0rsoKX72Rurl93UEVdRy5jXxyy5wPDyZofcK2Xp0B28U-0i3GBVUZO9PeU0GAZnMrI6pQwaTzOPjSnyR1apMNj3Mp08O9cxCy28pxwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWKbfV8_TYFNxT3ck85SEwJtk9m6TxjGDzvWi2H4E9Vi_h5Kf0OSZD1tlaJyp4K_giX8Vb9xJraoexw0nIAS8U9A-Y0t8D0w-Oubxl9wPK7onPP4FdjB58ImrveSSctFkNAjh-wvW_0GXIblTl8lqIIqMFoeUj7WtCgs3iKeDcpSChpSvUEbgB-WIjiPdEeKwSUQA1WiWllG5T_xHhi787zpxZHduNr1-23ZMuUSJ1tijUzP5chU84PJbtu7WVDyx6phid-apoKZ4NU_zPIeBHBjd3mJq9cpk7gLsfoGTXP22bkF7wra_yOx0yOtP97vK5rxoom2ExmNF1s9RxJQwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آتش سوزی گسترده هم اکنون مشهد سمت حرم
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18352" target="_blank">📅 12:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18351">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانال الاخباریه سوریه، وابسته به رژیم جدید این کشور، از منبعی در وزارت کشور در دمشق گزارش داد که «یگان‌های ویژه، تلاش برای قاچاق محموله‌ای از سلاح‌های پیشرفته و موشک‌ها از طریق مرز با عراق را خنثی کردند.» به گفته این منبع، «تحقیقات اولیه تأیید می‌کند که محموله توقیف شده قرار بوده از طریق خاک سوریه به حزب‌الله منتقل شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18351" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18350">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بیانیه جمع کثیری از ساکنان جنوب به اتاق جنگ :  ما ايرانيان ساكن جنوب
كشور، ترحم نمى خواهيم؛
ايرانى بدون جمهورى اسلامى
مى خواهيم.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18350" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18349">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbdd26b83a.mp4?token=awmK7LjfA2lGjImNQXt6mAvZt-UUBABqmhdEP4hzAa4jfgHKL29sdJYrfi2o0lW6OFbd0E7JE6nFzIh3moGkK0lH9JfQqNoYrCyCh4x3xGHbcGHUHrRbcAqtzMm9zXZbztmlkGafts99IvxKoZuhEJisey_itq0-Y3jt4AzL4GPWIHz4aOXuKRxBapgbu46VOrrARRsMbxH1k9mh7Pvr1ASEB1qXOMYHVQAOFFsTbMhk5dtmAwstBc8LEr-qgZP3mp33pWP6Y4Oo_OkfdnxCUd0RR7tqHyBcrKs0mP2V8cB7c-dhuztue_JFkQrnloO4HAjdq1FgMQCZfY17bcsIGFwFkf43DS8Ba7OZ3xYI2fVHmDhS_AQccp9jqh55pXdOdza8C3PqGb99CVlgq2mIRrDYg66x_54h0S87me4V7qpG--tAylnB41XPLUEL72E6rawQRGt4rG82l9kRlKF-sFAwy5CWhKgwPnSO5F74RaFNFwgf3S1ZPMMICA0Dpi_3Lnidq9m-qy1ILRfJbWL6IUqxy7ORS0-evaUOk1l_Oz4JSEJA8wXRG5w7od9TzX8u6rcw8ZDtMfTsDMfDQnLH_6WneJlpZ_7ou_gAPVtWOFxaYiB-xVYyH1pf1qX1G_BoB3yGSVgOvIxw6ZRa8Ev2AILnNgNMnTL_NstsSd867UY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbdd26b83a.mp4?token=awmK7LjfA2lGjImNQXt6mAvZt-UUBABqmhdEP4hzAa4jfgHKL29sdJYrfi2o0lW6OFbd0E7JE6nFzIh3moGkK0lH9JfQqNoYrCyCh4x3xGHbcGHUHrRbcAqtzMm9zXZbztmlkGafts99IvxKoZuhEJisey_itq0-Y3jt4AzL4GPWIHz4aOXuKRxBapgbu46VOrrARRsMbxH1k9mh7Pvr1ASEB1qXOMYHVQAOFFsTbMhk5dtmAwstBc8LEr-qgZP3mp33pWP6Y4Oo_OkfdnxCUd0RR7tqHyBcrKs0mP2V8cB7c-dhuztue_JFkQrnloO4HAjdq1FgMQCZfY17bcsIGFwFkf43DS8Ba7OZ3xYI2fVHmDhS_AQccp9jqh55pXdOdza8C3PqGb99CVlgq2mIRrDYg66x_54h0S87me4V7qpG--tAylnB41XPLUEL72E6rawQRGt4rG82l9kRlKF-sFAwy5CWhKgwPnSO5F74RaFNFwgf3S1ZPMMICA0Dpi_3Lnidq9m-qy1ILRfJbWL6IUqxy7ORS0-evaUOk1l_Oz4JSEJA8wXRG5w7od9TzX8u6rcw8ZDtMfTsDMfDQnLH_6WneJlpZ_7ou_gAPVtWOFxaYiB-xVYyH1pf1qX1G_BoB3yGSVgOvIxw6ZRa8Ev2AILnNgNMnTL_NstsSd867UY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این به من قدرت میداد که در مقابل  حوادث و اشکالات هیچوقت خم نشوم
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18349" target="_blank">📅 11:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18348">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlIz7rLVhsMbgkNoNfm0ilSZ2umgaMEOMHQP18NzZvN6pYIenJUzPN85wZZXPfTLst8Hjl1fkHIrCEK9uNNh5yDIsxWCTf_76V8t-x2LmctxgUvz7DMCb1hLfxM-nuMADFUOASV5FAySBkcMLUjicuLDw25vfAIadEaZ67L1GPNCcd_R98DBd_s9Pb6NYMYps80ukLU2HjOUvaJ_4xXBGSVJeDjfMniyOpiUJHsDk4TwgP6Pej9DwcvQ6LyO0zcUMgs96MCEP-ju9JBcWkY6o11mcBmMWMIc7MZAADHjRenAMPcfJhKtuMcQb_XqJ4IiqE1Rk6C_1G5ON16cRUMeyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18348" target="_blank">📅 11:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18347">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گزارش های زیاد از‌ سر تا سر مازندران مبنی بر قطع شدن آنتن ایرانسل
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18347" target="_blank">📅 11:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18346">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نیروهای دفاعی بحرين: سامانه‌های پدافند هوایی، تعدادی از حملات هوایی خصمانه رژیم ایران را امروز شناسایی و خنثی کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18346" target="_blank">📅 10:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18345">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کپلر: ۷ کشتی دیروز از تنگه هرمز عبور کردند که هیچ‌کدام نفتکش یا حمل‌کننده گاز نبودند.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18345" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18344">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزارت خزانه داری آمریکا؛ ۱۳۰ میلیون تتر دیگه از دارایی های ایران رو مسدود کرد!
جمع کل تترهای مسدود شده بانک مرکزی هم تو یک سال گذشته از ۱ میلیارد تتر عبور کرده...
@WarRoom
Tether = 189,000 T</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18344" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18343">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اتاق جنگ با یاشار : ‏قرمساقا هر چی دلقک و لمپن و خالتور تو فضای مجازی بود رو بعنوانِ کارشناس آورد تو صدای آمریکا فقط و فقط برای اینکه به پهلوی حمله کنن، تهشم میگفت صدای آمريکا بیان کننده نظرات رسمی دولت آمریکاست!
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18343" target="_blank">📅 10:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18342">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اتاق جنگ با یاشار : تمامی کودکان بیمارستان سرطانی اهواز در سلامت کامل هستند و حدود دویست نفر آنها به مکان دیگری منتقل شدند. این بیمارستان هدف هیچگونه حملاتی نبود. فقط چون حملات بسیار سنگین بود در اهواز و در نزدیکی آنجا، مانند تمام نقاط دیگر و تمام کودکان آن شهر و دیگر شهرها، در آنجا هم بسیار احساس میشد در نتیجه سوژه خوبی برای پروپاگاندا رژیم قرار‌گرفت ، تمام کودکان ایران فرزندان ما هستند و دردشان درد ما ! مانند دانش آموزان ما که صدایشان شنیده نمیشود و باید به آنها هم توجه شود !
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18342" target="_blank">📅 09:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18341">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شهر هایی که دیشب مورد حملات ارتش آمریکا قرار گرفته اند
💥
اهواز
💥
بندرعباس
💥
جزیره قشم
💥
سمنان
💥
سیریک
💥
چابهار
💥
کرمان
💥
بوشهر
💥
همدان
💥
کنارک
💥
راسک
💥
خنداب
💥
پاکدشت(پدافندی)
گسترده تر شدن موج حملات ارتش آمریکا و حمله به شهر های مرکزی
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18341" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18340">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دفتر کاتس ،وزیر دفاع تأکید کرد که اسرائیل بر ماندن در مناطق امنیتی در سوريه، غزه و لبنان اصرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18340" target="_blank">📅 09:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18339">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18339" target="_blank">📅 09:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18338">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در درباره تهدیدهای مطرح‌شده از سوی ایران علیه جانش: «اصلا فکر نمی‌کند».
او در گفتگو با فاکس بیزینس تاکید کرد: «اگر به این مسائل فکر کنم، دیگر نمی‌توانم مؤثر باشم.»(۳دقیقه با زیرنویس)
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18338" target="_blank">📅 09:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18337">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اطلاعیه سپاه  استان تهران درباره صدای شنیده‌شده در پاکدشت : عملیات پدافندی بود؛ هیچ اصابتی رخ نداده است
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18337" target="_blank">📅 09:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18336">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18336" target="_blank">📅 08:48 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
