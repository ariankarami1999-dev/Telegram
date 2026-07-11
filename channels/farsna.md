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
<img src="https://cdn4.telesco.pe/file/ZCqcQ8i2RsBMf_LxmISIrqVNjhLjOylK3ACjs2oJ6NwLXREV8uRAVpetpUeUtcsq3xRKBxGaWEmSH0S5hllGBrpc7AwCrjOXwaz5u7lH298YAD1cUhio4RDy-QBJgBzA3EjGxjiv4gfdtPA_5_RzpWVzXoG9rk1CV2oRKdEeR1VAYjCzTqTQok24eJYZjNIT6ihsGGvstlvSjysMTvzZmtKRYBBLuSuBCt5aKfC1m4d3DMnC-PgSaW58J313gvoXligjN2cbO5MjOE4h3iQ3ciavtLVZNhS1rYlzKWVOgtVXBH-mt7hLBCXy1oiTcsiViTjLQSdi8NmrH5tlBJuMDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 17:52:09</div>
<hr>

<div class="tg-post" id="msg-449184">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3M4hOCktrHKjxM4Xwa2qGpUYZXUEF4DNCi__W5ThDdmoJV0VTgKofDU87m9WMZ2abZhuR6UhpmjRijrCgyf2ip3ppomG0UdjeOtx2X0qnWFWtD_6hB4HYRl4FZTZFkMQpjvZjZ7PTsvQYyQyES0INiHX84QOQh-ZjfHpKV-g-ScIcQRrOX0Hg592j73PkjGQ2MMmatuEgFMgPgb4IIClOciOlnlTmP9IAjsfxfuk1FEwgIM5WYDth4jocMBmPRytFqUtN8av-J4sODAfmSbXmxpdilzGbi9QhYIXSHY7q9csrgdpIMYBxp-PV3tBOj6XK0W7JmyQRcS3YhH5jQVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: نقاط آسیب‌پذیر دشمن شناسایی و محاسبه شده و می‌دانیم در چه زمان و چگونه بر دشمن فشار وارد کنیم
🔹
ایران در جنگ تحمیلی دوم و سوم با پیشرفته‌ترین فناوری‌های اطلاعاتی، نظامی و جنگ روانی مواجه بود؛ عملکرد نیروهای مسلح در جنگ رمضان نسبت به جنگ ۱۲ روزه مبتکرانه تر و مقتدرانه‌تر در حوزه تاکتیک و تکنیک بود.
🔹
با وجود گستردگی و پیچیدگی میدان نبرد، نیروهای مسلح در کوتاه‌ترین زمان ممکن پاسخ قاطع به دشمن دادند؛ جنگ تحمیلی سوم بار دیگر ثابت کرد هر جا بر فناوری‌های نوین و دانش‌بنیان سرمایه‌گذاری کرده‌ایم، موفق بوده‌ایم.
🔹
تقویت بودجه دفاعی، توسعه فناوری‌های پیشرفته، بهره‌گیری از ظرفیت نخبگان داخل و خارج از کشور و ایجاد سازوکارهای چابک برای اکتساب فناوری باید با جدیت دنبال شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/farsna/449184" target="_blank">📅 17:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449183">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b54c80aa6a.mp4?token=HCpIbfVjt4ar9RQAPozrCFdlZx_u9-xZoeSA7BBgos7JTwjLyg4o0OAw4oRgNKbGt0SEy8ALDFHiEWuGDOqwE5oklKId9xQ3ZINFsyz9jwIo10PUoy7Qaif07QT5hmr4eJ2UYsYEKtw30jP2c0rMOuQupBEl4T9cZXykFqvM0ucSfhTKM_SkrmJQcx9gHStwFnSptHX1PjJT4QjhWGPXOEqDiGodwNYSnX6mwj-KWAXfRIr2CdL5rXJ7kH70oyNRKCiNl-TUuTFWe_zG7A9D3pgJF-sMbMBWdgIM68SLthubjb-jykp-doMb0JAAASE7_ow7FMJyaNrYolQVqfSYJrPM4J8SwjdAlmeQ6u0wpLF-90gPTvHBGHz--97Ez9ncST0NZUOFQI1i5jWZ0IeRj_sUqndlsGdlWX2jDnzCklAVIE8oF1YuN7a6Ey_Gn3Y_Xtbfp3403luTyN2KMsiFi9HN9wAt6txNVp18HAXi3XsB-xJZ_K2MQP-LCR3d5x61J9HcMMleCFMis0MF-DvrKffdPJPFGp8eVoOoLtetlzmtqzQktgDBmjUfz0Uua3xVhYpaqkM_YSa3yTqWDThXD92b3zOfhzQE68cwj4Cat0U3gGt22ZF_pqKoamkzzjxmndaS2jyQCtSHsIFJ9OmBbT4xOOc2NSBWBajTTI0j8W4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b54c80aa6a.mp4?token=HCpIbfVjt4ar9RQAPozrCFdlZx_u9-xZoeSA7BBgos7JTwjLyg4o0OAw4oRgNKbGt0SEy8ALDFHiEWuGDOqwE5oklKId9xQ3ZINFsyz9jwIo10PUoy7Qaif07QT5hmr4eJ2UYsYEKtw30jP2c0rMOuQupBEl4T9cZXykFqvM0ucSfhTKM_SkrmJQcx9gHStwFnSptHX1PjJT4QjhWGPXOEqDiGodwNYSnX6mwj-KWAXfRIr2CdL5rXJ7kH70oyNRKCiNl-TUuTFWe_zG7A9D3pgJF-sMbMBWdgIM68SLthubjb-jykp-doMb0JAAASE7_ow7FMJyaNrYolQVqfSYJrPM4J8SwjdAlmeQ6u0wpLF-90gPTvHBGHz--97Ez9ncST0NZUOFQI1i5jWZ0IeRj_sUqndlsGdlWX2jDnzCklAVIE8oF1YuN7a6Ey_Gn3Y_Xtbfp3403luTyN2KMsiFi9HN9wAt6txNVp18HAXi3XsB-xJZ_K2MQP-LCR3d5x61J9HcMMleCFMis0MF-DvrKffdPJPFGp8eVoOoLtetlzmtqzQktgDBmjUfz0Uua3xVhYpaqkM_YSa3yTqWDThXD92b3zOfhzQE68cwj4Cat0U3gGt22ZF_pqKoamkzzjxmndaS2jyQCtSHsIFJ9OmBbT4xOOc2NSBWBajTTI0j8W4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید خیلی بامعرفت بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/farsna/449183" target="_blank">📅 17:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449182">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3cd335d0f.mp4?token=QLgUG5-wsu_CSctzHmZVdKR1JBrDLXDxoEYwrP86UkdzVEhemAaubfgnJ6kZGtTb-Zf1NRjYa44wGZqSVNYVTL2LX5uM1zgnTbwMgXHFVAAgLYjXBA4xNZ9nnpXn2LJZf2RrR3yhW6igAnIDfwYbF-tCuYd4AykxXW5pet0m1zwqn5cYOQCtqj-MedXSdAZSBhLqirw-sWZ2fC5Ly9TFawHX2Wo4pDLUWCQC6AXLsYs54DaPf2da2xnET-dijQ93vnZkMjiTZgHd68nxtvzNSeqbntZBPc16I8p8aMilgGGEjiSKuFphF9GIkFnaX4Cs9qRZP2ZNh0YUW-lZS7Rvfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3cd335d0f.mp4?token=QLgUG5-wsu_CSctzHmZVdKR1JBrDLXDxoEYwrP86UkdzVEhemAaubfgnJ6kZGtTb-Zf1NRjYa44wGZqSVNYVTL2LX5uM1zgnTbwMgXHFVAAgLYjXBA4xNZ9nnpXn2LJZf2RrR3yhW6igAnIDfwYbF-tCuYd4AykxXW5pet0m1zwqn5cYOQCtqj-MedXSdAZSBhLqirw-sWZ2fC5Ly9TFawHX2Wo4pDLUWCQC6AXLsYs54DaPf2da2xnET-dijQ93vnZkMjiTZgHd68nxtvzNSeqbntZBPc16I8p8aMilgGGEjiSKuFphF9GIkFnaX4Cs9qRZP2ZNh0YUW-lZS7Rvfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این پیرزن ۹۴ ساله‌ با ویلچر در مراسم عزاداری رهبر شهید شرکت کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/449182" target="_blank">📅 17:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449181">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a20b915b99.mp4?token=kEuqTa5ECCvo92LhKO0Yat_EilkkbHF914Pm_8HT2MLLA_oJqF32Wzy2MboSAtlZfNITBBnaKHJ4uD00ugJ2Bq7N4mZdg9wTdqgZJqz2ThCwjhQ_BNaJVwmwiOpadvUAwr1hbX9cg29p8OLXa0CLn8c0ZOHY4B2rhtJ4nwVmfVykalaj0cCBvRTCHAvgNtdKCZR-26obCzycyjOqobCG_4vBKwbRx5zTpPx9jBUWIzIaXiiO8ZWHnEePD5xEGtB-ds3W2CcFeapwGsydd4xU6L-283UvKWG2-GyJcnA18JEk6Ga_NfnzRzSwTporQYES-8x3XMO9ZCx_QnakT6om0XuEXJh5QVnmcYn74cTSvPZQNcmk0ve-6E9sysUMoFAvDJsmL7I71LeVZFkqaobkgZWIWALs-904v8Z34AamReKxlcz3w0zxIua7XRrWlpccf1lQvGKbf6edeoV3yMe2ul5ATtKd-K6gdpZrzeGPrADnBf4iJRpd-eXzksoPnjW-quNnwRFOEm7hECwKzIeuxtMn62kngHpPKU2GY10RtZ2gA6xofL5PnmEjaKmAmYX3U8Od1ROCnUMEYkRZwTH58_1iwg3QcPkqEHKWTHvQCt76gwJOXmdR2oIRPkLVTQbL35LB4Q7wMQjZLLBn1modqM8Cc-304-QKKNo80W4osm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a20b915b99.mp4?token=kEuqTa5ECCvo92LhKO0Yat_EilkkbHF914Pm_8HT2MLLA_oJqF32Wzy2MboSAtlZfNITBBnaKHJ4uD00ugJ2Bq7N4mZdg9wTdqgZJqz2ThCwjhQ_BNaJVwmwiOpadvUAwr1hbX9cg29p8OLXa0CLn8c0ZOHY4B2rhtJ4nwVmfVykalaj0cCBvRTCHAvgNtdKCZR-26obCzycyjOqobCG_4vBKwbRx5zTpPx9jBUWIzIaXiiO8ZWHnEePD5xEGtB-ds3W2CcFeapwGsydd4xU6L-283UvKWG2-GyJcnA18JEk6Ga_NfnzRzSwTporQYES-8x3XMO9ZCx_QnakT6om0XuEXJh5QVnmcYn74cTSvPZQNcmk0ve-6E9sysUMoFAvDJsmL7I71LeVZFkqaobkgZWIWALs-904v8Z34AamReKxlcz3w0zxIua7XRrWlpccf1lQvGKbf6edeoV3yMe2ul5ATtKd-K6gdpZrzeGPrADnBf4iJRpd-eXzksoPnjW-quNnwRFOEm7hECwKzIeuxtMn62kngHpPKU2GY10RtZ2gA6xofL5PnmEjaKmAmYX3U8Od1ROCnUMEYkRZwTH58_1iwg3QcPkqEHKWTHvQCt76gwJOXmdR2oIRPkLVTQbL35LB4Q7wMQjZLLBn1modqM8Cc-304-QKKNo80W4osm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه‌ای که هر ایرانی، راوی آن شد
@Farsna</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/449181" target="_blank">📅 17:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449180">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0010f8fac.mp4?token=kFoadoz6kWC49470tSTUG0x-EAR2BlJbOxo_R0OTu6djxssOyyO8z4f_nkQdeGGNSQ0iDVD5VcMyR6EsQpBtQd3VptgjtEhMCcTefhaamITHHxfzyw9tYmXpYQWAAGmZU8mNhOvud7Fqp-o2Ej0TQzisS8OLneIScJ-FKZc86OQqr2q92QKDllGf1hKpBL-XLL_a9vhSFcnCrqsXlA1Vj95i6eywbKDDzMUTNQ-1ReemSApQtDUO-DJ_Tbn5C0ZZ4-u77JVCe8OaIMuHbv7lWYqmSSL6fP3SoIq7WTdZzelLXI2wH3KvR8BKy0FZVFbECGXPyBg-0UlEli3v0SVCVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0010f8fac.mp4?token=kFoadoz6kWC49470tSTUG0x-EAR2BlJbOxo_R0OTu6djxssOyyO8z4f_nkQdeGGNSQ0iDVD5VcMyR6EsQpBtQd3VptgjtEhMCcTefhaamITHHxfzyw9tYmXpYQWAAGmZU8mNhOvud7Fqp-o2Ej0TQzisS8OLneIScJ-FKZc86OQqr2q92QKDllGf1hKpBL-XLL_a9vhSFcnCrqsXlA1Vj95i6eywbKDDzMUTNQ-1ReemSApQtDUO-DJ_Tbn5C0ZZ4-u77JVCe8OaIMuHbv7lWYqmSSL6fP3SoIq7WTdZzelLXI2wH3KvR8BKy0FZVFbECGXPyBg-0UlEli3v0SVCVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسیر ما بعد از شهادت رهبر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/449180" target="_blank">📅 17:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449179">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a05b8dab0.mp4?token=d_DgP2s0r0qQ9Sgl_hcsReIINARflQJc_dv-Bq6vz7jvKO0lY29zK6BneE1iHZdVh9f4FYbsf9IsTV2UK7VMCN4eKE7K6Ce4Al1TKxOjZXtJBEr-KcX4j_0YwVT7KyuXoiTAB-S3zq2IHThgUsYTywfWckTz8vR1GTbDPi59bzcBWDj9UakncOPGwfvwW1ni-mQZYViLGtMk_fE6qmHF65LzSClhbpGZhJsxe5TZIAruqTPxKMZtrHJf2m0Ya-DZKS-X_Zawz84KheZjyrcdySChTOBpEJLdHGdBnx3RiZAXrdoMDrf1-h8Vl4LKMIzvcWKuc1K7zR-JPqXAnH2SJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a05b8dab0.mp4?token=d_DgP2s0r0qQ9Sgl_hcsReIINARflQJc_dv-Bq6vz7jvKO0lY29zK6BneE1iHZdVh9f4FYbsf9IsTV2UK7VMCN4eKE7K6Ce4Al1TKxOjZXtJBEr-KcX4j_0YwVT7KyuXoiTAB-S3zq2IHThgUsYTywfWckTz8vR1GTbDPi59bzcBWDj9UakncOPGwfvwW1ni-mQZYViLGtMk_fE6qmHF65LzSClhbpGZhJsxe5TZIAruqTPxKMZtrHJf2m0Ya-DZKS-X_Zawz84KheZjyrcdySChTOBpEJLdHGdBnx3RiZAXrdoMDrf1-h8Vl4LKMIzvcWKuc1K7zR-JPqXAnH2SJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند کلام با امامِ شهید
@Farsna</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/449179" target="_blank">📅 17:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449178">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-pGCmg1E5ia5XqQyfKoT_9PluZVBl1-1UkA6k4ShwaYcnbw4Y_h8H2_zN8gyAvGD0FCO4ZPj-BU5nPmu9y9T68v3VQvjOpRB6Q_cbFfYspwxA9if-M8PfoV9kVQbUFFXF74hwrj6cNTIWF-qQymqokd8wyWaIwUN4KVQF9U_wkkXvyxuraoyql-U_9X3GMHMCdcK_1uoZj3qIE0w8-sb9XBMEdfuYk-r8bgj_jCVymZ4PRN0mW6B-jZVsIEt9xWnl5kH9dZZQshACXb_aWhYXeiRSWWzh4a_U1QqVNmHEhbMYda0BdPVqWBg3NoFEY8ys6OSv1Auu2AE15xGfz1-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوت ناگهانی بازیکن آفریقای‌جنوبی حاضر در جام جهانی
⚽️
جیدن آدامز، بازیکن تیم ملی آفریقای جنوبی که در جام جهانی ۲۰۲۶ برای کشورش مقابل مکزیک، چک و کره‌جنوبی به میدان رفته بود، در سن ۲۵ سالگی درگذشت.
⚽️
براساس گزارش‌ها، علت مرگ آدامز هنوز اعلام نشده اما برخی از احتمال خودکشی او خبر داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/449178" target="_blank">📅 16:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449177">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d00e25a504.mp4?token=pHJXgiQ0eZksqCPUqPwKOCQkUXw9PJZL7gmPj9AVw4IH3RxNuXbncUjJNou8nK_IorV9HCzrkpgpI35D4rqnclGZukO6-UBmI_uUiBWCqs-73y64Gklr5UmLRZ3GV6WGhg9OrUoJkNy9L4WzEz3Wt-pJoVeqxfrvs4l8_12vcK_9o6NY4tGmzu2vegtbUJ2Ee0Z_8JNCPMwz5rTBcf3B4_0unthvNnTuoBIB5_set4aThAThUD8RIJVWaWMFctVrNcQv1VkaPWSAt_D3nAPK_9YzYkzaNkonzYKGwtJO_2tXbbFuIMJVKGUW31oY0nvGhZixMWcfMnQgCmBAzH0nK0mzzG8ulRt8EWKUhEmk9j4_slxp2ySOwt3LeZHqTlAyqLw9h3l7POXvXlj-bR91_lSIwhlBDqyVpsDXOj2yEGS7SwZO5MTLZeuFxL98vJNqkxlJAobkt-lUaP6Y4pYvD2G67PclblUHWyaDk-Du_8zoeKAcL37SyoLSpU83gvHKSbWGVvwoip6Lr2uyt9HLCZu-i8LKxJDm4f6yxsSwO3mzfS-Un_Tr4jvGc1Yo1Lkv1jUwIkztPluTQRE5NDX8NU3rqYdJR0Zv4oayykcjOm6JzLmWXPe8opTJP9cUhv_ohHVFpQ7sEfoiK-yAfbslbYm0K2Ircq3BRxrxm9koi7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d00e25a504.mp4?token=pHJXgiQ0eZksqCPUqPwKOCQkUXw9PJZL7gmPj9AVw4IH3RxNuXbncUjJNou8nK_IorV9HCzrkpgpI35D4rqnclGZukO6-UBmI_uUiBWCqs-73y64Gklr5UmLRZ3GV6WGhg9OrUoJkNy9L4WzEz3Wt-pJoVeqxfrvs4l8_12vcK_9o6NY4tGmzu2vegtbUJ2Ee0Z_8JNCPMwz5rTBcf3B4_0unthvNnTuoBIB5_set4aThAThUD8RIJVWaWMFctVrNcQv1VkaPWSAt_D3nAPK_9YzYkzaNkonzYKGwtJO_2tXbbFuIMJVKGUW31oY0nvGhZixMWcfMnQgCmBAzH0nK0mzzG8ulRt8EWKUhEmk9j4_slxp2ySOwt3LeZHqTlAyqLw9h3l7POXvXlj-bR91_lSIwhlBDqyVpsDXOj2yEGS7SwZO5MTLZeuFxL98vJNqkxlJAobkt-lUaP6Y4pYvD2G67PclblUHWyaDk-Du_8zoeKAcL37SyoLSpU83gvHKSbWGVvwoip6Lr2uyt9HLCZu-i8LKxJDm4f6yxsSwO3mzfS-Un_Tr4jvGc1Yo1Lkv1jUwIkztPluTQRE5NDX8NU3rqYdJR0Zv4oayykcjOm6JzLmWXPe8opTJP9cUhv_ohHVFpQ7sEfoiK-yAfbslbYm0K2Ircq3BRxrxm9koi7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم آستارا در سومین روز خاکسپاری امام شهید امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/449177" target="_blank">📅 16:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449176">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTth42eJYw_qrsFqh6dL8fPHw_mIruXzyrNQFPYLE-p8A_YbmADsPobvVUFq2kISUDTwEkri4f7zgN8_VxpDO8GVDkd-gciy2RlaDgL7_xRcigRe6gZczCxla5s4dJPlXI0LaQdjbA99ZjeHdAwKSuQ_L78J8yO7PbYmLKMM1fyPcqm6h9UVlrQxEpYG08ED9K8tqfL2mPg98RBAA0XkiufABpVcKqq9_1oZzpZs2Hnsk5qMQNp0M-3v3yl3yyxRSVrHeXjEwHlWWkBpeDODvqaFTZYBC6j5q-WQ5trle4VrsjyGJ2K8HStaxRDVBLh8RVhAWrpxIIyxkR2uJNpJsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس: قاتلین امام شهید به سزای اعمال خود خواهند رسید
🔹
کوثری: ما باید به معنای واقعی کلمه بگوییم که انتقام ما از دشمن دو جنبه دارد: نخست، حذف کسانی که در به شهادت رساندن حضرت آقا و فرماندهان دستور دادند که این افراد حتماً شناسایی شده‌اند و مورد نظر مردم و مسئولان قرار خواهند گرفت.
🔹
دوم اینکه، بالاخره این کسانی که به ظاهر زندگی دنیایی اما در واقع یک زندگی حیوانی دارند قطعاً به سزای اعمال خود خواهند رسید.
🔹
ما بایستی راه رهبر شهید انقلاب را با صلابت و محکم ادامه دهیم و ان‌شاءالله خواسته‌های ایشان را که مسیر رسیدن به قله است، پیش ببریم  و عمل کنیم که در نهایت موجب رضایت ایشان گردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/449176" target="_blank">📅 16:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449175">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4c72f6a4.mp4?token=ailt0ln9uS6EEeyMXQqwHJNY6ptUL6stS3q8RxcV-MgrSjSWzk9nDOIudgmb9pN9DdHHzRFxalqwuLbdZHurRx8ggpXKtOQDg_yBY2CRtKirQ3ipEdatdJ5azPhXlsllO9o-LdPMpaCIWmeWIZyK6ZBeiaN6C-YqMmoj1yRP4nfH5LjZpajtM3L0uh6ht5jaK9DiVSSgKkVcfhD-OB0ty-QIZOym44ZRYVAUWcX6P0OOaEzRmA0eY1UTBnDVkZ5b0_mNL-tr49YPOrJfUquM8QWgPXo265ftTcLiVuW7WcRAp7C20U6ZTfqki6N9Cp_y5S5ZKXXVZY1sFNKacRQVzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4c72f6a4.mp4?token=ailt0ln9uS6EEeyMXQqwHJNY6ptUL6stS3q8RxcV-MgrSjSWzk9nDOIudgmb9pN9DdHHzRFxalqwuLbdZHurRx8ggpXKtOQDg_yBY2CRtKirQ3ipEdatdJ5azPhXlsllO9o-LdPMpaCIWmeWIZyK6ZBeiaN6C-YqMmoj1yRP4nfH5LjZpajtM3L0uh6ht5jaK9DiVSSgKkVcfhD-OB0ty-QIZOym44ZRYVAUWcX6P0OOaEzRmA0eY1UTBnDVkZ5b0_mNL-tr49YPOrJfUquM8QWgPXo265ftTcLiVuW7WcRAp7C20U6ZTfqki6N9Cp_y5S5ZKXXVZY1sFNKacRQVzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی خاص از مزار رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/449175" target="_blank">📅 16:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449174">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca96947bd.mp4?token=GcU3nMpnay0VyISCjRqamnMDfsW6El5cWGNBzq_WcVQPPCAAekil1t3VEaj0-w2gDAYhZ2CsqjsSyGc1xR56QTVA4h0LkQhRDsEje1Izf_QRzLLsqN_pYAbczGS1EBtai8I0rC71AhQF95lVrxPYUjGI5Qykn7fxMCwR--kVoES3lBiMcsBf2xQmiuD7YQxkDF9Q05_eoY8uUCcKfZa_elquvue7Jyws9r9NX9y_JwIlgCmXUQSyVzIzUmkWZpSnIg3vvcOwI-Xvf--qXeJWXyCwGJ52PtAawxQMEbMPf3T2VUzdSbaWaz3kyGK_qvU2qAG0vLqFMx6yhd0sr9dUiYGAb1Hehmi68jHHiJouva0_z0K3QSBIJOBvbkREFaVKebN4id7q9jAqDQpegmP2hgv5NjxmP9d9nW1yY_ySi8ou9Iygciox3Vz2thLGgZdKven599VotMOaHNDDXytLXbb05POx4TEwiPszemee0SbJ_23fkQOymh7yS-6gH91joUMGTSSXXwlqecHSnfohWGQ-kCwUHDxJGnH6K8KYLYL7mZre7d_qoKozUkAvO9JEwILtLqipwrKSd7itbDL7FBOJd6aSXjOP2U5shvJ5SvkKteylTs_K1DyirgQo3MtyW1rUXnmaosAQEMkyVU37ejOeo_gnf_CAZF4Btemjf-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca96947bd.mp4?token=GcU3nMpnay0VyISCjRqamnMDfsW6El5cWGNBzq_WcVQPPCAAekil1t3VEaj0-w2gDAYhZ2CsqjsSyGc1xR56QTVA4h0LkQhRDsEje1Izf_QRzLLsqN_pYAbczGS1EBtai8I0rC71AhQF95lVrxPYUjGI5Qykn7fxMCwR--kVoES3lBiMcsBf2xQmiuD7YQxkDF9Q05_eoY8uUCcKfZa_elquvue7Jyws9r9NX9y_JwIlgCmXUQSyVzIzUmkWZpSnIg3vvcOwI-Xvf--qXeJWXyCwGJ52PtAawxQMEbMPf3T2VUzdSbaWaz3kyGK_qvU2qAG0vLqFMx6yhd0sr9dUiYGAb1Hehmi68jHHiJouva0_z0K3QSBIJOBvbkREFaVKebN4id7q9jAqDQpegmP2hgv5NjxmP9d9nW1yY_ySi8ou9Iygciox3Vz2thLGgZdKven599VotMOaHNDDXytLXbb05POx4TEwiPszemee0SbJ_23fkQOymh7yS-6gH91joUMGTSSXXwlqecHSnfohWGQ-kCwUHDxJGnH6K8KYLYL7mZre7d_qoKozUkAvO9JEwILtLqipwrKSd7itbDL7FBOJd6aSXjOP2U5shvJ5SvkKteylTs_K1DyirgQo3MtyW1rUXnmaosAQEMkyVU37ejOeo_gnf_CAZF4Btemjf-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ مردم ایران به ادبیات توهین‌آمیز ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/449174" target="_blank">📅 16:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449173">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ffca2e91.mp4?token=qQnx7gTTNSMAAlf63-h2hHtQvRz2u2Udp0o-fBdBI8hsxqMQjBwv_BhRNm1og8vx78EWarL0559qn0zurUrYUVLTjzrzkb4Uih97mFczo8g48MMZY0rg5GUADuIES1Aonn1QU0jywIk_Q7GIxCDRFYPcR-Ki1hc_MdjnZD7qm62qT9G6qVbSJ5rumHfvMPdvq9-Dnxiadk4Xqlb0h9ZvF6aTB8MWRU8pFvfP-7Fru5Y8mL874tjr6czfrhtchw9GJEIgmO3aoVdAJjCn_DGmgi-5GSJXyv85IWXh8TBUAkpKdUiJudg1wCZON6vIP1mygRyE_XLIoUNF1-tWBQMXdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ffca2e91.mp4?token=qQnx7gTTNSMAAlf63-h2hHtQvRz2u2Udp0o-fBdBI8hsxqMQjBwv_BhRNm1og8vx78EWarL0559qn0zurUrYUVLTjzrzkb4Uih97mFczo8g48MMZY0rg5GUADuIES1Aonn1QU0jywIk_Q7GIxCDRFYPcR-Ki1hc_MdjnZD7qm62qT9G6qVbSJ5rumHfvMPdvq9-Dnxiadk4Xqlb0h9ZvF6aTB8MWRU8pFvfP-7Fru5Y8mL874tjr6czfrhtchw9GJEIgmO3aoVdAJjCn_DGmgi-5GSJXyv85IWXh8TBUAkpKdUiJudg1wCZON6vIP1mygRyE_XLIoUNF1-tWBQMXdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الجزیره از حملهٔ هوایی رژیم صهیونیستی به شهرک المنصوری در شهرستان صور در جنوب لبنان خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/449173" target="_blank">📅 16:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449166">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZ5yQ8jEiqU90P6y6OwjVveyTps_9hV74BEtlEUVcrn_u00c75hjXzd_dwDPKuh77aeRXxvChLdgpWkz7oEBtBeh_Nuiq2KBHlNhozU-q3euE8cWwaxY4J68QiVrmnBWRiBj4mPL8uE1BqgGWSq2F0RzD-CtTmibcl18fJHOqkHv7yJwT2die70FrLkakhrDEwz28t-pa47QRSs1lQgIFdYsDJK32lg41kTbsDsenW0SxOq8eZ-MctVHhEEiPVSxj6oi8TDVCsE3N21UBGMItI6CYXcmFZPBLfrxJRz_uwdNLHqWzpnCsGDJd2HMjgvEljB4QdBJXykq0nqogttadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYbnr2o4v0uIP-lVMxMw8prxKyOulVqkEWzCUnMQRd2ZmThhw3zS8eVfUVcDwIfogXLZv3GD-M7zMzpXDABaHEyTRrZ-KiM0glEbv54fayt8v83mTIFNBq82_xQxcI5n18ZG8TfLeSMiTk43Glk74TstwClPnARC7p3Cpfj4hJQTdSa6sThndyjmCpvzK09MspGMGzlPSwD9RHRiw7zwwiY9Y7p_oCQ9QX-NB-dTP0JMeJLZPPm6hoDT8wro3bIK4i-SbG3_4CO1QU5x1qFu1Fug7B24GFeKuItUsjHvS2JmB-AE_Gay3iVG-RBEGygB1H753wX-EJ9O62oMoqZDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmXDrV9t4EQSm7xXpz4HXITXht2Isq_6qTSHsNW-1SFd20uwDTV7pl5gusKagMHgYUBlys2OkfdDDHzZScdaP2gvQDA3iPX33xVjC6qa4y1FPSfuduyjkYZJpe6e2sM-njc7Ccsb5czcyCdmR-y2tfdXxgwlyNCN-JPtRNcCsLWVrlHOIP1N-vUNrqSuoUZIeupAUD-47-FZ1jhGh6er1re3S8R0Z2NWRsxVrt9UY2aRlaJ9DRhC1NGQESG9p4I7Nw2PxhFoo0UhKjd6cevkgaTxX5vE0qKWGD11w5kOgjS7d9s8xHA5Kop_8PfEo69XjYnAZIZo7A8VLqVHITEeZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUxR2CzeE3ty5YirmlTeeM1Cfk_5LWhzMEJ88FvQT4JgP0Hh4zvMxtntmWmcvRurQOLIT80qzLfLve1E4I3ly9ZXppNeLVkjA39vbW7tYKWg2Gp06ZN8vGAFoEzzPx4PytV9F7fY5akY-2fc7P2zbUn4NJ0zSY1I4uWCpX5IX4eLv0ZpiISICC67u4SmeXonk0iX0PEn2CyksfWj0SbAf-ijuw1AuTvFk2liMjbeFIHECN7PIBrtYdXhcJLz7Ld3gCHSP0ULTyMfml762CdON0EVkqmITo-5fryvfvPNzHfVoJJHkfMSFiAhiZpPDXMREkOfZAOk6f7V4QbC_2AEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hI2D5OQgjOsu9reLK8ouYaTj4l-7G8sFh-oGhJVTJ9qcyicXeu9UMY2ffZ7HY0cPmeFcYrDIoWCBpJC525DN6cGrvrE7xNlaGjIxRhILdATE2IqAllBhC5nsnNb0qcOXIesXQ-eB3MVzTUXNdMInoRECaycGrDdDN9M1HHGlh6-TwenfRwXkQY6iAwk-ckEgIdHIGWiZxcneGLpOtnN0yY9TMuP3Ijx41mNZyIJXy4wQ9ll0UWKVMcgPTguaS3MG-ZRKPPzAChPizkzGgMj4mLeELlW00tmlIlk4uP9f0Cb4AYnLCp65b7lwIUCk02OMd8LCIoCaUnTKaG8le6FHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqaGBQ4FHVhcqcgFPrUGdXOxKyVtaht6fGoVKtb_sSTQb6URp01hbu70L5Hxx_b2dNlVjFXi4sxOwAoQv3Yyc9StdkNZPMBH4yHOGSn0z6ofr6Qq0grD5zIneRa979sQrtRon31-qcfq8ug6dRdGdIm70qUCIYuhomfidR9S2CCKIrbrc5KcL_MLeBwc122nj_vSIk4jPrfZogHHe74HwqpCotJpXZWTw3vHSShGF1Gv05OQg1QIiekcuJT3Tfi-QZUZC6KbAQy5g8Ad_AiVZl552WINKE7WqPwLVu8HuNggs2WIax8HuxpoN_5VnIF8nX0ikAWHxEqRkOOXE6RwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNx2bHgZDfNLbKUkztp0bPX720j1qt7EoDLBIbI9KICDnJqNqvy8EguO4bkdeWPFr6ApAmVlWw4hxxvvJoyy7qJ3_L0pRVlGYU04PcJrnu1WRzVviRYjPoJpLPDo_c72N3H4jQoKiWg2Q4CiBMjeJcUNGq9ysi3v7yYcQlz8mmZS4wCOP27x6zMr8Z1TgR5rYCtChPsTTyGblACZ43vylNaG-yVF3VvulLIgCrj65SgWuqlIBw8EXaeOJ0_9EiZl2luvz5HRquyrJxGAe9v7m51_d7UkP6uKa03jV4ASAtCH_q-hL5yNB4rlTb8lr3IfuqeMhOnNyGEiEJlpi53hzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت قائد شهید حضرت امام خامنه‌ای در مصلای تبریز
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/449166" target="_blank">📅 16:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449165">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ceeacc63d.mp4?token=f2UdxAx9sSYNSJMfugSQIO3di_cPE6pAwQbaCrmCbM9uOgbkEu6XUNlqh2DEIj3Ba5HFiMlZWg8ieQPtTfRWs6TrXYYFAHGA3GYs9Ic4q7IvOYZMj0Xc2WUVNXMfjtF-EEpEOuhK62MyY0xmYQ27I9SydNyMUGHd308o_Byz-iccKflyi2Br2SzrbIJYIcU_zI422P8c5vh49B805gCIK2duzCv-Y6afvC_pjUWWUxD1rVWU9LrNfUYkiRvQtRSKzlhYv_xmqb3ELHgDYB20YtP63_5s1Adndkuckz5xBnXoSwRMHO6eBGt8T844fA6zMR_dTNHZHn3Ah88hAKTMmE6cKHiSWC7SGsSDsEIquGvQ-TbglAo3erIWyEkBr6j_NpxSSa040NmrYm_hVZHTv1DuE_P-u9NjIaFmqFGa-Ram1vy2McMKX-ad1xB3qD4o0jFF2qrcmpOR-DYH9wIGazgMAg8jJdf_c-kx14546nL0utFGpn7qXGNI59vnRjtVwpHw7_b3bGLa_m02ol6_MGL3kAhEGJSTaNxDNDPxZves3cyLGI7lRr1txyBIRmDUDMeortcn2Qfepv2HP7mlrmp1pcFg7Vk_K3FLZzD5VJYnAEoF0A36zbHh5IlhRAy1Zm1aTAJCIs_mFXQpfsvh1Zkv4gFKwkFJ9Tkv3z3F_PI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ceeacc63d.mp4?token=f2UdxAx9sSYNSJMfugSQIO3di_cPE6pAwQbaCrmCbM9uOgbkEu6XUNlqh2DEIj3Ba5HFiMlZWg8ieQPtTfRWs6TrXYYFAHGA3GYs9Ic4q7IvOYZMj0Xc2WUVNXMfjtF-EEpEOuhK62MyY0xmYQ27I9SydNyMUGHd308o_Byz-iccKflyi2Br2SzrbIJYIcU_zI422P8c5vh49B805gCIK2duzCv-Y6afvC_pjUWWUxD1rVWU9LrNfUYkiRvQtRSKzlhYv_xmqb3ELHgDYB20YtP63_5s1Adndkuckz5xBnXoSwRMHO6eBGt8T844fA6zMR_dTNHZHn3Ah88hAKTMmE6cKHiSWC7SGsSDsEIquGvQ-TbglAo3erIWyEkBr6j_NpxSSa040NmrYm_hVZHTv1DuE_P-u9NjIaFmqFGa-Ram1vy2McMKX-ad1xB3qD4o0jFF2qrcmpOR-DYH9wIGazgMAg8jJdf_c-kx14546nL0utFGpn7qXGNI59vnRjtVwpHw7_b3bGLa_m02ol6_MGL3kAhEGJSTaNxDNDPxZves3cyLGI7lRr1txyBIRmDUDMeortcn2Qfepv2HP7mlrmp1pcFg7Vk_K3FLZzD5VJYnAEoF0A36zbHh5IlhRAy1Zm1aTAJCIs_mFXQpfsvh1Zkv4gFKwkFJ9Tkv3z3F_PI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرداری که ۲ بار شهادت را تجربه کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/449165" target="_blank">📅 16:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449164">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxuGtCizOqAGBv475R_8F8S1FgJxL1_4S8tapY0PK0qBBHnFC3qTSIyM_HQ5mvNi7aevdgOc2Ao4C68sYxd2hdzevMcU5Demhbj530xWzug2FOOTR2Y8n_FQAuV_BcBy33RWTMT0mMcGaM99LFYRhLesLndGrPu2_yO7W8Ug1Eu72JZ06tQsl4rmZngDw-JB-jI8J5eDM8GKDqSd3XaGRITrNfdM71QAy_M2u43KeLUBMEjiI75UMdpnMA71yOSLvQtdi8RHZLMT0prYLC0wZv6fPdoc0OFYENXN6UCCbtkXmaJFIWKGIYQ4esEVix4lLHI1M8BRKw6epG3NWkIRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌ثبت‌نام حج ۱۴۰۶ زودتر از همیشه آغاز می‌شود
🔹
معاون سازمان حج و زیارت اعلام کرد پیش‌ثبت‌نام حج تمتع ۱۴۰۶ از یکشنبه ۲۱ تیر آغاز می‌شود.
🔹
در مرحله نخست، فقط افرادی که در کاروان‌های حج ۱۴۰۵ ثبت‌نام کرده‌اند اما موفق به اعزام نشده‌اند، امکان ثبت درخواست دارند…</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/449164" target="_blank">📅 15:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449163">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd03739e4b.mp4?token=eBXznTEpFaMwwrewNJZTNYQYgT8KKdB9_fuzf8pRL-pE9-STSrVAgALZRPxV5FU4DHRIwgm2sNOv4BGIswPGSgXHPSVBpuoc1aiJDRHAxQKVurX1BcGW-_699IsIEnmwcd3CHVgd9psEAAMzW9BHdxOHBbNcamFYEBRWaWeK82AaJsH2vK0iQxplchupnojQXtmj11VrFTy2AyeqSdQhnChah6I00-8z3c5IhO9G3dZGrLmE254j9BNGZILJQnr0kXMGpBVxpMVcl3Qp2h-hHW3iCMVokt3WZ4ZCMIGJPTbYpEJe7Jl-8QmVcndZmGaK-9Ps8gXh4ZQ5YeEPVZ12xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd03739e4b.mp4?token=eBXznTEpFaMwwrewNJZTNYQYgT8KKdB9_fuzf8pRL-pE9-STSrVAgALZRPxV5FU4DHRIwgm2sNOv4BGIswPGSgXHPSVBpuoc1aiJDRHAxQKVurX1BcGW-_699IsIEnmwcd3CHVgd9psEAAMzW9BHdxOHBbNcamFYEBRWaWeK82AaJsH2vK0iQxplchupnojQXtmj11VrFTy2AyeqSdQhnChah6I00-8z3c5IhO9G3dZGrLmE254j9BNGZILJQnr0kXMGpBVxpMVcl3Qp2h-hHW3iCMVokt3WZ4ZCMIGJPTbYpEJe7Jl-8QmVcndZmGaK-9Ps8gXh4ZQ5YeEPVZ12xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع لبنانی از ۲ حملهٔ پهپادی ارتش صهیونیستی به جنوب لبنان خبر دادند  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/449163" target="_blank">📅 15:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449162">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQfnrdTz4Y-hEig5Y9xgjGV89y90gAjrUXzTkIvsVb32h-lWKNavYXj9VvaFh-w7BQCSo-pJfXaz2u3eMyk_uRGPUv8SSbHH6N0JogQKslYUrvcbq3gwMx-057LedwKgiMGymGBgg76H1xDeVSMW36NfizfbAYGX7FEuoQEHaca_MA7gX8-c-Jd8DJWyDSyTuzC8xDB-_61VEngV1ugozjC3GDx311403ZcH98Tt2Zbcpf30StAaN8XR3A0tllMNulv4iIgDDtpK8dbOV65AvPT7BKNqOue7iKs6hKnw2ZdDO03B8bgL4OLqhR9guiVaGDHB5YsCg-PeeXsOEdCOMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و شرط دریافت ارز اربعین اعلام شد
🔹
به‌گفتهٔ دبیر ستاد اربعین، توزیع ارز اربعین از امروز آغاز شده است و فقط زائرانی که در
سامانهٔ سماح
ثبت‌نام کنند می‌توانند تا ۲۰۰ هزار دینار عراق دریافت کنند؛ نرخ دولتی هر ۱۰۰۰ دینار برای زائران ۱۲۰ هزار تومان تعیین شده است.
🔹
متقاضیان می‌توانند با ثبت درخواست، ارز خود را از بانک‌های ملی، ملت، سپه، شهر، گردشگری، قرض‌الحسنه مهر ایران و پست‌بانک دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449162" target="_blank">📅 14:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449161">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiZrGYVAAld6iIZrKDZkMfKaRdpd8DIKb6GOAgpxiKdq11nMxMJA0lj93Qc30ClDlyNNh8wOabK2UC_0hj9ccLndSn8T9-ckd1tKUDnfjeJNvHgh218DCukziZmyukcUIyaulBJhdkgBHF_7n1cLrdyQOXWlOh_w9Nm6UNbLECxk0wgAUWTz8ug3kMCMC03jUdWp7t1NCjIdDYAz6MVfMsHLcI4Y9BkjYkGTDdDIQ33zRTs-v7kuuMMrA5C4nRVJ1yEK60X011asZZqzkH8dwnE1fqgBv9PXTHU4v5sGHxFxt-I7Tx8YiXmJpgsKAjE_rvzJzm0P3IC0Di5d2Wf7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌اندازی پایگاه اطلاع‌رسانی رهبر معظم انقلاب
🔹
پایگاه اطلاع‌رسانی رهبر معظم انقلاب، حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای راه‌اندازی شد.
🔹
مردم می‌توانند با مراجعه به نشانی
Rahbar.ir
به تازه‌ترین اخبار، اطلاعیه‌ها، پیام‌ها، بیانات، دیدارها، تصاویر، ویدئوها و سایر محتوای مرتبط با رهبر معظم انقلاب اسلامی دسترسی داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449161" target="_blank">📅 14:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449160">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b36056a2b.mp4?token=PRogxiXjvf9iepWV_iJSk0fmZmL4vDRclEFhDL3Fm0rFETyG-2Sroiw5DjBr0eaDuOvt0rDXdC1jdCYvr1jRfEcGIRaRbwMDq-a7yfdgbt90f58uedYfqTEzwpa1NTwh7BN2DNAVlrYEArbPZ7bX8TrnqHE9D3njCixSdSDhPsrCR5LeyB5rvPBL-pbdxKgBzu255Nmel28YC7FBGWqtwM-J4l5hF_pQ0WDCNv242ys0gPhYboyLsQIj-XUkno2rsOjxwHA2fYMNtRSNGD8Nn5R8WcsS_tT6t_OTMf1pU6jdl4Tay5V0A3qhB5YKwNVf5zxx661wOroUoxUaAlohdEmsLbOSdOQzsOIypxN4NYUvpg_x9Xdh-D1gNRh8TGd8Itw8DH49-iRbMPVjkM8LPHvvzeRaiX1_jugyqWb70NRY3QBb5FhGYOe0kpnOEcmOeQHUeSwVQDg6mGwGZOcwhhNksV9SP25F9S9C-o_R-1CozRQM3Q46EpXPn6wttUyC53NGZfKgwbOZadn72MKp008dX40pLuhSvxgtUdR4a3PVxd_yVFP5maGR3vFV77tIejISx5hYEfSrm7ZLIXSfm-QZgRhkefjAalAYgo92MhaeiYBk6b24nu2p5OhWPoFrbN9JvTeyi2i_-bz5O-tj_aQRQC79Uvay1WkqxsQ8s4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b36056a2b.mp4?token=PRogxiXjvf9iepWV_iJSk0fmZmL4vDRclEFhDL3Fm0rFETyG-2Sroiw5DjBr0eaDuOvt0rDXdC1jdCYvr1jRfEcGIRaRbwMDq-a7yfdgbt90f58uedYfqTEzwpa1NTwh7BN2DNAVlrYEArbPZ7bX8TrnqHE9D3njCixSdSDhPsrCR5LeyB5rvPBL-pbdxKgBzu255Nmel28YC7FBGWqtwM-J4l5hF_pQ0WDCNv242ys0gPhYboyLsQIj-XUkno2rsOjxwHA2fYMNtRSNGD8Nn5R8WcsS_tT6t_OTMf1pU6jdl4Tay5V0A3qhB5YKwNVf5zxx661wOroUoxUaAlohdEmsLbOSdOQzsOIypxN4NYUvpg_x9Xdh-D1gNRh8TGd8Itw8DH49-iRbMPVjkM8LPHvvzeRaiX1_jugyqWb70NRY3QBb5FhGYOe0kpnOEcmOeQHUeSwVQDg6mGwGZOcwhhNksV9SP25F9S9C-o_R-1CozRQM3Q46EpXPn6wttUyC53NGZfKgwbOZadn72MKp008dX40pLuhSvxgtUdR4a3PVxd_yVFP5maGR3vFV77tIejISx5hYEfSrm7ZLIXSfm-QZgRhkefjAalAYgo92MhaeiYBk6b24nu2p5OhWPoFrbN9JvTeyi2i_-bz5O-tj_aQRQC79Uvay1WkqxsQ8s4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف طولانی زائران حرم رضوی برای حضور بر سر مزار رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/449160" target="_blank">📅 14:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449159">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌ رهبر انقلاب: امید داریم آقای شهیدمان حضرت بقیة‌الله را همراهی کند
🔹
شما ای سرور عالی‌مقام! ای بزرگو‌ار! ای امام رئوف! یا اباالحسن الرّضا المرتضی که برترین صلوات خدا بر شما باد، اکنون جسم پاره‌پارهٔ خادمی از خادمین حضرتتان و عترت طاهره، پس‌از سال‌ها جِدّ…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/449159" target="_blank">📅 14:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449158">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌ رهبر انقلاب: عهد می‌بندیم از جنایتکاران انتقام بگیریم
🔹
ای قتیل مظلوم! ای مظلوم سرافراز! ای بندهٔ صالح خدا! حال که با چشمان اشکبار و دل‌های شکسته با پیکر شما وداع می‌کنیم، با شما عهد می‌بندیم که مکتب شما را پاس بداریم و آن طریق مستقیمی که شما ترسیم کردید…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/449158" target="_blank">📅 14:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449157">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌ رهبر انقلاب: ای پدر شهید امت! نوشیدن شهد شهادت که عمری در آرزوی آن بودید، گوارایتان باد!
🔹
پوشیدن خلعت شهادت با بدنی که نشان‌ها از مادرتان زهرای اطهر و جدتان اباعبدالله الحسین و ابالفضل العباس علیهم‌الصلاة والسلام دارد، مبارکتان باشد.
🔹
و شما ای همراهان…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449157" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449156">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌ رهبر انقلاب: آقای شهید ایران، حسینی بود، حسینی زیست و حسینی شهید شد
🔹
السَّلامُ‌ علیکَ یا ثاراللهِ وَ‌ ابنَ ثاره وَ الوِترَ المَوتور. السَّلامُ‌ علیکَ وَ علی جَدِّکَ وَ اَبیکَ وَ اُمِّکَ وَ اَخیکَ وَ المَعصومینَ مِن وُلدِک.
🔹
سلام بر امامی که ندای حیات‌بخش…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/449156" target="_blank">📅 14:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449155">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌ رهبر انقلاب: آقای شهید ایران، حسینی بود، حسینی زیست و حسینی شهید شد
🔹
السَّلامُ‌ علیکَ یا ثاراللهِ وَ‌ ابنَ ثاره وَ الوِترَ المَوتور. السَّلامُ‌ علیکَ وَ علی جَدِّکَ وَ اَبیکَ وَ اُمِّکَ وَ اَخیکَ وَ المَعصومینَ مِن وُلدِک.
🔹
سلام بر امامی که ندای حیات‌بخش…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/449155" target="_blank">📅 14:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449153">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">14050418_پیام_رهبر_معظم_انقلاب_اسلامی_به‌مناسبت_تشییع_و_تدفین_آقای.pdf</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/449153" target="_blank">📅 14:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449152">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">14050418_پیام_رهبر_معظم_انقلاب_اسلامی_به‌مناسبت_تشییع_و_تدفین_آقای.pdf</div>
  <div class="tg-doc-extra">150.4 KB</div>
</div>
<a href="https://t.me/farsna/449152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‌ رهبر انقلاب: انتقام خواست ملّت ماست و به‌طور حتمی باید صورت بگیرد
🔹
به پیشوای شهیدمان عرض میکنم: ای قتیل مظلوم! ای مظلوم سرافراز! ای بنده‌ی صالح خدا! حال که با چشمان اشکبار و دلهای شکسته با پیکر شما وداع میکنیم، با شما عهد می‌بندیم که مکتب شما را پاس بداریم…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/449152" target="_blank">📅 14:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449151">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تشکر رهبر انقلاب از حضور تاریخی ده‌ها میلیونی در ایران و عراق
🔹
جا دارد به همین مناسبت از حضور ده‌ها میلیونی، اعجاب‌برانگیز، دشمن‌شکن و تاریخی مردم در شهرها و روستاهای ایران و عراق خصوصاً تهران، قم، نجف، کربلا، و مشهد صمیمانه قدردانی میکنم. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/449151" target="_blank">📅 14:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449150">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhVtJ5NqdonIvZF2P8vYCRdhcDU__62967bk9hI2xj1wwuXoOqfFhJ9vyFNiEIMD2k252zikDqVdx8R0O9qx9zUnQPG00cM8B7iFkd5ddPk5hEfDR_p_y0Ml_xKzKiN7usPzTJs0NkqZnX8LL6-Vmnq_MSse3by-H-ouCmI1fU1Zqkb9CV2u0nP67vwxfTUXRA82G-NhsAPkJVY3t01FbcpK72I-cmG2DL_em3N9Xzpx7cEF3_2enye1dLfz6y0e4MaCQbk2A-_kzn5ltbYaae3Rk7vzPLAmloUAWYd949ilSveGXYF2ZuWxStFe5IxOEobn7CDntySkEEryO1KbQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انقلاب: عهد می‌بندیم که انتقام خون پاک رهبر شهید و همۀ شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/449150" target="_blank">📅 14:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449149">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
تا ساعتی دیگر پیام مهم حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر انقلاب اسلامی به‌مناسبت تشییع و تدفین آقای شهید ایران منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/449149" target="_blank">📅 14:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449148">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎥
هواشناسی: طی چند روز آینده نواحی جنوبی کشور دمای بالای ۵۰ درجه و تهران دمای بالای ۴۰ درجه خواهند داشت
🔹
شاخص اشعهٔ فرابنفش نیز افزایش خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/449148" target="_blank">📅 13:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449147">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a458db9dec.mp4?token=aN4doTRf11yCFonzok8GgcN41Juc0rwO_dAaaMC-R-TeQyE43_55yBV9m2LsbNDHPXctpd6qHZTRsurO6PO27mXaZpkN0iC3FZQgDaD60usiQy9kpT1tzApI5X5-H558ksCwqHx4qHN7XMQCFu9gdWhZ4gfcBxeJ9RQb-dWo7q5TfdBREKIDcgwWI5V6HTOQnRp8vqsflurGKis1eywM2T8HsE32xsEHzkcabq657xTol0Rrrw97AT0Ei-QMhgmw1Qjjo6Mj-mrpyA92gHrbVNHR-zzGRaUDuqIu1upkPuB4iPTP7ITghPJH_8OH2S6fLuwab2xv58S4NdHSyWBcT4HQzDAP1yL_ByjMGf3QR4yfLalFsVZ_3TOIxL4zCng3pPJyCRA3EvqFKlhWn6npBPlQyYRXchVh92FsDVRTafPCO738ClbMH514pLKd9GkOvTW3p5_evGFOlgwfvFXryEJAQT7KcTMb1qSTTRAInnw0oOsMUdrDUF8OrvUnLHNNAQbFnRwMlAu7CVIWblsZHvKJ0_IXX27X--snjWODN0A0FwXVaNsXV49vTTM1gk5TM_u_Gkvlo6wPPOrzjwgWZmKG_lsblZFOZvWakV3ZL3jNOfNc-2HzjnYGrx8k1EYiz1PIvtg8-ODMKiqlydRPF0-Vp15AxTuqFgpItES2s_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a458db9dec.mp4?token=aN4doTRf11yCFonzok8GgcN41Juc0rwO_dAaaMC-R-TeQyE43_55yBV9m2LsbNDHPXctpd6qHZTRsurO6PO27mXaZpkN0iC3FZQgDaD60usiQy9kpT1tzApI5X5-H558ksCwqHx4qHN7XMQCFu9gdWhZ4gfcBxeJ9RQb-dWo7q5TfdBREKIDcgwWI5V6HTOQnRp8vqsflurGKis1eywM2T8HsE32xsEHzkcabq657xTol0Rrrw97AT0Ei-QMhgmw1Qjjo6Mj-mrpyA92gHrbVNHR-zzGRaUDuqIu1upkPuB4iPTP7ITghPJH_8OH2S6fLuwab2xv58S4NdHSyWBcT4HQzDAP1yL_ByjMGf3QR4yfLalFsVZ_3TOIxL4zCng3pPJyCRA3EvqFKlhWn6npBPlQyYRXchVh92FsDVRTafPCO738ClbMH514pLKd9GkOvTW3p5_evGFOlgwfvFXryEJAQT7KcTMb1qSTTRAInnw0oOsMUdrDUF8OrvUnLHNNAQbFnRwMlAu7CVIWblsZHvKJ0_IXX27X--snjWODN0A0FwXVaNsXV49vTTM1gk5TM_u_Gkvlo6wPPOrzjwgWZmKG_lsblZFOZvWakV3ZL3jNOfNc-2HzjnYGrx8k1EYiz1PIvtg8-ODMKiqlydRPF0-Vp15AxTuqFgpItES2s_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
صف طولانی زائران حرم رضوی برای حضور بر مزار مطهر «آقای شهید ایران» در رواق دارالذکر  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/449147" target="_blank">📅 13:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449146">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e0ce0d1c.mp4?token=drbQ6BuCv7Aj4L7JUMp_bLSLGhsnzNOZLJO3fQKt5LCur2F5a417vYyvKVUTuDEhhdBMbPQMX2KQ3P9DSp8I5qlXNUdGkQQcoQpXM9JOUE4Z6cId6buUx3KjIpHo_hFNg6lWuSMP9D1UsTxGR3SKgEuOT-if-cXm3d7fltivoW_jOo0AssGVnroBkoeuGPgJSJtylHqaik7SDqTNaUBAdwRQHWrj3rXlKj0ebTNfJoab5G3GCf9MH96a0-w8lC-3ulFmSGeFi8onbxjcxP8AO2n25MC9zrmSvMYCR9f2ckPMamcTFD0wYY6OMmFwcxPSPY2ZPPcZ9PNXxykZTBTyJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e0ce0d1c.mp4?token=drbQ6BuCv7Aj4L7JUMp_bLSLGhsnzNOZLJO3fQKt5LCur2F5a417vYyvKVUTuDEhhdBMbPQMX2KQ3P9DSp8I5qlXNUdGkQQcoQpXM9JOUE4Z6cId6buUx3KjIpHo_hFNg6lWuSMP9D1UsTxGR3SKgEuOT-if-cXm3d7fltivoW_jOo0AssGVnroBkoeuGPgJSJtylHqaik7SDqTNaUBAdwRQHWrj3rXlKj0ebTNfJoab5G3GCf9MH96a0-w8lC-3ulFmSGeFi8onbxjcxP8AO2n25MC9zrmSvMYCR9f2ckPMamcTFD0wYY6OMmFwcxPSPY2ZPPcZ9PNXxykZTBTyJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع لبنانی از ۲ حملهٔ پهپادی ارتش صهیونیستی به جنوب لبنان خبر دادند
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449146" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449145">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جلسهٔ علنی مجلس فردا یا پس‌فردا برگزار می‌‎شود
🔹
به‌گفتۀ یکی از اعضای هیئت‌رئیسۀ مجلس، در هیئت‌رئیسه تصمیم گرفته شده که جلسۀ علنی مجلس به‌صورت حضوری، یکشنبه یا دوشنبه برگزار شود.
🔹
به‌گفتۀ او، تصمیم نهایی تا ساعات آینده گرفته می‌شود و به‌صورت رسمی اطلاع‌رسانی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/449145" target="_blank">📅 13:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449144">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">منبع آگاه: مذاکره تا عقب‌نشینی آمریکا از مواضعش منتفی است
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی در گفت‌وگو با فارس: گزارش‌های منتشرشده در برخی رسانه‌های نزدیک به رژیم صهیونیستی درباره درخواست ایران برای مذاکره با آمریکا کذب است.
🔹
جمهوری اسلامی ایران هیچ درخواستی برای مذاکره با آمریکا ارائه نکرده و هیچ مذاکره‌ای نیز تا زمانی که طرف آمریکایی از مواضع خود عقب‌نشینی نکند، انجام نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449144" target="_blank">📅 13:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449143">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaKrwgyI0aWTi50T2PLS6OSETi5L-gpG08nGlO97fpl9A3HDvpP1TQibKR_QDqvE5dQoDUKaFPmwrJVBkES1qbMJ6ebgwpf8vqYUf4GjlD9T6dJmVDxTVMuwZftslryQQaFY_wRgrD6L2gTDRF8FqXuNTxbki4cklNpSM6s6oifIX8N_o6xn8E5XW1rbM-8_71_m1j7i0AzbffrVD9hQvX1AqhVx1dfVAlfvrP0pZ-XIslQGnEXQ4xdxQCBCLz19MfbXLgT0wd4U7bti49P6dvu2t0kQbzrQx6yQ7nKuFVtkLE4g_lFw99xSqfDJiyh9TjCxD1ZttXA3vjPpBx1NMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف در مسیر لاریجانی؛ لانچر جنگ شناختی دست کیست؟
🔹
این روزها مردم ایران حق دارند خشمگین باشند. جنایت‌های آمریکا و رژیم صهیونیستی، شهادت رهبر، فرماندهان، دانشمندان و هم‌وطنان عزیزمان و اظهارات گستاخانه ترامپ، احساسات جامعه را جریحه‌دار کرده است. از سوی دیگر، بسیاری نیز گلایه دارند که چرا مسئولان به اندازۀ کافی به جنگ رسانه‌ای دشمن پاسخ نمی‌دهند و روشنگری لازم را انجام نمی‌دهند.
🔹
این مطالبه، مطالبه‌ای طبیعی است؛ اما نباید یک نکته مهم را فراموش کنیم. در میدان جنگ، همه یک مأموریت ندارند. فرمانده، نیروی اطلاعات، دیپلمات، رزمنده و دیده‌بان هر کدام وظیفه‌ای متفاوت دارند. اگر هرکس از روی احساس، مأموریت دیگری را بر عهده بگیرد، آرایش جبهه به هم می‌ریزد.
🔹
دستگاه دیپلماسی و نهادهای امنیتی گاهی به دلیل ملاحظات عملیاتی، نمی‌توانند همه واقعیت‌ها را بیان کنند؛ چراکه دشمن نیز رسانه‌ها را لحظه‌به‌لحظه رصد می‌کند. حتی ممکن است در برخی موارد، ضعف رسانه‌ای، تأخیر در اطلاع‌رسانی یا بی‌توجهی مدیریتی نیز وجود داشته باشد. مسئولان معصوم نیستند و خطا در هر مجموعه‌ای ممکن است رخ دهد.
🔹
اما حتی اگر چنین ضعفی وجود داشته باشد، راه اصلاح آن، توهین، تخریب و برهم زدن آرامش جبهه خودی نیست. این ضعف را می‌توان و باید نقد کرد، اما نقد با اهانت و هیجان‌زدگی تفاوت دارد.
دقیقاً همین نقطه، میدان جنگ شناختی است.
🔹
دشمن تلاش می‌کند خشم مردم را از خود منحرف کند و آن را متوجه مسئولان و نیروهای داخلی سازد. اگر بتواند میان مردم و مسئولانی که در خط مقدم دفاع از کشور قرار دارند شکاف ایجاد کند، بدون شلیک حتی یک گلوله به بخشی از هدف خود رسیده است.
🔹
امام راحل و رهبر شهید بارها بر صبر، بصیرت و حفظ وحدت تأکید کرده‌اند. تجربۀ برخورد با علی لاریجانی نیز نشان داد که گاهی فضای هیجانی، قضاوت‌های نادرستی را رقم می‌زند و بعدها بسیاری از همان منتقدان از رفتار خود پشیمان می‌شوند.
🔹
امروز نیز افرادی مانند محمدباقر قالیباف و سیدعباس عراقچی، فارغ از اختلاف‌نظرهای سیاسی، در صف نخست دفاع از منافع ملی قرار دارند و در صورت هرگونه اقدام تروریستی یا جنگ، جزو نخستین اهداف دشمن خواهند بود. ممکن است درباره روش‌ها نقد داشته باشیم، اما نباید جای رزمنده و دشمن را اشتباه بگیریم.
🔹
امروز مأموریت همۀ ما، شلیک موشک نیست؛ اما حفظ انسجام جبهه خودی، مقابله با شایعات، کنترل خشم و جلوگیری از دوقطبی‌سازی، بخشی از همین نبرد است.
🔹
در جنگ، رزمندۀ پشت لانچر اجازه ندارد از روی عصبانیت و بدون اطلاعات شلیک کند؛ چون ممکن است نیروهای خودی را هدف بگیرد. در جنگ شناختی نیز زبان، قلم و صفحه تلفن همراه ما همان لانچر است. هر جمله‌ای که از روی خشم و بدون دقت منتشر شود، اگر جبهه خودی را تضعیف کند، خواسته یا ناخواسته در زمین دشمن بازی کرده است.
🔹
خشم مردم سرمایه‌ای ارزشمند است؛ اما این سرمایه باید دقیقاً به سمت دشمن اصلی نشانه برود، نه به سوی کسانی که با همه ضعف‌ها و اختلاف‌نظرها، در خط مقدم دفاع از ایران ایستاده‌اند. از همین رو، اگر نقدی هم داریم، باید مسئولانه، منصفانه و در جهت اصلاح باشد، نه به گونه‌ای که آرایش جبهه خودی را بر هم بزند و دشمن را به هدفش نزدیک‌تر کند.
🔹
در پایان، نباید «دیپلماسی در میدان نبرد» و «اعتماد به دشمن» را با هم خلط کرد. مسئولان کشور بارها تأکید کرده‌اند که اگر مذاکره‌ای هم صورت گیرد، آن را بخشی از مدیریت میدان و «مذاکره در شرایط جنگ» می‌دانند، نه مذاکره‌ای از جنس اعتماد، سازش یا رابطه برد ـ برد با دشمن.
🔹
متأسفانه برخی اظهارنظرهای نسنجیده از سوی بعضی جریان‌های سیاسی که عقب‌نشینی و امتیازدهی را راه‌حل نهایی مشکلات معرفی می‌کنند، این دو مفهوم را در ذهن افکار عمومی درهم آمیخته و زمینه سوءبرداشت را فراهم کرده است.
🔹
درحالی که هم آموزه‌های قرآن کریم و هم تجربه تاریخی ملت ایران به ما می‌آموزد که به دشمن نباید اعتماد کرد و گره‌های اساسی کشور با تکیه بر اراده و توان داخلی گشوده می‌شود، نه با امید بستن به وعده‌های دشمن.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/449143" target="_blank">📅 13:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449142">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تحلیل داده‌محور از اجرای تفاهم ایران و آمریکا؛ یک گروه دانشگاهی «تفاهم‌سنج» را راه‌اندازی کرد
🔹
گروهی از پژوهشگران و متخصصان دانشگاهی، سامانهٔ «تفاهم‌سنج» را با هدف ارائهٔ تصویری شفاف و مستند از روند اجرای تفاهم ایران و آمریکا راه‌اندازی کرده‌اند.
🔹
به‌گزارش فارس، در شرایطی که روایت‌های متفاوت و گاه متضادی دربارهٔ میزان پایبندی طرفین به توافقات موجود مطرح می‌شود، این گروه دانشگاهی با اتکا به روش‌های آماری و داده‌های مستند، امکان سنجش عینی‌تر اجرای تفاهم را فراهم آورده است.
🔹
در این سامانه، هر خبر یا رویداد مرتبط با اجرای تفاهم، ابتدا به‌عنوان یک «شاهد» ثبت شده و براساس ۳ معیار اعتبار منبع، کیفیت مستندات و میزان ارتباط با ۱۴ بند تفاهم ارزیابی می‌شود؛ سپس با استفاده از یک مدل آماری مبتنی‌بر تجمیع شواهد، میزان تأیید یا نقض هر تعهد محاسبه شده و برای هر بند و برای کل تفاهم، شاخصی بین صفر تا ۱۰۰ به‌صورت مستمر به‌روزرسانی می‌شود.
🔹
پژوهشگران این پروژه تأکید کرده‌اند که هدف از طراحی «تفاهم‌سنج»، فراهم‌آوردن بستری برای قضاوت مبتنی‌بر داده به‌جای روایت‌های غیرمستند است. این سامانه که کار خود را به‌صورت آزمایشی آغاز کرده، در دسترس عموم قرار گرفته و مخاطبان می‌توانند با مراجعه به نشانی
Tafahomsanj.com
از آخرین وضعیت شاخص اجرای تفاهم مطلع شوند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449142" target="_blank">📅 13:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449141">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2NiktXL7a1j4SLB9Oz5Tf0R_wr7B77xDbAqScZDQlNL2mFWdQBGla3DwqBUKPX9oAu2H5X4eIEnwXku-6ok7Vr-P5E8RXUGtAx5ikF33BMmKo0dY3uJGZaFIew_ZGIBVAsfjrNsQIOk2FlekSxIyWXz7bkQXq_erwvcRBz9lDaSkrYZzY18i6BO7EbWqsq1SupwtJhvztJuyIGFbkQw8sVr-WZ8cZgOZKZsMYtMBZdA7oclHwoJdfpzYxlPzi3LHDEg5EmKTu6DoUllme2yNeY2O2F5QG131u85i6mCqTOP_huvHuMbCQNMDLpyx9Y19eUBQfqsbP8-Y6C9_x5AIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح کاهش قیمت گوشت اجرا می‌شود
🔹
به گفتهٔ وزارت جهاد کشاورزی، حدود ۷۰ درصد هزینه تولید گوشت مربوط به خوراک دام است و وابستگی به علوفهٔ وارداتی باعث افزایش قیمت شده است.
🔹
وزارت جهاد کشاورزی با توسعهٔ تولید علوفه ارزان داخلی در زمین‌های دیم، به‌دنبال کاهش هزینه خوراک دام، افزایش تولید گوشت و کاهش قیمت آن است.
🔹
دولت قصد دارد با توسعهٔ کشت دیم، استفاده از بذرهای مقاوم، کشاورزی حفاظتی و روش‌های نوین، وابستگی به واردات خوراک دام را کاهش دهد.
🔹
برخی کارشناسان نسبت به موفقیت این طرح به‌دلیل کمبود بارندگی در ایران تردید دارند، اما برخی دیگر معتقدند فناوری‌های جدید کشاورزی و اصلاح بذر می‌تواند تولید علوفه در مناطق کم‌بارش را ممکن کند.
@Farsna
-
⁨Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/449141" target="_blank">📅 13:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449140">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c645673a2.mp4?token=oXg_DMXNoVdRKOId4mv3wypMOt8irgT3cesP3-vFa09TtpsivudLecqXz3vlZFpsjKLZaNlSBydE5h6YxVg6fBoZbaY-kyt0qBH4wjCHUtVkWky5VkFcFYPec_M2SR_tEFUAOlRLfoOvp3nCpdcFnSTfse0sZa8lUVsQjPaIJuTXU4Rmg0QvBlgq9XyxiXIbpImghhoaNONLYVUonMMTxbugrGXKJbCY94VpdUTiTrXhimW0c8OyrfnjnHDrgNw6lXK9AD6Pm2hD7AgDXw-egxWgvU63j3wRSgRSewi-Ocd8KkZin8c78RZJp5SX87JvcOI9OrqYVsIHsu0YacfFgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c645673a2.mp4?token=oXg_DMXNoVdRKOId4mv3wypMOt8irgT3cesP3-vFa09TtpsivudLecqXz3vlZFpsjKLZaNlSBydE5h6YxVg6fBoZbaY-kyt0qBH4wjCHUtVkWky5VkFcFYPec_M2SR_tEFUAOlRLfoOvp3nCpdcFnSTfse0sZa8lUVsQjPaIJuTXU4Rmg0QvBlgq9XyxiXIbpImghhoaNONLYVUonMMTxbugrGXKJbCY94VpdUTiTrXhimW0c8OyrfnjnHDrgNw6lXK9AD6Pm2hD7AgDXw-egxWgvU63j3wRSgRSewi-Ocd8KkZin8c78RZJp5SX87JvcOI9OrqYVsIHsu0YacfFgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشت مردان آهنین به تلویزیون با یک سورپرایز
🔹
سری جدید مسابقات مردان آهنین با اجرای آیدین ختایی که از شرکت کنندگان قدیمی این برنامه است و حضور فرامرز خودنگاه، رضا قرایی و محراب فاطمی به زودی از شبکه سه پخش می‌شود
🔹
مردان آهنین هر شب ساعت ۲۰ از شبکه سه پخش می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/449140" target="_blank">📅 13:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449139">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=mvxljjBY25b3mfJjsJH58TnEV4wdAwvxliEvmXUk_f7fhXDXPjwIshpU2bYkDCQM0xIQ6jmW2kjaHjUmyKk9NhWV3lWsGs2NJWtzKPqmv9TsmR0tiJJpkqzVKSqnblD1GiIEQgQeLVPtJiGwoXQ51I-QsbYJqlWw2eBac_h74a2OZAJ6PBRwYgYsM3l3hRtVCxturcS9wuuEIewpshMCmTQQUxcGX1alVaEV7S9ADTD8BxaBCJ_iuVZrEJh-cKlUYTAsak736y28hLKxvcCK6IWkY9VL3lt7PKK5ojSHOiCAprJPfFBCuGBaIUBbPUjcvMf3fu9fK-KNQO5sXhqyQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=mvxljjBY25b3mfJjsJH58TnEV4wdAwvxliEvmXUk_f7fhXDXPjwIshpU2bYkDCQM0xIQ6jmW2kjaHjUmyKk9NhWV3lWsGs2NJWtzKPqmv9TsmR0tiJJpkqzVKSqnblD1GiIEQgQeLVPtJiGwoXQ51I-QsbYJqlWw2eBac_h74a2OZAJ6PBRwYgYsM3l3hRtVCxturcS9wuuEIewpshMCmTQQUxcGX1alVaEV7S9ADTD8BxaBCJ_iuVZrEJh-cKlUYTAsak736y28hLKxvcCK6IWkY9VL3lt7PKK5ojSHOiCAprJPfFBCuGBaIUBbPUjcvMf3fu9fK-KNQO5sXhqyQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
✨
✨
حسابتو طلایی کن
✨
✨
✨
‌
🟡
۶۶۶۶ سکه طلا برای ۳۳۳۳ نفر
و میلیاردها ریال جوایز نقدی دیگر ...
‌
✨
جشنواره بزرگ قرعه‌کشی حساب‌های قرض‌الحسنه بانک سپه
✨
‌
#بانک_سپه
#نخستین_بانک_ایرانی
‌
🌐
https://omidbank.ir
‌
🌐
https://banksepah.ir
‌
📲
@banksepahofficial</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/449139" target="_blank">📅 12:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449138">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/449138" target="_blank">📅 12:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449137">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
تا ساعتی دیگر پیام مهم حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر انقلاب اسلامی به‌مناسبت تشییع و تدفین آقای شهید ایران منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/449137" target="_blank">📅 12:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449135">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhGmmEbqxQlfclp83R0uLUeHBc3GVfxMx-VgDZwGIoTMBSHT2SvrLyTFepYhaFGMMPil6gXS65mXTdRtbmnaD5TTy65dcPiYJSdw3JSXUR2aG1V9qwwMcxrpjAzOnC4hd7HKgavhXgtHwRjMk-GrMJaDwXTNfase38YarLtxrpAghhg8jygDBLv3hxzZMP2niDDS342Jj2kdwC241_zvFeBZ2L7JuoyMvK5XNrmlm9iJTgEwePZAzKdJu6Gm0YUfemwk-_Btu-j0BxTpinNxrimFoU4I0rR1jw7asX3HEdAElFVmcvqgCnDEa_HpRsb5yt14c14_Ap168nZZHSxFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBPi4_gCpSCazXTy4deZrujQ8Y3ntdJiDZus4Kx_LgGpMJ37q2pZihjSGRuueIIRu6wD4f7ZnvI1vbMDFCTi6-WCc4Uob15reehiALD-z3Z9kI-y2_533HTloAXgaDChQ7FQAC7HmLdGFs9GFmpzoLgsx_0CUHHlPUjuGLhjUwU-9EnALPXn0PXvlektY1VA95g0rWfzwPSoIlRdLe5sEQejAqhyYoNTyU-x_D4H9gMZHOj48tZoSfJ-D_Oz8XUkoAm8Enn0ZhGh5_BkYdK6ajKUNBSLLOl3DjDRbPOhvEkzWCetvvzbLwSZ6LdOTvWvSidPDPFj2IN9nlm7PzEAvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شایعه‌سازی ضدانقلاب با انتشار خبر کذب تیراندازی در اطراف حرم امام رضا(ع)
🔹
پس از پایان مراسم تشییع پیکر رهبر شهید انقلاب که با حضور میلیونی مردم برگزار شد شایعاتی در خصوص تیراندازی در اطراف حرم امام رضا منتشر شد.
🔹
بررسی‌های خبرنگار فارس در مشهد حاکی است هیچ…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/449135" target="_blank">📅 12:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449132">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvbMeElunMUxq4XRAVg7oGEu_Lo4dTzGXs67Cn0GpIzaTCoCWo8PXlkUQP34dHYy2h0gpc6xOkI7zjsUjFH7obM9gHLjOoHB2tRL4jzriGGHH4KgStgH-1Mcc0n6lWytXQSIfyY7BYLdQcxpIxnMGhu3CLbso5TE2A4WMUCx8g5O1iNlA61h6tWDmQygy18CiM3d5eka8owMYkjLtgQ2pH2-yDBAxlQ8ushrD9qZ5PzxDs97HDBahQoHEgMrXmo3W5_E6RRZUZQyFfkbVj5cjl0WBjwoMfk9XNbPGixgRjWhaN2Kw5hgsJngT1l0nGHsMK7Aol_738BRozBr2-vf0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JcYetLVjjRKQ7P7lyH3GWaIXB_3b6pk2IKkIkbWCAN-3LHo8cBxFOWqJQQVuYlbZizCjNDmzWMfM6NGaj3rhszNOLhzZ6npFmYCkzf8XbsgLam3KqnrjFd3HE0UARG0S0WF2kBSB_ad36uV7lfqjDqzRGVmonAOAAIcgMADBcCalZNtz8dG-NXMx3rA0sGST2VKwKeFVn2-f0WidBAlUMQzmcSvdFlu1szEIjJL-2qAWxaVbcwSQeEXuDiqieHSZXTsTyFtp01TgTeglR7wx7hvLiOSUQ9idHwzM42w8BxaWUiLPAXuV9nkdxO8u8BPCZfHtQ1_BTRwfy_njv2WYOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juf2UfbC4Nd-H97MrH1tqTZUL5-Cm5jnd2PRgPgxq-dVAjq4ZuzQ289EG8gO_F1XgTF076z4h5NQ7jruGj2_Xzn8bGdf7xoLGC_lStKsW3xUW38j73rr__9ZjosqRe7lFUkTI2TySs2IUdNgU5m4yiE19CqsSTDF90TnvuMopKaVZp2rql0KY1pPxe-08l42h-aAKt7uTp4U5HID8w8f2u0oUdtcUgt4J8RV6yuPq4c5K2wYJ9GUpebkX2OdJVBugwXANUhlKWp5aVJ4mWoT9ozU5o7yyfhXVo-xwLLwmnN-0rn2Wk0ISQQk26x6v4qbijUjL5wzlWWIe57bwtV2Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
اولین شنبه در دارالذکر  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449132" target="_blank">📅 12:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449131">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6zz4-eEUYYrUDwJfp_wlYivyCO1A3m5ZjwAPaODjHrqd1oFsTEWFj5Jcm88jyykpFT-AkqkEqDE2IFYSdMhHs7ALihh6ib3_cYTTc6nZ5avrJ9gjy-x00fy1BIasPiBJhjoJ4-bpkjAytMQi_6csB0J6-rrdk35rC00El5HnaYWuRQepvj4CRB7xLVFLXu1-LAoosiSCInLGl681bfKakA8UcSOo5fARLT3qyl7QP-BROlWeNVabSOzuVyd7o2OkVnXOrJmHBK7DAmgjCV2MlGNaXleF4YTA207EaariGx8DsmqyEiHYh5-cCOXSoHahUhux7Wo5zsLPQcpUU9JWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریزش ۲ درصدی بورس در آغاز هفته
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۰۴ هزار واحدی به ۵ میلیون و ۱۸۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/449131" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449130">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqpMqBladttNr9POa5evTlT-qhjP1RwgvHS3NGdOxcbdLDrGuPgIBPlGZtNA2vusGa7VbzxxP2JBkjEbPtjUyNOOJaIETiui1AHXj_TcT-_K5zr0Xhl6c2Vv2LoiPoR0e-5FilEVdc2nwlljk4TWLjvDwMmKSkIVT0nF2Se9xdW0HWHCDteXllyX6RtBky-jmeQxC5DISfhEnof7QjnSciFRXCWhD4CRKQRaXA50vZ3bgkQLukCAvGMGK0nJL8KcuwA2tlFJwFcuvdG4Jx1rf3a7iqKylts58jnneNvcWBy4dNBelyv8iLLLdAwNf_hJU6TH7Ic48SQNjGE3R9871g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جلیلی: مذاکره در صورتی ارزشمند است که موجب تثبیت و ارتقای قدرت شود
🔹
نمایندهٔ رهبر انقلاب در شورای‌عالی امنیت ملی: مذاکره یک ابزار است؛ نه هدف. ممکن است در مقطعی کارآمد باشد و در مقطعی دیگر، نه.
🔹
نباید به ابزار موضوعیت داد؛ آنچه اهمیت دارد، نوع، چگونگی و زمان استفاده است آن است. اگر موجب تثبیت و ارتقای قدرت شود، ارزشمند است و اگر موجب تضعیف قدرت کشور شود، مضر است.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/449130" target="_blank">📅 12:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449129">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
رادیو ارتش صهیونیستی: یک افسر ارتش اسرائیل در پایگاه نظامی شهر الخلیل، بر اثر زیرگرفته‌شدن توسط یک شهروند اسرائیلی که «از اختلال روانی رنج می‌برد» زخمی شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/449129" target="_blank">📅 12:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449128">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsD1Q9FtTyE1onAXgBg0VTpgI2Z7rlisdW-oPYJrR_KMsHJ9HZ66irmTYgJMESGdHHgXU02RzdtxUlYFy3Eijf_U18PywIeu848x-NyfNOnxO2HIHP0aHqWEXocwEtlhCTBIp901lHR9ljxFImQ-vgRwBhVanJ6y8s4wdEzsLY7gmUie80Ff9ybPfUI4xMFLlJJr7vYng3ajLuddGzF8yyhQCs0LulmBk-U5EoL7IilCr22S8wPW8ez_Ql4RRpfXRBiUvNNvMwMWobPqtTX6SHSf49cJqnMOPcaaq0_5CaX_3I6-wqHHBhbdgljlB29z0vKCoeqTxIQG5oQ8DVYOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آمریکا پل کریدوری ایران با چین و روسیه را زد
🔹
بامداد امروز آمریکا با موشک‌های کروز پل راه‌آهن «آق‌تکه‌خان» پل استراتژیک کریدور ریلی چین-ترکمنستان-ایران در شهرستان آققلا، استان گلستان را هدف قرار داد.
🔹
مسیری که روسیه از آبان پارسال کالاهایش را از آن عبور…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/449128" target="_blank">📅 11:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449127">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قدردانی وزارت اطلاعات از امت اسلامی دربارهٔ حضور در آیین تشییع قائد شهید
🔹
وزارت اطلاعات: تشییع عظیم و تاریخی بزرگ عالم مجاهد، رهبر حکیم و فرمانده بصیر جبهه مقاومت در ایران سربلند و عراق کریم، جلوه‌ای ماندگار از وفاداری و بصیرت امت اسلامی و تجدید عهد با آرمان‌های الهی مکتب اسلام بود، حماسه‌ای که بار دیگر عمق پیوند ملت‌های مومن و با عزت ایران و عراق را به نمایش گذاشت.
🔹
اینک که آقای شهید امت، خامنه‌ای عزیز، این دردانه تاریخ جهان اسلام و تشیع پس از عمری مجاهدت با بدرقه تاریخی ده‌ها میلیون شیفته و دلداده، در آغوش امام رئوف حضرت علی ابن موسی الرضا(علیه السلام) آرمیده است.
🔹
ما سربازان گمنام امام زمان(عج) در وزارت اطلاعات، بر خود فرض می‌دانیم که از خالقان این عظمت تاریخی، روسا و هیئت‌های دولت‌های دوست و برادر، مراجع معظم تقلید در قم و نجف، مردم بزرگ ایران( اقوام، اصناف، اقشار، اهل سنت، رهبران و اقلیت‌های دینی و...) و ملت کریم و پرشور عراق، مرجعیت دینی، حوزه‌های علمیه، دولت عراق، عشایر، موکب داران، عتبه مقدس علوی، حسینی و عباسی و همه‌ی دلدادگان شهید امت در لبنان، پاکستان، افغانستان، آذربایجان، ترکیه، کشمیر، هندوستان، بحرین و سایر نقاط جهان، صمیمانه و متواضعانه، تشکر و قدردانی نماییم.
🔹
صحنه‌های پرشکوهی که در عراق توسط عشایر و جوانان ذیل مرجعیت دینی رقم خورد و میزبانی کریمانه آنان، جلوه‌ای درخشان از الفت و برادری دو ملت ایران و عراق بود، سرمایه‌ای ماندگار برای امت اسلامی و پشتوانه‌ای استوار برای تداوم راه شهیدان و یاد آور مجاهدت فرماندهان مقاومت شهیدان حاج قاسم و ابو مهدی المهندس در مقابله با گروه تروریستی داعش، که نام خود را در تاریخ مقاومت ماندگار کردند و بار دیگر با مخابره پیام انتقام، رهبران جبهه متخاصم را به واکنش ذلیلانه وادار کردند.
🔹
اینک ایران و عراق تحت ارشادات رهبر معظم انقلاب، حضرت آیت‌ الله سید مجتبی خامنه‌ای حسینی(مدظله) و مراجع معظم تقلید نجف به خصوص حضرت آیت الله العظمی سیستانی(حفظه الله)، در نعمتی کم نظیر که قرن‌ها امت اسلام از آن محروم بود به برکت این خون مبارک و  اتحاد حسینی و علوی متنعم‌اند.
🔹
در پرتو تلألو نورانی این نعمت الهی ما فرزندان خمینی کبیر، خامنه‌ای شهید در وزارت اطلاعات ضمن پاسداشت جلوه‌های این عظمت با رهبر معظم انقلاب(مدظله) عهد «خون و مجاهدت» می‌بندیم ذیل منویات ایشان، تا تحقق آرمان‌های امام راحل و رهبر شهید از پیشتازان نبرد عاشورایی علیه آمریکای جنایتکار و رژیم کودک‌کش صهیونیستی و خون‌خواه رهبر شهیدمان باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449127" target="_blank">📅 11:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449126">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
از رهبر شهید عذرخواهی می‌کنم و حلالیت می‌طلبم...
@Farspolitics</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/449126" target="_blank">📅 11:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkmwOLZCzxW_PfDC2c5JSRyjskFS__5fFJuqK_nXIyYhQXtkDXCl9JnbdGDW6fJSLp4oV442tCQJdNv9WBduWZIuBNWCgfMfuzOCY-ansEkuAhT2URIRMxf4Rfc_yGAI2ZWVWjJkBr1cuLx7UchxliA-RPJOWnrUjKx3WQLomjONXlv7orAmu-JeJjZRaFy9dmK2bFEGxUnt5gl9OVgtdkq7xlOtAcJWnu3LJFZsQy7A2D9tCzYOZBArSFTqHlU9-jxnZl_yDeb3Ca2B9rokH1tfBD8z7k_N2lnbowxILdqFxs_d9YueuW0oOcxQduRtisqCgLskKOHqn4FxOiA2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7OO69nX0QYCdsVUcb90cIgh4XJHPhSDGoOSG4b9NKS_vRyeKtEnvrospSuBYWIsyJ7SKmeSJR1lBlaiihjYD4rbPIxfryYfnxncfU-e5m0SQnJlwOwscFy3m2qSHfh561GeOxlrataFLs3dV8i_6d2zS5348GqWLd6oSXaIkNjuHSi389qzzcoMuATSxgFTc7lcU5MGR26facEfxedxptXmFhDivBz7w4CqMB8WtLUUKnhiUYHiRe5kL1paSug990z2pQ4eEnkhucLikIfvfGejTtFVjUL3Zq6tchfuAV1od0eqXMXIRcvfwf0sKveqpTHyWuCqOCinYcSMtYchXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MnvnVyRvapc1TB73PB8MA-KhtpFdA580NkwanDN8HbDFRmKIXb_p6snHRjKbyOikWbUtJ9HUys_gKmRVpVzR2emzGxymnTe7gZccKS1iMxVGki8ChHv3esPHUjbGCb5L0uuE1lDUJhqTCSyuIs_Uv_2vmRLzKF_obqNBUuqJH-LzGaSKa_p1AIL_aoY0Aplm7MCUOIOILfw0v-OZGaQ8gT9R4wsvNjlJHp4P421-b5jeAqhRNllOmlLcb-tZ_ITDM9qx4ubkM-p7qgClwG4vQbQ7Flwotn9hZvXNFiuORLVgcLlVwpmmOPHvrFI1FmybLSLOi9jeniGpkBEJZFCdGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AT4JmpN8-hpBhh1GexOzJTwHQ6F2yjb0cAA3HjQXhBuIKsAukeP8Uv-wqvfodrelFGGDuFfSSFktpB7gnz4X6HS8DgHw5QRaYPqHxsYRw77ay8XprluHGn3Um0yShh8wxXFm4Bnsw6YOvgdF7JNYsCjYiEifNG_J1816wWuWgsZqt1JNsF31b7DgPCpua_VysntGpRGtyOHgW3z2HlIeyjqJWjr7WaE1DL3Cj0WjIaxdMzkY1sbxjv6ECOB2zmOH02KluShYqijg0wPG0Yw94RiPO1Ehmc0bKFx1fWotGhmkvKqvABwaemy_XcK4YyNbLvKN2b_aSh9621PrKIIDNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJTD4TS31NjbYPrgfkcm50A9IJcoIpfKpWk9H4-WZbiKNjzZNjHMSyCbB4ytXtyIviTZIy1XoRianfI3VKe7oqYo9ti4hLXAIkps0gTjw3ndvPBNI83fU-Aubt5YAGylHNTNPCymWfzxGfawfr4tSTG3N3BUhypiUBk0dP9ZU-o2zUfasaUmdKaZXQGhvaYa8EZXY5e8RNEadc8Wjy3z8glZ4DHCaqOcuakR3e2ZWwaLVMixGKR5RTYyiRtBgtqyQyGK9l0J5RBPn8JVA_NU3lnwNU2r-GPaXu0BElPQZVovIYtzxKMFuwrFv8fMh9wE0EWMruRaaWdhXW_PCaJjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBFrGdJMBd0zdSojcGd9CF6PWO5JPsadKX7p5iFUM_KcGWSU7vXXcDTINdhpF8QvpmSQ1inYn3D5Y8UuGAqPHBZ9Ydgp1CLT_oYyUnkmAUKdp_CGjLbCbA0H1s1lPjEZ7spHcpja_q5x4fW_RBwpp-tbkbMgYtucZEMqgmqoN6RAG7uWv9DtNYkUKcB9Ulv_PPLeTrk_aTB7MGKren7cv1tFvTR_u5uIoOdlgbend3OZPbrq87ue9V7ZsxwZKzOzZBL9m0Ajtnaz62vlkEj6sjKl1_faOnhkPV-MpCLNuU7bYkidNigjh2ojw5LZnTYmlMMuyeICJhDjszWdtsScwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BD47UgMPR-QUp5m_sQ5TeXTlmG0On-vIRw-F300gVB84-7pp1_EAwGjxec6gnQ5Z0DeVLZhSAmtO67O0LKQvcv9Uqc7Lp6OQ9p_4sy1wAYuE7CfxuEQdvndyTTDPFRI-R6Hb7gb0zL1-MPWmIh5x6Opbm29qIDuY1mYI1jEQ13pd-_WLBpfhzpeUgJPOIQhIHYNG62566ScrTddUoDA2SSfvTXpWHTtKe-MfPoF7v5Qli4DIZy6633FOa97nFbfh5mM8C3xbUrHe4nPoQfNXNbJ3X27mwfwL9Ii0AyyqwS72FdGfuV5PFQ64ukjXUV4JX4y7pJdfsWScpo5Qta7RIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-VmelPNkXmnynW-uc65XrjB6thqof4RG0xDtvKBC5qWQ8gzQj8ayeq8NdhRIsOblpaWbtCEQaqEcxQ7UFsEDBRh7Ri_se16NRoNkvmyejmKQbt9aXaLw8AwenXJoQMLsy0JaBacWs8xi9aDXfbWhg7K-ac_EpKo8K5x4OP2LrxabqWQfEtK_FP-SvjtY9lKRtA0CSR0DlTHHedadhGstwqCLohQY1qUUwpRROSbsiGE2zTUg85U60QOVZOCf_fvl0u1ykWhoxQ2tt0BVghELFjRTpIaSsH4aunzmIWW90c8lhKKeH_AgfNIRa4agkO71qMMU6_zBVet-J5iUMJSig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین بزرگداشت رهبر عظیم‌الشأن شهیدمان از طرف رهبر انقلاب اسلامی در حرم مطهر رضوی
🔹
این مراسم امشب و فرداشب نیز پس از اقامه نماز جماعت مغرب و عشاء در صحن پیامبر اعظم(ص) برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449118" target="_blank">📅 11:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205d1d93d5.mp4?token=gS9rk2N2w8h6Wf7WnnYKODiOZFHQcbhyri-V7KJWAU5rJpsCY2yXmfDFp5F304Vaofh0A1f3L2NLD-gvcoMJUbY0z5Mb4XAv_N6YeR2eMsnkgwoDSXRXiAW96YMHGk0tJvqjczoxzJ2aYTAJGDXwirAAJ6O33qZfJrB4Go1WB9zgdMweaya8SlcQ7n0F9UVqWoiTrBqFpo-GgP2v2bKArGeqQo4_9R4aXMU5T27-Mq6YlhNlQ74ByNNXMNj4zPt03bypS3B3HbtyulSHbwAvjOaFcZvB1mz2VJatSisn_vEQcwiXwvuYgWdmv4qswKGpBfITTYoLGnYZqYT1WvqdwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205d1d93d5.mp4?token=gS9rk2N2w8h6Wf7WnnYKODiOZFHQcbhyri-V7KJWAU5rJpsCY2yXmfDFp5F304Vaofh0A1f3L2NLD-gvcoMJUbY0z5Mb4XAv_N6YeR2eMsnkgwoDSXRXiAW96YMHGk0tJvqjczoxzJ2aYTAJGDXwirAAJ6O33qZfJrB4Go1WB9zgdMweaya8SlcQ7n0F9UVqWoiTrBqFpo-GgP2v2bKArGeqQo4_9R4aXMU5T27-Mq6YlhNlQ74ByNNXMNj4zPt03bypS3B3HbtyulSHbwAvjOaFcZvB1mz2VJatSisn_vEQcwiXwvuYgWdmv4qswKGpBfITTYoLGnYZqYT1WvqdwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سربازان فردای ایران با گهواره‌ به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449117" target="_blank">📅 11:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌ فرماندار پاکدشت: صدای انفجار ناشی از امحای مهمات بود
🔹
صدای شنیده‌شده مربوط به عملیات کنترل‌شده امحای مهمات باقی‌مانده از جنگ بوده و هیچ‌گونه حادثه یا تهدیدی متوجه شهروندان نیست.
🔹
این عملیات با رعایت کامل ضوابط ایمنی و توسط نیروهای مسئول و متخصص انجام شده…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449116" target="_blank">📅 11:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449114">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyZ1hrTtmbQdL6NfJGAM-zRIj1HfymSOgeueXwTdqw5vR0nRfB1yL1W2b2uic8ZiVOmzQhK4MsNJXuiKnIXdcuLl1viIw8fugjScUY_fGbuXGPvjmeVuZNPHUoougCspGGx_8yPsKrx0elHaXtkyJR9PheofiqL7iNAC7b_xISXwJ6-r84HzDNkIAn9iMb2P4eFsusvTUVx8Qr56VN5M9SFU6YkOm0G-vFOyRIdVbztwjpokTD_HUJxX8LK5Gq4OhCzBPPetCQGj8Rw53P3NZusoeBULWGIaaTjI8-QJENdJwHtU4AxOYBVmCo49xBcfTDHK3WzlAW2HhwDCjSbbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل ارتش: راه امام شهید انقلاب را با قدرت ادامه می‌دهیم
🔹
حضور موج‌آسا و بی‌کران مردمان ایران عزیز، مسلمانان و آزادگان عالم در آیین وداع و تشییع پیکر مطهر رهبر شهید انقلاب و خانواده مکرم ایشان، حماسه‌ای درخشان از پیوند ناگسستنی میان ملت و آرمان‌هایی ترسیم کرد که با خون پاک شهیدان به ویژه امام و قائد شهید انقلاب، رنگ جاودانگی به خود گرفته است.
🔹
راه امام شهید انقلاب، با قدرت ادامه یافته و آینده‌ای روشن را برای ایران اسلامی، رقم خواهد زد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449114" target="_blank">📅 10:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449113">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ad7ae545.mp4?token=JNDMnWp9J5-Wbw39U8xkbTXO6H2yDinrHKVw1VArB0dXKjSo3GPNTuZwPyuILuOEyb5oQVX3SmFJqzGcAQpDSQkSm7Sbl4ovy4iEri7FnqLXxmYYnaqKNzevaTDawjJQlx4eVKcEZqWh5HaPowwVhWdWXMZStloi11WXQ9wMhlb9lWBbsJpxxPvJR2DNUxBPHDFI73PNJvu73xfsv18d1dMZchCVOZTpBfBVjoCkzOTPa9lI--ZG1scTmT5C4pUYlKH-1U8MMjAZ6leOGDaFY-SpVkoeBxkXrwhwvmxMy2U2l68eBud9Bd4y6VX_6BYJjvDqiTT3is_1qgkxGSqjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ad7ae545.mp4?token=JNDMnWp9J5-Wbw39U8xkbTXO6H2yDinrHKVw1VArB0dXKjSo3GPNTuZwPyuILuOEyb5oQVX3SmFJqzGcAQpDSQkSm7Sbl4ovy4iEri7FnqLXxmYYnaqKNzevaTDawjJQlx4eVKcEZqWh5HaPowwVhWdWXMZStloi11WXQ9wMhlb9lWBbsJpxxPvJR2DNUxBPHDFI73PNJvu73xfsv18d1dMZchCVOZTpBfBVjoCkzOTPa9lI--ZG1scTmT5C4pUYlKH-1U8MMjAZ6leOGDaFY-SpVkoeBxkXrwhwvmxMy2U2l68eBud9Bd4y6VX_6BYJjvDqiTT3is_1qgkxGSqjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مزار مطهر رهبر شهید انقلاب اسلامی و شهدای خانواده ایشان در رواق دارالذکر حرم امام رضا(ع).  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449113" target="_blank">📅 10:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d989485063.mp4?token=Mr-Zv1yBzqKelavjCL3y1Pq2m6sh1HN5aXJnSz8vBNO_6w-ECev14HELqPgPoGmyNNhQJsk9HLcttrNuKi1noP7CknxatYsTv8NEDWtjkKVCc8NciSHXCIYOz91mV6GvtDB-v_fFBqaeD0ln_PDbB7XkY03-O-IqrmjXfm_n8AI4WlOFDi74je5Q8HPLMrsRZoWzfm4Csokvkmyubt8JKurYgCX-CdlLEdwN-nrPVKZnO6uu9FOjBv6SlstZGcmgZbUf51rxtcHh5moYJyD_zc1D5Kmk-ekYNl4dpmQIW-ZIClLg84ke8dkEK-CeN7zbKi6CyaOVEaQ4tOLYBJO8SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d989485063.mp4?token=Mr-Zv1yBzqKelavjCL3y1Pq2m6sh1HN5aXJnSz8vBNO_6w-ECev14HELqPgPoGmyNNhQJsk9HLcttrNuKi1noP7CknxatYsTv8NEDWtjkKVCc8NciSHXCIYOz91mV6GvtDB-v_fFBqaeD0ln_PDbB7XkY03-O-IqrmjXfm_n8AI4WlOFDi74je5Q8HPLMrsRZoWzfm4Csokvkmyubt8JKurYgCX-CdlLEdwN-nrPVKZnO6uu9FOjBv6SlstZGcmgZbUf51rxtcHh5moYJyD_zc1D5Kmk-ekYNl4dpmQIW-ZIClLg84ke8dkEK-CeN7zbKi6CyaOVEaQ4tOLYBJO8SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاس گل هری کین به ترامپ
🔸
در شرایطی که ترامپ به‌دلیل دخالت در پروندۀ بالوگان با موجی از انتقادها روبه‌رو است، کاپیتان تیم ملی انگلیس در نشست خبری پیش از دیدار مقابل نروژ گفته حدود یک سال‌ونیم پیش با رئیس‌جمهور آمریکا گلف بازی کردم.
🔹
هری کین: راستش بد بازی نکردم. وقتی در پالم‌بیچ بودم، او از من دعوت کرد که با هم گلف بازی کنیم. خب، وقتی رئیس‌جمهور از تو دعوت می‌کند...
🔹
تجربۀ واقعاً عجیب و خاص بود که با او ملاقات کنم. راستش گلفش هم واقعاً خوب است. امیدوارم وقتی به سن او رسیدم، بتوانم به خوبی او بازی کنم. از اینکه دعوتم کرد، خوشحال شدم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/449112" target="_blank">📅 10:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51b25b24c.mp4?token=fNfactKujvpeUOccBO102CI58a9Cblu_AraHR832NEVr5IB6I6xdJCbw81n2sSJxMmAwce5PxHWq5YKR2TUzna00PWVMppXQAUAxrxsnv1A3NAkjdFhy9Ks2jElGCF1e4GPI8zWgW-psF7xiDbmdC_z1BspJGwm-h6bn9QmkFG7jIJUV15Ui7ABZbtnQxFODUHIGbp22ntIVt1GyPzOwV8ZAtVsYyd_R2nMe6dWTVgegxLQGnAIBMKt7uwVmF9cPt6hsvrzZNEPyRVhe6UfIewhva7VHhNpEE3Mi4vzwDm8RK0BsOAjfyIrkFsN3zIOldzQBqJ2A3rphSRMI0wXMEg659G8QgzhOT8uTIm8BctnNzUk4SQGEVcDlKnpEinhSGWyGQyamPYr5AlPll0ELJ-GwDrq9Ub8JIF9fermzZsybOJiY8SCxLfEAgGhLkyoxTbDnWGpTOBu8YlGVImgRy6g1i8j6Ba2PB3YKVMBaTclCPn1C6ByMOhgZ9OD3Eg_S5zzQutzrkQxGuNGQGw7BxwfzuaOB2gaY8wgkILAROMzYLsbwVeLZ5AO-tmBQFxKrgBi6zCN5Qyw6bsoKs0HYsrO7TmNyQ2jSDZ3VjaDhyEYwPoL40WB084f2x5xOHSskEk8y4R8OgQG1hPKJO8ZONE9YDc2DB-uqIYTOEJMlBKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51b25b24c.mp4?token=fNfactKujvpeUOccBO102CI58a9Cblu_AraHR832NEVr5IB6I6xdJCbw81n2sSJxMmAwce5PxHWq5YKR2TUzna00PWVMppXQAUAxrxsnv1A3NAkjdFhy9Ks2jElGCF1e4GPI8zWgW-psF7xiDbmdC_z1BspJGwm-h6bn9QmkFG7jIJUV15Ui7ABZbtnQxFODUHIGbp22ntIVt1GyPzOwV8ZAtVsYyd_R2nMe6dWTVgegxLQGnAIBMKt7uwVmF9cPt6hsvrzZNEPyRVhe6UfIewhva7VHhNpEE3Mi4vzwDm8RK0BsOAjfyIrkFsN3zIOldzQBqJ2A3rphSRMI0wXMEg659G8QgzhOT8uTIm8BctnNzUk4SQGEVcDlKnpEinhSGWyGQyamPYr5AlPll0ELJ-GwDrq9Ub8JIF9fermzZsybOJiY8SCxLfEAgGhLkyoxTbDnWGpTOBu8YlGVImgRy6g1i8j6Ba2PB3YKVMBaTclCPn1C6ByMOhgZ9OD3Eg_S5zzQutzrkQxGuNGQGw7BxwfzuaOB2gaY8wgkILAROMzYLsbwVeLZ5AO-tmBQFxKrgBi6zCN5Qyw6bsoKs0HYsrO7TmNyQ2jSDZ3VjaDhyEYwPoL40WB084f2x5xOHSskEk8y4R8OgQG1hPKJO8ZONE9YDc2DB-uqIYTOEJMlBKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز فصل دوم «سرآشپز»/ ادامه رقابت بزرگ آشپزی در شبکه سه
🔹
پس از استقبال مخاطبان از فصل نخست مسابقه تلویزیونی «سرآشپز»، فصل دوم این برنامه به زودی روی آنتن می‌رود.
🔹
این مسابقه با محوریت رقابت آشپزان و نمایش مهارت، خلاقیت و فرهنگ غذایی ایرانی تولید شده است.
🔹
سرآشپز در حالی آماده بازگشت به آنتن می‌شود که موفقیت فصل نخست و استقبال مخاطبان، زمینه‌ساز ادامه این رقابت تلویزیونی شده و انتظار می‌رود فصل جدید نیز با همان رویکرد سرگرم‌کننده و رقابتی، مورد توجه علاقه‌مندان قرار گیرد.
🔹
این برنامه از شنبه پس از اخبار ساعت ۲۲ از شبکه سه پخش می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/449111" target="_blank">📅 10:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4HFZ_jehUWCzu6IsBqNYHEj751-0OXmz5K80_3zrJUlDm2TCUk3za3Iqewj8WFeTy4KyRJmRTPRaVf_yumOU3PZYkZfYCD8i1YzweXzC-ZCcZnxMoMCPz9NdtED1rAj70d1Fnaa6qlQcsB0-35li-YtKjAF3wOlq8_ArYsLVtp1yWPTzuD-FxwuooxFHFHmKSjBrydeIXSkd6Ym2oSXGXRedzB_nCNtm-h-MjUG1xtO-6YzBbOQN1NGJ_EyUNA1zk54f2Rycs7Whh0iDlEFfpATRkWolye7DZ9hVDyFUARKcT1p62Z8B601k4MubNvJWmS_ze6C8NGKu_ni6_Io6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449110" target="_blank">📅 10:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449109" target="_blank">📅 10:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrMyHyGqA6n7LI3n_YRT0oZaMfk6Aebp69YgScpBXIH7SKi_WXSlYRWjsjBAFw3Cw_Dz7fWCF0WQgZqu3jL6oNdwozBRXd1Pq-Qyms46q6CZFQONZ9j_reI7C3GOPGYqGV1vwPmQuTC1zTC64W6Yb_TFsDsX3O7kBdFLpriXTlnhKLgfJgU-itSkQ_yiKv4zyQUMpkT5P-R0eU9vFUqjO_yomIUp7GEJujIrmCVxwoSPvkCysJJiwtVK4kBr0s801vzIlj-ePkiliC2pUAWpvpXkX-lue7J7ZhQWW2M3XQru6PqnFg5G_rlWax0gYEVD8-_fhoIomFDnDEGX-8Jspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پیام رزمندگان پای لانچر به مردم: خدا را شکر که جای خالی ما را در تشییع امام شهید پر کردید  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/449108" target="_blank">📅 10:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
شنیده شدن صدای انفجار در محدوده شرق استان تهران
🔹
دقایقی پیش مردم در پاکدشت و قیام‌دشت از سمت شرق استان تهران صدای انفجار شنیدند.
🔹
هنوز منشا و محل دقیق این انفجار مشخص نیست‌.
🔹
پیگیری‌های خبرنگار فارس برای مشخص شدن ابعاد این ماجرا ادامه دارد و اخبار تکمیلی…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farsna/449107" target="_blank">📅 09:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449106">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
شنیده شدن صدای انفجار در محدوده شرق استان تهران
🔹
دقایقی پیش مردم در پاکدشت و قیام‌دشت از سمت شرق استان تهران صدای انفجار شنیدند.
🔹
هنوز منشا و محل دقیق این انفجار مشخص نیست‌.
🔹
پیگیری‌های خبرنگار فارس برای مشخص شدن ابعاد این ماجرا ادامه دارد و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farsna/449106" target="_blank">📅 09:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0Jkp7wMe3GP1VwkyhA5eTb-0KFU08yqQ5Xzp34qxlwENFCkqNSRwBRi-P8IwfDdMvzBIuOX6mHY_XRZVbiACz4jlDs_MlYmbS-N_WKHA5tUOa5Cvi1hfsOZuKEnKKbB_LCdS3-wCWzndphSXgKXAKpZgyqXJOARUOjABPCCJ8MvuzbO05uxzaknkhV9SR4cBH2f2w5Vj67khHmfEjZ_75TzEOFFufXcWB34bUXoCN6K9-s26yyK7Tl0qxNqVONp6GPtH-L7tZpaufJBFMBFHDkhhSKKA-SuZcb1Bj45W_aPN0dxJndkBw3eP_QtGfdqu1KYaJYztB4jFn3BMp2Ffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی با استقبال مقامات عمانی وارد مسقط شد.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/449105" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449104">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5wi4C_0YyYx3wS1YiXt16HUE97aYqZPMR06YNdgROM5NO3s8y4oau8xOm1DCdOsQ_Zojpdz3gPohjOpB1TJQOoWtqk1Prw0Q2JMeMNlxj0XXwcuN2krMRm155ghbbcQIiK3wHRCVUEGuBwxqa04liC4mVNuwEs51GL_bc3EXBgrlTW2Vhn9m42YkkCADrjq6D2Gti32lHJfx9hEReQ9Jtv_k29y4tPbIZy-DmbRYZkbF4mhh2L8KolzbHZFGZc3OfrWWrPKbYP7fqnoOa4uYQXH_t38MJ4d7JIQmje-eznD8SqkSwlVHvYgr_YT_a3zi69T8AN7LPzJmwDvKKqiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی وزارت خارجه: نیروهای مسلح با چشمانی بیدار تحرکات دشمن را زیر نظر دارند.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/449104" target="_blank">📅 09:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449103">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a954ff7b09.mp4?token=jNjbBaGYrCC5STz2Z8pIEOGHzJGekuC__zIlWJzHkyDwl0XLtttC8WWkXbNTKc8ScbJbMVOXCTCq3I4Fbw-ryc9aX5qA0nO3cNO_pk39_-I_LHshINYSl0FeQxH0txhbuHfhLKA36fJoky906QQ-Z5SbojAoNnJdHzs358dUoJ5uHYCAsrnVjrIqdcto_S8qZ2ARmAixlIqIRZEmzRhSHGVNw3lhVmiwk6xbIXIR2SCGttAse7uHdJfHAFviLOyD1YXBBlPOvI6ijKktGPaWsrQ6d7enFZirklIonlQVgFSmsZyVVnQh5j-gqKkMzeaOocacHTjopM1bdWsJPieHrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a954ff7b09.mp4?token=jNjbBaGYrCC5STz2Z8pIEOGHzJGekuC__zIlWJzHkyDwl0XLtttC8WWkXbNTKc8ScbJbMVOXCTCq3I4Fbw-ryc9aX5qA0nO3cNO_pk39_-I_LHshINYSl0FeQxH0txhbuHfhLKA36fJoky906QQ-Z5SbojAoNnJdHzs358dUoJ5uHYCAsrnVjrIqdcto_S8qZ2ARmAixlIqIRZEmzRhSHGVNw3lhVmiwk6xbIXIR2SCGttAse7uHdJfHAFviLOyD1YXBBlPOvI6ijKktGPaWsrQ6d7enFZirklIonlQVgFSmsZyVVnQh5j-gqKkMzeaOocacHTjopM1bdWsJPieHrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ ۹۰۰ مار به ساکنان مردم چین
🔹
در پی جاری شدن سیل در یک مزرعۀ پرورش «کبرای قاتل» در چین، حدود ۹۰۰ مار از قفس‌ها گریخته و به ساکنان منطقه حمله کردند. شماری از ساکنان دچار مارگزیدگی شده‌ و با شتاب به بیمارستان منتقل شدند.
🔹
مقامات چین اعلام کردند که ۳۹ نفر از مردم جنوب این کشور در نتیجه سیل ناشی از طوفان گرمسیری «مایساک» جان باختند.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449103" target="_blank">📅 08:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449102">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انهدام محمولۀ انفجاری در مرز کردستان
🔹
فرمانده مرزبانی کردستان: مرزبانان با اشراف اطلاعاتی بر تحرکات گروهک‌های تروریستی، بسته‌ای مشکوک که به‌صورت ماهرانه‌ای جاسازی شده بود را شناسایی و کشف کردند.
🔹
در بررسی بسته ۴ قبضه نارنجک جنگی، ۸ قوطی تله انفجاری به‌همراه ساچمه‌های فلزی و کابل‌های مربوطه کشف و ضبط شد. این تجهیزات برای اقدامات خرابکارانه و ایجاد خسارت قابل استفاده بودند.
🔹
شناسایی و دستگیری عوامل مرتبط با این پرونده در دستور کار اطلاعاتی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/449102" target="_blank">📅 08:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449101">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Prd8Da9q6O1rTcmtR0uUzEJZKwtBKVvyNF0hJSxRqLu5P7o3aNmE7KOsrMYjXIPSVFro156EQ9duDz5f8f5Wja7J68QQkb0yua_Ac3O5oy94FQZo_NWAWo71tsUb02DtcWICiyT3tw-bPOqN9x_8gvCIGxsK8-Ue_gucp7S39JMy6KUCvy_w8v0fTjL6o669ilmJMSnD2Xhy5cPydy4jk_DTPpuU2-o0jJMLa3fhTvOKhwXwKQUN-Buvaju_5cR3EZmt2Jn9sxX_0aeIreH525uTAeV25H_3j4umVwAKzwpvEVqLJLuytV11Q6z9y6atxDEwd_-5PnLjgouWvBYZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آمریکا پل کریدوری ایران با چین و روسیه را زد
🔹
بامداد امروز آمریکا با موشک‌های کروز پل راه‌آهن «آق‌تکه‌خان» پل استراتژیک کریدور ریلی چین-ترکمنستان-ایران در شهرستان آققلا، استان گلستان را هدف قرار داد.
🔹
مسیری که روسیه از آبان پارسال کالاهایش را از آن عبور…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449101" target="_blank">📅 08:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449100">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860819be3b.mp4?token=PRcIu7t1vwXXYokeTGjaSpCxRFcteNY4w2cIrcd2YlKgodkZwjnrDH1RLKv4cy88UnFKe-Q-vvBObRdatE8ym4iakQFn_Ue-JKgZxCb5Te1bwAjliipAy6mdh3ddJt4VFsuSVSgJNJd4-R7v5aJP3HRnCZvxcYv9Xq5UqyLOyhMESmAVu3Z2_MCbj3KDXwd7fwv1fh-zr4VJnWtGCw7xfWMuylDYLdln-FQKeclMv9CsnPUhDUFc0Nsce-3r8XCPgL0W8m5VUt4_v_qHlSVmSUZau2oe2hE6qcWMfZZnFdjE5vUvW5hqt-Eq-o2qFq1NUn4TNNtn-ywBA5YhoJZLyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860819be3b.mp4?token=PRcIu7t1vwXXYokeTGjaSpCxRFcteNY4w2cIrcd2YlKgodkZwjnrDH1RLKv4cy88UnFKe-Q-vvBObRdatE8ym4iakQFn_Ue-JKgZxCb5Te1bwAjliipAy6mdh3ddJt4VFsuSVSgJNJd4-R7v5aJP3HRnCZvxcYv9Xq5UqyLOyhMESmAVu3Z2_MCbj3KDXwd7fwv1fh-zr4VJnWtGCw7xfWMuylDYLdln-FQKeclMv9CsnPUhDUFc0Nsce-3r8XCPgL0W8m5VUt4_v_qHlSVmSUZau2oe2hE6qcWMfZZnFdjE5vUvW5hqt-Eq-o2qFq1NUn4TNNtn-ywBA5YhoJZLyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰ کشته در سقوط مرگبار هواپیمای مسافربری در باهاما
🔹
یک هواپیمای مسافربری کوچک متعلق به شرکت «فلامینگو ایر» در آندروس شمالی، در غرب ناسائو پایتخت باهاما، سقوط کرد و هر ۱۰ سرنشین آن جان باختند.
🔹
سازمان بررسی سوانح هوایی باهاما در بیانیه‌ای اعلام کرد که اطلاعات اولیه نشان می‌دهد این هواپیما از فرودگاه بین‌المللی لیندن پیندلینگ به مقصد فرودگاه سن آندروس پرواز کرده بود که پیش از فرود دچار مشکل شد و به درون بوته‌ها سقوط کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/449100" target="_blank">📅 08:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449099">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSC8yO3K3mZiQm6Z31zpA3zm5n2yfPMQosLdjUMfFVa_RbjNcTZ8JOTfqM58KJm5GjOhJDrLsoBy_ZGFl1GVXyucvhLKF_GxN_m9GhfPi6FB3i2ukNIcs4XasdV3LkNKyqzocsFVxwRlYjp5RO_Ik15gsnyjFvwsdHbc29V3jMbbKiFYoljPo-VvO-L7sr-77ipeTB-fLFxliWmmGkmlKkl9SQYA0gU_0eIR497Rah6Hj20VUC4o-OY_RvFp8TqEQLQUqwutoG9bstg6utTvlVd3LSV2ldj-tRqbD78-4FMSnCgdUyx2MuNGz_MrOw03M4PNle11HFgIfQxEYmlMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رایگان بودن مترو و اتوبوس در تهران تا ۱۹ تیر تمدید شد
🔹
با تصویب اعضای شورای شهر تهران مترو و اتوبوس تا پایان مراسم تشییع رهبر شهید انقلاب ۱۹ تیر رایگان باقی ماند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449099" target="_blank">📅 08:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449098">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDMFKvMDVBl5IDvnQ8fZ3jfWheF2wvkD6QPuxJqUbYck2bSOyr3FHah2p5_MBCiq_rfh5u_fpBNLfP-EN9XxJZoHWyvjfKZIR9if-86UNCC6NKxlZ7XoyZQS04c8i5h3BgPCcGhnGzq1jx4XYhdQ6RLnPxKqQxKFfbib3gjzyMAZ5R9HpFeDBthbDsFFLXpCWCHOQ-Jtn9z1MBMnT-D4CEzDT560hbf-9tICntSR-IJAjwdLPinBhF1nK0nKtdwtx8v8fEQZA0Uo0Azwb8vFF6qpSzlcC2XzUo1X19uW7uyyfamBS9OCPIwXr8rQPA7Y-4q8hN7mL_mqten2L3c0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلفات زلزلۀ ونزوئلا از ۴۰۰۰ نفر فراتر رفت
🔹
رئیس مجلس ملی ونزوئلا: تعداد جانباختگان زمین‌لرزۀ مرگبار به ۴۱۱۸ تن افزایش یافت و شمار زخمی‌های این فاجعه نیز به ۱۶,۷۴۰ نفر رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449098" target="_blank">📅 07:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449097">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV6bxiaYY13BGME6n_dknldxti3rCFUkI8Gu8R8GrsMaLM5duUnhzzG8fp4wGiYvpqJPa4mUQ-iuZG9MVGI9iNLlGQkGFjPyQcSw0hHDNTYIKcuCbrkqV0TRTd0tvaWLek6xltucn6afpfENRn6T2JIvEcaJnyX7qUjjk-fKMEfWH7LAUZMiKgZt41aejKbta6BsDgd80XhPbOOzTEMCKFqevWYsullj4SnBESFqBtU_Tbg-kGJOu5-s1CEvdfg6groJurcA3b10hiETXgmdfcLP1NKFLqdcOTV715LGBhv3ADmt-_axex_L2cxpY9clUArEtdApjwi4PG09zQdRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام‌جهانی‌؛ یک جام برای فوتبال و یک گنج برای فیفا
🔹
یک تحلیل اقتصادی تازه نشان می‌دهد بزرگ‌ترین برندۀ جام‌جهانی نه تیم‌های حاضر در میدان، بلکه فیفا است؛ نهادی که بیشترین سهم از درآمدهای میلیارد دلاری جام‌جهانی ۲۰۲۶ را به خود اختصاص داده است!
🔹
فیفا از محل حق پخش تلویزیونی، قراردادهای اسپانسری، تبلیغات و سایر فعالیت‌های تجاری، انتظار دارد حدود ۱۳ میلیارد دلار درآمد کسب کند؛ رقمی که جام‌جهانی ۲۰۲۶ را به سودآورترین دورۀ تاریخ این رقابت‌ها برای نهاد حاکم بر فوتبال جهان تبدیل می‌کند.
🔗
متن کامل این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/449097" target="_blank">📅 07:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449096">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKmeTgLur7vlrwJP_OhnJLM3jCMupIgm8iepWqKNsriyjGSNxq2jV-xM5QloTYNIilQ4ID-sYWQMkyAWXJx4Ym_mR-bsSJPBo5R65GfwENlrWUUixAqK7Wzt2VLNgpRm_3SeouwfDZDSU1G3bimMkRExHrNBIiDDScFlmoqmKFJMPC95DqJNyTzORRQVqWFR3VGHjrBWVEhEvxGgfzFUOOVT5-3t_gB0JgDUUFed8aWXBLGvonQvtN5dGkMBVw9FIavPQA8eR4wAQ6o-Wr13FGpng_Co_sAoeT0yQ8eFepIbC8HnQwl49xafsL3WSqDTK3kGzwT-AIBsuRTmqtHpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با ذکر «الله»، آتش‌بازی تهدید علیه ایران راه انداخت
!
🔹
رئیس جمهور آمریکا در پیامی سرشار
از ترس و خشم که در شبکه اجتماعی «تروث سوشال» منتشر کرد، بار دیگر ایران را تهدید به حمله کرد.
🔹
در این پیام نوشته شده است «هزار موشک مسلح و آماده شلیک، جمهوری اسلامی ایران را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — حمد و سپاس خدا را! »
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449096" target="_blank">📅 07:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449095">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔹
شهردار کی‌یف،‌ پایتخت اوکراین: در پی حملات موشکی روسیه به چندین محله از این شهر، دست‌کم ۶ نفر مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449095" target="_blank">📅 06:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449094">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeFsOlsmWXwoyP0Yn3a8hH0INCTQmB2QFR_QS8SIoeAMrNXemHxboc6NhjIJOu2rM6j6HT_6KNihYH1Gv0_pTq0YS120leGGrazMPpMbCpla9nZwHAnsu9BLLo67_Ot01v-LnvitloKRvWbBEjzjZh52W_pzlLaxqPb_YyeXPO8np0ilYH4WArKZ1jDlkIg9QFVIQDrAn7-KoGQIyyFtKvWJH-ub1L18iMJeHEMJOAH7GUrnoRmzQN8XXDjIpC8YVxe2s7jcd4vamenkGklRemq1R_0sF_n-23vrhxjW68g4uKBh2lk2W2wF7dZjqO0FUJi490Cf7QG8vw_dRPELHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردی که ۱۰ ساعت زائران رهبر شهید را از زیر قرآن رد کرد
🔹
نه تابلویی کنار خود گذاشته بود و نه از کسی چیزی می‌خواست. قرآن را بالای سر گرفته بود و مردم را از زیر آن عبور می‌داد. کودکان، جوانان، زنان و مردان، یکی‌یکی از زیر قرآن رد می‌شدند و دوباره به صف جمعیت بازمی‌گشتند.
🔹
بعضی‌ها با تعجب می‌پرسیدند ماجرا چیست. وقتی پاسخ را می‌شنیدند، آرام از زیر قرآن رد می‌شدند، دستی به جلد آن می‌کشیدند و بی‌صدا اشک می‌ریختند.
🔗
ماجرای این قرآن در میان جمعیت زائران را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449094" target="_blank">📅 06:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449093">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaVep1MdvenBCwqgsI1IFsat5tXCW0Z9D5JqQ91t4Y2C9-4AfFbOce8x3e1kbONWxmPt3AzpomjB27uddXly8j10k4JHpFe8gYk6dPgXhrr3ymxblGvFQsHpl0SGTViMqt9PbB9hQCoS4mCS-8ninBGmn-pxMv8B1sPI6Dgm_h5L0WROE6nbwsLU1kf-Bb5jsnEnleiwvxz13xZzgS7WaOCULdxCH7jINz1M8nyll4Sxakf2Xo79PiBxdGgs0oSpwrESfgaI8zxDfAlKm2yXSf840ze9vLNPfZx68rrYNt_p9y9rONvGpIKASP1BYlUu1e-RlrNNa4rkFZnYhr45lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۳، ۴، ۵ و ۶ شارژ شد.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/449093" target="_blank">📅 06:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449091">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSHUrlwiOWKYv5qlpbAT1ObGyzbjVUQTCX9cbU9OpoyD9FiqTgm-boQ271RdVSokch-310QvCSFE5ncJEV_U679X3rhFczD_HvL62O0VQPQgxvasiqL8hQRxJj5Eoi9KtKhYoN6GGeDX7GM_W22UkUTzi4xEGx7HzLvtM-XTndmQMjWos1fljXW4ccNFoCU6-c5ZYBomrG9-2um_QoszwEdjU7MRSrRHUyg6jGInP5pXMuC6c7WL8hAg-_UWPf2KJ0Z-3epptkgFnm6wWotmSZwETCngTbUmQiytc8FmNhP87_ppDtwjSranuHt-QlozafkXpglcxClJKQbgMddaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش عراقچی به عهدشکنی جدید آمریکا با وضع تحریم علیه ایران
🔹
ایران تاکنون به تعهدات خود پایبند بوده است؛ برخلاف آنچه از سوی به‌اصطلاح وزیر خزانه‌داری ایالات متحده شاهدیم که با نقض بند ۹ یادداشت تفاهم، تعهدات آمریکا را زیر پا می‌گذارد.
🔹
این نقض، در ادامۀ سایر موارد نقض تعهدات و اقدامات نادرست ایالات متحده صورت گرفته است.
🔹
واقعیت روشن است: تنها راه پایبندی متقابل هر دو طرف به تعهداتشان است.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/449091" target="_blank">📅 06:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449090">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZWkryh15MGG7cpVx87jFn77oo5dN1B0m1-1u3hFX_dP3NC4HGYDHru7V4KXdTANIYZ3uZnca4S3iXKq3Lc8jMTgt7AvtKBpv_1UFD6BJ-5sMa-PQDz5RqjjSH782FKeNEWeQHmUrIp2S20GfMef_BhrmR_MPe8cerWomOnzR-v6hwk3_aGvAwiAqjKyHSczBhe6huvCBe2Yj3PGP9tH5h9U7k-VyYa-hc_HHYMaJOVRnBFZ7fbg5ngedo0C6mDXkRLk_Jac7bwBGoieaKbIL3ycxdfbhprEZCzYoYCimI4nUdrTTPfa_WTflrup8K2XUe7nTbvDipe-w83QP1WEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیالت راحت آقاجان، ما مراقب هرمز هستیم
🔹
در اوج گرمای طبرسی ۶۴، جایی که غبارِ راه و جمعیتِ زائران چشم را می‌گیرد، ناگهان بویی متفاوت می‌پیچد؛ بوی دریا، بوی نمک و بوی خلیج فارس. این بو از یک موکبِ خاص است. موکبی که خادمانش از یک جزیرۀ مهم آمده‌اند.
🔹
خادمی که در حال تعارف کردن چای و شربت به زائران مراسم رهبر شهید است، با همان صلابتِ مردانِ جنوب می‌گوید: «ما ۱۳ صیاد، همسر و بچه‌های کوچکمان را به خدا سپردیم و آمدیم تا یک پیام بسیار مهم را به رهبر شهیدمان برسانیم.»
🔗
برای شنیدن پیام موکب‌داران هرمزی به رهبر شهید
اینجا
را بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449090" target="_blank">📅 05:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449088">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yvs5ju8R8Uc1Ru3XJq0Ns2SpO3fLVE9_ptfuTjDD4XI0IWmvQqyJbmwPwLk4wosTYvbVZoGig1ZCInJrhB1j4XgBGXlvRX2vfHKSToj2DFhGQiKgI7W39oIq7rL8AM8Q6S_06Hb6O-LQ-CBwXwyjGHEbZtWrRn1vlaTd8EFouTBgboC9zn582CtaihP_-AMpUPTPZJevN2wGUK_MQ3DW-zJTgWshQRH8ZuS8SkKSR5iB6tQqEHec5UP7aLCFJng53-yyIYV_J67aGSnnlXUJcRiZC6mc6v8omLMlfj9ic4qanvfWsKgYQt2zXWoTPrk7BrOmXXTVftcIlHtBD5ePwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی چین از سلاح مایکروویوی؛ سلاحی که هدفش را بدون اصابت زمین‌گیر می‌کند
🔹
چین از یک سلاح مایکروویوی ۱۰۰ گیگاواتی رونمایی کرده که برای از کار انداختن پهپادها و سامانه‌های الکترونیکی طراحی شده است.
🔹
این سلاح به‌جای انفجار، پالس‌های مایکروویوی فوق‌قدرتمند را به سمت هدف می‌فرستد تا مدارهای الکترونیکی، سامانه‌های ارتباطی و پهپادها را از کار بیندازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/449088" target="_blank">📅 05:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449087">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kgl5sRwbLlu_Nc-e9MGQdbN4Ja7gqDOvq57AdFYnXMe5Iy_tABQILXADZ_DOc-FHm_g4ONLAnupl2X7_w8yBJV6myPL1HhyYYB-xNq_Pc4UIKRNojQOI4r-upiG5Xz3TbXr-FLUIM_ZK-2MaEwlGFgdFuLc42UcrpxyZJ426XtlPjQzqtIVW07lef5fhJIEWeUr8MB3eq5WnKliyYSzS7WUh70bufVCA45fO30sT6DRnU4GpTnCgyOa-_-Xb2wR5H31SjFzoAoQzoJCX9Ckeby-EDI6unyzxfyw6XJ-atrCkwBYdHtRCh1TIqxlWCuChusNbws_eQHWMBNdiHWHohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام دختر ویلچری به رهبر شهید رسید
🔹
جمله‌ای که روی بدنۀ کامیون نوشت، از آنِ او نبود. یادگاری کوتاه از دختر ۲۳ ساله‌ای که بیماری و خانه‌نشینی، راهش را به مراسم بسته بود؛ دختری که تنها یک خواهش داشت: «اگر من نمی‌توانم بیایم، تو به جای من سلامم را برسان و بنویس؛ آقا شفاعت کن ما را.»
🔹
به بدنۀ خودرو که می‌رسم، اولین چیزی که به چشم می‌آید نوشته‌هاست. آن‌قدر زیادند که از رنگ ماشین فقط تکه‌هایی کوچک باقی مانده است. هر کس جمله‌ای گذاشته و رفته؛ یکی نوشته «آقا شفاعت کن ما را»، دیگری «شهادتت مبارک» و آن یکی «حلال کن که دیر شناختمت».
🔗
ماجرای جالب این خودرو و دست نوشته‌های روی آن را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449087" target="_blank">📅 04:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449086">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdQNpM0G5i2b32kR8IetGQWwFY3JelY5bhtLhrYahhWAj2xlDyRaF0WaIquGfhiZMG6LSLGfQQgLCEWuWNNfebZF2HTsJxpr8QLBNMur2fE62th3jJB9IQzODH_Kuv7KngYSs6lcgQDJGSWGqdzcO5DwuxMkCPuQRD49c7XJAaWPhGFXh5RoDuj6GjukqY9Av-2f09bo6gpotTSPZBMv9LJxQO3i8HTq06nzBnx11q8cYxXDKT4kC5rbhB1ipLzkoiSRqOfn-olPs35qdSPLHZ3dodiBuvazm56wgXQoeGIYVfA4e4zVFGhZujKRtxSybagm6yJSkuiWWqKc685IKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شراکت اپل و خالق چت‌جی‌پی‌تی به دادگاه کشید
🔹
اپل با طرح شکایتی در دادگاه فدرال آمریکا، گفت اپن‌ای‌آی اسرار تجاری و اطلاعات محرمانه مرتبط با توسعه سخت‌افزار را سرقت کرده است؛ پرونده‌ای که دو کارمند سابق اپل و مدیر سخت‌افزار اپن‌ای‌آی نیز در آن نام برده شده‌اند.
🔹
اپل گفته اپن‌ای‌آی و استارتاپ «آی‌او پروداکتز» با همکاری دو کارمند سابق این شرکت، به اطلاعات محرمانه مربوط به طراحی سخت‌افزار و محصولات معرفی‌نشده اپل دست یافته‌اند. این شکایت در دادگاه فدرال کالیفرنیا ثبت شده و اپل خواستار توقف استفاده از این اطلاعات و دریافت غرامت شده است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449086" target="_blank">📅 04:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449085">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q78pDxJJoh__6fycF5nw8bNCcRRw5j83ER2e56GyZnwiA3r3WcAj7j9bnUEWqMM70-aYpPL14wK4FZcnDdt_R9LFdfKZ5jN2Vbih5YyQUPpbWmeoSi4KZ3bI3Wt1eRhRoVv_U6C8qbGTYi9sids7XoPJPNuIM8s9_9TZ3mQIm2ViGRFeB6F67RBuNbaefDpagwVSpmU5P8a2dZyoygr6HwDqZRzdE0gmoBVJTCrZm-X-m6t178CvGHamT1V6JNTKL--IH8DApdkII1Z0BVpo_-7d-dNUMybL_7WxCxP9fc2xiYkWDctrjiA_rqas2kDRppBjOfvTvl-V3T8Sg4PNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من داوطلب قتل ترامپ هستم!
🔹
با پوششی از کفن سفید و پلاکاردی کوبنده به صحنه آمده و برای انتقام رهبر شهیدش عزمی راسخ دارد؛ آن‌قدر راسخ که می‌گوید: «من داوطلب قتل ترامپ هستم!»
🔹
حتی اگر آن پلاکارد کاغذی با آن جمله قرمزرنگ لاتین در دستانش نباشد هم، پیامش روشن و واضح است. لباسش تضادی آشکار با بقیه دارد و همین که پا به خیابان‌های شهر می‌گذارد و یا در روزی مثل بدرقه رهبر شهید به صحنه می‌آید، دشمن همه چیز را از وجناتش می‌خواند. او نماینده‌ای از همه مردم ایران است.
🔗
جزئیات هشدار بانوی کفن‌پوش به ترامپ را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/449085" target="_blank">📅 03:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449084">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69921fea5c.mp4?token=nGcggSI-RiIy8C1tsQNsQzGVs3lTQPKvVdTTOCvlw4OfVi0NDCpg2XrPwb57v9oJyN7HP77pv1nxTqFWLNvHdNavUpPYmexs2fmKJ7sCrysCqFPx1PSdyiAdgl7AIVAXi6xH9zWOGib8SKm-YUFusvissneLTkIQKkSAmKXpWG2D0Hk8J6sEDEbTPHY5f8s1zEYFyNBNnMkd4AQzGlXkCGn2plYFxlpAzoqKqzPYCabk2Fqqec-T71jXYCTx9kBuk3-J0Csf0L7FoPWn6qFtAxsL5tSjIDfHBJH3hCnfHCW6YLbviNYyMFoBdk09kHOsIYGm_KpPePd6NxSXrRruMa-JL0aoTOEaiVBqwLSqqHFHvfv73h48hKZisw9ADNTVm-h6cMknwEt5D4PvJ6Dh_RbhecMEnB5X4jUZjK6kskyiFsRsUzR9vY-DDTXH8k_DUWBybLgBMRv1Cfo8At8pwe-B_Mmk1N68K6kP5iVYhElA_IXuBMsmrEGHzhcldh9VvOC7_omdMclHNr9VhttMA9Dt9psdhFYGPIyBHgMwz1hJ5ZAlQ2sb2DN4R5fZXMkV2Gf4mfL0tYmaxwod9Dt4RXww0kFKowd_P4f8zsTnRPn0KW03HQ5USJ4Zz4kOUSuU1YuQgGYkn5-DtKT2FSthDAdlA0P5YWmxCwr0wBUEY34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69921fea5c.mp4?token=nGcggSI-RiIy8C1tsQNsQzGVs3lTQPKvVdTTOCvlw4OfVi0NDCpg2XrPwb57v9oJyN7HP77pv1nxTqFWLNvHdNavUpPYmexs2fmKJ7sCrysCqFPx1PSdyiAdgl7AIVAXi6xH9zWOGib8SKm-YUFusvissneLTkIQKkSAmKXpWG2D0Hk8J6sEDEbTPHY5f8s1zEYFyNBNnMkd4AQzGlXkCGn2plYFxlpAzoqKqzPYCabk2Fqqec-T71jXYCTx9kBuk3-J0Csf0L7FoPWn6qFtAxsL5tSjIDfHBJH3hCnfHCW6YLbviNYyMFoBdk09kHOsIYGm_KpPePd6NxSXrRruMa-JL0aoTOEaiVBqwLSqqHFHvfv73h48hKZisw9ADNTVm-h6cMknwEt5D4PvJ6Dh_RbhecMEnB5X4jUZjK6kskyiFsRsUzR9vY-DDTXH8k_DUWBybLgBMRv1Cfo8At8pwe-B_Mmk1N68K6kP5iVYhElA_IXuBMsmrEGHzhcldh9VvOC7_omdMclHNr9VhttMA9Dt9psdhFYGPIyBHgMwz1hJ5ZAlQ2sb2DN4R5fZXMkV2Gf4mfL0tYmaxwod9Dt4RXww0kFKowd_P4f8zsTnRPn0KW03HQ5USJ4Zz4kOUSuU1YuQgGYkn5-DtKT2FSthDAdlA0P5YWmxCwr0wBUEY34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪️
آن طرف چه خبر؟
@rahbari_plus</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449084" target="_blank">📅 03:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449077">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EE7yfEPzCn0Hc0uXG_ZgxmHg0Y2Ev3AJnX0_u_LArKpEwLVrHI5qxbc6sV6Nk1Qyq6cQGOoPcgR4ZXDD5vmePpOK9B1rkhbId-pK0_kb6dcFluZGp1dHpXYVUMxQpah47luIEVL93etso0g0Xq0EpDL9nPcu6kaV-cn3IJpaY_AAV5nOZRn4a4Q_S0OnLOw6b-3Q2ZqEluwM3uvHnvaGr3eawt2mii79ZlOX1G5k6pCKHQUf1-WF4b4parCMk1cjFgVAKSPIsjhjb8hiAjj50Jd4ncA6X7SKTq737cXcLpOBI7GO05Cpmcc0HwgFz1AZVL-IrifznMSrFzosBUhkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTdVSYX0pJad_br5OeezMmiDUMQwJ4nxZizjvQhL7afqBWnUlA-0Nh8a_qlluklkjo7RC1ngxvJDDqsVXx-p8ljMZMxuFJsJvxQJFNCIodYGQbRmLSpAwkIyYdBZwJmT5GVhepqhVe-JNJHgbltW0n77D1M18FGkM5v68SEoxmqnIk8rYcZYFFyazVmiCvz7aFwDuEXZhbVE4JVO3h3tDz91jc7C1g5bsdfHxRxeigARV4mQzelxYnMFM41hlLJ4-bv6Tzzx5jX2YBKt7AUaFhuPwjvyOIk9HS3CWa__ZN0hMUZWvqaWrJDoKcPrGahnczw7wr9keOdVKrzGgCJUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZXeeR8f4HN48DsyRn1u8etaC6ZGQuy-xaJDHOGfr97LJPA9zgt5XIlupk0po4H7KcwdETmzZaMbNGUQyL4vPhuv-PXrYu_BWNKCkETZHTbTi65Zvsu-Vbb7YupqnlBbkaCduLQzrTSL0k6yLO9dRAIlMa0QneFmdRvzC7rfooes8epizMb2J44awfdIn74IL53VTGbhjsqZPZEVs1hbBybHxFgS5nTjvC2xUsp6-eg3h--wUW48YAQ-WfgNoiQOnUBc7gneZ2_Vwsi0lNphxb569EFUifBgSJSh3GYDwfO70Nv6VvpUnk-W8MofspA9E_EOcBLFcBM6clDBeiFnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/msmXpEIfwVvcStJla5cFdjfb-8LgIsn7yeO-rgQGnF_AICruNweEzC2s2JA_eaZCfVQJ6mZHfaiKUupctZMHjKWvAL4F0uhp4H8VRByfEPkxgmRw-WmjWLR1I4vkv8zKGd7s8Th55JhgHzwlygQLb4gsYjc39pF5MCxIvwMptcwRxEaDwUUo5LsSANZbYMw_KWXPDMf9h94_z7b7gnMefyafRpNaAzJZjTQL20mVaVo_cKWQiTIgwvIk6DA58F9Vg1rWRRHFC_V2OEwPGZ7Tl8CYCbysN4jhCK00T7Nokl8rCb8_vhDDOY3cLLX5W0J2-TQOHywhs6b1McdsBBgnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmPkK5z5Cr6qKyCtH13tLDGhH0EQp64sp_BfoWKk4h9WUqtQPrOIckXGTQg4clrowd_bFNI9LJp3zTuwoxPV0MGHGnjJi1OvJ1UtT74goOghgLZYkmypt5utcPpxSGNpuk-jlELzq9yyfe6NHJ5nW0LzXxMJcbPi3gsAsBarMEP7RVQ4j_QPIFV3QttfhW7PptHZ69kpgOZ9Hi--0-ZNIF85-iF41L67wpyLz6o-CHLf1b4SIyzCeeRgNIl-YYJlGKpB5seSl1972vSCzPzPxUH_gQqxoDI0Ic1vOZVQh-TtmuqEN76Y_WALZWMibLNtsV_hsPqebCUoMPV0YGSQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5SZckhCz1RG4uHXVo5EsIIXOpv6qE-kRq9-IdvcTsbichww-sEqLDsCnmzo546v4ZxLKyxe0CRaHT_Kbz0MxCLkhKl8Rsy3Dz6DbGfuyTxREW85Dmj0XleX9YjhW-xmu8wm6vl3Jh4i_vvg0JHqT2SSMXpyjenohu7dZIBg9qHlOeKo5_tD9AIv2v8xTI7Q005HhMH4inJbBl6xiibsz6tXzVNFjjlQQLBiCLFFStRget6FZkSmcFQc_iyjkAc6zB6k45JS2rhhFKpp_GRrLBEbnYefO3n5o0EqXwVwd4_Y91blo-chJFerl0f0a9tydP9TnLnRI7d6QQ-wqKcOJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQGdSGRyLa5vLzfqzpROFFS3QHmRnsdagk-ZTLiQqZt8i_0npme9TGBqkuzb2nFVw-zIgRU0DCoBnYhY8ujdQuc8wJvu-o4zqLhvE8f3m9kxfRTsr_ohJTp0cgoKlLV0Ze2NWYm_DTWjLrDr_LIN4W3eP2E5OzpxCDSTo_h0yVDDhxH6i1ZKKbsZafXG6Yyj1ChcQAq53Qj3vE_ikat4DRWkU1qljXIzvx0qPFL3cXnrECHDShHAe6TFIcGfkbdPIjNq-SH0tPQBtlk2fCLVdtOmQmfdGfLjhilzfrtKNnSNUYeroTpJtXh8grafkaGnksZZqYo07C-nZ7bo7IdZOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت رهبر شهید در حرم امام رضا(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449077" target="_blank">📅 03:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449076">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8la7XxIenlB_X68wBdzgf7oUDcB2JJCYbX2N4xnwJONTksCJzxVM87aLlkH1SZ9fZCpcLDtM7CtwPNUv6w71rQDdGO5Bd_UkhU4jNqdsBlX74UlNBoOYOAA0lb6knNhJQOYYm8v_2p-C6ydvhceQiLr-DaEiDK6LOh4Wd_gOrdDwqN_nKz3-bm_8lgsIDjS4D-9WDa9EQxEFg7qnGpba-VfVIB_Aqqrn247njaE5LJXtcYj1Tu9-nb7QOFF88nhUEdhL05sRXpLZozHfGZB6IXosmhTeaNzYckDiOpdoLfNBr-GR1e_9RPFIN2289TQIpm0ZlQW0Xbg2boImFQt8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله عراق: تشییع حماسی امام خامنه‌ای یک همه‌پرسی در عراق بود
🔹
دبیرکل حزب‌الله عراق: ملت سرافراز عراق در مراسم تاریخی و باشکوه تشییع پیکر امام‌مان هیچ تردیدی باقی نگذاشت و ثابت کرد که ملت مقاومت و جهاد است.
🔹
آن حضور میلیونی، در واقع همه‌پرسی بزرگی بود که در آن مردم اصیل عراق بار دیگر حمایت خود از مقاومت اسلامی و سلاح مقدس آن اعلام و بر آن تأکید کردند.
🔹
از همه رهبران سیاسی و مسئولان دولتی می‌خواهیم که به خواست ملت سرافراز عراق، یعنی ملت مقاومت و جهاد، احترام بگذارند و از همراهی با طرح‌ها و پروژه‌های استکباری یا همسو شدن با برنامه‌ها و اهداف شوم آنها به‌شدت پرهیز کنند.
🔹
همچنین هشدار می‌دهیم که اگر از مسیر درست منحرف شوند، ملت عراق سخن آخر را خواهد گفت و آن زمان، پشیمانی هیچ سودی نخواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449076" target="_blank">📅 02:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449075">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkJAuPTAFH1YlFlS9uGr4UEPWotcfrSxU8kNwBl3mqXnwkjVasrN9rNkxu70rpXC0G0IIQYVa0NpWxYJdnm19y_dsjaSjeLHCmBtDXQlukiYlZJ-iWvr0O5ZBte3NcB2EKAX-wp1Pjs1WAVESJnoXbCC2EVus47QXaZkjB5DfFgXi8w03nxlLho0fukJwtuGAUJjaYyUjcGziRz9hmEoHIPAVR6zM23GjD1n5I69iE3OQRvpkXZ6fg2tenB0OYYCYZkYWWhmAJIY7tshI8j7bpGgOo80rsI5u8rAufT4SNkg-5yGeFSczglbMw-_oVFqLdyvaT16i_B4BC0JQNAL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین جملۀ خصوصی رهبر شهید به یک جانباز
🔹
روی ویلچر، مردی نشسته که راه‌رفتن را سال‌هاست از یاد برده؛ «محمدرضا مرادی»، جانباز سال ۱۳۶۱ که در جنگ تحمیلی هر دو پای خود را جا گذاشته و حالا در شصت سالگی، با چشمانی بارانی و تکیه بر دست‌های کوچک نوه‌اش، برای بدرقۀ فرمانده‌اش آمده است.
🔹
مرادی به خاطره‌ای دور در سال ۱۳۹۵ نقب می‌زند؛ خاطره ای از ملاقات خصوصی جانبازها با رهبر شهید. «بعد از یک ملاقات عمومی با رهبر شهید ایشان خودشان گفتند می‌خواهم بچه‌های جانباز را خصوصی ببینم. آمدند؛ صمیمی و بی‌تکلف. تک‌تک ما را در آغوش گرفتند. با اینکه پا نداشتم، آقا خم شدند و مرا محکم بغل کردند.
وقتی نزدیک گوشم رسیدند، گفتند:..»
🔗
آن روز رهبر انقلاب در گوش این جانباز چه گفتند؟
اینجا
را بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/449075" target="_blank">📅 02:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449074">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9zbBYOHDa2AqgvU0QF90EqEp_vv8hlCBpt2RWP0IS7Gj4871EK9D2YUVEZTDxYFpKVqmD1AOeEl5Hynv_emU6Je0_HRxJaysX8B6QbbyaCRuBusoN6P3ZrRhKncU-jwObpR0uW3URSGspv4TKOdmTr-8a7qCXVEDG_hq8Vbbwm_lLZyWPqngklSMMYqI83h7rgRRcoSqSGU_qVV9NGkJhihZnrpgN545KsbAncI36ZhfEinInHxlI7Gao4A2Q2-pcz5IQfysiYXaeejKxbgyrAN6fF2QthM1HHxy7SQf-d9O17gB89mwIqpr7qNEKmOXksF0jtaoz6O7CnKrmdqng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیۀ اروپا: اعتیادآور بودن اینستاگرام برای متا گران تمام می‌شود
🔹
اتحادیۀ اروپا به متا هشدار داد درصورت تغییر ندادن قابلیت‌های اعتیادآور اینستاگرام و فیسبوک، با جریمه‌های سنگین روبه‌رو خواهد شد.
🔹
رگولاتورهای اروپایی معتقدند قابلیت‌هایی مانند پیشنهادهای شخصی‌سازی‌شده، پخش خودکار و اسکرول بی‌نهایت کاربران، به‌ویژه نوجوانان را برای مدت طولانی درگیر محتوا نگه می‌دارد و می‌تواند به استفاده افراطی و اعتیادآور از این پلتفرم‌ها منجر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/449074" target="_blank">📅 02:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449073">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
حملۀ هوایی رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری از حملۀ جنگنده‌های اسرائیلی به مناطقی از جنوب لبنان گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449073" target="_blank">📅 01:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449064">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDPGzE4NcoC2bDXcABmye2SX3mg8ca3Lqob8cS631N2lRDk8U7EKLc0cFA1jcUudo7c8K0JE_ypvpPbWkg2kP06TR6MFvGV4rhUFghnenwtZcursBDVw6Igs-4yKU7rispiQkahfNxIK5HXmaopdR5P5JIvZpznl8Ktc3vACzjVudwgFacGDSBcvVhA36LybXOPWP91INk_WGsmUbdtZMHK3lh7hg1UlCClASYaCq6uUwTCVJWYj0uVMajU22BZ3CUMiJCFB02wqDKLbH5HZOIYr1WKLfPUjlJ488AD6svR1b9HUMk_vdXvHAzYEpOfSgb1Gr5XCoZXFcUrN_v2raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDE-JRw35teD_4auOZMGp9Bslys-pyAMRdgNdqqfrIyRvtX3Ldjde_rhiARe4Ozl2llCyv_A3Kd4P2lqjszpiSK5-Lg_h376YLoKQlDjmBBzvj2VGed2k_T4ZI0L8fzjfH6YNTd6wtz9OrCCZPta5mXSkncwGsmQTObREUjl939s7VKfF7eWzokrgJXULDWFhj9eG_esGRF2wN-8bKvpbFuXTPKHQCIrwmiTDzPPZQKoV4r9fdnL_k3rJqyxflyK5lZewXouQMEZu7DKEg1U5cfpnE5H8wnV0XWZZP24CmocK7wKMP7Svskgvz1sFyFV25pMVEgsHgzrarRd5V04yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riI2UK-GZgw8dnwNYo5ljPUql9GlWWYf7EQUhUkKLyDwe9BMxZooocLzvK6imJrwdVdqd7UXAVhbW4QkR6RRf5k71-7oYSo52Xf_bc71-pjKdwXhZznk--5rXjepFvVO-BAyJ4XWIjX2UqRjHzxOtM3IiCGqlhUFE8bwUJCVw3cT1YIDua_bQMsVa5_5W1vqhq8ZrgI4XZOGy_OQkzTPW1k5sz3Qde5wsog7pVR7r_PRnPOKWo3rV2ycZYboK3z26mqqdK5d8NNKCUg9izdPFf8lA42p_mxKX-K2mEbuuG8A5ZYuAKxPMSAg4z-7mNyWMJkeT0FNoijap8vBMsasCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjjHw-UJdgiI9I2kx7zY2lym9Kdzfjk9pH4uQcydkwXXuuBRTHMI7ZQNwM3TdBukvvVG9yhI4dRvcgIVrFKHASZdRBZ4yEz9_XpzPLAiDwYTKEvVyKfMfylgto794JaIW0nNSJazyHLdJwAKl7G6eJpZf46POzI7CtgUlAloULYek2SUEjBG9676umuT3Y1gLiVPnpVDAQe7WQqQVddG5wuD9fEl6EmwD1_8OWV0CDQAWg4oB5hwDJpbeKC_XnkckITT-cs_XJqnifHFhJYs9mrw00jPh55qZsOAnoiR3TFMevViB8ed5Y4kohhtWs6-HFRi4GaH05vFqSFbeU68DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTiqOKw9VVE_yn09QGFkNgcXwahKRKUafJGkvVie4WD4Qyt4jYY0dLS68doxgFFdFJUk9JqzF_UvrHHvUq6on4WdxPg8dAke-TkTrVzfU_zMw1ifbzXjaY2gF5J2BFjXmB4irt79lhDhYk4LcwWP8UfqZVSRxwCF7WiBHPnPjmC_ju-eUxcNZR0CeQzw33eXkJV7nrZ_1K6-_DXxRiU9yYCJvwHBnKWGTCtxR2vVoUTpaFEYgzSRM1YfFK-QWAqyqK2ysTJm_eW8h7nkFybyTzxch0Gla3SDsJXVci1XgHgJLi9uYy-WisDNqQ-DdeYjNwposmow25hRbB5Tfrx2Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RL5_nukWlnO6Y-_T7OAcztSR8IJCH3Ipbj2K23_dWC6FPdO7mVp6TVq_r8Wc2iA_JBd6SIWFhUJOAl180pLBiyyRI3u5i_HKvwbwX7DtE31XNSmdnuMsfsRh-FWNxC5Xf0sHFnUxh4FaXeOeYuQl00kSvV6tBSrg1KE0ENMX4CYed6bQusI7Sk-42MJgoSfWVifg8_CsJFnC2CEW-VyyrucT5dCKsMYRYnTei2Tpn7HHiz_DtpuJJEB2T81LEngiuipXCq-ptsfSJWyfun1SrkNXd_fYMwJLerMUxoT134_xKWj70ZOfBfqiPmWCoM-p885UBRMOJ5qnwKLk75PNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/McXhIioZaGQ9q8G0-diqz3LI6cRL_x4tESJnHd3ghXo-KThWlXnNdEvgp4U6Jg80NGiGaY7maXs37Oxs-t2ZA4drcAwoa82CnuLxyON5g7IyjuvQ2HVoHds1tiEeJp_vMlZRNcPXEj2L_r0yyZTUUSnTKMULP_v1YA7_6-J--Nqcuyqsk_tYrTYPpKqN40wDQsXeZXqZF-U_wYa6eJ7iQA-Zmu4WfJC5CEaVEHpH9el3pAwfQOAUyKR89mpVzFjQXi8hAWj0qz8hosVwXPncF11ZARaP6K1CybXJ4bHXc4dCRKY0JpxlnHCGrrDQDkZTc-MsXqIpBnSpBwNEWFwtTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H76NEonCKAO_VXpUXfvyUsbl867HNYNuiaHNfddU6oN2CdwsCjW78U-JC2QPor_CVpquhIyFOGwzRqL7aBJbnuj9wDXSg6N-3yab_wRO_oDVLpy50zfteHkNu3Ivv4zZy9b-6UMwwG-nErwJFdlfKWUbgedn8_B7VUoV5n2Rr_S6KTrS5XKg84ZM5TNGbPEX0E0Bq4BUM9Jshc6LJ78KvhxNnCeThbz_B01uQ8sjzo-BXW-KXyzoa3Tt-SapPdMgVFgCOF6zAERowpbWd8oU009McMT9sj6HbyOLBXt7Gc6qA8cWyJWiOe6XQUtyecBlehTd-51_GTYEcSDCFzXWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iopwe5y7uziMlwFNpxwHWKDBPFzmaLpfNx0RSYy_VrSZaPzOG-fkIP9lWMX43SCbQ-fNZWUMAgofo37pDVy8w3xi7QCe_Y9yF-jHNDrEKTr9qXWNUYEN8Bdh6o-xtPsXE_au3PpI0c6rY1VmC8AoPeG7kCVbgr7DvLVFssFvkciGolOaIUa_MsArxMQzemuO4pgnmYOv_mtMGUqc1oBAekf9nyFwfHrdl3qHJo4yHAnMLeD3_r6aT63Z-she95MgMOh9F0JUh1_nmLXZyBgzcsinxL3y_k_LbQ3vwDacBrKlaNUEz-kxz7unng7NZCw6g2jG2pP71k90TZwQv5zIwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای مزار مطهر رهبر شهید انقلاب در رواق دارالذکر حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/449064" target="_blank">📅 01:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449063">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f04c77390.mp4?token=BXJZdtw8P58M_cvlV5eRN9HpU8sNjRhaP0i96_C0ko-5z-h-n6KNNLNwEn0E-WaO2lY6MwvK4ZYQ_ThXvmR-6EYaL_Ias8I2ASRYvJYmHah5Y-rzb4c99OFG2DF-66cA9h6qPUluDGj7HE9fwvFdH-wsTGFepwKC00CZK7bEniAhyWGD1_59ek6Foh_MNox2A_U2rUbdeayAiotfI7jyOOgBHzI8D_5Gu8iaGp3JLsHeQytNpkM58nh5-rQyuEhmd4WLR2FG_ihD4VdGSoM4mKr67rS8pWxHmrx4xAexaA0QCVtHvZp15jewBGeBg56WvtTNTxkZg1scN2XDczfX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f04c77390.mp4?token=BXJZdtw8P58M_cvlV5eRN9HpU8sNjRhaP0i96_C0ko-5z-h-n6KNNLNwEn0E-WaO2lY6MwvK4ZYQ_ThXvmR-6EYaL_Ias8I2ASRYvJYmHah5Y-rzb4c99OFG2DF-66cA9h6qPUluDGj7HE9fwvFdH-wsTGFepwKC00CZK7bEniAhyWGD1_59ek6Foh_MNox2A_U2rUbdeayAiotfI7jyOOgBHzI8D_5Gu8iaGp3JLsHeQytNpkM58nh5-rQyuEhmd4WLR2FG_ihD4VdGSoM4mKr67rS8pWxHmrx4xAexaA0QCVtHvZp15jewBGeBg56WvtTNTxkZg1scN2XDczfX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی قمی‌ها به شب ۱۳۲ رسید
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/449063" target="_blank">📅 01:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449062">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نگرانی هم‌حزبی‌های ترامپ از تنش‌‌آفرینی‌های او با ایران
🔹
اقدامات و اظهارات تنش‌آفرین ترامپ، دربارۀ ایران نگرانی‌های هم‌حزبی‌های او را به‌همراه داشته است.
🔹
رسانه‌های آمریکا گزارش داده‌اند که اعضای حزب جمهوری‌خواه واهمه دارند که ترک میز مذاکره و بازگشت به درگیری‌ها با ایران می‌تواند به افزایش سرسام‌آور قیمت بنزین شده و ضربۀ نهایی را به این حزب در انتخابات میان‌دوره‌ای کنگره وارد کند.
🔹
یک نماینده جمهوری‌خواه در کنگرۀ آمریکا که اشاره‌ای به نام او نشده گفته که تداوم جنگ با ایران نه‌تنها قیمت نفت را بالا می‌برد، بلکه «ضربۀ مهلکی به ادعای مدیریت و کفایت کلی دولت ترامپ» وارد خواهد کرد.
🔹
او در ادامه پرسید: «منظورم این است که ترامپ واقعاً دارد چه کار می‌کند؟ چرا اوضاع این‌قدر بد پیش می‌رود؟ و آیا اصلاً نقشه مشخصی برای بیرون آمدن از این وضعیت وجود دارد؟»
🔹
یک نمایندۀ دیگر جمهوری‌خواه نیز که خواست نامش فاش نشود نیز گفت: «واضح است که آرزوی همۀ ما پایان سریع این جنگ است.»
🔹
او تاکید کرد که از سرگیری درگیری‌ها آسیب سیاسی جدی به حزب وارد خواهد کرد: «اکثریت ما در کنگره، به خصوص جمهوری‌خواهان، نیاز داریم که او هر چه زودتر کار را تمام کند. این وضعیت از نظر سیاسی آسیب‌رسان است.»
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/449062" target="_blank">📅 01:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449061">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حملۀ پهپادی رژیم صهیونیستی به خانه‌های مسکونی در غزه
🔹
المیادین: پهپادهای اسرائیلی به‌شدت به سمت خانه‌های شهروندان در محله‌های الشجاعیه و الطفاح در شرق شهر غزه شلیک کردند.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/449061" target="_blank">📅 01:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449059">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1pg1V67FEltxUFkoYYXBkahwPWek3OM_Ruwo9OYNea9LyXMIqChq25KOfKfFOgHJQKBqHA8K_ZKvmthYldVu6b4Zuq6B-FQi1Xk5ad5rRlHc8g4RIBpmwlfGUljMGueaZUf-57bI-qF_h9QRGj66k9mHG3lZhWuSpH4AQsz5juaExkK9yxSUNZZJjXxKtLf2OAyqd2C5SjBINctf1kGIUmH5ioMb_zI173IyO48hsT5rZWGJpQVDnYS-hISjy7bKviDDckIizMoifRMYTpTt0aqenS_p3i5hr9M0JOFalc6tF42JHsn7SJdJnTsF061jBI-bkQkcaA9YXBrrYGbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش معاون وزارت خارجه به نقش امارات در تجاوز آمریکا به ایران
🔹
غریب‌آبادی: وزارت بازرگانی آمریکا سند جدیدی را منتشر کرده: تسهیل مقررات کنترل صادرات و ارتقای جایگاه صادراتی به امارات به پاس حمایت آن از تجاوز نظامی علیه ایران.
🔹
این اعتراف رسمی واشنگتن و سند رسوایی ابوظبی، مسئولیت بین‌المللی و آثار حقوقی مستقیمی دارد. امارات عربی متحده باید پاسخگو باشد.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/449059" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449050">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ljAL-GKNmUv7qYNDRY2NgbNVT3lGRk1fX81KJ1c8imPyqxeA0zF4L9752RBgnJiQTRMWkPTryjZ0s7jdQh7vfPsl0ahKOvWGUNKuZp-2_uvD8KJhoksl9Ow4QFNr-ejFoVp7__Eli5PxVs65HKiHs5j4shUKL2JPxy-cYBIeLbpfHs2ug98ORQeHUww1o4ctM1wVboqsPG32JIyOJYMljtwA_vV6jcIdEDbirQlBu7k9CyMOQuQCdJhPzSRjrK1XkNw1gPTRiKwLx5iVfjRvmg3Gdcv_NqRFHzplAprB5wJOkUKF4TB1McT2nvJERKOWd3MyV8prov20JVhYiS7z0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRaggFBeaFhUYVjNOtu3O6PbnlZiJ4JPa0DHiVa3FrbEQyvdzb0bkEWSrcn0R2Vfh-nsaNyqgOeqZnc_rtcsiUqgPyxeHTeEvaeqb3oVj4Jl0pe7L3CFA2HMY_QaqtaLWhX185cFW-VA7fgDjlrB_Pj4FKWjAsVX2ore3v2OghRIXWOnVe3U_-k1k-8_xANFhctvfrW86KZtzF6xtEkmYqCCZrlWaPX5pjK_fQ4xQIHQ1JjnlOumRYHXYStBWbVOb8chi3cWu_motz2IhI3aDAj8Jylu2ORcmO0QzesO-ydM1FAdXBLVN5DIpFlJondg4F5zZuTZDBAjy5D_euu86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOcDlfccc9t1ulVHBInSTt6b-Q0AI3Bh0S7b6_r_xH-YSaTTFVTkl_KDVcbxccEnZdXn5gPAeQ2KThXQp7eK4D6GmuXNwuSOCKo7l8TW1oYdAqftEOdprmYi1LvDNGKb7hLCNzga1EDZTysuDHDFkVyAOQe8Ur-3JI6kpSPLxSTv0N3nZZfc_Cd2uO4N_vdC74t9Ecjw0-Ab8PTo1xlYjdvKriqtGIcVFhOIlz9Q2CRhgdnyDa2eFXKQ7IiikxaaWuC3qi1H3R9QOg1CxccB5w3okb3MtF0t9Wo-Nl59tkk6Mtl8crMMZhLPxQlOp_eFirxwoyeEya5F5dUVKrj6dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUFB00EhWtS1a2xJ1P8mrmBOhBfMMcmht3w8fBdfqfzXtB7khcfLfKwRQM2o7wTAq65qyAS0fJ8sx9SG50CvhU4_EhlO4o3W2RuiTKADzI7YuGm-IETm3B3vhfVy5jRPh8A3R8NF5qFmQgmW6Ec1xRDJ-vgO8ngSkW_GivL-wjOIbgSxAgQxZozyeVSCEpvcECJLK-D-LFiTC7eBB414z4rtd0a1fjqpipoik57bsOvzKu9YSC9Hj9yT4WlJsksa3zloM2l-p6otb400ytzm5x1ew0pTKO30Eurgq3NWFcwgjJlDA9tNbELZ9v49VRkY-fnw9op4ckTmJu0x_0bf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXRpFTmZtsp1Zix2Na-RVzb9idzo4xwBc3ahhFjq8znKkj8ucX2d4dv_1jcE2_25E2DN0QUcq_ZBBNHwPaD8KmQzszz-kRaUAgm-q-gC_NcYS1PXi7YXHyODVmEjHCKzWIyLfAV7UikywUVShVkBUowF0DWfrBx7xb2xa079XVREmhEOiRIxMcZEV_8-H8dF28iI0wV0SV0lSvYI6xCQKn9WwPkPHNPj8ZfMhwtc99KwMAkEIaOTOvqKu1QRnIkutAvS4qOT031ZdpOiobIi1XUCO0cCC53ibqKrDN3OreMTfcW9H5Fmlq34HmpCjHV3qpYF8lNnYm7L8Kj7raAqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlCRQHgRC7C77-Myl_v6uZoXz4XoFWdVU7ytqdAhDSuApg8rFDLsQVidRV7nUcsk3SYSJrvKYnJPHab93PCy-KlO9-tAGlZH29b8QbrVtWPPoroYMSos7jRJw3W1KepT10yHPslqd38a3wHjH9UtzOO8myfufA529_XQiuH5_0EDGXZShHHAOdfq4V2y6B26Mg1H2X5UnqB98T2FG6omcbENa1Do6g63D5Qn8AnTS5MetOzFoi06rpPTcqw6T9Gu2ZygkOpzZFbO0VKVIe8zWwxyMC8sro5_aa9tVr_qkbg8h0SACf1-wigcqKwb0HVWkQI-mtZBzoyb5PsAnTOLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nzzn1EXXe8cuJbgUsDB7of-8jRZNkql7X5TE-yqhNVglb6PFqSRgX0Q7McvEYqMd8eJCj9cPlCMUQ4AjMO-lWjy-KIWcQpl6oHA3R1UHBLbGgibeOY7uMYDetjAOGuPAAe24FlE94-X7VelozmQgw6SGRf10QStInPmgoWFX-sDLQGWFmShrd14VFfScklDhdcTA0IwjgpiO1dxp2bH6iwyq4o2h5IP5Hij_knXMz2xmAYE1NndwLsEZv8frAVMecNDrfHd4iZZUjEKOUU67b8uWK-04CpNeMELMdAcNI87RQ1NFIUJSkM_Ot4Cq7ZssxJ9ADp2NY36rA4_vKvqMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3RjtoHNyx8-fpfKWdOhPWRNDZdDgTiVQpyLvnrjj97TS0iOnd-F7BIpBThTnykGiIM9fYYfHkE_EwzSNohikEeQZuCj1DScP6wp_ssxWdVPd6ufr6lHV9jzneaegP21dyR8FC04r1vQVqcWcNGajt-lU29hzYrVqH4r8wjSeXjQ7eTxSN_1ceXzLlIrWShFuQB1Zi5Q_vGT_amQk8vh07drMETUvadRrJfXJCDL8SLGYoFwtaVl7APhfgDtttLComLpNHlqnzOPE_F7fVUAQsALM_1p0k4lYxnZBUcbxRShigD-PE3wmHP05lUdv8CrwBA8WocI6s7y8dStRKwc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoSfux0N0KbMWqeSq4H26HPq97lVlztCw16OMKhwt918kLOygys4BL4zLdogJF-sg0qHkOkkOI2zbp4xSPodDqX-DZSSBnGV7QtopM89M84roQuv_VBeql160kJbe7qL92HHV5iFYz2gtPp0yVOHbylzyTViV0ccF7s14x15JB-P1E0l7APsHytHnYiKqXhLQy0ggeddXacqi0HnhZQb0Z48lyATyZfDD0tjrAfvqEdihWZ7F-auHF0vhZeNWN3x6pg60NOkAoSSJmecc7fgfEjBwT_cjh6lIed_RNKD0-X5TdHhZlOiQitHA8L3BOzMg9PEQKSVlThe05nZBdVwcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شام‌غریبان امام شهید در بوشهر
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/449050" target="_blank">📅 00:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449045">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwNQdsoVnXdl8Hvi3ukUXWF0oXLIYZ50Ny6PzNq3yw_qptfM9iQamKDo63jfJZaX8OvTPVgV0gGP047vHLq44ticiNeue6zpFff-e3dT7b5UQbY2dJ9qoGBJPDDDUlLxsOq53SRmoxVUpoTfTLVoVLe0naFU49x3IR7DwB8pgEN4Hg7jajg5OmUxjt7w6AbAh1FCfUk2Iaima48sLTDR1CC2rlZDF6omtNF0ZDng7f2a9aZ6pMrRo9DCvfBKN-hfCdfNqv8ZtUsv2d0OMDy_uaRyEe93IOKq5Vp7JI9nCyllCxy75HRIPUFklIXeQ7Dnpd-Pf3R23ZWDFe1xLJrv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LF1HW5ZQyMONu5Q6-9nHCK-_2o8MUXmnz1Fb5DDNrMqSyB1xTXCXIyhXyTyUxbI3q674ym2E-OPGrY0YXvGEHj7JR8zTRV59bT17pd5WqaNBUbfYiqW8NZoWORFnvmCpt-Mhk7wYA19nyjmFy0WoiACOeFCWVCeDfPG7UqMclxpUxCsFcXUilA94EaZYdRGsLthyuqaBDPSxPEqkPKppYriY6IzuBavCJNNYc7yF6cceCpPdoRWQlXP4eMtgksIPyVkJYJObw3kicWMU-R-uFUXHms89P6RbON5XgacPZvPLOnL6OJe4yBbwRonDSdF3A8INkHjD54PhbRQsKUcQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQS468UF7A9ztv7Jl_0WWlaUcrsOtka3lVXFjP7uB6wOnFilUjo0rGAtWdaYtQEZdfFA_t6XAAGAymRyrp-A1Baw_s3eprpqc8DrP56_qcggar5evvQQnLJg6YP-vEDFBeN5poXXUdDdhW83PmFZaraWVvD3KB2z8ZQ5b3JDXiBY-HMacxO3dkPuXIV74JqFiJfc-mqmvipVzkz29aMBCxL5mRjfFsLqNKt72F05QN1eFriOADQ1C8qmxTwwTCgWRUGJCps2ZMPKFc0G-HjL99WQVnC6OzhYix63E_CU_ixjGOXc7WTzHNluFZIbNQwrdO7S2kFnFLxevG7wH868Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQG4giGrPze9Q2ivSFA8t4fiFyCoVpIRcD3XQJfcNzi5zaiYUgPv6zWek-kCQ_MO59Id2-1n_Bl_1DSpb1fX0X1lG0SLjON9wJkGv7L6Jltho7_ppTwr6aGQvhmqOHcgwtSzxDA3gGHfSuBDPCqsFmYgWOd_S4zXVS61w6_FiXoZimuFWU1nKtNnf-6HSjOP6JKNkzDosKHmfd3yZ30BWbyQVvQFblO1uJcd4uVbQZUP5TyIuaXGBVbigR_wMJOZADvM0_IuU9srN-KAs1vIU0miseFviK9fGBxgdMI6aoRA-I7uFkoTvhATRmHHPCnpJp4c3F-TYokoKyBjuCqTmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lt1ZeCd16wnPP2gedl3cuc4g7LRGEaiq_Yegth1sHJdOGUByP4ap5KkyFOOUw0RJOQyuVOfhNnYPhD0-8hvzUNkAkmkzQoNAuh7NUowxvIwXiUHVNu4fMDCb83EnvLLk2--00eHgzSH7ro7eOMFyRiv_r8WGAwH2g26m4fGM6svXOs8He54hhM1TwzwK6kRazNSnjE9BUBGlxbYePqCyoZH7whoxbl6HTxKuElrEeg7AfvGWOw-YIGi9bKm37UWLdNjRH1y21_WZogNBEQMbVEe7UCV_6aJe9XFaGKT3eTBSYN6PuOhSkfxlhBsGsDPI35c44QwNdNS6q0uye1747g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۰ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449045" target="_blank">📅 00:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449038">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlLuHnzGzbud3eGUWyjK1ZutDYJ6lu2dWCby78Cl6l-GEh91pE-vCceYRJLULuo3QtGY41KWjTpJnP6hxT68mScwfSnWWaOBLwHbBEmqN8zNgYQ4TUMpEddQ8Gc1opf9O4hnhWW4q_2lDf5xJd0U9du46Ih2aI-jr3QPwcoRfak4s29Mm_jxIEVOixrWRCsw85yqn-tcey_Q404zZW1OdhzVnf-5IClp0SmNUYnw0JA_KT9rl3OFCAc3IVKuFc0sTM1ww07Wj5RBVvCa7YIscfLohrGOxbfABd9FbiBgxbYggV3u3U0xdS3QLHDvMy97ppQbqvW0gXeisOf5TMr3KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oF0TCklrMpLD2RJMCh-FS6S69rtMYD4XMQ5-UrJRwIMAjRlEyb9j7ppReyl723tG_hqGhBT9d-POoCbnbl4vOZPTySpBq6f1NV4yW4BCvL50JIimLI92T2RTSnLqHhkDk7FjtHO2mH2dKttsU-8k8YP2DkfPT7LhHPqmrVuPBCJadi_l3CoztQuXPT2EB172obgDY9jAyyaC8LBgdSbyMc_0cUitXHX3_ymbnH_pS_B9glciKNZWGl9lG7HNSWQiju5EMitOfRPE0-PlJdpHWf-uDHjFXCZ16Yzh4KoEKzPZojE85MrDv7GduJhPFaqk85AMIqklS322_DKoeoE2nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Js4xYb9EnbvFNtQNM0D5XZ9AdXKPWBsyvC8yHjFTsctbrkPeQG9RR65XC1Vd7Lj6rc4mU-mxJkUTRx6WIV49ucwmRoON-ncED5a55JKd77GS5JTsuPtH4usHk0JL7hrAk4UockJwfXTvijsLaI-agwZPXUW-36qnEgcSXdNM5DETFPuXPlItrZWlQzI9-VIAAjxw52RGykMCPg3RythUowVzFhobiOvHzd7_vggInqVcj8JCZ3tQ05gTwN51euHh7PScdk7Z-Eq3XzuUXnx6M-02A36FhHhoPNhpJfcNODRYCTzTLLgo5m_vBbq88zi4E1pLR4xfnvjeQeCZcxlu0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WwRR71ILW6B331Zql-CKGCDkn8AyP-2sSRRWI0fhc7gEP7HByRS7JZAP_kHEiLZ3w2CkDR3lwX8zqRD1DnjlgWmFhCq_cM8cpgfbU17xrOQ3lYsWgwdKJYXvmkawee88tT2S0flgije8y-ZYRKVAgblajZhxzf2rH5QbB05rB7jwToiJLmApkJr8tZo6sO16HVKfHKXRozgyS9xmgUiO6zkxYRMZrKQsD5CC4DspN5Xk8ABiAsf9T9KgZb2wSt9ZL1NbojCO07ZvG3BsjIcMyDJ5KN58C2Zm3DBOeaJVHshvrKIhovyP3kHebvueGQEFgAQB4W-3pLEIeHDFMUIHiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfoHXJU128k23aAx5CMdUeBKE6KBm9XZVvLInKQ9MeGlGujTSYoJAd7hkOA0hu6_Q-B_4J3nyFYDqz70qDCH0Ei0VoM3mEx8WNhLC_vxaRURk5AsRL1BdKAnCwB97AeXhz1p9kw2OoiFnm1gB9nNWQT6xojR_CO4TvIgOFQ2nBNab2XTkzMZY6Vmg4eLwGVOxhNoTQeJHBpk_v0uK-z-5W_Hu3p4K5ZlFgJ00XE9fMsQRC-JgXiFmn70x1PyutVE8iQLoJAzCKzkAszjMxsUkVSuKsOA53qqVGx5yEfWpvIPE56HIPQlO3QyFL7xZ9R_n0eOJPo9L2OlVScf3pKHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-EdKNmNpgcdvzk1ArrUaWCuYzLCthLYki8YkOAYGTzpAvFxghM87u-g1FnCeALlKW8e4PyZHCIqi6U93lkWl5Q5tBVmNkg7jxbVEPRTgRcnuNMM8kye40sAbqqYbbKyse07eK2VpyNhDytEuWLuiX_GJB0oXlZgWw2ROWZVolD2tSwT0sdfblVfywwQ_2cdJri0C0aY8LUMihP4DSS6OmNI5PBqHuR6fdKilByF8aSNv8kKwWT20VWdtQ_dmonz_9eDHfZfcvDeQow8lYFDtSdeJ1vIH_7_O9-OoVuJNOW0b6HjTpnwBO7OU4XAPIRG1PLbOxO7fTKfaKqMayQHMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnvntUi8R7koTRaDjwDXuibE5m9epqeTauGKQNua-k4q157GDU9jkdUU8RX9Yn0OC9m9fag8Yuz_oGIEBjZC4pdhRMMdx9z0jf8nLYOigMnbHPBgZVRt5tz8_rMFSgPpSWlYoSdQKc_7CzP3hOyBB5LrV0O__e_vhdklC4v_0pMtZgGaPC-044E36MC5obPOIhdlpHOugZz-dQorm6nPXXjd9WnrDyjbM2adh6Mthkw-LCowICy00SrkZhuLQtu2YlwT1hhBkPuMxa4Eex1hjyqWeH_xM8g7cbI6l-vBaoW6AfEFoYjo5qHN6qjnUUl3um8WbzvGtfpOirOTEMoCGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449038" target="_blank">📅 00:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449037">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKuA2xXhPp81YtfFv_ktnpHUP4GEQ3stBbWS5mVsoSns-2ivWmOUuDSnvkWe56JVS0YpCt8OxrN2xp6hYLA_3ftg2BoWOO1Qi7C0Cmb5tbjhytxhZ55BZViR890Mzq6BhbSop4opOh33ATRKUfcY9On4o4Er4ODMuvbySjdsn2xwYDyGR2FiN97c-1KdTW1NUf7WAY6ZJUsSY46GvFwEUj82AysngkHaNfH7s7J2VsC9PNAeiWCWJD1RYGlnsfh0YYTsQZOSnqbJA0vAeSoVOfCDNuiK1g7sFqVmcmx0WkogrOTb9R2SnTAvvxAbg6_Zsj_x68fwweCJkDFlpcs63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلجی: تشییع ده‌ها میلیونی، پایگاه مردمی ایران در منطقه را به نمایش گذاشت
🔹
رئیس شورای اطلاع‌رسانی دولت سیزدهم: حضور مردم، چه در شب‌های حضور میدانی و چه در مراسم تشییع گستردۀ تهران، قم، مشهد و به‌ویژه عراق، پیام روشنی از ثبات جمهوری اسلامی و استمرار این مسیر با قدرت بیشتر دارد.
🔹
آمریکایی‌ها، صهیونیست‌ها و تحلیلگران جهان این واقعیت را درک کرده‌اند که ایران نه‌تنها تضعیف نشده، بلکه با اتکا به پشتوانۀ مردمی، قدرتمندتر از گذشته به مسیر خود ادامه می‌دهد.
🔹
این حضور گسترده، علاوه بر نمایش ثبات و استمرار انقلاب، بیانگر پایگاه مردمی جمهوری اسلامی نه‌تنها در داخل ایران، بلکه در سراسر منطقه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/449037" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449036">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEAIVrm7Fe3S1hfhOJQJoHMlnkjx3GZV7KxfBDH9QoH6o_uhl28htL3BbDTsk6U7kqM9AXt-uwC3JXT_uZZohmo4-sqheJsw10HVreio_ZKsKykVxIgLYwltQzkOFdX_q6Jqsa5xgWVHGs2xaGA6B0x--1VwvZ_LwrwARRSqvVkdHvl-K0Bbj4_yG6GHCqwhpQ5fNlevd6Ws8fbmCgQ2sDJM763OVaQXRySnBqil9CcoQW2TIGxCjUqiLpPJWXqm2-ztXwnjopeJjTeTpdsJekUuqBKibDDnYTeweg_jKtC8GgNoUsUkeI0Qrngx5yJB8N3uViZNP6BFaylz5GRD6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل دوم اسپانیا در دقیقه ۸۸
⚽️
اسپانیا ۲ - ۱ بلژیک @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449036" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449035">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de99893385.mp4?token=DaRILPOLFnAf2codxLkj8l-khDCnKZSwixIuLZwSE2o7jhyWwnxREKHTGlY9DJmoGwM9g1ic1KRLZHic4fJ9ebhBxWSEZXLrX213R3-VJGLwJz1FPR7RjwR44qxO2HKq9KWQ8bNt2V0y2GVihl932r0St5t2SqBY-jYT2l3qCt6JMRAmzVMI7iWNwd0sJshCZPSfrpc9wFtKdJs5DMYVUXnFChoiM3DJWprJp4ymF_UTg_sUhy2m3n7kCUgFOl0x4LQStKCyTJaPvIX8mava19yQ8EKBCMnB67Uh32mWfmALZ-7hkty3W9SW1koao9G9uXr4kKnVumBvs3ewGerIHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de99893385.mp4?token=DaRILPOLFnAf2codxLkj8l-khDCnKZSwixIuLZwSE2o7jhyWwnxREKHTGlY9DJmoGwM9g1ic1KRLZHic4fJ9ebhBxWSEZXLrX213R3-VJGLwJz1FPR7RjwR44qxO2HKq9KWQ8bNt2V0y2GVihl932r0St5t2SqBY-jYT2l3qCt6JMRAmzVMI7iWNwd0sJshCZPSfrpc9wFtKdJs5DMYVUXnFChoiM3DJWprJp4ymF_UTg_sUhy2m3n7kCUgFOl0x4LQStKCyTJaPvIX8mava19yQ8EKBCMnB67Uh32mWfmALZ-7hkty3W9SW1koao9G9uXr4kKnVumBvs3ewGerIHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرانجام دروازه اسپانیا در دقیقه ۴۱ باز شد
⚽️
اسپانیا ۱ - ۱ بلژیک @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449035" target="_blank">📅 00:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449034">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تصادف ۲ اتوبوس حامل زائران عراقی در محور سبزوار
🔹
اورژانس سبزوار: برخورد دو دستگاه اتوبوس با یکدیگر منجر به مصدومیت ۱۲ نفر شد که ۱۰ مصدوم در محل حادثه سرپایی درمان و ۲ نفر نیز به بیمارستان منتقل شدند.
🔹
اتوبوس حادثه دیده مربوط به زائران عراقی مراسم تشییع رهبر شهید بود که بعد از این حادثه، به موکب نماز جمعه جهت تکریم اعزام شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/449034" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449033">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53005e601.mp4?token=RI8WIRQD4-kkAXElZRZBYXZ8-jhDqKCCE6-w0RqTMl3VLBrI-uKUl4bQQn1W8IHLrYeowx_tyo448bHkp3MIxhrXgpopOtxbwWFqO9SrnSHet7Q6j2u9Jti1EMXU3VMqXw3YutqUMW2esPuUGbLIsdiGQ2i3zq9pQtDDsqpgzf3Gs0DJ-LMeh9Cjwln_3ZA4ttuDXYZJNSu13mqqaGXm7SAwj195SGkOl_LQ3wsKuCWxTUVqyFy_UQkCLi5yp43kjNLR13dVxSL7XaaaqK994Em51ofU7IJhVoZXalDnODeIcBv7tVcBRLN6mK2oTSuqyIla86b3M55XFcsnGV6mKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53005e601.mp4?token=RI8WIRQD4-kkAXElZRZBYXZ8-jhDqKCCE6-w0RqTMl3VLBrI-uKUl4bQQn1W8IHLrYeowx_tyo448bHkp3MIxhrXgpopOtxbwWFqO9SrnSHet7Q6j2u9Jti1EMXU3VMqXw3YutqUMW2esPuUGbLIsdiGQ2i3zq9pQtDDsqpgzf3Gs0DJ-LMeh9Cjwln_3ZA4ttuDXYZJNSu13mqqaGXm7SAwj195SGkOl_LQ3wsKuCWxTUVqyFy_UQkCLi5yp43kjNLR13dVxSL7XaaaqK994Em51ofU7IJhVoZXalDnODeIcBv7tVcBRLN6mK2oTSuqyIla86b3M55XFcsnGV6mKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلیلی: معیشت بدون امنیت و دفاع از حاکمیت کشور به‌دست نمی‌آید
🔹
قراردادن خط خون‌خواهی مقابل معیشت، نوعی تحجر است؛ تحجر یعنی شما یک پاسخی برای یک سوالی داشته باشید و اگر ۱۰ بار تجربه نشان داد که پاسخ‌تان غلط است بازهم آن را تکرار کنید.  @Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/449033" target="_blank">📅 00:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449032">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea766c1af2.mp4?token=t_AxHu4RxoIvTQJ2kkSQnYW9FIDYkZ2Q8FPMOmuarx0CbAJSmThrZILXeA7UcWLv22w7w4nJj6scykJlFq98pup_zs7C6JlRtjgFyumYZjUWXa-XBXV9WqI_R3OMYI0Z5Vwa9VNlcPO9FCfl4jH3ZueKnMRrlL0eVsX3fXupSUnPUTaIw_0C4S6sxZLsGUHA-jI6eV2yAwCkQ-9Um-LwuBff_c_cNr6tyDcpZtlJmSwvNIrClwWmwYzeulaBrsC9MpRVwDIHBmxkwj1zYuzIbTze3gkTZufhWNW5OueYDD24l9AchaAA8zp-PYfIrz0y-Y_FL5nY0PFxwA1K94TWOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea766c1af2.mp4?token=t_AxHu4RxoIvTQJ2kkSQnYW9FIDYkZ2Q8FPMOmuarx0CbAJSmThrZILXeA7UcWLv22w7w4nJj6scykJlFq98pup_zs7C6JlRtjgFyumYZjUWXa-XBXV9WqI_R3OMYI0Z5Vwa9VNlcPO9FCfl4jH3ZueKnMRrlL0eVsX3fXupSUnPUTaIw_0C4S6sxZLsGUHA-jI6eV2yAwCkQ-9Um-LwuBff_c_cNr6tyDcpZtlJmSwvNIrClwWmwYzeulaBrsC9MpRVwDIHBmxkwj1zYuzIbTze3gkTZufhWNW5OueYDD24l9AchaAA8zp-PYfIrz0y-Y_FL5nY0PFxwA1K94TWOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: آمریکا تفاهم‌نامه را نقض کرده و ما هیچ تعهدی را بدون مابه‌ازا اجرا نمی‌کنیم
🔹
رویکرد ما تعهد در برابر تعهد است. اگر طرف مقابل تعهداتش را نقض کند متقابلا ایران همان کار را انجام خواهد داد. @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/449032" target="_blank">📅 00:02 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
