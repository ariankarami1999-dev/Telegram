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
<img src="https://cdn4.telesco.pe/file/TsJG-tXh4zslwA5kyaFRz6zZUfRB7uw_QZrhmkocBYuy7lty-Whvl21f3Wm5nTKdK3B03bMoT-aQU5C2zZrDl0OLvOCze6zp9xWXZ2-yTyoZZPAqB8oxa5keTSnxp-cPkKdICVK4t3FDstZzRgY4v-nxLv05N5fGyjx8yjbHM2ltJenkxVQDtsjYRm86INPNv8FUDgccCJmj-UxAjifGQtYxx4s9bKQB3K6zj3empbw2KpXTyaJqfK55rcXmXaflWHMO9DIcE_1-xmjeUc8cxvbR5JonH8r7vLV2XaOgmrYLeymiN9i-niPFcu5ioDIP0Mu7hJVLm9yIBaAZgSeYzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 15:53:56</div>
<hr>

<div class="tg-post" id="msg-661423">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKpFPDxjI1McbSb8rRWXp-sMD3rKCf1_qfAMH9AzR6NcHjXOYh8Zd85pxMZu6sKInwDulNyUhc9mjhA85gVTdeORZgJWcls33enVNXDye62UaRrFA88eVEfXvdUA48KtL9Mp0HRHrNhHuRpqbndH9IahjXw_TYLhbhtVVfhJQXd6j8dXSzLSXE61m2wijDjLM61i4BxuMp03yeTZFzkF3yYgD3Q-gwcQ_0A-DzX7wrltyWnafoUvAMBhYMHq2DWMPqg60P2QKU4lpfo606ExsvejB9MsrgULhvi25gQSkEumxwZhC8eLj3ILbW58tJd0b-kN5wT0NFgQMPX0eV4j9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
«سِروال»، سوپر مدل دنیای حیوانات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/661423" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661422">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
یارانه خردادماه ۱۴۰۵ به حساب سرپرستان خانوار دهک‌های چهارم تا نهم واریز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/661422" target="_blank">📅 15:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661421">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/972310ae87.mp4?token=Cm443kqXA9kOJZkzfwiYFYjVE86xlkkaChLXVDxz12u-X4z_XXaNInq7KUSfJNfMQ11F5vOBh-7WZ0wqML9SoqdIVXBEJGDTZCWOQcFoSZEpxTuFs-6gwzVuDnUYyAjykkSVNjuQcbeCOVEr6o6F0B0ml_SNbPO4j6-wSdjofP_n8Xj36PgeXJMXzNNY8RDQEOVRoRqaGQh9JhXBTjhnKRBt4uqSfHk-xRHd0GlZRRFd7E_fCu35QaamDtRVFV3CbjW3GAnrxmzFz6TF5isdmzZ-BRHnjmiQN_oRB3pxPmLsYoNIE9fIV9N16xwl1HeWRnNdmILckzcFA71seGvUkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/972310ae87.mp4?token=Cm443kqXA9kOJZkzfwiYFYjVE86xlkkaChLXVDxz12u-X4z_XXaNInq7KUSfJNfMQ11F5vOBh-7WZ0wqML9SoqdIVXBEJGDTZCWOQcFoSZEpxTuFs-6gwzVuDnUYyAjykkSVNjuQcbeCOVEr6o6F0B0ml_SNbPO4j6-wSdjofP_n8Xj36PgeXJMXzNNY8RDQEOVRoRqaGQh9JhXBTjhnKRBt4uqSfHk-xRHd0GlZRRFd7E_fCu35QaamDtRVFV3CbjW3GAnrxmzFz6TF5isdmzZ-BRHnjmiQN_oRB3pxPmLsYoNIE9fIV9N16xwl1HeWRnNdmILckzcFA71seGvUkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونزوئلایی‌ها تصاویر ترامپ و روبیو را به نشانه اعتراض سوزاندند
🔹
تصاویر سیاستمداران آمریکایی که بیشترین ارتباط را با تجاوز آمریکا به ونزوئلا دارند، توسط معترضان مخالف موضع واشنگتن نسبت به این کشور در خیابان‌های کاراکاس لگدمال و به آتش کشیده شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/661421" target="_blank">📅 15:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661420">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/254877efcb.mp4?token=MfBeQGJA8DfdHqSM8ZVgFHTuJW3IpJOcOQlvzH8tohfFfkpJA00fhVTwuuIb6apjXfO7HlKZ1UC_XslJqnGi3Nj82_UBV2ncf1hJzrRK3iQqHt4AN7tJnVzFkalA5y-TIAtYROOCnJ9B225WiwZTXzkNnVZGVavPPqqo9d7AT9D89hcLxpfN2W7IGhMo5jstrqyLtrKHSJhyfs7V1sDxmBaq1ct2ELDC-q2P8SvdJG_XeGJCJQED1NKj98kDeXqaNC0YqOBKrNHtw9FBh70giRJDJTJsOCTvhJhm5D_4TQzRn9kfNx0CwGnw3WXQtsrAPLqgyBhfeeb4n76wYS3IzRZPX9DEIsW6AfdSjv1V59N31xiPIPmaaD_aUC_5FU5VNg8fFkwWZHxvdEV3B6oxLdgBtWNB5f0rK02rY-XzQlBiRUx6FC6sO_zc28hCzKxZUhNL1hBbTVGKirrW1Ve-J4wSX_oJTRLyrmrs5NUEvZ6eBYdzt6csuGMdukhHYjElY2E8vA95mxA50gRJRHkfzwikVWcbFANAA4uJM1H0eQUBKNSb_SaO3puExmPTYLKZhh8H5K-zSCSqCnq54mXHdy9FeMS302Lutk-Ep_tW5iZ3fTbqwAve_3Eq57dw6LFPEf2nmhgj-jV9jRfI_r5dEqvHPDTCdEsa2L-lcp2Mnvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/254877efcb.mp4?token=MfBeQGJA8DfdHqSM8ZVgFHTuJW3IpJOcOQlvzH8tohfFfkpJA00fhVTwuuIb6apjXfO7HlKZ1UC_XslJqnGi3Nj82_UBV2ncf1hJzrRK3iQqHt4AN7tJnVzFkalA5y-TIAtYROOCnJ9B225WiwZTXzkNnVZGVavPPqqo9d7AT9D89hcLxpfN2W7IGhMo5jstrqyLtrKHSJhyfs7V1sDxmBaq1ct2ELDC-q2P8SvdJG_XeGJCJQED1NKj98kDeXqaNC0YqOBKrNHtw9FBh70giRJDJTJsOCTvhJhm5D_4TQzRn9kfNx0CwGnw3WXQtsrAPLqgyBhfeeb4n76wYS3IzRZPX9DEIsW6AfdSjv1V59N31xiPIPmaaD_aUC_5FU5VNg8fFkwWZHxvdEV3B6oxLdgBtWNB5f0rK02rY-XzQlBiRUx6FC6sO_zc28hCzKxZUhNL1hBbTVGKirrW1Ve-J4wSX_oJTRLyrmrs5NUEvZ6eBYdzt6csuGMdukhHYjElY2E8vA95mxA50gRJRHkfzwikVWcbFANAA4uJM1H0eQUBKNSb_SaO3puExmPTYLKZhh8H5K-zSCSqCnq54mXHdy9FeMS302Lutk-Ep_tW5iZ3fTbqwAve_3Eq57dw6LFPEf2nmhgj-jV9jRfI_r5dEqvHPDTCdEsa2L-lcp2Mnvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشه‌ای از تمرینات پرفشار کره‌جنوبی در راه آماده سازی برای جام جهانی آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/661420" target="_blank">📅 15:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661419">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
دادخواست رسمی خانواده شهدای مدرسه میناب علیه آمریکا ثبت شد
🔹
رئیس مرکز وکلا، کارشناسان رسمی و مشاوران خانوادهٔ قوه‌قضاییه از ثبت دادخواست به وکالت از خانواده شهدای مدرسهٔ «شجرهٔ طیبه» میناب علیه دولت آمریکا خبر داد و اعلام کرد این اقدام پس‌از دریافت وکالت از خانوادهٔ شهدا انجام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/661419" target="_blank">📅 15:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661418">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1960e5024c.mp4?token=pQoA7r_Tf69VvnASZtrBk2bbFHTQOlMF4NcHcrzEbviYGaIsoSD3mUdJZ-5nined7cTeXnqrbFUTZO3ASZFk4JqECr4z-_NCkQWDuWSXcgzqSBg1vMEBnt6mnGUG4Bu7-K5zyrVCJAr8MnP4SPdhYPvJCGWFyILBebbJzeFJw68-AtTL_c5tTIVmyMWGS82aWybBRkK3y3AabJhdw6momc34b5qZ6pYI7HIrND51DjrbmbeCwf-HiOwbTBVdImfSGkvBQZiobDXevzuzUsqqCk7W4yEW4urrPQNB6TqCnrqoCKX2u6sWMPrhF_dzM3hMXMZOY30Wv0ToQ-e5GjhSLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1960e5024c.mp4?token=pQoA7r_Tf69VvnASZtrBk2bbFHTQOlMF4NcHcrzEbviYGaIsoSD3mUdJZ-5nined7cTeXnqrbFUTZO3ASZFk4JqECr4z-_NCkQWDuWSXcgzqSBg1vMEBnt6mnGUG4Bu7-K5zyrVCJAr8MnP4SPdhYPvJCGWFyILBebbJzeFJw68-AtTL_c5tTIVmyMWGS82aWybBRkK3y3AabJhdw6momc34b5qZ6pYI7HIrND51DjrbmbeCwf-HiOwbTBVdImfSGkvBQZiobDXevzuzUsqqCk7W4yEW4urrPQNB6TqCnrqoCKX2u6sWMPrhF_dzM3hMXMZOY30Wv0ToQ-e5GjhSLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لاپید: تنگه هرمز قلب معادله جنگ ایران است
🔹
رهبر اپوزیسیون اسرائیل می‌گوید هر تصمیم نظامی علیه ایران، بدون در نظر گرفتن اثرش بر بازار انرژی جهانی و تنگه هرمز، عملاً نادیده گرفتن واقعیت‌های اقتصادی آمریکا و سیاست داخلی آن است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661418" target="_blank">📅 15:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661417">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd6d14fba.mp4?token=Dp1Xk_p6sph2iWcsSWYwkYJ6i4J1x6vpijXEPoGsAOWqCjzjOe_GwfT6VFyKHJKtb5tVlvaeLDYra2RPsWUfOgh5tircD79uzlT7M4HB-Hq9aFWTmctlNKoc1yxW1UXFKBCI5w84l2WB53Nuc_0wdv9irVNW5Wts8G0kA8WY3bgAIASb9JXOJEYseHRCgAlTzfLFNLePnufm77dAxhfc4-wSPZQv70tgjqUeca6HR6tTXxNsnhU_BkGmAzOXok2ynXAxu26WvRWXLsnCnJc4QNsUvo1RtlQDZtoN8rzELqeQQsTdS9OvJ4aaWWqjwi-LwIfWKW6rg0mMW9q6TQWutYPEOUDxc8n-3HK3-P-oasSMRrVNFPhB-tyDEIaUXP4rnBGgqRPtmXR0AqdDxJ391uXNPV3b2OxO2uG8mt1GMmsWVQ6nskPBLU_jRbL4gVAJYHNldYmaEFy_4XiRgkzTbpx-jzvycmCj3FBu2ahGFfg3OB-EVia5_fkSGMR9Z_P0ugXsuJofoX9N9jDuovAn1peHgI4g18M7DUY9_TGKBtPHkgtAUv5hXqyOow_nTWLkXqZ8zrzLYMpuMxtQB9h4PvWIjdH6YtkQ_BtEElFGhHH3GrBPw0LGCHyrxLDLAE_YO2qfL4cCHdIv5_J3nwxzcXBhkn7vOoSj1clIpOgyuj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd6d14fba.mp4?token=Dp1Xk_p6sph2iWcsSWYwkYJ6i4J1x6vpijXEPoGsAOWqCjzjOe_GwfT6VFyKHJKtb5tVlvaeLDYra2RPsWUfOgh5tircD79uzlT7M4HB-Hq9aFWTmctlNKoc1yxW1UXFKBCI5w84l2WB53Nuc_0wdv9irVNW5Wts8G0kA8WY3bgAIASb9JXOJEYseHRCgAlTzfLFNLePnufm77dAxhfc4-wSPZQv70tgjqUeca6HR6tTXxNsnhU_BkGmAzOXok2ynXAxu26WvRWXLsnCnJc4QNsUvo1RtlQDZtoN8rzELqeQQsTdS9OvJ4aaWWqjwi-LwIfWKW6rg0mMW9q6TQWutYPEOUDxc8n-3HK3-P-oasSMRrVNFPhB-tyDEIaUXP4rnBGgqRPtmXR0AqdDxJ391uXNPV3b2OxO2uG8mt1GMmsWVQ6nskPBLU_jRbL4gVAJYHNldYmaEFy_4XiRgkzTbpx-jzvycmCj3FBu2ahGFfg3OB-EVia5_fkSGMR9Z_P0ugXsuJofoX9N9jDuovAn1peHgI4g18M7DUY9_TGKBtPHkgtAUv5hXqyOow_nTWLkXqZ8zrzLYMpuMxtQB9h4PvWIjdH6YtkQ_BtEElFGhHH3GrBPw0LGCHyrxLDLAE_YO2qfL4cCHdIv5_J3nwxzcXBhkn7vOoSj1clIpOgyuj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحریم و اغتشاش دستپخت ما برای نابودی ایران بود
نفتالی بنت:
🔹
در زمان نخست‌وزیریم، با همکاری موساد و سایر گروه‌ها رویکردی ۱۳گانه در قبال ایران اتخاذ کرده بودم.
🔹
این رویکرد شامل فشارهای اقتصادی، سیاسی، امنیتی و غیره بود.
🔹
یکی از کارهایی که کردیم این بود که هزاران ماهواره استارلینک را داخل این کشور قاچاق کردیم تا در اغتشاشات، اتصال اینترنت برقرار بماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661417" target="_blank">📅 15:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661416">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33afe1d58.mp4?token=c3Af2IF6w8syDgKRVTTVAq6SKdcF4fEzWR8A--SUaIix7ycdNun-Bs_2J5CVVAdqLBQP8rYWR0zHOMgP2uoLFme_KSH2ZoCup6RMH_g4cZeitRDUEBa8TNpVBhO2TeUjBKblec8JbRaxNv42LZHNUxmy94qau2lrIlu7GP64v1-XVlMfsQeXyG1Ga4ypXujTwx1Ye8JQoCw732Iw0eus6TtcN9C1Y2dZyFtOV7VbTj8JaAie9H4aBEnxQ9yl89YaTjySJEw-WFCpa2fjyI5-rZytbsw4zr9LoQa8gc4FrPLrI8BdKFxQPoxm0pNJV1bKQlNHiboqdIteR0hU1_rVyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33afe1d58.mp4?token=c3Af2IF6w8syDgKRVTTVAq6SKdcF4fEzWR8A--SUaIix7ycdNun-Bs_2J5CVVAdqLBQP8rYWR0zHOMgP2uoLFme_KSH2ZoCup6RMH_g4cZeitRDUEBa8TNpVBhO2TeUjBKblec8JbRaxNv42LZHNUxmy94qau2lrIlu7GP64v1-XVlMfsQeXyG1Ga4ypXujTwx1Ye8JQoCw732Iw0eus6TtcN9C1Y2dZyFtOV7VbTj8JaAie9H4aBEnxQ9yl89YaTjySJEw-WFCpa2fjyI5-rZytbsw4zr9LoQa8gc4FrPLrI8BdKFxQPoxm0pNJV1bKQlNHiboqdIteR0hU1_rVyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پروفسور جیانگ تحلیلگر سیاسی: از نظر راهبردی ایران نباید آتش بس را می‌پذیرفت
🔹
اگر ۶ ماه دیگر جنگ ادامه پیدا می‌کرد کار آمریکا و اسرائیل تمام بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661416" target="_blank">📅 15:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661415">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738e76890c.mp4?token=EDuuwfFyPM3trE05UDr1cuwlfMHCmQhyxYafEDZvG9-mHZFk9rq0yYHSDCyeAp65AMHuaTXb9O-oI_1MBpuNdGVoiOMHLgMs31zvolEq2bSQzXbDZWB4-9ajadRtlXo5DJ2333JgUKWUQTk8xbGCH0wPA3fT98J_I3xPf73H9PNfKL9W05zF8eCSBlDcUcgW3fg8oZveHgYv5qUM5Cg-ZbioCQ-Jt0Plm7BnIVp7OH-uUWcbL8Vt1q1LubJWTNjNmA4dBxbjwps15Cp3MwQO89ybTPF72eUXH1Mk9oT3u3AyXGha3JvoMyHg8ke-spJ45ZUCvLp7JWJX-BXO4aXVgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738e76890c.mp4?token=EDuuwfFyPM3trE05UDr1cuwlfMHCmQhyxYafEDZvG9-mHZFk9rq0yYHSDCyeAp65AMHuaTXb9O-oI_1MBpuNdGVoiOMHLgMs31zvolEq2bSQzXbDZWB4-9ajadRtlXo5DJ2333JgUKWUQTk8xbGCH0wPA3fT98J_I3xPf73H9PNfKL9W05zF8eCSBlDcUcgW3fg8oZveHgYv5qUM5Cg-ZbioCQ-Jt0Plm7BnIVp7OH-uUWcbL8Vt1q1LubJWTNjNmA4dBxbjwps15Cp3MwQO89ybTPF72eUXH1Mk9oT3u3AyXGha3JvoMyHg8ke-spJ45ZUCvLp7JWJX-BXO4aXVgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لاپید: تنگه هرمز قلب معادله جنگ ایران است
🔹
رهبر اپوزیسیون اسرائیل می‌گوید هر تصمیم نظامی علیه ایران، بدون در نظر گرفتن اثرش بر بازار انرژی جهانی و تنگه هرمز، عملاً نادیده گرفتن واقعیت‌های اقتصادی آمریکا و سیاست داخلی آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661415" target="_blank">📅 15:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661414">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وزارت امور خارجه سوئیس: ما به فراهم کردن محیطی محرمانه و قابل اعتماد جهت تسهیل گفتگوها در بورگونشتوک پیرامون اجرای یادداشت تفاهم ادامه می‌دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661414" target="_blank">📅 15:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661413">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee9dcec1c.mp4?token=mRvbiFdfNt5QuO39NzDA_jhluCbXj9rdAo0p1-bkkvQlWy_y7HOF0lQ7XFSIDA2XdEzZo8oH23MYqgkYpMmGHInv14Ol7EvTTTx3DTazc9MRBaGGWG44Op_brZ1KU_etMuAVk0nY8pVzKoKmz-BTozZ-ZuTcjP-OVMMS7l6QfmgrS_KShdAD-J9riNFOvOMArzsceiXu-zup7OCqncZ_U74sOWmPFsmoCUBynueCGSR2_KN_I8A_DgklzM-GdGvkeNPXaP7LE6KYFNcS9vySDBcdU9HhKnrkbkxQiMCmgvJnSeBiyUzqcbLk9-nLM9eIkgJGK153wCnoZc_5frZzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee9dcec1c.mp4?token=mRvbiFdfNt5QuO39NzDA_jhluCbXj9rdAo0p1-bkkvQlWy_y7HOF0lQ7XFSIDA2XdEzZo8oH23MYqgkYpMmGHInv14Ol7EvTTTx3DTazc9MRBaGGWG44Op_brZ1KU_etMuAVk0nY8pVzKoKmz-BTozZ-ZuTcjP-OVMMS7l6QfmgrS_KShdAD-J9riNFOvOMArzsceiXu-zup7OCqncZ_U74sOWmPFsmoCUBynueCGSR2_KN_I8A_DgklzM-GdGvkeNPXaP7LE6KYFNcS9vySDBcdU9HhKnrkbkxQiMCmgvJnSeBiyUzqcbLk9-nLM9eIkgJGK153wCnoZc_5frZzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندیشمند برجسته آمریکایی؛ این واقعا شگفت‌انگیز است، این یک تسلیم بی‌قیدوشرط بود/ایران به هر آنچه می‌خواست رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661413" target="_blank">📅 14:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661412">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139b8a8525.mp4?token=TaecoO_u4-Q4vEqOOl-zXj7ZJtfKjbLahhUHj6_C-7QsZK1WfQxvSJFYTrPMpUaJv-DwjTDLQBC--K4UnC7YPxOSVHwBBBsVKje_TzeJO3URydee2d7JGW8WTnv3gUXZtxLwi_xxKAUEo_ZP7Jff3n5ngPy_EKZ8Dw1AaUSYkSl3uY2jArCis6_bpzjhr52sA_LYnxGf5dmt43bvOCm4YkB0njIknSvm0IBsTWJl42sV4NUumL5dbh2a3YZb_RF9qabWe_7p4ttlNRmcvOpoAYs-Qiw2Lkc2gU6JjzM9NTaCQGyQQdGtmf3920A6zaYDTDmqaGqg3BA8BjUQdRxU1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139b8a8525.mp4?token=TaecoO_u4-Q4vEqOOl-zXj7ZJtfKjbLahhUHj6_C-7QsZK1WfQxvSJFYTrPMpUaJv-DwjTDLQBC--K4UnC7YPxOSVHwBBBsVKje_TzeJO3URydee2d7JGW8WTnv3gUXZtxLwi_xxKAUEo_ZP7Jff3n5ngPy_EKZ8Dw1AaUSYkSl3uY2jArCis6_bpzjhr52sA_LYnxGf5dmt43bvOCm4YkB0njIknSvm0IBsTWJl42sV4NUumL5dbh2a3YZb_RF9qabWe_7p4ttlNRmcvOpoAYs-Qiw2Lkc2gU6JjzM9NTaCQGyQQdGtmf3920A6zaYDTDmqaGqg3BA8BjUQdRxU1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر معظم انقلاب: رئیس‌جمهور ایالات متحده بود که برای این یادداشت تفاهم التماس می‌کرد
🔹
ترامپ: بدون توافق ذخایر نفت تنها ۴ هفته دوام می‌آورد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661412" target="_blank">📅 14:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661411">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wtm30eyedmAFUIYyaN8ZT_gKuZUnfplu3mzqnZxQUPG-aNnfEDbswKdklxAh57YWvo_gxEiu7EJo7ewyfyF4Pn6rmzAPT0gOV1yYiKSTdU30f1x1GZigehEhPOZIKkYx240PMuk-mUr8A5kXNiwJtDzpJ-I4HJiAbc0ilvIYqr3nIKbwF-m7zz2HwxjhYmUzWuzkUiSiDdpBgy3OgthAbr75TLk9B3xwUZk6sYp_SXHuwhxVVro8hpNH2XqVvyKp3XckdkehJbQmUg5mNYuUx8lmxzJwA5NpaAYxc07goGdGG_i8uVAnEHUa5j7aPnXD7k19Ycyf-SslMysIgMCB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد
🔹
دولت‌های اوباما و بایدن در قبال ایران ضعیف عمل کرده‌اند. با روی کار آمدن من، سیاست آمریکا در قبال ایران تغییر کرد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661411" target="_blank">📅 14:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661410">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
حزب الله: در مقابل تلاش دشمن برای تصرف اراضی لبنان کوتاه نمی‌آییم
🔹
اتاق عملیات حزب الله لبنان با صدور بیانیه‌ای اعلام کرد که همزمان با پایبندی مقاومت اسلامی به آتش‌بس، در مقابله با هرگونه تلاش دشمن برای تصرف اراضی و گسترش اشغالگری کوتاهی نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661410" target="_blank">📅 14:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661409">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
نیروی دریایی سپاه: اگر شناورها مسیر دریایی جنوب جزیرۀ لارک را رعایت نکنند، مسئولیت هر اتفاقی با خودشان است
🔹
از برخورد احتمالی با مین تا تصادف‌های دریایی و حتی هدف قرار گرفتن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661409" target="_blank">📅 14:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661408">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b36f5f37d.mp4?token=TeDqvbkmkdjVfD5g2jgj4EIaWEkk2gF0LG1VqLWXQTJykTaKG6WRTEQKDyNY1tYjvEFsS_y-PjMa_Ql4kbgNOqHtqJkWvotPKWzQIOi6yQ0NvmcUbjCSUNZ_6eYBZKISRviRD42A9yiqi9x8k5SpxQtC5PPdd-C87sPWiV4WqfU0kHo4RwPuGtdEkCFFJL-BD5Yz2cIwLS7m6lc1-R3ea3vYCVz4IB-xU1msEZ-G1f0pdmnNmRm2KKnGnJst-bRuZ8TngdvwXG6sDAVtCYQNBgQJLS8NlS6Z9aeRXEONSlXMN7BCAZ9FojMez3GE66Weev1Y2DHzo4v8O_DJFHFyJiJphBk4P1sxfydcY-qqMqw2EOFn0ep46ZgeU5qwoBB0tzbwfHMCr-idmhfn_tEZL96Vls4Aj-XvlJf2W2I2b_dg5CnDQynMZb89mtx9S1bfXWwWMSMEqv-kscI6nrLE8bd0CGH7044a0Lh6Q40tsfcsfzI3tjIwH1tXZkBFCSOp5rxTnaoEs8hKT3ZqLp7yhKr1w8fRP2Bn6mtmi3bnGWrSVK2XWzhJqr3DO-U52cPPAE-xM9X9EvNWV4Yc8sXSb8JlbmlkzxNaKRMu-T5D6zIYoTv6wd0JHkbYsPKWwek8M9jaqKiKC-hsG9QeQ9BLnLIuoZAIG5pfk3sI4AEfecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b36f5f37d.mp4?token=TeDqvbkmkdjVfD5g2jgj4EIaWEkk2gF0LG1VqLWXQTJykTaKG6WRTEQKDyNY1tYjvEFsS_y-PjMa_Ql4kbgNOqHtqJkWvotPKWzQIOi6yQ0NvmcUbjCSUNZ_6eYBZKISRviRD42A9yiqi9x8k5SpxQtC5PPdd-C87sPWiV4WqfU0kHo4RwPuGtdEkCFFJL-BD5Yz2cIwLS7m6lc1-R3ea3vYCVz4IB-xU1msEZ-G1f0pdmnNmRm2KKnGnJst-bRuZ8TngdvwXG6sDAVtCYQNBgQJLS8NlS6Z9aeRXEONSlXMN7BCAZ9FojMez3GE66Weev1Y2DHzo4v8O_DJFHFyJiJphBk4P1sxfydcY-qqMqw2EOFn0ep46ZgeU5qwoBB0tzbwfHMCr-idmhfn_tEZL96Vls4Aj-XvlJf2W2I2b_dg5CnDQynMZb89mtx9S1bfXWwWMSMEqv-kscI6nrLE8bd0CGH7044a0Lh6Q40tsfcsfzI3tjIwH1tXZkBFCSOp5rxTnaoEs8hKT3ZqLp7yhKr1w8fRP2Bn6mtmi3bnGWrSVK2XWzhJqr3DO-U52cPPAE-xM9X9EvNWV4Yc8sXSb8JlbmlkzxNaKRMu-T5D6zIYoTv6wd0JHkbYsPKWwek8M9jaqKiKC-hsG9QeQ9BLnLIuoZAIG5pfk3sI4AEfecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چیزی به نام آتش‌بس در لبنان وجود ندارد!
🔹
خبرنگار: شاهد یکی از شدیدترین حملات به منطقه نبطیه هستیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661408" target="_blank">📅 14:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661405">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2029917f7.mp4?token=YBvVjryGQSuWxs8OScW5hZvaiV-etnpXqqQNd2a5qct0SbQqwB5JFNr_-_gWXW1l6e0IEj9HApD2e2YRfKEgEOPQWZsKYO-3eqCE9xu-u8SHwHsiplroD2rGKWOdXoRHmQ1R2QFK_wxEZ-pks-ZvvpGjIrwsF1odgKS0SbXfxDVt7jEAp_E3-wiFuF8AzWm4fIwlv7_bsU1wCGmQyVLSQFaNR81lJknJ5DSxUQuf5IEp7wDDh6GcrF8FczOP_KOQMGXqsq1zCaHFkluUzF71oHJ1C9k67ZU53yk6OylhDjYsYdrS9CBFxc8ZP7YQrG6s9nw8hS-F-l34T255EQ2y_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2029917f7.mp4?token=YBvVjryGQSuWxs8OScW5hZvaiV-etnpXqqQNd2a5qct0SbQqwB5JFNr_-_gWXW1l6e0IEj9HApD2e2YRfKEgEOPQWZsKYO-3eqCE9xu-u8SHwHsiplroD2rGKWOdXoRHmQ1R2QFK_wxEZ-pks-ZvvpGjIrwsF1odgKS0SbXfxDVt7jEAp_E3-wiFuF8AzWm4fIwlv7_bsU1wCGmQyVLSQFaNR81lJknJ5DSxUQuf5IEp7wDDh6GcrF8FczOP_KOQMGXqsq1zCaHFkluUzF71oHJ1C9k67ZU53yk6OylhDjYsYdrS9CBFxc8ZP7YQrG6s9nw8hS-F-l34T255EQ2y_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایت در شهرک قناریت در جنوب لبنان
🔹
منابع لبنانی از حملات شدید و پیوسته به شهرک قناریت در جنوب این کشور خبر دادند که تا این لحظه به شهادت دست‌کم ۷ نفر و مجروح‌شدن ۱۷ تن دیگر منجر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661405" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661404">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ابلاغ دستورالعمل فروش ارز اربعین؛ سهم هر زائر ۲۰۰ هزار دینار
🔹
بانک مرکزی دستورالعمل تأمین و فروش ارز زیارتی اربعین سال ۱۴۰۵ را ابلاغ کرد که بر اساس آن هر متقاضی بالای پنج سال می‌تواند تا سقف ۲۰۰ هزار دینار عراق دریافت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661404" target="_blank">📅 14:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661403">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a971dbe16.mp4?token=piBImmlDU4umo-YqcHAQjZYd6vKo-ZB9ucnr9VfZzkhwX-YWN39_LWWtX0B3p9bxDt8vRPD4BGjsjF1lwQw40Cp23lM9e5pkJnQwi1vOZYpNMpJdne2z_84RlbOISZ5KFaoFMGvM37getmMN9rTrGrtvzWxfMipoeSGMvh-GcO7MfI_cbjgkIT25DeNso6aVFzOGEtwkdgIKLIZItyvH5QGnGHQ1ZyTqR5xCnW1insOS5uWM0gaPBZJNiRZXZI2xzQ2Qd-XIKI8MBZibluUsdOJQZ5Llk8rg5AdKQmIf5oVPTorFTB3yiT1AFE0NGxEqEZwqXk3shZadrht7BqXckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a971dbe16.mp4?token=piBImmlDU4umo-YqcHAQjZYd6vKo-ZB9ucnr9VfZzkhwX-YWN39_LWWtX0B3p9bxDt8vRPD4BGjsjF1lwQw40Cp23lM9e5pkJnQwi1vOZYpNMpJdne2z_84RlbOISZ5KFaoFMGvM37getmMN9rTrGrtvzWxfMipoeSGMvh-GcO7MfI_cbjgkIT25DeNso6aVFzOGEtwkdgIKLIZItyvH5QGnGHQ1ZyTqR5xCnW1insOS5uWM0gaPBZJNiRZXZI2xzQ2Qd-XIKI8MBZibluUsdOJQZ5Llk8rg5AdKQmIf5oVPTorFTB3yiT1AFE0NGxEqEZwqXk3shZadrht7BqXckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پرده لباس‌های یک‌شکل مدیرعامل انویدیا؛ سادگی به سبک میلیاردرها: هر روز مشکی می‌پوشم تا یک تصمیم کمتر بگیرم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661403" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661401">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U942zxZWRxOHHOtWHvJ7jGcd-cBWddVwNWA2Ktq3jtwVREvHHQhdXNGKSWey5_88tz8HaDn4phfiqGKDPyaA3-4D6fWtSZMbjVzabreUqE_vs9a4X5f8TlxcBn7nxpmyNFgNnjvyn66oQdO8IdZA-nbUzNJbjp9YfOboiRZh3aZ093tK01n8_T9LqUMfvqZk56G0oFeJ6F_-0QLbm-CHNluoBN82W2h2MAPwhQQZtoJmsfkHtXTEm3PbO3r144jzwheTvtXNLLCaF7LwzlVt-QZdEx3bUP-oImLrd9-v00uP9ZLAieGWyzYCsuDfMlxqfaMV4qtPJAgox49FP_5fdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰ درصد بازار پوشاک در اختیار کالای قاچاق
🔸
سالانه حدود ۲.۵ تا ۳ میلیارد دلار از بازار پوشاک کشور به کالای قاچاق اختصاص دارد.
🔸
برآوردها نشان می‌دهد سهم قاچاق در این بازار تا حدود ۳۰٪ کل مصرف است.
@amarfact</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661401" target="_blank">📅 14:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661400">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d08bb1e1.mp4?token=I9XgkGQh-qXqV43q-b9apft94wX7ntGUBGtewtyKw5FNy49Vd2-6B00ArMpv3-OXfdpsGIlCypZfrGGPvYjr6JKqn4OEss1i-gPW-7yIN-edkJ5ImXU1jgyRJeOaR0QQruUJ30kQG31VjgYgDSRWma_YxvYEpMtcu7xxA0exH2OWtOlMhqXp5zBCDDCFEtV-kqjpMqkTLUIuh6pYLgx78KE_Ygkv2bLCHJKzVXYBnAPLqbpp9nZq2d4a5kkHtmoezxoCXTRqk5NkVNqdYszL5CdVt4SlZ_sUQ5oR5LUeiitvWlihe63pZza3v13Y9LA8OokLe0084Hg2GEySewWxIpgmL_R9JQpiTcO2qScN_GkIzj_V0fnhYInMB0LU-CX3jls95RpwPxY4P50jHsmE1b1dOEgrkT0DmSf8jkWXrc9TraxVDheFI3wAZ1jQYKktCZxzYFiKRJ5zdHUaLF1AJyXferv8rBOM9VwFIJity0BM0WPDTx8AGsKiMT085SAauA_2ztrOvXiYJwtJlbJO8NgOk4zniAJJEvuA5VqJGaZHqiNfn84aq8NaMx_8B8sZ_BOFklTdVq9uNlRTSywkCk1B8xA9Z311WmXNFh-NXI0M5ErCu0uGqjjv8KWiXMY2287gpud1FL2aMiThTeZMIaWyia1b5o4y8pKsU4_5pWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d08bb1e1.mp4?token=I9XgkGQh-qXqV43q-b9apft94wX7ntGUBGtewtyKw5FNy49Vd2-6B00ArMpv3-OXfdpsGIlCypZfrGGPvYjr6JKqn4OEss1i-gPW-7yIN-edkJ5ImXU1jgyRJeOaR0QQruUJ30kQG31VjgYgDSRWma_YxvYEpMtcu7xxA0exH2OWtOlMhqXp5zBCDDCFEtV-kqjpMqkTLUIuh6pYLgx78KE_Ygkv2bLCHJKzVXYBnAPLqbpp9nZq2d4a5kkHtmoezxoCXTRqk5NkVNqdYszL5CdVt4SlZ_sUQ5oR5LUeiitvWlihe63pZza3v13Y9LA8OokLe0084Hg2GEySewWxIpgmL_R9JQpiTcO2qScN_GkIzj_V0fnhYInMB0LU-CX3jls95RpwPxY4P50jHsmE1b1dOEgrkT0DmSf8jkWXrc9TraxVDheFI3wAZ1jQYKktCZxzYFiKRJ5zdHUaLF1AJyXferv8rBOM9VwFIJity0BM0WPDTx8AGsKiMT085SAauA_2ztrOvXiYJwtJlbJO8NgOk4zniAJJEvuA5VqJGaZHqiNfn84aq8NaMx_8B8sZ_BOFklTdVq9uNlRTSywkCk1B8xA9Z311WmXNFh-NXI0M5ErCu0uGqjjv8KWiXMY2287gpud1FL2aMiThTeZMIaWyia1b5o4y8pKsU4_5pWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت نوزدهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم اعظم فکریان که در قالی‌بافی مشغول به کار بودند و یک روز به دلیل بی احترامی فرزندشان دلشکسته شده و اقدام به خودکشی می‌کنند و روح از بدن جدا و به عالم برزخ سفر کرده و تشنگی مفرط و عذاب‌آوری را درک می‌کنند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: اعظم فکریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661400" target="_blank">📅 14:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661398">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71bb3ee9dd.mp4?token=mLt8Xazrjd_iS8sRu5vevcEkMXKZECHp1BqoAbkXtfOgS5M0Kj82VN_3nalzciJMPo6Lz3NmTCUJvgGlsVscNvEwkVI8G0MzVZB8rTJx_OqFU6I8sCB0SpXn4OKpZ2PxPNNYeVlwOKRtx7GDwzPX5caVTHiLx0018oWBXHvD7039vqilfWbFTpSPXL9N4ASRHZqqMm0ej0T3rXD6VN2YPZ4kCx5yQxlQcE3et2BgpVbwSlhkSb9fcxMT6XSjwCH8yd4ib0HEvNZktAj9DAIZyRo5eUlSYjV4D8l1gk2S3pyW4ZMWQuMXXT2jLGwWoITv1_AIRGfo4T3zRKzYCd1umg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71bb3ee9dd.mp4?token=mLt8Xazrjd_iS8sRu5vevcEkMXKZECHp1BqoAbkXtfOgS5M0Kj82VN_3nalzciJMPo6Lz3NmTCUJvgGlsVscNvEwkVI8G0MzVZB8rTJx_OqFU6I8sCB0SpXn4OKpZ2PxPNNYeVlwOKRtx7GDwzPX5caVTHiLx0018oWBXHvD7039vqilfWbFTpSPXL9N4ASRHZqqMm0ej0T3rXD6VN2YPZ4kCx5yQxlQcE3et2BgpVbwSlhkSb9fcxMT6XSjwCH8yd4ib0HEvNZktAj9DAIZyRo5eUlSYjV4D8l1gk2S3pyW4ZMWQuMXXT2jLGwWoITv1_AIRGfo4T3zRKzYCd1umg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماشای بازی ترکیه در آمفی‌تئاتر باستانی کاش
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661398" target="_blank">📅 14:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661397">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJIThEQ4EU0-ZD5LXZfbWrq8vRu5eGnoWb2VQCW6cdEoBqzduPDsR47XrVhLDDvzfga1n4codpeX9d8-UbFBHmnYyHinu9E0lTBW4sHKH7zeAmS-CpLov_Uryr1hLFmJCZgJaPO5h7E-qyaYCMLzUeMOxMUmRoxspuAP49kaA2Iu9dgqBAvuNkboV_mVgcVJfsCXrDetYu6Wn8DfpW9zOVGKcH94f8T1MUDdpRtNi8Ai_mjIr_pGcHJDoSSpYiXdIl5pH5WtBm07VvCcPjSXBFQqiwL_UMzZ3Krcxrg-LPcfAyogWJmWGQs_MfLNLD4AEHd5271R6iKH5_P_rDxY3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«قرار بازداشت» رو زیاد شنیدیم، ولی دقیقاً یعنی چی؟ #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661397" target="_blank">📅 14:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661396">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291962135c.mp4?token=Jzm22rC9fHZkzFF6oh3_3-J3cqQMflnxsBuwqMtWsBqDBVvQ1T2ax8WdHJ3OAhYvU6md2OcaW4V4sZfWBRwlZI0X4XxGbjXXLUZgwy1aEAP9RiEXTj2mmP4wBRlpt8KWCXoPdxaNbSBnj112_C-9AdYbTbnI-XN62RHztPT-MemG7BH7vuyEDaxWyFhKM2RYiNLBX9pSS0qEFdI2hw64eSZb0n39WN-Ss9Jpr9Ah4JjpIfNm3PCAPESj8ztoi4YBPjVgAQ5Pc59LAyi-H4cHmL2X2sirOug4DBLVvexVFyxIulF_4lfsmKAM02DHQa9SEIBkNjF_zY32NIdYkuQcfR40BUve2o3YiAxXptcvvibqbAVhwwiRSA3Rog_XiYXgySxz5PTbTbqRRW-WT6S5p8Wz3wtmRWUq7BFH4m_pCAN86BexL5-tVetT6XjHs2rPxyuVGjS9hMFgxUiLRE58HMu8qCo4O-pLJI6ZI_luf-CfP0JplRBeehqLr3PmunUScDvfEufqslK4q5e84WNVBGC9yL5D5glGeElsibYQskVtlQffBYE6ey1nv65c0O-k2RVnR4BK8zRbH8vPj6rD83i5He1eiDwJMtM6Pw-bw8dK5C86RJXwvnRIrURppyAc2A_48Hz_-71zizLlDoN88cxmizF37J_J_0OJW_fP8ac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291962135c.mp4?token=Jzm22rC9fHZkzFF6oh3_3-J3cqQMflnxsBuwqMtWsBqDBVvQ1T2ax8WdHJ3OAhYvU6md2OcaW4V4sZfWBRwlZI0X4XxGbjXXLUZgwy1aEAP9RiEXTj2mmP4wBRlpt8KWCXoPdxaNbSBnj112_C-9AdYbTbnI-XN62RHztPT-MemG7BH7vuyEDaxWyFhKM2RYiNLBX9pSS0qEFdI2hw64eSZb0n39WN-Ss9Jpr9Ah4JjpIfNm3PCAPESj8ztoi4YBPjVgAQ5Pc59LAyi-H4cHmL2X2sirOug4DBLVvexVFyxIulF_4lfsmKAM02DHQa9SEIBkNjF_zY32NIdYkuQcfR40BUve2o3YiAxXptcvvibqbAVhwwiRSA3Rog_XiYXgySxz5PTbTbqRRW-WT6S5p8Wz3wtmRWUq7BFH4m_pCAN86BexL5-tVetT6XjHs2rPxyuVGjS9hMFgxUiLRE58HMu8qCo4O-pLJI6ZI_luf-CfP0JplRBeehqLr3PmunUScDvfEufqslK4q5e84WNVBGC9yL5D5glGeElsibYQskVtlQffBYE6ey1nv65c0O-k2RVnR4BK8zRbH8vPj6rD83i5He1eiDwJMtM6Pw-bw8dK5C86RJXwvnRIrURppyAc2A_48Hz_-71zizLlDoN88cxmizF37J_J_0OJW_fP8ac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نبویان جزئیات جدید درباره نامه‌های رهبری ارائه کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/661396" target="_blank">📅 13:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661395">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
وزیر کشور پاکستان وارد مشهد شد
🔹
پیش از ظهر شنبه هواپیمای حامل وزیر کشور پاکستان که به منظور دیدار با مقامات جمهوری اسلامی به کشورمان سفر کرده است، در مشهد به زمین نشست.  #اخبار_مشهد در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661395" target="_blank">📅 13:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661394">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab51b559a8.mp4?token=bzpy39wPkhuKOKAKoO5S1TYV__tf2MVYY-uizJNec-YpluGNtTW-gDwbYES0yI2qFvWvAgHrGaGLSzynW-hvoFHOWtDrj86sGXRE2MWPRlhoJbazs3RUWY8man8oJTgbXKOWvz4PYQQ1XfqBXpJxtQp0l2leNg0sJ7-ZXPZktYW1A6vl9wwONVMMthQq4JdMHOKq3dzY2QkAIU0l0ChX4AmgJXA7wThWD8ANsg7c8q_0b6xFZSOi_qzk3gFfX7_dWAscV0LOz95LA9-5rYospxpXMjDPuLzDGv4fw_Bt-xFtspi4696J3mic03EKjutTWLYXSqgdHF69BSj5Opm1LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab51b559a8.mp4?token=bzpy39wPkhuKOKAKoO5S1TYV__tf2MVYY-uizJNec-YpluGNtTW-gDwbYES0yI2qFvWvAgHrGaGLSzynW-hvoFHOWtDrj86sGXRE2MWPRlhoJbazs3RUWY8man8oJTgbXKOWvz4PYQQ1XfqBXpJxtQp0l2leNg0sJ7-ZXPZktYW1A6vl9wwONVMMthQq4JdMHOKq3dzY2QkAIU0l0ChX4AmgJXA7wThWD8ANsg7c8q_0b6xFZSOi_qzk3gFfX7_dWAscV0LOz95LA9-5rYospxpXMjDPuLzDGv4fw_Bt-xFtspi4696J3mic03EKjutTWLYXSqgdHF69BSj5Opm1LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت اطلاعات از شناسایی و دستگیری سه تن از لیدرهای میدانی و ۱۴ نفر از مزدوران شبکه خرابکاری خیابانی دشمن آمریکایی-صهیونیستی در استان ایلام
خبر داد
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661394" target="_blank">📅 13:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661392">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e1db5f80.mp4?token=PtsIvCv3ooSIHfx2Zwln1RbnCl8sHkHSEVTh4YHhNAg76QoLqqOZ0AW9q691neSjm7L68pL2zX2NH8Ak8panolVrIPSmqPkTz3eSdQUWh0ouS-ebp__uX32E5JkQab7ejrmDIDeaXIMUXTJE4dGrjnXNxq-dxrZmyMg0c-wbbN9UHnT_RBvzouuEEloXyVcJauFM71PGl936PKg-vmU_xjSnawcQofNLe7xZY_O3WcEIQry0ZaQjm0V0jW5lNtcxiXUkI1-sNy3jT7Jw9WYOh5_bG4JTwkI-vDzYktLGoMG6BEAdgCdWoV6CFTl2zdK2lpzIspML4T3MgUuiqC1fYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e1db5f80.mp4?token=PtsIvCv3ooSIHfx2Zwln1RbnCl8sHkHSEVTh4YHhNAg76QoLqqOZ0AW9q691neSjm7L68pL2zX2NH8Ak8panolVrIPSmqPkTz3eSdQUWh0ouS-ebp__uX32E5JkQab7ejrmDIDeaXIMUXTJE4dGrjnXNxq-dxrZmyMg0c-wbbN9UHnT_RBvzouuEEloXyVcJauFM71PGl936PKg-vmU_xjSnawcQofNLe7xZY_O3WcEIQry0ZaQjm0V0jW5lNtcxiXUkI1-sNy3jT7Jw9WYOh5_bG4JTwkI-vDzYktLGoMG6BEAdgCdWoV6CFTl2zdK2lpzIspML4T3MgUuiqC1fYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل در ووهان چین
🔹
به دنبال جاری شدن سیل در ووهان چین، حمل و نقل در شهر مختل شده و خودروها در خیابان‌های آبگرفته، شناور شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661392" target="_blank">📅 13:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661391">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مشمولان اعزامی تیرماه ۱۴۰۵ برای دریافت برگ محل مراجعه و معرفی‌نامه به دفاتر پلیس+۱۰ مراجعه کنند.
🔹
هلاکت یک نظامی دیگر رژیم صهیونیستی در جنوب لبنان
🔹
یک شهید و ۸ زخمی در حمله هوایی اسرائیل به منطقه صیدا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661391" target="_blank">📅 13:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661390">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpcMQ28Lo5ETFKaZKzNCAkzQ-Fx1DezVcpm5h0bI8r1K8W8J3FBVHy1rX72Cb6VQDhZet7jOBbGg1pAgBmQS8BbQCZb46VHV009wodKjEqRLuaLILXoTNCmRgWRJnOh9bHnM9K2hkUDqRwtHHYZ3bq7_79QiCKbc1c2emSvOriilALAZD_HPJKqymNxxuX9MMsXTQrqjHwHDwc6NUSTus0vde-NWDcAtUNo8IkYs2hgzMsJxn5u2AT7hcY74hfhR84VhfvHbpaEIMdpI2Udlqr8Gj5XUl4CaXh8qCWX2A9KMsEW0_LjCKlwiTWLxk1fZQ5lXwjmhcoAu4TZKlyF6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت کاربر آمریکایی درباره مادورو و نتانیاهو: یکی این تناقض رو برام توضیح بده
کاربر آمریکایی:
🔹
ما مادورو را براساس یک حکمِ بازداشت دستگیر کردیم، اما نتانیاهو که در ۱۲۴ کشور تحت تعقیبه، شش بار به کاخ سفید دعوت شده؟ یکی این تناقض رو برام توضیح بده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661390" target="_blank">📅 13:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661389">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
حمایت خواننده لس‌آنجلسی از ایران و تیم ملی
🔹
گورگن زرگریان خواننده لس آنجلسی که در حمایت از تیم ملی فوتبال تا تیخوانا آمده، برای ایران و تیم ملی کشورمان آرزوی موفقیت کرد.
🔹
گفتنی است، او خواننده‌ای است که پیش از این از مواضع قیصر انتقاد می‌کرد!
خبرهای لحظه به لحظه جام جهانی را اینجل کلیک کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/661389" target="_blank">📅 13:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661388">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENMIvHaRTIjf6YjcjLkRhHIbBczE5TvlBh3dOXcmvV1ukkBYRDs4pgrkQ2pmggux1SzlXr9dChHdqtrNIBxIfEEZE7bf34xZFfsaJ6sFi8g04bB_XZHIu22SvwOdTKaLJrcREVOBFmdXVECevs13luT4BsacX4kPVQDuOGjNaLaQex7qke8qmLc-YJBrmCNdMLjjjGaehN0NPgQVJF2eZrq6liBAq5w0egSQPLkBcPs4_eMI3DvtIuzMS05JofEGCt2v-o_ptkdaYTmz1NxIFEGY94793IBOS0C8AdnTwHy4bdGdWZRRyQoq1GJJjFRO1CcO50_ppYBEafIzqO254Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب هولناک جنایت میناب، برندۀ جایزۀ بهترین عکس سال جهان شد
🔹
مرتضی آخوندی، عکاس ایرانی، به خاطر تصویر هوایی تحسین‌شده‌اش از مراسم تشییع جنازه باشکوه ۱۶۸ دانش‌آموز شهید در میناب، مقام اول جوایز معتبر گلدن شات ۲۰۲۶ را از آن خود کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661388" target="_blank">📅 13:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661387">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
واشنگتن پست به نقل از یک مقام پاکستانی: اسلام آباد با تهران و واشنگتن در تماس است و با جدیت برای رفع موانع تلاش می کند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661387" target="_blank">📅 13:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661384">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
واشنگتن پست به نقل از یک مقام پاکستانی: اسلام آباد با تهران و واشنگتن در تماس است و با جدیت برای رفع موانع تلاش می کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661384" target="_blank">📅 13:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661383">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای ارتش اسرائیل در حال بمباران جنوب لبنان
:
اگر حزب الله از نقض توافقات و انجام عملیات خصمانه دست بردارد، ثبات برای هر دو طرف ممکن خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661383" target="_blank">📅 13:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661382">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from️لوازم خانگی بهشت بانه️(admin)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qh7HqxNQGOn5QY7xDQlervCdcAGLMx4lsBBwVF-3GZMzrkw26Pw1iihKUjI5vlNHQ6pT8UNyd0yAS6Or-J3qx0Qh6GqlzEIPeUC29HjK2Yj8zzi-IQUw74kiWGM117slF8aNrB_x4qiT6DBnG07GnPsHK-RV8YSLFct8TcwiFMn5diw7gRn6d-wskwfaYGuAN1-9flJoLtDREdcOvhTbYELKNdAgI0pouc23B2W-N9RZZynhckV6giQ0yJaqNXIWG44Oz4zdymD70JmwyYqF8tP6C2sj1lEJSX2CQs8OFMWvtQLJcOTMHm_4pCJMSX-fgpkfVMH81Vx3CfN6I2efVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش اجناس با نرخ دلار150.000
💵
✅
فروشگاه  بهشت بانه سلیمانیه عراق
✅
لوازم خانگی عمده برندهای معتبر
✅
الجی کره
✅
بوش المان
✅
سامسونگ
✅
تحویل درب منزل باگارانتی شرکتی
✅
تسویه درب منزل
✅
لینک ورود به کانال تلگرامی فروشگاه
👇
📱
https://t.me/beheshtbaneh2021
📱
https://t.me/beheshtbaneh2021
✅
مشاوره کامل خرید تلفنی خانم ها فلاحی
👇
😮
😬
09188806440
🥳
😬
09182643758
✅
مشاوره حرفه ای در پی وی
👇
👇
✅
@banehonline2025
✅
@ORGINAL3758</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661382" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661381">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiliHeGd1JZMG4e95eBA_Kz3Ont4Fahq-BfmKHYKSqGV7IVoNBmc4fgXBbXXRRsaWVes9QCTWb5F3s9D1rRfR2CpSk8UBmDLYLY31r571f0m8MZT_v96vcywg8tQaX86DbIEWLyLAdllczgu89F9mbPGjhBbUI8wrV_bZ2HbZOWUXqQ2QcjMkEPPl8EV8KhYWkQcIrZa16qtB3GVb88qDRmwqrCbKkEUbSbmCvdE8CXZZJPBzhpFZu787UjOF0m9jWkOtwGOeGQ_fn-mmxO-aXdv_cDzglfezspdCnoGf1fvthD_7bVvZHYFpE64ObLtjEApIwa4Zj4pKa4KePGXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس روز ناسا
🔹
ناسا در بخش «عکس روز نجومی» خود تصویری خیره‌کننده از پدیده اختفای سیاره زهره توسط ماه منتشر کرده است؛ رویدادی آسمانی که در آن زهره برای مدتی پشت قرص ماه پنهان شد و سپس از لبه روشن آن دوباره ظاهر شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661381" target="_blank">📅 12:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661380">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e74710a9.mp4?token=Z-vkxLpwC8FPDUG4k6xQt9h-lCeASNp-WXkwU0OKrU1iZmIP5XakZEgtfmd6XhaYJgzEDTxsFXq6vsf8ZApuR6XMj8FmVN7_f0ltgQ0t36p9Cn9UCgouXf2Ud93bUYq_dihVDAfLgBi1Q14WO5tY6oH1mLZZn9oEI1PZatNRu5ptcI5kOT5hXyABm4Sigi2Ko3VBH2cdK-MAxOGCTud9V8LK69bYr1wqsYmNabo2uaRF-jqFz5g9CN6YmyHP0-95PDbAuicQ3p-sOBg8vc2MlRYTLLSyafnceWFT3VNK7wudK6lAvJJbkUIn_XL9YpdQyXAiX_eUYqs2RrREPgfwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e74710a9.mp4?token=Z-vkxLpwC8FPDUG4k6xQt9h-lCeASNp-WXkwU0OKrU1iZmIP5XakZEgtfmd6XhaYJgzEDTxsFXq6vsf8ZApuR6XMj8FmVN7_f0ltgQ0t36p9Cn9UCgouXf2Ud93bUYq_dihVDAfLgBi1Q14WO5tY6oH1mLZZn9oEI1PZatNRu5ptcI5kOT5hXyABm4Sigi2Ko3VBH2cdK-MAxOGCTud9V8LK69bYr1wqsYmNabo2uaRF-jqFz5g9CN6YmyHP0-95PDbAuicQ3p-sOBg8vc2MlRYTLLSyafnceWFT3VNK7wudK6lAvJJbkUIn_XL9YpdQyXAiX_eUYqs2RrREPgfwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات موزون بازیکنان و سرمربی در رختکن مکزیک بعد صعود به مرحله حذفی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661380" target="_blank">📅 12:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661378">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b20f033d.mp4?token=UAJQayd0VJWHOcdkzF12kyJQQjh1fKYlxh7CrnWIlVMMEhQodafAAIui4WSQ5yySr5Ko3YScVnoRD9lCOiP5kOPzhIVqb6H_pYdXsRppW6XYFixFiJ022NWuLNq-h_0enw46sNep-lOuSTDZXN4wLXtJTlhHNAjBsRZhEUuc-jtVOfhwrsknwXeq727biNgmvE05ESrO7FDJ7CLuSguhR_gGcCjsxtL2wB9WU5ouFIYmNNfo1c4efL9od34lqaXgFhYPVI1Cwe8qqnxJ7BEGKNlicnuPqCDgBMOtB3ysvSas9r07xhpJn6rXbGbvu6un4yfR5FjsG5vESBPyEkZGVHYYgtgsefKiYIuuTibBrZaAG3KlhwGJcnF-obu73QNpizUvN0_groPEJ8AiONXgCfnOPkWHq-3Kpjvr46EyYgMbeDxRq3hatKeS0-VzBzyjR3eq3aFaetr9VWp4gSZSHVRCMYHNVcZLoMLJWkDFyWfDRJB7kO0Y203U1vRsca0sFVZ8anqvgsPKYFQ-15W5ssAOs4QW0s3mbc5YH4jF9xWeyQprxlA2rAt8E4dqUWo4FQJeDd_1wS65UlqE9SVAEt0wNvKdmusafhuPFNHGLNKt5qAJ2E2uMzkT9AYpWyG_hUYkhVmA5eCbg3T3lFhcJNoys82ufh22vvzydX-qNPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b20f033d.mp4?token=UAJQayd0VJWHOcdkzF12kyJQQjh1fKYlxh7CrnWIlVMMEhQodafAAIui4WSQ5yySr5Ko3YScVnoRD9lCOiP5kOPzhIVqb6H_pYdXsRppW6XYFixFiJ022NWuLNq-h_0enw46sNep-lOuSTDZXN4wLXtJTlhHNAjBsRZhEUuc-jtVOfhwrsknwXeq727biNgmvE05ESrO7FDJ7CLuSguhR_gGcCjsxtL2wB9WU5ouFIYmNNfo1c4efL9od34lqaXgFhYPVI1Cwe8qqnxJ7BEGKNlicnuPqCDgBMOtB3ysvSas9r07xhpJn6rXbGbvu6un4yfR5FjsG5vESBPyEkZGVHYYgtgsefKiYIuuTibBrZaAG3KlhwGJcnF-obu73QNpizUvN0_groPEJ8AiONXgCfnOPkWHq-3Kpjvr46EyYgMbeDxRq3hatKeS0-VzBzyjR3eq3aFaetr9VWp4gSZSHVRCMYHNVcZLoMLJWkDFyWfDRJB7kO0Y203U1vRsca0sFVZ8anqvgsPKYFQ-15W5ssAOs4QW0s3mbc5YH4jF9xWeyQprxlA2rAt8E4dqUWo4FQJeDd_1wS65UlqE9SVAEt0wNvKdmusafhuPFNHGLNKt5qAJ2E2uMzkT9AYpWyG_hUYkhVmA5eCbg3T3lFhcJNoys82ufh22vvzydX-qNPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از جنگ روسیه و اوکراین چه‌خبر؟
خلاصه آخرین تحولات جنگ بین روسیه و اوکراین
🔹
آخرین تحولات جنگ بین روسیه و اوکراین از صبح ۱۹ ژوئن
برای دیدن کامل ویدیو کلیک کنید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/661378" target="_blank">📅 12:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661376">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
تغییر ناگهانی در هیئت مدیره خلیج فارس/محمود امین نژاد جایگزین ایلکا شد
یک رسانه اقتصادی مدعی شد:
🔹
در اقدامی عجیب ، شنیده ها حکایت از آن دارد، محمود امین نژاد جایگزین ایلکا شد.
🔹
دلیل این جابجایی های ناگهانی هنوز مشخص نیست و باید منتظر نتیجه بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/661376" target="_blank">📅 12:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661375">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5860865c54.mp4?token=AnlmznI0Yr9dqz1gOwoTF-_aeZ5UpwITJ2sJI3U9kTSkz_ipTuKyk2W19lgdFCNAJuBBKPEuUQVTfGr-ssHmG3FqjXgt5cWKBPhO54TTNMJGs04Pn6Wmr2X4mFfUIu_3M858l4HqRzbr_hSObfGzMv0jBf6G3b9rfZMQqPp3ngLhLSmHLtJ7BKJFjCDxOZ-b1uh2z_4TEj6pQ3PtfqVK0ReDI9Em3uMHnj0BL2sIIZoIPqRtOiYwUHWVFd9D6WnpMqfirYTohBRMH2ulOOs85lQbZUDOIifHVEux4E-SIAXZKQacG4mdxIms6aqUFzdstYq1VEQWfSf4rK7bx9n0rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5860865c54.mp4?token=AnlmznI0Yr9dqz1gOwoTF-_aeZ5UpwITJ2sJI3U9kTSkz_ipTuKyk2W19lgdFCNAJuBBKPEuUQVTfGr-ssHmG3FqjXgt5cWKBPhO54TTNMJGs04Pn6Wmr2X4mFfUIu_3M858l4HqRzbr_hSObfGzMv0jBf6G3b9rfZMQqPp3ngLhLSmHLtJ7BKJFjCDxOZ-b1uh2z_4TEj6pQ3PtfqVK0ReDI9Em3uMHnj0BL2sIIZoIPqRtOiYwUHWVFd9D6WnpMqfirYTohBRMH2ulOOs85lQbZUDOIifHVEux4E-SIAXZKQacG4mdxIms6aqUFzdstYq1VEQWfSf4rK7bx9n0rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از صعود آمریکا و مکزیک تا حذف ترکیه و خط و نشون کورتوآ برای تیم ملی
▪️
قسمت ششم برنامه جام تایم
#جام_۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/661375" target="_blank">📅 12:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661363">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeNdfeU8wVwEe867-qNPerWwW80G-kiyjRsFKFfOvq4rbbVqRD7FfFtQcAZgUx2emNJc1QUhY1fgjV1BprTWd6Ln5XTQpjYqNXOCecsDP5IuinJDFWEQMqoCJ-q-Ab_WEoCovYpahM2HhZcQy8phYViKiEwOUMSYOyPQ_4sTd_t-m999bX_3yGY0Fu61iSavWerXPeI5G2PZdgKEryd8FwcY_Xfh0SaT_m4J7FqlDW3onT68iHMSKynzkWAFIwCPPT3nSXIi53KKpjKSH9gBYbic11a_TF1oOMu3M2_2vz0tedm5wqrb2wYAS_HNeKRf8SXlKfVGLDKT8C1p0zVGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArvyBZUf3W_NHB9kdCNkSIPBW4-TgVXgv3tW6zXMhuHPwXhfYGV1OoNMR_yHVqo7SFl2RIbyASMt1OqjwWzuVN3xkMiEP3XPSqy5MkhJcvl0i5loFYULdQeEw81K6fn5sz_m0tMVOlC6F3nAwe4Lt2qIpMyLtIlViNhdrPGxtTcQDfSONlA88B3ouOfkXBqs0Y3NoLjDsVv07Qz6ftI7n8ZDMCx2NFX_wI9vvyMgxFGU5bewBbdcxUYxidBPfzw3NQj-itakQN8NPGn3YCnsir9qC5F5y58F1EGUjBzHUpsrK0Vx4frIh5okZSLdAkqVt-pMy2MOupADUQNfqlTHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NscBnIPA-rkHsOXYnntHo0I9SI0r-gWwkqQ0EiT2tZjTYGq1Lrc4O6zkU9hszbsmDjtOSHnclbxQiOuPZmubP-OfsNvcGJ4EnBeD69jPaMj7vWK5FUzls4WrDAGIsku2Gy-0rGF43hZIL9V8k3IIpF5BcY4RoaQENw2ue9bPxCUtPFy86lmW6byxj5SqiX5a0MzatxKhCyhRH5A-b4o7k5uzRKw7LTih5Jho5pt1IZLTALhxTVD_YZXn5tRrcEJcbXzxytrXMgJHu2nWZ5V6o7MHDhJ40wp48gaeAG_0BT2KzgrdVH48SGddWeHREDkp1q5h1x2JE1M9_bAy6jSUCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFRVEvm7EUUN9kOhC_mEzClrGRFxphxFt7elALj59ttMX9JeZxq0oMMe5FtUBLZUmieILzlaWNpLDrQQIwpxj6UFac3FKl5J0GHsarbDFcrnOeZJNmS-ooqW70jXvSZwTONy6PdZHEGiPg28E5csV9Ch_nVYVx22YZWKGjHvHOkHaC8uYUoPsiyX7PTHRRqlA8_LDAK1nqPOrzhDoLzwCv7VbY4Z_Zkl38__ElRqGXRG66LFhvQQKfjm70AQKzAzmyLg9CoXZ9-TmDiHRTt_8wddvlAtufI6phBaC_oF5hgVfLXdE4eLsvrosZHhz9O-sWd55al_j2cp2ZiXwD5DTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyOXE3L7DaxBiTgQfG8PUnyMwyhXqeCKdocGnD06DY_Z_DPSLwXhmjQhOSnskb_8jQPng035-N5Gj_KAahJKkZ5oJzt32E75oI60HKmBq4SNodzHuWg88DTipg0rqC7JX9bhb-xW4zm7qDZNeBX8DOqUfJyuveu3qg2eNUVbWAJ6T4FcUqmFkcceVrjzxuT_MgmDwvSZVZs-DlXMfllWVdqZcygP-wR3Bf9BRz5NZIqfDqHkx5pQAn0FNJKQdN6pBYUjkT4XmtAlxLzVR85TwslNBD3vpjtK0cv90LKPBF8icNbdREFqfv-p0Xb5vjMXicdxe1SIUxyNOcdkETn_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFMkCIjwWX5ifIMdIExuC7VNtamwIYiUjg6GsYwYKfuEwaJvxYz6oeDkTBbPF7GYeUi8CCqmRqmeX53RqL9B1FAKiD7O-qwW_v0_oZcjdlQKHQY6RgEPgAZCfyvitrAxJrMwEheiZpnprwRaCWVDtu1xsFdAfEF0ERk0BjuwshyU6KEo811sbneLd19kIn92Ksy21YxntnJz7q4NtSJftE7P6QTjLsEXgA4Mp-_5zQFDqfOPubKEUOuuwG6jj3pKBvYNUJ5H_LK5gLBDZDiRNaoi3jBPlKpUeK__xvex0HEqMi_CqcdYA3owGPNgaLgOsv4sbQDbUKsmnL9J3eJp0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXO73YKX8S2R3PfqJeQWauJ9Y8gLYFfL0ND7e5R3wyreLvLLZ7OBmNLmUyokqCnPzFDljB6qk8xv41_W6f6O-0roLIyVauxmAUDGqa9xZPpRmLqjzyFsL5CiUPFPsbre-phiX_w8Qll8lAJnSYWPKTTtvTIHxGibFRT3bRRBETdHvL1rEyUu8xMgOQ2IaaTyf4m8MWoUeoRR01ItBbHSRz2cXTNwSZ-XuZtIQdwhRNwiAJsQxxemiQNWRGpHVNJI-s79yslMgovjB-WOhPiWipsC6mVoZGFrh2TKBh-SNIhvCP2aSKEAweuXWXCFUwec-EbrZB2Ah46SzUUZz55g9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFGCXsYbBnntiOn0CZUMpd2CTxSXtW9H9Z2gu6WsBBKGWxq94z58m512Nue4KKK1YGGOMOpRkq9sCSdAT2zxMYfyEY1M2QHv6DxnkNLOBg1rZr3V6BWlJE_86ym9h19xyDCoBhqS7EduS2FkSydxRkFjHcM15tko_vOttyhIkWnMCNNs36Hmu6fYu3PceRJTfem0S77xfB1XDcTkuCffcCsfrfCi8039TAHaAnNu9bTZTlWhh_VlPF7wLSeAWCPvBeAmlaBk-IkD-b2y1yCXszcAxCfbxq9FcXHoMXE22qOZWRPkj-OxnjoMKfd4YVvdS0hvcktIl4OWlvlbDMDfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jT1gBoEwk1Z4w_4H-ewUZh_T-x1IzOcS1divYK_bxQ0tF72nEZzsR4ll02_bq4KaEP4I_oBAAzc8LP8ySKQHNY4wsGB4cMwk4R5r71DIRuRzdR_aRnc3H0o3xTkSfTNPooSgxRmdHJESOxV68Xhi_I3tfM-abOTgbiCiDM33fn9Ua7YmyF5bDV_iyMb7NKKa1QFhTN9il2IQhQq1Y32XVDsDQHTI8NA2mNc5BKsIxY_tY7Za4FG_lpWWRuB_BoymxC4l2M5uCGcoKuVCbMrvYYuzKn4lYRY7qUeULWmYZopaNB5TPzQgbz78k-SYjkWy9-tbM0gIVijneAOMniQKdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcc_6tcIxt-lC871ZTOJS_wtfVybtNGq3m_SH6W-KtSIakKE-sOY8YZUXQ2rFEnFVxzA_crMv5M_ML8BBSxoCBbyRiTCQWYGbUQ0Th5Ax1QxZX3x0g0bLgWC2VmBffDUs8PjIbEZlajaIliDy9TT1Z0ri8oEvkUEQIySg0_u25o0sNfGa1mz9EZum_mejleKmWYR0H9skZYJZanVB_sixvxqfL4zt00AEKzgBDkEIQzS0VyqYs6-A4AkrcjDIbmBhKeus-2iZ69lS1bdtRdeZsoToRefJeaBLgWsvpkhunw3N9czDxg2V8GuXcyFGuKZ6JCyIiSJV1yNYbqsVvG3rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیرخوارگان حسینی
🔹
بخشی از تصاویر ارسالی مخاطبان خبرفوری در پویش بزرگ شیرخوارگان حسینی.
🔸
الوفوری را دنبال کنید
👇
#ایران_حسینی
@Alo_fori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/661363" target="_blank">📅 12:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661362">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPhSJO9hO1--58k2WrEfxhlq9XiiJrZvn0wL2hS70ca6_5e7xOLCun3yWVdUqjcwT26wMJ8yAP3Dy_lbMivs6rl6V6fFX0xqBJkiai2lmewqK89KMousZH5iA5-PYEvbzsunxAV8tw-N6el88o6e6PE74cAkK14xt3AuRLKv0H-bG6p-pBcHAsXs5VWnOjxo7DkB5edfcHiwHPS_SVEZVb19OwDOX0UTJmh41UBbvgsmmsGUs6KqbMAuDVJorz33AkHy1qm-_KByEhrtBQgkRUUbahXITKtp-do6QLRNBnBUJgDKNm8M3K3h2dtEMitGpiChnXEViVXff1YgyaaCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
گرفتگی عضلات داور آلمانی، بازی آمریکا و استرالیا را ۲ دقیقه متوقف کرد
🔹
داور ۴۵ ساله آلمانی، فلیکس تسوایر، در دقیقه ۹۳ نیمه دوم، هنگام اعلام خطا ناگهان به دلیل گرفتگی شدید عضلات پا بر روی زمین افتاد. این صحنه که در آستانه سوت پایان بازی رخ داد، باعث توقف حدود دو دقیقه‌ای مسابقه شد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/661362" target="_blank">📅 12:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661360">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM-q4NZpTyi4KUaRtCY_qta0jRLqb3wzvRu0qtyF_hrU35erVp4xpJjg9Nq5kL4DCXZDnj4IswE97AOY5jX_vsaVIxRThXMw5qZTGPHOKpjtaHHF8_7ylcJjBNtc4TqarwuwspX1TyVuRsd4bJxSE6hXzd3e71YifrerPOJQCg9JpVowDFOVrGpMO_9LgkAUJTxgqOxWUnP9sUGq1p1nkew0kSP-2lxdun3HmDbf_tHRm5JAwJFnCgjoYsmnJkhHeLpuLpA9YwkRj-RWHjsN8ly4-6Hv3J1KWBTBiRaW0xe6jCAtvLgi1W0aFV_QByGIHJM3y6W_SCTj8hB1a5nzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر کنایه‌آمیز حزب‌الله از آتش‌سوزی یک تانک مرکاوا
🔹
حزب‌الله با انتشار تصویر آتش‌سوزی یک تانک مرکاوا در بلندی علی الطاهر به شعار لشکر ۴۰۱ زرهی ارتش اسرائیل اشاره کرد: «نیروی زرهی پیروز است»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/661360" target="_blank">📅 12:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661359">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f66a56e223.mp4?token=NdBU1TiKdt028jJZVJHmE4-JMRMYjzSulDKAytlkAbP4KMsaupXpWgqVmXLopVFEfOkVjC8FZjYxM5DejLGzgRkqSL13xRiAWA7eveAXfKl9yzPjCpZO0dquP7lqDplzomQYns6_rs0G8MnAVRpwz3ljGbrw7oamvGd0XOKicgS5gbxFdbVYSlAiFmnjwpyIqqR31SDk2gT0hvo2PmDSmhie4gTklWS9TIaqUxPq5eKDSGlyNdvWekVWCwQUkUvJVpgFoYjz3TC51WzEwz_sC8G7pUy-K-mWFHPTC1BqVYvY61cy9hQuzsq9LlW7q1f3VkUxq9c_m5azdsRO_uSkNamjJc-cyRsZJpL2MgErNlOsoEvepVZANALGT0MskU-jp-w9fbDuv2hsTYynHSQ1_0T6r_3n-b9gRB2gJwvqllg9hN8cX-92JHOyDciUOEr6kXHbnKGawGpx3dUEFmIV6KuXGX_Xh4YhIn211pT4PZ-PluxsK1ZXqDP0g1eDQ3pVipRCTAwLsBPL-avDh7cFP9RWLqX9EPevzDXbmsfcrsKcqjZEeHV_DIVSxN3n3nKlnnRU7gkucaA9t6zdbto8-MrnoYMR7t_6PbqEJF48XMDKVYd2Qshlu61bfKlf_G4jiG-1kONWNdGttdRUC3XGRHx4Z3M_tnWfqNGRbwahzYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f66a56e223.mp4?token=NdBU1TiKdt028jJZVJHmE4-JMRMYjzSulDKAytlkAbP4KMsaupXpWgqVmXLopVFEfOkVjC8FZjYxM5DejLGzgRkqSL13xRiAWA7eveAXfKl9yzPjCpZO0dquP7lqDplzomQYns6_rs0G8MnAVRpwz3ljGbrw7oamvGd0XOKicgS5gbxFdbVYSlAiFmnjwpyIqqR31SDk2gT0hvo2PmDSmhie4gTklWS9TIaqUxPq5eKDSGlyNdvWekVWCwQUkUvJVpgFoYjz3TC51WzEwz_sC8G7pUy-K-mWFHPTC1BqVYvY61cy9hQuzsq9LlW7q1f3VkUxq9c_m5azdsRO_uSkNamjJc-cyRsZJpL2MgErNlOsoEvepVZANALGT0MskU-jp-w9fbDuv2hsTYynHSQ1_0T6r_3n-b9gRB2gJwvqllg9hN8cX-92JHOyDciUOEr6kXHbnKGawGpx3dUEFmIV6KuXGX_Xh4YhIn211pT4PZ-PluxsK1ZXqDP0g1eDQ3pVipRCTAwLsBPL-avDh7cFP9RWLqX9EPevzDXbmsfcrsKcqjZEeHV_DIVSxN3n3nKlnnRU7gkucaA9t6zdbto8-MrnoYMR7t_6PbqEJF48XMDKVYd2Qshlu61bfKlf_G4jiG-1kONWNdGttdRUC3XGRHx4Z3M_tnWfqNGRbwahzYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صهیونیست‌ها می‌خواستند پسرم را با پرچم ایران بکشند!
🔹
پزشکی که برای حمایت از تیم ملی از لس آنجلس امریکا اومده تیخوانا مکزیک آمده، در گفتگو با خبرفوری می‌گوید: سخت‌ترین زمان عمرم آن چند ساعتی بود که در جنگ دوازده روزه منتظر پاسخ دادن ایران بودم!
خبرهای جام‌جهانی را اینجا هر لحظه دنبال کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661359" target="_blank">📅 12:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661358">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSkZ3xf4fwVnWSjYrEn0tf2NGB_ecbCrXBnWtjsESZln-r7nIL3jcz5tTZgqBReNIRkst01NlPBx-EK8eBDlTwdGi9HNwojNn9mgdQebfIs9U_89CBWgAlWBLH5FKtTB0hX4xJ5hfc0NlSsvViLbUFVkFDbNrNM8tgF--HAu6ZyC-ta6T0b8_t-uBKbtbkfIEM6udSZMNyBdzfVK1P6GtQLk0e5dh3BS-4oqW_WdzrU18cg0Nl6N7tVe3lF2_HxbGM7oEnk-JK5SFl3fgTsa3RP21B9orBqsXGkH3laLBm12P5Vw37XoY2ebhJT8vZg1aTJZOsUgAm4Uh3xbX1giRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۸ نکتۀ مهم پیام رهبر معظم انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661358" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661357">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4df5454c51.mp4?token=sQ6g2qwtIBmbAPXGAmcC4dJbgE_pR_2YQHODfrk6pqWxU6d18rWhwzSTz2X6Gd-n7IysxLbPsSdZ81RwfHBSUP3mTGGcbQjoW9yskUBaLTmzpdDaBvMsNvKwHRFcqg3RjMpGjWJHvMfWuAub021f3ByTw50dBp4OBhDXzLTjkT4Z6qL_9cTo-RyFdzxx-2CDCKIC7Cckb-YxaD7NgRr-m_lxdqkqoWXwcG_tIE6nSFx1nAHr04iX_O2B1Rp-eWc1GLcVvNr7_RXXBFm0CkNNMy_ZFOV5Cf7zbtnMl1OLscYzApmPfzgnKy7tjX8oYewXNK10-U7N199xsbp7h5OvdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4df5454c51.mp4?token=sQ6g2qwtIBmbAPXGAmcC4dJbgE_pR_2YQHODfrk6pqWxU6d18rWhwzSTz2X6Gd-n7IysxLbPsSdZ81RwfHBSUP3mTGGcbQjoW9yskUBaLTmzpdDaBvMsNvKwHRFcqg3RjMpGjWJHvMfWuAub021f3ByTw50dBp4OBhDXzLTjkT4Z6qL_9cTo-RyFdzxx-2CDCKIC7Cckb-YxaD7NgRr-m_lxdqkqoWXwcG_tIE6nSFx1nAHr04iX_O2B1Rp-eWc1GLcVvNr7_RXXBFm0CkNNMy_ZFOV5Cf7zbtnMl1OLscYzApmPfzgnKy7tjX8oYewXNK10-U7N199xsbp7h5OvdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ با استفاده از تروریسم کلامی به دنبال چیست؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/661357" target="_blank">📅 12:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661355">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b0e42be7.mp4?token=unkEsiUSQsBJfeQsAOeaCr50vGirSFMbB8o6CuPOH-U6KqYk50_hOa8O6lpUK5VlkThGBTgLffFe7JNs99IysFHjWlVwwZ1PWOsivhBz0gEWnD-IFkd_XwY30sNARdJSh5NjqP5hfjjoGDdycotDjj1uZZ6DGcIGM3GTmDxDz8SHvkMA728gnu3coUvPeWJbxaov9UDcPDq0qHxi8o9NkSAM54IistgWj1p3wtcDOZhIXwW7bad-OPGSAxCdAISnBGb3Su1KaJ5pzDH1vYioFgFZVMWmc7-DoXY6iClB4uGnFltpHL4uO0SswWVb5HF4i4DOOzebcCwIqeLZJy5Nkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b0e42be7.mp4?token=unkEsiUSQsBJfeQsAOeaCr50vGirSFMbB8o6CuPOH-U6KqYk50_hOa8O6lpUK5VlkThGBTgLffFe7JNs99IysFHjWlVwwZ1PWOsivhBz0gEWnD-IFkd_XwY30sNARdJSh5NjqP5hfjjoGDdycotDjj1uZZ6DGcIGM3GTmDxDz8SHvkMA728gnu3coUvPeWJbxaov9UDcPDq0qHxi8o9NkSAM54IistgWj1p3wtcDOZhIXwW7bad-OPGSAxCdAISnBGb3Su1KaJ5pzDH1vYioFgFZVMWmc7-DoXY6iClB4uGnFltpHL4uO0SswWVb5HF4i4DOOzebcCwIqeLZJy5Nkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات هم اکنون اسرائیل به جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/661355" target="_blank">📅 12:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661353">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
آموزش و پرورش: ثبت‌نام دانش‌آموزان هفتمی در مدارس نمونه‌دولتی براساس محدوده جغرافیایی انجام شود
🔹
اخذ شهریه ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/661353" target="_blank">📅 12:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661352">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
وزیر کشور پاکستان عازم تهران شد
🔹
سناتور سیدمحسن رضا نقوی وزیر کشور پاکستان برای دیدار با مسئولان بلندپایه ایرانی لحظاتی قبل عازم‌ تهران شده است.
🔹
وزیر کشور پاکستان پیشبرد مذاکرات بین ایران و آمریکا را در تهران پیگیری خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/661352" target="_blank">📅 11:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661351">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3a7754df.mp4?token=kvabYfPRcHiKWHmdK7RXp-wQiJanOGlzGIehD5jMr_NRWvmobB5wugS377qFiugWcaXxJ0IgmSLb-33vwQBztmZHgCUwaZPxicMqq2u_D8gTQFXAhNrmCLKXx3Q3gy1n2BoaoviU2TzHHyTEzFrL8K_9bz_fF5oow_93zZ0L3Lt7_vSWQgy0bLgfSLaPUOELoAFTWC8fGOuF4_IgVE9Cj5WTFkA5gioFlmfnZHXcXAg48RCGS80g2sutAmkwz-32Ld5Mtv5xJp32-G_65T5XjJ1FZuuA6JDMjLLloFTq6HXC07A9nF6AC0-Yc3tItExyUZC1fT45qw6qxi2tyeFGx4RkrwlEUx1-01uwTTgD7VURZ2UCj7OR0lmZfJxC8eHIaB8NzF_szVYtyBx0lS0-h4H0soLSkBQk9Cmr2qIDGZF2gkPJfiG44ImsKzONORQwWUGmAdZJvtoyPF0Hb182IiN8ABqopevKbYzPVGiwnQFBvcU6D1-d5u4hJoND1gOuMNoFvpLCiCGBb42OgiQvAd89UluiQ_jemNGR5FsgQNbfXZ_zSVAqfH3mEzgqrwoKxzZh26UChfGPWEE7E-pDo0xWLdqkG1_bxuufwXvwopv-lAZgWYiX_s2neaNPOgbl8EKh-xANxfrHatyzDc0X6c3pk3UpHVMIUSivxQ1iPJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3a7754df.mp4?token=kvabYfPRcHiKWHmdK7RXp-wQiJanOGlzGIehD5jMr_NRWvmobB5wugS377qFiugWcaXxJ0IgmSLb-33vwQBztmZHgCUwaZPxicMqq2u_D8gTQFXAhNrmCLKXx3Q3gy1n2BoaoviU2TzHHyTEzFrL8K_9bz_fF5oow_93zZ0L3Lt7_vSWQgy0bLgfSLaPUOELoAFTWC8fGOuF4_IgVE9Cj5WTFkA5gioFlmfnZHXcXAg48RCGS80g2sutAmkwz-32Ld5Mtv5xJp32-G_65T5XjJ1FZuuA6JDMjLLloFTq6HXC07A9nF6AC0-Yc3tItExyUZC1fT45qw6qxi2tyeFGx4RkrwlEUx1-01uwTTgD7VURZ2UCj7OR0lmZfJxC8eHIaB8NzF_szVYtyBx0lS0-h4H0soLSkBQk9Cmr2qIDGZF2gkPJfiG44ImsKzONORQwWUGmAdZJvtoyPF0Hb182IiN8ABqopevKbYzPVGiwnQFBvcU6D1-d5u4hJoND1gOuMNoFvpLCiCGBb42OgiQvAd89UluiQ_jemNGR5FsgQNbfXZ_zSVAqfH3mEzgqrwoKxzZh26UChfGPWEE7E-pDo0xWLdqkG1_bxuufwXvwopv-lAZgWYiX_s2neaNPOgbl8EKh-xANxfrHatyzDc0X6c3pk3UpHVMIUSivxQ1iPJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاصه بازی هائیتی و برزیل
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661351" target="_blank">📅 11:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661350">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e94943171.mp4?token=T6f4Kg5-3zvrZstwatSInIbrVn7QFGWJQvZD3YKsyn2sbwvg15xty5xZXmol6oPsC8hSrpMil58MtSYcd8eeSz7hFwDOgZDg3wKWrxNzMe1DF4zJ5EGcsX4yZ8ADUMUCu8FKxufRz2UJIxMROSoL7X1z_wXvJ9bMkuKBoy1LenZ1w683zIeJThkrVWPbz5PWvC9YKO-vMeppEzXgMkDXUB-gAcDMN8jIHuT0dO-LbwtMhKm6gcweB4qPOx1PttBksnNHmV_pXnzc4jRA-fyn2jC0jybmXk1g5dazfwGcFd67DXW-gZ7x83_XUuXzoZVU1_gX3Vvdv-lOUPMqfDuUkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e94943171.mp4?token=T6f4Kg5-3zvrZstwatSInIbrVn7QFGWJQvZD3YKsyn2sbwvg15xty5xZXmol6oPsC8hSrpMil58MtSYcd8eeSz7hFwDOgZDg3wKWrxNzMe1DF4zJ5EGcsX4yZ8ADUMUCu8FKxufRz2UJIxMROSoL7X1z_wXvJ9bMkuKBoy1LenZ1w683zIeJThkrVWPbz5PWvC9YKO-vMeppEzXgMkDXUB-gAcDMN8jIHuT0dO-LbwtMhKm6gcweB4qPOx1PttBksnNHmV_pXnzc4jRA-fyn2jC0jybmXk1g5dazfwGcFd67DXW-gZ7x83_XUuXzoZVU1_gX3Vvdv-lOUPMqfDuUkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زباله‌ها در هلند چطور زیر زمین جمع‌آوری می‌شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661350" target="_blank">📅 11:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661348">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
یک جفت لاستیک موتورسیکلت ۴ میلیون تومان / نگهداری سی جی ۱۲۵ هم سخت شد!
🔹
قیمت لاستیک موتورسیکلت به حدود ۲ میلیون تومان برای هر حلقه رسیده و برای یک جفت حدود ۴ میلیون تومان هزینه دارد.
🔹
این در حالی است که ۱۰ سال پیش قیمت هر لاستیک حدود ۴۰ تا ۷۰ هزار تومان بوده و حالا نسبت به درآمدها هم فشار زیادی ایجاد کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661348" target="_blank">📅 11:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661347">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcJfF7-c5Clwlzvtx0XPPb7eLv5IqccrPn9fry_OxK2waBq-Q3D5ixbS8ny0DkRJPqGwvS8U9Vk754mzKPCe262sw5oEqawzjbBDdgMUN5EG_EHhMM3EAIINSt2f3Z2-EzD95uICtfHU93TBFuuT_2raH3FOqimBNcjWZ2I5IW1nP6ZmkY3k76XqzAZe7riWrqpIfAN4_2YtqwICkXeIsgtvofQ1oSBf5hmVzZVr59lKlW4sfTgkfZn32eZ23P1zr0rHepRVhs2scytwaumKd2Xga0UyCgg7zRWD0RsMRuH1ApIAxpbhfu4vYl3prbsl8hF4ehSgCBEaeXCSZD4f8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661347" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661345">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrNB-Y-nvcnTuv2p_SYN_iWCN-34ClaQ6QMFKl4lJMa-zUEXKywfnyFiNN2vKXPuHI0K7YMPuqiS37idedDMAreW2J3hbNsN8QK8o9Hx0HvA43MY6fz-NEbbtNz0lsLxz8-rRJFBhRDBoxIO8lVM3mw4XTDENF2u0bU9V2bpP9m72MDY7PHXh9-DS-VCfES4XDRcfALVZlCiFBWlSxCwD31XtZM44OZNVEEVEOjBbrGO6tUZvKUNj9VdToiNbFrqqNdFRxMVYT4i0vkM3gnVRMtbtiZ4FND4oSQ9tWEP4YQgw2ZE0yXMlpRAiHySjrLZj8CE0YBmGud2M_m0kdgoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک تنظیم مخفی که می‌تونه گوشی‌ات رو نجات بده، قبل از اینکه دزد گوشیت رو خاموش کنه، این قابلیت رو فعال کن! #نبض_تکنولوژی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/661345" target="_blank">📅 11:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661340">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6aecc6ee.mp4?token=PGilxfiGkYD-18xfb3s6ICCzd6RUdLAeUexOXdElNAzGKLgTkmUQYt3tohThRrPrLGmxNDqu7pAhEmTY3aiiT5lu53W21d1kh7gPZe7kJcifwniufC2y37Gvcf6izuUFy79NRj_e3gkWqxakaQR3TBe1AW4oXGsJslOHPScZmozBjBznwxv5ELzHuaACuVPsxT7n0gji7FI9VSfsN0G9EdxvtVw9r8UwTdxN4tGUf5LYjqfj6DaUcDZF6aUVHn0Q_yTfHqPiXRb9EOMsafDhOQjlfG03pzNjRSORQFCt1BHicwZ42yjDSdVOe79ZQ6Rp3aiirKUOIgu_Q0yVrfrCow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6aecc6ee.mp4?token=PGilxfiGkYD-18xfb3s6ICCzd6RUdLAeUexOXdElNAzGKLgTkmUQYt3tohThRrPrLGmxNDqu7pAhEmTY3aiiT5lu53W21d1kh7gPZe7kJcifwniufC2y37Gvcf6izuUFy79NRj_e3gkWqxakaQR3TBe1AW4oXGsJslOHPScZmozBjBznwxv5ELzHuaACuVPsxT7n0gji7FI9VSfsN0G9EdxvtVw9r8UwTdxN4tGUf5LYjqfj6DaUcDZF6aUVHn0Q_yTfHqPiXRb9EOMsafDhOQjlfG03pzNjRSORQFCt1BHicwZ42yjDSdVOe79ZQ6Rp3aiirKUOIgu_Q0yVrfrCow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ شهید در حمله اسرائیل به شهرک باریس در جنوب لبنان
🔹
منابع خبری لبنان گزارش دادند که در حمله هوایی رژیم صهیونیستی به شهرک باریس در جنوب لبنان ۴ نفر به شهادت رسیدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/661340" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661339">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: همه شرکت کنندگان در مراسم تشییع و تدفین رهبر شهید در شهرهای تهران، مشهد و قم تحت پوشش بیمه رایگان قرار می‌گیرند
علی زینی‌وند:
🔹
همچنین همه جاماندگان از مراسم اربعین که در مسیر حرم مطهر حضرت عبدالعظیم حسنی علیه السلام خواهند بود شامل بیمه رایگان خواهند بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/661339" target="_blank">📅 11:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661338">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtdwUCUlScYDj9jmX7ZjtX8mMulZL6NQR_Hm82ZYMM1td-qrC01guz68XMBwOGpayutpVif29_AEBUDK-hvQ86VTSpoYrKZj9uMf9gIx85oEiRiGpok_zhfI5oE0m06V5Bta_NYqB8_MBVBOe2_INnmTAzKhJiBgmCjYP--LiQduA_6xzCUiVvOmRsV11lGdtGRe3HmxcYacQXe1asXBfmoEzaMJP3Q6Zk8CXTJNGCdQ3Xr7DQyz_yEAb0gxCoHVsrfBSsc9LqTX-mU46KNeqnxjsFrvsVk39sbIrLvvGxlMWHoxLDbBx7p0mgGkoy3FiHo93BSlR2uvZ1XesXCgLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم سالاری در آینه اعتماد
یادداشت محسن بیگلربیگی در روزنامه اعتماد
در راستای پیام مقام معظم رهبری
آنجا که رهبر انقلاب با وجود داشتن دیدگاه یا نظر متفاوت، به تعهد رئیس‌جمهور در پاسداری از حقوق ملت ایران اعتماد می‌کنند و مسئولیت تصمیم را به دولت واگذار می‌نمایند، یکی از ارزشمندترین صحنه‌های بلوغ سیاسی و حکمرانی در جمهوری اسلامی به نمایش گذاشته می‌شود. این رفتار نشان می‌دهد که مردم‌سالاری دینی نه یک شعار، بلکه سازوکاری عملی برای پیوند میان رأی مردم، مسئولیت مدیران و نظارت و هدایت کلان نظام است.
اعتماد، سرمایه‌ای است که به آسانی به دست نمی‌آید. همان‌گونه که رئیس‌جمهور در برابر ملت مسئول است، این اعتماد نیز مسئولیتی مضاعف بر دوش دولت قرار می‌دهد تا در همه تصمیمات، منافع ملی را بر هر ملاحظه دیگری ترجیح دهد و پاسخگوی نتایج عملکرد خود باشد. در چنین شرایطی، مردم نیز با مشاهده این پیوند میان اعتماد و مسئولیت، احساس می‌کنند رأی آنان در عالی‌ترین سطوح تصمیم‌گیری کشور اثرگذار و محترم شمرده می‌شود.
امروز بیش از هر زمان دیگری کشور نیازمند تقویت همین سرمایه اجتماعی است. سرمایه‌ای که از تعامل سازنده، اعتماد متقابل و مسئولیت‌پذیری شکل می‌گیرد و می‌تواند پشتوانه عبور از دشواری‌ها و چالش‌های پیش رو باشد. اقتدار ایران تنها در توان نظامی یا ظرفیت‌های اقتصادی خلاصه نمی‌شود؛ بخشی مهم از این اقتدار از اعتماد میان مردم و حاکمیت و میان ارکان مختلف نظام سرچشمه می‌گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/661338" target="_blank">📅 11:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661337">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: کنکور سراسری ۱۴۰۵ در ۲۹ و ۳۰ مرداد برگزار می‌شود و زمان آن تغییر نمی‌کند
🔹
نتایج نهایی کنکور احتمالاً در
نیمه اول آبان
یا
نیمه اول آذر
اعلام خواهد شد.
🔹
برای
آسیب‌دیدگان جنگ
نیز سهمیه‌ای در نظر گرفته شده که پس از بررسی نهایی به تصویب خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/661337" target="_blank">📅 11:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661334">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJzPQmDFQ_emlav0OCuzZ3_p_zQHH2NsOllyj4YNkv-9lkWxuD5gvjDrkuIn42cpVn-m2p_VdILMv_DfxOF65lBHhAiCBMmDGYLvd6rbpiV1H5YLkMHH5RLgNVf91nAzb5AIDeXgFCbNUGdtDTxnH7PKX2yl6zLicQABpUJjniCvRmA_mTs-OpdIUcfSQPbp9FNbB56O9b7dS1NMpl84Mt_mPnWO924BxfFv0cDcIlsQ2reQ6v74hWLxKIxl8YOzWsJcTqyMGfLxIpQ1dLTgAm244BNkU0TxnkUfCFniU5mzLUnyWnjhvRHIliQMM0FBC_VZ5Vtbgfa4pqiBDjAYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم برتری شبکه سه در تجربه تماشای فوتبال در ایران
🔸
در این نظرسنجی بیش از ۳۶ هزار نفر شرکت کردند که سهم روبیکا ۴۴٪، سهم بله حدود ۳۱٪ و تلگرام ۲۵٪ بوده است.
🔸
بیش از ۷۱٪ شرکت‌کنندگان مسابقات جام جهانی را از طریق شبکه سه صداوسیما پیگیری می‌کنند.
🔸
شبکه سه صداوسیما همچنان نقش غالب در پخش و جذب مخاطب برای رویدادهای بزرگ ورزشی دارد و جایگاه پررنگی را در تجربه جمعی تماشای جام جهانی حفظ کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/661334" target="_blank">📅 11:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661332">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
وزیر کشور پاکستان عازم تهران شد
🔹
سناتور سیدمحسن رضا نقوی وزیر کشور پاکستان برای دیدار با مسئولان بلندپایه ایرانی لحظاتی قبل عازم‌ تهران شده است.
🔹
وزیر کشور پاکستان پیشبرد مذاکرات بین ایران و آمریکا را در تهران پیگیری خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/661332" target="_blank">📅 11:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661331">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f067281ed7.mp4?token=q2hq0JKmWMUDX3dmazg5PXqlEERlfV1SACEvtNcmx5eT6qogt-rjGhgf0uSrS3IU28JVPjyKYV4p-Wb1zIvUA6At_focjyGtj9WFlIMNG8-cwBCjtlXxyMu0yDR1dOvR1THUrMSDyRS7dEuagS2ASEiHuiEV9xDVdzevddaNLFfDHXbHeCCskaUhhEUi15-_jiSM_BY5brPyzA4tZye8f-oJiXylxt2g16QYiPPWkJzZ8-wO8PPbvfZuMV__qUtUgCEnJH3jdA7vxvr4d8HlZDsCtqcrr33VsyQil1O_tL08q9PgAmX9QD38gEvsYNinapX9KgjtvAIBRTqNFOXgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f067281ed7.mp4?token=q2hq0JKmWMUDX3dmazg5PXqlEERlfV1SACEvtNcmx5eT6qogt-rjGhgf0uSrS3IU28JVPjyKYV4p-Wb1zIvUA6At_focjyGtj9WFlIMNG8-cwBCjtlXxyMu0yDR1dOvR1THUrMSDyRS7dEuagS2ASEiHuiEV9xDVdzevddaNLFfDHXbHeCCskaUhhEUi15-_jiSM_BY5brPyzA4tZye8f-oJiXylxt2g16QYiPPWkJzZ8-wO8PPbvfZuMV__qUtUgCEnJH3jdA7vxvr4d8HlZDsCtqcrr33VsyQil1O_tL08q9PgAmX9QD38gEvsYNinapX9KgjtvAIBRTqNFOXgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور:
برچسب تندرو زدن به منتقدین تفاهم را قبول نداریم/ طبیعی است مذاکره و تفاهم مخالف و موافق داشته باشد/ جنگ و صلح دست رهبری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/661331" target="_blank">📅 11:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661330">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
وزیر کشور پاکستان عازم تهران شد
🔹
سناتور سیدمحسن رضا نقوی وزیر کشور پاکستان برای دیدار با مسئولان بلندپایه ایرانی لحظاتی قبل عازم‌ تهران شده است.
🔹
وزیر کشور پاکستان پیشبرد مذاکرات بین ایران و آمریکا را در تهران پیگیری خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/661330" target="_blank">📅 11:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661329">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxVIeADjhdcKE1pjgWQAvkDJYEhUGuM3aGh5VS-yKVGi9zVXqvs_EEZgP9Tyk33AqjuNoKqpmv3cjdTKeEdCbHrk8dqlXzjQdwLCBRtWqcWEdVR1f_HtCvn9Uc5TT_6xn0KuHIy4q4geojuQVWf1c6ScLygunyUBH_4PjXJweURMp6kcpmh8g-oxvWMZAcurrloXmn7NuJdn6uRt-yxMU7uqnFNeZLOrP3nlvpVf_l9I3BwOOeqXnJonPDRNGYT29MbGFkGHLe4SE3CrSknsX3WK8izIekZU5cKrjurcjoG_SlIXxwDaFAf3q4uHmcqgr6ayVZIP0neN4Vu0wpPv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
فقط تا
شنبه ۳۰  خرداد ماه
فرصت دارید
❗️
اگه بیمه شخص ثالث خودروی شما منقضی شده، الان بهترین زمان برای تمدیده
👇
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود! فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید
✔️
تا ۲ میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
#بخشودگی
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/661329" target="_blank">📅 11:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661328">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
بانک مرکزی: ارقام و درصدهای مطرح‌شده درباره افزایش یا کاهش نرخ سود سپرده یا تسهیلات بانکی، اعم از افزایش یک‌باره یا مرحله‌ای، در برخی رسانه ها مورد تأیید بانک مرکزی نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/661328" target="_blank">📅 10:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661325">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOqQQ8iNCnNH44bnMIvI7Oq93NnsVz9kireU_r-5IWpx3IFdPPRbk_9qxwwK_Wkcqm4hYoX9Il3h9pb46FBlsB01-pgkoPqH-GlaO47FHRbtXnwgINyjCff5fNAliucNAfRaC5HOsd6Y0futTM-7HZzUTLjoBe1JljZQaJtGIoyxwRCMiVpRdgI0mbOw5dzPu6UMUgO48Nwf-ZzGLcvBZe-MFaq9HVe7SQ7dYml0AqrFRxvzqVWPbJdWYrkQgP6KRuUxJAxo90i48zd33s7BqyD8-rAmzAWO4p-NtpaDBCk9nOie6qxi7LMybZcP831HTDkI7zDmiJgxjyns1qlQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موج افزایش دما از امروز آغاز می‌شود
🔹
بررسی نقشه‌های هواشناسی نشان می‌دهد از امروز شنبه، دمای هوا در بسیاری از مناطق کشور روند افزایشی به خود خواهد گرفت. این افزایش دما به‌صورت تدریجی و پلکانی ادامه یافته و در روزهای اول و دوم تیرماه بیش از پیش محسوس خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/661325" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661324">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
دارایی‌های مسدود شده ایران کجاست و چقدر است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/661324" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661323">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ_gsFWruar_pmXJs1iy-p_23EA3BpHzqkd5c_4ujBdrHGWuyzJfgU5RTYQqo4ij2Z6q8u8Q0P0cVN6tBv19pyOMT2sKlviQasjU5lXX1HWk9IIdHM76QDLQntDYxH-VaWTglMMavUbOYTQlw0zPp1iX1nlGLWkEWkFdtctWKK_RR6bzPLHNoAYPOG6DreAgo5HOaB6zIwyVkgm1boXL2n-L5tNZefCbQJNoSnt2781heOIIiuEi-3ttodFax55FJayHw8LbD0yfmDytcYczKVN-vzHAORSIN-P7XupH2FRoK-X6pyFPPJwRb_5lRALrAEV8GsO3nbTIVXJMJKAjiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت  طلا و سکه هم اکنون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/661323" target="_blank">📅 10:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661321">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546bc2bcd6.mp4?token=UbdW944YNIDbE4wM_a4d1NVnUmMPUEodTjg0NAgyKirMJ24IBd7mddySIqc3kqZQkzIPMJbm6ofZXIC-_a6ItBVrKEUMKOZa8HdVSo5pMu_6ZD72G75ttuLX3Ss3hTqw3BAH2Fap2WTmI5ZDVKG-e-X1kBth1QnkFSOv35tTQchyJOnjo0N-mpZYuqGE-WYmbHIXGoNwntV4l-Y5w5y_f0hd5QyvbB3EZVXjYbgWaBVHH6V8vcP4-xoq5bfs8QAEQpSJ9hOkSBOamosmABzw_mZyQH_7AuWhLD5wDRT7B_kbOJCE8ytJ5fgwt6CGsvvFqfuGC32r-cuhpemn2qVEOqDoyKyPdSu1x98CokHOvCd5iu6mAi9oI3Im0EtlIlwWGxc6iGBbg7U76fHr6wcwB2XtPkD-dDkc0vgxxHLLYABdnVmh7Z2_h7f5cd59EW4HMMsdBrc9z_JpfgDCE5kMXNu8LWMe2Y344W5AtGvBDvhHop6zy6HBw4kGQ99sRRgq_OAZLjceeNHeFNWLv1HH9HnGk_svQZ4rLKb0x4qRC1-w03QsToLBk8OOCJeWLFb-z1KTutvCqT-rVwOUG_99MdMCwSdAFt3KNB59r9_6akqeBbyWF7xN888_wbooiNrTX8il-u-ofwabSQfFOKwIsQYzWheoH8kjCcFHiq82mO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546bc2bcd6.mp4?token=UbdW944YNIDbE4wM_a4d1NVnUmMPUEodTjg0NAgyKirMJ24IBd7mddySIqc3kqZQkzIPMJbm6ofZXIC-_a6ItBVrKEUMKOZa8HdVSo5pMu_6ZD72G75ttuLX3Ss3hTqw3BAH2Fap2WTmI5ZDVKG-e-X1kBth1QnkFSOv35tTQchyJOnjo0N-mpZYuqGE-WYmbHIXGoNwntV4l-Y5w5y_f0hd5QyvbB3EZVXjYbgWaBVHH6V8vcP4-xoq5bfs8QAEQpSJ9hOkSBOamosmABzw_mZyQH_7AuWhLD5wDRT7B_kbOJCE8ytJ5fgwt6CGsvvFqfuGC32r-cuhpemn2qVEOqDoyKyPdSu1x98CokHOvCd5iu6mAi9oI3Im0EtlIlwWGxc6iGBbg7U76fHr6wcwB2XtPkD-dDkc0vgxxHLLYABdnVmh7Z2_h7f5cd59EW4HMMsdBrc9z_JpfgDCE5kMXNu8LWMe2Y344W5AtGvBDvhHop6zy6HBw4kGQ99sRRgq_OAZLjceeNHeFNWLv1HH9HnGk_svQZ4rLKb0x4qRC1-w03QsToLBk8OOCJeWLFb-z1KTutvCqT-rVwOUG_99MdMCwSdAFt3KNB59r9_6akqeBbyWF7xN888_wbooiNrTX8il-u-ofwabSQfFOKwIsQYzWheoH8kjCcFHiq82mO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دوربین‌های مداربسته از لحظات اولیه حمله به نزدیکی بیمارستان سوانح سوختگی شهید مطهری در جنگ رمضان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/661321" target="_blank">📅 10:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661319">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
استارلینک رسماً وارد عراق شد
!
🔹
دولت عراق به‌طور رسمی مجوز فعالیت استارلینک را صادر کرد تا سرویس اینترنت ماهواره‌ای اسپیس‌ایکس بتواند خدمات خود را در این کشور ارائه دهد.
🔹
مقام‌های عراقی این تصمیم را گامی مهم برای توسعه زیرساخت دیجیتال، گسترش اینترنت پرسرعت و پوشش مناطق محروم و دورافتاده عنوان کرده‌اند؛ مناطقی که هنوز دسترسی مناسبی به شبکه‌های ثابت و فیبر نوری ندارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/661319" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661317">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9388f2d36a.mp4?token=lUCw1fXVE9iaPb0rTTFpt2mhVZT16S71b4auGEYM4lgeK-4VAJQRB81kTDFO7lZWBYizp9aQwlRvWLk4k26hXxvKqrbzkIxkoeqlE-KwO1eFPIPavpVOiBjz6BoAw9Ja-0J8Vaam5CJTTd8UYWGKbK3FmVpWFJd1lwwziHQXvLW9mjZB2_mCWIw2YRB0DoGg3O2b1KCmN_LDVc360IG3L-JvzXMmacA6IQhGzlzuOaqYLrU1oIRJz5YG4L5uzzjwSX3KyEpRKcDSYR6UdKSRqdOJNqIm_GOIW4K387j7MFpgMKiXa-TluTy0QIkjC3yBLqmq-IDltw25qHZW69V1Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9388f2d36a.mp4?token=lUCw1fXVE9iaPb0rTTFpt2mhVZT16S71b4auGEYM4lgeK-4VAJQRB81kTDFO7lZWBYizp9aQwlRvWLk4k26hXxvKqrbzkIxkoeqlE-KwO1eFPIPavpVOiBjz6BoAw9Ja-0J8Vaam5CJTTd8UYWGKbK3FmVpWFJd1lwwziHQXvLW9mjZB2_mCWIw2YRB0DoGg3O2b1KCmN_LDVc360IG3L-JvzXMmacA6IQhGzlzuOaqYLrU1oIRJz5YG4L5uzzjwSX3KyEpRKcDSYR6UdKSRqdOJNqIm_GOIW4K387j7MFpgMKiXa-TluTy0QIkjC3yBLqmq-IDltw25qHZW69V1Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا فصل گیلاسه این دسر فرانسوی رو از دست نده
🍰
چیا میخوایم؟
🔹
گیلاس حدود ۴۰۰ گرم
🔹
تخم مرغ ۴ عدد
🔹
آرد سفید نصف لیوان
🔹
شیر نصف لیوان
🔹
خامه نصف لیوان
🔹
شکر یک لیوان
🔹
وانیل یک ق چ‌
🔹
بیکینگ پودر یک ق چ
🔹
کره برای چرب کردن کف ظرف به مقدار لازم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/661317" target="_blank">📅 10:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661315">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e5bf166b.mp4?token=YkFPyLntNNkT8EM8PIVzY3EU2IYfKh--mcFtklnSQGrQoyB0jBISVTGaFDxLklUI30YmKY2wn2UHzqd2aTdHOav5QPiQFiNGa8CaYf5qvJ5CFA_LxFuaowRv0Lq-e5FW4eEeA4Le8a3lzkbs9u8DIxrneYiRIGhKtGZpsZ05zYiwYYjwgW_qP1XHOoK-362MSRCjlvtu038R89xhfuC5c-11CyKPZjSf8eJwM4Qm_jhq2Ew2qW3Jnm2Yl0gesaanqWT_2s2WAO-5ckG18lTprpUWPjMFj3Jt5nnn_D3T5Hi9vAldQkKJgdK1waB_PLetGY6bHHqmLfSu8TAp2Ey82JJ-WEgyF0rwbJmZD6yk2C4rGfQfRmjGwq6GhreqkZ2pCAOI_yzEylQGj3xER4NCgoWsXGYpqYhbPi6pONm_HLUPS4V0MHCAAy0ZWQz_uOCAOz9pYw5dwte0rNNQrsPFwz82JDsUOeylq9lg7ZvuqMV8jdoIzv1Csj0Hgyo4YMKIZZM2qK7NInF_tUqovJksr5P_hHraWqRZv8mnSEyOUJWRMcc_E1fn9BKjK41zi8zIZh8irO4BT4gUdz4YOkBwTSy8E-5dciGTiUj5BYefV0Odnp74xJsfSu2L8QlHA5fCk1opHzfp22yxvRgilHuEY2umqrIwBvhUemmvevOoHD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e5bf166b.mp4?token=YkFPyLntNNkT8EM8PIVzY3EU2IYfKh--mcFtklnSQGrQoyB0jBISVTGaFDxLklUI30YmKY2wn2UHzqd2aTdHOav5QPiQFiNGa8CaYf5qvJ5CFA_LxFuaowRv0Lq-e5FW4eEeA4Le8a3lzkbs9u8DIxrneYiRIGhKtGZpsZ05zYiwYYjwgW_qP1XHOoK-362MSRCjlvtu038R89xhfuC5c-11CyKPZjSf8eJwM4Qm_jhq2Ew2qW3Jnm2Yl0gesaanqWT_2s2WAO-5ckG18lTprpUWPjMFj3Jt5nnn_D3T5Hi9vAldQkKJgdK1waB_PLetGY6bHHqmLfSu8TAp2Ey82JJ-WEgyF0rwbJmZD6yk2C4rGfQfRmjGwq6GhreqkZ2pCAOI_yzEylQGj3xER4NCgoWsXGYpqYhbPi6pONm_HLUPS4V0MHCAAy0ZWQz_uOCAOz9pYw5dwte0rNNQrsPFwz82JDsUOeylq9lg7ZvuqMV8jdoIzv1Csj0Hgyo4YMKIZZM2qK7NInF_tUqovJksr5P_hHraWqRZv8mnSEyOUJWRMcc_E1fn9BKjK41zi8zIZh8irO4BT4gUdz4YOkBwTSy8E-5dciGTiUj5BYefV0Odnp74xJsfSu2L8QlHA5fCk1opHzfp22yxvRgilHuEY2umqrIwBvhUemmvevOoHD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس یادگاری مکزیکی حامی فلسطین با پرچم ایران و لباس تیم ملی
خبرهای جام‌جهانی را اینجا هر لحظه دنبال کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/661315" target="_blank">📅 10:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661312">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmvqS9n9ykTI9ZI-k27WcHtiwzd6MmHqyedqiWKN7A7wbfcfgsyYW0vt6BJRc-frBTFiRsZM4wO69HDZ1NE9mIuSvv4JHgauJ7sThTPGTeOlh0b8jiq1YKOWmwOWldQCwJk13bvBMhl6AC7oxmKdgQOWBeHJV1z7ViIL_1zis_YjgxGXrxWOUUU-38Jk9bo8fdTzTbgUYIY-muBpW5V_65k1ZltH7eaHlyJINQnPxTQAmP6AW_ln0OweG0NPkqCvkxOL-IvY3j57r2BxxmWl2g0ZRaekJywr4gLx0YghMP8246iuXSyb6qquFeyo-pf2vYx6KXwOOx7RlrA0GlHtwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاکر کارلسون، روزنامه‌نگار امریکایی: ترامپ فهمیده است برای موفقیت توافق با ایران باید نتانیاهو و اسرائیل را تضعیف کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/661312" target="_blank">📅 10:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
وزیر کشور پاکستان عازم تهران شد
🔹
سناتور سیدمحسن رضا نقوی وزیر کشور پاکستان برای دیدار با مسئولان بلندپایه ایرانی لحظاتی قبل عازم‌ تهران شده است.
🔹
وزیر کشور پاکستان پیشبرد مذاکرات بین ایران و آمریکا را در تهران پیگیری خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/661311" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661309">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvrIA12Xvv9r-NIf9eYVKN2a6m7e3V73D7VtfLo09SJGhmBGHr1xvRmbstl8FFsdCyc3yPa5KGxx8Ri4cRjhWB_nWMAIjg46dya939IcyIJ4FQ-1MY2I48brOjm0yuvpZkFtClnlvonHAz2P-FbCEAC69VlSUo46sbY-mToHjfM-xIKBJNmbS4jnti_TBdw7FzRyv5b8NKGb-tu7VlArk4jQdLgXg6899Y1d417XXCqVgR5WXbpzOuETWQW-XWQKMwkUl6RZfwZ4gsGQdF-WN532WER0qgVJVpAQxOH7SAqSBgmQRU9WdNUqRHDpx3vps3-W5ZgdKLL9ssRwCc_h2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دارایی‌های مسدود شده ایران کجاست و چقدر است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/661309" target="_blank">📅 10:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661307">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bdcc6dd0.mp4?token=vzCFFeRWLJFOrb34wrwrP8gNNDPRDC9aq2V7KebNyOpaoivex4l5hDA_oFLtuPz9i4Il77BXU05VxKKu4apMQULRTvAan8Cv120Eu1YAGwhKQNnJzpqP3aZ-mBMBi-ieffjLpDevKFbaRjtrU83tKkjAFIC5f3jdF8QP5YR4xcpV3LA3I0qmG5eGtEgbKYgYIXRWeG-6Qqtod52vUmBHdOU822UrlVMFDb3UfB6Er75oBr1dIFa_beqNgxI-Wn3o6D5BMt3yQwTnE38TaXrrocHOFdchk8LpVXxcP_YqvQzw7PH0aGewTaa98djdMbxXwPBUzVVjz-yIpKhdf-wWGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bdcc6dd0.mp4?token=vzCFFeRWLJFOrb34wrwrP8gNNDPRDC9aq2V7KebNyOpaoivex4l5hDA_oFLtuPz9i4Il77BXU05VxKKu4apMQULRTvAan8Cv120Eu1YAGwhKQNnJzpqP3aZ-mBMBi-ieffjLpDevKFbaRjtrU83tKkjAFIC5f3jdF8QP5YR4xcpV3LA3I0qmG5eGtEgbKYgYIXRWeG-6Qqtod52vUmBHdOU822UrlVMFDb3UfB6Er75oBr1dIFa_beqNgxI-Wn3o6D5BMt3yQwTnE38TaXrrocHOFdchk8LpVXxcP_YqvQzw7PH0aGewTaa98djdMbxXwPBUzVVjz-yIpKhdf-wWGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی بیش از حد فکر می‌کنی، فقط ذهنت خسته نمی‌شه؛ بدنت هم هزینه می‌ده‌ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/661307" target="_blank">📅 10:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661306">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
سیاوش قمیشی در سفرها با خودش قرآن می‌برد
امیر قمیشی، تهیه‌کننده و برنامه‌ساز تلویزیون:
🔹
با وجود اختلاف‌نظرهای سیاسی، سیاوش قمیشی به عقاید او احترام می‌گذارد و پس از شنیدن خبر فوت برادرش فقط گریه کرد.
🔹
به گفته همسر سیاوش قمیشی، او در هر سفر، قرآنی به یادگار مانده از مادرش را همراه خود می‌برد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/661306" target="_blank">📅 09:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661301">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeYZkFSWFMRT3Q3s9e-D6C9EdrNrxwSuBRqMtXwYV2XkNxBd3Vg_m7dlg4V3N0HKgl7qWAcucrT3O_2P6jQCxKLZnPrn4Mc9cqmPiE7DXvr2qIyRKmPTuHH7qQIcJgZYDhaBfbWnXdeySROu3Uq8G-o55tqkwxcjx-S11pJkhf4sFRr98tgQWqkJl1xhauYqjrqvki1vgzj2GomlYv-MtDfqWuHfKVheaGvyxFK3eRXWjy0TgNafw7nCop_vDL9VJ7SXnbiMiCXbThBCwJnURrDMN1DoTzcq7VoXPo4wktHKCSoSD1Bpohla0hVartmWAX4dCUq6P8MojYLzwvnVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKsuuix8mDRIQdByQCo3-eM95dITDFLdc6kdDccdz0igps8C_jprkC602QD1HOTJ3Z5y9p9x06L-FkHemXjjqOCR8l2Pzj2aPoxvHpMul5fDN-YCWHUCDLGnTeOV4K3I_DKXqK_ibY8DTCd0qDmjZqCVpHdSQDzh6nNPLSiIRnLSxf7cIirR1XVGfXTQow4kpKZ6h3k-VKHlQStAn7SQ0PmRzHux5Q1GaEPFjlCyjINDD_cnPKOMU-iaQurnD0TZaPUJk5VlVXRwVE0OL6IjW4eVPmZA1H4FamqrdbfjNT5Hb0IfRIQWACcJ8gN1_uXwT7OwjyvUPsp93HUzTNkuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwtGCTw3UewiYsTuLKrIBTfM8pfSMjKDJiBkiNwVO7BpzKjaxi29z1ikNtCDHhPdERSC3SnBI7nbVLrcwwwZXABGxKU6AZWprcTLL-sqxsJSzfoUzGzOxu5ixdxbwjxMPUrs-IG9YgDayZkthAYWNQy4bG0eeR7vj4yTwRzGftGO09gFBAfi1N5e45f6rhAA4BRxFJoPWkcBFrTtimaPT0xPEF8sGfZhV92dYVgrC4MNN3GUqxRU-FHjs2dYUZUxCKvZ2g_LzF1lqf3-lzXVwamIz0fvUFhKdBzGbTQ4wjlOMf3C1gM-e4j5nKoqh1NV9X-RqUSf0C3gwi53f1O36A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از بمباران‌های وحشیانه و پیاپی رژیم صهیونیستی در جنوب لبنان از صبح امروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/661301" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661300">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
تصویر منتشر شده توسط کانال دوازده رژیم صهیونیستی از حمله این رژیم به شهر کفار رومان در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/661300" target="_blank">📅 09:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661299">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_RAFIx25JJl9a4UPQPjVu_YwaeZ5rll0S_9nVv8fJq3RJo3tLoImH_vNAKFKinlkiqBuB4VXzBsK-OfXK9aQiAQcBrvevVnWD_pPTbcWSWGtpkQtzJIjbzO8wiY8pmrlnpep9HOn4XYJaYMK0Tr6DvumHdjuIEjBYa9jLsuxe1kBc03IP9hq6B54U4un-ACUai3PblN4qvzrTb4LEybRp69_XGLm6sy7D1rZUOO39JL35yxysCsL6fptOm62RTGY7x0Ezh9MeZcrmzRNDVwyZUDisi3cA8ZS21g0rD30R87Ca7V9hLyEDf1Qrfe9lGHvGgIwRxpjBR93UyNxrrL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با تصمیم مدیران پرسپولیس، قرار است دراگان اسکوچیچ جانشین اوسمار روی نیمکت سرخپوشان پایتخت شود
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/661299" target="_blank">📅 09:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661298">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJkvi-vaocKrFjjW9ZGZlFzDYxu6cbvTTMO73upw0T8LA2ET5f02A9AysydyozjZJfFcrWslZyWfwQg33Bxp-uiJIf5gP8Xv2u6UZWnUtSmYO3552htEEzCDA5AYXAnDnIxfYgSbRdocqDn8F9eOl4S3MDfh7AWx4pfV30MF0JqsqOsyUby1hu4lZef0TllwbAu9cjVhdb9EHsok50z3iz5mHKFcmVe95E4O7whyRs6GpnRK0eCe5KwZ8iz6LSuxzx5beXKVlcQ_wBYEFcNePCj4j5T60TlYPXhASejgXQAK49CkSE_U5RBPNTPmw3sKKyb1be5unc7b52JIckmskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از حملات هوایی رژیم صهیونیستی به شهر نبطیه و شهرک نبطیه فوقا در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/661298" target="_blank">📅 09:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661296">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
شکایت ایران به فیفا از محدودیت‌های سفر در جام جهانی  فدراسیون فوتبال ایران:
🔹
درخواست ورود تیم ملی به آمریکا دو روز قبل از بازی با بلژیک از سوی میزبان پذیرفته نشده و این موضوع روند آماده‌سازی تیم را مختل کرده است؛ به همین دلیل ایران به فیفا شکایت کرده است.…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/661296" target="_blank">📅 09:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661291">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1dhDCvfmfN2xutTLGY10zpU9VW6xI-MH-g-VoyOPHELGERqFThJbKnDos_rEmwVxKQWFG4kULsawKIVZLeVtT9khBVKc4eCQD7ojKuQLs4NusZdyFOLbgEEoUbP7B1oBCUcCLox7dKl5R5wM5L5DsS3JWbC3IgyIGPbiEalEgNz7xjWcBXx2XMOtHYNrUQ-uK5EpHF2xikWvlB205gA8-PbZISlMNrfrAFLEzu3fRM4laLaG9-19f2ZQiWpZd8kiIyPu11NbH4tjTEHK9LHBQsytCWqmVhenOI9G4StvBQkPDi6cSsO1dgE0yagf6oCXdDMPI0WtVdGYDwmfmTATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tgwv39In_nQ1q2YEoBxvLhzC76lytgdf97GJ2z3WYeN3inKwkr9B4GbNI6v6teL2krbbQCS6-_KtS6e3L9rrSEPA7qOyY-GNulnYzQzqi4NybGftpH_VVZSiId5t1IgXFWu_tJSkSmnK0qTp4OL_sAAl6hzKNa_VZUrSJyXe0oF4V8wg1Rr8g1-CsQAHZc1MByGwSDTrLN6BEmq7Ug3lVgwsYJzA6G9OQunaogEjaBpl6YtVNRVP-YKaGkq06lzUktB6c3qLZI6v6Mx7LbOnPTpYtzbRygbcYwQvZO69_jUtJxsUuymYjk2sWWJGgdbILBfw5H7b7KxnFNKP7jW5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkTX34mnewgRMWKdXHjT3YlyrhGHIfamreVQsaxCpMmBKwRCQlXkrXhSez4roObky8i2khUzje0C2-hlw8j890iBALJEpPI-NMmto-l48yO0z5N7K82QlKoJa1uzsnuikCPyHvpp9l-WoJyVqxvRCjXrKf6D9ZE9XdJvqr_XICrNhwkt3c4ABnmKy08V7Nb9D5_d0kNgyLO8NAW7_hJ72RhSTMLQ_kR06vgeCX0QtTmBjrtYVkj6E7tLgQ1a-Yw8fkTpK93cCXm3Vluu2pTHpm2jd8xj2aAuHtEHqn83JmA_Kiz8100PZDn5p_D3cnSCl1VLxGTktS_g7FQSGW1vUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خبرگزاری رویترز به نقل از خبرگزاری لبنان (NNA): جنگنده‌ها و پهپادهای رژیم صهیونیستی از شب گذشته تا صبح امروز حملاتی را در منطقه النبطیه انجام دادند و ساختمان‌های مسکونی و خانه‌ها را ویران کردند، در حالی که توپخانه اسرائیل قبل از سپیده دم النبطیه و حومه…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/661291" target="_blank">📅 09:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661290">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaDj9T6ibSFqlxd0rvGayLk8zSx1AoUmnO0gqv_iv_jgfOGJVg-D9KlDOPPWQApN8dqiEuUPv4o9XJ0YofvjdpuQnMhQmZVKepe5Ft-kTpIsgmk8TqVVefpcI-1t1kQamPf_dvu87hJhylpENBuurYq10GSH0BSQ-RfmWZVNOk1aYEiFvBC7mxpMvakY46joGMTf9PruBd0ebS-_WB3RPkK1dY7zBQooNKQyfsu-NJOYJnPyLOS1NkEaTobbrqBos-zH0phXpTbl5bjtdRBgJ1R_nau0ktgpqD-qr2WYL5J7HqfZWrsGskDte5RI5tfG4V83WzlMdt5SmBDrVREF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس تهران ۸۹ هزار واحد مثبت شد و به تراز ۵ میلیون و ۲۴۰ هزار واحد صعود کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/661290" target="_blank">📅 09:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661287">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
خبرگزاری رویترز به نقل از خبرگزاری لبنان (NNA): جنگنده‌ها و پهپادهای رژیم صهیونیستی از شب گذشته تا صبح امروز حملاتی را در منطقه النبطیه انجام دادند و ساختمان‌های مسکونی و خانه‌ها را ویران کردند، در حالی که توپخانه اسرائیل قبل از سپیده دم النبطیه و حومه آن را بمباران کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/661287" target="_blank">📅 09:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661286">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_eyKrKZWIDTLW_Lscs_hd6PqZPNpZGv3QZBHjEVWW7yxjg-vRxtpxqevHA3nvhdOlJciRJAsdpTcWTqAxrOrsOCfL1pkG_DnXelKr76oHvWEbpA40L1UDtGEA4-xO0Y-SYD9ZgrXir2QEab1yFowrlx3iuu3-1oBr3kfQyTUj0un0fN-w9eFDAM3D8sH0GioHY9ZcArr03JWM6VQ1zIs2nT1zthR-cZo5obOBgUOYvrqL77jBTKnvkXrz_Q_zP0gd635l1KXH3O4tgQPZZq5qaoMP-zT5JE5WYkN6SuHNEP4n0rEZbKQL5b4atE2xJ91RAO2SbZXnTzYdwE73npqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس: آمریکا همچنان اراده‌ای بر جلب اعتماد ملت ایران ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/661286" target="_blank">📅 09:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661285">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
قائم‌پناه: دارایی‌های بلوکه‌شده ایران به صورت کامل و تدریجی آزاد می‌شود
معاون اجرایی رئیس‌جمهور:
🔹
۲۵ میلیارد دلار از دارایی‌های بلوکه شده ایران به صورت کامل و البته تدریجی آزاد خواهد شد و از آن به عنوان منبعی برای توسعه زیرساخت‌ها استفاده خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/661285" target="_blank">📅 09:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661283">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920b1127f5.mp4?token=v8_O7SaRAONGl_5oqfp74Pc1ikUNNOvQhdEeF7aPah3HZQ-gvwYUYwN78q3SHVCCq7qZPW7EY88UVx46TxuUWFBf_LeAj1KZSS0806XCy_cTJcrEjEtWBxOVfEpIcSnE7jn-Zr1RNQGqR0hDt28psj6mvZgevenmiUppuSdRs0jLmOMT-3XLXkFsNs0LuQcd5NJ4KQGEm9C1FUrLGD-g4u7Rkx5j19rFTPXTu1tDyKGQDTjUxf0_AxeTJCxi0BtDuwTRmFdqOShOzO43UdcXfIVtup3p7b2KZk6fpcqObiW9A8gn7YZ-BA5iHQNhYXUqB-b4mkaRV7JFf9zoFgCb6Bk3Wli2n4GBEUhes17rGhW_AMmFCwzqpe5ALBavLLTHv3yRAjhHv4Nu5g40tcns4HkGVWetXVtoexM84eahieVunDFVUzPAdoCM4rZrq6gj0dFl6vWKmGghuU3Q-fKnfViqU3AIwpQkFzV-JU9l4JugTljlg8C-S0zN6d6Sg1ZCpI7pu89sGA6jnVFbXbdsW5f0frtKzp9VNNWsG-CNEECKCsch89P2MnPeHYu0pE1GjuVFoAq43DZvkvvGbeBeN_nrzBxD4P4ka2RNCBjy2yY_QoXwLxe3GC3imyNMZiLGDkVqsTMY4VMY7uB-PX3yScO-kq7OX_yb9qCS1hc6WR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920b1127f5.mp4?token=v8_O7SaRAONGl_5oqfp74Pc1ikUNNOvQhdEeF7aPah3HZQ-gvwYUYwN78q3SHVCCq7qZPW7EY88UVx46TxuUWFBf_LeAj1KZSS0806XCy_cTJcrEjEtWBxOVfEpIcSnE7jn-Zr1RNQGqR0hDt28psj6mvZgevenmiUppuSdRs0jLmOMT-3XLXkFsNs0LuQcd5NJ4KQGEm9C1FUrLGD-g4u7Rkx5j19rFTPXTu1tDyKGQDTjUxf0_AxeTJCxi0BtDuwTRmFdqOShOzO43UdcXfIVtup3p7b2KZk6fpcqObiW9A8gn7YZ-BA5iHQNhYXUqB-b4mkaRV7JFf9zoFgCb6Bk3Wli2n4GBEUhes17rGhW_AMmFCwzqpe5ALBavLLTHv3yRAjhHv4Nu5g40tcns4HkGVWetXVtoexM84eahieVunDFVUzPAdoCM4rZrq6gj0dFl6vWKmGghuU3Q-fKnfViqU3AIwpQkFzV-JU9l4JugTljlg8C-S0zN6d6Sg1ZCpI7pu89sGA6jnVFbXbdsW5f0frtKzp9VNNWsG-CNEECKCsch89P2MnPeHYu0pE1GjuVFoAq43DZvkvvGbeBeN_nrzBxD4P4ka2RNCBjy2yY_QoXwLxe3GC3imyNMZiLGDkVqsTMY4VMY7uB-PX3yScO-kq7OX_yb9qCS1hc6WR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوت کوزه‌گری برای پخت یک کوکوسبزی مجلسی و بی‌نظیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/661283" target="_blank">📅 08:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661281">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rl8ceEXXEnbkGdYrwekMhnV18uUqnUt2AjsvNaWezpzjaf9xlRTuifdOLJbvbGoLeK1qMzAGvDuf1WCBOt9F4iivcA29-r460FNUDsWz4eh0w07fDk5NaVUNvbJ3ppRzP9shvyp5sHKqoDV8tcUPdNVa4yygRP0pxgio8n7_e3XvpN3wVBr_I2mWxVU1WZVVoWBPBuSSCFObNMk7gS5fi1MedF-zbAI5sNpl5-yTSSqlh_Co3hRs50aFPFSVKvi5032rZJBEO7FGfzXjcNoL8jXgkBSKydvzukQtLnnobKjCC9-5GWqJkaSn9TeuBWvIsJIOZNdZgumuta1Pj9xHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاجعه بزرگ؛ سقوط یک امپراتوری!
🔹
سکانس پایانی امروز - حذف شوکه‌کننده ترکیه
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/661281" target="_blank">📅 08:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661280">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ab59f856.mp4?token=vicVtPCdxnzV1qNj17hvfc3nGhP_LKcrTA0Pek62VRI6I2f-N2GUZNhhBaOX2QXhiwC-BnnVcik3eDw-wcINnvNwnMRmec6nMl-wE3kXuITR5dsd_2jlfp-FXCckmJ1GKrKtdp_vB330Sh7hgErVX9KZjQEnis9-0ftk0ZUHgperHHOwKfCk8gMqFlYebkxldwqIQGr-STUhxOa9gu7Md__TI7Y0EH6H3-Za5Z2agorQ3GsuQoy0aPEWUQkP9gGckwzDDeMvJ10egZLTAZKIvYt2SU-xAnkeKoc3mB7UQSklsPb_ngYZan52Ybkhr615o7gHpxttuWdjBWUPUAc51A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ab59f856.mp4?token=vicVtPCdxnzV1qNj17hvfc3nGhP_LKcrTA0Pek62VRI6I2f-N2GUZNhhBaOX2QXhiwC-BnnVcik3eDw-wcINnvNwnMRmec6nMl-wE3kXuITR5dsd_2jlfp-FXCckmJ1GKrKtdp_vB330Sh7hgErVX9KZjQEnis9-0ftk0ZUHgperHHOwKfCk8gMqFlYebkxldwqIQGr-STUhxOa9gu7Md__TI7Y0EH6H3-Za5Z2agorQ3GsuQoy0aPEWUQkP9gGckwzDDeMvJ10egZLTAZKIvYt2SU-xAnkeKoc3mB7UQSklsPb_ngYZan52Ybkhr615o7gHpxttuWdjBWUPUAc51A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم برزیل به هائیتی توسط وینیسیوس ۳+۴۵
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/661280" target="_blank">📅 08:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661279">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beccc0a7db.mp4?token=CTmNNz65OiP326NpB766mNQuRJKtwT2KEeCT9hufABr1hb-XoTMF2jv2Qk-RZLpzWmapaoN__6wNwolOGyYpI6wA197jfqXQkuInzd5GCPGWHZTqwkqvR8xKfMiD6-31LuZRruIcVEUvskafNthAAs_8Lg5I99S8ix_hr3NNSQ3YH_13zTql4a35lCXYZ0Sjcw4iakLQ7TYMDuUqDWUIe3hGwmCkhGoY1sBwlCNElxoXmsBm6lJChiGERe_FZObzFEXhD2-SzS44c0UJH2Xw7svgLTeiwQpDCVS84idIW-sjk703UvU_whPglxolRrL8UoEP_STzwRFFgqAjRie1dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beccc0a7db.mp4?token=CTmNNz65OiP326NpB766mNQuRJKtwT2KEeCT9hufABr1hb-XoTMF2jv2Qk-RZLpzWmapaoN__6wNwolOGyYpI6wA197jfqXQkuInzd5GCPGWHZTqwkqvR8xKfMiD6-31LuZRruIcVEUvskafNthAAs_8Lg5I99S8ix_hr3NNSQ3YH_13zTql4a35lCXYZ0Sjcw4iakLQ7TYMDuUqDWUIe3hGwmCkhGoY1sBwlCNElxoXmsBm6lJChiGERe_FZObzFEXhD2-SzS44c0UJH2Xw7svgLTeiwQpDCVS84idIW-sjk703UvU_whPglxolRrL8UoEP_STzwRFFgqAjRie1dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم برزیل به هائیتی توسط کونیا ۳۶
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/661279" target="_blank">📅 08:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661278">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5qdSALyyfCkkbxnxCXYwwMUCkNNNggqtEqMOhcfk4BRD_MoFu5grAheusO8D4-T1Cov-bh2vKjwjhkYgwTn6RiMfGRH81ZmkeBfbc2uAXDFqMPVKdSP_d4poyL1YjakwzMExtTIqLaP3un_CxpT9DwfdiG3dqcbSNHU4_3l_tuao6K7cOj7rdf0PXCzw4iis6IjPNHUC0WfHpsx9EG3yhMBStyPayJTU5PoSxU7eFqn_meWsRO51_Ff9v98oeK2KoOe8sGAUBlELNJGegiitFqOM4g38OtuvAWx3j47o1bl_zHmO91Vi6VU_lojwqov3jW646Shd7F9l_nAiyuPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/661278" target="_blank">📅 08:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661275">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596213382c.mp4?token=dAzkjVT74o41g5YZ0Y_R7ehBDo9QvP_IZIqV5N5eJl-7sSlzf8LnOhzeXCseQiK4UOprYWQjURC1DR3F026OtVWW_HB3EN6UWbuJYAZgbP2eCUdAm5HeFJF3RqlmHBhEHjNqSSiLIGngRv8CREEmYTUJRk3VCwjTF9Gvpcuu3YSJVlc6ftLx02wKnCKJlmlXUhuWacemfb-Jrr5Zvz1acdNw7YFrTP7TIj2H3jkaxmn1kgkV2fopZVwKbWBp5B2suYr-mWb7X5Nd8YoZAUPeAJ3g81J5GDa92bfIOPwZyIUHFWuSpjo1wU1DLHTv5U2qixg7Iu927XjUpRKTlIDTtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596213382c.mp4?token=dAzkjVT74o41g5YZ0Y_R7ehBDo9QvP_IZIqV5N5eJl-7sSlzf8LnOhzeXCseQiK4UOprYWQjURC1DR3F026OtVWW_HB3EN6UWbuJYAZgbP2eCUdAm5HeFJF3RqlmHBhEHjNqSSiLIGngRv8CREEmYTUJRk3VCwjTF9Gvpcuu3YSJVlc6ftLx02wKnCKJlmlXUhuWacemfb-Jrr5Zvz1acdNw7YFrTP7TIj2H3jkaxmn1kgkV2fopZVwKbWBp5B2suYr-mWb7X5Nd8YoZAUPeAJ3g81J5GDa92bfIOPwZyIUHFWuSpjo1wU1DLHTv5U2qixg7Iu927XjUpRKTlIDTtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول برزیل به هائیتی توسط کونیا ۲۳
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/661275" target="_blank">📅 08:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661274">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76c44f88a.mp4?token=FPY4mkJJAXW60NnmvhJbpuPc6KIuJ39FO9NovfUyW71ogfS-lFlLFrYtXXp2R6sj00B8nq3qup-53u1z8Y30Bc7Magb1Jh2RU0XWT77G2SQvdoc4CjfWIWIZWm-tihdi3M_X2gbTBRY9A3UoG4hL_tAhNe94tzkLAW8Afj0vc4YjesZLzlYUjt-4VPe3f4JVEmJd8AxfoCH2dtu4S12i4sdnkWovI6ABC4N6gHPBDjoN9s-WIRwvhXyvDxTcpW1Ntg5EfECHyn8Mu4NX_gWfEuYScvLz-Uf82R_dzntipUCce08XCsxZ_MwADzRygewtU6kU_BZFsWILfdzA6_NWsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76c44f88a.mp4?token=FPY4mkJJAXW60NnmvhJbpuPc6KIuJ39FO9NovfUyW71ogfS-lFlLFrYtXXp2R6sj00B8nq3qup-53u1z8Y30Bc7Magb1Jh2RU0XWT77G2SQvdoc4CjfWIWIZWm-tihdi3M_X2gbTBRY9A3UoG4hL_tAhNe94tzkLAW8Afj0vc4YjesZLzlYUjt-4VPe3f4JVEmJd8AxfoCH2dtu4S12i4sdnkWovI6ABC4N6gHPBDjoN9s-WIRwvhXyvDxTcpW1Ntg5EfECHyn8Mu4NX_gWfEuYScvLz-Uf82R_dzntipUCce08XCsxZ_MwADzRygewtU6kU_BZFsWILfdzA6_NWsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حتی تماشا کردنش هم ترسناکه! ۴۷ متر سقوط در زاویه ۸۷ درجه با ترن هوایی در ایتالیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/661274" target="_blank">📅 08:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661271">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ونس: ترامپ درباره جزئیات نحوه پایان جنگ با ایران، با نتانیاهو اختلاف‌نظر دارد  جی‌ دی ونس، معاون ترامپ:
🔹
ترامپ در خصوص جزئیات دقیق نحوه پایان دادن به جنگ با ایران، اختلاف‌نظرهایی با نتانیاهو دارد.
🔹
رهبران آمریکا باید بسیار محتاط باشند و بر اساس منافع ما…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/661271" target="_blank">📅 07:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661270">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
آکسیوس: ویتکاف عازم سوئیس است؛ کوشنر هم‌اکنون در سوئیس است
🔹
انتظار می‌رود دور نخست مذاکرات آمریکا با ایران در آنجا برگزار شود.
🔹
هنوز مشخص نیست زمان جدیدی برای مذاکرات تعیین شده یا نه.
🔹
معلوم نیست ونس هم به سوئیس سفر کند یا نه.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/661270" target="_blank">📅 07:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661268">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
آکسیوس: ویتکاف عازم سوئیس است؛ کوشنر هم‌اکنون در سوئیس است
🔹
انتظار می‌رود دور نخست مذاکرات آمریکا با ایران در آنجا برگزار شود.
🔹
هنوز مشخص نیست زمان جدیدی برای مذاکرات تعیین شده یا نه.
🔹
معلوم نیست ونس هم به سوئیس سفر کند یا نه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/661268" target="_blank">📅 07:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661265">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESF6DUHxqBbQr4UF8Ftcxry8XoOLu_aegxnr8HVEnPc6JMsEDqhfYlk9gt5LsJvhSMaqaF4Z6XVNd_TzGxieU3YEdIDm0D84HONP0ZjepN2RNdQYa0g_7qvrhykocOhWJeja8uAZcSiEjfIykvmyGvqnQD2IF5TuYtUFbigsMKGrTkv-fsL67vYtr-NdLcIc1eZPXXCDDYnAmyT48BHmWTrYWS4py7cwet4_VH4q0a_51pTp65D8oPV8WF7Vz-lx2q2tbgVLj--KACtbveE7Kb9t3YT0DL7gyvw8smkNgZEX1KXUhnR4JoergV_Rfc5UghVHoNa8by_UbAQfXzUhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین حذف شده جام جهانی مشخص شد
🔹
پس از پایان دور دوم در
گروه C جام جهانی، هائیتی به عنوان اولین تیم از جام جهانی ۲۰۲۶ حذف شد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/661265" target="_blank">📅 07:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661264">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ونس: ترامپ درباره جزئیات نحوه پایان جنگ با ایران، با نتانیاهو اختلاف‌نظر دارد
جی‌ دی ونس، معاون ترامپ:
🔹
ترامپ در خصوص جزئیات دقیق نحوه پایان دادن به جنگ با ایران، اختلاف‌نظرهایی با نتانیاهو دارد.
🔹
رهبران آمریکا باید بسیار محتاط باشند و بر اساس منافع ما [ایالات متحده] عمل کنند، نه منافع هیچ کشور دیگری.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/661264" target="_blank">📅 07:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661263">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ae9133ed.mp4?token=NmvFxjev0gPnd-xbUbnvG9VTedxHjFPNdpzCN9Og5NeKi1v7yXHINUfMZD5xz9Ie_OupJapQ04hUW1l0imXEW6R5L8MA-1QZ3qaVy3xbWPFMUPyhwp7QuRjPhpYA6eYapNeeFlyXnkAHbBT8S9WGvLce7DO1WfOVrZTpdqK-q57-qWVAyf4cwX6Y8wrqyZi4fzlf2Sk2vnFyUmZP9By_yetTQQPqf-pheoFAa5oCT4pZWaXLpc0LZ1n6yOnnmLJOO2w7p-wPwBpqp_Cz81o-v2R9D9I56HjizklHGPNJCNVRHpL_D8PqvwjFxdigcaMeiKqfOvFK8cNTiOzz9shjJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ae9133ed.mp4?token=NmvFxjev0gPnd-xbUbnvG9VTedxHjFPNdpzCN9Og5NeKi1v7yXHINUfMZD5xz9Ie_OupJapQ04hUW1l0imXEW6R5L8MA-1QZ3qaVy3xbWPFMUPyhwp7QuRjPhpYA6eYapNeeFlyXnkAHbBT8S9WGvLce7DO1WfOVrZTpdqK-q57-qWVAyf4cwX6Y8wrqyZi4fzlf2Sk2vnFyUmZP9By_yetTQQPqf-pheoFAa5oCT4pZWaXLpc0LZ1n6yOnnmLJOO2w7p-wPwBpqp_Cz81o-v2R9D9I56HjizklHGPNJCNVRHpL_D8PqvwjFxdigcaMeiKqfOvFK8cNTiOzz9shjJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر لاریجانی: ما با چه استدلالی آتش‌بس را پذیرفتیم؟ در پیام اول مقام معظم رهبری گفته شد این تنگه باید حفظ شود تا برکات زیادی داشته باشد. ما از این تنگه غرامت را میگیریم ، نه این صندوق در هوای کسی هم نخواهد داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/661263" target="_blank">📅 07:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661262">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cb0c9a6.mp4?token=R_0cXOCw6hBzEHOrMrYpveBhzWZwoSgmLd7_s9A1tpjYjBfnIAvwhMthMmI4R64aLwixZv218Vy82AMFZJGzfFyuOF3lQXJ24YhP2Cth7NGISpwFkg1515pznmmq47FQBahgBzXyrZsqtvadbVXTXKLJXCtCzaI68SsnmREp_saGBZLBPwCN-41k4s40IZ0bE671zLFQBQTy7m9QnkPUQqYRUs2v1YOKnT4cRCqD2kpgbYca03rWCN-O3kFT8Nda4hU6sP-EAsmofJP2fHxBfDEHssw4h5z0dkePL1w8MzkfdAUQSwkJMGehInzL6tL2gqNGLL2UmrSqBUpZtWvkaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cb0c9a6.mp4?token=R_0cXOCw6hBzEHOrMrYpveBhzWZwoSgmLd7_s9A1tpjYjBfnIAvwhMthMmI4R64aLwixZv218Vy82AMFZJGzfFyuOF3lQXJ24YhP2Cth7NGISpwFkg1515pznmmq47FQBahgBzXyrZsqtvadbVXTXKLJXCtCzaI68SsnmREp_saGBZLBPwCN-41k4s40IZ0bE671zLFQBQTy7m9QnkPUQqYRUs2v1YOKnT4cRCqD2kpgbYca03rWCN-O3kFT8Nda4hU6sP-EAsmofJP2fHxBfDEHssw4h5z0dkePL1w8MzkfdAUQSwkJMGehInzL6tL2gqNGLL2UmrSqBUpZtWvkaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری خطاب به ترامپ: شما دنبال تسلیم بی‌قیدوشرط ایران بودید، تفاهم‌نامه که شبیه تسلیم ایران نیست
🔹
ترامپ:  در واقع، احتمالاً تسلیم بی‌قیدوشرط هست.
🔹
مجری:  واقعاً؟
🔹
ترامپ:  فکر می‌کنم همین‌طور باشد. ببینید، آن‌ها دیگر نیروی نظامی ندارند. شناورهایشان به قعر…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/661262" target="_blank">📅 07:33 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
