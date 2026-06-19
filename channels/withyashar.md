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
<img src="https://cdn4.telesco.pe/file/R-2G-6ZRbML_SHh4yUJa_DcAibIynRy-jfbi9pWdgUti9xO885JSKZNFcbxjePOD4SmTdipJ-34Cjf-0aXPCEqEUb-a8hjWRkK5MfrMxpn1n-hdWXKqGL2bB0zBGEUwdloRuPk9w_dL_IyQq8htZvMPfqJJGDJU4OctcDVIcE14F1RoEMYsxUd-zmkgmMl92G4Iobn9R-FOsknfZGp5DU5Wuhx0pTiP-c3jLCGToe1SJY9tClxz7XWoXqhiOs7oF4u1UZDIQokcKdJ_SpkMpu5eXcXIw2Uv0xb1DreSBkLgaCoc17XsfFGCNmLgv_Da0NF6gK63ie_O8YIGqM0woSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 13:44:06</div>
<hr>

<div class="tg-post" id="msg-15313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مشاور هیئت مذاکره‌کننده ایرانی، مرندی:
نظام ترامپ به توافق پایبند نیست. و ایران در این شرایط یادداشت تفاهم را اجرا نخواهد کرد. اقتصاد آمریکا در معرض فروپاشی است و اسرائیل مجازات خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/15313" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شبکه CNN به نقل از منابع آگاه اعلام کرد که پیش شرط ایران برای شروع مذاکرات در سوئیس توقف درگیری‌ها در لبنان است
@withyashar</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/withyashar/15312" target="_blank">📅 13:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b3d24142f.mp4?token=HpzeMUFvKgmCZC5mYz8vS3MxXoZ5zagqlXLyExxOUHoUdEcT_yjssvCN_RuqdoDUKnuAVHGLVF-HIEtNiSvK89h1W55QswrVGqM8KW_ejWNuO7nfvkTxixn8hMo-afAimh5QtS10FWrWZj_zs4-ms9h3NfencqXaYVkQ1B_lwNzWhM8E8y-FVIAlHHlks6xJS-VlXl9hED3efY20mBu2BLDurdazSoBM-p3hfq0qm5Q_OygiSt6lbj6jxKXh8VxlTY0pVxwMWr-J5aWsda12rtBq66bkEv9ZSuVOsH1i4ZvBVGXLxEvT-C-OXNzr3O2i7sYdhuLvXkLakcSnhv0YMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b3d24142f.mp4?token=HpzeMUFvKgmCZC5mYz8vS3MxXoZ5zagqlXLyExxOUHoUdEcT_yjssvCN_RuqdoDUKnuAVHGLVF-HIEtNiSvK89h1W55QswrVGqM8KW_ejWNuO7nfvkTxixn8hMo-afAimh5QtS10FWrWZj_zs4-ms9h3NfencqXaYVkQ1B_lwNzWhM8E8y-FVIAlHHlks6xJS-VlXl9hED3efY20mBu2BLDurdazSoBM-p3hfq0qm5Q_OygiSt6lbj6jxKXh8VxlTY0pVxwMWr-J5aWsda12rtBq66bkEv9ZSuVOsH1i4ZvBVGXLxEvT-C-OXNzr3O2i7sYdhuLvXkLakcSnhv0YMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توقیف یک دستگاه نیسان گاوی عجیب برای اهداف خاص توسط پلیس
@withyashar
🤯</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/withyashar/15311" target="_blank">📅 13:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bffa7007.mp4?token=bqI7-R2sEvzDtz4BZcvDQdBeOQFikrg88ad1gwUnuO4sijRc_3cu6zWD9H4bKKmCAZFwUMj9q3sbO237MW3A7RXsSl4tRjxoMxjzXBqUqz0N8nNa5ypCKzm1DPIrbOLezqMBuy-B8f98sQq5RFn69D4XhRMO-krlclfAv5ZWWvTxZ7V1W0-SOLzya_DxD7N5K310KUHQY71k-nlIeoQcPIrx5nc9Iiw9IM9PsGS04ka3minzP80RaX2890KKPkFKrVPZvS8o0uQvKWtAzLPlyWSjTVTBgj8IKzUUmGp5vWMpr0D6yDJvcqMGiNenJHIgyTmDl1HnwL3ju1W6TAS7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bffa7007.mp4?token=bqI7-R2sEvzDtz4BZcvDQdBeOQFikrg88ad1gwUnuO4sijRc_3cu6zWD9H4bKKmCAZFwUMj9q3sbO237MW3A7RXsSl4tRjxoMxjzXBqUqz0N8nNa5ypCKzm1DPIrbOLezqMBuy-B8f98sQq5RFn69D4XhRMO-krlclfAv5ZWWvTxZ7V1W0-SOLzya_DxD7N5K310KUHQY71k-nlIeoQcPIrx5nc9Iiw9IM9PsGS04ka3minzP80RaX2890KKPkFKrVPZvS8o0uQvKWtAzLPlyWSjTVTBgj8IKzUUmGp5vWMpr0D6yDJvcqMGiNenJHIgyTmDl1HnwL3ju1W6TAS7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حساب رسمی‌کاخ سفید: دیروز ترامپ تو نشست سران جی7 وقتی وارد شد بلند گفت رئیس منم
@withyashar</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/withyashar/15310" target="_blank">📅 12:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B07PdT2OvqF0WW-Xs1lXpcwWwpoPmNlj4flyF4G8BfuJsgIRmH3grW9dzbnOCJkcmA7sMnXfXS3XCdk6Qw2wp7h4SaMt1lmG5goY21mbbyFFDA5YlJ_jRDZaFZ_l-xS25WZ6ZpbVdtdrRP9neWLpaAFMAsGWZ8nl92KKImnxdlivRJTVmXVl6yGTsR7WINVRGm2F0AoGmvnouRzaFJoX_U5yIOf9tj0eFg7bzdWLEXc4vX0LSn2RkXNDp9mktCYox6v_d170HAom8qoDG1x6FL7heRIFmn9ELwRyFWbEFg210zaPLcpIiRMyuhm4PNI_MSQ7-M4cmw1IkNGo_X5-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: ۳پا چندین سلول مخفی در عراق ایجاد کرده است تا حملاتی علیه کشورهای خلیج فارس که میزبان نیروهای آمریکایی هستند انجام دهد، که خارج از ساختارهای فرماندهی سنتی شبه‌نظامیان عمل می‌کنند تا خطر شناسایی کاهش یابد
سه تا چهار سلول، هر کدام متشکل از حدود ده مبارز شیعه عراقی نخبه، حداقل هفت حمله پهپادی بین ۲۰ آوریل تا ۱۷ مه علیه اهدافی در کویت، عربستان سعودی و… از محل‌های پرتاب نزدیک بصره و سماوه انجام دادند.
برخی اعضا از مقاومت اسلامی در عراق جذب شده‌اند، اما سلول‌های جدید مستقیماً به سپاه پاسداران گزارش می‌دهند نه به رهبری شبه‌نظامیان مستقر.
@withyashar</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/withyashar/15309" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c913f668.mp4?token=nLArA8TCaSwXElcGcBUWVaY6xtGjGtPPcslM2geE3yN0ioFLg77o67_ypnn-a1yF1U5obe09VklIhpuUVzg7W-eJr5cypbYK2oNctofK7BlMT9qagEwHA6SWyQQJVBpItYJmea2hw7h8xOhpWfc7JBZclGQFtMzLIVHVrT_7K0m2Yr8GvNvITeu_luspiTNQP_9i-p_osxRXXptMYlYdGPkCfDfeGXVmMolLL8yCNZTj4P1u9zJa9Bgxe7me36s1sFtU9ymD16D7k-l8FZVMRrDWr-LTGsdofEXNi0jTlqEwL4uaTBNsbcGYjHsjXKUtRqOU0WXfiVnXyVl0TKJSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c913f668.mp4?token=nLArA8TCaSwXElcGcBUWVaY6xtGjGtPPcslM2geE3yN0ioFLg77o67_ypnn-a1yF1U5obe09VklIhpuUVzg7W-eJr5cypbYK2oNctofK7BlMT9qagEwHA6SWyQQJVBpItYJmea2hw7h8xOhpWfc7JBZclGQFtMzLIVHVrT_7K0m2Yr8GvNvITeu_luspiTNQP_9i-p_osxRXXptMYlYdGPkCfDfeGXVmMolLL8yCNZTj4P1u9zJa9Bgxe7me36s1sFtU9ymD16D7k-l8FZVMRrDWr-LTGsdofEXNi0jTlqEwL4uaTBNsbcGYjHsjXKUtRqOU0WXfiVnXyVl0TKJSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:حملات را یادتان هست؟ آنها وارد می‌شدند و بیرون می‌آمدند.ما وارد می‌شویم، نابود می‌کنیم و آنجا را ترک نمی‌کنیم. این کاری است که ما اکنون در لبنان انجام می‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/withyashar/15308" target="_blank">📅 12:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuAfDZcMQKHGxbYegFrW7lk_ibgpxXKeglN4RY2ooklsOtOA7A07007paPIZPjDkvTE5Beo_J2w1-suq3_AC_kW1erTq4_1-KGXOZxscxffZMgHGjd6-7dKjV-VJUWhlEgnbO3q_IFNzDtbjAM1THeZSLXRvzrVSoXb07v48-Z5y7gfIDzQGasTFtugYyCrdf3GGDiMjGaOKq7QHfjwy-RGOlKQ3vHW11GtRglNSLzaarPBBxrbOhCHtDuOLpj3TkfzZftS_C64GGvDpVHsaYOXOzFQXLvvd34ICKGs2I4I4VwqCdD1rqrEnmipgLCnKantY_gr1ZBGibog2uPeJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات ارتش اسرائیل ساعاتی پیش در بعلبک، در عمق حدود ۸۵ کیلومتری در عمق لبنان. حمله‌ای غیرمعمول در عمق آن - ارتش اسرائیل در ماه‌های اخیر تقریباً در دره لبنان و منطقه بعلبک حمله نکرده است
@withyashar</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/withyashar/15307" target="_blank">📅 12:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15306">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd1e599ede.mp4?token=UUC9s-ussMWLqEPE-SIr3iu5fg9kUvN6bMu9Blx2i4i9kFpTc-fETFjJ6ojVLpmy6SAQ-oLWfRWnD5Io2j6qaIbHvv9vqNUHMlDP3QgS7mTi3738RxMGF9uSGtg91ce0vCARePs0K9V0xjcPifPYGziijVQ9Peoa6xKvR8P8wTdBL8DKy4ld-euKPexDKHJG50tBFUM3XCbXHG-I9TqRasG8Us5wsH_XamXnvWWXcWlYQKM3snniD8FUlItKPDYXuQr80VxpwDc837VUGtc0KH5feXxbp5nkseJpPbw_RrJZCXAT7NE9WeXaCgyw8Ry1UOVqT-XHkucHG7HSuEFvfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd1e599ede.mp4?token=UUC9s-ussMWLqEPE-SIr3iu5fg9kUvN6bMu9Blx2i4i9kFpTc-fETFjJ6ojVLpmy6SAQ-oLWfRWnD5Io2j6qaIbHvv9vqNUHMlDP3QgS7mTi3738RxMGF9uSGtg91ce0vCARePs0K9V0xjcPifPYGziijVQ9Peoa6xKvR8P8wTdBL8DKy4ld-euKPexDKHJG50tBFUM3XCbXHG-I9TqRasG8Us5wsH_XamXnvWWXcWlYQKM3snniD8FUlItKPDYXuQr80VxpwDc837VUGtc0KH5feXxbp5nkseJpPbw_RrJZCXAT7NE9WeXaCgyw8Ry1UOVqT-XHkucHG7HSuEFvfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز، درباره لبنان:تمام خط اول روستاهای لبنان ویران شده است.ما در حال ویران کردن تمام خانه‌ها هستیم. ساکنان دیگر هرگز آنها را در مقابل چشمان خود نخواهند دید.
@withyashar</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/withyashar/15306" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15305">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم. @withyashar</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/withyashar/15305" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15304">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هم اکنون منابع لبنانی می‌گویند:
ستون‌های زرهی اسرائیلی در حال پیشروی به سمت نبطیه، پایتخت حزب‌الله در جنوب لبنان هستند و درگیری‌ها سنگینی گزارش می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/withyashar/15304" target="_blank">📅 12:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15303">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575f785e69.mp4?token=bSEdfUcD0dRUfExkB22jBTbh4z1B_No3kJoyhV-zoCR5F3gR5NAeTkIZXBGIge5N2STni0rdr6zX-HH7d4NtfTOIOq93BhWis6gBL0bc5j2x_GnQ1SKroqjy1jMK85pwirQbMEmU9pQqJfb2joEwgbjFMThn3dXJkFQhPTJETrrSuGvVN818LlKFE1aOe6Zo_oAHYcaBopwEl9fbwvKhw7b8HbcffkD42TNPPatTzfskKaHGq9fCdU4ZNpS0IjWPdbQCkXjxYGcyltDp_GMf3xu5cQ5Ab34G1D0KwmHPymR5byweXY6hn2mUwngL8oGdfy5NAQ2In-U6P8UdG0VVUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575f785e69.mp4?token=bSEdfUcD0dRUfExkB22jBTbh4z1B_No3kJoyhV-zoCR5F3gR5NAeTkIZXBGIge5N2STni0rdr6zX-HH7d4NtfTOIOq93BhWis6gBL0bc5j2x_GnQ1SKroqjy1jMK85pwirQbMEmU9pQqJfb2joEwgbjFMThn3dXJkFQhPTJETrrSuGvVN818LlKFE1aOe6Zo_oAHYcaBopwEl9fbwvKhw7b8HbcffkD42TNPPatTzfskKaHGq9fCdU4ZNpS0IjWPdbQCkXjxYGcyltDp_GMf3xu5cQ5Ab34G1D0KwmHPymR5byweXY6hn2mUwngL8oGdfy5NAQ2In-U6P8UdG0VVUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم.
@withyashar</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/15303" target="_blank">📅 11:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15302">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سوئیس رسما اعلام کرد: مذاکرات ایران و آمریکا برگزار نخواهد شد @withyashar</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/withyashar/15302" target="_blank">📅 11:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15301">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دو حمله هوایی به لبنان
الجزیره از دو حمله هوایی اسرائیل به شهرک عین بورضای و حومه شهر بعلبک در منطقه البقاع در شرق لبنان خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/15301" target="_blank">📅 11:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15300">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1fHrfVI6CbeOV3bRgznb2B9cq0Ydvbnb690qkB6p6kR56i2sKKZ9KGW8FXm2zxFY-kH0qlIeKqZlViQ3gVplnl4ytsdFo-c0r5Xspbz2mopL9IRIEdE4_oGRn1hrwnud0AoPTDM2C8ddxbVv1EVmRpZJo_l_HPZ-ZVTALgJMp_sSo8OlxvcVvSomqfhr8CtB-f3Kfc7Rsz-edaBT1V8iKfLPJ_UpRldJkq0JG-wIH3M6rBxZuIoD1MS6g9PMxV4HLSycAd4rNPgM2SL1DPq8SgPSZrxymcDEJXBHNeZouGewsDDZESi-dl3RNj-aaTfI0D_CuuzvGRYpqpM0zpT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین : یک ایده جدید:
دست از قلدربازی برای متحدانمان و چاپلوسی برای دشمنمان بردارید.
@withyashar</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/15300" target="_blank">📅 11:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15299">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سوئیس رسما اعلام کرد: مذاکرات ایران و آمریکا برگزار نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/15299" target="_blank">📅 11:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15298">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بن گویر وزیر امنیت اسراییل:به ازای هر اشک یک مادر اسرائیلی، هزار مادر لبنانی باید گریه کنند. کل لبنان باید بسوزد
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/15298" target="_blank">📅 10:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15297">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TERpVbhLAOMYPHHYnHOhB57TDyThl7X18mI8Fgxr3UonjhN9BCJJ2uIlo32cLHPzgQfsWUjiMzT_9BYD6vO7ZZzzdmR1HJF-8Re6enU5V1_d06USk9dlkH6oeGruXyE_qMih8DS1JnCHAWQ1FQFWCqdcQfm2WXeARDEXUtZxMpjwSO1wDFChVXGcLm8oNS8WrMMxEjFtpoie_bTkawrkz3ZH026KBIVZhnaWEnFuchW47JhhhtTQFON3GrYy14CPQ1eDMDYOrG9e29uUp8-vHJ83T0TaHmMDwqoU2OXaQ9WQuzvACXoLyd4Yg3q8t2puCPkozLrgZu10ghp48hScqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لورا لومر خبرنگار نزدیک به ترامپ جاویدنام های دی ماه رو حدود ۱۰۰ هزار نفر اعلام کرد
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/15297" target="_blank">📅 10:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602da85ed4.mp4?token=IcFR7EU3iUqeJ1fDnwxIngj9h5Hu-qTap5NYOFMfvTE4krPVVcL9mjdk-0CHVjNj9jBA18aWc9AInCMP56NrPD2HyqAe7xGevHEcC_W7UWZI0WOhOfeVSOMu83iZGXXKPBiRlTh-mydY2KaAUPsSJCaU5AwFABPv5a0CpjdlMMMwxXNuOu2FNKJfw1knd3jViWTDczDEdajFra14ohqWIhjbIGZDlRJIgAPh9jkEWDWJd0EqL9cFmEOlTU4mXueH4k6RTdZqtkIFBeJd-PAtyWHfvZdnAA-nkZoCsRrlW02xsbbf8vZy-sbMzZnaGiE-3SYD0AQv_CHSlkVIOZZgKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602da85ed4.mp4?token=IcFR7EU3iUqeJ1fDnwxIngj9h5Hu-qTap5NYOFMfvTE4krPVVcL9mjdk-0CHVjNj9jBA18aWc9AInCMP56NrPD2HyqAe7xGevHEcC_W7UWZI0WOhOfeVSOMu83iZGXXKPBiRlTh-mydY2KaAUPsSJCaU5AwFABPv5a0CpjdlMMMwxXNuOu2FNKJfw1knd3jViWTDczDEdajFra14ohqWIhjbIGZDlRJIgAPh9jkEWDWJd0EqL9cFmEOlTU4mXueH4k6RTdZqtkIFBeJd-PAtyWHfvZdnAA-nkZoCsRrlW02xsbbf8vZy-sbMzZnaGiE-3SYD0AQv_CHSlkVIOZZgKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری اکسیوس: در مورد نه تنها اعمال قدرت، بلکه محدودیت‌های قدرت خود به عنوان نتیجه از درگیری ایران چه آموخته‌اید؟
ترامپ: هیچ محدودیتی وجود ندارد. من هنوز آن درس را نیاموخته‌ام. می‌دانم که وجود دارند، اما می‌دانید، هیچ محدودیتی وجود ندارد. ما آن‌ها را کاملاً از نظر نظامی شکست دادیم
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/15296" target="_blank">📅 10:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15294">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb0c5fe35.mp4?token=lzTz3TY3Elx4AoCQkh9sPpuv0MZPmbxjfdDj9LPdLZJR3ScTuTi14rTy58n7ZmGa_JMGdmZgYhTj85q1u32BkEnrlOUwV7kp17JI71n2w76Dae0bibTwQTsBBwPp4w20Xl6tPB52MODVsjwaFFh3CykFtIgDcNpyYvgWLzk8rtOUSZOD9l2Sz-6K0YSrpBd4NugOwHBdj07ud81fH0Du3ul3yYpQRwkANOh693Juvj_zCSyaxW375vGSfzwzRzBEgynGZMrPkZ4P1JEuKSqAywBNv7Av_er0wY7CO4AN-L6GTdr4m2snJhGsIVj2CjoFSpFIjJYWQRmej7eQZrvPDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb0c5fe35.mp4?token=lzTz3TY3Elx4AoCQkh9sPpuv0MZPmbxjfdDj9LPdLZJR3ScTuTi14rTy58n7ZmGa_JMGdmZgYhTj85q1u32BkEnrlOUwV7kp17JI71n2w76Dae0bibTwQTsBBwPp4w20Xl6tPB52MODVsjwaFFh3CykFtIgDcNpyYvgWLzk8rtOUSZOD9l2Sz-6K0YSrpBd4NugOwHBdj07ud81fH0Du3ul3yYpQRwkANOh693Juvj_zCSyaxW375vGSfzwzRzBEgynGZMrPkZ4P1JEuKSqAywBNv7Av_er0wY7CO4AN-L6GTdr4m2snJhGsIVj2CjoFSpFIjJYWQRmej7eQZrvPDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در آغاز درگیری ایران، شما صحبت کردید که فقط تسلیم بی‌قید و شرط را می‌خواهید. تفاهم‌نامه شبیه تسلیم بی‌قید و شرط به نظر نمی‌رسد.
ترامپ : واقعاً احتمالاً تسلیم بی‌قید و شرط است. من اینطور فکر می‌کنم
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/15294" target="_blank">📅 10:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15293">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزارت خارجه آمریکا: حزب‌الله باید خلع سلاح شود
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/15293" target="_blank">📅 10:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15292">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دلار داره آرامش قبل طوفان رو تجربه میکنه و ممکنه بزودی حرکت بزرگش رو آغاز کنه  رفقایی که نمیدونن دلار میریزه یا رشد میکنه عضو این کانال تحلیل بشن بهتون میگه:  https://t.me/+hLt81qXCGTQzOWQ0 https://t.me/+hLt81qXCGTQzOWQ0  لامصب اطلاعات رانتی داره</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/15292" target="_blank">📅 02:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15291">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دلار داره آرامش قبل طوفان رو تجربه میکنه و ممکنه بزودی حرکت بزرگش رو آغاز کنه
رفقایی که نمیدونن دلار میریزه یا رشد میکنه عضو این کانال تحلیل بشن بهتون میگه:
https://t.me/+hLt81qXCGTQzOWQ0
https://t.me/+hLt81qXCGTQzOWQ0
لامصب اطلاعات رانتی داره</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/15291" target="_blank">📅 02:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15290">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش های محلی در جنوب لبنان،
از حملات هوایی سنگین جنگنده های اسرائیلی خبر می‌دهند،آسمان جنوب شرقی لبنان به دلیل شلیک گسترده منور های روشنایی ارتش اسرائیل روشن شده است.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15290" target="_blank">📅 01:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15289">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کامنت جدیدم زیر پست ترامپ، لاتیش کردم
😂
فقط همین کامنت رو لایک کنید . ترجمه در کانال تلگرام.  https://www.instagram.com/reel/DZvkK0jpILu/?comment_id=18367681780225433  ترجمه :    ببین ترامپ،  می‌دونم دیر یا زود این کار رو به سرانجام می‌رسونی، ولی رفیق، این…</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15289" target="_blank">📅 01:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15288">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کامنت جدیدم زیر پست ترامپ، لاتیش کردم
😂
فقط همین کامنت رو لایک کنید . ترجمه در کانال تلگرام.
https://www.instagram.com/reel/DZvkK0jpILu/?comment_id=18367681780225433
ترجمه :    ببین ترامپ،
می‌دونم دیر یا زود این کار رو به سرانجام می‌رسونی، ولی رفیق، این دیگه درست نیست. مردم ایران از این همه انتظار و بلاتکلیفی به مرز دیوانگی رسیده‌اند.
این داستان را تمام کن و کار را یکسره کن.
خیلی از ما در این ماجرا کنار تو هستیم، اما باور کن این آخرین تغییر رژیمی است که حاضر به حمایت از آن هستیم. بعد از این دیگر چنین چیزی تکرار نخواهد شد.
عشقی.</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15288" target="_blank">📅 01:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15287">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزیر دفاع اسرائیل:اسرائیل توانایی انجام عملیات مستقل علیه ایران را دارد و در هر لحظه برای اجرای یک عملیات آبی و سفید در ایران آماده است.
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/15287" target="_blank">📅 01:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15286">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر دارایی اسرائیل، بزالئل سموتریچ:
غزه در ویرانه باقی خواهد ماند. در نهایت، مهاجرت رخ خواهد داد، زیرا در دهه‌های آینده چیزی برای جستجو در آنجا وجود نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15286" target="_blank">📅 01:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15285">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ: پیت هگست قراره خیلی پیروزی های دیگه بدست بیاره پسر خوبیه
من فقط مردمی رو دوس دارم که طرفدار من باشن
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/15285" target="_blank">📅 01:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15284">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این پست جنجالی را از دست ندید، کلیک کنید و کارهای اداریش را انجام بدهید. حتماً تا انتها ببینید.  https://www.instagram.com/reel/DZvdCMHxeYT/?igsh=MW50eDUzOWQ0MnFzYw==  اتاق جنگ با یاشار : Bagher.exe</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/15284" target="_blank">📅 00:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15283">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">subseven</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/15283" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15282">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/15282" target="_blank">📅 00:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15281">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این پست جنجالی را از دست ندید، کلیک کنید و کارهای اداریش را انجام بدهید. حتماً تا انتها ببینید.
https://www.instagram.com/reel/DZvdCMHxeYT/?igsh=MW50eDUzOWQ0MnFzYw==
اتاق جنگ با یاشار : Bagher.exe</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/15281" target="_blank">📅 00:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15280">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfpGymKndKBQPowJqchYHqmJUoU1627eCCKWIaEMpFCykPoxwrhsJk-RnJu-P4ujRbSrPNV-1b984z_tfkIr1XpiZMZ_o_ACZe0XWzi0-XUYQxifU3fj22bH46R6d8fxUA7LNXQ52FVaLVO-kF7iPxt0ZBeQjQj2zLSqQQM6-JxUE7iN2tBcqyAjQruIJTf4ROnt9JTPzNauMQ0cvgUWszY3ATeQfsg4xQlnhUerEWWCscr73noWUGS7FAgUN5KeNtBrkfNCzUxQWDrcGMyWvjTI9k66G1Uv4uuvtlhMPmAPsC5OXMW3ZAM1UHcmEFgBrVzUEcofdzemy47X_JQMvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15280" target="_blank">📅 00:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15279">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزیر جنگ اسرائیل: قدرت ایران را درهم شکستیم، رهبران، دانشمندان هسته‌ای و زیرساخت‌ها را هدف قرار دادیم و برنامه هسته‌ای ایران را از بین بردیم؛ اکنون باید اطمینان حاصل کنیم که این برنامه دوباره احیا نشود
اسرائیل در هر لحظه برای عملیات مستقل در ایران آماده است
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/15279" target="_blank">📅 23:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15278">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">المیادین به نقل از منبع آگاه: هیئت مذاکره کننده ایرانی سفر خود به سوئیس را به دلیل تداوم حملات اسرائیل به جنوب لبنان متوقف می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/15278" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15277">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbYjMiVmPna0K7Az4ojIUTnb-ZeiZXudnnibHxGZGDnmw01HP1bxnyjCIVsGTgjSFIO6qwfbZ2xLzODAivxTxz04IUVhbseWa4XdjJW3Ya-HqI_TrQliMWeEkqyKRvOu_TP-lc8vzSJX6Qy-wKixxs_SJMfuCc0zFwBM9b-70HRNLLsp_tdgSGCZzXwxQbhiEJvE3Lx66OS3IhyUOUBOu0QyZ_UhY4TEH9DAM7erm2tUWdNJWoIKMWpPTAn39hN3V_8NZzhE6Wjl5BuukHtvXHMWgEDeVkMDLqIwzTput1G8IyBbRE80YWBApO-pKJslUh6I-vXfdADrwVXRjh3UEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: ایالات متحده به صلح متعهد است و ما از همه در خاورمیانه می‌خواهیم که به تعهد خود برای پیشرفت عالی مذاکرات ما پایبند بمانند.
بازارها از آنچه اتفاق می‌افتد هیجان‌زده‌اند:قیمت نفت به شدت کاهش یافته و سهام به سرعت افزایش یافته است.
ما انتظار داریم آتش‌بس کامل در تمام جبهه‌ها، از جمله لبنان، «حزب‌الله» و اسرائیل برقرار شود. از توجه شما به این موضوع سپاسگزاریم!
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15277" target="_blank">📅 23:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15276">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شورای عالی امنیت ملی:
بر اساس تفاهم‌نامه منعقد شده، تا ۶۰ روز هیچ‌گونه عوارضی از کشتی‌های عبوری از تنگه هرمز دریافت نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/15276" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15275">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromyegi❤️</strong></div>
<div class="tg-text">به یزدان قسم فقط کانال خودتو میبینم و طبق تحلیل هات روانمو سالم نگهداشتم وگرنه با این توافق الکی که پیش اومده خودکشی میکردم
😮‍💨
دمت گرم
🤍
من به تغییر رژیم ایمان دارم و میدونم طبق گفته شما زمان بر هست پس صبر میکنم
پاینده ایران و جاویدشاه
👑
✌🏻
❤️</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/15275" target="_blank">📅 22:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15274">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آسوشیتدپرس: کاخ سفید توافق با ایران را به کنگره ارسال کرد
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/15274" target="_blank">📅 21:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15273">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فارس:  تیم مذاکره‌کننده ایران تا حصول اطمینان کامل از توقف حملات به لبنان، هرگونه گفت‌وگوی تکمیلی را به حالت تعلیق درآورد
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15273" target="_blank">📅 21:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15272">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رهبری سیاسی اسرائیل به نیروهای دفاعی اسرائیل اجازه داده است که در داخل «خط زرد» در جنوب لبنان تیراندازی کنند.
انتظار می‌رود مقامات ارشد نظامی در ساعات آینده قوانین درگیری و راهنمایی‌های عملیاتی به فرماندهان میدانی را به‌روزرسانی کنند.
این تصمیم همچنین شامل برنامه‌هایی برای نابودی هر «زیرساخت مرتبط با حزب‌الله» است که در داخل «خط زرد» شناسایی شود.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15272" target="_blank">📅 21:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15271">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله به ایران و حزب الله آماده شوند
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15271" target="_blank">📅 21:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15270">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsDltNIruDpvLK8Hevo1wxTnlkv3_yikK8l4Ra5s7CLLPpySY2mx0tA3UZLnXShxkQfy-Sb1RIe2mxUVBwpH5khCB4YB1SDBDUkLI3vBLVRt39h-JDffkFJkIx2bxVHFyPPQVA3QY416DAAF-furi4vE7hxBSLObkyXWlS7OcrvSLz7JsptxE3Hqx1orCH5NP1VSdwEnSacQOOmqiJW_Y5TaWQZLdoJzwHkNWpIYLXxkhfwzkAlPY0F7eY0OjgMfryxWYc02ODKF5WxBvlczBLuWYx-k63Fs13Cq5eUmkqwLUvAfJvxKuEHYkaiojzCx9Fc40mr-OawwAcedUhbzvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس:  پیام جدید  iRahbar
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/15270" target="_blank">📅 21:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15269">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15269" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15268">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyGgUWJgRmDNkdD6NX6LBJ0AkEc92j-eXC0p4X_86AvlAW1CB7XvQ-inzgklLI1fdJSAJzWA5rrnpRfpOqWZXot6najKAQ3Us-y4XhR_3_M0kmnhHTYFgyICbCVPJ8CiWxV7ETAvNW_rgL554GzYd5cCv71m_dzWatpeBoETG8jwKhbqrEXX4bjOrt2vtOrXWhG-zhqD95frDRFVLcCUbd191B-vCTlwt6BBXtZe6uSrsgNpDT85P-svJpUylvdfIDWNrKCrJRwXb6AMbqbaOQ-SdWFfMJXz3OKT58egWednKtk69Bag4bZ2RVnf8XM59-QoaAKdUZ0232qOorQPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : هیچ پرداخت ۳۰۰میلیارد دلاری از سوی آمریکا به ایران در کار نیست.
این خبر جعلی است!
تنها چیزی که نصیب آمریکا شده، موفقیت، کاهش قیمت نفت و پیروزی است.
بازار سهام را ببینید.
تبلیغات «دُمکرات‌ها» در جریان است!!
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/15268" target="_blank">📅 20:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15267">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/15267" target="_blank">📅 20:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15266">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6Nyw2UctnImmH-X1xYaVShROlrSlhZ27syfVWF8qdERFzqT0a0QahISMtrBEusoemJURIBiNruUYEcLF_oNezybEGOo-u-laNgFSzvkYdeIO2ywGN2_TMKSGpjhJ0j_KhOydhEeOVngmEvJ-evM4sMp_1emhK3RM7AyvWuIe3rvEhEC65mmmqrtUjHBa0P7Cvs8uWEeJKsxCtEtlbDNdRish0VP-iC8oEE1KVlQr6uHGW10zgkaK3np5mZlfwd6PVGAyo5t7RrTn1F6gLniY2tSV9lgsjYyQYAUJ9L22C4Uh0QHe3z235XBifGL3w3VRKzBnhinqa0P_RHg9Vtdlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نیروهای ایالات متحده، بنا بر دستور رئیس‌جمهور، محاصره تمامی رفت‌وآمدهای دریایی به بنادر و مناطق ساحلی ایران و از آن‌ها را لغو کردند.
نیروهای آمریکایی دیگر مانع تردد کشتی‌ها به مقصد بنادر ایران یا خروج از آن‌ها در خلیج فارس و دریای عمان نمی‌شوند. تمامی اقدامات نظامی آمریکا برای اجرای این محاصره متوقف شده است.
ناوهای جنگی ما همچنان در منطقه حضور خواهند داشت تا اطمینان حاصل شود که همه مفاد این توافق به‌طور کامل رعایت و اجرا می‌شود و از قدرت و اعتبار کامل برخوردار است.
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/15266" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15265">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ونس درباره نتانیاهو: من گزارش آکسیوس را دیدم که می‌گوید نتانیاهو عصبانی است.این بازتابی از گفتگوهایی که من با او داشته‌ام نیست. شاید او چیزی به شخص دیگری می‌گوید که به من نمی‌گوید.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15265" target="_blank">📅 20:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15264">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a543e5cc9e.mp4?token=SB2xX6Iu7aGz9o2Nqyb7THwiKFHP7UvvuDzJDW1Vn-48q2FC25Y9w3YVjqgy7BW7kEEqDrfDUC5QNlfbS-cHFMdXqN1YbhZ-lF_MmyvMX3_0mJB97niihGU3YzPgye0AMwRTDdp49Wx4T6DS5zNQszJxDWwlwUkvS20alocj4RBATNgKU96_rXJj4SWxqmn2k3obsJHtoMLF_uxbs389nKFt46uKdEmDzpKlDlhAHt3YpgJaYOnKrZi9dBed2JI8neB2wHEdR6NYxt6dNyjqSGpY2uTUCOzYhdK_G3-ZSB7ZmdL6xz1FHaF_I7ZMmdFgds2DHTC4qfFH0psccn6GBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a543e5cc9e.mp4?token=SB2xX6Iu7aGz9o2Nqyb7THwiKFHP7UvvuDzJDW1Vn-48q2FC25Y9w3YVjqgy7BW7kEEqDrfDUC5QNlfbS-cHFMdXqN1YbhZ-lF_MmyvMX3_0mJB97niihGU3YzPgye0AMwRTDdp49Wx4T6DS5zNQszJxDWwlwUkvS20alocj4RBATNgKU96_rXJj4SWxqmn2k3obsJHtoMLF_uxbs389nKFt46uKdEmDzpKlDlhAHt3YpgJaYOnKrZi9dBed2JI8neB2wHEdR6NYxt6dNyjqSGpY2uTUCOzYhdK_G3-ZSB7ZmdL6xz1FHaF_I7ZMmdFgds2DHTC4qfFH0psccn6GBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی.دی. ونس در مورد لغو تحریم‌ها:
«راستش را بخواهید، ما این را یک امتیاز بزرگ به ایرانی‌ها ندیدیم — ایران هم... این را به‌عنوان یک امتیاز برای خودشان تلقی نکرد، چون چیزی که مانع فروش نفت آنها می‌شد، تحریم‌ها نبود.
آنها بدون هیچ تخفیفی نفت زیادی می‌فروختند، چون تحریم‌ها اساساً ناکارآمد بودند.
در آن مرحله، کاری که تحریم‌ها کردند این بود که سیستم مالی ایران را به نوعی به سمت سیستم بانکی سایه‌ای (غیررسمی) سوق دادند.
با لغو تحریم‌ها، در واقع خواهیم توانست کمی ببینیم که سیستم مالی آنها پول را به کجا می‌فرستد و از کجا پول دریافت می‌کند. این یک مزیت واقعی است.»
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/15264" target="_blank">📅 19:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15263">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lL5Ll6mdYBHv1ZmGaJRz5vEyHE5sdlxBC7jM2lMBXM_IRNMnnsGxzv-uGFILv4eMlkpwXSXPLIo3Dl2PJKHiFXTvPTtd_XvAY_d_47W48QV3U2FvL6c7S0KVy5tUoedr-0oO-lTCOe-NlFiDap52xrFua4X-23rwsMK2gWW6cKLzRZfhb_NmummJ6u3MFik8LEFwbcnIzvFDDCAqaBqXXyCRmzUR0Z7rLoeY2417E8sHcgsfC-_8JEEeOm4DG64g8muBd5PhyYomYiAGXguWBdUdsTYEWEcS5t2RiFtqF6s7fz2eiOhlQuddCzikZY2S-chzSIFxGFXqKY97nITNGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ترامپی که امضاش اینهمه بالا پایین داره انتظار ثبات روانی دارید ، موج مکزیکی هم رد کرده نوار قلبه
😂
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/15263" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15262">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ونس: اگر ایرانی‌ها رفتار خود را تغییر ندهند، ارتش و برنامه هسته‌ای آنها همچنان نابود خواهد شد.
ما در حال حاضر یک تحریم اقتصادی فلج‌کننده علیه ایران اعمال می‌کنیم و تا زمانی که این کشور رفتار خود را به‌طور اساسی تغییر ندهد، به آن پایان نخواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/15262" target="_blank">📅 19:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15261">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آمریکا حتی یک سنت هم به ایران نمی‌دهد
جی‌دی ونس: "آنچه از همه شما می‌خواهم این است که صادقانه گزارش دهید که ایالات متحده حتی یک سنت هم به ایران نمی‌دهد...حتی مزایای اقتصادی، کاهش تحریم‌ها و غیره که با این معامله همراه است، فقط در صورتی اتفاق می‌افتد که ایرانی‌ها عمل کنند!"
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/15261" target="_blank">📅 19:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15260">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">معاون رئیس جمهور آمریکا: دوره ۶۰ روزه مندرج در یادداشت تفاهم با ایران از امروز آغاز شد.
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/15260" target="_blank">📅 19:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15259">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15259" target="_blank">📅 18:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15258">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ایهود باراک، نخست‌وزیر سابق اسرائیل:
احتمالا نتانیاهو در آستانه انتخابات، به لبنان حمله خواهد کرد، و در تلاش است یک جنگ ابدی را با ایران و حزب‌الله آغاز کند
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/15258" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15257">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایرنا: ایران به پاکستان اطلاع داده است دیگر نیازی به برگزاری جلسه حضوری در سوئیس نیست.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15257" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15256">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5wtfMT7D-7GBBUKvy8aB5GVUu_5V7pOqTvsAUv3eKZ3sC4OQ-ISDzVVC2VB2oGUIzWK7f6P7Pqo6vWiVknPLxY4k-3FU1uqn-Xt1MX-hHLuM92hWH0hRi5uSmTmUcRBqr3O12NYbCP504keOWflwf__evZFQvnGCbmR3Hhttx0nxTwjNBNxo-fM22ld1Uih0yjxb6bv31UxBIg0Om88Q_ZkXKTaSXTar-tSCKGoYcjqJied1cnzcf1agBTQy1Nq_xV3Ikg39MJRqyacObkyy8051hOWHhQu_ZA2dkgbL_gfKW-1KW5tn0aL6hKG18MKz5cRYlv9t-7c9lOBozlfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نفت در حال جریان است، ایران هرگز نباید سلاح هسته‌ای داشته باشد (جهان امن‌تر خواهد بود!)، بازارهای بورس با قدرت در حال رشدند، اشتغال به رکورد رسیده، و قیمت‌ها در حال کاهش‌اند (امکان خرید بیشتر شده!). کشور ما قوی، امن و محترم‌تر از هر زمان دیگری است. “خواهش می‌کنم!
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/15256" target="_blank">📅 17:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15255">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تلویزیون پاکستان:
سفر برنامه‌ریزی شده نخست وزیر شهباز شریف به سوئیس بدون ذکر دلیل لغو شد.
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/15255" target="_blank">📅 17:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15254">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">از صبح حملات اسرائیل به جنوب لبنان پر قدرت ادامه دارن
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15254" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15253">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3483473645.mp4?token=NQepFurRu09B64QkqgY_LLuioa1B50lGT7UvOWKjgGD_DaHQpJGgW6K5OV6Rn7CVrPXK6OJutWeBSy2nm0qc0QMa2nVb-oYilIfrN8a5wEdiriKF_i_d0CKtms0gECyIV5i9wshOLFaiT1rHRfXcehqTPkYkYvUTJ8AWsWqKWKSPGMMF3xEB4azsJ-BkmF39PEwWuhPDtwmvQ_CasYxZkH9tPZ95k4Txi8Q8kS5tjgBiMss7-gYc9umByNYiFFAJzlt39BZFo4d5CkH8M3CDAxQCdt2Ad0_ERB8JPQn6pSyaBU3grxUjLAjX7iFmqJz0tBtLqkFdjC3rCBy8OBCf0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3483473645.mp4?token=NQepFurRu09B64QkqgY_LLuioa1B50lGT7UvOWKjgGD_DaHQpJGgW6K5OV6Rn7CVrPXK6OJutWeBSy2nm0qc0QMa2nVb-oYilIfrN8a5wEdiriKF_i_d0CKtms0gECyIV5i9wshOLFaiT1rHRfXcehqTPkYkYvUTJ8AWsWqKWKSPGMMF3xEB4azsJ-BkmF39PEwWuhPDtwmvQ_CasYxZkH9tPZ95k4Txi8Q8kS5tjgBiMss7-gYc9umByNYiFFAJzlt39BZFo4d5CkH8M3CDAxQCdt2Ad0_ERB8JPQn6pSyaBU3grxUjLAjX7iFmqJz0tBtLqkFdjC3rCBy8OBCf0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز شبکه پویای صداوسیما اومده و یه برنامه کودک در مورد توافق کردن و سازگاری گذاشته که تندرو ها به شدت عصبی شدن
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/15253" target="_blank">📅 16:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15252">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy5Qs57cYeOAAzG7w8L8CzJkGvz-jgnt3Dh1ryt_KP0jOoyggcwyqSKwkypBk3cbXX3y4U2njIgzOfOUdIkYfMpeuyfUCfKtG_T_SEGoUcidtJz-3NCaZs9CAS53ug1yd6tKxqcvhAoCGQ_iBHVijRnHyNT44DVJIIR2Kc05emYWcCwq4u6wI1Z8MVl6MrZbmD1N2kJ1wLM1HDsMvCr9FOamzo5C0FnEhHytxUSDjlxJjPAUtZcyERSY-ciNLzG3-jlrniITvBkQDYKDP1gkecqO61bL7gquk8gBH5A0gxDNj_SBRk1yynYQriKJzFtcbLXypq9BYnOqGwdawHtn7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : پاپ لئو از توافق صلح آمریکا و ایران تمجید کرد
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/15252" target="_blank">📅 16:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15251">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">محمد محبی فوتبالیست تیم جمهوری اسلامی که در خوشحالی زدن گل به تیم نیوزلند، به مردم شلیک کرد، رفته و عکس مهسا امینی رو کنده و انداخته توی سطل زباله... @withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/15251" target="_blank">📅 16:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15250">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/15250" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15249">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آموزش و پرورش
: ثبت‌نام برای ترمیم نمرات تا پایان هفته جاری امکان‌پذیر خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/15249" target="_blank">📅 15:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15248">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=RMCCcJHq9lrJicacQbwi_HUo7u7XU1dCBfcooXmDiWbHCw_cpW90VWstZt92v2rZBY6P_IiHFpm2IfhhchAyGK6U1vPnTdjNBzul_kWm4lDifKzolKkK8-Rsw5IBF5uIf6AAH6zpSZYXWQoQ7w_PUKhmn36oHisKj7ka5z5b6-uFihyac40_EFImXDLk1Y3jHroTGWnVTXXyR6fKXOF_YyFDD9c8dWORHFuqy1FMJ5K7_0L8MUVVkWNyVEkqc6EHDRv6sYO3NzUKe272Cg5gla_AmUz4QuAhgjWn2mOvEvYIQJwsomDZcwlEp2hSkwBDAqxQH0rfTcjOKBKvTwlzbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=RMCCcJHq9lrJicacQbwi_HUo7u7XU1dCBfcooXmDiWbHCw_cpW90VWstZt92v2rZBY6P_IiHFpm2IfhhchAyGK6U1vPnTdjNBzul_kWm4lDifKzolKkK8-Rsw5IBF5uIf6AAH6zpSZYXWQoQ7w_PUKhmn36oHisKj7ka5z5b6-uFihyac40_EFImXDLk1Y3jHroTGWnVTXXyR6fKXOF_YyFDD9c8dWORHFuqy1FMJ5K7_0L8MUVVkWNyVEkqc6EHDRv6sYO3NzUKe272Cg5gla_AmUz4QuAhgjWn2mOvEvYIQJwsomDZcwlEp2hSkwBDAqxQH0rfTcjOKBKvTwlzbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درست خوندم؟ Porngraph?</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/15248" target="_blank">📅 15:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15247">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirAbbas</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD6qObEucJYEmG-rUyXbA-HWEWxwSQZy-o4gGv8fc6JplhbPyuLvMdlaR9E7C5JzCrsJ5sJIOjJhWwKUB1j4DkbSbvDDk30IU9mAeg424vKfvEI9PKP9JqQH7izsq7gmMaovZRpPNUFRy3yZN1omWcrlOzXyFNF4rPScF2xKengD0KViG3LJU374QB5cpkeTCydUcaU6q6IYMC3Qa2nHxcTmCsKEG0sVS61UooAYU5eqDMNdPcshCh_NIMM5xK8ABXdE1yYYHgoej23yrlbkQdR4T9wKBtQunEoPrA-r4qRNSFMoyzMvqBVfgFxcpgJBd5XsiBrXwIokL8C37aMnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درست خوندم؟
Porngraph?</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/15247" target="_blank">📅 15:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15246">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/15246" target="_blank">📅 15:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15245">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شبکه کان اسرائیل: موضوع عقب‌نشینی از لبنان هفته آینده با هیئت لبنانی در واشنگتن مورد بررسی قرار خواهد گرفت
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/15245" target="_blank">📅 15:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15244">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرگزاری CNN : نتانیاهو معتقده توافقی حاصل نمیشه و جمهوری اسلامی با پایان دادن به موضوع هسته‌ای موافقت نمیکنه
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/15244" target="_blank">📅 15:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15241">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVAOkOZ6Fnf15mYp7Qygo_ap0v09PaHv8vCkIgHdI5Ho9HhWMai-Gr9dAA9FQ1OFyq87h9soGUq8UM_VJZnOEaf4929V7CLE1UOZcLj2N7jhM-xzAoofna0YV3rdfKzke450wGblIAdPlD89CuorZG0mQWCqI6V9NzyrTeRx-3rqU35KB9jrx2Vwdk0MAsHJSMHWEE49foBYPLHhxEjaFtFLnEeLKRFjyD_K9_xkhFBNQbhfXqY2sBForELdEJ4LTv7qwgHTnq7bK8H1_N192poythZktT7RXLTiOlNEn7XiaZQmrt_csP9dsxDcVekA6bxi9gtXkLvKxGnvFdPkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ATwprUXQf56vstV8itPtpotE_JMfEcJKPXHIPtgHxmA4BHAjKhXekdpwONLH7CUp8roOkbpEGO8kYkbhoOfe5lAf2lDsWDTgMP_6kWSq1BkXgGk3LHMwkl_Ub_ESTov3i6f0jzYwLKejYODec_9yJpfYUtPnn9OaIN34bwH_8UwxcwmeYci4Qn3Wrtyisk6BRDOSsQSdVNs2XJhc55sJYOmDYHKRDWtsIJemaGJQuLyORavBP1Urho_sPTxiAOHbzdl9qfVxydgF6CObwBNEkQrEGsyLk9gz0pjm7RggnwcJNvLbgwKilrjiZOTVGUZfNeYsDjSsc85tqM8_SS7Lew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TxCUiiYjvR__LklnHdUhZbqtamTothUWhL97cH7kP3_XzRpMQ6qwTlwa5k-Nol53sKCsNjYEI8fYpMKTmx0cDrHOn5dvSU4amROVfm-qTYSsvxCH9L-JrWZ0W3Kq_uVFNb6iFpK0pNO_YboalryMhPowfSWDSFdPnUyCQ0XyAEu8lzETlDpAG95TmwAx1MJOrwXs-blcL-ylJTouz4vNdAFuCfGw4H5UDAK6gYFarll6olTwzJAkXfq93FmFK-lPgMkLhHJzy-6xoaZYadcWBmKL4npVHmF6G04UrkfZrOf2ipX_ahoWwh6o_V2n9GymKGLbSX0JcZ_OX8zuA41nHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکان نسخه اصل سند امضاشده را منتشر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/15241" target="_blank">📅 15:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15240">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d36518f3c9.mp4?token=nSe-_xI01e5umzDQfykACZWg8MsdHqNvBlkU6ytw_hrzn-lxUIxQVc5CFEQyANZyQvLIoJRKab4dKafDoqRMZCPPOMpcI6Jf3U2DO-BR7AKwIxsIVu3bNEs_Kx7XnW4sfaTXPNCE_siOWQeUINXS64N8PZEISySaPH3rM2X9BxoFANhzK7qkDbT9tywJww7DKv96jYGwact1FGCUXFB6kkhyzqkW8VBnRz6l3g9FP9G-PH49wDs7nT7f7nrWTew6a_Ilz8Q-S8zT1kx6E2vCfbxKMLbJ9dUWXbn_73Ug0BuI2iNplcosy8ECMirwLYTH8lp3MjhWA1TXESM4Ft_Mqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d36518f3c9.mp4?token=nSe-_xI01e5umzDQfykACZWg8MsdHqNvBlkU6ytw_hrzn-lxUIxQVc5CFEQyANZyQvLIoJRKab4dKafDoqRMZCPPOMpcI6Jf3U2DO-BR7AKwIxsIVu3bNEs_Kx7XnW4sfaTXPNCE_siOWQeUINXS64N8PZEISySaPH3rM2X9BxoFANhzK7qkDbT9tywJww7DKv96jYGwact1FGCUXFB6kkhyzqkW8VBnRz6l3g9FP9G-PH49wDs7nT7f7nrWTew6a_Ilz8Q-S8zT1kx6E2vCfbxKMLbJ9dUWXbn_73Ug0BuI2iNplcosy8ECMirwLYTH8lp3MjhWA1TXESM4Ft_Mqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی :
40 هزار ایرانی تو عرض دو روز برای یه توافق هسته‌ای یا باز موندن تنگه هرمز جونشون رو از دست ندادن.
اون‌ها برای آزادی و دموکراسی جونشون رو فدا کردن. اما عجیب اینجاست که تو هیچ‌کدوم از این مذاکرات، اصلاً دیده نشدن و هیچ اسمی ازشون نبوده.
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/15240" target="_blank">📅 15:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15239">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/15239" target="_blank">📅 14:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15238">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">راستی از لحظه ای که ادمین بیارم به شما اطلاع میدم ولی دایرکت رو هیچ وقت به هیچ کسی دسترسیش رو نمیدم و پیامهای شما تا ابد فقط دست شخص خودم امن خواهد ماند.</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/15238" target="_blank">📅 14:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15237">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دنبال شخصی هستم که برام ویکیپدیا بیاره بالا خیلی کم لطفیه بعد از حدود ۲۵ سال فعالیت در حوزه تک و کارهای انقلابی بسیار بزرگ، صفحه ویکیپدیا نداشته باشم و افرادی که خودم به مارکت آوردم و معروف کردم داشته باشند. امیدوارم یک فرد فوق‌العاده قوی در این زمینه کمک کنه و واسم بسازه.</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/15237" target="_blank">📅 14:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15236">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15236" target="_blank">📅 14:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15235">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فقط ‌یک پیغام</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15235" target="_blank">📅 14:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15234">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60e87c2bd5.mp4?token=KmewsB3AXucgZYJYHx94FZ8394h9-IqQyKhKtMKq6zBMsiubirUtGFkaGgLUqc2gMCNH7KYQC9JGiv_N9CMU7hZe2MdpaxAwf_y4g1KO_G_KzqKvjgCtlIlx740PZ1KJwU7KFOQZk_P1RQe2pjrFA5iZR89j3ZOB8pYcpaO7UFtZ4UkHRRJI-abHRqXl5W31t1UwAleoQv36JNgbczGVbZw_RBrCQc7kHnERHOpi1jN72aDKT9ILZnpvPeL11EnYC_oYkD-7VrYlGwZ5S82_5QXK3OAEzxNI38h2qRXmf4EVjDTArSkJqWo4Zv-a8VzjbSySxknDCznn9_3JMqUTlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60e87c2bd5.mp4?token=KmewsB3AXucgZYJYHx94FZ8394h9-IqQyKhKtMKq6zBMsiubirUtGFkaGgLUqc2gMCNH7KYQC9JGiv_N9CMU7hZe2MdpaxAwf_y4g1KO_G_KzqKvjgCtlIlx740PZ1KJwU7KFOQZk_P1RQe2pjrFA5iZR89j3ZOB8pYcpaO7UFtZ4UkHRRJI-abHRqXl5W31t1UwAleoQv36JNgbczGVbZw_RBrCQc7kHnERHOpi1jN72aDKT9ILZnpvPeL11EnYC_oYkD-7VrYlGwZ5S82_5QXK3OAEzxNI38h2qRXmf4EVjDTArSkJqWo4Zv-a8VzjbSySxknDCznn9_3JMqUTlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه سر حال هستین بریم برای مرحله بعدی کارا و گسترده تر کنیم
👍
یه ریکشن لایک بدین پر ریزون باشه تا بگم</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/15234" target="_blank">📅 14:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزیر جنگ آمریکا: به طرف ایرانی اعتماد نداریم و آماده هستیم در صورت لزوم حملات علیه ایران را از سر بگیریم
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/15233" target="_blank">📅 14:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a485ae7493.mp4?token=pUi0LNKYtWYKnhlF4Lg20oeM-sFaqLNESdKZUxyJ-5u4c6n_x-FiWaw_QUVIGwif5TIo6rlx0-xQFYjZU9Y4R9uw_5UOuCSCR758QkvMECvB9ZXcqUTWmsLSSEERBuJ4OU7-u4ghSPDZeO1LbvSQFfgixm8PQrTtv8uQS9GmDirPbF1_XqLVnxyGD_1FlJCHj2VAHFGGdpSI2-U7lPFIYJyRPAxwCvZZeMO4WVLEkzUjnSTF5zZhEu3mV35tUW4MkWJ53EACwHo-OmxDlWjqldM2kbUtGDYS4IhaBrlSRvuMaXVP2yKIpMyzfwdzvpKng489KNPoToD5Ui-V37Ok9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a485ae7493.mp4?token=pUi0LNKYtWYKnhlF4Lg20oeM-sFaqLNESdKZUxyJ-5u4c6n_x-FiWaw_QUVIGwif5TIo6rlx0-xQFYjZU9Y4R9uw_5UOuCSCR758QkvMECvB9ZXcqUTWmsLSSEERBuJ4OU7-u4ghSPDZeO1LbvSQFfgixm8PQrTtv8uQS9GmDirPbF1_XqLVnxyGD_1FlJCHj2VAHFGGdpSI2-U7lPFIYJyRPAxwCvZZeMO4WVLEkzUjnSTF5zZhEu3mV35tUW4MkWJ53EACwHo-OmxDlWjqldM2kbUtGDYS4IhaBrlSRvuMaXVP2yKIpMyzfwdzvpKng489KNPoToD5Ui-V37Ok9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد محبی فوتبالیست تیم جمهوری اسلامی که در خوشحالی زدن گل به تیم نیوزلند، به مردم شلیک کرد، رفته و عکس مهسا امینی رو کنده و انداخته توی سطل زباله...
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/15232" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اگه سر حال هستین بریم برای مرحله بعدی کارا و گسترده تر کنیم
👍
یه ریکشن لایک بدین پر ریزون باشه تا بگم</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/15231" target="_blank">📅 13:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی اعلام کرد:
در حال حاضر، سطح تماس‌ها و ارتباطات با ایران در پایین‌ترین حد خود قرار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/15230" target="_blank">📅 13:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/15229" target="_blank">📅 12:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15228">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزیر امور خارجه اسرائیل : روابط با مسئول سیاست خارجی اتحادیه اروپا را قطع خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/15228" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15227">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">منابع العربیه گزارش دادند «نخستین دور از مذاکرات فنی مستقیم واشینگتن و تهران فردا در زوریخ سوئیس برگزار می‌شود.»
به گفته منابع این مذاکرات فنی میان ایران و آمریکا شامل جنبه‌های حقوقی و قانونی مربوط به رفع تحریم‌ها علیه ایران خواهد بود.
منابع العربیه خاطرنشان کردند گفت‌وگوهای فنی ایران و آمریکا پرونده دارایی‌ها و وجوه مسدودشده ایران در قطر و همچنین پرونده هسته‌ای ایران را در بر می‌گیرد.
قرار است در نشست‌های مذاکراتی غیرعلنی و اعلام‌نشده، پرونده‌های مرتبط با لبنان و حزب‌الله نیز مورد بحث و بررسی قرار گیرد.
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/15227" target="_blank">📅 12:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15226">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOjnLL806drODCUL4y76n6SX6tYbIWR5tLgw4mwejyPmbiXfWNTAmvsL7mZabMyu8nUAPKJlnwnXFM5zt1oo64oKywjGE5ZbDTwb2bxOidLIEb62ONXBrdKpIseo1sCa2aNgc1zDaA_cueoyfqmQNLxbtGh2T-NN3m1RDxBvh6Ltp8RiuKR3rm3cGxCO1rVODiROcKKcBaMR2IvwwUgwF1nGCL_2HZZeoFTKVhn_w1t7-c7sz_f9IJdkPnNfcIVGhWjXaD-qT1TleG1tU_7jGT3wOS-Ugca0ssjXaqwrRAioh3zT5slfU2a-qA5iZsIj9Mw4WdPypsr4o-CiAPjJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث:  این احمق‌ها که فکر می‌کنند من در قبال ایران به اندازه کافی سختگیر نبودم، در حالی که بازار سهام به تازگی به بالاترین حد خود رسیده و قیمت نفت «به سرعت در حال سقوط» است، یا حسودند، آدم‌های بد یا احمق. آمریکا را دوباره بزرگ خواهیم کرد!!!
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/15226" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شهباز شریف هم یادداشت تفاهم ایران و آمریکا را امضا کرد @withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/15225" target="_blank">📅 12:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15224">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b5b52d5b0.mp4?token=eXMPKBRudu84vLoVe-ziqGZ5ngIzMhrBrrJ8nOpMpvG5T0DlsbqMeRlxm1EGEkRuEHsMBm-wPOcRNY0Mc4Kd49EDBcRPL6SxhRsK9nUdzRbS0KNGmDDJMoKsRbhskqddBQktIoJeSEv-JzwxoxAY823tWcRQEl06NjHk_XapGzE_Hefw5gW03Mq6QylENXn8ZGybKgq7DpxgK0NLpo4hak8N__7g08TDAnMoogdJTe_3GmC2hJ3U0UsvdOOPZG1OH3H7iW0NKd2jsB8vB0O4JWxYP93dQduhrTcZk2V8-QzrVq16JAlyYKNoWfmFYKE95GcWJxWO9j8RTYSV0R87VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b5b52d5b0.mp4?token=eXMPKBRudu84vLoVe-ziqGZ5ngIzMhrBrrJ8nOpMpvG5T0DlsbqMeRlxm1EGEkRuEHsMBm-wPOcRNY0Mc4Kd49EDBcRPL6SxhRsK9nUdzRbS0KNGmDDJMoKsRbhskqddBQktIoJeSEv-JzwxoxAY823tWcRQEl06NjHk_XapGzE_Hefw5gW03Mq6QylENXn8ZGybKgq7DpxgK0NLpo4hak8N__7g08TDAnMoogdJTe_3GmC2hJ3U0UsvdOOPZG1OH3H7iW0NKd2jsB8vB0O4JWxYP93dQduhrTcZk2V8-QzrVq16JAlyYKNoWfmFYKE95GcWJxWO9j8RTYSV0R87VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهباز شریف هم یادداشت تفاهم ایران و آمریکا را امضا کرد
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/15224" target="_blank">📅 11:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15223">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حسن روحانی هم اومد:
اسرائیل احتمالاً سعی می‌کنه با ایجاد تنش( در لبنان و …)، توافق ایران و آمریکا رو به هم بزنه؛ همون‌طور که قبلاً هم برای ضربه زدن به برجام تلاش کرده بود…
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/15223" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15222">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزیر دفاع آلمان اعلام کرد این کشور در حال اعزام دو کشتی مین روب به دریای سرخ است تا برای یک مأموریت نظامی احتمالی در تنگه هرمز آماده شود.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15222" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15221">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9baDUd3Df-AAYE3hxap30gzn1mwHDUzeamdPOUhCSA4AhIcgeMEpurcXNt7yDev0t0COOhEWZlbg-2nnYqdYPzZSLWGwK9uXoqLNFUMnlWLLedhm3uBn5HBxIwTTnerQEwMTAh2gGnQ7gVxEUF1pa78lWbmIVaIe7sgkQpVwYza-1XWahNyzdHwHFdlJSQ-GZ-jfsAiEtvzJfE-UVV1haM0HqRPKRhxCP1NfEfXkIm2bBXuUr_VS3SlyAayj1bslbhmzO1e9ztL-77uRkXhI_ZHFMKTQi0qbyUAfYlzUUqjPDrQYzEF6Kq21RvV7QjkAJ5FaOhxEuyBzf-GsrVpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری متفاوت از ترامپ و مکرون در ورسای
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/15221" target="_blank">📅 11:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15220">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رویترز: اسرائیل قصد عقب‌نشینی از مواضع خود در جنوب لبنان را ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15220" target="_blank">📅 11:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15219">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گروسی (مدیر کل
آژانس بین‌المللی انرژی اتمی
) : در مذاکرات سوئیس شرکت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/15219" target="_blank">📅 11:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15218">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/15218" target="_blank">📅 10:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15217">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اتاق جنگ با شما : درود و خسته نباشید
ما که می دونیم به قاهره نزدیک میشیم
حالا تو این راه تفاهم امضا بشه یکم از لحاظ اقتصادی و گرونی بهتر بشه
به نفع مردمه که یخورده تو این مدت نفس بکشن
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15217" target="_blank">📅 10:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15216">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15216" target="_blank">📅 10:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15215">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آکسیوس: رسانه‌های نزدیک به نتانیاهو به دلیل توافق با ایران، حمله به دولت ترامپ را آغاز کردند
مجری شبکه ۱۴ اسرائیل: ویتکاف و کوشنر یهودستیز هستند و اسرائیل را فروخته‌اند
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/15215" target="_blank">📅 10:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15214">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlZO4b4IlPloYNB8DzQWuWLOXplMeIk9QglNmdvd0Pz-0hyJ0nXGltArA7Ieq2U63isxiyljptb9s2NtumrtWDnBrSZfNbIPLAHRAdnLwkWH-4T26T7ZSBV_KQAp2UeV5xNyb7VJqdlxmISuX2SmB3CQAHCovXTWyskqhGXYeQzggYvuo8N6avwirA6mlHa-sakSvqlAIOZXqVhcRsATyQTTWh2Aa0CVjCOYpIbl2qebRL3s2K3TJjgtVCAzqyXucH-utsumDG4_3XBhg1UatYTZ8AeaZm2AK2ThE0KjrJ3lBaUgR1ed7CJmdjkLY6OBMK4L5aQNpbcupGBJfSOL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای مضحک پزشکیان که مانند یک شکلک کارتونی با دماغ بزرگ و دست دراز شده برای گدایی است.
@withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/15214" target="_blank">📅 10:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15213">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دولت سوئیس اعلام کرد که روز جمعه نشستی با حضور نمایندگان آمریکا، ایران، پاکستان، قطر و دیگر کشورهای مرتبط برگزار خواهد شد تا مذاکرات مقدماتی انجام شود.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15213" target="_blank">📅 10:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15212">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وال استریت ژورنال: ترامپ در حال از دست دادن تندروهایی است که زمانی از جنگ ایران دفاع می‌کردن
@withyashar
الجزیره: موجی از خشم سیاسی واشنگتن را بر سر توافق با ایران فرا گرفته</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/15212" target="_blank">📅 10:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15211">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سناتور بلومنتال: سنا قطعا توافق با ایران را تصویب نمی‌کند
محکومیت دو حزبی برای یک توافق ننگین عجیب نیست که شبیه «تسلیم بی‌قید و شرط» است، نه توسط ایران، آنطور که ترامپ خواسته بود، بلکه توسط آمریکا.
بیش از ۳۰۰ میلیارد دلار ثروت بادآورده، لغو تحریم‌ها، فروش نامحدود نفت، عدم بازرسی یا تأیید کامل. همه اینها به خاطر وعده‌های مبهم و غیرقابل اجرا در مورد تسلیحات هسته‌ای است که ادعای ایران برای پیروزی در برابر شیطان بزرگ را تقویت می‌کند.
هر چیزی شبیه به این توافق به محض ورود به سنا از بین خواهد رفت. برای اینکه اثر اجرایی داشته باشد، باید در اینجا تصویب شود.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/15211" target="_blank">📅 10:08 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
