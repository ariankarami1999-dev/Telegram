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
<img src="https://cdn4.telesco.pe/file/vKaaqCogmf1Zy81Ibog-afdJ1RQ_JLfTU7M8wvUGUESKJ82TKU2zuvBl0qOadCxLCJ9BjiC4G8g2HRBD1mQ3d9B3g0qEfAEarBqsHEGE_DXfxkWlIcPlvpNePxGQ8pLOdQo2oDPyvWAKOMHIS9T7ujVDbq4xUZjKZ_CcFShHiZ_KKdhzfetGfkMU06Y3EoraGT9ecg1hW6QlT3RQnfk7CnTbPIWwn0u004GaIM9bAHmNNxO1va_kamBjBotZ2G2Pu0iCkYp0kwvI-dTZkZXpZ9vc2rIzb7plhZt2vgV3GiqXF7oMbPrC1qIdReDDHng_97BXFFchdPfoTtGiD3bwfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 15:23:35</div>
<hr>

<div class="tg-post" id="msg-454199">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vbu4lGF0o4CiSaM-SEfUx8fKTXXv1cgzyIqT8-0WqMCOQQffdodYxylu5q8uYjiu0VQo88EfrIdl68cNTM1TPgS0FKexAn7YmwUhrCb7onzFzLqDiLUm3vzRmD7CVTa7YQXrO_gJK0pUmGh0_kpcL_EREOlnyvi3YaPo-H8Tesm2OyBXzvSHB3tcNyLjsldc2MQ-4iuY-UqZ7VXorpvUgphp4lF44u70AAnQbssLESJDnjWLCycmU6EnA-aIOlGO4wvk8-xwsGf4ocuf-DywGJZIhYCEpR6V1ybPtEi3vz6IFqtomexT89aC6dcqg2HjelY8PbMH_XdprrGb4uapfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز گوشت را در آمریکا گران کرد
🔹
مارک وارنر نمایندۀ ایالت ویرجینیا در مجلس سنای آمریکا می‌گوید: «قیمت گوشت گاو در آمریکا ۱۲ درصد و مواد غذایی ۴ درصد افزایش یافت».
🔹
اختلال در حمل‌ونقل دریایی از طریق تنگه هرمز دلیل اصلی رشد قیمت از سوی کارشناسان این…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/farsna/454199" target="_blank">📅 15:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454198">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌ کرمانشاه چهارشنبه تعطیل شد
🔹
استانداری کرمانشاه: با تصمیم کارگروه مدیریت مصرف انرژی استان، ادارات و دستگاه‌های اجرایی دولتی، بانک‌ها به‌جز شعب کشیک، بیمه‌ها و نهادهای عمومی غیردولتی روز چهارشنبه ۱۴ مرداد ۱۴۰۵ تعطیل خواهد بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farsna/454198" target="_blank">📅 14:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454197">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19878aefa0.mp4?token=XEdgZ7882-NnyxbBg7daczgObH6eUcsxoST3xdeTJZ7skBhtQFVR4jF9_VJD9tROyDqcHxCh7-UQciVVhoRk8_F26yvXM-eNRmRjnZ-JiRDemOG3T8n8zMnIZXt0TpwUmQ25QICuvwFbeCyhIHrzUQwGw5XwBaiuMOMoyzDfSLkY7axuWBO3tlKzNTsFuL5yVFjCHf7pgy5Ksd9O16h2y2iYd4bZ9vd9HuVKpZyFuVfx3wkTRy-flvHwz3dIBMkFNKCfF4mOeuS3wKE9XwzNXk-ikFgaT5yuZ8Zp9Hz5qPwEGxNb5UMypzfBCngjVcXt-FJg6Oa-j4nj-V0owICsqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19878aefa0.mp4?token=XEdgZ7882-NnyxbBg7daczgObH6eUcsxoST3xdeTJZ7skBhtQFVR4jF9_VJD9tROyDqcHxCh7-UQciVVhoRk8_F26yvXM-eNRmRjnZ-JiRDemOG3T8n8zMnIZXt0TpwUmQ25QICuvwFbeCyhIHrzUQwGw5XwBaiuMOMoyzDfSLkY7axuWBO3tlKzNTsFuL5yVFjCHf7pgy5Ksd9O16h2y2iYd4bZ9vd9HuVKpZyFuVfx3wkTRy-flvHwz3dIBMkFNKCfF4mOeuS3wKE9XwzNXk-ikFgaT5yuZ8Zp9Hz5qPwEGxNb5UMypzfBCngjVcXt-FJg6Oa-j4nj-V0owICsqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعترافات امید بهزاد و پوریا صفوت عاملان رژیم صهیونیستی که صبح امروز اعدام شدند  @Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/454197" target="_blank">📅 14:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454195">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVfs6zatnasa7Jj6BMUCdfkEVVRYrhngoMXJ8L9uy8-LXOJwgOjL1LNHsrHLWmsecKyAxeUmdRH6v1EDXwAGjHnLS8SvqYMiWK8lB7vfMAJ20V_WKTCkFIPj5vh6zfZhzoUQXELEQRVGOgEVboM_r5wYnlbiN1IQlUkpI-__Q2vNIe-4pmiM2PdwMRrNTwmcImq0hKpsTR4GIIqw12K7MFSHrJSHnVWniYP-qZS8TArER-VDyAGjcW7GOvGnuaxwo__Zi63sNtaFa1DHo3SSTIbOctLXqjKKA7Gav2CD2KxWgEAK1QpE5yoPU9Me3AExrs-mhUJQi3RzvLMm415uCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فردوسی‌پور را باز کنید
🔹
«من را در صداوسیما ناجوانمردانه کنار گذاشتند. از چه می‌ترسید که اجازه نمی‌دهید کار کنم؟ من بله‌قربان‌گو نمی‌شوم، حتی اگر بخواهید مرا بازداشت کنید.» این جملات را عادل فردوسی‌پور پس از بسته‌شدن وبگاه «فوتبال ۳۶۰» در برنامهٔ ویژهٔ…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/454195" target="_blank">📅 14:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454194">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4270bcb2cd.mp4?token=urCcf2AWiPsIOVyBIV2W9CYi7prte8MtFshXRtP-9ZtJrFMi2A5ecHmdvIPZUxzX9mV9uKNV8_2vnMWSZmykrNsaOQyvIDKmSpdDMSaXydpF1U5qyM_KxL7BePfiaOp-xm30_mO8GLFomAYuirUtCtRIovA8Rqzmg01_4bdrmk-fQINmXQ9D_EbTA_HazS5NFP1MTR3YkucJVQkYg4w-tVqwXoK4B6J6z0KBegkX6DNcluP5hwtzlBo3py7QDDnBXARm-vtKrTGz3vEn9mw6ZX7aLxAIEJgfe9LUmncMalAJIJ4TGlLFLvqkUDgckNzPLEGmfXsW2sgTLQODA0jKkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4270bcb2cd.mp4?token=urCcf2AWiPsIOVyBIV2W9CYi7prte8MtFshXRtP-9ZtJrFMi2A5ecHmdvIPZUxzX9mV9uKNV8_2vnMWSZmykrNsaOQyvIDKmSpdDMSaXydpF1U5qyM_KxL7BePfiaOp-xm30_mO8GLFomAYuirUtCtRIovA8Rqzmg01_4bdrmk-fQINmXQ9D_EbTA_HazS5NFP1MTR3YkucJVQkYg4w-tVqwXoK4B6J6z0KBegkX6DNcluP5hwtzlBo3py7QDDnBXARm-vtKrTGz3vEn9mw6ZX7aLxAIEJgfe9LUmncMalAJIJ4TGlLFLvqkUDgckNzPLEGmfXsW2sgTLQODA0jKkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: تا الان ۳ میلیون و ۲۶۰ هزار زائر از کشور خارج شده‌اند
🔹
۲ میلیون و ۲۰۰ هزار زائر اربعین به کشور بازگشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/454194" target="_blank">📅 14:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454193">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b99256aa.mp4?token=t-hctHVO-3Zm7HhmzLeTWRRrE8SP9H_5XpQXHvOu1D9ifZyGsmn5DLDhg1wjjzw7ennPAhDhFj4Bt1u_XiK8iouXcxyvEVzqphwxk1D2o-5Z4Dd9XfqhoqPqNbVwYwM7KdGZHlISUNx72Kggj8cSUA51u_l4VMn0XfeOo-548fG40LxPXo0JnnzBPwKRuGRv0EIcuuHYntx3iK3A0PXJ8RzGP_tG71hSegKTj4rX4GP1GdKXm2D0VbV6TwD7JLD3bhBmXs1VqEaIC1e3fetNYEpUdhPN4NIqWOXXNs7S287KfYn5K9ctmrxyBgR6efninW4riwm3GprNEfwYBhbKfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b99256aa.mp4?token=t-hctHVO-3Zm7HhmzLeTWRRrE8SP9H_5XpQXHvOu1D9ifZyGsmn5DLDhg1wjjzw7ennPAhDhFj4Bt1u_XiK8iouXcxyvEVzqphwxk1D2o-5Z4Dd9XfqhoqPqNbVwYwM7KdGZHlISUNx72Kggj8cSUA51u_l4VMn0XfeOo-548fG40LxPXo0JnnzBPwKRuGRv0EIcuuHYntx3iK3A0PXJ8RzGP_tG71hSegKTj4rX4GP1GdKXm2D0VbV6TwD7JLD3bhBmXs1VqEaIC1e3fetNYEpUdhPN4NIqWOXXNs7S287KfYn5K9ctmrxyBgR6efninW4riwm3GprNEfwYBhbKfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز عراقچی راهی سفر اربعین است</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/454193" target="_blank">📅 14:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454192">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur-fELOY2FZOjdiWhOcLHqegFrlBfnYdXVCn_AVIgjAqEJ_lxmkemhMI8KRFCL5600gFN0pf5lPxEsEjTIun7r6obCun7Z0o4y-AgIpJt_4EJRyKzUd6AA-72uTT9VrhcC1kY6eYhy60XBf6yFXWVPM4-xQ8qBbEggeVQbacmNLkc3UJX7PszIqFHXyyopEuX20N76wETl5iLI7pXgHksMT7_AogbqDAXjn9tv95QPGJF24zhMMH4fLfgZZxVdDYh_Fknm_nphNYKflmcSoIdACmDhsQ50XzGibuhA3BuyzBmvkrUrcugCT2yYn4xzXl4gooGAJblSmWQYWmHhetNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت مذاکره با آمریکای ترامپ بن‌بست است
🔹
نگاه دولت فعلی آمریکا به مذاکره با ایران نه یک نگاه تاکتیکی و نه حتی صرفا راهبردی، بلکه شامل عناصر کاملا ایدئولوژیک است که با نگاهی به ماهیت آن، می‌توان نتیجه هر مذاکره‌ای را از پیش دانست.
🔗
شرح کامل این یادداشت را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/454192" target="_blank">📅 14:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454191">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba17c5d31.mp4?token=ir1zNN4T4ZLjrbJ9UZZqEYfGKAPXkUTqK1o2qv3NyD53Iv926j5ULKCZVTFI9P7W-Bjh2NSeD09xR_ZMIkLfs4iGVT378uokkajTrGzukllfkY9H8qqrm6RQFopq1qcWKkwTJ7NyFbwkb8er3lEdP8lJ9t-kF_HRuFGGs2lbZ10psyaZ-VWbx2D0QPG5PRv8R4eqhB66tMt6-mQ6Ov57jQ0UTEuUecdo5ULjrdlSnpDfzt5j-Eqd3AITcwPaqxjWZOXWUbIre4fPGeg29Jmz-ngRCBSMxs36jY9TGi_kW5RYMLACv8q7fl1USoesd302AfUz1Y8g30WSzgWW5U4jKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba17c5d31.mp4?token=ir1zNN4T4ZLjrbJ9UZZqEYfGKAPXkUTqK1o2qv3NyD53Iv926j5ULKCZVTFI9P7W-Bjh2NSeD09xR_ZMIkLfs4iGVT378uokkajTrGzukllfkY9H8qqrm6RQFopq1qcWKkwTJ7NyFbwkb8er3lEdP8lJ9t-kF_HRuFGGs2lbZ10psyaZ-VWbx2D0QPG5PRv8R4eqhB66tMt6-mQ6Ov57jQ0UTEuUecdo5ULjrdlSnpDfzt5j-Eqd3AITcwPaqxjWZOXWUbIre4fPGeg29Jmz-ngRCBSMxs36jY9TGi_kW5RYMLACv8q7fl1USoesd302AfUz1Y8g30WSzgWW5U4jKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر بهداشت: طرح پزشک‌خانواده از این هفته در روستاها اجرا می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/454191" target="_blank">📅 14:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454190">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNf30l0NgGlxoHsfBFlCcPj7mKNiaPsjb0r9RO0AzqmQ1mjiWeXe3VuOusHH2MgaxirBb8K47cMXmVRvX80oCSLwyQPcu3CceI00F86fdKI8iZ6RqmOvCPwBmbLFMA5yObpvNYSRwqYo39ngXY74CRnHbAhXpQOfZf278pL3wTmpII0I2xpN3ITasMHh-w4cxxRePBlQmZd_eazUOzb0bBy5-h8_WtUsu_MK54VdyWySyAOMCG_kC1n7NJf3lsSty8Ffqaa8Fz68Bx79mi0X6MTLmuTNUNLZipBAWbYkXW0ghefnfm_vp3vt5wYB63zTzgc1gONxeiA62m1a4pLG6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکورت هوایی آمریکا در تنگۀ هرمز
🔹
پایش داده‌های ناوبری هوایی نشان می‌دهد که هواپیماهای پشتیبانی نظامی آمریکا در خلیج‌فارس فعال شده‌اند.
🔹
پیش از این هم چنین پشتیبانی‌های هوایی هر زمان که نیروی دریایی آمریکا تصمیم داشت نظم ایرانی تنگه هرمز را بر هم بزند، دیده شده بود.
🔹
هنوز کشتی حامل گاز قطر که جمعه‌شب می‌خواست با اسکورت آمریکا از تنگۀ هرمز عبور کند، در بخش جنوبی این آبراه زمین‌گیر است.
🔹
براساس تصاویر ماهواره‌ای، هواپیمای هشدار زودهنگام و کنترل هوابرد آمریکا از ساعات اولیه امروز فعال شده و به‌سمت تنگۀ هرمز در حرکت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/454190" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454189">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H46eCeYWJx5GDcOuMpVACoT4RRy1rdBdgK9vKpvklQqyM_bcCUlInHYtcxXNe-HhGQu5xwXAfnk90tWt51RY4JActBJX_-rDzQqTvMkpFVg3H3AfSAXHjW0Uvj4RZrpBycCgTIAuaeIfnMIxUwDxSwkeI5VmvkV8RmizPsHpGjH4spBZKdNxb5lZ-854O7GQcTd64AQ23T_99M2FKprrd2olNTsZ9ie2ZbIoLuG9ouCMJImbkyZnT2Iqrs5wigd0O-i7Dfcpg-eO9fEuBJF452thfyY_LT9JGBmQBbytsa9x935srvacjyOf3bWljntDOhqNE3NclHZA9bG8Hbwqlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک تجارت به کاهش ۱۰ هزار میلیارد تومانی سود پاسخ داد
بانک تجارت درخصوص خبری با موضوع تعدیل صورت‌های مالی این بانک، با اشاره به ابلاغیه بانک مرکزی به بانک‌های کشور در خصوص اصلاح رویه تسعیر دارایی‌های ارزی، به تشریح اجرای دستورالعمل مذکور در بانک تجارت پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/454189" target="_blank">📅 14:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454188">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrbNAWXQLRbqqraxBQvdyLrDmB2S2VhsS3EHYR1hzlDu_J0qpu_BanhqgZ0TpWBkG-w4hEKZel1JQ1TQFXbKPcar6Rw0Bxb3Jv-_FdxKuwAO2SXvfokmTyx6ZodKujy4dbyVW68U8xjFFAi7mPNzQbW3EUFMRtA9GVU6FZPuzNoROoeRgxkyUWpQDrrvIFL-MijPKPSHKIVBKs4fThn45R-I8xNK0AexC2Is8x-b0QRmi9eLjwlL0bsa92BNOgwObSu5hZ2Wcosd48uVRtR-YO4m7IDCecTOc_0jJAGOviB6hDGm6lt2h906poaduWf77izMnpYz40HyCcr0fYdwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
فهرست برندگان پایان دوره قرعه‌کشی طرح «فرالیگ» بانک رفاه کارگران اعلام شد
🔹️
با پایان طرح "فرالیگ" بانک رفاه کارگران، ویژه مسابقات جام جهانی 2026 و جمع‌بندی نهایی امتیازات شرکت‌کنندگان، اسامی سه برنده نهایی این طرح اعلام شد.
🔹️
بر این اساس، نفرات برتری که موفق به کسب بیشترین امتیاز در این طرح شدند، جوایز ویژه خود را به شرح زیر دریافت می‌کنند:
🥇
نفر اول: آقای حسن بابالوئی (برنده جایزه ۲۰۰ میلیون تومانی)
🥈
نفر دوم: آقای احمد نصرت‌فر (برنده جایزه ۱۰۰ میلیون تومانی)
🥉
نفر سوم: آقای مسعود نجفی ده‌پهنی (برنده جایزه ۵۰ میلیون تومانی)
🔹️
بانک رفاه کارگران ضمن تبریک به این برگزیدگان، از مشارکت تمامی شرکت‌کنندگان در این طرح قدردانی کرد.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/454188" target="_blank">📅 14:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454187">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/454187" target="_blank">📅 14:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454183">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df7882a7db.mp4?token=lzWpPsxqm7-hh91PpcpdDtH_3669wVPiXe4Q1Sm-bXLy9Af93Qy8md53d4CbzoAJaeI6RmyyI-Q1zAOr6dyXg6EWLNKjIWxcygd0XmU4BP5qagK5O0IOQwuY0tIDq9lPGVIJBXfAbYUrNtXuRWAwHjPyJwa2iklWyX5qIuyEq_UGvqJbyiivff479XJGxkBF9VrsBLMaiwtdIdOvIOtCbs-ZBKrGiQf0eg4CJvWEPn97h0buBi8ZiBvU3b3YPYHwpr6Sr8mb90Rtf4X6MO0w-AaRpfaTy2BelzT_w5MUy0fJzWLJxfdRIxWTKB9P6qWORCkac0kYSBLLFiQ03zzGXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df7882a7db.mp4?token=lzWpPsxqm7-hh91PpcpdDtH_3669wVPiXe4Q1Sm-bXLy9Af93Qy8md53d4CbzoAJaeI6RmyyI-Q1zAOr6dyXg6EWLNKjIWxcygd0XmU4BP5qagK5O0IOQwuY0tIDq9lPGVIJBXfAbYUrNtXuRWAwHjPyJwa2iklWyX5qIuyEq_UGvqJbyiivff479XJGxkBF9VrsBLMaiwtdIdOvIOtCbs-ZBKrGiQf0eg4CJvWEPn97h0buBi8ZiBvU3b3YPYHwpr6Sr8mb90Rtf4X6MO0w-AaRpfaTy2BelzT_w5MUy0fJzWLJxfdRIxWTKB9P6qWORCkac0kYSBLLFiQ03zzGXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چندین ایالت آمریکا همچنان در آتش می‌سوزند؛ ۶۰ هزار نفر تخلیه و دست‌کم ۶۰۰ ساختمان نابود شدند
🔹
مقام‌های آمریکایی اعلام کردند آتش‌سوزی‌های گسترده در شرق ایالت واشنگتن، به‌ویژه در اطراف شهر اسپوکن، تاکنون دست‌کم ۶۰۰ خانه، واحد تجاری و دیگر ساختمان‌ها را نابود کرده و موجب تخلیه حدود ۶۰ هزار نفر شده است.
🔹
آسوشیتدپرس گزارش کرده که آتش‌سوزی‌های اطراف اسپوکن در روزهای گذشته حدود ۲۱ کیلومتر مربع را در بر گرفته و بخشی از ده‌ها آتش‌سوزی گسترده در غرب آمریکاست که توان نیروهای امدادی و آتش‌نشانی فدرال، ایالتی و محلی را به چالش کشیده است.
🔹
در این گزارش آمده که همزمان در غرب ایالت آیداهو و شرق اورگان نیروهای امدادی برای دهمین روز متوالی با استفاده از بولدوزر و بالگرد در حال مهار آتشی هستند که نزدیک به ۱۳۶۰ کیلومتر مربع از مراتع را سوزانده و بیش از ۶۰۰ خانه و ۸۰۰ ساختمان دیگر را تهدید می‌کند.
🔹
همچنین در مرکز ایالت یوتا، وسعت یک آتش‌سوزی بزرگ در ۲ روز گذشته از حدود ۴۱ کیلومتر مربع به ۱۴۵ کیلومتر مربع افزایش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/454183" target="_blank">📅 13:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454182">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هرمزگان چهارشنبه تعطیل شد
🔹
معاون منابع استانداری هرمزگان: به‌دلیل تداوم افزایش دمای هوا و ضرورت مدیریت مصرف انرژی تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی چهارشنبه ۱۴ مرداد تعطیل است.  @Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/454182" target="_blank">📅 13:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454181">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf79599adc.mp4?token=GkzXZk2Amlu_VzCgGp-LmXrTaJvAieZtQU7Jw63TYjhwoIA46Fgr8aOOQ16jpDEVGa9L9gmXWmZLqfXPWq-vFrtwRxO9oj2ZONS7-izIGIZjjdhCJiVPxdymPgosz8xi2aXUWJ5T5Wn1Ha6lD7kX8RLn14tnfWfWYCV0-1upqGiReKJvWRzu00CYajtMfk-DCjeno9La75--Tf5OzymAmIVSqNcM99V3LLERwcVWfFfujs4MpJQxFQeSevhzhPNIdZSSZtGC_C1zGEstoDpZfNynU1lszu5F1aeVgXk5YYz8F2TzYsOUop9piYZ7mVx3R_Qpwl7XQed9LRsFYpHqwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf79599adc.mp4?token=GkzXZk2Amlu_VzCgGp-LmXrTaJvAieZtQU7Jw63TYjhwoIA46Fgr8aOOQ16jpDEVGa9L9gmXWmZLqfXPWq-vFrtwRxO9oj2ZONS7-izIGIZjjdhCJiVPxdymPgosz8xi2aXUWJ5T5Wn1Ha6lD7kX8RLn14tnfWfWYCV0-1upqGiReKJvWRzu00CYajtMfk-DCjeno9La75--Tf5OzymAmIVSqNcM99V3LLERwcVWfFfujs4MpJQxFQeSevhzhPNIdZSSZtGC_C1zGEstoDpZfNynU1lszu5F1aeVgXk5YYz8F2TzYsOUop9piYZ7mVx3R_Qpwl7XQed9LRsFYpHqwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاسوس موساد: باز شدن تنگۀ هرمز بستگی به خواست ایران دارد
🔹
منشه امیر، جاسوس و سخنگوی موساد: ایران قدرت بستن شریان‌های حیاتی جهان را در اختیار دارد!
🔹
آیا تنگه هرمز باز شد؟ مسلما نه! آیا باز خواهد شد؟ بستگی به خواست ایران دارد!
🔹
حکومت ایران به تاکتیکی موفقیت‌آمیز رسیده؛ آن‌ها می‌گویند ما موشک داریم، می‌توانیم همه تأسیسات کشورهای امیرنشین عرب و اسرائیل را نابود کنیم!
🔹
خبر رسیده موشک‌های پاتریوت آمریکا کم شده است؛ بنابر تمامی این عوامل، ترامپ بار دیگر جنگ را عقب انداخت.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/454181" target="_blank">📅 12:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454180">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKL3xH4SAV8yjlp4bECHrZexYgzZdU4z7Qqu3T5ioXkJYRrYz_YZkmhXlQNwiJVHPvExIu_7yj-2m_KCBFPrEWJbSUszKZbXuE58qzW_v2iR9c6Ud6kCSkrNV8vJJuX5MVNeDnwQ4_9RBbJ6FjjWeH3JmD14zcRjit1u7BKo8z_SNwg7FJth52No97n4Ev7RBwAuoQjAiUcsIQNpVG9fXyXzLDdJulV-ETSJFaGf0knHtSIW6GmV7aOslAIjXNATS94XeVbGt_UfctoLbqTRzkW2OhZ8ar8lQlYxJHp8nb0qNPDc5e9TVt4Z2BmROLW_qk7ROr_zc5v9maThoGK9vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامهٔ جهش‌های سه‌رقمی بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۳ هزار واحدی به ۵ میلیون و ۲۷۷ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/454180" target="_blank">📅 12:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454179">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJiV8PuUgvZOeZFTykPQWyx7GuyVZrxdPrWTHKtZCWGdd_D7VujDzr3xJAOgUVsLuIBSBMydWntkAO4LrYDpPsVbWFMIWYaERVgSQBkakFCJfQvrk3frIbIf_6qp6v_6kooNJkNODoDbwOAQIAglR2g-Oy77wl-KorO2MbGNEl9xZNfPDnHNA4cqAKPInavqSutmwdx1_-9ZjnnCRLO-2LidMY67YJKB5hdw-xSTl-p2reXND1Kld2n7AgcumCG5iU5Z1aoWvImEtukHpYVR7Xj4yN3GyuLQlfzCNOW9EPVYtEzklrbKTVWV3jJ0BaA1oToX_sfcdi7jEowkLtHcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام پهپاد MQ9 بر فراز تنگه هرمز
🔹
یک فروند پهپاد MQ9 توسط آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه بر فراز آسمان تنگه هرمز رهگیری و مورد اصابت قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/454179" target="_blank">📅 12:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454178">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUhCxWgeOJennZpmAOFDFs07hNY808AVktz7Y1fDmqKXvMbF3skI0BHeZNfU3iT28sRrYAVSlQuBit_gWLy-cbl-cXDEK-jE4b02OsHDG-F4DAY2XatYcUygd35EMyeiOF-P-M9vWHJ-1wkt1TvG0nYPtByVqaHee94V7OCiJSSJrFBzBKHMrf-VUt3U8JpXXVInkr4FAUq71twg0hhaiNYJfqsznuEbVyVZfa6RG4ZzE9AD2GO--NVSrWWWDuE9vNmhlvHsUqeePKzEQkySRw-PCGySzusxc7ISIp5exSSXVOitJilOQdb4Q3sRapIe18m-BAHWDk2CwO4GWpYm5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن ۶ نفتکش سعودی را به مارپیچ آفریقا انداخت
🔹
تصاویر ماهواره‌ای و داده‌های ردیابی دریایی نشان می‌دهد که دست‌کم شش نفتکش حامل پرچم سعودی، مسیر خود را از تنگۀ باب‌المندب به‌سمت دماغۀ امید نیک در جنوب آفریقا تغییر داده‌اند تا از حملات نیروهای یمنی در امان بماند.
🔹
پیش از این و با بسته شدن تنگۀ هرمز، عربستان بخش عمدۀ صادرات نفت خود را از طریق خط لولۀ شرق-غرب به بندر ینبع در دریای سرخ هدایت می‌کرد و این مسیر به تنها راه باقی‌مانده برای صادرات نفت این کشور تبدیل شده بود.
🔹
حال با تهدید این مسیر نیز، نفتکش‌های سعودی ناچار به انتخاب مسیرهای دورتر و پرهزینه‌تر برای رساندن محموله‌های خود به بازارهای آسیا هستند.
🔹
براساس گزارش ویندوارد، تغییر مسیر نفتکش‌های سعودی هزینه‌های سنگینی به‌همراه داشته؛ به‌طوری که زمان سفر در مسیر تایوان به بندر ینبع از ۲۴ روز به بیش از ۵۶ روز رسیده و هر تردد را ۲ تا ۲.۵ میلیون دلار گران‌تر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/454178" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454177">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18286dd58.mp4?token=TLBZ3-QAOp8sUkpwYUfb_0cLuJdMP1cb4RicwvvmdLSUSqM0lDnfWk4jfYcpCJ7EXrxof6QT_A8iFGD09O-W3Esbp2wxSCRlmb-hiU_Qd1G2IgJm_3YUNnz9fNxCBNc9OE5quVECw7sFKP3ZUrs9q-Nyv6uHuXEkvyMZUox-WdrFIVrG2vxxmpp8DSqoQ4YpzD0yIhgDBaEtExu-DRZMGkoLnDyYNNsFfxgI3OWwjoFJtdZaUL7YmE3qSDwzgIHl0xPdO7XZ7TKzN3rwGVeceocHoOsFgyCX76VRPjGaPcKa_nS1gj739cEVjFDJDcNL8mLQS6ei9uu4Xn6Gl0CXsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18286dd58.mp4?token=TLBZ3-QAOp8sUkpwYUfb_0cLuJdMP1cb4RicwvvmdLSUSqM0lDnfWk4jfYcpCJ7EXrxof6QT_A8iFGD09O-W3Esbp2wxSCRlmb-hiU_Qd1G2IgJm_3YUNnz9fNxCBNc9OE5quVECw7sFKP3ZUrs9q-Nyv6uHuXEkvyMZUox-WdrFIVrG2vxxmpp8DSqoQ4YpzD0yIhgDBaEtExu-DRZMGkoLnDyYNNsFfxgI3OWwjoFJtdZaUL7YmE3qSDwzgIHl0xPdO7XZ7TKzN3rwGVeceocHoOsFgyCX76VRPjGaPcKa_nS1gj739cEVjFDJDcNL8mLQS6ei9uu4Xn6Gl0CXsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاور پیشین سازمان جهانی بهداشت: کووید ۱۹، ساخت آمریکا بود
🔹
در حالی که آمریکاییان بارها گسترش کووید ۱۹ و همه‌گیری بیماری کرونا را به گردن چینی‌ها انداخته‌اند، اکنون جفری ساکس، استاد دانشگاه آمریکایی اذعان کرده که این پژوهشگران ایالات متحده بوده‌اند که با دستکاری در ژن ویروس‌های کرونا، ویروس کرونای جدیدی را ایجاد کرده‌اند.
🔹
به گفته جفری ساکس که ریاست کمیسیونی در سازمان جهانی بهداشت در زمینه کووید ۱۹ داشته، پژوهش برای دستکاری ژن‌های ویروس کرونا، «با تأمین مالی مؤسسه ملی بهداشت آمریکا (NIH) و توسط یک تیم تحقیقاتی در دانشگاه کارولینای شمالی انجام شده است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/454177" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454176">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPlab_Ye0wkV4toP4dLT9ZT9PnBm4P1sg5zxpTCfETF2gVlD45ZJTVY0X5yJHNCxUWApB7qx1Ik2zaXmofnHRKZn2ElWUHnrKWGKzMZKZLUxCZXyxXx3KgAO45KW5YLfGaowG_DTzlOYBcoYZXxZJucDt6OSl5oWOMQ4Mdy16tELQxPnByLh_X5qYkB1CAVadIc5sR5vSBy_NFrDviIbli6M6s9GMqO68NSLRROqtBqeQJESKccxwD7nFTGx1FkFrrlhadZDpId79_ctrqjirxV3J3dyY1f1XredoMqtPb6kkuD8qE_q2thUOCuHTgj1lsOJDjkMtH61h_glXmT7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
روایت محمدصادق لواسانی؛ خبرنگار فرهنگی سینمایی از پخش یک سریال متفاوت در شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/454176" target="_blank">📅 12:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454175">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12bacc8c1f.mp4?token=VgGQrZS6KyAt_9C4AafR1XAP1rBqbSNlRXrJp1R_F5aiiYAe2BBpyFEhfQZ82B2-9L9s4N827PoZWmWVNVbRoZMYb-gthOzjfTVgX-vdWCuIIxJpxmJt8f_4cy_queoaM2MBRhFm9etjBCh9SVlQyoVAu6zplBBJMRy99yr9smvmANl3kgjnd0q_y9PjgBvGpvcRSFis1qNw3zntsxmjlGM2UBLKjuXPKm834OBFCTGnP0UIw5ld0-k-orp8nw0Q5axsWy-uRu7YSPZlkFUoTx9fjR6wHiomxtb1HHJlVhvMDf0Zg5U7WO3OILF94geV4rgqz9XCceBaMs5OLsbCKA09EdhfXwxCfC3MO0w2txBgx1rQUioAdZJ38nn4aM22flreCmdY7W6kRp6YTreYqkXphsQHDkRY46HsmV_AJPeMRixD2GYfvq8KNADQsTyQBrdIh3Tb2vJt9GAPssLm9g-R9Ikfo3yigF3Xx7D-xqqCItbbqXstWxsodX09O2TbE87bHU0012_pjXcdrwQ97kWKniU-zisgpzSMMXqTOwZ6j1wQ2kleFqWj_AtAN3R4a7sVI1Io1l-S3mt1JjawDAE-FJf2Lyp39XlhziBYtiHtZHHue6v_TZE6mzr8JfHPJA7IeeXjF7_NXqAIdy7Q9QjvZTcbT5uG_WRSjqCOcpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12bacc8c1f.mp4?token=VgGQrZS6KyAt_9C4AafR1XAP1rBqbSNlRXrJp1R_F5aiiYAe2BBpyFEhfQZ82B2-9L9s4N827PoZWmWVNVbRoZMYb-gthOzjfTVgX-vdWCuIIxJpxmJt8f_4cy_queoaM2MBRhFm9etjBCh9SVlQyoVAu6zplBBJMRy99yr9smvmANl3kgjnd0q_y9PjgBvGpvcRSFis1qNw3zntsxmjlGM2UBLKjuXPKm834OBFCTGnP0UIw5ld0-k-orp8nw0Q5axsWy-uRu7YSPZlkFUoTx9fjR6wHiomxtb1HHJlVhvMDf0Zg5U7WO3OILF94geV4rgqz9XCceBaMs5OLsbCKA09EdhfXwxCfC3MO0w2txBgx1rQUioAdZJ38nn4aM22flreCmdY7W6kRp6YTreYqkXphsQHDkRY46HsmV_AJPeMRixD2GYfvq8KNADQsTyQBrdIh3Tb2vJt9GAPssLm9g-R9Ikfo3yigF3Xx7D-xqqCItbbqXstWxsodX09O2TbE87bHU0012_pjXcdrwQ97kWKniU-zisgpzSMMXqTOwZ6j1wQ2kleFqWj_AtAN3R4a7sVI1Io1l-S3mt1JjawDAE-FJf2Lyp39XlhziBYtiHtZHHue6v_TZE6mzr8JfHPJA7IeeXjF7_NXqAIdy7Q9QjvZTcbT5uG_WRSjqCOcpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
#تماشا_کنید
💠
رونمایی از طرح «
کیف پول مهارت - کاراکارت
»
با مشارکت بانک تجارت، سازمان فنی و حرفه‌ای کشور و شرکت کارت اعتباری ایران کیش با حضور آقای دکتر عارف معاون اول رییس جمهور
✅
کیف پول مهارت یک اعتبار اولیه و محرک است برای کسانی که انگیزه یادگیری دارند اما برای شروع مسیر آموزشی با محدودیت مالی مواجه هستند.
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/454175" target="_blank">📅 12:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454174">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/454174" target="_blank">📅 12:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454173">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727ab2e627.mp4?token=eJWj2iCi6EWqS-o4SEWLqxbWsa6jmMijoNIb9_1-QIuTpd87uWUtfpeUhhKtbbKvECecX3WzAoxkV9_xwp-O3Yp0ecHXAdtuiw27IAE9W14l8SELF29Y1iGG3DXCwyqIy4-ZGQAkFDtz0ehA0Y4pBRPPFDCO-ddHuMITbTEFEjDr_yFJDAkO65ljERnjNDnbRuvHSNUd1nu_BCoNjll-1TyeJbYaEc5O94OS7zlpvSOr_lvwovIbKgOd4wJfiuDgigi6VCAlYStkmcl6qjj2X36_d2-8yHBsDUoVn3odrw2i8YyxwDtRW-Ic8xHbiCE9Q9wU62yINhgKAmV6XwWADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727ab2e627.mp4?token=eJWj2iCi6EWqS-o4SEWLqxbWsa6jmMijoNIb9_1-QIuTpd87uWUtfpeUhhKtbbKvECecX3WzAoxkV9_xwp-O3Yp0ecHXAdtuiw27IAE9W14l8SELF29Y1iGG3DXCwyqIy4-ZGQAkFDtz0ehA0Y4pBRPPFDCO-ddHuMITbTEFEjDr_yFJDAkO65ljERnjNDnbRuvHSNUd1nu_BCoNjll-1TyeJbYaEc5O94OS7zlpvSOr_lvwovIbKgOd4wJfiuDgigi6VCAlYStkmcl6qjj2X36_d2-8yHBsDUoVn3odrw2i8YyxwDtRW-Ic8xHbiCE9Q9wU62yINhgKAmV6XwWADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۴ مسیر ویژه برای زیارت مرقد رهبر شهید ایجاد شد
🔹
با تغییرات جدید و گشوده‌شدن رواق دارالذکر به روی زائران ۴ مسیر ویژه زیارت مرقد رهبر شهید در حرم رضوی ایجاد شد.
🔹
در مسیر نخست، زائران آقا از صحن آزادی وارد رواق دارالسرور شده و پس از عبور به روضۀ منوره مشرف…</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/454173" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454171">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هرمزگان چهارشنبه تعطیل شد
🔹
معاون منابع استانداری هرمزگان: به‌دلیل تداوم افزایش دمای هوا و ضرورت مدیریت مصرف انرژی تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی چهارشنبه ۱۴ مرداد تعطیل است.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/454171" target="_blank">📅 12:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454170">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هیئت‌رئیسۀ خبرگان: زمزمه‌های تسلیم‌طلبی به اسم صلح، خیانت نابخشودنی است
🔹
هیئت‌رئیسۀ مجلس خبرگان رهبری با صدور بیانیه‌ای ضمن تقدیر از حضور بی‌نظیر مردم در مراسم تشییع تاریخی قائد شهید امت، بر حمایت کامل از مواضع عزتمندانۀ رهبر معظم انقلاب، حضرت آیت‌الله سیدمجتبی خامنه‌ای، تأکید و التزام عملی همۀ مسئولان به رهنمودهای ایشان را خواستار شد.
🔹
در این بیانیه که به‌مناسبت ایام اربعین حسینی صادر شده، آمده است: پیام‌های حکیمانه، بصیرت‌افزا، امیدبخش و عزتمندانه رهبر معظم انقلاب، راه‌گشا و راهنمای مردم شریف ایران و امت اسلامی است و باید نصب‌العین مسئولان محترم نظام قرار گیرد.
🔹
هیئت‌رئیسۀ مجلس خبرگان همچنین با اشاره به زمزمه‌های تسلیم‌طلبی از جانب مرجفون و توطئه‌گران به اسم دفاع از صلح، آن را خیانتی نابخشودنی دانسته و بر مواجهه قانونی با چنین اقداماتی به‌عنوان وظیفه مسلم مسئولان تأکید کرده است.
🔹
در بخش دیگری از این بیانیه، بر ضرورت حفظ اتحاد مقدس و پیروی از رهنمودهای رهبر معظم انقلاب به‌عنوان فصل‌الخطاب و تنها محور وحدت تاکید شده و التزام عملی کامل همۀ مسئولان به نظر ولی‌فقیه، واجب عقلی و شرعی خوانده شده است.
🔗
متن کامل بیانیه را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/454170" target="_blank">📅 11:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454169">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f7297b6e.mp4?token=fthllon9GkzzNVlfUleTelCtfN1H61ZhKrYRulCyYSGGagHn-NBrqIehuvFI0WppE9vZ3h2kv1_zbLp1i8PKZNjA1AqRrkGfpX5kMhXTHTaMshAxwOBgzukOX2RD2R0th2KqBuJJAN7fwbyWgUpSKYgF-DosQ1raLIFYDI8I-iXlhhCM5aqvD7a_9e7uo-6C3G__E32kSM4k1JQx9hapJnE7KD9AiiEbu36Y1VPDyiVpIWiEn5kIvx41kDH1x68Fs5p_N8z5p0xhvC6sODyq3CaBGN4UOqdh7R7SdF__tSAbTMfmA4BNC4KbQTQSNZ3jMgjwyaeDt96iEOsSz_iPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f7297b6e.mp4?token=fthllon9GkzzNVlfUleTelCtfN1H61ZhKrYRulCyYSGGagHn-NBrqIehuvFI0WppE9vZ3h2kv1_zbLp1i8PKZNjA1AqRrkGfpX5kMhXTHTaMshAxwOBgzukOX2RD2R0th2KqBuJJAN7fwbyWgUpSKYgF-DosQ1raLIFYDI8I-iXlhhCM5aqvD7a_9e7uo-6C3G__E32kSM4k1JQx9hapJnE7KD9AiiEbu36Y1VPDyiVpIWiEn5kIvx41kDH1x68Fs5p_N8z5p0xhvC6sODyq3CaBGN4UOqdh7R7SdF__tSAbTMfmA4BNC4KbQTQSNZ3jMgjwyaeDt96iEOsSz_iPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجهٔ اوکراین اطمینان داده که حمله به کشتی ایرانی غیرعمدی بوده</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/454169" target="_blank">📅 11:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454168">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3HvJWcthDygjDARLC-771eSs40Z8yMt7ljQkwjO6jsZCdFzestvgHMLQYnGDWXBGyfV8-gjmve8zXLfTvyWGtgyB8Sjm5_9Q5ZmECVf_MQ8mRmnv3rWm0jrGGE-tijfNWrx6G9DGNzYXYmFLV5s0hjeVfCs_miRPQ5Zey94rJzsV3Aqwh5fn44-fZVayV1UANIltwUztFoAjOHFWOrOOx-J7uDZw0uEaGDwawxplL7ebVC9FctGWy820phRT3XkCjYYsUzsnqY1X1hXth3zv3DMZ2_zY3S3QlBQpO0oVOHd9LkRCAiU5F8OU2krN8_58KIEsmBNiz4zGPdYyaeRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز گوشت را در آمریکا گران کرد
🔹
مارک وارنر نمایندۀ ایالت ویرجینیا در مجلس سنای آمریکا می‌گوید: «قیمت گوشت گاو در آمریکا ۱۲ درصد و مواد غذایی ۴ درصد افزایش یافت».
🔹
اختلال در حمل‌ونقل دریایی از طریق تنگه هرمز دلیل اصلی رشد قیمت از سوی کارشناسان این حوزه مطرح شده است.
🔹
طبق آمارهای رویترز، آمریکا به‌دلیل خشکسالی و افزایش تقاضای داخلی واردکنندۀ خالص گوشت گاو است و سالانه ۲.۷ میلیون تن وارد می‌کند.
🔹
افزایش هزینۀ انرژی،‌ حمل‌ونقل و بیمۀ کشتی‌ها قیمت گوشت وارداتی و تولید داخلی را گران کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/454168" target="_blank">📅 11:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454166">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عملیات انهدام مهمات در شرق تهران
🔹
روابط‌عمومی سپاه حضرت سیدالشهدا(ع) استان تهران: انهدام مهمات عمل‌نکرده تجاوز آمریکایی صهیونی در شرق تهران حوالی محدودۀ پارچین امروز از ساعت ۱۴ الی ۱۶ صورت می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/454166" target="_blank">📅 11:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454165">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca09dbe42.mp4?token=tEvAu80GzpcCNHF2-mERsPxo9jDsXFjEZFs14n5vvSX0DUCFmDooGCajR6ox888aNfqUErCOGZZQFFwJWXJ2ad9WUDVzOOMIkEj8IE3zKTBFSnyug-OiFHmbQMWPjLEtTwpeGRnPvcVESTy0GSldiF7qrQrjBY22bFfuwxaPPlV7Vw5XfUsub1hjKFkjcKTKVwqMNJDaeOkbUKbQwD6hqpe_0evEwtwUxTjmJcOWRWsPp7WTOLJ-D0F5_Oa8C-GPnfXZPCKD8qL0egi_fMSg6PwvYkzUNVL3ClbzlUiVqlIJSxpvF-tuTlqBt_KtMIr5USfVLCEG62wLzzMxAegiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca09dbe42.mp4?token=tEvAu80GzpcCNHF2-mERsPxo9jDsXFjEZFs14n5vvSX0DUCFmDooGCajR6ox888aNfqUErCOGZZQFFwJWXJ2ad9WUDVzOOMIkEj8IE3zKTBFSnyug-OiFHmbQMWPjLEtTwpeGRnPvcVESTy0GSldiF7qrQrjBY22bFfuwxaPPlV7Vw5XfUsub1hjKFkjcKTKVwqMNJDaeOkbUKbQwD6hqpe_0evEwtwUxTjmJcOWRWsPp7WTOLJ-D0F5_Oa8C-GPnfXZPCKD8qL0egi_fMSg6PwvYkzUNVL3ClbzlUiVqlIJSxpvF-tuTlqBt_KtMIr5USfVLCEG62wLzzMxAegiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: به‌تجربه برای ما اثبات شده که چیزی جز اقتدار دشمن را از شرارت بازنمی‌دارد.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454165" target="_blank">📅 11:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454164">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10fa703e3.mp4?token=jdoi3fDCfjdlAqFqooR4BCIZIJet8SmDdY6jm0RpCK3NkB0CCFLRabUMZmwXSMxIu4FXVnH8F2w47scL-t5sUrnwR9SOct1a5koWueO1JHnelB30ET5QGKzWNuqd8S1EXp0Ayx88oox1Be4bO65nzoYAogTaTR6ySsXCjvw7Cm2lIv9VSN3uSf530LyerfXyA6vgLcpjNuEXHMGjpkCIBImwhk8IN-3vxHAjy4vmMK2ihHRXyDzMwUcyA41GedJDJV4tiIo2K8p8zV3WwnKcxW5bj5mh7XfkOcsi4kwmQqlJ9nScAxgaVJC0x5jsCKCLZ3jHX9OtHEDJTkM3CurrQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10fa703e3.mp4?token=jdoi3fDCfjdlAqFqooR4BCIZIJet8SmDdY6jm0RpCK3NkB0CCFLRabUMZmwXSMxIu4FXVnH8F2w47scL-t5sUrnwR9SOct1a5koWueO1JHnelB30ET5QGKzWNuqd8S1EXp0Ayx88oox1Be4bO65nzoYAogTaTR6ySsXCjvw7Cm2lIv9VSN3uSf530LyerfXyA6vgLcpjNuEXHMGjpkCIBImwhk8IN-3vxHAjy4vmMK2ihHRXyDzMwUcyA41GedJDJV4tiIo2K8p8zV3WwnKcxW5bj5mh7XfkOcsi4kwmQqlJ9nScAxgaVJC0x5jsCKCLZ3jHX9OtHEDJTkM3CurrQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مذاکره‌ای با آمریکا نداریم
🔹
مذاکرات فعلی ما با عمان و متمرکز بر مسیر تردد ایمن کشتی‌رانی در تنگهٔ هرمز است. تلاش داریم در اولین فرصت با همکاری عمان مسیر موقتی را تعیین بکنیم تا براساس آن بتوانیم ایمنی کشتی‌رانی در تنگهٔ هرمز را فراهم…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454164" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454163">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89df9c9324.mp4?token=EZmnxRFzCO2W-US3d1Itpm649b4F76c_l8Ljsbi0iOPQDjY5-KvZevNKKJxaXVjRqjP61xBVijtR9KhOImsKW4jylfMHQx9UmnKdDjKWkdpPRtXhIYvgydtcXq7e0cBvskihaAOOTNBiAdus2w7kFD4kzt3dRa6k48UdnjyME_sWlihGwBLduhIaD9JBgSVzEsYvVzcSvvmhDlmtaHCHpJzvWsfFsotHmXj_ceqN2frZbjNbieXK8Xgyt3lqDayUzwEoeoi4wGbZmFnqjTWvG98bcZuBaYXayzHtjhHn9Pupd520ul8F8-0ncke4rfNeA8PFEYaF8rbY_oP7RAj47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89df9c9324.mp4?token=EZmnxRFzCO2W-US3d1Itpm649b4F76c_l8Ljsbi0iOPQDjY5-KvZevNKKJxaXVjRqjP61xBVijtR9KhOImsKW4jylfMHQx9UmnKdDjKWkdpPRtXhIYvgydtcXq7e0cBvskihaAOOTNBiAdus2w7kFD4kzt3dRa6k48UdnjyME_sWlihGwBLduhIaD9JBgSVzEsYvVzcSvvmhDlmtaHCHpJzvWsfFsotHmXj_ceqN2frZbjNbieXK8Xgyt3lqDayUzwEoeoi4wGbZmFnqjTWvG98bcZuBaYXayzHtjhHn9Pupd520ul8F8-0ncke4rfNeA8PFEYaF8rbY_oP7RAj47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مذاکره‌ای با آمریکا نداریم
🔹
مذاکرات فعلی ما با عمان و متمرکز بر مسیر تردد ایمن کشتی‌رانی در تنگهٔ هرمز است. تلاش داریم در اولین فرصت با همکاری عمان مسیر موقتی را تعیین بکنیم تا براساس آن بتوانیم ایمنی کشتی‌رانی در تنگهٔ هرمز را فراهم بکنیم.
🔹
تا زمانی که شرارت و محاصره توسط آمریکا ادامه پیدا کند، وضعیت تنگهٔ هرمز تغییر نخواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454163" target="_blank">📅 10:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454161">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjrDo3Wt1moLj0ykARyWeQ0mvRnWUCe8Nw7Cy3sz2xN_d9YACzRs4y6tvPEQfB2yc1Rgk2EzyVv3qFsIM0Xz5g50pHGb7iCciRO9EiuDA6KBErCPBuS7hKoFehBg08XC0YKbHkznEbmoRbAajThGsSzOHrVjoM-FRajMVl7pTyPrQ55E-RCnR24iHc5j76M7TwzUIbd_A81ZcRSuq8rR1Kvkyc7I0FpYJP_gVRwq6WcBi63jxNDRMitQai5CILs6VdpWJx8C6XxkqjW699DbkN2SgwCoiVNMdYYd19dNWPitB8aR7izIxC_Y3y5HU4pQ0H_ebyEIshF4DQQpw_0dtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wi92PVOVZtdl6wA_jseSG08hcsEeD8gPaX3S7e3y0D5hqwuvx-fUyzMb6y6TpwZshZfOkr6r5hui-cuKWZh8tffntxXJfwGgQmLZ-kjgV0yOEJyBBZjpS-kFro0A1Ybo9PDWUop2O2G5f-6gXx2rkIUpzF1MsBdtBoeeQIdfb-dEdUO54cQsalA574ajHlXLzjPtLrRqIWtAYa3FjkfwwrhPo2P8BlWPID83udOjxnPJfUj6eUDSCtcXavsY4mwa69XEWXtJtpsZQPH_cS3W8CTtbBEKMiRGuQYti9Cqesd8hEngGjzQT9U7L9mYoaGtFaChJF0z12rV6Bnun1G4Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۲ بانک صاحب نیشکر هفت‌تپه می‌شوند
🔹
هیئت واگذاری واگذاری سهام دولت در شرکت کشت‌وصنعت نیشکر هفت‌تپه به دو بانک ملی و صادرات را مصوب کرد.
🔸
پیش از این سال ۱۴۰۱ شورای‌عالی هماهنگی اقتصادی سران قوا با واگذاری شرکت نیشکر هفت‌تپه برای افزایش سرمایه بانک ملی و پرداخت بدهی‌های دولت به بانک صادرات موافقت کرده بود.
🔹
طبق مصوبۀ هیئت واگذاری، ۹۵ درصد سهام دولت ۱۰.۳ هزار میلیارد تومان قیمت‌گذاری شده و قرار است به‌صورت مساوی به این دو بانک داده شود.
🔹
شرکت هفت‌تپه در حال حاضر از شرکت‌های زیرمجموعۀ سازمان گسترش و نوسازی صنایع ایران (ایدرو) است و ۶۶۶۸ نفر به‌صورت رسمی، قراردادی و فصلی در آن کار می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/454161" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454160">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9d889b23.mp4?token=kRrGrWY5yCAUHPODIhWwliRAEg4kNkC9SAhq3TV83osYrFjwL2O_XJWKxNJo1Eb5XyD_uL9WBw3qXSAYqFbPwb90D2F8VEckQWu-CiYR7kBRgndoIats_gcseKoEf84pNRcLKj4Wg-2m6TWzne2FA3FOuBdx1Cblx5gGKsABbbckYX_jbWlx8jJnX6mLBdUrkaZCFbVZicBceTDkWvfDh7AtB5G_ksXZI5izhDeh-pwq59YriCCn6gzVcQlbvWdgJ0CYF-Xts-serQkZMTU8tqBk2o5gBjXuKwf_CyxVug5ik33vI2T8cwUEYqvkDMDPegeL-XXze7gMPBrNWt_1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9d889b23.mp4?token=kRrGrWY5yCAUHPODIhWwliRAEg4kNkC9SAhq3TV83osYrFjwL2O_XJWKxNJo1Eb5XyD_uL9WBw3qXSAYqFbPwb90D2F8VEckQWu-CiYR7kBRgndoIats_gcseKoEf84pNRcLKj4Wg-2m6TWzne2FA3FOuBdx1Cblx5gGKsABbbckYX_jbWlx8jJnX6mLBdUrkaZCFbVZicBceTDkWvfDh7AtB5G_ksXZI5izhDeh-pwq59YriCCn6gzVcQlbvWdgJ0CYF-Xts-serQkZMTU8tqBk2o5gBjXuKwf_CyxVug5ik33vI2T8cwUEYqvkDMDPegeL-XXze7gMPBrNWt_1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر جدید از لحظات اولیۀ حمله به مدرسۀ میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/454160" target="_blank">📅 10:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454159">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در اصفهان
🔹
سپاه صاحب‌‌الزمان اصفهان: امروز تا ساعت ۱۴ احتمال شنیده شدن صدای انفجار کنترل‌شده در محدودۀ صفه، بهارستان و اطراف آن وجود دارد و جای نگرانی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/454159" target="_blank">📅 10:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454158">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmkmaCrL9a4d8hDeXgPIdalpyRaKM3_wMVFKkggdscym3_aKRVcR2_AtrXzUqnxw7d_DV_rIcscetrgkwg3sm8vJlFBECJmdphcE8p4yjQnuuoRLiOGqmw-fVEJXUSaJjIIZwT3hFD_qH0U51JTBB0HfE54VWhnmXC8l1huNJ7TmAzYEVI7cMp_BkCPEWbIsEgZmJiUCMTNtJkHj-bBPfQCN78hXF292k5SHFaEBU51TliokH_EUcPQRt43v57JrDjV_OWVgr8E6SJRp1BqyHs1dUxhl3U_rQcrXv-fW6WEA3Y95oZPtywsV5NnfN9dAmb-4fkyzxJJ9aju-ghdMYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: قدرت‌سازی در بسیج ارمغان شهید سلیمانی بود
🔹
فرمانده قرارگاه خاتم‌الانبیا با حضور در منزل سردار سرلشکر شهید «غلامرضا سلیمانی» رئیس فقید سازمان بسیج مستضعفین، با خانواده معظم این شهید گران‌قدر دیدار و گفت‌و‌گو کرد.
🔹
سرلشکر عبداللهی: قدرت‌سازی در معماری جدید بسیج و تبدیل بسیج از یک نهاد صرفاً عملیاتی به دانشگاهی برای پشتیبانی از کیان ایران بزرگ‌ترین ارمغان رئیس شهید سازمان بسیج مستضعفین بود.
🔹
شهید سلیمانی با برنامه‌ریزی دقیق، توانست بسیج را به دانشگاهی مهارت‌آفرین و شبکه‌ای تخصصی برای پشتیبانی از کیان جمهوری اسلامی تبدیل کند.
🔹
آنان که با جنایت و ترور به‌دنبال توقف این مسیر الهی بودند، امروز می‌بینند که بسیج و جبهه مقاومت، به برکت خون پاک این شهید و همت والای همرزمانش، روزبه‌روز بالنده‌تر و حماسی‌تر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454158" target="_blank">📅 10:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454157">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شارژ مرحلهٔ جدید کالابرگ از پنجشنبه آغاز می‌شود
🔹
مرحلهٔ جدید طرح کالابرگ الکترونیکی از پنجشنبه با شارژ اعتبار مشمولانی که رقم آخر کد ملی آن‌ها ۰، ۱ یا ۲ است، آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/454157" target="_blank">📅 10:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454156">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c51d0ea242.mp4?token=ljYLFtqHuDJ0YqOvyAb7rSeo1y_znZaa5zULfPEFKizE6d7QGrpzM4oEv_lo42yLC_dgrFkaYzsNeKV57TNlG_qQtVdVApkDrxtwHnfQaUDFcodvCpjUQLDn7LZ_Vdu073GxSYxLxNt23_6Fc3F_dGrPXoWsxaeTKSWARL2NZpJXKjNxlHYQs1uOuIZp1LKC-LgDGUeTzW_mLHJlDrZwXdjMBaX1U0IdhakL4u4CMuV7PfXZkk0tj6dBLZE-6BbVjcVxuHv2cibF_6dRw0xDxYhrv9ym1XuZdUEhLHZwJP-STUFZ9TvbAwAx59RGjmbbvYClI1qTXY9HnKzGs9GV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c51d0ea242.mp4?token=ljYLFtqHuDJ0YqOvyAb7rSeo1y_znZaa5zULfPEFKizE6d7QGrpzM4oEv_lo42yLC_dgrFkaYzsNeKV57TNlG_qQtVdVApkDrxtwHnfQaUDFcodvCpjUQLDn7LZ_Vdu073GxSYxLxNt23_6Fc3F_dGrPXoWsxaeTKSWARL2NZpJXKjNxlHYQs1uOuIZp1LKC-LgDGUeTzW_mLHJlDrZwXdjMBaX1U0IdhakL4u4CMuV7PfXZkk0tj6dBLZE-6BbVjcVxuHv2cibF_6dRw0xDxYhrv9ym1XuZdUEhLHZwJP-STUFZ9TvbAwAx59RGjmbbvYClI1qTXY9HnKzGs9GV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲ عامل صهیونیست‌ها در جنگ‌های ۱۲ و ۴۰ روزه اعدام شدند
🔹
امید بهزاد و پوریا صفوت، ۲ مزدور رژیم صهیونیستی که در جریان جنگ رمضان و جنگ ۱۲ روزه با ارسال مختصات، تصاویر و اطلاعات مراکز نظامی و امنیتی برای افسران موساد و کانال‌های ارتباطی وابسته به این سرویس جاسوسی…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454156" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454155">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ5J5BQpJUGSZGRhENu2Y5q5EqbZOJtwBq20LISYmkQsFGnNDQ_6VaGmTnXdGMD0lm9fl6r9oZemphfKE1oNP7shCezy15Yvz4FiSgdbsrJw5wLuahhomebcKUzrV9ALBH2wI5nZw5ciJ__VjfX47UIe450_6bEppQOKHLMD3IU8InCisPkaCAqkOD_3R1uhODahPH1q5q1GV7qlsfK75xcdp3yqXfbVpIGdVJ_0SmvPPKLNPY2bZM4E_wVuVvdRJRcB1OWFZBwct4wJZSEcpxk6QIvP32BBgJy8h1bUi6eq_Pca3zeYJL874IHzsflY1GLB-QIeBPfYQm6r-b_T8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رقابت شدید روسای‌جمهور آمریکا برای فحاشی
🔹
نتیجه یک مطالعاتی تحقیقاتی نشان می‌دهد که استفاده رئیس‌جمهور آمریکا و مقامات ارشد آمریکایی از الفاظ رکیک، طی دهه اخیر روند صعودی گرفته است.
🔹
طبق تحقیقات استاد علوم سیاسی دانشگاه کاردیف جوزف فیلیپس، ۸۷ درصد از کل موارد فحاشی علنی روسای جمهور آمریکا از سال ۱۹۱۹، فقط طی دهه گذشته ثبت شده است.
🔹
طبق نتیجه تحقیقات او، اکثریت قریب به اتفاق موارد فحاشی در انظار عمومی (۷۸ درصد) توسط دونالد ترامپ و جو بایدن انجام شده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454155" target="_blank">📅 09:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454153">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e9b676cc8.mp4?token=Z0-60A9DPedE8cFkYfkZuWU6_EDaBozoNKlDInHLcgVbmOGZRFg4KNLneIP8moHB-DPbjaQic7PKgU6ipXCQlr63dyQ1zCXwdqU9S99OSUltQO8ilwDAF01-Xdg1Kq-1L1I9Fy-4njubB6ad34EY5jgVHjeBKLfG06kJC3beXlLAt0kO_Mse_GPe_rxSyMTvdzGSWQkilEwPK-RTN-Bxlx2d_DBNSr9RXGMxwUz6LIZzA6Oy5e958UBr51rqRT6ooSwWGb1HBFkG6PmzGHTDwQDE07vodBUMQgXmCjHEJUfAZ0qIvuLH6lmDzOSauayKj3fpvpCp5aIMaVOmOfTMnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e9b676cc8.mp4?token=Z0-60A9DPedE8cFkYfkZuWU6_EDaBozoNKlDInHLcgVbmOGZRFg4KNLneIP8moHB-DPbjaQic7PKgU6ipXCQlr63dyQ1zCXwdqU9S99OSUltQO8ilwDAF01-Xdg1Kq-1L1I9Fy-4njubB6ad34EY5jgVHjeBKLfG06kJC3beXlLAt0kO_Mse_GPe_rxSyMTvdzGSWQkilEwPK-RTN-Bxlx2d_DBNSr9RXGMxwUz6LIZzA6Oy5e958UBr51rqRT6ooSwWGb1HBFkG6PmzGHTDwQDE07vodBUMQgXmCjHEJUfAZ0qIvuLH6lmDzOSauayKj3fpvpCp5aIMaVOmOfTMnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: امروز در مازندران، گلستان، خراسان‌شمالی و ارتفاعات شرقی البرز شاهد بارش هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454153" target="_blank">📅 09:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454152">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">۲ عامل صهیونیست‌ها در جنگ‌های ۱۲ و ۴۰ روزه اعدام شدند
🔹
امید بهزاد و پوریا صفوت، ۲ مزدور رژیم صهیونیستی که در جریان جنگ رمضان و جنگ ۱۲ روزه با ارسال مختصات، تصاویر و اطلاعات مراکز نظامی و امنیتی برای افسران موساد و کانال‌های ارتباطی وابسته به این سرویس جاسوسی کمک شایانی به آن‌ها در رسیدن به اهداف خود کرده بودند اعدام شدند.
🔹
بررسی‌های فنی انجام‌شده بر روی تلفن همراه امید بهزاد نشان داد او در جریان جنگ رمضان، بار‌ها مختصات، موقعیت جغرافیایی و اطلاعات مربوط به مراکز نظامی، انتظامی و امنیتی را برای کانال‌های وابسته به موساد ارسال کرده است.
🔹
پوریا صفوت، از جمله سربازان نتانیاهو و خائن به کشور بود که در راستای همکاری اطلاعاتی با رژیم صهیونیستی در شرایط جنگی، اقدام به ارسال مختصات مکان‌های نظامی و امنیتی به شبکه اینترنشنال می‌کرد.
🔹
در یکی از پیام‌هایی که محکوم‌علیه برای موساد ارسال کرده، آمده: فیلمش را هم دارم که از این مرکز دارند به‌سمت پهپاد یا جنگنده شلیک می‌کنند، ولی اینترنت ضعیفه و ارسال نمی‌شود؛ ممنون از شما سربازان حضرت موسی!
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454152" target="_blank">📅 08:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454151">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda4f01039.mp4?token=OqDpfl257Mf9YEzLECz8CG2ZIlbCVXetfVMeljpx9Ug5J8csItzwZH9PZaaJ_LGTeMtrPKzJea2uyeU8ghVUI6-eSzWEj9-2qXdh84pkDbdRvLYPRPSBCbkPlkmiZK4o92GjLUo67zFbUvclDPKTurgVehEMd9VNpyZvicEIYsNJDbQZELqEr9ZuV6pBkah_XOzoLAj3qYOTOoVnUWAJ8HKeRB5Q6d_VGkrdoB2F7PQ410Xas95HxLZxeAPj9VLptbfGt-YVFK9sWt162VQ0MmDQCzVRVow-c2C4wopEK06atefWMgA03QNe_CdpQeMgSpoOc1j1Ki4rDwuADwifCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda4f01039.mp4?token=OqDpfl257Mf9YEzLECz8CG2ZIlbCVXetfVMeljpx9Ug5J8csItzwZH9PZaaJ_LGTeMtrPKzJea2uyeU8ghVUI6-eSzWEj9-2qXdh84pkDbdRvLYPRPSBCbkPlkmiZK4o92GjLUo67zFbUvclDPKTurgVehEMd9VNpyZvicEIYsNJDbQZELqEr9ZuV6pBkah_XOzoLAj3qYOTOoVnUWAJ8HKeRB5Q6d_VGkrdoB2F7PQ410Xas95HxLZxeAPj9VLptbfGt-YVFK9sWt162VQ0MmDQCzVRVow-c2C4wopEK06atefWMgA03QNe_CdpQeMgSpoOc1j1Ki4rDwuADwifCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج بازگشت روان زائران حسینی در مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454151" target="_blank">📅 07:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454150">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رئیس فیفا با طناب ترامپ به چاه افتاد
🔹
نشریۀ تلگراف از تصمیم قاطع یوفا دربارۀ رئیس فیفا بعد از طرح فروش جام‌جهانی خبر داد و نوشت: زمان اخراج اینفانتینو رسیده است!
🔹
طرح فروش حقوق تجاری جام‌جهانی به شرکت برادر داماد ترامپ، هفتۀ گذشته از سوی رئیس فیفا مطرح شد…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/454150" target="_blank">📅 07:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454149">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d75154934.mp4?token=gLIWuEfkTF-mU0ODxbggWe9SiaNPoPS6D_K3IZZtVM3cVob5m-D6aO1sv_im5opbErGhvHRH2c-jzbqHoJaSyfZSFzRz_k3ilPHUuDA8BDOVtkwESoMt4QagazMtFnFmHVErQ9bMedmUcZcNNOpCUUFIhzDNM5OKKRyXldqi59YBprSeSTVPczHcibXVm89htpbI2oOH3WrwRmXoqF1yeYHMyJ47WXTFEqoSLlj0SCR7l7SknjzswBqG_eREbXeXSRb-7Cll8Kte526hNMlhtez9f6X2gpUxRjLCJxznSDAmaeYI4mzXMeQjHeR3-UB-7_CtBfTZPOiDUXf-abEFvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d75154934.mp4?token=gLIWuEfkTF-mU0ODxbggWe9SiaNPoPS6D_K3IZZtVM3cVob5m-D6aO1sv_im5opbErGhvHRH2c-jzbqHoJaSyfZSFzRz_k3ilPHUuDA8BDOVtkwESoMt4QagazMtFnFmHVErQ9bMedmUcZcNNOpCUUFIhzDNM5OKKRyXldqi59YBprSeSTVPczHcibXVm89htpbI2oOH3WrwRmXoqF1yeYHMyJ47WXTFEqoSLlj0SCR7l7SknjzswBqG_eREbXeXSRb-7Cll8Kte526hNMlhtez9f6X2gpUxRjLCJxznSDAmaeYI4mzXMeQjHeR3-UB-7_CtBfTZPOiDUXf-abEFvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد روان در گیت‌های ورودی مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/454149" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454148">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vidcbmN1qiYOzA-ThPf7OWNYptu6RqvqnaH-6qiG3UsA_sxX8n6GB7rSnqZ5LWLOAgnVaOVNNX-IMzyyyCvxIQOO3hYG3Q1L2mL6ejVZfi_9_E__SRDgIDqddYgbI8kbZo8OcnLG6thdmlRJjtVng1zBXJUoUlF8_6j2HuHx9xDYMKgX0GLoi1M501qYHSx7et1k4mtGcL2zlm7B97-7iTD_GBKBsquMapHmmfEp5MMIrrM7HAxhf9SF2_YdG3GblYIl10-6HC07Ql_5P4cc3wyS1ks-rfjFCtkpeZinuDlcxH-sYJsnjKy2l2FmjZi_pLAW_oQQAGQLG3RfWl5wvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش‌و‌پرورش: شیر یا تغذیه رایگان در مدارس توزیع می‌شود
🔹
سخنگوی آموزش‌وپرورش: در مناطقی که امکان توزیع شیر نیست، از کیک‌های غنی‌شده حاوی خرما، نان‌های غنی‌شده و سایر مواد غذایی مغذی استفاده می‌شود.
🔹
تصمیم‌گیری دربارۀ نوع تغذیه در هر منطقه کاملاً تخصصی و با نظر شورای عالی سلامت انجام می‌شود، اما اولویت با شیر خواهد بود.
🔹
اعتبار این طرح برای دانش‌آموزان مدارس ابتدایی دولتی پیش‌بینی شده و امیدواریم با فراهم شدن شرایط، از مهرماه اجرایی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/454148" target="_blank">📅 06:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454141">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eykzv3SW7DgF4BY4QZZX2b9tHLuUIO51syPR9QX2wQEGF5m-_gl0FPgbibh8-yMSurcPY81F4WYlNkeMv7qGhTBj3LgmB_mW93Dea7iFblywPRqvsZB3qlzAS9mkyZeRicSC0VX2I3DQcg5hq__poNrPR2vUiRkAkaIJgp5Y7LarEXk46PqQyUQCSGFi1EPzzW2Ltj2dPysRq8-EwTrH523LhOX_jZc_HRaNI4tvmKr9K9rtKAE6lTJ7dcSbJz1RAIbZT3YMNbjE8Q8RANxzD3aMFslJZGvgGrHnSOGjvMG1uAYQCjbBxAJ1Kv_xbWDd70C5hgqn-2TtWE5KWERR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmpH188rB2vfQeoHvo1_cMxpecP4lqIc6sAeKpqeW9bu9gD69haHIM5hIXDYZpnTH9uFrw1r73vHJnXaWUT4cOe3dUKNxqGIIIazI9vs12k8FRVQmubDDmK4t_n-g7H0KSn7LzvTiYuy0itdpssQAoeLlGCTwKWTSKxwz_kc8sXtydj_cMFznCrDXRVhagaP03GA6Af4cQB4GBLIi6LR9gY-GMVeJJ-O6XohuxcQRiOg9B7BgKavt8RrxBWk4wvLjQbrQSyFmez5HmAhOhdXC5ZIhZUkMVNMc7nPAoaiubgxQ55Mfr4hjduXUAz4qvY5Nl1QfnnVQiB28khfY5JPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSeM52tEG7hqo8jd-q4GLiCmGdNxI8tflhKDcoFfM7oCbDxGEAOaI6J8_dgSa29esYKu4weeZriVXEeOEwtbDqJzAV--tIdRkBTVqlnZ9slr4vKQu31cx2RyNyaAmssbrnqB7I9-r8yHhDp429aXtcFWSq53g66YfkuZxMM1Ihk1vpsIJrPVCl1zCL_JfurSIlt02KLrBm4LkPC_3a8lenAgqV5hf4-k4-RnUw8PyqAhJFIyi9_0RLsvknJu_Tt_8RG3T_s3eEr8p0FqE9X0DhtmeQ5J6vypWg8kJ-s-1xE5XeE-M9gSMLSAYmWr_kDBrU89hEAY9aSsiTLCPYq7rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JggIMQEbMBiomHBF-gWwZVwHXZj60vyXWrbdrNl8n4gWz_n6wIYsksgW_4TClFpDhgBJktUFCMxFRD9KN1d1sPJjtoV9f-Uto4C3epQueEnF7MrMEkSdN2aC9OdVju-Fp1gRub8E_vKvywZxMS_dcN9Gb4qONImy02NDUw12gp0BW2dUJEa9j_ugzTs0jUmn_ZUgrjmEGL8ZQ0vQp9YgCRTPS-bQpTso-B0un8zmwdhhGQNh3Um2c5-779b2zkB_qRvTvK9zHZTdnQfqoJbPA3VIJo2LSQgqnD0M5oCjIVKtyunONOukrr3XCMpn4nuCgv0r3qyRRDZ9k_ydXdcfew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCmLApVyJtezkRgu4rFt95x7QMeUA0aeRGff41-CIhegPgmiTAewrRvgduNwn4lqXFX2Y53ZwjM3aegxE4Qa2nfQGDRYgj4S1hYqkLpIO5qIrW_T0TmD2TQkE7FxGKEHHcPRDgF4KP_tL4THPuDWgEPTAhkHILyswrdLuw1QsFTevrTYLG6xlxrY5Mz45t5TFgV_68qzVWG28_CoEOp_wAnhGQyFhgbBM50hPWT5hTANxedLiH_pMWPpeCNPYrTr8hXK9ll-H-kvTcXjI5C5EXuTkCnyCeDfR4U0LUbSW7haZwaHQdYcDoGJ8gD8HhA4AoqMiSmzxIsO3kVPGoT46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UD5U3WchbG1E6b-smxvm0rKHMMCqmLzbAi_OV9y3DOm1mmYJZbbiuVuGQkQxqfzVPXrKt5uYS6-4Qxu8jW3qu9_ZFvMd5kV3XgnXK3-fOEympS80SY8dkuZ0j2gnpOla5wN5jPp51QWvG09eFQHumhHSg4TZBwjg_x-nETnmCDdgXEKYmyMKFXc-inrqueKjX6yKDW_YZMbMocAWlIT5XxAXPdAGqzTwJhcdsTeLzR5NqUJJz7d59xLD7YChIVi1MhxF82z0kHa22vJ6fLb6mDWWCr4UeT5XmpUjakfLHBj1VvKncGaFHQkTwpIx8zHrF-LyAdePSVaHdRgpzSznbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRf0ghuPb-IT-4zfzYFmPOw9sAutJtNPbTO3J-RW8C3UCh2pM5sx9xXUv3Bkdu_fqBUZwJ10orqnJMywdFwwqBEMJ1q3ZZDxOvTtU9LqV7pE5O_yOW-mkZz-LGZp2Qtm7mM9OBxvAr3U_S8cv0OnqNefcxOBAyuQJTOushBDyF69fyr4tiLktedZPRf62r8DHjF1f5_s4bjVQ__zLhYUxnk79vBKy2wNFLSfIF7jrZa4nt4zG_ajOblj4KjBNw46Q6_coP9Hdt_wXvGODZd26S6HYbNqkm9F3jp6T_ty5TJ0vqnQKeTWaXX0D6OJMwFYgzHOkCLqWPppPxAZYoR-eA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قدم‌های عاشقانه در طلوع آفتاب
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/454141" target="_blank">📅 05:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454140">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8a3bff1d.mp4?token=PemNtQ_jxOx_3dpzD9R1-3vQJftihIgy-WBwJJyOQ9FVNVz28rkYxPtqltnECdhcZdK141zlK0la8pf6KjrHYJV3shnv8Uuz06f88usEiIrMFhP3VSZ2cLpLKpUj62sqI3qfeAXNB_F98V1fisouiEJuE3vxHhlN9zCv5nYjC0cz7VlMFfAmAwqDc6inbX1qwrQVmjNof42TwkZbFnFR1wwULUvalxvTi_3HJxK69VENmlHi-ZYBX-6Bg1ZCSm3UITVjVaHkOLzHWNu7sN62YN-Avfg3gJzJkTL7LIW-V41WWJiZUK5CuJQ8eT0BnekGHbSciSHMKsDYU6C5Msw9mTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8a3bff1d.mp4?token=PemNtQ_jxOx_3dpzD9R1-3vQJftihIgy-WBwJJyOQ9FVNVz28rkYxPtqltnECdhcZdK141zlK0la8pf6KjrHYJV3shnv8Uuz06f88usEiIrMFhP3VSZ2cLpLKpUj62sqI3qfeAXNB_F98V1fisouiEJuE3vxHhlN9zCv5nYjC0cz7VlMFfAmAwqDc6inbX1qwrQVmjNof42TwkZbFnFR1wwULUvalxvTi_3HJxK69VENmlHi-ZYBX-6Bg1ZCSm3UITVjVaHkOLzHWNu7sN62YN-Avfg3gJzJkTL7LIW-V41WWJiZUK5CuJQ8eT0BnekGHbSciSHMKsDYU6C5Msw9mTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سربازی که در صف تماس با مادرش، و دلتنگ او به شهادت رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454140" target="_blank">📅 05:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454139">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c670bd2ac5.mp4?token=jch5kdP9zmJq9kEvLW8GI_nx03ZRUb2ZqA7bX18NU_WsR4aZD4ZGn9EZf-wBBItwlJiN_Uh0FehkZ26NLahgk5vyXaxlAR-09-dgLmhFp_4MdOCgbFtz10td-SWeUxfIgOZugSIGq2OFNIz81fjQw3Pe3ysRcnLLM1xrx_Sa4FUe15ZtBX5e-kVNKATaXH0J8T-X3dp8Nwx0L-R8fnPmvNcBYA6ZsfuSS-fxUhvg7j4lJxlqg0J1GuLSnJbwBXsO7hMNOUzwBOvOwFolXdAv9_JyELG_Eh0K1rNKrJE5fYQOV32sa8PJ7O_SJUOO9Rtf-M9iV_-4PZ2H3j4b_iSquw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c670bd2ac5.mp4?token=jch5kdP9zmJq9kEvLW8GI_nx03ZRUb2ZqA7bX18NU_WsR4aZD4ZGn9EZf-wBBItwlJiN_Uh0FehkZ26NLahgk5vyXaxlAR-09-dgLmhFp_4MdOCgbFtz10td-SWeUxfIgOZugSIGq2OFNIz81fjQw3Pe3ysRcnLLM1xrx_Sa4FUe15ZtBX5e-kVNKATaXH0J8T-X3dp8Nwx0L-R8fnPmvNcBYA6ZsfuSS-fxUhvg7j4lJxlqg0J1GuLSnJbwBXsO7hMNOUzwBOvOwFolXdAv9_JyELG_Eh0K1rNKrJE5fYQOV32sa8PJ7O_SJUOO9Rtf-M9iV_-4PZ2H3j4b_iSquw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
برافراشته‌شدن پرچم ایران در بین‌الحرمین   @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454139" target="_blank">📅 04:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454138">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">زمین لرزۀ ۵.۵ ریشتری در فلسطین و مصر
🔹
مرکز جغرافیایی بیت‌المقدس: زمین‌لرزه‌ای نسبتا شدید به بزرگی ۵.۵ ریشتر، جنوب فلسطین و مصر را لرزاند.
🔹
خبرگزاری رویترز نیز گزارش داد، ساکنان پایتخت مصر زمین‌لرزه‌ای به بزرگی ۵.۴ ریشتر را احساس کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454138" target="_blank">📅 04:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454137">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCu-XKfWo7fg3zJa8ivRoZRbbHg8f1VEowfT1YN7dKyasAHIkLjCRluJ3isgeHdLWiuOHrjDnO0Atw-q1pW8d3mx7OIhNsjO3CW3L01rkyhOYCt0oBvzHi0o9M4HVzyjeIRkbJarLc4PmDQAeZjgEAQ4tHOP6D0EoZCXdRajBOrnmeJ2KMKO30gwa4vbFBzJw_azs2X0fhlhWm-sahpn18-viJl8do3hAU16PueqagKZzTdm4JA9qFHXho82_6FJJNmF1B_co7pbnKaAdB-TkV-XjxHf1MjSY4F9bJoj_a-K2FVx4nan2dv2WbFV7QkUXlljiSClCjtJwIK2zxFtXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنش بین وزارت جنگ و ارتش اسرائیل؛ ارتش از دستور کاتز سرپیچی کرد
🔹
درحالیکه وزیر جنگ اسرائیل از برکناری فرماندۀ فرماندهی مرکزی ارتش این رژیم خبر داد، ارتش اسرائیل از این فرمان سرپیچی و تاکید کرد، کاتز هیچ اختیاری در این زمینه ندارد.
🔹
روزنامۀ یدیعوت آحارونوت نوشت این اقدام یکی از شدیدترین رویارویی‌های علنی میان وزیر جنگ و فرماندهی ارتش اسرائیل در سال‌های اخیر است.
🔹
دفتر نخست وزیر رژیم صهیونیستی هنوز به این بحران واکنشی نشان نداده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/454137" target="_blank">📅 03:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454136">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کشف مخزن و انشعاب غیرمجاز انتقال نفت در استان بوشهر
🔹
فرماندۀ انتظامی استان بوشهر: انشعابی با لولۀ ۴۲ اینچی به طول ۹۰۰ متر، و مخزن زیرزمینی ذخیرۀ نفت در شهرستان دشتی استان بوشهر شناسایی شد.
🔹
تاکنون بیش از ۵۰ هزار لیتر نفت خام به ارزش ۵۰ میلیارد ریال کشف و تجهیزات توقیف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454136" target="_blank">📅 03:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454135">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeZUfMMDm5nR_GioVALFJD9_Qub-L41RovuTWWGG2X2JJn9QuJuR9xJ2rKtHd1ngBiifmbImvIWs50yoABRfag9JOWt3CCRnqQvTMhLEnnbBYl9JMb1f3IvGeFh_5ENAqnNP7N2c8NbA3VVWMnUZDWxYGZQP12fG_EVUoGx_ShfCKWluaI1oLd5dP_Ix_8i-jXUOyNEykBeM_IHocFtOoRFZqOVj1Z7i5-kw9b5_Sa0QC2k4HIHu3Fl8mpiQ-YrC_LxGXjLWL5MTPPzOYsKiIsiEBBDqO-J77nzAlDUGOGoxjkzlvFYQzlCoSIVx8-vdozljQC54lQPuYpLFvmPDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب فروشگاه‌های کالابرگ تا آخر تیر تسویه شد
🔹
در حالی که برخی مغازه‌داران طرف قرارداد با کالابرگ از عدم واریز وجوه خود گلایه داشتند، معاون وزیر رفاه اعلام کرد تسویه‌حساب با فروشگاه‌های طرف قرارداد کالابرگ تا آخر تیر ۱۴۰۵ انجام شده است.
🔹
همچنین وی از الزام فروشگاه‌های طرف قرارداد به اتصال سامانۀ صندوق فروشگاهی تا پایان شهریور خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/454135" target="_blank">📅 02:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454134">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8yTLkMHHi1dmhLQkyw-VgCN2ZpkJjU6ZGadhQ6ZS-JUKnxPe_cfTOfS38hMjWEbZmoPN8Dsva9pdS_N0syGeVnngYMhwFJmYjwC0PcUH8wju3WrnNEB2kRXgS-u7PmWtnKuPPuf2PJM3JMITA6RJV9HfhElHE2POMqeWb1bjVun-xjrd5-w2fJxRdm8hXAEiYk_aBeK1oeonTZdtrjUPCicK4YX8UPg0uFK-_2mDKhfTHdA8vlIu_zELZjI7bkBk2xFHbYp0-8RgfWan59lA7fhAmMYUmQvPzROLUlQUucZdBfzuCmb2u2zbr6VeKnm37FmiCNQcDgkw_INEqPudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه تختی هم مثل آزادی شخم خورد
🔹
با اعلام مدیرکل ورزش‌وجوانان استان تهران، ورزشگاه تختی به‌دلیل کاشت چمن تا حدود یک سال آینده آمادۀ میزبانی از مسابقات فوتبال نخواهد بود.
🔸
سال ۱۴۰۴ چند بازی استقلال و پرسپولیس در این ورزشگاه انجام شد که اعتراض کادر فنی و بازیکنان تیم‌ها را به‌دنبال داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/454134" target="_blank">📅 02:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454133">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
وقوع حادثۀ دریایی در دریای عمان
🔹
رویترز به نقل از یک مقام دریایی انگلیس از وقوع یک انفجار در نزدیکی یک کشتی، در شمال‌شرقی خصب عمان خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/454133" target="_blank">📅 01:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454132">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ادعای ترامپ: از دوشنبه مذاکرات با ایران آغاز می‌شود
🔹
رئیس‌جمهور آمریکا پس از عقب‌نشینی از صدور دستور حمله به ایران در اظهاراتی مدعی شد: از سوی عربستان، امارات، قطر و حتی ایران از من خواسته شده که حملات را متوقف کنم!
🔹
وقتی متحدان درخواست می‌کنند که حمله متوقف شود، باید بگویی بسیار خب، ببینیم چه می‌شود. متحدان معتقدند که توافقی در راه است. دربارۀ تنگۀ هرمز توافقی وجود دارد و دربارۀ موضوع هسته‌ای نیز توافقی حاصل خواهد شد.
🔹
ما درحال مذاکره با آن‌ها هستیم. این مذاکرات از فردا بعدازظهر آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/454132" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454131">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NngK398En3_DsXUWoiOhJc_WGY_7nHexG7X7GkAHsunhxDA4VhkGh3m4nQmd7sPWNuE7qjSXVuueCZIWXl6_gB-1hoAekXyqZ5qPHFatdm-WlXIXe5VYD6Rq3lwW4Aif77Nm3JkH-2rpNyjdidiWO2x0DXkImx7kCkJRz5jQuUISKVQSLTsJzC_BMa_N4e8LW8tQD9XWRY1Cv5vKsHIqNVwGP_hQTkMlOz7nHK0z5xziFv8XlWctdJri4NY7DswtLBdy-LDTtx5Hap_-1wGi5S0Yvld1JlBBXY0t6FxMdp6aj2iuj-JIYnAGfEp8fD3LKe0kQqq5ZnaHXTbfYcbUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکۀ آمریکایی: مجروحان ارتش آمریکا در جنگ با ایران به ۶۵۳ نفر رسید؛ ۱۷۰ نظامی هم ضربۀ مغزی شدند
🔹
ای‌بی‌سی نیوز دربارۀ تلفات نظامیان آمریکایی در جنگ ایران گزارش داد  شمار مجروحان ارتش آمریکا به ۶۵۳ نفر رسیده که از این میان، حداقل ۶۴ نفر از افسران ارشد بوده‌اند.
🔹
این رسانه تاکید کرد اسناد و داده‌هایی در اختیار دارد که نشان می‌دهد در حملات ایران دست‌کم ۱۷۰ نظامی آمریکایی دچار آسیب‌های مغزی و ضربه به سر شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/454131" target="_blank">📅 01:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454126">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnvvN-u4IXtag8Qzkz0G25AL6zHPb7gIoWbX_A-yrM43Xp7X87gJjgm7QY2FM7VIrL72msgen3U7bd7yX5iUJjCzwOrMkN-3OHc_MmpDQ5qYij7O8O7TnQ0qB9dLT5nIHOg-ATz1RXwPWLbaxIR3Xz1OF6AHfR8cN-U248ptWHY6fsrnjlEPx4-aiv5eGfu12SY2k1FpYqficRByER23KVBsxo1tS1uTTsuoeB9PzBflqOD8wH-tQ3-68ILgbVYX_X4aMfSf-E1Rati8RUqca-IOz351YAbqJcBb6Ej__vXMdevOqbqJuFRawPXv5vKqWQ_unHQFB-yvHqHsmEZn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mP79Dsyb6vlBHiLmzRNO58JG6UHowB_zJIMn9RLG3Tlq4q1xRrFG3CGmhFqph34-rIT_9C-hIVtcNOLQ2IQvAlOsYyP3fI5qKrr5jiaIEx6AEbiVMguQTAToGUA1HkO6RT5nG_nrJURB3UOifIP2wA98TSLBWzJS135ukIvk9vbTskz6q8j0x6NxGMslZaztSEhWqJmsfTEF4SMzD8WIKz81cfldfHl43r_5b9PsL8rdhvD03v-fSJQItEgzkJL8BCQSIF7mguYnNwKCiSaSKPntVAKHqVAWBHjWapmoIbOtSM_6pLBh8WWIttLNWyOI1BdfghBbgbde0YDsEuSIAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQlB6Ja8yTjvfWCAONZpDaLWsIv6AU853_9de4028JZlFK-JXNKCY54vs4kPO3BLWhLnzlrm53I3GRk4IYqORmF_IDB5Ci-n48tPTCZu_gRbRdsT7IvuN7L1TE2kTmTkmGqzXl3PpWVwNFUx5eu6Z_ivD5pzynuCw0zigeL2gMxb-snSDCoNCJq6QxJ2qBcb-dTAY0ak3eBWup42BI9CaugvssuTzG57BFDuXvkJd3xoNtXmymaVPWn2E4-ZmTfWlBO7EjDdKKJblRutU3IYjsk-CQSU7vquMTPf-QkbLVDNQH0QurCAHW7INTXwBvM0FyHG_NqGJkstwC5iZfr-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qm3kygWBaGbpA_qnLNzdlbwR_gkQIfJ9nnfWSxF5238SdUTUefEH2685yNlCqbbegKzsMdj1DgAuMSNuA_BqomEApdbZMy2qWvZfqeB0vXzbAdYZ-QkRKTeJVQpH0mC-UozDawziQPtok98UMMQpKfVOpQZoupFW30Tp3QKalKOH12_4mpda9uCoK-ST-6aki9wTD_PtWTtCMmX241rhM4hkoJit1sLjDpyGnceVQwp46_ialzSc0KGEHBmrkMm0q3DOx6IFcFTGM00jla2ZBJGILmIsXivvmpEwd0_MsI2T2WydbZSgc62DtnFOv9K5E256lm2QHHJkdKg4zFoofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-Y7a_YNInfprbwuAd3qIpgqFfZlkSrUV1fP1C2-k-NS_-vJWoqyFkS5A7kL1IpgsLXHhrM9u_MWKCZTQK1Vv4n5O_b63MCGW6oEcWVBcSkgHWcjsvsjin5igJtNZB9Oy1mFPaY45BmpRAGRVxA37vApEa7nF2OVeX8WRO8e9-kLW6QCKpOOwSK1Fc38nEr3twmWsrrYRFJBI9i-8F2CD2EggovkyYk0i5WMmmVKzWq-ssUU7c9XGE9TKYMHGnucD_xzb2i5ODH7rujozhKT2082WhcDQYy5o-ehBo5StffX08jjWZMdJPb-vjd9Og4EDEHMtZc63XnWVN_iz6Wd9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۲ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454126" target="_blank">📅 01:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454116">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtkZk7mnSeYJLqfoYVd_Wggfh1vVGoTHVxADGWzpQ_ohWtf6zrYw874kCKRltMS4FvCq0PNzgMtXljReGmVkY8fOVqbzZzCU2JzY3Oyd09pZgJD0VVOmJrofRz9CXKxk8lvaY4jOKDRD-2Y4C3lEWzzsavB0tx3wEZocEPO2FkLvXbK8dXKtjDLaCbyAieh8rPkPj92eIW_Yorpr1fX0KuB9V2NSYKulslj2exUxTQPkztKB1y_GwO6R0d_zC0WvoWM9gx_MfCfVhJamnDfXWKEh_z_myM0nzIUTFbMWgaN719ip6g0Jp3CKWf3TqrJ7kRpiVkHxNjpvSUO2WW9eLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bEzOg6AkSrfq1z5xWOYiUj3jlQR13SLdOltF14SZhTwAgj5N0rPMNXJ_t9CTx99I1QIDfhzmgPfjanKcBe-90aD8WiwLm9xKRfhoXDW9UXeXcr3Tu625joE5a5AFpNeDXA06p8eRPp-LBufYVsTfJ_Rxnf-I9M-483FBnnPbyiXPZdflo8SeYTyc16K3Ooparpz414-xsjXnrA9Hf7_HV2qiMHh0-nK0kR_VmiZeVbHJhifMCTdQHKyHX0qn37Ob-IT4mQ_AKiqFR7LsWxkRV4KxxMyFYtJ0smixdHno2lCrrLzN21Pq2UcM7wjZ-u7KNMVhEz88pWfbNq5BMt8bzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3wz1EInNDOlbWwtnGhrZHtTeKG3N0la7OH7F-xwSAJhuWbTR4_nu46UMqP4YowpFznhvAFoCpQ1fqthVsi9qhT1jt6PhORgv0Gc4Ayyd06dJ3sUsCyOGADdaCDDiYVA3fOJ7xzC0CN-6HfUKth7zaV0a6urYiyzVxSSkVlREtv-d2m07cRSZo6poUWRM6kzRXSBZPfRRXz9DYFCnIcIIqPE1SxgzuXzgwH2ciWM_YLLlJsxP-SQ-CiD0iAAP28Fjlbce-50ZgSHy3MXRQ6khrN67P495aT6TeZywNCHP0gvbspkH1YBE1UymIRPjS-D0LLaaX3z1zAFClp8i2qbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVYJycbYdJ-vIgw5S_1V5W7gJ-eEXtNYxOx7ypCL5_Ltb1njUUbedeh3z9ebJSfeliA31exPkQ0AbhY8G-MgOm9R2dKOpx-ggkhPldPxFQXnyDfUXcHza80JRhFbuX9mALz0OneUTRwnx2eABIpapEeJk0zZfoWPuFWN6VuL34sUU7ebJ4iMPQm2gz7cuppqJVgHfxh0qqBxymSXMZMk_MUXc5wcamMD4nooV01Os8w1QCmwq6bPnQdFx1zfcQdYUYJ4kEm1HECaLue_oRtY-NpuuF2PnRFBsUn7vV8TWwONN095hZ9JLalKhbeg0pltLMLX_6PzOqaDxd6NXy_Pkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrUMcVx7blghHTAoXKj5I8Knn1U5qsohdt1nvjTw7iLR1npQeEao1ZkCHq2SAE5ZQQhdnAhq8bxgd5HXLAw8enLAQMszK7dz22UytDhOviFxnqO0Lm2kQhffuHsTotw2oQIxj3BsO_84Ta95TZkPOtKYI_XAustJuQ5MEJsKDdEoSSs6ejtZJvzOtCqin0ov0gWjLeiydGyJLq_rsg1GSRdUBij19FDXxGk8jZfsJAwy4KmWGfosvZOLGLWDecs5GilZNG9iR0nKGuJBOM-StQxliDN4MPckB1oY1Myzl3_Wbj0j8wZ1gxJwaZTk57zRKGYNChs22tMxl161orXjhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFap-TBYHznkfXxvn8cVryt-_cjlGf2Ajlb65kH8ejUU8pYB58abt52VVi11vO_DZCdInTB3yWuX7Dg2JXIFfMOH4fnoW6IbII7pw5hd2sCM-CtIYKZ83lkNzXbVRH-rE_TC5NAtGQYmUxT2Q62mtK0l1vxr2K_KB8NPl7yW6zMuux21jZdrm1Oy2pQX9w3_0ALGw2WyH4H0wFYDeTn0HNK05wKeWjKzeVsY9tMerBxVN1cXWudPQwOWPob9ORKaYhZyUFPqclj8DT5wGeTCehEFYF8ELqo4F91571UgtFp9LVXX5KVO7phKA9Y0uGPD7x8ULpObrmPunH5TxuMEuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4O-_hkR7AI-dhf6_7Bp32X66FdY8n1t_4teLNM87gQLjdwX0qfMPDXdX6bm7A4UaAthToiLJ-eiiqKjPKqbyL3VOdAaZkKGNod36NPH11FJ3Pmj5u1mUo3mymUOYTSgGJosd69XZ4Ut3PBXUEUsVexAJXCZNnhsUISsRQ-gIkfJT2cxbEdDEptmXzZeubmkbdmsavi_WxzhvF1L6L09gPoNhE2AFtczG-CJT3KHLRSfFiCL2D76N77wQJ1rGstY2iWXk-vOOSRaVrtbeN-WgT6zWys6AE3MV4JIry8kXRLtUlBBg6BJf_ZFjdI1GS6RmmE4Lf-ogrT6T9DFGHqmlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PW_YxpNMJafBB0TyfSi4wiDuorGcA-uc2vUcv5x7qDXaSd81EkyjU4SsH8knb-a-So7nEWwWiIiYW-2ckgSVZV_MALmH2xC3Aq9GooeyoWPlu2bt5Kkp3RRnHlt-q0TAuOf9uwKMtpQfi7ngAgvdfkq_9MmAbX75hsRhecpzYN9XwBhTx9XqOzVNT03fLnYsthUrueXb_7IrJThUbCkB9GnMMwpgKNewsMXpyTIzdVEwMJDJ4ULT5p4SlnpMf_Y1c56-KPR7zbVDT8nnKE5mLAa3HI5xlloaUid6WqBhoikNoGyiItj_p59VWb9HRdfsOpnzvFPEXWxWHejyfbEx4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BM4IaXGaRpV8z4efr4nijAMFs60ATrdoIFiM-2yhzVQwRIOcHjfpYuk49ECvh6XXPx5NkdvQB5kGzgJf0otZUwI0yvG7-pYMairrv1mWeg1Lv7D4BqS2visA_SFDd2nU6Tku6pckCA6567Pyu7535aLi7K3b7-B2fudmJF2Hq-IT97EhaW0MWDVWtarRcCHyXleZCsaLuCcQqJe6fCuiHPQrw6mk2VqnVTqFEmYhk6HEqLv4BrL14ZnHxCV9bXdEEO2Kt0RgJrDYMstVzm-QJ7-_B9xEEbKZDF2ttHyg3ieKWhMDWjBuOfhGvTxUFXszCN_1kBn0oo8d-ZBd_3GVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEdhrCIroLVcpH1o73WXD-dK9e_VE8PFflwhSfPjdBeQzCAMKXqYq5bNI-9H3bGcDmgJRVDO4wtxuXhlJrVA9cEmoU1ozWUotiUNq6lHH6RmbVUfSJeGmGtdKthznGeqTluwouYY0K8cPvimOHWRWvrku1axrCsm8ANFvXLvfJ9hi1Q9zfUYHGca32YfilWB8pWLK4Y2JfFo1ec1_DWD99LNxGsv1tmw2-BSJJBWwFWNe0xYJdViH_BvacdS-hDF52tJ0Z1fh_2WB3no5RioX9Yizfo-6hj9eQ-JDOj5vxpC8fogneQoqrEEEl_Kz1g4LckFN2s6N-Q5bW-ivPLWvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454116" target="_blank">📅 01:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454115">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMTvKMOavBwXUrqv-6dq_6Sq_rUwTKOlo0Oy5WXClIG2IOlMdcMi7H5dqhtW6vhNbF_P_Qc8xkzhJwYakh2E5KO93FzlZTTMSEa1EOAEI1aTSh4IPw1-Ve3xe0YF9uvubnAv_mR5oCTh7CbEXlLs8QPXw6cPcQBLsFVPvT-jL_1OZW8PfrGJ4QEuJlT-v8bd1bQXZD82Krqv-3ci_5WkVPi8zrZcRYCJswJTTmmkJ6Jxvazm1N77xMm7slGsgX0UImOgp2sO58scJXLFSBP6jqRKEXPKHtbuufXWdDaRhMDOZNOo_8sPb0TSzyFKgFCI4a03aL-unYbpXPakfEEg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، پست‌هایش را پیش‌فروش می‌کند!
🔹
اگر کسی بخواهد پست‌های رئیس‌جمهور آمریکا را «چند ثانیه زودتر» ببیند، باید ماهانه ۱۰۰ هزار دلار پیاده شود! چراکه گویا ترامپ رسماً جایگاه ریاست‌جمهوری را به یک اتاق سیگنال‌دهی و دستگاه اسکناس‌سازی تبدیل کرده است.
🔹
اشتراک ماهانه ۱۰۰ هزار دلاری برای دسترسی سریع‌تر به پست‌های رئیس‌جمهور آمریکا، در نگاه اول، تنها چند ثانیه یا چند دقیقه زودتر ادعاهای ترامپ را در اختیار مشتریان قرار می‌دهد؛ اما در دنیای معاملات الگوریتمی، همین فاصلۀ زمانی می‌تواند میلیون‌ها دلار سود یا زیان ایجاد کند.
🔹
دلیل آن نیز روشن است؛ تجربه نشان داده بسیاری از پست‌های ترامپ، به‌ویژه دربارۀ تعرفه‌ها، روابط خارجی، شرکت‌های بزرگ یا سیاست‌های اقتصادی، توان جابه‌جا کردن قیمت سهام، ارز و حتی بازار کالاها را دارند.
🔹
اگر تا دیروز سرمایه‌گذاران برای تحلیل سخنان ترامپ رقابت می‌کردند، امروز باید برای دسترسی سریع‌تر به همان سخنان نیز پول بپردازند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454115" target="_blank">📅 00:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454114">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d3c943d32.mp4?token=NGKz5303vNMDrBMBXaAQgloSc0SsNZg9Cl6rqUa4pls-1bFOsT5GPoJRztbSaQ6LId98iwb8gmvX-4ch0SIYoxnygD_RD3M1U0SHATTeaqmUuODVyGFnV958d6zTaMANw4gnAyRfGB2WKmGlsCcfawUpvLVnurCFN4DfMbDmQgqXUGFSmvuo0tkAepER3CTwkGQdeVi1N_bVjZB_9jgtUAmTdVY6D41r4bOleHBkSvDDrvxFepxX2LTEjZTdr_VbgOBCJ6_6dqVl7gSmw8AyWwMNnc5nspTpu6oBTF7i7WPGN-C-XBfUY_yaReUhQb4HVfuaNOXfa0k0QNaHAWVbPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d3c943d32.mp4?token=NGKz5303vNMDrBMBXaAQgloSc0SsNZg9Cl6rqUa4pls-1bFOsT5GPoJRztbSaQ6LId98iwb8gmvX-4ch0SIYoxnygD_RD3M1U0SHATTeaqmUuODVyGFnV958d6zTaMANw4gnAyRfGB2WKmGlsCcfawUpvLVnurCFN4DfMbDmQgqXUGFSmvuo0tkAepER3CTwkGQdeVi1N_bVjZB_9jgtUAmTdVY6D41r4bOleHBkSvDDrvxFepxX2LTEjZTdr_VbgOBCJ6_6dqVl7gSmw8AyWwMNnc5nspTpu6oBTF7i7WPGN-C-XBfUY_yaReUhQb4HVfuaNOXfa0k0QNaHAWVbPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظی عراقی‌ها با زائران در مرز مهران: اگر کوتاهی کردیم ببخشید
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454114" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454113">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPiodd2uYErAUAzgBWn1deF2HolMY8TNpdgQPqeNZCWiseolhE305t5XDcGPD5T3An8W1iPW6jl4UB1-F2n17u-iAd867yIMP7CWrxPcJJpMvdFeil-Brf_e-m8K9JkJLRZSGGwfBWeqsmv9O8Cu1kvj-Ht7VwkbG156lua7MqXfIawQYDBti8hbJTgD1lyvGnJuKGKgI2FSofLI4INdfZt6MNRQSoinJfqvZrDfmIdoRn5xCvm3d_lRWJxv3olmB5biN2UWyF9I8O4ddWF5fDsmwj179p90Y7LjJ9bwkp-8coeJGTAIcxhrPhDO1RTu3xpPcUOm13j28LWBKBDh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین ژست اوپک برای افزایش تولید بدون تنگۀ هرمز
🔹
اوپک‌پلاس با افزایش تولید روزانه ۱۸۸ هزار بشکه‌ای تولید اعضایش موافقت کرد که آخرین مرحله از جبران کاهش تولید ۶ سالۀ این گروه است.
🔹
کشورهای عضو این گروه از زمان همه‌گیری کرونا و بعد از آن با شروع جنگ اوکراین برای کنترل بازار و جلوگیری از افت قیمت نفت، تولید خود را کاهش دادند؛ حالا دو سال است که می‌خواهند به‌تدریج این کاهش را جبران کنند.
🔹
درحالی در این توافق قرار است عربستان بیشترین افزایش تولید را داشته باشد که ۵ روز است پالایشگاه جیزان این کشور با ظرفیت ۴۰۰ هزار بشکه‌ به خاطر حملات یمن تعطیل شده است.
🔸
تحلیلگر نفتی بلومبرگ می‌گوید «تا تنگۀ هرمز باز نشود، بیشتر این افزایش‌ها فقط روی کاغذ است» زیرا عربستان، کویت و عراق نمی‌توانند تولید خود را افزایش دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454113" target="_blank">📅 00:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454112">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مسمومیت ۱۴ شناگر یک استخر در تبریز
🔹
اورژانس آذربایجان‌شرقی: در پی احتمال استنشاق گاز کلر در یکی از استخرهای تبریز، ۱۴ نفر با علائم مشکلات و مسمومیت تنفسی مواجه شدند.
🔹
مصدومان پس از دریافت خدمات اولیۀ درمانی، به مراکز درمانی منتقل شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454112" target="_blank">📅 00:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454111">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bff5fe5a.mp4?token=Trb-eQj3xGi2Nqb4iD1CAhibvS0VyEBgobwJtOBDkE9ZlEX2iaCWPyoPZbWh3Hxlc4de4-MCUA7ApODYYDHqx876KqeOhG9y1N2fpv3s6_ZyiZi0eItYndjn1syMyDOSG5oBzdSJeRMQplom7NqxA39QnG8u9X8KjVA0yhhJJRmzeSN8Ks0iQQEzfgXbfcpQT8ord8LIZMCLlKrsdRQqk89wtxZJI5OUFzLrpUicw9yqNwwKual6y-G5fylJNKt2g23DeQGdjIv5T-4YHbiNMUocyhrymLoZ8dfFGTJI9_Hsx27pQ_jJLsVKqQ8UfL2lo5Px6G1d5R4UGg24rKhA3g7S9WZS3YQwxYtx_V3D2BeYFxogVYJ9iSFgPR5OXb2eggqDiTW2oaQltVpUxoDWaZA7fNryTXjCBTLVYnkXbZ5m3MsYvVXOsch74laoaAca2GcGx_OSFhYVXM47i30tAlzrmJt32nuQPeVkw5dyN859vmh0-SdGZA1HW3rYbFQBXjReKyMpdcN5YzVY5iInRH_XJVOggylYPwl4_qnslfHkGhlXg7Qwocp2EF1KdkzJ_mcdf0KsLan7zlp_HxnFB8YyEBJnQ-hWCqlNchiNS9YvFikuZh3kSn9Qmovp5TEWH2ybFPW-_Z3zN4ah8jXlwjzUXz4SpqoSI4SEwFg37pM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bff5fe5a.mp4?token=Trb-eQj3xGi2Nqb4iD1CAhibvS0VyEBgobwJtOBDkE9ZlEX2iaCWPyoPZbWh3Hxlc4de4-MCUA7ApODYYDHqx876KqeOhG9y1N2fpv3s6_ZyiZi0eItYndjn1syMyDOSG5oBzdSJeRMQplom7NqxA39QnG8u9X8KjVA0yhhJJRmzeSN8Ks0iQQEzfgXbfcpQT8ord8LIZMCLlKrsdRQqk89wtxZJI5OUFzLrpUicw9yqNwwKual6y-G5fylJNKt2g23DeQGdjIv5T-4YHbiNMUocyhrymLoZ8dfFGTJI9_Hsx27pQ_jJLsVKqQ8UfL2lo5Px6G1d5R4UGg24rKhA3g7S9WZS3YQwxYtx_V3D2BeYFxogVYJ9iSFgPR5OXb2eggqDiTW2oaQltVpUxoDWaZA7fNryTXjCBTLVYnkXbZ5m3MsYvVXOsch74laoaAca2GcGx_OSFhYVXM47i30tAlzrmJt32nuQPeVkw5dyN859vmh0-SdGZA1HW3rYbFQBXjReKyMpdcN5YzVY5iInRH_XJVOggylYPwl4_qnslfHkGhlXg7Qwocp2EF1KdkzJ_mcdf0KsLan7zlp_HxnFB8YyEBJnQ-hWCqlNchiNS9YvFikuZh3kSn9Qmovp5TEWH2ybFPW-_Z3zN4ah8jXlwjzUXz4SpqoSI4SEwFg37pM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش عراقی‌ها به دیدن یک تصویر خاص در مسیر «مشایه»
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454111" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454110">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2deda5123.mp4?token=MWrddv8rarTq5Odn8JXkGKgZK5uIDAYKRaEHOg2s7i4vDOk3PbmlZX-whRjA1wnKRRJpA2iuLIRBdsb7oTpFxDHd1YUxUhsDNVIU2CXy7PZdAqUpvwBzbD8AWqXIlqf9t6teZq4AOkIsQ0CkNFWx4Aln44FL1FY7Icq43W2lXa7moK_5kMT-3fBRbQPo1cycUxw7tT9UX5gBOcRgovcCqCtvB7V69xfnsZIAtAiHphR0iQDNfU3sNVYDxxQU6hCx9gMAk80Yfdao2VQ3WbhJFshABpnOqHJGbYa5nF9w25bK1ic2tAVPPHSaw42bxxlTIiP08awbBPwTYZ-kxUoh1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2deda5123.mp4?token=MWrddv8rarTq5Odn8JXkGKgZK5uIDAYKRaEHOg2s7i4vDOk3PbmlZX-whRjA1wnKRRJpA2iuLIRBdsb7oTpFxDHd1YUxUhsDNVIU2CXy7PZdAqUpvwBzbD8AWqXIlqf9t6teZq4AOkIsQ0CkNFWx4Aln44FL1FY7Icq43W2lXa7moK_5kMT-3fBRbQPo1cycUxw7tT9UX5gBOcRgovcCqCtvB7V69xfnsZIAtAiHphR0iQDNfU3sNVYDxxQU6hCx9gMAk80Yfdao2VQ3WbhJFshABpnOqHJGbYa5nF9w25bK1ic2tAVPPHSaw42bxxlTIiP08awbBPwTYZ-kxUoh1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خلبان ایرانی در محرم‌شهر: کارشناسان جهان باور نمی‌کردند خلبان‌های ایرانی با جنگنده F5 عملیاتی در جهان انجام دهند که دنیا انگشت به دهن بماند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454110" target="_blank">📅 23:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454109">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKebKzgMAFHF3OMBltpHZBnnfjj0WK1j5_iRPntE7HxTkUPFMbMGrUl2xQBccp-LOfyfbh7ct4N5pKYJyK_-KtXmxzLvi4k17-fp2-bQnx-kozyBU-0IUg3ubC8TOx-IwXIBkWs_MvslwvUcQ_HgpZJKpsyHWfaurOevCwCNDtsAcue3PJVFzFHdaDe6sL0ByqOu7bujS10ar6scyj5j-gN-STP9hhyi4BMYrYl8uIhmPq_ngY8CyeNi7ftmyNb46Cu5QgqkGfI_g1Ao6GFYfQ_jEcVNM10hd1S1FmYrH-Nfkzlq4ILQIwM_K0UlZjtiNmKXdXXkm34z7RxNOVIexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تکبُّر ترامپ» و خودداری از پایان دادن به جنگی که باخته است
🔹
پنج سال از عقب‌نشینی پرهرج‌ومرج نیروهای آمریکایی از کابل می‌گذرد. حمله و اشغال افغانستان به رهبری ناتو که پس از حادثه ۱۱ سپتامبر آغاز شد، اکنون به طور گسترده یک شکست برای آمریکا تلقی می‌شود.
🔹
به گزارش گاردین، این جنگ جان بیش از ۲۴۰۰ نظامی آمریکایی و ۴۵۰ نظامی انگلیسی و ده‌ها، شاید هم صدها هزار غیرنظامی را گرفت، تعداد دقیق کشته‌ها نامشخص است.
🔹
با این حال، طالبان بلافاصله پس از خروج آمریکا به قدرت بازگشت و حکومت را به‌دست گرفت. در نتیجه افغانستان به نماد مداخله‌گری و دولت‌سازی نسنجیده غرب تبدیل شد. این جنگ، نمونه‌بارز جنگ «ابدى» بود، اصطلاحی که نخستین بار در طول جنگ ویتنام ابداع شد.
🔹
گاردین تأکید کرد که اگر این روایت عبرت‌آموز، ارزشش را حفظ کرده بود. به عنوان بازدارنده‌ای برای سیاستمداران و ژنرال‌هایی بود که وسوسه می‌شوند بدون دلیل موجه، اهداف مشخص و قابل‌دستیابی و استراتژی خروج، عجولانه وارد درگیری‌های بی‌پایان شوند.
🔸
شرح کامل این گزارش را
اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454109" target="_blank">📅 23:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454108">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a169a1467.mp4?token=JL7NltOXZ48P7ikKttkbR0pOlBz1FEYM1L6u5pLhrJZkqFw7r6eGfOX1ignU_5ZKCxDAs4Vf_0ggGPt-Lveb5fmXp8tHdlUXXEn25fjiA-3yAFwKCR0N-xSvkMhilqwwVyYW447QsMYg8IVYp72SutYRHHA_FWLuZfiUN7EDVpw9vMwna2IcBJ3TWTNOsKI0UUgg8XFiieyBxuEAJL-Rqnb9o4b4SxkmMKcNPRqMx8FUSw5bg_CqpHsAuEKNQWz4iCZEJ851x8br7LrU_E4S7EeGcDLEn1gERmdvcRB2rmry0RKTGjbgRwsGfhCj7vB_p7RQ0i-0MEXG_V8mrObCPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a169a1467.mp4?token=JL7NltOXZ48P7ikKttkbR0pOlBz1FEYM1L6u5pLhrJZkqFw7r6eGfOX1ignU_5ZKCxDAs4Vf_0ggGPt-Lveb5fmXp8tHdlUXXEn25fjiA-3yAFwKCR0N-xSvkMhilqwwVyYW447QsMYg8IVYp72SutYRHHA_FWLuZfiUN7EDVpw9vMwna2IcBJ3TWTNOsKI0UUgg8XFiieyBxuEAJL-Rqnb9o4b4SxkmMKcNPRqMx8FUSw5bg_CqpHsAuEKNQWz4iCZEJ851x8br7LrU_E4S7EeGcDLEn1gERmdvcRB2rmry0RKTGjbgRwsGfhCj7vB_p7RQ0i-0MEXG_V8mrObCPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ ملت امام حسین(ع) به تهدیدات ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454108" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454107">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb6cc9232.mp4?token=mA5-WvTTMoPQWfrEyssbt1LlEfefDgiPHMr5lBILKQ9Tez-UbhfRZAT2t5b4j9vvgLX-HrJ9MWSQWUD8i54d5AuHsENubWpFFVju3JwIp8kaOP3VHr2EMK-cbM7pp7sxCDUULPAjFuczHklHM0Cno8BdKXMBSoNBhBk7jVT-dC2CTPqUMggkrhLtlYCOeCQEQVTRc9vONKxYabT_9szE6BzBzk1B8sXq-QZTLTTXE9oksqrsW8KhCDwdLwc2OxzggcTUj3sdUQ9f04z9dYabUYyvjDfNS310mI-AS_10u7U88BBvynfAClOgVGbyam8A3gpCRJGRvJMjDK-ntZhU3ydXPkO3Ef0MOuZBLtHrTBO7lT2hVJMgJVZbTv3H3aSfqRbjpmlicR5768-YXGuTxF066FSgSaHgI29DnqMUmNWtUNGa9zNU6wBLckDrhL86ehz7atWpc-f4i0IrfU-MmMGI10ImTy5OnrNE3jSvzQvyztsvUAcBRGyqfXhM2aQUvI3BfUDUb6pKTflyKgl3EpcCCkoBB4jK__ckUYkb2hBhwE45mxIL5P6elTcXSHSW5PwHaY1GPFRXx-VJf4JHdpxXezHe-LMVVOv0B-IQiTSZ0QiWU0GHtmG2eq2WgUJifSuDrG-CzD26yUlAMThWbNyjAvMnrb6V-MOcoqTRZTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb6cc9232.mp4?token=mA5-WvTTMoPQWfrEyssbt1LlEfefDgiPHMr5lBILKQ9Tez-UbhfRZAT2t5b4j9vvgLX-HrJ9MWSQWUD8i54d5AuHsENubWpFFVju3JwIp8kaOP3VHr2EMK-cbM7pp7sxCDUULPAjFuczHklHM0Cno8BdKXMBSoNBhBk7jVT-dC2CTPqUMggkrhLtlYCOeCQEQVTRc9vONKxYabT_9szE6BzBzk1B8sXq-QZTLTTXE9oksqrsW8KhCDwdLwc2OxzggcTUj3sdUQ9f04z9dYabUYyvjDfNS310mI-AS_10u7U88BBvynfAClOgVGbyam8A3gpCRJGRvJMjDK-ntZhU3ydXPkO3Ef0MOuZBLtHrTBO7lT2hVJMgJVZbTv3H3aSfqRbjpmlicR5768-YXGuTxF066FSgSaHgI29DnqMUmNWtUNGa9zNU6wBLckDrhL86ehz7atWpc-f4i0IrfU-MmMGI10ImTy5OnrNE3jSvzQvyztsvUAcBRGyqfXhM2aQUvI3BfUDUb6pKTflyKgl3EpcCCkoBB4jK__ckUYkb2hBhwE45mxIL5P6elTcXSHSW5PwHaY1GPFRXx-VJf4JHdpxXezHe-LMVVOv0B-IQiTSZ0QiWU0GHtmG2eq2WgUJifSuDrG-CzD26yUlAMThWbNyjAvMnrb6V-MOcoqTRZTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت مردم میهن‌دوست تاکستان امشب هم خیابان‌ها را پر کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454107" target="_blank">📅 23:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454106">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575dbde72d.mp4?token=rpGo4XkwPpVIsmkWYylUQDY8rkzH7wGBFG-bpCVnGbJpy91CFpebUhkiY6gNJfkWhzGMjwZuz8_4HlSoF-3P2eOrUzD6nvPHf-muwZKGw31Yb7PrbiN0SXeTd-LxjmfJEcoxJryRBJBhIGgcZWCggKAlR4BKcrX5_zg5uImGG9W-b61wfFqQUz8izXYGTo6JriBbK2SIXBDDBJ5o1LFK3orkveCpxUEbA8WFhO1nx6gtVgDCGNJqMGcT_CLELAcOsqMxAOF1t2zYXHDjiLWi7pKLsaIa1YY_oOA6IcDN3w7BCx12ui195eMGN1A_BGH5W0YB0x-YTRv4W6NeGfN5bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575dbde72d.mp4?token=rpGo4XkwPpVIsmkWYylUQDY8rkzH7wGBFG-bpCVnGbJpy91CFpebUhkiY6gNJfkWhzGMjwZuz8_4HlSoF-3P2eOrUzD6nvPHf-muwZKGw31Yb7PrbiN0SXeTd-LxjmfJEcoxJryRBJBhIGgcZWCggKAlR4BKcrX5_zg5uImGG9W-b61wfFqQUz8izXYGTo6JriBbK2SIXBDDBJ5o1LFK3orkveCpxUEbA8WFhO1nx6gtVgDCGNJqMGcT_CLELAcOsqMxAOF1t2zYXHDjiLWi7pKLsaIa1YY_oOA6IcDN3w7BCx12ui195eMGN1A_BGH5W0YB0x-YTRv4W6NeGfN5bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری مردم همدان در ایستگاه ۱۵۵ تجمعات مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/454106" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454105">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کشتی روسیه توقیف شد
🔹
نیروی دریایی بریتانیا اعلام کرد ساعاتی پیش یک کشتی روسیه‌ای را در آب‌های نزدیک پانتلریا (جزیره‌ای میان تونس و سیسیل) توقیف کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/454105" target="_blank">📅 23:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454104">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57ade8a38.mp4?token=ggbniKEcETG5oh3VID0P33hOfky1bk0kf6uuAQyHw5uBJtmWplmT0sr6ESycw1xYP3edCSOQwO95fl3cP8KqwVTopvxGKHPJV5q7lgqcVvWgfoar5uJYy-iK1KYexwbQQrbPJevzMVXISaXw3Lyk-meyHPReu5MnKfFmmw-uWGmc5BgQshssb7nd2nH7xctIwv5cwdIEXeAfwwRG8wlGl_OoeQ0v225YwVvb8xk4TP3wGJSTCIh3ek_y47HVBDz0tN2vzhcAPvhn3skUx9hTVBDnZE67pAYhoi-dBTW_Rbc_32eiBz9fwGICsmMn6znKAWYnPZP2cTMhOWQ4yn-sejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57ade8a38.mp4?token=ggbniKEcETG5oh3VID0P33hOfky1bk0kf6uuAQyHw5uBJtmWplmT0sr6ESycw1xYP3edCSOQwO95fl3cP8KqwVTopvxGKHPJV5q7lgqcVvWgfoar5uJYy-iK1KYexwbQQrbPJevzMVXISaXw3Lyk-meyHPReu5MnKfFmmw-uWGmc5BgQshssb7nd2nH7xctIwv5cwdIEXeAfwwRG8wlGl_OoeQ0v225YwVvb8xk4TP3wGJSTCIh3ek_y47HVBDz0tN2vzhcAPvhn3skUx9hTVBDnZE67pAYhoi-dBTW_Rbc_32eiBz9fwGICsmMn6znKAWYnPZP2cTMhOWQ4yn-sejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه‌خوانی از زبان‌حال جامانده‌های اربعین در حرم رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/454104" target="_blank">📅 23:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454103">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ef4c7f5.mp4?token=CclnpDTBFUwEc3GyXnc1YjneYfKoB7tNFa0JLACYupuey6pb0T4zxHHByMUjjGPW7FnCQP92oF7S6keE5sQehDvJakHHb6HNxRNcryXzNpZLXJc-X0aSbKUoeOH28EaRfpIOaksZ1TJsymPC-lheBFqU4Tb6blvCxaX1MWzxMNMV50VbyEHeFPPcoBfNnZP1vy1e2Rlx4g6ZZ8GWrbwCLwA7dPTRLRMHDUAm81MVzpiDf_MsI66HXSiEA3IyjqsXmzxhcYP38-RX9a628wIIVbfP3KfPmxFmez5ZARlleUkIkgxQdax8VVlql_ng09oSUwj8to4SO5nrATAmMbbA4Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ef4c7f5.mp4?token=CclnpDTBFUwEc3GyXnc1YjneYfKoB7tNFa0JLACYupuey6pb0T4zxHHByMUjjGPW7FnCQP92oF7S6keE5sQehDvJakHHb6HNxRNcryXzNpZLXJc-X0aSbKUoeOH28EaRfpIOaksZ1TJsymPC-lheBFqU4Tb6blvCxaX1MWzxMNMV50VbyEHeFPPcoBfNnZP1vy1e2Rlx4g6ZZ8GWrbwCLwA7dPTRLRMHDUAm81MVzpiDf_MsI66HXSiEA3IyjqsXmzxhcYP38-RX9a628wIIVbfP3KfPmxFmez5ZARlleUkIkgxQdax8VVlql_ng09oSUwj8to4SO5nrATAmMbbA4Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعارهای مردم شهرکرد در شب ۱۵۵ تجمعات ملی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/454103" target="_blank">📅 22:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454102">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d0a061f9.mp4?token=PFrCslrjCxWRRg9DyoOA-3YcA_WFbVHAx9g8Lxt6E2N4F50XN7sYHpULysrIA3WOjubjqOXhQtfu72TIZN0hk0dod-H4Z61KzRwMf7W3dakLqQzY8qfr5q-M2J13nkVN5pwgQwGMwFzGryIvVYpSFXWaD6fKQpcjyqDxn-IyKFxrEMwajjIMCZUaKes7fRonpgWzXYEoeOVIiAe1fMhe9cz3KYh3IwI0gBJ6afnCwXrQYSFHXlm6Wopt_v8sYTWbKI_0ZGIB-JC4CtGJimvvvypVNwjpnda2eI8GC3pqgICcCrG5xCoqcM-m-yy5bWVeWJMF7detMijhvJD4i3SSwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d0a061f9.mp4?token=PFrCslrjCxWRRg9DyoOA-3YcA_WFbVHAx9g8Lxt6E2N4F50XN7sYHpULysrIA3WOjubjqOXhQtfu72TIZN0hk0dod-H4Z61KzRwMf7W3dakLqQzY8qfr5q-M2J13nkVN5pwgQwGMwFzGryIvVYpSFXWaD6fKQpcjyqDxn-IyKFxrEMwajjIMCZUaKes7fRonpgWzXYEoeOVIiAe1fMhe9cz3KYh3IwI0gBJ6afnCwXrQYSFHXlm6Wopt_v8sYTWbKI_0ZGIB-JC4CtGJimvvvypVNwjpnda2eI8GC3pqgICcCrG5xCoqcM-m-yy5bWVeWJMF7detMijhvJD4i3SSwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش باران تابستانی در بشاگرد استان هرمزگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/454102" target="_blank">📅 22:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454101">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ورود ۱۱ تن کمک‌های بشردوستانه روسیه به کشور
🔹
فرماندار بندر آستارا:  محمولۀ ۱۱ تنی کمک‌های بشردوستانۀ روسیه  از مرز آستارا وارد کشور شد و به جمعیت هلال‌احمر تحویل داده شد.
🔹
اقلام تحویلی شامل داروهای ضروری، تجهیزات درمانی، بسته‌های امدادی و سایر ملزومات موردنیاز برای مدیریت بحران و ارائه خدمات امدادی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/454101" target="_blank">📅 22:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454100">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f524f49466.mp4?token=YqXj8ivq2eUyV-grp9a-P-hmnkM_g6jJTFr7wvE-rd2kIixJ1jZoaJuwoPBEC9Qm67Ri60Bo1_ljL62YWnu_Y2bzXtFTatx1pNJbg9icsL6pmYdjH8InVL1gTj1Wl24MeU4k44UMDsH4NsuQ_-jfyFr43YZrRjTsTQ7IHW3Dgmy9uhw4Nk-ia7gk-GrbWR2O9icyZ5qp0OIv8RFmHGCIHSOYFIZI_3w9Yp4iqxOVM4IrZIlXlIeiwsfwU-sRaMukVRsSeFZN7LcD_-9N3qLI66WkFRw_iX0vKciTkiiblJe06cswHozGRrGWZBGILLlV6USv1CyxzapQhH62JeX6CoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f524f49466.mp4?token=YqXj8ivq2eUyV-grp9a-P-hmnkM_g6jJTFr7wvE-rd2kIixJ1jZoaJuwoPBEC9Qm67Ri60Bo1_ljL62YWnu_Y2bzXtFTatx1pNJbg9icsL6pmYdjH8InVL1gTj1Wl24MeU4k44UMDsH4NsuQ_-jfyFr43YZrRjTsTQ7IHW3Dgmy9uhw4Nk-ia7gk-GrbWR2O9icyZ5qp0OIv8RFmHGCIHSOYFIZI_3w9Yp4iqxOVM4IrZIlXlIeiwsfwU-sRaMukVRsSeFZN7LcD_-9N3qLI66WkFRw_iX0vKciTkiiblJe06cswHozGRrGWZBGILLlV6USv1CyxzapQhH62JeX6CoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی اربعینی مهدی رسولی در وداع با پیکر ۳ شهید حملۀ آمریکایی در بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/454100" target="_blank">📅 22:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454099">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poqeLA9daLVozk_VWNn5jIzfaH1uEcTqNoSEGOAN5DBceo15xGgUVKMLnnQRiaoVDeGO2XWwoTp0gMQXbgGmuJKx72ZC_WGVl2FeRCuro7b62-9qwjopgfsc32k_4UQ8sf2RT37Q4vpkNT-UkAhApX_j6dni-nPTJJt08OQAc-ENsWGXjdQF3zfO_rhrXP0PxKlwEmGn6E_M8nLZfRloFicJQdq0nhiSPur605jSSQZmU_2xWd1YqwinVzFoDfY0HHrxm_9KOd_pKa2yuhHo7w2PsHO_8Mhp9CFe3U6xuUSrS7fR9E_VWA67voZT5kGVs9Nzj1-sdnhjvn7okltiug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: باید دشمن را وادار کنیم به تفاهم‎نامه پایبند بماند
🔹
تفاهم‌نامه‌ای که امضا شد حاصل خرد جمعی اعضای شعام بود و همه اعضا با آن همدل‌اند. باور دارم این تفاهم‌نامه مرکز ثقل روابط خارجی ما در آینده خواهد بود.
🔹
باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند. امنیت کشور، منطقه و هم‌پیمانان ما با این تفاهم‌نامه ارتقا می‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/454099" target="_blank">📅 22:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454098">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad9674ca9.mp4?token=vcHf2Wu7tlxm9N9kJnE6O67ABdfEKqAL3SgzACDamWBtAjdQL-neloC0gSbRPcF2WVd5_AEB0ALYX9UOD7mwHbyU2XhJC7GChvML1RAB0V3SuVxxFUv5p0pRASxP9gZC0JVHbW7ZGRaxwzW43bvcpGlz3Gje9Y2uAs4NlgZfdflYYND62ap75jPIkqxz3H_cY_D8HWiktYxrh9u0xjUuPPgfbwvZ_-u5EjQpZNy_D3WH-xf3zHgN1RonuvW9vlJItgIOSvTkP-STnS1KGHbx7btAZjFT5-0XtnH9JmNa28gKKLmQQoiz5C_SG4Hy9tbBOihX1OcWlwia0jz4VUTIupKENDO5p8QQnXBIEJt_liQNKiK195m01Wb_qEgxMe7a1Ef1AQGVQuvdhF1LIbeYCkiWM6edZx5Z1SsVA2sGER2eT9Yi8TOsG5KSUzKUW8SSLIHgBx_B5FE7lzIRxEQMp2-zN_H1-nrDS4lPVr7X21hiweL_HdLdGIKFM9xWpudm8gBH2hHY8QYQQsYVTmXRMQjSNFlAFhzJajC7wRh0lk9znE0W7SQoes-7-Why3IBXL21xRWqwb6CuJ0If1sHhlLRlbeBziciPk4U2ERYrTA7b0y_H6gR-cGTxmd8NL25o7XnLcN0EVpQFvis1N_p_QEmOD1e1hE1Hxzitsx0I9sc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad9674ca9.mp4?token=vcHf2Wu7tlxm9N9kJnE6O67ABdfEKqAL3SgzACDamWBtAjdQL-neloC0gSbRPcF2WVd5_AEB0ALYX9UOD7mwHbyU2XhJC7GChvML1RAB0V3SuVxxFUv5p0pRASxP9gZC0JVHbW7ZGRaxwzW43bvcpGlz3Gje9Y2uAs4NlgZfdflYYND62ap75jPIkqxz3H_cY_D8HWiktYxrh9u0xjUuPPgfbwvZ_-u5EjQpZNy_D3WH-xf3zHgN1RonuvW9vlJItgIOSvTkP-STnS1KGHbx7btAZjFT5-0XtnH9JmNa28gKKLmQQoiz5C_SG4Hy9tbBOihX1OcWlwia0jz4VUTIupKENDO5p8QQnXBIEJt_liQNKiK195m01Wb_qEgxMe7a1Ef1AQGVQuvdhF1LIbeYCkiWM6edZx5Z1SsVA2sGER2eT9Yi8TOsG5KSUzKUW8SSLIHgBx_B5FE7lzIRxEQMp2-zN_H1-nrDS4lPVr7X21hiweL_HdLdGIKFM9xWpudm8gBH2hHY8QYQQsYVTmXRMQjSNFlAFhzJajC7wRh0lk9znE0W7SQoes-7-Why3IBXL21xRWqwb6CuJ0If1sHhlLRlbeBziciPk4U2ERYrTA7b0y_H6gR-cGTxmd8NL25o7XnLcN0EVpQFvis1N_p_QEmOD1e1hE1Hxzitsx0I9sc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرکت دسته‌های عزاداری در بین‌الحرمین، ۲ شب مانده به اربعین
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454098" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454097">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5decb8892.mp4?token=NbXXojehDfcTA95p-GIGcZ7mUBGOjQfV-ocsqycqVfuPBZTYo2C-Tlhus2aqPRdZVHaD6b1qktuZhBKebPM0l0PNBcdBnut-yvqyLFSajfWf67JTnRwUTuCX3j56Tp7myk1MOuNIsd3EQOUATuKM5aAl26Me4LwqocMPHRMci6QCAdudSjlrnd-33VO4wl4fGHARce5R_aBeWD5HMj2end1AtdghIgFFxQlgTGSmUwW3aKPCUMXuOX1okfFtbQdmKP2V6wJ1_AT3QcD3VTSnlubShfK5qFMMRInIEXueAKZQERMh0gCqxk46hzUbPxVki6Y0qfSK-Ai33CrO1MWKAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5decb8892.mp4?token=NbXXojehDfcTA95p-GIGcZ7mUBGOjQfV-ocsqycqVfuPBZTYo2C-Tlhus2aqPRdZVHaD6b1qktuZhBKebPM0l0PNBcdBnut-yvqyLFSajfWf67JTnRwUTuCX3j56Tp7myk1MOuNIsd3EQOUATuKM5aAl26Me4LwqocMPHRMci6QCAdudSjlrnd-33VO4wl4fGHARce5R_aBeWD5HMj2end1AtdghIgFFxQlgTGSmUwW3aKPCUMXuOX1okfFtbQdmKP2V6wJ1_AT3QcD3VTSnlubShfK5qFMMRInIEXueAKZQERMh0gCqxk46hzUbPxVki6Y0qfSK-Ai33CrO1MWKAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ستاد مرکزی اربعین: به علت ازدحام از زائرین می‌خواهیم همراهی و حوصلۀ بیشتری با مسئولین و خادمین داشته باشند
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454097" target="_blank">📅 21:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454096">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6bd968655.mp4?token=uy6jRyD08eGshoP2bDUf2XsXjgvEQPf0i28bCG4tznSauHSJt7XAFDxk7EjDU9fVu2dH0P-kXpVf2CykZUWR_FlWpU0Z6pT-jBKqXfw4zz6RDw7w8sp_j_AfQEhkkynDrBWYr4FfX553BgQF3nRn9YPRFgdnhvweSGsiTG_LYDiq8-Yhl79WgtZzOM-wbtRJ_XRNT9JdXw55Fs3TCnxU_JAi1H6PwOd6TAT0VduwTF3G3ZlULAMvvkuhRO2TEmFSM5NE9LwJgE2tXzdl5y-TySwNea0K6U53gTgJLf4OMs-8dOSbh_2Ojrm_r2QHE7HXTlDoWCs8Irw8lXxnOeF5LBkOecdv7URrjveFEPAjodlSajJbzrTloPipcX3CADg6UaDab-zVoO1bU6_xM3d1T-oaGvfdG8wHMt91-5RPD1QEh_xV3fM7krTbHktPzqnLmhpxLohPI1QxD3G0tmYOFw--e3gEHnXPZsdNV48VXNmx7C4DMYc8-50fSImS19x7uuMGKniFOniUqBIRfzZkdF5I4dYPH0TA6gqg40iDKF4cUNNMndmu95ggAYXU_oh2SUDocK1bSeezN7Qhtb2ovGec0NYGEjJPMpz72oDH9ZidChCrprHhAXu5-Icm9qdsNcQO20JLK77R7i-M74NjBxAhbFd8f7H_9I2YtB_ICYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6bd968655.mp4?token=uy6jRyD08eGshoP2bDUf2XsXjgvEQPf0i28bCG4tznSauHSJt7XAFDxk7EjDU9fVu2dH0P-kXpVf2CykZUWR_FlWpU0Z6pT-jBKqXfw4zz6RDw7w8sp_j_AfQEhkkynDrBWYr4FfX553BgQF3nRn9YPRFgdnhvweSGsiTG_LYDiq8-Yhl79WgtZzOM-wbtRJ_XRNT9JdXw55Fs3TCnxU_JAi1H6PwOd6TAT0VduwTF3G3ZlULAMvvkuhRO2TEmFSM5NE9LwJgE2tXzdl5y-TySwNea0K6U53gTgJLf4OMs-8dOSbh_2Ojrm_r2QHE7HXTlDoWCs8Irw8lXxnOeF5LBkOecdv7URrjveFEPAjodlSajJbzrTloPipcX3CADg6UaDab-zVoO1bU6_xM3d1T-oaGvfdG8wHMt91-5RPD1QEh_xV3fM7krTbHktPzqnLmhpxLohPI1QxD3G0tmYOFw--e3gEHnXPZsdNV48VXNmx7C4DMYc8-50fSImS19x7uuMGKniFOniUqBIRfzZkdF5I4dYPH0TA6gqg40iDKF4cUNNMndmu95ggAYXU_oh2SUDocK1bSeezN7Qhtb2ovGec0NYGEjJPMpz72oDH9ZidChCrprHhAXu5-Icm9qdsNcQO20JLK77R7i-M74NjBxAhbFd8f7H_9I2YtB_ICYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر ۳ شهید حملۀ آمریکا به قشم در بندرعباس
🔸
در حملۀ بامداد ۸ مرداد دشمن آمریکایی به منزل مسکونی در محلۀ چاهتنگو شهر قشم، پدر و مادر خانواده و یک کودک ۲ ساله به شهادت رسیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/454096" target="_blank">📅 21:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454089">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JtUkQda3-xryFpEK9eQPulfT59zwVasX70XSXzPxVhHEyfSRSqJiIv9T-MOpM7Op2J1hQoE566mrw1oh7MJZYwQg4H8EhDu3rTrEoATPg1sfqtXvwgkRFqbCsV9iiQZUNYEdk1gs34EI1R14wVWZq8PmTPIXO5cp96YMRfUaEJ4LpMu5fVJ-0YHetSRw3LIrrtS0XQVRY5hSlUcSbUe1KDgfZJQKtpUh_rMjxSz6dxEfTlzWHBRXQmeOdR3oZncz3TNzDH9SLCr0ns57pPO-ADGNa7WnLYNjw9cRaYZXipCBdYXoPXL6H23D29bl_QXdC6haZt63xt7v14vIxlUXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSeMoLtmqlOGjWITP3IeRo3M5ofcb8ZBZbXZuKdr30vazvqC0lri-5ikEMKJIc-SQQGAuvmLy4xrVDbfODOqufUx7z9KfL0QOgcNo785mgY2_gFAfryME3H4I2V8Dq0g3pfn417mVNcvhfVhr5Jpv8sj1Ft0kZv47jl_RSTXpYisSi-SLxNw1jNqyh50SowWu2sTpgF-D2QLfbZhjd1t3rWVpwebqAqsZo8yGVuzh8JTkX-xkVMBaWApWfCdbU3GnNsFUhHkX0D7TMKM_gfLkr0fIHuceDPMC-PJcQGwDWQsDMX_oWlpXPAxlZ19gBLM7y0_mdE0LaLuTrrpJZBsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sg4qyWjHhNrUPcnDrbACxOFTQgZH281VJVk2Mj7fagsmYhye59LFZsXBZnR8Jp5ImBrWQea7C_ZQXUTHqFE_rj9C-g9ETNSGUaPtgBbX2lXphel4i8Nz9j9LDdWJWI8FxthoWjY4aPZG3ZCg-vFzSMIMo8lQo2Xswv9lS9P6SKiDE1PUMnji990pA93OwX6pz3Jd8S0N_1LXsRShsDMWSVG8K3GtFUg4efpMWOBbYL6AQMq1zoql8fYRjgsofNqkXo2ikcZ8V8QOK-cySWC9XPwA-b9avGvvW0HB0hD_i1ZEG_kCRP7_spTBprhNxuAnr3Kx0fnEjMhwEMDSf6bZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMozjlBUfoBU9G9ViYeYAvh57dZThndydd94qxK6waaoLxyNKc3joLezN0keaNWin8EWNwyDtKeyLPMAtJZyVW7rAGrQNvvdb9GUmjbNADno31IqDXDZiKf8kUM-0IoSGxVrTrsB6o4xSlsoxmxGiTjlYM6mv0xPmQ1XgEpIEdG6vLccc7Ny58YliZI6fkeQlB81I_1SoYlV6AGMHTudCX54uZJDXLSaxaNLTGUNOuO1oLJ7YYzaN2PwzBsVmLxSH4xjKkEZgCHQf1G8iFr-bTWwu_ak6UQdjPg86ER3N7M8JYMNNhIws-xxcDDYZshd6uQvYNxTPh1YmGjvHTX0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LN9bzTxa3RUHoX56AyHAPmsetUIcVPtVZhinI-TYRIF62lsFUR5gLRBpDc2su8QiO73BAkcVdIflmCMgoZE2DhZZnJWvBkNzE-S5RpIgy_BOR47MaYw4o57qmZ3ajJTBXb_SPaeNb_zNlSw75K4xF5bj2-l49pYueeskEjZaJ0Qfz_OES6NZjgMKf-jntTdTT1xIWYQjht7fwpokXAVimz04PKDBEamKbOknXidhjYVLRuGlazu1Igw9EVJf6iEav_ZhyCu1yNQCHsbvERLeBNnoqcwqk7yRj__EeATP76jE4IRGyiSuZtj_fsGUkmaARph-e7EQpIRcSdoeBjvFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-VB99b4cirvJ8barY8nJ0G6IxYiylNjzlZhg5bCv9zkHdVAu__Zl5B2GKgbQAUUmsiKNG2Bs4NnsCSxzieLtwm-A8JgrStuQ4smnDa8bilW7_AwqQS2DgfuKyy4ZzVyC9kMF27BVX8imevB19ZguWXGQiO_zHDkWHnsNBmsSao-weVWZOupOaKhnh5J8574WotUAR4zGhcw7XQ36opR3KhDzGlBWk6ECUAM5lSIFpP6XZNiozhc51bnly1kfgrZ9OD_vaf1TJ7eoCbnV9MxPAia6klO3DlnQh0DYBzgVUu9QemEZspLrujmS0IKaasrsqEafJnZIz20BNPmRyLYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQIMOCHy2q7UdCkV8tMPggPWCyw2BpXtAHA88CFfDPCXz69vCjIStHSKaBqAet4UpIybboZh1-LUg80WEZPmYHuUY5jNmO6AFZPqHqgIIXVTJAZtgNn5xIoTfnB7bQg7v3q_3TSvcHMZACEL7MknTg6FAo6t0I7rizdJz9kqpbv4DrBTvLlEO9XFh3f9bYXMPumI5T98B4yNXQI4uIZ0HsCJlzOUOnODHeGbKKDVP7sG7Qpp8D41Nyua9jfg1RKC0jPzNQEnS1nbUWnxwPiFdI7jir6APpHEFGeJFMkfcQEd1tdJDt6WGIgZAo_opkcifjax6quqbQd5FHo8JU2uEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خدمت به زائران در مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454089" target="_blank">📅 21:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454088">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuR9Fn2W8c7pJ8d6wQu4mz_r9mr7MYn8fFG7kzBJ6ZzgY-jLt8IklM4Jayb2-uuPTeyA5DqblKixEiv01BxcI-FC4JjNTTDuMFQukHtSBxyYiIKUiYzz-U_2X6awwgZBb-TQ5oEQtGRbdo1WXCsqcnfqtqR4Rlc2BVbjbQSR-vLiOhVFZTXwPFX8L3OdSa8tuYXbCObMbLu90EjfLytDEt3DmYrMpYRHWlByhYd6sgZqa1pPLZcxkUu4uPFYI2ZQ1I0gq0Ca2s_25rPu6zn57xxPAKvFRPAuB8cQNNpnUFDUpvp7hsPRYdBxgmlNVPN-cdKojSA7zNsd_0w-veX5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
پشتیبانی مداوم و گره‌گشا از پروژه‌های شهری با «مسیر جدید تأمین کالا»/ شهرداری تهران چقدر مصالح از بورس کالا، خریده است؟/ افتتاح پیاپی پروژه‌ها، با وجود شرایط جنگی
محمدعلی‌نژاد معاون شهردار تهران:
🔺
برای نخستین بار، در دوره ششم مدیریت شهری، مصالح پروژه‌های شهری از بورس کالا خریداری شد و این شیوه تأمین مصالح، ادامه دارد.
🔺
شهرداری تهران تاکنون، ۳۱۵۰۰ میلیارد تومان انواع مصالح پرکاربرد پروژه‌های شهری را از بورس کالا خریداری و تأمین کرده است.
🔺
با وجود شرایط جنگی، در ۴ ماهه ابتدایی سال جاری، ۱۰ هزار میلیارد تومان انواع میلگرد، ورق، سیمان و قیر از بورس خریداری و برای پروژه‌های اولویت‌دار تأمین شد.
🔺
خرید از بورس، ضمن افزایش شفافیت و سرعت تأمین کالا، کشف قیمت منصفانه و کاهش ریسک معاملات را در پی دارد.
🔺
افتتاح پروژه‌های شهری، طی ماه‌های گذشته و در شرایط جنگی، افتخار مدیریت شهری است و به زودی، پروژه‌های متعدد و بزرگ مقیاس دیگری نیز به بهره‌برداری خواهد رسید.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454088" target="_blank">📅 21:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454087">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD_6N8cL5LAmhI-4RoKEoqJToBRJiRP3yFvxNlfv8tMIyw-WtGhRKCngYke4VqThyc0JpewE0FbSJQTyCW4dpmStB_SmD41n7xChjxsMG9jWyjHA4_ovgq4FD5VDb7Ru3c8dnMQC9zFIHUst3rM64v1Fv3OhYeZQ5wkXt59Hcuxsb1H70Co1TJkeLO3g36mFu50PY6SQHku9F8y9NiQO2289qxmCKgZFYR1Cl6q30RLfWmgu9n25iur0kJolTzvOZELc_LwJTZuDpmaykFWa3AGdvpDa9iGncYck8xSStNk42UK5dpc8FKPh1txFxWaBPc2UJntRmO7d1SxwCc7zmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
در چهار ماه نخست سال جاری
بانک کشاورزی ۱۰ هزار میلیارد ریال تسهیلات برای توسعه تولید بذر گواهی‌شده پرداخت کرد
🔻
بانک کشاورزی از ابتدای سال ۱۴۰۵ تا پایان تیرماه با هدف تقویت زنجیره تأمین نهاده‌های اساسی کشاورزی و ارتقای کیفیت تولید محصولات زراعی در مجموع ۱۰۴۱۲ میلیارد ریال تسهیلات در اختیار فعالان حوزه تولید بذر گواهی‌شده قرار داد؛ رقمی که نسبت به مدت مشابه سال گذشته ۲۴ درصد افزایش یافته است.
🔻
استفاده از این بذور به‌عنوان یک سرمایه ژنتیکی، تأثیری تعیین‌کننده در بهبود عملکرد مزارع دارد. مقاومت بالا در برابر تنش‌های محیطی (مانند کم‌آبی و سرما)، مقابله با آفات و بیماری‌ها، ارتقای کیفیت و ارزش غذایی محصول، سهولت در برداشت مکانیزه و افزایش بازارپسندی، از مهم‌ترین دستاوردهای استفاده از نهاده‌های استاندارد است که در نهایت منجر به بهبود معیشت کشاورزان و ارتقای بهره‌وری ملی می‌شود.
🔗
مشروح‌خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454087" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454086">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454086" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454085">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یک شهید در حملۀ تروریستی به یکی از مقرهای ارتش در مریوان
🔹
تیپ ۳۲۸ مریوان: در ساعت ۳ بامداد امروز، عوامل گروهک تروریستی پژاک با استفاده از ۲ فروند ریزپرنده انتحاری و شلیک راکت آرپی‌جی به یکی از مقرهای این تیپ در مرز حمله کردند.
🔹
در جریان این اقدام تروریستی، یک سرباز به نام ابوالفضل گودرزی به درجه رفیع شهادت نائل آمد و یک نیروی دیگر نیز مجروح شد که بلافاصله جهت مداوا به مراکز درمانی منتقل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454085" target="_blank">📅 21:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454084">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4KqdFWVHqB5eIMq0DFQiKJDh5JV6flVOdIkFdwIQD8iBBx-kwUzfPgMSLlxdadFI3GcZG1NnL262d3-hvl6_vC3gCq9p7gVBYzFY8fsZUHz7KDxrroPhG10TCCbV0ZRATPoI-HOLZEBpBz9TMciXz8KumigMJyrJy5EUeJ0Cs150SXZap1q3EJ9tRHXaJxwADYH3Bf_6m-0_AWeMB5PPFfANssoea2N-2V2igvPlT52Fwp9X7VbZtsNZR1BfodUbkfD6SG2W2CNgbc6jttuCSM1zkTnCCUnR4ZAi1av56YkW-5780Qtl0WZMVjL7kSxXe2X_R8lnzVP2lEUyiuUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت‌ژورنال: کشورهای عربی از راهکار نداشتن ترامپ مقابل ایران ناامید شده‌اند
🔹
نشریۀ آمریکایی وال‌استریت‌ژورنال: «کشورهای حاشیه خلیج فارس در گفت‌وگوهای پشت صحنه از فقدان یک استراتژی شفاف ازسوی دولت ترامپ مقابل ایران ابراز ناامیدی کرده‌اند.
🔹
کشورهای عربی خواستار تضمین‌های مداوم ترامپ مبنی بر حمایت نظامی آمریکا در صورت طولانی‌شدن این درگیری‌های متقابل شده‌اند».
🔹
روزنامه وال‌استریت‌ژورنال چند روز پیش از این گزارش داده بود که جنگ با ایران موجب شده ایالات‌متحده کاهش حضور در کویت را مورد بررسی قرار دهد؛ این درحالی‌ست که مقام‌های کویتی اعلام کرده‌اند که همچنان نیازمند حمایت آمریکا هستند.
🔹
این نشریه همچینین نوشته مقام‌های کویت مانند دیگر کشورهای خلیج فارس از این‌ که ترامپ جنگی را بدون مشورت آن‌ها آغاز کرد که آن‌ها را در تیررس قرار داد، ناراحت و آشفته هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454084" target="_blank">📅 20:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454083">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HboBCXRErDSjKht6ofL93fr5VPcckY137hwzKAExzWHimrImvrXIa3FWD3SWLepIj8uarPxokeGNLH1bKxIywDzIj4T8Rzi04UuSijatk3u4J3gfoE8ADzoc2NVk1IG6gs1o0N2aXo7yHlVEFBqeSA7ph6eqeSbZRFzqBEZ0AWoQzS0NLbcIirnr0no0w-h8f8DX9gATNH8KtxGNSl2IBECcvUo633RP8ZtLqNB2ejFc8paXBLE0Wxc15T0Cay-lMMGZ3-vt0EhV-kSNq-q8LZYoOTf8FeA4-jPziJ9CwNmhx9HVkDhuJuw9XNPcRg9ZwT4qRe6NmE-WsnnYm1floQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
برافراشته‌شدن پرچم ایران در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454083" target="_blank">📅 20:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454082">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: هر کشوری با آمریکا در حمله به ایران همکاری یا همدستی کند با دفاع مشروع ایران مواجه خواهد شد
🔹
در اختیار قراردادن پایگاه یا امکانات نظامی و لجستیک در اختیار طرف متجاوز، آن کشور را در ردیف متجاوزان قرار خواهد داد. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454082" target="_blank">📅 20:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454081">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: همۀ دوستان و همسایگان باید بدانند که تبعات هرگونه حملۀ آمریکا به زیرساخت‌های ایران، دامن همه را خواهد گرفت. @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454081" target="_blank">📅 20:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454080">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKgaRQbHR3tY2AEEtb9bZ5ij4WJu8AnjUD3nvgBMA7BAjpOKExJQn583_3AtUy6Vx4HX39Gua5Ay9kn7dfw2nWJWkNGvgPLR7dN1grrcRuaYaC0F8FBuAScfU4Qe2ISnJbD8FRVjZBBgEhkmRXnK0m7yd1QRu2X5NRN_hdNJhhLqS7waBI5q2HQtKsZkUkcWTWI1p5a2QAd8lJqQq5FPAEnfNlFUNEeCcAdnK_YA9tAc7lZOdY-3yJ2GLT4Hccfo1E0z0tPywrzJWLq-13yr0jysh1x7nkfmoTvejikNlVEzY3dPvpyE-vvTCaqSrJ5uVSG5i02oCA3f_eUqc9NSzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: مذاکرات میان ایران و عمان در مسیر نهایی شدن قرار دارد و مراحل پایانی خود را طی می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454080" target="_blank">📅 20:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454079">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: مکالمات آقای عراقچی با مسئولان پاکستان و ترکیه هشدار و تهدید آمریکایی‌ها به پاسخ متقابل درصورت اقدام علیه ایران بوده است. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454079" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454078">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عراقچی: برای پاسخ به هر ماجراجویی آمریکا آماده‌ایم
🔹
وزیر خارجه در تماس تلفنی با فرمانده ارتش پاکستان و وزیر خارجۀ ترکیه: نسبت به هرگونه اقدام ماجراجویانه از سوی ارتش آمریکا هشدار می‌دهیم.
🔹
جمهوری اسلامی ایران برای صیانت از حاکمیت ملی، تمامیت ارضی و امنیت…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454078" target="_blank">📅 20:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454076">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: ایران به‌خاطر تهدیدها و فشارهای رسانه‌ای از مواضعش کوتاه نخواهد آمد. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454076" target="_blank">📅 20:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454075">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: وضعیت تنگۀ هرمز به‌هیچ‌عنوان به وضعیت پیش‌از جنگ باز نخواهد گشت. @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454075" target="_blank">📅 20:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454074">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌‌
🔴
سخنگوی وزارت خارجه: گفت‌گوهای ایران و عمان دوجانبه است و به طرف دیگری مربوط نمی‌شود
🔹
موضوع گفت‌و‌گوی ایران و عمان برای رسیدن به سازوکاری که منافع ما را تامین کند چیز جدیدی نیست و از مدت‌هاست آغاز شده. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454074" target="_blank">📅 20:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454073">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: جمهوری اسلامی ایران براساس منافع و مصالح کشور عمل می‌کند و تحت‌تاثیر تهدید و ارعاب دیگران تصمیم خود را تغییر نمی‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454073" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454072">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: جمهوری اسلامی ایران براساس منافع و مصالح کشور عمل می‌کند و تحت‌تاثیر تهدید و ارعاب دیگران تصمیم خود را تغییر نمی‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454072" target="_blank">📅 20:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454071">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9tCGzlCdxeBDFHDWtV7UCEAxCzKN8aA-cah3r7sPGl21Y0b53QgV4welOeUGA6w2gVtaXGJ0CVlS8QxPi9u2HinoSOfJWWHFKCn8hviFnFxxco2D1KD3eOkSg-FZjQS6s7xYvNVm4WtFKiJaRK3AED9vV13cOs9Rtl9StLWoptrQ_JN7FjHAl9fbagA1p9IMgR6gEbVa142U-txv6vlb5C9iWrSLAXr-BG9uQa0trnIJNxOl5lYcwVolRNk9g6gFicrG0eXNtbGfalk8qvtDONG5KDn4bLcXdwD6fv_frpopF_doZRe6ZG33xPZdV5ENFvcHSyLHhmQGIT5w4qZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
موج بازگشت زائران حسینی از کربلای معلی در مرز مهران   @Farsna - Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454071" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454070">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAxjmDXxXTp_okIKIl5jJkq7wLgEMy6TcmDVzQQ1X8lTo9FZNzgljjmxEgKFDj6opfyeEf5yIxK4K6HCqXarGItD2K1_p8k1otUtMoVl9hXhveP-d4Cwq2vhLdYmArCHphsT5jQvYycXMtNzLOE7LQf5s5dbKI1Kv0EtQppMfpqM6jSREbZWOh1-tGzCERYnFo5DmnH5Nw76cnEpC-nrWbk-3AE2jHubF8MmxxiF2AkOfJpHg7zu5B9vHWIOeBramSQ-VrAtvTcLy6dCnL3Vthy47e6RaY0PfHTCURGa9Z9vPlkr9s6Qhy6EaNQ8icaInK3I89aQs3zFUVUyHYzkYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام قدردانی رهبر معظم انقلاب به خادمان اربعین در مرز شلمچه عراق ابلاغ شد
🔹
نماینده ولی‌فقیه در خوزستان با حضور در مرز شلمچه عراق و دیدار با موکب‌داران و مسئولان عراقی پیام قدردانی و تشکر رهبر معظم انقلاب اسلامی از مردم، خادمان و موکب‌داران عراق به‌پاس میزبانی کریمانه و خدمت خالصانه به زائران اربعین حسینی را ابلاغ و لوح تقدیر به آنان اهدا کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454070" target="_blank">📅 19:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454069">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93a7858fce.mp4?token=KmYqOXE9URRiVI-ZNt_VVSQI0hdsMchyepvOXZvHnCjaNw2Hw7SHGjh3bzGhzITEmf2E0crHhrfTZ_-1M7JDzTReD9VhGH_i4kEsaPdUYNmJBKp0Dk_-tZYaQETr__m3O3xsHU1wQUrIBLMOUqIfDfeKkiSuNHBVkVVyiQZ-YyoZ-GcOcsfIQsceh0H5eOmptk3zNhmYStW1kHI2tFRUnM8GSWIJel_GG1YzC7T8N1R3FzukszfRdBVZTFVyLB7OyyQE6wp4YSM6XIf83uw5R6PyD3lQ9w4RyGB9J-3y4df-SjbmE5Cdx_xxcKjPmg5XZRVIa3qdbz21ay6jt1su4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93a7858fce.mp4?token=KmYqOXE9URRiVI-ZNt_VVSQI0hdsMchyepvOXZvHnCjaNw2Hw7SHGjh3bzGhzITEmf2E0crHhrfTZ_-1M7JDzTReD9VhGH_i4kEsaPdUYNmJBKp0Dk_-tZYaQETr__m3O3xsHU1wQUrIBLMOUqIfDfeKkiSuNHBVkVVyiQZ-YyoZ-GcOcsfIQsceh0H5eOmptk3zNhmYStW1kHI2tFRUnM8GSWIJel_GG1YzC7T8N1R3FzukszfRdBVZTFVyLB7OyyQE6wp4YSM6XIf83uw5R6PyD3lQ9w4RyGB9J-3y4df-SjbmE5Cdx_xxcKjPmg5XZRVIa3qdbz21ay6jt1su4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار مرگبار در پاکستان
🔹
رسانه‌ها از وقوع انفجاری در شهر کَبَل در شمال‌غرب پاکستان خبر می‌دهند. در این حادثه دست‌کم ۷ نفر کشته و ۱۵ نفر زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454069" target="_blank">📅 19:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454068">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJb1mwi8RR8UQ296fnqinQgbS9Wm-4_DbGEQ3kKyg9qBho8J2SpHCRIZ7RxqNeSAranjXZhPSrcPFX8ras3RB_xwr8arPSVOV5o4yY80Jhss1_AsixxRC0uR57ugesXr9El1_OOsHSbh71UxYvWXtrgXY0oxl-FWTf_lXi6D7xnfS57eU5ukBuducf506zOpgmb7aKDea3Jj6cJZyjQkMwLcSR4P-J0B54sKO4rlJVd2d3Do0w_-ZLDcEoKHIDV-Tg3FVETNkWyPciJczJYSt-NSmvWkS6fYb7AGw3w5PjByzF8Fmpup96nQ2Nl7rBD76UY8Ln6QtlMeQ2Rh_0ylAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیموچی در اصفهان ماندنی شد
🔹
✔️
مهدی لیموچی، وینگر سپاهان قرارداد خود را با این باشگاه یک فصل دیگر تمدید کرد.
@Sportfars</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454068" target="_blank">📅 19:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454067">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecda317b69.mp4?token=cMrVP9uv274ZILIRDLHbK7Q_zz9jdjvoBm6yDKss8GBMo8JzlgnGHaitER5vR79PhD_sTaQcaDDUGKWdFWQq4eU3KjfMmNh3E7IqlnVd5GMsepYZN9sglMAGK5gXRbxcUYxm8YRF5wco5YEmrhdcE7moBqFf8bX3Zpy9M2kZqyrOq-DsA-oeYEzyY06p-fShTK24F-WR1GZOmbXO_TECaVKvImeObs4wMFzdEY_zNx9diHxc5fudHCN31BjaSEBiMPEznq-N10U4iGG5QfTEpVUjVHTB65oDuKPiMndTJYcpzIemYUOoxv7SFGaf7B7yFXk40qgZ9CL5hBtMWUPfVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecda317b69.mp4?token=cMrVP9uv274ZILIRDLHbK7Q_zz9jdjvoBm6yDKss8GBMo8JzlgnGHaitER5vR79PhD_sTaQcaDDUGKWdFWQq4eU3KjfMmNh3E7IqlnVd5GMsepYZN9sglMAGK5gXRbxcUYxm8YRF5wco5YEmrhdcE7moBqFf8bX3Zpy9M2kZqyrOq-DsA-oeYEzyY06p-fShTK24F-WR1GZOmbXO_TECaVKvImeObs4wMFzdEY_zNx9diHxc5fudHCN31BjaSEBiMPEznq-N10U4iGG5QfTEpVUjVHTB65oDuKPiMndTJYcpzIemYUOoxv7SFGaf7B7yFXk40qgZ9CL5hBtMWUPfVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌پردۀ هجوم مهاجران به اسپانیا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454067" target="_blank">📅 19:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454066">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d965dc091c.mp4?token=MfPITI3dZPFnxO-tVmISSOGzLJILCrxlkdi8rcd5xEfhsSBzsaC1CryrowkIjPhy7o7cj4pL1IhNjMxTY6gEDIgVk7CvuPeG-HbDKa2m7MeeLqWFxc_Vg1PlL7-2PEHV4jy3T5SxV5FyM09yrA0igK0yETZHx2Q7vw78QgpmtBr9zRJVnmaLmg6iI3buAjT_caJNp766s-6TamRfhit-LCkWSnbFrL2u4udAsAwRHhzuum5Q0V0nnKbHR-BMGFJHFphQAslI_DfqyjIFEX_ndenddvF4bkybmVBmt60tkqXAe3NrlbFLOitLPaUAIC7YLJb699BrVSBXALwmOsmrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d965dc091c.mp4?token=MfPITI3dZPFnxO-tVmISSOGzLJILCrxlkdi8rcd5xEfhsSBzsaC1CryrowkIjPhy7o7cj4pL1IhNjMxTY6gEDIgVk7CvuPeG-HbDKa2m7MeeLqWFxc_Vg1PlL7-2PEHV4jy3T5SxV5FyM09yrA0igK0yETZHx2Q7vw78QgpmtBr9zRJVnmaLmg6iI3buAjT_caJNp766s-6TamRfhit-LCkWSnbFrL2u4udAsAwRHhzuum5Q0V0nnKbHR-BMGFJHFphQAslI_DfqyjIFEX_ndenddvF4bkybmVBmt60tkqXAe3NrlbFLOitLPaUAIC7YLJb699BrVSBXALwmOsmrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: با وجود افزایش حجم سفر زائران اربعین، فوتی‌های تصادفات نسبت به مدت مشابه سال گذشته ۴۰ درصد کاهش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454066" target="_blank">📅 18:51 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
